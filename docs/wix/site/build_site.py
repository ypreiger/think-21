#!/usr/bin/env python3
"""Write preview pages and Wix embed snippets from one source."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSS = (ROOT / "css" / "think21.css").read_text()
EMBED_DIR = ROOT.parent / "embed"

LOGO = "https://static.wixstatic.com/media/7bf4a3_87c3f8d5734f4118ab2df3ac98df9ffa~mv2.png"
FONT = "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&family=Spinnaker&display=swap"

PREVIEW = {
    "home": "index.html",
    "thinking": "thinking.html",
    "bpm": "bpm.html",
    "startups": "startups.html",
    "ai": "ai.html",
    "iso": "iso.html",
    "shop": "shop.html",
    "about": "about.html",
    "questions": "idea-validation.html",
    "research": "research.html",
    "insights": "https://www.think-21.com/blog",
    "post_triz": "https://www.think-21.com/post/contradiction-the-core-of-triz-and-systemic-innovative-thinking",
    "post_methods": "https://www.think-21.com/post/triz-methods-for-resolving-systemic-contradictions",
    "post_whys": "https://www.think-21.com/post/five-whys-the-power-of-rca-in-architectural-assessment-and-pfmea",
    "linkedin": "https://www.linkedin.com/in/yaakovpreiger/",
}

LIVE = {
    "home": "https://www.think-21.com/",
    "thinking": "https://www.think-21.com/thinking",
    "bpm": "https://www.think-21.com/bpm",
    "startups": "https://www.think-21.com/startups",
    "ai": "https://www.think-21.com/ai",
    "iso": "https://www.think-21.com/iso",
    "shop": "https://www.think-21.com/shop",
    "about": "https://www.think-21.com/team",
    "questions": "https://www.think-21.com/idea-validation",
    "research": "https://www.think-21.com/research",
    "insights": "https://www.think-21.com/blog",
    "post_triz": PREVIEW["post_triz"],
    "post_methods": PREVIEW["post_methods"],
    "post_whys": PREVIEW["post_whys"],
    "linkedin": PREVIEW["linkedin"],
}

NAV = [
    ("thinking", "Thinking"),
    ("bpm", "BPM"),
    ("startups", "Startups"),
    ("ai", "AI"),
    ("iso", "ISO"),
    ("insights", "Insights"),
    ("shop", "Shop"),
    ("about", "About"),
]

QUESTIONS = [
    (
        "Idea validation questions",
        [
            "What does the company do?",
            "What is unique about the company?",
            "What problem does your product solve / market need does it fill?",
            "How big is the market opportunity?",
            "Where are you headquartered?",
            "How big can the company get?",
            "What is the actual addressable market?",
            "What is the size of the market that will buy your product or service?",
            "What percentage of the market do you plan to get over what period of time?",
            "How did you arrive at the sales of your industry and its growth rate?",
            "Why does your company have high growth potential?",
            "Can you name somebody who would benefit from your product or service?",
            "Who are the founders and key team members?",
            "What relevant domain experience does the team have?",
            "What key additions to the team are needed in the short term?",
            "Why is the team uniquely capable of executing the company’s business plan?",
            "How many employees do you have?",
            "What motivates the founders?",
            "Do you have a mentor or industry advisor that you can call on?",
            "How do you plan to scale the team in the next 12 months?",
            "Who are your design partners and why?",
            "Who are your advisory board — business, domain experts — and why?",
        ],
    ),
    (
        "Products, services and roadmap",
        [
            "What problem / market need does your product solve?",
            "What is the main contradiction you address?",
            "Why do users care about your product or service?",
            "How have others attempted to solve this problem before, and why did their solutions succeed or fail?",
            "Does your idea already exist in the same way you were going to create it?",
            "How many specific benefits for your product or idea can you list?",
            "Can you state, in clear language, the key features of your product or service?",
            "What are the key differentiated features of your product or service?",
            "What are the major product milestones?",
            "What are the two or three key features you plan to add on each milestone?",
            "What have you learned from early versions of the product or service?",
            "Provide a demonstration of the product or service.",
            "Do you have access to the various resources you need to launch a business?",
            "Do you have distributors or partners to help you scale your business?",
            "What would it take to build a minimum viable product to test the market?",
            "Can you produce the actual product yourself, or do you have a partner who can?",
            "What key intellectual property does the company have (patents, patents pending, copyrights, trade secrets, trademarks, domain names)?",
            "What comfort do you have that the company’s intellectual property does not violate the rights of a third party?",
            "How was the company’s intellectual property developed?",
            "Would any prior employers of a team member have a potential claim to the company’s intellectual property?",
            "Have you done a SWOT analysis?",
            "Who are your potential competitors?",
            "What gives your company a competitive advantage?",
            "What key features does your product or service have that others will have a hard time copying?",
            "What advantages does your competition have over you?",
            "Compared to your competition, how do you compete with respect to price, features, and performance?",
            "What are the barriers to entry?",
        ],
    ),
    (
        "Marketing and customer acquisition",
        [
            "How does the company market or plan to market its products or services?",
            "What is the company’s PR strategy?",
            "What is the company’s social media strategy?",
            "What is the cost of a customer acquisition?",
            "What is the projected lifetime value of a customer?",
            "What advertising will you be doing?",
            "What is the typical sales cycle between initial customer contact and closing of a sale?",
            "What early traction has the company gotten (sales, traffic to the company’s website, app downloads, etc., as relevant).",
            "How can the early traction be accelerated?",
            "What has been the principal reasons for the early traction?",
            "Have you reached out to potential customers for feedback?",
            "Can you set up a landing page and encourage interested people to sign up for more information?",
            "Can you get paying customers from your target market to pre-order based on a blueprint or mock-up?",
        ],
    ),
    (
        "Risks, assumptions, and return",
        [
            "What do you see are the principal risks to the business?",
            "What legal risks do you have?",
            "Do you have any regulatory risks?",
            "Are there any product liability risks?",
            "Describe your assumptions used for the solution feasibility.",
            "Describe your assumptions used for market estimation.",
            "What will it take to break even or make a profit?",
            "How can investors in your idea make a profit?",
            "What is the likely exit – IPO or M&A?",
        ],
    ),
]


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def question_html() -> str:
    parts = []
    for title, items in QUESTIONS:
        lis = "\n".join(f"          <li>{esc(item)}</li>" for item in items)
        parts.append(
            f"""    <section class="section">
      <div class="wrap">
        <h2>{esc(title)}</h2>
        <ol class="questions">
{lis}
        </ol>
      </div>
    </section>"""
        )
    return "\n".join(parts)


def pages(url):
    from page_bodies import build_pages
    return build_pages(url, question_html())


def header(url, current: str) -> str:
    links = []
    for key, label in NAV:
        current_attr = ' aria-current="page"' if key == current else ""
        links.append(f'        <a href="{url[key]}"{current_attr}>{label}</a>')
    return f"""
  <header class="site-header">
    <a class="brand" href="{url['home']}">
      <img src="{LOGO}" alt="" width="48" height="48">
      <span>Think21</span>
    </a>
    <input class="nav-toggle" id="nav-toggle" type="checkbox">
    <label class="nav-toggle-label" for="nav-toggle">Menu</label>
    <nav class="nav" aria-label="Primary">
{chr(10).join(links)}
    </nav>
  </header>"""


def footer(url) -> str:
    return f"""
  <footer class="site-footer">
    <div class="wrap">
      <p>Yaakov Preiger · <a href="{url['linkedin']}">LinkedIn</a> · <a href="tel:+972544872442">+972 54 487 2442</a></p>
      <p>© 2026 Think21</p>
    </div>
  </footer>"""


def write_preview(key, title, description, body, current):
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="stylesheet" href="{FONT}">
  <link rel="stylesheet" href="css/think21.css">
</head>
<body>
{header(PREVIEW, current)}
  <main>
{body}
  </main>
{footer(PREVIEW)}
</body>
</html>
"""
    (ROOT / PREVIEW[key]).write_text(doc)


HEIGHTS = {
    "home": (2550, 4200),
    "thinking": (2000, 3500),
    "bpm": (2550, 4000),
    "startups": (1400, 2300),
    "questions": (5700, 8700),
    "ai": (1950, 3200),
    "research": (1100, 1900),
    "iso": (500, 700),
    "shop": (1250, 2100),
    "about": (850, 1400),
}


def write_embed(key, body):
    desktop, mobile = HEIGHTS[key]
    snippet = f"""<!-- Paste this entire file into Wix: Add Elements, Embed Code, Popular Embeds, Embed HTML, Enter Code. Desktop height {desktop}px. Mobile height {mobile}px. -->
<link rel="stylesheet" href="{FONT}">
<style>
{CSS}
</style>
<div class="t21-root">
{body}
</div>
"""
    EMBED_DIR.mkdir(parents=True, exist_ok=True)
    name = {
        "home": "home.html",
        "questions": "idea-validation.html",
    }.get(key, f"{key}.html")
    (EMBED_DIR / name).write_text(snippet)


def main():
    preview_pages = pages(PREVIEW)
    live_pages = pages(LIVE)
    for key, (title, description, body, current) in preview_pages.items():
        write_preview(key, title, description, body, current)
    for key, (_, _, body, _) in live_pages.items():
        write_embed(key, body)
    print(f"Wrote preview pages in {ROOT}")
    print(f"Wrote embed snippets in {EMBED_DIR}")


if __name__ == "__main__":
    main()
