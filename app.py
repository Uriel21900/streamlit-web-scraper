import streamlit as st
import pandas as pd
import plotly.express as px
from scraper import scrape_yahoo_active

st.set_page_config(page_title="Web Scraper Dashboard", layout="wide", page_icon="📈")

st.title("📈 Live Web Scraper Dashboard")
st.markdown("This dashboard pulls live data from Yahoo Finance's **Most Active** stocks page and visualizes it in real-time.")

@st.cache_data(ttl=60) # Cache data for 60 seconds
def load_data():
    return scrape_yahoo_active()

try:
    with st.spinner("Fetching live data from Yahoo Finance..."):
        df = load_data()
        
    st.success("Data loaded successfully!")
    
    # The columns on Yahoo Finance are usually:
    # 'Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)', '52 Wk Range'
    
    # Let's inspect the columns safely and assign fallback names if they don't match exactly
    # Find the columns that represent Price, Change %, and Volume.
    price_col = [c for c in df.columns if 'Price' in c]
    price_col = price_col[0] if price_col else 'Price (Intraday)'
    
    change_col = [c for c in df.columns if '%' in c]
    change_col = change_col[0] if change_col else '% Change'
    
    volume_col = [c for c in df.columns if 'Volume' in c and 'Avg' not in c]
    volume_col = volume_col[0] if volume_col else 'Volume'
    
    # Data Cleaning for charting
    # Volumes are often written like "45.1M" or just numbers, but pandas read_html usually gets the raw numbers if there's no M/B suffix.
    # In recent Yahoo Finance, Volume is an integer or string with commas.
    # Let's clean the numeric columns to make sure they are floats
    
    def clean_numeric(val):
        if pd.isna(val):
            return 0.0
        if isinstance(val, str):
            val = val.replace(',', '').replace('+', '').replace('%', '')
            # Handle M/B/T suffixes if they exist
            if val.endswith('M'):
                return float(val[:-1]) * 1e6
            elif val.endswith('B'):
                return float(val[:-1]) * 1e9
            elif val.endswith('T'):
                return float(val[:-1]) * 1e12
        try:
            return float(val)
        except:
            return 0.0

    df_clean = df.copy()
    df_clean['Numeric_Volume'] = df_clean[volume_col].apply(clean_numeric)
    df_clean['Numeric_Price'] = df_clean[price_col].apply(clean_numeric)
    df_clean['Numeric_Change_Pct'] = df_clean[change_col].apply(clean_numeric)

    # Sort by Volume for the bar chart
    df_top_volume = df_clean.sort_values(by='Numeric_Volume', ascending=False).head(20)

    st.subheader("📊 Most Active Stocks by Trading Volume")
    fig_bar = px.bar(
        df_top_volume, 
        x='Symbol', 
        y='Numeric_Volume', 
        hover_data=['Name', price_col, change_col],
        color='Numeric_Change_Pct',
        color_continuous_scale=px.colors.diverging.RdYlGn,
        labels={'Numeric_Volume': 'Trading Volume', 'Numeric_Change_Pct': '% Change'},
        template='plotly_dark'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Price vs % Change (Top 20)")
        fig_scatter = px.scatter(
            df_top_volume,
            x='Numeric_Price',
            y='Numeric_Change_Pct',
            size='Numeric_Volume',
            color='Numeric_Change_Pct',
            hover_name='Symbol',
            hover_data=['Name'],
            color_continuous_scale=px.colors.diverging.RdYlGn,
            labels={'Numeric_Price': 'Price ($)', 'Numeric_Change_Pct': '% Change'},
            template='plotly_dark'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        st.subheader("🗄️ Raw Scraped Data")
        st.dataframe(df, use_container_width=True, hide_index=True)

    # Footer
    st.markdown("---")
    st.markdown("*Note: Data is scraped live from Yahoo Finance. Please respect their terms of service.*")

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.warning("Please check if the website structure has changed or if you are being blocked.")
