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
