#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF - May 8, 2026."""

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

DATE = "May 8, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-08.pdf"

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
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "Brazil's Central Bank Bans Stablecoin and Crypto Settlement in Regulated eFX Cross-Border Payments",
            "what": (
                "Brazil's Banco Central published Resolution No. 561 on April 30, 2026, prohibiting "
                "electronic foreign exchange (eFX) providers from using stablecoins or other "
                "cryptocurrencies -- including USDT, USDC, and Bitcoin -- to settle international "
                "remittances and cross-border transfers. The rule takes effect October 1, 2026. "
                "eFX operators must now use formal foreign exchange transactions or non-resident "
                "real accounts for international settlement. The ban targets operators like Wise, "
                "Nomad, and Braza Bank that had integrated stablecoin settlement into their flows. "
                "Unauthorized firms have until May 2027 to apply for BCB approval."
            ),
            "why": [
                "Monetary sovereignty rationale: roughly 90% of regulated cross-border crypto remittances in Brazil involve stablecoins, raising BCB concerns over tax evasion, AML exposure, and capital flow control.",
                "Creates a direct policy divergence with jurisdictions (US, Singapore, UAE) actively developing regulated stablecoin payment frameworks -- corridor strategy must be jurisdiction-mapped.",
                "PSPs operating Brazil remittance corridors face a mandatory architecture change: stablecoin settlement legs must be replaced by compliant FX or non-resident account structures before October 2026.",
                "Signals that major emerging market regulators will assert control over digital rails entering official payment infrastructure, regardless of stablecoin's broader global momentum.",
            ],
            "region": "Brazil / Latin America",
            "players": "Banco Central do Brasil, Wise, Nomad, Braza Bank, eFX operators, stablecoin issuers",
            "tag": "Regulation / Cross-Border / Stablecoins",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "Singapore Incorporates SPaN to Consolidate National Payment Infrastructure Governance",
            "what": (
                "MAS and ABS have incorporated the Singapore Payments Network (SPaN), a new entity "
                "to govern Singapore's eight national payment schemes: FAST, GIRO, PayNow, SGQR, "
                "and associated infrastructure. SPaN operationally ready by end-2026. Founding board "
                "includes two MAS representatives, five D-SIB nominees, and four independent directors."
            ),
            "why": [
                "SPaN consolidates scheme governance and rule-setting under a single national body -- analogous to NPCI (India), Pay.UK, or NPP Australia in governance architecture.",
                "A unified operator enables faster scheme evolution, reducing fragmentation that currently slows PayNow feature rollout and FAST enhancement cycles.",
                "For PSPs and fintechs, SPaN creates a single scheme-level relationship for licensing, access, and pricing negotiation -- simplifying but also centralising market power.",
                "End-2026 operational readiness means scheme rule changes and access framework revisions could activate within 6-8 months -- product and compliance teams need early engagement.",
            ],
            "region": "Singapore / APAC",
            "players": "MAS, ABS, DBS, OCBC, UOB, HSBC, Citibank, Maybank, Standard Chartered, PSPs",
            "tag": "Infrastructure / Market Structure / RTP",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "UAE Digital Dirham Launches for Retail -- FIT Programme Exceeds 85% Completion",
            "what": (
                "The CBUAE officially launched the Digital Dirham (retail CBDC) for consumer and "
                "business payments in March 2026, integrating with UAE Pass and major banking apps. "
                "Cross-border capability is live with Saudi Arabia and India. The Financial "
                "Infrastructure Transformation (FIT) Programme is 85%+ complete, targeting full "
                "integration by year-end. A new CBUAE Law brought open finance providers and VA "
                "payment services within CBUAE licensing scope, with a September 16, 2026 deadline."
            ),
            "why": [
                "The Digital Dirham makes UAE one of the first countries globally to move a retail CBDC from pilot to live operational status.",
                "Live cross-border capability with Saudi Arabia and India directly competes with traditional remittance rails across two of UAE's highest-volume corridors.",
                "September 2026 licensing deadline for newly in-scope open finance and VA payment services creates immediate compliance pressure for embedded finance operators in the UAE.",
                "Combined FIT programme completion reshapes UAE's infrastructure from fragmented legacy to modern, unified digital infrastructure -- elevating its GCC and global hub position.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Aani, UAE banking sector, open finance providers, VA payment services",
            "tag": "Infrastructure / CBDC / Regulation",
            "novelty": "Escalation -- retail launch confirmed, licensing deadline active",
        },
        {
            "num": "4.",
            "headline": "SWIFT ISO 20022: November 2026 Structured Address Deadline Now Critical Path",
            "what": (
                "Following the end of MT/MX coexistence in November 2025, SWIFT activated automatic "
                "surcharges from January 1, 2026 for institutions still relying on in-flow translation "
                "or MT contingency processing. November 2026 is the hard deadline when fully "
                "unstructured postal addresses cease to be accepted. SEPA 3.7 (pain.001.001.09, "
                "pain.008.001.08, pain.002.001.10) is now mandatory, with SEPA 3.6 decommissioned."
            ),
            "why": [
                "SWIFT's pricing surcharges create escalating cost pressure for institutions that have not fully remediated customer address data and core banking configurations.",
                "Unstructured address data is a systemic gap in AML/sanctions screening quality; November 2026 ends tolerance for legacy data practices in cross-border payment flows.",
                "Banks with large corporate treasury and correspondent banking books face active data remediation touching CRM, KYC, and ERP/TMS format configurations simultaneously.",
                "SEPA 3.7 cascades into payment factory configurations -- corporate treasurers operating multi-bank setups require coordinated format-level updates before year-end.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone payment operators, corporate treasuries, TMS and ERP vendors, correspondent banks",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation -- cost penalties active, November 2026 deadline approaching",
        },
        {
            "num": "5.",
            "headline": "Stablecoin Cross-Border Settlement at Strategic Inflection: $400B Real-World Volume Meets Regulatory Bifurcation",
            "what": (
                "Adjusted stablecoin transaction volumes grew 91% to $10.9T in 2025, with real-world "
                "payment volumes doubling to ~$400B (60% estimated B2B). This drives commercial "
                "interest in stablecoins as a cross-border bridge between domestic RTP networks. "
                "However, Brazil's Resolution 561 ban and divergence between regulatory regimes -- "
                "US, Singapore, UAE developing permissive-but-structured frameworks vs. Brazil's ban -- "
                "create a bifurcated global landscape."
            ),
            "why": [
                "Stablecoin B2B settlement is no longer theoretical: ~$240B in estimated B2B stablecoin flows in 2025 represents a meaningful challenge to SWIFT for specific corridors.",
                "The Brazil ban illustrates the critical variable: whether a jurisdiction accepts stablecoin settlement inside regulated payment infrastructure, not just as a parallel activity.",
                "For PSPs, stablecoin settlement is viable in US/Singapore/UAE corridors but now carries regulatory risk in Brazil-connected flows.",
                "The convergence narrative -- stablecoins as interoperability bridge between domestic RTP networks -- depends on regulatory acceptance in both origin and destination jurisdictions.",
            ],
            "region": "Global",
            "players": "Circle (USDC), Tether (USDT), cross-border PSPs, Pix, UPI, PayNow, SEPA Instant, BCB",
            "tag": "Stablecoins / Cross-Border / Regulation",
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

    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Adyen Acquires Talon.One for 750M EUR -- First-Ever M&A Signals Shift to Commerce Intelligence",
            "what": (
                "Adyen signed a definitive agreement to acquire Berlin-based enterprise loyalty and "
                "promotions platform Talon.One for 750M EUR (~$876M) in an all-cash deal -- Adyen's "
                "first-ever acquisition. Talon.One serves 300+ enterprise merchants including H&M and "
                "Nordstrom, generates ~60M EUR ARR growing 30-40% annually. Deal close expected H2 2026."
            ),
            "why": (
                "Adyen's acquisition marks a strategic pivot beyond payment acceptance into real-time "
                "commerce decisioning. By combining Adyen's payment infrastructure and transaction data "
                "with Talon.One's real-time decisioning engine, merchants can align customer identity, "
                "pricing, and promotions dynamically at the point of transaction -- positioning Adyen "
                "as a full commerce intelligence layer. For competing PSPs and platforms, this raises "
                "the product requirement bar significantly."
            ),
            "strategic": "Leading payment processors are moving from rail-layer to commerce-intelligence platform -- product strategies that stop at acceptance risk ceding merchant value to integrated rivals.",
        },
        {
            "num": "2.",
            "headline": "Ebury Raises ~550M GBP with Santander Increasing Majority Stake to 55%",
            "what": (
                "UK-based SME cross-border payments specialist Ebury is raising approximately 550M GBP, "
                "with majority shareholder Santander committing a new 50M GBP investment to increase "
                "its stake from 50.1% to 55%. The raise reinforces Ebury's position as Europe's "
                "leading SME FX and cross-border payments platform."
            ),
            "why": (
                "Santander deepening its Ebury commitment signals strategic confidence in the SME "
                "cross-border payments segment despite competition from embedded B2B payment entrants "
                "and RTP-linked rails. The capital positions Ebury to expand geographic coverage, "
                "product depth, and potentially pursue acquisitions. For payments strategists, this "
                "confirms the specialist multi-currency SME segment retains distinct structural value."
            ),
            "strategic": "Specialist SME cross-border FX platforms retain strong investor conviction -- the SME treasury and FX segment remains a structurally distinct opportunity.",
        },
        {
            "num": "3.",
            "headline": "Squads Raises $18M from Coinbase and Solana for Stablecoin Payment Infrastructure",
            "what": (
                "Stablecoin infrastructure startup Squads raised $18M on May 7, 2026, with Coinbase "
                "Ventures and Solana Foundation participating. Capital will fund expansion of "
                "multi-signature wallet and smart treasury infrastructure for institutional stablecoin "
                "payment flows on Solana."
            ),
            "why": (
                "The timing -- one week after Brazil's stablecoin ban -- underscores the geographic "
                "bifurcation of stablecoin payment infrastructure investment. Capital is concentrating "
                "in permissive-framework jurisdictions while emerging market regulators assert control. "
                "This signals that stablecoin infrastructure investment is accelerating on compliant "
                "rails even as individual market access becomes more complex."
            ),
            "strategic": "Institutional stablecoin treasury infrastructure is attracting serious capital -- watch enterprise treasury and B2B payment orchestration use cases mature rapidly in 2026.",
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

    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "Sovereign regulators are drawing hard lines around digital rails in official payment infrastructure.",
            "Brazil's Resolution 561 reflects a broader pattern of emerging market central banks asserting "
            "monetary sovereignty over digital settlement layers inside regulated infrastructure. The divergence "
            "between permissive frameworks (US, Singapore, UAE) and restrictive ones (Brazil) is becoming a "
            "structural feature of the cross-border landscape. Multi-corridor product strategies must be built "
            "on jurisdiction-level regulatory maps, not universal stablecoin assumptions."
        ),
        (
            "Core payment infrastructure in key hubs is entering a new consolidated phase.",
            "Singapore's SPaN incorporation, UAE's FIT 85%+ completion, and SWIFT's November 2026 deadline "
            "all converge: payment infrastructure modernisation is entering its final execution and governance "
            "phase. For PSPs and banks, new scheme rules, access frameworks, and data standards will "
            "crystallise within 6-12 months -- requiring active engagement with scheme operators."
        ),
        (
            "Leading payment processors are expanding from acceptance infrastructure to commerce intelligence.",
            "Adyen's EUR 750M acquisition of Talon.One is a strategic signal about where payment processor "
            "value is moving. The next competitive layer is real-time commerce decisioning: merging transaction "
            "data, customer identity, loyalty, and dynamic pricing at the moment of payment. Product leaders "
            "who limit their roadmap to acceptance and settlement are operating a generation behind."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(f">> {title}", s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Map stablecoin regulatory posture jurisdiction-by-jurisdiction before embedding digital asset rails.",
            "The Brazil ban makes explicit that stablecoin settlement inside regulated cross-border flows is a "
            "jurisdiction-by-jurisdiction decision. For multi-corridor products, a regulatory posture map for each "
            "destination country must precede architecture decisions. Build regulatory optionality into corridor "
            "settlement design -- not stablecoin dependency."
        ),
        (
            "2.  Engage SPaN and CBUAE FIT scheme processes now -- access rules will finalise within 6-8 months.",
            "Singapore's SPaN reaches operational readiness by end-2026; the CBUAE FIT targets full integration "
            "by the same period. Both will generate new scheme rules and access criteria. Early engagement "
            "through industry consultations or working groups will allow product and compliance teams to shape "
            "-- or at minimum anticipate -- new frameworks. CBUAE September 2026 deadline is the near-term "
            "forcing function for UAE-market operators."
        ),
        (
            "3.  Reframe your ISO 20022 programme as a data quality and risk asset, not a compliance workstream.",
            "SWIFT's active pricing surcharges and the November 2026 structured address hard deadline make ISO "
            "20022 remediation a cost and risk issue with a binary deadline. Institutions that invest in genuine "
            "data enrichment -- structured address pipelines, client data remediation, AML-linked data quality -- "
            "will compound returns in sanctions screening precision, STP rates, and fraud detection."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    story.append(section_header("5.", "OPTIONAL WATCHLIST -- Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "Project Nexus live implementation: Philippines confirmed, mid-2027 corridor target.",
            "BSP Philippines confirmed integration alignment with the BIS-led Nexus multilateral instant payment "
            "scheme. PSPs in ASEAN and India corridors should begin API integration planning and FX liquidity "
            "modelling for the Nexus settlement model now."
        ),
        (
            "US GENIUS Act (stablecoin legislation) -- Senate consideration imminent.",
            "The GENIUS Act, if passed, would create the first US federal stablecoin payment framework -- directly "
            "contrasting with Brazil's ban and potentially accelerating corridor bifurcation. Watch for Senate vote "
            "timing and final framework structure on reserve, redemption, and payment-system-access requirements."
        ),
        (
            "CBUAE licensing deadline for newly in-scope firms -- September 16, 2026.",
            "Open finance providers, VA payment services, and enabling technology providers newly within CBUAE "
            "licensing scope have until September 16, 2026 to regularise. Watch for MPI and payment token "
            "service applications, and potential enforcement action against non-compliant UAE-market operators."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(f">> {title}", s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources. Intended for informational purposes only. "
        "Key sources: Banco Central do Brasil (bcb.gov.br), MAS (mas.gov.sg), CBUAE (centralbank.ae), "
        "SWIFT (swift.com), BIS (bis.org), CoinDesk, PYMNTS, Fintech Futures, Payment Expert, The Paypers, "
        "American Banker, Banking Dive, FXC Intelligence, Global Government Fintech.",
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
        title=f"Daily Payments & Fintech Intelligence Brief - {DATE}",
        author="Payments Intelligence",
        subject="Daily global payments and fintech briefing"
    )
    s = build_styles()
    story = build_story(s)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    main()
