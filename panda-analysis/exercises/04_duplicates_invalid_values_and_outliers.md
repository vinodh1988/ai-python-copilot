# Module 4: Duplicates, Invalid Values, and Outliers

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 5: Duplicates and Invalid Values

### Cell 19: Detect duplicate orders

Question: How many duplicate `order_id` values exist?

Guidelines:

- Use `.duplicated()`.
- Display all duplicate rows sorted by `order_id`.

```python
duplicate_orders = df[df.duplicated("order_id", keep=False)].sort_values("order_id")
duplicate_orders
```

### Cell 20: Remove duplicate orders

Question: Remove duplicated `order_id` records, keeping the first occurrence.

Guidelines:

- Record row count before and after.
- Explain why `order_id` should be unique.

```python
before = len(df)
df = df.drop_duplicates(subset="order_id", keep="first")
after = len(df)
before, after, before - after
```

### Cell 21: Identify invalid quantity and discount values

Question: Which rows contain invalid `quantity` or `discount_pct` values?

Guidelines:

- Quantity should be greater than zero.
- Discount should be between 0 and 1.

```python
invalid_quantity = df[df["quantity"] <= 0]
invalid_discount = df[(df["discount_pct"] < 0) | (df["discount_pct"] > 1)]

len(invalid_quantity), len(invalid_discount)
```

### Cell 22: Clean invalid quantity and discount values

Question: Clean invalid quantities and discounts using defensible business rules.

Guidelines:

- Replace quantity less than or equal to zero with 1.
- Cap discount below 0 at 0 and above 1 at 1.

```python
df.loc[df["quantity"] <= 0, "quantity"] = 1
df["discount_pct"] = df["discount_pct"].clip(lower=0, upper=1)
```

### Cell 23: Detect outliers

Question: Find possible outliers in `unit_price`, `shipping_cost`, and `quantity`.

Guidelines:

- Use boxplots and percentile checks.
- Decide whether outliers are errors or rare but valid transactions.

```python
df[["unit_price", "shipping_cost", "quantity"]].quantile([0.01, 0.25, 0.5, 0.75, 0.99])
```

### Cell 24: Treat extreme unit price outliers

Question: Cap extreme `unit_price` values using the 99th percentile.

Guidelines:

- Create `unit_price_capped`.
- Do not overwrite the original price until you are confident.

```python
p99_price = df["unit_price"].quantile(0.99)
df["unit_price_capped"] = df["unit_price"].clip(upper=p99_price)
```

