# Module 8: Challenge Exercises

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 9: Challenge Exercises

### Cell 41: Build a reusable cleaning function

Question: Convert the cleaning logic into a function named `clean_orders_data(raw_df)`.

Guidelines:

- The function should accept a raw DataFrame and return a cleaned DataFrame.
- Do not mutate the input DataFrame.
- Include text cleaning, missing value treatment, date conversion, duplicate removal, invalid value handling, and derived columns.

### Cell 42: Export cleaned data

Question: Save the cleaned DataFrame as `data/customer_orders_cleaned.csv`.

Guidelines:

- Use `index=False`.
- Reload the file to confirm it was written correctly.

```python
df.to_csv("data/customer_orders_cleaned.csv", index=False)
pd.read_csv("data/customer_orders_cleaned.csv").head()
```

### Cell 43: Executive summary table

Question: Create a one-table summary for business stakeholders.

Guidelines:

- Include total orders, total net sales, average order value, return rate, late shipping rate, and average rating.
- Format values for readability.

```python
executive_summary = pd.DataFrame({
    "metric": [
        "Total Orders",
        "Total Net Sales",
        "Average Order Value",
        "Return Rate",
        "Late Shipping Rate",
        "Average Rating"
    ],
    "value": [
        len(df),
        df["net_sales"].sum(),
        df["total_order_value"].mean(),
        df["is_returned"].mean(),
        df["is_late_shipping"].mean(),
        df["customer_rating"].mean()
    ]
})

executive_summary
```

### Cell 44: Write insights

Question: Write five business insights from your cleaned, aggregated, and visualized data.

Guidelines:

- At least two insights should come from aggregations.
- At least two insights should come from visualizations.
- Each insight should mention the evidence used.
- Include one recommended business action.

### Cell 45: Reflection

Question: Which cleaning decision had the largest impact on the analysis?

Guidelines:

- Compare row counts, missing values, duplicate counts, and revenue before and after cleaning.
- Explain how bad data could mislead aggregation and visualization results.

