#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief – May 20, 2026."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.colors import HexColor

DATE   = "May 20, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-20.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B06000")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
    base = getSampleStyleSheet()
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
        "sub_lbl":     ParagraphStyle("sub_lbl", fontSize=9, textColor=HexColor("#404040"),
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
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
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
        ("BACKGROUND", (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    novelty_color = GREEN if "New" in novelty else AMBER
    tag_para = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=novelty_color,
        leading=11, borderPadding=3))
    reg_para = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
        "play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "", play_para, ""]],
        colWidths=[42*mm, 44*mm, 8*mm, 76*mm]
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

    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 ──────────────────────────────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "Nexus Global Payments Issues Tender for Technical Operator — Live Implementation Clock Running",
            "what": (
                "Nexus Global Payments (NGP), the Singapore-incorporated entity established by BIS and "
                "five central bank partners (MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of "
                "Thailand), has issued a formal Invitation to Tender for its Nexus Technical Operator — "
                "the entity that will build, operate, and maintain the multilateral instant cross-border "
                "payment network. The operator selection marks the decisive operational step toward live "
                "implementation, with the platform now targeting go-live across five IPS networks by "
                "2026-end and full country onboarding by mid-2027. When live, the scheme will serve "
                "1.7 billion people with sub-60-second cross-border settlement."
            ),
            "why": [
                "The tender crystallises the governance and commercial model: the Technical Operator will be a contracted private entity, not a central bank function — a significant market structure signal for infrastructure vendors and PSPs.",
                "Any PSP seeking early Nexus connectivity must now track which entity wins the operator role, as it determines technical standards, API specifications, and integration timelines.",
                "Project Nexus is the only multilateral instant cross-border payment scheme entering live operation globally — bilateral linkages (e.g. PayNow-UPI) will operate in parallel but at smaller scale and narrower corridor scope.",
                "For Singapore-based payment firms, this is a structural expansion of the accessible addressable market for A2A cross-border flows: one connection to Nexus reaches India, Malaysia, Philippines, and Thailand instantly.",
            ],
            "region": "Singapore / Asia-Pacific",
            "players": "NGP, BIS, MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, Technical Operator bidders",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "UAE Open Finance Goes Live — Ziina Executes First Customer-Initiated A2A Payment via CBUAE Framework",
            "what": (
                "Lean Technologies and Ziina have announced the first live customer-initiated Open Finance "
                "payment in the UAE under the Central Bank of the UAE's Open Finance framework. Ziina app "
                "users can now complete instant, account-to-account bank payments through regulated Open "
                "Finance APIs that connect directly to their bank accounts — bypassing card rails entirely. "
                "This milestone, coming approximately six months after the CBUAE's Open Finance Regulation "
                "came into force, represents the first real-world transaction proof of the UAE's centralized "
                "API hub model, which provides a single secure connection across the entire banking and "
                "insurance market."
            ),
            "why": [
                "The UAE has become the first country globally to implement a consolidated trust-framework and centralised API hub for open finance — this live transaction demonstrates the model is operationally viable, not just regulatory architecture.",
                "The CBUAE's Financial Infrastructure Transformation Programme is now reported as 85% complete; live Open Finance payments bring the programme's commercial impact into the consumer economy for the first time.",
                "A2A payment flows via Open Finance APIs structurally threaten card interchange economics in the UAE. Acquirers, card networks, and digital wallet providers operating in the GCC should model scenario impact.",
                "For PSPs building regional GCC infrastructure, the UAE's central hub model is more scalable than bilateral open-banking integrations — it creates a single connection to all participating UAE banks.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Lean Technologies, Ziina, UAE banks",
            "tag": "Open Finance / RTP / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "ISO 20022 Structured Address Deadline — 65% of Messages Still Non-Compliant with November 2026 Hard Cutoff",
            "what": (
                "SWIFT has confirmed that as of May 2026, approximately 65% of cross-border payment messages "
                "still contain unstructured postal address data, despite the November 14, 2026 hard deadline "
                "for structured addresses across CBPR+ and key Payment Market Infrastructures. After this "
                "date, payments with unstructured address fields will no longer be processed, creating direct "
                "operational disruption risk for non-compliant banks and their corporate clients. Minimum "
                "compliance requires at minimum structured Town Name and Country fields; fully structured "
                "addresses are the preferred standard."
            ),
            "why": [
                "With six months remaining and 65% of message volume still non-compliant, the industry is at acute operational risk of widespread payment failures in November 2026 — this is not a fringe compliance gap.",
                "Banks with large SME and retail cross-border transaction volumes face the most exposure, as corporate treasury clients are typically better prepared than transactional banking customers.",
                "Structured address data is a prerequisite for high-quality sanctions screening and AML transaction monitoring — November 2026 compliance doubles as a risk management inflection point, not merely a format change.",
                "ERP and TMS vendors must urgently confirm their ISO 20022 address capture upgrades are production-ready, as corporate payment file generation is often the weakest link in the data quality chain.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, global correspondent banks, corporate treasuries, TMS/ERP vendors, payment factories",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — non-compliance gap materially wider than expected",
        },
        {
            "num": "4.",
            "headline": "US RTP Volume Surges — TCH Reports $1.3 Trillion in 2025, Cross-Border Expansion Confirmed",
            "what": (
                "The Clearing House's RTP Network processed $1.3 trillion in 2025 — a 428% increase year-on-year "
                "— partly driven by the transaction limit increase from $1 million to $10 million in February 2025. "
                "FedNow, with approximately 1,700 member institutions, processed over $850 billion in 2025, up more "
                "than 2,100% from the prior year. US RTP transaction volumes are projected at 8 billion in 2026 and "
                "13.9 billion by 2028. TCH has confirmed the RTP Network will add cross-border payment capability "
                "in the near term, directly competing with SWIFT and digital-asset cross-border rails for USD "
                "settlement legs."
            ),
            "why": [
                "The volume acceleration is structural, not cyclical — payroll, insurance disbursements, gig economy payments, and supplier payments are all migrating to real-time rails, creating durable transaction flow shifts.",
                "FedNow's 2,100% volume growth indicates a base-building phase is completing; the network is now approaching scale where B2B use cases (treasury, liquidity management) become commercially attractive.",
                "RTP's cross-border expansion, combined with the Federal Reserve's earlier CBPR+ proposal, signals that the domestic-to-international rail boundary is dissolving for USD — with significant implications for correspondent banking economics.",
                "PSPs offering US dollar cross-border payments need a clear 12-18 month competitive positioning strategy against a world where RTP provides real-time domestic USD settlement as the anchor leg.",
            ],
            "region": "United States",
            "players": "The Clearing House (TCH), Federal Reserve (FedNow), US banks, PSPs, corporate treasuries",
            "tag": "RTP / Cross-Border / Market Structure",
            "novelty": "Follow-up with material update — cross-border expansion confirmed",
        },
        {
            "num": "5.",
            "headline": "GENIUS Act Implementation Underway — US Stablecoin Issuers Enter Compliance Build Phase",
            "what": (
                "Following the signing of the GENIUS Act (Guiding and Establishing National Innovation for "
                "U.S. Stablecoins) in July 2025, US stablecoin issuers are now in active compliance build "
                "phase. The Act requires 100% reserve backing with liquid USD-denominated assets, monthly "
                "public reserve disclosures, and full AML/sanctions program compliance. Secondary legislation "
                "and implementing rules from US regulators are expected by mid-2026. Globally, the US, EU "
                "(MiCA), UK, Singapore, UAE, and Japan have now converged on full reserve backing, licensed "
                "issuers, and guaranteed redemption as the core stablecoin regulatory framework — narrowing "
                "the gap between stablecoins and e-money regulation significantly."
            ),
            "why": [
                "Global regulatory convergence on stablecoin standards transforms the competitive landscape: compliant, fully-reserved stablecoins are now regulated payment instruments, not crypto experiments — opening institutional adoption pathways.",
                "MiCA's stablecoin provisions are fully live since December 2024; GENIUS Act puts the US on a parallel compliance trajectory by mid-2026, enabling interoperable stablecoin payment flows between the world's two largest financial markets.",
                "Payment institutions building stablecoin settlement infrastructure (B2B cross-border, treasury, liquidity) now have regulatory certainty in all major jurisdictions — reducing the primary barrier to institutional deployment.",
                "For banks, the key strategic question is whether to issue proprietary stablecoins, partner with compliant issuers, or integrate stablecoin rails into existing payment orchestration — each path has materially different infrastructure implications.",
            ],
            "region": "Global / United States / Europe",
            "players": "US Federal regulators, Circle, Tether, major bank issuers, MiCA-regulated EMIs, GENIUS Act implementation bodies",
            "tag": "Stablecoins / Regulation / Market Structure",
            "novelty": "Follow-up with material update — global regulatory convergence confirmed",
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
            "headline": "NAB Acquires UK Fintech Banked — Pay by Bank Infrastructure Moves Inside a Major Bank",
            "what": (
                "National Australia Bank (NAB) has acquired London-based fintech Banked, which developed a "
                "Pay by Bank and payment orchestration platform enabling customers to pay merchants directly "
                "from their bank accounts, delivering real-time settlement at lower processing costs. The "
                "acquisition gives NAB direct ownership of A2A payment infrastructure and accelerates its "
                "open banking payment capability across the Australian and UK markets."
            ),
            "why": (
                "This acquisition is a clear signal that major banks are choosing to own A2A payment "
                "infrastructure rather than partner with it — reflecting the strategic value now assigned to "
                "open banking payment rails. For fintech PSPs, the bank-as-acquirer trend compresses the "
                "independent infrastructure layer. For merchants, bank-owned Pay by Bank products bring "
                "institutional distribution and trust to what has been a fragmented market."
            ),
            "strategic": "Bank consolidation of A2A/open banking infrastructure is accelerating — independent fintech payment orchestration players face a shrinking addressable market.",
        },
        {
            "num": "2.",
            "headline": "UK HM Treasury Payments Forward Plan — 3-Year A2A Roadmap Formalises Regulatory Commitment",
            "what": (
                "The UK Government's HM Treasury Payments Forward Plan (February 2026) established a "
                "three-year regulatory roadmap to position account-to-account (A2A) payments as a "
                "ubiquitous UK payment method. The plan commits to supporting the UK Payment Infrastructure "
                "(UKPI) with first live payments expected in early 2026, and explicitly names A2A as a "
                "strategic priority alongside card modernisation and the New Payments Architecture (NPA). "
                "Bizum Pay's first European A2A NFC wallet is also targeting launch in Q2-Q3 2026, "
                "extending A2A to in-store point-of-sale for the first time at scale."
            ),
            "why": (
                "HM Treasury's formal 3-year A2A roadmap removes the largest residual uncertainty about "
                "whether A2A will receive sustained regulatory backing in the UK — a critical market where "
                "card network economics have historically resisted disruption. Combined with SEPA Instant "
                "mandatory adoption in Europe and live Open Finance payments in the UAE, Q2 2026 may be "
                "the inflection quarter where A2A payments move from regulatory promise to infrastructure "
                "reality across the three most important payment geographies outside Asia."
            ),
            "strategic": "A2A payment infrastructure is simultaneously going live in UAE, Europe, and UK — the multi-market convergence is a once-in-a-decade structural shift for payment product leaders to position against.",
        },
        {
            "num": "3.",
            "headline": "Embedded Finance Infrastructure Reaches $197bn — B2B APIs Capture Outsized Value",
            "what": (
                "The embedded finance market has grown to a projected $197bn in 2026 (from $148bn in 2025), "
                "maintaining a ~31% CAGR through 2034. Value concentration has shifted decisively to "
                "B2B infrastructure — payments APIs, compliance-as-a-service, embedded lending tooling, "
                "and treasury orchestration platforms — rather than consumer-facing distribution. "
                "2025 recorded the highest-ever fintech M&A transaction count; 2026 is characterised by "
                "consolidation and execution, with large institutions acquiring or absorbing fintech "
                "infrastructure players."
            ),
            "why": (
                "The shift from consumer fintech to infrastructure fintech redefines where margin pools "
                "accrue. Platform-layer players — BaaS, orchestration, compliance APIs — are capturing "
                "value previously held in distribution. The bank-acquisition trend (NAB/Banked being one "
                "example) reflects institutional recognition that API-layer infrastructure is a durable "
                "strategic asset, not a vendor service."
            ),
            "strategic": "Infrastructure fintech is now the primary value-capture layer — payments product leaders should evaluate build vs. buy decisions against a background of accelerating bank consolidation.",
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
            "▶  A2A payments are simultaneously going live in three major non-Asian markets — this is a structural inflection, not a trend.",
            "In the same quarter: UAE executes its first live Open Finance A2A transaction under CBUAE's "
            "centralised hub model; the UK formalises a 3-year A2A-as-ubiquitous-payment regulatory roadmap; "
            "SEPA Instant mandatory adoption matures in Europe. Combined with Nexus operationalising in "
            "Asia-Pacific, this represents the broadest simultaneous advance of A2A payment infrastructure in "
            "the payments industry's history. Card network economics face credible structural pressure in "
            "multiple major markets simultaneously for the first time."
        ),
        (
            "▶  Real-time rails are crossing borders — the distinction between domestic IPS and cross-border infrastructure is dissolving.",
            "Project Nexus tendering for its Technical Operator, the US RTP Network confirming cross-border "
            "capability, and FedNow's prior cross-border regulatory proposal collectively signal that "
            "domestically-designed instant payment systems are aggressively extending their perimeters. "
            "This creates a new category of competitive pressure on SWIFT CBPR+, card cross-border rails, "
            "and specialist cross-border PSPs — particularly for the USD and ASEAN currency corridors."
        ),
        (
            "▶  Stablecoin regulation is converging globally — institutional payment deployment is now a compliance question, not a policy one.",
            "With the US GENIUS Act in implementation, MiCA fully live, and Singapore, UAE, UK, and Japan all "
            "operating reserve-backed stablecoin frameworks, the global regulatory perimeter for payment "
            "stablecoins is effectively closed. The remaining uncertainty is implementation detail, not "
            "whether stablecoins will be regulated. For payment firms, this shifts the strategic question "
            "from 'will regulation happen' to 'how do we build stablecoin settlement into our platform "
            "architecture.'"
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
            "1.  Start Nexus integration planning now — the operator selection determines your technical entry point.",
            "The Nexus Technical Operator tender will produce a winner within months. Once selected, the "
            "operator sets the API standards, compliance framework, and integration specs for the entire "
            "multilateral network. PSPs operating in or targeting ASEAN+India corridors should be in active "
            "dialogue with potential operator bidders and be building internal FX liquidity and compliance "
            "architecture for five-corridor simultaneous settlement. The mid-2027 live window is "
            "infrastructure-build time, not commercial-readiness time."
        ),
        (
            "2.  The ISO 20022 structured address gap is your most immediate operational risk this year.",
            "65% non-compliance with six months to the November 14 deadline is a risk management emergency, "
            "not a project milestone. Prioritise a complete audit of your payment message generation pipeline "
            "and your corporate clients' payment file formats. Build a structured address validation service "
            "as a screening gate upstream of SWIFT submission. Institutions that invest in data enrichment "
            "now will also generate compounding AML and sanctions screening benefits — turning a compliance "
            "cost into a risk capability advantage."
        ),
        (
            "3.  Stablecoin payment architecture decisions need to be made in 2026, not 2027.",
            "With global regulatory convergence effectively complete, the window for early-mover institutional "
            "stablecoin payment positioning is open now. Determine your firm's posture: issuer, integrator, "
            "or platform. For cross-border treasury and B2B settlement use cases, regulated stablecoins "
            "are already operationally viable in MiCA and GENIUS Act jurisdictions. Waiting for further "
            "regulatory clarity is no longer a defensible delay — the clarity has arrived."
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
            "●  Nexus Technical Operator selection — outcome expected Q3 2026.",
            "The winner of the Nexus Technical Operator tender will become the most strategically important "
            "new payments infrastructure player in Asia-Pacific. Watch for announcements from established "
            "infrastructure vendors, payment scheme operators, and technology providers. The selection will "
            "confirm the technical architecture and commercial model for multilateral instant cross-border "
            "settlement serving 1.7 billion people."
        ),
        (
            "●  CBUAE September 16, 2026 licensing deadline — wave of open finance applications incoming.",
            "Open finance providers and virtual asset payment services newly brought into CBUAE licensing "
            "scope under Federal Decree-Law No. 6 of 2025 must regularise by September 16. Watch for a "
            "surge of license applications and potential enforcement actions against non-compliant operators "
            "in the UAE market. The deadline also signals CBUAE's appetite to extend regulatory perimeter "
            "to embedded finance and digital asset payment players across the GCC."
        ),
        (
            "●  US RTP cross-border launch timeline and partner announcement — TCH expected to confirm Q3 2026.",
            "The Clearing House's confirmation of RTP cross-border capability has created market expectation "
            "of a partner announcement and launch timeline in mid-2026. Watch for named correspondent banking "
            "or specialist PSP intermediaries, the corridors targeted for initial activation, and whether "
            "the USD 10 million transaction limit applies to cross-border flows. This is the defining "
            "domestic-to-international RTP architecture decision for USD corridors."
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
        "regulatory releases, scheme operator announcements, and reputable financial media. It is intended "
        "for informational purposes only and does not constitute investment, legal, or regulatory advice. "
        "Key sources: BIS (bis.org), MAS (mas.gov.sg), CBUAE (centralbank.ae / rulebook.centralbank.ae), "
        "SWIFT (swift.com), HM Treasury (gov.uk), PYMNTS, The Payments Association, Fintech News Singapore, "
        "Fintech News Middle East, The Asian Banker, Global Government Fintech, American Banker, Wamda, "
        "Red Compass Labs, FXC Intelligence, BVNK, Blockchain Council.",
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
