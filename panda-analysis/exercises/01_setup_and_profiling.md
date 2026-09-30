# Module 1: Setup and Initial Data Profiling

> Work through this module cell by cell. Run the modules in numeric order because later exercises use variables and cleaned columns created earlier. Start the notebook from the `panda-analysis` project folder so the dataset path `data/customer_orders_dirty_10000.csv` resolves correctly.
## Suggested Setup

### Cell 1: Import libraries

Question: Import the Python libraries needed for data preparation and visualization.

Guidelines:

- Use `pandas` and `numpy` for data work.
- Use `matplotlib.pyplot` and `seaborn` for charts.
- Set display options so you can see enough rows and columns.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", 50)
sns.set_theme(style="whitegrid")
```

### Cell 2: Load the CSV

Question: Load `data/customer_orders_dirty_10000.csv` into a DataFrame named `df_raw`.

Guidelines:

- Use `pd.read_csv`.
- Do not clean anything in this cell.
- Display the first five rows.

```python
df_raw = pd.read_csv("data/customer_orders_dirty_10000.csv")
df_raw.head()
```

### Cell 3: Basic shape and structure

Question: How many rows and columns are present? What are the column names and data types?

Guidelines:

- Use `.shape`, `.columns`, and `.info()`.
- Write two observations about the dataset structure.

```python
df_raw.shape
df_raw.info()
```

## Section 1: Initial Data Profiling

### Cell 4: Preview random records

Question: Inspect a random sample of 10 records. What visible quality issues can you find?

Guidelines:

- Use `.sample(10, random_state=42)`.
- Look for blanks, inconsistent casing, odd numeric values, and invalid dates.

```python
df_raw.sample(10, random_state=42)
```

### Cell 5: Summary statistics

Question: Generate descriptive statistics for numeric and categorical columns.

Guidelines:

- Use `.describe()` for numeric columns.
- Use `.describe(include="object")` for text columns.
- Identify possible outliers and high-cardinality fields.

```python
df_raw.describe()
df_raw.describe(include="object")
```

### Cell 6: Data quality checklist

Question: Create a quick profiling table showing missing count, missing percentage, unique count, and data type for every column.

Guidelines:

- Use `.isna().sum()`, `.nunique()`, and `.dtypes`.
- Sort by missing percentage descending.

```python
profile = pd.DataFrame({
    "dtype": df_raw.dtypes,
    "missing_count": df_raw.isna().sum(),
    "missing_pct": df_raw.isna().mean() * 100,
    "unique_count": df_raw.nunique(dropna=True)
}).sort_values("missing_pct", ascending=False)

profile
```

