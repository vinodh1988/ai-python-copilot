# Excel Analytics: Pivot Aggregation and Projection Questions

## Objective

Use Microsoft Excel PivotTables to analyze the seven generated CSV datasets. For each dataset, create PivotTables that aggregate key measures by categorical fields, compare ordinal groups, and project future outcomes using PivotTable summaries with calculated fields, formulas, or forecast sheets where appropriate.

## General PivotTable Instructions

For each CSV file:

1. Import the CSV into Excel as a table.
2. Create at least one PivotTable per question.
3. Use rows, columns, values, and filters to summarize the data.
4. Use sums, averages, counts, minimums, maximums, and percentages where relevant.
5. Format monetary values, percentages, and dates correctly.
6. Add slicers or filters for at least one nominal or ordinal column.
7. For projection questions, use PivotTable results as the source for formulas, trend calculations, or Excel Forecast Sheet.
8. Create the required PivotCharts in the same worksheet segment as their related PivotTables, with a clear title, axis labels, legend, and data labels where useful.

---

## Dataset 1: Retail Customer Purchases

File: `datasets/01_retail_customer_purchases.csv`

1. Create a PivotTable showing total `sales_amount` by `region` and `product_category`. Which region-category combination generates the highest revenue?
2. Calculate average `discount_pct` by `loyalty_tier`. Do higher loyalty tiers receive higher average discounts?
3. Aggregate total `items_purchased` and average `unit_price` by `product_category`. Which product category has the highest purchase volume?
4. Group `purchase_date` by month and year, then calculate monthly total `sales_amount`. Which months show the strongest sales?
5. Project next quarter sales by using the monthly sales PivotTable and a simple moving average or Excel forecast. Which region is expected to contribute the most sales?
6. Create a calculated field or helper column for customer age using `customer_birth_year`, then use a PivotTable to compare average `sales_amount` by age group and loyalty tier.
7. Create a clustered column PivotChart showing total `sales_amount` by `region`, with `product_category` as the series. Add a timeline for `purchase_date` and a slicer for `loyalty_tier`. Which categories drive the leading region's sales?

---

## Dataset 2: Healthcare Patient Visits

File: `datasets/02_healthcare_patient_visits.csv`

1. Create a PivotTable counting `visit_id` by `diagnosis_category` and `pain_level`. Which diagnosis category has the most severe or critical cases?
2. Calculate average `treatment_cost` and average `waiting_time_minutes` by `diagnosis_category`.
3. Aggregate average `medications_count` by `pain_level`. Does medication count increase with pain severity?
4. Group `visit_date` by month and calculate total visits and average treatment cost over time.
5. Project next six months of visit volume using monthly visit counts from the PivotTable.
6. Compare average `body_temperature_c` by `pain_level` and `diagnosis_category`. Which groups show elevated temperature patterns?
7. Create a combo PivotChart showing monthly visit count as columns and average `treatment_cost` as a line on a secondary axis. Add a slicer for `diagnosis_category`. Do higher visit volumes coincide with higher average costs?

---

## Dataset 3: Student Learning Performance

File: `datasets/03_student_learning_performance.csv`

1. Create a PivotTable showing average `final_score` by `school_type` and `subject_stream`.
2. Count students by `engagement_level` and `passed`. What pass rate does each engagement level achieve?
3. Aggregate average `study_hours_per_week`, average `assignments_completed`, and average `absences` by `engagement_level`.
4. Use `examination_year` as rows and calculate yearly average `final_score` and pass rate.
5. Project next year average `final_score` by `subject_stream` using yearly PivotTable trends.
6. Create score bands such as 0-39, 40-59, 60-79, and 80-100, then use a PivotTable to compare score distribution across school types.
7. Create a 100% stacked column PivotChart showing the pass/fail percentage by `engagement_level`, with a slicer for `school_type`. Which engagement level has the strongest pass-rate profile?

---

## Dataset 4: Employee Workforce Analytics

File: `datasets/04_employee_workforce.csv`

1. Create a PivotTable showing average `monthly_salary` by `department` and `job_level`.
2. Count employees by `department`, `job_role`, and `attrition`. Which departments have the highest attrition count?
3. Calculate attrition rate by `job_level` and `performance_rating`.
4. Aggregate average `overtime_days`, `training_hours`, and `projects_completed` by `performance_rating`.
5. Use `joining_year` to summarize employee count by year, then project workforce size for the next two years.
6. Compare average salary and average projects completed for employees with `attrition` = Yes versus No.
7. Create a bar PivotChart showing attrition rate by `department`, split by `job_level`. Add slicers for `performance_rating` and `job_role`. Which department-level combination needs the most attention?

---

## Dataset 5: Banking Customer Risk

File: `datasets/05_banking_customer_risk.csv`

1. Create a PivotTable showing count of customers by `risk_grade` and `defaulted`.
2. Calculate default rate by `account_type` and `occupation_group`.
3. Aggregate average `credit_score`, `monthly_income`, `loan_amount`, and `account_balance` by `risk_grade`.
4. Create a helper column for loan-to-income ratio, then summarize average ratio by `risk_grade` and `defaulted`.
5. Use `missed_payments` groups such as 0, 1-3, 4-6, 7-9, and 10-12 to compare default rates.
6. Project potential default exposure by multiplying default rate by total `loan_amount` for each risk grade.
7. Create a combo PivotChart showing total `loan_amount` as columns and default rate as a line by `risk_grade`. Add slicers for `account_type` and `occupation_group`. Which risk grade combines high exposure with a high default rate?

---

## Dataset 6: Manufacturing Quality and Maintenance

File: `datasets/06_manufacturing_quality.csv`

1. Create a PivotTable showing total `defects_count` by `machine_type` and `plant`.
2. Calculate average `maintenance_cost` by `defect_severity`.
3. Aggregate average `vibration_mm_s`, `pressure_bar`, `temperature_c`, and `error_events` by `machine_type`.
4. Group `inspection_date` by month and summarize total defects and total maintenance cost.
5. Project next quarter maintenance cost using monthly PivotTable totals.
6. Compare defect severity distribution by plant. Which plant has the highest percentage of major or critical inspections?
7. Create a line PivotChart showing monthly total `defects_count` and monthly total `maintenance_cost`, using a secondary axis where needed. Add slicers for `plant` and `machine_type`. Do defect spikes align with maintenance-cost increases?

---

## Dataset 7: Logistics and Delivery Performance

File: `datasets/07_logistics_delivery_performance.csv`

1. Create a PivotTable showing average `freight_cost` by `shipping_mode` and `delivery_priority`.
2. Calculate total `packages_count` and average `delay_days` by `destination_region`.
3. Count shipments by `shipping_mode` and `delivered_on_time`. Which shipping mode has the best on-time percentage?
4. Aggregate average `distance_km`, total `freight_cost`, and average `delay_days` by `delivery_priority`.
5. Use `dispatch_year` to summarize yearly shipment count and freight cost, then project next year freight cost.
6. Create distance bands such as 0-500, 501-1500, 1501-3000, and 3000+, then compare delay performance across shipping modes.
7. Create a combo PivotChart showing shipment count as columns and on-time delivery percentage as a line by `shipping_mode`. Add slicers for `destination_region` and `delivery_priority`. Which mode balances volume and reliability best?

---

## Cross-Dataset Challenge Questions

1. Which dataset shows the strongest relationship between an ordinal category and a continuous measure when summarized in a PivotTable?
2. Across retail, banking, manufacturing, and logistics, which dataset has the highest monetary total?
3. Compare percentage outcomes across datasets: retail discount rate, student pass rate, employee attrition rate, banking default rate, and logistics on-time rate.
4. Build one executive summary sheet with a PivotTable output from each dataset and one short written insight for each.
5. For each dataset, identify one metric that can be projected forward and explain which historical grouping should be used for the projection.
6. Build an executive dashboard containing one KPI and one PivotChart from each dataset. Use consistent titles, number formats, and colors, and include slicers or timelines where they improve comparison. Which three visual findings are most important for decision-makers?
