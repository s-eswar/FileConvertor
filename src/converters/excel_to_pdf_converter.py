from src.converters.base_converter import BaseConverter
from src.utils.excel_ops import read_excel_file, save_csv
from src.utils.pdf_utils import generate_pdf
from src.utils.pdf_generator.generator import export_dataframe_to_pdf
import logging
import os

class ExcelToPDFConverter(BaseConverter):
    def convert(self, excel_file, column_name, output_folder="pdfs", sheet_name="Sheet1", title="BINARY DATA"):
        try:
            os.makedirs(output_folder, exist_ok=True)
            df = read_excel_file(excel_file, sheet_name)
            if column_name not in df.columns:
                logging.error(f"Column '{column_name}' not found in the Excel file.")
                return

            unique_values = df[column_name].unique()
            for value in unique_values:
                filtered_df = df[df[column_name] == value]
                filtered_df["S.No."] = range(1, len(filtered_df) + 1)
                save_csv(filtered_df, output_folder="csvs", file_name=f"{value}_{len(filtered_df)}.csv")
                # data = [filtered_df.columns.tolist()] + filtered_df.values.tolist()
                # generate_pdf(data, output_folder, f"{value}_{len(filtered_df)}.pdf", title)
                export_dataframe_to_pdf(filtered_df, output_folder + f"/{value}_{len(filtered_df)}.pdf", title)
        except Exception as e:
            logging.error(f"An error occurred: {e}")