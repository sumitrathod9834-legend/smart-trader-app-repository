import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Master Trade Live", layout="wide")
st.title("📈 Master Trade Live")

# Sidebar
symbol = st.sidebar.text_input("Enter Symbol", "BTC-USD")
# Use '5d' period so you can see data even on weekends!
data = yf.download(symbol, period="5d", interval="15m")

# --- THE FIX: Safety Check ---
if data is not None and not data.empty:
    # 1. Draw the Chart
    fig = go.Figure(data=[go.Candlestick(
        x=data.index, open=data['Open'], high=data['High'],
        low=data['Low'], close=data['Close']
    )])
    fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # 2. Show Price ONLY if data exists (Fixes TypeError)
    last_price = data['Close'].iloc[-1]
    st.success(f"Latest Price for {symbol}: {last_price:.2f}")
else:
    # This shows instead of the red error box
    st.error(f"⚠️ No live data for '{symbol}' right now.")
    st.info("Indian Markets are CLOSED on weekends. Try 'BTC-USD' to see a live crypto chart!")
