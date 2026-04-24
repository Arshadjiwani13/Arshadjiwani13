#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF using ReportLab."""

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

DATE = "April 24, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-04-24.pdf"

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
            "headline": "Federal Reserve Proposes Cross-Border Expansion for FedNow",
            "what": (
                "On April 8, 2026, the Federal Reserve issued a formal proposal to amend Regulation J "
                "Subpart C, which governs FedNow®. The amendment would allow U.S. member banks to "
                "designate non-Federal Reserve intermediaries to handle the international leg of "
                "cross-border transfers — effectively making FedNow capable of settling the domestic "
                "USD leg of international payments instantly. The public comment window closes June 7, 2026."
            ),
            "why": [
                "FedNow has been domestic-only since launch; this is the first structural step toward making it a cross-border-capable settlement rail.",
                "Correspondent banks and specialist PSPs can become designated intermediaries — reshaping competitive positioning for USD cross-border corridors.",
                "Persistent challenges include FX processing complexity, multi-jurisdiction compliance, and still-low FedNow adoption among smaller U.S. institutions.",
                "Creates competitive pressure on SWIFT, card rails, and fintech cross-border players for domestic USD settlement legs.",
            ],
            "region": "United States",
            "players": "Federal Reserve, U.S. banks, correspondent banks, cross-border PSPs",
            "tag": "Cross-Border / RTP",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "Project Nexus Enters Live Implementation — Philippines Confirms Connectivity",
            "what": (
                "Nexus Global Payments (NGP), incorporated in Singapore by BIS and five central bank "
                "partners (MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand), is "
                "progressing toward live implementation of the world's first multilateral instant "
                "cross-border payment scheme. The Philippines' BSP confirmed integration alignment "
                "in March 2026, with full onboarding targeted by mid-2027. The scheme targets "
                "sub-60-second settlement across five national IPS networks, serving 1.7 billion people."
            ),
            "why": [
                "Unlike bilateral instant payment linkages, Nexus creates a hub-and-spoke scheme layer enabling any-to-any corridor connectivity via a single connection.",
                "PSPs in connected markets must rethink corridor pricing, FX liquidity management, and compliance architecture against a 2027 live horizon.",
                "Singapore's role as NGP's incorporation jurisdiction reinforces its position as Asia-Pacific's payments infrastructure anchor.",
                "Central bank-backed multilateral infrastructure reduces fragmentation risk inherent in bilateral linkage proliferation.",
            ],
            "region": "Singapore / Asia-Pacific",
            "players": "MAS, BIS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, NGP",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "3.",
            "headline": "SWIFT ISO 20022: Pricing Penalties Active, Structured Address Deadline Approaching",
            "what": (
                "Following the end of the MT/MX coexistence period in November 2025, SWIFT activated "
                "automatic surcharges from January 1, 2026 for institutions still relying on in-flow "
                "translation services or contingency MT processing. SEPA version 3.7 is now mandatory, "
                "introducing updated pain.001.001.09 credit transfer and pain.008.001.08 direct debit "
                "formats. A hard deadline for fully structured postal address fields (structured country "
                "code and town name minimum) applies from November 2026."
            ),
            "why": [
                "SWIFT's pricing lever is the most direct mechanism to accelerate compliance — institutions now face real and escalating cost consequences for inaction.",
                "Unstructured legacy address data is a systemic AML/sanctions weakness; structured ISO 20022 data directly enhances screening precision and reduces false positives.",
                "Banks with large corporate client bases face active data remediation programs to meet November 2026 structured address requirements.",
                "SEPA 3.7 changes cascade into ERP/TMS configurations — payment factories and corporate treasury integrations require format-level updates now.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone payment operators, corporate treasuries, TMS/ERP vendors",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — cost penalties now active",
        },
        {
            "num": "4.",
            "headline": "CBUAE Tightens AML/CFT Expectations; Open Finance Now a Licensed Activity",
            "what": (
                "The Central Bank of the UAE published revised AML/CFT/CPF guidance on April 16, 2026, "
                "signaling a structural shift from procedural compliance toward continuous, "
                "technology-enabled risk management. This follows the landmark CBUAE Law (Federal "
                "Decree-Law No. 6 of 2025), effective September 2025, which brought open finance "
                "service providers and virtual asset payment services explicitly within CBUAE "
                "licensing scope for the first time. Newly in-scope entities have until September 16, 2026 to regularise."
            ),
            "why": [
                "Open finance providers and VA payment services are now explicitly licensed activities — a major regulatory perimeter expansion with real licensing and capital implications.",
                "The shift to continuous, technology-enabled risk monitoring raises the bar for RegTech adoption across UAE-regulated payment firms.",
                "Combined with the Consumer Protection Regulation (issued April 15, 2026), CBUAE is executing a synchronized multi-dimensional regulatory modernization.",
                "September 2026 creates a compressed compliance runway for embedded finance and crypto-payment operators in the UAE.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, payment service providers, open finance platforms, VA payment services, RegTech firms",
            "tag": "Regulation / Fraud-Risk",
            "novelty": "New today",
        },
        {
            "num": "5.",
            "headline": "MAS Calls for PFMI-Standard Oversight of Systemic Stablecoins at IMF Meetings",
            "what": (
                "At the IMF Spring Meetings on April 13, 2026, a senior MAS official called for "
                "stablecoins with systemic payment relevance to be assessed under the Principles for "
                "Financial Market Infrastructures (PFMI) — the same standards applied to systemically "
                "important payment systems, CCPs, and CSDs. This positions MAS as a global leader in "
                "applying robust FMI regulation to large-scale stablecoin networks rather than "
                "treating them as a distinct asset class."
            ),
            "why": [
                "PFMI application to stablecoins would impose settlement finality, liquidity risk management, operational resilience, and governance standards currently required of central infrastructure.",
                "This significantly raises the compliance bar for large stablecoin issuers seeking payment-system scale, narrowing regulatory arbitrage.",
                "MAS is positioning Singapore as the intellectual framework-setter for stablecoin payment governance — differentiating from U.S. and EU approaches.",
                "PSPs and banks building stablecoin payment overlays must monitor whether PFMI criteria become a licensing or interoperability prerequisite.",
            ],
            "region": "Singapore / Global",
            "players": "MAS, IMF, global stablecoin issuers, BIS, central banks",
            "tag": "Stablecoins / Regulation / Market Structure",
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
            "headline": "Embedded Finance Passes $197bn in 2026 — Infrastructure Layer Captures Outsized Value",
            "what": (
                "The embedded finance market has grown from $148bn in 2025 to a projected $197bn "
                "in 2026, maintaining a ~31% CAGR through 2034. Growth is concentrated in B2B "
                "infrastructure — payments APIs, compliance-as-a-service, embedded lending tooling — "
                "rather than consumer-facing neobank distribution. 2025 recorded the highest-ever "
                "fintech M&A transaction count, and 2026 is expected to be an execution and "
                "consolidation year for infrastructure players."
            ),
            "why": (
                "The shift from consumer fintech to infrastructure fintech redefines where margin "
                "pools accrue. Platform-layer players — BaaS, orchestration, compliance APIs — "
                "are capturing value previously held in distribution. For payments product leaders, "
                "orchestration and API-led connectivity are becoming durable structural moats, not "
                "just operational necessities."
            ),
            "strategic": "Infrastructure-first embedded finance is outpacing consumer neobanks as the primary value-capture layer in 2026.",
        },
        {
            "num": "2.",
            "headline": "Ripple Secures Expanded MAS MPI License — Institutional Digital Payments Widen",
            "what": (
                "Ripple obtained an expanded Major Payment Institution (MPI) license from MAS, "
                "allowing broader institutional digital payment services in Singapore. This positions "
                "Ripple to serve regulated institutional cross-border payment flows in the Singapore "
                "market, complementing existing corridor operations in the Middle East and Asia-Pacific."
            ),
            "why": (
                "In the context of Project Nexus and Singapore's role as a regional cross-border "
                "payments hub, a regulated institutional digital asset payment player with MAS "
                "approval adds a new competitive vector against traditional correspondent banking "
                "and remittance corridors. The MPI license signals MAS's continued openness to "
                "regulated digital payment rails alongside traditional infrastructure."
            ),
            "strategic": "MAS-licensed digital asset payment infrastructure is becoming a credible institutional option in Singapore cross-border corridors.",
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
            "▶  Domestic instant rails are going cross-border — and competing for the same flows.",
            "FedNow's cross-border proposal and Project Nexus's live-implementation phase signal that "
            "the RTP infrastructure layer is extending internationally. This is not marginal: it "
            "redraws the competitive boundary between domestic settlement, correspondent banking, and "
            "specialist cross-border rails. The 2027 horizon is structurally significant for USD and "
            "ASEAN corridor strategies."
        ),
        (
            "▶  Regulatory perimeter expansion is accelerating across key payments hubs.",
            "UAE's CBUAE Law and MAS's PFMI stablecoin stance both reflect deliberate expansion of "
            "the regulatory perimeter to cover open finance, digital assets, and technology enablers "
            "of payments. Firms operating across these jurisdictions face compressed timelines for "
            "licensing uplift, governance restructuring, and technology-enabled compliance investment."
        ),
        (
            "▶  ISO 20022 data quality is becoming a cost and risk variable, not just a compliance exercise.",
            "SWIFT's pricing penalties for non-compliant address data and SEPA 3.7 mandatory adoption "
            "shift ISO 20022 from a migration project to an ongoing operational and risk management "
            "discipline. Institutions that invest in structured data quality will derive compounding "
            "returns in fraud detection, sanctions screening, and STP — outperforming those treating "
            "it as a one-time project."
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
            "1.  Monitor the FedNow cross-border comment period closely (closes June 7).",
            "The comment window will reveal which correspondent banks and PSPs are positioning as "
            "designated intermediaries for cross-border FedNow flows. This shapes competitive "
            "architecture for USD corridors through 2027+. If your firm handles USD cross-border "
            "payments, a formal regulatory response may be warranted to influence the intermediary "
            "framework before it crystallises."
        ),
        (
            "2.  Accelerate Project Nexus readiness if you operate in ASEAN or India corridors.",
            "With NGP incorporated and live implementation underway, PSPs in connected markets need "
            "to begin technical integration planning now. The mid-2027 onboarding timeline is closer "
            "than it appears. Early movers on API connectivity, FX liquidity for Nexus corridors, "
            "and compliance alignment will have structural first-mover advantages."
        ),
        (
            "3.  Treat ISO 20022 structured data as a product and risk asset, not just a compliance task.",
            "SWIFT's January 2026 pricing penalties are the opening move; November 2026 structured "
            "address hard deadline is the closing one. Leaders who frame this as a data quality "
            "program — investing in enrichment pipelines, client data remediation, and downstream "
            "ML-based fraud and sanctions benefit — will outperform those running it as a one-time "
            "migration workstream."
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
            "●  RTP Network (TCH) domestic-correspondent launch — September 2026.",
            "The Clearing House's RTP network is targeting September 2026 for domestic-correspondent "
            "activity as a precursor to full cross-border capability. Watch for intermediary "
            "announcements and competitive positioning from Visa, Mastercard, and digital-asset "
            "cross-border players."
        ),
        (
            "●  CBUAE licensing deadline for newly in-scope firms — September 16, 2026.",
            "The six-month window for open finance providers and VA payment services to regularise "
            "under the CBUAE Law closes in September. Watch for a wave of license applications and "
            "potential enforcement actions against non-compliant operators in the UAE market."
        ),
        (
            "●  Cross-border data interoperability standards — BIS/FSB/FATF framework convergence.",
            "Global payments move fast, but jurisdictional data rules and structured messaging gaps "
            "are creating new 'data border' bottlenecks. Watch for BIS, FSB G20 cross-border "
            "payments roadmap, and FATF to issue coordinated frameworks addressing data interoperability "
            "in cross-border payment flows — a structural constraint that no single rail can solve alone."
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
        "Federal Reserve (federalreserve.gov), MAS (mas.gov.sg), SWIFT (swift.com), BIS (bis.org), "
        "CBUAE (centralbank.ae), American Banker, PYMNTS, Payment Expert, Sullivan &amp; Cromwell, "
        "White &amp; Case, Norton Rose Fulbright, FXC Intelligence.",
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
