#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 18, 2026."""

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

DATE   = "May 18, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-18.pdf"

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


def tag_row(tag, novelty, region, players, s):
    tag_para = Paragraph(
        f"<font color='white'><b> {tag} </b></font>",
        ParagraphStyle("tag", fontSize=8, fontName="Helvetica-Bold",
                        textColor=WHITE, backColor=NAVY, leading=11, borderPadding=3))
    novelty_para = Paragraph(
        f"<font color='white'><b> {novelty} </b></font>",
        ParagraphStyle("nov", fontSize=8, fontName="Helvetica-Bold",
                        textColor=WHITE, backColor=GREEN, leading=11, borderPadding=3))
    reg_para = Paragraph(
        f"<b>Region:</b> {region}",
        ParagraphStyle("reg", fontSize=8, fontName="Helvetica",
                        textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(
        f"<b>Players:</b> {players}",
        ParagraphStyle("play", fontSize=8, fontName="Helvetica",
                        textColor=HexColor("#333333"), leading=11))
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

    # ── SECTION 1: TOP PAYMENTS HEADLINES ──────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "SWIFT ISO 20022: November 2026 Structured Address Deadline Is Now the Execution Imperative",
            "what": (
                "With the MT/MX coexistence period closed since November 2025 and surcharges active "
                "from January 1, 2026 for institutions still using in-flow translation or contingency "
                "MT processing, the industry now faces the next hard deadline: structured postal "
                "addresses — including mandatory country codes and town names — must be embedded in "
                "all payment instructions by November 2026. SWIFT has also confirmed that all "
                "financial institutions must be able to receive Exceptions and Investigations (E&amp;I) "
                "messages in MX format (camt.110/111) from November 14, 2026, and MT101 "
                "multi-instruction messages will be rejected from the same date."
            ),
            "why": [
                "The January 2026 pricing penalties are the market's first tangible cost signal — institutions still on translation services are incurring escalating charges today.",
                "Unstructured address fields are a systemic AML and sanctions-screening weakness; structured ISO 20022 data directly reduces false positives and improves screening precision.",
                "Banks with large corporate client bases face active client data remediation programs — ERP and TMS integrations require format-level updates for SEPA 3.7 and CBPR+ simultaneously.",
                "MT101 discontinuation affects multibank direct debit instructions; corporates and their banks need to confirm readiness across all correspondent relationships now.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, eurozone payment operators, corporate treasuries, TMS/ERP vendors, correspondent banks",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — active cost penalties, 6-month countdown to Nov deadline",
        },
        {
            "num": "2.",
            "headline": "UAE Central Bank Expands Regulatory Perimeter: Virtual Asset Payments and DeFi Now Licensed Activities",
            "what": (
                "Federal Decree-Law No. 6 of 2025, which came into force in September 2025, brought "
                "virtual assets, stablecoins, tokenized real-world assets, DeFi protocols, "
                "decentralized exchanges, wallets, and blockchain infrastructure under the Central "
                "Bank of the UAE's (CBUAE) direct authority — a landmark perimeter expansion. "
                "The compliance deadline for all newly in-scope entities is September 16, 2026. "
                "The CBUAE also approved the UAE's first regulated USD-backed stablecoin in January "
                "2026 under the Payment Token Services Regulation, and granted a Stored Value "
                "Facility license to Crypto.com — the first such license issued to a "
                "cryptocurrency platform globally."
            ),
            "why": [
                "The perimeter expansion is comprehensive — embedded finance platforms, crypto payment gateways, and open finance providers all face new licensing and capital requirements.",
                "A September 2026 compliance deadline creates a compressed 4-month runway for affected entities to regularise, driving urgency for licensing applications and governance restructuring.",
                "The USD-backed stablecoin approval signals CBUAE's appetite to license regulated digital payment instruments, not just restrict them — a materially different regulatory posture.",
                "UAE is accelerating toward its 2026 cashless transaction target, and this regulatory infrastructure is the enabling architecture for that national priority.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, virtual asset payment providers, stablecoin issuers, open finance platforms, Crypto.com, embedded finance operators",
            "tag": "Regulation / Market Structure",
            "novelty": "Escalation — Sept 2026 compliance deadline now 4 months away",
        },
        {
            "num": "3.",
            "headline": "A2A Payments Structurally Embedded in Europe: One Year of Mandatory SEPA Instant — PSD3/PSR Agreement Reinforces",
            "what": (
                "One year after the SEPA Instant Credit Transfer Regulation mandated instant payment "
                "availability across eurozone institutions, A2A payment flows have transitioned from "
                "experimental to structurally embedded in European market infrastructure. The "
                "November 2025 political agreement between the European Parliament and Council on "
                "PSD3 and the Payment Services Regulation (PSR) deepens this further: PSR will "
                "legally mandate payment service institutions to share fraud intelligence via shared "
                "data infrastructure, and will strengthen consumer protections for A2A transactions. "
                "Pan-European scheme Wero is gaining material traction as a consumer A2A wallet overlay."
            ),
            "why": [
                "A2A is no longer a challenger to cards in Europe — it is the structurally mandated default, backed by regulation, real-time infrastructure, and competitive scheme development.",
                "Mandatory fraud intelligence sharing under PSR creates new compliance obligations for all eurozone PSPs and introduces a new category of shared infrastructure dependency.",
                "Wero's rise signals that pan-European scheme overlay is a viable commercial model, putting pressure on domestic wallet operators and card-on-file incumbents.",
                "PSD3/PSR will require product and compliance redesign across onboarding, authentication, fraud controls, and consumer recourse — a material product development cycle.",
            ],
            "region": "Europe",
            "players": "EBA, European Commission, eurozone PSPs, Wero, national payment authorities, card networks",
            "tag": "RTP / Open Finance / Regulation",
            "novelty": "Follow-up with material update — PSD3/PSR political agreement reached Nov 2025",
        },
        {
            "num": "4.",
            "headline": "UK APP Fraud Independent Review Due Q2 2026 — PSR/FCA Integration Signals Elevated Enforcement",
            "what": (
                "The UK Payment Systems Regulator (PSR) launched an independent review of the "
                "Authorised Push Payment (APP) fraud Reimbursement Requirement, introduced in "
                "October 2023 with a mandatory reimbursement cap of £415,000 per claim. The review "
                "report is due in Q2 2026, coinciding with the expected integration of the PSR into "
                "the Financial Conduct Authority (FCA) — a structural consolidation that is expected "
                "to accelerate enforcement of APP fraud rules, including transaction monitoring "
                "obligations, screening requirements, and reimbursement compliance for payment and "
                "e-money institutions."
            ),
            "why": [
                "The review could trigger recalibration of the £415,000 cap, the 50/50 cost-sharing model between sending and receiving PSPs, and the consumer eligibility criteria — all materially affecting PSP liability models.",
                "PSR/FCA integration concentrates payment-specific enforcement authority in a single, more powerful regulator — raising the enforcement risk for non-compliant payment firms.",
                "UK firms must ensure transaction monitoring systems, fraud detection controls, and reimbursement workflows are fully documented and audit-ready before the report lands.",
                "The UK APP fraud framework is a global policy benchmark — the review findings will influence regulatory design in Singapore, Australia, and the EU under PSR.",
            ],
            "region": "United Kingdom",
            "players": "PSR, FCA, UK banks, payment institutions, e-money institutions, APP fraud victims",
            "tag": "Fraud-Risk / Regulation",
            "novelty": "Escalation — review report imminent in Q2 2026",
        },
        {
            "num": "5.",
            "headline": "Central Banks Rewriting Cross-Border Playbook: FedNow Proposes Intermediary Model; Data Borders Emerge as New Bottleneck",
            "what": (
                "Two structurally significant cross-border payment developments are converging. "
                "First, the Federal Reserve has proposed allowing U.S. member banks to designate "
                "non-Federal Reserve intermediaries to handle the international leg of payments — "
                "effectively enabling FedNow to settle the domestic USD leg of cross-border "
                "transactions instantly. Second, a new systemic constraint is emerging: while "
                "payment rails have become faster globally, jurisdictional data regulations, "
                "unstructured legacy messaging, and fragmented KYC/AML data standards are creating "
                "'data border' bottlenecks that slow compliance processing even when settlement "
                "is instantaneous."
            ),
            "why": [
                "FedNow's cross-border extension would reposition it as a strategic rail for USD corridor settlement — creating competitive pressure on correspondent banks, SWIFT, and fintech cross-border specialists.",
                "The 'data border' problem is structurally underappreciated: ISO 20022's data richness is necessary but not sufficient — regulatory fragmentation across jurisdictions creates non-payment compliance latency that no single rail can solve.",
                "Organisations building cross-border payment products must now design for data compliance architecture as explicitly as settlement architecture.",
                "G20 cross-border payments roadmap deadlines and BIS/FSB frameworks targeting frictionless data exchange become critical infrastructure dependencies, not optional enhancements.",
            ],
            "region": "United States / Global",
            "players": "Federal Reserve, BIS, FSB, SWIFT, correspondent banks, cross-border PSPs, G20 central banks",
            "tag": "Cross-Border / RTP / Infrastructure",
            "novelty": "New today — data border bottleneck emerging as systemic constraint",
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

    # ── SECTION 2: MAJOR FINTECH HEADLINES ─────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Fasset Raises $51M to Scale Stablecoin-Powered Payments Across 50+ Emerging Market Corridors",
            "what": (
                "Dubai-headquartered Fasset closed a $51 million raise backed by Japan's SBI Group, "
                "Investcorp, and Turkey's Arz Portföy, to expand its stablecoin-powered banking "
                "and payment platform. Fasset processes over $32 billion in annualised payment "
                "volume across more than 50 corridors spanning Asia, Africa, and the Middle East. "
                "The raise comes weeks after a series of prominent stablecoin payment raises in "
                "the same corridors, underscoring GCC and emerging market appetite for regulated "
                "digital payment infrastructure."
            ),
            "why": (
                "Fasset's model — using stablecoins as the settlement layer across emerging market "
                "corridors — directly challenges both traditional remittance networks and "
                "correspondent banking arrangements for high-cost, low-liquidity corridors. "
                "The SBI Group backing adds Japanese institutional credibility and potential "
                "corridor expansion into Japan–Asia flows. For payments leaders, this signals "
                "that stablecoin settlement is moving from proof-of-concept to institutional-scale "
                "commercial infrastructure in GCC and emerging market corridors."
            ),
            "strategic": "Stablecoin-powered corridor payments are attracting institutional capital and reaching commercial scale — the window for traditional remittance incumbents to respond is narrowing.",
        },
        {
            "num": "2.",
            "headline": "Keel Emerges from Stealth as Profitable BaaS Infrastructure Platform After Neobank Pivot",
            "what": (
                "UK-based Keel has emerged from stealth with a profitable Banking-as-a-Service "
                "platform offering payments processing, card issuing, multi-currency infrastructure, "
                "and compliance services to fintech companies — after pivoting away from a "
                "consumer neobank model. Keel joins a growing list of infrastructure-first "
                "fintech players capturing margin through enabling capabilities rather than "
                "direct-to-consumer distribution, a pattern consistent with 2026's broader "
                "shift from neobank proliferation to embedded finance infrastructure."
            ),
            "why": (
                "The neobank-to-BaaS pivot is itself a signal: consumer fintech distribution is "
                "commoditising while infrastructure enablement — compliance APIs, multi-currency "
                "rails, card issuing — retains pricing power. Keel's profitability claim at launch "
                "is notable; it indicates a unit-economics discipline that contrasts with "
                "burn-driven neobank models. For payments leaders evaluating BaaS partnerships, "
                "the market is now segmenting into profitable infrastructure specialists vs. "
                "scale-at-any-cost consumer distributors."
            ),
            "strategic": "Infrastructure-first BaaS platforms are outcompeting consumer neobanks on margin — the payments enabling layer is where durable fintech value is accruing in 2026.",
        },
        {
            "num": "3.",
            "headline": "Real-Time Payments and A2A Infrastructure Now Cover 80+ Live Schemes Globally — Multi-Rail Architecture Becomes Table Stakes",
            "what": (
                "A 2026 market report confirms that real-time payment schemes now exceed 80 live "
                "networks globally, underpinned by ISO 20022's data-rich messaging standard. "
                "A2A payment volumes in markets with mature instant infrastructure — India (UPI), "
                "Brazil (Pix), UK (Faster Payments), EU (SEPA Instant) — have reached dominant "
                "share in domestic retail payments. Cross-border RTP connectivity projects, "
                "including Project Nexus and bilateral IPS linkages, are extending this to "
                "international corridors."
            ),
            "why": (
                "The 80+ scheme figure is more than a market milestone — it creates a multi-rail "
                "orchestration imperative for any PSP operating across multiple geographies. "
                "No single rail covers all corridors; smart routing across domestic RTP schemes, "
                "correspondent networks, and emerging cross-border linkages is now a core product "
                "capability, not an enhancement. Payments platforms that cannot orchestrate "
                "across rails face structural cost and speed disadvantages."
            ),
            "strategic": "Multi-rail orchestration is now foundational payment infrastructure — PSPs without it face compounding cost and competitive disadvantage as RTP scheme coverage expands.",
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

    # ── SECTION 3: WHAT MATTERS MOST ───────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  ISO 20022 structured data quality is now a live cost and risk variable — not a future project.",
            "SWIFT's January 2026 pricing penalties transformed ISO 20022 compliance from a "
            "migration project into an ongoing operational cost driver. The November 2026 structured "
            "address hard deadline — six months away — means institutions that have not launched "
            "client data remediation programs are now behind schedule. Leaders who frame this as a "
            "data quality and fraud reduction investment, rather than a compliance checkbox, will "
            "outperform peers by deriving compounding returns in sanctions screening precision, "
            "AML false positive reduction, and STP rates."
        ),
        (
            "▶  Regulatory perimeters in payments are expanding faster than most firms have planned for.",
            "UAE's CBUAE Law and the UK PSR/FCA merger both signal a sustained pattern: regulators "
            "are deliberately widening scope to capture previously unregulated payment activities — "
            "open finance, virtual asset payments, embedded finance. In Europe, PSD3/PSR adds "
            "mandatory fraud intelligence sharing to the compliance stack. Firms operating across "
            "these jurisdictions face a compounding multi-regulator compliance burden that demands "
            "centralised regulatory change management capability, not jurisdiction-by-jurisdiction "
            "reactive compliance."
        ),
        (
            "▶  The cross-border payments architecture debate is entering its decisive phase.",
            "FedNow's proposed cross-border intermediary model and the emergence of 'data borders' "
            "as a systemic constraint both signal that the cross-border payments architecture question "
            "is no longer theoretical. The 2027 horizon for Project Nexus, FedNow cross-border "
            "capability, and structured data compliance convergence means strategic decisions made "
            "in the next 12 months — on rail selection, intermediary relationships, and compliance "
            "data architecture — will define competitive positioning for the decade."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4: IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER ──────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Launch or accelerate ISO 20022 structured address data remediation — the November 2026 deadline is 6 months away.",
            "If your institution is still relying on SWIFT's in-flow translation services, you are "
            "paying escalating surcharges today. More urgently, the November 2026 structured address "
            "deadline requires client-level data to be fully structured across all payment "
            "instructions. This is a client-facing data collection exercise as much as an internal "
            "systems change — start with your highest-volume corporate clients and work outward. "
            "Frame the investment in terms of fraud reduction, screening efficiency, and STP gains, "
            "not just compliance cost."
        ),
        (
            "2.  If you operate in the UAE or serve UAE-regulated clients, audit your CBUAE license position now.",
            "September 16, 2026 is the compliance deadline for entities newly in-scope under "
            "Federal Decree-Law No. 6 of 2025. With four months remaining, the licensing runway "
            "is compressed. If your platform touches open finance data, virtual asset payment "
            "flows, or tokenised instruments in the UAE, engage UAE regulatory counsel immediately "
            "to assess whether you are in scope. The CBUAE has signalled enforcement intent — "
            "a proactive licensing application is materially better than a post-deadline response."
        ),
        (
            "3.  Build multi-rail orchestration into your core product roadmap — 80+ live RTP schemes make it non-negotiable.",
            "The global RTP landscape now spans 80+ schemes. No PSP operating across geographies "
            "can rely on a single rail strategy. Intelligent payment routing — selecting the optimal "
            "rail by corridor, cost, speed, and compliance — is the foundational capability that "
            "differentiates platform-grade PSPs from single-rail operators. For product leaders, "
            "this is not a future enhancement: it is a current product gap that compounds with "
            "every new RTP scheme or cross-border linkage that goes live."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5: WATCHLIST ────────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  UK APP Fraud Independent Review Report — due Q2 2026.",
            "The PSR's independent review of the APP fraud Reimbursement Requirement is due imminently. "
            "The report may recalibrate the £415,000 cap, the 50/50 cost-sharing model, or consumer "
            "eligibility criteria — all with immediate P&amp;L implications for UK payment institutions. "
            "Watch for the report and any accompanying FCA/PSR enforcement guidance, as it will set "
            "the UK fraud compliance tone for the rest of 2026."
        ),
        (
            "●  CBUAE September 2026 compliance deadline — enforcement risk is rising.",
            "With newly in-scope entities required to regularise under UAE Federal Decree-Law No. 6 "
            "of 2025 by September 16, 2026, watch for CBUAE to begin publishing a list of licensed "
            "entities and, subsequently, enforcement actions against non-compliant operators. The "
            "CBUAE's track record on enforcement has been increasingly assertive — do not assume "
            "a grace period beyond the stated deadline."
        ),
        (
            "●  SWIFT MT101 and E&amp;I messaging deadlines — November 14, 2026.",
            "Multi-instruction MT101 messages will be rejected from November 14, 2026, and all "
            "institutions must be able to receive E&amp;I messages in MX format from the same date. "
            "Watch for correspondent banks and corporates to begin formal readiness confirmations "
            "and for SWIFT to publish any updated guidance or remediation tooling for institutions "
            "that have not yet completed migration across their correspondent networks."
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
        "SWIFT (swift.com), CBUAE (centralbank.ae), PSR / FCA (psr.org.uk, fca.org.uk), "
        "MAS (mas.gov.sg), Federal Reserve (federalreserve.gov), BIS (bis.org), European Commission, "
        "PYMNTS, Payment Expert, Finance Magnates, Red Compass Labs, Fintech Futures, Fintech Global, "
        "The Paypers, Norton Rose Fulbright, LSEG Risk Intelligence.",
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
