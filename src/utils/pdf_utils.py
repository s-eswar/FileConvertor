import os
from fpdf import FPDF
import logging

def generate_pdf(data, output_folder, file_name, title):
    """Generate a PDF from data with optimized execution."""
    try:
        os.makedirs(output_folder, exist_ok=True)
        pdf = FPDF(orientation='P', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=8)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.ln(5)

        # Precompute column widths
        page_width = pdf.w - 20  # Account for margins
        col_widths = [max(pdf.get_string_width(str(value)) for value in col) + 4 for col in zip(*data)]
        total_width = sum(col_widths)

        # Scale column widths to fit the page
        if total_width > page_width:
            scale_factor = page_width / total_width
            col_widths = [width * scale_factor for width in col_widths]

        # Render table header
        for i, col in enumerate(data[0]):
            pdf.cell(col_widths[i], 10, str(col), border=1, align='C')
        pdf.ln()

        # Render table rows
        for row in data[1:]:
            # Calculate the maximum height of the row
            max_row_height = 0
            cell_heights = []
            for i, cell in enumerate(row):
                x, y = pdf.get_x(), pdf.get_y()
                pdf.multi_cell(col_widths[i], 5, str(cell), border=0)
                cell_height = pdf.get_y() - y
                cell_heights.append(cell_height)
                max_row_height = max(max_row_height, cell_height)
                pdf.set_xy(x, y)  # Reset position after calculating height

            # Ensure max_row_height is not too small
            max_row_height = max(max_row_height, 10)

            # Render all cells in the row with the same height
            y_start = pdf.get_y()
            for i, cell in enumerate(row):
                pdf.set_xy(pdf.get_x() + sum(col_widths[:i]), y_start)
                pdf.multi_cell(col_widths[i], max_row_height / (max_row_height // 10), str(cell), border=1, align='L')
            pdf.ln(max_row_height)

        # Save the PDF
        pdf_path = os.path.join(output_folder, file_name)
        pdf.output(pdf_path)
        logging.info(f"PDF created: {pdf_path}")
    except Exception as e:
        logging.error(f"Error generating PDF '{file_name}': {e}")
        raise