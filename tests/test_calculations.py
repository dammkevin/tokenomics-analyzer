from src.calculations import calculate_metrics


def test_market_cap():
    token_data = {
        "price": 2,
        "circulating_supply": 100000000,
        "max_supply": 1000000000,
        "annual_emissions": 30000000,
        "upcoming_unlock": 12000000
    }

    metrics = calculate_metrics(token_data)

    assert metrics["market_cap"] == 200000000


def test_inflation_rate():
    token_data = {
        "price": 2,
        "circulating_supply": 100000000,
        "max_supply": 1000000000,
        "annual_emissions": 30000000,
        "upcoming_unlock": 12000000
    }

    metrics = calculate_metrics(token_data)

    assert round(metrics["inflation_rate"], 2) == 30.00
