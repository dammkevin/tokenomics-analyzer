# tokenomics-analyzer
A Python-based tool for analyzing cryptocurrency tokenomics to evaluate dilution risk, inflation pressure, and token unlock impact.

This project simulates how crypto analysts assess token supply dynamics and identify risks that may influence price behavior.


## Features

- Calculates key metrics:
  - Market Cap
  - Fully Diluted Valuation (FDV)
  - Circulating Supply %
  - Inflation Rate
  - Token Unlock Impact

- Generates plain-English insights:
  - Dilution risk
  - Emissions (inflation) pressure
  - Unlock pressure
  - FDV overhang

- Provides an overall risk score:
  - Low / Moderate / High

- Includes forward-looking supply projections:
  - Models circulating supply growth over time
  - Incorporates emissions and upcoming unlocks

- Interactive Streamlit dashboard:
  - User input panel
  - Real-time metric updates
  - Supply projection visualization


## Why This Project Matters

Token price alone does not reflect true risk.

In crypto, supply dynamics such as:
- low circulating supply
- high inflation
- large token unlocks

can create significant downward price pressure over time.

This tool helps identify those risks early by analyzing how supply evolves.


## Tech Stack

- Python  
- Streamlit  
- Pandas  


## How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run the app

python -m streamlit run app.py


## Example Insights

### High Risk Token

- Low circulating supply
- High inflation
- Large unlock events
- FDV much higher than market cap

Indicates potential dilution and sell pressure.

### Low Risk Token

- High circulating supply
- Low inflation
- Small unlocks
- FDV close to market cap

Indicates more stable supply dynamics.