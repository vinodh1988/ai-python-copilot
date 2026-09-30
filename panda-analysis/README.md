# Pandas Data Preparation and Analysis

A hands-on, cell-by-cell exercise project for learning data preparation, cleansing, feature engineering, aggregation, and visualization with pandas.

## Dataset

Use `data/customer_orders_dirty_10000.csv`. It contains 10,000 deliberately imperfect customer-order records, including missing values, duplicate order IDs, inconsistent text, invalid dates, impossible numeric values, and outliers.

## Exercise Order

1. [Setup and Initial Data Profiling](exercises/01_setup_and_profiling.md) - Cells 1-6
2. [Missing Values](exercises/02_missing_values.md) - Cells 7-12
3. [Text and Date Cleaning](exercises/03_text_and_date_cleaning.md) - Cells 13-18
4. [Duplicates, Invalid Values, and Outliers](exercises/04_duplicates_invalid_values_and_outliers.md) - Cells 19-24
5. [Derived Columns and Final Validation](exercises/05_derived_columns_and_validation.md) - Cells 25-28
6. [Aggregation](exercises/06_aggregation.md) - Cells 29-33
7. [Visualization](exercises/07_visualization.md) - Cells 34-40
8. [Challenge Exercises](exercises/08_challenge_exercises.md) - Cells 41-45

## Learning Goals

- Load and inspect a raw CSV dataset.
- Identify data quality issues before modifying data.
- Clean missing, invalid, duplicated, and inconsistent records.
- Create derived columns for business analysis.
- Aggregate prepared data into useful summaries.
- Visualize trends, comparisons, distributions, and relationships.

## How to Work

Create a notebook in this folder and complete each Markdown exercise as a separate notebook cell. Keep the notebook working directory at the project root so `data/customer_orders_dirty_10000.csv` resolves correctly. Complete the modules in order because each one builds on the prepared DataFrame from the previous module.
