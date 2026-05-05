#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 5, 2026."""

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

DATE   = "May 5, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-05.pdf"

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
    tag_para     = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=GREEN,
        leading=11, borderPadding=3))
    reg_para     = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para    = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
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

    # ── SECTION 1 ──────────────────────────────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "Brazil's Central Bank Bans Crypto and Stablecoin Settlement in Regulated Cross-Border eFX Rails",
            "what": (
                "On April 30, 2026, Brazil's Banco Central do Brasil (BCB) published Resolution No. 561, "
                "amending the rules governing its electronic foreign exchange (eFX) system — the "
                "regulated channel for digital international remittances, purchases, withdrawals, and "
                "transfers. The rule explicitly bans eFX participants from using virtual assets, "
                "including stablecoins and Bitcoin, to settle cross-border obligations. Payments must "
                "now clear through traditional foreign exchange transactions or non-resident Brazilian "
                "real accounts. The restriction is effective October 1, 2026."
            ),
            "why": [
                "Brazil's crypto market processes $6–8 billion monthly, with stablecoins accounting for roughly 90% of volume — this is a structural closure of a major back-end payment rail, not a marginal rule.",
                "The BCB's rationale is monetary sovereignty: foreign-issued stablecoins operating inside regulated eFX would erode state control over payment infrastructure and capital flow visibility.",
                "This is a deliberate divergence from the U.S. pro-stablecoin regulatory posture and signals that major EM central banks are drawing hard lines between digital asset investment and regulated payment infrastructure.",
                "PSPs and remittance platforms serving Brazil corridors using stablecoin settlement rails must implement alternative FX settlement mechanisms before October 1 or exit the regulated market.",
            ],
            "region": "Brazil / Latin America",
            "players": "Banco Central do Brasil, eFX payment providers, stablecoin issuers, remittance fintechs",
            "tag": "Cross-Border / Stablecoins / Regulation",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "SWIFT Blockchain Shared Ledger Enters MVP Live Transactions — 50+ Banks Enrolled in New Consumer Payments Scheme",
            "what": (
                "SWIFT has completed the design phase of its blockchain-based shared ledger and is "
                "now building the first MVP iteration for real-world transactions in 2026. The ledger "
                "is built on Linea, a permissioned Ethereum Layer-2 network developed by ConsenSys, "
                "and uses smart contracts to enable tokenized deposits, regulated stablecoins, and CBDCs "
                "to move across institutions in real time, 24/7. In parallel, SWIFT has launched a new "
                "end-to-end cross-border payments scheme for consumers and SMEs — co-developed with more "
                "than 40 banks — targeting H1 2026 MVP delivery, with over 50 banks now enrolled."
            ),
            "why": [
                "SWIFT is not just modernising its messaging layer — it is building a settlement infrastructure that can interoperate with tokenized assets and digital money, repositioning it for the next generation of cross-border financial flows.",
                "The Linea/Ethereum L2 architecture is a deliberate choice for permissioned, institutional-grade interoperability rather than public blockchain exposure, addressing risk concerns from central banks and regulated FIs.",
                "The consumer/SME payments scheme with 50+ banks is a competitive response to Project Nexus and bilateral instant payment linkages — SWIFT is asserting relevance in the sub-threshold, retail cross-border corridor.",
                "Banks signed into both tracks face integration investments at two levels: digital asset settlement (ledger) and retail cross-border scheme (API/messaging). Roadmap sequencing is now urgent.",
            ],
            "region": "Global",
            "players": "SWIFT, ConsenSys (Linea), 50+ enrolled banks, central banks, tokenized deposit issuers",
            "tag": "Infrastructure / Cross-Border / Market Structure",
            "novelty": "New material development",
        },
        {
            "num": "3.",
            "headline": "Bank Indonesia Confirmed as Full Nexus Member — BI-FAST to Join Multilateral Instant Payment Network",
            "what": (
                "Bank Indonesia (BI), previously a Special Observer in the BIS-backed Nexus scheme, "
                "confirmed full membership in early 2026 and will connect its national instant payment "
                "system, BI-FAST, to the Nexus multilateral network. Nexus Global Payments (NGP) "
                "simultaneously appointed its first Board Chair and formalized Indonesia as the "
                "sixth participant, expanding the network's reach to one of the world's largest "
                "remittance corridor nations. Indonesia's Payment System Blueprint 2030 and the ASEAN "
                "Regional Payment Connectivity framework are cited as alignment drivers."
            ),
            "why": [
                "Indonesia is a tier-1 remittance market as both a major source of migrant worker outflows and a large inbound recipient — its entry converts Nexus from a Southeast Asian experiment to a genuinely high-volume economic corridor network.",
                "With six IPS networks now connecting (India, Malaysia, Philippines, Singapore, Thailand, Indonesia), Nexus covers a combined population of ~2 billion and some of the world's most active remittance routes.",
                "Domestic clearing and settlement will remain within Indonesia under national sovereignty provisions — a model other large EM central banks are likely to study before joining similar multilateral schemes.",
                "PSPs operating in ASEAN corridors should now treat BI-FAST integration as a near-term technical requirement, not a future-state aspiration.",
            ],
            "region": "Singapore / ASEAN / Indonesia",
            "players": "Bank Indonesia, Nexus Global Payments, MAS, BIS, RBI, BSP, Bank Negara Malaysia, Bank of Thailand",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "4.",
            "headline": "DORA Enforcement Goes Active Across Europe — Grace Period Over, First Compulsion Payments Issued",
            "what": (
                "The EU's Digital Operational Resilience Act (DORA), fully applicable since January 17, "
                "2025, has entered its active enforcement phase in 2026. With only approximately 50% of "
                "in-scope firms assessed as fully compliant, National Competent Authorities (NCAs) are "
                "now conducting active enforcement reviews, automatically cross-checking Register of "
                "Information data, and issuing the first compulsion payments. Non-compliant organisations "
                "face fines up to 2% of global annual turnover or EUR 10 million (whichever is higher), "
                "with individual-level fines reaching EUR 1 million. Critical ICT third-party providers "
                "face enhanced penalties of EUR 5 million plus 1% of daily global turnover for continued "
                "non-compliance, for up to six months."
            ),
            "why": [
                "The shift from supervisory tolerance to active enforcement marks a structural step change — firms that deferred DORA remediation in 2025 now face compulsion payments and reputational risk from enforcement action.",
                "Third-party ICT provider oversight is DORA's most complex and costly dimension for payment firms reliant on cloud infrastructure, core banking platforms, and payment processing vendors.",
                "Payment infrastructure firms, PSPs, banks, and crypto-asset service providers are all in scope — DORA is not a banking-only regulation and cannot be treated as such by payments-specialist firms.",
                "For global payment platforms operating EU entities, DORA compliance gap assessments must be a board-level risk item today, not a 2027 project.",
            ],
            "region": "Europe / Global",
            "players": "NCAs, EBA, ESMA, EIOPA, payment firms, banks, cloud providers, core banking vendors",
            "tag": "Regulation / Infrastructure / Fraud-Risk",
            "novelty": "Escalation / broader impact today",
        },
        {
            "num": "5.",
            "headline": "UAE FIT Programme 85% Complete; First Open Finance Cross-Border GCC Payments Launched via Al Tareq",
            "what": (
                "The UAE's Financial Infrastructure Transformation (FIT) Programme — the CBUAE's "
                "flagship 10-initiative infrastructure modernization agenda — is reported at 85% "
                "completion, with full integration targeted for 2026. In a landmark first, UAE fintech "
                "Spare received In-Principle Approval (IPA) from the CBUAE under the Open Finance "
                "Regulatory Framework and launched the first seamless open banking-powered cross-border "
                "payment solution within the GCC using the national Al Tareq open finance scheme. This "
                "marks the transition of UAE Open Finance from regulatory framework to live product."
            ),
            "why": [
                "The FIT Programme encompasses the domestic card scheme (Jaywan), the CBDC pilot (mBridge cross-border with China), open finance, and instant payment infrastructure — its near-completion signals the UAE's payment infrastructure is approaching full-stack maturity.",
                "Spare's Al Tareq-powered GCC cross-border product is the first real-world validation that the CBUAE Open Finance Regulatory Framework is commercially operational, not just a compliance regime.",
                "Over time, open finance corridors within the GCC could link banks, fintechs, and payment providers across Saudi Arabia, UAE, and other member states — creating a regulated, API-based A2A alternative to card rails for regional transfers.",
                "Combined with the CBUAE licensing deadline of September 16, 2026 for newly in-scope firms, the UAE is simultaneously closing compliance gaps and demonstrating commercial activation of its open finance ecosystem.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Spare, Al Tareq scheme, GCC payment providers, open finance fintechs",
            "tag": "Open Finance / Cross-Border / Infrastructure",
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
            "headline": "Capital One Acquires Brex for $5.15 Billion — Corporate Payments Consolidation Accelerates",
            "what": (
                "Capital One agreed to acquire business payments and spend management fintech Brex "
                "for $5.15 billion in a cash-and-stock transaction, marking one of the largest "
                "bank acquisitions of a payments fintech in recent years. The deal gives Capital One "
                "direct access to Brex's corporate card, expense management, and payment infrastructure "
                "stack, significantly strengthening its position in the business spending and "
                "treasury management segment. The acquisition reflects escalating strategic urgency "
                "among incumbent banks to own the technology layer that sits above card rails."
            ),
            "why": (
                "The deal is a direct signal that corporate payments — expense management, "
                "spend controls, and treasury connectivity — is now a strategic battleground for "
                "major banks, not just fintechs. For payment platform leaders, this accelerates "
                "the obsolescence of white-label corporate card programs and increases pressure on "
                "standalone expense management providers. It also compresses the window for B2B "
                "payment fintechs to differentiate before being absorbed by incumbent acquirers."
            ),
            "strategic": "Bank acquisition of payment-native fintech technology layers is becoming the dominant corporate payments consolidation pattern in 2026.",
        },
        {
            "num": "2.",
            "headline": "Rain Raises $250 Million Series C at $1.95 Billion Valuation for Stablecoin Payment Infrastructure",
            "what": (
                "Rain, a stablecoin payment infrastructure platform, closed a $250 million Series C "
                "led by Iconiq Capital, valuing the company at $1.95 billion. Rain is building the "
                "rails-level infrastructure that enables merchants, PSPs, and enterprises to "
                "issue, accept, and settle using stablecoins — positioning itself as the plumbing "
                "layer between on-chain stablecoin liquidity and traditional payment acceptance "
                "networks. The raise comes as Visa's stablecoin settlement program has reached a "
                "$4.5 billion annualised run rate and Mastercard's $1.8 billion acquisition of BVNK "
                "is pending regulatory close."
            ),
            "why": (
                "Infrastructure-layer stablecoin companies are now attracting institutional-scale "
                "capital at multiples comparable to traditional payments infrastructure firms — "
                "a clear signal that institutional investors view stablecoin payment rails as a "
                "durable category, not a speculative bet. For payments product leaders, the "
                "emerging architecture of stablecoin-as-settlement-rail is maturing rapidly: "
                "Visa at $4.5B annualised, Mastercard acquiring BVNK, and Rain building the "
                "mid-market infrastructure layer together suggest a new parallel settlement stack "
                "is being institutionalized, not just experimented with."
            ),
            "strategic": "Stablecoin infrastructure is transitioning from crypto-native experiment to institutionally-backed parallel payment settlement rail, with capital and schemes now committed at scale.",
        },
        {
            "num": "3.",
            "headline": "EU Instant Payments Regulation: First Mandatory Reporting Cycle Opens — Compliance Transparency Now Mandatory",
            "what": (
                "From April 2026, the EU Instant Payments Regulation (IPR) requires all Payment "
                "Service Providers (PSPs) in scope to submit standardized annual reports to their "
                "national competent authorities. The first report, due April 9, 2026, covers "
                "retrospective data on instant payment uptake and compliance metrics. This reporting "
                "cycle is the first time regulators across the EU will have a standardized, "
                "comparable view of instant payment adoption rates, fee structures, and operational "
                "compliance across PSPs — creating a new supervisory transparency instrument."
            ),
            "why": (
                "Mandatory reporting transforms EU IPR compliance from a self-assessed internal "
                "matter into a supervised, comparable dataset visible to NCAs. PSPs that have "
                "under-invested in instant payment rollout or fee alignment will face increased "
                "supervisory attention based on comparative reporting data. For payments product "
                "leaders building Europe-facing products, IPR reporting creates both a compliance "
                "obligation and a market intelligence opportunity — understanding where peers are "
                "lagging or leading on A2A instant payment infrastructure."
            ),
            "strategic": "EU IPR reporting turns instant payment adoption into a supervised metric, accelerating compliance pressure on laggard PSPs and revealing competitive gaps across European markets.",
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
            "▶  Central banks are drawing hard lines between digital assets and regulated payment infrastructure.",
            "Brazil's stablecoin ban in regulated eFX rails and the CBUAE's September 2026 licensing "
            "deadline for virtual asset payment services both reflect a clear policy stance: central "
            "banks will permit digital assets as investment instruments, but are unwilling to cede "
            "control over regulated payment settlement infrastructure to foreign-issued, unregulated "
            "tokens. This bifurcation — between permissioned digital money (CBDCs, regulated "
            "stablecoins) and unregulated crypto rails — is the defining regulatory theme of 2026 "
            "for cross-border payment operators."
        ),
        (
            "▶  SWIFT and Nexus are both racing to own the next layer of cross-border payment settlement.",
            "SWIFT's blockchain ledger MVP and new consumer payments scheme with 50+ banks, alongside "
            "Nexus's expansion to six national IPS networks covering 2 billion people, represent two "
            "structurally different but complementary bets on the future of cross-border payments. "
            "SWIFT is extending its intermediary network into tokenized asset settlement; Nexus is "
            "removing intermediaries entirely for IPS-to-IPS flows. Both are approaching real-world "
            "deployment simultaneously, creating genuine competitive pressure on correspondent banking "
            "corridors and specialist cross-border fintechs."
        ),
        (
            "▶  Regulation is compressing the timeline for compliance investment — DORA, UAE licensing, and EU IPR all have 2026 hard dates.",
            "DORA active enforcement, UAE's September 16 licensing regularization deadline, and the "
            "EU IPR reporting cycle all represent regulatory hard dates that are now inside a "
            "six-month operating window. Payment firms that treated 2025 as a planning year must "
            "treat 2026 as an execution year. The cost of deferral is now financial (fines, penalties, "
            "surcharges) rather than just reputational."
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
            "1.  If you operate cross-border corridors touching Brazil, you have five months to replace stablecoin settlement rails.",
            "BCB Resolution No. 561 is unambiguous: stablecoin and crypto settlement in regulated eFX "
            "flows ends October 1, 2026. That is a fixed technical and legal migration deadline — not a "
            "guidance date. PSPs and remittance platforms should immediately audit which settlement "
            "legs rely on virtual asset rails, assess traditional FX settlement alternatives, and "
            "escalate this as a product-critical compliance risk. Waiting for the October deadline "
            "creates unacceptable operational exposure."
        ),
        (
            "2.  DORA compliance is not an IT risk project — it is a payments product risk.",
            "With active enforcement underway and 50% of firms still not fully compliant, DORA's "
            "third-party ICT oversight requirements directly affect how payment platforms contract "
            "with cloud providers, core banking vendors, and payment processing partners. Product "
            "leaders must understand which third-party dependencies sit inside DORA's Register of "
            "Information obligations and ensure ICT concentration risk is surfaced and managed — "
            "not delegated entirely to technology teams."
        ),
        (
            "3.  Stablecoin infrastructure is becoming a strategic vendor decision, not a crypto experiment.",
            "Rain at $1.95 billion, Mastercard acquiring BVNK, Visa at $4.5 billion annualised — "
            "these are infrastructure-level commitments, not pilots. Payment product leaders at "
            "banks, PSPs, and payment platforms should be making deliberate decisions now about "
            "whether to build, buy, or partner for stablecoin settlement capability. The window "
            "for 'wait and see' is narrowing: major schemes have placed their bets and the "
            "infrastructure layer is consolidating around a small number of well-capitalised players."
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
            "●  SWIFT blockchain shared ledger — first live tokenized deposit transactions (H1 2026).",
            "SWIFT's MVP live transaction milestone is targeted for H1 2026, meaning a real-world "
            "tokenized deposit transfer across institutions on the Linea ledger could be announced "
            "within weeks. Watch for the bank participants named in the first live transactions — "
            "they will signal which institutions are positioning as early adopters of DLT-based "
            "settlement infrastructure within the SWIFT network."
        ),
        (
            "●  G20 Cross-Border Payments Roadmap — 2025 targets assessment due (FSB / BIS).",
            "The FSB and BIS are expected to publish their assessment of progress against the G20 "
            "2025 cross-border payment targets (cost, speed, transparency, access) in mid-2026. "
            "The assessment will determine whether the targets will be extended, revised, or "
            "replaced for the next phase — a significant input to regulatory and infrastructure "
            "roadmaps for all major payment hubs including Singapore, UAE, and the EU."
        ),
        (
            "●  MAS MPI licensing pipeline for institutional digital payment players.",
            "Following Ripple's expanded MPI license from MAS in Q1 2026, watch for additional "
            "institutional digital payment applicants entering MAS's licensing pipeline. Singapore's "
            "regulator is clearly building a diversified ecosystem of regulated digital payment "
            "infrastructure players alongside traditional rails — a trend that will accelerate as "
            "Project Nexus approaches live implementation and creates demand for regulated FX "
            "and liquidity providers within the scheme."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, and reputable financial media. It is intended for informational purposes "
        "only and does not constitute investment, legal, or regulatory advice. Key sources: "
        "Banco Central do Brasil (bcb.gov.br), SWIFT (swift.com), BIS (bis.org), CBUAE (centralbank.ae), "
        "Bank Indonesia (bi.go.id), MAS (mas.gov.sg), Regulation-DORA.eu, CoinDesk, CNBC, "
        "Fortune, Fintech Futures, The Paypers, Ledger Insights, The Asian Banker, Central Banking.",
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
