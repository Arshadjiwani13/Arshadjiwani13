#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – June 1, 2026."""

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

DATE   = "June 1, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-06-01.pdf"

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
            "headline": "Project Nexus: Indonesia Joins as Sixth Country; Technical Operator Tender Launched",
            "what": (
                "Indonesia has officially joined Project Nexus as its sixth participating country, "
                "extending the multilateral instant cross-border payment scheme's reach to cover "
                "Singapore, India, Malaysia, Philippines, Thailand, and Indonesia — connecting "
                "IPS networks that collectively serve over 2 billion people. Nexus Global Payments "
                "(NGP), incorporated in Singapore, has simultaneously issued an Invitation to Tender "
                "for the Nexus Technical Operator, the firm that will build the Nexus software, set "
                "up and operate the infrastructure, and run day-to-day technical and business "
                "operations. This marks the decisive transition from architecture design to live build."
            ),
            "why": [
                "Indonesia's addition via BI-FAST dramatically expands corridor coverage; Indonesia-Singapore and Indonesia-India are among the highest-value ASEAN remittance corridors globally.",
                "The Technical Operator RFP is the critical path item — the selected firm will define API standards, connectivity sequencing, and commercial models for all six corridors.",
                "PSPs and banks in all six connected markets should treat the tender timeline as their live-implementation countdown clock; 2027 is not abstract.",
                "The hub-and-spoke model means a single Nexus integration unlocks any-to-any connectivity across all six markets — a structural efficiency gain vs. bilateral linkage proliferation.",
                "Singapore's role as NGP's incorporation domicile consolidates its position as the de facto anchor for Asia-Pacific multilateral payments infrastructure.",
            ],
            "region": "Singapore / Asia-Pacific (ASEAN + India)",
            "players": "Nexus Global Payments, MAS, BIS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, Bank Indonesia",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "Follow-up with material update",
        },
        {
            "num": "2.",
            "headline": "Singapore Payments Network (SPaN) Targets End-2026 Operational Readiness",
            "what": (
                "The Monetary Authority of Singapore and the Association of Banks in Singapore have "
                "confirmed that the Singapore Payments Network (SPaN), incorporated as a not-for-profit "
                "company in late 2025, is targeting operational readiness by end 2026. SPaN will "
                "assume consolidated governance over Singapore's eight national payment schemes — "
                "including FAST, GIRO, PayNow, and SGQR — under a single entity, replacing the "
                "fragmented oversight previously split across ABS and MAS. The 11-member board "
                "includes MAS, Domestic Systemically Important Banks, and four independent directors."
            ),
            "why": [
                "Consolidating eight national scheme governance structures under one entity reduces fragmentation, accelerates rule-making, and creates a single point of accountability for scheme evolution.",
                "SPaN's mandate to govern both national and cross-border payment schemes positions it as Singapore's primary interlocutor with Project Nexus and bilateral IPS linkage counterparts.",
                "For PSPs and banks operating in Singapore, SPaN creates a new industry engagement point for scheme rule changes, fee structures, and innovation mandates — firms should begin relationship-building now.",
                "The governance model (not-for-profit, bank + MAS board) mirrors successful European FMI governance structures and represents a deliberate institutional design choice.",
            ],
            "region": "Singapore",
            "players": "MAS, ABS, DBS, OCBC, UOB, Citibank, HSBC, and Singapore D-SIBs",
            "tag": "Infrastructure / Market Structure",
            "novelty": "New today",
        },
        {
            "num": "3.",
            "headline": "GENIUS Act Implementation: OCC, FDIC, and FinCEN Issue Multi-Agency Stablecoin NPRMs",
            "what": (
                "The U.S. GENIUS Act (signed July 2025) is now generating its implementing regulatory "
                "architecture. The OCC, FDIC, and FinCEN/OFAC have each published Notices of Proposed "
                "Rulemaking covering, respectively: licensing standards for national bank stablecoin "
                "issuers; prudential capital and liquidity requirements for FDIC-supervised issuers; "
                "and AML/CFT and OFAC sanctions compliance program requirements applicable to all "
                "Permitted Payment Stablecoin Issuers. The rules, if finalized as proposed, will "
                "establish the first comprehensive federal licensing framework for payment stablecoins "
                "in the United States — with 47 organizations including Visa, JPMorgan, and Coinbase "
                "already having submitted formal comments."
            ),
            "why": [
                "Multi-agency rulemaking simultaneously on licensing, prudential standards, and AML/CFT means stablecoin issuers face a layered compliance build-out, not a single checkbox — raising costs and entry barriers.",
                "The GENIUS Act explicitly prohibits payment stablecoins from paying interest, narrowing the economic model toward pure payment-utility use cases rather than yield-bearing instruments.",
                "Visa and JPMorgan's formal engagement in the comment process signals that major incumbent payment rails view stablecoin regulation as strategically material — not marginal.",
                "Circle's CPN (already at $8.3B annualized volume) and Coinbase's USDC positioning stand to benefit most from a clear federal framework; unregulated offshore issuers face competitive disadvantage.",
                "European central banks filing as informal observers signals international concern about dollar-stablecoin dominance in cross-border payment corridors.",
            ],
            "region": "United States / Global",
            "players": "OCC, FDIC, FinCEN, OFAC, Circle, Coinbase, Visa, JPMorgan, stablecoin issuers",
            "tag": "Regulation / Stablecoins",
            "novelty": "Escalation — multi-agency rulemaking now active",
        },
        {
            "num": "4.",
            "headline": "UK Payments Forward Plan: Commercial VRP Goes Live; Future Entity Selection Imminent",
            "what": (
                "The UK's Payment Systems Regulator and FCA confirmed that the first live commercial "
                "Variable Recurring Payments (cVRP) transactions have processed under the "
                "industry-led UK Payments Initiative (UKPI) scheme, with initial use cases covering "
                "utility payments, financial services, and government payments. Separately, the "
                "UK's Payments Forward Plan (published February 2026) sets a Q3 2026 timeline for "
                "the FCA to consult on the long-term open banking interface regulatory framework, "
                "and for industry to select the 'Future Entity' central standards body that will "
                "govern Open Banking going forward. The PSR's proposed consolidation into the FCA "
                "remains subject to primary legislation."
            ),
            "why": [
                "cVRP going live transforms the UK from open banking infrastructure buildout to active commercial deployment — the payment volume ramp now begins in earnest.",
                "cVRP in utility and government use cases creates the recurring-payment beachhead that enables A2A to challenge direct debit dominance in the UK's highest-volume payment category.",
                "The Future Entity selection will determine the governance model, commercial framework, and API standards for UK open banking through to 2030 — a consequential decision for every bank and fintech operating in the market.",
                "PSR/FCA consolidation, if legislated, would materially restructure UK payments oversight, removing a dedicated regulator and raising questions about prioritisation within a broader FCA mandate.",
            ],
            "region": "United Kingdom",
            "players": "PSR, FCA, HM Treasury, UKPI member banks, UK fintechs, open banking TPPs",
            "tag": "Open Finance / A2A / Regulation",
            "novelty": "Escalation — cVRP transactions now live",
        },
        {
            "num": "5.",
            "headline": "Mastercard Explores Divestiture of Nets RTP Unit; Pivots Capital Toward Stablecoin Infrastructure",
            "what": (
                "Mastercard has engaged investment bankers to manage the potential sale of its "
                "real-time payments business acquired from Denmark's Nets Group in 2019 for $3.2 "
                "billion. The unit generates approximately $370 million in annual revenue and "
                "~$100 million in EBITDA — implying significant value erosion from the acquisition "
                "price. Private equity firms are reported as the primary likely bidders. "
                "The divestiture is expected to free capital to accelerate Mastercard's stablecoin "
                "strategy, including the anticipated acquisition of BVNK, a stablecoin infrastructure "
                "provider, at a reported valuation of up to $1.8 billion."
            ),
            "why": [
                "Mastercard's willingness to take a loss on a $3.2B RTP acquisition signals that owning instant payment processing infrastructure in regulated European markets is no longer strategically compelling at scale.",
                "The capital reallocation toward BVNK and stablecoin infrastructure reveals how card networks are repositioning: away from owning domestic rails, toward controlling the settlement and token layer of next-generation payment corridors.",
                "This is a direct signal to other card networks, PSPs, and banks: the competitive moat in payments is shifting from rail ownership toward orchestration, digital money issuance, and global settlement capability.",
                "A private equity acquisition of the Nets RTP unit creates a new category of dedicated RTP infrastructure operator, potentially more aggressive on commercial terms and geographic expansion.",
            ],
            "region": "Europe / Global",
            "players": "Mastercard, Nets Group, BVNK, potential PE acquirers, European RTP operators",
            "tag": "M&A / Market Structure",
            "novelty": "Follow-up with material update",
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
            "headline": "Circle CPN + Nium: USDC Settlement Connected to 190-Country Payout Network",
            "what": (
                "Circle announced a partnership with Nium, the real-time cross-border payments "
                "infrastructure provider, to connect Circle's CPN Managed Payments stablecoin "
                "settlement infrastructure with Nium's payout rails spanning more than 190 "
                "countries. CPN Managed Payments — launched April 8, 2026 — allows banks, "
                "fintechs, and PSPs to settle in USDC without directly managing digital assets; "
                "the Nium integration adds local currency delivery as the final mile. CPN has "
                "reached $8.3 billion in annualized transaction volume as of March 2026."
            ),
            "why": (
                "The Circle-Nium integration creates a practical stablecoin-to-fiat corridor "
                "that removes the two primary barriers to institutional stablecoin adoption: "
                "direct crypto custody and last-mile local currency payout. For banks and PSPs "
                "competing in cross-border corridors, this is a live alternative settlement "
                "layer with real volume, not a whitepaper. The $8.3B annualized run rate "
                "signals this is moving beyond early adopters into commercial consideration."
            ),
            "strategic": "Stablecoin-based cross-border settlement is transitioning from proof-of-concept to a credible institutional commercial option, reaching scale that demands a strategic response from traditional PSPs.",
        },
        {
            "num": "2.",
            "headline": "MAS Project MindForge Phase 2: AI Risk Toolkit for Financial Services Published",
            "what": (
                "MAS concluded Phase 2 of Project MindForge and published an AI Risk Management "
                "Toolkit for the financial services sector. The initiative, developed in "
                "collaboration with Singapore's Government Technology Agency and the Singapore "
                "Police Force, applies AI and machine learning techniques specifically to "
                "scam detection and financial crime prevention across the banking sector. "
                "MAS also issued guidance calling for industry-wide upskilling in AI capabilities "
                "via the Institute of Banking and Finance."
            ),
            "why": (
                "AI-driven fraud and scam detection is becoming a regulatory expectation, not "
                "just an operational choice — MAS is setting the toolkit standard that regulated "
                "institutions will be expected to align to. For payment platforms and banks "
                "operating in Singapore, MindForge output represents a de facto compliance "
                "framework for AI use in financial crime prevention, with direct implications "
                "for vendor selection, model governance, and audit readiness."
            ),
            "strategic": "MAS is establishing AI-driven financial crime prevention as a regulated discipline — Singapore-based payment firms must align their fraud and AML AI governance to the MindForge framework.",
        },
        {
            "num": "3.",
            "headline": "U.S. RTP Network: $480B Processed in Q1 2026 Alone as Instant Payments Enter High-Growth Phase",
            "what": (
                "The Clearing House's RTP Network processed 128 million transactions totalling "
                "$480 billion in Q1 2026 — equivalent to a $1.9 trillion annualised run rate. "
                "Combined FedNow and RTP volume exceeded $2 trillion in all of 2025, with "
                "58% of U.S. banks enabling instant payments now operating on both networks. "
                "FedNow's per-payment limit was raised to $10 million in November 2025, "
                "enabling high-value treasury and B2B use cases. Over 2,700 financial "
                "institutions now participate across both networks."
            ),
            "why": (
                "U.S. RTP volumes are confirming a structural transition from early adoption "
                "to mainstream usage. The $10M limit expansion unlocks B2B and treasury use "
                "cases that represent far larger transaction value than consumer P2P — the "
                "next volume phase will be driven by enterprise, not retail, adoption. For "
                "fintechs and banks globally, U.S. RTP maturity raises the baseline "
                "expectation for instant settlement capability in any payment product."
            ),
            "strategic": "The U.S. instant payment market is no longer nascent — enterprise adoption, multi-rail participation, and high-value limits are creating a deep domestic RTP ecosystem that will increasingly inform cross-border connectivity requirements.",
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
            "▶  Multilateral instant payment infrastructure is now in live-build mode — the 2027 horizon is real.",
            "Project Nexus moving into Technical Operator tender phase, with Indonesia as the sixth country, "
            "is not incremental news — it is the transition from architecture to operational reality. The "
            "ASEAN + India corridor set now covered by Nexus represents a significant portion of global "
            "remittance value and a direct competitive threat to correspondent banking, card-network "
            "remittance products, and specialist cross-border PSPs. The competitive advantage window for "
            "early-mover connectivity is 12-24 months."
        ),
        (
            "▶  Stablecoin regulation is moving from political to operational — the compliance clock is running.",
            "The GENIUS Act's multi-agency NPRMs mean stablecoin issuers and the banks that integrate them "
            "now face real licensing timelines, capital requirements, and AML program obligations. Circle's "
            "CPN at $8.3B annualized volume — backed by a live Nium integration for fiat delivery — shows "
            "that compliant stablecoin infrastructure is already in commercial use at scale. The question "
            "for every payment product leader is no longer whether stablecoin settlement is credible, but "
            "how to respond strategically."
        ),
        (
            "▶  A2A and open banking are past the inflection point — cVRP live in the UK, SPaN governing Singapore.",
            "The UK's first live cVRP transactions and Singapore's SPaN consolidation both represent "
            "governance and commercial infrastructure reaching maturity, not just regulatory aspiration. "
            "The practical implication: A2A is no longer a 'future threat' to card rails in high-priority "
            "markets — it is a present-tense alternative in recurring and government payment categories. "
            "Product strategies that treat A2A as a secondary consideration now carry material risk of "
            "being wrong-footed as volume ramps."
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
            "1.  Begin Nexus technical readiness assessment now — the Technical Operator tender sets your integration clock.",
            "The selection of the Nexus Technical Operator will establish API specifications, "
            "connectivity timelines, and participant onboarding requirements for all six corridor markets. "
            "PSPs and banks with material exposure to Singapore-India, Singapore-Indonesia, or "
            "ASEAN remittance corridors should immediately: (a) map current FX liquidity positions "
            "against Nexus corridor requirements; (b) identify ISO 20022 compliance gaps for "
            "Nexus messaging; (c) begin internal advocacy for budget allocation to Nexus "
            "integration in 2027 planning cycles. The mid-2027 live timeline is closer than "
            "annual planning horizons typically accommodate."
        ),
        (
            "2.  Develop a deliberate stablecoin settlement strategy before GENIUS Act final rules crystallize.",
            "With Circle CPN at $8.3B annualized volume and multi-agency rulemaking now active, "
            "the window to engage stablecoin settlement as a strategic option — rather than a "
            "reactive compliance response — is narrowing. Product leaders should assess: "
            "where stablecoin settlement (via CPN-style managed models) could outperform "
            "correspondent banking on cost and speed for specific corridors; how GENIUS Act "
            "licensing requirements affect your current or planned stablecoin integrations; "
            "and whether your cross-border product roadmap treats stablecoin as a threat, "
            "a complement, or an opportunity. A neutral position is increasingly indefensible."
        ),
        (
            "3.  Monitor Mastercard's Nets divestiture for what it reveals about RTP infrastructure economics.",
            "A major card network selling a $3.2B RTP acquisition at a loss to fund a $1.8B "
            "stablecoin acquisition is a strategic signal of the highest order. Track: "
            "who acquires the Nets RTP unit and on what commercial terms (this will set "
            "market pricing for standalone RTP infrastructure businesses); whether other "
            "card networks follow with similar divestitures; and how BVNK's capabilities "
            "shape Mastercard's cross-border stablecoin settlement offering. The M&A activity "
            "here is revealing where major players believe the durable value pools in payments "
            "will accrue over the next decade."
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
            "●  Nexus Technical Operator selection — H2 2026.",
            "The firm contracted to build and operate Nexus infrastructure will define the API "
            "standards, commercial participation model, and security architecture for the world's "
            "first multilateral instant cross-border payment network. Likely candidates include "
            "global payment technology vendors and infrastructure specialists. The selection "
            "announcement will be the single most important milestone in cross-border payment "
            "infrastructure for 2026 — watch the tender outcome closely."
        ),
        (
            "●  UK Future Entity for Open Banking — selection expected Q3 2026.",
            "The body selected to succeed the Open Banking Implementation Entity (OBIE) as "
            "the central standards-setter for UK open banking will shape cVRP commercial "
            "rollout, data sharing rules, and A2A payment governance through to 2030. "
            "Multiple consortia are expected to bid; the governance model chosen will "
            "directly influence how quickly cVRP can scale beyond the initial phase-1 use "
            "cases into e-commerce, travel, and B2B payment categories."
        ),
        (
            "●  GENIUS Act final rules and first licensed payment stablecoin issuers — Q4 2026.",
            "OCC, FDIC, and FinCEN comment periods are closing through Q2 2026, with final "
            "rules expected by Q3-Q4. The issuance of the first federal licenses for Permitted "
            "Payment Stablecoin Issuers will be a foundational market structure event — "
            "determining which entities can issue, which banks can integrate, and what "
            "compliance architecture the entire stablecoin payment ecosystem must conform to. "
            "Watch also for whether the EU's MiCA framework and the UK's stablecoin regime "
            "converge or diverge from the GENIUS Act approach."
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
        "regulatory releases, scheme operator announcements, and reputable financial media. "
        "It is intended for informational purposes only and does not constitute investment, legal, "
        "or regulatory advice. Key sources: BIS (bis.org), MAS (mas.gov.sg), Federal Register "
        "(federalregister.gov), OCC (occ.treas.gov), FDIC (fdic.gov), Treasury (home.treasury.gov), "
        "PSR/FCA (psr.org.uk), HM Treasury (gov.uk), PYMNTS, Fintech Futures, The Asian Banker, "
        "Global Government Fintech, Electronic Payments International, The Fintech Times, "
        "Fintech News Singapore, Red Compass Labs, Northey Point, Brookings Institution.",
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
