import pandas as pd
from reportlab.platypus import Paragraph, Table, TableStyle
from src.utils.pdf_generator.config import get_pdf_styles, COLOR_PRIMARY, COLOR_ALT_ROW, COLOR_GRID, COLOR_BOX, colors


def build_pdf_table(df: pd.DataFrame, available_width: float) -> Table:
    """
    Converts a pandas DataFrame into a formatted ReportLab Table with
    custom column widths (narrow S.No, expanded owner/district) and centered alignment.
    """
    title_style, c_head, c_cell, l_head, l_cell = get_pdf_styles()

    header_row = []
    data_rows = []

    # Map column names to custom widths (in points) and alignments
    # Automatically detects typical column naming patterns
    for col in df.columns:
        col_lower = str(col).lower()
        if any(k in col_lower for k in ['sno', 's.no', 'id', 'no']):
            header_row.append(Paragraph(str(col), c_head))
        else:
            header_row.append(Paragraph(str(col), l_head))

    for _, row in df.iterrows():
        row_cells = []
        for col_name, val in zip(df.columns, row):
            val_str = str(val) if pd.notna(val) else ""
            col_lower = str(col_name).lower()

            # Center small code/ID/S.No columns; left align names/districts
            if any(k in col_lower for k in ['sno', 's.no', 'id', 'no']):
                row_cells.append(Paragraph(val_str, c_cell))
            else:
                row_cells.append(Paragraph(val_str, l_cell))
        data_rows.append(row_cells)

    table_data = [header_row] + data_rows

    # --- CUSTOM COLUMN WIDTH DISTRIBUTION ---
    # Give S.No / ID a narrow width (~40pt) and distribute remaining width
    # heavily to 'owner_name' and 'district' columns.
    num_cols = len(df.columns)
    col_widths = []

    for col in df.columns:
        col_lower = str(col).lower()
        if any(k in col_lower for k in ['sno', 's.no', 'id', 'no']):
            col_widths.append(45)  # Narrow width for Serial Number / ID
        elif any(k in col_lower for k in ['owner', 'district', 'name', 'address', 'description']):
            col_widths.append(available_width * 0.32)  # Expanded width for text-heavy columns
        else:
            col_widths.append(available_width * 0.26)  # Standard width for other columns

    # Normalize widths to exactly match available_width if proportions exceed
    total_calculated = sum(col_widths)
    if total_calculated > 0:
        col_widths = [w * (available_width / total_calculated) for w in col_widths]

    # Construct Table
    pdf_table = Table(table_data, colWidths=col_widths, repeatRows=1)

    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),

        # Row padding
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),

        # Grid lines & alternating colors
        ('INNERGRID', (0, 0), (-1, -1), 0.5, COLOR_GRID),
        ('BOX', (0, 0), (-1, -1), 1, COLOR_BOX),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COLOR_ALT_ROW]),
    ])

    pdf_table.setStyle(table_style)
    return pdf_table