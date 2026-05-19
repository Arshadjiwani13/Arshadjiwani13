#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 19, 2026."""

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

DATE   = "May 19, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-19.pdf"

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
            "headline": "Singapore Incorporates SPaN — Unified Governance for All 8 National Payment Schemes",
            "what": (
                "The Monetary Authority of Singapore (MAS) and the Association of Banks in Singapore "
                "(ABS) have incorporated Singapore Payments Network (SPaN), a new not-for-profit "
                "company limited by guarantee, to govern and administer Singapore's eight national "
                "payment schemes: FAST, GIRO, PayNow, SGQR, and four others. Governance previously "
                "split across SCHA, ABS, MAS, and Infocomm is now consolidated under an 11-member "
                "board comprising MAS representatives, five financial institution directors, and "
                "independent industry members. SPaN is expected to be fully operational by end-2026, "
                "with a phased transition of all scheme administration responsibilities."
            ),
            "why": [
                "SPaN creates a single point of accountability for Singapore's payment scheme governance — "
                "removing structural fragmentation that has historically slowed coordinated scheme evolution.",
                "Scheme membership will expand beyond D-SIBs to include other direct participants of "
                "national payments infrastructure, broadening the governance base over time.",
                "This positions Singapore's domestic infrastructure for accelerated alignment with "
                "Project Nexus and future cross-border interoperability requirements under a unified "
                "governance entity rather than ad-hoc coordination.",
                "International PSPs and non-bank payment institutions operating in Singapore should "
                "monitor the SPaN membership expansion timeline — it may affect their scheme access "
                "rights, participation fees, and future scheme-rule consultation processes.",
            ],
            "region": "Singapore",
            "players": "MAS, ABS, DBS, OCBC, UOB, Citibank, HSBC, Maybank, Standard Chartered, PayNow ecosystem",
            "tag": "Infrastructure / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "CBUAE Launches Nationwide KYC Platform with Norbloc — Open Finance Infrastructure Deepens",
            "what": (
                "The Central Bank of the UAE announced a unified digital identity platform for "
                "Emirati financial institutions, fintechs, and individuals, signing a technical "
                "partnership with Sweden-based Norbloc to build the system. The platform is designed "
                "to create a shared, interoperable KYC data layer that reduces duplicate onboarding "
                "costs and accelerates digital financial access. This development follows CBUAE's "
                "Aani instant payments platform (now at 12.5 million users) and the Al Tareq open "
                "finance framework, which enables licensed third-party providers to securely access "
                "financial data — now approaching live implementation."
            ),
            "why": [
                "A shared KYC utility at the national level directly reduces onboarding friction for "
                "payments operators, fintechs, and banks — lowering the cost and time of customer "
                "acquisition across UAE's regulated financial sector.",
                "Combined with Al Tareq open finance, a national digital identity layer creates the "
                "infrastructure backbone for account aggregation, embedded finance, and A2A "
                "payment initiation — broadly analogous to what the UK Open Banking standard and "
                "India's AA framework enable.",
                "CBUAE's coordinated roll-out of Aani, Al Tareq, and now a national KYC platform "
                "reflects a deliberate infrastructure-first strategy that positions UAE as a leading "
                "GCC open finance hub rather than just a regulatory sandbox market.",
                "For international PSPs entering UAE, shared KYC lowers onboarding costs but also "
                "raises expectations for API-native, real-time identity integration — infrastructure "
                "investments become table stakes faster.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Norbloc, UAE banks, fintechs, Al Etihad Payments (Aani)",
            "tag": "Open Finance / Infrastructure / Regulation",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "MAS + Banks Launch Cross-Industry AI Scam Detection POV — 5-Bank Transaction Data Pooled",
            "what": (
                "MAS announced on May 4, 2026 that it is conducting a Proof-of-Value (POV) for "
                "pre-emptive AI/ML-based scam detection in collaboration with the Government "
                "Technology Agency of Singapore (GovTech) and the Singapore Police Force. The POV "
                "pools anonymised transaction data from five major Singaporean banks to train shared "
                "AI/ML models capable of identifying higher-risk transactions and accounts before "
                "fraud is consummated. Separately, MAS and the Association of Banks in Singapore "
                "(ABS) also launched a review of GIRO payment security — evaluating customer-set "
                "monthly deduction limits, enhanced transaction monitoring, and tightened due "
                "diligence standards for billing organisations."
            ),
            "why": [
                "Cross-bank data sharing for fraud detection is structurally distinct from "
                "single-bank fraud models — the network effect of pooled data significantly "
                "improves model precision, especially for mule account detection and cross-institution "
                "fraud rings.",
                "Pre-emptive scam detection (before payment execution) is the frontier of payment "
                "fraud risk management; reactive post-payment controls are increasingly inadequate "
                "against real-time payment fraud vectors.",
                "MAS's regulatory imprimatur for cross-bank data sharing in a POV context sets a "
                "precedent that may evolve into a shared fraud utility model — similar to the UK's "
                "Confirmation of Payee or the US RTP network's fraud intelligence-sharing frameworks.",
                "The GIRO security review signals regulatory attention to the pull payment model — "
                "PSPs and billing organisations should expect tighter due diligence and monitoring "
                "obligations for automated recurring debit schemes.",
            ],
            "region": "Singapore",
            "players": "MAS, GovTech, Singapore Police Force, DBS, OCBC, UOB and other D-SIBs, ABS",
            "tag": "Fraud-Risk / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "GENIUS Act Stablecoin AML/Sanctions NPRM — FinCEN and OFAC Issue Joint Proposed Rules",
            "what": (
                "On April 10, 2026, the US Department of the Treasury's Financial Crimes Enforcement "
                "Network (FinCEN) and Office of Foreign Assets Control (OFAC) jointly issued a Notice "
                "of Proposed Rulemaking (NPRM) to implement AML and sanctions compliance requirements "
                "for permitted payment stablecoin issuers under the GENIUS Act (enacted July 2025). "
                "The proposed rules require stablecoin issuers to establish full Bank Secrecy "
                "Act-compliant AML programs and OFAC sanctions screening frameworks. Public comments "
                "are due June 9, 2026. Separately, OCC proposed rulemaking for national bank "
                "stablecoin issuance closed comments on May 1, 2026."
            ),
            "why": [
                "The first-ever joint FinCEN-OFAC stablecoin NPRM is a structural milestone — "
                "stablecoin payment issuers are now treated as full BSA-regulated financial "
                "institutions with all associated AML programme and sanctions screening obligations.",
                "This closes a material regulatory arbitrage gap that non-bank stablecoin issuers "
                "previously exploited relative to banks and licensed money transmitters operating "
                "payment corridors.",
                "PSPs and banks building stablecoin payment overlays or settlement layers must now "
                "plan for full AML/CFT programme integration, transaction monitoring, and OFAC "
                "screening costs — significantly changing unit economics for stablecoin payment rails.",
                "The GENIUS Act + NPRM framework convergence positions the U.S. toward alignment "
                "with global stablecoin regulation trends (EU MiCA, Singapore MAS Payment Services "
                "Act, UAE VA regime) — creating a more predictable global operating environment "
                "for institutional stablecoin payment infrastructure.",
            ],
            "region": "United States / Global",
            "players": "FinCEN, OFAC, OCC, US Treasury, Circle, Coinbase, Paxos, bank stablecoin issuers",
            "tag": "Stablecoins / Regulation / Fraud-Risk",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "5.",
            "headline": "UK A2A/VRP Milestones Execute on 2026 Forward Plan — Open Banking Future Entity Selected",
            "what": (
                "HM Treasury's Payments Forward Plan (February 2026) is now delivering on its "
                "committed milestones. Q1 2026 saw the first live Commercial Variable Recurring "
                "Payments (VRP) under the UK Payments Initiative (UKPI) scheme go live. In April "
                "2026, an organisation was selected as the Future Entity — a central standards and "
                "governance body for UK Open Banking. Q4 2026 will introduce a new Data Use and "
                "Access Act Statutory Instrument. Despite strong infrastructure, A2A payments "
                "still account for only approximately 5% of UK e-commerce transactions, "
                "significantly below markets with comparable technical capabilities."
            ),
            "why": [
                "Live Commercial VRP represents a consent-first, programmable alternative to card-on-file "
                "and direct debit — eliminating silent churn, adding real-time consent transparency, "
                "and reducing card interchange costs for subscription and recurring payment merchants.",
                "The Future Entity's selection resolves a governance vacuum that has stalled UK Open "
                "Banking commercial rollout since the CMA's Open Banking Implementation Entity (OBIE) "
                "wind-down was announced — providing the standards certainty that PSP product investment "
                "decisions require.",
                "The 5% A2A e-commerce share versus infrastructure capability gap reveals that the "
                "binding constraint in UK A2A adoption is merchant integration and consumer "
                "payment-experience parity with cards — not the underlying technology.",
                "For cross-border PSPs serving UK merchants, VRP creates a new revenue-displacing "
                "payment method for subscriptions at lower interchange costs — a structural threat "
                "to card volume in high-frequency recurring billing segments.",
            ],
            "region": "United Kingdom",
            "players": "HM Treasury, PSR, FCA, Bank of England, UKPI, Future Entity, UK PSPs, merchants",
            "tag": "Open Finance / RTP / Regulation",
            "novelty": "Escalation — milestones executing",
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
            "headline": "Paymentology Secures $175M — Cloud-Native Issuer-Processing Scale Confirmed",
            "what": (
                "Paymentology, a cloud-native global issuer-processor operating across close to 70 "
                "countries, secured a $175 million investment co-led by Apis Partners and Aspirity "
                "Partners. The funding will support further geographic expansion and product "
                "development. Paymentology processes issuing transactions for banks, fintechs, and "
                "embedded finance providers across Africa, the Middle East, Asia, and Latin America — "
                "regions where legacy issuer-processing infrastructure is weakest and greenfield "
                "digital bank launch activity is highest."
            ),
            "why": (
                "A $175M round at this stage signals that global institutional capital continues "
                "to flow disproportionately into cloud-native issuer-processing infrastructure "
                "rather than consumer-facing fintech. Paymentology's multi-geography footprint "
                "across high-growth markets (MENA, Africa, LatAm) represents a structural "
                "alternative to legacy processors (FIS, Fiserv, Worldline) for challenger bank "
                "launches, embedded card programs, and cross-border acquiring infrastructure. "
                "This directly competes with incumbents' attempts to cloud-migrate their legacy "
                "stacks while retaining clients."
            ),
            "strategic": "Cloud-native issuer-processor infrastructure in high-growth markets is attracting large-scale institutional capital, confirming the infrastructure layer as the dominant fintech value-capture thesis for 2026.",
        },
        {
            "num": "2.",
            "headline": "Fasset Raises $51M — Stablecoin-Powered Cross-Border Payments Gains Institutional Backing",
            "what": (
                "Fasset, a Los Angeles-based stablecoin-powered neobank, raised $51 million led by "
                "Japan's SBI Group with participation from Investcorp and Turkey's Arz Portföy. "
                "Fasset processes over $32 billion in annualised payment volume, serving more than "
                "1,000 SMBs across 125 countries via 50+ payment corridors focused on Asia, Africa, "
                "and the Middle East. The platform uses stablecoins as the settlement layer for "
                "cross-border SME payments, bypassing correspondent banking infrastructure for "
                "corridors where traditional rails are slow, expensive, or unreliable."
            ),
            "why": (
                "SBI Group's lead participation is significant — it signals Japanese institutional "
                "capital entering stablecoin-powered cross-border payment infrastructure, not just "
                "crypto speculation. Fasset's corridor footprint (Asia, MENA, Africa) directly "
                "overlaps with Project Nexus's initial corridors and the UAE's GCC cross-border "
                "payment ambitions, creating potential future interoperability intersections. "
                "At $32B annualised volume, Fasset is approaching the scale threshold where it "
                "becomes regulatorily material — GENIUS Act AML obligations in the US and "
                "UAE/Singapore licensing requirements will define whether its growth trajectory "
                "is sustainable."
            ),
            "strategic": "Stablecoin cross-border payment platforms are scaling into institutional capital and real corridor volumes — the narrative is shifting from speculative infrastructure to regulated payment utility.",
        },
        {
            "num": "3.",
            "headline": "Project Nexus Appoints NETS-PayNet JV as Technical Operator — AWS and Endava to Build Platform",
            "what": (
                "Nexus Global Payments (NGP) formally appointed a joint venture between NETS "
                "(Singapore's Network for Electronic Transfers) and PayNet (Malaysia's Payments "
                "Network) as the Nexus Technical Operator (NTO) in February 2026. The NTO will "
                "work with Amazon Web Services as cloud infrastructure provider and Endava as "
                "technical development partner. Technical platform development is now underway, "
                "with go-live targeted for 2027 and the first connected corridors expected to "
                "include the FAST-DuitNow (Singapore-Malaysia), PromptPay (Thailand), UPI (India), "
                "and InstaPay (Philippines) linkages."
            ),
            "why": (
                "The NTO appointment converts Project Nexus from blueprint to active build — a "
                "material escalation of implementation risk and opportunity. The choice of NETS "
                "and PayNet (Singapore and Malaysia's national payment network operators) as "
                "the technical operator grounds Nexus in sovereign domestic infrastructure "
                "rather than commercial intermediary architecture. AWS as cloud partner signals "
                "the hyperscaler-as-critical-infrastructure model extending to multilateral "
                "central bank payment systems. PSPs in India, Malaysia, Philippines, Singapore, "
                "and Thailand should be in active Nexus integration planning now."
            ),
            "strategic": "Project Nexus is in active technical build with a sovereign-backed operator and hyperscaler infrastructure partner — the 2027 go-live window is now credible, not aspirational.",
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
            "▶  Payment infrastructure governance is consolidating around sovereign entities — not commercial incumbents.",
            "Singapore's SPaN, the UAE's Al Etihad Payments (Aani), and Project Nexus's sovereign "
            "NTO appointment all reflect the same structural signal: governments and central banks "
            "are asserting direct control over the governance of national and multilateral payment "
            "infrastructure. This is deliberate. Fragmented commercial governance of systemically "
            "important payment schemes creates coordination failures; consolidated sovereign "
            "governance removes them. For commercial PSPs, this narrows the space for scheme-layer "
            "rent extraction but creates new surface area for value-added services built on stable, "
            "well-governed rails."
        ),
        (
            "▶  Stablecoin payments are entering the regulated mainstream — simultaneously in multiple jurisdictions.",
            "The US GENIUS Act AML/NPRM, Singapore's PFMI stablecoin advocacy at the IMF, and "
            "Fasset's institutional funding raise reflect the same underlying shift: stablecoin "
            "payment infrastructure is no longer being evaluated as a speculative crypto asset class "
            "but as a regulated payment rail subject to BSA, AML, sanctions, and in Singapore's "
            "vision, full PFMI standards. The direction of travel is clear — stablecoin payment "
            "issuers and users will be regulated on par with licensed money transmitters and payment "
            "system operators. Firms building stablecoin payment overlays must price in full "
            "compliance cost structures now."
        ),
        (
            "▶  Fraud prevention is moving from reactive to pre-emptive, and from single-institution to cross-industry.",
            "MAS's five-bank AI/ML scam detection POV is a signal of where the frontier of payment "
            "fraud risk management is heading. Pre-payment, cross-institution, AI-driven risk "
            "models — not post-payment reconciliation — are the new standard. The UK's "
            "Confirmation of Payee, Singapore's POV, and the US RTP fraud intelligence frameworks "
            "all converge on the same architecture: shared data, network-level intelligence, and "
            "real-time pre-authorisation risk scoring. PSPs and banks that delay investing in "
            "pre-payment fraud infrastructure will face both regulatory pressure and rising "
            "fraud loss exposure."
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
            "1.  If you operate in ASEAN, accelerate Project Nexus and SPaN integration planning now.",
            "SPaN's end-2026 operational readiness, combined with Nexus's active technical build "
            "toward a 2027 go-live, creates a 12-18 month window to shape your connectivity "
            "architecture decisions. PSPs serving Singapore, Malaysia, Thailand, India, or "
            "Philippines corridors should be in dialogue with the NTO (NETS-PayNet JV) now to "
            "understand integration specifications. First-mover connectivity positions translate "
            "directly into corridor pricing power and merchant/consumer switching costs. Waiting "
            "until go-live to begin technical integration is strategically equivalent to missing "
            "the opportunity entirely."
        ),
        (
            "2.  Build the UAE open finance stack as a product platform, not a compliance checklist.",
            "CBUAE's coordinated roll-out of Aani (12.5M users), Al Tareq (open finance framework), "
            "and a national KYC utility creates a genuine payments product opportunity in the UAE. "
            "The infrastructure exists for account aggregation, instant A2A payment initiation, "
            "embedded onboarding, and personalised financial product distribution — all on a "
            "licensed, regulator-endorsed basis. Product teams in UAE or GCC-focused firms should "
            "be building Al Tareq-native product propositions now, ahead of the licensing and "
            "implementation window crystallising in H2 2026."
        ),
        (
            "3.  Treat stablecoin payment compliance as a day-one architecture decision, not a retrofit.",
            "Whether or not your firm is a stablecoin issuer, the GENIUS Act AML/NPRM and "
            "PFMI advocacy signal that stablecoin-denominated payment flows — for cross-border "
            "settlement, treasury management, or embedded finance — will carry full AML/CFT "
            "obligations within 12-18 months across all major jurisdictions. Product and platform "
            "teams evaluating stablecoin integration must design AML programme, sanctions "
            "screening, and transaction monitoring into their architecture from the start. "
            "Post-hoc compliance retrofitting on live payment volumes is significantly more "
            "expensive and riskier than building it in from day one."
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
            "●  GENIUS Act AML/NPRM Comment Period Closes June 9, 2026.",
            "The comment period for FinCEN and OFAC's joint stablecoin AML/sanctions rulemaking "
            "closes June 9. Comments from major banks, stablecoin issuers (Circle, Coinbase, "
            "Paxos), and fintech trade associations will reveal the key contested provisions — "
            "particularly around transaction monitoring thresholds, third-party wallet screening "
            "obligations, and cross-border stablecoin flow treatment. The final rule will define "
            "the compliance cost structure for the entire stablecoin payments sector."
        ),
        (
            "●  SPaN Membership Expansion Beyond Singapore D-SIBs — Timeline TBC.",
            "SPaN's initial board and membership comprises MAS and the six Domestic Systemically "
            "Important Banks. The next phase — opening membership to other direct participants "
            "of national payments infrastructure (non-bank PSPs, e-money issuers, international "
            "banks) — has no confirmed timeline. Watch for MAS consultation on expanded membership "
            "criteria, as this determines whether PayNow, FAST, and SGQR scheme access rights "
            "and governance voice are available to non-D-SIB payment participants."
        ),
        (
            "●  MENA Cross-Border Payment Corridors — Regional Instant Payment Interoperability Accelerating.",
            "The MENA region has reached what analysts describe as a digital economy inflection "
            "point, with Aani, GCC-wide payment linkage discussions, and new bilateral instant "
            "payment corridor announcements (UAE-India, UAE-Saudi) creating rapid infrastructure "
            "expansion. Watch for CBUAE announcements on international Aani connectivity extensions "
            "and the progress of Arab Monetary Fund-led regional payment interoperability frameworks "
            "as these begin to compete with SWIFT and card rails for intra-GCC and "
            "GCC-Asia corridor flows."
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
        "MAS (mas.gov.sg), CBUAE (centralbank.ae), BIS (bis.org), US Treasury/FinCEN/OFAC "
        "(federalregister.gov), HM Treasury (gov.uk), SWIFT (swift.com), Fintech Futures, "
        "The Paypers, PYMNTS, Fintech News Singapore, Global Government Fintech, Fintech.global, "
        "CoinDesk, IBS Intelligence, Bird &amp; Bird, The Asian Banker.",
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
