# Module 6: Aggregation

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 7: Aggregation

### Cell 29: Revenue by product category

Question: Which product categories generate the highest total net sales?

Guidelines:

- Group by `product_category`.
- Aggregate order count, total net sales, average order value, and average discount.
- Sort by total net sales descending.

```python
category_summary = (
    df.groupby("product_category")
    .agg(
        orders=("order_id", "count"),
        total_net_sales=("net_sales", "sum"),
        avg_order_value=("total_order_value", "mean"),
        avg_discount=("discount_pct", "mean")
    )
    .sort_values("total_net_sales", ascending=False)
)

category_summary
```

### Cell 30: Monthly trend aggregation

Question: How do orders and revenue trend over time?

Guidelines:

- Group by monthly period.
- Aggregate order count and net sales.
- Convert the period to timestamp for plotting.

```python
monthly_summary = (
    df.groupby(df["order_date"].dt.to_period("M"))
    .agg(orders=("order_id", "count"), net_sales=("net_sales", "sum"))
    .reset_index()
)

monthly_summary["order_month_period"] = monthly_summary["order_date"].dt.to_timestamp()
monthly_summary.head()
```

### Cell 31: Region and channel performance

Question: Which region and sales channel combinations perform best?

Guidelines:

- Group by `region` and `sales_channel`.
- Calculate total net sales and average rating.
- Sort from highest to lowest net sales.

```python
region_channel_summary = (
    df.groupby(["region", "sales_channel"])
    .agg(
        orders=("order_id", "count"),
        net_sales=("net_sales", "sum"),
        avg_rating=("customer_rating", "mean")
    )
    .sort_values("net_sales", ascending=False)
)

region_channel_summary.head(15)
```

### Cell 32: Pivot table

Question: Build a pivot table showing net sales by region and product category.

Guidelines:

- Use `pd.pivot_table`.
- Fill missing combinations with zero.
- Add row and column totals if useful.

```python
sales_pivot = pd.pivot_table(
    df,
    values="net_sales",
    index="region",
    columns="product_category",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

sales_pivot
```

### Cell 33: Return rate analysis

Question: Which categories or channels have the highest return rate?

Guidelines:

- Use `is_returned`.
- Compare return rate by category and sales channel.
- Return rate is the mean of the boolean column.

```python
return_rate = (
    df.groupby(["product_category", "sales_channel"])
    .agg(return_rate=("is_returned", "mean"), orders=("order_id", "count"))
    .sort_values("return_rate", ascending=False)
)

return_rate.head(15)
```

