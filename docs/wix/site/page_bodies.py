"""Page copy for the Think21 preview and the Wix embed snippets."""


def build_pages(url, questions_body: str):
    u = url
    home = f"""
    <section class="hero">
      <div class="wrap hero-inner">
        <p class="eyebrow">Think21</p>
        <h1>BPM-360, 21 Prisms, and the AI drafts behind them.</h1>
        <p class="lede">This site lists the work Yaakov Preiger already has in manuscript: the BPM-360 handbook and production-readiness gate, the 21 Prisms book, the Master Prompt Architect drafts, and the startup questions published here. A price appears only after the file, the license, and the amount are set in Wix Stores.</p>
        <div class="actions">
          <a class="btn" href="{u['bpm']}">Open BPM-360</a>
          <a class="text-link" href="{u['shop']}">See the draft catalog</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <p class="kicker">Catalog</p>
        <h2>What is real, and what is still a slot</h2>
        <div class="sheet-wrap">
          <table class="sheet">
            <thead>
              <tr><th>Item</th><th>Area</th><th>State</th></tr>
            </thead>
            <tbody>
              <tr><td>BPM-360 handbook</td><td>BPM</td><td>Manuscript exists. Not for sale.</td></tr>
              <tr><td>Production Readiness workbook</td><td>BPM</td><td>Framework exists. Workbook file is still a placeholder.</td></tr>
              <tr><td>21 Prisms of Thinking</td><td>Thinking</td><td>Book manuscript exists, currently in Russian. Retailer link is not confirmed.</td></tr>
              <tr><td>Companion workbook, journal, cards, team toolkit</td><td>Thinking</td><td>Placeholders. Not packaged.</td></tr>
              <tr><td>Idea-validation questions</td><td>Startups</td><td>Already on this site. Read them now.</td></tr>
              <tr><td>Master Prompt Architect, Basic / Pro / Enterprise</td><td>AI</td><td>Source drafts exist. Not a certified product.</td></tr>
              <tr><td>Seven-day AI learning practice</td><td>AI</td><td>Draft exercise sequence. Claims still need review.</td></tr>
              <tr><td>Responsible AI research</td><td>AI</td><td>Page is up. The approved questionnaire is not.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap split">
          <div>
            <h2>BPM-360</h2>
            <p>Adaptive business-process management for conditions that keep changing. Ten aspects, from strategy through governance, plus a production-readiness review before a change goes live. This is a handbook and a workbook, not a consulting offer.</p>
            <p><a href="{u['bpm']}">Read the ten aspects</a></p>
          </div>
          <div>
            <h2>AI, including the research page</h2>
            <p>Prompt drafts in three tiers, a seven-day practice, and a separate research page. The research form is a technical draft. It is not an open study.</p>
            <p><a href="{u['ai']}">Open AI</a> · <a href="{u['research']}">Research page</a></p>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid">
        <article class="card">
          <p class="tag">On this site</p>
          <h3>Startups</h3>
          <p>The current material is the question list already published: company, product, market, team, and risk. A later toolkit can sit beside it. Nothing here is an accelerator or a funding screen.</p>
          <a href="{u['startups']}">Open Startups</a>
        </article>
        <article class="card">
          <p class="tag">Manuscript</p>
          <h3>21 Prisms</h3>
          <p>A map in three stages, twenty-one prisms, and a short postscript. The file in hand is the Russian book. Companion downloads are named and not built yet.</p>
          <a href="{u['thinking']}">Open Thinking</a>
        </article>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>From the archive</h2>
        <p>Essays already on the site. They stay as writing.</p>
        <ul class="links">
          <li><a href="{u['post_triz']}">Contradiction, TRIZ, and systemic thinking</a></li>
          <li><a href="{u['post_methods']}">TRIZ methods for systemic contradictions</a></li>
          <li><a href="{u['post_whys']}">Five whys in architectural assessment</a></li>
        </ul>
        <p class="note">ISO and certification work is a smaller, separate door. It is not part of this catalog. <a href="{u['iso']}">ISO</a></p>
      </div>
    </section>
"""
    thinking = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Thinking</p>
        <h1>21 Prisms of Thinking</h1>
        <p class="lede">The book is a map, not a personality test. Twenty-one prisms in three stages, plus a postscript. The manuscript on file is in Russian: «21 призма мышления». An English retailer link is not confirmed, so this page does not send you to a store.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>How the book is arranged</h2>
        <div class="grid">
          <article class="card">
            <h3>Stage 1</h3>
            <p>I want to, but I don’t know what. Seven prisms for the start, when the impulse is there and the form is not.</p>
            <ul class="links">
              <li>Open thinking</li>
              <li>Creative thinking</li>
              <li>Divergent thinking</li>
              <li>Mindfulness</li>
              <li>Emotional intelligence</li>
              <li>Positive-realistic thinking</li>
              <li>Resource-oriented thinking</li>
            </ul>
          </article>
          <article class="card">
            <h3>Stage 2</h3>
            <p>I know what I want, but not how. Seven prisms that turn a wish into a path you can test.</p>
            <ul class="links">
              <li>Strategic thinking</li>
              <li>Analytical thinking</li>
              <li>Causal thinking</li>
              <li>Logical thinking</li>
              <li>Convergent thinking</li>
              <li>Ethical and ecological thinking</li>
              <li>Metacognitive thinking</li>
            </ul>
          </article>
          <article class="card">
            <h3>Stage 3</h3>
            <p>I’m on the way, and the energy drops. Seven prisms for staying in motion.</p>
            <ul class="links">
              <li>Systemic thinking</li>
              <li>Process thinking</li>
              <li>Productive thinking</li>
              <li>Detailed thinking</li>
              <li>Critical thinking</li>
              <li>Entrepreneurial thinking</li>
              <li>Noospheric thinking</li>
            </ul>
          </article>
          <article class="card">
            <h3>Postscript</h3>
            <p>A twenty-second note, not one of the twenty-one: transcendent thinking. It stays outside the three stages.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap">
          <h2>Files around the book</h2>
          <div class="sheet-wrap">
            <table class="sheet">
              <thead><tr><th>File</th><th>State</th><th>What a buyer would get</th></tr></thead>
              <tbody>
                <tr><td>21 Prisms of Thinking</td><td>External, when a retailer is confirmed</td><td>The book. Buying it elsewhere will not unlock files on this site.</td></tr>
                <tr><td>Companion workbook</td><td>Placeholder</td><td>Exercises matched to the prisms. No file yet.</td></tr>
                <tr><td>Reflection and decision journal</td><td>Placeholder</td><td>A place to record which prism you used. No file yet.</td></tr>
                <tr><td>Card set</td><td>Placeholder</td><td>One card per prism. No file yet.</td></tr>
                <tr><td>Team toolkit</td><td>Placeholder</td><td>A shared session outline. No file yet.</td></tr>
              </tbody>
            </table>
          </div>
          <p class="note">The first item to finish is one approved companion, not all five at once.</p>
        </div>
      </div>
    </section>
"""
    bpm = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">BPM</p>
        <h1>BPM-360</h1>
        <p class="lede">Adaptive business-process management for VUCA and BANI conditions. The handbook treats BPM as a set of lenses and a lifecycle, not as a single diagram. Nothing on this page is a consulting engagement.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div>
          <h2>What the manuscript already contains</h2>
          <p>A readable handbook: why the usual method mix breaks apart, what BPM-360 includes and what it refuses to be, then the working parts. Structural logic. Several lenses on the same process. Event-driven work. Decisions under uncertainty. TRIZ for contradictions. A production-readiness review before go-live.</p>
          <p>After that, ten aspects you can re-enter, and a method library. The golden path in the manuscript is an example, not a law: start from purpose, use design thinking, choose lenses, frame the contradiction, run an event storm, then pass a readiness gate.</p>
        </div>
        <article class="card">
          <p class="tag">Draft offer</p>
          <h3>Handbook</h3>
          <p>The book file exists in manuscript. It is not attached to a Wix product, and it has no price. When it is approved, the same product will show here and in the Shop.</p>
        </article>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap">
          <h2>Ten aspects</h2>
          <p>A loop, not a waterfall. You can return to an earlier aspect when the situation changes.</p>
          <ol class="aspects">
            <li>Strategy and goal setting</li>
            <li>Customer focus and value delivery</li>
            <li>Process discovery and modeling</li>
            <li>Implementation and delivery</li>
            <li>Technology and automation enablement</li>
            <li>Performance measurement and analytics</li>
            <li>Continuous improvement and optimization</li>
            <li>Risk, constraints, and resilience</li>
            <li>Change and adaptation</li>
            <li>Governance and compliance</li>
          </ol>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Production readiness</h2>
        <p>The handbook’s production-readiness framework is the gate between “the project is finished” and “the operation can carry it.” It checks three pillars before go-live. The detailed question list stays in the workbook file. It is not printed here.</p>
        <div class="grid">
          <article class="card">
            <h3>People</h3>
            <p>Roles, staffing, training, and who owns support after launch.</p>
          </article>
          <article class="card">
            <h3>Process</h3>
            <p>Updated procedures, controlled inputs and outputs, metrics, escalation, and the rules that apply.</p>
          </article>
          <article class="card">
            <h3>Technology</h3>
            <p>Capacity, monitoring, security and privacy, backup and recovery.</p>
          </article>
        </div>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap">
          <h2>BPM products</h2>
          <div class="sheet-wrap">
            <table class="sheet">
              <thead><tr><th>Product</th><th>State</th><th>Notes</th></tr></thead>
              <tbody>
                <tr><td>BPM-360 handbook</td><td>Draft</td><td>Manuscript exists. Hidden in the Shop until price, license, and file are set.</td></tr>
                <tr><td>Production Readiness workbook</td><td>Placeholder</td><td>The gate is specified. The sellable workbook file is not packaged.</td></tr>
                <tr><td>Method-card set</td><td>Placeholder</td><td>The handbook names a toolbox of methods, from event storming and BPMN to root-cause analysis. Cards are not a separate file yet.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
"""
    startups = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Startups</p>
        <h1>Use the question list that is already here</h1>
        <p class="lede">This is the startup material for now. It is the long validation list published on this site: what the company does, who it is for, how the product is different, and what can break. It is not an accelerator, a fund, or a screening form.</p>
        <div class="actions">
          <a class="btn" href="{u['questions']}">Open the question list</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Three checks the current page already asks for</h2>
        <div class="grid">
          <article class="card">
            <h3>Relevance</h3>
            <p>The idea has to meet a real need, and it has to stay movable when that need shifts.</p>
          </article>
          <article class="card">
            <h3>People</h3>
            <p>Name the founders, the experience they actually have, and the roles still missing.</p>
          </article>
          <article class="card">
            <h3>Time and money</h3>
            <p>From a first testable version to cash. The list asks for the sales cycle, the cost of a customer, and what break-even requires.</p>
          </article>
        </div>
        <p class="note">There is no registration for an investment platform on Think21.</p>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap split">
          <div>
            <h2>Idea-to-viable-concept toolkit</h2>
            <p>Placeholder. A later pack can turn the same questions into a working file. It is not a second product today, and it does not depend on another platform.</p>
          </div>
          <article class="card">
            <p class="tag">Placeholder</p>
            <h3>Not in the Shop</h3>
            <p>No price, no download. The questions remain the thing you can use.</p>
          </article>
        </div>
      </div>
    </section>
"""
    questions = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Startups</p>
        <h1>Idea validation</h1>
        <p>You need a dream large enough to matter, and you also need answers an investor, or the work itself, will demand. The questions below are the list already published on this site.</p>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap grid">
          <article class="card">
            <h3>Relevance</h3>
            <p>A strong idea still has to meet what people need, and stay adaptable when that need moves.</p>
          </article>
          <article class="card">
            <h3>People</h3>
            <p>Passion, skill, and persistence, plus the team you have and the one you still need.</p>
          </article>
          <article class="card">
            <h3>Time, actions, and money</h3>
            <p>From a first version to cash. The idea and the team still have to survive the calendar.</p>
          </article>
        </div>
      </div>
    </section>
{questions_body}
"""
    ai = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">AI</p>
        <h1>Prompt tools, a seven-day practice, and a research page</h1>
        <p class="lede">Three different things. The prompt files are product drafts. The seven-day practice is a learning draft. The research page is not a product and is not an open study.</p>
        <p><a href="{u['research']}">Open the research page</a></p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <h2>Master Prompt Architect</h2>
        <p>One family, from four source files. You choose a tier, fill the fields, and copy the result into the model you already use. The drafts talk about safety and governance. This site does not sell them as injection-proof, hallucination-free, or certified.</p>
        <div class="sheet-wrap">
          <table class="sheet">
            <thead><tr><th>Draft</th><th>Who it is for</th><th>State</th></tr></thead>
            <tbody>
              <tr><td>Simple prompt builder</td><td>Everyday tasks: role, context, instructions, constraints, output format</td><td>Source draft</td></tr>
              <tr><td>Minimal enterprise instruction</td><td>A shorter organizational system prompt</td><td>Source draft. Claims need review.</td></tr>
              <tr><td>Enterprise instruction</td><td>A longer organizational version, including modes and an authority order</td><td>Source draft. Not a security test.</td></tr>
              <tr><td>Basic</td><td>A short fill-in template for ordinary tasks</td><td>Packaging draft</td></tr>
              <tr><td>Pro</td><td>A structured template when the task has several parts</td><td>Packaging draft</td></tr>
              <tr><td>Enterprise tier</td><td>A fill-in template aimed at higher-stakes work, with room for limits and disclaimers</td><td>Packaging draft. Not an enterprise certificate.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note">Basic, Pro, and Enterprise are tiers of one family. They are hidden in the Shop until you approve the file, the license, and the price. Overlapping editions should not all be published as if they were unrelated products.</p>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap">
          <h2>Seven-day practice</h2>
          <p>From the draft essay on using AI as a practice tool rather than a substitute for the work. Each day is a short session. The performance claims in that essay are not repeated here. Publish the essay only after the sources are checked.</p>
          <ol class="days">
            <li><strong>Day 1. Intention.</strong> Name one learning goal and write what you already know.</li>
            <li><strong>Day 2. Retrieval.</strong> Quiz yourself first. Then compare with questions an AI tool generates.</li>
            <li><strong>Day 3. Questions.</strong> Ask two or three harder questions and work through them.</li>
            <li><strong>Day 4. Teach-back.</strong> Explain the topic in your own words, then let a tool critique the explanation.</li>
            <li><strong>Day 5. Practice.</strong> Take the hard part and work targeted problems, checking each one.</li>
            <li><strong>Day 6. Reflection.</strong> Record one thing you learned, one confusion, and any wrong answer from the tool.</li>
            <li><strong>Day 7. Next step.</strong> Set the following session. Note whether the thinking felt different.</li>
          </ol>
          <p class="tag">Draft</p>
          <p>A downloadable version of this sequence is a placeholder until the editorial pass is done.</p>
        </div>
      </div>
    </section>
"""
    research = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Responsible AI research</p>
        <h1>Research page</h1>
        <p class="lede">The study page opens in a new tab. It holds the invitation, ethics, sign-in, and consent. From there, the questionnaire opens in the same way this site will open it later.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div>
          <h2>What stays true when the study opens</h2>
          <ul class="links">
            <li>You can read this page without an account.</li>
            <li>Taking part will not require a purchase.</li>
            <li>Creating an account is not research consent.</li>
            <li>Consent will be a separate unchecked choice, with a version and a date.</li>
            <li>Answers are spoken or typed on the questionnaire page. The participant checks the transcript before it is saved.</li>
            <li>Do not put employer secrets, client names, or another person’s private data in an answer.</li>
          </ul>
          <p>Researcher contact: <a href="mailto:yaakov.preiger@think-21.com">yaakov.preiger@think-21.com</a></p>
        </div>
        <article class="card">
          <p class="tag">Preview</p>
          <h3>Open the study page</h3>
          <p>The button leaves this site and opens the study page. Sign-in and consent stay there. The questionnaire opens from that page.</p>
          <p><a href="https://intro-think-21.apps.ocp.7hrxw.sandbox880.opentlc.com/" target="_blank" rel="noopener">Open the study page</a></p>
        </article>
      </div>
    </section>
    <section class="band">
      <div class="section">
        <div class="wrap">
          <p><a href="{u['ai']}">Back to AI</a></p>
        </div>
      </div>
    </section>
"""
    iso = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Separate, and secondary</p>
        <h1>ISO</h1>
        <p class="lede">Quality, environmental, safety, and information-security work sits with VP Quality, not in the Think21 catalog. This page stays short on purpose.</p>
        <p class="note">vp-quality.com is not open yet. There is no button until that site is actually live. A Think21 account is not a VP Quality account.</p>
        <p>Older ISO essays can remain in <a href="{u['insights']}">Insights</a>. They are articles.</p>
      </div>
    </section>
"""
    shop = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Wix Stores</p>
        <h1>Shop</h1>
        <p class="lede">Checkout belongs to Wix Stores, on this same page, under this introduction. The rows below are the products to create there as hidden items. A hidden item has no public price. When you publish one, it should appear in this gallery and on its area page from the same Wix product.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <div class="sheet-wrap">
          <table class="sheet">
            <thead><tr><th>Create this product</th><th>Area</th><th>Show publicly</th></tr></thead>
            <tbody>
              <tr><td>BPM-360 handbook</td><td><a href="{u['bpm']}">BPM</a></td><td>No. Manuscript only.</td></tr>
              <tr><td>Production Readiness workbook</td><td><a href="{u['bpm']}">BPM</a></td><td>No. Placeholder.</td></tr>
              <tr><td>BPM-360 method cards</td><td><a href="{u['bpm']}">BPM</a></td><td>No. Placeholder.</td></tr>
              <tr><td>21 Prisms of Thinking</td><td><a href="{u['thinking']}">Thinking</a></td><td>No, until a retailer URL is real. Mark it as an external book, not a Wix download.</td></tr>
              <tr><td>21 Prisms companion workbook</td><td><a href="{u['thinking']}">Thinking</a></td><td>No. Placeholder.</td></tr>
              <tr><td>Reflection and decision journal</td><td><a href="{u['thinking']}">Thinking</a></td><td>No. Placeholder.</td></tr>
              <tr><td>21 Prisms card set</td><td><a href="{u['thinking']}">Thinking</a></td><td>No. Placeholder.</td></tr>
              <tr><td>21 Prisms team toolkit</td><td><a href="{u['thinking']}">Thinking</a></td><td>No. Placeholder.</td></tr>
              <tr><td>Master Prompt Architect, Basic</td><td><a href="{u['ai']}">AI</a></td><td>No. Draft.</td></tr>
              <tr><td>Master Prompt Architect, Pro</td><td><a href="{u['ai']}">AI</a></td><td>No. Draft.</td></tr>
              <tr><td>Master Prompt Architect, Enterprise</td><td><a href="{u['ai']}">AI</a></td><td>No. Draft. Do not claim a certification.</td></tr>
              <tr><td>Seven-day AI learning practice</td><td><a href="{u['ai']}">AI</a></td><td>No, until the essay is edited.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="note">The startup question list is free reading on <a href="{u['questions']}">Idea validation</a>. It is not a Shop item. Research is not a Shop item.</p>
      </div>
    </section>
"""
    about = f"""
    <section class="page-head">
      <div class="wrap">
        <p class="kicker">Yaakov Preiger</p>
        <h1>About</h1>
        <p class="lede">I work on architecture and systematic thinking, including S.I.T. and TRIZ. Think21 is where I publish BPM-360, 21 Prisms, the startup questions, and the AI drafts.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap split">
        <div>
          <p>This site is my own material. It is not a consulting menu and not an employer’s service list. ISO work is intentionally the small page.</p>
          <p>If you create an account, or you send the draft research form, I receive a notice at <a href="mailto:yaakov.preiger@think-21.com">yaakov.preiger@think-21.com</a>. Sign-in is Google first. A LinkedIn login is not connected yet. A Google account can be Gmail or another address on Google.</p>
          <div class="contact-row">
            <a href="mailto:yaakov.preiger@think-21.com">yaakov.preiger@think-21.com</a>
            <a href="{u['linkedin']}">LinkedIn</a>
            <a href="tel:+972544872442">+972 54 487 2442</a>
          </div>
        </div>
        <article class="card">
          <h3>Start here</h3>
          <ul class="links">
            <li><a href="{u['bpm']}">BPM-360</a></li>
            <li><a href="{u['thinking']}">21 Prisms</a></li>
            <li><a href="{u['startups']}">Startup questions</a></li>
            <li><a href="{u['ai']}">AI drafts</a></li>
            <li><a href="{u['research']}">Research page</a></li>
            <li><a href="{u['shop']}">Shop</a></li>
          </ul>
        </article>
      </div>
    </section>
"""
    return {
        "home": ("Think21", "BPM-360, 21 Prisms, prompt drafts, and the startup questions already on this site.", home, "home"),
        "thinking": ("Thinking | Think21", "21 Prisms of Thinking: three stages, twenty-one prisms, and the files that are not packaged yet.", thinking, "thinking"),
        "bpm": ("BPM | Think21", "BPM-360 handbook, ten aspects, and the production-readiness gate. No consulting offer.", bpm, "bpm"),
        "startups": ("Startups | Think21", "The idea-validation questions already published on Think21.", startups, "startups"),
        "questions": ("Idea validation | Think21", "The existing Think21 question list for testing an idea.", questions, "startups"),
        "ai": ("AI | Think21", "Master Prompt Architect drafts, a seven-day practice, and the research page.", ai, "ai"),
        "research": ("Research | Think21", "Responsible AI research page. The approved questionnaire is not open.", research, "ai"),
        "iso": ("ISO | Think21", "ISO work is separate from the Think21 catalog and is not a product on this site.", iso, "iso"),
        "shop": ("Shop | Think21", "Hidden Wix Stores products for BPM-360, 21 Prisms, and the prompt drafts.", shop, "shop"),
        "about": ("About | Think21", "Yaakov Preiger. BPM-360, 21 Prisms, and the Think21 drafts.", about, "about"),
    }
