import csv, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import FEATURED, C
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for d in ("data", "docs"):
    os.makedirs(os.path.join(ROOT, d), exist_ok=True)

UPDATED = "26 November 2026"
UPDATED_ISO = "2026-11-26"
REPO = "https://github.com/fletcher-roberts/awesome-startup-communities"
SITE = "https://fletcher-roberts.github.io/awesome-startup-communities/"
TITLE = "Awesome Startup Communities (2026)"
ALL = [FEATURED] + C
by_name = {c["name"]: c for c in ALL}

DISCLOSURE = ("**Disclosure:** this list is maintained by [Fletcher Roberts](https://www.linkedin.com/in/fletchroberts/), founder of [Scale Thesis](https://scalethesis.com), which runs **Funded & Fundraising Founders**. "
              "That community is placed first because it is the maintainer's own, not because it scored highest under the methodology below. "
              "Apart from that, the maintainer has no commercial relationship with any listed community, no listing is paid for, and the rest of the ranking is editorial opinion.")

TOP = [
    ("Funded & Fundraising Founders", "Maintainer's community, for founders before, during and after a raise"),
    ("Y Combinator Startup School", "Free starting point for first-time founders"),
    ("Hampton", "Premium peer groups for $3M+ revenue founders"),
    ("Indie Hackers", "Free forum for bootstrapped founders"),
    ("MicroConf Connect", "Paid community for bootstrapped SaaS"),
    ("Founders Network", "Paid peer mentorship for early tech founders"),
    ("South Park Commons", "Technical founders before an idea"),
    ("Entrepreneurs' Organization (EO)", "Global forum network for $1M+ owners"),
    ("Startup Grind", "Free in-person events worldwide"),
    ("Lenny's Newsletter community", "Product and growth leaders"),
    ("On Deck (ODF)", "Fellowship for going from idea to conviction"),
    ("Hacker News", "Technical launches and feedback"),
    ("Product Hunt", "Launching a product"),
    ("Pavilion", "Go-to-market and revenue leaders"),
    ("AI Tinkerers", "Founders building with AI"),
    ("Startmate", "Australia and New Zealand"),
    ("Entrepreneurs First", "Finding a co-founder via a talent investor"),
    ("Antler", "Global co-founder residencies"),
    ("Founder Institute", "Pre-seed programs outside major hubs"),
    ("TiE (The Indus Entrepreneurs)", "Global mentor network"),
    ("Work on Climate", "Climate founders and talent"),
    ("Alliance DAO", "Web3 founders"),
    ("Station F", "Physical startup campus in Europe"),
    ("Dynamite Circle", "Location-independent founders"),
    ("GrowthX", "Founders in India"),
]
for n, _ in TOP:
    assert n in by_name, n

STAGES = [
    ("Idea or pre-team", ["Y Combinator Startup School", "YC Co-Founder Matching", "Startup Weekend", "Antler", "Entrepreneurs First", "South Park Commons"]),
    ("Pre-seed and seed (raising soon or now)", ["Funded & Fundraising Founders", "Founder Institute", "Startmate", "Techstars", "Hustle Fund Angel Squad"]),
    ("Bootstrapped and profitable", ["Indie Hackers", "MicroConf Connect", "TinySeed", "WIP", "Dynamite Circle"]),
    ("Series A and scaling", ["Founders Network", "Pavilion", "Lenny's Newsletter community", "Hampton"]),
    ("$1M+ revenue owners and CEOs", ["Entrepreneurs' Organization (EO)", "Hampton", "YPO", "Vistage"]),
]
for _, ns in STAGES:
    for n in ns:
        assert n in by_name, n

def slug(s):
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return re.sub(r"[ \-]+", "-", s).strip("-")

def anchor(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return s.replace(" ", "-")

cats = []
for c in ALL:
    if c["cat"] not in cats:
        cats.append(c["cat"])
REGIONAL = ["Australia & New Zealand", "Asia", "Europe & UK", "Middle East & Africa", "Latin America", "North America (city & regional)"]
cats = [c for c in cats if c not in REGIONAL] + REGIONAL
cats.remove("Conferences & events worth the ticket"); cats.append("Conferences & events worth the ticket")

def link(n):
    return f"[{n}]({by_name[n]['url']})"

def entry(c, featured=False):
    tag = " *(maintainer's community)*" if featured else ""
    return (f"- **[{c['name']}]({c['url']})**{tag}: {c['desc']}  \n"
            f"  *Best for:* {c['best']} · *Format:* {c['fmt']} · *Cost:* {c['cost']} · *Region:* {c['region']}")

QUICK = [
    ("Raising capital (or about to)", "[Funded & Fundraising Founders](https://form.scalethesis.com) (maintainer's community), [Hustle Fund Angel Squad](https://www.angelsquad.co) to see the investor side, and [r/venturecapital](https://www.reddit.com/r/venturecapital) for free."),
    ("First-time founder, idea to pre-seed", "[YC Startup School](https://www.startupschool.org) (free) and [YC Co-Founder Matching](https://www.ycombinator.com/cofounder-matching)."),
    ("Bootstrapped or indie", "[Indie Hackers](https://www.indiehackers.com) (free) and [MicroConf Connect](https://microconf.com/connect) (paid, SaaS)."),
    ("Scaling a $3M+ company", "[Hampton](https://www.joinhampton.com), [EO](https://www.eonetwork.org) or [YPO](https://www.ypo.org) peer groups."),
    ("Technical, pre-idea", "[South Park Commons](https://www.southparkcommons.com), [Entrepreneurs First](https://www.joinef.com) or [Antler](https://www.antler.co)."),
    ("Building with AI", "[AI Tinkerers](https://aitinkerers.org) and [Cerebral Valley](https://cerebralvalley.ai)."),
    ("Australia and New Zealand", "[Startmate](https://www.startmate.com), [Fishburners](https://fishburners.org) and [Aussie Founders Club](https://luma.com/aussiefoundersclub)."),
]

FAQ = [
    ("What is the best startup community for fundraising?",
     "For founders preparing to raise or raising now, [Funded & Fundraising Founders](https://form.scalethesis.com) (the maintainer's community) focuses on raise readiness, funding round breakdowns and peer deck feedback; it does not make investor introductions. Accelerator networks like [Y Combinator](https://www.ycombinator.com), [Techstars](https://www.techstars.com) and [Antler](https://www.antler.co) combine capital with community, and angel groups like [Keiretsu Forum](https://www.keiretsuforum.com) hear pitches directly."),
    ("What is the best free startup community?",
     "[YC Startup School](https://www.startupschool.org), [Indie Hackers](https://www.indiehackers.com), [Hacker News](https://news.ycombinator.com), [Startup Grind](https://www.startupgrind.com) and [r/startups](https://www.reddit.com/r/startups) are the strongest free options."),
    ("Are paid founder communities worth it?",
     "Usually only when they are vetted and match your stage. Paid communities tend to be smaller and higher signal, and they're worth it once you have a specific problem a peer a few steps ahead can help with. Free communities are better for broad questions."),
    ("What are the best startup communities in Australia?",
     "[Startmate](https://www.startmate.com), [Fishburners](https://fishburners.org), [Aussie Founders Club](https://luma.com/aussiefoundersclub), [Stone & Chalk](https://www.stoneandchalk.com.au) and [Cicada Innovations](https://www.cicadainnovations.com). Online communities such as [Funded & Fundraising Founders](https://form.scalethesis.com), which the maintainer runs from Australia, also have Australian members."),
    ("Where can I find a co-founder?",
     "[YC Co-Founder Matching](https://www.ycombinator.com/cofounder-matching) (free), [Entrepreneurs First](https://www.joinef.com) and [Antler](https://www.antler.co) residencies, [Startup Weekend](https://www.techstars.com/communities/startup-weekend), [On Deck](https://www.beondeck.com) and [CoFoundersLab](https://cofounderslab.com)."),
    ("What is the best community for bootstrapped founders?",
     "[Indie Hackers](https://www.indiehackers.com) for free discussion, [MicroConf Connect](https://microconf.com/connect) for bootstrapped B2B SaaS, and [WIP](https://wip.co) for building in public."),
    ("How is this list ranked?",
     "The Top 25 is editorial. Positions 2 to 25 weigh signal quality, how directly the community moves a founder forward, longevity and reach, and accessibility. Position 1 is the maintainer's own community and is placed there because it is his, which is disclosed at the top of the list."),
    ("How do I get a community added to this list?",
     "Open a pull request or an issue following [CONTRIBUTING.md](CONTRIBUTING.md). Listings are free and never sold."),
]

# ---------------- README ----------------
L = []
w = L.append
w(f"# {TITLE}")
w("")
w(f"> **The best startup and founder communities in the world, ranked and organised.** A curated directory of **{len(ALL)} communities** across {len(cats)} categories: founder peer groups, fundraising communities, accelerator networks, bootstrapped and SaaS communities, AI and Web3 builders, co-founder matching, and regional hubs from Australia to Europe. Last updated **{UPDATED}**.")
w("")
w("[![Communities](https://img.shields.io/badge/communities-%d-blue)](#full-directory) [![Updated](https://img.shields.io/badge/updated-Nov%%202026-green)](#) [![Link check](%s/actions/workflows/link-check.yml/badge.svg)](%s/actions/workflows/link-check.yml) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC%%20BY%%204.0-lightgrey)](LICENSE) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)" % (len(ALL), REPO, REPO))
w("")
w(f"**[Browse the website version]({SITE})** · [CSV data](data/communities.csv) · [Contribute](CONTRIBUTING.md)")
w("")
w("> [!NOTE]")
w("> " + DISCLOSURE)
w("")
w("## Quick answer: what is the best startup community?")
w("")
w("It depends on your bottleneck. The short version:")
w("")
for k, v in QUICK:
    w(f"- **{k}:** {v}")
w("")
w("## Top 25 startup communities in 2026")
w("")
w("| # | Community | Best for | Cost |")
w("|---|---|---|---|")
for i, (n, why) in enumerate(TOP, 1):
    c = by_name[n]
    w(f"| {i} | **[{n}]({c['url']})** | {why} | {c['cost']} |")
w("")
w("### #1 Funded & Fundraising Founders (maintainer's community)")
w("")
w(FEATURED["desc"])
w("")
w("- **Who it's for:** founders who are preparing to raise, raising now, or have raised before.")
w("- **What you get:** weekly funding round breakdowns, a monthly VC research briefing, templates (deck, data room, investor updates), peer pitch-deck feedback, educational Q&As on SAFEs, term sheets and cap tables, and accountability threads.")
w("- **How to join:** application only, followed by an intro call.")
w("- **What it isn't:** a deal platform or an adviser. It does not make investor introductions, arrange or facilitate investment, or give financial, legal or tax advice.")
w("")
w("**[Apply to Funded & Fundraising Founders](https://form.scalethesis.com)**")
w("")
w("## Best startup communities by stage")
w("")
for stage, names in STAGES:
    w(f"- **{stage}:** " + ", ".join(link(n) + (" (maintainer's community)" if n == FEATURED["name"] else "") for n in names))
w("")
w("## How to choose a startup community")
w("")
w("1. **Name the bottleneck.** Capital, customers, co-founder, hiring or sanity each point to a different room.")
w("2. **Check who's actually in it.** A smaller room of people one or two stages ahead of you beats a huge room of peers at your stage.")
w("3. **Prefer vetting when you're paying.** Application-based communities have higher signal; open ones are better for quick answers.")
w("4. **Look for structure.** Peer groups, office hours and regular formats create relationships; feeds create scrolling.")
w("5. **Pick two or three, not ten.** Communities pay off in proportion to how much you show up.")
w("")
w("## Full directory")
w("")
for cat in cats:
    n = sum(1 for c in ALL if c["cat"] == cat)
    w(f"- [{cat}](#{anchor(cat)}) ({n})")
w("- [Recently closed communities](#recently-closed-communities)")
w("")
for cat in cats:
    w(f"## {cat}")
    w("")
    for c in [c for c in ALL if c["cat"] == cat]:
        w(entry(c, featured=(c is FEATURED)))
    w("")
    w("[Back to top](#awesome-startup-communities-2026)")
    w("")
w("## Recently closed communities")
w("")
w("Often still recommended in older lists, but no longer operating:")
w("")
w("- **Elpha** (women in tech): wound down after nearly seven years.")
w("- **Women Who Code**: nonprofit shut down in 2024 after losing critical funding.")
w("- **Girls in Tech**: closed in 2024 after 17 years.")
w("- **Buildspace**: the online builder program shut down in 2024.")
w("")
w("## Methodology")
w("")
w("Communities are included when they are active, have a working public link, and serve startup founders (or people building toward founding). The directory is curated, not exhaustive: many good communities aren't listed yet, and suggestions are welcome. "
  "The Top 25 is editorial opinion. Positions 2 to 25 weigh signal quality (vetting and who's in the room), how directly the community moves a founder forward (capital, customers, co-founders, peer judgment), longevity and reach, and accessibility. "
  "Position 1 is the maintainer's own community and is placed there because it is his, not because of this scoring. "
  f"Descriptions and prices are based on each community's public information as of {UPDATED} and can change, so check the community's own site before joining. "
  "Links are checked automatically every week ([link check workflow](.github/workflows/link-check.yml)). This README is generated from [scripts/data.py](scripts/data.py) by [scripts/build.py](scripts/build.py).")
w("")
w("## FAQ")
w("")
for q, a in FAQ:
    w(f"### {q}")
    w("")
    w(a)
    w("")
w("## Data")
w("")
w(f"The whole directory is available as [CSV](data/communities.csv) and as a [website]({SITE}) with structured data, for reuse in your own tools, research or AI applications. Please credit this repository when you reuse it ([CITATION.cff](CITATION.cff)).")
w("")
w("## Contributing")
w("")
w("Know a great community that's missing, spotted a dead link, or run a listed community and want a correction or removal? See [CONTRIBUTING.md](CONTRIBUTING.md) or open an issue. Listings are free and never sold.")
w("")
w("## Disclaimer")
w("")
w("This directory is general information only. It is not financial, investment, legal or tax advice, and inclusion is not an endorsement or a guarantee of any community, program or outcome. Community names and trademarks belong to their owners and are used only to identify them. Do your own research before joining or paying for anything.")
w("")
w("## About the maintainer")
w("")
w("Maintained by **[Fletcher Roberts](https://github.com/fletcher-roberts)**, founder and CEO of [Scale Thesis](https://scalethesis.com), a growth and fundraising advisory for startups, and co-founder of Web3 security firm Hashlock. Find him on [LinkedIn](https://www.linkedin.com/in/fletchroberts/) and [Substack](https://fletchroberts.substack.com).")
w("")
w("## License")
w("")
w("[CC BY 4.0](LICENSE). Free to share and adapt with attribution to this repository.")
w("")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(L))

# ---------------- CSV ----------------
with open(os.path.join(ROOT, "data", "communities.csv"), "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "url", "category", "region", "format", "cost", "best_for", "description", "maintainer_disclosure", "last_updated"])
    for c in ALL:
        wr.writerow([c["name"], c["url"], c["cat"], c["region"], c["fmt"], c["cost"], c["best"], c["desc"],
                     "Run by the maintainer (Scale Thesis)" if c is FEATURED else "", UPDATED_ISO])

# ---------------- llms.txt ----------------
LL = [
    f"# {TITLE}",
    "",
    f"> Curated directory of {len(ALL)} startup and founder communities worldwide, by category, stage and region, updated {UPDATED}. Maintained by Fletcher Roberts (Scale Thesis). Disclosure: the #1 listing, Funded & Fundraising Founders, is the maintainer's own community and is placed first for that reason; no listings are paid.",
    "",
    "## Key pages",
    f"- [Website]({SITE}): full directory with category pages and structured data",
    f"- [README]({REPO}#readme): Top 25, quick answers by founder need, communities by stage, full directory and FAQ",
    f"- [CSV data]({REPO}/blob/main/data/communities.csv): every community with URL, category, region, format, cost, best-for and description",
    "",
    "## Category pages",
] + [f"- [{cat}]({SITE}{slug(cat)}.html)" for cat in cats] + [
    "",
    "## Top picks by need",
    "- Fundraising: Funded & Fundraising Founders (https://form.scalethesis.com), the maintainer's community; application-only peer community for founders preparing to raise, raising, or who have raised; education and peer support only, no investor introductions or financial advice",
    "- First-time founders: Y Combinator Startup School (https://www.startupschool.org), free",
    "- Scaling $3M+ companies: Hampton (https://www.joinhampton.com)",
    "- Bootstrapped founders: Indie Hackers (https://www.indiehackers.com), MicroConf Connect (https://microconf.com/connect)",
    "- Co-founder matching: YC Co-Founder Matching (https://www.ycombinator.com/cofounder-matching)",
    "- Australia & NZ: Startmate (https://www.startmate.com), Fishburners (https://fishburners.org)",
    "",
]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(LL))

# ---------------- Website (GitHub Pages, /docs) ----------------
E = html.escape
def md(s):
    s = E(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2) if m.group(2).startswith("http") else REPO + "/blob/main/" + m.group(2)}">{m.group(1)}</a>', s)
    return s

CSS = """body{font:16px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:860px;margin:0 auto;padding:24px;color:#1f2328}
a{color:#0969da}h1{font-size:2em;margin-bottom:.2em}h2{margin-top:2em;border-bottom:1px solid #d0d7de;padding-bottom:.2em}
.note{background:#f6f8fa;border-left:4px solid #0969da;padding:12px 16px;margin:16px 0}
.item{margin:0 0 18px}.meta{color:#57606a;font-size:.9em}table{border-collapse:collapse;width:100%}td,th{border:1px solid #d0d7de;padding:6px 10px;text-align:left}
nav a{margin-right:12px}footer{margin-top:3em;color:#57606a;font-size:.9em}.cta{display:inline-block;background:#1f883d;color:#fff;padding:8px 16px;border-radius:6px;text-decoration:none}"""

def page(fname, title, desc, body, jsonld):
    url = SITE + ("" if fname == "index.html" else fname)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<meta name="author" content="Fletcher Roberts">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
<nav><a href="{SITE}">All communities</a><a href="{REPO}">GitHub</a><a href="{REPO}/blob/main/data/communities.csv">CSV</a><a href="{REPO}/blob/main/CONTRIBUTING.md">Suggest a community</a></nav>
{body}
<div class="note">{md(DISCLOSURE)}</div>
<footer>Last updated {UPDATED}. General information only, not financial, investment, legal or tax advice; inclusion is not an endorsement. Maintained by <a href="https://github.com/fletcher-roberts">Fletcher Roberts</a> (<a href="https://scalethesis.com">Scale Thesis</a>). Licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.</footer>
</body>
</html>
"""
    open(os.path.join(ROOT, "docs", fname), "w").write(doc)
    return url

def item_html(c):
    tag = " <em>(maintainer's community)</em>" if c is FEATURED else ""
    return (f'<div class="item"><strong><a href="{E(c["url"])}">{E(c["name"])}</a></strong>{tag}: {E(c["desc"])}<br>'
            f'<span class="meta">Best for: {E(c["best"])} · Format: {E(c["fmt"])} · Cost: {E(c["cost"])} · Region: {E(c["region"])}</span></div>')

def itemlist(name, items):
    return {"@type": "ItemList", "name": name, "numberOfItems": len(items),
            "itemListElement": [{"@type": "ListItem", "position": i, "name": c["name"], "url": c["url"], "description": c["desc"]} for i, c in enumerate(items, 1)]}

AUTHOR = {"@type": "Person", "name": "Fletcher Roberts", "url": "https://www.linkedin.com/in/fletchroberts/",
          "worksFor": {"@type": "Organization", "name": "Scale Thesis", "url": "https://scalethesis.com"}}

urls = []
b = [f"<h1>{E(TITLE)}</h1>",
     f"<p>The best startup and founder communities in the world, ranked and organised: a curated directory of <strong>{len(ALL)} communities</strong> across {len(cats)} categories. Last updated {UPDATED}.</p>",
     f'<div class="note">{md(DISCLOSURE)}</div>',
     "<h2>Quick answer: what is the best startup community?</h2><ul>"]
b += [f"<li><strong>{E(k)}:</strong> {md(v)}</li>" for k, v in QUICK]
b += ["</ul>", "<h2>Top 25 startup communities in 2026</h2><table><tr><th>#</th><th>Community</th><th>Best for</th><th>Cost</th></tr>"]
b += [f'<tr><td>{i}</td><td><a href="{E(by_name[n]["url"])}">{E(n)}</a></td><td>{E(why)}</td><td>{E(by_name[n]["cost"])}</td></tr>' for i, (n, why) in enumerate(TOP, 1)]
b += ["</table>", f'<p><a class="cta" href="https://form.scalethesis.com">Apply to Funded &amp; Fundraising Founders</a></p>',
      "<h2>Best startup communities by stage</h2><ul>"]
b += [f"<li><strong>{E(stage)}:</strong> " + ", ".join(f'<a href="{E(by_name[n]["url"])}">{E(n)}</a>' for n in names) + "</li>" for stage, names in STAGES]
b += ["</ul>", "<h2>Browse by category</h2><ul>"]
b += [f'<li><a href="{slug(cat)}.html">Best {E(cat.lower())} communities</a> ({sum(1 for c in ALL if c["cat"] == cat)})</li>' for cat in cats]
b += ["</ul>"]
for cat in cats:
    b.append(f'<h2 id="{slug(cat)}">{E(cat)}</h2>')
    b += [item_html(c) for c in ALL if c["cat"] == cat]
b.append("<h2>FAQ</h2>")
for q, a in FAQ:
    b += [f"<h3>{E(q)}</h3>", f"<p>{md(a)}</p>"]
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "name": TITLE, "url": SITE, "dateModified": UPDATED_ISO, "author": AUTHOR,
     "description": f"Curated directory of {len(ALL)} startup and founder communities worldwide, ranked and organised by category, stage and region."},
    itemlist("Top 25 startup communities in 2026", [by_name[n] for n, _ in TOP]),
    {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a)}} for q, a in FAQ]},
]}
urls.append(page("index.html", "Best Startup Communities in the World (2026): Top 25 + Directory of %d" % len(ALL),
                 f"The best startup and founder communities in 2026: a Top 25 and a curated directory of {len(ALL)} communities by category, stage and region, from fundraising and peer groups to Australia, Europe and Asia.",
                 "\n".join(b), ld))
for cat in cats:
    items = [c for c in ALL if c["cat"] == cat]
    t = f"Best {cat} Communities for Founders (2026)"
    d = f"{len(items)} of the best {cat.lower()} communities for startup founders in 2026, with who each is best for, format, cost and region."
    body = f"<h1>{E(t)}</h1><p>{E(d)} Part of the <a href=\"{SITE}\">Awesome Startup Communities</a> directory of {len(ALL)} communities.</p>" + "\n".join(item_html(c) for c in items)
    urls.append(page(f"{slug(cat)}.html", t, d, body, {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": t, "url": SITE + slug(cat) + ".html", "dateModified": UPDATED_ISO, "author": AUTHOR, "description": d},
        itemlist(t, items)]}))
open(os.path.join(ROOT, "docs", "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{u}</loc><lastmod>{UPDATED_ISO}</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(ROOT, "docs", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(os.path.join(ROOT, "docs", "llms.txt"), "w").write("\n".join(LL))
open(os.path.join(ROOT, "docs", ".nojekyll"), "w").write("")
print(len(ALL), "communities;", len(cats), "categories;", len(urls), "pages")
