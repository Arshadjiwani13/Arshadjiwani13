#!/usr/bin/env python3
"""Generate Daily Payments & Fintech Intelligence Brief PDF – May 28, 2026."""

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

DATE   = "May 28, 2026"
OUTPUT = "/home/user/Arshadjiwani13/Daily_Payments_Fintech_Brief_2026-05-28.pdf"
# See generate_briefing_2026-05-28.py for full source
