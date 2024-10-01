# Option Pricing Model

This is a web-based application that allows users to calculate European-style option prices (Call and Put) using the **Black-Scholes** formula. The app also computes the Greeks (Delta, Gamma, Theta, Vega) for both Call and Put options.

This app is built with **Streamlit** and **Plotly** for data visualization. The app uses **Yahoo Finance** to fetch historical stock prices and **SciPy** to compute the normal distribution.

## Features

- **Real-time Stock Data**: Enter a stock ticker, and the app fetches the stock's historical data and displays a price graph.
- **Option Pricing**: Calculate the price of European Call and Put options using the Black-Scholes model.
- **Greeks Calculation**: Compute the following Greeks:
  - Delta
  - Gamma
  - Theta
  - Vega
- **Interactive Sliders**: Adjust parameters such as Strike Price, Time to Maturity, Risk-Free Rate, and Volatility through intuitive sliders.

## Libraries Used

- `streamlit`: For creating the web interface.
- `yfinance`: For fetching historical stock data.
- `numpy`: For numerical calculations.
- `scipy.stats`: For computing standard normal cumulative distribution and probability density.
- `plotly`: For plotting stock price graphs.

## Installation

To run the app locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Aarnav005/Option-Pricing-Model.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Option-Pricing-Model
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter a valid stock ticker symbol (e.g., `AAPL` for Apple).
2. Adjust the sliders for **Strike Price**, **Time**, **Risk-Free Rate**, and **Volatility**.
3. Click the **Call Option Price** or **Put Option Price** button to compute the option price and Greeks.
4. The current stock price will be fetched and displayed along with the computed option price and Greeks.

## Black-Scholes Formula

The Black-Scholes formula for pricing European options is as follows:

\[
C = S N(d_1) - K e^{-rT} N(d_2) \quad \text{for Call options}
\]

\[
P = K e^{-rT} N(-d_2) - S N(-d_1) \quad \text{for Put options}
\]

Where:

- \( C \) is the Call option price
- \( P \) is the Put option price
- \( S \) is the current stock price
- \( K \) is the strike price
- \( T \) is the time to maturity
- \( r \) is the risk-free interest rate
- \( \sigma \) is the volatility
- \( N \) is the cumulative distribution function of the standard normal distribution
- \( d_1 \) and \( d_2 \) are intermediate calculations:
  \[
  d_1 = \frac{\ln(S / K) + (r + 0.5 \sigma^2) T}{\sigma \sqrt{T}}
  \]
  \[
  d_2 = d_1 - \sigma \sqrt{T}
  \]
