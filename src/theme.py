"""Theme and styling configuration matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st

THEME_COLORS = {
    "surface": "#031427",
    "background": "#031427",
    "surface_lowest": "#000f21",
    "surface_low": "#0b1c30",
    "surface_container": "#102034",
    "surface_high": "#1b2b3f",
    "surface_highest": "#26364a",
    "primary": "#adc6ff",
    "primary_container": "#4d8eff",
    "on_primary_container": "#00285d",
    "secondary": "#4edea3",
    "secondary_container": "#00a572",
    "tertiary": "#ffb95f",
    "tertiary_container": "#ca8100",
    "on_surface": "#d3e4fe",
    "on_surface_variant": "#c2c6d6",
    "outline": "#8c909f",
    "outline_variant": "#424754",
    "error": "#ffb4ab",
}

SCRAPEFLOW_LOGO_URL = "https://lh3.googleusercontent.com/aida/AEtjO1WIv3jfadeVK7rGEbEXwV8auc3N6upx3Ha8YzJrQ2snFtnPG3DwcmQkha8Om_33p1O9qacJ123oZKGBtQIgQtA7GMofr7RBlOPKLkTVfcqqkFnuFr4U9pTVbtX7VCKgRqz1BSxHpUV5ahK62Hw2Eky-khG8pvJcaskXBiXKjPTdaJLauzGoKQLjyfCLwKOnchHoYfD11MU054JU5j0qB235sGQHTvPMXCWTx6K_h3xI4q9IXqo3YVy51_A"
USER_AVATAR_URL = "https://lh3.googleusercontent.com/aida-public/AB6AXuC8IqL6kWvrlvAWMqQNRKEI7u9615o-kOQel-edWukvpqxnxEifVdoqZzH0FprnOFAuuByLew5T2uN1ttQ2J-LsGN37BxYNOqQdmxzzGRzgV71r_G6PgE-ibLBXUmIWWixYDeU0SbLHECkYsrgNbHwrL3YGkuBDQIf8a3TsjRW4hfd1CN12IkLCX1INaHwYY6FrIHAdcja-XiisHNQkMQ-AKxV0vo91fsRY7Ql4--6fgHLDo7hJ1ezljw"
GPU_PREVIEW_IMG = "https://lh3.googleusercontent.com/aida-public/AB6AXuB0OJnXXagYQl_IkRrEjl1CG12DPsbhPlYv1Ys_sXmSxeicY7Xl097lPeTrgozVUkOhvfDuBqRqogFWvVFETeJTZhpNTGFFfAlvboufHSQT41vXRPj6pdLYcbqydmIJlwY7IqUGVjWySv3LrmferqUzDUk9--5DUg5eV6N2gJKhFH_O2_8cy5Tx4nvtVcx0kGovEk8hldu7lu6tAZiA_K6vR7Zja6Ps4KznwkmEPKnS8jexBdoD0_1nUQ"

def inject_custom_theme():
    """Injects the core dark CSS, Tailwind script, and Google Fonts into Streamlit."""
    st.markdown(
        """
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" />
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
        tailwind.config = {
          darkMode: "class",
          theme: {
            extend: {
              colors: {
                "surface": "#031427",
                "primary-fixed": "#d8e2ff",
                "outline-variant": "#424754",
                "surface-tint": "#adc6ff",
                "on-tertiary": "#472a00",
                "on-surface-variant": "#c2c6d6",
                "surface-container-low": "#0b1c30",
                "error": "#ffb4ab",
                "on-surface": "#d3e4fe",
                "on-primary-fixed": "#001a42",
                "secondary-fixed-dim": "#4edea3",
                "tertiary-fixed": "#ffddb8",
                "tertiary-container": "#ca8100",
                "inverse-primary": "#005ac2",
                "surface-bright": "#2a3a4f",
                "on-primary-container": "#00285d",
                "surface-container-lowest": "#000f21",
                "on-tertiary-container": "#3e2400",
                "primary-fixed-dim": "#adc6ff",
                "outline": "#8c909f",
                "on-primary-fixed-variant": "#004395",
                "primary": "#adc6ff",
                "secondary-container": "#00a572",
                "on-primary": "#002e6a",
                "background": "#031427",
                "on-secondary": "#003824",
                "surface-container-high": "#1b2b3f",
                "on-secondary-container": "#00311f",
                "secondary-fixed": "#6ffbbe",
                "on-secondary-fixed": "#002113",
                "on-secondary-fixed-variant": "#005236",
                "surface-container-highest": "#26364a",
                "inverse-on-surface": "#213145",
                "on-background": "#d3e4fe",
                "on-tertiary-fixed-variant": "#653e00",
                "on-error-container": "#ffdad6",
                "inverse-surface": "#d3e4fe",
                "primary-container": "#4d8eff",
                "surface-dim": "#031427",
                "surface-variant": "#26364a",
                "secondary": "#4edea3",
                "tertiary": "#ffb95f",
                "tertiary-fixed-dim": "#ffb95f",
                "error-container": "#93000a",
                "on-error": "#690005",
                "surface-container": "#102034",
                "on-tertiary-fixed": "#2a1700"
              },
              fontFamily: {
                "body-md": ["Inter", "sans-serif"],
                "code-md": ["JetBrains Mono", "monospace"],
                "headline-md": ["Inter", "sans-serif"],
              }
            }
          }
        }
        </script>
        <style>
            /* Base Streamlit App Overrides */
            html, body, [data-testid="stAppViewContainer"], .stApp {
                background-color: #031427 !important;
                color: #d3e4fe !important;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            }

            /* Remove default padding */
            .main .block-container {
                padding-top: 0.5rem !important;
                padding-bottom: 2rem !important;
                padding-left: 1.5rem !important;
                padding-right: 1.5rem !important;
                max-width: 100% !important;
            }

            /* Hide Streamlit Header & Footer */
            header[data-testid="stHeader"] {
                display: none !important;
            }
            footer {
                display: none !important;
            }

            /* Custom Dark Sidebar */
            [data-testid="stSidebar"] {
                background-color: #000f21 !important;
                border-right: 1px solid rgba(66, 71, 84, 0.3) !important;
                min-width: 260px !important;
                max-width: 280px !important;
            }
            [data-testid="stSidebar"] > div:first-child {
                padding-top: 0.5rem !important;
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }

            /* Scrollbar styling */
            ::-webkit-scrollbar {
                width: 6px;
                height: 6px;
            }
            ::-webkit-scrollbar-track {
                background: #000f21;
            }
            ::-webkit-scrollbar-thumb {
                background: #1b2b3f;
                border-radius: 3px;
            }
            ::-webkit-scrollbar-thumb:hover {
                background: #26364a;
            }

            /* Code font everywhere needed */
            code, pre, .font-code {
                font-family: 'JetBrains Mono', monospace !important;
            }

            /* Material symbols styling */
            .material-symbols-outlined {
                font-family: 'Material Symbols Outlined' !important;
                font-weight: normal;
                font-style: normal;
                font-size: 18px;
                line-height: 1;
                letter-spacing: normal;
                text-transform: none;
                display: inline-block;
                white-space: nowrap;
                word-wrap: normal;
                direction: ltr;
                -webkit-font-feature-settings: 'liga';
                -webkit-font-smoothing: antialiased;
                vertical-align: middle;
            }

            /* Streamlit widgets dark styling */
            div[data-testid="stTextInput"] input {
                background-color: #102034 !important;
                color: #d3e4fe !important;
                border: 1px solid rgba(66, 71, 84, 0.4) !important;
                border-radius: 8px !important;
                font-family: 'JetBrains Mono', monospace !important;
            }
            div[data-testid="stTextInput"] input:focus {
                border-color: #adc6ff !important;
                box-shadow: 0 0 0 1px #adc6ff !important;
            }

            /* Button dark styling */
            div.stButton > button {
                background-color: #4d8eff !important;
                color: #00285d !important;
                font-weight: 600 !important;
                border: none !important;
                border-radius: 8px !important;
                padding: 0.5rem 1rem !important;
                transition: all 0.2s ease !important;
            }
            div.stButton > button:hover {
                background-color: #adc6ff !important;
                color: #001a42 !important;
            }

            /* Radio & Toggle styling */
            [data-testid="stRadio"] label, [data-testid="stCheckbox"] label {
                color: #c2c6d6 !important;
                font-size: 0.85rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
