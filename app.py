import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import time

st.title("📈 Master Trade Live")
symbol = st.sidebar.text_input("Enter Symbol (e.g., BTC-USD or RELIANCE.NS)", "BTC-USD")
data = yf.download(symbol, period="1d", interval="5m")

if not data.empty:
    fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], 
                    high=data['High'], low=data['Low'], close=data['Close'])])
    st.plotly_chart(fig)
    time.sleep(10)
    st.rerun()
