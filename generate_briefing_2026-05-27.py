#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 27, 2026."""

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

DATE = "May 27, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-27.pdf"

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
            "headline": "BRICS Pay Reaffirmed at May Ministerial: IPS Interoperability and CBDC Linkage on the Agenda",
            "what": (
                "At the BRICS Finance Ministers and Central Bank Governors meeting in May 2026, members "
                "formally reaffirmed commitment to advancing BRICS Pay as a multilateral cross-border "
                "payments platform. The framework targets interoperability among national instant payment "
                "systems (IPS) and CBDC networks — including India's digital rupee, China's e-CNY, and "
                "Russia's digital ruble — as an alternative settlement path that bypasses USD correspondent "
                "banking and SWIFT. More than 65% of intra-BRICS trade is already conducted in local "
                "currencies, providing commercial momentum for the infrastructure initiative."
            ),
            "why": [
                "BRICS Pay is not a single currency project — it is an IPS-CBDC interoperability layer, making it architecturally comparable to Project Nexus but geopolitically motivated.",
                "65%+ intra-BRICS local-currency trade creates genuine commercial volume to underpin the infrastructure case; this is no longer purely aspirational.",
                "The initiative directly challenges USD correspondent banking revenues and SWIFT's role in emerging-market settlement corridors involving BRICS economies.",
                "For corridor operators in India, UAE, and ASEAN corridors linked to BRICS flows, the interoperability roadmap will reshape FX liquidity and compliance requirements.",
                "The technical framework targeting 20,000 TPS puts BRICS Pay in the same processing tier as established high-volume domestic IPS — signaling serious engineering commitment.",
            ],
            "region": "Global / BRICS (India, China, Russia, Brazil, South Africa, UAE, Saudi Arabia)",
            "players": "BRICS Finance Ministers, RBI, People's Bank of China, Bank of Russia, SAMA, CBUAE",
            "tag": "Cross-Border / Infrastructure / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "Project Nexus: Indonesia Joins as 6th Partner; Technology Operator Selected — Build Phase Active",
            "what": (
                "Project Nexus, the BIS-led multilateral instant cross-border payment scheme, has entered "
                "its active build phase. Indonesia's central bank has joined as the sixth partner alongside "
                "India, Malaysia, Philippines, Singapore, and Thailand. Nexus Global Payments (NGP), "
                "incorporated in Singapore, has selected its technology operator and appointed senior "
                "executives, with sub-60-second settlement across six national IPS networks targeted for "
                "live implementation. The scheme is designed to serve 1.7+ billion people across member "
                "markets, with legal and technical framework updates expected during 2026."
            ),
            "why": [
                "Indonesia's inclusion closes a significant ASEAN gap — adding Southeast Asia's largest economy and one of its highest-volume remittance-receiving markets.",
                "Moving from blueprint to active technology build with a named operator is the most concrete operational milestone yet — 2026-2027 live deployment is now structurally credible.",
                "Nexus's hub-and-spoke design means a single technical integration gives PSPs access to all six markets — a material competitive advantage over bilateral-linkage models.",
                "Singapore's role as NGP's incorporation and operational anchor reinforces MAS's position as the region's cross-border payments infrastructure hub.",
                "PSPs serving ASEAN-India corridors need to engage Nexus readiness planning now — first-mover technical integrations will define commercial positioning for the next decade.",
            ],
            "region": "Singapore / ASEAN / India",
            "players": "BIS, MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, Bank Indonesia, NGP",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "3.",
            "headline": "SAMA Activates First Live Open Banking Licences in Saudi Arabia — B2B Data Flows Commercialising",
            "what": (
                "Saudi Arabia's Central Bank (SAMA) transitioned from regulatory sandbox to full commercial "
                "operations for open banking in early 2026, granting the first live open banking licences "
                "to approved firms. The Saudi open banking framework mandates standardised API access to "
                "account data and payment initiation for licensed third-party providers, enabling account "
                "aggregation, payment initiation, and financial management services. This follows years of "
                "SAMA-led industry consultation and sandbox testing, and positions Saudi Arabia as the "
                "GCC's most advanced open banking jurisdiction."
            ),
            "why": [
                "Live licensing — not sandbox pilots — means commercial revenue generation and compliance obligations are now real for Saudi open banking participants.",
                "Payment initiation services enabled by open banking create a direct A2A payment channel, providing an alternative to card-based consumer and B2B payments at the point of commerce.",
                "Saudi Arabia's 35M+ population and high smartphone penetration creates a large addressable market for API-native payment and financial management products.",
                "GCC fintechs and banks seeking regional scale now have a licensed open banking gateway in the Gulf's largest economy — creating cross-border product design opportunities.",
                "Regulatory sequencing signals: UAE's open finance licensing and Bahrain's earlier open banking framework now have a Saudi counterpart, creating a multi-jurisdiction GCC open finance arc.",
            ],
            "region": "Saudi Arabia / GCC",
            "players": "SAMA, Saudi banks, licensed third-party open banking providers, GCC fintechs",
            "tag": "Open Finance / Regulation / A2A",
            "novelty": "Escalation — sandbox to live commercial licensing",
        },
        {
            "num": "4.",
            "headline": "SWIFT ISO 20022: November 2026 Structured Address Hard Deadline — Cross-Industry Data Remediation Urgency",
            "what": (
                "With the MT-to-MX coexistence period having ended in November 2025, SWIFT is enforcing "
                "a hard deadline of November 2026 for structured postal address data in cross-border "
                "payment messages. From that date, payments with fully unstructured addresses will be "
                "rejected. The minimum requirement is at least a structured Town Name and Country field "
                "(hybrid addressing). Fully unstructured legacy data — prevalent across corporate "
                "ERP/TMS integrations — must be remediated before the deadline. SEPA version 3.7 "
                "updated formats (pain.001.001.09, pain.008.001.08) are already mandatory."
            ),
            "why": [
                "The November 2026 deadline is six months away — corporate data remediation programs that have not started face material rejection risk on cross-border payment flows.",
                "Structured address data is not just a compliance requirement: it directly improves sanctions screening precision and reduces false-positive rates in AML workflows.",
                "Banks with large corporate and institutional payment client bases must run coordinated outreach and data enrichment programs across counterparties and correspondent networks.",
                "ERP, TMS, and payment factory vendors face a wave of upgrade requests as corporates realize format-level changes are required in their treasury systems.",
                "Institutions treating ISO 20022 as a one-time migration project — rather than an ongoing data quality discipline — face escalating cost and operational risk as hard deadlines approach.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone banks, corporate treasuries, TMS/ERP vendors, compliance teams",
            "tag": "Infrastructure / Regulation / Fraud-Risk",
            "novelty": "Escalation — six-month hard deadline now proximate",
        },
        {
            "num": "5.",
            "headline": "Robinhood Receives MAS In-Principle Approval for Singapore Brokerage — Signals Broader Asia Buildout",
            "what": (
                "Robinhood has received an In-Principle Approval (IPA) from the Monetary Authority of "
                "Singapore (MAS) for a brokerage licence, marking its first regulatory foray into Asia. "
                "The IPA covers capital markets services and financial advisory activities. While not a "
                "payments licence, the move signals that large US retail fintech platforms — which "
                "increasingly bundle payment, savings, and investment features — are seeking regulated "
                "footholds in Singapore as a springboard for Southeast Asian market entry."
            ),
            "why": [
                "Robinhood's MAS IPA is a platform-expansion play: the company's US trajectory shows it builds toward payments, cards, and banking features after establishing an investment beachhead.",
                "Singapore's role as Asia-Pacific fintech hub means IPA holders can use MAS licensing as a trust signal for expansion into Malaysia, Thailand, and other ASEAN markets.",
                "The move intensifies competitive pressure on regional digital banks (GXS, Trust Bank, Maribank) and wealth platforms already operating in Singapore.",
                "For payments product leaders, the arrival of large US consumer fintech platforms in ASEAN with bundled financial service models will accelerate expectations for integrated account, payment, and investment experiences.",
            ],
            "region": "Singapore / ASEAN / United States",
            "players": "Robinhood, MAS, regional digital banks, incumbent brokerages",
            "tag": "Regulation / Market Structure / Product Launch",
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

    # ── SECTION 2 ──────────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Adyen Acquires Talon.One for €750M — First-Ever Acquisition Merges Payments with Loyalty Decisioning",
            "what": (
                "Adyen announced a definitive agreement to acquire Berlin-based loyalty and promotions "
                "platform Talon.One for €750 million — its first acquisition since founding. Talon.One "
                "serves 300+ global merchants, generating approximately €60M in annualised recurring "
                "revenue. The deal is expected to close H2 2026. Adyen plans to integrate Talon.One's "
                "real-time offer decisioning engine with its Unified Commerce payment stack, enabling "
                "merchants to apply consistent customer identity and targeted promotions directly within "
                "the payment flow across online and in-store channels."
            ),
            "why": (
                "This is architecturally significant: Adyen is embedding loyalty and offer decisioning "
                "into the payment moment itself — transforming the terminal and API from a clearing "
                "mechanism into a real-time commercial engagement layer. For merchants, this reduces "
                "integration complexity and unlocks personalised pricing at scale. For the payments "
                "industry, it signals that full-stack processors are expanding their value proposition "
                "upstream into the customer experience — a direct challenge to standalone loyalty "
                "platforms and marketing technology vendors."
            ),
            "strategic": "Payments platforms are absorbing adjacent commerce layers; the gateway/acquirer is evolving into a real-time commerce operating system.",
        },
        {
            "num": "2.",
            "headline": "Paymentology Raises $175M — Cloud-Native Issuer-Processing Scale Accelerates",
            "what": (
                "Paymentology, a cloud-native global issuer-processor operating across nearly 70 countries, "
                "secured $175M in a funding round co-led by private equity firms Apis Partners and "
                "Aspirity Partners. The capital will fund expansion of its processing infrastructure "
                "across emerging markets — particularly in Africa, MENA, and Southeast Asia — and "
                "accelerate product development across virtual card issuance, tokenisation, and "
                "real-time card controls."
            ),
            "why": (
                "Paymentology's raise validates the infrastructure-first embedded finance thesis: "
                "investors are backing processing-layer companies with emerging-market breadth rather "
                "than consumer-facing distribution plays. At 70-country scale, Paymentology competes "
                "directly with Marqeta, GPS, and legacy issuer-processors for embedded finance, "
                "neobank, and digital wallet clients. The MENA and SEA focus areas align directly "
                "with the UAE and Singapore payment ecosystem themes, where demand for modern "
                "issuing infrastructure is strong among digital banks and fintech licensees."
            ),
            "strategic": "Cloud-native issuer-processing infrastructure is attracting PE-scale capital as emerging-market embedded finance demand intensifies.",
        },
        {
            "num": "3.",
            "headline": "GCC Fintech Funding Rebounds to $89.4M in April — Payments and Embedded Finance Lead",
            "what": (
                "GCC fintech funding rebounded sharply to $89.4M in April 2026, the highest monthly "
                "figure for the year and the fourth consecutive month of payments and embedded finance "
                "leading sector allocation. Despite a challenging geopolitical environment, investors "
                "are directing capital into payment infrastructure, embedded finance platforms, B2B "
                "financial tools, and cross-border compliance technology. The UAE and Saudi Arabia "
                "continue to account for the majority of deal flow, with Bahrain active in regulatory "
                "sandbox licensing."
            ),
            "why": (
                "Regional funding resilience reflects the structural tailwinds of SAMA's open banking "
                "launch, the CBUAE regulatory perimeter expansion, and growing B2B digitisation "
                "demand across Gulf corporates. Payment infrastructure and compliance technology "
                "are capturing a disproportionate share — consistent with global trends favouring "
                "infrastructure over distribution. For product leaders, the GCC represents a "
                "well-capitalised and increasingly regulated market where both payments infrastructure "
                "and embedded finance propositions can scale with regulatory backing."
            ),
            "strategic": "GCC is transitioning from a growth-stage fintech market to a maturing payments infrastructure market — funding and regulation are moving in parallel.",
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
            "▶  Multilateral instant payment infrastructure is becoming geopolitically bifurcated.",
            "Two parallel multilateral IPS architectures are now in active build simultaneously: "
            "Project Nexus (BIS-led, ASEAN + India, Singapore-anchored) and BRICS Pay (member "
            "CBDC + IPS interoperability, US-dollar-bypass orientation). Both are progressing "
            "from intent to engineering reality in 2026. The global cross-border payment "
            "infrastructure landscape is fragmenting along geopolitical lines — creating "
            "corridor-level strategic choices for PSPs, banks, and central banks about which "
            "rail standards and settlement models to build toward."
        ),
        (
            "▶  Regulatory perimeters in key payments hubs are expanding rapidly — open finance and digital assets are being pulled in.",
            "SAMA's transition from sandbox to live open banking licensing, the CBUAE's licensed "
            "open finance and virtual asset payment perimeter, and MAS's application of PFMI "
            "standards to stablecoins collectively signal a coordinated GCC-Singapore regulatory "
            "maturation cycle. For firms operating across these markets, the compliance question "
            "has shifted from 'when will this be regulated?' to 'when does my licence expire if "
            "I don't act?' — September 2026 is the nearest hard deadline."
        ),
        (
            "▶  Full-stack processors are expanding their value proposition from payment clearing to commerce orchestration.",
            "Adyen's Talon.One acquisition is not an isolated deal — it is part of a broader "
            "pattern in which leading payment processors embed loyalty, identity, and offer "
            "decisioning directly into the payment stack. This redraws the boundary between "
            "payments infrastructure and merchant technology, with implications for standalone "
            "martech and loyalty vendors, for merchants evaluating platform consolidation, and "
            "for PSPs whose proposition remains narrowly defined around clearing and settlement."
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
            "1.  Take a position on which multilateral cross-border rail your platform builds toward — and when.",
            "Project Nexus and BRICS Pay are both moving from blueprint to build. If you serve "
            "ASEAN-India corridors, Nexus technical integration planning should be active now — "
            "the 2026-2027 live horizon is real. If you serve corridors involving BRICS economies "
            "(India-UAE, ASEAN-China), BRICS Pay's IPS-CBDC interoperability roadmap will create "
            "new corridor routing and FX liquidity choices by 2027. Treating these as 'watch and "
            "wait' items is no longer a neutral stance."
        ),
        (
            "2.  Engage SAMA's live open banking framework as a commercial product opportunity, not just a compliance posture.",
            "Saudi Arabia's first live open banking licences mean payment initiation and account "
            "data aggregation APIs are commercially available in the Gulf's largest market. For "
            "PSPs and embedded finance players with GCC presence, this is an A2A product launch "
            "window — not a future-state planning exercise. First movers in SAMA-licensed payment "
            "initiation will define the A2A product standard before card-based defaults entrench."
        ),
        (
            "3.  Run an ISO 20022 address data audit now — November 2026 is a six-month countdown, not a planning horizon.",
            "SWIFT's November 2026 structured address hard deadline will reject non-compliant "
            "cross-border payment messages. This is not a format upgrade — it is a data quality "
            "problem that requires counterparty outreach, ERP/TMS configuration changes, and "
            "enrichment pipeline work. Product and operations leaders who commission audits in "
            "June will have enough runway; those who wait until Q3 will face compressed and "
            "costly remediation against an immovable deadline."
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
            "●  CBUAE licensing deadline for open finance and VA payment providers — September 16, 2026.",
            "Firms newly in scope under CBUAE Federal Decree-Law No. 6 of 2025 have six months "
            "to regularise their licensing position. The September 16 deadline will trigger a "
            "wave of applications and potentially enforcement scrutiny of non-compliant UAE-based "
            "embedded finance and crypto-payment operators. Watch for early movers to use "
            "regulatory status as a competitive differentiator in the UAE market."
        ),
        (
            "●  Project Nexus legal and technical framework release — H2 2026.",
            "NGP has committed to releasing updated legal and technical implementation frameworks "
            "during 2026. These documents will define the API standards, FX liquidity model, "
            "compliance architecture, and PSP onboarding criteria for the scheme. They represent "
            "the most important structural technical input for any PSP building ASEAN cross-border "
            "payment strategy through 2027 and beyond."
        ),
        (
            "●  US consumer fintech platforms entering ASEAN — regulatory and competitive escalation.",
            "Robinhood's MAS IPA signals a wave of large US retail fintech platforms seeking "
            "regulated Asian market entry via Singapore. As these platforms bundle investments, "
            "payments, and banking features, watch for MAS to clarify activity-based licensing "
            "boundaries and for incumbent regional digital banks to respond with product and "
            "pricing adjustments. The competitive dynamic will reshape both the payments and "
            "wealth platform segments across Southeast Asia."
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
        "BRICS Brasil, Atlantic Council, Asian Banker, Manila Bulletin, Global Government Finance, "
        "MAS (mas.gov.sg), SWIFT (swift.com), BIS (bis.org), SAMA, Gulf News, Fintech Futures, "
        "Fintech Global, PYMNTS, The Paypers, Banking Dive, American Banker, CB Insights.",
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
