"""ScrapeFlow Cloud Extraction Platform - Streamlit Application
Matching Stitch reference design node bb592e1f18264b76811e85fc518f909f 1:1.
"""
import os
import streamlit as st
import streamlit.components.v1 as components

# Set page configuration with dark cyber-terminal defaults
st.set_page_config(
    page_title="ScrapeFlow — Cloud Extraction Platform",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="collapsed"
)

# Streamlit Chrome Removal & Full-Viewport CSS
st.markdown("""
<style>
    /* Completely hide Streamlit header, toolbar, sidebar, and footer */
    header[data-testid="stHeader"],
    footer,
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    .stAppToolbar,
    #MainMenu,
    [data-testid="stDecoration"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Zero out all body and container padding/margin */
    html, body, #root, .stApp, [data-testid="stAppViewContainer"], .main, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
        overflow: hidden !important;
        background-color: #031427 !important;
    }
    
    /* Make iframe fill the exact viewport seamlessly */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 999999 !important;
    }
</style>
""", unsafe_allow_html=True)

# Path to unified master Stitch application
html_path = os.path.join(os.path.dirname(__file__), "assets", "master_stitch_app.html")
if not os.path.exists(html_path):
    html_path = os.path.join(os.path.dirname(__file__), "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    master_html = f.read()

# Query param support for deep linking: ?page=schema_selectors, etc.
query_page = st.query_params.get("page", None)
if query_page:
    script_injection = f"<script>document.addEventListener('DOMContentLoaded', () => {{ switchView('{query_page}'); }});</script>"
    master_html = master_html.replace("</body>", f"{script_injection}</body>")

components.html(master_html, height=1200, scrolling=True)
