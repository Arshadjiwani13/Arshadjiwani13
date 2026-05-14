#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 14, 2026."""

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

DATE   = "May 14, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-14.pdf"

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
        colWidths=[42*mm, 44*mm, 4*mm, 80*mm]
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

    # ── Cover ──────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 : TOP PAYMENTS HEADLINES ────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "Paymentology Raises $175M — Issuer Processor Moves Into Stablecoin, AI & Credit",
            "what": (
                "On May 12, 2026, Paymentology — a cloud-native global issuer-processor operating "
                "across 68 countries — closed a $175 million private equity round co-led by Apis "
                "Partners and Aspirity Partners. New sales grew 117% year-on-year in FY25 and "
                "transaction volumes rose 65%. The company will use proceeds to expand beyond core "
                "card issuer processing into adjacent capabilities including credit, stablecoin "
                "processing, tokenization, and AI-driven payment services."
            ),
            "why": [
                "Issuer processors are broadening their stack from commodity card processing toward "
                "higher-margin AI and digital asset services — signalling where competitive "
                "differentiation is moving.",
                "Stablecoin processing at the issuer layer positions Paymentology to serve "
                "fintechs and banks building MiCA- and GENIUS Act-compliant stablecoin payment "
                "products without building the processing plumbing themselves.",
                "117% sales growth validates cloud-native issuer processing as a structural "
                "winner over legacy monolithic platforms — legacy processors face accelerating "
                "client migration pressure.",
                "The round creates a well-capitalised independent challenger to Marqeta, "
                "Galileo, and Thredd in the global issuer-processor market.",
            ],
            "region": "Global (UK-headquartered, 68 countries)",
            "players": "Paymentology, Apis Partners, Aspirity Partners, Marqeta, Galileo",
            "tag": "Infrastructure / Product Launch",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "CBUAE Grants First Crypto SVF License — Crypto.com Cleared for Government Payments in UAE",
            "what": (
                "The Central Bank of the UAE (CBUAE) granted Foris DAX Middle East FZE "
                "(the UAE entity of Crypto.com) a Stored Value Facilities (SVF) license on "
                "May 11, 2026 — the first such license issued to a cryptocurrency platform "
                "in the UAE. The SVF authorization allows Crypto.com to hold and transfer "
                "stored monetary value on behalf of users, and specifically enables UAE "
                "residents to pay government fees using digital assets through Crypto.com's platform."
            ),
            "why": [
                "First regulated crypto payment license in the UAE marks a structural threshold "
                "— the CBUAE is deliberately operationalizing its Payment Token Services "
                "Regulation rather than leaving it as a framework document.",
                "Government fee payment is a high-trust, high-visibility use case: it signals "
                "sovereign-level acceptance of digital asset payment channels and will "
                "accelerate consumer and merchant adoption.",
                "This creates a reference precedent for other crypto players seeking SVF "
                "licenses in the UAE — a queue of applications is likely to follow ahead "
                "of the September 2026 compliance deadline for newly in-scope entities.",
                "Combined with the Digital Dirham CBDC strategy, the UAE is assembling a "
                "layered digital payments architecture spanning CBDC, regulated stablecoins, "
                "and crypto payment services.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Crypto.com (Foris DAX Middle East FZE), UAE government",
            "tag": "Regulation / Wallets",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "ECB's Lagarde Warns Euro Stablecoins Risk 'Digital Dollarisation' — Backs Public Infrastructure",
            "what": (
                "Speaking at the Banco de Espana LatAm Forum on May 8, 2026, ECB President "
                "Christine Lagarde argued that euro-denominated stablecoins carry structural "
                "weaknesses: financial instability from sudden mass redemptions and monetary "
                "policy transmission risk if deposits migrate out of the banking system. "
                "With 98% of the $310 billion stablecoin market denominated in USD, Lagarde "
                "warned of accelerating 'digital dollarisation' and called for Europe to build "
                "tokenized settlement infrastructure anchored in central bank money — "
                "specifically the ECB's digital euro programme, targeting launch by 2029."
            ),
            "why": [
                "Lagarde's speech deepens the ECB-vs-private-sector divide on stablecoin "
                "strategy: European bank consortia planning private digital euros now face "
                "explicit institutional pushback from the ECB itself.",
                "The $310B stablecoin market figure and 98% USD denomination data point "
                "establishes the scale argument for European monetary sovereignty concerns "
                "— framing this as a geopolitical and structural payment risk, not just a "
                "financial stability technicality.",
                "MiCA's EUR 200M/day cap on non-euro stablecoin transactions may face "
                "renewed pressure to be tightened or applied more aggressively as "
                "Lagarde's position hardens.",
                "For PSPs operating USDC/USDT payment corridors in Europe, regulatory "
                "trajectory is clearly restrictive — invest in MiCA-compliant euro "
                "stablecoin alternatives or SEPA Instant migration now.",
            ],
            "region": "Europe / Global",
            "players": "ECB, Christine Lagarde, European bank consortia, Circle (USDC), Tether (USDT)",
            "tag": "Stablecoins / Regulation / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "UK Open Banking: Amazon Adds Pay by Bank at Checkout; UKPI cVRP Scheme Enters Live Phase",
            "what": (
                "Two concurrent developments are accelerating UK account-to-account payment "
                "adoption in 2026. First, Amazon launched Pay by Bank as a checkout option "
                "in the UK in partnership with TrueLayer — the most significant mainstream "
                "A2A commerce moment in UK open banking history. Second, the UK Payments "
                "Initiative (UKPI) achieved its first live cVRP (commercial variable recurring "
                "payment) transactions in Q1 2026, with the FCA and PSR providing pricing model "
                "clarity that allows UKPI to operate commercially ahead of pending legislation. "
                "Variable recurring payments now account for 16% of all UK open banking payments."
            ),
            "why": [
                "Amazon's adoption removes the 'no major merchant acceptance' objection to "
                "A2A checkout in the UK and will force competitor merchants to evaluate "
                "Pay by Bank as a lower-cost alternative to card processing.",
                "UKPI cVRP going live with FCA/PSR-endorsed pricing ends a multi-year "
                "impasse on commercial VRP models — utility, financial services, and "
                "government payment use cases can now scale.",
                "16% VRP share of open banking transactions signals the inflection point "
                "where A2A recurring payments move from pilot to structural volume.",
                "Pressure on acquirers and PSPs to support open banking checkout APIs "
                "at the same quality tier as card acceptance APIs is now commercial, "
                "not just regulatory.",
            ],
            "region": "UK / Europe",
            "players": "Amazon, TrueLayer, UKPI, FCA, PSR, Open Banking Limited",
            "tag": "Open Finance / A2A / Merchant",
            "novelty": "New today",
        },
        {
            "num": "5.",
            "headline": "SWIFT ISO 20022: November 2026 Structured Address Deadline — Six Months to Hard Compliance",
            "what": (
                "With the MT/MX coexistence period ended in November 2025 and financial "
                "penalties active from January 1, 2026 for institutions still relying on "
                "in-flow translation services, the next hard SWIFT deadline arrives "
                "November 14, 2026: all cross-border payments must use fully structured "
                "or hybrid-structured postal addresses, and all financial institutions "
                "must be capable of receiving Enquiry and Investigation (E&amp;I) messages "
                "in MX format (camt.110 / camt.111). Unstructured address data will be "
                "decommissioned across CBPR+ and major national clearing systems."
            ),
            "why": [
                "Six months to a hard decommissioning deadline: institutions still running "
                "unstructured address data face message rejection, not just cost penalties, "
                "from November onwards.",
                "Structured address fields directly enable higher-quality sanctions "
                "screening and fraud pattern detection — institutions that invest in "
                "enrichment pipelines will compound operational benefits beyond compliance.",
                "Corporate clients and payment factories must update ERP/TMS format "
                "configurations now; retrofitting after November is operationally "
                "disruptive and reputationally exposed.",
                "Correspondent banking chains with weak data-quality links are systemic "
                "risk: a single non-compliant intermediary can block the entire chain.",
            ],
            "region": "Global",
            "players": "SWIFT, global correspondent banks, payment processors, ERP/TMS vendors",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — hard deadline six months out",
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

    # ── SECTION 2 : MAJOR FINTECH HEADLINES ───────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "MAS Launches Cross-Bank AI Consortium for Pre-Emptive Scam Detection",
            "what": (
                "On May 4, 2026, the Monetary Authority of Singapore announced the successful "
                "conclusion of Project MindForge Phase 2, publishing an AI Risk Management "
                "Toolkit for the financial services sector. Concurrently, MAS launched a "
                "Proof-of-Value initiative pooling transaction data across five banks, working "
                "with GovTech Singapore and the Singapore Police Force, to develop cross-institution "
                "AI/ML models capable of identifying higher-risk transactions and accounts "
                "before a scam completes — rather than detecting it after the fact."
            ),
            "why": (
                "Cross-institution AI data pooling for fraud detection is structurally new: "
                "it treats the payments ecosystem as a shared risk surface rather than a "
                "collection of isolated institutional risk models. The AI Risk Management "
                "Toolkit sets a formal governance standard for AI deployment in financial "
                "services, becoming a benchmark regulators in other markets will reference. "
                "For payments product leaders, this signals that anti-scam AI is becoming "
                "a scheme-level and ecosystem-level expectation, not just an individual bank "
                "capability."
            ),
            "strategic": (
                "MAS is institutionalising AI-based payments fraud intelligence at the "
                "ecosystem level — a model other central banks and payment schemes are likely "
                "to replicate in high-scam-risk corridors globally."
            ),
        },
        {
            "num": "2.",
            "headline": "Mastercard-BVNK $1.8B Deal: Regulatory Approvals Advancing as Stablecoin Frameworks Mature",
            "what": (
                "Mastercard's $1.8 billion acquisition of BVNK — announced in March 2026 — "
                "is progressing through regulatory review with closure expected by late 2026. "
                "BVNK's platform spans on-chain and fiat payment rails across 130+ countries, "
                "providing Mastercard with licensed stablecoin infrastructure, multi-chain "
                "settlement capability, and banking and liquidity provider relationships. "
                "The deal takes on renewed strategic weight as the US GENIUS Act "
                "implementing regulations advance (final rules expected July 2026) "
                "and global stablecoin regulatory frameworks — MiCA in Europe, Payment Token "
                "Services Regulation in UAE, MAS SCS framework in Singapore — enter enforcement phase."
            ),
            "why": (
                "Each new national stablecoin framework that reaches enforcement phase validates "
                "the strategic logic of Mastercard's acquisition: BVNK's existing licenses, "
                "compliance infrastructure, and corridor relationships become more valuable, "
                "not less, as the regulatory barrier to entry rises. Visa and other card "
                "networks face structural pressure to respond — either through M&amp;A or "
                "accelerated internal builds. For PSPs and banks, the card network stablecoin "
                "strategy pivot means new settlement options and new competitive dynamics "
                "for cross-border B2B flows within 18-24 months."
            ),
            "strategic": (
                "The Mastercard-BVNK deal is the clearest signal that card network economics "
                "are being repositioned around multi-rail settlement — stablecoin capability "
                "is transitioning from optional to table stakes for global payment networks."
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

    # ── SECTION 3 : WHAT MATTERS MOST ─────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Stablecoin regulation is bifurcating between public CBDC infrastructure "
            "and private payment instruments — with product consequences on both sides.",
            "Lagarde's ECB speech and the UAE's first crypto SVF license represent opposite "
            "ends of the same policy spectrum. Europe is hardening toward public-infrastructure "
            "primacy, while the UAE is pragmatically licensing private crypto payment operators "
            "within a structured regulatory perimeter. For payments product leaders, the "
            "strategic question is no longer 'if' stablecoins matter — it is which jurisdiction's "
            "model will prevail in your target corridors, and how your platform architecture "
            "accommodates both."
        ),
        (
            "▶  A2A payments are crossing the merchant acceptance threshold in the UK.",
            "Amazon adding Pay by Bank and UKPI's first live cVRP transactions in the same "
            "quarter marks an inflection point. The 'chicken-and-egg' A2A adoption problem "
            "— no merchant acceptance without consumer volume, no consumer volume without "
            "merchant acceptance — has been broken at the most visible e-commerce scale. "
            "Card acquirers and PSPs that have been treating open banking as a future option "
            "now face active commercial pressure."
        ),
        (
            "▶  Issuer processing and infrastructure players are racing up the stack into AI and digital assets.",
            "Paymentology's $175M raise and expansion into stablecoin processing, AI, and "
            "credit — alongside Mastercard's BVNK acquisition — signal that the issuer "
            "processing and payment infrastructure layer is consolidating around firms that "
            "can bundle traditional card processing with next-generation capabilities. "
            "Pure-play commodity processors face margin compression and client migration "
            "unless they accelerate roadmaps toward AI-augmented and digital-asset-capable platforms."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4 : IMPLICATIONS ───────────────────────────────────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  If you operate in the UAE or serve UAE-corridor payments, September 2026 "
            "is a hard regulatory deadline — not a planning horizon.",
            "The CBUAE's SVF license for Crypto.com, combined with the September 2026 "
            "compliance deadline for newly in-scope firms under Federal Decree-Law No. 6 "
            "of 2025, creates a six-month window. Open finance providers, embedded payment "
            "operators, and VA payment services without clear licensing paths need to "
            "engage CBUAE now. The reference precedent set by Crypto.com's SVF approval "
            "signals that the CBUAE is actively issuing — move fast."
        ),
        (
            "2.  Reassess your A2A product investment thesis for UK/EU markets — "
            "the merchant acceptance argument is no longer a blocker.",
            "Amazon's Pay by Bank adoption and the UKPI cVRP launch remove the two "
            "structural objections to A2A investment: lack of major merchant acceptance "
            "and absence of a commercially viable recurring payment model. If your product "
            "roadmap has deprioritised open banking payment initiation, re-evaluate "
            "urgency now. The window to establish A2A capability before it becomes table "
            "stakes for UK/EU merchant acquiring is narrowing."
        ),
        (
            "3.  Use Paymentology's roadmap as a competitive benchmark for your "
            "issuer processing or card platform strategy.",
            "The $175M raise and explicit expansion into stablecoin processing, AI-driven "
            "services, tokenization, and credit defines where issuer-processor competition "
            "is heading over the next 18-24 months. Whether you are evaluating a "
            "third-party processor, building an internal platform, or assessing a BaaS "
            "proposition, the capabilities Paymentology is building should anchor "
            "your platform requirements assessment."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 : WATCHLIST ──────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  US GENIUS Act final implementing regulations — expected July 2026.",
            "The GENIUS Act passed in July 2025 but final OCC rules governing which "
            "non-bank entities can issue payment stablecoins are due July 2026. "
            "These rules will determine market structure for USD stablecoin payments "
            "globally — watch for draft rules and comment periods that will signal "
            "the regulatory architecture for the next wave of USD stablecoin issuers."
        ),
        (
            "●  EU MiCA EUR 200M/day cap enforcement on non-euro stablecoins.",
            "MiCA's transaction cap on USDT and USDC for EU payment use cases is live "
            "in framework but enforcement posture remains unclear. As USDC/USDT usage "
            "in European payment corridors grows, watch for the EBA or national "
            "competent authorities to issue enforcement guidance that will reshape "
            "stablecoin corridor routing economics."
        ),
        (
            "●  UKPI cVRP scheme expansion to merchant payments beyond Phase 1 use cases.",
            "UKPI's Phase 1 covers utilities, financial services, and government payments. "
            "The next expansion to general merchant payments — including e-commerce — "
            "is the critical gateway to open banking displacing card payments at scale. "
            "Watch for UKPI governance announcements and FCA legislative timeline "
            "updates expected by end-2026."
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
        "This briefing is compiled from publicly available sources including central bank "
        "publications, regulatory releases, and reputable financial media. It is intended "
        "for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources: CBUAE (centralbank.ae), ECB (ecb.europa.eu), "
        "MAS (mas.gov.sg), SWIFT (swift.com), Mastercard (mastercard.com), "
        "Open Banking Limited (openbanking.org.uk), PSR (psr.org.uk), "
        "PYMNTS, Payment Expert, Fintech Global, MENA Fintech Association, "
        "The Paypers, CNBC, BusinessWire.",
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
