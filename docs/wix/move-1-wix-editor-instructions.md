# Moved

Use `docs/wix/COPY-INTO-WIX-DESIGNER.md`. Paste the files in `docs/wix/embed/`. Preview `docs/wix/site/index.html` in a browser first.

The steps below are the earlier text-only version. Follow the copy guide instead.

# Move 1 — Wix Editor instructions

Do this on the existing site. Do not publish until you have read the preview page in a browser and the new homepage on a Wix preview.

I cannot open your Wix account, so these steps are for you in the Editor. Paste text exactly. Do not add prices, downloads, sign-in, or a research form.

## Before you edit

1. Go to [Wix dashboard](https://manage.wix.com/) and open the site for `think-21.com`.
2. If the plan includes site duplication, duplicate the site first and edit the duplicate. If it does not, edit the live site but click **Save**, not **Publish**, until the preview looks right.
3. Confirm the editor is the classic Wix Editor. The public site loads classic Editor bundles, not Wix Studio. If Wix offers “Open in Studio”, decline that for this move.
4. Write down, for the audit file, and do not change them yet:
   - Site ID (Settings → Site settings, or the ID in the editor URL)
   - Premium plan name
   - Installed apps (look for Blog, Stores, Members, Forms)
   - Whether Dev Mode / Git integration is available
   - Whether any Members or Orders exist

## A. Fix the header

The live header shows the globe logo on top of the words “Future Certified” and the first menu items.

1. Click the header.
2. Select the logo image. Make it about 48–56 px tall and left-align it with padding from the left edge.
3. Select the text that says **Future Certified**. Change it to **Think21**.
   - Font: Spinnaker, if it is still in the site fonts. Otherwise Montserrat.
   - Color: `#0B1C4D`
   - Size: about 22 px
   - Place it to the right of the logo, not underneath it.
4. Select the menu. Place it to the right of the wordmark with a clear gap. On a 1280 px-wide preview, the logo, the word Think21, and all eight items must sit on one line without overlap.
5. Header background stays white. Do not add a second menu for Sign in or Cart.

Menu item text and links, in this order:

| Menu label | Link |
|---|---|
| Thinking | `/thinking` |
| BPM | `/bpm` |
| Startups | `/startups` |
| AI | `/ai` |
| ISO | `/iso` |
| Insights | `/blog` |
| Shop | `/shop` |
| About | `/team` |

Remove from the header menu: What We Do, Methods, Certify, The Team, Contact, Articles, and every ISO submenu. Those pages stay on the site. They are only removed from the menu.

Footer menu: Home, Insights (`/blog`), About (`/team`). Remove Certify and the ISO list from the footer.

Footer copyright line, replace the 2022 Future Certified line with:

```text
© 2026 Think21
```

Keep the phone `+972544872442` and `https://www.linkedin.com/in/yaakovpreiger/` until you choose a support email. Remove the company URLs `linkedin.com/company/Think21-experts/` and `linkedin.com/company/future-certified` from the header icons if both are showing. One personal LinkedIn link is enough.

## B. Site language and SEO

1. In the dashboard, set the site language to English if a control exists. The published page currently announces `lang="ru"`, and the skip link is Russian (“Перейти к основному контенту”) even though the copy is English.
2. Homepage SEO:
   - Page title: `Think21`
   - Description: `Thinking tools, BPM, startup methods, and responsible AI research from Yaakov Preiger. Browse freely. Products and research open only when they are approved.`

## C. Homepage `/`

Delete or hide the current sections (accelerator, investment platform, certification, consulting services, “Here’s what we provide”, Future Certified implementation, newsletter if you do not want a marketing list yet). Keep the header and footer.

Rebuild with normal Wix strips, not an HTML embed. The file `docs/wix/preview/homepage.html` is only a picture of the layout. Open it in a browser, then recreate the sections below.

Use the existing colors: navy `#0B1C4D`, teal button `#5AA4A4`, deep teal `#2B8580`, gold eyebrow `#D4D200`, off-white text `#F4F8F8` on the dark hero, body `#303030`. Buttons are square, uppercase, Montserrat.

### Hero (dark strip)

Eyebrow:

```text
Think21
```

Title:

```text
Tools for thinking, building, and deciding.
```

Paragraph:

```text
Practical material from Yaakov Preiger: thinking methods, BPM, startup definition, and responsible AI. Read what is published. Buy or download only what is actually listed. Research collection is not open.
```

Button label: `START WITH THINKING`  
Button link: `/thinking`

Second text link: `Read insights` → `/blog`

### Four area cards

Card title: `Thinking`  
Text:

```text
21 Prisms and the practical thinking material around it. Companion files appear here after they are packaged and approved. The book is listed only with a confirmed retailer link.
```

Link label: `Open Thinking` → `/thinking`

Card title: `BPM`  
Text:

```text
BPM-360 and production readiness. This area stays explanatory until an existing workbook is approved for download or sale.
```

Link label: `Open BPM` → `/bpm`

Card title: `Startups`  
Text:

```text
Idea validation and problem definition, including the question list already on this site. This is not an accelerator and not an investment screen.
```

Link label: `Open Startups` → `/startups`

Card title: `AI`  
Text:

```text
A place for AI tools, learning notes, and responsible AI research. No prompt pack is on sale yet. The study is not collecting responses.
```

Link label: `Open AI` → `/ai`

### Book strip

Heading:

```text
21 Prisms
```

Text:

```text
The book will be linked here when the retailer listing is confirmed. Buying the book from a retailer does not automatically unlock files on this site.
```

Do not add a Buy button.

### Research strip

Heading:

```text
Responsible AI research
```

Text:

```text
A study invitation will live under AI. Taking part will require its own consent. It will not require a purchase, and registering for the site will not be research consent. Nothing is open for participants yet.
```

Link label: `See the AI page` → `/ai`

### Insights strip

Heading:

```text
From the archive
```

Text:

```text
Essays already on the site. ISO articles remain essays. They are not an offer to certify a company.
```

Three text links:

- `Contradiction, TRIZ, and systemic thinking` → `/post/contradiction-the-core-of-triz-and-systemic-innovative-thinking`
- `TRIZ methods for systemic contradictions` → `/post/triz-methods-for-resolving-systemic-contradictions`
- `Five whys in architectural assessment` → `/post/five-whys-the-power-of-rca-in-architectural-assessment-and-pfmea`

### Contact strip

Heading:

```text
About
```

Text:

```text
Yaakov Preiger. Architecture, systematic inventive thinking, and TRIZ, applied to products and operating decisions.
```

Links:

- `About` → `/team`
- `LinkedIn` → `https://www.linkedin.com/in/yaakovpreiger/`
- Phone text: `+972544872442`

Remove the “Register for invest-platform” and “GET STARTED” buttons that lead into consulting pages.

## D. New pages

For each new page: Add Page → Blank page → set the URL slug exactly → hide it from the automatic menu if Wix adds it twice → paste one heading and the paragraphs. Add the same header and footer as the home page.

### `/thinking`

SEO title: `Thinking | Think21`

```text
Thinking

21 Prisms is the thinking framework for this area. The page will list the book, a companion workbook, and shorter tools when each one is approved.

Nothing here is a free download yet. A public preview will be a separate file from the full workbook.

Related reading is in Insights, including the TRIZ notes already published on this site.
```

Link: `Read the TRIZ notes` → `/post/contradiction-the-core-of-triz-and-systemic-innovative-thinking`

### `/bpm`

SEO title: `BPM | Think21`

```text
BPM

This area is for BPM-360 and production-readiness material drawn from existing work. A workbook will be listed when the package, license, and price are approved.

There is no consulting engagement for sale on this page.
```

### `/ai`

SEO title: `AI | Think21`

```text
AI

Three separate blocks will live here.

Products. Prompt and learning files stay unpublished until packaging, license, and claims are approved. These notes are not a certification and not a guarantee about model safety.

Responsible AI research. The public explanation will be posted here when the study title, consent, and eligibility are approved. The questionnaire is not on this site yet. Please do not send study answers by email or through the contact form.

Insights. Essays and exercises can be linked here after editorial review.
```

### `/iso`

SEO title: `ISO | Think21`

```text
ISO

Quality, environmental, safety, and information-security work is handled separately by VP Quality. Think21 does not sell certifications, and a Think21 account will not be a VP Quality account.

vp-quality.com is not open yet. This page will link there when that site is live.
```

Do not add a button to vp-quality.com while it only says Coming Soon.

### `/shop`

SEO title: `Shop | Think21`

```text
Shop

Approved tools will be listed here and on their area pages from the same catalog. There are no products, prices, or files for sale yet.

You can still read Insights and the area pages.
```

Link: `Read insights` → `/blog`

If Wix Stores is not installed, do not install it in this move. A text page is the correct empty state.

## E. Rewrite `/startups` in place

Keep the URL. Replace the screening and mentoring offer with:

SEO title: `Startups | Think21`

```text
Startups

This area collects idea-validation and problem-definition material. It is not an accelerator, a fund, or a screening process.

Start with the question list already published: the problem, the market, the team, and the next twelve months. A packaged tool will be added only after it is approved.

There is no registration for an investment platform.
```

Link: `Open the question list` → `/idea-validation`

On `/idea-validation`, leave the questions. Delete any button that says register, invest, or get certified.

## F. About page for now

On `/team`, change the H1 from `ABOUT US` to `About`. Keep the first-person bio. Delete any sentence that offers to design a client’s system as a service menu. You can keep the description of architecture, S.I.T., and TRIZ experience.

Suggested replacement for the opening, if you want it in this pass:

```text
I’m Yaakov Preiger. I work on architecture and systematic thinking, including S.I.T. and TRIZ, and I publish the tools and notes collected on Think21.

This site is my own material. It is not a consulting catalog and not an employer’s service list.
```

## G. Check before publish

Desktop and phone preview:

- Header items do not overlap.
- Home no longer says Future Certified, accelerator, investment platform, or certification.
- Thinking, BPM, AI, ISO, and Shop open and do not show a price.
- Startups does not ask anyone to register for screening.
- Insights still opens the existing blog.
- Old URLs such as `/iso-9001` still open if typed. They are simply absent from the menu.
- Contact form, if you leave it, is not on the new ISO or AI research sections. Do not label it as a way to join the study.

When that preview is right, publish once. Send the preview link if you want a second pass before that.

## Explicitly later

- Google and LinkedIn sign-in, My Library, private files
- Wix Stores, payment provider, taxes
- One real product, after you approve the file, license, and price
- Research instrument, consent, dictation, and PDF service
- Redirects from old ISO and consulting URLs
- A Think21 logo, if you want to retire the globe mark
