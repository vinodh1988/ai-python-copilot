# Pandas Analytics Notebook Assignments

## Assignment Rules

- Create two separate Jupyter notebooks, one for each dataset.
- Load each dataset into a pandas DataFrame named `df`.
- Use pandas for inspection, cleaning, transformation, and grouping.
- Use Matplotlib through pandas plotting or `matplotlib.pyplot` for visualization.
- Every visualization must be a bar chart. Allowed variations are vertical bar, horizontal bar, grouped bar, and stacked bar charts.
- Do not use line, pie, scatter, histogram, box, area, or heatmap charts.
- Add a chart title, axis labels, readable category labels, a legend when multiple measures are displayed, and `tight_layout()` to every chart.
- Write observations in Markdown cells after the main analysis sections.

---

## Notebook 1: Retail Customer Purchase Analytics

**Notebook filename:** `01_retail_customer_purchases_analysis.ipynb`  
**Dataset:** `datasets/01_retail_customer_purchases.csv`

### Objective

Use pandas grouping and bar charts to compare sales performance by region, product category, loyalty tier, and purchase month.

### Required Notebook Cells

#### Cell 1 - Markdown: Title and Business Questions

Add the notebook title, dataset name, and these questions: Which regions generate the most sales? Which product categories lead in sales and purchase volume? How do discounts and sales differ across loyalty tiers? Which region-category combinations contribute the most sales? How does sales performance change by purchase month?

#### Cell 2 - Code: Import Libraries

Import `pandas` as `pd` and `matplotlib.pyplot` as `plt`. Set a readable plotting style and a default figure size. Do not import other visualization libraries or create charts in this cell.

#### Cell 3 - Code: Load the Dataset as df

Read `datasets/01_retail_customer_purchases.csv` with `pd.read_csv()` and assign it to `df`. Parse `purchase_date` as a date during loading or convert it immediately afterward with `pd.to_datetime()`. Display the first five rows and print the DataFrame shape.

#### Cell 4 - Code: Inspect Data Quality

Display column names, data types, missing-value counts, and duplicated-row count. Check whether `transaction_id` is unique. Use `describe()` for numeric columns. Identify issues without plotting.

#### Cell 5 - Code: Prepare Analysis Columns

Convert `loyalty_tier` to an ordered categorical column using Bronze, Silver, Gold, Platinum. Create `purchase_month` from `purchase_date` in `YYYY-MM` format. Calculate `customer_age` as purchase year minus `customer_birth_year`, then create ordered age groups: Under 25, 25-34, 35-44, 45-54, 55-64, and 65+. Preview the new columns.

#### Cell 6 - Code: Group Sales by Region

Group `df` by `region` and calculate total `sales_amount`, total `items_purchased`, and transaction count using `transaction_id`. Give the output columns clear names, sort by total sales descending, and save the result as `region_summary`.

#### Cell 7 - Code: Plot Regional Sales

Use `region_summary` to create a vertical bar chart of total sales by region. Format the y-axis as currency and add value labels above the bars. The chart must make the highest-sales region easy to identify.

#### Cell 8 - Code: Group and Plot Product Categories

Group by `product_category` and calculate total sales and total items purchased. Save the result as `category_summary`. Create two bar-chart subplots: total sales by category and total items by category. Sort both results for easy comparison.

#### Cell 9 - Code: Analyze Loyalty Tiers

Group by the ordered `loyalty_tier` and calculate average `discount_pct`, average `sales_amount`, and transaction count. Save the result as `loyalty_summary`. Create separate bar-chart subplots for average discount and average sales because they use different units. Preserve the logical loyalty order.

#### Cell 10 - Code: Compare Region and Product Category

Use `groupby()` or `pivot_table()` to calculate total `sales_amount` for every `region` and `product_category` combination. Save it as `region_category_sales`. Create a stacked bar chart with regions on the x-axis and product categories as stacked segments.

#### Cell 11 - Code: Analyze Monthly Sales

Group by `purchase_month`, calculate total monthly sales, sort chronologically, and save the result as `monthly_sales`. Plot a vertical bar chart. Reduce the number of visible x-axis labels if they overlap, but retain every monthly bar.

#### Cell 12 - Code: Analyze Customer Age Groups

Group by ordered age group and calculate average sales amount and total items purchased. Save the output as `age_summary`. Create two bar-chart subplots and identify the group with the highest average spending and the group purchasing the most items.

#### Cell 13 - Markdown: Retail Findings

Write at least five evidence-based findings. Each finding must quote a value or comparison from a grouped result and connect it to a business question. Include one recommendation related to region, product category, or loyalty strategy.

### Notebook 1 Deliverables

- A cleaned and prepared DataFrame named `df`.
- At least five named grouped summary objects.
- Bar charts for region, product category, loyalty tier, region-category sales, monthly sales, and age groups.
- A final Markdown interpretation containing at least five findings and one recommendation.

---

## Notebook 2: Healthcare Patient Visit Analytics

**Notebook filename:** `02_healthcare_patient_visits_analysis.ipynb`  
**Dataset:** `datasets/02_healthcare_patient_visits.csv`

### Objective

Use pandas grouping and bar charts to compare visit volume, treatment cost, waiting time, medication use, pain level, diagnosis category, and monthly activity. The dataset is synthetic and must not be used for clinical decisions.

### Required Notebook Cells

#### Cell 1 - Markdown: Title and Analysis Questions

Add the notebook title, dataset name, synthetic-data disclaimer, and these questions: Which diagnosis categories have the most visits? How do treatment cost and waiting time vary by diagnosis? How do medication use and treatment cost change across pain levels? Which diagnosis-pain combinations account for the most visits? How does visit volume change by month?

#### Cell 2 - Code: Import Libraries

Import `pandas` as `pd` and `matplotlib.pyplot` as `plt`. Set a consistent plot style and default figure size. Do not create a chart in this cell.

#### Cell 3 - Code: Load the Dataset as df

Read `datasets/02_healthcare_patient_visits.csv` with `pd.read_csv()` and assign it to `df`. Parse or convert `visit_date` to pandas datetime format. Display the first five rows and print the DataFrame shape.

#### Cell 4 - Code: Inspect Data Quality

Display column names, data types, missing-value counts, and duplicated-row count. Confirm that `visit_id` is unique. Use `describe()` for numeric fields and display value counts for `diagnosis_category` and `pain_level`. Do not plot in this cell.

#### Cell 5 - Code: Prepare Analysis Columns

Convert `pain_level` to an ordered categorical column using None, Mild, Moderate, Severe, Critical. Create `visit_month` from `visit_date` in `YYYY-MM` format. Create temperature bands named Below Normal, Normal, Elevated, and High, with clearly stated boundaries. Preview the transformed columns and verify pain-level order.

#### Cell 6 - Code: Group Visits by Diagnosis

Group by `diagnosis_category` and calculate visit count, average treatment cost, average waiting time, and average medication count. Name the columns clearly, sort by visit count, and save the result as `diagnosis_summary`.

#### Cell 7 - Code: Plot Visit Count by Diagnosis

Create a horizontal bar chart from `diagnosis_summary` showing visit count by diagnosis. Sort it so the diagnosis with the most visits is easy to identify and add count labels to the bars.

#### Cell 8 - Code: Plot Cost and Waiting Time by Diagnosis

Create two bar-chart subplots from `diagnosis_summary`: average treatment cost by diagnosis and average waiting time by diagnosis. Use separate plots because their units differ. Format treatment cost as currency and waiting time in minutes.

#### Cell 9 - Code: Analyze Pain Levels

Group by ordered `pain_level` and calculate visit count, average medications count, average treatment cost, and average body temperature. Save the result as `pain_summary`. Create bar-chart subplots for average medication count and average treatment cost while preserving pain order.

#### Cell 10 - Code: Compare Diagnosis and Pain Level

Use `groupby()` or `pivot_table()` to count `visit_id` for every diagnosis and pain-level combination. Save it as `diagnosis_pain_counts`. Plot a stacked bar chart with diagnosis categories on the x-axis and pain levels as stacked segments. Keep the legend in ordinal pain order.

#### Cell 11 - Code: Analyze Monthly Visit Volume

Group by `visit_month`, count visits, sort chronologically, and save the result as `monthly_visits`. Plot a vertical bar chart. Reduce displayed x-axis labels if they overlap while retaining every monthly bar.

#### Cell 12 - Code: Analyze Temperature Bands

Group by `temperature_band` and calculate visit count, average medications count, and average treatment cost. Save the result as `temperature_summary`. Create bar-chart subplots for visit count and average treatment cost, keeping temperature bands in logical order.

#### Cell 13 - Code: Compare Previous Visits

Create ordered bands for `previous_visits`: 0, 1-2, 3-5, and 6+. Group by these bands and calculate average waiting time and average treatment cost. Save the result as `previous_visit_summary`. Plot both measures as separate bar charts and state whether higher previous-visit counts appear associated with either measure.

#### Cell 14 - Markdown: Healthcare Findings

Write at least five evidence-based findings, each citing a value or comparison from grouped results. Include one operational recommendation related to visit demand, waiting time, or resource planning. Do not make clinical recommendations.

### Notebook 2 Deliverables

- A cleaned and prepared DataFrame named `df`.
- At least six named grouped summary objects.
- Bar charts for diagnosis volume, diagnosis cost, diagnosis waiting time, pain-level measures, diagnosis-pain composition, monthly visits, temperature bands, and previous-visit bands.
- A final Markdown interpretation with at least five findings, one operational recommendation, and no clinical claims.

---

## Submission Checklist

- Both notebooks run from top to bottom without errors.
- Each CSV is loaded into a DataFrame named `df`.
- Dates and ordered categories are converted correctly before grouping.
- Grouped outputs use clear variable and column names.
- Every chart is a bar chart and directly uses a grouped pandas result.
- Every chart includes a title, axis labels, readable tick labels, and a legend where required.
- No unsupported chart type appears anywhere in either notebook.
- Final findings are supported by displayed calculations rather than assumptions.
