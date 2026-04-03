def calculate_metrics(token_data):
    price = token_data["price"]
    circulating_supply = token_data["circulating_supply"]
    max_supply = token_data["max_supply"]
    annual_emissions = token_data["annual_emissions"]
    upcoming_unlock = token_data["upcoming_unlock"]

    metrics = {
        "market_cap": price * circulating_supply,
        "fdv": price * max_supply,
        "circulating_percentage": (circulating_supply / max_supply) * 100,
        "inflation_rate": (annual_emissions / circulating_supply) * 100,
        "unlock_impact": (upcoming_unlock / circulating_supply) * 100
    }

    return metrics


def project_supply_growth(token_data, years=5):
    circulating_supply = token_data["circulating_supply"]
    max_supply = token_data["max_supply"]
    annual_emissions = token_data["annual_emissions"]

    projections = []
    projected_supply = circulating_supply

    for year in range(1, years + 1):
        projected_supply += annual_emissions

        if projected_supply > max_supply:
            projected_supply = max_supply

        circulating_percentage = (projected_supply / max_supply) * 100

        projections.append({
            "year": year,
            "projected_supply": projected_supply,
            "circulating_percentage": circulating_percentage
        })

        if projected_supply == max_supply:
            break

    return projections
