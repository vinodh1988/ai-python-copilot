# Matplotlib Analytics Notebook Assignments

## Common Rules

- Create two separate Jupyter notebooks, one for each dataset.
- Load each CSV into a pandas DataFrame named df; use pandas for preparation and aggregation.
- Create every visualization directly with matplotlib.pyplot or Matplotlib axes methods.
- Do not use Seaborn, Plotly, Altair, Bokeh, or pandas .plot().
- Use varied chart types chosen for the analytical question.
- Every chart needs a meaningful title, axis labels, readable ticks, and a legend whenever color, line style, marker, size, or stacked sections encode data.
- Define and reuse a deliberate color palette. Avoid assigning random colors.
- Use fig, ax = plt.subplots() and tight_layout() or constrained layout.
- Hybrid charts may combine bars and lines with ax.twinx() when measures have different scales.
- Add annotations only when they help identify peaks, outliers, totals, or important comparisons.

---

## Notebook 1: Retail Purchase Visualization with Matplotlib

**Notebook filename:** 01_retail_matplotlib_analysis.ipynb  
**Dataset:** datasets/01_retail_customer_purchases.csv

### Objective

Analyze retail sales, product mix, discounts, loyalty tiers, customer age, and monthly performance while demonstrating purposeful use of multiple Matplotlib chart types.

### Required Notebook Cells

#### Cell 1 - Markdown: Title and Questions

Add the notebook title, dataset path, and six questions covering monthly sales trends, regional performance, product mix, loyalty-tier behavior, the relationship between price and sales, and customer-age patterns.

#### Cell 2 - Code: Imports and Visual Theme

Import pandas as pd, NumPy as np, matplotlib.pyplot as plt, and Matplotlib currency and percentage formatters. Define named palettes for regions, product categories, and loyalty tiers. Configure figure size, font size, grid visibility, and background defaults through plt.rcParams.

#### Cell 3 - Code: Load the CSV as df

Read the retail CSV into df and parse purchase_date as datetime. Display the first five rows, shape, and data types. The DataFrame variable must be exactly df.

#### Cell 4 - Code: Validate and Prepare Data

Check missing values, duplicate rows, and unique transaction_id values. Convert loyalty_tier to the ordered sequence Bronze, Silver, Gold, Platinum. Create purchase_month, customer_age, and an ordered age_group. Also calculate discount_value as items_purchased multiplied by unit_price minus sales_amount.

#### Cell 5 - Code: Monthly Sales Line Chart

Group total sales_amount by purchase_month. Use ax.plot() to create a line chart with visible markers. Apply one strong color, a subtle grid, currency formatting, and an annotation for the highest-sales month. Do not add a legend for a single obvious series.

#### Cell 6 - Code: Regional Hybrid Chart

Group by region to calculate total sales and average sales per transaction. Plot total sales as bars on the primary axis and average transaction value as a contrasting line with markers on a secondary axis created with ax.twinx(). Combine handles from both axes into one legend and label both y-axes.

#### Cell 7 - Code: Product Category Donut Chart

Aggregate sales by product_category. Use ax.pie() with a center circle to create a donut chart. Apply the category palette, show percentage labels, place the category legend outside the chart, and display total sales as centered text.

#### Cell 8 - Code: Discount Histogram

Use ax.hist() to show the distribution of discount_pct with meaningful bin boundaries and visible edges. Add vertical lines for mean and median using different colors and line styles. Include both reference lines in a legend.

#### Cell 9 - Code: Loyalty-Tier Box Plot

Create a list of sales_amount arrays in loyalty-tier order and draw a box plot with ax.boxplot(). Assign a tier color to each box, emphasize medians, label each tier, and format the y-axis as currency. Add a Markdown observation about median, spread, and outliers.

#### Cell 10 - Code: Price and Sales Scatter Plot

Plot unit_price against sales_amount. Draw each product_category as a separate scatter series so category color appears in a legend. Use transparency to reduce overlap and marker size to represent items_purchased. Explain the x-position, y-position, color, and size encodings.

#### Cell 11 - Code: Regional Product-Mix Stacked Bars

Create a region-by-category sales table with pivot_table(). Build a stacked bar chart with repeated ax.bar() calls and a cumulative bottom array. Reuse category colors, move the legend outside the axes, and annotate total sales above each regional stack.

#### Cell 12 - Code: Customer Age Bubble Chart

Group by age_group to calculate average sales, total items, and transaction count. Use ax.scatter() with age group on the x-axis, average sales on the y-axis, bubble size for transaction count, and bubble color for total items. Add a labeled colorbar and annotate each bubble.

#### Cell 13 - Code: Retail Dashboard

Create a 2-by-2 dashboard with plt.subplots(). Include monthly sales as a line chart, regional sales as a bar chart, category share as a donut chart, and loyalty-tier sales as a box plot. Add a figure-level title and ensure legends do not overlap neighboring plots.

#### Cell 14 - Markdown: Findings and Design Review

Write at least five findings supported by calculated values. Explain why each chart type was suitable, how colors were kept consistent, where legends were necessary or unnecessary, and what the hybrid chart showed that a single-axis chart could not.

### Notebook 1 Deliverables

- Line, hybrid bar-line, donut, histogram, box, scatter, stacked bar, bubble, and dashboard visuals.
- Consistent colors and correctly placed legends.
- At least one peak annotation and mean/median reference annotations.
- Five analytical findings and a chart-design justification.

---

## Notebook 2: Healthcare Visit Visualization with Matplotlib

**Notebook filename:** 02_healthcare_matplotlib_analysis.ipynb  
**Dataset:** datasets/02_healthcare_patient_visits.csv

### Objective

Explore synthetic visit demand, diagnosis mix, pain level, medication use, treatment cost, temperature, and waiting time using varied Matplotlib charts. This synthetic dataset must not be used for clinical decisions.

### Required Notebook Cells

#### Cell 1 - Markdown: Title, Disclaimer, and Questions

Add the title, dataset path, synthetic-data disclaimer, and six operational questions covering monthly demand, diagnosis distribution, pain-level costs, waiting-time distribution, medication patterns, and relationships among waiting time, temperature, and cost.

#### Cell 2 - Code: Imports and Visual Theme

Import pandas as pd, NumPy as np, matplotlib.pyplot as plt, and useful Matplotlib formatters. Define a sequential pain-level palette from a neutral color for None to a strong warning color for Critical. Define a separate categorical palette for diagnoses and set readable plt.rcParams defaults.

#### Cell 3 - Code: Load the CSV as df

Read the healthcare CSV into df and parse visit_date. Display the first five rows, shape, and data types. The DataFrame variable must be named df.

#### Cell 4 - Code: Validate and Prepare Data

Check missing values, duplicates, unique visit_id values, and numeric ranges. Convert pain_level to the ordered sequence None, Mild, Moderate, Severe, Critical. Create visit_month and clearly defined temperature_band categories. Display category counts in logical order.

#### Cell 5 - Code: Monthly Visits and Cost Dual-Line Chart

Group by visit_month to calculate visit count and average treatment cost. Plot visit count as a solid line with circle markers on the primary axis and average cost as a dashed line with square markers on a secondary axis. Use distinct colors, combine handles into one legend, and annotate peak visit volume.

#### Cell 6 - Code: Diagnosis Donut Chart

Count visits by diagnosis_category and create a donut chart. Use the diagnosis palette, show percentages, place the legend outside, and show total visits in the center. Group very small categories into Other only if labels are unreadable, and document that transformation.

#### Cell 7 - Code: Waiting-Time Histogram

Plot waiting_time_minutes with ax.hist(). Choose sensible bins and visible edges. Add mean and median reference lines with distinct styles, include them in a legend, and annotate the 90th percentile.

#### Cell 8 - Code: Treatment-Cost Box Plot

Draw a box plot of treatment_cost for each ordered pain level with ax.boxplot(). Use the pain palette, currency formatting, and emphasized median lines. Add a Markdown interpretation about distribution, variability, and outliers without clinical claims.

#### Cell 9 - Code: Waiting Time and Cost Scatter Plot

Plot waiting time on the x-axis and treatment cost on the y-axis. Draw one scatter series per pain level using consistent colors and a legend. Use marker size for medications_count and transparency for overlapping points. Explain all visual encodings.

#### Cell 10 - Code: Diagnosis and Pain Stacked Bars

Create a diagnosis-by-pain visit-count table. Build a stacked bar chart using repeated ax.bar() calls and cumulative bottom values. Keep pain colors and legend entries in ordinal order. Add total visit labels above each diagnosis.

#### Cell 11 - Code: Medication and Cost Hybrid Chart

Group by pain level to calculate average medications count and average treatment cost. Plot medications as bars and treatment cost as a line on a secondary y-axis. Use pain colors for bars, a contrasting line color, two labeled scales, and one combined legend.

#### Cell 12 - Code: Temperature and Cost Hexbin Chart

Use ax.hexbin() for body_temperature_c versus treatment_cost, with color representing observation density. Add a labeled colorbar, choose a readable Matplotlib colormap, and explain why hexagonal aggregation helps with a large dataset.

#### Cell 13 - Code: Diagnosis Profile Radar Chart

Select the four diagnosis categories with the most visits. Calculate their average waiting time, treatment cost, medication count, and previous visits, then normalize each metric from 0 to 1. Create a polar radar chart with one colored line and translucent fill per diagnosis. Close each polygon, label metrics, place the legend outside, and state that normalized values are profiles rather than original units.

#### Cell 14 - Code: Healthcare Dashboard

Create a 2-by-2 dashboard containing monthly visits, diagnosis share, waiting-time distribution, and the medication-cost hybrid chart. Add a figure title, manage legends and spacing carefully, and include the synthetic-data disclaimer as a small figure note.

#### Cell 15 - Markdown: Findings and Design Review

Write at least five operational findings supported by grouped values or descriptive statistics. Explain the sequential and categorical palettes, identify charts requiring legends, explain the dual-axis hybrid chart, and state one limitation of normalized radar values. Do not make clinical recommendations.

### Notebook 2 Deliverables

- Dual-line, donut, histogram, box, scatter, stacked bar, hybrid bar-line, hexbin, radar, and dashboard visuals.
- Consistent pain-level and diagnosis colors with complete legends.
- Peak, percentile, total, and reference-line annotations.
- Five operational findings, design reasoning, and no clinical claims.

---

## Submission Checklist

- Both notebooks run from top to bottom without errors.
- Each CSV is loaded into a DataFrame named df.
- All charts use Matplotlib directly; no other visualization library and no pandas .plot() calls are used.
- Chart types match their analytical questions.
- Colors retain consistent meanings within each notebook.
- Legends explain every non-obvious color, marker, line, size, or stacked encoding.
- Dual-axis charts label both axes and use a combined legend.
- Titles, labels, ticks, annotations, and legends do not overlap.
- Conclusions refer to displayed calculations and avoid unsupported claims.
