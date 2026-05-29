#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 29, 2026."""

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

DATE   = "May 29, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-29.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B05800")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
    base = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle("cover_title", fontSize=26, textColor=WHITE,
                                      fontName="Helvetica-Bold", alignment=TA_CENTER, leading=32),
        "cover_sub":   ParagraphStyle("cover_sub", fontSize=14, textColor=HexColor("#B4D2FF"),
                                      fontName="Helvetica", alignment=TA_CENTER, leading=20),
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
         [Spacer(1, 6 * mm)]],
        colWidths=[170 * mm]
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
        colWidths=[170 * mm]
    )
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    novelty_color = AMBER if "Escalation" in novelty else GREEN
    tag_para = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=novelty_color,
        leading=11, borderPadding=3))
    reg_para = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
        "play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "", play_para, ""]],
        colWidths=[42 * mm, 48 * mm, 8 * mm, 72 * mm]
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
    story.append(Spacer(1, 8 * mm))

    # ── SECTION 1: Top Payments Headlines ─────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3 * mm))

    headlines = [
        {
            "num": "1.",
            "headline": "SWIFT Retail Cross-Border Framework: 25+ Banks Targeting June 2026 Go-Live",
            "what": (
                "SWIFT and a coalition of global banks are rolling out a new payments framework "
                "for retail and SME cross-border transactions, originally announced in Brussels on "
                "March 5, 2026. More than 25 banks have committed to processing live payments under "
                "the framework by June 2026, with corridors spanning Australia, Bangladesh, Canada, "
                "China, Germany, India, Pakistan, Spain, Thailand, the UK, and the US. Over 50 banks "
                "have signed up in total, with further market activations targeted by year-end. "
                "The framework guarantees cost certainty, full-value delivery, end-to-end traceability, "
                "and the fastest possible speed — including instant settlement where local infrastructure "
                "permits. Early participants include Bank of America, BNP Paribas, Citi, Deutsche Bank, "
                "JPMorgan Chase, and Standard Chartered."
            ),
            "why": [
                "This is SWIFT's most direct structural response to competitive pressure from Visa Direct, Mastercard Move, Wise, and stablecoin payment rails — it reframes SWIFT as a guarantor of consumer-facing payment experience, not just an interbank messaging network.",
                "The June live-date concentrates urgency: banks in the listed corridors must now operationalize the framework or fall behind on transparency commitments to end customers.",
                "Cost-certainty and full-value delivery guarantees introduce new SLA obligations for correspondent chains — potentially restructuring how nostro/vostro fee models are disclosed and absorbed.",
                "If early volume is meaningful, this framework becomes the de facto benchmark against which faster payment challengers are judged on price, speed, and traceability for the $150T+ consumer cross-border market.",
            ],
            "region": "Global",
            "players": "SWIFT, BofA, BNP Paribas, Citi, Deutsche Bank, JPMorgan, Standard Chartered, 40+ regional banks",
            "tag": "Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "2.",
            "headline": "EU PSD3 / PSR Heading to Parliament Plenary — Official Journal Publication Imminent",
            "what": (
                "The Third Payment Services Directive (PSD3) and its accompanying, directly applicable "
                "Payment Services Regulation (PSR) cleared the Council 'I' Item approval on April 22, "
                "2026, with agreed texts published April 23. The ECON Committee voted on May 5, 2026. "
                "A Parliament plenary vote is expected in May, with Official Journal publication "
                "targeted for end of Q2 or early Q3 2026. The PSR — directly applicable across all "
                "27 EU member states without national transposition — takes effect 21 months after "
                "publication (approximately late 2027). Key reforms include mandatory payee IBAN name "
                "verification (Confirmation of Payee equivalent), APP fraud liability allocation, "
                "enhanced open banking API standards, and strengthened non-bank PSP access to payment accounts."
            ),
            "why": [
                "The directly applicable PSR eliminates 27-nation transposition variation — product architecture decisions made now must target a single harmonised standard, not 27 local interpretations.",
                "Payee IBAN name verification (CoP) becomes a legal requirement: banks and PSPs that have not yet built proxy lookup infrastructure must accelerate implementation.",
                "APP fraud liability shifts create direct P&L exposure — PSPs that fail to deploy compliant fraud warnings face mandatory reimbursement obligations to customers.",
                "Open banking API mandates will increase A2A payment competitiveness, raising existential pressure on card-based payment volumes in high-RTP-penetration markets.",
            ],
            "region": "Europe",
            "players": "European Parliament, Council of EU, EBA, national regulators, all EU-licensed PSPs",
            "tag": "Regulation / Open Finance",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "SEPA Instant Fraud Surging 175% vs 98% Volume Growth — Compliance Architecture Under Strain",
            "what": (
                "Following mandatory SEPA Instant Payments activation across the EU (October 2025), "
                "fraudulent instant credit transfer transactions have grown approximately 175% — nearly "
                "double the ~98% growth rate in overall instant payment volume. European APP fraud "
                "losses are now estimated at up to €2.4 billion annually and growing 20–25% per year. "
                "Banks are required to complete full AML, sanctions screening, and fraud detection "
                "within a 10-second processing window — a requirement that fundamentally breaks legacy "
                "batch-oriented compliance architectures. Regulators are simultaneously calling for "
                "lower SAR thresholds for instant payment transactions."
            ),
            "why": [
                "The 10-second AML and fraud window is not a marginal constraint — it forces a complete architectural shift from batch-based to real-time, event-driven compliance stacks.",
                "APP fraud growth at 20–25% annually means the €2.4B loss figure will compound rapidly; institutions lacking real-time behavioural analytics are exposed to both financial loss and regulatory liability.",
                "PSD3/PSR payee verification requirements (arriving 2027) will help at the point of initiation, but institutions need interim controls now to reduce losses in the intervening period.",
                "This creates near-term commercial opportunity for real-time fraud, AML, and sanctions screening vendors — AI-native compliance infrastructure providers will gain market share over legacy batch vendors.",
            ],
            "region": "Europe",
            "players": "EU banks, EBA, national competent authorities, real-time fraud/AML vendors, TCH, EBA Clearing",
            "tag": "Fraud-Risk / RTP",
            "novelty": "Escalation / broader impact today",
        },
        {
            "num": "4.",
            "headline": "UAE CBUAE Compliance Deadline at 16 Weeks — Tech Providers and Open Finance Now In-Scope",
            "what": (
                "Federal Decree-Law No. 6 of 2025 (CBUAE Law), enacted September 2025, brought a "
                "significantly expanded set of financial services activities within CBUAE's licensing "
                "perimeter — including payment services using virtual assets, decentralised protocols, "
                "digital platforms that intermediate payment services, open finance providers, and "
                "technology infrastructure operators that enable licensed financial activities. "
                "The September 16, 2026 compliance deadline — approximately 16 weeks away — applies "
                "to all newly in-scope entities. Non-compliance carries fines between AED 50,000 and "
                "AED 500 million, plus potential imprisonment. The CBUAE issued revised AML/CFT/CPF "
                "guidance in April 2026, signaling a shift toward continuous, technology-enabled risk monitoring."
            ),
            "why": [
                "For the first time, CBUAE explicitly brings payment technology infrastructure providers — including API middleware, blockchain settlement layers, and DeFi protocols — within UAE banking supervision.",
                "Open finance platforms operating in the UAE must now obtain a CBUAE licence or restructure their business models before mid-September 2026 — a compressed 16-week runway.",
                "The AED 500M fine ceiling makes non-compliance a systemic financial risk, not just a regulatory inconvenience, for large international payment infrastructure firms with UAE exposure.",
                "The GCC's leading financial hub is now one of the most comprehensive payment regulatory jurisdictions globally — raising both the compliance cost and the credibility signal for operating in the UAE market.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, open finance platforms, virtual asset payment providers, payment middleware firms, RegTech vendors",
            "tag": "Regulation / Market Structure",
            "novelty": "Escalation / deadline at 16 weeks",
        },
        {
            "num": "5.",
            "headline": "ISO 20022 Inflection: 2026 Marks the End of Coexistence — Data Quality Now a Cost Variable",
            "what": (
                "2026 is widely identified as the structural inflection point for ISO 20022, when "
                "end-to-end structured data can deliver consistent operational outcomes across the "
                "majority of payment corridors. SWIFT's January 2026 pricing penalties for institutions "
                "still relying on in-flow MT translation or contingency MT processing are now active. "
                "SEPA version 3.7 — with updated pain.001.001.09 credit transfer formats — is mandatory. "
                "A hard deadline for fully structured postal address fields applies from November 2026. "
                "Near 95% of financial services firms are either modernising payment infrastructure "
                "or planning to, with AML and real-time fraud monitoring as the primary drivers."
            ),
            "why": [
                "SWIFT pricing penalties convert ISO 20022 compliance from a strategic aspiration to an active cost variable — institutions are now paying for non-compliance every month.",
                "Structured remittance and party data is enabling automation, reducing repair rates, and allowing faster investigations — banks investing in native ISO 20022 processing are beginning to see measurable STP improvements.",
                "The November 2026 structured address hard deadline requires active client data remediation programs; corporate payment factories and ERP integrations need format-level updates now.",
                "Structured data quality is becoming a fraud and sanctions screening competitive advantage: richer address and party data reduces false positive rates and improves genuine hit detection.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, SEPA payment operators, corporate treasuries, TMS/ERP vendors, correspondent banks",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — pricing penalties active, Nov 2026 deadline approaching",
        },
    ]

    for h in headlines:
        block = []
        block.append(Paragraph(f"{h['num']}  {h['headline']}", s["headline"]))
        block.append(Paragraph("What happened:", s["sub_lbl"]))
        block.append(Paragraph(h["what"], s["body"]))
        block.append(Paragraph("Why it matters:", s["sub_lbl"]))
        block.extend(bullets(h["why"], s))
        block.append(Spacer(1, 2 * mm))
        block.append(tag_row(h["tag"], h["novelty"], h["region"], h["players"], s))
        block.append(Spacer(1, 3 * mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3 * mm))
        story.append(KeepTogether(block))

    # ── SECTION 2: Major Fintech Headlines ────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3 * mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Mastercard Acquires BVNK for Up to $1.8B — Stablecoin Infrastructure Enters Scheme Layer",
            "what": (
                "Announced March 2026 and currently pending regulatory approval (expected late 2026), "
                "Mastercard is acquiring BVNK — a UK-headquartered stablecoin infrastructure provider "
                "operating across 130+ countries — for $1.5B plus $300M in contingent payments. "
                "BVNK enables enterprise clients to send and receive payments via stablecoins on all "
                "major blockchain networks, with fiat on/off-ramp connectivity. The acquisition is "
                "designed to make on-chain payment settlement natively accessible within the "
                "Mastercard network, creating interoperability between fiat rails and blockchain settlement."
            ),
            "why": (
                "This is the largest-ever card scheme acquisition of stablecoin infrastructure and "
                "a structural signal that Mastercard views on-chain/fiat interoperability as a core "
                "capability layer — not a fringe product. If integrated effectively, BVNK gives "
                "Mastercard a real-time stablecoin settlement option accessible via its existing "
                "merchant and bank relationships, without merchants needing separate crypto infrastructure. "
                "Visa, Stripe, and PayPal will face heightened competitive pressure to match this "
                "stablecoin capability at scheme scale."
            ),
            "strategic": "Stablecoin settlement is moving from fintech experimentation to card-scheme infrastructure — product teams must model what this means for their cross-border economics within 18–24 months.",
        },
        {
            "num": "2.",
            "headline": "MAS Advances Tokenized Bills Trial and BLOOM Initiative — Digital Money Becomes Operational",
            "what": (
                "MAS has confirmed a 2026 live trial of tokenized MAS bills settled in wholesale "
                "central bank digital currency (wCBDC), with primary dealers issuing and settling "
                "via blockchain-based tokens. The BLOOM initiative (Borderless, Liquid, Open, "
                "Online, Multi-currency), launched October 2025, is advancing trials with tokenized "
                "bank liabilities and regulated stablecoins for wholesale settlement across Singapore's "
                "financial ecosystem. Project Guardian — MAS's institutional tokenization framework — "
                "has been expanded for cross-border applications, including Les Gardiennes with Banque "
                "de France, UBS, and Societe Generale, testing tokenized repo transactions using "
                "tokenized assets and digital money across jurisdictions."
            ),
            "why": (
                "Singapore is moving from tokenization pilots to institutional-grade, wCBDC-settled "
                "infrastructure in a single year. The combination of tokenized government securities, "
                "wholesale CBDC settlement, and cross-border tokenized asset trials positions MAS as "
                "the most operationally advanced central bank in digital money infrastructure globally. "
                "This has direct implications for financial institutions in Singapore that must now "
                "develop capability to integrate tokenized assets and digital money into payment "
                "rails and treasury operations — not as a future-state consideration, but for 2026 trials."
            ),
            "strategic": "MAS is building the reference architecture for digital wholesale money — financial institutions in Singapore should treat 2026 as the year to develop real institutional capability, not just monitor developments.",
        },
        {
            "num": "3.",
            "headline": "UPI Global: Cross-Border Transactions Up 20x — Regulatory Reckoning Ahead",
            "what": (
                "UPI cross-border transaction volumes surged over 20 times from FY2024 to FY2025 "
                "(37,060 to 755,000+ transactions), with 601,000 processed in the first four months "
                "of FY2026 alone. UPI is now operational in eight countries (Bhutan, Singapore, Qatar, "
                "Mauritius, Nepal, UAE, Sri Lanka, France) and is being extended to East Asia (Japan, "
                "Malaysia). India has joined Project Nexus alongside MAS, Bank Negara Malaysia, BSP "
                "Philippines, and Bank of Thailand. Legal analysis published May 2026 identifies "
                "data localisation, settlement finality, and dispute resolution harmonisation as "
                "the primary constraints on UPI's further expansion beyond the Indian diaspora."
            ),
            "why": (
                "UPI's 20x transaction growth validates the demand for instant cross-border A2A payments — "
                "but the regulatory reckoning is arriving simultaneously with expansion. Each new market "
                "brings a fresh set of jurisdictional requirements on data residency, FX conversion, "
                "consumer protection, and AML that India's domestic regulatory model does not automatically "
                "satisfy. This tension between volume growth and regulatory friction is the defining "
                "strategic challenge for UPI's global ambitions and a lesson for all cross-border RTP "
                "expansion strategies."
            ),
            "strategic": "UPI's growth trajectory demonstrates real consumer demand for low-cost instant cross-border A2A — but the regulatory model for outbound expansion is still unresolved, creating both risk and opportunity for PSPs in target corridors.",
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
        block.append(Spacer(1, 3 * mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3 * mm))
        story.append(KeepTogether(block))

    # ── SECTION 3: What Matters Most ──────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3 * mm))

    themes = [
        (
            "▶  Scheme infrastructure is converging on the retail cross-border battlefield.",
            "SWIFT's retail framework, Mastercard's BVNK acquisition, and UPI's corridor expansion "
            "are all competing for the same consumer and SME cross-border payment flow. The next "
            "12 months will begin to reveal which infrastructure model — correspondent network reform, "
            "stablecoin rails, or bilateral/multilateral RTP linkages — captures the highest-growth "
            "corridors. The outcome is not zero-sum, but market positioning decisions made in H2 2026 "
            "will have durable strategic consequences."
        ),
        (
            "▶  Compliance architecture has become the primary bottleneck for real-time payment scale.",
            "The SEPA Instant fraud surge (175%), CBUAE regulatory perimeter expansion, EU PSD3 "
            "payee verification mandates, and ISO 20022 pricing penalties all point to the same "
            "structural truth: infrastructure is running ahead of compliance architecture, and "
            "regulators are closing the gap. The banks and PSPs that invest now in real-time, "
            "event-driven compliance stacks — rather than patching batch systems — will carry "
            "structural operating leverage into the next infrastructure cycle."
        ),
        (
            "▶  Digital money is transitioning from pilot to operational infrastructure in 2026.",
            "MAS tokenized bills, Mastercard/BVNK, BLOOM, and Project Nexus together represent "
            "a decisive shift: tokenized assets and stablecoin settlement are no longer "
            "future-state concepts — they are being built into institutional-grade infrastructure "
            "with real counterparties, real settlement, and real regulatory frameworks. Financial "
            "institutions that treat this as a 2028 problem are already behind."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3 * mm))

    # ── SECTION 4: Implications ────────────────────────────────────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3 * mm))

    implications = [
        (
            "1.  The SWIFT retail framework June go-live forces an immediate corridor product decision.",
            "Banks and PSPs in the eleven launch corridors (AU, BD, CA, CN, DE, IN, PK, ES, TH, UK, US) "
            "must decide now whether to adopt the framework and gain cost-certainty/traceability "
            "commitments — or hold back and risk consumer-facing transparency disadvantages against "
            "adopters. This is not a watch-and-wait situation: June is weeks away. Product leaders "
            "should be in active conversations with their correspondent relationships and payment "
            "operations teams about framework readiness."
        ),
        (
            "2.  EU PSD3 payee verification architecture must begin design now — not at transposition.",
            "With the PSR applying approximately 21 months after Official Journal publication (late "
            "2027), the design window is now. Payee IBAN name verification requires proxy lookup "
            "infrastructure, customer-facing warning UX, and liability-allocation logic that touches "
            "multiple product layers. Firms that start design in Q3 2026 will have meaningful "
            "optionality; those that wait for national guidance risk costly last-minute builds "
            "with compressed timelines."
        ),
        (
            "3.  Model the stablecoin settlement scenario before Mastercard/BVNK closes.",
            "The Mastercard/BVNK deal is expected to close late 2026. Once BVNK infrastructure is "
            "scheme-native, stablecoin settlement becomes accessible to any Mastercard-connected "
            "merchant or bank without requiring separate crypto infrastructure. Product leaders in "
            "cross-border payments should model now: what happens to FX margin economics, settlement "
            "timing advantages, and consumer UX for high-frequency/low-value flows when stablecoin "
            "settlement is available via existing scheme rails? The strategic response needs to be "
            "designed before the capability lands, not after."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2 * mm))
        story.append(KeepTogether(block))

    # ── SECTION 5: Watchlist ───────────────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3 * mm))

    watchlist = [
        (
            "●  SWIFT Retail Framework June Go-Live: Volume and Adoption Signal.",
            "The critical question is whether the June 2026 launch generates meaningful consumer "
            "payment volume across the committed corridors — or whether it remains an early-adopter "
            "demonstration. Volume data in Q3 will reveal whether SWIFT's retail corridor franchise "
            "can be meaningfully defended against fintech challengers. Watch for initial corridor "
            "metrics from Bank of America, Citi, and Standard Chartered, who are among the most "
            "globally exposed participants."
        ),
        (
            "●  MAS Stablecoin Legislation Draft — Singapore Setting the Regional Template.",
            "MAS has confirmed it is ready to begin drafting stablecoin legislation. When the "
            "consultation paper is published — likely H2 2026 — it will set the regulatory template "
            "other Asian markets may adopt or adapt. Combined with the PFMI-standard call for "
            "systemic stablecoins made at the IMF Spring Meetings, this will shape the institutional "
            "stablecoin landscape across Asia-Pacific for the next three to five years."
        ),
        (
            "●  UPI Regulatory Friction in Non-ASEAN Markets — Data Localisation and Dispute Resolution.",
            "As UPI pushes into Japan, Malaysia, and Central Asian markets, jurisdictional friction "
            "on data localisation, settlement finality, and consumer dispute resolution is becoming "
            "the binding constraint — not technology. Watch for NPCI International to publish updated "
            "expansion frameworks or bilateral regulatory agreements that may resolve these friction "
            "points and unlock the next phase of volume growth beyond the Indian diaspora."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2 * mm))
        story.append(KeepTogether(block))

    # ── Footer / Disclaimer ───────────────────────────────────────────────────
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, scheme announcements, and reputable financial media. It is intended for "
        "informational purposes only and does not constitute investment, legal, or regulatory advice. "
        "Key sources: SWIFT (swift.com), European Parliament, CBUAE (centralbank.ae), MAS (mas.gov.sg), "
        "BIS (bis.org), Mastercard (mastercard.com), PYMNTS, American Banker, The Paypers, "
        "Payment Expert, S&amp;P Global Market Intelligence, Norton Rose Fulbright, Morrison Foerster, "
        "Flagright, Fintech Global, India Corporate Law Blog, IBEF.",
        s["footer_note"]
    ))

    return story


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MGRAY)
    canvas.drawCentredString(
        A4[0] / 2, 12 * mm,
        f"Daily Payments & Fintech Intelligence Brief  |  {DATE}  |  Page {doc.page}"
    )
    canvas.setStrokeColor(SILVER)
    canvas.setLineWidth(0.3)
    canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)
    canvas.restoreState()


def main():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=20 * mm, rightMargin=20 * mm,
        topMargin=18 * mm,  bottomMargin=20 * mm,
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
