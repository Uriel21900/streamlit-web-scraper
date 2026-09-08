"""Sidebar navigation matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st
from src.theme import SCRAPEFLOW_LOGO_URL

def render_sidebar():
    """Renders the exact dark ScrapeFlow sidebar."""
    with st.sidebar:
        # Header with Logo & Version
        st.html(f"""
        <div style="height: 56px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid rgba(66, 71, 84, 0.2); padding-bottom: 8px; margin-bottom: 12px;">
            <img src="{SCRAPEFLOW_LOGO_URL}" alt="ScrapeFlow Logo" style="height: 32px; width: auto; object-fit: contain;" />
            <span style="font-size: 18px; font-weight: 600; letter-spacing: -0.015em; color: #d3e4fe; margin-left: 4px;">ScrapeFlow</span>
            <span style="margin-left: auto; font-size: 10px; font-family: 'JetBrains Mono', monospace; font-weight: 600; text-transform: uppercase; background: #1b2b3f; color: #adc6ff; padding: 2px 6px; border-radius: 4px;">v2.4</span>
        </div>

        <div style="display: flex; align-items: center; justify-content: space-between; padding: 4px 6px; font-size: 10px; font-family: 'JetBrains Mono', monospace; font-weight: 600; text-transform: uppercase; color: rgba(194, 198, 214, 0.7); margin-bottom: 8px;">
            <span>Navigation Core</span>
            <span class="material-symbols-outlined" style="font-size: 14px;">keyboard_arrow_down</span>
        </div>
        """)

        # Streamlit Radio navigation disguised in ScrapeFlow style
        nav_options = [
            "Extraction Studio",
            "Active Scrape Jobs (4 running)",
            "Schema & Selectors",
            "Proxies & Anti-Bot",
            "API & Webhooks",
            "Settings & Limits",
        ]

        selected_nav = st.radio(
            "Navigation Core",
            nav_options,
            index=0,
            label_visibility="collapsed"
        )

        st.html("""
        <div style="margin-top: 1.5rem; border-top: 1px solid rgba(66, 71, 84, 0.2); padding-top: 1rem;">
            <div style="font-size: 11px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">View Configuration</div>
        </div>
        """)

        # Stitch 1:1 View Toggle
        preview_mode = st.toggle(
            "🖥️ 1:1 Stitch Mode",
            value=False,
            help="Toggle pixel-perfect exact Stitch canvas view from node bb592e1f18264b76811e85fc518f909f"
        )

        # Bottom Proxy Health Status Card
        st.html("""
        <div style="margin-top: 2rem; padding: 12px; border-radius: 8px; border: 1px solid rgba(66, 71, 84, 0.2); background: rgba(11, 28, 48, 0.5);">
            <div style="display: flex; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #c2c6d6;">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="width: 8px; height: 8px; border-radius: 50%; background: #4edea3; display: inline-block;"></span>
                    <span>Pool Healthy</span>
                </div>
                <span style="color: #4edea3; font-weight: 600;">99.4%</span>
            </div>
            <div style="width: 100%; background: #26364a; height: 4px; border-radius: 9999px; margin-top: 6px; overflow: hidden;">
                <div style="background: #4edea3; height: 100%; width: 99.4%; border-radius: 9999px;"></div>
            </div>
            <div style="font-size: 10px; color: #8c909f; margin-top: 6px; font-family: 'JetBrains Mono', monospace;">
                32/40 Workers Active • TLS 1.3
            </div>
        </div>
        """)

        return selected_nav, preview_mode
