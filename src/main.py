import argparse
from src.converters.converter_factory import ConverterFactory
from src.utils.logging_utils import configure_logging
import logging

if __name__ == "__main__":
    configure_logging()
    parser = argparse.ArgumentParser(description="Convert files using various converters.")
    parser.add_argument("converter_type", help="Type of converter (e.g., 'excel_to_pdf', 'word_to_pdf').")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("--column_name", help="Column name for Excel to PDF conversion.")
    parser.add_argument("--output_folder", default="output", help="Folder to save the output files.")
    parser.add_argument("--sheet_name", default="Sheet1", help="Sheet name for Excel files.")
    parser.add_argument("--title", default="BINARY DATA", help="Title for the PDF header.")
    args = parser.parse_args()

    try:
        converter = ConverterFactory.get_converter(args.converter_type)
        if args.converter_type == "excel_to_pdf":
            converter.convert(args.input_file, args.column_name, args.output_folder, args.sheet_name, args.title)
        elif args.converter_type == "word_to_pdf":
            converter.convert(args.input_file, args.output_folder)
    except Exception as e:
        logging.error(f"An error occurred: {e}")