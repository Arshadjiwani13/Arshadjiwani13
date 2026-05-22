#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 22, 2026."""

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

DATE   = "May 22, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-22.pdf"

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
        [[Paragraph("Daily Payments &amp; Fintech Intelligence Brief", s["cover_title"]),],
         [Paragraph(DATE, s["cover_sub"])],
         [Spacer(1, 6*mm)]],
        colWidths=[170*mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return tbl


def section_header(number, title, s):
    tbl = Table(
        [[Paragraph(f"{number}  {title}", s["sec_hdr"])]],
        colWidths=[170*mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LGRAY),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    tag_para    = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=GREEN,
        leading=11, borderPadding=3))
    reg_para    = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para   = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
        "play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "", play_para, ""]],
        colWidths=[38*mm, 40*mm, 12*mm, 80*mm]
    )
    tbl.setStyle(TableStyle([
        ("SPAN",          (2,1),(3,1)),
        ("SPAN",          (2,0),(3,0)),
        ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0),(-1,-1), 2),
        ("BOTTOMPADDING", (0,0),(-1,-1), 2),
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
            "headline": "EU Instant Payments Regulation Enters Active Enforcement — Only 33% of PSPs Compliant",
            "what": (
                "The EU Instant Payments Regulation (IPR) crossed from implementation into enforcement "
                "in April 2026. PSPs submitted their first mandatory compliance reports to national "
                "competent authorities by April 9, 2026, covering data retrospective to October 2022. "
                "Reports must detail instant payment uptake, fee parity with standard SEPA credit "
                "transfers, Verification of Payee (VoP) coverage, and rejected-transfer metrics. "
                "Despite the compliance deadline, only approximately 33% of PSPs have achieved full "
                "readiness — with legacy infrastructure gaps in VoP, real-time sanctions screening, "
                "and structured address handling cited as the primary blockers."
            ),
            "why": [
                "Enforcement is live: member state NCAs can now issue administrative sanctions for IPR non-compliance — creating direct regulatory and reputational risk for laggard PSPs.",
                "The two-thirds non-compliance rate is a systemic signal that SEPA Instant adoption is not progressing uniformly; gaps are concentrated in mid-tier banks and non-bank PSPs.",
                "VoP implementation remains the hardest technical requirement — requiring real-time name-account matching across the SEPA zone, a problem that scales with counterparty database quality.",
                "The November 2026 structured address mandate (ISO 20022) compounds this: institutions must resolve two overlapping remediation tracks simultaneously.",
                "PSPs meeting these requirements early will benefit from improved STP rates, lower AML false positives, and competitive differentiation in B2B treasury flows.",
            ],
            "region": "Europe (EU / EEA)",
            "players": "EU PSPs, NCAs, ECB, EBA, SWIFT, corporate treasuries, RegTech vendors",
            "tag": "Regulation / RTP",
            "novelty": "Escalation — enforcement phase now active",
        },
        {
            "num": "2.",
            "headline": "SWIFT CBPR+ November 2026 Hard Deadline: Structured Addresses Mandatory, MT101 Discontinued",
            "what": (
                "SWIFT has confirmed that November 14, 2026 marks the hard cut-off for two "
                "interconnected CBPR+ changes: (1) all cross-border payment messages must use "
                "hybrid or fully structured postal address fields — unstructured formats will be "
                "rejected by the network; and (2) the interbank MT101 Request-for-Transfer message "
                "is formally discontinued and replaced by pain.001 v9. SWIFT has been charging "
                "automatic surcharges since January 1, 2026 for institutions still using in-flow "
                "translation or contingency MT processing, creating financial escalation toward the "
                "November deadline. J.P. Morgan plans to implement pain.001 v9 sending capability "
                "in Q4 2026, while its AI address-structuring model has been deployed to remediate "
                "legacy unstructured data in corporate client records."
            ),
            "why": [
                "The November 14 deadline is a hard network enforcement date — unstructured addresses will be rejected at the SWIFT gateway, not just penalized with surcharges.",
                "Institutions with large corporate client bases face an active data remediation challenge: converting decades of unstructured address records to ISO 20022-compliant structured fields.",
                "SWIFT's AI address-structuring tool lowers the remediation cost, but adoption requires integration into existing client data workflows and onboarding processes.",
                "MT101 discontinuation directly affects corporate-to-bank and bank-to-bank payment instruction formats — TMS, ERP, and payment factory integrations must be updated.",
                "Banks completing this migration early convert a compliance cost into an AML/sanctions operational advantage: richer structured data directly improves screening precision.",
            ],
            "region": "Global",
            "players": "SWIFT, global correspondent banks, corporate treasuries, J.P. Morgan, TMS/ERP vendors",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — 6 months to hard deadline",
        },
        {
            "num": "3.",
            "headline": "UAE: Ziina Executes First Live Open Finance A2A Payment — Open Finance Moves from Regulation to Reality",
            "what": (
                "Ziina, a UAE-based consumer payments app, executed the UAE's first live "
                "customer-initiated Open Finance payment in partnership with Lean Technologies — "
                "the country's first licensed Open Finance technical service provider. Using "
                "CBUAE-regulated Open Finance APIs connected to major UAE banks, Ziina customers "
                "can now complete instant account-to-account bank payments without entering card "
                "details. This follows the CBUAE's Open Finance Regulation framework, underpinned "
                "by Nebras (the national Open Finance platform) and Al Tareq (the Central Bank's "
                "API framework). Separately, the CBUAE's Jisr platform for CBDCs has been "
                "interlinked with the UAE Instant Payment Interface (IPI) and the domestic "
                "card scheme Jaywan to support cross-border settlement."
            ),
            "why": [
                "This is the first live proof-of-concept execution of UAE Open Finance — moving from regulation to real-world A2A payment flows for consumers.",
                "The Ziina-Lean model demonstrates the licensed API provider structure working in practice: bank connectivity, consent management, and instant settlement in a single flow.",
                "The CBUAE's multi-rail integration (Open Finance + IPI + Jaywan + Jisr CBDC) is building a unified domestic payment infrastructure stack rarely seen at this speed in the GCC.",
                "For PSPs and fintechs in the UAE, the Ziina execution defines the product benchmark and compliance reference architecture for A2A payment flows.",
                "Merchant acquirers and card-payment incumbents should note: Open Finance A2A is becoming a credible alternative payment channel in the UAE.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Ziina, Lean Technologies, UAE banks, Nebras, Al Tareq",
            "tag": "Open Finance / A2A",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "Project Nexus: NGP Incorporated, Network Operator Tender Published — 2026 Go-Live in Scope",
            "what": (
                "Nexus Global Payments (NGP), the operational entity for the BIS-led Project Nexus "
                "multilateral instant cross-border payment scheme, has been formally incorporated as "
                "a not-for-profit organisation in Singapore. The five founding central banks — MAS, "
                "Reserve Bank of India, Bank Negara Malaysia, Bangko Sentral ng Pilipinas, and Bank "
                "of Thailand — have published an invitation to tender for the network operator role "
                "that will manage the Nexus hub connecting their domestic instant payment systems "
                "(PayNow, UPI/IMPS, DuitNow, InstaPay, PromptPay). The scheme targets sub-60-second "
                "cross-border settlement for a potential market of 1.7 billion people, with a full "
                "go-live window of 2026–2027."
            ),
            "why": [
                "Project Nexus is the most ambitious multilateral instant cross-border payment initiative globally — a single hub connecting five national IPS networks with enforceable scheme standards.",
                "The NGP incorporation and operator tender represent the shift from blueprint to operational infrastructure: this is no longer a research project.",
                "Singapore's role as NGP's incorporation jurisdiction further cements its position as the operational anchor of Asia-Pacific's cross-border payment modernization.",
                "PSPs and banks in India, Malaysia, Singapore, Philippines, and Thailand must now plan for Nexus connectivity — API integration, FX liquidity management, compliance alignment.",
                "Bilateral IPS linkages (e.g., PayNow-UPI, PayNow-DuitNow) will co-exist initially; Nexus is the long-term multi-lateral successor that reduces fragmentation.",
            ],
            "region": "Singapore / Asia-Pacific (India, Malaysia, Philippines, Thailand)",
            "players": "MAS, BIS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, NGP, domestic IPS operators",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "5.",
            "headline": "UK cVRP: FCA and PSR Issue Pricing Clarity — Commercial VRP Adoption Accelerating in 2026",
            "what": (
                "The FCA and PSR published regulatory clarity on open banking pricing models in "
                "early 2026, resolving a long-standing commercial ambiguity that had held back "
                "voluntary commercial variable recurring payment (cVRP) adoption. The UK Payments "
                "Initiative (UKPI) — a 31-firm consortium established in 2025 — launched Phase 1 "
                "use cases covering utility payments, financial services payments, and government "
                "payments. The first live cVRP was processed in November 2025 via Tink/Visa/Kroo Bank, "
                "with wider adoption expected through 2026. The Data (Use and Access) Act Statutory "
                "Instrument granting the FCA formal rule-setting powers over open banking is expected "
                "to be laid before Parliament in Q4 2026, and a 'Future Entity' standards body is "
                "being selected in April 2026."
            ),
            "why": [
                "Pricing clarity removes the primary commercial blocker for cVRP — PSPs can now price and structure commercial VRP products with regulatory certainty.",
                "The UKPI Phase 1 use cases (utilities, government, financial services) are high-volume, high-frequency payment categories that give A2A rails a viable mainstream entry point.",
                "The FCA's Q4 2026 rule-setting powers and Future Entity selection signal that UK open banking is transitioning from industry self-governance to a durable regulatory framework.",
                "Card networks (Visa via Tink) are embedding themselves in the open banking stack early — reinforcing their role even as A2A challenges card payment dominance.",
                "UK cVRP as a mainstream channel remains contingent on consumer experience parity with cards and on merchant adoption — watch for 2026 adoption metrics at year-end.",
            ],
            "region": "United Kingdom",
            "players": "FCA, PSR, UKPI, Tink/Visa, Kroo Bank, Open Banking Limited, open banking PSPs",
            "tag": "Open Finance / RTP / Regulation",
            "novelty": "Follow-up with material update",
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
            "headline": "Mastercard Acquires BVNK for $1.8B — Largest Stablecoin Deal Pending Regulatory Approval",
            "what": (
                "Mastercard announced a definitive agreement in March 2026 to acquire BVNK, a "
                "London-based stablecoin infrastructure firm, for up to $1.8 billion (including "
                "$300 million in contingent payments). BVNK operates a fiat-to-stablecoin bridge "
                "across 130+ countries on all major blockchain networks and processed significant "
                "payment volumes for institutional and corporate clients. Regulatory approval is "
                "expected by late 2026. Mastercard has simultaneously launched 'Agent Pay', an "
                "agentic commerce payments capability built for AI-driven transaction environments. "
                "The BVNK deal eclipses Stripe's $1.1 billion acquisition of Bridge in February 2025, "
                "making it the largest stablecoin infrastructure acquisition to date."
            ),
            "why": (
                "Mastercard is executing a deliberate strategic repositioning from card network to "
                "programmable money infrastructure. BVNK gives Mastercard fiat-blockchain bridging "
                "capability at institutional scale, positioning the company to participate in the "
                "emerging stablecoin payment layer as it intersects with the GENIUS Act regulatory "
                "framework in the US and MiCA in Europe. For banks and PSPs, a Mastercard-owned "
                "BVNK represents potential disintermediation of correspondent banking in corridors "
                "where stablecoin settlement is commercially superior. The Agent Pay announcement "
                "signals Mastercard is simultaneously betting on AI-driven commerce as a parallel "
                "payment channel."
            ),
            "strategic": "Mastercard is transforming from a card network to a multi-rail programmable payments infrastructure — stablecoin and AI commerce are both now core to its product strategy.",
        },
        {
            "num": "2.",
            "headline": "GENIUS Act Implementation: OCC Comment Period Closes, Treasury AML Rules Proposed",
            "what": (
                "The US OCC's proposed rulemaking to implement the GENIUS Act — which established "
                "a federal licensing and supervisory framework for payment stablecoins — closed its "
                "public comment period on May 1, 2026, receiving industry responses to 211 specific "
                "questions. Separately, the US Treasury proposed rules applying Bank Secrecy Act and "
                "AML obligations to permitted payment stablecoin issuers. The Bank Policy Institute "
                "submitted detailed recommendations on reserve requirements, interoperability, "
                "and oversight allocation between OCC and state regulators. A final OCC rule is "
                "expected in H2 2026, with compliance timelines crystallizing for bank and non-bank "
                "stablecoin issuers."
            ),
            "why": (
                "The GENIUS Act comment period closing is the pivotal transition from legislative "
                "intent to regulatory precision. The OCC's final rule will define who can issue, "
                "what reserves are required, and how oversight is allocated — directly shaping the "
                "competitive structure of US dollar stablecoin payments infrastructure. Treasury's "
                "AML proposal means stablecoin issuers will face BSA compliance obligations on "
                "par with banks — raising the cost and operational complexity of entry for non-bank "
                "issuers, and favoring large regulated institutions. For product leaders, the "
                "H2 2026 final rule is the decision-gate for USD stablecoin product roadmaps."
            ),
            "strategic": "The OCC final rule, expected H2 2026, will be the structural determinant for USD stablecoin payment product architecture — plan roadmaps around this decision point.",
        },
        {
            "num": "3.",
            "headline": "MAS Tokenized CBDC Pilot for Government Bills — Wholesale Digital Settlement Infrastructure Advancing",
            "what": (
                "MAS announced a pilot program for tokenized Singapore government bills to be issued "
                "and settled using a wholesale central bank digital currency (wCBDC). Primary dealers "
                "will issue and settle MAS bills through blockchain-based tokens backed by the "
                "Singapore dollar wCBDC. This builds on Project Guardian — MAS's broader institutional "
                "tokenization initiative, which now includes over 40 financial institutions — and "
                "follows Singapore's cross-border digital asset settlement agreement with Deutsche "
                "Bundesbank, targeting universal standards for tokenized payments and securities."
            ),
            "why": (
                "MAS is advancing from institutional tokenization experiments to actual government "
                "securities issuance on wholesale CBDC rails — a significant step toward programmable "
                "money as real operating infrastructure. The 40-institution Project Guardian network "
                "and Bundesbank partnership signal that Singapore is building toward a live tokenized "
                "capital markets and payments infrastructure, not merely a sandbox. For banks and "
                "payment infrastructure operators, this defines the trajectory: wCBDC-settled "
                "tokenized assets as the long-term direction for institutional settlement."
            ),
            "strategic": "MAS's wCBDC pilot and Project Guardian ecosystem position Singapore as the leading live deployment environment for institutional tokenized finance — a platform advantage for globally active banks.",
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
            "▶  2026 is the inflection year for Open Finance and A2A payments moving from regulation to live execution.",
            "UAE's first live Open Finance A2A payment (Ziina/Lean), UK cVRP's pricing clarity and UKPI Phase 1 "
            "deployment, and Singapore's wCBDC tokenization pilot all confirm that the 2023-2025 regulatory "
            "frameworks are now yielding live products. The question is no longer whether A2A and open finance "
            "will scale — it is which markets, which use cases, and which product architectures will lead. "
            "The UAE is moving faster than most observers expected; UK is structurally consolidating; "
            "Singapore is setting the infrastructure benchmark."
        ),
        (
            "▶  Stablecoins are graduating from crypto speculation to payment infrastructure — with regulatory scaffolding arriving.",
            "The Mastercard/BVNK acquisition, GENIUS Act implementation, and MAS PFMI framework call all "
            "represent different facets of the same structural shift: stablecoin payment infrastructure is "
            "being treated as regulated, institutionally significant payment rails. The GENIUS Act final rule "
            "(H2 2026) and MiCA implementation create the first real regulatory foundation for USD and EUR "
            "stablecoin payments at scale. Banks and PSPs need strategies for where stablecoin rails "
            "compete with, complement, or displace their existing products."
        ),
        (
            "▶  ISO 20022 data quality is bifurcating the industry — institutions that invest now will compound advantages.",
            "SWIFT's active financial penalties, the November 2026 hard deadline for structured addresses, "
            "and the EU IPR's enforcement phase are all converging on the same operational problem: "
            "payment data quality. The 33% PSP compliance rate on EU IPR and the scale of corporate "
            "address remediation programs reveal that data quality is the execution gap separating "
            "leading from lagging institutions. Leaders who treat this as a data product investment "
            "— not a compliance migration — will gain durable advantages in fraud detection, "
            "sanctions screening, and STP rates."
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
            "1.  UAE and UK Open Finance are now actionable product opportunities — define your A2A strategy now.",
            "With Ziina/Lean demonstrating the UAE's first live A2A Open Finance payment, and the UK's "
            "UKPI advancing cVRP Phase 1 with regulatory pricing clarity, both markets have crossed "
            "the threshold from feasibility to execution. Product leaders in these geographies should "
            "be accelerating A2A payment product development, reviewing API provider partnerships "
            "(Lean, Tink, Token.io), and stress-testing card-alternative use cases (utilities, "
            "B2B payables, financial services). The UAE September 2026 licensing deadline is a "
            "hard constraint for competitive positioning."
        ),
        (
            "2.  Build your GENIUS Act readiness plan — the H2 2026 final rule is the USD stablecoin decision gate.",
            "If your product roadmap includes any USD stablecoin payment capability — whether issuing, "
            "processing, or integrating stablecoin rails — the OCC's final GENIUS Act rule is the "
            "structural determinant for what is permissible, by whom, and under what capital and "
            "compliance conditions. A stablecoin product built on assumptions that diverge from the "
            "final rule faces re-architecture risk. Now is the time to engage your regulatory counsel, "
            "map your stablecoin product architecture against the draft rules, and identify the "
            "highest-risk assumptions in your current roadmap."
        ),
        (
            "3.  Treat November 2026 ISO 20022 structured address migration as a data quality product sprint, not IT compliance.",
            "Six months to the SWIFT CBPR+ structured address hard deadline, with EU IPR enforcement "
            "active and SEPA 3.7 now mandatory, payment data quality is a live operational and "
            "commercial problem. Product leaders should reframe this: structured address data is "
            "not a compliance requirement — it is a data asset that directly improves fraud detection, "
            "reduces sanctions screening false positives, and raises STP rates. The firms that "
            "invest in address enrichment pipelines, client data remediation programs, and "
            "AI-assisted structuring now will have measurable performance advantages by Q1 2027."
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
            "●  Project Nexus network operator selection outcome — expected H2 2026.",
            "The NGP invitation to tender for the Nexus network operator will determine which "
            "institution manages the hub connecting five Asian IPS networks for 1.7 billion people. "
            "The operator selection will signal the commercial model, fee structure, and technical "
            "requirements for PSP participants in connected markets. Watch for announcements from "
            "likely contenders including SWIFT, Mastercard, regional payment infrastructure operators, "
            "and BIS Innovation Hub alumni."
        ),
        (
            "●  CBUAE Open Finance licensing wave — September 16, 2026 deadline.",
            "Firms newly in-scope under the CBUAE Law (Federal Decree-Law No. 6 of 2025) — including "
            "open finance service providers and virtual asset payment services — must regularise their "
            "licensing by September 16, 2026. Watch for a wave of license applications, market "
            "entry from international open finance players, and potential enforcement actions against "
            "operators who miss the window. This is the defining regulatory gate for UAE fintech "
            "market structure in H2 2026."
        ),
        (
            "●  OCC GENIUS Act final rule — expected H2 2026.",
            "The most consequential piece of US payments regulatory infrastructure to drop in years. "
            "The final rule will define reserve requirements, interoperability obligations, state vs. "
            "federal oversight allocation, and AML compliance standards for payment stablecoin issuers. "
            "Watch for the rule's treatment of non-bank issuers (which determines whether fintechs "
            "can compete with banks on USD stablecoin issuance) and its interoperability provisions "
            "(which determine whether stablecoin payment rails can be open or remain siloed)."
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
        "CBUAE (centralbank.ae), MAS (mas.gov.sg), SWIFT (swift.com), BIS (bis.org), FCA (fca.org.uk), "
        "PSR (psr.org.uk), OCC (occ.gov), US Treasury, ECB (ecb.europa.eu), CNBC, Fortune, "
        "The Asian Banker, Fintech News ME, The Paypers, Datos Insights, S&amp;P Global, FXC Intelligence.",
        s["footer_note"]
    ))

    return story


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MGRAY)
    canvas.drawCentredString(
        A4[0]/2, 12*mm,
        f"Daily Payments & Fintech Intelligence Brief  |  {DATE}  |  Page {doc.page}"
    )
    canvas.setStrokeColor(SILVER)
    canvas.setLineWidth(0.3)
    canvas.line(20*mm, 15*mm, A4[0]-20*mm, 15*mm)
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
