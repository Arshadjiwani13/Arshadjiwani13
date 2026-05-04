#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 4, 2026."""

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

DATE   = "May 4, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-04.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B85C00")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
    return {
        "cover_title": ParagraphStyle("cover_title", fontSize=26, textColor=WHITE,
                                      fontName="Helvetica-Bold", alignment=TA_CENTER, leading=32),
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


def tag_row(tag, novelty, region, players, s, novelty_color=None):
    nc = novelty_color or GREEN
    tag_para = Paragraph(
        f"<font color='white'><b> {tag} </b></font>",
        ParagraphStyle("tag", fontSize=8, fontName="Helvetica-Bold",
                       textColor=WHITE, backColor=NAVY, leading=11, borderPadding=3)
    )
    novelty_para = Paragraph(
        f"<font color='white'><b> {novelty} </b></font>",
        ParagraphStyle("nov", fontSize=8, fontName="Helvetica-Bold",
                       textColor=WHITE, backColor=nc, leading=11, borderPadding=3)
    )
    reg_para = Paragraph(
        f"<b>Region:</b> {region}",
        ParagraphStyle("reg", fontSize=8, fontName="Helvetica",
                       textColor=HexColor("#333333"), leading=11)
    )
    play_para = Paragraph(
        f"<b>Players:</b> {players}",
        ParagraphStyle("play", fontSize=8, fontName="Helvetica",
                       textColor=HexColor("#333333"), leading=11)
    )
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "",           play_para, ""]],
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

    # ── Cover ─────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1: TOP PAYMENTS HEADLINES ─────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": (
                "SWIFT ISO 20022 Structured Address Deadline — Six Months Out, "
                "65 Percent of Messages Still Non-Compliant"
            ),
            "what": (
                "With the hard removal of unstructured postal addresses from CBPR+ ISO 20022 messages "
                "set for November 14, 2026 (SR 2026 standards release), SWIFT data indicates approximately "
                "65% of payment messages still carry unstructured address data. From that date, all CBPR+ "
                "messages must include at minimum a structured country code and town name for every agent "
                "and party; fully structured addresses are preferred. SWIFT's open-source AI Address "
                "Structuring Model — released free of charge — is available to help institutions remediate "
                "legacy address data at scale."
            ),
            "why": [
                "Six months is a short operational runway for institutions carrying large volumes of unstructured legacy address data; non-compliance will result in message rejection, not just penalties.",
                "Structured address data is a direct input to AML and sanctions screening precision — this is simultaneously a compliance program and a fraud-risk infrastructure upgrade.",
                "Corporate treasury, ERP, and TMS integrations require format-level remediation that goes beyond bank-side fixes; the data quality problem sits upstream in client systems.",
                "SWIFT's AI model lowers barriers for smaller institutions and mid-tier banks; those not using it face a competitive data-quality disadvantage by year-end.",
            ],
            "region": "Global",
            "players": "SWIFT, correspondent banks, corporate treasuries, TMS / ERP vendors, sanctions screening providers",
            "tag": "Infrastructure / Cross-Border",
            "novelty": "Escalation — 6-month hard deadline",
            "novelty_color": AMBER,
        },
        {
            "num": "2.",
            "headline": (
                "Indonesia Joins Project Nexus — BIS Multilateral IPS Network "
                "Expands to Six Central Banks, Covering 2+ Billion People"
            ),
            "what": (
                "Bank Indonesia has formally joined the BIS-led Project Nexus, adding the country's "
                "BI-FAST instant payment system to the multilateral network alongside Malaysia, "
                "the Philippines, Singapore, Thailand, and India. Nexus Global Payments (NGP), "
                "incorporated in Singapore in 2025, is now developing a formal rulebook, ISO 20022 "
                "technical specifications, and PSP onboarding frameworks. Indonesia's entry — connecting "
                "a population of 280 million and a rapidly growing digital payments market — materially "
                "widens the addressable network and corridor diversity."
            ),
            "why": [
                "Nexus now covers six of Asia's most important instant payment systems; the addition of Indonesia is strategically significant given its scale and remittance corridor importance.",
                "Any PSP seeking to serve ASEAN cross-border corridors will need a Nexus connectivity strategy; bilateral linkage approaches alone will be structurally inferior once Nexus is live.",
                "NGP's ISO 20022-native architecture means Nexus also becomes a data richness test — institutions with clean ISO 20022 data will process more efficiently across the network.",
                "The mid-2027 live implementation horizon is firming up; this is now a product and technology planning timeline, not a research topic.",
            ],
            "region": "ASEAN / South Asia / Global",
            "players": "BIS, NGP, Bank Indonesia, MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
            "novelty_color": GREEN,
        },
        {
            "num": "3.",
            "headline": (
                "UAE Financial Infrastructure Transformation Programme 85% Complete — "
                "Open Finance and Aani Positioned as Regional Blueprint"
            ),
            "what": (
                "The UAE's Financial Infrastructure Transformation (FIT) Programme — covering Aani "
                "(instant payments), Jaywan (domestic card scheme), open finance, central bank digital "
                "infrastructure, and a digital KYC utility — has been reported as approximately 85% "
                "complete. The CBUAE's Open Finance Regulation, live since 2024, now makes UAE one of "
                "the most advanced open finance jurisdictions globally. Aani, operated by Al Etihad "
                "Payments (AEP), is scaling toward the CBUAE's stated target of 90% digital transactions "
                "by end of 2026. The FIT Programme's breadth — simultaneously modernising the domestic "
                "card scheme, instant rail, open finance, and digital identity layers — is increasingly "
                "cited as a model for comprehensive payments ecosystem modernisation."
            ),
            "why": [
                "The simultaneous delivery of instant payments, domestic card scheme, open finance, and digital identity under a single programme is architecturally significant — few markets have achieved this level of coordinated infrastructure reform.",
                "Aani and Jaywan together provide the UAE with domestic alternatives to Visa/Mastercard and SWIFT that could meaningfully reduce foreign exchange leakage on domestic transactions.",
                "The 90% digital transaction target by end-2026 creates urgency for PSPs and acquirers to meet new onboarding and interoperability requirements before the deadline crystallises.",
                "UAE's FIT Programme is now being studied by GCC peers and other emerging markets as a replicable model for sovereign payments infrastructure investment.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Al Etihad Payments, UAE PSPs, banks, open finance providers, Jaywan",
            "tag": "Infrastructure / Regulation / Open Finance",
            "novelty": "Escalation / broader regional impact",
            "novelty_color": AMBER,
        },
        {
            "num": "4.",
            "headline": (
                "Qivalis: Ten European Banks Form MiCA-Licensed Euro Stablecoin Consortium — "
                "H2 2026 Launch Targeted"
            ),
            "what": (
                "A consortium of ten major European banks — ING, UniCredit, CaixaBank, BNP Paribas, "
                "KBC, Danske Bank, DekaBank, SEB, Raiffeisen Bank International, and Banca Sella — "
                "has incorporated Qivalis, a Dutch-based entity, to issue a fully MiCA-compliant "
                "euro-denominated stablecoin. Qivalis is seeking licensing from the Dutch Central Bank "
                "(DNB) as an e-money institution, targeting first issuance in H2 2026. The stablecoin "
                "is designed for cross-border payments, programmable finance, digital asset delivery-versus-payment "
                "(DvP) settlement, and supply chain use cases — explicitly positioned as a European "
                "counterweight to USD-dominated stablecoin market share (USDT, USDC)."
            ),
            "why": [
                "This is the largest coordinated bank-issued stablecoin initiative globally — ten systemically important banks issuing a single, jointly-governed instrument under a major regulatory framework.",
                "MiCA's EUR 200 million/day cap on non-euro stablecoins used for payments creates a structural regulatory advantage for Qivalis in eurozone payment flows.",
                "Bank-issued euro stablecoin settlement could disrupt correspondent banking economics for intra-European and EUR cross-border flows, especially for trade finance and institutional settlement.",
                "The programmable payments use case — enabling conditional, automated disbursements — is a direct competitive challenge to traditional payment orchestration and escrow models.",
            ],
            "region": "Europe / Global",
            "players": "ING, UniCredit, CaixaBank, BNP Paribas, KBC, Danske Bank, DekaBank, SEB, Raiffeisen, Banca Sella, DNB, ECB",
            "tag": "Stablecoins / Market Structure / Cross-Border",
            "novelty": "New today",
            "novelty_color": GREEN,
        },
        {
            "num": "5.",
            "headline": (
                "US GENIUS Act Implementation: OCC Publishes 376-Page Proposed Rule — "
                "Bank Stablecoin Issuance Framework Due July 2026"
            ),
            "what": (
                "The Office of the Comptroller of the Currency (OCC) published a 376-page proposed "
                "rule on February 25, 2026, operationalising the GENIUS Act — the first federal U.S. "
                "stablecoin law, signed by President Trump on July 18, 2025. The rule establishes "
                "licensing requirements, reserve composition standards (1:1 USD, short-term Treasuries, "
                "overnight repos, or Fed credits), monthly reserve reporting obligations (audited by "
                "registered accounting firms), and explicit prohibition on paying interest or yield "
                "on stablecoins. Final regulations are targeted for July 2026, with the law taking "
                "full effect no later than January 18, 2027."
            ),
            "why": [
                "Once finalised, U.S. nationally chartered banks will be able to issue stablecoins — a structural change that brings regulated bank money onto programmable payment rails for the first time at scale.",
                "The prohibition on yield-bearing stablecoins preserves bank deposit economics; this is a deliberate design choice that limits stablecoin disintermediation of bank funding models.",
                "Large U.S. banks (JPMorgan, Citi, BofA) and tech-adjacent payment firms are expected to be early applicants — the competitive dynamics among issuers will directly affect cross-border payment corridors.",
                "Together with the Qivalis euro stablecoin and MAS PFMI framework, a multilateral regulated stablecoin payment layer is materialising across three major currency jurisdictions simultaneously.",
            ],
            "region": "United States / Global",
            "players": "OCC, Federal Reserve, U.S. banks, stablecoin issuers, GENIUS Act, Congress",
            "tag": "Regulation / Stablecoins",
            "novelty": "Follow-up with material update",
            "novelty_color": GREEN,
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
        block.append(tag_row(h["tag"], h["novelty"], h["region"], h["players"], s,
                             novelty_color=h.get("novelty_color")))
        block.append(Spacer(1, 3*mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── SECTION 2: MAJOR FINTECH HEADLINES ────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": (
                "Adyen Acquires Talon.One for €750M — First-Ever Acquisition "
                "Targets Loyalty-Commerce Convergence at Point of Payment"
            ),
            "what": (
                "Adyen has signed a definitive agreement to acquire Talon.One, a Berlin-based "
                "real-time loyalty and promotions engine, for €750 million — Adyen's first-ever "
                "acquisition after a decade of building exclusively in-house. Talon.One generates "
                "approximately €60 million in ARR with 30–40% annual growth, and has strong overlap "
                "with Adyen's existing enterprise merchant base. The deal enables real-time SKU-level "
                "promotions, loyalty point redemptions, and personalised pricing to be applied directly "
                "within the payment flow — before a transaction is completed — across both online and "
                "in-store channels. The transaction is expected to close H2 2026, pending regulatory approval."
            ),
            "why": (
                "Adyen's shift from pure-play payment processing toward merchant engagement infrastructure "
                "marks a strategic inflection. By embedding loyalty decisioning inside the payment moment, "
                "Adyen competes directly with Salesforce Commerce Cloud, Braze, and loyalty platform "
                "specialists. For payments product leaders, this signals that the next battleground for "
                "large PSPs is not transaction economics but the merchant's ability to drive customer "
                "lifetime value through the payment interface. Adyen's willingness to abandon its "
                "build-only philosophy for a €750M bet signals how important this layer has become."
            ),
            "strategic": (
                "Payments processors are expanding into merchant-intelligence and loyalty infrastructure "
                "— the competitive perimeter is shifting from transaction rails to the commerce layer."
            ),
        },
        {
            "num": "2.",
            "headline": (
                "Ebury Raises £550M as Santander Increases Stake to 55% — "
                "Cross-Border SME Payments Consolidation Continues"
            ),
            "what": (
                "Ebury, the UK-based cross-border payments and FX specialist, is raising approximately "
                "£550 million, with majority shareholder Santander contributing £50 million to increase "
                "its stake to 55%. The raise positions Ebury for expansion in high-growth markets and "
                "reinforces its infrastructure for SME cross-border payments, trade finance, and "
                "multi-currency treasury management. The deal reflects a broader trend of incumbent banks "
                "deepening ownership of specialist cross-border payment platforms rather than building "
                "competing capabilities organically."
            ),
            "why": (
                "Santander's stake increase to majority ownership represents a classic bank-fintech integration "
                "playbook: acquire distribution reach and technology capability while maintaining brand "
                "separation. For the cross-border SME payments segment, this further concentrates the "
                "competitive field around bank-backed platforms (Ebury, Wise Business, Airwallex) with "
                "deep balance sheet support. Pure-play independent cross-border platforms face increasing "
                "pressure as incumbents close the product gap with capital advantages."
            ),
            "strategic": (
                "Banks are acquiring strategic stakes in cross-border fintech platforms rather than building; "
                "independent cross-border PSPs face a consolidating competitive landscape."
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

    # ── SECTION 3: WHAT MATTERS MOST ──────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Regulated stablecoin infrastructure is crystallising across three major "
            "currency jurisdictions simultaneously.",
            "The Qivalis euro stablecoin (10 European banks, MiCA-licensed), the U.S. GENIUS Act "
            "implementation (bank issuance framework due July 2026), and MAS's PFMI-standard "
            "stablecoin governance position are not isolated developments — they represent a "
            "coordinated global shift toward regulated digital money on programmable rails. Within "
            "18 months, stablecoin settlement could be a licensed, mainstream option for institutional "
            "cross-border, trade finance, and DvP flows in EUR, USD, and SGD corridors. The "
            "architecture of cross-border payments is being rebuilt from the settlement layer up."
        ),
        (
            "▶  Cross-border instant payment multilateralisation is moving from blueprint to live infrastructure.",
            "Project Nexus now covers six central banks and 2+ billion people, with a formal "
            "rulebook and ISO 20022 technical specifications in development. Indonesia's addition "
            "is strategically significant — BI-FAST is one of the region's highest-volume instant "
            "rails. PSPs and banks that treat Nexus as a 2027 problem rather than a 2025–26 design "
            "question are already behind on corridor strategy, FX liquidity positioning, and "
            "compliance architecture. The window for first-mover advantage is narrowing."
        ),
        (
            "▶  ISO 20022 data quality has become an active operational risk and cost variable — not a project.",
            "SWIFT's January 2026 pricing penalties for translation services and the November 2026 "
            "hard unstructured-address removal are converting ISO 20022 compliance from a one-time "
            "migration into a continuous data quality discipline. With 65% of messages still "
            "non-compliant six months from the deadline, the institutions that invest in enrichment "
            "pipelines, client data remediation programmes, and AI-assisted address structuring "
            "will derive compounding benefits in STP rates, sanctions screening quality, and "
            "correspondent relationship economics — those that do not will face rejection, delays, and cost."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4: IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER ─────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Start your ISO 20022 structured address programme now — message rejection is six months away.",
            "November 14, 2026 is not a warning; it is a hard rejection boundary. Institutions that "
            "have not already completed a data quality audit of their address fields, deployed SWIFT's "
            "AI structuring model for remediation, and updated client onboarding and ERP/TMS integration "
            "requirements will face operational disruptions before year-end. Frame this internally as "
            "a payments STP and fraud-risk programme, not a compliance overhead — the data quality "
            "investment will pay back in screening efficiency and straight-through processing rates."
        ),
        (
            "2.  Build a Project Nexus corridor strategy for ASEAN and South Asia — the mid-2027 live horizon is now a product planning date.",
            "With NGP incorporated, Indonesia now on board, and a formal rulebook in development, "
            "Nexus is past the point of being an interesting experiment. For PSPs and banks serving "
            "ASEAN, India, or Gulf-to-ASEAN corridors, this is the moment to map which markets you "
            "serve, model the FX liquidity requirements of sub-60-second settlement, and begin "
            "API connectivity design. Early movers on NGP integration will structurally outperform "
            "on speed, cost, and compliance in what will become the dominant ASEAN cross-border rail."
        ),
        (
            "3.  Monitor Qivalis and the OCC rule closely — bank-issued stablecoins are becoming a "
            "parallel payment and settlement rail for institutional and cross-border flows.",
            "The H2 2026 Qivalis launch and the July 2026 OCC final rule together create the "
            "conditions for bank-issued stablecoin settlement to become a real competitive option "
            "within 12 months. For payments product leaders, the questions to begin scoping now "
            "are: which of our clients' use cases — cross-border trade, DvP, programmable disbursements "
            "— would benefit from stablecoin settlement? What correspondent banking or FX relationships "
            "are potentially disrupted? And where should we build, partner, or simply monitor?"
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5: WATCHLIST ───────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  OCC Final Stablecoin Rule — July 2026.",
            "The OCC's finalised GENIUS Act implementing regulations will determine the capital, "
            "reserve, and operational requirements for bank stablecoin issuance in the U.S. "
            "Watch for which large U.S. banks file early applications and how Federal Reserve "
            "oversight of bank holding company stablecoin activities interacts with the OCC framework. "
            "The rule will also clarify whether non-bank fintechs can obtain federal stablecoin "
            "licences — a key competitive dimension."
        ),
        (
            "●  CBUAE Licensing Deadline for Newly In-Scope Entities — September 16, 2026.",
            "Open finance service providers and virtual asset payment services operating in the UAE "
            "must regularise under the new CBUAE Law by September 16, 2026. Expect a wave of "
            "licence applications and potential enforcement actions against non-compliant operators "
            "in Q3 2026. Watch also for CBUAE guidance on technical standards for open finance APIs, "
            "which has not yet been published in full detail."
        ),
        (
            "●  Nexus Global Payments Rulebook Publication — H2 2026.",
            "NGP is developing the formal Nexus rulebook, ISO 20022 technical specifications, and "
            "PSP onboarding standards. Publication is expected in H2 2026 and will set out the "
            "commercial, technical, and compliance requirements for PSPs to connect. This is the "
            "moment to identify your Nexus readiness gap and begin regulatory engagement, "
            "particularly for firms operating in Singapore, India, Malaysia, the Philippines, "
            "Thailand, and now Indonesia."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── Disclaimer ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, scheme operator communications, and reputable financial industry media. "
        "It is intended for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources: SWIFT (swift.com), BIS (bis.org), CBUAE (centralbank.ae), "
        "MAS (mas.gov.sg), OCC (occ.gov), Adyen, FinTech Futures, The Paypers, Ledger Insights, "
        "The Asian Banker, Global Government Fintech, PYMNTS, American Banker, Cointelegraph.",
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
