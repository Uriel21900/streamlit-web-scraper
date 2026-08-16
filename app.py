import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
from scraper import scrape_yahoo_data, fetch_financial_news

st.set_page_config(page_title="Data Analytics Platform", layout="wide", page_icon="📈")

# --- UI Header ---
st.title("📈 Enterprise Data Analytics Platform")
st.markdown("Automated web scraping, API integration, and machine-learning predictive analytics.")

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Dashboard Controls")
    
    data_source = st.radio("Select Data Source:", ["Live Web Scraper & News", "Upload Custom Data (ML Analytics)"])
    st.markdown("---")

# ==========================================
# MODE 1: LIVE WEB SCRAPER & NEWS API
# ==========================================
if data_source == "Live Web Scraper & News":
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
        if st.button("🔄 Force Refresh Data"):
            st.cache_data.clear()

    @st.cache_data(ttl=300, show_spinner=False) 
    def load_data(endpoint):
        return scrape_yahoo_data(endpoint)
        
    @st.cache_data(ttl=300, show_spinner=False)
    def load_news():
        return fetch_financial_news()

    with st.spinner(f"Fetching live market data and news APIs..."):
        result = load_data(selected_endpoint)
        news_result = load_news()

    if not result["success"]:
        st.error("⚠️ Data Extraction Failed")
        st.warning(result["error"])
    else:
        df = result["data"]
        st.success(f"Successfully loaded records for {selected_name}!")
        
        # --- Data Cleaning ---
        price_col = next((c for c in df.columns if 'Price' in c), 'Price (Intraday)')
        change_col = next((c for c in df.columns if '%' in c), '% Change')
        volume_col = next((c for c in df.columns if 'Volume' in c and 'Avg' not in c and '24' not in c), 
                          ('Volume in Currency (24Hr)' if 'crypto' in selected_endpoint else 'Volume'))
        
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
        df_clean['Numeric_Volume'] = df_clean[volume_col].apply(clean_numeric) if volume_col in df_clean.columns else 0.0
        df_clean['Numeric_Change_Pct'] = df_clean[change_col].apply(clean_numeric) if change_col in df_clean.columns else 0.0

        df_top = df_clean.sort_values(by='Numeric_Volume', ascending=False).head(20)

        # Main Chart
        st.subheader(f"📊 Top 20 by Volume: {selected_name}")
        if df_top['Numeric_Volume'].sum() > 0:
            fig_bar = px.bar(
                df_top, x='Symbol', y='Numeric_Volume', 
                color='Numeric_Change_Pct', color_continuous_scale=px.colors.diverging.RdYlGn,
                labels={'Numeric_Volume': 'Trading Volume', 'Numeric_Change_Pct': '% Change'},
                template='plotly_dark'
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")
        col_data, col_news = st.columns([2, 1])
        
        with col_data:
            st.subheader("🗄️ Raw Market Data")
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download as CSV", data=csv_data, file_name=f"yahoo_{selected_endpoint}.csv", mime="text/csv")
            st.dataframe(df, use_container_width=True, hide_index=True)
            
        with col_news:
            st.subheader("📰 Live News API Feed")
            if news_result["success"]:
                for article in news_result["data"]:
                    st.markdown(f"**[{article['title']}]({article['link']})**")
                    st.caption(f"{article['published']}")
                    st.markdown("---")
            else:
                st.warning("News feed temporarily unavailable.")

# ==========================================
# MODE 2: CUSTOM DATA IMPORT & ML ANALYTICS
# ==========================================
else:
    st.subheader("📂 Advanced Analytics: Upload Custom Dataset")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'): df = pd.read_csv(uploaded_file)
            else: df = pd.read_excel(uploaded_file)
                
            st.success(f"Successfully loaded {len(df)} rows from {uploaded_file.name}!")
            all_columns = df.columns.tolist()
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            
            # --- Aggregation Engine (Pivot Table) ---
            st.markdown("---")
            st.subheader("🧮 Data Aggregation Engine")
            st.markdown("Instantly build Pivot Tables to summarize your data.")
            
            agg_col1, agg_col2, agg_col3 = st.columns(3)
            with agg_col1:
                group_by_col = st.selectbox("Group By (Category):", ["None"] + all_columns, index=0)
            with agg_col2:
                metric_col = st.selectbox("Metric to Aggregate:", numeric_columns if numeric_columns else all_columns)
            with agg_col3:
                agg_method = st.selectbox("Aggregation Method:", ["Sum", "Average", "Count"])
                
            if group_by_col != "None" and metric_col:
                agg_func = 'sum' if agg_method == "Sum" else 'mean' if agg_method == "Average" else 'count'
                df_agg = df.groupby(group_by_col)[metric_col].agg(agg_func).reset_index()
                st.dataframe(df_agg, use_container_width=True)
                plot_df = df_agg
            else:
                plot_df = df
            
            # --- Dynamic Charting & ML ---
            st.markdown("---")
            st.subheader("🎨 Predictive Charting (Machine Learning)")
            
            if len(all_columns) >= 2:
                col_x, col_y, col_type = st.columns(3)
                with col_x:
                    x_axis = st.selectbox("X-Axis (Categories/Dates)", options=plot_df.columns.tolist(), index=0)
                with col_y:
                    y_default = next((c for c in plot_df.columns if c in numeric_columns), plot_df.columns[1])
                    y_axis = st.selectbox("Y-Axis (Values)", options=plot_df.columns.tolist(), index=plot_df.columns.tolist().index(y_default))
                with col_type:
                    chart_type = st.selectbox("Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart"])
                    
                enable_ml = False
                if chart_type in ["Scatter Plot", "Line Chart"] and pd.api.types.is_numeric_dtype(plot_df[y_axis]):
                    enable_ml = st.checkbox("🔮 Enable ML Trendline Forecast (Linear Regression)", value=False)
                
                try:
                    if chart_type == "Bar Chart":
                        fig = px.bar(plot_df, x=x_axis, y=y_axis, template='plotly_dark')
                    elif chart_type == "Line Chart":
                        fig = px.line(plot_df, x=x_axis, y=y_axis, template='plotly_dark')
                    else:
                        fig = px.scatter(plot_df, x=x_axis, y=y_axis, template='plotly_dark')
                        
                    # Inject Machine Learning Trendline
                    if enable_ml:
                        # Prepare data for sklearn
                        # If X is categorical/dates, we convert it to numeric sequence for simple regression
                        plot_df = plot_df.dropna(subset=[x_axis, y_axis])
                        X_raw = plot_df[x_axis]
                        y = plot_df[y_axis].values
                        
                        # Convert X to numeric steps if it's not strictly numerical
                        if pd.api.types.is_numeric_dtype(X_raw):
                            X = X_raw.values.reshape(-1, 1)
                        else:
                            X = np.arange(len(X_raw)).reshape(-1, 1)
                            
                        model = LinearRegression()
                        model.fit(X, y)
                        
                        # Predict over the same range plus a 20% forecast into the future
                        future_steps = int(len(X) * 0.2)
                        if future_steps < 1: future_steps = 1
                        
                        X_pred = np.arange(len(X) + future_steps).reshape(-1, 1)
                        y_pred = model.predict(X_pred)
                        
                        # Add Trendline Trace
                        fig.add_trace(go.Scatter(
                            x=X_raw.tolist() + [f"Forecast {i}" for i in range(1, future_steps+1)] if not pd.api.types.is_numeric_dtype(X_raw) else X_pred.flatten(), 
                            y=y_pred,
                            mode='lines',
                            name='ML Forecast',
                            line=dict(color='red', dash='dash')
                        ))

                    st.plotly_chart(fig, use_container_width=True)
                except Exception as chart_e:
                    st.warning(f"Could not render chart or run ML model. Check data types: {str(chart_e)}")
            else:
                st.info("Dataset needs at least two columns.")

            st.markdown("---")
            st.subheader("🗄️ Raw Data Preview")
            st.dataframe(df.head(100), use_container_width=True, hide_index=True) # Limit to 100 to save memory
            
        except Exception as e:
            st.error("Error analyzing file.")
            st.write(str(e))

st.markdown("---")
st.caption("*Disclaimer: This platform uses advanced external APIs, web scraping, and machine learning models. Built for enterprise analytics.*")
