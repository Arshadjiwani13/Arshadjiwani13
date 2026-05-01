#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 1, 2026."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.colors import HexColor

DATE   = "May 1, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-01.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
    return {
        "cover_title": ParagraphStyle("cover_title", fontSize=26, textColor=WHITE,
                                      fontName="Helvetica-Bold", alignment=TA_CENTER,
                                      leading=32),
        "cover_sub":   ParagraphStyle("cover_sub",   fontSize=14, textColor=HexColor("#B4D2FF"),
                                      fontName="Helvetica",       alignment=TA_CENTER, leading=20),
        "sec_hdr":     ParagraphStyle("sec_hdr", fontSize=12, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=16, spaceBefore=6),
        "headline":    ParagraphStyle("headline", fontSize=10.5, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=14, spaceBefore=8),
        "sub_lbl":     ParagraphStyle("sub_lbl", fontSize=9,  textColor=HexColor("#404040"),
                                      fontName="Helvetica-Bold", leading=12, spaceBefore=4),
        "body":        ParagraphStyle("body", fontSize=9.5, textColor=BLACK,
                                      fontName="Helvetica", leading=13, alignment=TA_JUSTIFY,
                                      spaceBefore=2),
        "bullet":      ParagraphStyle("bullet", fontSize=9.5, textColor=BLACK,
                                      fontName="Helvetica", leading=13, leftIndent=12,
                                      bulletIndent=2, spaceBefore=1),
        "italic":      ParagraphStyle("italic", fontSize=9.5, textColor=HexColor("#333333"),
                                      fontName="Helvetica-Oblique", leading=13,
                                      leftIndent=8, spaceBefore=2, alignment=TA_JUSTIFY),
        "theme_title": ParagraphStyle("theme_title", fontSize=9.5, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=13, spaceBefore=6),
        "watchlbl":    ParagraphStyle("watchlbl", fontSize=9, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=13, spaceBefore=6),
        "footer_note": ParagraphStyle("footer_note", fontSize=7.5, textColor=MGRAY,
                                      fontName="Helvetica-Oblique", leading=11,
                                      alignment=TA_JUSTIFY, spaceBefore=6),
    }


def cover_block(s):
    tbl = Table(
        [[Paragraph("Daily Payments &amp; Fintech Intelligence Brief", s["cover_title"])],
         [Paragraph(DATE, s["cover_sub"])],
         [Spacer(1, 6*mm)]],
        colWidths=[170*mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return tbl


def section_header(number, title, s):
    tbl = Table(
        [[Paragraph(f"{number}  {title}", s["sec_hdr"])]],
        colWidths=[170*mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    tag_para = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=GREEN,
        leading=11, borderPadding=3))
    reg_para = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
        "play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "",           play_para, ""]],
        colWidths=[38*mm, 40*mm, 12*mm, 80*mm]
    )
    tbl.setStyle(TableStyle([
        ("SPAN",          (2, 1), (3, 1)),
        ("SPAN",          (2, 0), (3, 0)),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return tbl


def bullets(items, s):
    return [Paragraph(f"• &nbsp; {item}", s["bullet"]) for item in items]


def build_story(s):
    story = []

    # Cover
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 ──────────────────────────────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "Global Payments Closes $17B Worldpay Deal; FIS Acquires Issuer Solutions Unit — US Processing Landscape Permanently Redrawn",
            "what": (
                "Global Payments has completed its $17.0 billion acquisition of Worldpay, "
                "creating a refocused merchant-acquiring and gateway specialist. Simultaneously, "
                "FIS acquired Global Payments' Issuer Solutions processing unit for $13.5 billion, "
                "giving FIS a pure-play issuer processing capability to complement its existing "
                "banking and capital markets technology stack. The two deals, totaling approximately "
                "$30.5 billion, represent the largest simultaneous restructuring of US payments "
                "processing infrastructure in over a decade."
            ),
            "why": [
                "Global Payments-Worldpay creates a merchant-acquiring-focused processor with combined scale rivaling Fiserv, while FIS exits acquiring to double down on issuer processing — a deliberate unbundling of legacy conglomerate models.",
                "Merchants and PSPs evaluating acquirer relationships now face a materially changed counterparty landscape; platform consolidation timelines and pricing structures will shift as integration proceeds.",
                "FIS's standalone issuer processing unit now competes more directly with TSYS (Global Payments legacy), Fiserv, and specialist card processors — intensifying competition in a market undergoing rapid ISO 20022 and real-time payment upgrades.",
                "The combined deals signal that scale and vertical focus — not breadth — are the dominant strategic logic in 2026 payments processing consolidation.",
            ],
            "region": "United States / Global",
            "players": "Global Payments, Worldpay, FIS, Fiserv, TSYS, merchant PSPs",
            "tag": "M&A / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "UAE Digital Dirham: Five Weeks Live — mBridge Expands, Jisr Cross-Border Platform Adds New Central Bank Partners",
            "what": (
                "The Digital Dirham, the UAE's retail central bank digital currency (CBDC), "
                "has now been in live retail circulation for over five weeks since its March 2026 "
                "launch. Early deployment is concentrated in government-to-person disbursements "
                "and QR-code merchant payments. Concurrently, the CBUAE has confirmed further "
                "expansion of the mBridge wholesale tokenized settlement network — currently "
                "supporting direct settlement corridors with Saudi Arabia, China, and India — "
                "and the Jisr cross-border instant payment platform is onboarding additional "
                "central bank participants in 2026, extending instant settlement beyond the "
                "existing Gulf bilateral links."
            ),
            "why": [
                "UAE is simultaneously operating a retail CBDC, a wholesale tokenized ledger (mBridge), and a cross-border IPS (Jisr) — the most multi-layered CBDC and RTP infrastructure stack in the GCC, and among the most advanced globally.",
                "mBridge's existing corridors with China and India directly address UAE's two largest inbound remittance volumes, creating practical settlement efficiency that bypasses correspondent banking latency.",
                "Payment firms operating UAE merchant and remittance flows must now plan for API integration across CBDC, card, IPS, and mBridge rails — a more complex orchestration environment than any single-rail market.",
                "Merchant acceptance mandates for Digital Dirham have not yet been issued, but CBUAE's trajectory toward a 'full integration' target (FIT Programme) makes this a medium-term policy watch.",
            ],
            "region": "UAE / GCC / Asia",
            "players": "CBUAE, mBridge consortium, BIS Innovation Hub, participating central banks, UAE PSPs",
            "tag": "Infrastructure / Stablecoins / Cross-Border",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "3.",
            "headline": "Capital One-Discover Enters Integration Phase 2: Network Internalization Strategy Comes into Focus",
            "what": (
                "Following Federal Reserve and OCC approval of Capital One's $51.8 billion "
                "acquisition of Discover Financial Services, Capital One has begun Phase 2 "
                "integration planning with a stated focus on the Discover network — the only "
                "US credit card network wholly owned by an issuer. Capital One is evaluating "
                "routing a material portion of its own credit card volume through Discover's "
                "merchant acceptance network, which would directly reduce dependency on "
                "Visa and Mastercard interchange and network service fees."
            ),
            "why": [
                "If Capital One routes significant volume through Discover, it becomes the first US issuer in decades to materially break from the Visa/Mastercard duopoly — with direct implications for network fee income and issuer economics across the industry.",
                "Merchant acquiring and co-branded card programs face renegotiation pressure as Capital One-Discover defines its network positioning; merchants may see shifts in acceptance terms and routing dynamics.",
                "Discover's international acceptance network (including its JCB partnership) gives Capital One a latent cross-border network asset that could be repurposed for international card strategy — a significant differentiator from domestic-only ambitions.",
                "Other large US issuers will monitor Capital One's network internalization results closely; success would validate a model that others may seek to replicate or lobby against through scheme rule changes.",
            ],
            "region": "United States / Global",
            "players": "Capital One, Discover, Visa, Mastercard, merchant acquirers, card networks",
            "tag": "Market Structure / Cards",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "4.",
            "headline": "FedNow $10M Transaction Cap Unlocks B2B Instant Payments — But Interoperability with RTP Remains Unresolved",
            "what": (
                "The Federal Reserve's FedNow instant payment service now operates with a "
                "$10 million per-transaction ceiling — a significant increase from earlier "
                "limits — making it viable for commercial real estate, supply chain finance, "
                "payroll, and corporate treasury operations. Over 1,500 financial institutions "
                "across all 50 US states are now connected, with adoption concentrated among "
                "institutions above $1 billion in assets. However, FedNow and The Clearing "
                "House's RTP network continue to operate as separate, non-interoperable "
                "systems, creating a structurally fragmented US instant payments landscape "
                "that PSPs must navigate through dual-rail strategies."
            ),
            "why": [
                "The $10M transaction cap was FedNow's primary barrier to B2B adoption; its removal unlocks a substantially larger commercial payment opportunity that justifies renewed business-case investment from treasury and corporate banking product teams.",
                "Dual-rail fragmentation (FedNow at $10M vs. RTP at $1M, with no interoperability) forces PSPs to build routing logic, manage split liquidity pools, and maintain dual technical integrations — increasing operational complexity without corresponding revenue uplift.",
                "The Fed's April 2026 cross-border proposal creates a strategic arc from domestic RTP to international USD settlement; the $10M B2B limit is a prerequisite for that cross-border ambition to be credible for institutional flows.",
                "Non-US PSPs and banks with USD transaction banking ambitions should build FedNow connectivity into their US market strategy as the commercial use case becomes demonstrably viable.",
            ],
            "region": "United States",
            "players": "Federal Reserve, The Clearing House, RTP, US banks, corporate treasury PSPs",
            "tag": "RTP / Infrastructure",
            "novelty": "Escalation / broader impact today",
        },
        {
            "num": "5.",
            "headline": "SWIFT Structured Address Deadline: Six-Month Countdown Activates — Correspondent Banks Launch Client Remediation Programs",
            "what": (
                "With exactly six months remaining before SWIFT's November 2026 hard deadline "
                "for fully structured postal address data in cross-border payment messages, "
                "major correspondent banks have activated formal client data remediation "
                "programs. SWIFT will reject — not convert, not flag — payment messages "
                "containing unstructured free-text address fields from November 2026 onward. "
                "Simultaneously, MT101 multi-instruction messages face termination, with "
                "migration to pain.001 XML required. SEPA version 3.7 format changes "
                "(pain.001.001.09 and pain.008.001.08) are now mandatory across eurozone clearing."
            ),
            "why": [
                "Payment rejection — not surcharge — is the consequence from November 2026, making this the most operationally impactful SWIFT deadline in the ISO 20022 migration sequence. Corporate treasurers and ERP vendors face a hard cut-off.",
                "Correspondent banks face a dual remediation burden: upgrading their own gateway configurations and ensuring that corporate client ERP, TMS, and treasury platform integrations produce correctly structured output fields.",
                "Structured address data materially improves AML/sanctions screening precision by enabling automated, deterministic field matching rather than probabilistic free-text parsing — a direct fraud and compliance quality benefit.",
                "TMS and ERP vendors (SAP, Oracle, Kyriba, GTreasury) are seeing urgent enterprise demand for pain.001.001.09 format support; firms not already engaged in vendor certification testing face implementation risk before November.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone payment operators, correspondent banks, corporate treasury teams, TMS/ERP vendors",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation / broader impact today",
        },
    ]

    for h in headlines:
        block = []
        block.append(Paragraph(f"{h['num']}  {h['headline']}", s["headline"]))
        block.append(Paragraph("What happened:", s["sub_lbl"]))
        block.append(Paragraph(h["what"], s["body"]))
        block.append(Paragraph("Why it matters:", s["sub_lbl"]))
        block.extend(bullets(h["why"], s))
        block.append(Spacer(1, 2*mm))
        block.append(tag_row(h["tag"], h["novelty"], h["region"], h["players"], s))
        block.append(Spacer(1, 3*mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── SECTION 2 ──────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Capital One Acquires Brex for $5.15B — Incumbent Banks Move to Own Corporate Spend Management",
            "what": (
                "Capital One has reached a definitive agreement to acquire Brex, the "
                "corporate spend management and expense platform serving high-growth "
                "technology companies, for $5.15 billion. The deal is expected to close "
                "by mid-2026 and pairs Capital One's commercial banking infrastructure "
                "and balance sheet with Brex's modern API-native spend management stack, "
                "virtual card issuance, and cash management product set."
            ),
            "why": (
                "The Brex acquisition validates the B2B embedded payments thesis at scale: "
                "incumbent banks are now willing to pay premium multiples for fintech spend "
                "management platforms rather than build them organically. This signals that "
                "corporate card issuance, virtual card management, and expense orchestration "
                "have become strategic acquisitions rather than IT projects. For payments "
                "product leaders, it confirms that corporate spend management is consolidating "
                "into banking infrastructure — and that standalone B2B fintech platforms "
                "without deep distribution face an M&A-or-die strategic fork."
            ),
            "strategic": "Incumbent bank M&A of B2B fintech platforms is reshaping the corporate payments value chain — distribution now wins over pure product differentiation.",
        },
        {
            "num": "2.",
            "headline": "Embedded Finance Infrastructure Surpasses $197B — B2B API Layer Outpaces Consumer Distribution",
            "what": (
                "The global embedded finance market has reached approximately $197 billion "
                "in 2026, maintaining a compound annual growth rate above 30% through 2025. "
                "Critically, value concentration has shifted: infrastructure-layer players — "
                "payments APIs, compliance-as-a-service, embedded lending tooling, and "
                "orchestration middleware — are capturing outsized margin relative to "
                "consumer-facing neobank distribution. 2025 recorded the highest-ever "
                "fintech M&A transaction count, and 2026 is executing the consolidation "
                "cycle, with infrastructure platforms the dominant acquisition targets."
            ),
            "why": (
                "The embedded finance story has fundamentally shifted from 'which neobank "
                "will win consumers' to 'which infrastructure layer will be indispensable "
                "to banks, brands, and platforms.' This redefines where payments product "
                "investment should concentrate. Orchestration, API connectivity, and "
                "compliance-as-a-service are not commodities — they are the new strategic "
                "moat in a market where every brand wants to embed financial services "
                "without building regulated infrastructure."
            ),
            "strategic": "Platform-layer embedded finance is definitively outcompeting consumer distribution as the primary margin pool — investment strategy should follow the infrastructure, not the app.",
        },
        {
            "num": "3.",
            "headline": "Global Stablecoin Regulatory Convergence: Seven Major Economies Now Mandate Reserve Backing and Licensed Issuers",
            "what": (
                "As of May 2026, the US, EU, UK, Singapore, Hong Kong, UAE, and Japan have "
                "each enacted stablecoin payment frameworks requiring full reserve backing, "
                "licensed issuers, and guaranteed redemption rights. The convergence is "
                "broadly aligned on structure but diverges on permissible reserve assets, "
                "cross-border recognition, and systemic oversight thresholds. MAS has "
                "separately proposed applying PFMI-equivalent standards to systemically "
                "significant stablecoins — a stance that, if adopted more broadly, would "
                "subject large stablecoin networks to the same operational resilience, "
                "liquidity, and governance requirements as central market infrastructure."
            ),
            "why": (
                "Stablecoins have crossed from asset classification debates into payment "
                "infrastructure regulation. The convergence of licensing frameworks across "
                "seven major economies means that regulated stablecoin issuers now have a "
                "credible compliance pathway in most major payment markets — but the "
                "divergence on systemic thresholds and cross-border recognition creates "
                "persistent fragmentation risk for firms seeking truly global stablecoin "
                "payment utility. For PSPs and banks, this signals that stablecoin rails "
                "are entering the regulatory-certainty zone required for institutional adoption."
            ),
            "strategic": "Stablecoin regulation is mature enough for institutional product decisions — the question is no longer 'if' but 'which jurisdiction and which issuers meet the bar.'",
        },
    ]

    for h in fintech:
        block = []
        block.append(Paragraph(f"{h['num']}  {h['headline']}", s["headline"]))
        block.append(Paragraph("What happened:", s["sub_lbl"]))
        block.append(Paragraph(h["what"], s["body"]))
        block.append(Paragraph("Why it matters to fintech / payments:", s["sub_lbl"]))
        block.append(Paragraph(h["why"], s["body"]))
        block.append(Paragraph("Strategic relevance:", s["sub_lbl"]))
        block.append(Paragraph(h["strategic"], s["italic"]))
        block.append(Spacer(1, 3*mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── SECTION 3 ──────────────────────────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  US payments market structure is being permanently redrawn through M&A consolidation.",
            "The Global Payments-Worldpay-FIS triple restructuring and Capital One's simultaneous "
            "acquisition of both Discover and Brex represent a once-in-a-decade realignment of issuer, "
            "network, acquirer, and corporate spend relationships. The competitive landscape for merchant "
            "acquiring, issuer processing, and B2B payments will look materially different by end-2026 "
            "than it did at the start of the year. PSPs, merchants, and banks must reassess counterparty "
            "relationships and platform roadmaps against a new industry topology."
        ),
        (
            "▶  The GCC — and UAE specifically — is running the world's most advanced multi-layer payment modernization.",
            "The UAE's simultaneous deployment of Digital Dirham (retail CBDC), mBridge (wholesale "
            "tokenized settlement across Asia corridors), and Jisr (cross-border IPS) represents the "
            "most complex and ambitious payment infrastructure stack being operated at real-world scale. "
            "This is not pilot territory — it is live production infrastructure. Payment firms with GCC "
            "or South Asian corridor exposure must treat UAE as a multi-rail orchestration market, not "
            "a simple card or wire market."
        ),
        (
            "▶  ISO 20022 data quality is moving from compliance milestone to permanent competitive differentiator.",
            "SWIFT's November 2026 hard rejection policy for unstructured address data signals that ISO "
            "20022 is now an ongoing operational discipline, not a one-time migration. Institutions that "
            "invest in structured data enrichment pipelines, client remediation programs, and downstream "
            "ML-based fraud and sanctions benefit capture will compound those returns over years. Those "
            "treating it as a point-in-time project face rising rejection risk, surcharge exposure, and "
            "AML quality degradation."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4 ──────────────────────────────────────────────────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Reassess card acceptance and routing strategy in light of Capital One-Discover network internalization.",
            "Capital One routing its own volume through the Discover network is the most credible "
            "challenge to Visa and Mastercard's US dominance in years. If successful, it creates a "
            "case study that will pressure other large issuers to pursue similar vertical integration "
            "or renegotiate network agreements. Payments product leaders should model the implications "
            "for interchange economics, acceptance infrastructure, and scheme dependency across their "
            "own issuer or acquirer relationships — and monitor Q3 2026 for Capital One's first public "
            "volume routing disclosures."
        ),
        (
            "2.  Build a UAE multi-rail product monitoring function — the GCC is no longer a single-rail market.",
            "With Digital Dirham, mBridge, Jisr, and conventional card/IPS rails all operational "
            "in UAE, any product or platform serving UAE payment flows must now manage multi-rail "
            "orchestration, CBDC API integration planning, and real-time settlement across "
            "cross-border corridors. This is not a future consideration — it is the current operating "
            "environment. Firms without a UAE digital infrastructure roadmap are already behind. "
            "Watch specifically for CBUAE merchant acceptance mandates for Digital Dirham, which "
            "would create a compliance-driven integration deadline."
        ),
        (
            "3.  Treat FedNow's $10M B2B limit as a trigger to reopen your US instant payment use case backlog.",
            "Value limits were the primary reason B2B FedNow use cases failed business-case hurdles. "
            "With the $10M ceiling in place, commercial real estate, payroll, supply chain finance, "
            "and high-value vendor payments are now structurally viable on FedNow rails. Product "
            "leaders with US commercial banking or corporate treasury mandates should run a fresh "
            "use-case prioritisation exercise against the new limit — and build dual-rail routing "
            "logic to navigate FedNow vs. RTP based on amount, counterparty, and speed requirements."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 ──────────────────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  Visa and Mastercard response to Capital One-Discover network internalization.",
            "The card scheme duopoly will not absorb Capital One's potential volume shift passively. "
            "Watch for Visa and Mastercard network rule changes, renegotiated issuer incentive "
            "agreements, or regulatory lobbying against Discover's acceptance-rule structures. "
            "The first evidence of response is likely to emerge through Q2 and Q3 2026 earnings calls "
            "and scheme rule bulletins."
        ),
        (
            "●  CBUAE Digital Dirham merchant acceptance mandate — timing and scope.",
            "Most retail CBDCs globally have avoided mandatory merchant acceptance mandates in "
            "early phases. CBUAE's FIT Programme 'full integration' target for 2026 implies a "
            "more directive stance may follow adoption metrics. If CBUAE issues a tiered acceptance "
            "mandate for Digital Dirham — as China has done for e-CNY — it creates a compliance "
            "deadline for all UAE PSPs and acquirers, irrespective of current product roadmaps."
        ),
        (
            "●  BIS Project Nexus PSP technical rulebook — Q2 2026 publication expected.",
            "Nexus Global Payments (NGP) is expected to publish final PSP connectivity specifications "
            "and access criteria in Q2 2026. This will define exactly what technical and compliance "
            "standards PSPs must meet to connect their domestic IPS to the Nexus scheme layer — "
            "determining which firms can access sub-60-second multi-corridor settlement by 2027. "
            "Early movers on compliance alignment and API integration will have structural "
            "first-mover advantages in ASEAN and India corridors."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # Disclaimer
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, and reputable financial media. It is intended for informational purposes "
        "only and does not constitute investment, legal, or regulatory advice. Key sources: "
        "CBUAE (centralbank.ae), Federal Reserve (federalreserve.gov), MAS (mas.gov.sg), "
        "SWIFT (swift.com), BIS (bis.org), Digital Dubai (digitaldubai.ai), PYMNTS, American Banker, "
        "PwC Global M&amp;A Trends, Harvard Law School Forum on Corporate Governance, "
        "Red Compass Labs, Payment Expert, FXC Intelligence, QED Investors, Crunchbase.",
        s["footer_note"]
    ))

    return story


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MGRAY)
    canvas.drawCentredString(
        A4[0] / 2, 12*mm,
        f"Daily Payments & Fintech Intelligence Brief  |  {DATE}  |  Page {doc.page}"
    )
    canvas.setStrokeColor(SILVER)
    canvas.setLineWidth(0.3)
    canvas.line(20*mm, 15*mm, A4[0] - 20*mm, 15*mm)
    canvas.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=18*mm,  bottomMargin=20*mm,
        title=f"Daily Payments & Fintech Intelligence Brief – {DATE}",
        author="Payments Intelligence",
        subject="Daily global payments and fintech briefing"
    )
    s = build_styles()
    story = build_story(s)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    main()
