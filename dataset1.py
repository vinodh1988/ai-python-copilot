"""Generate Dataset 1: synthetic retail customer purchases."""

from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker


ROW_COUNT = 10_000
RANDOM_SEED = 42
REFERENCE_DATE = date(2026, 9, 28)
OUTPUT_PATH = (
    Path(__file__).resolve().parent
    / "datafolder"
    / "01_retail_customer_purchases.csv"
)

REGIONS = ["North", "South", "East", "West", "Central"]
PRODUCT_CATEGORIES = ["Electronics", "Clothing", "Home", "Grocery", "Sports"]
LOYALTY_TIERS = ["Bronze", "Silver", "Gold", "Platinum"]


def generate_retail_data(row_count: int = ROW_COUNT) -> pd.DataFrame:
    """Return a reproducible synthetic retail purchase DataFrame."""
    rng = np.random.default_rng(RANDOM_SEED)
    Faker.seed(RANDOM_SEED)
    fake = Faker()

    region = rng.choice(REGIONS, size=row_count, p=[0.20, 0.24, 0.21, 0.22, 0.13])
    product_category = rng.choice(
        PRODUCT_CATEGORIES,
        size=row_count,
        p=[0.24, 0.21, 0.20, 0.23, 0.12],
    )
    loyalty_tier = rng.choice(
        LOYALTY_TIERS,
        size=row_count,
        p=[0.42, 0.32, 0.19, 0.07],
    )

    tier_item_effect = {
        "Bronze": 0.0,
        "Silver": 0.5,
        "Gold": 1.0,
        "Platinum": 1.8,
    }
    item_lambda = 2.2 + np.array([tier_item_effect[tier] for tier in loyalty_tier])
    items_purchased = np.clip(rng.poisson(item_lambda) + 1, 1, 15).astype(int)

    category_base_price = {
        "Electronics": 160.0,
        "Clothing": 55.0,
        "Home": 90.0,
        "Grocery": 18.0,
        "Sports": 75.0,
    }
    base_prices = np.array(
        [category_base_price[category] for category in product_category]
    )
    unit_price = np.maximum(
        2.0,
        rng.lognormal(np.log(base_prices), 0.35),
    ).round(2)

    tier_discount = {
        "Bronze": 2.0,
        "Silver": 7.0,
        "Gold": 13.0,
        "Platinum": 20.0,
    }
    discount_average = np.array([tier_discount[tier] for tier in loyalty_tier])
    discount_pct = np.clip(rng.normal(discount_average, 3.5), 0, 35).round(2)
    sales_amount = (
        items_purchased * unit_price * (1 - discount_pct / 100)
    ).round(2)

    start_date = date(
        REFERENCE_DATE.year - 3,
        REFERENCE_DATE.month,
        REFERENCE_DATE.day,
    )
    purchase_dates = [
        fake.date_between_dates(date_start=start_date, date_end=REFERENCE_DATE)
        for _ in range(row_count)
    ]

    data = pd.DataFrame(
        {
            "transaction_id": [
                f"TXN-{number:07d}" for number in range(1, row_count + 1)
            ],
            "customer_name": [fake.name() for _ in range(row_count)],
            "region": region,
            "product_category": product_category,
            "loyalty_tier": pd.Categorical(
                loyalty_tier,
                categories=LOYALTY_TIERS,
                ordered=True,
            ),
            "items_purchased": items_purchased,
            "customer_birth_year": rng.integers(1945, 2008, size=row_count),
            "unit_price": unit_price,
            "discount_pct": discount_pct,
            "sales_amount": sales_amount,
            "purchase_date": pd.to_datetime(purchase_dates),
        }
    )
    return data


def validate_retail_data(data: pd.DataFrame) -> None:
    """Raise an assertion error when a required data rule is violated."""
    expected_columns = [
        "transaction_id",
        "customer_name",
        "region",
        "product_category",
        "loyalty_tier",
        "items_purchased",
        "customer_birth_year",
        "unit_price",
        "discount_pct",
        "sales_amount",
        "purchase_date",
    ]

    assert list(data.columns) == expected_columns, "Unexpected columns"
    assert len(data) == ROW_COUNT, f"Expected {ROW_COUNT:,} rows"
    assert data["transaction_id"].is_unique, "Transaction IDs must be unique"
    assert not data["transaction_id"].isna().any(), "Transaction IDs cannot be null"
    assert not data.isna().any().any(), "Dataset contains missing values"
    assert set(data["region"]).issubset(REGIONS), "Invalid region"
    assert set(data["product_category"]).issubset(
        PRODUCT_CATEGORIES
    ), "Invalid category"
    assert list(data["loyalty_tier"].cat.categories) == LOYALTY_TIERS
    assert data["loyalty_tier"].cat.ordered, "Loyalty tier must be ordered"
    assert data["items_purchased"].between(1, 15).all(), "Invalid item count"
    assert pd.api.types.is_integer_dtype(data["items_purchased"])
    assert data["customer_birth_year"].between(1945, 2007).all()
    assert pd.api.types.is_integer_dtype(data["customer_birth_year"])
    assert data["unit_price"].gt(0).all(), "Unit prices must be positive"
    assert data["discount_pct"].between(0, 35).all(), "Invalid discount"
    assert data["sales_amount"].gt(0).all(), "Sales amounts must be positive"

    expected_sales = (
        data["items_purchased"]
        * data["unit_price"]
        * (1 - data["discount_pct"] / 100)
    ).round(2)
    assert np.allclose(
        data["sales_amount"],
        expected_sales,
    ), "Incorrect sales amount"

    start_date = pd.Timestamp(
        REFERENCE_DATE.year - 3,
        REFERENCE_DATE.month,
        REFERENCE_DATE.day,
    )
    end_date = pd.Timestamp(REFERENCE_DATE)
    assert data["purchase_date"].between(
        start_date,
        end_date,
    ).all(), "Invalid date"


def print_summary(data: pd.DataFrame) -> None:
    """Print table-based checks and summaries without visualizations."""
    print("\nFirst five rows")
    print(data.head().to_string(index=False))

    print("\nData types")
    print(data.dtypes.to_string())

    print("\nMissing values")
    print(data.isna().sum().to_string())

    print("\nLoyalty tier counts")
    print(data["loyalty_tier"].value_counts(sort=False).to_string())

    print("\nNumeric summary")
    print(data.describe(include=[np.number]).round(2).to_string())

    print("\nAverage discount by loyalty tier")
    print(
        data.groupby(
            "loyalty_tier",
            observed=False,
        )["discount_pct"].mean().round(2).to_string()
    )


def main() -> None:
    data = generate_retail_data()
    validate_retail_data(data)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT_PATH, index=False)

    saved_data = pd.read_csv(OUTPUT_PATH)
    assert saved_data.shape == data.shape, (
        "Saved CSV shape does not match source data"
    )

    print_summary(data)
    print(f"\nCreated {OUTPUT_PATH}")
    print(
        f"Saved {len(saved_data):,} rows "
        f"and {saved_data.shape[1]} columns."
    )


if __name__ == "__main__":
    main()

