def display_results(token_data, metrics, risk_summary, projections):
    print()
    print("=" * 50)
    print("TOKENOMICS ANALYZER REPORT")
    print("=" * 50)

    print()
    print("Token Information")
    print("-" * 50)
    print(f"Token Name:                 {token_data['token_name']}")

    print()
    print("Core Metrics")
    print("-" * 50)
    print(f"Market Cap:                 ${metrics['market_cap']:,.2f}")
    print(f"Fully Diluted Valuation:    ${metrics['fdv']:,.2f}")
    print(f"Circulating Supply %:       {metrics['circulating_percentage']:.2f}%")
    print(f"Inflation Rate:             {metrics['inflation_rate']:.2f}%")
    print(f"Upcoming Unlock Impact:     {metrics['unlock_impact']:.2f}%")

    print()
    print("Overall Risk Summary")
    print("-" * 50)
    print(f"Overall Risk Level:         {risk_summary['overall_risk']}")
    print(f"Risk Score:                 {risk_summary['risk_score']} / 8")

    print()
    print("Detailed Risk Analysis")
    print("-" * 50)
    for message in risk_summary["risk_messages"]:
        print(f"- {message}")

    print()
    print("Supply Projection (Year 1 includes upcoming unlock)")
    print("-" * 50)
    for projection in projections:
        print(
            f"Year {projection['year']}: "
            f"Projected Circulating Supply = {projection['projected_supply']:,.2f} "
            f"({projection['circulating_percentage']:.2f}% of max supply)"
        )

    print()
    print("=" * 50)
