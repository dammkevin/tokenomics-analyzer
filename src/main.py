from input_handler import get_token_inputs
from calculations import calculate_metrics, project_supply_growth
from risk_analysis import analyze_risks
from display import display_results


def main():
    token_data = get_token_inputs()
    metrics = calculate_metrics(token_data)
    risk_summary = analyze_risks(metrics)
    projections = project_supply_growth(token_data, years=5)
    display_results(token_data, metrics, risk_summary, projections)


if __name__ == "__main__":
    main()
