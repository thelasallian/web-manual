# TheLaSallian Web Manual

The Web section manual of **The LaSallian**, built with [Starlight](https://starlight.astro.build) and deployed automatically on every push to `main`.

## Live URLs

| Host | URL | Setup |
| --- | --- | --- |
| GitHub Pages | https://thelasallian.github.io/web-manual/ | Automatic via `.github/workflows/deploy.yml`. Enable once: repo **Settings → Pages → Source: GitHub Actions**. |
| Cloudflare Pages | https://web-manual.pages.dev (or custom domain) | Connect the repo in the Cloudflare dashboard: build command `npx astro build`, output dir `dist`, env var `SITE_BASE=/`. |

## Editing content

Everything lives in plain Markdown under [`src/content/docs/manual/`](src/content/docs/manual/):

- Large chapters (Website, Coverages, Web Specials) are split into sub-pages; each folder is a chapter, each `index.md` a section.
- Edit a file, commit to `main` (or open a PR), and the site redeploys automatically.
- Add images next to the pages in `manual/images/` and reference them relatively.

### Conventions

- Headings inside a page start at `##`.
- Internal links use relative paths, e.g. `(../bots/#pingloi)` or `(./articles/#311-uploading-articles-in-wordpress)`.
- Callouts use Starlight asides: `:::note[Title]` … `:::` / `:::caution[...]`.

## Local development

```sh
npm install
npm run dev      # dev server at localhost:4321/web-manual
npm run build    # production build into dist/
```

## Regenerating from the source document

`scripts/migrate.py` is a one-time converter from the original Google Docs export (`TLS Web Manual.md`, Pandoc-flavored Markdown with base64-embedded images). If the source doc ever gets re-exported:

```sh
python3 scripts/migrate.py   # re-extracts images + regenerates all pages
```

Warning: it overwrites everything under `src/content/docs/manual/` — hand edits made after migration will be lost. Prefer editing the generated files directly.
