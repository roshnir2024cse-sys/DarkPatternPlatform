import pandas as pd


def detect_fake_discount(df):
    """
    Detect products with unusually high discounts.
    Returns dataframe with new column:
    PotentialFakeDiscount
    """

    df["PotentialFakeDiscount"] = "No"

    df.loc[
        (df["discount_percentage"] >= 70),
        "PotentialFakeDiscount"
    ] = "Yes"

    return df