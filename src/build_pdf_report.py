from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    Image,
    KeepTogether
)
from reportlab.lib.units import inch
import os


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Project root:
# adult_income_eda_project/
# ├── data/
# ├── reports/
# │   └── charts/
# └── src/
#     └── build_pdf_report.py

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


REPORTS_DIR = os.path.join(BASE_DIR, "reports")
CHARTS_DIR = os.path.join(REPORTS_DIR, "charts")

PDF_PATH = os.path.join(
    REPORTS_DIR,
    "Adult_Income_EDA_Report.pdf"
)

# Create required folders
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(CHARTS_DIR, exist_ok=True)


# ============================================================
# 2. CREATE PDF DOCUMENT
# ============================================================

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)


# ============================================================
# 3. STYLES
# ============================================================

styles = getSampleStyleSheet()


# ---------- Title ----------
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=24,
    leading=30,
    spaceAfter=20
)


# ---------- Subtitle ----------
subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=11,
    leading=16,
    spaceAfter=20
)


# ---------- Section Heading ----------
heading_style = ParagraphStyle(
    "HeadingStyle",
    parent=styles["Heading2"],
    fontSize=16,
    leading=20,
    spaceBefore=12,
    spaceAfter=10
)


# ---------- Chart Heading ----------
chart_heading_style = ParagraphStyle(
    "ChartHeadingStyle",
    parent=styles["Heading2"],
    alignment=TA_CENTER,
    fontSize=15,
    leading=19,
    spaceAfter=12
)


# ---------- Body ----------
body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=16,
    spaceAfter=9
)


# ---------- Caption ----------
caption_style = ParagraphStyle(
    "CaptionStyle",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=9,
    leading=13,
    textColor=colors.grey,
    spaceBefore=8,
    spaceAfter=8
)


# ---------- Interpretation ----------
interpretation_style = ParagraphStyle(
    "InterpretationStyle",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    leftIndent=10,
    rightIndent=10,
    spaceBefore=5,
    spaceAfter=12
)


# ============================================================
# 4. STORY
# ============================================================

story = []


# ============================================================
# 5. TITLE PAGE
# ============================================================

story.append(Spacer(1, 70))

story.append(
    Paragraph(
        "Adult Income EDA Project",
        title_style
    )
)

story.append(
    Paragraph(
        "Exploratory Data Analysis Report",
        subtitle_style
    )
)

story.append(Spacer(1, 15))

story.append(
    Paragraph(
        "<b>Dataset:</b> UCI Adult Income Dataset<br/><br/>"
        "<b>Records:</b> 48,842<br/><br/>"
        "<b>Objective:</b> Explore demographic, educational, "
        "and employment-related patterns associated with income.",
        body_style
    )
)

story.append(Spacer(1, 35))

story.append(
    Paragraph(
        "Data Science Portfolio Project",
        subtitle_style
    )
)

story.append(
    Paragraph(
        "Python • Pandas • NumPy • Matplotlib • Seaborn",
        subtitle_style
    )
)

story.append(PageBreak())


# ============================================================
# 6. PROJECT OVERVIEW
# ============================================================

story.append(
    Paragraph(
        "1. Project Overview",
        heading_style
    )
)

story.append(
    Paragraph(
        "This project performs Exploratory Data Analysis (EDA) "
        "on the UCI Adult Income dataset. The analysis examines "
        "patterns between income and variables such as education, "
        "work class, occupation, sex, age, and weekly working hours.",
        body_style
    )
)

story.append(
    Paragraph(
        "The main purpose of the project is to understand the "
        "structure of the dataset, identify meaningful patterns, "
        "and communicate findings using statistical summaries "
        "and visualizations.",
        body_style
    )
)


# ============================================================
# 7. DATASET OVERVIEW
# ============================================================

story.append(
    Paragraph(
        "2. Dataset Overview",
        heading_style
    )
)

dataset_data = [
    ["Item", "Description"],
    ["Dataset", "UCI Adult Income Dataset"],
    ["Records", "48,842"],
    ["Target", "Income"],
    ["Income Groups", "50K or Less / Above 50K"],
    [
        "Important Features",
        "Age, Work Class, Education, Occupation, "
        "Sex, Hours per Week"
    ]
]

dataset_table = Table(
    dataset_data,
    colWidths=[1.7 * inch, 4.6 * inch]
)

dataset_table.setStyle(
    TableStyle([
        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.lightgrey
        ),
        (
            "GRID",
            (0, 0),
            (-1, -1),
            0.5,
            colors.grey
        ),
        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),
        (
            "VALIGN",
            (0, 0),
            (-1, -1),
            "TOP"
        ),
        (
            "FONTSIZE",
            (0, 0),
            (-1, -1),
            9
        ),
        (
            "PADDING",
            (0, 0),
            (-1, -1),
            6
        )
    ])
)

story.append(dataset_table)

story.append(Spacer(1, 15))


# ============================================================
# 8. DATA CLEANING
# ============================================================

story.append(
    Paragraph(
        "3. Data Cleaning",
        heading_style
    )
)

cleaning_points = [
    "Loaded and inspected the Adult Income dataset.",
    "Standardized column names for easier analysis.",
    "Handled missing and unknown values.",
    "Cleaned categorical variables.",
    "Standardized income categories.",
    "Created a high_income feature for analysis.",
    "Checked duplicate records.",
    "Checked numerical variables and missing values."
]

for point in cleaning_points:
    story.append(
        Paragraph(
            "• " + point,
            body_style
        )
    )


# ============================================================
# 9. EDA OVERVIEW
# ============================================================

story.append(
    Paragraph(
        "4. Exploratory Data Analysis",
        heading_style
    )
)

story.append(
    Paragraph(
        "The exploratory analysis investigates how income is "
        "distributed and how it varies across education, work "
        "class, occupation, sex, age, and weekly working hours.",
        body_style
    )
)

story.append(
    Paragraph(
        "Visualizations are used to make comparisons easier and "
        "to identify patterns that may not be obvious from raw data.",
        body_style
    )
)


# ============================================================
# 10. CHART INFORMATION
# ============================================================

chart_files = [

    (
        "01_income_distribution.png",
        "Income Distribution",
        "This chart shows the distribution of observations "
        "across the two income categories.",
        "The visualization helps identify whether the dataset "
        "is balanced or dominated by one income category."
    ),

    (
        "02_income_rate_by_education.png",
        "Income Rate by Education",
        "This chart compares the percentage of individuals "
        "with higher income across education levels.",
        "The comparison can help identify differences in the "
        "observed higher-income rate across education groups."
    ),

    (
        "03_income_rate_by_workclass.png",
        "Income Rate by Work Class",
        "This chart compares higher-income rates across "
        "different work-class categories.",
        "The chart shows that income patterns vary across "
        "different employment categories."
    ),

    (
        "04_income_rate_by_occupation.png",
        "Income Rate by Occupation",
        "This chart compares the percentage of higher-income "
        "observations across occupations.",
        "The visualization highlights differences in the "
        "observed income distribution among occupations."
    ),

    (
        "05_income_rate_by_sex.png",
        "Income Rate by Sex",
        "This chart compares higher-income rates between "
        "the sex categories represented in the dataset.",
        "The chart describes differences in observed income "
        "rates between these groups; it does not establish "
        "the reason for those differences."
    ),

    (
        "06_weekly_hours_by_income.png",
        "Weekly Hours by Income",
        "This chart compares weekly working hours across "
        "the income categories.",
        "The visualization helps examine whether typical "
        "working hours differ between income groups."
    ),

    (
        "07_age_distribution_by_income.png",
        "Age Distribution by Income",
        "This visualization compares the age distributions "
        "of the income categories.",
        "The chart helps identify differences in age patterns "
        "between income groups."
    ),

    (
        "08_education_vs_income.png",
        "Education vs Income",
        "This visualization examines the relationship between "
        "education level and income category.",
        "It provides a visual comparison of income patterns "
        "across education groups."
    ),

    (
        "09_age_vs_education_number.png",
        "Age vs Education Number",
        "This chart examines age in relation to the numerical "
        "education representation.",
        "The visualization helps explore how age and education "
        "level are distributed together."
    )
]


# ============================================================
# 11. ADD CHARTS
# ============================================================

charts_found = 0
charts_missing = []

for (
    filename,
    chart_title,
    caption,
    interpretation
) in chart_files:

    chart_path = os.path.join(
        CHARTS_DIR,
        filename
    )

    if os.path.exists(chart_path):

        charts_found += 1

        story.append(PageBreak())

        story.append(
            Paragraph(
                chart_title,
                chart_heading_style
            )
        )

        # Create image
        img = Image(
            chart_path,
            width=6.5 * inch,
            height=4.2 * inch
        )

        # Keep image and text together
        chart_content = [
            img,
            Paragraph(
                "<b>Figure:</b> " + caption,
                caption_style
            ),
            Paragraph(
                "<b>Interpretation:</b> " + interpretation,
                interpretation_style
            )
        ]

        story.append(
            KeepTogether(chart_content)
        )

    else:

        charts_missing.append(filename)


# ============================================================
# 12. CHART STATUS
# ============================================================

story.append(PageBreak())

story.append(
    Paragraph(
        "5. Visualization Summary",
        heading_style
    )
)

story.append(
    Paragraph(
        f"A total of <b>{charts_found}</b> chart(s) were found "
        f"and included in the report.",
        body_style
    )
)

if charts_missing:

    story.append(
        Paragraph(
            "<b>Charts not found:</b>",
            body_style
        )
    )

    for missing in charts_missing:

        story.append(
            Paragraph(
                "• " + missing,
                body_style
            )
        )

else:

    story.append(
        Paragraph(
            "All expected charts were successfully found "
            "and included in the report.",
            body_style
        )
    )


# ============================================================
# 13. KEY FINDINGS
# ============================================================

story.append(
    Paragraph(
        "6. Key Findings",
        heading_style
    )
)

findings = [

    "Income is distributed across two main categories: "
    "50K or Less and Above 50K.",

    "Education level shows different observed income "
    "patterns across groups.",

    "Income patterns vary across work-class categories.",

    "Different occupations show different observed "
    "higher-income rates.",

    "The income distribution differs between the demographic "
    "groups represented in the dataset.",

    "Weekly working hours can be compared across income "
    "categories to identify differences in working patterns.",

    "Age provides another useful dimension for examining "
    "income distributions.",

    "Age and education can be analyzed together to understand "
    "how these variables are distributed in the dataset."
]

for finding in findings:

    story.append(
        Paragraph(
            "• " + finding,
            body_style
        )
    )


# ============================================================
# 14. LIMITATIONS
# ============================================================

story.append(
    Paragraph(
        "7. Limitations",
        heading_style
    )
)

limitations = [

    "EDA identifies patterns and associations but does "
    "not prove causation.",

    "Categorical variables require careful interpretation "
    "because category definitions can affect results.",

    "Income is represented as a category rather than an "
    "exact individual income value.",

    "The dataset represents a particular source population "
    "and time period.",

    "Observed differences between groups should not be "
    "interpreted as evidence that one variable directly "
    "causes another."
]

for limitation in limitations:

    story.append(
        Paragraph(
            "• " + limitation,
            body_style
        )
    )


# ============================================================
# 15. CONCLUSION
# ============================================================

story.append(
    Paragraph(
        "8. Conclusion",
        heading_style
    )
)

story.append(
    Paragraph(
        "The Adult Income EDA project demonstrates a complete "
        "data analysis workflow including data loading, "
        "data cleaning, feature preparation, exploratory "
        "analysis, and visualization.",
        body_style
    )
)

story.append(
    Paragraph(
        "The analysis provides a structured view of income "
        "patterns across demographic, educational, and "
        "employment-related variables. The visualizations "
        "make it easier to compare groups and identify "
        "relationships within the dataset.",
        body_style
    )
)

story.append(
    Paragraph(
        "These findings can serve as a foundation for further "
        "statistical analysis or machine-learning experiments.",
        body_style
    )
)


# ============================================================
# 16. FINAL REPORT INFORMATION
# ============================================================

story.append(Spacer(1, 25))

story.append(
    Paragraph(
        "<b>Tools Used:</b> Python, Pandas, NumPy, "
        "Matplotlib, Seaborn, ReportLab",
        body_style
    )
)

story.append(
    Paragraph(
        "<b>Project Type:</b> Exploratory Data Analysis",
        body_style
    )
)


# ============================================================
# 17. BUILD PDF
# ============================================================

try:

    doc.build(story)

    print()
    print("======================================")
    print("PDF CREATED SUCCESSFULLY!")
    print("======================================")
    print()
    print("Charts found :", charts_found)
    print("Charts missing:", len(charts_missing))
    print()
    print("PDF Location:")
    print(PDF_PATH)
    print()

    if charts_missing:

        print("Missing chart files:")
        for file in charts_missing:
            print(" -", file)

    print()
    print("======================================")

except Exception as e:

    print()
    print("======================================")
    print("ERROR WHILE CREATING PDF")
    print("======================================")
    print()
    print("Error:", e)
    print()