# Wix Stores, sign-in, and the research mailbox

Do this in the same Editor session as the page paste. Products stay hidden. No price is public.

Mailbox for both notices: `yaakov.preiger@think-21.com`

## Shop: use Wix Stores, not a fake cart

The embed on the Shop page is only the introduction and the product list. The gallery and checkout are the Wix Stores app.

1. In the Editor, open the App Market and add **Wix Stores**. If it is already installed, skip this.
2. Open **Shop** in the Editor. Keep the embed from `docs/wix/embed/shop.html` at the top.
3. Click **Add Elements** → **Store** → **Product Gallery**. Place it under the embed, full width.
4. Leave the gallery on the default “all products” source. Hidden products will not show, so the gallery can look empty. That is the correct public state.
5. In the dashboard, open **Settings → Store products & inventory** or the store currency setting. Choose the currency you will actually charge. Do not publish a price yet.

### Create each product as hidden

Dashboard → **Store Products** → **New Product**. For every row:

- Type: **Digital**
- Visible: **Hidden** (wording may be “Not visible on your site”)
- Price: if Wix requires a number, enter `1` in your currency and keep the product hidden. Do not turn on a Buy button on the public pages. Replace that number before you ever unhide the product.
- Do not upload the manuscript. If a digital product demands a file, upload a plain text file whose only line is `Not released.`
- Ribbon, subscription, and tax: leave them off
- Inventory: do not track quantity

| Product name | SKU | Area page to link in the description |
|---|---|---|
| BPM-360 handbook | T21-BPM-HANDBOOK | `/bpm` |
| Production Readiness workbook | T21-BPM-PRF | `/bpm` |
| BPM-360 method cards | T21-BPM-CARDS | `/bpm` |
| 21 Prisms companion workbook | T21-PRISMS-WB | `/thinking` |
| Reflection and decision journal | T21-PRISMS-JOURNAL | `/thinking` |
| 21 Prisms card set | T21-PRISMS-CARDS | `/thinking` |
| 21 Prisms team toolkit | T21-PRISMS-TEAM | `/thinking` |
| Master Prompt Architect, Basic | T21-MPA-BASIC | `/ai` |
| Master Prompt Architect, Pro | T21-MPA-PRO | `/ai` |
| Master Prompt Architect, Enterprise | T21-MPA-ENT | `/ai` |
| Seven-day AI learning practice | T21-AI-7DAY | `/ai` |

Paste this into the BPM-360 handbook description:

```text
Adaptive business-process management for conditions that keep changing. Ten aspects, from strategy through governance, and a production-readiness review before go-live. Manuscript only. This product is hidden until the file, the license, and the price are approved. It is not a consulting engagement.
```

Paste this into the Production Readiness workbook description:

```text
A go-live gate for people, process, and technology. The question list stays in the workbook file. That file is not attached yet.
```

Paste this into each Master Prompt Architect description, and change the tier name:

```text
A fill-in prompt template from the Master Prompt Architect drafts. Basic, Pro, and Enterprise are tiers of one family. This page does not claim the prompts are injection-proof, hallucination-free, or certified. Hidden until the file and the license are approved.
```

Do not create a Wix product for the 21 Prisms book. It will be an external retailer link when that URL is confirmed. Do not create a product for the startup questions or for the research page.

## Sign-in: Google now, LinkedIn when the app exists

Wix can show **Continue with Google** today. That covers Gmail and any other Google account. Wix does not include a real LinkedIn login button. Do not label a normal email form as LinkedIn login.

### Google

1. **Add Elements** → **Members** → **Member Login Bar**. Put it in the header, on the right, clear of the menu.
2. Click the bar → **Set up** or **Settings**.
3. Turn **Google** on.
4. If you see a switch for email-and-password signup, turn it off. If the switch is not there, leave it and we will block password-only accounts before any free file is added. There is no free file yet.
5. New members should not be added to a public directory or a newsletter by default.

### Email you when someone registers

1. Dashboard → **Automations** → **New Automation**.
2. Trigger: **Member registers** (if you do not see it, use **Contact created** and limit it to site members).
3. Action: **Send an email**.
4. To: `yaakov.preiger@think-21.com`
5. Subject: `New Think21 registration`
6. Body, with the automation’s name and email fields inserted:

```text
A new member registered on think-21.com.

Name: 
Email: 

This notice is registration only. It is not research consent and not a purchase.
```

7. Turn the automation on. Register a test Google account that is not your admin login, confirm the mail arrives, then you can remove that test member.

### LinkedIn

A working LinkedIn button needs a LinkedIn developer app with Sign In using OpenID Connect, then a small backend bridge. That bridge is not something to paste into an HTML embed.

Until the app exists:

1. Do not add a header button that says it logs people in with LinkedIn.
2. Optional, on the About page only: a Wix form titled **Request LinkedIn sign-in**. Fields: name, email, LinkedIn profile URL. Email the submission to `yaakov.preiger@think-21.com`. The success text must say: “This is a request. It does not sign you in.”

When you have created the LinkedIn app, send the client id and the exact callback URL you registered. The login bridge gets built against those, not guessed.

## Research form

On the new **Research** page, under the embed from `docs/wix/embed/research.html`:

1. **Add Elements** → **Contact** → **Contact Form** (or **Get in touch**).
2. Delete extra fields. Add the fields in `docs/wix/embed/research.html`, in that order. Both checkboxes start unchecked. The draft-study checkbox is required.
3. Form settings → **Email notifications** → send to `yaakov.preiger@think-21.com`.
4. Turn off “subscribe to the mailing list” and any marketing automation on this form.
5. Success message: `Received. This draft is not a study submission.`
6. Submit the form yourself once and confirm the mail arrives at `yaakov.preiger@think-21.com`.

The same inbox receives new members and draft research submissions. They are different events. Do not send research answers to a sales or newsletter list.
