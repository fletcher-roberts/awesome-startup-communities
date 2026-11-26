# README renderer in the Awesome list format (https://github.com/sindresorhus/awesome).
# Run via build.py, which provides ALL, FEATURED, TOP, QUICK, STAGES, FAQ, CANON, cats, by_name, SITE, REPO, UPDATED.

UTM = "https://form.scalethesis.com/?ref=github-awesome-"

def plain(s):
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)

def gh_anchor(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return s.replace(" ", "-")

def sentence(s):
    s = s.strip()
    return s if s.endswith(".") else s + "."

def awesome_entry(c):
    if c is FEATURED:
        return (f"- [{c['name']}]({FFF_PAGE}) - Maintainer's community, ranked #1 in this list (disclosed). {c['desc']} "
                f"Best for: {c['best']}. Membership: {c['cost']}. Region: {c['region']}.")
    return f"- [{c['name']}]({c['url']}) - {sentence(c['desc'])} Best for: {sentence(c['best'])} Cost: {sentence(c['cost'])} Region: {sentence(c['region'])}"

def table(rows):
    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    out = ["| " + " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(rows[0])) + " |",
           "| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |"]
    for r in rows[1:]:
        out.append("| " + " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(r)) + " |")
    return out

SECTIONS = ["Top 25 Startup Communities", "Featured: Funded & Fundraising Founders", "Quick Picks by Need", "Communities by Stage"] + cats + ["Recently Closed Communities"]

A = []
a = A.append
a("# Awesome Startup Communities [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
a("")
a(f"> The best startup and founder communities in the world, ranked and organised: {len(ALL)} founder peer groups, fundraising communities, accelerator networks, bootstrapped and SaaS communities, AI and Web3 builders, co-founder matching and regional hubs. Updated {UPDATED}.")
a("")
a("**Disclosure:** maintained by Fletcher Roberts, founder of [Scale Thesis](https://scalethesis.com), which runs Funded & Fundraising Founders. That community is placed #1 because it is the maintainer's own, not because of the scoring in the footnotes. No other listing is paid for, and the maintainer has no commercial relationship with any other listed community.")
a("")
a(f"Prefer a website? Browse the [searchable web version]({SITE}).")
a("")
a("## Contents")
a("")
for s_ in SECTIONS:
    a(f"- [{s_}](#{gh_anchor(s_)})")
a("")
a("## Top 25 Startup Communities")
a("")
rows = [["#", "Community", "Best for", "Cost"]]
for i, (n, why) in enumerate(TOP, 1):
    c = by_name[n]
    name = f"**[{n}]({UTM}top25)**" if c is FEATURED else n
    rows.append([str(i), name, why, c["cost"]])
A.extend(table(rows))
a("")
a("Every community in the Top 25 is listed with a link and details in its category below.")
a("")
a("## Featured: Funded & Fundraising Founders")
a("")
a(CANON.replace("Funded & Fundraising Founders (FFF)", "**Funded & Fundraising Founders (FFF)**", 1))
a("")
a(f"Members get weekly funding round breakdowns, a monthly VC research briefing, deck, data room and investor update templates, peer pitch-deck feedback, educational Q&As on SAFEs, term sheets and cap tables, and accountability threads. Membership is application only, followed by an intro call. It is for education and peer support only: it does not make investor introductions, arrange or facilitate investment, or give financial, legal or tax advice.")
a("")
a(f"**[Apply to Funded & Fundraising Founders]({UTM}featured)**")
a("")
a("## Quick Picks by Need")
a("")
for k, v in QUICK:
    a(f"**{k}:** {plain(v)}")
    a("")
a("## Communities by Stage")
a("")
for stage, names in STAGES:
    a(f"**{stage}:** " + ", ".join(n + (" (maintainer's community)" if n == FEATURED["name"] else "") for n in names) + ".")
    a("")
for cat in cats:
    a(f"## {cat}")
    a("")
    for c in [c for c in ALL if c["cat"] == cat]:
        a(awesome_entry(c))
    a("")
a("## Recently Closed Communities")
a("")
a("These still appear in older lists but are no longer operating: Elpha (women in tech) wound down after nearly seven years; Women Who Code shut down in 2024 after losing critical funding; Girls in Tech closed in 2024 after 17 years; and Buildspace shut down in 2024.")
a("")
a("## Contributing")
a("")
a("Suggestions, corrections and removal requests are welcome. Read the [contribution guidelines](CONTRIBUTING.md) first. Listings are free and never sold.")
a("")
a("## Footnotes")
a("")
a("### Methodology")
a("")
a("Communities are included when they are active, have a working public link, and serve startup founders or people building toward founding. The directory is curated, not exhaustive. "
  "The Top 25 is editorial opinion. Positions 2 to 25 weigh signal quality (vetting and who's in the room), how directly the community moves a founder forward (capital, customers, co-founders, peer judgment), longevity and reach, and accessibility. "
  "Position 1 is the maintainer's own community and is placed there because it is his, not because of this scoring. "
  f"Descriptions and prices are based on each community's public information as of {UPDATED} and can change, so check the community's own site before joining. "
  "Links are checked automatically every week. This README is generated from `scripts/data.py`.")
a("")
a("### FAQ")
a("")
for q_, ans in FAQ:
    if q_.startswith("How do I get a community added"):
        continue
    ans = plain(ans)
    if q_.startswith("What is the best startup community for fundraising"):
        ans = ans.replace("Funded & Fundraising Founders (the maintainer's community)", f"[Funded & Fundraising Founders]({UTM}faq) (the maintainer's community)", 1)
    a(f"**{q_}** {ans}")
    a("")
a("### Data")
a("")
a("The whole directory is available as [CSV data](data/communities.csv) and the [website](" + SITE + "#top) has structured data for search engines and AI tools. Please credit this repository when you reuse it, using the [citation file](CITATION.cff).")
a("")
a("### Disclaimer")
a("")
a("This directory is general information only. It is not financial, investment, legal or tax advice, and inclusion is not an endorsement or a guarantee of any community, program or outcome. Community names and trademarks belong to their owners and are used only to identify them. Do your own research before joining or paying for anything. Licensed under CC BY 4.0.")
a("")
a("### About the Maintainer")
a("")
a("Maintained by [Fletcher Roberts](https://www.linkedin.com/in/fletchroberts/), founder and CEO of Scale Thesis, a growth and fundraising advisory for startups, and co-founder of Web3 security firm Hashlock. He also writes on [Substack](https://fletchroberts.substack.com).")
a("")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(A))
print("awesome README written")
