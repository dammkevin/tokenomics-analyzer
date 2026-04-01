def main():
    print("=== Tokenomics Analyzer ===")
    print()

    token_name = input("Enter token name: ")
    price = float(input("Enter token price: "))
    circulating_supply = float(input("Enter circulating supply: "))
    total_supply = float(input("Enter total supply: "))
    max_supply = float(input("Enter max supply: "))
    annual_emissions = float(input("Enter annual token emissions: "))
    upcoming_unlock = float(input("Enter upcoming token unlock amount: "))

    market_cap = price * circulating_supply
    fdv = price * max_supply
    circulating_percentage = (circulating_supply / max_supply) * 100
    inflation_rate = (annual_emissions / circulating_supply) * 100
    unlock_impact = (upcoming_unlock / circulating_supply) * 100

    print()
    print("=== Tokenomics Report ===")
    print(f"Token: {token_name}")
    print(f"Market Cap: ${market_cap:,.2f}")
    print(f"Fully Diluted Valuation (FDV): ${fdv:,.2f}")
    print(f"Circulating Supply Percentage: {circulating_percentage:.2f}%")
    print(f"Inflation Rate: {inflation_rate:.2f}%")
    print(f"Upcoming Unlock Impact: {unlock_impact:.2f}%")

    print()
    print("=== Risk Analysis ===")

    if circulating_percentage < 40:
        print("- High dilution risk: a low percentage of the max supply is currently circulating.")
    elif circulating_percentage < 70:
        print("- Moderate dilution risk: a meaningful amount of supply is still not circulating.")
    else:
        print("- Lower dilution risk: most of the max supply is already circulating.")

    if inflation_rate > 15:
        print("- Aggressive emissions: inflation rate is high.")
    elif inflation_rate > 5:
        print("- Moderate emissions: inflation exists but is not extreme.")
    else:
        print("- Low emissions pressure: inflation rate is relatively low.")

    if unlock_impact > 10:
        print("- Major unlock pressure: upcoming unlock is large relative to circulating supply.")
    elif unlock_impact > 5:
        print("- Moderate unlock pressure: upcoming unlock may create selling pressure.")
    else:
        print("- Low unlock pressure: upcoming unlock appears relatively small.")

    if fdv > market_cap * 3:
        print("- FDV is much higher than market cap, which may suggest future dilution overhang.")
    else:
        print("- FDV is not excessively above market cap.")

if __name__ == "__main__":
    main()
