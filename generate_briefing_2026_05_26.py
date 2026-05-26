#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF — May 26 2026."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak,
)
from reportlab.lib.colors import HexColor

DATE   = "May 26, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-26.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B45309")
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
        colWidths=[170*mm],
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
        colWidths=[170*mm],
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    novelty_color = GREEN if "New" in novelty else (AMBER if "Escalation" in novelty else HexColor("#1A6B9A"))
    tag_p = Paragraph(
        f"<font color='white'><b> {tag} </b></font>",
        ParagraphStyle("tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE,
                       backColor=NAVY, leading=11, borderPadding=3),
    )
    nov_p = Paragraph(
        f"<font color='white'><b> {novelty} </b></font>",
        ParagraphStyle("nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE,
                       backColor=novelty_color, leading=11, borderPadding=3),
    )
    reg_p  = Paragraph(f"<b>Region:</b> {region}",  ParagraphStyle("reg",  fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_p = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle("play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_p, nov_p, "", ""],
         [reg_p, "",   play_p, ""]],
        colWidths=[42*mm, 46*mm, 8*mm, 74*mm],
    )
    tbl.setStyle(TableStyle([
        ("SPAN",          (2, 1), (3, 1)),
        ("SPAN",          (2, 0), (3, 0)),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return tbl


def blt(items, s):
    return [Paragraph(f"• &nbsp; {item}", s["bullet"]) for item in items]


def build_story(s):
    story = []

    # ── Cover ──────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── Section 1: Top Payments Headlines ─────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "SWIFT Retail Cross-Border Framework Targets June Go-Live Across Five of the Ten Largest Remittance Markets",
            "what": (
                "SWIFT has confirmed that more than 25 banks are on track to process live "
                "retail cross-border payments under its new consumer framework by end of June 2026, "
                "covering corridors to Australia, Bangladesh, Canada, China, Germany, India, Pakistan, "
                "Spain, Thailand, the UK, and the US. The framework mandates certainty of cost, "
                "full-value delivery, end-to-end traceability, and instant settlement where "
                "infrastructure permits. Separately, SWIFT is building a blockchain-based shared "
                "ledger to enable 24/7 real-time cross-border settlement across its 11,500-institution "
                "network — a meaningful infrastructure extension beyond its core messaging role."
            ),
            "why": [
                "SWIFT is repositioning from a pure messaging network to a settlement and "
                "orchestration layer for cross-border retail flows — a direct competitive response "
                "to Wise, Ripple, stablecoin corridors, and bilateral RTP linkages.",
                "The five remittance-market corridors covered include India, Bangladesh, and Pakistan — "
                "corridors where fintech disruptors have historically outpaced banks on cost and speed.",
                "The blockchain-shared-ledger addition is architecturally significant: it signals SWIFT's "
                "intent to run parallel rail infrastructure rather than cede 24/7 real-time settlement "
                "to non-bank players.",
                "For transaction banking product heads: bank participation in this framework creates "
                "a defensible retail cross-border value proposition without surrendering the SWIFT "
                "correspondent relationship infrastructure.",
            ],
            "region": "Global",
            "players": "SWIFT, 25+ global banks across AU, BD, CA, CN, DE, IN, PK, ES, TH, UK, US",
            "tag": "Cross-Border / Infrastructure",
            "novelty": "Escalation — June go-live imminent",
        },
        {
            "num": "2.",
            "headline": "EU PSD3 / PSR Heads to Parliament Plenary Vote — Verification of Payee, Fraud Liability, and Open Banking Overhaul Near-Final",
            "what": (
                "Following COREPER's endorsement of the trilogue agreement on April 22, 2026, the "
                "European Parliament's ECON Committee voted on May 5, with a plenary vote expected "
                "before end of May. Official Journal publication is anticipated in June or July 2026, "
                "triggering a 21-month implementation clock. PSD3 governs authorisation, governance, "
                "and capital for payment institutions; the companion Payment Services Regulation (PSR) "
                "introduces EU-wide Verification of Payee, mandatory PSP liability for impersonation "
                "fraud where controls are absent, and considerably stronger enforcement of open banking "
                "API obligations — including the right of national regulators to penalise banks that "
                "fail to meet API quality standards."
            ),
            "why": [
                "EU-wide Verification of Payee is the most structurally significant consumer protection "
                "shift since PSD2 — extending what the UK's CoP scheme proved to the full eurozone.",
                "PSP fraud liability provisions shift the risk calculus: institutions without adequate "
                "controls will bear losses from impersonation fraud, directly incentivising investment "
                "in real-time name-matching and transaction monitoring.",
                "The enforceable API quality regime fundamentally changes the open banking dynamic — "
                "banks can no longer provide sub-standard access without regulatory consequence.",
                "21-month implementation clock post-publication means firms need to begin gap assessments "
                "against final PSR conduct rules now, not after Official Journal publication.",
            ],
            "region": "Europe / EU",
            "players": "European Parliament, European Commission, EBA, EU payment institutions, open banking TPPs, PSPs",
            "tag": "Regulation / Open Finance",
            "novelty": "Escalation — plenary vote imminent",
        },
        {
            "num": "3.",
            "headline": "UAE Digital Dirham (Retail CBDC) Live Since March — GCC Corridor Integration With Saudi Arabia, India, and China Active",
            "what": (
                "The UAE Central Bank's Digital Dirham launched for retail transactions in March 2026, "
                "making the UAE one of the first countries globally to deploy a fully operational "
                "retail CBDC. The Digital Dirham enables instant peer-to-peer payments and cross-border "
                "transfers with Saudi Arabia, India, and China via integration with UAE Pass and major "
                "banking applications. All UAE-licensed financial institutions are mandated to integrate "
                "by end of 2026. The retail launch complements the existing wholesale Digital Dirham "
                "already settled through mBridge for institutional cross-border flows."
            ),
            "why": [
                "The UAE now operates a dual CBDC stack — retail (Digital Dirham) and wholesale "
                "(via mBridge) — the most integrated central bank digital infrastructure in the GCC.",
                "Cross-border capability with Saudi Arabia and India directly targets the highest-volume "
                "remittance corridors from the UAE, putting direct pressure on exchange houses and "
                "traditional remittance operators.",
                "Mandatory bank integration creates a universal acceptance floor — unlike voluntary "
                "wallet schemes, the Digital Dirham will be embedded in standard banking UX by end-2026.",
                "The UAE is now the most concrete real-world test case for retail CBDC at corridor scale — "
                "key reading for MAS, RBI, and other central banks managing related programs.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, UAE licensed banks, exchange houses, fintech firms, SAMA (Saudi Arabia), RBI (India), PBoC (China)",
            "tag": "Infrastructure / Cross-Border",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "4.",
            "headline": "mBridge Tops $55B in Cross-Border CBDC Settlements; BRICS 2026 Summit to Advance Multi-CBDC Interoperability",
            "what": (
                "Project mBridge, the multi-CBDC platform for China, Hong Kong, Thailand, UAE, and "
                "Saudi Arabia, has now settled over 4,000 cross-border transactions totalling "
                "approximately $55.5 billion since reaching minimum viable product stage — with "
                "China's digital yuan accounting for an estimated 95% of volume. At the BRICS "
                "May 2026 ministerial meeting, member states reaffirmed commitment to advancing "
                "BRICS Pay as a platform linking national instant payment systems and CBDCs. "
                "India separately proposed linking BRICS-nation CBDCs, with the framework tabled "
                "for the 2026 BRICS Summit hosted by India."
            ),
            "why": [
                "mBridge moving through $55B at MVP stage signals genuine transactional utility — "
                "this is no longer a pilot; it is a functioning alternative settlement rail for "
                "participating central banks.",
                "BRICS Pay + CBDC interoperability would constitute a parallel global payment "
                "infrastructure covering a significant share of global trade flows outside USD-denominated "
                "correspondent banking.",
                "The UAE's participation in both mBridge and the BRICS Pay initiative places it "
                "uniquely at the intersection of the two most active alternative payment infrastructure "
                "projects globally.",
                "India's proposal, combined with its historically cautious position on de-dollarisation, "
                "suggests pragmatic positioning — CBDC interoperability framed as efficiency rather "
                "than geopolitical alignment.",
            ],
            "region": "Global / GCC / BRICS",
            "players": "CBUAE, PBoC, HKMA, Bank of Thailand, Saudi Central Bank, Reserve Bank of India, BIS",
            "tag": "Cross-Border / Market Structure / Stablecoins",
            "novelty": "Escalation — $55B milestone, BRICS May reaffirmation",
        },
        {
            "num": "5.",
            "headline": "Data Interoperability Is the New Cross-Border Bottleneck — Structured Address Deadline Closes In",
            "what": (
                "A convergence of market and regulatory signals confirms that data quality — not rail "
                "speed — is now the primary friction point in cross-border payments. SWIFT's November "
                "2026 deadline for fully structured postal address fields in all cross-border "
                "payment instructions is approaching, with free-text entries to be rejected outright. "
                "Industry analysis from PYMNTS and Atlantic Council cites data governance fragmentation, "
                "divergent AML/KYC data standards, and jurisdictional data-localisation rules as the "
                "main operational drag on corridor performance — even where RTP rails exist end-to-end."
            ),
            "why": [
                "SWIFT's hard address rejection from November 2026 creates a systemic STP failure "
                "risk for any institution still relying on legacy free-text address fields — "
                "payment rejections will cascade into client experience and fee exposure.",
                "The 'data border' problem is structural: even fully interoperable rails cannot deliver "
                "on speed and cost promises if data standards, screening rules, and KYC signals "
                "cannot travel with the payment message.",
                "For compliance teams, structured ISO 20022 data directly improves sanctions screening "
                "precision and reduces AML false positives — the compliance ROI case for data "
                "remediation is now clear.",
                "Product leaders building on cross-border corridors must treat data enrichment "
                "and structured address hygiene as core platform features, not remediation tasks.",
            ],
            "region": "Global",
            "players": "SWIFT, global correspondent banks, corporate treasuries, RegTech vendors, AML screening providers",
            "tag": "Infrastructure / Fraud-Risk",
            "novelty": "Escalation — November 2026 hard deadline approaching",
        },
    ]

    for h in headlines:
        block = []
        block.append(Paragraph(f"{h['num']}  {h['headline']}", s["headline"]))
        block.append(Paragraph("What happened:", s["sub_lbl"]))
        block.append(Paragraph(h["what"], s["body"]))
        block.append(Paragraph("Why it matters:", s["sub_lbl"]))
        block.extend(blt(h["why"], s))
        block.append(Spacer(1, 2*mm))
        block.append(tag_row(h["tag"], h["novelty"], h["region"], h["players"], s))
        block.append(Spacer(1, 3*mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── Section 2: Fintech Headlines ───────────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Fasset Raises $51M to Scale Stablecoin-Powered SMB Cross-Border Payments Across 50+ Corridors",
            "what": (
                "Los Angeles-based Fasset closed a $51 million funding round led by Japan's SBI Group, "
                "with participation from Investcorp and Turkey's Arz Portföy. Fasset operates a "
                "stablecoin-powered payment and banking infrastructure processing over $32 billion "
                "in annualised volume for more than 1,000 SMBs across 125 countries on 50+ corridors "
                "spanning Asia, Africa, and the Middle East. The capital will be deployed toward "
                "new market expansion, SMB lending and trade finance products, and development of "
                "'Own Network' — its proprietary stablecoin payment and custody infrastructure."
            ),
            "why": (
                "Fasset's funding and volume metrics validate the stablecoin-for-B2B-payments thesis "
                "at meaningful scale. The SMB cross-border segment — high friction, high cost, "
                "underserved by traditional banks — is precisely where stablecoin rails offer the "
                "clearest unit economics advantage over correspondent banking. SBI Group's lead "
                "position signals Japanese institutional capital is backing stablecoin payment "
                "infrastructure in emerging market corridors as a long-term strategic play."
            ),
            "strategic": (
                "Stablecoin B2B payment infrastructure is attracting institutional capital at scale — "
                "this positions corridor-by-corridor displacement of correspondent banking for SMB "
                "flows as a near-term reality, not a future scenario."
            ),
        },
        {
            "num": "2.",
            "headline": "Bunq Applies for Mexican Banking Licence — European Neobank Global Expansion Via Banking Licence Strategy Continues",
            "what": (
                "Dutch neobank Bunq has submitted a banking licence application to Mexico's CNBV "
                "in coordination with Banco de México. If approved, Bunq would offer full-service "
                "banking in Mexico including multi-currency accounts and deposit protection. "
                "Bunq already holds banking licences in the EU and has been expanding its licensing "
                "footprint globally as its primary market-entry mechanism, differentiating itself "
                "from fintechs that enter via partnerships or limited e-money authorisations."
            ),
            "why": (
                "The banking-licence-first expansion strategy is significant: it signals that "
                "scaling neobanks are now opting for full regulatory standing in new markets rather "
                "than the faster but shallower BaaS/e-money route. Mexico is a high-stakes market — "
                "one of the world's top remittance destinations — and a banking licence there "
                "positions Bunq to compete across retail banking and remittance corridors "
                "simultaneously."
            ),
            "strategic": (
                "Full banking licences — not e-money or BaaS partnerships — are becoming the "
                "preferred expansion mechanism for scaling neobanks seeking durable product scope "
                "and regulatory parity with incumbents."
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

    # ── Section 3: What Matters Most ───────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  SWIFT is repositioning from messaging to settlement — and the retail cross-border "
            "market is the battleground.",
            "The June 2026 retail framework go-live, combined with SWIFT's blockchain-ledger "
            "infrastructure investment, signals a fundamental strategic pivot: SWIFT is not "
            "just modernising its messaging standard (ISO 20022), it is building settlement "
            "and orchestration capability to compete with fintech cross-border rails. For "
            "banks, this is an opportunity to defend retail cross-border relevance. For "
            "fintech players, it narrows the window in which speed and cost advantages are "
            "structurally unchallenged.",
        ),
        (
            "▶  The GCC is now the world's most active live laboratory for multi-layer CBDC infrastructure.",
            "The UAE's retail Digital Dirham, its wholesale mBridge participation, and the "
            "emerging BRICS Pay interoperability agenda collectively make the GCC — and "
            "specifically the UAE — the most advanced real-world deployment of CBDC-based "
            "payment infrastructure at corridor scale. This is not speculative: the UAE now "
            "has functioning retail and wholesale CBDC with active cross-border capability "
            "to Saudi Arabia, India, and China. Regional banks and PSPs operating in these "
            "corridors face a near-term shift in the operating model for remittance and "
            "institutional settlement flows.",
        ),
        (
            "▶  Regulation is simultaneously tightening on fraud liability, data quality, and "
            "digital asset perimeters — and the timelines are converging in 2026.",
            "PSD3/PSR's fraud liability shift, SWIFT's structured address rejection from "
            "November 2026, and the CBUAE's September 2026 licensing deadline for newly "
            "in-scope entities are not isolated events — they form a synchronized global "
            "regulatory tightening cycle. Firms operating across Europe, UAE, and on SWIFT "
            "rails simultaneously face compressing compliance windows. This rewards those "
            "with unified data, risk, and regulatory infrastructure — and penalises fragmented "
            "point-solution compliance stacks.",
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── Section 4: Implications for Product Leaders ────────────────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Map your corridor exposure against the SWIFT retail framework June go-live.",
            "The corridors going live in June — India, Bangladesh, Pakistan, UK, US, Australia, "
            "China, Germany, Spain, Thailand, Canada — cover the majority of the world's highest-volume "
            "consumer and SMB remittance flows. If your platform touches any of these corridors, "
            "the competitive pressure timeline is now measured in weeks, not quarters. Identify "
            "which committed banks are your counterparties and assess whether your pricing and "
            "speed commitments remain differentiated under the new framework guarantees.",
        ),
        (
            "2.  Start PSD3/PSR gap assessment now — do not wait for Official Journal publication.",
            "The plenary vote is imminent and the framework texts are published. The 21-month "
            "implementation clock starts on Official Journal publication (expected June/July 2026), "
            "giving you until approximately March or April 2028 to comply. That timeline will "
            "compress fast. Priority gaps to assess: EU Verification of Payee integration, "
            "open banking API quality standards versus your current TPP access implementation, "
            "and fraud reimbursement liability exposure under impersonation fraud scenarios.",
        ),
        (
            "3.  Treat the GCC CBDC corridor as a near-term operating environment, not a future scenario.",
            "The UAE's retail Digital Dirham is live. mBridge is processing billions. BRICS Pay "
            "interoperability is on the 2026 Summit agenda. PSPs and banks handling UAE-India, "
            "UAE-Saudi, or UAE-China flows should be running scenario planning now: what does "
            "your cost structure, compliance framework, and client proposition look like when "
            "the payer's bank offers CBDC settlement at near-zero cost and instant finality? "
            "First-mover banks that integrate the Digital Dirham early will capture the "
            "adoption curve in the world's largest remittance sending hub.",
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── Section 5: Watchlist ───────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  BRICS Summit 2026 (India) — CBDC and BRICS Pay interoperability framework announcement.",
            "India chairs the 2026 BRICS Summit and has tabled a proposal to link member-nation "
            "CBDCs. The outcome will determine whether mBridge and BRICS Pay converge into a "
            "unified alternative settlement infrastructure covering China, India, UAE, Saudi Arabia, "
            "Russia, Brazil, and South Africa — collectively representing a substantial share of "
            "global trade volume. Any formal interoperability framework agreed here would be the "
            "most significant development in alternative global payment infrastructure since SWIFT's "
            "post-2022 geopolitical moment.",
        ),
        (
            "●  SWIFT blockchain shared ledger — technical specification and bank participation announcement.",
            "SWIFT has signalled it is building blockchain-based shared ledger infrastructure "
            "for 24/7 real-time cross-border settlement. The technical specification, governance "
            "model, and which banks are in the initial cohort have not yet been published. "
            "This could redefine whether SWIFT becomes a settlement network (not just a messaging "
            "standard) — watch for the architecture announcement and early-adopter bank list.",
        ),
        (
            "●  EU PSD3/PSR Official Journal publication — triggering 21-month implementation clock.",
            "Expected June/July 2026. Publication starts the compliance clock for all EU-regulated "
            "payment institutions. Watch for EBA technical standards mandates that will follow "
            "within 12 months of publication — particularly on open banking API performance "
            "standards and Verification of Payee technical requirements. These standards will "
            "define implementation scope more precisely than the directive texts alone.",
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
        "regulatory releases, scheme operator announcements, and reputable financial and industry media. "
        "It is intended for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources for this edition: SWIFT (swift.com), European Parliament / "
        "European Commission, CBUAE (centralbank.ae), BIS (bis.org), MAS (mas.gov.sg), "
        "Atlantic Council, PYMNTS, American Banker, Ledger Insights, Fintech Futures, CoinDesk, "
        "Norton Rose Fulbright, Morrison Foerster. Sources accessed May 26, 2026.",
        s["footer_note"],
    ))

    return story


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MGRAY)
    canvas.drawCentredString(
        A4[0] / 2, 12*mm,
        f"Daily Payments & Fintech Intelligence Brief  |  {DATE}  |  Page {doc.page}",
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
        subject="Daily global payments and fintech briefing",
    )
    s = build_styles()
    story = build_story(s)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF created: {OUTPUT}")


if __name__ == "__main__":
    main()
