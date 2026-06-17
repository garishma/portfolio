# portfolio_data.py — Single source of truth, extracted from Garishma Gupta's resume

IDENTITY = {
    "name_first": "Garishma",
    "name_last": "Gupta",
    "title": "Senior Technology & Operations Leader",
    "tagline": "PMP Certified · AI Strategy · Digital Transformation",
    "value_proposition": "Translating complex operational problems into scalable, AI-led solutions — across healthcare-tech and BFSI.",
    "email": "garishma.gari@gmail.com",
    "phone": "+91 961 932 3028",
    "location": "Mumbai, India",
    "linkedin": "https://www.linkedin.com/in/garishma-gupta",
}

SUMMARY = (
    "I'm a results-driven Technology & Operations leader with 10+ years of progressive experience — "
    "from technical delivery to heading cross-functional teams, managing multi-project portfolios, and "
    "driving organisation-wide digital transformation across healthcare-tech and BFSI. Currently serving "
    "as Senior Technical Operations Manager at EPC Tech, I own a portfolio of 20+ AI and automation "
    "initiatives, aligning technology strategy with business objectives across BU, HR, Product, and "
    "external stakeholders. Known for translating complex operational problems into scalable, AI-led "
    "solutions with a consistent track record of measurable impact and a deep commitment to ethical, "
    "purposeful technology."
)

STATS = [
    {"value": "10+",    "label": "Years of Experience"},
    {"value": "20+",    "label": "Projects Owned"},
    {"value": "80–90%", "label": "Manual Effort Reduced"},
    {"value": "~98%",   "label": "AI Solution Accuracy"},
]

INDUSTRIES = [
    "Healthcare-Tech",
    "BFSI",
    "Tech Services",
]

COMPETENCIES = {
    "Leadership & Strategy": [
        "Technology Operations Leadership",
        "Digital Transformation Strategy",
        "Portfolio Management",
        "Stakeholder Management",
        "Cross-functional Team Leadership",
        "Change Management",
        "Business Technology Alignment",
    ],
    "Project Delivery": [
        "PMP",
        "Agile / Scrum",
        "SDLC",
        "Project Governance",
        "Jira & Confluence",
        "Sprint Planning",
        "Risk Management",
        "Vendor Coordination",
    ],
    "AI & Automation": [
        "AI Strategy & Implementation",
        "Workflow Automation",
        "Prompt Engineering",
        "Python",
        "LangChain",
        "LangGraph",
        "Ollama",
        "RAG",
        "Zoho Creator",
        "Claude / Anthropic APIs",
        "MCP Server",
        "Neptune DB (Gremlin)",
    ],
    "Domain Expertise": [
        "Healthcare-Tech Platforms",
        "Banking & Financial Services",
    ],
}

EXPERIENCE = [
    {
        "id": "epc-tech",
        "company": "EPC Tech Pvt. Ltd.",
        "location": "Mumbai, India",
        "title": "Senior Technical Operations Manager",
        "period": "Jul 2025 – Present",
        "sector": "Healthcare-Tech",
        "team": "20+ concurrent projects",
        "achievements": [
            "Spearhead the organisation's technology and operations strategy, owning end-to-end delivery of 20+ AI, automation, and digital transformation initiatives across BU, HR, Product, and Commercial teams.",
            "Directed the strategic rollout of ILD Connect — a regulatory-aligned digital platform — aligning legal, marketing, and BU stakeholders across multiple departments to meet compliance and go-to-market timelines.",
            "Architected and deployed 15+ automation solutions across HR, operations, and commercial functions, reducing collective manual effort by 80–90% and cutting turnaround time from hours to minutes.",
            "Championed organisation-wide AI adoption by leading the AI Refresher Video programme and driving HR legal compliance for AI use across EPC Tech employees.",
            "Represented EPC Tech at national industry events including AI in Clinical Excellence, Mumbai and GU ASCO Conference, Bangalore.",
        ],
    },
    {
        "id": "stigya",
        "company": "STIGYA",
        "location": "India (HK/US Client — Gya Labs)",
        "title": "Senior Software Engineer → Acting Project Manager",
        "period": "Jul 2022 – Sep 2024",
        "sector": "Tech Services",
        "team": "Cross-functional team of 15",
        "achievements": [
            "Promoted from Python Developer to Acting Project Manager within 8 months, recognised for technical delivery quality and client communication with an international client (Gya Labs, Hong Kong/US).",
            "Led a cross-functional team of 15 (developers, testers, UI/UX designers) with accountability for delivery timelines, requirement alignment, and client satisfaction.",
            "Established Agile delivery processes from scratch — introducing stakeholder reporting cadences, and process standardisation that improved team velocity and on-time delivery.",
            "Managed end-to-end client relationship for an automation project scraping Amazon.com product performance data and translating insights into actionable marketing inputs.",
        ],
    },
    {
        "id": "tcs",
        "company": "Tata Consultancy Services",
        "location": "India (Global Banking Clients)",
        "title": "Senior Software Engineer → Acting Tech Lead",
        "period": "Aug 2016 – Jun 2022",
        "sector": "BFSI",
        "team": "4 global banking clients · 6 years",
        "achievements": [
            "Nordea Bank (Acting Tech Lead) — Led a team of 3 engineers; owned coordination between developers and testers, managed Unix deployments, and produced monthly performance reports for senior banking stakeholders.",
            "Luminor Bank — Primary owner of the Deposit module in a Progress 4GL banking system; accountable for requirement adherence and full delivery quality.",
            "ABN AMRO — Managed daily system performance reporting and communicated code change impacts to business stakeholders across AS400 and WTX environments.",
            "Citibank US — Handled inbound credit card operations for US customers over 18 months; achieved 5/5 performance appraisal, recognised for service quality and issue resolution.",
        ],
    },
    {
        "id": "fis",
        "company": "Fidelity National Information Services (FIS)",
        "location": "Mumbai, India",
        "title": "Technical Support Representative",
        "period": "Aug 2014 – Jan 2016",
        "sector": "BFSI",
        "team": "L1/L2 Support",
        "achievements": [
            "Managed full IT support ticket lifecycle for senior associates — triaging, resolving, and escalating to hardware teams with consistent SLA adherence using CMS, Active Directory, VPN, and Change Management tools.",
            "Recognised as Best Performer for technical problem-solving efficiency and quality of stakeholder support.",
        ],
    },
]

ACHIEVEMENTS = [
    {
        "metric": "80–90%",
        "headline": "Manual Effort Eliminated",
        "context": "Architected and deployed 15+ automation solutions across HR, operations, and commercial functions at EPC Tech — cutting turnaround time from hours to minutes.",
    },
    {
        "metric": "20+",
        "headline": "AI Initiatives Owned Simultaneously",
        "context": "Currently governing a full portfolio of 20+ AI, automation, and digital transformation projects as Senior Technical Operations Manager.",
    },
    {
        "metric": "~98%",
        "headline": "AI Solution Accuracy",
        "context": "Delivered AI-led solutions with near-perfect accuracy rates, establishing benchmarks for automation quality across the organisation.",
    },
    {
        "metric": "8 months",
        "headline": "Promoted to Acting PM",
        "context": "Elevated from Python Developer to Acting Project Manager at STIGYA within 8 months — recognised for technical excellence and international client communication.",
    },
    {
        "metric": "5 / 5",
        "headline": "Performance Appraisal at Citibank US",
        "context": "Achieved a perfect performance rating across 18 months of inbound credit card operations for US customers at TCS.",
    },
    {
        "metric": "15+",
        "headline": "Team Members Led",
        "context": "Built and led cross-functional teams of developers, testers, and designers across both product and client-delivery environments.",
    },
]

EDUCATION = [
    {"degree": "MBA in Information Technology", "institution": "NMIMS, Mumbai",          "year": "2024"},
    {"degree": "ANIIT in Information Technology","institution": "NIIT",                  "year": "2014"},
    {"degree": "Bachelor of Commerce",           "institution": "K.J. Somaiya College",  "year": "2007"},
]

CERTIFICATIONS = [
    {"name": "Project Management Professional (PMP)",       "issuer": "PMI",        "year": "Apr 2026–2029", "badge": "PMP"},
    {"name": "Use AI as a Creative or Expert Partner",      "issuer": "Google",     "year": "Jun 2026",      "badge": "AI"},
    {"name": "Building Ethical AI Frameworks for PM",       "issuer": "AI CERTs®",  "year": "May 2025",      "badge": "AI"},
    {"name": "Generative AI Mindset",                       "issuer": "Outskill",   "year": "Aug 2025",      "badge": "AI"},
    {"name": "Generative AI Overview for Project Managers", "issuer": "PMI",        "year": "May 2025",      "badge": "PMI"},
    {"name": "Introduction to - Agile",                     "issuer": "Simplilearn","year": "May 2025",      "badge": "Agile"},
]
