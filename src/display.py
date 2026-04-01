def display_results(token_data, metrics, risk_messages):
    print()
    print("=== Tokenomics Report ===")
    print(f"Token: {token_data['token_name']}")
    print(f"Market Cap: ${metrics['market_cap']:,.2f}")
    print(f"Fully Diluted Valuation (FDV): ${metrics['fdv']:,.2f}")
    print(f"Circulating Supply Percentage: {metrics['circulating_percentage']:.2f}%")
    print(f"Inflation Rate: {metrics['inflation_rate']:.2f}%")
    print(f"Upcoming Unlock Impact: {metrics['unlock_impact']:.2f}%")

    print()
    print("=== Risk Analysis ===")
    for message in risk_messages:
        print(f"- {message}")
