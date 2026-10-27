import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from src.utils.pdf_generator.config import DEFAULT_PAGE_SIZE, DEFAULT_MARGIN, get_pdf_styles
from src.utils.pdf_generator.builder import build_pdf_table


def export_dataframe_to_pdf(df: pd.DataFrame, pdf_path: str, title: str = "Report Table") -> None:
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=DEFAULT_PAGE_SIZE,
        leftMargin=DEFAULT_MARGIN,
        rightMargin=DEFAULT_MARGIN,
        topMargin=DEFAULT_MARGIN,
        bottomMargin=DEFAULT_MARGIN
    )

    story = []
    title_style, _, _, _, _ = get_pdf_styles()

    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 15))

    available_width = doc.width
    pdf_table = build_pdf_table(df, available_width)
    story.append(pdf_table)

    doc.build(story)
    print(f"PDF successfully generated at: {pdf_path}")


# if __name__ == "__main__":
#     # Test dataset matching your requirement (S.No, owner_name, district)
#     sample_data = {
#         "S.No": [1, 2, 3, 4],
#         "owner_name": ["Rajesh Kumar", "Ananya Sharma", "Priya Nair", "Vikram Verma"],
#         "district": ["Hyderabad", "Rangareddy", "Medchal-Malkajgiri", "Sangareddy"],
#         "Project Description": [
#             "Building robust MLOps pipelines with Docker Swarm and Spark.",
#             "Overseeing health platform setups and quarterly milestones.",
#             "Designing scalable REST APIs and Redis caching layers.",
#             "Automating integration testing and pipeline validations."
#         ],
#         "Status": ["Active", "Completed", "Active", "Pending"]
#     }
#
#     df_sample = pd.DataFrame(sample_data)
#     export_dataframe_to_pdf(df_sample, "optimized_report.pdf", title="District Owner Allocation Report")