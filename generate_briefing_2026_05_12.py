#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief – May 12, 2026."""

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

DATE   = "May 12, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-12.pdf"

NAVY   = HexColor("#0F3782")
LBLUE  = HexColor("#4A90D9")
LGRAY  = HexColor("#F0F4FF")
MGRAY  = HexColor("#6E6E6E")
GREEN  = HexColor("#287840")
AMBER  = HexColor("#B05A00")
WHITE  = colors.white
BLACK  = colors.black
SILVER = HexColor("#DDDDDD")


def build_styles():
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
    novelty_color = AMBER if novelty.startswith("Escalation") else GREEN
    tag_para = Paragraph(
        f"<font color='white'><b> {tag} </b></font>",
        ParagraphStyle("tag", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE,
                       backColor=NAVY, leading=11, borderPadding=3))
    novelty_para = Paragraph(
        f"<font color='white'><b> {novelty} </b></font>",
        ParagraphStyle("nov", fontSize=8, fontName="Helvetica-Bold", textColor=WHITE,
                       backColor=novelty_color, leading=11, borderPadding=3))
    reg_para  = Paragraph(f"<b>Region:</b> {region}",
                          ParagraphStyle("reg",  fontSize=8, fontName="Helvetica",
                                         textColor=HexColor("#333333"), leading=11))
    play_para = Paragraph(f"<b>Players:</b> {players}",
                          ParagraphStyle("play", fontSize=8, fontName="Helvetica",
                                         textColor=HexColor("#333333"), leading=11))
    tbl = Table(
        [[tag_para, novelty_para, "", ""],
         [reg_para, "",          play_para, ""]],
        colWidths=[42*mm, 46*mm, 8*mm, 74*mm]
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

    # ── SECTION 1 — TOP PAYMENTS HEADLINES ────────────────────────────────────
    story.append(section_header("1.", "TOP PAYMENTS HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    headlines = [
        {
            "num": "1.",
            "headline": "UK FCA Supplementary Safeguarding Regime Now Live — Payment & E-Money Firms Enter New Compliance Era",
            "what": (
                "The FCA's Supplementary Safeguarding Regime (Policy Statement PS25/12) came into force "
                "on 7 May 2026, introducing materially strengthened rules for all UK-regulated payment "
                "institutions and e-money institutions. Effective immediately, firms must perform daily "
                "reconciliations on every reconciliation day (excluding weekends and bank holidays), "
                "maintain a resolution pack, segregate e-money and payment service funds separately, "
                "and file new monthly returns covering safeguarding methods, amounts held, shortfalls, "
                "and breaches. An annual safeguarding audit is mandatory for firms holding over "
                "GBP 100,000 in safeguarded funds over any rolling 53-week period."
            ),
            "why": [
                "This is the most significant structural reform to UK payment firm safeguarding since the Payment Services Regulations 2017 — raising the baseline consumer protection floor across the entire sector.",
                "Monthly regulatory returns create a new data-driven supervisory relationship with the FCA; firms with weak reconciliation or reporting infrastructure face immediate compliance risk.",
                "The separate segregation requirement for e-money versus payment service funds forces operational model changes at multi-product payment firms.",
                "A second Post-Repeal Regime (full statutory trust framework) follows once HM Treasury revokes the PSRs and EMRs — firms must plan for continuous regulatory evolution, not a one-time uplift.",
                "Non-UK EU firms with UK passporting or reverse solicitation exposure must assess whether equivalent safeguarding coverage exists under their home-country frameworks.",
            ],
            "region": "UK",
            "players": "FCA, UK payment institutions, e-money institutions, BaaS providers, neobanks",
            "tag": "Regulation",
            "novelty": "Escalation — regime now active",
        },
        {
            "num": "2.",
            "headline": "SWIFT November 2026 Structured Address Deadline: Only 35% Compliant — Six Months to Hard Stop",
            "what": (
                "SWIFT has confirmed that from November 2026, cross-border CBPR+ payment messages "
                "containing unstructured postal addresses will be rejected outright — not translated or "
                "repaired. With approximately 65% of payment messages still carrying unstructured "
                "address data as of Q1 2026, the industry faces a critical and compressing compliance "
                "gap. SWIFT has made its AI-based open-source address structuring model freely "
                "available to accelerate remediation. Fully structured or hybrid postal addresses "
                "will be the only accepted format from November 2026 for all agents and parties in "
                "CBPR+ instructions."
            ),
            "why": [
                "A 65% non-compliance rate six months before a hard rejection deadline is a systemic risk signal — payment message failure rates could spike materially in Q4 2026 if institutions do not act now.",
                "This is not a cosmetic formatting change: structured address data directly enables higher-precision AML/sanctions screening and significantly reduces false positives in automated compliance filters.",
                "Correspondent banks with large corporate client portfolios face the heaviest remediation burden — client data enrichment programs must begin immediately to avoid downstream message rejection.",
                "SWIFT's free AI address structuring model lowers the technical barrier, but the operational challenge is data sourcing and client instruction updates at scale.",
                "November 2026 is also the final lever in SWIFT's escalating pricing pressure strategy that began with coexistence-period surcharges in January 2026.",
            ],
            "region": "Global",
            "players": "SWIFT, correspondent banks, corporate treasuries, TMS/ERP vendors, compliance technology providers",
            "tag": "Infrastructure / Regulation",
            "novelty": "Escalation — 6-month hard deadline",
        },
        {
            "num": "3.",
            "headline": "OCC Issues Proposed Rules Under GENIUS Act — US Stablecoin Framework Enters Implementation Phase",
            "what": (
                "The US Office of the Comptroller of the Currency (OCC) has published a Notice of "
                "Proposed Rulemaking (Bulletin 2026-3) implementing the requirements of the GENIUS Act "
                "(signed into law July 18, 2025) for non-bank payment stablecoin issuers. The proposed "
                "rules address reserve requirements, audit and attestation standards, custody "
                "arrangements, and the federal licensing pathway for non-bank issuers seeking "
                "OCC-supervised 'Federal Qualified Payment Stablecoin Issuer' status. A separate "
                "rulemaking covering BSA/AML and OFAC sanctions compliance obligations will follow "
                "in coordination with the US Treasury Department. Regulators are required to "
                "promulgate final rules by July 2026, with full GENIUS Act compliance mandatory "
                "by January 2027."
            ),
            "why": [
                "The GENIUS Act ends regulatory ambiguity for US payment stablecoins — creating a dual federal/state licensing framework that defines which entities can legally issue stablecoins at scale.",
                "OCC's proposed rules set the 100% reserve and audit standards that will determine whether major stablecoin issuers can serve regulated financial institutions as payment counterparties.",
                "Banks and non-bank issuers must now make strategic decisions about charter type, reserve composition, and custody arrangements — with real capital and operational implications.",
                "The BSA/AML rulemaking gap (coming separately) is a material uncertainty: stablecoin issuers cannot fully assess compliance cost structures until those rules are finalized.",
                "Global implications: EU MiCA, Singapore MAS, UAE CBUAE, and UK FCA frameworks will each benchmark against the US GENIUS Act standard for cross-border stablecoin interoperability.",
            ],
            "region": "United States",
            "players": "OCC, US Treasury, Federal Reserve, stablecoin issuers, banks, non-bank payment stablecoin issuers",
            "tag": "Stablecoins / Regulation",
            "novelty": "New today",
        },
        {
            "num": "4.",
            "headline": "Project Nexus: Indonesia Joins — Multilateral Cross-Border IPS Network Now Spans Six Countries",
            "what": (
                "Bank Indonesia has formally joined the BIS Project Nexus multilateral cross-border "
                "instant payment framework, expanding the network to six founding countries: India, "
                "Malaysia, the Philippines, Singapore, Thailand, and now Indonesia. Nexus Global "
                "Payments (NGP), incorporated in Singapore in late 2025, is progressing through live "
                "implementation planning, with technical integration and commercial framework "
                "development underway across connected instant payment systems (IPS). The scheme "
                "targets sub-60-second settlement via ISO 20022 API connectivity, serving a "
                "combined population exceeding 2 billion people across its six-country footprint."
            ),
            "why": [
                "Indonesia's inclusion adds the fourth-largest population and a major remittance-sending and -receiving economy — materially increasing the commercial addressable market for Nexus corridors.",
                "Unlike bilateral linkages, Nexus creates a single-connection hub enabling any-to-any corridor access; Indonesia's addition benefits all five existing members simultaneously.",
                "PSPs in India-Indonesia, Philippines-Indonesia, and Malaysia-Indonesia corridors — currently served by expensive correspondent banking or card rails — face the highest near-term disruption.",
                "The ISO 20022 / API architecture makes Nexus natively compatible with MAS's open finance data standards and SWIFT CBPR+ — positioning it as a sustainable long-term infrastructure play.",
                "Singapore's dual role as NGP's incorporation jurisdiction and MAS's participation reinforces its position as the central node of Asia-Pacific payment infrastructure governance.",
            ],
            "region": "Asia-Pacific / Singapore",
            "players": "BIS, Bank Indonesia, MAS, RBI, Bank Negara Malaysia, BSP Philippines, Bank of Thailand, NGP",
            "tag": "RTP / Cross-Border / Infrastructure",
            "novelty": "New today",
        },
        {
            "num": "5.",
            "headline": "Singapore Payments Network (SPaN) Advances Toward End-2026 Operational Readiness",
            "what": (
                "Singapore Payments Network (SPaN), the new not-for-profit entity established jointly "
                "by MAS and the Association of Banks in Singapore (ABS) to govern all eight national "
                "payment schemes (FAST, GIRO, PayNow, SGQR, and others), is advancing toward its "
                "target operational readiness date of end-2026. SPaN's 11-member board — comprising "
                "two MAS representatives, five financial institution directors, and four independent "
                "directors — is completing the onboarding of direct participants and the formal "
                "handover of scheme governance from existing administrators. Founding members include "
                "Citibank, DBS, HSBC, Maybank, OCBC, Standard Chartered, and UOB."
            ),
            "why": [
                "Consolidating governance of eight national payment schemes under one entity eliminates fragmentation risk and creates a single accountable body for Singapore's payment infrastructure — a structural upgrade from the current multi-administrator model.",
                "SPaN positions Singapore to make faster, more coordinated decisions on domestic scheme evolution — including PayNow enhancements, cross-border linkage governance, and resilience standards.",
                "As Project Nexus advances, SPaN becomes the de facto governance counterparty for Singapore's participation — a critical linkage between domestic and international infrastructure.",
                "The not-for-profit model and MAS co-governance structure provides regulatory legitimacy while keeping commercial participation incentives for member banks.",
                "End-2026 operational readiness creates a governance milestone that will define Singapore's payment infrastructure trajectory into 2027 and beyond.",
            ],
            "region": "Singapore",
            "players": "MAS, ABS, SPaN, DBS, OCBC, UOB, HSBC, Standard Chartered, Citibank, Maybank",
            "tag": "Market Structure / Infrastructure",
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

    # ── SECTION 2 — MAJOR FINTECH HEADLINES ───────────────────────────────────
    story.append(PageBreak())
    story.append(section_header("2.", "MAJOR FINTECH HEADLINES", s))
    story.append(Spacer(1, 3*mm))

    fintech = [
        {
            "num": "1.",
            "headline": "ECB Calls for Function-Based Stablecoin Regulation — Separates Instrument Logic from Use-Case Logic",
            "what": (
                "On May 8, 2026, an ECB Executive Board member delivered a keynote arguing that "
                "stablecoin regulation must separate the function of the instrument (store of value, "
                "means of payment, unit of account) from the instrument itself. The ECB's position "
                "contrasts with MiCA's asset-class approach and aligns conceptually with MAS's PFMI "
                "framework call — both central banks are signalling that payment-scale stablecoins "
                "should be regulated as financial market infrastructure, not simply as crypto assets. "
                "The ECB also flagged risks from dollar-denominated stablecoins displacing euro-area "
                "payment instruments."
            ),
            "why": (
                "The ECB's function-based framework represents a significant intellectual shift that "
                "could reshape post-MiCA stablecoin regulation in Europe — particularly as the "
                "GENIUS Act creates US-domiciled payment stablecoins at scale. If large-cap "
                "USD-denominated stablecoins gain EU payment traction, the ECB's concern about "
                "monetary sovereignty becomes a live policy driver, potentially accelerating the "
                "digital euro as a payment instrument. For banks and PSPs building stablecoin "
                "overlays, the divergence between ECB/MAS (function-based) and current MiCA "
                "(instrument-based) creates regulatory arbitrage risk that must be monitored closely."
            ),
            "strategic": "ECB's function-based stance, if adopted, would impose FMI-level obligations on payment-scale stablecoins across Europe — fundamentally changing the cost structure of stablecoin payment services.",
        },
        {
            "num": "2.",
            "headline": "Singapore Fintech Funding Reaches US$319M in State-of-Play 2026 Report — Payments Dominates",
            "what": (
                "The Singapore Fintech Association's State of Play 2026 report confirms Singapore as "
                "the leading ASEAN fintech hub with US$319 million in fintech funding in the measured "
                "period, with payments infrastructure accounting for the largest share of deals. "
                "Growth is concentrated in B2B payments tooling, cross-border infrastructure, and "
                "compliance technology rather than consumer neobanking. Digital wallet transaction "
                "volumes are projected to reach SGD 89 billion by 2027, with PayNow and GrabPay "
                "maintaining dominant domestic positions."
            ),
            "why": (
                "The concentration of funding in payments infrastructure — not consumer distribution — "
                "confirms that the value-capture layer in Singapore fintech has shifted to "
                "middleware, orchestration, and compliance tooling. This structural pattern aligns "
                "with SPaN's governance ambitions and MAS's Project Nexus positioning: Singapore is "
                "building a payments infrastructure export model, not just a domestic fintech market. "
                "For product leaders, this signals that Singapore-based payments infrastructure "
                "investments are likely to attract disproportionate regulatory support and "
                "institutional partnership interest through 2027."
            ),
            "strategic": "Singapore's funding concentration in payments infrastructure reinforces its role as Asia-Pacific's payments technology hub — with ecosystem effects that extend through Nexus and SPaN into regional corridors.",
        },
        {
            "num": "3.",
            "headline": "UAE FIT Programme — 2026 Full Integration Target Year Active Across All Nine Initiatives",
            "what": (
                "The CBUAE's Financial Infrastructure Transformation (FIT) Programme — a nine-initiative "
                "digital transformation roadmap launched in 2023 — has 2026 as its full integration "
                "target year. Key 2026 milestones include: the retail Digital Dirham (CBDC) pilot "
                "expansion with potential retail launch; the Jisr cross-border CBDC payment platform "
                "adding new central bank participants beyond China; a domestic card scheme launch; "
                "open finance framework implementation; and enhanced AML/CFT technology integration "
                "across UAE payment infrastructure."
            ),
            "why": (
                "The UAE is executing the most comprehensive payment infrastructure modernization "
                "program in the GCC — simultaneously advancing CBDC, open finance, domestic card "
                "rails, and cross-border payment integration within a single coordinated regulatory "
                "program. For banks and PSPs operating in the UAE, 2026 is the year when FIT "
                "Programme requirements shift from planning to live compliance. The Jisr platform's "
                "expansion beyond the China corridor creates new opportunities for cross-border "
                "payment providers in the UAE as additional central bank participants join."
            ),
            "strategic": "The UAE's FIT Programme convergence in 2026 creates simultaneous demand for CBDC integration, open finance API readiness, and cross-border payment connectivity — making it one of the most complex and opportunity-rich payment markets globally.",
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

    # ── SECTION 3 — WHAT MATTERS MOST ─────────────────────────────────────────
    story.append(section_header("3.", "WHAT MATTERS MOST", s))
    story.append(Spacer(1, 3*mm))

    themes = [
        (
            "▶  Regulatory perimeters are hardening simultaneously across the UK, US, EU, UAE, and Singapore.",
            "Five jurisdictions are in active implementation of major payment regulation simultaneously: the UK "
            "FCA safeguarding regime (live), the US GENIUS Act (OCC rules proposed), EU MiCA full compliance "
            "(mid-2026), UAE FIT Programme (full integration target), and Singapore SPaN governance "
            "consolidation (end-2026). For global payment platforms operating across these markets, "
            "regulatory change is no longer sequential — it is concurrent and compressing. Compliance "
            "infrastructure investment must keep pace with this convergence or face fragmented, "
            "jurisdiction-specific operational models."
        ),
        (
            "▶  The stablecoin regulatory framework is fracturing along function vs. instrument lines — "
            "with major payment consequences.",
            "The ECB's function-based stance, MAS's PFMI-standard call, and the US GENIUS Act's "
            "instrument-specific approach are creating three distinct regulatory philosophies for "
            "payment stablecoins. As USD-denominated stablecoins scale under GENIUS Act authorisation, "
            "ECB and MAS concerns about monetary sovereignty become live policy drivers. The practical "
            "implication: stablecoins that achieve payment-scale adoption may face retrospective "
            "FMI-level regulatory requirements — materially raising operating costs and compliance "
            "obligations beyond what current licensing frameworks anticipate."
        ),
        (
            "▶  Asia-Pacific is building the most interconnected real-time cross-border payment "
            "infrastructure in the world.",
            "Project Nexus with six countries (now including Indonesia), Singapore's SPaN governance "
            "body, MAS's Project Nexus co-anchoring, and Singapore's dominant fintech funding position "
            "combine to create a structurally interconnected real-time payments ecosystem that is more "
            "advanced than any comparable initiative in the US or EU. The 2027 live implementation "
            "horizon for Nexus is tighter than most payment leaders appreciate. PSPs, banks, and "
            "corporate treasurers with ASEAN corridor exposure must begin technical and commercial "
            "preparation now."
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
            "1.  If your firm operates in the UK, validate FCA safeguarding compliance immediately — "
            "the regime is live.",
            "The FCA's May 7 effective date is not a future planning item — it is a current "
            "compliance requirement. The new monthly returns, daily reconciliation obligations, and "
            "resolution pack requirements are in force now. Firms that have not completed their "
            "safeguarding model review, books-and-records uplift, and FCA reporting system integration "
            "face immediate regulatory exposure. Prioritise a gap assessment against PS25/12 "
            "requirements before end of May. The Post-Repeal Regime (full statutory trust) is coming "
            "next — treat this as phase one of a multi-year transformation, not a one-time fix."
        ),
        (
            "2.  Treat the November 2026 SWIFT structured address deadline as a data product program, "
            "not a technical migration.",
            "With 65% of messages still non-compliant and six months until hard rejection, the "
            "structured address deadline is the most pressing data quality risk in cross-border "
            "payments today. The technical fix (SWIFT's free AI structuring model) exists; the "
            "operational challenge is sourcing complete, accurate address data from clients and "
            "enriching legacy payment templates at scale. Build this as a data enrichment product "
            "program with a client outreach component — the downstream payoff in reduced AML "
            "false positives and higher STP rates compounds the compliance argument into a "
            "business case."
        ),
        (
            "3.  Begin Project Nexus readiness planning for ASEAN corridors now — the 2027 live "
            "window is closer than it appears.",
            "With Indonesia's addition to Nexus, six of ASEAN's largest economies are now inside "
            "the multilateral instant payment network. The ISO 20022 API architecture and sub-60-second "
            "settlement target are defined; what remains is technical integration, FX liquidity "
            "framework design for Nexus corridors, and compliance architecture mapping across six "
            "jurisdictions. PSPs and banks with ASEAN remittance or corporate payment corridor "
            "exposure should begin vendor assessments, FX pre-funding strategy reviews, and "
            "compliance architecture design for the Nexus model now — first-mover readiness "
            "will be a durable competitive advantage in corridors where Nexus replaces legacy rails."
        ),
    ]

    for title, body in implications:
        block = []
        block.append(Paragraph(title, s["theme_title"]))
        block.append(Paragraph(body, s["body"]))
        block.append(Spacer(1, 2*mm))
        story.append(KeepTogether(block))

    # ── SECTION 5 — OPTIONAL WATCHLIST ────────────────────────────────────────
    story.append(section_header("5.", "OPTIONAL WATCHLIST — Watch Next", s))
    story.append(Spacer(1, 3*mm))

    watchlist = [
        (
            "●  OCC GENIUS Act BSA/AML rules — expected H2 2026.",
            "The OCC's proposed Bulletin 2026-3 explicitly defers BSA/AML and OFAC stablecoin "
            "compliance rules to a separate rulemaking with the US Treasury. This is the most "
            "consequential open question for payment stablecoin issuers — without knowing their "
            "AML obligations, they cannot fully model operating costs or design compliance "
            "architectures. Watch for Treasury-led consultation timing and scope, which will "
            "define the real cost structure of US-licensed payment stablecoin issuance."
        ),
        (
            "●  CBUAE Digital Dirham retail pilot expansion — Q2/Q3 2026.",
            "The UAE Central Bank is expected to expand the retail Digital Dirham (CBDC) pilot "
            "beyond the initial closed-loop phase during mid-2026, with a potential retail "
            "launch announcement before year-end. Watch for announcements on participating banks, "
            "wallet providers, and merchant integration — this would be the first retail CBDC "
            "live deployment in a major GCC economy and a template for other Gulf central banks."
        ),
        (
            "●  FCA Post-Repeal Regime for payment safeguarding — HM Treasury consultation timing.",
            "The FCA's Supplementary Regime (now live) is phase one; the Post-Repeal statutory "
            "trust framework is phase two, contingent on HM Treasury revoking the PSRs and EMRs. "
            "Watch for Treasury's consultation timeline on revocation, which will define the "
            "implementation window for the full statutory trust model. The statutory trust "
            "framework will require more fundamental changes to firm structures and insolvency "
            "arrangements than the Supplementary Regime alone."
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
        "This briefing is compiled from publicly available sources including central bank publications, "
        "regulatory releases, scheme operator announcements, and reputable financial industry media. "
        "It is intended for informational purposes only and does not constitute investment, legal, or "
        "regulatory advice. Key sources: FCA (fca.org.uk), SWIFT (swift.com), OCC (occ.treas.gov), "
        "BIS / Project Nexus (bis.org), MAS (mas.gov.sg), CBUAE (centralbank.ae), ECB (ecb.europa.eu), "
        "Norton Rose Fulbright, Gibson Dunn, Fintech Futures, Fintech Singapore, Global Government Fintech, "
        "The Payments Association, The Asian Banker, PYMNTS.",
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
