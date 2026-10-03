# Public site audit — 28 September 2026

Scope: what a visitor can see at https://www.think-21.com/ and what is in https://github.com/ypreiger/think-21. Dashboard-only facts (site ID, plan, members, orders, installed apps, Git integration) were not available.

## Repository

`ypreiger/think-21` on `main` contains `.gitignore` and `docs/Think21_End_to_End_Design_v1.0.md` plus the docx twin. There is no Wix site code and no Git integration connection. The local `think-21` folder is not a git clone.

## Platform

- Wix, confirmed by the `generator` meta tag and `static.parastorage.com` / `static.wixstatic.com`.
- Classic Editor, not Studio: page scripts are `rb_wixui.thunderbolt_bootstrap-classic` and classic section bundles.
- Blog is installed. Sitemaps are pages, blog posts, and blog categories. No product, booking, or member URLs appear.
- `robots.txt` is the Wix default. Sitemap lastmod for pages is 2025-03-30. Newest blog edit in the sitemap is 2025-04-19.
- Published `lang` is `ru` while the copy is English. The skip link is Russian.

## Visual baseline

Tokens are in `docs/wix/design-tokens.json`.

- Header is white. Logo is a circular globe (`logo.png`). On a desktop render the logo and the truncated words “Future Certi” sit on top of “What We Do”.
- Hero is a near-black image with a blue-green glow. Eyebrow “Future Certified” is gold `#D4D200`. The main line is off-white Spinnaker, about 50 px.
- Buttons are square teal `#5AA4A4`, uppercase.
- Headings use Spinnaker. Body uses Montserrat, with Futura LT Book on some paragraphs.
- Footer: ©2022 by Future Certified. Phone +972544872442. LinkedIn company Think21-experts, plus personal and Future Certified company links in the header.

## Information architecture

Primary menu: What We Do, Methods, Certify, The Team, Contact, Articles.

Defects:

- ESG → `/iso-9001`, whose title is ESG, not ISO 9001.
- ISO 9001 → `/copy-of-iso-9001`, whose title is ISO 14001 and whose text matches `/iso-14001`.
- The Team → `/partners`. `/team` is a different page.
- Contact → `/`.

Page-by-page actions are in `docs/wix/page-migration-map.md`.

## Fit to design v1.0

The live site is a Future Certified consulting, accelerator, investment, and certification offer. Version 1 of the design is a personal Think21 catalog: Thinking, BPM, Startups, AI, a separate ISO referral, Insights, and Shop. Research and checkout are specified later and are not on the public site.

`vp-quality.com` responds with Coming Soon, so an ISO button must not be added until that site is actually open.

## Acceptance for this audit slice

A page-migration map and a design-token file now exist as proposals. They are not an owner-approved production change. Member IDs and orders were not inspected and must not be recreated.
