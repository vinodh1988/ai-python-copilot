# Module 2: Missing Values

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 2: Missing Values

### Cell 7: Find missing values

Question: Which columns contain missing values, and which missing values are most important for analysis?

Guidelines:

- Display only columns where missing count is greater than zero.
- Classify each missing column as critical, useful, or optional.

```python
missing = df_raw.isna().sum()
missing[missing > 0].sort_values(ascending=False)
```

### Cell 8: Missing values by category

Question: Are missing values concentrated in specific product categories or sales channels?

Guidelines:

- Group by `product_category` and `sales_channel`.
- Compare missing `unit_price`, `customer_rating`, and `ship_date`.

```python
df_raw.groupby("product_category")[["unit_price", "customer_rating", "ship_date"]].apply(lambda x: x.isna().mean() * 100)
```

### Cell 9: Create a working copy

Question: Create a new DataFrame named `df` for cleaning while preserving the raw data.

Guidelines:

- Use `.copy()`.
- All future transformations should use `df`.

```python
df = df_raw.copy()
```

### Cell 10: Impute missing customer names

Question: Fill missing `customer_name` values using a clear placeholder.

Guidelines:

- Use `"Unknown Customer"`.
- Check the missing count after filling.

```python
df["customer_name"] = df["customer_name"].fillna("Unknown Customer")
df["customer_name"].isna().sum()
```

### Cell 11: Handle missing categorical values

Question: Fill missing categorical fields with `"Unknown"` where dropping rows would lose useful transaction data.

Guidelines:

- Apply this to columns like `region`, `state`, `city`, `customer_segment`, `product_category`, `sales_channel`, `payment_method`, and `marketing_source`.
- Keep a list of columns so the operation is repeatable.

```python
categorical_cols = [
    "region", "state", "city", "customer_segment", "product_category",
    "sales_channel", "payment_method", "marketing_source"
]

df[categorical_cols] = df[categorical_cols].fillna("Unknown")
df[categorical_cols].isna().sum()
```

### Cell 12: Handle missing numeric values

Question: Decide how to fill missing `unit_price` and `customer_rating`.

Guidelines:

- Fill `unit_price` with the median price by `product_category`.
- Fill remaining missing prices with the overall median.
- Fill `customer_rating` with the median rating.

```python
df["unit_price"] = df["unit_price"].fillna(
    df.groupby("product_category")["unit_price"].transform("median")
)
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].median())
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())
```

