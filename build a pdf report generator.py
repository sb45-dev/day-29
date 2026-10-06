import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# -----------------------------
# 1. Create sample business data
# -----------------------------

data = {
    "Employee": ["Sandeep", "Rahul", "Aman", "Priya", "Neha"],
    "Department": ["IT", "Sales", "IT", "HR", "Sales"],
    "Sales": [50000, 65000, 45000, 40000, 70000]
}

df = pd.DataFrame(data)

# Save sample dataset
df.to_csv("business_data.csv", index=False)


# -----------------------------
# 2. Calculate summary metrics
# -----------------------------

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
highest_sales = df["Sales"].max()
lowest_sales = df["Sales"].min()


# -----------------------------
# 3. Create PDF
# -----------------------------

pdf_file = "business_report.pdf"

document = SimpleDocTemplate(
    pdf_file,
    pagesize=A4
)

styles = getSampleStyleSheet()

elements = []

# Title
title = Paragraph(
    "Business Sales Report",
    styles["Title"]
)

elements.append(title)
elements.append(Spacer(1, 20))


# -----------------------------
# 4. Add summary information
# -----------------------------

summary = [
    ["Metric", "Value"],
    ["Total Sales", f"₹{total_sales:,.2f}"],
    ["Average Sales", f"₹{average_sales:,.2f}"],
    ["Highest Sales", f"₹{highest_sales:,.2f}"],
    ["Lowest Sales", f"₹{lowest_sales:,.2f}"]
]

summary_table = Table(summary)

summary_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ])
)

elements.append(summary_table)
elements.append(Spacer(1, 25))


# -----------------------------
# 5. Add employee data
# -----------------------------

elements.append(
    Paragraph("Employee Sales Data", styles["Heading2"])
)

table_data = [list(df.columns)] + df.values.tolist()

employee_table = Table(table_data)

employee_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (2, 1), (2, -1), "RIGHT"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ])
)

elements.append(employee_table)


# -----------------------------
# 6. Generate PDF
# -----------------------------

document.build(elements)

print("PDF report generated successfully!")
print("File name:", pdf_file)
print("Dataset created: business_data.csv")