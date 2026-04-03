import pandas as pd
import streamlit as st

from src.calculations import calculate_metrics, project_supply_growth
from src.risk_analysis import analyze_risks


def validate_inputs(token_data):
    errors = []

    if token_data["price"] <= 0:
        errors.append("Price must be greater than 0.")
    if token_data["circulating_supply"] <= 0:
        errors.append("Circulating supply must be greater than 0.")
    if token_data["total_supply"] <= 0:
        errors.append("Total supply must be greater than 0.")
    if token_data["max_supply"] <= 0:
        errors.append("Max supply must be greater than 0.")
    if token_data["annual_emissions"] < 0:
        errors.append("Annual emissions cannot be negative.")
    if token_data["upcoming_unlock"] < 0:
        errors.append("Upcoming unlock cannot be negative.")
    if token_data["total_supply"] < token_data["circulating_supply"]:
        errors.append("Total supply cannot be less than circulating supply.")
    if token_data["max_supply"] < token_data["total_supply"]:
        errors.append("Max supply cannot be less than total supply.")
    if token_data["max_supply"] < token_data["circulating_supply"]:
        errors.append("Max supply cannot be less than circulating supply.")

    return errors


def main():
    st.set_page_config(page_title="Tokenomics Analyzer", layout="wide")

    st.title("Tokenomics Analyzer")
    st.caption("Analyze crypto token dilution, inflation, FDV overhang, and unlock pressure.")

    # Sidebar Inputs
    with st.sidebar:
        st.header("Token Inputs")

        token_name = st.text_input("Token Name", value="RiskyToken")
        price = st.number_input("Token Price", min_value=0.0, value=2.0)
        circulating_supply = st.number_input("Circulating Supply", min_value=0.0, value=100000000.0)
        total_supply = st.number_input("Total Supply", min_value=0.0, value=500000000.0)
        max_supply = st.number_input("Max Supply", min_value=0.0, value=1000000000.0)
        annual_emissions = st.number_input("Annual Emissions", min_value=0.0, value=30000000.0)
        upcoming_unlock = st.number_input("Upcoming Unlock", min_value=0.0, value=12000000.0)
        years = st.slider("Projection Years", 1, 10, 5)

    token_data = {
        "token_name": token_name,
        "price": price,
        "circulating_supply": circulating_supply,
        "total_supply": total_supply,
        "max_supply": max_supply,
        "annual_emissions": annual_emissions,
        "upcoming_unlock": upcoming_unlock
    }

    errors = validate_inputs(token_data)

    if errors:
        st.error("Please fix the following issues:")
        for error in errors:
            st.write(f"- {error}")
        return

    
    metrics = calculate_metrics(token_data)
    risk_summary = analyze_risks(metrics)
    projections = project_supply_growth(token_data, years)

    df = pd.DataFrame(projections)

    # Executive Summary
    st.subheader("Executive Summary")
    st.write(risk_summary["executive_summary"])

    # Metrics Row 1
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Market Cap", f"${metrics['market_cap']:,.2f}")
    col2.metric("FDV", f"${metrics['fdv']:,.2f}")
    col3.metric("Circulating %", f"{metrics['circulating_percentage']:.2f}%")
    col4.metric("Overall Risk", risk_summary["overall_risk"])

    # Metrics Row 2
    col5, col6, col7 = st.columns(3)
    col5.metric("Inflation Rate", f"{metrics['inflation_rate']:.2f}%")
    col6.metric("Unlock Impact", f"{metrics['unlock_impact']:.2f}%")
    col7.metric("Risk Score", f"{risk_summary['risk_score']} / 8")

    # Risk Details
    st.subheader("Detailed Risk Analysis")
    for msg in risk_summary["risk_messages"]:
        st.write(f"- {msg}")

    # Projection Chart
    st.subheader("Supply Projection")
    st.caption("Year 1 includes upcoming unlock + emissions")

    st.line_chart(df.set_index("year")["projected_supply"])

    st.dataframe(df, width='stretch')


if __name__ == "__main__":
    main()
