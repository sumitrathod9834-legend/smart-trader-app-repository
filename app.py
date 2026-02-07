import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Master Trade Live", layout="wide")
st.title("📈 Master Trade Live")

# Sidebar for input
symbol = st.sidebar.text_input("Enter Symbol (e.g., BTC-USD)", "BTC-USD")
period = st.sidebar.selectbox("Period", ["1d", "5d", "1mo"])
interval = st.sidebar.selectbox("Interval", ["5m", "15m", "1h", "1d"])

# Fetch Data
with st.spinner('Fetching data...'):
    data = yf.download(symbol, period=period, interval=interval)

if not data.empty:
    # Create Chart
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name="Price"
    )])
    
    fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Show last price so we know it's working
    st.success(f"Latest Price for {symbol}: {data['Close'].iloc[-1]:.2f}")
else:
    st.error(f"No data found for {symbol}. If it's an Indian stock, remember the market is closed on weekends!")
    st.info("Try typing 'BTC-USD' to test if the connection is working.")
