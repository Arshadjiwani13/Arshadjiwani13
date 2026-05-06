#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 6, 2026."""

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

DATE   = "May 6, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-06.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
ORANGE = HexColor("#C05000")
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
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
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
        ("BACKGROUND", (0, 0), (-1, -1), LGRAY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    return tbl


def tag_row(tag, novelty, region, players, s):
    novelty_bg = GREEN if "New" in novelty else (ORANGE if "Escalation" in novelty else LBLUE)
    tag_para = Paragraph(f"<font color='white'><b> {tag} </b></font>", ParagraphStyle(
        "tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=NAVY,
        leading=11, borderPadding=3))
    novelty_para = Paragraph(f"<font color='white'><b> {novelty} </b></font>", ParagraphStyle(
        "nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE, backColor=novelty_bg,
        leading=11, borderPadding=3))
    reg_para  = Paragraph(f"<b>Region:</b> {region}", ParagraphStyle(
        "reg", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(f"<b>Players:</b> {players}", ParagraphStyle(
        "play", fontSize=8, fontName="Helvetica", textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "",           play_para, ""]],
        colWidths=[42*mm, 44*mm, 8*mm, 76*mm]
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
    story.append(Spacer(1, 8*mm))

    # ── SECTION 1 ──────────────────────────────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "FCA Payment Safeguarding Rules Enter Force — New Obligations Live for "
                        "Payment and E-Money Firms",
            "what": (
                "As of May 7, 2026, the FCA's revamped safeguarding regime (Policy Statement PS25/12) "
                "is now in full effect for all UK-regulated payment institutions and e-money firms. "
                "The rules introduce daily reconciliation of safeguarded funds, mandatory annual "
                "safeguarding audits by qualified auditors (with results submitted to the FCA), "
                "and monthly regulatory returns confirming safeguarding practices. Firms must also "
                "maintain comprehensive resolution packs to enable prompt fund return in insolvency "
                "scenarios. An exemption from the audit requirement applies only where a firm has "
                "not safeguarded more than £100,000 at any point in a 53-week period."
            ),
            "why": [
                "This is a major operational uplift for mid-tier and challenger payment firms — daily "
                "reconciliation and audit mandates require significant process and technology investment.",
                "The resolution pack requirement signals the FCA is pre-positioning for orderly wind-down "
                "of payment firms — a direct response to high-profile firm failures in prior years.",
                "Monthly returns create a new ongoing supervisory data flow; non-compliance will now "
                "be detectable quickly, raising the stakes for firms with weak safeguarding governance.",
                "EMIs and PIs operating in UK with multiple currencies or complex client money structures "
                "face the highest compliance burden — outsourced compliance and RegTech tooling demand "
                "will rise sharply in H2 2026.",
            ],
            "region": "United Kingdom",
            "players": "FCA, UK payment institutions, e-money institutions, auditors, RegTech providers",
            "tag": "Regulation / Fraud-Risk",
            "novelty": "New today",
        },
        {
            "num": "2.",
            "headline": "Federal Reserve Cross-Border FedNow Proposal: Comment Window Open Until "
                        "June 9",
            "what": (
                "The Federal Reserve's April 8, 2026 proposal to amend Regulation J Subpart C remains "
                "open for public comment until June 9, 2026. The proposal would allow FedNow "
                "participants to designate non-Reserve Bank intermediaries — including non-U.S. "
                "correspondent banks — to process the international leg of cross-border instant "
                "payments. FedNow now counts over 1,700 participating institutions, surpassing TCH "
                "RTP's ~1,200. Separately, TCH's RTP network is preparing domestic-correspondent "
                "bank activity for September 2026 as a precursor to cross-border expansion, while "
                "FedNow volume hit $5.2 billion in a single day in recent testing."
            ),
            "why": [
                "The June 9 comment period is the critical window for banks and PSPs to shape the "
                "intermediary framework — designations will define who controls cross-border FedNow "
                "flow routing and economics.",
                "FedNow's institution count now exceeds RTP, signalling it is becoming the primary "
                "instant rail for smaller U.S. institutions — cross-border capability amplifies this "
                "structural advantage.",
                "TCH RTP's September 2026 domestic-correspondent launch and FedNow's cross-border "
                "ambition together signal U.S. instant rails will serve international flows within "
                "18 months — compressing SWIFT/card incumbent advantages in USD corridors.",
                "For PSPs serving inbound USD remittance corridors (Asia, MENA, Latin America), "
                "the cost and speed implications of a Fed-backed instant cross-border rail are "
                "strategically significant.",
            ],
            "region": "United States / Global",
            "players": "Federal Reserve, The Clearing House, U.S. banks, correspondent banks, "
                       "cross-border PSPs",
            "tag": "Cross-Border / RTP / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "3.",
            "headline": "UK Government Confirms PSR Abolition — Payment Systems Oversight "
                        "Consolidates into FCA by End-2026",
            "what": (
                "The UK government has confirmed, following its September 2025 consultation, that "
                "the Payment Systems Regulator (PSR) will be abolished and its functions transferred "
                "to the Financial Conduct Authority (FCA). Legislation is targeted for completion "
                "by end-2026. The FCA will absorb the PSR's mandate to promote competition and "
                "innovation in payment systems, protect consumers, and oversee access and pricing "
                "in designated payment systems. Respondents broadly welcomed the consolidation as "
                "reducing regulatory duplication and streamlining engagement."
            ),
            "why": [
                "A single UK payments regulator significantly reduces compliance overhead for firms "
                "currently maintaining dual FCA/PSR engagement — but raises questions about "
                "whether PSR's sharper competition focus will be diluted inside a larger prudential body.",
                "Card scheme and interbank pricing oversight (historically a PSR focus) must now be "
                "maintained within the FCA — watch for how the FCA structures a dedicated payments "
                "competition function post-merger.",
                "Open banking commercial model development (cVRP, UKPI) was under PSR/FCA joint "
                "oversight — merger may accelerate FCA-led open banking regulatory framing.",
                "International firms and payment systems operators will need to update regulatory "
                "engagement frameworks as the PSR's separate identity and decision processes cease "
                "to exist.",
            ],
            "region": "United Kingdom",
            "players": "UK HM Treasury, FCA, PSR, payment system operators, banks, fintechs",
            "tag": "Regulation / Market Structure",
            "novelty": "Escalation — consolidation confirmed",
        },
        {
            "num": "4.",
            "headline": "US Senate CLARITY Act Stablecoin Yield Compromise — Legislation "
                        "Advancing Toward Markup",
            "what": (
                "Senators Tillis and Alsobrooks released a formal CLARITY Act compromise text on "
                "stablecoin yield rules, clearing a key Senate Banking Committee obstacle. The "
                "compromise prohibits stablecoin yield that is the functional or economic equivalent "
                "of bank deposit interest, but explicitly permits yield from 'bona fide activities' "
                "such as staking rewards and protocol distributions. Coinbase and Circle immediately "
                "endorsed the deal and are pushing the committee toward a markup vote. The bill "
                "treats stablecoins as payment instruments requiring full reserve backing, licensed "
                "issuers, and guaranteed redemption rights."
            ),
            "why": [
                "If passed, this would be the first comprehensive U.S. federal stablecoin law — "
                "transforming stablecoins from a de-facto grey zone into a regulated payment "
                "instrument with defined capital, reserve, and redemption requirements.",
                "The yield compromise draws a clear line between payment stablecoins and "
                "deposit-taking — protecting banks' regulatory moat while legitimising "
                "protocol-native yield, a key crypto industry demand.",
                "Circle (USDC) and other reserve-backed stablecoin issuers stand to benefit "
                "most from a clear federal licensing path — reducing state-by-state patchwork risk.",
                "For PSPs and banks building stablecoin payment rails, a federal licensing "
                "framework will crystallise the product compliance architecture required for "
                "B2B and cross-border stablecoin settlement at scale.",
            ],
            "region": "United States",
            "players": "US Senate Banking Committee, Coinbase, Circle, stablecoin issuers, banks, "
                       "federal regulators",
            "tag": "Stablecoins / Regulation",
            "novelty": "Escalation — bill advancing to markup",
        },
        {
            "num": "5.",
            "headline": "CFPB Section 1033 Open Banking Goes Live: Large Bank Compliance "
                        "Deadline Passed in April 2026",
            "what": (
                "The Consumer Financial Protection Bureau's Section 1033 open banking rule "
                "(finalized October 2024) reached its first compliance milestone in April 2026, "
                "with the largest U.S. depository institutions required to enable standardized, "
                "machine-readable data sharing with consumer-authorized third parties at no charge. "
                "Covered data includes transaction histories, account balances, and payment terms. "
                "Smaller institutions follow on a staggered timeline through April 2030. This "
                "is the first mandatory open banking standard in the United States."
            ),
            "why": [
                "The U.S. open banking era is now formally underway — A2A payment overlays, "
                "personal finance aggregators, and account-switching services can now access "
                "standardized data from major U.S. banks as a legal right, not a commercial "
                "negotiation.",
                "Pay-by-bank (A2A) use cases will accelerate as data access costs drop and "
                "account verification becomes standardized — directly pressuring card network "
                "transaction volumes in use cases such as bill pay, e-commerce, and P2P.",
                "For PSPs building data-powered payment products in the U.S., Section 1033 "
                "lowers the marginal cost of bank connectivity — favouring infrastructure "
                "players who can aggregate and act on this data at scale.",
                "Risk: CFPB enforcement posture under the current administration remains "
                "uncertain — implementation quality and early enforcement priority are worth "
                "monitoring closely.",
            ],
            "region": "United States",
            "players": "CFPB, major U.S. banks, data aggregators, fintech PSPs, A2A payment "
                       "providers",
            "tag": "Open Finance / Regulation / RTP",
            "novelty": "Escalation — compliance deadline passed",
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
            "headline": "Ebury Raises £550 Million — Santander Backs Cross-Border Payments "
                        "Scale-Up",
            "what": (
                "Ebury, the international payments and FX fintech majority-owned by Santander, "
                "closed a ~£550 million funding round led by Centerbridge Partners, with "
                "participation from Santander (£50 million), Vitruvian Partners, and 83North. "
                "Santander's stake decreases from 66% to 55% as part of the structure. Ebury "
                "operates in 30 regulated markets, processes payments in 140+ currencies across "
                "160 countries, and has grown revenues at 30%+ per annum since Santander's 2020 "
                "investment. Proceeds target product development, geographic expansion, and "
                "AI-powered payment processing and FX optimization."
            ),
            "why": (
                "This is the largest cross-border payments fintech raise of 2026 to date. The "
                "Santander-Centerbridge structure signals institutional confidence in SME-focused "
                "cross-border payment infrastructure at a time when FedNow and SWIFT ISO 20022 "
                "evolution are reshaping corridor economics. Ebury's geographic scale (160 countries, "
                "140+ currencies) gives it a structural moat in the SME cross-border segment that "
                "pure-play RTP infrastructure plays cannot easily replicate. The AI capability focus "
                "is directionally aligned with where cross-border payment differentiation is moving: "
                "FX pricing intelligence, compliance automation, and payment routing optimization."
            ),
            "strategic": (
                "Ebury's raise confirms that cross-border payment infrastructure targeting SMEs "
                "remains a high-conviction institutional investment category in 2026, even as "
                "macro headwinds affect broader fintech funding."
            ),
        },
        {
            "num": "2.",
            "headline": "AML Enforcement Enters Real-Time Era: FINTRAC Fines VersaBank; "
                        "Regulators Signal Escalating Scrutiny",
            "what": (
                "FINTRAC fined VersaBank CA$42,075 on May 5, 2026 for AML/CTF policy failures "
                "and inadequate high-risk client controls — one of several enforcement actions "
                "as regulators globally transition from rule-setting to active enforcement. U.S. "
                "bank regulators (FDIC, NCUA, OCC) and FinCEN are advancing coordinated AML "
                "rulemaking requiring continuous, risk-driven monitoring aligned with product, "
                "customer, and geography exposure. The EU Instant Payments Regulation has "
                "accelerated real-time AML monitoring mandates across eurozone PSPs."
            ),
            "why": (
                "The convergence of instant payment rails and rising enforcement intensity creates "
                "a structural risk for PSPs: you cannot pause a real-time payment for manual "
                "review. This is driving urgent investment in AI-powered, inline transaction "
                "monitoring capable of microsecond risk scoring. For payments product leaders, "
                "AML and fraud controls must now be first-class product components — not "
                "compliance overlays — designed into the payment flow architecture from inception."
            ),
            "strategic": (
                "Real-time compliance is becoming a payment product differentiator: PSPs with "
                "embedded, instant AML/fraud scoring will outperform those running batch or "
                "post-transaction controls as enforcement risk and instant payment volumes grow."
            ),
        },
        {
            "num": "3.",
            "headline": "UK cVRP Phase 1 Live: Commercial Variable Recurring Payments Begin "
                        "Reshaping A2A Landscape",
            "what": (
                "Commercial Variable Recurring Payments (cVRP) went live in the UK under the "
                "first-phase commercial model agreed by the FCA and industry in early 2026, with "
                "live payments under the UK Payment Innovation (UKPI) scheme beginning in Q1 2026. "
                "VRPs now account for 16% of UK open banking transactions, driven primarily by "
                "sweeping VRPs to date. Commercial cVRP extends this model to broader merchant "
                "use cases including subscriptions, utilities, and variable billing. The FCA will "
                "assess phase 1 growth by end-2026 to inform a long-term regulatory framework."
            ),
            "why": (
                "cVRP is the mechanism that transforms open banking from a data-access layer into "
                "a full-cycle payments rail capable of displacing card-on-file and direct debit "
                "for recurring merchant payment use cases. The commercial model launch removes "
                "the last structural barrier to mainstream merchant adoption in the UK. Combined "
                "with Amazon and eBay enabling Pay-by-Bank for UK consumers, A2A is crossing "
                "from early-adopter to mainstream payment infrastructure in the UK market."
            ),
            "strategic": (
                "UK cVRP's commercial launch marks the tipping point for A2A recurring payment "
                "viability — PSPs and merchants should accelerate integration planning given the "
                "FCA's intent to build a long-term regulatory framework from Q4 2026 observations."
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

    # ── SECTION 3 ──────────────────────────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Real-time rails are going cross-border — and the window to shape the framework "
            "is narrow.",
            "Both FedNow (proposed rule, June 9 comment close) and TCH RTP (September 2026 "
            "domestic-correspondent launch) are on parallel tracks toward international capability. "
            "These are not distant roadmap items — they are active regulatory and operational "
            "developments with hard timelines. PSPs and banks in major cross-border corridors "
            "must treat them as a near-term strategic priority, not a future-watch item."
        ),
        (
            "▶  Regulatory structure in major markets is being redrawn — simultaneously.",
            "UK is merging its payments regulator into the FCA (end-2026). The U.S. is on the "
            "verge of passing its first stablecoin law. The U.S. also activated its first mandatory "
            "open banking standard this week. These are structural changes, not incremental rule "
            "updates — they redefine who regulates what, what is legal, and what is required "
            "across three of the world's most important payments markets."
        ),
        (
            "▶  Open finance is crossing from optionality to obligation — A2A product strategy "
            "must accelerate.",
            "UK cVRP commercial model is live. U.S. Section 1033 large-bank deadline has passed. "
            "Europe's Instant Payments Regulation is driving VoP and A2A infrastructure across "
            "the eurozone. The account-to-account payment model is no longer a niche alternative "
            "— it is becoming regulated, mandated payment infrastructure in the world's largest "
            "consumer markets. Product teams still treating A2A as exploratory are now behind "
            "the regulatory curve."
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
            "1.  If your firm operates in the UK — FCA safeguarding compliance is not optional "
            "from today.",
            "Daily reconciliation, annual audit, and monthly FCA returns are now legally required "
            "for UK PIs and EMIs. The resolution pack requirement is particularly demanding for "
            "firms with complex multi-currency client money structures. Treat this as an "
            "immediate operational gap-close priority, not a future roadmap item. The FCA's "
            "enhanced supervisory data flow from monthly returns means deficiencies will be "
            "visible to the regulator in near-real time."
        ),
        (
            "2.  File comments or watch the FedNow cross-border comment period (closes June 9).",
            "The shape of the designated intermediary framework will define who controls "
            "USD cross-border routing economics for the next decade. If your firm processes "
            "USD cross-border flows or services remittance corridors involving the U.S., "
            "monitor submissions from large U.S. correspondent banks closely — they will "
            "signal competitive positioning before the rule is finalized. A formal submission "
            "from your organization could influence the intermediary eligibility criteria."
        ),
        (
            "3.  Accelerate A2A product strategy — open banking is moving from opt-in "
            "to mandatory infrastructure.",
            "With U.S. Section 1033 live, UK cVRP commercial model launched, and EU "
            "Instant Payments Regulation driving VoP adoption, 2026 is the year the A2A "
            "competitive threat to card-on-file and direct debit becomes structural rather "
            "than hypothetical. Product leaders should be actively scoping use-case-specific "
            "A2A product roadmaps (subscriptions, payouts, bill pay) and assessing where "
            "their current card/ACH/SEPA flows are most at risk of displacement."
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
            "●  TCH RTP domestic-correspondent bank activity — September 2026 launch.",
            "The Clearing House's September 2026 target for domestic-correspondent activity on "
            "the RTP network is the operational bridge toward full cross-border RTP capability. "
            "Watch for TCH–EBA Clearing–SWIFT joint announcement on the legal/administrative "
            "framework for trans-Atlantic RTP linkage — the operational feasibility study is "
            "complete; the legal structure is the remaining gating item."
        ),
        (
            "●  UK PSR/FCA merger legislation — end-2026 target.",
            "The legislative vehicle to formally dissolve the PSR board and transfer its "
            "functions to the FCA is expected before end-2026. Watch for clarity on how "
            "FCA will structure its dedicated payments competition function, and whether "
            "PSR's card scheme interchange and access pricing oversight will be maintained "
            "with equivalent rigour or deprioritized within the broader FCA mandate."
        ),
        (
            "●  SWIFT structured address hard deadline — November 2026.",
            "After November 2026, only structured or hybrid postal addresses will be "
            "accepted in SWIFT cross-border payment messages. Institutions that have not "
            "completed data remediation and client outreach programs are now at risk of "
            "payment rejection at scale. Watch for SWIFT's compliance monitoring reports "
            "and early rejection statistics as November approaches — these will be "
            "leading indicators of systemic industry readiness."
        ),
    ]

    for title, body in watchlist:
        block = []
        block.append(Paragraph(title, s["watchlbl"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── Disclaimer ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 4*mm))
    story.append(HRFlowable(width="100%", thickness=0.3, color=SILVER))
    story.append(Paragraph(
        "This briefing is compiled from publicly available sources including central bank "
        "publications, regulatory releases, and reputable financial media. It is intended "
        "for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources: FCA (fca.org.uk), Federal Reserve "
        "(federalreserve.gov), Sullivan &amp; Cromwell (sullcrom.com), Crowdfund Insider, "
        "FXC Intelligence, Norton Rose Fulbright, RSM UK, FinTech Futures, "
        "Santander press release (santander.com), CoinDesk, The Payments Association, "
        "PYMNTS, American Banker, A&amp;O Shearman, Open Banking Expo.",
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
