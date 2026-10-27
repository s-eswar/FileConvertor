from src.converters.excel_to_pdf_converter import ExcelToPDFConverter
from src.converters.word_to_pdf_converter import WordToPDFConverter

class ConverterFactory:
    @staticmethod
    def get_converter(converter_type):
        if converter_type == "excel_to_pdf":
            return ExcelToPDFConverter()
        elif converter_type == "word_to_pdf":
            return WordToPDFConverter()
        else:
            raise ValueError(f"Unknown converter type: {converter_type}")