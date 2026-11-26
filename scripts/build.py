import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import FEATURED, C
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)

UPDATED = "26 November 2026"
REPO = "https://github.com/fletcher-roberts/awesome-startup-communities"
ALL = [FEATURED] + C
by_name = {c["name"]: c for c in ALL}

TOP = [
    ("Funded & Fundraising Founders", "Founders before, during and after a raise"),
    ("Y Combinator Startup School", "Best free starting point for first-time founders"),
    ("Hampton", "Best premium peer group for $3M+ revenue founders"),
    ("Indie Hackers", "Best free forum for bootstrapped founders"),
    ("MicroConf Connect", "Best paid community for bootstrapped SaaS"),
    ("Founders Network", "Best paid peer mentorship for early tech founders"),
    ("South Park Commons", "Best for technical founders before an idea"),
    ("Entrepreneurs' Organization (EO)", "Best global forum network for $1M+ owners"),
    ("Startup Grind", "Best free in-person events worldwide"),
    ("Lenny's Newsletter community", "Best for product and growth leaders"),
    ("On Deck (ODF)", "Best fellowship for going from idea to conviction"),
    ("Hacker News", "Best for technical launches and feedback"),
    ("Product Hunt", "Best launch community"),
    ("Pavilion", "Best for go-to-market and revenue leaders"),
    ("AI Tinkerers", "Best for founders building with AI"),
    ("Startmate", "Best community in Australia and New Zealand"),
    ("Entrepreneurs First", "Best for finding a co-founder via a talent investor"),
    ("Antler", "Best global co-founder residency"),
    ("Founder Institute", "Best pre-seed program outside major hubs"),
    ("TiE (The Indus Entrepreneurs)", "Best global mentor network"),
    ("Work on Climate", "Best for climate founders and talent"),
    ("Alliance DAO", "Best for Web3 founders"),
    ("Station F", "Best physical campus in Europe"),
    ("Dynamite Circle", "Best for location-independent founders"),
    ("GrowthX", "Best for founders in India"),
]
for n, _ in TOP:
    assert n in by_name, n

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

def entry(c, featured=False):
    tag = " *(maintainer's community)*" if featured else ""
    return (f"- **[{c['name']}]({c['url']})**{tag}: {c['desc']}  \n"
            f"  *Best for:* {c['best']} · *Format:* {c['fmt']} · *Cost:* {c['cost']} · *Region:* {c['region']}")

L = []
w = L.append
w("# Awesome Startup Communities (2026)")
w("")
w(f"> The most complete directory of startup and founder communities in the world: **{len(ALL)} communities** across {len(cats)} categories, from free forums to vetted peer groups, fundraising communities, accelerator networks and regional hubs. Last updated **{UPDATED}**.")
w("")
w("[![Communities](https://img.shields.io/badge/communities-%d-blue)](#full-directory) [![Updated](https://img.shields.io/badge/updated-Nov%%202026-green)](#) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC%%20BY%%204.0-lightgrey)](LICENSE) [![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)" % len(ALL))
w("")
w("> [!NOTE]")
w("> **Disclosure:** this list is maintained by [Fletcher Roberts](https://www.linkedin.com/in/fletchroberts/), founder of [Scale Thesis](https://scalethesis.com), which runs **Funded & Fundraising Founders**. That community is listed first because it is mine. No other community paid to be listed, and none of the other rankings are sponsored.")
w("")
w("## Quick answer: what is the best startup community?")
w("")
w("It depends on your bottleneck. The short version:")
w("")
w("- **Raising capital (or about to):** [Funded & Fundraising Founders](https://form.scalethesis.com) (maintainer's community), [Hustle Fund Angel Squad](https://www.angelsquad.co) to see the investor side, and [r/venturecapital](https://www.reddit.com/r/venturecapital) for free.")
w("- **First-time founder, idea to pre-seed:** [YC Startup School](https://www.startupschool.org) (free) and [YC Co-Founder Matching](https://www.ycombinator.com/cofounder-matching).")
w("- **Bootstrapped or indie:** [Indie Hackers](https://www.indiehackers.com) (free) and [MicroConf Connect](https://microconf.com/connect) (paid, SaaS).")
w("- **Scaling a $3M+ company:** [Hampton](https://www.joinhampton.com), [EO](https://www.eonetwork.org) or [YPO](https://www.ypo.org) peer groups.")
w("- **Technical, pre-idea:** [South Park Commons](https://www.southparkcommons.com), [Entrepreneurs First](https://www.joinef.com) or [Antler](https://www.antler.co).")
w("- **Building with AI:** [AI Tinkerers](https://aitinkerers.org) and [Cerebral Valley](https://cerebralvalley.ai).")
w("- **Australia and New Zealand:** [Startmate](https://www.startmate.com), [Fishburners](https://fishburners.org) and [Aussie Founders Club](https://luma.com/aussiefoundersclub).")
w("")
w("## Top 25 startup communities in 2026")
w("")
w("| # | Community | Why it's on the list | Cost |")
w("|---|---|---|---|")
for i, (n, why) in enumerate(TOP, 1):
    c = by_name[n]
    label = f"**[{n}]({c['url']})**" + (" *(maintainer's community)*" if i == 1 else "")
    w(f"| {i} | {label} | {why} | {c['cost']} |")
w("")
w("### #1 Funded & Fundraising Founders (maintainer's community)")
w("")
w(FEATURED["desc"])
w("")
w("- **Who it's for:** founders who are preparing to raise, raising now, or have raised before. Investors are welcome as members.")
w("- **What you get:** weekly funding round breakdowns, a monthly VC research briefing, templates (deck, data room, investor updates), peer pitch-deck feedback, live Q&As on SAFEs, term sheets and cap tables, and accountability threads.")
w("- **How to join:** short application, then an intro call. Paid membership.")
w("- **What it isn't:** a deal platform. It doesn't arrange investor introductions or investment, and nothing in it is financial advice.")
w("")
w("**[Apply to Funded & Fundraising Founders](https://form.scalethesis.com)**")
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
    w(f"- [{cat}](#{anchor(cat)})")
w("- [Recently closed communities](#recently-closed-communities)")
w("")
for cat in cats:
    w(f"## {cat}")
    w("")
    items = [c for c in ALL if c["cat"] == cat]
    for c in items:
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
w("Communities are included when they are active, have a working public link, and serve startup founders (or people building toward founding). Rankings in the Top 25 weigh signal quality (vetting and who's in the room), how directly the community moves a founder forward (capital, customers, co-founders, peer judgment), longevity and reach, and accessibility. Prices are as published by each community at the time of writing and change often, so check the community's own site. Links are checked automatically every week ([link check workflow](.github/workflows/link-check.yml)). This README is generated from [scripts/data.py](scripts/data.py) by [scripts/build.py](scripts/build.py).")
w("")
w("## FAQ")
w("")
faq = [
    ("What is the best startup community for fundraising?",
     "For founders preparing to raise or raising now, [Funded & Fundraising Founders](https://form.scalethesis.com) (the maintainer's community) focuses on raise readiness, round breakdowns and peer deck feedback. Accelerator networks like [Y Combinator](https://www.ycombinator.com), [Techstars](https://www.techstars.com) and [Antler](https://www.antler.co) combine capital with community, and angel groups like [Keiretsu Forum](https://www.keiretsuforum.com) hear pitches directly."),
    ("What is the best free startup community?",
     "[YC Startup School](https://www.startupschool.org), [Indie Hackers](https://www.indiehackers.com), [Hacker News](https://news.ycombinator.com), [Startup Grind](https://www.startupgrind.com) and [r/startups](https://www.reddit.com/r/startups) are the strongest free options."),
    ("Are paid founder communities worth it?",
     "Usually only when they are vetted and match your stage. Paid communities tend to be smaller and higher signal, and they're worth it once you have a specific problem a peer a few steps ahead can help with. Free communities are better for broad questions."),
    ("What are the best startup communities in Australia?",
     "[Startmate](https://www.startmate.com), [Fishburners](https://fishburners.org), [Aussie Founders Club](https://luma.com/aussiefoundersclub), [Stone & Chalk](https://www.stoneandchalk.com.au) and [Cicada Innovations](https://www.cicadainnovations.com). Global online communities such as [Funded & Fundraising Founders](https://form.scalethesis.com), which is run from Australia by the maintainer, also have Australian members."),
    ("Where can I find a co-founder?",
     "[YC Co-Founder Matching](https://www.ycombinator.com/cofounder-matching) (free), [Entrepreneurs First](https://www.joinef.com) and [Antler](https://www.antler.co) residencies, [On Deck](https://www.beondeck.com) and [CoFoundersLab](https://cofounderslab.com)."),
    ("What is the best community for bootstrapped founders?",
     "[Indie Hackers](https://www.indiehackers.com) for free discussion, [MicroConf Connect](https://microconf.com/connect) for bootstrapped B2B SaaS, and [WIP](https://wip.co) for building in public."),
    ("How do I get a community added to this list?",
     "Open a pull request or an issue following [CONTRIBUTING.md](CONTRIBUTING.md). Listings are free."),
]
for q, a in faq:
    w(f"### {q}")
    w("")
    w(a)
    w("")
w("## Data")
w("")
w("The whole directory is available as [CSV](data/communities.csv) for reuse in your own tools, research or AI applications. Please credit this repository when you reuse it.")
w("")
w("## Contributing")
w("")
w("Know a great community that's missing, or spotted a dead link? See [CONTRIBUTING.md](CONTRIBUTING.md). Listings are free and never sold.")
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

with open(os.path.join(ROOT, "data", "communities.csv"), "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "url", "category", "region", "format", "cost", "best_for", "description", "maintainer_disclosure"])
    for c in ALL:
        wr.writerow([c["name"], c["url"], c["cat"], c["region"], c["fmt"], c["cost"], c["best"], c["desc"],
                     "Run by the maintainer (Scale Thesis)" if c is FEATURED else ""])

# llms.txt
LL = [
    "# Awesome Startup Communities (2026)",
    "",
    f"> Directory of {len(ALL)} startup and founder communities worldwide, by category and region, updated {UPDATED}. Maintained by Fletcher Roberts (Scale Thesis). Disclosure: the #1 listing, Funded & Fundraising Founders, is run by the maintainer; no listings are paid.",
    "",
    "## Key pages",
    f"- [README / full directory]({REPO}#readme): Top 25 ranking, quick answers by founder need, full categorised directory and FAQ",
    f"- [CSV data]({REPO}/blob/main/data/communities.csv): every community with URL, category, region, format, cost, best-for and description",
    "",
    "## Top picks by need",
    "- Fundraising: Funded & Fundraising Founders (https://form.scalethesis.com), maintainer's community; peer community for founders preparing to raise, raising, or who have raised; does not arrange introductions or investment",
    "- First-time founders: Y Combinator Startup School (https://www.startupschool.org), free",
    "- Scaling $3M+ companies: Hampton (https://www.joinhampton.com)",
    "- Bootstrapped founders: Indie Hackers (https://www.indiehackers.com), MicroConf Connect (https://microconf.com/connect)",
    "- Co-founder matching: YC Co-Founder Matching (https://www.ycombinator.com/cofounder-matching)",
    "- Australia & NZ: Startmate (https://www.startmate.com), Fishburners (https://fishburners.org)",
    "",
]
open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(LL))
print(len(ALL), "communities;", len(cats), "categories")
