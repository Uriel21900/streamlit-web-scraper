import streamlit as st
import pandas as pd
import plotly.express as px
from scraper import scrape_yahoo_data

st.set_page_config(page_title="Data Dashboard", layout="wide", page_icon="📊")

# --- UI Header ---
st.title("📊 Universal Data Dashboard")
st.markdown("Extract live market data from the web, or upload your own custom dataset for instant visualization.")

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    
    data_source = st.radio("Select Data Source:", ["Live Web Scraper", "Upload Custom Data"])
    st.markdown("---")

# ==========================================
# MODE 1: LIVE WEB SCRAPER
# ==========================================
if data_source == "Live Web Scraper":
    with st.sidebar:
        st.subheader("🌐 Scraper Settings")
        category_map = {
            "Most Active Stocks": "most-active",
            "Top Gainers": "gainers",
            "Top Losers": "losers",
            "Cryptocurrencies": "crypto"
        }
        selected_name = st.selectbox("Select Market Category:", list(category_map.keys()))
        selected_endpoint = category_map[selected_name]
        
        st.markdown("---")
        st.markdown("Data is cached for 5 minutes. Click below to force a live update.")
        if st.button("🔄 Force Refresh Data"):
            st.cache_data.clear()

    @st.cache_data(ttl=300, show_spinner=False) 
    def load_data(endpoint):
        return scrape_yahoo_data(endpoint)

    with st.spinner(f"Fetching live data for {selected_name}..."):
        result = load_data(selected_endpoint)

    if not result["success"]:
        st.error("⚠️ Data Extraction Failed")
        st.warning(result["error"])
        st.info("Tip: If you are seeing a 403 or Timeout error, the hosting IP might be temporarily blocked. Try refreshing in a few minutes.")
    else:
        df = result["data"]
        st.success(f"Successfully loaded {len(df)} records for {selected_name}!")
        
        # Flexibly find columns
        price_col = [c for c in df.columns if 'Price' in c]
        price_col = price_col[0] if price_col else 'Price (Intraday)'
        change_col = [c for c in df.columns if '%' in c]
        change_col = change_col[0] if change_col else '% Change'
        volume_col = [c for c in df.columns if 'Volume' in c and 'Avg' not in c and '24' not in c]
        volume_col = volume_col[0] if volume_col else ('Volume in Currency (24Hr)' if 'crypto' in selected_endpoint else 'Volume')
        
        def clean_numeric(val):
            if pd.isna(val): return 0.0
            if isinstance(val, str):
                val = val.replace(',', '').replace('+', '').replace('%', '')
                if val.endswith('M'): return float(val[:-1]) * 1e6
                elif val.endswith('B'): return float(val[:-1]) * 1e9
                elif val.endswith('T'): return float(val[:-1]) * 1e12
            try: return float(val)
            except: return 0.0

        df_clean = df.copy()
        if volume_col in df_clean.columns: df_clean['Numeric_Volume'] = df_clean[volume_col].apply(clean_numeric)
        else: df_clean['Numeric_Volume'] = 0.0
            
        if price_col in df_clean.columns: df_clean['Numeric_Price'] = df_clean[price_col].apply(clean_numeric)
        else: df_clean['Numeric_Price'] = 0.0
            
        if change_col in df_clean.columns: df_clean['Numeric_Change_Pct'] = df_clean[change_col].apply(clean_numeric)
        else: df_clean['Numeric_Change_Pct'] = 0.0

        df_top = df_clean.sort_values(by='Numeric_Volume', ascending=False).head(20)

        st.subheader(f"📊 Top 20 by Volume: {selected_name}")
        if df_top['Numeric_Volume'].sum() > 0:
            fig_bar = px.bar(
                df_top, x='Symbol', y='Numeric_Volume', 
                hover_data=['Name', price_col, change_col] if 'Name' in df_top.columns else None,
                color='Numeric_Change_Pct', color_continuous_scale=px.colors.diverging.RdYlGn,
                labels={'Numeric_Volume': 'Trading Volume', 'Numeric_Change_Pct': '% Change'},
                template='plotly_dark'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Volume data is not available to render a bar chart.")

        st.markdown("---")
        col1, col2 = st.columns([3, 1])
        with col1: st.subheader("🗄️ Raw Scraped Data")
        with col2:
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Data as CSV", data=csv_data,
                file_name=f"yahoo_{selected_endpoint}_data.csv", mime="text/csv",
                use_container_width=True
            )
        st.dataframe(df, use_container_width=True, hide_index=True)


# ==========================================
# MODE 2: CUSTOM DATA IMPORT
# ==========================================
else:
    st.subheader("📂 Upload Custom Dataset")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            # Read file based on extension
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                # Requires openpyxl installed, but Streamlit cloud pandas handles basic excel if installed, 
                # we'll use read_excel and hope openpyxl is available, or fallback to csv recommendation.
                df = pd.read_excel(uploaded_file)
                
            st.success(f"Successfully loaded {len(df)} rows from {uploaded_file.name}!")
            
            # --- Dynamic Charting ---
            st.markdown("---")
            st.subheader("🎨 Dynamic Visualization")
            st.markdown("Select columns from your dataset to build a custom chart.")
            
            all_columns = df.columns.tolist()
            # Try to auto-guess numeric columns for Y-axis
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            
            if len(all_columns) >= 2:
                col_x, col_y, col_type = st.columns(3)
                with col_x:
                    x_axis = st.selectbox("X-Axis (Categories/Dates)", options=all_columns, index=0)
                with col_y:
                    y_default = numeric_columns[0] if numeric_columns else all_columns[1]
                    y_axis = st.selectbox("Y-Axis (Values)", options=all_columns, index=all_columns.index(y_default) if y_default in all_columns else 1)
                with col_type:
                    chart_type = st.selectbox("Chart Type", ["Bar Chart", "Line Chart", "Scatter Plot"])
                
                # Render Dynamic Chart
                try:
                    if chart_type == "Bar Chart":
                        fig = px.bar(df, x=x_axis, y=y_axis, template='plotly_dark')
                    elif chart_type == "Line Chart":
                        fig = px.line(df, x=x_axis, y=y_axis, template='plotly_dark')
                    else:
                        fig = px.scatter(df, x=x_axis, y=y_axis, template='plotly_dark')
                        
                    st.plotly_chart(fig, use_container_width=True)
                except Exception as chart_e:
                    st.warning(f"Could not render {chart_type} with the selected columns. Try selecting different data types.")
            else:
                st.info("Your dataset needs at least two columns to generate a chart.")

            # --- Data Table ---
            st.markdown("---")
            st.subheader("🗄️ Raw Data Preview")
            st.dataframe(df, use_container_width=True, hide_index=True)
            
        except Exception as e:
            st.error("Error reading file. Please ensure it is a valid CSV or Excel file.")
            st.write(str(e))
    else:
        st.info("Please upload a file to get started.")

st.markdown("---")
st.caption("*Disclaimer: Data is automatically extracted from public web sources or uploaded directly by the user. This dashboard is for informational and educational purposes only.*")
