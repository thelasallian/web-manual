import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// Base path is set by CI: GitHub Pages project sites need '/web-manual',
// Cloudflare Pages / custom domains use '/'.
const base = process.env.SITE_BASE ?? '/web-manual';

export default defineConfig({
	site: 'https://thelasallian.github.io',
	base,
	integrations: [
		starlight({
			title: 'TheLaSallian Web Manual',
			description: 'The LaSallian Web Section Manual',
			logo: {
				src: './src/assets/logo.png',
			},
			customCss: ['./src/style/custom.css'],
			sidebar: [
				{ label: 'Change Log', link: '/manual/change-log/' },
				{
					label: '1. About the Section',
					link: '/manual/about-the-section/',
				},
				{
					label: '2. Roles & Responsibilities',
					link: '/manual/roles-and-responsibilities/',
				},
				{
					label: '3. Website',
					items: [
						{ label: 'Overview', link: '/manual/website/' },
						{ label: '3.1. Articles', link: '/manual/website/articles/' },
						{ label: '3.2. Managing Users and Authors', link: '/manual/website/managing-users-and-authors/' },
						{ label: '3.3. Managing Tags', link: '/manual/website/managing-tags/' },
						{ label: '3.4. Managing the “Preview” Page', link: '/manual/website/managing-the-preview-page/' },
						{ label: '3.5. Managing the “About Us” Page', link: '/manual/website/managing-the-about-us-page/' },
						{ label: '3.6. Technical Information & Maintenance', link: '/manual/website/technical-information-and-general-maintenance/' },
						{ label: 'Appendix 3.a. Regular Section Tags', link: '/manual/website/appendix-3a-list-of-regular-section-tags/' },
					],
				},
				{
					label: '4. Social Media',
					link: '/manual/social-media/',
				},
				{ label: '5. Bots', link: '/manual/bots/' },
				{ label: '6. Newsroom', link: '/manual/newsroom/' },
				{ label: '7. Captions', link: '/manual/captions/' },
				{
					label: '8. Coverages',
					items: [
						{ label: 'Overview', link: '/manual/coverages/' },
						{ label: "8.1. Web's Role", link: '/manual/coverages/webs-role/' },
						{ label: '8.2. Types of Coverages', link: '/manual/coverages/types-of-coverages/' },
						{ label: '8.3. Volunteering (10-61)', link: '/manual/coverages/volunteering-10-61/' },
						{ label: '8.4. Backing Out of Coverages (10-22)', link: '/manual/coverages/backing-out-of-coverages-10-22/' },
						{ label: '8.5. Requirement Per Staffer', link: '/manual/coverages/requirement-per-staffer/' },
						{ label: '8.6. UAAP Sports Manual', link: '/manual/coverages/uaap-sports-manual/' },
					],
				},
				{ label: '9. Notion', link: '/manual/notion/' },
				{
					label: '10. Web Specials, Microsites, etc.',
					items: [
						{ label: 'Overview', link: '/manual/web-specials-microsites/' },
						{ label: '10.1. Types of Projects', link: '/manual/web-specials-microsites/types-of-projects/' },
						{ label: '10.2. Workflow', link: '/manual/web-specials-microsites/workflow/' },
						{ label: '10.3. Uploading the Website Files', link: '/manual/web-specials-microsites/uploading-the-website-files/' },
						{ label: '10.4. Creating a Subdomain', link: '/manual/web-specials-microsites/creating-a-subdomain/' },
						{ label: '10.5. The WordPress REST API', link: '/manual/web-specials-microsites/the-wordpress-rest-api/' },
						{ label: '10.6. Main Repositories', link: '/manual/web-specials-microsites/main-repositories/' },
					],
				},
			],
		}),
	],
});
