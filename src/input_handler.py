def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than 0. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def validate_token_data(token_data):
    errors = []

    if token_data["total_supply"] < token_data["circulating_supply"]:
        errors.append("Total supply cannot be less than circulating supply.")

    if token_data["max_supply"] < token_data["total_supply"]:
        errors.append("Max supply cannot be less than total supply.")

    if token_data["max_supply"] < token_data["circulating_supply"]:
        errors.append("Max supply cannot be less than circulating supply.")

    return errors


def get_token_inputs():
    print("=== Tokenomics Analyzer ===")
    print()

    while True:
        token_data = {
            "token_name": input("Enter token name: "),
            "price": get_positive_float("Enter token price: "),
            "circulating_supply": get_positive_float("Enter circulating supply: "),
            "total_supply": get_positive_float("Enter total supply: "),
            "max_supply": get_positive_float("Enter max supply: "),
            "annual_emissions": get_non_negative_float("Enter annual token emissions: "),
            "upcoming_unlock": get_non_negative_float("Enter upcoming token unlock amount: ")
        }

        errors = validate_token_data(token_data)

        if not errors:
            return token_data

        print()
        print("Input Error(s):")
        for error in errors:
            print(f"- {error}")
        print("Please re-enter the token data.\n")
