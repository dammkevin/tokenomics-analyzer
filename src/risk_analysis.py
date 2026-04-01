def analyze_risks(metrics):
    risk_messages = []

    if metrics["circulating_percentage"] < 40:
        risk_messages.append("High dilution risk: a low percentage of the max supply is currently circulating.")
    elif metrics["circulating_percentage"] < 70:
        risk_messages.append("Moderate dilution risk: a meaningful amount of supply is still not circulating.")
    else:
        risk_messages.append("Lower dilution risk: most of the max supply is already circulating.")

    if metrics["inflation_rate"] > 15:
        risk_messages.append("Aggressive emissions: inflation rate is high.")
    elif metrics["inflation_rate"] > 5:
        risk_messages.append("Moderate emissions: inflation exists but is not extreme.")
    else:
        risk_messages.append("Low emissions pressure: inflation rate is relatively low.")

    if metrics["unlock_impact"] > 10:
        risk_messages.append("Major unlock pressure: upcoming unlock is large relative to circulating supply.")
    elif metrics["unlock_impact"] > 5:
        risk_messages.append("Moderate unlock pressure: upcoming unlock may create selling pressure.")
    else:
        risk_messages.append("Low unlock pressure: upcoming unlock appears relatively small.")

    if metrics["fdv"] > metrics["market_cap"] * 3:
        risk_messages.append("FDV is much higher than market cap, which may suggest future dilution overhang.")
    else:
        risk_messages.append("FDV is not excessively above market cap.")

    return risk_messages
