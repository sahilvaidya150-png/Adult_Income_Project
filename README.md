# 📊 Adult Income — Exploratory Data Analysis

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the UCI Adult Income dataset to understand the factors associated with an individual's income level.

The analysis focuses on demographic, educational, occupational, and work-related characteristics and explores how these variables differ between people earning **$50K or less** and those earning **above $50K** per year.

The project includes data cleaning, transformation, statistical analysis, and visualization using Python.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Understand the structure and characteristics of the dataset.
* Clean missing, duplicate, and inconsistent data.
* Analyze income distribution.
* Study the relationship between income and education.
* Analyze income differences across occupations and work classes.
* Compare income groups by sex.
* Examine working hours across income groups.
* Explore age and education relationships.
* Create meaningful visualizations to communicate insights.
* Generate a professional PDF report containing the analysis.

---

## 📂 Dataset

The project uses the **UCI Adult Income Dataset**.

### Dataset Information

* **Total records:** 48,842
* **Original features:** 15
* **Target variable:** Income
* **Income categories:**

  * `50K or Less`
  * `Above 50K`

The dataset contains information related to:

* Age
* Work Class
* Education
* Education Number
* Marital Status
* Occupation
* Relationship
* Race
* Sex
* Capital Gain
* Capital Loss
* Hours per Week
* Native Country
* Income

---

## 🛠️ Technologies Used

| Technology       | Purpose                             |
| ---------------- | ----------------------------------- |
| Python           | Programming and analysis            |
| Pandas           | Data manipulation and cleaning      |
| NumPy            | Numerical operations                |
| Matplotlib       | Data visualization                  |
| Seaborn          | Statistical visualization           |
| Jupyter Notebook | Interactive analysis                |
| ReportLab        | PDF report generation               |
| Git & GitHub     | Version control and project sharing |

---

## 🧹 Data Cleaning

Several data-preparation steps were performed before analysis.

### Main cleaning steps

* Loaded and inspected the dataset.
* Standardized column names.
* Checked missing values.
* Identified duplicate records.
* Handled missing/unknown values represented by `?`.
* Cleaned inconsistent income labels.
* Converted relevant columns to appropriate data types.
* Created a binary `high_income` variable for analysis.

### Income transformation

The income categories were standardized into:

```text
50K or Less
Above 50K
```

A `high_income` flag was also created to make income-group analysis easier.

---

# 📈 Exploratory Data Analysis

The project uses multiple visualizations to understand patterns in the dataset.

## 1. Income Distribution

Shows the number of individuals in each income group.

**Purpose:** Understand the overall distribution of the target variable.

---

## 2. Income by Education

Examines how income groups vary across different education levels.

**Purpose:** Understand the relationship between educational attainment and income category.

---

## 3. Income by Occupation

Compares income groups across different occupations.

**Purpose:** Explore how income distribution varies between occupational categories.

---

## 4. Income by Work Class

Analyzes income groups across different work-class categories.

**Purpose:** Examine differences in income distribution based on employment/work-class type.

---

## 5. Income by Sex

Compares income categories across sex groups.

**Purpose:** Examine differences in the distribution of income categories.

---

## 6. Hours Worked per Week

Analyzes weekly working hours across income groups.

**Purpose:** Understand how working hours are distributed between income categories.

---

## 7. Age Distribution

Examines the distribution of age within the dataset.

**Purpose:** Understand the demographic structure of the population.

---

## 8. Age vs Education

Explores the relationship between age and education level.

**Purpose:** Examine how educational attainment varies across different age groups.

---

## 9. Education and Income Rate

Analyzes the proportion of individuals above the income threshold across education categories.

**Purpose:** Compare income rates across different levels of education.

---

# 🔍 Key Findings

The analysis provides several observations about the Adult Income dataset:

* Income categories are not evenly distributed across the dataset.
* Income distribution varies across education levels.
* Different occupations show different income distributions.
* Work class is associated with differences in income-group distribution.
* Income categories differ across sex groups.
* Weekly working hours vary between income groups.
* Age and education show observable patterns that can be explored through visualization.
* Education level provides useful information when analyzing income categories.

> **Note:** These findings describe patterns in this dataset and should not be interpreted as proof that any single factor causes higher income.

---

# 📊 Project Structure

```text
adult_income_eda_project/
│
├── data/
│   ├── adult.data
│   └── adult.test
│
├── reports/
│   ├── charts/
│   └── Adult_Income_EDA_Report.pdf
│
├── src/
│   ├── Data Cleaning.ipynb
│   ├── Data Analysis.ipynb
│   └── build_pdf_report.py
│
├── README.md
│
└── requirements.txt
```

---

# ▶️ How to Run the Project

## 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

## 2. Navigate to the project

```bash
cd adult_income_eda_project
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 6. Run the analysis

Open the notebooks inside the `src` folder:

```text
Data Cleaning.ipynb
Data Analysis.ipynb
```

Run the notebook cells to reproduce the analysis.

## 7. Generate the PDF report

```bash
python src/build_pdf_report.py
```

The generated report will be saved inside:

```text
reports/Adult_Income_EDA_Report.pdf
```

---

# 📄 PDF Report

A complete PDF report containing the project's analysis and visualizations is available in the `reports` folder.

**Report:** `Adult_Income_EDA_Report.pdf`

---

# ⚠️ Limitations

This project has several limitations:

* The analysis is based on the available Adult Income dataset.
* Dataset patterns do not establish causal relationships.
* Some records contain missing or unknown values.
* Income is represented using a threshold rather than an exact continuous salary.
* The analysis is exploratory and does not represent a predictive machine-learning model.
* Results may not generalize to populations outside the dataset.

---

# 🚀 Future Improvements

The project can be extended by:

* Building machine-learning models to predict income categories.
* Performing feature engineering.
* Comparing multiple classification algorithms.
* Applying cross-validation.
* Evaluating models using precision, recall, F1-score, and ROC-AUC.
* Building an interactive dashboard using Power BI or Streamlit.
* Deploying

