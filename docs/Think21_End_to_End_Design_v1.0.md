# Think21 Digital Platform
## End-to-End Design and Implementation Specification

**Version:** 1.0  
**Date:** 28 September 2026  
**Owner:** Yaakov Preiger  
**Primary domain:** https://www.think-21.com/  
**Implementation target:** Existing Wix site, extended with Velo and a small processing service  
**Delivery audience:** Site owner, developer, Cursor or another coding assistant

## 1. Design decisions

| Decision | Implementation baseline |
|---|---|
| Preserve Wix | Extend the existing site. Do not replace it with a standalone application or migrate editors without approval. |
| One catalog, multiple areas | Thinking, BPM, Startups and AI each have their own landing page and relevant products. The general Shop aggregates the same catalog. |
| Separate ISO business | ISO is a referral area linking to VP Quality at `vp-quality.com`. Its future checkout, customer records and consulting remain separate. |
| Registration gate | Google or LinkedIn registration is required to obtain free workbooks, access purchased assets and participate in research. Browsing remains public. |
| Configurable access | The owner defines each asset as free to registered members, included with specified purchases, or separately paid. |
| Academic questionnaire | Located under AI / Responsible AI Research. Registration does not constitute research consent or marketing consent. |
| Text and voice | Each eligible narrative answer can be typed or dictated. Speech is transcribed into editable text; the participant approves the text. |
| PDF and records | Final submission stores structured answers and generates one PDF containing the completed questionnaire. Participants can download it and request an emailed copy. |
| Storage | Wix CMS is the primary structured-response store. PDFs use private Wix Media files. Google Drive is an optional administrator archive, not a second editable master. |
| Future integrations | Q-Hub can replace the research implementation through a versioned adapter. The Revenue Agent can consume approved product data, never research responses. |

**Scope boundary:** This is a personal Think21 platform. Employer/client material, a consulting-first business, a multi-vendor marketplace, and a public research-data repository are outside version 1.

**Implementation rule:** Requirements marked MUST are launch requirements. Proposed configuration defaults are identified explicitly. Provider permissions, payments, research approval and production access must be supplied through owner-controlled accounts.

### 1.1 Reading map

Sections 2-5 define the site and product experience. Sections 6-10 specify identity, permissions, commerce and research. Sections 11-15 define storage, interfaces, administration and security. Sections 16-19 cover implementation, testing, release decisions and sources.

## 2. Existing-site reuse and deployment boundary

### 2.1 Existing-site audit: first implementation task

Preserve the current domain and recover the current Wix site's design tokens from its editor before changing layouts. Do not infer its fonts, colors, installed apps, subscriptions or page structure from this specification.

| Audit item | Required output |
|---|---|
| Site and editor | Site ID, current editor type, published revision, plan, enabled developer features and installed apps. |
| Visual baseline | Desktop/mobile screenshots; logo source; fonts; color tokens; header, footer, buttons and spacing. |
| Information architecture | Existing URLs, page titles, navigation, forms, products, redirects and content to retain. |
| Existing data | Members, orders, CMS collections and integrations requiring preservation. No production personal data in development fixtures. |
| Development connection | Git integration eligibility, package compatibility and a separate test site or safe preview workflow. |
| Owner decisions | Retain, revise, merge, redirect or retire each current page. Approve revised homepage before rollout. |

**Acceptance:** An approved page-migration map and design-token file exist before production content changes. Existing member IDs and order history must not be recreated or discarded.

### 2.2 Delivery boundary

Use Wix for pages, responsive layout, commerce, membership and content administration. Use custom Velo backend modules for authorization, entitlements and research records. Use one containerized processing service for speech transcription, PDF rendering and optional PDF attachments/Drive exports. Do not run Chromium or long-running transcription inside a Wix page request.

Git Integration & Wix CLI for Sites supports local IDE development and GitHub-based code management. It is distinct from the CLI for new Wix apps/headless projects. Use the existing site's supported integration, not a generated headless replacement. [W1]

## 3. Site map and page responsibilities

**Primary navigation:** Thinking | BPM | Startups | AI | ISO | Insights | Shop | About.  
**Utility navigation:** Sign in / My Library | Cart | Language.  
**Research entry:** AI > Responsible AI Research. It is not a commercial product category.

Paths below are target routes. Retain existing good URLs where practical and configure redirects for changes. Native Wix Stores product and checkout routes remain Wix-managed.

| Page / route | Audience and content | Main action |
|---|---|---|
| Home `/` | Value proposition, area cards, actual featured products, book introduction and a research invitation. | Explore an area or Shop. |
| Thinking `/thinking` | 21 Prisms, practical thinking material, companion assets and book retailer links. | Get a free resource or buy a toolkit. |
| BPM `/bpm` | BPM-360, Production Readiness and products derived from existing personal IP. | View available BPM tools. |
| Startups `/startups` | Idea validation, problem definition and existing innovation material. | View startup tools and examples. |
| AI `/ai` | Separate blocks for Products, Responsible AI Research and Insights. | Buy a tool or view the research invitation. |
| ISO `/iso` | Concise VP Quality introduction. Clearly identified external provider. | Visit VP Quality when its site is live. |
| Shop `/shop` | One searchable catalog, with filters for area, format, language and access type. | View product or add to cart. |
| Product page | Outcome, audience, deliverables, preview, language, license, version, price and access rule. | Buy, sign in, or download if entitled. |
| Free resource `/resources/{slug}` | Public description/preview; protected file available only after registration. | Sign in and obtain resource. |
| Research overview `/ai/research` | Approved study explanation, eligibility, time estimate, privacy and contact details. | Sign in to participate. |
| Questionnaire `/research/{studySlug}` | Consent, eligibility, questions, dictation, review and submission. | Save draft or submit. |
| Research receipt `/research/receipt/{id}` | Current participant's submitted record and PDF status. | Download or request copy. |
| My Library `/account/library` | Free resources claimed and purchased assets; no other member's data. | Download permitted version. |
| My Research `/account/research` | Own drafts, submitted receipts and withdrawal-request entry. | Resume or view own response. |
| Insights `/insights` | Articles, excerpts and free educational content. | Read; optionally register for resources. |
| About / Contact | Personal professional background and support contact. No employer-service catalog. | Contact / support. |
| Policies | Privacy, terms, licensing, refund/delivery policy, accessibility and study information. | Read policies without signing in. |

**Research page treatment:** Use the Think21 brand, but remove product recommendations, cart prompts, marketing popups, chatbots and advertising/session-replay scripts from the questionnaire, consent and receipt views. The public AI landing page may link to both commerce and research.

### 3.1 Shared page templates

**Area template:** Introductory value proposition > explanation of the framework > available products > registered-member resources > related Insights. Each product card uses the same catalog record as the Shop.

**Product template:** Problem/outcome > who it is for > exact package contents > preview > format/language/version > license/support/update terms > price and action > relevant alternatives. Do not promise unlimited support, lifetime updates or guaranteed results by default.

**Empty-category behavior:** Keep unpublished products out of public galleries. Show useful existing content instead of fictitious products or an empty store. A category can exist internally before products are approved.

### 3.2 Language and accessibility

English is the proposed initial Think21 interface language. Keep content and product language separate so Hebrew or other product editions can be listed without translating the entire site. Questionnaire languages are enabled only when the approved instrument and consent are available in that language.

Support keyboard navigation, visible focus, semantic labels, readable contrast, mobile layouts, screen-reader status announcements and right-to-left rendering where required. Dictation MUST remain optional: the complete questionnaire must work with a keyboard and no microphone.

## 4. Catalog, content and initial product families

### 4.1 Catalog structure

A **product** is the commercial offer. A **resource** is an individual downloadable asset. A **resource version** identifies an immutable file release. A product can grant multiple resources, and a resource can appear in multiple areas without being duplicated.

| Entity | Required business fields |
|---|---|
| Area | Stable ID, slug, title, summary, display order, publication state. |
| Catalog entry | ID, type (paid/free/external), area IDs, audience, outcome, format, language, preview, publication state. |
| Paid offer | Wix product/variant IDs, SKU, currency, native price, license, included resources and upgrade policy. Wix remains authoritative for price/order data. |
| Resource | ID, area IDs, description, current version, access policy, permitted uses and support instructions. |
| Resource version | Version ID, language, private file ID, checksum, release notes, publication date and compatibility notes. No public file URL. |
| External entry | Retailer/provider name, verified external URL and clear external-purchase label. No local entitlement implied. |

### 4.2 Seed catalog: candidates, not an instruction to build everything

| Area | Family | Initial implementation treatment |
|---|---|---|
| Thinking | 21 Prisms Companion Workbook, reflection/decision journal, cards and team toolkit | Prepare one owner-approved product first. Keep the rest unpublished until packaged. |
| Thinking / Books | 21 Prisms book | Link to confirmed Spines/retailer listings. No automatic bonus entitlement for an external purchase without a separate redemption process. [U7] |
| BPM | BPM-360 / Production Readiness workbook | Catalog area and draft offer only until an existing-IP package is approved. No new consulting workstream. |
| Startups | Idea Validation / Idea-to-Viable-Concept tools | Reuse selected original material. Do not introduce the full Arbitrage platform as a site dependency. |
| AI | Master Prompt Architect | Treat the four supplied files as source versions within one family. The owner approves packaging, tiers and licenses before publishing overlapping editions. [U2-U5] |
| AI / Thinking | AI learning and reflection materials | The supplied Brain Acceleration document provides candidate workflows and a seven-day exercise sequence. Publish only after editorial/source review. [U6] |
| ISO | VP Quality tools/services | External referral only in version 1. Separate checkout and consent boundaries. |

The prompt documents contain intended quality/governance instructions, not evidence of guaranteed safety or enterprise certification. Do not market prompt-only products as injection-proof, hallucination-free or independently certified. Remove drafting artifacts and unsupported research/performance claims before publication. [U2-U6]

### 4.3 Product approval checklist

For every published offer, the owner approves: package contents; intellectual-property/production-file rights; working download files; language; version; license; price; tax treatment; support boundary; refund policy; and the free/purchase access rule. All previews must be separate, deliberately public files.

## 5. Functional requirements and user journeys

| ID | Requirement |
|---|---|
| FR-01 | Public pages and catalog descriptions work without registration. |
| FR-02 | Registration/sign-in offers Google and LinkedIn. No Facebook or standalone password-registration offer. |
| FR-03 | A member obtains free assets without checkout when the asset policy permits it. |
| FR-04 | Paid/bonus assets require a server-verified qualifying purchase or an audited manual grant. |
| FR-05 | Each area displays its own offers; Shop displays the same offers across areas. |
| FR-06 | Members have My Library, order access and private research receipts. |
| FR-07 | Research requires sign-in, eligibility and separate versioned informed consent. It never requires a purchase. |
| FR-08 | Narrative answers support typing, dictation, correction and explicit approval. |
| FR-09 | Draft progress can be saved and resumed. Final submissions are immutable records. |
| FR-10 | Every accepted submission generates a PDF and remains available to authorized administration. |
| FR-11 | The participant can download the PDF and optionally request an email copy. |
| FR-12 | Administrators control products/access, studies, response exports, failed jobs and retention. |
| FR-13 | Research data remains isolated from sales automation, marketing segmentation and product analytics. |
| FR-14 | Versioned exports and an adapter boundary permit future Q-Hub integration without changing public research URLs. |

### 5.1 Core journeys

**Free resource:** Public area > resource preview > Google/LinkedIn sign-in > return to resource > backend policy check > private download > resource appears in My Library. Registration does not subscribe the member to marketing.

**Paid product:** Area or Shop > product page > sign-in > cart/checkout > verified paid order > entitlement grant > My Library download. A pending or failed payment does not unlock files.

**Research:** Public invitation > sign-in > eligibility > information sheet and consent > questions > typed/dictated text > participant review > Submit > saved response ID > PDF processing > downloadable PDF and optional email copy.

**Administrator:** Staff authentication > authorized dashboard > relevant study/product view > export, retry or policy change > audit record. Website member roles must not confer staff administration rights.

## 6. Platform modules and component architecture

### 6.1 Native Wix versus custom components

| Component | Selected implementation | Boundary |
|---|---|---|
| Pages and area layouts | Existing Wix Editor/Studio environment | Reuse approved visual tokens and responsive components. |
| Shop and orders | Wix Stores / Wix eCommerce | Catalog, cart, payment-provider integration and order history. [W2] |
| Member account | Wix Members Area and compatible authentication UI | Account/session and account pages. [W3] |
| Google login | Native Wix Google sign-in where it supports the required flow | Test the installed authentication experience; Wix documentation differs between editor/app generations. [W4] |
| LinkedIn login | Custom OIDC-to-Wix session bridge | Not a native standard Wix social-login button. [W4-W6] |
| Access rules / library | Velo web modules + private CMS collections | Server-side entitlements; not just hidden buttons or member-only pages. [W7-W9] |
| Research questionnaire | Config-driven custom page/component + Velo | Native forms alone do not implement the specified consent, transcript review and submission lifecycle. |
| Voice capture | Production-tested custom element using MediaRecorder | Never assume a generic Wix HTML iframe has microphone permission. [W10-W12, W30] |
| Speech/PDF processing | One Node.js container service, proposed Google Cloud Run | Transcription adapter, HTML-to-PDF renderer, optional attachment/Drive adapters. [W13-W16] |
| Response data / files | Wix CMS + private Wix Media | Structured answers in CMS; PDFs and paid assets in private Media. [W8-W9] |
| Asynchronous delivery | Durable outbox + managed task queue | Proposed Cloud Tasks invokes the worker; retries survive a closed browser. [W16] |
| Email | Transactional email adapter | Secure member-portal link; optional actual PDF attachment through an attachment-capable service. [W17-W18] |
| Optional archive | Google Drive adapter | Dedicated admin archive; no participant Drive/Gmail scopes. [W19] |

### 6.2 Logical architecture

```text
PUBLIC / MEMBER BROWSER
  Wix area pages + shared catalog + member library
  Custom research form + optional voice recorder
              |
              v
WIX VELO BACKEND: TRUST BOUNDARY
  Identity bridge | Policy engine | Commerce adapter
  Research service | Admin service | Durable job outbox
       |                     |                   |
       v                     v                   v
Wix Stores / Members    Private Wix CMS     Processing gateway
Private Wix Media       and response data   + durable task queue
                                                |
                                                v
                                       Container worker
                                       Speech-to-text
                                       PDF renderer
                                       Transactional email
                                       Optional Drive archive
```

**Authoritative systems:** Wix Members for member IDs; Wix eCommerce for orders/payment state; CMS policy data for access rules; immutable CMS submission snapshots for research answers. The PDF is a representation of the snapshot, not the primary database.

**No headless rewrite:** Only the specialist worker runs outside Wix. Preserve native checkout; do not build custom card handling. Keep ordinary public pages free of questionnaire/recording scripts until needed.

## 7. Identity and registration

### 7.1 Account model

The public sign-in screen offers **Continue with Google** and **Continue with LinkedIn**. A Google account can use Gmail or another verified address; the baseline is Google authentication, not an `@gmail.com` suffix restriction. A domain-only restriction would require a separate owner decision.

The canonical application identity is `wixMemberId`. Provider identity is `(issuer, subject)`, not display name or an email supplied by the browser. Do not request LinkedIn contacts, employer data, posting permissions, Gmail access or participant Google Drive access.

| Identity case | Required behavior |
|---|---|
| First Google sign-in | Complete the supported Wix Google flow, obtain the authenticated member, record acceptance of site terms and return to the original route. |
| First LinkedIn sign-in | Validate OIDC response, resolve an approved email, safely create/link the Wix member, then establish a Wix member session. |
| Same email, unlinked account | Require authentication to the existing account before linking. Never silently merge because an email matches. |
| LinkedIn email missing/unverified | Collect and verify an email in the pending sign-in transaction, or offer Google sign-in. Do not fabricate an email address. |
| Existing provider changes email | Resolve by the established provider subject/member mapping. Email changes require verification and must not select another member's account. |
| Declined social authorization | Return a recoverable sign-in message; preserve the original destination, not sensitive research answers. |
| Blocked/deleted member | Deny session establishment and protected-resource access. Preserve only records required by the approved retention policy. |

LinkedIn's OIDC documentation makes email and email verification optional and requires application access to its sign-in product. LinkedIn authentication is not proof of real-world identity or research eligibility. [W5]

### 7.2 LinkedIn bridge sequence

1. The browser creates a high-entropy verifier in session storage and sends its hash to `beginLinkedInLogin`. The backend creates a short-lived transaction with state, nonce, an allowlisted return path and the browser challenge.
2. Redirect to LinkedIn's authorization-code flow with only `openid`, `profile` and `email`. Register the exact production/test callbacks. Use the provider's supported PKCE and nonce behavior through a maintained OIDC library; verify this in the authentication spike.
3. The backend callback validates state, exchanges the code server-side and verifies the ID token signature, issuer, audience and expiry. Verify nonce where supported and bind the result to the original transaction. Reject unexpected subjects or malformed tokens.
4. Resolve the provider mapping and any email-verification/account-linking requirement. Store only the minimum result. Do not retain provider access tokens for later marketing.
5. Redirect to a completion page with an opaque, short-lived redemption code, not a Wix session token. The browser redeems it with its original verifier.
6. Atomically consume the redemption record. Generate the Wix session token only for the server-resolved member email; apply it with the supported Wix session API. Delete transient secrets and return to the original allowlisted path. [W6]

**Critical prohibition:** Never expose `generateSessionToken(email)` as an unrestricted web method. That API can create/log in a member for the supplied email; only a verified, bound, single-use identity transaction may reach it. Do not place access tokens or session tokens in URLs, analytics or logs. [W6]

### 7.3 Social-only sign-up configuration

Use a two-button public login experience. Disable/hide alternate signup routes in the installed authentication app and inspect native cart/account screens for fallback email signup. Hiding a field is not a backend security restriction.

Protected application methods also require a server-verified Google/LinkedIn enrollment record. A Wix account created through an alternate route must complete approved social linking before obtaining free assets or starting research. Record provider enrollment only from a trusted authentication result, never a browser flag. If the native Google flow cannot establish that evidence, use the validated OIDC bridge for both providers.

The pre-build authentication spike MUST verify Google, LinkedIn, return-to-page behavior and existing-member linking on the published test domain. If the installed native Google UI cannot provide the required social-only flow, route Google OIDC through the same trusted bridge rather than leave an unintended password-registration path. This fallback changes the authentication adapter, not the site architecture.

Do not confuse Wix headless identity examples with a requirement to rebuild the existing site. Select the documented session bridge supported by this Wix site; verify exact imports against its SDK generation before implementation. [W4, W6]

### 7.4 Account and consent settings

New member profiles are private. Do not enable a public member directory, automatic community membership or public activity feeds. Site terms acceptance, research consent, voice-processing permission, email-copy preference and optional marketing subscription are separate fields. Unchecked marketing consent must not block registration, free downloads or research. [W3, W20]

Store only required contact details. Use Google/LinkedIn identity solely for account authentication; ask research eligibility questions directly through the approved instrument.

## 8. Access policies, commerce and digital delivery

### 8.1 Access-policy model

| Policy | Check performed on backend | Public action |
|---|---|---|
| `PUBLIC_PREVIEW` | Published preview only; never the full workbook. | View preview. |
| `REGISTERED_FREE` | Active authenticated member; asset is published. | Sign in to download / Download. |
| `PURCHASE_ANY` | Active member holds at least one qualifying product/variant grant. | Included with specified product(s). |
| `PURCHASE_ALL` | Active member holds every explicitly required grant. | Explain required package. |
| `MANUAL_GRANT` | Explicit, active, audited grant for this member/resource. | Open in My Library. |
| `EXTERNAL` | No local fulfillment. Display approved external link. | Buy from retailer / Visit VP Quality. |

An area may define a default policy for new resources, but every published resource receives an explicit policy. An empty `PURCHASE_ANY` or `PURCHASE_ALL` product list is invalid and must deny access, not unlock everything. Category membership alone never grants ownership.

The owner can preview policy behavior as Guest, Member, Buyer of Product A, and Buyer of Product B before publishing. Changes require a revision and audit entry. Previously purchased rights must follow the offer/license accepted at purchase, not an accidental later catalog edit.

### 8.2 Purchase and entitlement flow

1. Show public offers using Wix product IDs; route purchases through the signed-in flow. Restrict the cart to members and disable unguarded Buy Now/express paths for launch. Wix notes that some purchase paths can bypass a restricted cart. [W21]
2. On payment/order events, verify the event source, deduplicate by event ID and retrieve the current order from Wix. Never accept a browser's `paid=true` or a successful redirect as payment evidence. [W22]
3. Resolve the verified member/order association. Use authenticated member ID where available. A guest/bypassed order must enter `UNCLAIMED`, with no protected file released until a Google/LinkedIn member proves ownership.
4. Grant the resources included in the paid line item and persist the offer/version policy snapshot. A delayed event may be reconciled from the authoritative order API when the member opens My Library.
5. Process cancellation, refund and dispute states. Apply item-level revocation for refunded items; do not revoke a resource still covered by another valid purchase. Route ambiguous partial refunds to an administrator.
6. Run periodic reconciliation to recover missed or out-of-order events. Event handling must be idempotent and tolerate delayed delivery. [W22]

Zero-price member resources use a direct claim flow, not a zero-value checkout. Paid offers and bonuses are separate from academic participation.

### 8.3 Native digital files versus protected assets

Wix Stores automatically delivers digital product links when an order is paid; its standard download links expire after 30 days. This is useful native fulfillment, but it is not the same as a member-authenticated, purchase-aware library. [W2]

**Selected design:** Keep actual workbooks, prompt packs and purchased resources in private storage. Where Wix requires a digital attachment for a store product, attach a small Access Guide explaining how to open My Library; do not attach the protected workbook itself. State this delivery method accurately on the product page and receipt.

The account library is the normal fulfillment surface. It checks identity and entitlement each time it issues a download. This also supports product bonuses and new file versions without relying on old retailer/checkout links.

### 8.4 Secure download flow

`requestDownload(resourceVersionId)` authenticates the member, checks the current grant/version scope, writes a minimal commercial download event and requests a short-lived URL for that single private file. No private file IDs or URLs are included in public CMS records, page datasets, search indexing or product descriptions.

Set `private: true` when uploading protected Wix Media files. Public files cannot be made private merely by hiding a page; re-upload through the private-file API where necessary. Use the single-file temporary download API, not the permanent multi-file ZIP download URL. Prepackage bundles as one private ZIP. [W8-W9]

**Proposed transport default:** 5-minute product download URLs, shorter for research PDFs where supported. A signed URL is a temporary bearer link and can be forwarded while valid. This is access control, not DRM; already downloaded files cannot be remotely revoked. Avoid claims of unshareable documents.

### 8.5 External book and ISO purchases

Book retailer links remain external. Do not assume Spines supplies real-time customer identity or purchase webhooks. A future reader-bonus redemption flow must specify evidence, privacy and fraud handling separately. [U7]

VP Quality remains a separate seller. Do not silently share member details, merge carts or grant cross-site purchase rights. Any later reseller/shared-login arrangement requires an explicit agreement and a new integration design.

## 9. Responsible AI research

### 9.1 Academic release gate

Public framing is Responsible AI, with interpretation risk and organizational human-AI decision-making as relevant context. The precise study title, method, recruitment criteria and questions must come from the approved doctoral protocol.

Before enabling collection, record the applicable advisor/ethics approval, approved questionnaire and consent versions, eligible population, processor/storage choices and retention/withdrawal terms. A web questionnaire must not silently replace an interview-based feasibility design. Until approved, use an explicitly labeled test study with synthetic responses only.

Registration links participation to an account. The service must describe records as **confidential and pseudonymised**, not anonymous. An identity mapping still exists, even when exported answers use random participant IDs. [W23]

### 9.2 Consent and eligibility flow

| Step | Required behavior |
|---|---|
| Public information | Study overview, eligibility, estimated duration, registration requirement and researcher contact visible without login. |
| Registration | Google/LinkedIn sign-in; no research answers collected during account creation. |
| Eligibility | Approved questions only. Record outcome; do not infer eligibility from LinkedIn profile or purchased products. |
| Research consent | Show the approved information sheet and explicit unchecked consent. Save version, timestamp and participant reference. |
| Dictation permission | Before first recording, explain the speech processor, temporary audio handling and text alternative. Browser microphone permission is not research consent. |
| Email-copy choice | Optional; separate from consent to participate and from marketing. A copy is available in the private account without email. |
| Withdrawal | Explain the approved process and cutoff, including what cannot be removed after irreversible anonymisation/aggregation. |

No rewards, discounts or marketing follow-ups should be tied to research answers or completion unless explicitly approved as part of the protocol. Research pages must not request employer/client secrets; display a clear warning against entering identifiable third-party or confidential business information.

### 9.3 Questionnaire schema and rendering

Support single choice, multiple choice, fixed scale, short text and long text. Dictation is available only on text questions configured with `allowVoice=true`. Render approved labels and ordered choices verbatim. Do not use an LLM to improvise follow-up questions, rewrite the instrument or score respondents in version 1.

A study version includes: stable question IDs; approved language; section order; required/optional flags; allowed choices and scales; length limits; branching conditions; consent version; and instrument hash. Store skipped-by-branch, unanswered-optional and answered values distinctly.

Publishing a changed question, consent or scale creates a new version. Existing drafts remain pinned to their original version unless the researcher explicitly closes it and communicates the effect. Never mix versions silently in exports.

### 9.4 Draft and final-answer behavior

Autosave typed/accepted text with a visible Saved / Saving / Not saved state. Save on question navigation as well as after a short debounce. Keep unsent content in memory and warn before leaving; do not persist sensitive answers in ordinary browser local storage by default.

Every draft is owned through the server-resolved participant mapping. Use immutable revision records with a unique key for `(draftId, revision)` to detect competing saves. Do not rely on a read-then-update counter as an atomic lock. A conflict prompts reload/merge rather than silently overwriting another tab's answers.

The participant can review every answer, edit text and confirm the final record. Dictated text that has not been accepted cannot be submitted. Submission validation is repeated server-side against the pinned instrument, consent and eligibility.

### 9.5 Submission and artifact states

```text
Study:      DRAFT -> APPROVED -> OPEN -> PAUSED / CLOSED
Draft:      IN_PROGRESS -> READY_FOR_REVIEW -> SUBMITTED
Response:   immutable final snapshot + separate withdrawal status
PDF job:    PENDING -> PROCESSING -> READY / RETRYABLE / FAILED
Email job:  NOT_REQUESTED / PENDING -> SENT / UNKNOWN / FAILED
Archive:    DISABLED / PENDING -> ARCHIVED / FAILED
```

Commit the final structured snapshot before dispatching PDF/email/export jobs. An atomic unique insert keyed to the allowed submission prevents double-submit duplicates. A replay with the same payload hash returns the same receipt; a conflicting payload returns a conflict error.

The submission receipt must appear even when PDF/email processing is temporarily unavailable. Closing the browser must not cancel committed processing. Administrators see failed artifacts separately from accepted responses and can retry without collecting another response.

## 10. Dictation, transcription, PDF and email

### 10.1 Dictation experience

Each voice-enabled text answer displays Write / Dictate, recording state, timer, Stop, Discard, transcript preview, and Use this text. The user can append additional clips, replace text after confirmation, or edit everything manually.

1. Request explicit voice-processing permission and then browser microphone permission on a user action.
2. Record a short clip using `getUserMedia` and `MediaRecorder`; negotiate a supported MIME type at runtime. Stop all microphone tracks on stop, navigation or component teardown. [W10-W11]
3. Obtain a short-lived upload/transcription capability from Velo. The backend verifies the member, draft ownership, study status, consent and question permission.
4. Send the audio directly to the processing service, not through a Velo web-method payload. The capability is bound to one job, draft, question, revision and allowed size/duration.
5. The service validates the capability, consumes its job claim, checks the actual media and transcribes it. Audio is processed in memory and discarded after processing; no permanent audio archive is enabled in the baseline.
6. Persist a short-lived pending transcript in the private research store, and return it to the authorized participant. The user edits/accepts it; only accepted text becomes an answer.
7. Delete superseded pending transcripts according to the configured draft policy. Silence, unintelligible speech or a provider failure must never produce invented text.

**Meaning of voice-to-text:** Transcribe in the spoken language. Do not translate, summarize, polish arguments or replace the participant's wording with AI-generated prose. Store input mode and review status for methodological analysis; do not infer personality, competence, emotion or risk from the voice.

### 10.2 Browser and provider choices

Use a Wix custom element tested on the published domain, not only Editor Preview. An iframe needs explicit microphone permission from its parent; merely embedding an HTML form is insufficient. If the selected Wix component cannot request microphone access, use a same-brand, top-level recorder route with the same short-lived capability. Returning its transcript must not expose another member's draft. [W10]

Browser `SpeechRecognition` is not the baseline because availability and processing behavior differ by browser. Native keyboard dictation remains a user-controlled text-entry alternative; the site-provided recording flow uses the approved processor. [W12]

**Proposed processor:** Google Cloud Speech-to-Text behind a `TranscriptionProvider` adapter. Start with the approved questionnaire language, normally English if that is the approved instrument. Confirm region, model and processor terms before enabling production. Google currently documents Hebrew as `iw-IL` for Chirp 3, with a preview status; do not assume the web locale `he-IL` is the API code or silently enable a preview model. [W13-W14]

**Proposed engineering defaults:** 55 seconds and 8 MB per clip, with an additional clip allowed after each transcription. These sit below Google's documented synchronous short-audio limits. Overall duration limits must be visible and agreed with the researcher; do not silently cut off answers. Provider-specific limits remain adapter configuration. [W13]

Disable optional provider data logging/training enrollment. Document the actual processor retention and processing region in the approved information sheet. Local audio deletion does not erase email copies or override a processor's contractual retention. [W15]

### 10.3 PDF generation

The PDF worker reads only the immutable submitted snapshot and its pinned questionnaire text. Use an HTML print template and server-side Chromium through Playwright. Escape participant content; disable scripts, remote URL fetching and uncontrolled HTML. Embed licensed fonts available in the deployment image, with correct Hebrew/RTL and mixed-language layout where enabled. [W24]

| PDF field | Specification |
|---|---|
| Document heading | Think21 / Responsible AI Research, approved study title and confidentiality label. |
| Receipt metadata | Response ID, instrument version, submission timestamp/time zone and language. |
| Consent reference | Approved consent version and consent timestamp; no access tokens or identity-provider details. |
| Questionnaire | Every applicable question in its original order, with the approved final answer. |
| Unanswered items | Explicitly distinguish optional unanswered and branching-skipped items. |
| Footer | Page number, researcher/support contact and approved withdrawal reference. |
| Integrity | Internal snapshot hash and template version stored in metadata/manifest; no full personal email by default. |

Generate a separate PDF for each completed questionnaire, not one file that combines multiple participants. Default filename: `Think21-Research-{responseId}.pdf`. The PDF and admin record contain identical approved answers. No AI-generated interpretation is added.

Upload as a private Wix Media file and wait for successful processing before marking it READY. Retrying uses the same snapshot/hash and must not overwrite another response's artifact. The UI shows generation progress and offers a retry/contact message without asking the user to resubmit answers.

### 10.4 Participant copy

Offer three choices at completion: Download in account; email a secure account link; or, when enabled, email the PDF as an attachment. The optional attachment choice must explain that an ordinary email attachment can be forwarded and cannot be recalled.

The member-account link is the default. Its destination requires the correct member session; it is not a permanent public Drive URL. For actual attachments, use an attachment-capable transactional provider, such as the documented Postmark Email API, behind an adapter. Do not assume Wix Triggered Emails supports arbitrary per-user attachments. [W17-W18]

Send only to the verified address belonging to the requesting participant. Address changes require verification. Email contains no promotional content, tracking pixel or link tracking. Store delivery ID/status, not an unnecessary duplicate of answers in logs. A provider timeout with uncertain delivery is UNKNOWN: reconcile before automatically resending.

The participant can request another copy through the authenticated receipt page, subject to a resend limit. Email failure does not affect submission validity or account download availability.

## 11. Data model, storage and retention

### 11.1 CMS collections

All collections below are application-managed. Public projections must contain no secrets or private file references. Private collections permit no direct browser read/write, even for logged-in members; access goes through backend authorization.

| Collection | Core contents | Access |
|---|---|---|
| `Areas` | Public area content and display order. | Published projection public; editing authorized staff. |
| `CatalogEntries` | Safe product/resource metadata, area links, Wix product IDs and external links. | Published projection public. |
| `Resources` / `ResourceVersions` | File IDs, immutable releases, licenses and version policy. | Backend and authorized content staff. |
| `AccessPolicies` / `OfferGrants` | Registered-free or qualifying purchases; product-to-resource mapping and revision. | Backend and commerce administrator. |
| `Entitlements` | Member, resource, source order/line/grant, version scope, status and grant/revocation timestamps. | Backend; member receives only own safe projection. |
| `IdentityLinks` / `AuthTransactions` | Verified social enrollment and provider subject mapping; short-lived login transaction state. | Authentication backend only. |
| `MemberPreferences` | Terms version, locale and independent marketing preference. | Own-member projection; authorized backend. |
| `ResearchStudies` / `StudyVersions` | Protocol configuration, approvals, immutable questions and consent text. | Research administrator; approved public overview separately projected. |
| `ResearchParticipants` | Random per-study participant ID linked to Wix member ID; eligibility and contact reference. | Restricted research identity boundary. |
| `ResearchConsents` | Participant/study/version, scope, acceptance/withdrawal and timestamp. | Research backend and authorized investigator. |
| `ResponseDrafts` | Versioned draft snapshots, accepted text, branching state and autosave revision. | Own-participant backend access only. |
| `PendingTranscripts` | Job/question/revision, transcript, processor metadata and expiry. | Own-participant backend; no marketing access. |
| `ResearchSubmissions` | Immutable final answer snapshot, question/version references, participant code and integrity hash. | Research backend and investigator. |
| `ResearchArtifacts` | PDF/Drive IDs, template/snapshot hash and processing state. | Own-participant projection or investigator. |
| `ProcessingJobs` / `IntegrationOutbox` | Job purpose, idempotency key, attempts, state and non-sensitive error code. | Backend/operations. |
| `AuditEvents` | Actor reference, action, entity, timestamp and outcome. No raw responses/tokens. | Authorized audit/operations staff. |
| `DeletionRequests` | Request scope, identity verification, affected artifacts, status and completion record. | Privacy/research administrator. |

**Identity separation:** Research answer snapshots carry a random study-specific participant ID, not email, name, OAuth subject or commercial profile. Re-identification requires the restricted mapping. Content staff, the Sales Agent and VP Quality have no access to that mapping or response collections.

**CMS caveat:** Wix owners and high-privilege CMS collaborators may retain broad access. Do not assume an application dashboard role hides data from the platform owner. Restrict platform collaborators as well as application roles; use a separate approved research datastore later if institutional separation cannot be met. [W25]

### 11.2 Consistency and uniqueness

Use deterministic UUIDs or a single composite-key field for unique inserts: provider identity, draft revision, allowed participant submission, order-line/resource grant and processing idempotency key. Avoid unsupported multi-column uniqueness assumptions. Wix supports unique indexes and is eventually consistent; use consistent reads where a just-written consent, grant or submission must be observed immediately. [W26-W27]

Do not assume multi-collection ACID transactions. The single immutable submission is the commit boundary; projections, PDFs, email and archives are idempotent downstream effects. Outbox recovery must find committed submissions missing an artifact job. Configure a scheduled, authenticated reconciliation task independent of page visits; proposed interval is five minutes. Use stable job keys and retry backoff. Monitor stale jobs so a failed initial enqueue cannot leave a submission permanently without a PDF.

Set bounded payload limits below the selected Wix item/request quotas. A proposed v1 maximum is 200 KB per final answer snapshot; tune against the approved instrument and test before activation. A required answer must not be truncated silently to fit a database limit.

### 11.3 File-storage selection

| Data | Version 1 location | Rules |
|---|---|---|
| Original commercial packages | Private Wix Media | Versioned files; temporary authorized download only. |
| Public previews | Public Wix Media | Separate deliberately reduced examples; no confidential data. |
| Accepted research answers | Private Wix CMS | Authoritative structured snapshot. |
| Participant PDFs | Private Wix Media | File IDs referenced from protected artifact records. |
| Raw dictation clips | Browser/service memory during processing | Not persisted by the application in the baseline; processor terms still apply. |
| Optional research archive | Dedicated Google Drive folder/shared drive | JSON snapshot + PDF + manifest; administrator-only access. |
| Development fixtures | Local/test repository | Synthetic participants and answers only. |

### 11.4 Optional Google Drive archive

Enable only after the owner approves the account, region/processor implications and permissions. Do not request participants' Drive permission: the archive belongs to the research administrator.

For a supported Google Workspace Shared Drive, use a dedicated service account with minimum necessary access. For personal My Drive, use administrator OAuth with securely stored refresh credentials; a service account cannot own files or provide its own storage quota. [W19]

Proposed structure: `Think21 Research/{studyId}/{instrumentVersion}/{responseId}/`, containing `response.json`, `response.pdf` and `manifest.json`. Keep identity mappings in a separately restricted location, not beside de-identified exports. Do not create anyone-with-link sharing.

Archive write failures remain visible and retryable without invalidating the CMS submission. Choose CMS as the only editable master; a manual Drive edit never changes the accepted research record. Include Drive copies in deletion/withdrawal workflows.

### 11.5 Retention configuration

| Record type | Baseline rule |
|---|---|
| OAuth attempts and redemption secrets | Short expiry; proposed 10 minutes; remove on successful use/expiry. |
| Audio | Release application memory after processing or abandonment; no durable raw-audio retention. |
| Pending transcripts/drafts | Proposed deletion after 30 days of inactivity, subject to approved protocol. Notify users where required. |
| Submitted responses and identity mapping | Set from institutional protocol before collection opens; no invented universal retention period. |
| PDFs and Drive archives | Follow response retention and withdrawal scope. |
| Commercial orders/invoices | Separate accounting/legal retention schedule; account deletion does not automatically remove legally retained records. |
| Logs/backups | Explicit access and retention schedule; no response bodies or session tokens. |

An account deletion request and a research withdrawal request are separate processes. Explain their effects, record completion and propagate permitted deletions to every controlled store/processor. A PDF already downloaded or emailed to the participant is outside subsequent server-side revocation.

## 12. Application interfaces and repository structure

### 12.1 API contract conventions

The following names are application interfaces to implement, not claims that Wix provides these functions natively. Browser-to-Wix functions use `.web.js` methods with restrictive permissions. The backend resolves the caller; requests never accept an authoritative `memberId`, admin role, paid flag or file URL. [W7]

Responses use `{ok, data, error, correlationId}`. Standard errors: `UNAUTHENTICATED`, `FORBIDDEN`, `INVALID_INPUT`, `NOT_ELIGIBLE`, `CONSENT_REQUIRED`, `STUDY_CLOSED`, `CONFLICT`, `RATE_LIMITED`, `PROCESSING`, `DEPENDENCY_UNAVAILABLE`. Return safe errors, not stack traces or raw vendor responses.

| Interface | Input | Output / authorization |
|---|---|---|
| `getCatalog` | Area/filter/page | Published safe metadata; public. |
| `beginLinkedInLogin` | Return path, browser challenge | Authorization URL; public, rate-limited. |
| `redeemLogin` | Opaque code, verifier | Bound one-use Wix session result; no caller-supplied email. |
| `claimFreeResource` | Resource ID | Library entry; authenticated policy check. |
| `getMyLibrary` | Cursor/filter | Current member's resources and allowed versions. |
| `requestDownload` | Resource-version ID | Temporary single-file URL; active entitlement check. |
| `beginResearch` | Study/version, approved eligibility and consent input | Own participant/draft ID; study and consent validation. |
| `saveDraftRevision` | Draft ID, base revision, answer changes | New revision or CONFLICT; own draft only. |
| `createVoiceJob` | Draft ID, question ID/revision, MIME and language | Job ID and bounded one-use worker capability. |
| `getVoiceJob` | Job ID | Own pending transcript/status; no other user's job. |
| `acceptTranscript` | Job ID, base revision, participant-edited text | Accepted answer revision. |
| `submitResearch` | Draft ID/revision, final confirmation, copy preference, idempotency key | Stable submission ID and artifact state. |
| `getMyResearchReceipt` | Response ID | Own approved snapshot/PDF status. |
| `requestResearchPdf` | Response ID | Authorized private PDF download. |
| `requestResearchCopy` | Response ID, link/attachment mode | Email job ID; verified own recipient only. |
| `requestWithdrawal` | Response ID, reason optional | Tracked request under approved protocol. |
| `adminExportStudy` | Study/version, approved filters and format | Private export job; investigator only. |
| `adminRetryJob` | Job ID, reason | Authorized retry with audit. |

### 12.2 Internal service interfaces

| Interface | Security and behavior |
|---|---|
| `POST /voice/transcribe` | Short-lived signed capability; bounded multipart audio; one-use job claim; CORS allowlist is additional protection, not authentication. |
| `POST /jobs` | Signed backend request; create durable task using job ID, not response content, in queue payload. |
| Worker task handler | Managed-queue service identity only; verify audience/issuer and job purpose. |
| Wix internal worker read/write | HMAC/JWS-authenticated callback; timestamp, nonce, body hash and job scope. Only the fields needed for that job. |
| Wix commerce events | Native event hook or verified Wix webhook; retrieve current order and deduplicate. |
| Email status callback | Verify provider callback authenticity; update delivery status without storing message content. |

Use distinct secrets for authentication, worker callbacks and commerce integrations. Store them in Wix Secrets Manager and the worker platform's secret store. Reject stale signatures and replayed nonces. Never put a broad Wix API key in the browser or allow the worker to query arbitrary collections.

### 12.3 Core schema examples

```json
{
  "resourceId": "thinking-companion",
  "policyVersion": 1,
  "access": "PURCHASE_ANY",
  "qualifyingOffers": ["owner-configured-offer-id"],
  "versionPolicy": "PURCHASED_MAJOR_VERSION",
  "published": false
}
```

```json
{
  "schemaVersion": "1.0",
  "studyId": "responsible-ai",
  "instrumentVersion": "owner-approved-version",
  "responseId": "server-generated-uuid",
  "participantId": "random-study-specific-code",
  "language": "en",
  "consentVersion": "owner-approved-consent",
  "submittedAt": "server-generated-UTC-timestamp",
  "answers": [
    {
      "questionId": "approved-question-id",
      "questionText": "Exact approved wording",
      "type": "longText",
      "value": "Participant-reviewed answer",
      "inputMode": "dictated_then_edited",
      "reviewed": true,
      "answerState": "answered"
    }
  ]
}
```

These are structural examples, not an approved study instrument. Stable question IDs and instrument versions must be preserved in JSON/CSV exports for future Q-Hub migration.

### 12.4 Suggested code organization

```text
site/                       # Preserve Wix-generated structure
  src/pages/                # Area, library, research and login pages
  src/public/               # Safe UI helpers and schemas
  src/backend/
    catalog.web.js
    library.web.js
    research.web.js
    auth.web.js
    admin.web.js
    events.js               # Wix order/payment event adapters
    http-functions.js       # OIDC and signed worker callbacks
    services/               # Policies, entitlements, consent, jobs
    repositories/           # Wix CMS access behind authorization
    adapters/               # Wix commerce, media, email, Q-Hub seam
  custom-elements/          # Recorder source, wired to site tooling
worker/
  src/auth/                 # Capability and callback verification
  src/transcription/        # Approved provider adapter
  src/pdf/                  # Escaped HTML templates + renderer
  src/email/                # Transactional provider adapter
  src/archive/              # Optional Drive adapter
  src/jobs/                 # Durable task handlers
contracts/                  # JSON Schema and example payloads
migrations/                 # Collections, indexes and seed metadata
tests/                      # Unit, contract, browser and abuse tests
```

The actual site-generated paths take precedence. `.web.js` methods call typed, validated internal services; an AI coding assistant must not invent Wix imports, bypass permission checks or replace existing Wix routing without verifying compatibility.

### 12.5 Deployment configuration

Keep separate development/test/production credentials and data. Publish secrets through the platform secret stores, never a checked-in `.env` file. The repository contains only an `.env.example` or equivalent inventory with empty values.

| Configuration group | Required entries |
|---|---|
| Site identity | Environment, Wix site ID, canonical origin, approved callback URLs and return-path allowlist. |
| Social login | Google/LinkedIn client configuration; client secrets where custom bridges are used; state/redemption expiry. |
| Worker and queue | Worker URL, region, task queue identity, callback signing keys and reconciliation schedule. |
| Transcription | Provider/model/language mapping, approved processing region, clip limits, concurrency and cost ceiling. |
| Documents | Template version, approved fonts, private file destination and signed-link expiry. |
| Email | Verified sender/domain, provider credentials, approved templates, copy mode and resend limits. |
| Optional archive | Drive enablement, approved folder/shared-drive ID and administrator/service credentials. |
| Research release | Approved study/version IDs, consent versions, retention configuration and responsible contact. |
| Feature switches | Research collection open/closed; dictation; PDF attachment; Drive archive; third-party analytics on permitted pages. |

Store feature-switch changes with an audit record. Closing research collection must prevent new submissions according to the approved study policy without disabling existing participant receipts. Disabling dictation must leave typed answering available. Never reuse production response data to test a switch or migration.

## 13. Administration and reporting

### 13.1 Administrative workspaces

| Workspace | Required actions |
|---|---|
| Content/catalog | Edit areas; publish/unpublish entries; assign categories; preview public pages; manage language/version metadata. |
| Asset access | Upload private package; define free/purchase policy; map qualifying products; simulate member access; audit grants/revocations. |
| Commerce | Use Wix order management; review unclaimed orders, entitlement mismatches, partial refunds and download issues. |
| Research | Configure and approve study versions; open/pause/close collection; view response status; inspect individual approved records; export. |
| Processing | Monitor transcription/PDF/email/archive failures; retry safely; view costs/quotas and kill switches. |
| Privacy | Review consent/withdrawal/deletion requests; record scope; propagate removal; produce completion evidence. |

Use Wix native administration where it fits. Add a restricted application dashboard for entitlement policies and research operations. Research-admin actions require both staff authentication and an application authorization check; an ordinary site-member role must not be sufficient.

### 13.2 Research exports

Provide CSV for analysis, JSON for complete structured records and PDF for individual human-readable responses. Every export includes study ID, instrument version, stable question IDs, answer state and input mode. Exclude email/provider identities by default. Provide a data dictionary defining scales, missing values and branching.

Exports must paginate beyond a single API page and preserve Unicode. Escape spreadsheet formula-injection prefixes in CSV cells. Restrict identity-linked exports to an explicit investigator action with an audit reason. Store generated exports privately and delete them under an export-retention rule.

### 13.3 Metrics

**Commercial:** Views, registrations, resource claims, paid orders, net receipts, refunds, entitlement failures and downloads. Report native sales attribution only where actually observable; an outbound Spines click is not a verified book sale.

**Research operations:** Eligible starts, consented drafts, accepted submissions by instrument/language, input modes, PDF success and withdrawal requests. Do not expose answers or participant identities in the commercial dashboard. Suppress small-cell public research summaries until the researcher approves disclosure.

**Operations:** Dependency failures, job age, retries, transcription minutes, file storage and email delivery. No text/voice response bodies in monitoring.

## 14. Security, privacy and operational requirements

| Control | Required implementation |
|---|---|
| Authorization | Deny by default; server-resolved member/participant; check ownership on every object read, write and download. |
| CMS exposure | No member/public direct permissions on response, consent, identity, policy or entitlement collections. Public projections are explicitly filtered. |
| Privileged access | Minimize Wix collaborator permissions; MFA for administrator/provider accounts; no shared admin passwords. |
| Transport and secrets | HTTPS; secrets only in backend stores; key rotation; no secrets in repository, page code or downloadable packages. |
| Input protection | Schema validation, bounded fields, escaped output, safe filenames and no arbitrary URL fetches. |
| Rate and cost protection | Rate-limit login, voice-ticket issuance, transcription, downloads, PDF/email retries and exports. Bound worker concurrency and vendor spend. |
| Research isolation | No ads, marketing automation, session replay, answer-based segmentation or sales-agent access on research routes. |
| Caching | Never share-cache member libraries, signed URLs, consent state, transcripts or responses. Cache only public catalog projections. |
| Logging | IDs/status/error codes only. Redact tokens, addresses and text before errors leave the service. |
| File protection | Explicit private upload; single-file short-lived access; no public Drive links. |
| Consent and deletion | Versioned consent; approved retention; auditable withdrawal/deletion across CMS, Media, exports and processors. |
| Backups | Separate recovery process for CMS records and private files; encrypted/restricted copies, retention and a tested restore. |
| AI isolation | No answer-improving LLM and no third-party model training on research data. Audio transcription only under approved processing terms. |

Wix page restrictions and frontend checks are not substitutes for backend authorization. Browser-visible code is public, and exported web methods can be called with arbitrary inputs; validate before using elevated permissions. [W28]

**Research governance:** Review registration-only sampling, identity linkage, voice processing, approved languages, retention and contact permissions with the academic supervisor/ethics process. Do not claim blanket legal compliance from a template or a platform setting. Confirm applicable Israeli/EU data and consumer obligations with the responsible adviser before public launch.

### 14.1 Failure behavior

| Failure | User experience and recovery |
|---|---|
| Provider login unavailable | Show retry/other supported provider; do not create an unverified fallback identity. |
| Microphone denied/unsupported | Keep typed answering fully usable; no repeated intrusive permission prompts. |
| Network lost during typing | Show Not saved, retain current in-memory text and warn before leaving. |
| Voice request timeout | Preserve existing answer; retrieve job status before re-transcribing; allow retry or typing. |
| Speech service down/budget reached | Disable site dictation with a clear explanation; typed responses remain available. |
| Duplicate or conflicting save | Return stable receipt or revision conflict; never overwrite a submitted record. |
| PDF worker down | Response stays accepted; show PDF pending and retry through durable jobs. |
| Email uncertain/failed | Keep account PDF available; reconcile delivery before resend. |
| Drive unavailable | Preserve primary response/PDF; queue archive retry and alert admin. |
| Payment event delayed | Show access processing; reconcile from Wix; do not ask for a second payment. |

### 14.2 Cost model and operating limits

The baseline requires a Wix plan supporting the selected commerce/custom features, an eligible payment provider, a small worker deployment, transcription usage and transactional email. It is not a zero-cost system. Select the actual plan and provider in the owner account; do not assume Wix Payments is available for an Israeli merchant. Wix documents local provider integrations such as Tranzila. [W29]

Track recurring platform cost separately from payment fees and variable transcription/PDF/email usage. Set owner-approved alerts and a hard dictation/attachment kill switch. Public content, product access and typed research should continue when optional processing is paused.

## 15. Future integration boundaries

**Q-Hub:** Implement a `ResearchRepository` and versioned export schema. Future Q-Hub integration can import study/question versions, consents, pseudonymous responses and artifact references using an approved migration. Preserve public routes and stable IDs. Never silently migrate identity mappings or broaden participant consent.

**Revenue Agent:** Expose only a read-only, published commercial catalog: problem, audience, outcome, approved claims, language, format, current offer link and price source. Later sales integrations require scoped credentials. The agent must not see research participation, answers, voice clips, consent records or research contact details.

**VP Quality:** External referral in v1. A future affiliate/reseller arrangement can be implemented separately; no automatic shared account, order or mailing list.

**Future applications:** TrueMeter, Arbitrage and other portfolio products may later have explicit product entries or separate services. They are not dependencies of this site release.

## 16. Build plan and deliverables

| Stage | Build scope | Exit condition |
|---|---|---|
| 0. Audit and risk spikes | Existing-site/design audit; Google/LinkedIn login; private-file test; production microphone test; worker PDF proof with synthetic data. | Prove the four integration risks before bulk page/content work. |
| 1. Site foundation | Approved design tokens, navigation, area templates, catalog schema, Shop and public policy pages. | One catalog entry appears consistently in Shop and two relevant areas. |
| 2. Members and access | Social registration, My Library, private files, free-claim policies, purchase mapping and native checkout integration. | Guest/member/buyer/refund scenarios pass. |
| 3. Research text flow | Versioned instrument, eligibility, consent, drafts, review, submission and investigator export. | Synthetic research completed end to end with no public data exposure. |
| 4. Voice and documents | Recorder, provider adapter, reviewed transcript, PDF worker, optional email copy and durable recovery. | Typed, voice and mixed responses produce matching PDFs. |
| 5. Operations and optional archive | Admin dashboards, deletion, backups, rate/cost limits, Drive adapter if enabled. | Restore and withdrawal tests pass; alerts and kill switches work. |
| 6. Content and launch | Approved products, prices, licenses, research activation and page redirects. | Signed release checklist and rollback plan. |

**Implementation deliverables:** Site code in owner-controlled Git; worker source and container definition; environment/secret inventory without secret values; CMS schema/index migrations; seed catalog and synthetic study; contract schemas; test suite; deployment/rollback instructions; administrator runbook; and measured acceptance results.

Use the existing Wix-generated repository and native SDK versions. Confirm package imports and API contracts from current documentation. Do not create a second unrelated web application because a coding assistant cannot edit a Wix visual component automatically. Keep visual-editor tasks in an explicit manual task list.

## 17. Acceptance tests and launch gates

| Test ID | Test | Pass condition |
|---|---|---|
| AT-01 | Browse without login | Public areas, descriptions and policies work; protected files do not. |
| AT-02 | Google and LinkedIn registration | Both complete on production-like domain and return to requested page. |
| AT-03 | Malicious LinkedIn flow | Wrong state, expired token, replayed redemption and mismatched subject are rejected. |
| AT-04 | Email/account collision | No takeover/automatic merge; missing email receives verification or supported-provider fallback. |
| AT-05 | Free workbook gating | Guest denied; registered member succeeds; public source contains no protected file URL. |
| AT-06 | Purchase mapping | Buying A unlocks exactly its resources and bonuses, not unrelated B. |
| AT-07 | Checkout bypass/pending payment | No file released without verified member ownership and completed payment. |
| AT-08 | Duplicate/out-of-order payment events | Single effective grant; current Wix order state wins. |
| AT-09 | Refund/partial refund | Correct resource revoked unless independently owned through another valid grant. |
| AT-10 | Cross-member requests | Changing resource/response/job IDs never reveals another member's private data. |
| AT-11 | Consent and eligibility | No study starts before approval/consent; refusal does not affect shopping or free resources. |
| AT-12 | Save/resume and two tabs | Correct draft resumes; stale revision generates conflict, not silent loss. |
| AT-13 | Typed questionnaire | All applicable questions and answer states preserved in snapshot/export/PDF. |
| AT-14 | Dictation | Microphone opens only on action; transcript editable; final text matches user-approved version. |
| AT-15 | Voice failures | Silence, denial, oversized media, wrong MIME and provider outage never invent/overwrite answers. |
| AT-16 | Mobile/browser matrix | Current Chrome, Edge, Safari and Firefox; iOS Safari and Android Chrome; typed fallback always works. |
| AT-17 | Language/PDF | Unicode, long text, page breaks and RTL render correctly for every enabled questionnaire language. |
| AT-18 | Double submit and closed browser | One committed response; PDF continues independently of the browser. |
| AT-19 | PDF/email retry | Same snapshot; correct recipient; failed email does not lose accepted response. |
| AT-20 | Research isolation | No marketing/session-replay scripts or response payloads appear in commerce analytics/logs. |
| AT-21 | Admin permissions | Content staff cannot access research collections; investigator exports are audited. |
| AT-22 | Export completeness | Pagination, versions, skipped values and CSV injection handling are correct. |
| AT-23 | Deletion/withdrawal | Approved removal reaches CMS, Media and enabled Drive exports; exceptions are documented. |
| AT-24 | Backup/restore and rollout | Restore tested; rollback does not erase orders or accepted submissions. |
| AT-25 | Cost controls | Voice/email abuse is bounded; disabling worker features leaves typed research and library access usable. |

**Production research gate:** Approved protocol/instrument/consent, approved processors and retention, tested privacy boundaries, working exports and a named responsible researcher. Test-mode success does not authorize collecting real participants.

**Production commerce gate:** Working payments/refunds, finalized prices/licenses, secure fulfillment, seller/contact details, terms and an end-to-end test purchase with the selected payment provider.

## 18. Owner configuration and unresolved launch decisions

These are implementation inputs, not reasons to delay building the test system. Unknown values must remain unpublished or feature-disabled; a coding assistant must not invent them.

| Configuration | Required decision / proposed default |
|---|---|
| Wix site/editor/plan | Audit and confirm; preserve existing site. |
| Visual tokens | Extract logo, font/color/spacing from the current editor; owner approves any revisions. |
| Social identity | Google + LinkedIn; Google-account access rather than Gmail-domain restriction. |
| LinkedIn developer access | Owner creates/verifies app and enables OIDC; approve exact callback URLs. |
| Public products | Owner selects first ready offers; no obligation to populate every category. |
| Asset access | Per-resource free/purchase policy, qualifying offers, license and update entitlement. |
| Payments | Merchant entity, currency, eligible provider, taxes/invoices and refund rules. |
| Study | Approved title, protocol, question/consent versions, eligibility and publication dates. |
| Study languages | Approved instruments only; voice provider/model tested per language. |
| Voice | Proposed 55-second / 8 MB clips; editable transcript; application audio not retained. |
| Primary response store | Wix CMS + private Wix Media. |
| Drive archive | Off until account/permissions are approved; then one-way archive. |
| Email copies | Private portal link default; PDF attachment enabled only with approved processor and explicit participant choice. |
| Data retention | Set from approved research and commercial schedules before production. |
| Support | Contact address, escalation owner, retry handling and service/update promises. |
| Q-Hub and Sales Agent | Interfaces reserved; no live research-to-marketing data integration. |

**Definition of done:** A visitor can register with either supported provider; obtain only permitted resources; buy and access a product; participate in an approved study using text or dictation; approve the transcript; submit once; receive a correct PDF; and have the records available only to the right participant and administrators. All failure, privacy and recovery tests above pass.

## 19. Sources and implementation references

### 19.1 User-provided design and content sources

**U1.** Think21 site/portfolio requirements and decisions in this conversation, through 28 September 2026. Source of scope, domain separation, registration, access, questionnaire, PDF and administration requirements.

**U2.** `1-MASTER PROMPT ARCHITECT for Regular Users.pdf`, pages 1-3. Personal prompt-building source material.

**U3.** `2-MASTER PROMPT ARCHITECT Enterprise-Grade System Instruction Minimal Version.pdf`, pages 1-5. Compact organizational prompt instructions; draft product claims require review.

**U4.** `3-MASTER PROMPT ARCHITECT Enterprise-Grade System Instruction.pdf`, pages 1-8. Extended prompt-system source; includes deployment/audit language and drafting artifacts, not tested security assurances.

**U5.** `4-MASTER PROMPT ARCHITECT Productized Prompt Template.pdf`, pages 1-8. Candidate Basic/Pro/Enterprise packaging and customizable templates.

**U6.** `Brain Acceleration vs. Atrophy in the AI Era-1.pdf`, pages 4-11. Candidate learning workflows and seven-day exercise material. Scientific/performance claims require separate verification before publication.

**U7.** `Book distribution.docx`, pages 1-2. Supplied Spines/retailer distribution correspondence and production-file handover status; not a signed derivative-rights agreement.

### 19.2 Official technical references

Reference checks: 28 September 2026. These establish platform capabilities; policy values and architectural choices in this document remain project decisions. Recheck SDK imports, quotas and account availability during Stage 0.

**W1. Wix Git Integration and CLI for Sites**  
https://dev.wix.com/docs/develop-websites-sdk/code-your-site/developer-environments/ides/git-integration/about-git-integration-with-wix-cli

**W2. Wix Stores digital products, delivery and standard link expiry**  
https://support.wix.com/en/article/wix-stores-adding-a-digital-product

**W3. Wix Members Area**  
https://support.wix.com/en/article/site-members-adding-and-setting-up-the-members-area

**W4. Wix authentication app and native social providers**  
https://support.wix.com/en/article/wix-site-members-the-difference-between-the-default-signup-and-login-forms-and-the-member-authentication-app-ja

**W5. LinkedIn OpenID Connect**  
https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2

**W6. Wix third-party session bridge and session application**  
https://dev.wix.com/docs/velo/apis/wix-members-backend/authentication/generate-session-token  
https://dev.wix.com/docs/sdk/host-modules/site/authentication/apply-session-token

**W7. Wix backend web-method permissions**  
https://dev.wix.com/docs/velo/apis/wix-web-module/web-method

**W8. Wix Media private files**  
https://dev.wix.com/docs/velo/apis/wix-media-v2/files/private-files

**W9. Wix temporary single-file downloads**  
https://dev.wix.com/docs/velo/apis/wix-media-v2/files/generate-file-download-url

**W10. Browser microphone security and embedding requirements**  
https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia

**W11. Browser recording API**  
https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder

**W12. Browser speech-recognition API and availability**  
https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition

**W13. Google Cloud short-audio transcription limits**  
https://docs.cloud.google.com/speech-to-text/v2/docs/sync-recognize

**W14. Google Cloud supported languages and Chirp 3 status**  
https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages  
https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3

**W15. Google Cloud Speech data usage**  
https://docs.cloud.google.com/speech-to-text/docs/v1/data-usage-faq

**W16. Cloud Run asynchronous tasks**  
https://docs.cloud.google.com/run/docs/triggering/using-tasks

**W17. Wix triggered-email reference**  
https://dev.wix.com/docs/velo/apis/wix-crm-backend/triggered-emails/email-contact

**W18. Postmark transactional email and attachments**  
https://postmarkapp.com/developer/api/email-api

**W19. Google Drive Shared Drives and service-account ownership**  
https://developers.google.com/workspace/drive/api/guides/about-shareddrives

**W20. Wix private member profiles**  
https://support.wix.com/en/article/site-members-making-a-member-profile-public

**W21. Wix sign-in before purchase and cart-bypass caveat**  
https://support.wix.com/en/article/requiring-customers-to-sign-up-before-making-purchases

**W22. Wix payment-status events, verification and duplicate-event ID**  
https://dev.wix.com/docs/api-reference/business-solutions/e-commerce/orders/orders/payment-status-updated

**W23. ICO explanation of pseudonymisation versus anonymity**  
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/pseudonymisation/

**W24. Playwright PDF rendering API**  
https://playwright.dev/docs/api/class-page#page-pdf

**W25. Wix collection permissions and administrator access**  
https://support.wix.com/en/article/cms-changing-your-collection-permissions

**W26. Wix indexes and uniqueness**  
https://dev.wix.com/docs/develop-websites/articles/databases/wix-data/collections/indexes-and-wix-data-collections

**W27. Wix Data eventual consistency**  
https://dev.wix.com/docs/velo/apis/wix-data-v2/eventual-consistency

**W28. Wix security best practices**  
https://dev.wix.com/docs/develop-websites/articles/best-practices/security-best-practices

**W29. Wix example of an Israel-supported payment-provider integration**  
https://support.wix.com/en/article/connecting-tranzila-as-a-payment-provider

**W30. Wix custom elements and published-versus-preview behavior**  
https://dev.wix.com/docs/develop-websites/articles/wix-editor-elements/custom-elements/about-custom-elements
