def get_token_inputs():
    print("=== Tokenomics Analyzer ===")
    print()

    token_data = {
        "token_name": input("Enter token name: "),
        "price": float(input("Enter token price: ")),
        "circulating_supply": float(input("Enter circulating supply: ")),
        "total_supply": float(input("Enter total supply: ")),
        "max_supply": float(input("Enter max supply: ")),
        "annual_emissions": float(input("Enter annual token emissions: ")),
        "upcoming_unlock": float(input("Enter upcoming token unlock amount: "))
    }

    return token_data
