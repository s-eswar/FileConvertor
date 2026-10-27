from src.converters.base_converter import BaseConverter
from fpdf import FPDF
import os
import logging

class WordToPDFConverter(BaseConverter):
    def convert(self, word_file, output_folder="pdfs"):
        try:
            # Example implementation for Word to PDF conversion
            from docx import Document
            doc = Document(word_file)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            for paragraph in doc.paragraphs:
                pdf.multi_cell(0, 10, paragraph.text)

            os.makedirs(output_folder, exist_ok=True)
            pdf_path = os.path.join(output_folder, os.path.basename(word_file).replace(".docx", ".pdf"))
            pdf.output(pdf_path)
            logging.info(f"PDF created: {pdf_path}")
        except Exception as e:
            logging.error(f"Error converting Word to PDF: {e}")