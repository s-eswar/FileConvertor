from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

DEFAULT_PAGE_SIZE = landscape(A4)
DEFAULT_MARGIN = 30

COLOR_PRIMARY = colors.HexColor("#1F2937")
COLOR_ALT_ROW = colors.HexColor("#F9FAFB")
COLOR_GRID = colors.HexColor("#E5E7EB")
COLOR_BOX = colors.HexColor("#9CA3AF")


def get_pdf_styles():
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=COLOR_PRIMARY,
        alignment=0
    )

    # Centered style for S.No or index columns
    center_header_style = ParagraphStyle(
        'CenterHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.whitesmoke,
        alignment=1  # Centered
    )

    center_cell_style = ParagraphStyle(
        'CenterCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=colors.black,
        alignment=1  # Centered
    )

    # Left-aligned style for text columns (Names, Districts, etc.)
    left_header_style = ParagraphStyle(
        'LeftHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.whitesmoke,
        alignment=0  # Left
    )

    left_cell_style = ParagraphStyle(
        'LeftCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=colors.black,
        alignment=0  # Left
    )

    return title_style, center_header_style, center_cell_style, left_header_style, left_cell_style