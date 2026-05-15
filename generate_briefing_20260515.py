#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 15, 2026."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.platypus import PageBreak
from reportlab.lib.colors import HexColor

DATE   = "May 15, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-15.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
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
         [reg_para, "", play_para, ""]],
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

    # ── SECTION 1 ─────────────────────────────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": (
                "TCH RTP Network Breaks Single-Day Records on May Day; "
                "September 2026 Cross-Border Milestone Confirmed"
            ),
            "what": (
                "The Clearing House's RTP network processed 2.27 million transactions valued at "
                "$8.62 billion on May 1, 2026 — both new single-day records. Tax refund "
                "disbursements via the network rose 78% in the first four months of 2026 versus "
                "the same period in 2025, reflecting accelerating adoption for high-value, "
                "time-sensitive treasury and disbursement use cases. TCH simultaneously confirmed "
                "that domestic-correspondent-bank activity — the precursor to full cross-border "
                "capability — will launch in September 2026, building on the existing IXB pilot "
                "with Europe's EBA Clearing."
            ),
            "why": [
                "The 78% surge in tax disbursements signals that government and institutional use cases are finally scaling on RTP — a critical inflection point for B2B and B2G payment flows.",
                "The September 2026 correspondent-bank activation is a structural milestone: it creates the domestic-side settlement architecture needed for international RTP flows, directly competing with correspondent banking FX legs.",
                "Combined with FedNow's cross-border proposal (public comment window closing June 7), the U.S. is moving simultaneously on two RTP cross-border vectors — creating a complex, parallel competitive landscape.",
                "For treasury and cash management platforms, the volume data validates RTP as a credible rail for large-value corporate and portfolio-rebalancing use cases, not just consumer P2P.",
            ],
            "region": "United States",
            "players": "The Clearing House (TCH), EBA Clearing, U.S. financial institutions, corporate treasurers",
            "tag": "RTP / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": (
                "ECB's Lagarde Warns of 'Digital Dollarisation' from USD Stablecoins; "
                "Calls for CBDC-Anchored Public Infrastructure"
            ),
            "what": (
                "In a May 8 keynote, ECB President Christine Lagarde warned that the $310 billion "
                "USD stablecoin market — dominated by Tether (USDT) and Circle (USDC) — poses a "
                "direct threat to Europe's monetary sovereignty through 'digital dollarisation.' "
                "Lagarde called on EU policymakers to prioritize public tokenized infrastructure "
                "anchored in central bank money rather than promoting privately issued euro-pegged "
                "stablecoins, positioning the ECB's digital euro as the correct institutional "
                "response. Her stance diverges explicitly from the Bundesbank, which has expressed "
                "greater openness to privately issued euro stablecoins under MiCA."
            ),
            "why": [
                "The ECB-Bundesbank split on euro stablecoins reflects a substantive policy fracture within the eurozone — with real implications for MiCA licensing, market entry, and product strategy for stablecoin issuers.",
                "Lagarde's 'digital dollarisation' framing is being adopted by a growing number of non-U.S. central banks, building momentum for CBDC-first regulatory frameworks that constrain private stablecoin payment use.",
                "For PSPs and fintechs operating in Europe, regulatory clarity on stablecoin payment utility is now deferred to the digital euro timeline (ECB targeting 2029), creating a multi-year uncertainty window.",
                "The speech signals the ECB will resist permitting large USD stablecoins to function as payment infrastructure in the eurozone — with potential implications for MiCA enforcement priorities.",
            ],
            "region": "Europe / Global",
            "players": "ECB, Christine Lagarde, Tether, Circle, Bundesbank, EU member states, MiCA-licensed issuers",
            "tag": "Stablecoins / Regulation / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": (
                "Brazil's Central Bank Bans Crypto Settlement in Regulated Cross-Border Payments "
                "(BCB Resolution No. 561)"
            ),
            "what": (
                "Banco Central do Brasil (BCB) published Resolution No. 561 on April 30, 2026, "
                "amending the eFX regulatory framework to explicitly prohibit the use of stablecoins, "
                "bitcoin, or other cryptocurrencies as settlement instruments within Brazil's regulated "
                "electronic foreign exchange system. The ban targets fintechs and payment firms using "
                "crypto rails on the back-end of cross-border remittances and international transfers. "
                "Individual holdings and direct crypto investments remain unaffected; the ban applies "
                "specifically to the institutional settlement layer of regulated cross-border flows."
            ),
            "why": [
                "Brazil's eFX system is one of the most active cross-border payment corridors in Latin America — this ban directly closes a channel used by fintechs to offer faster or cheaper international transfers via crypto rails.",
                "The move creates competitive asymmetry: fintechs that built cost advantages through stablecoin settlement must now rebuild on traditional FX rails, potentially eroding speed and cost advantages.",
                "Brazil's action contrasts sharply with Tetra Digital and other players using stablecoins as an invisible bridge between RTP networks — illustrating the global regulatory divergence in stablecoin payment use.",
                "PSPs with Latin American corridors should monitor whether other BCB trading partners (Argentina, Colombia, Mexico) follow with similar eFX restrictions under pressure from financial stability concerns.",
            ],
            "region": "Brazil / Latin America",
            "players": "Banco Central do Brasil (BCB), eFX providers, cross-border fintechs, remittance platforms",
            "tag": "Regulation / Cross-Border / Stablecoins",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": (
                "Singapore SPaN Confirms End-2026 Operational Timeline — "
                "All D-SIBs Join as Founding Members"
            ),
            "what": (
                "The Singapore Payments Network (SPaN), incorporated by MAS and the Association of "
                "Banks in Singapore (ABS) as a not-for-profit company, has confirmed its target of "
                "being operationally ready by the end of 2026. SPaN will consolidate governance of "
                "Singapore's eight national payment schemes — including FAST, GIRO, PayNow, and SGQR "
                "— currently fragmented across the Singapore Clearing House Association (SCHA), ABS, "
                "MAS, and Infocomm. All seven Domestic Systemically Important Banks (DBS, OCBC, UOB, "
                "HSBC, Citibank, Maybank, and Standard Chartered) have been confirmed as founding "
                "members alongside MAS."
            ),
            "why": [
                "Consolidating eight payment schemes under a single governance entity is a structural rationalization that reduces fragmentation risk and creates a unified upgrade path for Singapore's payment infrastructure.",
                "SPaN's mandate explicitly covers cross-border payment schemes — positioning it as the institutional counterpart to Project Nexus and bilateral payment linkages as they scale toward 2027.",
                "The D-SIB membership composition gives SPaN broad banking system buy-in from day one, reducing the adoption friction that has hampered similar governance reforms in other markets.",
                "End-2026 operational readiness aligns SPaN's governance capacity with the critical Phase 2 of Project Nexus and the expected expansion of PayNow-linked cross-border corridors.",
            ],
            "region": "Singapore",
            "players": "MAS, ABS, DBS, OCBC, UOB, HSBC, Citibank, Maybank, Standard Chartered, SPaN",
            "tag": "Infrastructure / Market Structure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "5.",
            "headline": (
                "Cross-Border Payments Hit a 'Data Border' Bottleneck — "
                "Speed Gains Undermined by Structured Data Gaps"
            ),
            "what": (
                "New analysis from BIS, PYMNTS, and FXC Intelligence highlights that cross-border "
                "payment rails are now fast enough to settle in near-real-time, but a growing "
                "'data border' problem is creating friction at the compliance, sanctions screening, "
                "and reconciliation layer. Unstructured address data, inconsistent beneficiary "
                "information formatting, and mismatched ISO 20022 adoption depth across jurisdictions "
                "are generating false-positive compliance holds, manual intervention queues, and "
                "settlement delays that negate speed improvements at the rail level. The FSB and BIS "
                "G20 cross-border payments roadmap identifies this as a Tier 1 structural barrier."
            ),
            "why": [
                "The 'data border' insight reframes the cross-border payments problem: the bottleneck is no longer settlement speed, it is data quality, structure, and interoperability between jurisdictions.",
                "ISO 20022 structured address requirements (November 2026 deadline) are the most immediate lever — but adoption depth varies significantly, meaning compliance-rich corridors will outperform data-poor ones.",
                "For PSPs and banks building cross-border payment products, investing in upstream data enrichment and structured messaging pipelines now creates compounding advantage in STP rates and compliance cost reduction.",
                "This dynamic also explains why FX and sanctions screening vendors are seeing demand surge — the speed of rails is revealing the slowness of the compliance layer, not removing it.",
            ],
            "region": "Global",
            "players": "BIS, FSB, SWIFT, cross-border PSPs, sanctions screening vendors, correspondent banks",
            "tag": "Cross-Border / Infrastructure / Fraud-Risk",
            "novelty": "New today",
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

    # ── SECTION 2 ─────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": (
                "Payward Acquires Reap in $600M Deal — "
                "Crypto Infrastructure Moves into B2B Payments"
            ),
            "what": (
                "Payward (Kraken's parent) agreed to acquire Reap, a B2B payments and "
                "corporate card infrastructure provider, in a $600 million cash-and-stock "
                "deal in May 2026. Reap enables businesses — particularly in Asia — to issue "
                "corporate cards, manage multi-currency accounts, and make cross-border payments "
                "using a combination of traditional and crypto-adjacent rails. The deal represents "
                "one of the largest crypto-to-payments infrastructure M&amp;A transactions in the "
                "Asia-Pacific region."
            ),
            "why": (
                "The acquisition signals a strategic pivot by crypto-native platforms toward "
                "regulated B2B payment infrastructure — specifically in corridors where Reap "
                "has existing client relationships and regulatory footprints. For traditional "
                "PSPs and corporate payment providers in Asia, this creates a new class of "
                "well-capitalized competitor with a hybrid crypto-traditional product stack. "
                "It also validates the 'B2B payments + digital asset rails' thesis at meaningful scale."
            ),
            "strategic": (
                "Crypto-native platforms acquiring regulated payments infrastructure is accelerating "
                "competitive pressure on traditional B2B payment providers in Asia."
            ),
        },
        {
            "num": "2.",
            "headline": (
                "UK Fintech Adfin Raises $18M Series A — "
                "Request-to-Pay Infrastructure Gains Investor Backing"
            ),
            "what": (
                "London-based Adfin closed an $18 million Series A round to expand its "
                "request-to-pay (R2P) and account-to-account (A2A) payment infrastructure "
                "platform. Adfin connects billers, merchants, and consumers via open banking "
                "payment initiation, with a focus on recurring billing, invoicing, and "
                "subscription payment workflows. The round comes as the UK's Pay.UK R2P "
                "scheme continues to gain traction and open banking payment volumes grow."
            ),
            "why": (
                "R2P infrastructure is maturing from a scheme-level concept into a fundable, "
                "scalable product category. Adfin's focus on billers and recurring payments "
                "targets one of the most defensible A2A use cases — where card rails still "
                "dominate but A2A unit economics are structurally superior for high-frequency "
                "recurring transactions. For payments product leaders, this signals that R2P "
                "infrastructure is crossing the early-adopter threshold in the UK market."
            ),
            "strategic": (
                "R2P is graduating from scheme experimentation to funded infrastructure — "
                "biller-side adoption is the current growth wedge."
            ),
        },
        {
            "num": "3.",
            "headline": (
                "Embedded Finance Hits $197 Billion in 2026 — "
                "Infrastructure Layer Capturing Outsized Margin"
            ),
            "what": (
                "The embedded finance market has grown from $148 billion in 2025 to an estimated "
                "$197 billion in 2026, maintaining a ~31% CAGR. Growth is concentrated in "
                "B2B infrastructure — payments APIs, compliance-as-a-service, and embedded "
                "lending tooling — rather than consumer-facing neobank distribution. The year "
                "is tracking as an execution and consolidation cycle, with the highest-ever "
                "fintech M&amp;A transaction count recorded in 2025 carrying through into 2026."
            ),
            "why": (
                "The concentration of embedded finance growth in the infrastructure and API "
                "layer — not consumer distribution — confirms that margin pools in fintech are "
                "migrating to platform and orchestration players. For payments product leaders, "
                "this is a signal that platform-layer positioning (BaaS, orchestration, compliance "
                "APIs) is becoming a structural moat rather than an operational enabler. "
                "Consolidation among smaller BaaS providers is creating M&amp;A opportunity "
                "for well-capitalized infrastructure players."
            ),
            "strategic": (
                "Infrastructure-first embedded finance is outpacing consumer neobanks as the "
                "primary value-capture and M&amp;A target layer in 2026."
            ),
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

    # ── SECTION 3 ─────────────────────────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Speed is solved. The new cross-border payments bottleneck is data quality.",
            "Rails — domestic RTP, SWIFT gpi, Project Nexus — are now fast enough to settle "
            "in near-real-time for most corridors. The emerging constraint is structured data: "
            "unformatted beneficiary information, unstructured addresses, and mismatched "
            "ISO 20022 adoption depths are creating compliance holds that negate rail-level speed "
            "improvements. The data enrichment and structured messaging layer is where cross-border "
            "payment product differentiation will now be fought."
        ),
        (
            "▶  Global stablecoin regulation is fracturing along geopolitical lines.",
            "The ECB-Bundesbank divergence on euro stablecoins, Brazil's eFX ban, MAS's PFMI "
            "stance from April, and the U.S. GENIUS Act's permissive approach are producing "
            "fundamentally different stablecoin payment frameworks across major markets. "
            "Firms building stablecoin payment products face a patchwork of jurisdiction-specific "
            "constraints — not a unified global regime. Corridor-by-corridor regulatory mapping "
            "is now a first-order product requirement."
        ),
        (
            "▶  Singapore is assembling an end-to-end payments infrastructure stack for 2027.",
            "SPaN (governance), Project Nexus (multilateral cross-border), and MAS's regulatory "
            "framework (PFMI standards for stablecoins, MPI licensing) are converging into a "
            "coherent national payments architecture targeting 2026-2027 operationalization. "
            "No other jurisdiction is moving this comprehensively across governance, infrastructure, "
            "and regulation simultaneously — reinforcing Singapore's position as Asia-Pacific's "
            "payment infrastructure anchor."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4 ─────────────────────────────────────────────────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Invest in structured data pipelines now — they are becoming the primary "
            "cross-border performance lever.",
            "The 'data border' bottleneck means that rail speed is no longer the differentiator. "
            "PSPs and banks with clean, structured, ISO 20022-compliant beneficiary data will "
            "achieve materially higher STP rates, lower false-positive compliance holds, and "
            "faster settlement confirmation. This is a product and engineering investment decision "
            "that pays compound returns — build the enrichment capability before the November 2026 "
            "structured address deadline forces it reactively."
        ),
        (
            "2.  Build a stablecoin regulatory map before building a stablecoin payment product.",
            "With Brazil banning crypto settlement, the ECB opposing private stablecoins in the "
            "eurozone, MAS requiring PFMI standards, and the U.S. moving permissively via the "
            "GENIUS Act, any stablecoin-enabled cross-border payment product requires corridor-by-"
            "corridor regulatory analysis before architecture decisions are locked. Teams assuming "
            "a global stablecoin payment strategy will work uniformly are building on sand."
        ),
        (
            "3.  Treat Singapore's SPaN and Nexus convergence as a 2027 platform commitment date.",
            "With SPaN targeting end-2026 operational readiness and Project Nexus live "
            "implementation for 2027, PSPs operating in ASEAN or with exposure to Singapore, "
            "India, Malaysia, Thailand, or Philippines corridors now have a concrete platform "
            "timeline to plan against. The technical integration, FX liquidity, and compliance "
            "architecture decisions that need to be made now will determine whether your firm is "
            "a first-wave participant or a catch-up player in 2027."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 ─────────────────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  FedNow Cross-Border Public Comment Period Closes June 7, 2026.",
            "The Federal Reserve's proposal to amend Regulation J Subpart C — enabling "
            "non-Fed intermediaries to handle cross-border FedNow legs — closes for public "
            "comment on June 7. Watch for intermediary positioning announcements from major "
            "correspondent banks, Visa, Mastercard, and specialist cross-border PSPs. "
            "The comment responses will reveal which institutions are positioning as FedNow "
            "cross-border intermediaries and what the competitive architecture will look like."
        ),
        (
            "●  TCH RTP Domestic-Correspondent Activation — September 2026.",
            "The September 2026 launch of correspondent-bank activity on the RTP network "
            "is the structural stepping stone to full cross-border capability. Watch for "
            "announcements of which correspondent banks have enrolled, pricing structures, "
            "and whether TCH-EBA IXB pilot volumes accelerate following activation. "
            "This will also signal whether RTP becomes a credible SWIFT alternative for "
            "USD cross-border flows."
        ),
        (
            "●  UAE CBUAE Licensing Deadline for Open Finance and VA Payment Firms — September 16, 2026.",
            "The six-month window for newly in-scope open finance providers and virtual asset "
            "payment services to regularise under CBUAE's Federal Decree-Law No. 6 of 2025 "
            "closes in September 2026. Watch for a wave of MPI/RPS license applications, "
            "potential enforcement actions against non-compliant operators, and consolidation "
            "among smaller UAE-based payment and crypto firms unable to meet capital and "
            "governance requirements."
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
        "regulatory releases, and reputable financial media. It is intended for informational and "
        "educational purposes only and does not constitute investment, legal, or regulatory advice. "
        "Key sources used in today's edition: The Clearing House (theclearinghouse.org), "
        "ECB (ecb.europa.eu), Banco Central do Brasil (bcb.gov.br), MAS (mas.gov.sg), "
        "BIS (bis.org), PYMNTS, American Banker, Fintech Futures, FXC Intelligence, Payment Expert, "
        "CoinDesk, The Payments Association.",
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
