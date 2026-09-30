# Module 3: Text and Date Cleaning

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Section 3: Text Cleaning and Standardization

### Cell 13: Clean whitespace

Question: Remove leading and trailing spaces from all text columns.

Guidelines:

- Select object columns.
- Use `.str.strip()`.

```python
object_cols = df.select_dtypes(include="object").columns
for col in object_cols:
    df[col] = df[col].str.strip()
```

### Cell 14: Standardize casing

Question: Standardize categorical text values so duplicate categories collapse correctly.

Guidelines:

- Use title case for fields like `region`, `customer_segment`, `product_category`, `sales_channel`, `payment_method`, and `order_status`.
- Check unique values before and after.

```python
standardize_cols = ["region", "customer_segment", "product_category", "sales_channel", "payment_method", "order_status"]
for col in standardize_cols:
    df[col] = df[col].str.title()

{col: sorted(df[col].dropna().unique())[:20] for col in standardize_cols}
```

### Cell 15: Fix remaining blank categories

Question: Correct empty strings that still remain after stripping spaces.

Guidelines:

- Replace empty strings with `"Unknown"`.
- Recheck unique values for important categorical columns.

```python
for col in object_cols:
    df[col] = df[col].replace("", "Unknown")

{col: sorted(df[col].dropna().unique())[:20] for col in standardize_cols}
```

## Section 4: Date Cleaning

### Cell 16: Convert date columns

Question: Convert `order_date` and `ship_date` to datetime values.

Guidelines:

- Use `errors="coerce"` so invalid dates become missing values.
- Count how many invalid or missing dates remain.

```python
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

df[["order_date", "ship_date"]].isna().sum()
```

### Cell 17: Remove rows with invalid order dates

Question: Should rows with missing or invalid `order_date` be removed?

Guidelines:

- `order_date` is critical for trend analysis.
- Drop rows where `order_date` is missing.
- Report rows before and after.

```python
before = len(df)
df = df.dropna(subset=["order_date"])
after = len(df)
before, after, before - after
```

### Cell 18: Calculate shipping delay

Question: Create a `shipping_days` column from `ship_date - order_date`.

Guidelines:

- Use `.dt.days`.
- Keep missing shipping days for orders without valid ship dates.
- Later, compare by `order_status`.

```python
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days
df[["order_date", "ship_date", "shipping_days"]].head()
```

