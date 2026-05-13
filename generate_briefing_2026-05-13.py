#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF — May 13, 2026."""

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

DATE   = "May 13, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-13.pdf"

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


def tag_row(tag, novelty, novelty_color, region, players, s):
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
        colWidths=[48*mm, 48*mm, 4*mm, 70*mm]
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


def divider():
    return [HRFlowable(width="100%", thickness=0.5, color=SILVER), Spacer(1, 3*mm)]


def build_story(s):
    story = []

    # ── Cover ─────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 — TOP PAYMENTS HEADLINES ───────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "PSD3 / PSR Final Texts Published — EU Parliament Plenary Vote Imminent",
            "what": (
                "On April 23, 2026, the Council of the European Union published the final compromise "
                "texts for the Third Payment Services Directive (PSD3) and the new Payment Services "
                "Regulation (PSR). The ECON Committee voted on May 5; a Parliament plenary vote is "
                "expected in late May, with Official Journal publication targeted for June/July 2026 "
                "(possibly slipping to September). The rules will apply 21 months post-publication "
                "— placing full implementation in late 2027 or early 2028."
            ),
            "why": [
                "PSD3 and PSR split PSD2's monolithic scope: PSD3 governs authorisation, governance, "
                "capital, and supervision of payment institutions; PSR directly regulates payment "
                "conduct — applying without national transposition, enabling faster and more uniform "
                "EU-wide regulatory effect.",
                "The PSR's direct applicability is the architectural shift: unlike PSD2, there is no "
                "transposition ambiguity by member state — timelines and obligations are uniform from "
                "day one.",
                "Non-EU PSPs serving EU markets, and all EU-licensed PSPs, should begin PSD3/PSR "
                "readiness assessments now — the 21-month window starts on Official Journal "
                "publication, not when national laws are enacted.",
                "Open banking provisions in PSD3 strengthen ASPSP data-sharing obligations and "
                "introduce a new 'payment service data scheme' concept — material implications for "
                "A2A payment product and open finance infrastructure strategy.",
            ],
            "region": "European Union",
            "players": "European Parliament, Council of the EU, European Commission, banks, PSPs, fintechs",
            "tag": "Regulation / Open Finance / Market Structure",
            "novelty": "New today",
            "novelty_color": GREEN,
        },
        {
            "num": "2.",
            "headline": "GENIUS Act: FDIC and OCC Run Concurrent NPRMs — Comment Period Closes June 9",
            "what": (
                "Two parallel U.S. stablecoin rulemakings are in the comment phase simultaneously. "
                "The OCC published its GENIUS Act NPRM on March 2, 2026; the FDIC approved its NPRM "
                "on April 7, 2026 (Federal Register, April 10; comment deadline June 9). Both agencies "
                "propose: 2-business-day redemption requirements for Permitted Payment Stablecoin "
                "Issuers (PPSIs), reserve asset standards, capital requirements, and risk management "
                "frameworks. The GENIUS Act's 18-month outer limit from enactment (July 18, 2025) "
                "sets a January 2027 floor for the effective date — or 120 days post-final-rules, "
                "whichever comes first."
            ),
            "why": [
                "Two concurrent NPRMs from the FDIC and OCC define the institutional architecture "
                "for U.S. stablecoin payment rails — who can issue, how reserves are structured, "
                "and what redemption UX is legally permissible.",
                "The 2-business-day redemption requirement has direct implications for stablecoin "
                "payment liquidity design — it limits atomic settlement propositions currently "
                "marketed by crypto-native issuers.",
                "Non-bank issuers face a structural disadvantage: the GENIUS Act's framework "
                "favors FDIC- and OCC-supervised entities — reshaping competition between "
                "bank-issued and non-bank-issued stablecoins as payment instruments.",
                "The June 9 comment deadline is the clearest opportunity for PSPs, banks, and "
                "payments infrastructure firms to shape the final US stablecoin payment framework.",
            ],
            "region": "United States",
            "players": "FDIC, OCC, Federal Reserve, Treasury, stablecoin issuers, banks, PSPs",
            "tag": "Stablecoins / Regulation / Market Structure",
            "novelty": "Follow-up with material update",
            "novelty_color": AMBER,
        },
        {
            "num": "3.",
            "headline": "FSB Launches Cross-Border Payments Public-Private Implementation Phase — G20 Targets at Risk",
            "what": (
                "In March 2026, the FSB convened its Cross-Border Payments Summit in London, "
                "launching a new structured public-private implementation phase under the G20 "
                "Roadmap. The Institute of International Finance (IIF) committed to producing "
                "industry findings and recommendations in H2 2026. FSB data shows G20 Roadmap "
                "KPIs for 2025 achieved only marginal improvement since 2023, with the 2027 "
                "targets — sub-1% retail cross-border cost, 75% of payments in under 1 hour, "
                "expanded access — now considered unlikely to be met on schedule."
            ),
            "why": [
                "The official acknowledgment that 2027 Roadmap targets are at risk is a material "
                "policy signal — it opens a window for recalibrating targets and reprioritising "
                "interventions, with the IIF report becoming the primary industry voice in that "
                "process.",
                "The shift to public-private co-design changes how PSPs should engage: active "
                "participation in IIF workstreams and FSB consultation processes now offers "
                "greater leverage over framework design than waiting for final rules.",
                "FX markup transparency, access for underserved corridors, and data "
                "interoperability remain the persistent bottlenecks — the same gaps that existed "
                "when the Roadmap launched in 2020.",
                "ISO 20022 adoption by RTGS systems is projected to reach 83% by end-2026 "
                "(BIS CPMI), overtaking fast-payment-system adoption for the first time — a "
                "technical milestone the Roadmap depends on but does not alone resolve.",
            ],
            "region": "Global",
            "players": "FSB, BIS, G20, IIF, central banks, global PSPs, correspondent banks",
            "tag": "Cross-Border / Market Structure / Regulation",
            "novelty": "Escalation — G20 targets officially at risk",
            "novelty_color": AMBER,
        },
        {
            "num": "4.",
            "headline": "ISO 20022 RTGS Adoption Reaches Structural Tipping Point — November Structured Address Deadline in Focus",
            "what": (
                "BIS CPMI data confirms ISO 20022 adoption by RTGS systems is on track to surpass "
                "83% by end-2026, overtaking fast-payment systems and representing the first time "
                "the standard becomes functionally dominant across high-value settlement "
                "infrastructure. Simultaneously, SWIFT's November 2026 CBPR+ deadline for fully "
                "structured postal address fields — mandatory structured country code and town name "
                "minimum — is the most pressing near-term compliance horizon for cross-border "
                "payment institutions. SEPA version 3.7 (pain.001.001.09 and pain.008.001.08) is "
                "mandatory now, cascading into payment factory and ERP/TMS format dependencies."
            ),
            "why": [
                "83% RTGS adoption is not a migration milestone — it is the point at which ISO "
                "20022 becomes the default expectation of global high-value settlement, making "
                "non-compliance a competitive and operational liability rather than a timeline "
                "risk.",
                "Institutions with unstructured legacy address data face SWIFT surcharges "
                "(active since January 1, 2026) and a hard exclusion risk from November 2026 — "
                "data remediation programs must be operating at scale now, not scoped.",
                "Fully structured ISO 20022 data unlocks compounding returns: enhanced ML-based "
                "fraud detection, higher-confidence sanctions screening, and straight-through "
                "processing rates that reduce manual intervention costs.",
                "SEPA 3.7 format changes cascade into corporate payment factory integrations, "
                "ERP/TMS configurations, and bank-to-corporate API schemas — product and "
                "operations teams must validate end-to-end format compliance now.",
            ],
            "region": "Global / Europe",
            "players": "SWIFT, SEPA operators, BIS CPMI, corporate treasuries, TMS/ERP vendors, correspondent banks",
            "tag": "Infrastructure / Regulation",
            "novelty": "Follow-up with material update",
            "novelty_color": AMBER,
        },
        {
            "num": "5.",
            "headline": "MAS Launches Project BLOOM — Tokenized Settlement Assets and Agentic Payments",
            "what": (
                "The Monetary Authority of Singapore launched Project BLOOM (Borderless, Liquid, "
                "Open, Online, Multi-currency), a structured financial industry collaboration "
                "exploring tokenized bank liabilities and well-regulated stablecoins as settlement "
                "assets for cross-border payments. BLOOM's three initial workstreams are: "
                "(1) distribution and clearing of tokenized settlement assets, (2) programmable "
                "compliance controls for automated AML/KYC, and (3) agentic payments — fully "
                "AI-initiated, automated payment flows. MAS will also trial tokenized government "
                "bills in 2026, settled using wholesale central bank digital currency (wCBDC)."
            ),
            "why": [
                "Project BLOOM is MAS's first structured, multi-firm program specifically targeting "
                "tokenized settlement infrastructure — moving from sandboxed experimentation to "
                "industry-scale design of production-grade payment architecture.",
                "Agentic payments represent a genuinely new product category: AI agents initiating "
                "transactions autonomously require new authorization frameworks, liability models, "
                "real-time spending controls, and audit trails — none of which current payment "
                "schemes are designed for.",
                "Tokenized bank liabilities as settlement assets could eliminate pre-funding and "
                "trapped nostro/vostro liquidity in cross-border corridors — a structural cost "
                "reduction that benefits both PSPs and their corporate clients.",
                "Singapore's simultaneous operation of Project Nexus (multilateral IPS linkage), "
                "BLOOM (tokenized settlement), and wCBDC trials positions MAS as the most "
                "comprehensive testing ground for next-generation payment infrastructure globally.",
            ],
            "region": "Singapore / Global",
            "players": "MAS, financial industry participants, stablecoin issuers, banks, technology providers",
            "tag": "Infrastructure / RTP / Open Finance / Stablecoins",
            "novelty": "New today",
            "novelty_color": GREEN,
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
        block.append(tag_row(h["tag"], h["novelty"], h["novelty_color"],
                             h["region"], h["players"], s))
        block.append(Spacer(1, 3*mm))
        block.extend(divider())
        story.append(KeepTogether(block))

    # ── SECTION 2 — MAJOR FINTECH HEADLINES ──────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Adyen Acquires Talon.One for €750 Million — Merchant Value Stack Expands Beyond Payments",
            "what": (
                "Adyen has signed a definitive agreement to acquire Talon.One, a Berlin-based "
                "enterprise-grade provider of loyalty, promotion, and referral management "
                "software, for €750 million. The transaction is expected to close in H2 2026. "
                "Talon.One serves major enterprise merchants managing complex multi-channel "
                "loyalty and discount programs across digital and physical commerce environments."
            ),
            "why": (
                "Adyen is making a deliberate move from payment processor to merchant operating "
                "system. By combining real-time transaction data at the authorization layer with "
                "loyalty and promotion management, Adyen gains the ability to offer merchants "
                "real-time promotion triggers, customer lifetime value analytics, and "
                "dynamic incentive personalization at point-of-sale — creating a closed-loop "
                "data and payments offering that neither pure loyalty platforms nor pure "
                "processors currently provide at scale. This competes directly with "
                "Stripe's merchant-side product stack and intensifies the battle for enterprise "
                "merchant platform ownership."
            ),
            "strategic": "Payment processors are racing to own the merchant value stack beyond the authorization moment — loyalty, data, and engagement infrastructure are the next competitive frontier.",
        },
        {
            "num": "2.",
            "headline": "Ebury Raises £550 Million — Santander Doubles Down on B2B Cross-Border Payments",
            "what": (
                "UK fintech Ebury, specialising in cross-border payments, FX risk management, "
                "and trade finance for SMEs and mid-market corporates, raised approximately "
                "£550 million in new funding. Majority shareholder Santander increased its "
                "stake in the round, which was led by new investor Centerbridge Partners "
                "alongside Vitruvian Partners and 83North. The raise positions Ebury to "
                "accelerate geographic expansion and deepen its payments and lending product set."
            ),
            "why": (
                "A £550 million raise for a B2B cross-border payments fintech, in an environment "
                "where European fintech funding is down approximately 60%, is a significant "
                "outlier. It signals sustained institutional conviction in the underserved "
                "SME cross-border payments segment — a market where bank offerings remain "
                "expensive, opaque, and slow. Santander's increased stake deepens the "
                "bank-fintech co-ownership model and creates a strategic distribution advantage "
                "across Santander's global banking footprint, particularly in the UK, Spain, "
                "and Latin America. Combined with Ebury's FX and trade finance capabilities, "
                "this positions it as a serious platform competitor to traditional correspondent "
                "banking for mid-market cross-border flows."
            ),
            "strategic": "B2B cross-border payments for SMEs remains a high-conviction category — even in a tighter funding environment — with bank-fintech co-ownership emerging as the dominant scaling model.",
        },
        {
            "num": "3.",
            "headline": "European Fintech Funding Down 60% — Infrastructure Layer Outperforms Consumer Neobanks",
            "what": (
                "European fintech funding has fallen approximately 60% from peak levels, with "
                "the neobank wave stratifying sharply into three tiers: pan-European leaders "
                "running licensed banks (Revolut, N26, Monzo, Bunq), a mid-tier of profitable "
                "vertical challengers, and a significant wave of failures among mid-sized "
                "neobanks that exhausted runway after cheap capital dried up. Meanwhile, "
                "embedded finance infrastructure — payments APIs, compliance-as-a-service, "
                "embedded lending — is capturing disproportionate value, with the global "
                "embedded finance market reaching approximately $197 billion in 2026 (31% CAGR "
                "through 2034)."
            ),
            "why": (
                "The stratification of European fintech reflects a market structure shift: the "
                "consumer distribution layer is consolidating toward a few scaled winners, "
                "while infrastructure and API-layer players are growing faster and capturing "
                "more durable margin. For payments product leaders, this means the strategic "
                "value of orchestration platforms, compliance APIs, and embedded payment "
                "infrastructure has increased — and the risk of over-indexing on consumer "
                "distribution without infrastructure differentiation has become clear."
            ),
            "strategic": "Infrastructure-first fintech is outcompeting consumer distribution as the primary value-capture layer — the margin pool is moving to the platform, not the product.",
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
        block.extend(divider())
        story.append(KeepTogether(block))

    # ── SECTION 3 — WHAT MATTERS MOST ────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Regulation is converging simultaneously across all major payment hubs — on both ends of the stack.",
            "PSD3/PSR, GENIUS Act NPRMs, and MAS BLOOM are all reaching decision points "
            "in the same narrow window. Organisations operating across US, EU, and Singapore "
            "jurisdictions face a multi-front compliance and product re-architecture calendar "
            "through 2027. The regulatory scaffolding being installed now — stablecoin issuance "
            "rules, PSR conduct obligations, tokenized settlement frameworks — will define the "
            "competitive operating environment for the next decade."
        ),
        (
            "▶  Tokenized settlement infrastructure is moving from policy aspiration to institutional program.",
            "MAS BLOOM represents the clearest signal yet that central banks and regulated "
            "institutions are actively designing — not just studying — tokenized settlement "
            "for cross-border payments. Combined with Singapore's wCBDC trials, the GENIUS "
            "Act's stablecoin payment framework, and the FSB's public-private implementation "
            "phase, the conditions for a meaningful tokenized payment layer are coalescing "
            "across multiple jurisdictions simultaneously. The question is no longer if, "
            "but which architecture wins — and who the intermediaries are."
        ),
        (
            "▶  The G20 cross-border payments ambition is formally behind schedule — creating both risk and opportunity.",
            "With 2027 G20 Roadmap KPIs acknowledged as unlikely to be met, the FSB and IIF "
            "are entering a period of Roadmap revision. This creates a genuine lobbying and "
            "agenda-setting opportunity for payment infrastructure players who can demonstrate "
            "credible corridor-level impact. It also signals that the correspondent banking "
            "model, despite ISO 20022 uplift, is not delivering the speed, cost, and "
            "transparency improvements that the Roadmap promised — keeping pressure on "
            "multilateral alternatives like Project Nexus."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4 — IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER ───────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Engage the GENIUS Act comment process before June 9.",
            "The FDIC's 2-business-day redemption requirement and reserve asset framework will "
            "define US stablecoin payment UX, liquidity management, and competitive structure. "
            "For any organisation building or planning stablecoin payment capabilities in the "
            "US market, the comment window is the highest-leverage moment to shape the final "
            "framework — not just observe it. Particular attention should go to the redemption "
            "timeline, reserve asset eligibility, and interoperability obligations."
        ),
        (
            "2.  Launch a PSD3 / PSR readiness program with a late-2027 target date.",
            "The 21-month implementation window starts on Official Journal publication "
            "(estimated June/July 2026). For EU-market participants, the PSR's direct "
            "applicability means obligations will be uniform and immediate — no transposition "
            "gaps. Two parallel workstreams are needed: (a) PSR conduct compliance and "
            "open banking data-sharing obligations; (b) PSD3 authorisation, capital, and "
            "governance alignment by jurisdiction. Begin scope assessment now — late "
            "readiness programs in mid-2027 will face regulatory and resourcing constraints."
        ),
        (
            "3.  Define your agentic payments policy before regulators define it for you.",
            "MAS BLOOM's explicit agentic payments workstream is an early signal that "
            "regulators are beginning to engage with AI-initiated payment flows. Payments "
            "product leaders should define internal frameworks now: what authorization "
            "levels can AI agents hold? What real-time spending controls apply? Who bears "
            "liability for erroneous agent-initiated transactions? Organisations that "
            "publish internal agentic payment governance policies in 2026 will be better "
            "positioned to participate in regulatory design processes — and to win "
            "institutional client trust when agentic payment products launch."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 — WATCHLIST ─────────────────────────────────────────────────
    story.append(Spacer(1, 3*mm))
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  IIF Cross-Border Payments Recommendations Report — H2 2026.",
            "The IIF has committed to producing industry findings and recommendations for "
            "evolving the G20 Roadmap framework. This document will be the primary industry "
            "voice in the next phase of cross-border payment reform design. Payments "
            "organisations should engage the IIF working process now and monitor the draft "
            "for corridor prioritisation, technology recommendations, and governance proposals "
            "that could become the basis for FSB's revised Roadmap targets."
        ),
        (
            "●  GENIUS Act Final Rules — Effective Date Window (120 days post-final-rules or January 2027).",
            "The FDIC comment period closes June 9 and OCC's on a similar timeline. Watch "
            "for final rule publication in Q3/Q4 2026 — which triggers the 120-day clock "
            "for the GENIUS Act's effective date. This is the hard deadline for stablecoin "
            "payment issuers to be licensed, reserves to be structured, and redemption "
            "mechanisms to be in production. Banks and PSPs planning stablecoin payment "
            "products must have implementation programs running before final rules publish."
        ),
        (
            "●  EU PSD3/PSR Official Journal Publication — June/July 2026 (potentially September).",
            "The timing of Official Journal publication directly sets the 21-month "
            "implementation clock. A September publication pushes full PSR applicability "
            "to mid-2028, while a June publication targets late 2027. Both timelines are "
            "close enough that readiness programs should run to the earlier scenario. "
            "Watch for Parliament plenary vote outcome and legal-linguistic review timeline "
            "to determine which publication date is realistic."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── Footer disclaimer ─────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, scheme operator announcements, and reputable financial media. It is "
        "intended for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources: MAS (mas.gov.sg), FSB (fsb.org), BIS CPMI (bis.org), "
        "FDIC (fdic.gov), OCC (occ.treas.gov), Federal Register (federalregister.gov), "
        "European Council (consilium.europa.eu), SWIFT (swift.com), Linklaters, Norton Rose "
        "Fulbright, Morgan Lewis, Freshfields, DLA Piper, PYMNTS, FinTech Futures, "
        "The Payments Association, Convera, JPMorgan Payments Insights.",
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
