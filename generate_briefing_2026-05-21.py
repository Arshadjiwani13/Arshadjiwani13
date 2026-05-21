#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF — May 21, 2026."""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.colors import HexColor

DATE   = "May 21, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-21.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B35C00")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
    return {
        "cover_title": ParagraphStyle("cover_title", fontSize=26, textColor=WHITE,
                                      fontName="Helvetica-Bold", alignment=TA_CENTER, leading=32),
        "cover_sub":   ParagraphStyle("cover_sub",   fontSize=14,
                                      textColor=HexColor("#B4D2FF"),
                                      fontName="Helvetica", alignment=TA_CENTER, leading=20),
        "sec_hdr":     ParagraphStyle("sec_hdr", fontSize=12, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=16, spaceBefore=6),
        "headline":    ParagraphStyle("headline", fontSize=10.5, textColor=NAVY,
                                      fontName="Helvetica-Bold", leading=14, spaceBefore=8),
        "sub_lbl":     ParagraphStyle("sub_lbl", fontSize=9, textColor=HexColor("#404040"),
                                      fontName="Helvetica-Bold", leading=12, spaceBefore=4),
        "body":        ParagraphStyle("body", fontSize=9.5, textColor=BLACK,
                                      fontName="Helvetica", leading=13,
                                      alignment=TA_JUSTIFY, spaceBefore=2),
        "bullet":      ParagraphStyle("bullet", fontSize=9.5, textColor=BLACK,
                                      fontName="Helvetica", leading=13,
                                      leftIndent=12, bulletIndent=2, spaceBefore=1),
        "italic":      ParagraphStyle("italic", fontSize=9.5,
                                      textColor=HexColor("#333333"),
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
        colWidths=[40*mm, 40*mm, 10*mm, 80*mm]
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

    # ── Cover ─────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 — Top Payments Headlines ────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "SWIFT Issues November 2026 Ultimatum on Structured Address Data — "
                        "Non-Compliant Payments Face Rejection",
            "what": (
                "SWIFT has confirmed that from November 14, 2026, cross-border payment messages "
                "containing unstructured postal addresses will be rejected outright by the network. "
                "A hybrid-format minimum — structured country code and town name — becomes the "
                "hard compliance floor for all CBPR+ participants. Concurrently, from the same "
                "date, all institutions must be able to receive Enquiry and Investigation (E&I) "
                "messages in MX format (camt.110 / camt.111). Institutions that migrated to ISO "
                "20022 messaging but retained legacy unstructured address fields in their payment "
                "data face a critical six-month remediation window. Since January 2026, SWIFT has "
                "been levying automatic surcharges on in-flow translation and contingency MT "
                "processing, accelerating the cost case for full compliance."
            ),
            "why": [
                "The November 2026 rejection mandate transforms ISO 20022 structured data from a "
                "best-practice aspiration into a hard operational dependency — non-compliant "
                "payment files will simply fail.",
                "For banks with large corporate client bases, the critical dependency is upstream: "
                "ERP, TMS, and treasury system data quality must be addressed at the source, not "
                "patched at the payment gateway.",
                "Structured address data has direct AML/sanctions screening value — it is a "
                "foundational input for entity resolution, reducing false positives and enabling "
                "more precise name matching.",
                "PSPs and transaction banks that achieve full structural compliance ahead of "
                "the deadline gain a quality and STP advantage over laggards; late movers risk "
                "payment rejection incidents affecting client relationships.",
            ],
            "region": "Global / SWIFT Network",
            "players": "SWIFT, global correspondent banks, transaction banking units, TMS/ERP vendors, corporate treasuries",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — hard rejection deadline six months away",
        },
        {
            "num": "2.",
            "headline": "US GENIUS Act Stablecoin Rules Due July 2026 — "
                        "AML/CFT Framework for Payment Stablecoins Takes Shape",
            "what": (
                "With the GENIUS Act now enacted into US law, the Office of the Comptroller of "
                "the Currency (OCC) published its implementing rule on March 2, 2026 (Federal "
                "Register 2026-04089), establishing the licensing and reserve framework for "
                "payment stablecoin issuers under OCC jurisdiction. FinCEN and OFAC followed on "
                "April 8, 2026, with a joint Notice of Proposed Rulemaking to create a "
                "comprehensive AML/CFT framework for permitted payment stablecoin issuers — "
                "mirroring the Bank Secrecy Act obligations applied to traditional PSPs. "
                "Final rules are due July 18, 2026. Circle (USDC) holds a federal stablecoin "
                "charter under the OCC and is positioned as the most compliance-ready major "
                "issuer. The US stablecoin market has crossed $319.6 billion in total market "
                "cap, with USDT at $189.6 billion and USDC at $77.6 billion as of late April 2026."
            ),
            "why": [
                "The GENIUS Act creates a binding federal licensing framework that treats payment "
                "stablecoins as regulated payment instruments — narrowing regulatory arbitrage "
                "and raising the entry bar for new issuers.",
                "The FinCEN/OFAC AML/CFT rulemaking closes a structural gap: stablecoin "
                "payment operators will now carry BSA obligations equivalent to licensed MSBs "
                "and banks, including SAR filing, CDD, and transaction monitoring.",
                "For banks and PSPs building stablecoin settlement or payment overlays, "
                "July 2026 is a hard planning horizon — compliance architecture, onboarding "
                "flows, and AML tooling must be ready before products go live.",
                "USDC's OCC charter advantage may reshape B2B and institutional stablecoin "
                "payment corridors, particularly for cross-border USD settlement, where "
                "regulatory clarity is a vendor selection criterion.",
            ],
            "region": "United States / Global",
            "players": "OCC, FinCEN, OFAC, Circle (USDC), Tether (USDT), US banks, PSPs, stablecoin issuers",
            "tag": "Stablecoins / Regulation",
            "novelty": "Follow-up with material update — AML rules now in NPRM stage",
        },
        {
            "num": "3.",
            "headline": "TCH RTP Network Sets Single-Day Volume Record — "
                        "Cross-Border Extension Targeted for September 2026",
            "what": (
                "The Clearing House's RTP network processed 2.27 million transactions worth "
                "$8.62 billion on May 1, 2026 — a new single-day record. Year-to-date through "
                "April 2026, tax refund disbursements via RTP grew 78% versus the same period "
                "in 2025, reflecting deepening institutional adoption in government disbursement "
                "use cases. The network is now processing over 1.5 million transactions per day "
                "on average, approaching $500 billion in quarterly value. The Clearing House has "
                "confirmed that cross-border-enabled domestic correspondent activity on the RTP "
                "network is targeted for September 2026, marking the first step toward making "
                "RTP a component of international payment flows."
            ),
            "why": [
                "RTP's trajectory from a niche innovation rail to mainstream settlement "
                "infrastructure is now measurable — the May 1 volume record and 78% government "
                "disbursement growth indicate institutional-grade adoption velocity.",
                "The September 2026 cross-border activation creates a new USD settlement pathway "
                "for international payments — directly competitive with FedNow's parallel "
                "cross-border expansion proposal (Fed comment period closes June 7).",
                "Two competing US instant-payment rails extending into cross-border territory "
                "simultaneously creates a structural complexity for PSPs that must choose or "
                "maintain dual-rail connectivity strategies.",
                "Insurance and healthcare disbursement growth indicates RTP is capturing "
                "regulated-industry disbursement flows previously dominated by ACH — a "
                "permanent market structure shift, not a short-term spike.",
            ],
            "region": "United States",
            "players": "The Clearing House, US financial institutions, correspondent banks, PSPs, healthcare and insurance disbursers",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "New today — record volume + cross-border date confirmed",
        },
        {
            "num": "4.",
            "headline": "UK Regulators Clarify Open Banking Commercial Model — "
                        "VRPs Now 16% of Open Banking Payments",
            "what": (
                "The FCA and PSR issued a joint statement in Q1 2026 clarifying their enforcement "
                "position on the UK Payments Initiative (UKPI) commercial model for variable "
                "recurring payments (VRPs). The regulators confirmed support for a fee-based "
                "commercial VRP framework covering regulated financial services, utilities, and "
                "public sector use cases. VRPs now account for 16% of all open banking payment "
                "transactions in the UK — a material share reflecting growing A2A payment "
                "adoption. Separately, the PSR's proposed merger into the FCA remains in "
                "consultation, with HM Treasury seeking to consolidate regulatory oversight "
                "of payment systems under a single supervisor. PSD3 and the Payment Services "
                "Regulation (PSR) are expected to come into force across the EU in 2026, "
                "refining liability, authentication, and data-sharing frameworks."
            ),
            "why": [
                "Regulatory clarity on VRP commercial models unblocks a critical adoption "
                "barrier — the absence of a sustainable fee framework had stalled VRP "
                "expansion beyond the free-to-use sweeping use case.",
                "16% VRP penetration of UK open banking payments is a tipping point signal: "
                "A2A is transitioning from pilot infrastructure to mainstream payment channel.",
                "The PSR-into-FCA merger proposal would simplify the regulatory landscape "
                "but creates transition risk for payment system operators currently engaging "
                "both regulators on scheme access, interchange, and infrastructure oversight.",
                "PSD3/PSR implementation across the EU in 2026 creates a synchronized "
                "regulatory window for open banking-to-A2A conversion strategies — "
                "product leaders should be mapping customer journeys now.",
            ],
            "region": "United Kingdom / Europe",
            "players": "FCA, PSR, UKPI, UK banks, open banking TPPs, utility and public sector payment operators",
            "tag": "Open Finance / Regulation / A2A",
            "novelty": "Follow-up with material update — VRP share data + commercial model clarity",
        },
        {
            "num": "5.",
            "headline": "European Sovereign Payments Scheme Gains Momentum — "
                        "Domestic Schemes Merge to Form Continental A2A Network",
            "what": (
                "A February 2026 Memorandum of Understanding between five major European domestic "
                "payment schemes — Bancomat (Italy), Bizum (Spain), SIBS/MB Way (Portugal), "
                "Vipps MobilePay (Nordics), and the European Payments Initiative (Wero) — "
                "marks the most significant European payments sovereignty development in a decade. "
                "The MoU establishes the foundation for a pan-European A2A payment network with "
                "interoperability across member markets, directly targeting Visa and Mastercard's "
                "dominance in European card payments. This development is framed by EU policymakers "
                "as a strategic response to US card and Big Tech payment infrastructure dependency. "
                "Separately, the mandatory adoption of SEPA Instant Payments across Europe "
                "reached its one-year anniversary in February 2026, with A2A described as the "
                "defining payments technology trend of 2026."
            ),
            "why": [
                "Five domestic schemes merging signals a credible path to pan-European A2A "
                "infrastructure that has eluded the continent for years — the combination of "
                "Wero's fintech execution capability and established national scheme reach "
                "creates genuine network effect potential.",
                "This directly threatens Visa/Mastercard's European card interchange revenues "
                "and Google/Apple Pay dominance in mobile payments — and the EU is explicitly "
                "framing it as a strategic sovereignty project.",
                "PSPs operating in European markets must model a scenario where A2A becomes "
                "the default consumer payment method within 3–5 years, replacing card-on-file "
                "flows for e-commerce and recurring payments.",
                "SEPA Instant's one-year mandatory anniversary means the rail infrastructure "
                "is now universally available — the limiting factor shifts from infrastructure "
                "to scheme design, consumer habit, and merchant acceptance.",
            ],
            "region": "Europe",
            "players": "Bancomat, Bizum, SIBS/MB Way, Vipps MobilePay, Wero/EPI, European Commission, Visa, Mastercard",
            "tag": "Market Structure / Open Finance / RTP",
            "novelty": "Follow-up with material update — MoU confirmed and strategic framing elevated",
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

    # ── SECTION 2 — Major Fintech Headlines ───────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "FIS Taps Anthropic to Automate AML with AI Agents — "
                        "BMO and Amalgamated Bank in First Cohort",
            "what": (
                "FIS announced a partnership with Anthropic to deploy a Financial Crimes AI Agent "
                "powered by Claude, with BMO and Amalgamated Bank among the first financial "
                "institutions entering development. FIS provides the core financial-crimes "
                "infrastructure layer while Claude models supply the reasoning capability for "
                "alert triage, entity resolution, and investigator support. The partnership "
                "targets the structural challenge of legacy AML platforms — designed for batch "
                "processing and static rules — that are now misaligned with real-time payment "
                "rails. US financial institutions alone spend $35–40 billion annually on AML "
                "compliance. A separate May 2026 analysis from Napier AI warns that bolting AI "
                "onto legacy AML foundations will not solve the underlying brittle architecture "
                "problem: platform modernization, not AI overlay, is the structural solution."
            ),
            "why": (
                "AML automation at tier-1 bank scale via a major infrastructure vendor (FIS) "
                "is qualitatively different from point-solution AI tools. If this deployment "
                "achieves material false-positive reduction and alert triage efficiency at BMO "
                "scale, it will rapidly become a competitive benchmark that other banks cannot "
                "ignore. For payment platform architects, this reinforces a critical design "
                "principle: real-time payment rails require continuous, event-driven AML "
                "monitoring — the batch-processing paradigm is now structurally obsolete."
            ),
            "strategic": (
                "AI-native financial crimes infrastructure is emerging as a competitive "
                "differentiator; legacy compliance platforms face existential pressure to "
                "modernize or be displaced by vendor-led AI-agent models."
            ),
        },
        {
            "num": "2.",
            "headline": "Capital One–Discover Integration Reshapes US Card Market Structure",
            "what": (
                "The Federal Reserve and OCC approved Capital One's $51.8 billion acquisition "
                "of Discover, with the transaction closing in May 2026. The combined entity "
                "creates the largest US credit card issuer by loan balances and, critically, "
                "gives Capital One ownership of the Discover payment network — the only major "
                "US card network not currently owned by a bank. This is the first time a "
                "large US bank has acquired a card network since the industry structure was "
                "established, fundamentally changing the vertical integration dynamics of "
                "US card payments."
            ),
            "why": (
                "Capital One now controls both the issuer and the network — a structural "
                "position that Visa, Mastercard, and Amex do not hold. This enables Capital "
                "One to route its own card transactions over Discover rails, bypassing "
                "interchange fees on a material share of its portfolio. Long-term, it creates "
                "pricing and network-access leverage that no other US bank currently possesses. "
                "For merchants, acquirers, and PSPs, this shifts negotiating dynamics around "
                "Discover network acceptance, routing, and potentially introduces a new "
                "competitive variable in least-cost routing strategies."
            ),
            "strategic": (
                "Vertical integration of issuing and network ownership at scale sets a "
                "strategic precedent — other large banks and fintechs will reassess whether "
                "network ownership is a viable moat in the evolving US payments landscape."
            ),
        },
        {
            "num": "3.",
            "headline": "Xero Acquires Melio Payments for $2.5 Billion — "
                        "Embedded B2B Payments in Accounting Software Scale Up",
            "what": (
                "Xero, the cloud accounting platform, completed its acquisition of Melio "
                "Payments — a B2B payments platform for SMEs — for $2.5 billion. Melio "
                "enables small businesses to pay and receive business payments via ACH, "
                "card, and check, embedded natively within accounting workflows. The "
                "acquisition brings payments infrastructure directly into Xero's 4+ million "
                "customer base, enabling native bill payment, AR/AP automation, and cash "
                "flow management at the point of accounting reconciliation."
            ),
            "why": (
                "Accounting software is one of the highest-intent touchpoints for B2B "
                "payment initiation — Xero's acquisition is a direct play to own the "
                "payment trigger, not just the ledger. For B2B payment PSPs and "
                "embedded finance platforms, this signals that accounting software vendors "
                "are transitioning from payment referrers to payment operators. The "
                "$2.5 billion price reflects the embedded finance premium on owning "
                "SME payment flows at scale, not just data."
            ),
            "strategic": (
                "Accounting-native payment execution is becoming a structural moat for "
                "SME-focused platforms — embedded B2B payments at the point of "
                "reconciliation compresses the distance between financial data and "
                "payment action to zero."
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

    # ── SECTION 3 — What Matters Most ─────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Real-time rail infrastructure is going cross-border — and two US rails "
            "are racing each other to get there first.",
            "Both TCH RTP (September 2026 target) and FedNow (Reg J amendment in comment "
            "period) are extending into cross-border territory simultaneously. For PSPs and "
            "transaction banks, the strategic question is no longer whether US instant rails "
            "will support international flows — it is which rail, which intermediary model, "
            "and which corridors will dominate. Dual-rail strategy and intermediary selection "
            "are now live product decisions, not future-state planning."
        ),
        (
            "▶  Regulatory perimeters are expanding synchronously across all major "
            "payments jurisdictions.",
            "The GENIUS Act (US), CBUAE Law (UAE), PSD3/PSR (EU), and UK National Payments "
            "Vision represent a synchronized global wave of regulatory scope expansion — "
            "covering stablecoins, open finance, VRPs, and payment technology operators. "
            "The window between regulation passing and compliance deadlines is compressing. "
            "Payment firms operating across multiple jurisdictions face an unusually dense "
            "multi-horizon compliance calendar for the remainder of 2026."
        ),
        (
            "▶  A2A / open banking is reaching the inflection point between infrastructure "
            "availability and mainstream adoption.",
            "SEPA Instant's one-year mandatory anniversary, VRPs at 16% of UK open banking "
            "payments, and the five-scheme European MoU all signal that the enabling "
            "infrastructure for A2A is now in place. The rate-limiting factor has shifted "
            "to commercial model clarity, consumer habit formation, and merchant incentive "
            "structures — which are all now actively moving. European card network "
            "displacement is no longer a theoretical outcome."
        ),
    ]

    for title, body in themes:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── SECTION 4 — Implications for a Payments Product Leader ────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Make November 2026 SWIFT structured address compliance a product delivery "
            "milestone — not a compliance backlog item.",
            "Six months is a short runway when the remediation dependency sits in client-side "
            "ERP and TMS data models, not your own systems. Map your payment file flows to "
            "identify where unstructured address data enters the chain, issue client "
            "notifications now, and build rejection-scenario handling into your payment "
            "operations playbook. Early completion creates a competitive quality story; "
            "late remediation creates client relationship risk at the worst possible time."
        ),
        (
            "2.  Build a dual-rail cross-border strategy for US instant payments before "
            "September 2026 crystallises the market structure.",
            "TCH RTP's September 2026 cross-border date and FedNow's comment period "
            "are running concurrently. The intermediary models, pricing structures, and "
            "FX integration patterns will be set in the next 90 days. If your firm handles "
            "USD cross-border flows, engage now — either by submitting to the Fed Reg J "
            "comment process, evaluating intermediary partnerships, or modelling RTP "
            "corridor economics. Waiting for the market to settle means accepting someone "
            "else's structural choices."
        ),
        (
            "3.  Reassess your European A2A and open banking product roadmap against a "
            "3–5 year card displacement scenario.",
            "The five-scheme European MoU, SEPA Instant's universal availability, and VRP "
            "commercial model clarity combine into a single signal: A2A is transitioning "
            "from optional overlay to primary payment method in Europe. Product leaders "
            "with European exposure should model card-to-A2A migration scenarios for their "
            "highest-volume use cases — e-commerce checkout, subscriptions, B2B invoice "
            "settlement — and assess which merchant segments are most immediately addressable "
            "with A2A economics."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 — Optional Watchlist ────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  GCC Open Banking frameworks — Saudi Arabia SAMA sandbox expansion, "
            "UAE AlTareq rollout depth.",
            "The GCC open banking ecosystem is maturing rapidly but unevenly. Saudi Arabia's "
            "SAMA sandbox is expanding API scope, and the UAE's AlTareq platform is moving "
            "from framework to live payment initiation. Watch for formal open banking "
            "regulation (rather than sandbox guidance) from CBUAE — likely in H2 2026 "
            "— which would create a concrete licensing and API standardization deadline "
            "for financial data and payment initiation providers across the UAE."
        ),
        (
            "●  GENIUS Act implementing rules — July 18, 2026 finalization date.",
            "The FinCEN/OFAC joint AML/CFT NPRM for payment stablecoin issuers and the "
            "OCC implementing rule will crystallize the compliance architecture for US "
            "stablecoin payments. Watch for the final rule's treatment of non-US issuers "
            "serving US persons — the extraterritorial scope of the BSA obligations will "
            "determine whether Tether (USDT) can maintain meaningful US market access, "
            "and whether foreign banks can custody GENIUS Act-compliant stablecoins."
        ),
        (
            "●  AI-native AML platform displacement — watch for bank RFPs and vendor "
            "consolidation signals.",
            "The FIS-Anthropic deployment signals the opening of an AI-native AML "
            "infrastructure wave. Over the next 6–12 months, watch for large bank RFPs "
            "that explicitly require AI-agent-based alert triage and investigation support "
            "— rather than AI overlays on legacy platforms. Legacy AML vendors (NICE Actimize, "
            "Oracle FCCM, SAS) face existential pressure to ship credible native AI "
            "architectures or face displacement. This is a M&A and platform-strategy signal "
            "worth tracking closely."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── Disclaimer ────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank "
        "publications, regulatory releases, scheme operator announcements, and reputable "
        "financial media. It is intended for informational purposes only and does not "
        "constitute investment, legal, or regulatory advice. Key sources: SWIFT (swift.com), "
        "The Clearing House (theclearinghouse.org), Federal Reserve (federalreserve.gov), "
        "FCA/PSR (fca.org.uk / psr.org.uk), CBUAE (centralbank.ae), MAS (mas.gov.sg), "
        "OCC / FinCEN / OFAC (federalregister.gov), Fintech Global (fintech.global), "
        "The Paypers (thepaypers.com), American Banker, PYMNTS.com.",
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
