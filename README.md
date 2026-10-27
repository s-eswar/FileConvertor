```markdown
# Excel to PDF/CSV Converter

This project converts Excel data into PDFs and CSVs grouped by a specific column. It is modularized with utility scripts for better maintainability and extensibility.

## Features
- Reads data from an Excel file.
- Groups data by a specified column.
- Saves grouped data as CSV files.
- Generates PDFs for grouped data with customizable layouts.
- Ensures proper formatting, including dynamic row heights, column widths, and padding for better readability.
- Handles large datasets efficiently.

## Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To convert an Excel file into PDFs and CSVs grouped by a specific column:

1. Run the `ExcelToPDFConverter` class:
   ```bash
   python src/converters/excel_to_pdf_converter.py
   ```

2. Provide the following parameters:
   - `excel_file`: Path to the Excel file.
   - `column_name`: Column name to group data by.
   - `output_folder`: (Optional) Folder to save the generated PDFs and CSVs. Default is `pdfs`.
   - `sheet_name`: (Optional) Sheet name in the Excel file. Default is `Sheet1`.
   - `title`: (Optional) Title for the generated PDFs. Default is `BINARY DATA`.

### Example
```python
from src.converters.excel_to_pdf_converter import ExcelToPDFConverter

converter = ExcelToPDFConverter()
converter.convert(
    excel_file="data.xlsx",
    column_name="district",
    output_folder="output",
    sheet_name="Sheet1",
    title="District Owner Allocation Report"
)
```

## Output
- **CSV Files**: Saved in the `csvs` folder (or specified output folder).
- **PDF Files**: Saved in the `pdfs` folder (or specified output folder) with proper formatting:
  - Dynamic row heights based on content.
  - Consistent column widths.
  - No gaps or overlapping content.

## Project Structure
- `src/converters`: Contains the main conversion logic.
- `src/utils`: Utility scripts for Excel operations, PDF generation, and formatting.
- `src/utils/pdf_generator`: Handles PDF layout and styling.

## Dependencies
- `pandas`
- `fpdf`
- `reportlab`

Install these dependencies using:
```bash
pip install pandas fpdf reportlab
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```