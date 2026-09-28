# Analytics Practice: 25 Questions

Use the CSV files in the `datasets` folder to answer the following questions with pandas.

## Rules

- Do not create charts or visualizations.
- Do not import Matplotlib, Seaborn, Plotly, or other plotting libraries.
- Present answers as pandas Series, DataFrames, pivot tables, rankings, percentages, or short written conclusions.
- Show the pandas code used to produce every answer.
- Round monetary values and percentages to two decimal places where appropriate.
- State any assumptions made during the analysis.

## Retail Sales

Dataset: `01_retail_sales.csv`

1. Calculate total orders, units sold, revenue, cost, profit, average order value, overall profit margin, and return rate.

2. Rank all product categories by revenue. For each category, also show units sold, profit, profit margin, revenue share, average discount, and return rate.

3. Identify the five best-selling products by units sold and the five highest-performing products by profit. Explain whether the two rankings are the same.

4. Create a monthly performance table containing orders, revenue, profit, profit margin, and month-over-month revenue growth. Which three months generated the highest revenue?

5. Compare regions and sales channels using order count, average order value, revenue, profit, and return rate. Which region-channel combination performs best based on both revenue and profit?

## Customer Churn

Dataset: `02_customer_churn.csv`

6. Calculate the overall churn rate and compare churn rates across Basic, Standard, and Premium plans.

7. Compare churned and retained customers using average tenure, monthly charges, usage hours, support tickets, satisfaction score, and late payments.

8. Create a churn table by contract type and autopay status. Which combination has the highest churn rate, and which has the lowest?

9. Group customers into tenure bands of `1-12`, `13-24`, `25-48`, and `49-72` months. Calculate customer count, average total charges, and churn rate for each band.

10. Identify the customer characteristics most associated with churn by comparing churn rates across satisfaction scores, support-ticket counts, and late-payment counts. Write three evidence-based observations.

## Supply Chain

Dataset: `03_supply_chain.csv`

11. Calculate the overall on-time delivery rate, stockout rate, average lead-time delay, total freight cost, and average defect rate.

12. Rank suppliers using on-time delivery rate, average delay, defect rate, stockout rate, freight cost per unit, and supplier rating. Which supplier appears most reliable?

13. Compare shipping modes by shipment count, average distance, planned lead time, actual lead time, on-time rate, and average freight cost.

14. Determine which product category and destination region combination has the highest stockout rate. Include only combinations with at least 50 shipments.

## HR Attrition

Dataset: `04_hr_attrition.csv`

15. Calculate overall employee attrition and compare attrition rates by department and job role. Include employee count and average monthly income.

16. Compare employees who left with employees who stayed using years at company, monthly income, overtime, training hours, job satisfaction, absenteeism, and promotion status.

17. Create experience bands of `0-2`, `3-5`, `6-10`, `11-15`, and `16+` years. Calculate employee count, average income, promotion rate, and attrition rate for each band.

18. Analyze how overtime and job satisfaction interact. Which overtime-satisfaction combination has the highest attrition rate? Exclude groups with fewer than 30 employees.

## Marketing Campaigns

Dataset: `05_marketing_campaigns.csv`

19. Calculate total impressions, clicks, conversions, spend, revenue, overall click-through rate, conversion rate, return on ad spend, and profit.

20. Rank marketing channels by return on ad spend. Also show impressions, clicks, conversions, spend, revenue, click-through rate, and conversion rate.

21. Compare campaign performance across audience segments and devices. Which audience-device combination produces the highest conversion rate and return on ad spend? Include only combinations with at least 20 records.

22. Create a monthly campaign table containing spend, revenue, conversions, profit, return on ad spend, and month-over-month revenue growth. Identify the three most profitable months.

## Predictive Maintenance

Dataset: `06_predictive_maintenance.csv`

23. Compare records with and without a failure within seven days using temperature, vibration, pressure, rotational speed, operating hours, days since maintenance, error count, and energy consumption.

24. Calculate failure rate and maintenance-required rate by machine type and plant. Which machine type-plant combination has the highest failure rate? Include only combinations with at least 100 sensor records.

25. Create risk bands using temperature, vibration, days since maintenance, and error count. Produce a table showing record count, maintenance-required rate, and seven-day failure rate for each risk band, then explain whether failure rate rises with risk.

## Submission Checklist

- All 25 questions are answered.
- Every answer includes executable pandas code.
- Results are displayed only as tables, values, rankings, or written observations.
- No visualizations or plotting libraries are used.
- Percentages and monetary values are clearly labelled and rounded.
- Final conclusions are supported by calculated results.

