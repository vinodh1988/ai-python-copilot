# Microsoft Copilot Exercise: Generate Synthetic Analytics Data

## Learning objective

Use Microsoft Copilot, Python, NumPy, pandas, and Faker to create seven synthetic CSV datasets for analytics. Each dataset must contain these kinds of columns:

| Data type | Meaning | Examples |
|---|---|---|
| Nominal | Categories with no natural order | Region, department, product category |
| Ordinal | Categories with a meaningful order | Low, Medium, High |
| Discrete | Countable whole-number values | Number of purchases, defects |
| Continuous | Measured values that may contain decimals | Revenue, distance, salary |
| Interval | Equal differences are meaningful, but zero is not a true absence | Celsius temperature, calendar year |

Note: A variable can belong to more than one classification system. Celsius temperature is numerically continuous and uses an interval measurement scale. For this exercise, label it as interval.

## Part 1: Install the libraries

### Terminal or command prompt

~~~bash
python -m pip install numpy pandas Faker
~~~

### Jupyter notebook

~~~python
%pip install numpy pandas Faker
~~~

Restart the notebook kernel if the imports do not work immediately.

### Verify the installation

~~~python
import numpy as np
import pandas as pd
from faker import Faker

print("NumPy:", np.__version__)
print("pandas:", pd.__version__)
print("Faker sample:", Faker().name())
~~~

## Part 2: Instructions for working with Copilot

For every dataset:

1. Read the concept and required schema.
2. Paste its prompt into Microsoft Copilot.
3. Review Copilot's explanation and generated code.
4. Check that it uses NumPy, Faker, and pandas.
5. Run the code in a notebook cell or Python file.
6. Correct any errors with help from Copilot.
7. Confirm that the DataFrame contains exactly 10,000 rows.
8. Validate IDs, missing values, categories, numeric ranges, and relationships.
9. Export the result to the specified CSV filename.
10. Read the CSV back with pandas to confirm it was saved correctly.

## Common requirements for all seven prompts

Copilot must:

- Use numpy.random.default_rng(42) for reproducible numeric generation.
- Use Faker.seed(42) and Faker() for suitable names, IDs, locations, and dates.
- Use pandas to create, validate, and export the DataFrame.
- Generate exactly 10,000 rows.
- Create realistic relationships between columns.
- Avoid impossible values and invalid categories.
- Make every ID unique and non-null.
- Use ordered pandas categorical data for ordinal columns where appropriate.
- Create the datasets folder with pathlib if it does not exist.
- Save CSV files with index=False.
- Print a preview, data types, missing-value counts, category frequencies, and numeric summaries.
- Avoid charts and visualization libraries.

---

## Dataset 1: Retail Customer Purchases

Output file: datasets/01_retail_customer_purchases.csv

| Column | Classification | Rules |
|---|---|---|
| transaction_id | Nominal | Unique ID |
| customer_name | Nominal | Synthetic name |
| region | Nominal | North, South, East, West, Central |
| product_category | Nominal | Electronics, Clothing, Home, Grocery, Sports |
| loyalty_tier | Ordinal | Bronze, Silver, Gold, Platinum |
| items_purchased | Discrete | Integer from 1 to 15 |
| customer_birth_year | Interval | Calendar year from 1945 to 2007 |
| unit_price | Continuous | Positive value |
| discount_pct | Continuous | 0 to 35 |
| sales_amount | Continuous | Calculated amount |
| purchase_date | Date | Within the last three years |

### Prompt for Microsoft Copilot

~~~text
Create a complete executable Python program that generates exactly 10,000 synthetic retail purchase records using pandas, NumPy, and Faker. Follow the common requirements in this exercise.

Create transaction_id, customer_name, region, product_category, loyalty_tier, items_purchased, customer_birth_year, unit_price, discount_pct, sales_amount, and purchase_date. Treat region and product category as nominal; loyalty tier as ordinal with Bronze < Silver < Gold < Platinum; items purchased as discrete; unit price, discount, and sales amount as continuous; and birth year as interval.

Make higher loyalty tiers likely to receive larger discounts. Calculate sales_amount as items_purchased * unit_price * (1 - discount_pct / 100). Validate all fields and save the result to datasets/01_retail_customer_purchases.csv. Do not create visualizations. Explain the code after presenting it.
~~~

---

## Dataset 2: Healthcare Patient Visits

Output file: datasets/02_healthcare_patient_visits.csv

| Column | Classification | Rules |
|---|---|---|
| visit_id | Nominal | Unique ID |
| patient_name | Nominal | Synthetic name |
| blood_group | Nominal | Valid blood group |
| diagnosis_category | Nominal | High-level diagnosis |
| pain_level | Ordinal | None, Mild, Moderate, Severe, Critical |
| previous_visits | Discrete | Non-negative integer |
| medications_count | Discrete | Non-negative integer |
| body_temperature_c | Interval | Plausible Celsius value |
| treatment_cost | Continuous | Positive value |
| waiting_time_minutes | Continuous | Non-negative value |
| visit_date | Date | Within the last two years |

### Prompt for Microsoft Copilot

~~~text
Create a complete Python program that generates exactly 10,000 synthetic healthcare visit records using pandas, NumPy, and Faker. Follow the common requirements.

Create visit_id, patient_name, blood_group, diagnosis_category, pain_level, previous_visits, medications_count, body_temperature_c, treatment_cost, waiting_time_minutes, and visit_date. Blood group and diagnosis are nominal. Pain level is ordinal with None < Mild < Moderate < Severe < Critical. Visit and medication counts are discrete. Treatment cost and waiting time are continuous. Celsius body temperature is interval.

Keep values plausible, but state that the synthetic data is not for clinical decisions. Make severe pain and elevated temperature moderately associated with more medications and higher treatment cost. Validate the data and save it to datasets/02_healthcare_patient_visits.csv. Do not create charts.
~~~

---

## Dataset 3: Student Learning Performance

Output file: datasets/03_student_learning_performance.csv

| Column | Classification | Rules |
|---|---|---|
| student_id | Nominal | Unique ID |
| school_type | Nominal | Public, Private, Charter |
| subject_stream | Nominal | Science, Commerce, Arts, Vocational |
| engagement_level | Ordinal | Very Low through Very High |
| absences | Discrete | Non-negative integer |
| assignments_completed | Discrete | Integer from 0 to 20 |
| study_hours_per_week | Continuous | 0 to 40 |
| final_score | Continuous | 0 to 100 |
| examination_year | Interval | 2022 to 2026 |
| passed | Nominal | Yes or No |

### Prompt for Microsoft Copilot

~~~text
Generate exactly 10,000 synthetic student performance records with pandas, NumPy, and Faker. Follow the common requirements.

Include student_id, school_type, subject_stream, engagement_level, absences, assignments_completed, study_hours_per_week, final_score, examination_year, and passed. School type, stream, and passed are nominal. Engagement is ordinal with Very Low < Low < Medium < High < Very High. Absences and assignments are discrete. Study hours and score are continuous. Examination year is interval.

Higher engagement, study hours, and completed assignments should generally improve final_score, while excessive absences should reduce it. Keep scores from 0 to 100 and derive passed from final_score >= 40. Validate and save as datasets/03_student_learning_performance.csv. Do not create visualizations.
~~~

---

## Dataset 4: Employee Workforce Analytics

Output file: datasets/04_employee_workforce.csv

| Column | Classification | Rules |
|---|---|---|
| employee_id | Nominal | Unique ID |
| department | Nominal | Business department |
| job_role | Nominal | Consistent with department |
| job_level | Ordinal | Entry, Associate, Senior, Lead, Manager |
| performance_rating | Ordinal | Poor through Excellent |
| projects_completed | Discrete | Non-negative integer |
| overtime_days | Discrete | Monthly whole-number count |
| training_hours | Continuous | 0 to 100 |
| monthly_salary | Continuous | Positive value |
| joining_year | Interval | 2000 to 2026 |
| attrition | Nominal | Yes or No |

### Prompt for Microsoft Copilot

~~~text
Generate exactly 10,000 synthetic employee workforce records using pandas, NumPy, and Faker. Follow the common requirements.

Include employee_id, department, job_role, job_level, performance_rating, projects_completed, overtime_days, training_hours, monthly_salary, joining_year, and attrition. Department, role, and attrition are nominal. Job level and performance rating are ordinal. Project and overtime counts are discrete. Training hours and salary are continuous. Joining year is interval.

Keep roles consistent with departments. Make salary generally increase with job level and experience. Make attrition somewhat more likely with high overtime, low performance, and entry-level jobs, but do not make it perfectly predictable. Validate and save to datasets/04_employee_workforce.csv. Do not use plotting libraries.
~~~

---

## Dataset 5: Banking Customer Risk

Output file: datasets/05_banking_customer_risk.csv

| Column | Classification | Rules |
|---|---|---|
| customer_id | Nominal | Unique ID |
| account_type | Nominal | Savings, Current, Salary, Business |
| occupation_group | Nominal | High-level occupation |
| risk_grade | Ordinal | Very Low through Very High |
| monthly_transactions | Discrete | Non-negative integer |
| missed_payments | Discrete | 0 to 12 |
| account_balance | Continuous | Monetary value |
| monthly_income | Continuous | Positive value |
| credit_score | Interval | 300 to 850 |
| loan_amount | Continuous | Non-negative value |
| defaulted | Nominal | Yes or No |

### Prompt for Microsoft Copilot

~~~text
Create exactly 10,000 synthetic banking risk records using pandas, NumPy, and Faker. Follow the common requirements.

Create customer_id, account_type, occupation_group, risk_grade, monthly_transactions, missed_payments, account_balance, monthly_income, credit_score, loan_amount, and defaulted. Account type, occupation, and default status are nominal. Risk grade is ordinal with Very Low < Low < Medium < High < Very High. Transaction and missed-payment counts are discrete. Balance, income, and loan amount are continuous. Treat credit score as interval for this exercise.

Lower credit scores, more missed payments, higher loan-to-income values, and higher risk grades should increase default probability without making default perfectly predictable. Validate the dataset and save it as datasets/05_banking_customer_risk.csv. Do not create charts.
~~~

---

## Dataset 6: Manufacturing Quality and Maintenance

Output file: datasets/06_manufacturing_quality.csv

| Column | Classification | Rules |
|---|---|---|
| inspection_id | Nominal | Unique ID |
| machine_type | Nominal | CNC, Press, Lathe, Welder, Conveyor |
| plant | Nominal | Plant identifier |
| defect_severity | Ordinal | None, Minor, Moderate, Major, Critical |
| defects_count | Discrete | Non-negative integer |
| error_events | Discrete | Non-negative integer |
| vibration_mm_s | Continuous | Positive measurement |
| pressure_bar | Continuous | Positive measurement |
| temperature_c | Interval | Plausible Celsius value |
| maintenance_cost | Continuous | Non-negative value |
| inspection_date | Date | Within the last two years |

### Prompt for Microsoft Copilot

~~~text
Generate exactly 10,000 synthetic manufacturing inspection records using pandas, NumPy, and Faker. Follow the common requirements.

Include inspection_id, machine_type, plant, defect_severity, defects_count, error_events, vibration_mm_s, pressure_bar, temperature_c, maintenance_cost, and inspection_date. Machine type and plant are nominal. Defect severity is ordinal with None < Minor < Moderate < Major < Critical. Defect and error counts are discrete. Vibration, pressure, and maintenance cost are continuous. Celsius temperature is interval.

Make elevated temperature, high vibration, and more error events associated with greater defect severity and maintenance cost. Keep values plausible and non-negative. Validate and save as datasets/06_manufacturing_quality.csv. Do not create visualizations.
~~~

---

## Dataset 7: Logistics and Delivery Performance

Output file: datasets/07_logistics_delivery_performance.csv

| Column | Classification | Rules |
|---|---|---|
| shipment_id | Nominal | Unique ID |
| shipping_mode | Nominal | Road, Rail, Air, Sea |
| destination_region | Nominal | Delivery region |
| delivery_priority | Ordinal | Low, Standard, High, Urgent |
| packages_count | Discrete | Positive integer |
| delay_days | Discrete | Non-negative integer |
| distance_km | Continuous | Positive value |
| freight_cost | Continuous | Positive value |
| warehouse_temperature_c | Interval | Celsius temperature |
| dispatch_year | Interval | 2022 to 2026 |
| delivered_on_time | Nominal | Yes or No |

### Prompt for Microsoft Copilot

~~~text
Generate exactly 10,000 synthetic logistics delivery records using pandas, NumPy, and Faker. Follow the common requirements.

Create shipment_id, shipping_mode, destination_region, delivery_priority, packages_count, delay_days, distance_km, freight_cost, warehouse_temperature_c, dispatch_year, and delivered_on_time. Shipping mode, destination, and on-time status are nominal. Priority is ordinal with Low < Standard < High < Urgent. Package and delay counts are discrete. Distance and freight cost are continuous. Warehouse temperature in Celsius and dispatch year are interval.

Make freight cost depend on distance, package count, priority, and shipping mode. Make long-distance road and sea shipments somewhat more likely to be delayed, while urgent shipments should generally have fewer delays. Derive delivered_on_time from delay_days. Validate and save as datasets/07_logistics_delivery_performance.csv. Do not create charts.
~~~

---

## Final validation prompt

After generating each dataset, paste this prompt into Copilot:

~~~text
Review my generated DataFrame and provide pandas validation code only. Confirm that it has exactly 10,000 rows, all required columns, a unique and non-null ID, allowed nominal values, correctly ordered ordinal values, whole numbers in discrete columns, valid ranges in continuous and interval columns, no impossible values, and the expected relationships between important columns. Read the saved CSV back and confirm its row and column counts. Return a compact validation summary table and do not create visualizations.
~~~

## Final submission checklist

- Seven separate CSV files are present in the datasets folder.
- Every CSV has exactly 10,000 rows.
- Every dataset contains nominal, ordinal, discrete, continuous, and interval columns.
- NumPy uses a fixed random seed.
- Faker uses a fixed seed.
- pandas creates, validates, and exports every dataset.
- IDs are unique and required values are not missing.
- Ordinal values follow the specified order.
- Discrete columns contain whole numbers.
- Continuous and interval values remain within valid ranges.
- Relationships are realistic but not perfectly predictable.
- Each saved CSV can be read back successfully.
- No charts or visualizations are created.

