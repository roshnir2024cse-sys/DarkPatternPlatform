import pandas as pd


def detect_review_risk(df):
    """
    Detect products with weak review trust.
    """

    df["ReviewTrustRisk"] = "No"

    condition = (
        (df["rating"] < 3.5)
        |
        (df["rating_count"] < 100)
    )

    df.loc[
        condition,
        "ReviewTrustRisk"
    ] = "Yes"

    return df