import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def stock_graph(sym):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sym.index, y=sym['Close'].values.flatten()))
    st.plotly_chart(fig)

start_date = "2011-01-01"
end_date = "2024-01-01"

st.title("OPTION PRICING MODEL")
ticker=st.text_input("Enter ticker symbol")
if ticker:
    tables=yf.download(ticker,start=start_date,end=end_date)
    with st.sidebar:
        st.title("Graph of Stock price")
        stock_graph(tables)

stock = yf.Ticker(ticker)
S = stock.info['currentPrice']
st.write(f"The current price is {S}")
K = st.slider('Strike Price', min_value=0, max_value=int(S*2), value=int(S))
T = st.slider("Time to Maturity (in years)", min_value=0.0, max_value=10.0, value=1.0)
r = st.slider("Risk-Free Rate (as a percentage)", min_value=0.0, max_value=10.0, value=5.0) / 100
sigma = st.slider("Volatility (as a percentage)", min_value=0.0, max_value=100.0, value=20.0) / 100

call_button = st.button("Call Option Price")
put_button = st.button("Put Option Price")

if call_button:
        option_price = black_scholes(S, K, T, r, sigma, option_type='call')
        st.write(f"The Call option price is: {option_price}")
        st.write(f"DELTA:   {calc_delta(S, K, T, r, sigma, option_type='call')}")
        st.write(f"GAMMA:   {calc_gamma(S, K, T, r, sigma)}")
        st.write(f"THETA:   {calc_theta(S, K, T, r, sigma, option_type='call')}")
        st.write(f"VEGA:   {calc_vega(S, K, T, r, sigma)}")
elif put_button:
        option_price = black_scholes(S, K, T, r, sigma, option_type='put')
        st.write(f"The Put option price is: {option_price}")
        st.write(f"DELTA:   {calc_delta(S, K, T, r, sigma, option_type='put')}")
        st.write(f"GAMMA:   {calc_gamma(S, K, T, r, sigma)}")
        st.write(f"THETA:   {calc_theta(S, K, T, r, sigma, option_type='put')}")
        st.write(f"VEGA:   {calc_vega(S, K, T, r, sigma)}")




