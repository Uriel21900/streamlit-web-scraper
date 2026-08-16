import streamlit as st
import pandas as pd
import plotly.express as px
from scraper import scrape_yahoo_data

st.set_page_config(page_title="Web Scraper Dashboard", layout="wide", page_icon="📈")

# --- UI Header ---
st.title("📈 Live Market Data Scraper")
st.markdown("Automated data extraction and visualization from Yahoo Finance.")

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    
    # Category Selector
    category_map = {
        "Most Active Stocks": "most-active",
        "Top Gainers": "gainers",
        "Top Losers": "losers",
        "Cryptocurrencies": "crypto"
    }
    selected_name = st.selectbox("Select Market Category:", list(category_map.keys()))
    selected_endpoint = category_map[selected_name]
    
    st.markdown("---")
    
    # Manual Refresh Cache Button
    st.markdown("Data is automatically cached for 5 minutes to prevent IP bans. Click below to force a live update.")
    if st.button("🔄 Force Refresh Data"):
        st.cache_data.clear()

# --- Data Fetching (Cached) ---
# TTL = 300 seconds (5 minutes). This is a safe caching window for a commercial app.
@st.cache_data(ttl=300, show_spinner=False) 
def load_data(endpoint):
    return scrape_yahoo_data(endpoint)

# --- Main Application Logic ---
with st.spinner(f"Fetching live data for {selected_name}..."):
    result = load_data(selected_endpoint)

if not result["success"]:
    # Graceful Error UI
    st.error("⚠️ Data Extraction Failed")
    st.warning(result["error"])
    st.info("Tip: If you are seeing a 403 or Timeout error on the cloud, the hosting IP might be temporarily blocked by Yahoo. Try clicking 'Force Refresh Data' in a few minutes.")
else:
    df = result["data"]
    st.success(f"Successfully loaded {len(df)} records for {selected_name}!")
    
    # --- Data Cleaning ---
    # Find relevant columns flexibly in case of layout changes
    price_col = [c for c in df.columns if 'Price' in c]
    price_col = price_col[0] if price_col else 'Price (Intraday)'
    
    change_col = [c for c in df.columns if '%' in c]
    change_col = change_col[0] if change_col else '% Change'
    
    volume_col = [c for c in df.columns if 'Volume' in c and 'Avg' not in c and '24' not in c]
    volume_col = volume_col[0] if volume_col else ('Volume in Currency (24Hr)' if 'crypto' in selected_endpoint else 'Volume')
    
    def clean_numeric(val):
        if pd.isna(val):
            return 0.0
        if isinstance(val, str):
            val = val.replace(',', '').replace('+', '').replace('%', '')
            if val.endswith('M'): return float(val[:-1]) * 1e6
            elif val.endswith('B'): return float(val[:-1]) * 1e9
            elif val.endswith('T'): return float(val[:-1]) * 1e12
        try:
            return float(val)
        except:
            return 0.0

    df_clean = df.copy()
    if volume_col in df_clean.columns:
        df_clean['Numeric_Volume'] = df_clean[volume_col].apply(clean_numeric)
    else:
        df_clean['Numeric_Volume'] = 0.0
        
    if price_col in df_clean.columns:
        df_clean['Numeric_Price'] = df_clean[price_col].apply(clean_numeric)
    else:
        df_clean['Numeric_Price'] = 0.0
        
    if change_col in df_clean.columns:
        df_clean['Numeric_Change_Pct'] = df_clean[change_col].apply(clean_numeric)
    else:
        df_clean['Numeric_Change_Pct'] = 0.0

    # Sort by Volume for the charts
    df_top = df_clean.sort_values(by='Numeric_Volume', ascending=False).head(20)

    # --- Visualizations ---
    st.subheader(f"📊 Top 20 by Volume: {selected_name}")
    
    if df_top['Numeric_Volume'].sum() > 0:
        fig_bar = px.bar(
            df_top, 
            x='Symbol', 
            y='Numeric_Volume', 
            hover_data=['Name', price_col, change_col] if 'Name' in df_top.columns else None,
            color='Numeric_Change_Pct',
            color_continuous_scale=px.colors.diverging.RdYlGn,
            labels={'Numeric_Volume': 'Trading Volume', 'Numeric_Change_Pct': '% Change'},
            template='plotly_dark'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Volume data is not available for this category to render a bar chart.")

    # --- Data Table & Export ---
    st.markdown("---")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("🗄️ Raw Scraped Data")
    
    with col2:
        # Export Functionality
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv_data,
            file_name=f"yahoo_{selected_endpoint}_data.csv",
            mime="text/csv",
            use_container_width=True
        )

    st.dataframe(df, use_container_width=True, hide_index=True)

    # Footer Disclaimer
    st.markdown("---")
    st.caption("*Disclaimer: Data is automatically extracted from public web sources. This dashboard is for informational and educational purposes only. Please verify data accuracy independently.*")
