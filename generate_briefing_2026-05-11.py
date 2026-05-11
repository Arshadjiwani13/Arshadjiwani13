#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF — May 11, 2026."""

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

DATE = "May 11, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-11.pdf"

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

    # ── COVER ──────────────────────────────────────────────────────────────────
    story.append(cover_block(s))
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1: TOP PAYMENTS HEADLINES ──────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "US GENIUS Act Crosses Into Implementation: FDIC Issues Proposed Rulemaking for Stablecoin Issuers",
            "what": (
                "The FDIC Board approved a Notice of Proposed Rulemaking (NPRM) to implement "
                "requirements under the GENIUS Act, establishing a prudential framework for "
                "FDIC-supervised permitted payment stablecoin issuers. The proposed rules address "
                "reserve asset composition, redemption obligations, capital adequacy, and risk "
                "management standards. Simultaneously, the Clarity Act compromise text — brokered "
                "between Senate Banking Committee members, the White House, and crypto/banking "
                "industry groups — emerged on May 1, 2026, drawing immediate pushback from six "
                "major banking trade associations on May 8, who argued the yield-carve-out "
                "provisions grant unfair competitive advantages to crypto firms."
            ),
            "why": [
                "Stablecoins now have a regulatory implementation pathway in the US — the GENIUS Act "
                "is no longer a framework debate but an active compliance program with deadlines and "
                "capital requirements.",
                "FDIC supervision of stablecoin issuers introduces bank-equivalent prudential standards "
                "to crypto payment infrastructure — this will reshape who can issue at payment-system "
                "scale and at what cost.",
                "The banking industry's Clarity Act objections signal a sustained structural tension "
                "between bank yield economics and crypto platform economics — this regulatory fight "
                "is not over, and the final text will set competitive boundaries for years.",
                "For payments product leaders, stablecoin issuance is moving from a product feature "
                "to a licensed and capitalized payment infrastructure activity — with direct implications "
                "for partnership, white-label, and infrastructure decisions.",
            ],
            "region": "United States",
            "players": "FDIC, OCC, US Senate Banking Committee, banking trade groups, stablecoin issuers, crypto exchanges",
            "tag": "Stablecoins / Regulation / Market Structure",
            "novelty": "Escalation — implementation now active",
        },
        {
            "num": "2.",
            "headline": "MAS Launches Wholesale CBDC Pilot for Tokenized MAS Bills; Finalizes Stablecoin Rules and Signs Bundesbank Cross-Border Pact",
            "what": (
                "The Monetary Authority of Singapore confirmed a 2026 live pilot enabling primary "
                "dealers to issue and settle MAS Treasury Bills through blockchain-based tokens "
                "backed by a wholesale Singapore-dollar CBDC. The initiative builds on Project "
                "Guardian — now comprising 40+ financial institutions — and follows MAS's "
                "finalization of full-reserve stablecoin regulations requiring SGD 1 million "
                "minimum capital. MAS also signed a cross-border collaboration pact with the "
                "Deutsche Bundesbank to develop universal standards for tokenized payments, "
                "securities, and assets."
            ),
            "why": [
                "This is the first instance of a G20-equivalent central bank anchoring tokenized "
                "government securities settlement to wholesale CBDC — establishing a model for "
                "private-chain assets settling against central bank money with no counterparty risk.",
                "The Bundesbank pact signals convergence between Singapore and European central bank "
                "infrastructure thinking on tokenization standards — creating early cross-jurisdictional "
                "interoperability architecture.",
                "MAS's finalized full-reserve stablecoin rules, combined with the CBDC pilot, place "
                "Singapore in a unique position: offering both a regulated stablecoin pathway and a "
                "wholesale CBDC settlement layer for institutional use.",
                "For cross-border payment and treasury product leaders, Singapore is establishing "
                "itself as the proving ground for tokenized money settlement — with implications for "
                "liquidity management, T-bill collateral, and intraday settlement architecture.",
            ],
            "region": "Singapore / Germany / Global",
            "players": "MAS, Deutsche Bundesbank, DBS, JPMorgan, Standard Chartered, Project Guardian partners",
            "tag": "Infrastructure / Stablecoins / Cross-Border",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "CBUAE Deploys World-First Sovereign Financial Cloud — FIT Programme Reaches Critical Infrastructure Phase",
            "what": (
                "The Central Bank of the UAE announced the deployment of the world's first sovereign "
                "financial cloud services infrastructure, built in partnership with Core42 (a G42 "
                "subsidiary). The platform provides an isolated, nationally controlled environment "
                "hosting critical banking data, applications, and services — embedding AI and "
                "real-time analytics. This forms a core pillar of the CBUAE's Financial "
                "Infrastructure Transformation (FIT) programme, which also encompasses the Aani "
                "instant payments platform, a CBDC initiative, and open finance regulatory "
                "infrastructure under the Federal Decree-Law No. 6 of 2025."
            ),
            "why": [
                "A central bank-controlled financial cloud is a novel infrastructure model — it "
                "centralizes operational resilience, data sovereignty, and AI capability in a "
                "nationally governed environment that can set interoperability and access standards "
                "for all UAE-regulated financial institutions.",
                "For payment firms operating in the UAE, this infrastructure layer creates both an "
                "opportunity (shared services, API connectivity, regulatory sandbox access) and an "
                "obligation to align technical architecture with sovereign cloud standards.",
                "Combined with the September 2026 licensing deadline for open finance and VA payment "
                "providers under the CBUAE Law, the UAE is executing a simultaneous technology and "
                "regulatory modernization that creates a compressed upgrade cycle for all market participants.",
                "The GCC's compound annual growth in payments is among the highest globally — "
                "this infrastructure investment signals long-duration platform ambition, not "
                "incremental improvement.",
            ],
            "region": "UAE / GCC",
            "players": "CBUAE, Core42, G42, UAE-licensed banks and PSPs, Aani platform participants",
            "tag": "Infrastructure / Regulation / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "UK Open Banking Achieves Mainstream Commerce Penetration — VRPs at 16%, Amazon and eBay Live",
            "what": (
                "UK open banking payment volumes rose 53% year-on-year, with Variable Recurring "
                "Payments (VRPs) now representing 16% of all open banking transactions — up from "
                "negligible levels in 2024. The payment method has entered mainstream e-commerce "
                "with live integrations on Amazon UK and eBay. The first live payments under the "
                "UKPI (UK Payments Infrastructure) scheme launched in Q1 2026. allpay launched its "
                "Pay by Bank solution. In Europe, TrueLayer announced the acquisition of Zimpler "
                "to build a pan-European Pay by Bank network spanning the Nordics and beyond. "
                "HM Treasury is expected to grant the FCA new rule-setting powers for open banking "
                "in 2026."
            ),
            "why": [
                "Amazon and eBay integration is not marginal — it is structural confirmation that "
                "Pay by Bank has cleared the merchant trust and conversion-rate threshold required "
                "for mainstream commerce adoption in the UK.",
                "VRPs at 16% of open banking volume is a material market-structure signal: "
                "subscription and recurring payment use cases are migrating from cards toward "
                "account-to-account rails faster than most projections anticipated.",
                "The TrueLayer/Zimpler acquisition indicates that European Pay by Bank players are "
                "consolidating to achieve the geographic scale needed to compete with card-network "
                "ubiquity — a structural prerequisite for merchant-side adoption.",
                "FCA rule-setting authority in 2026 will determine long-term commercial viability "
                "of open banking payments — the regulatory architecture for monetization, premium "
                "APIs, and data sharing is still being constructed.",
            ],
            "region": "UK / Europe",
            "players": "Open Banking Ltd, FCA, HM Treasury, TrueLayer, allpay, Amazon, eBay, Zimpler, UK PSPs",
            "tag": "Open Finance / RTP / Market Structure",
            "novelty": "Escalation — mainstream commerce milestone",
        },
        {
            "num": "5.",
            "headline": "SWIFT ISO 20022: Structured Address Hard Deadline Enters Six-Month Window — Compliance Pressure Intensifies",
            "what": (
                "With November 14, 2026 now six months away, SWIFT's hard deadline for removing "
                "unstructured postal addresses from cross-border payments over CBPR+ and key Payment "
                "Market Infrastructures is entering the critical execution phase. Since January 1, "
                "2026, automatic surcharges have been active for institutions relying on in-flow "
                "translation services or contingency MT processing. The requirement mandates "
                "structured country codes and town names minimum — a foundational data-quality "
                "shift affecting all corporate payment instructions across the correspondent "
                "banking network."
            ),
            "why": [
                "The six-month window is the final forcing function for corporate treasury and "
                "payment factory data remediation programs — ERP/TMS configurations must be "
                "updated, client master data enriched, and validation rules deployed.",
                "Institutions still on in-flow translation are now paying SWIFT pricing penalties "
                "while also facing a hard cut-off in November — the cost-risk calculus strongly "
                "favors accelerating native ISO 20022 adoption.",
                "Structured address data is a systemic enabler for AML/sanctions screening "
                "precision — banks that complete remediation early gain a compounding advantage "
                "in false-positive reduction and automated STP.",
                "Corporate clients with complex multi-entity payment structures face the highest "
                "remediation complexity; banks that offer structured data enrichment as a "
                "managed service will differentiate on client value.",
            ],
            "region": "Global",
            "players": "SWIFT, correspondent banks, corporate treasuries, ERP/TMS vendors, Payment Market Infrastructures",
            "tag": "Infrastructure / Regulation / Cross-Border",
            "novelty": "Escalation — 6-month final window now active",
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

    # ── SECTION 2: MAJOR FINTECH HEADLINES ────────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "Adyen Acquires Talon.One for €750M — Payment Processors Move Up the Commerce Stack",
            "what": (
                "Dutch paytech Adyen signed a definitive agreement to acquire Berlin-based customer "
                "loyalty and promotions platform Talon.One for €750 million, funded from Adyen's "
                "cash reserves with closing expected H2 2026. Talon.One's rule-based promotion "
                "engine integrates directly into checkout and payment flows, allowing merchants to "
                "execute targeted loyalty, discount, and incentive programs at the transaction layer."
            ),
            "why_matters": (
                "Adyen is making a deliberate product bet that the future payment processor "
                "is a commerce enablement platform — not just a settlement rail. Embedding loyalty "
                "economics at the payment moment collapses the gap between transaction data and "
                "customer engagement, creating a margin expansion opportunity beyond processing fees. "
                "This acquisition follows Stripe's commerce tooling investments and signals a "
                "broader competitive reframing: PSPs that own merchant-side value chain layers "
                "beyond payments will structurally outperform those that compete on processing margin alone."
            ),
            "strategic": "Payment processors are acquiring commerce-layer capabilities as a structural moat against commoditization of settlement infrastructure.",
        },
        {
            "num": "2.",
            "headline": "Ebury Raises £550M as Santander Increases Stake to 55% — SME Cross-Border Infrastructure at Scale",
            "what": (
                "UK-headquartered SME cross-border payments and FX firm Ebury raised approximately "
                "£550 million in a new funding round, with majority shareholder Santander increasing "
                "its stake to 55% via a new £50 million direct investment. The remaining capital "
                "came from external institutional investors. Ebury processes FX and cross-border "
                "payments for over 50,000 SME clients across 25+ currencies."
            ),
            "why_matters": (
                "Santander's stake increase to majority control signals strategic intent to integrate "
                "Ebury's SME cross-border infrastructure more deeply into Santander's global "
                "commercial banking distribution. For the SME cross-border payments market — "
                "still fragmented and underserved by traditional correspondent banking — "
                "this represents a bank-fintech convergence model at scale: bank distribution "
                "network plus fintech FX and payment execution stack. Santander's global "
                "footprint in Latin America, Europe, and the UK makes Ebury a credible "
                "challenger to SWIFT-based SME payment flows."
            ),
            "strategic": "Bank-controlled fintech platforms for SME cross-border payments are emerging as the mid-market alternative to both pure correspondent banking and standalone fintech rails.",
        },
        {
            "num": "3.",
            "headline": "Global Fintech Funding Exceeds $814M Across 17 Deals Week of May 8 — Infrastructure Concentration Continues",
            "what": (
                "Fintech.global reported $814 million raised across 17 funding rounds in the week "
                "ending May 8, 2026, with capital concentrated in B2B infrastructure, compliance "
                "technology, and embedded finance tooling. Separately, cumulative global fintech "
                "funding surpassed $800 billion in total since sector inception, with US firms "
                "capturing the dominant share. InsurTech firm Corgi reached unicorn status at "
                "$1.3 billion valuation following a $160 million Series B."
            ),
            "why_matters": (
                "The composition of funding — infrastructure and compliance over consumer distribution "
                "— continues to validate the thesis that value creation in fintech is migrating from "
                "the front-end to the middleware and platform layer. For payments specifically, "
                "orchestration, compliance-as-a-service, and API-native banking infrastructure "
                "are attracting institutional capital at a point where consumer neobanks are "
                "consolidating and cutting costs."
            ),
            "strategic": "Infrastructure fintech is the 2026 VC thesis — consistent with the product platform shift toward API-layer value capture over distribution-layer competition.",
        },
    ]

    for h in fintech:
        block = []
        block.append(Paragraph(f"{h['num']}  {h['headline']}", s["headline"]))
        block.append(Paragraph("What happened:", s["sub_lbl"]))
        block.append(Paragraph(h["what"], s["body"]))
        block.append(Paragraph("Why it matters to fintech / payments:", s["sub_lbl"]))
        block.append(Paragraph(h["why_matters"], s["body"]))
        block.append(Paragraph("Strategic relevance:", s["sub_lbl"]))
        block.append(Paragraph(h["strategic"], s["italic"]))
        block.append(Spacer(1, 3*mm))
        block.append(HRFlowable(width="100%", thickness=0.5, color=SILVER))
        block.append(Spacer(1, 3*mm))
        story.append(KeepTogether(block))

    # ── SECTION 3: WHAT MATTERS MOST ──────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  The stablecoin regulatory architecture is shifting from framework to enforcement "
            "reality — with payment-system-scale implications.",
            "The US GENIUS Act FDIC rulemaking, MAS's finalized full-reserve stablecoin rules, "
            "and MAS's earlier call for PFMI-standard oversight of systemic stablecoins collectively "
            "signal that regulators are no longer designing the framework — they are building the "
            "enforcement and supervisory infrastructure. This changes the competitive calculus for "
            "stablecoin-as-payment-rail: only well-capitalized, fully licensed issuers will "
            "operate at payment-system scale. For banks and PSPs, the question is no longer "
            "whether stablecoins are real — it is whether to build, buy, or partner against "
            "a now-defined regulatory baseline."
        ),
        (
            "▶  Central bank infrastructure investment is creating new platform layers that will "
            "define market access rules for the next decade.",
            "The CBUAE's sovereign financial cloud and MAS's wholesale CBDC settlement pilot are "
            "not incremental upgrades — they are new infrastructure layers sitting beneath "
            "commercial payment activity. These platforms will set API standards, data governance "
            "rules, and interoperability requirements that commercial participants must align to. "
            "Firms that engage early with central bank infrastructure programs — as primary "
            "dealers, pilot participants, or certified API partners — gain first-mover access "
            "to the terms of market participation before they become mandatory compliance "
            "obligations."
        ),
        (
            "▶  Account-to-account payment adoption is accelerating past the tipping point "
            "in the UK, with Europe following structurally.",
            "53% YoY volume growth, VRP at 16% of transactions, and Amazon/eBay "
            "integrations in the UK represent a qualitative shift: A2A payments are no longer "
            "a fringe alternative to cards — they are entering the mainstream purchasing flow "
            "for millions of consumers. Combined with EU PSR provisional political agreement "
            "and TrueLayer/Zimpler consolidation, the European Pay by Bank network is gaining "
            "the geographic and commercial scale to challenge card-rail economics on high-value "
            "and recurring payment use cases."
        ),
    ]

    for title, body in themes:
        story.append(Paragraph(title, s["theme_title"]))
        story.append(Paragraph(body, s["body"]))
        story.append(Spacer(1, 3*mm))

    # ── SECTION 4: IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER ─────────────────
    story.append(section_header("4.", "IMPLICATIONS FOR A PAYMENTS PRODUCT LEADER", s))
    story.append(Spacer(1, 3*mm))

    implications = [
        (
            "1.  Develop a stablecoin payment infrastructure position now — before the GENIUS Act "
            "framework crystallizes into competitive disadvantage.",
            "The FDIC NPRM opens a comment period and implementation runway. Payments product "
            "leaders should assess whether their firm's strategic position requires becoming a "
            "permitted stablecoin issuer, a distribution partner, or a settlement infrastructure "
            "provider — and map that to the reserve, capital, and compliance requirements in the "
            "proposed rules. Waiting until implementation is finalized means starting execution "
            "behind competitors already building to the proposed standard."
        ),
        (
            "2.  If you operate in the UAE or plan to enter the GCC market, align your technical "
            "architecture to the CBUAE sovereign cloud and FIT programme standards proactively.",
            "The sovereign cloud and Aani instant payments platform are becoming the technical "
            "baseline for UAE-regulated payments. Firms that engage with CBUAE's developer "
            "ecosystem, API standards, and licensing requirements before September 2026 — "
            "particularly for open finance services and VA payment services now in scope — "
            "will avoid the compressed compliance crunch that will hit late movers. "
            "Early certification on the sovereign cloud infrastructure is a durable "
            "market-access advantage."
        ),
        (
            "3.  Treat the SWIFT November 2026 structured address deadline as a client value "
            "opportunity, not just an internal compliance workstream.",
            "Banks and PSPs that launch client-facing structured data enrichment tools — "
            "validating and auto-completing address fields in payment files, providing "
            "dashboards on compliance readiness, and offering managed remediation services — "
            "will capture fee revenue and client stickiness from the thousands of corporate "
            "clients now under pressure to meet the November deadline. The data quality "
            "improvement also generates downstream benefit in sanctions screening, STP rates, "
            "and AML false-positive reduction that strengthens the ROI narrative internally."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5: OPTIONAL WATCHLIST ─────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  Clarity Act final text and Senate floor vote — June/July 2026.",
            "The Clarity Act banking industry pushback on May 8 signals active lobbying pressure "
            "before any Senate floor vote. Watch for revised text on the yield carve-out "
            "provisions — the final language will determine whether bank and crypto stablecoin "
            "issuers compete on level terms or whether the Act creates a structural arbitrage "
            "for crypto-native issuers. This is the most consequential near-term text to monitor "
            "for US stablecoin payment infrastructure strategy."
        ),
        (
            "●  Project Nexus — PSP technical integration announcements (ASEAN corridors).",
            "With live implementation underway and BSP Philippines confirmed for onboarding by "
            "mid-2027, watch for corridor-specific PSP announcements across the SGD/MYR/THB/INR/PHP "
            "corridors. Early PSP technical partnerships with Nexus Global Payments will reveal "
            "which players are positioning for first-mover advantage in the multilateral instant "
            "cross-border scheme — and which are waiting for the infrastructure to mature."
        ),
        (
            "●  EU PSR formal adoption and PSD3 trilogue finalization — H1/H2 2026.",
            "Following the November 2025 provisional political agreement on the EU Payments "
            "Package (PSD3 + PSR), formal adoption and publication in the Official Journal is "
            "expected in H1-H2 2026. Watch for the final PSR text on open banking premium API "
            "access, VRP-equivalent mandates for the Eurozone, consumer protection for instant "
            "payment fraud, and PSP liability rules — these will set the European competitive "
            "and regulatory environment for the next seven to ten years."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── DISCLAIMER ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank "
        "publications, regulatory releases, and reputable financial media. It is intended for "
        "informational purposes only and does not constitute investment, legal, or regulatory "
        "advice. Key sources: FDIC (fdic.gov), OCC (occ.treas.gov), MAS (mas.gov.sg), "
        "CBUAE (centralbank.ae), SWIFT (swift.com), FCA (fca.org.uk), BIS (bis.org), "
        "Coindesk, PYMNTS, Fintech Futures, Fintech.global, Open Banking Expo, "
        "The Payments Association, Khaleej Times, Zawya, Gulf News.",
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
