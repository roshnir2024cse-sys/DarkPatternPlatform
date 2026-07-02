import pandas as pd


def detect_pricing_risk(df):

    df["PremiumDiscountRisk"] = "No"

    condition = (
        (df["actual_price"] > 10000)
        &
        (df["discount_percentage"] > 50)
    )

    df.loc[
        condition,
        "PremiumDiscountRisk"
    ] = "Yes"

    return df