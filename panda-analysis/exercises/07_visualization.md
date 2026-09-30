# Module 7: Visualization

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 8: Visualization

### Cell 34: Bar chart of category revenue

Question: Visualize total net sales by product category.

Guidelines:

- Use a horizontal bar chart.
- Sort categories from highest to lowest.
- Label axes clearly.

```python
plt.figure(figsize=(10, 5))
category_summary["total_net_sales"].sort_values().plot(kind="barh")
plt.title("Total Net Sales by Product Category")
plt.xlabel("Net Sales")
plt.ylabel("Product Category")
plt.tight_layout()
plt.show()
```

### Cell 35: Monthly revenue line chart

Question: Visualize monthly revenue over time.

Guidelines:

- Use a line chart.
- Plot `order_month_period` on the x-axis and `net_sales` on the y-axis.
- Look for seasonality, growth, or drops.

```python
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_summary, x="order_month_period", y="net_sales", marker="o")
plt.title("Monthly Net Sales Trend")
plt.xlabel("Month")
plt.ylabel("Net Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Cell 36: Distribution of order values

Question: What is the distribution of total order value?

Guidelines:

- Use a histogram.
- Try different bin sizes.
- Consider whether the distribution is skewed.

```python
plt.figure(figsize=(10, 5))
sns.histplot(df["total_order_value"], bins=40, kde=True)
plt.title("Distribution of Total Order Value")
plt.xlabel("Total Order Value")
plt.ylabel("Order Count")
plt.tight_layout()
plt.show()
```

### Cell 37: Boxplot by category

Question: How does order value vary by product category?

Guidelines:

- Use a boxplot.
- Rotate labels if needed.
- Identify categories with larger spread or high-value orders.

```python
plt.figure(figsize=(12, 5))
sns.boxplot(data=df, x="product_category", y="total_order_value")
plt.title("Order Value Distribution by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Order Value")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
```

### Cell 38: Heatmap from pivot table

Question: Visualize region-category net sales as a heatmap.

Guidelines:

- Remove the `All` row and column from the pivot before plotting.
- Use annotations if the table is small enough.

```python
heatmap_data = sales_pivot.drop(index="All", errors="ignore").drop(columns="All", errors="ignore")

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".0f")
plt.title("Net Sales Heatmap by Region and Product Category")
plt.xlabel("Product Category")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
```

### Cell 39: Scatter plot of discount and sales

Question: Does a higher discount appear related to higher net sales?

Guidelines:

- Use a scatter plot.
- Plot `discount_pct` against `net_sales`.
- Use `product_category` as hue.

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df.sample(min(2000, len(df)), random_state=42), x="discount_pct", y="net_sales", hue="product_category", alpha=0.6)
plt.title("Discount Percentage vs Net Sales")
plt.xlabel("Discount Percentage")
plt.ylabel("Net Sales")
plt.tight_layout()
plt.show()
```

### Cell 40: Late shipping comparison

Question: Compare customer rating for late and on-time shipments.

Guidelines:

- Use a bar chart or boxplot.
- Filter to rows where `shipping_days` is not missing.
- Compare average rating and rating distribution.

```python
shipping_rating = df.dropna(subset=["shipping_days"])

plt.figure(figsize=(7, 5))
sns.boxplot(data=shipping_rating, x="is_late_shipping", y="customer_rating")
plt.title("Customer Rating by Late Shipping Flag")
plt.xlabel("Late Shipping")
plt.ylabel("Customer Rating")
plt.tight_layout()
plt.show()
```

