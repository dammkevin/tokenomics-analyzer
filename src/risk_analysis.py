def analyze_risks(metrics):
    risk_messages = []
    risk_score = 0
    key_drivers = []

    if metrics["circulating_percentage"] < 40:
        risk_messages.append("High dilution risk: a low percentage of the max supply is currently circulating.")
        key_drivers.append("low circulating supply")
        risk_score += 2
    elif metrics["circulating_percentage"] < 70:
        risk_messages.append("Moderate dilution risk: a meaningful amount of supply is still not circulating.")
        key_drivers.append("moderate remaining dilution")
        risk_score += 1
    else:
        risk_messages.append("Lower dilution risk: most of the max supply is already circulating.")

    if metrics["inflation_rate"] > 15:
        risk_messages.append("Aggressive emissions: inflation rate is high.")
        key_drivers.append("aggressive emissions")
        risk_score += 2
    elif metrics["inflation_rate"] > 5:
        risk_messages.append("Moderate emissions: inflation exists but is not extreme.")
        key_drivers.append("moderate inflation")
        risk_score += 1
    else:
        risk_messages.append("Low emissions pressure: inflation rate is relatively low.")

    if metrics["unlock_impact"] > 10:
        risk_messages.append("Major unlock pressure: upcoming unlock is large relative to circulating supply.")
        key_drivers.append("large upcoming unlock")
        risk_score += 2
    elif metrics["unlock_impact"] > 5:
        risk_messages.append("Moderate unlock pressure: upcoming unlock may create selling pressure.")
        key_drivers.append("moderate upcoming unlock")
        risk_score += 1
    else:
        risk_messages.append("Low unlock pressure: upcoming unlock appears relatively small.")

    if metrics["fdv"] > metrics["market_cap"] * 3:
        risk_messages.append("FDV is much higher than market cap, which may suggest future dilution overhang.")
        key_drivers.append("large FDV overhang")
        risk_score += 2
    elif metrics["fdv"] > metrics["market_cap"] * 1.5:
        risk_messages.append("FDV is moderately above market cap, which suggests some future dilution risk.")
        key_drivers.append("some FDV overhang")
        risk_score += 1
    else:
        risk_messages.append("FDV is not excessively above market cap.")

    if risk_score >= 6:
        overall_risk = "High"
    elif risk_score >= 3:
        overall_risk = "Moderate"
    else:
        overall_risk = "Low"

    executive_summary = generate_executive_summary(overall_risk, key_drivers)

    risk_summary = {
        "risk_score": risk_score,
        "overall_risk": overall_risk,
        "risk_messages": risk_messages,
        "key_drivers": key_drivers,
        "executive_summary": executive_summary
    }

    return risk_summary


def generate_executive_summary(overall_risk, key_drivers):
    if not key_drivers:
        return (
            f"This token appears {overall_risk.lower()} risk based on the current inputs. "
            "The analyzer did not detect any major tokenomics red flags."
        )

    if len(key_drivers) == 1:
        driver_text = key_drivers[0]
    elif len(key_drivers) == 2:
        driver_text = f"{key_drivers[0]} and {key_drivers[1]}"
    else:
        driver_text = ", ".join(key_drivers[:-1]) + f", and {key_drivers[-1]}"

    return (
        f"This token appears {overall_risk.lower()} risk based on the current inputs, "
        f"primarily due to {driver_text}."
    )
