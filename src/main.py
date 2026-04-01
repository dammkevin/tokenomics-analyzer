from input_handler import get_token_inputs
from calculations import calculate_metrics
from risk_analysis import analyze_risks
from display import display_results


def main():
    token_data = get_token_inputs()
    metrics = calculate_metrics(token_data)
    risk_messages = analyze_risks(metrics)
    display_results(token_data, metrics, risk_messages)


if __name__ == "__main__":
    main()
