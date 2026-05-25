#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 25, 2026."""

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

DATE   = "May 25, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-25.pdf"

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
            "headline": "SWIFT Blockchain Shared Ledger Moves to MVP — Live Real-World Transactions Targeted for 2026",
            "what": (
                "SWIFT has completed the design phase of its blockchain-based shared ledger and is "
                "actively building the first iteration toward an MVP that will process live real-world "
                "transactions in 2026. More than 30 global financial institutions — including JPMorgan, "
                "HSBC, BNP Paribas, Deutsche Bank, and Bank of America — shaped the design phase. The "
                "ledger uses smart contracts to record, sequence, and validate transactions, enabling "
                "tokenized deposits, regulated stablecoins, and CBDCs to move between institutions "
                "24/7 with real-time settlement finality. In parallel, 25+ banks will adopt SWIFT's "
                "new retail transaction transparency framework by end of June 2026."
            ),
            "why": [
                "If the MVP delivers on its 2026 live timeline, it marks the first fundamental change to SWIFT's settlement architecture in its 50-year history — moving from message-relay to settlement-infrastructure.",
                "The shared ledger directly targets the costliest friction points in correspondent banking: nostro pre-funding inefficiency, reconciliation overhead, and T+1 or longer settlement cycles.",
                "Banks participating in the MVP gain first-mover advantage in shaping the interoperability and liquidity management protocols that govern tokenized cross-border payments.",
                "For PSPs and payment orchestrators, a 24/7 SWIFT ledger is a potential competitive reset — if it achieves real-time finality, the structural case for legacy correspondent correspondent chains weakens materially.",
            ],
            "region": "Global",
            "players": "SWIFT, JPMorgan, HSBC, BNP Paribas, Deutsche Bank, Bank of America, 30+ global banks",
            "tag": "Infrastructure / Cross-Border",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "2.",
            "headline": "US RTP Network Sets Single-Day Records on May 1 — Volume, Value Both Peak",
            "what": (
                "The Clearing House's RTP network processed 2.27 million transactions worth $8.62 billion "
                "on May 1, 2026 — new single-day records for both volume and value. Tax refund disbursements "
                "drove significant growth, up 78% in the first four months of 2026 versus the same period "
                "in 2025. Instant payments are now approaching $500 billion in quarterly value, with over "
                "1.5 million transactions per day on average. The RTP network now processes over 98% of "
                "U.S. bank-to-bank instant payments by institution coverage."
            ),
            "why": [
                "Government disbursement use cases — tax refunds, healthcare, insurance — are proving to be the volume catalyst for US RTP adoption, not just consumer P2P, signaling a structural shift in institutional use of real-time rails.",
                "Push payment fraud risk is escalating in parallel: unlike ACH, instant RTP settlement leaves no reversal window, making fraud prevention a product-critical investment, not an optional control.",
                "The record volumes validate the business case for banks still evaluating FedNow and RTP investment — the revenue pool from instant payment orchestration is materializing faster than projected.",
                "For cross-border players, the deepening domestic RTP liquidity pool in the US strengthens the case for FedNow's proposed cross-border extension (currently in public comment).",
            ],
            "region": "United States",
            "players": "The Clearing House, US banks, FedNow, payment processors, government disbursement agencies",
            "tag": "RTP / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "SAMA Issues First Live Open Banking Licenses in Saudi Arabia — Payment Initiation Now Active",
            "what": (
                "Saudi Arabia's central bank SAMA has formally commenced licensing fintech companies "
                "to provide open banking services, transitioning from sandbox to live regulated activity. "
                "Lean Technologies received the first Major Payment Institution (MPI) licence under the "
                "new framework; NTS (New Tech Software) received a second. Critically, Phase 2 of SAMA's "
                "Open Banking Framework introduces Payment Initiation Services (PIS), allowing merchants "
                "to accept payments directly from customers' bank accounts — a structural A2A payment "
                "capability now live in Saudi Arabia for the first time, aligned with Vision 2030's "
                "National Fintech Strategy."
            ),
            "why": [
                "Saudi Arabia's PIS activation is the most consequential open banking development in the GCC this year — it creates a live A2A payment rail that challenges card acceptance economics for merchants in the Kingdom.",
                "SAMA's licensing structure (MPI framework) mirrors MAS and CBUAE approaches, signaling GCC-wide convergence toward regulated open finance licensing architectures.",
                "Lean Technologies' first-mover position gives it a structural regulatory advantage in Saudi A2A payment flows — a market with $80bn+ projected digital payment transaction value.",
                "Regional PSPs, acquirers, and international card networks must now treat Saudi PIS as a credible alternative payment method, not a future concept.",
            ],
            "region": "Saudi Arabia / GCC",
            "players": "SAMA, Lean Technologies, NTS, Saudi banks, merchants, GCC PSPs",
            "tag": "Open Finance / Regulation / RTP",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "MAS Revokes Bsquared Technology MPI License — Enforcement Signal Sharpens",
            "what": (
                "The Monetary Authority of Singapore revoked the Major Payment Institution (MPI) license "
                "of Bsquared Technology (BSQ) on May 14, 2026. An onsite inspection by MAS found "
                "significant weaknesses in risk management practices and conflict of interest policies, "
                "failure to meet outsourcing guidelines in related-entity arrangements, and — most "
                "seriously — the submission of false or misleading information to the regulator. MAS also "
                "separately confirmed a proof-of-value initiative with five Singapore banks and the "
                "Government Technology Agency to deploy AI/ML models for pre-emptive scam detection "
                "across shared transaction datasets."
            ),
            "why": [
                "License revocation for false reporting to MAS is a category-one enforcement signal — it clarifies that MAS treats misleading regulatory submissions as a grounds for disqualification, not just sanction.",
                "The simultaneous AI scam detection POV with five banks reflects MAS's two-track approach: tighten licensing standards while building shared industry infrastructure for fraud prevention.",
                "For payment fintechs seeking or holding MAS MPI licenses, outsourcing arrangements with related entities are now a specific examination focus — governance structures must be structurally independent.",
                "The AI/ML initiative for cross-bank scam detection is a template for collaborative fraud intelligence that could become a scheme-level requirement in Singapore.",
            ],
            "region": "Singapore",
            "players": "MAS, Bsquared Technology, Singapore banks, GovTech, Singapore Police Force",
            "tag": "Regulation / Fraud-Risk",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "5.",
            "headline": "ISO 20022 Structured Address Hard Deadline — Six Months to November 2026 Enforcement",
            "what": (
                "With November 2026 now six months away, the hard deadline for fully structured postal "
                "address fields in SWIFT CBPR+ and SEPA payments has become an urgent operational "
                "priority. After November 15, 2026, SWIFT will reject payments containing unstructured "
                "addresses. SEPA version 3.7 — mandatory since November 2025 — introduced updated "
                "formats (pain.001.001.09, pain.008.001.08, pain.002.001.10). From November 2026, "
                "banks must also be able to receive camt.110 investigation messages. SWIFT pricing "
                "penalties for non-compliant institutions have been active since January 2026."
            ),
            "why": [
                "The November 2026 structured address mandate is now within the standard system-change delivery window — institutions that have not started data remediation programs face real delivery risk.",
                "Unstructured legacy address data is the single largest remaining gap in ISO 20022's AML and sanctions screening uplift promise — banks resolving this now gain permanent improvements in screening precision and false-positive reduction.",
                "Corporate treasury and ERP/TMS vendors whose clients have not updated pain.001 format mappings will generate rejected payment traffic from November 2026 — a client retention risk for banks managing corporate payment factories.",
                "SWIFT's escalating pricing penalties are a commercial mechanism to force action — institutions delaying remediation face both rejection risk and cost escalation simultaneously.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone banks, corporate treasuries, TMS/ERP vendors, payment factories",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — six-month countdown active",
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
            "headline": "Adyen Acquires Talon.One for €750M — First-Ever M&amp;A Breaks 20-Year Build-Only Rule",
            "what": (
                "Adyen has signed a definitive agreement to acquire Berlin-based Talon.One for €750 "
                "million in cash, funded from existing resources. This is Adyen's first acquisition in "
                "its two-decade history, deliberately ending its build-only philosophy. Talon.One is a "
                "real-time loyalty, promotions, and incentives decisioning platform serving 300+ global "
                "retailers, with ~€60 million in recurring revenue growing at 30–40% annually. The "
                "transaction is subject to regulatory approval and expected to close in H2 2026."
            ),
            "why": (
                "Adyen is embedding loyalty and promotional data into its payment decisioning layer — "
                "creating a unified commerce signal that combines transaction data with behavioral incentive "
                "logic at the point of payment. This directly challenges Stripe, Salesforce Commerce Cloud, "
                "and standalone loyalty platforms for control of the merchant revenue optimization stack. "
                "For payment product leaders, this signals that the strategic battleground for acquirer "
                "value is shifting from payment processing margin to data-driven merchant outcome ownership."
            ),
            "strategic": "The payments-to-loyalty convergence is now happening at platform level — Adyen's move pressures processors to build or buy comparable merchant engagement infrastructure.",
        },
        {
            "num": "2.",
            "headline": "Paymentology Secures $175M Investment — Card Processing Infrastructure Consolidates",
            "what": (
                "UK-based card processing infrastructure firm Paymentology secured a $175 million "
                "investment co-led by Aspirity Partners and Apis Partners. Paymentology operates a "
                "cloud-native card issuer processing platform serving banks and fintechs across "
                "emerging markets in Africa, Asia, the Middle East, and Latin America."
            ),
            "why": (
                "Paymentology's raise signals continued institutional appetite for cloud-native card "
                "processing infrastructure in emerging markets — particularly in regions where legacy "
                "bank processor incumbents (Fiserv, FIS, Temenos) have weaker penetration. The GCC "
                "and Southeast Asian market contexts are directly relevant: as neobanks and embedded "
                "finance players scale in these regions, card issuance infrastructure is becoming a "
                "strategic input, not a commodity. The investment also reflects broader consolidation "
                "pressure in the card processing space as scale requirements grow."
            ),
            "strategic": "Cloud-native card issuer processing is consolidating around a small group of scaled platforms — the window for independent regional incumbents is narrowing.",
        },
        {
            "num": "3.",
            "headline": "PayPal Restructures into Three Divisions — Operational Simplification with $1.5bn Savings Target",
            "what": (
                "PayPal announced a restructure of its operating model into three defined divisions: "
                "(1) Checkout Solutions and PayPal; (2) Consumer Financial Services and Venmo; "
                "(3) Payment Services and Crypto. The restructure targets $1.5 billion in cost savings "
                "over two to three years and is framed as a recommitment to fundamentals after years "
                "of strategic sprawl."
            ),
            "why": (
                "PayPal's structural separation of crypto from its core consumer and merchant products "
                "is strategically significant — it signals a deliberate attempt to manage the crypto "
                "narrative independently without contaminating the core merchant checkout and Venmo "
                "growth stories. The cost-out target of $1.5bn reflects a shift from growth-at-all-costs "
                "to margin discipline, which will affect product investment prioritization across the portfolio. "
                "For competing PSPs and acquirers, a leaner, more focused PayPal is a more dangerous competitor."
            ),
            "strategic": "PayPal's restructure is a strategic reset, not just a cost exercise — watch for accelerated checkout and Venmo product investment once the simplification delivers operating leverage.",
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
            "▶  Payment infrastructure is entering a live-transaction phase, not just a standards phase.",
            "SWIFT's blockchain ledger MVP targeting 2026 live transactions, US RTP breaking single-day "
            "records, and Saudi Arabia activating live PIS licensing all represent the same signal: "
            "infrastructure that has been debated for years is now executing in production. The gap "
            "between 'announced' and 'live' is closing faster than expected across multiple rails and "
            "geographies simultaneously. This compresses the available planning window for incumbents."
        ),
        (
            "▶  GCC open finance is no longer aspirational — it is a licensed, live competitive reality.",
            "SAMA's activation of Payment Initiation Services in Saudi Arabia, combined with CBUAE's "
            "open finance licensing regime and UAE's September 2026 compliance deadline, means the GCC "
            "is now a live A2A and open banking market, not an emerging one. Regional banks, PSPs, "
            "and international payment players that have not built GCC open finance product strategies "
            "are now behind the regulatory and market curve."
        ),
        (
            "▶  The payment platform value chain is consolidating around data — and Adyen just showed why.",
            "Adyen's acquisition of Talon.One — its first-ever — signals that payment platforms are "
            "moving to own the data layer connecting transaction signals to merchant outcomes. The "
            "payments-to-loyalty convergence is happening at the infrastructure level, not just the "
            "application layer. This is part of a broader pattern: Adyen, Stripe, and PayPal are "
            "all expanding the product surface beyond payment processing toward merchant intelligence "
            "and revenue optimization. The margin pool is moving up the stack."
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
            "1.  Treat Saudi Arabia's PIS activation as a near-term product and corridor opportunity, not a watch item.",
            "SAMA's live PIS licensing creates the first regulated A2A payment capability in the Gulf's "
            "largest economy. For PSPs, acquirers, and banks with Saudi merchant or consumer exposure, "
            "this is not a 2027 roadmap item — Lean Technologies has a first-mover MPI licence now. "
            "Evaluate integration into SAMA's open banking API layer and assess whether your Saudi payment "
            "acceptance stack needs a PIS track to stay competitive on merchant cost and conversion."
        ),
        (
            "2.  ISO 20022 structured address remediation must be a live program, not a Q4 sprint.",
            "The November 2026 SWIFT rejection deadline for unstructured addresses is six months away. "
            "For any institution processing CBPR+ or SEPA credit transfers, this is within the minimum "
            "delivery window for data remediation, system change, and UAT. Audit your current payment "
            "factory's address field completeness now. Frame the remediation as a fraud/sanctions "
            "screening uplift investment — not just a compliance cost — to secure the business case."
        ),
        (
            "3.  Monitor SWIFT's blockchain ledger MVP milestones — they will determine whether correspondent banking economics shift in 2027.",
            "The SWIFT shared ledger's 2026 live-transaction target, with 30+ major banks already "
            "signed on to the design phase, is the most consequential infrastructure development in "
            "cross-border payments this decade if it executes. Track which banks announce participation "
            "in the live MVP. If JPMorgan, HSBC, and Deutsche Bank go live with tokenized deposit "
            "settlement on the ledger in 2026, the correspondent banking model faces structural "
            "disruption in 2027 — and your platform's nostro liquidity and FX pricing strategy needs a contingency."
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
            "●  SWIFT blockchain ledger MVP live-transaction announcement — H2 2026.",
            "The first real-world transaction on SWIFT's blockchain-based shared ledger will be a "
            "landmark moment. Watch for participant bank announcements and the specific use cases "
            "confirmed for MVP (tokenized deposits vs. stablecoins vs. CBDC settlement) — the asset "
            "type chosen will signal which tokenized payment architecture gains institutional momentum."
        ),
        (
            "●  UAE CBUAE licensing deadline for open finance and virtual asset payment services — September 16, 2026.",
            "The six-month compliance window closes in September for firms newly in-scope under CBUAE "
            "Federal Decree-Law No. 6 of 2025. Watch for a licensing rush and potential enforcement "
            "actions against non-compliant embedded finance and crypto payment operators in the UAE — "
            "this will clarify who the regulated open finance players are in the market."
        ),
        (
            "●  Project Nexus PSP onboarding timelines — ASEAN corridor activation.",
            "With Nexus Global Payments (NGP) incorporated and BSP Philippines confirming integration "
            "alignment, the next milestone is PSP-level onboarding announcements for the India-ASEAN "
            "corridors. Watch for MAS and RBI joint statements on technical standards and commercial "
            "framework — these will define the pricing, liquidity, and compliance requirements for "
            "the world's first multilateral instant cross-border payment scheme."
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
        "SWIFT (swift.com), The Clearing House (theclearinghouse.org), SAMA (sama.gov.sa), "
        "MAS (mas.gov.sg), CBUAE (centralbank.ae), FintechNews.sg, The Paypers, PYMNTS, "
        "American Banker, Ledger Insights, Adyen (adyen.com), Fintech Futures, Fintech Global.",
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
