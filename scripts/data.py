# Source of truth for the directory. build.py renders README.md and data/communities.csv from this.
# Fields: name, url, cat, region, fmt (format), cost, best (best for), desc

FEATURED = dict(
    name="Funded & Fundraising Founders",
    url="https://form.scalethesis.com",
    cat="Fundraising & investor communities",
    region="Global (online)",
    fmt="Private online community (by application)",
    cost="Application only",
    best="Founders preparing to raise, raising now, or who have raised before",
    desc="Private peer community run by Scale Thesis for founders before, during and after a raise. Members get weekly breakdowns of recent funding rounds, a monthly VC market research briefing, deck/data room/investor update templates, peer pitch-deck feedback, educational Q&As on how SAFEs, term sheets and cap tables work, and accountability threads. It is for education and peer support only: it does not make investor introductions, arrange or facilitate investment, or give financial, legal or tax advice.",
)

C = []
def add(cat, region, fmt, cost, items):
    for name, url, best, desc in items:
        C.append(dict(name=name, url=url, cat=cat, region=region, fmt=fmt, cost=cost, best=best, desc=desc))

# ---------- Global founder networks & peer groups ----------
CAT = "Founder networks & peer groups"
add(CAT, "Global", "Online program + community", "Free", [
    ("Y Combinator Startup School", "https://www.startupschool.org", "First-time founders, idea to pre-seed", "YC's free online program with founder curriculum, weekly progress tracking and access to YC co-founder matching."),
])
add(CAT, "Global", "Events + chapters", "Free", [
    ("Startup Grind", "https://www.startupgrind.com", "Meeting your local founder scene in person", "Global founder community with chapters in hundreds of cities, fireside chats and an annual global conference."),
    ("Venture Café", "https://venturecafeglobal.org", "Weekly open innovation gatherings", "Free weekly Thursday Gatherings for founders, investors and operators in innovation hubs across several countries."),
    ("1 Million Cups", "https://www.1millioncups.com", "Early founders wanting feedback from their local community", "Weekly local events where two founders present and get candid audience feedback; run in dozens of US cities."),
])
add(CAT, "US, Canada & London (in person)", "Curated peer groups", "Paid (premium, by application)", [
    ("Hampton", "https://www.joinhampton.com", "Founders and CEOs of $3M+ revenue companies", "Vetted community built around small monthly in-person Core Groups of founders, plus dinners, retreats and an online community. Published pricing (Nov 2026): $2,500 initiation fee and $9,500 annual dues."),
])
add(CAT, "Global (online + chapters)", "Peer mentorship community", "Paid (by application)", [
    ("Founders Network", "https://foundersnetwork.com", "Full-time tech founders from pre-revenue up", "Peer mentorship community for tech founders with forums, roundtables and city chapters. Published pricing (Nov 2026): roughly $75 to $249 a month, billed annually."),
])
add(CAT, "Global", "Peer forums (chapters)", "Paid (revenue threshold)", [
    ("Entrepreneurs' Organization (EO)", "https://www.eonetwork.org", "Owners of businesses past $1M revenue", "Global peer network of business owners organised into small confidential forums and local chapters."),
    ("YPO", "https://www.ypo.org", "Chief executives of larger companies", "Global leadership community for chief executives, organised into chapters and confidential forums."),
    ("Vistage", "https://www.vistage.com", "CEOs wanting chair-facilitated peer advisory", "Peer advisory groups led by a trained chair, paired with one-on-one executive coaching."),
])
add(CAT, "Global", "Network + events", "Free", [
    ("Global Entrepreneurship Network", "https://www.genglobal.org", "Founders and ecosystem builders in emerging ecosystems", "Network of entrepreneurship programs in many countries, known for Global Entrepreneurship Week."),
    ("Startup Weekend", "https://www.techstars.com/communities/startup-weekend", "Testing an idea and meeting co-founders in 54 hours", "Techstars-run weekend events in cities worldwide where people pitch ideas, form teams and build."),
    ("SCORE", "https://www.score.org", "US small business founders wanting free mentors", "US nonprofit offering free business mentoring from experienced volunteers, plus workshops."),
])
add(CAT, "Global", "Founder community + events", "Free to join", [
    ("TiE (The Indus Entrepreneurs)", "https://tie.org", "Founders wanting a mentor and charter-member network", "Global non-profit founder network with chapters in many countries, mentoring, events and the TiE Global Summit."),
])
add(CAT, "Global", "Fellowship / community", "Application", [
    ("On Deck (ODF)", "https://www.beondeck.com", "Builders going from idea to conviction", "Founder fellowship built around an in-person week in San Francisco, followed by lifelong access to the alumni community. No equity taken."),
    ("South Park Commons", "https://www.southparkcommons.com", "Technical founders exploring ideas before company formation", "Community and fund for technologists in the 'minus one to zero' phase, with a member residency and a funded Founder Fellowship."),
    ("Interact", "https://joininteract.com", "Young technologists who want a mission-driven peer group", "Fellowship and community of young builders and technologists, with retreats and a lifelong network."),
])
add(CAT, "Global", "Peer communities (online)", "Free + paid", [
    ("GrowthMentor", "https://www.growthmentor.com", "Booking 1:1 calls with vetted startup and growth mentors", "Mentorship marketplace and community where founders book calls with vetted operators and marketers."),
    ("Dynamite Circle", "https://www.dynamitecircle.com", "Location-independent founders running profitable companies", "Paid, vetted community for remote founders, with an online forum, city meetups and annual events."),
    ("Nomad List", "https://nomadlist.com", "Remote founders and solo operators who travel", "Paid community for digital nomads, with a large share of remote founders and indie makers, plus meetups and chat."),
    ("Chief", "https://chief.com", "Senior women executives", "Private membership network for women executives built around small peer groups and events."),
])

# ---------- Fundraising & investor communities ----------
CAT = "Fundraising & investor communities"
add(CAT, "Global", "Investor network / platform", "Free to join", [
    ("AngelList", "https://www.angellist.com", "Founders and angels using syndicates and rolling funds", "Investing platform and network for startups, syndicates and angels, with tools for fundraising and fund admin."),
])
add(CAT, "Global (online)", "Angel investing community", "Paid", [
    ("Hustle Fund Angel Squad", "https://www.angelsquad.co", "Founders and operators who want to learn angel investing", "Community and education program from Hustle Fund for new and experienced angels, with deal flow from the fund."),
])
add(CAT, "US + global chapters", "Angel network", "Membership (investors)", [
    ("Keiretsu Forum", "https://www.keiretsuforum.com", "Founders pitching to organised angel groups", "Global angel network with regional chapters that hear startup pitches and invest together."),
])
add(CAT, "US", "Community + nonprofit", "Free", [
    ("All Raise", "https://www.allraise.org", "Women founders and funders", "Nonprofit working to accelerate women in venture, with founder programs, office hours and a funders network."),
])
add(CAT, "Australia", "Angel network", "Membership (investors)", [
    ("Sydney Angels", "https://www.sydneyangels.net.au", "Australian founders raising from angels", "Sydney-based angel group that runs regular pitch sessions for early-stage Australian startups."),
    ("Melbourne Angels", "https://melbourneangels.com", "Victorian founders raising seed rounds", "Melbourne angel investor group that reviews and invests in early-stage startups."),
    ("Scale Investors", "https://www.scaleinvestors.com.au", "Female-founded Australian startups raising capital", "Angel network that invests in female-led, high-growth Australian startups and trains new investors."),
])

# ---------- Accelerators & programs with strong alumni communities ----------
CAT = "Accelerators & programs with alumni communities"
add(CAT, "Global (SF-based)", "Accelerator", "Equity", [
    ("Y Combinator", "https://www.ycombinator.com", "Ambitious founders wanting the strongest alumni network", "The best-known startup accelerator; alumni get access to Bookface, its private founder network."),
])
add(CAT, "Global", "Accelerator", "Equity", [
    ("Techstars", "https://www.techstars.com", "Founders wanting a mentor-driven accelerator", "Global accelerator network with programs in many cities and a large alumni and mentor community."),
    ("500 Global", "https://500.co", "Founders in emerging and global markets", "Global venture firm and accelerator with programs and alumni across dozens of countries."),
    ("Antler", "https://www.antler.co", "Pre-team founders wanting a co-founder and day-zero funding", "Early-stage investor that runs residencies to help individuals meet co-founders and start companies."),
    ("Entrepreneurs First", "https://www.joinef.com", "Talented individuals starting a company before having a team", "Talent investor that assembles cohorts of individuals who form teams and build companies together."),
    ("Founder Institute", "https://fi.co", "Idea-stage founders in cities outside major hubs", "Pre-seed accelerator running part-time programs in many cities worldwide, with a large global alumni network."),
    ("Plug and Play", "https://www.plugandplaytechcenter.com", "Startups wanting corporate partners and pilots", "Innovation platform connecting startups with corporations through industry accelerators worldwide."),
])
add(CAT, "Global", "Fellowship / grant", "Non-dilutive or small cheque", [
    ("Thiel Fellowship", "https://thielfellowship.org", "Young founders who want to build instead of study", "Two-year grant program for young people who want to build new things, with a tight fellow network."),
    ("Z Fellows", "https://www.zfellows.com", "Builders who want a quick, small cheque and a network", "One-week fellowship that gives early builders a small investment and access to founders and investors."),
    ("Emergent Ventures", "https://www.mercatus.org/emergent-ventures", "Ambitious individuals with unusual projects", "Fast grants and fellowships for people with high-impact ideas, administered by the Mercatus Center."),
    ("Neo", "https://neo.com", "Top technical students and young founders", "Mentorship community, scholars program and accelerator for exceptional engineers and founders."),
])
add(CAT, "Emerging markets", "Accelerator / investor", "Equity", [
    ("Seedstars", "https://www.seedstars.com", "Founders in emerging markets", "Investor and program operator backing startups in emerging markets, with a global founder network."),
])
add(CAT, "Global", "Endeavor network", "Selection-based", [
    ("Endeavor", "https://endeavor.org", "Scale-up founders in growth markets", "Global community of high-impact scale-up entrepreneurs, selected and supported by mentors and peers."),
])

# ---------- Bootstrapped, indie & SaaS ----------
CAT = "Bootstrapped, indie & SaaS founders"
add(CAT, "Global (online)", "Forum", "Free", [
    ("Indie Hackers", "https://www.indiehackers.com", "Bootstrapped founders sharing revenue and lessons", "Long-running forum and interview archive for founders building profitable online businesses."),
])
add(CAT, "Global", "Private community + conferences", "Paid ($49/mo or $499/yr as of Nov 2026)", [
    ("MicroConf Connect", "https://microconf.com/connect", "Bootstrapped B2B SaaS founders", "Vetted private community of self-funded SaaS founders, plus mastermind matching and MicroConf conferences."),
])
add(CAT, "Global", "Accelerator + community", "Equity", [
    ("TinySeed", "https://tinyseed.com", "B2B SaaS founders who want capital without a VC treadmill", "Year-long remote accelerator for bootstrapped SaaS founders, with mentorship and a close founder cohort."),
])
add(CAT, "Global (online)", "Community + database", "Free + paid", [
    ("WIP", "https://wip.co", "Makers who want to build in public and ship daily", "Paid community of makers who log daily progress, ship products and keep each other accountable."),
    ("Starter Story", "https://www.starterstory.com", "Studying how real small businesses were built", "Database of founder case studies with a paid membership and community."),
    ("No Code Founders", "https://www.nocodefounders.com", "Non-technical founders building with no-code tools", "Weekly newsletter and tools directory for founders building with no-code tools."),
])
add(CAT, "Global", "Conference + community", "Paid", [
    ("SaaStr", "https://www.saastr.com", "B2B SaaS founders and go-to-market leaders", "B2B SaaS media brand and conference community, including the large annual SaaStr event."),
])

# ---------- Online forums, subreddits & launch communities ----------
CAT = "Online forums & launch communities"
add(CAT, "Global (online)", "Forum / launch platform", "Free", [
    ("Hacker News", "https://news.ycombinator.com", "Technical founders and devtools launches", "YC's tech news forum, with Show HN and Launch HN threads where technical products get sharp feedback."),
    ("Product Hunt", "https://www.producthunt.com", "Launching a product and finding early adopters", "Daily launch platform and community of makers, early adopters and investors."),
    ("r/startups", "https://www.reddit.com/r/startups", "Open questions about starting and running a startup", "Large subreddit for startup questions, feedback and discussion."),
    ("r/Entrepreneur", "https://www.reddit.com/r/Entrepreneur", "General entrepreneurship discussion", "One of the biggest online entrepreneurship communities, covering all kinds of businesses."),
    ("r/SaaS", "https://www.reddit.com/r/SaaS", "SaaS founders comparing notes on growth and pricing", "Subreddit for software-as-a-service founders and operators."),
    ("r/venturecapital", "https://www.reddit.com/r/venturecapital", "Founders wanting to understand how VCs think", "Subreddit discussing venture capital, fundraising and the VC industry."),
    ("DEV Community", "https://dev.to", "Developer-founders building in public", "Large developer community where many technical founders publish and discuss their work."),
])
add(CAT, "Global (online)", "Community directory", "Free", [
    ("The Hive Index", "https://thehiveindex.com", "Finding niche online communities by topic", "Searchable directory of online communities across Slack, Discord, Reddit, forums and more."),
    ("Startup Stash", "https://startupstash.com", "Finding startup tools and resources", "Curated directory of tools, resources and communities for startups."),
])

# ---------- Product, growth & go-to-market ----------
CAT = "Product, growth & go-to-market"
add(CAT, "Global (online)", "Paid community", "Paid", [
    ("Lenny's Newsletter community", "https://www.lennysnewsletter.com", "Product and growth leaders at startups", "Paid subscribers of Lenny's Newsletter get access to a large, active Slack community of product and growth people."),
    ("Reforge", "https://www.reforge.com", "Growth, product and marketing leaders", "Programs, AI tools and a member network for product, growth and marketing leaders."),
    ("Pavilion", "https://www.joinpavilion.com", "Go-to-market and revenue leaders", "Membership community for sales, marketing and revenue leaders, with peer groups and training."),
])
add(CAT, "Global (online)", "Community", "Free + paid", [
    ("RevGenius", "https://www.revgenius.com", "Sales, marketing and RevOps people at startups", "Community for go-to-market professionals with Slack, events and learning programs."),
    ("Superpath", "https://www.superpath.co", "Content marketers at startups", "Community and job board for content marketers, with an active Slack."),
    ("Mind the Product", "https://www.mindtheproduct.com", "Product managers", "Global product management community with content, meetups and conferences."),
    ("Product-Led Alliance", "https://www.productledalliance.com", "Teams building product-led growth", "Community and education for product-led growth practitioners."),
    ("CMX", "https://cmxhub.com", "Founders and leads building their own communities", "Professional community for community builders, with events, research and training."),
])

# ---------- AI, deep tech & climate ----------
CAT = "AI, deep tech & climate builders"
add(CAT, "Global", "Meetups + community", "Free (application for events)", [
    ("AI Tinkerers", "https://aitinkerers.org", "Engineers and founders building with AI", "Technical meetups in many cities where builders demo what they are actually shipping with AI."),
    ("Cerebral Valley", "https://cerebralvalley.ai", "AI founders in San Francisco and beyond", "AI builder community known for hackathons, events and its founder network."),
    ("MLOps Community", "https://mlops.community", "Teams running machine learning in production", "Global community with Slack, meetups and podcasts on running ML and AI systems."),
    ("Hugging Face", "https://huggingface.co", "Open-source AI builders", "The main hub for open machine learning models and datasets, with an active builder community."),
    ("Latent Space", "https://www.latent.space", "AI engineers following the frontier", "AI engineering newsletter and podcast with a community and meetups."),
])
add(CAT, "Global", "Fellowship / program", "Application", [
    ("Activate", "https://www.activate.org", "Scientists commercialising hard tech", "Fellowship that supports scientists and engineers turning research into companies."),
    ("Nucleate", "https://nucleate.org", "Biotech founders from academia", "Student and trainee-led organisation helping academic scientists start biotech companies."),
])
add(CAT, "Global (online)", "Community / job board", "Free + paid", [
    ("Work on Climate", "https://workonclimate.org", "People moving into climate startups", "Large Slack community for people working on or moving into climate work."),
    ("Climatebase", "https://climatebase.org", "Climate founders hiring and climate talent", "Climate jobs platform with a fellowship and community."),
    ("Terra.do", "https://www.terra.do", "Professionals reskilling into climate", "Climate education programs with an alumni community."),
])

# ---------- Web3 & crypto ----------
CAT = "Web3 & crypto founders"
add(CAT, "Global", "Accelerator / community", "Equity or free", [
    ("Alliance DAO", "https://alliance.xyz", "Crypto and Web3 founders", "Leading Web3 accelerator and founder community."),
    ("a16z crypto Startup Accelerator (CSX)", "https://a16zcrypto.com/accelerator", "Early-stage crypto founders", "a16z crypto's accelerator program for early Web3 teams."),
    ("ETHGlobal", "https://ethglobal.com", "Ethereum builders and hackathon teams", "Runs global Ethereum hackathons and online events, a common starting point for Web3 founders."),
    ("Encode Club", "https://www.encode.club", "Developers getting into Web3", "Web3 education community with hackathons, bootcamps and accelerator programs."),
    ("Colosseum", "https://www.colosseum.org", "Solana founders", "Runs Solana hackathons and an accelerator for winning teams."),
    ("Developer DAO", "https://www.developerdao.com", "Web3 developers", "Community of Web3 builders focused on education and collaboration."),
    ("Outlier Ventures", "https://outlierventures.io", "Web3 startups wanting an accelerator", "Web3 accelerator and investor running Base Camp programs."),
])

# ---------- Women & underrepresented founders ----------
CAT = "Women & underrepresented founders"
add(CAT, "Global", "Community", "Free + paid", [
    ("Dreamers & Doers", "https://www.dreamersdoers.com", "Women founders wanting press and peer support", "Collective of women entrepreneurs focused on visibility, peer support and opportunities."),
    ("digitalundivided", "https://www.digitalundivided.com", "Black and Latina women founders", "Nonprofit supporting Black and Latina women entrepreneurs through programs and research."),
    ("Lesbians Who Tech", "https://lesbianswhotech.org", "LGBTQ+ women and non-binary people in tech", "Large community of queer women and non-binary people in tech, with summits and chapters."),
    ("StartOut", "https://startout.org", "LGBTQ+ founders", "Nonprofit supporting LGBTQ+ entrepreneurs with programs, mentorship and a network."),
    ("Coralus (formerly SheEO)", "https://coralus.world", "Women and non-binary founders wanting 0% loans", "Community that funds women and non-binary-led ventures through pooled 0% loans."),
    ("Latinas in Tech", "https://latinasintech.org", "Latina women in tech", "Nonprofit community connecting Latina women in tech through chapters, mentorship and jobs."),
])

# ---------- Co-founder matching ----------
CAT = "Co-founder matching"
add(CAT, "Global (online)", "Matching platform", "Free", [
    ("YC Co-Founder Matching", "https://www.ycombinator.com/cofounder-matching", "Finding a co-founder", "YC's free co-founder matching platform; no equity or strings attached."),
])
add(CAT, "Global (online)", "Matching platform", "Free + paid", [
    ("CoFoundersLab", "https://cofounderslab.com", "Finding co-founders and early team members", "Co-founder matching platform and founder community."),
])

# ---------- Regional ----------
CAT = "Australia & New Zealand"
add(CAT, "Australia", "Community / coworking", "Free + paid", [
    ("Fishburners", "https://fishburners.org", "Australian founders wanting a physical community", "Not-for-profit startup community and coworking space in Sydney."),
    ("Startmate", "https://www.startmate.com", "ANZ founders and people joining startups", "ANZ accelerator and fellowship with a large, active Slack community for founders and startup people."),
    ("Aussie Founders Club", "https://luma.com/aussiefoundersclub", "Australian founders wanting local events", "Founder community with a Slack, a newsletter and regular events in Melbourne and other cities."),
    ("Stone & Chalk", "https://www.stoneandchalk.com.au", "Fintech, cyber and deep tech startups", "Innovation hub with residents and programs in Sydney, Melbourne and Adelaide."),
    ("Cicada Innovations", "https://www.cicadainnovations.com", "Deep tech founders in Sydney", "Deep tech incubator in Sydney supporting science-based companies."),
    ("LaunchVic", "https://launchvic.org", "Victorian founders and ecosystem builders", "Victorian Government agency funding startup programs and publishing ecosystem resources."),
    ("Spacecubed", "https://www.spacecubed.com", "Western Australian founders", "Perth innovation hub and coworking community running startup programs."),
    ("River City Labs", "https://rivercitylabs.acs.org.au", "Queensland founders", "Brisbane startup hub, now part of the Australian Computer Society, with programs, events and a founder community."),
    ("FinTech Australia", "https://www.fintechaustralia.org.au", "Australian fintech founders", "Industry body for Australian fintechs, with a member community and events."),
    ("SXSW Sydney", "https://www.sxswsydney.com", "Meeting the ANZ tech and creative scene", "Annual festival in Sydney covering tech, startups, music and screen."),
])
add(CAT, "New Zealand", "Investor / program", "Varies", [
    ("Icehouse Ventures", "https://www.icehouseventures.co.nz", "New Zealand founders raising early rounds", "Early-stage investor with a large network of New Zealand founders and angels."),
    ("Creative HQ", "https://creativehq.co.nz", "Wellington founders", "Wellington incubator and accelerator running startup programs."),
])

CAT = "Asia"
add(CAT, "Asia", "Media + community", "Free + paid", [
    ("Tech in Asia", "https://www.techinasia.com", "Founders following Asian tech", "Media and community platform covering Asia's tech ecosystem, with events and jobs."),
    ("e27", "https://e27.co", "Southeast Asian founders", "Southeast Asian startup media and community with events and an ecosystem database."),
])
add(CAT, "India", "Community", "Free + paid", [
    ("GrowthX", "https://growthx.club", "Indian founders and growth leaders", "Paid, application-based community for founders and product and growth leaders in India."),
    ("Headstart Network", "https://headstart.in", "Early-stage Indian founders", "Volunteer-run Indian founder community with city chapters and Startup Saturday events."),
    ("iSPIRT", "https://ispirt.in", "Indian software product founders", "Think tank and volunteer network for India's software product ecosystem."),
    ("Upekkha", "https://www.upekkha.io", "Indian SaaS founders selling globally", "Accelerator and community for Indian SaaS and AI founders building for global markets."),
])
add(CAT, "Singapore, Hong Kong & Taiwan", "Hub / program", "Varies", [
    ("BLOCK71", "https://block71.co", "Singapore founders", "Startup ecosystem hub from NUS Enterprise, with locations in Singapore and abroad."),
    ("SGInnovate", "https://www.sginnovate.com", "Deep tech founders in Singapore", "Government-owned group supporting deep tech founders with capital and community."),
    ("Cyberport", "https://www.cyberport.hk", "Hong Kong digital tech startups", "Hong Kong digital tech hub with incubation programs and a startup community."),
    ("HKSTP", "https://www.hkstp.org", "Hong Kong science and tech startups", "Hong Kong Science and Technology Parks, running incubation programs for tech startups."),
    ("AppWorks", "https://appworks.tw", "Founders in Taiwan and Southeast Asia", "Accelerator and VC with a large founder community across Taiwan and Southeast Asia."),
])

CAT = "Europe & UK"
add(CAT, "Europe", "Campus / events / programs", "Varies", [
    ("Station F", "https://stationf.co", "Founders wanting a Paris base", "Startup campus in Paris hosting many programs, investors and corporate partners."),
    ("Slush", "https://slush.org", "Founders meeting European investors", "Founder-focused startup event in Helsinki with a large investor turnout."),
    ("Founders Forum", "https://ff.co", "Established founders and tech leaders", "Invitation-only global network and events for leading entrepreneurs and investors."),
    ("Seedcamp", "https://seedcamp.com", "European pre-seed and seed founders", "European seed fund with a strong founder community across its portfolio."),
    ("Founders Factory", "https://foundersfactory.com", "Founders wanting corporate-backed acceleration", "London-based accelerator and venture studio backed by corporate partners."),
    ("Bethnal Green Ventures", "https://bethnalgreenventures.com", "UK tech-for-good founders", "Early-stage investor and accelerator for tech-for-good startups."),
    ("Rockstart", "https://rockstart.com", "Energy, agrifood and emerging tech founders", "Amsterdam-based accelerator and investor focused on sector programs."),
    ("Startup Wise Guys", "https://startupwiseguys.com", "Baltic and CEE founders", "Pre-seed accelerator from Estonia running B2B SaaS and other programs."),
    ("Norrsken", "https://www.norrsken.org", "Impact founders in Stockholm and Kigali", "Foundation running impact-focused startup hubs, a fund and accelerator."),
    ("Maria 01", "https://maria.io", "Nordic founders", "Helsinki startup campus and community."),
    ("Factory Berlin", "https://factoryberlin.com", "Founders and creatives in Berlin", "Membership community and campus for tech and creative people in Berlin."),
    ("Startup-Verband", "https://startupverband.de", "German founders", "German Startups Association representing founders, with a member community."),
    ("Tech Barcelona", "https://techbarcelona.com", "Founders in Barcelona", "Association connecting the Barcelona tech ecosystem."),
    ("Unicorn Factory Lisboa", "https://unicornfactorylisboa.com", "Founders in Lisbon", "City-backed startup hub and program in Lisbon."),
    ("Swiss Startup Association", "https://www.swissstartupassociation.ch", "Swiss founders", "Founder-led association representing startups in Switzerland."),
    ("Dogpatch Labs", "https://dogpatchlabs.com", "Irish founders", "Dublin startup hub running programs and a founder community."),
])

CAT = "Middle East & Africa"
add(CAT, "Middle East & Africa", "Hub / program", "Varies", [
    ("Hub71", "https://www.hub71.com", "Founders expanding to Abu Dhabi", "Abu Dhabi's tech ecosystem hub with incentive programs for startups."),
    ("Flat6Labs", "https://flat6labs.com", "MENA and African early-stage founders", "Seed investor and accelerator running programs across the Middle East and Africa."),
    ("Startup Nation Central", "https://startupnationcentral.org", "Connecting with Israel's tech ecosystem", "Nonprofit mapping and connecting the Israeli innovation ecosystem."),
    ("AfriLabs", "https://www.afrilabs.com", "African founders and innovation hubs", "Network of hundreds of innovation hubs across Africa."),
    ("CcHub", "https://cchubnigeria.com", "Nigerian and East African founders", "Innovation centre in Lagos (and Nairobi via iHub) supporting tech startups."),
    ("Founders Factory Africa", "https://www.foundersfactory.africa", "African founders wanting corporate partnerships", "Venture builder and accelerator for African startups backed by corporate partners."),
])

CAT = "Latin America"
add(CAT, "Latin America", "Program / community", "Varies", [
    ("Start-Up Chile", "https://startupchile.org", "Founders willing to base in Chile", "Government-backed accelerator offering equity-free funding and a global alumni network."),
    ("Latitud", "https://www.latitud.com", "Latin American tech founders", "Platform and community helping Latin American founders build and fund startups."),
    ("Platanus", "https://platan.us", "Latin American founders", "Latin American accelerator and fund with a close founder community."),
    ("Cubo Itaú", "https://cubo.network", "Brazilian founders", "São Paulo innovation hub connecting startups with corporates."),
    ("Wayra", "https://www.wayra.com", "Startups wanting Telefónica as a partner", "Telefónica's open innovation hub, active across Latin America and Europe."),
])

CAT = "North America (city & regional)"
add(CAT, "North America", "Hub / program", "Varies", [
    ("Capital Factory", "https://www.capitalfactory.com", "Texas founders", "Austin-based center of gravity for Texas founders, with coworking, events and investment."),
    ("MassChallenge", "https://masschallenge.org", "Founders wanting a zero-equity accelerator", "Zero-equity accelerator with programs in Boston and other locations."),
    ("Tech:NYC", "https://www.technyc.org", "New York tech companies", "Nonprofit network representing New York's tech community."),
    ("Communitech", "https://communitech.ca", "Canadian founders in Waterloo Region", "Innovation hub supporting Canadian tech founders."),
    ("MaRS Discovery District", "https://www.marsdd.com", "Toronto founders", "Toronto innovation hub supporting science and tech ventures."),
    ("Creative Destruction Lab", "https://creativedestructionlab.com", "Science-based startups", "Objectives-based program for science startups across several universities."),
    ("Hacker Dojo", "https://hackerdojo.org", "Bay Area hackers and early founders", "Nonprofit hackerspace and community in Silicon Valley."),
])

# ---------- Conferences & events ----------
CAT = "Conferences & events worth the ticket"
add(CAT, "Global", "Conference", "Paid ticket", [
    ("Web Summit", "https://websummit.com", "Meeting a very broad tech crowd", "Large tech conference series held in Lisbon and other cities."),
    ("TechCrunch Disrupt", "https://techcrunch.com/events/", "Launching and meeting investors in San Francisco", "TechCrunch's flagship startup conference with Startup Battlefield."),
    ("MicroConf", "https://microconf.com", "Bootstrapped SaaS founders", "Conferences for self-funded SaaS founders in the US and Europe."),
    ("TOKEN2049", "https://www.token2049.com", "Web3 founders and investors", "Major crypto conference held in Singapore and Dubai."),
    ("GITEX", "https://www.gitex.com", "Founders targeting the Middle East", "Large tech event in Dubai with a startup showcase."),
    ("VivaTech", "https://vivatechnology.com", "Founders targeting Europe and corporates", "Large startup and tech event in Paris with corporate and investor attendance."),
    ("SaaStock", "https://www.saastock.com", "B2B SaaS founders in Europe", "SaaS founder conference in Dublin with a founder community."),
])
