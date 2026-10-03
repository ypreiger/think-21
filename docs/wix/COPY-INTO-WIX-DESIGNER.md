# Copy this into the Wix Editor

I cannot open your Wix account. You paste the files. Do not publish until the last checklist.

Two folders:

| Folder | What it is | Do this with it |
|---|---|---|
| `docs/wix/site/` | Preview you can open in a browser, including the header | Double-click `index.html` and click around. Do not paste these files into Wix. |
| `docs/wix/embed/` | The code for each page, with the CSS already inside | Paste the **source** of these files into Embed HTML. |

Copy the source, not the picture. If you open an embed file in a browser and copy the visible words, the colors and layout are lost. In Cursor, open the file, press Command-A, then Command-C.

Each embed file starts with a comment that names the desktop height and the mobile height. That comment is for you. It does not show on the site.

## Before you change the live site

1. Go to [manage.wix.com](https://manage.wix.com/) and open the Editor for think-21.com. This site uses the classic Wix Editor, not Wix Studio. If a button offers Studio, stay in the Editor you have.
2. If your plan can duplicate a site, duplicate it and edit the copy. Otherwise edit this site and use **Save**. Leave **Publish** until the end.
3. The left rail uses **Pages & Menu** and **Add Elements** (the plus).

## 1. Create the new pages

Click **Pages & Menu**. For each new page, click **Add Page**, choose a blank page, and name it. Then set the URL:

1. Click the **More Actions** icon next to that page.
2. Click **SEO Basics**.
3. Set **URL slug** to the value in the table. Press Enter.

| Page name in the panel | URL slug | Embed file to paste later |
|---|---|---|
| Thinking | `thinking` | `docs/wix/embed/thinking.html` |
| BPM | `bpm` | `docs/wix/embed/bpm.html` |
| AI | `ai` | `docs/wix/embed/ai.html` |
| Research | `research` | `docs/wix/embed/research.html` |
| ISO | `iso` | `docs/wix/embed/iso.html` |
| Shop | `shop` | `docs/wix/embed/shop.html` |

Do not create a second Home, Startups, Blog, or Team page. Those URLs already exist. You will replace what is on them.

Rename the existing Team page to **About**. Open its SEO Basics and make sure the slug is still `team`. If Wix changed it to `about`, set it back to `team`.

## 2. Header and menu

On the canvas, click the header.

1. Select the globe logo. Drag it to the left. Drag a corner until it is about 48 px tall. It must not cover the menu.
2. Double-click the words **Future Certified** and replace them with `Think21`. Color `#0B1C4D`. Font Spinnaker if it is in the font list, otherwise Montserrat. About 22 px.
3. Drag the menu to the right of that word so the logo, the word, and the menu sit on one line.

Open the menu (click it and choose **Manage Menu**, or use **Pages & Menu**). Remove these items from the menu only. Do not delete the pages:

What We Do, Methods, Certify and every ISO item under it, The Team, Contact, Articles.

Add items in this order. Drag them if Wix drops them somewhere else.

| Menu label | Points to |
|---|---|
| Thinking | page Thinking |
| BPM | page BPM |
| Startups | page Startups |
| AI | page AI |
| ISO | page ISO |
| Insights | the existing blog page (`/blog`) |
| Shop | page Shop |
| About | the page whose address is `/team` |

For Insights, add the existing blog page and rename that menu label to Insights. Leave the address as `/blog`.

Do not put Research in the top menu. The AI page links to it. Sign-in is the Wix member bar from `docs/wix/WIX-STORES-AND-SIGN-IN.md`, not a menu item. There is no Cart item until a product is visible.

## 3. Footer

If the footer has its own menu, set it to Home, Insights, About. If it shares the header menu, it will already have changed.

Double-click the copyright line and replace it with:

```text
© 2026 Think21
```

Keep the phone `+972544872442` and one link to `https://www.linkedin.com/in/yaakovpreiger/`. Remove extra LinkedIn company icons from the header if two or three are showing.

## 4. Paste a page

Repeat this for every row in the table below.

1. Open that page on the canvas.
2. Delete the old sections under the header. Click a section, press Delete, and continue until the header and footer are the only pieces left. This removes the accelerator, investment, certification, and contact-form blocks on Home.
3. If Wix left a big page title such as THINKING, delete that text too. The pasted page has its own title.
4. Click **Add Elements** → **Embed Code** → **Popular Embeds** → **Embed HTML**.
5. Click **Enter Code**.
6. Open the embed file in Cursor, select all, copy, and paste into **Add your code here**. Click **Update**.
7. Click the embed. Turn on **Stretch to full width** if that control is there, and set the side margins to 0. If there is no Stretch control, drag the side handles out to the edges of the page.
8. Drag the bottom handle to the desktop height in the table. A little extra white is fine. An inner scrollbar means the box is too short, so drag it further down.
9. Click the phone icon at the top of the Editor to open the mobile view. Select the same embed and set the mobile height. Then switch back to desktop.

Use **Embed HTML**. Do not use **Embed a Site**.

| Page on the canvas | File | Desktop height | Mobile height |
|---|---|---|---|
| Home | `docs/wix/embed/home.html` | 2550 px | 4200 px |
| Thinking | `docs/wix/embed/thinking.html` | 2000 px | 3500 px |
| BPM | `docs/wix/embed/bpm.html` | 2550 px | 4000 px |
| Startups | `docs/wix/embed/startups.html` | 1400 px | 2300 px |
| Idea Validation | `docs/wix/embed/idea-validation.html` | 5700 px | 8700 px |
| AI | `docs/wix/embed/ai.html` | 1950 px | 3200 px |
| Research | `docs/wix/embed/research.html` | 1100 px | 1900 px |
| ISO | `docs/wix/embed/iso.html` | 500 px | 700 px |
| Shop | `docs/wix/embed/shop.html` | 1250 px | 2100 px |
| About (`/team`) | `docs/wix/embed/about.html` | 850 px | 1400 px |

On Shop, add the Wix Product Gallery under the embed, as described in `docs/wix/WIX-STORES-AND-SIGN-IN.md`. On Research, do not add a Wix form. The embed already opens the questionnaire in a new tab.

Leave `/blog` as the Wix blog. Do not paste HTML over it.

The shared stylesheet, if you want to read it, is `docs/wix/site/css/think21.css`. You do not paste that file by itself. It is already inside every embed file.

## 5. Search titles

For each page: **Pages & Menu** → **More Actions** → **SEO Basics**.

| Page | Title tag | Meta description |
|---|---|---|
| Home | Think21 | BPM-360, 21 Prisms, prompt drafts, and the startup questions already on this site. |
| Thinking | Thinking \| Think21 | 21 Prisms of Thinking: three stages, twenty-one prisms, and the files that are not packaged yet. |
| BPM | BPM \| Think21 | BPM-360 handbook, ten aspects, and the production-readiness gate. |
| Startups | Startups \| Think21 | The idea-validation questions already published on Think21. |
| Idea Validation | Idea validation \| Think21 | The existing Think21 question list for testing an idea. |
| AI | AI \| Think21 | Master Prompt Architect drafts, a seven-day practice, and the research page. |
| Research | Research \| Think21 | Responsible AI research page. The approved questionnaire is not open. |
| ISO | ISO \| Think21 | ISO work is separate from the Think21 catalog. |
| Shop | Shop \| Think21 | Hidden Wix Stores products for BPM-360, 21 Prisms, and the prompt drafts. |
| About | About \| Think21 | Yaakov Preiger. BPM-360, 21 Prisms, and the Think21 drafts. |

In the site dashboard, set the site language to English if you can find Language. The published page currently announces Russian while the words are English.

## 6. Check, then publish

Preview desktop and mobile.

- The header logo, Think21, and the eight menu items do not overlap.
- Home no longer says Future Certified, accelerator, investment platform, or certification.
- Thinking, BPM, AI, Research, ISO, and Shop open, and none of them shows a public price.
- BPM names the ten aspects. AI names Basic, Pro, and Enterprise and links to Research.
- Startups opens the existing question list.
- Insights opens the existing blog.
- About is the old `/team` address with the new text.
- Typing `/iso-9001` still opens the old page. It is simply absent from the menu.
- ISO does not link to vp-quality.com.

Then click **Publish** once.

## Shop, Google sign-in, and the research mailbox

Follow `docs/wix/WIX-STORES-AND-SIGN-IN.md` after the pages are pasted.

Create the Wix Stores products as hidden. Turn on Google sign-in. Send new registrations to `yaakov.preiger@think-21.com`. The research page opens the questionnaire in a new tab. Do not add a LinkedIn button that pretends to log someone in. Do not link to vp-quality.com. Do not upload the manuscripts as public downloads.
