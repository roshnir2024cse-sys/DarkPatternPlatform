def calculate_score(df):

    scores = []
    risk_levels = []

    for _, row in df.iterrows():

        score = 0

        if row["PotentialFakeDiscount"] == "Yes":
            score += 30

        if row["ReviewTrustRisk"] == "Yes":
            score += 30

        if row["PremiumDiscountRisk"] == "Yes":
            score += 40

        scores.append(score)

        # Risk Level
        if score >= 80:
            risk_levels.append("Critical")
        elif score >= 60:
            risk_levels.append("High")
        elif score >= 30:
            risk_levels.append("Medium")
        else:
            risk_levels.append("Low")

    df["DarkPatternScore"] = scores
    df["RiskLevel"] = risk_levels

    return df