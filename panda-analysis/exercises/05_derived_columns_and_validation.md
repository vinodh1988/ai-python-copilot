# Module 5: Derived Columns and Final Validation

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 6: Derived Columns

### Cell 25: Revenue calculations

Question: Create gross, discount, net, and total order value columns.

Guidelines:

- `gross_sales = quantity * unit_price_capped`
- `discount_amount = gross_sales * discount_pct`
- `net_sales = gross_sales - discount_amount`
- `total_order_value = net_sales + shipping_cost`

```python
df["gross_sales"] = df["quantity"] * df["unit_price_capped"]
df["discount_amount"] = df["gross_sales"] * df["discount_pct"]
df["net_sales"] = df["gross_sales"] - df["discount_amount"]
df["total_order_value"] = df["net_sales"] + df["shipping_cost"]
```

### Cell 26: Date-derived columns

Question: Create year, month, quarter, month name, and weekday columns from `order_date`.

Guidelines:

- These columns support aggregation and visualization.
- Use `.dt` accessors.

```python
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["order_quarter"] = df["order_date"].dt.to_period("Q").astype(str)
df["order_month_name"] = df["order_date"].dt.month_name()
df["order_weekday"] = df["order_date"].dt.day_name()
```

### Cell 27: Business rule columns

Question: Create columns that classify transactions into useful business groups.

Guidelines:

- Create `order_size` from `total_order_value`.
- Create `is_returned` from `order_status`.
- Create `is_late_shipping` where `shipping_days` is greater than 7.

```python
df["order_size"] = pd.cut(
    df["total_order_value"],
    bins=[-np.inf, 100, 500, 1000, np.inf],
    labels=["Small", "Medium", "Large", "Premium"]
)

df["is_returned"] = df["order_status"].eq("Returned")
df["is_late_shipping"] = df["shipping_days"] > 7
```

### Cell 28: Final validation

Question: Validate that the cleaned dataset is ready for analysis.

Guidelines:

- Check missing values.
- Confirm no duplicate `order_id`.
- Confirm no invalid quantity or discount remains.

```python
validation = {
    "rows": len(df),
    "duplicate_order_ids": df.duplicated("order_id").sum(),
    "invalid_quantity": (df["quantity"] <= 0).sum(),
    "invalid_discount": ((df["discount_pct"] < 0) | (df["discount_pct"] > 1)).sum(),
    "missing_by_column": df.isna().sum().sort_values(ascending=False).head(10)
}

validation
```

