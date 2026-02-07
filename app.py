import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Master Trade Live", layout="wide")
st.title("📈 Master Trade Live")

# Sidebar
symbol = st.sidebar.text_input("Enter Symbol (e.g., BTC-USD)", "BTC-USD")
period = st.sidebar.selectbox("Period", ["5d", "1mo", "6mo"]) # 5d is better for weekends
interval = st.sidebar.selectbox("Interval", ["1h", "1d", "15m"])

# Fetch Data
with st.spinner('Fetching data...'):
    data = yf.download(symbol, period=period, interval=interval)

# --- THE FIX: Error Handling ---
if data is not None and not data.empty:
    # Check if we actually have the 'Close' column and data in it
    if len(data) > 0:
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close']
        )])
        fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Only show price if it exists to avoid TypeError
        last_price = data['Close'].iloc[-1]
        st.success(f"Latest Price for {symbol}: {last_price:.2f}")
    else:
        st.warning("Data found, but it is too limited to display a chart.")
else:
    st.error(f"⚠️ No data found for '{symbol}'.")
    st.info("💡 Note: Indian Markets (NSE/BSE) are CLOSED on weekends. Try testing with 'BTC-USD' to see a live chart right now.")
