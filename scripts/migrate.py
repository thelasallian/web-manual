#!/usr/bin/env python3
"""One-time migration: converts the Google Docs export of the TLS Web Manual
into clean, split Starlight content. Re-run only if the source doc changes."""

import base64
import posixpath
import re
from pathlib import Path

SRC = Path("/Users/jabinguamos/Documents/School/TLS/webman/TLS Web Manual.md")
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "src" / "content" / "docs" / "manual"
IMAGES = DOCS / "images"

ESCAPABLE = r"[-_.*+#~!`()\[\]{}<>|\\&$]"

CHAPTERS = {
    "Change Log": ("change-log", "Change Log"),
    "1. About the Section": ("about-the-section", "About the Section"),
    "2. Roles & Responsibilities": ("roles-and-responsibilities", "Roles & Responsibilities"),
    "3. Website": ("website", "Website"),
    "4. Social Media": ("social-media", "Social Media"),
    "5. Bots": ("bots", "Bots"),
    "6. Newsroom": ("newsroom", "Newsroom"),
    "7. Captions": ("captions", "Captions"),
    "8. Coverages": ("coverages", "Coverages"),
    "9. Notion": ("notion", "Notion"),
    "10. Web Specials, Microsites, etc.": ("web-specials-microsites", "Web Specials, Microsites, etc."),
}

# Chapters large enough to be split into one sub-page per level-2 section.
SPLIT_H2 = {"3. Website", "8. Coverages", "10. Web Specials, Microsites, etc."}

# Heading text -> admonition inserted directly below the heading.
LEGACY_NOTES = {
    "3.6. Technical Information and General Maintenance": (
        ":::caution[Legacy - cPanel has been retired]\n"
        "TLS no longer uses a cPanel server. The sections below are kept for "
        "historical reference only. The website and web specials are now "
        "deployed through Git-based hosting.\n"
        ":::"
    ),
    "10.3. Uploading the Website Files": (
        ":::caution[Legacy - cPanel has been retired]\n"
        "The cPanel upload methods below are obsolete and kept for historical "
        "reference only.\n"
        ":::"
    ),
    "10.4. Creating a Subdomain": (
        ":::caution[Legacy - cPanel has been retired]\n"
        "Subdomains are no longer provisioned through cPanel.\n"
        ":::"
    ),
}


def github_slug(text: str) -> str:
    """Mirrors github-slugger/rehype-slug so rewritten anchors match rendered ids."""
    text = re.sub(r"[*_`]", "", text).strip().lower()
    kept = []
    for ch in text:
        if ch.isalnum() or ch in " -_":
            kept.append(ch)
    return re.sub(r"\s+", "-", "".join(kept).strip())


def unescape(text: str) -> str:
    parts = re.split(r"(`[^`]*`)", text)
    return "".join(
        p if p.startswith("`")
        else re.sub(re.escape("\\") + ESCAPABLE, lambda m: m.group(0)[1], p)
        for p in parts
    )


def clean_heading(text: str) -> tuple[str, str | None]:
    anchor = None
    m = re.search(r"\s*\{#([^}]+)\}\s*$", text)
    if m:
        anchor = m.group(1)
        text = text[: m.start()]
    text = re.sub(r"\*{1,2}", "", unescape(text))
    return re.sub(r"\s+", " ", text).strip(), anchor


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")

    # Extract base64 image definitions into files.
    IMAGES.mkdir(parents=True, exist_ok=True)
    ext_by_ref = {}
    for ref, ext, data in re.findall(
        r"^\[(image\d+)\]: <data:image/(png|jpeg|jpg);base64,([^>]+)>",
        raw,
        re.MULTILINE,
    ):
        (IMAGES / f"{ref}.{ext}").write_bytes(base64.b64decode(data))
        ext_by_ref[ref] = ext
    print(f"extracted {len(ext_by_ref)} images")

    raw = re.sub(r"^\[image\d+\]: <data:image/[^>]+>\n?", "", raw, flags=re.MULTILINE)
    # Placeholder is resolved to a page-relative path at write time.
    raw = re.sub(r"!\[\]\[(image\d+)\]", r"![image](IMGREF:\1)", raw)

    # Split into chapters on top-level bold headings; fence-aware so `#`
    # comments inside code blocks never trigger a split.
    chapters: list[tuple[str | None, list[str]]] = []
    in_fence = False
    for line in raw.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            if chapters:
                chapters[-1][1].append(line)
            continue
        if not in_fence and re.match(r"^#[ \t]+\*\*", line):
            title, _ = clean_heading(line[2:])
            chapters.append((title, [line]))
            continue
        if chapters:
            chapters[-1][1].append(line)

    # Clean each chapter body; build the global pandoc-anchor map.
    # Split chapters get one sub-page per h2; everything else stays whole.
    anchor_map: dict[str, tuple[str, str]] = {}  # pandoc -> (page_path, heading_slug)
    pages: dict[str, dict] = {}  # page_path -> {"title": str, "lines": [str]}
    is_first_line = True
    for chapter_title, lines in chapters:
        page_slug, label = CHAPTERS[chapter_title]
        split = chapter_title in SPLIT_H2
        current = page_slug
        pages[current] = {"title": label, "lines": []}
        is_first_line = True
        for line in lines:
            hm = re.match(r"^(#{1,6})\s*(.*)$", line)
            if hm and is_first_line and hm.group(1) == "#":
                _, anchor = clean_heading(hm.group(2))
                if anchor:  # links to a chapter title go to the page root
                    anchor_map[anchor] = (page_slug, "")
                is_first_line = False
                continue  # chapter h1 becomes frontmatter title
            is_first_line = False
            if hm:
                text, anchor = clean_heading(hm.group(2))
                if not text:
                    continue  # stray empty heading from the export
                slug = github_slug(text)
                if hm.group(1) == "##" and split:
                    section_slug = github_slug(re.sub(r"^[\d.]+\s*", "", text))
                    current = f"{page_slug}/{section_slug}"
                    pages[current] = {"title": text, "lines": []}
                    if anchor:  # links to the section title go to the page root
                        anchor_map[anchor] = (current, "")
                    note = LEGACY_NOTES.get(text)
                    if note:
                        pages[current]["lines"].extend(note.splitlines())
                    continue  # h2 becomes the sub-page's frontmatter title
                if anchor:
                    anchor_map[anchor] = (current, slug)
                pages[current]["lines"].append(f"{hm.group(1)} {text}")
                note = LEGACY_NOTES.get(text)
                if note:
                    pages[current]["lines"].extend([""] + note.splitlines())
                continue
            # Google Docs indents paragraphs with tabs, which markdown would
            # render as code blocks; strip leading tabs but keep list spaces.
            line = re.sub(r"^\t+", "", line)
            line = re.sub(r"^─+\s*$", "", unescape(line))
            pages[current]["lines"].append(line)

    def rewrite_for(page: str) -> callable:
        def rewrite(m: re.Match) -> str:
            target = anchor_map.get(m.group(1).lstrip("#"))
            if not target:
                return m.group(0)
            t_page, t_slug = target
            rel = posixpath.relpath(f"/{t_page}", f"/{page}")
            return f"({rel}#{t_slug})" if t_slug else f"({rel}/)"

        return rewrite

    for path, meta in pages.items():
        depth = path.count("/")
        img_prefix = ("./" if depth == 0 else "../" * (depth + 1)) + "images"
        body = "\n".join(meta["lines"])
        body = re.sub(r"\((#[^)\s]+)\)", rewrite_for(path), body).strip() + "\n"
        body = re.sub(
            r"IMGREF:(image\d+)",
            lambda m: f"{img_prefix}/{m.group(1)}.{ext_by_ref[m.group(1)]}",
            body,
        )
        if not body.strip():
            children = sorted(
                p for p in pages
                if p.startswith(f"{path}/") and len(p.split("/")) == 2
            )
            items = "\n".join(f"- [{pages[c]['title']}](./{c.split('/')[1]}/)" for c in children)
            body = f"This section covers:\n\n{items}\n" if children else \
                "> This section has no additional content.\n"
        front = f'---\ntitle: "{meta["title"]}"\n---\n\n'
        out_dir = DOCS / path if "/" in path else DOCS
        out_dir.mkdir(parents=True, exist_ok=True)
        name = "index.md" if "/" in path else f"{path}.md"
        (out_dir / name).write_text(front + body, encoding="utf-8")

    print(f"wrote {len(pages)} pages")


if __name__ == "__main__":
    main()
