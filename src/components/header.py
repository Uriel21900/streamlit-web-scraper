"""Top operational cluster header matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st
from src.theme import USER_AVATAR_URL

def render_header(cluster_name="prod-ecom-crawler-us-east", active_workers=32, total_workers=40, req_rate="12.4"):
    """Renders the top operational header with telemetry metrics and user profile."""
    st.html(f"""
    <div style="
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        padding: 8px 16px;
        background: rgba(0, 15, 33, 0.9);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid rgba(66, 71, 84, 0.25);
        border-radius: 12px;
        margin-bottom: 16px;
    ">
        <!-- Left Section: Cluster Selector & Quick Search -->
        <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <div style="
                display: flex;
                align-items: center;
                gap: 6px;
                background: #0b1c30;
                border: 1px solid rgba(66, 71, 84, 0.3);
                padding: 4px 10px;
                border-radius: 6px;
                font-family: 'JetBrains Mono', monospace;
                font-size: 11px;
                color: #d3e4fe;
                cursor: pointer;
            ">
                <span class="material-symbols-outlined" style="font-size: 16px; color: #adc6ff;">dns</span>
                <span>{cluster_name}</span>
                <span class="material-symbols-outlined" style="font-size: 16px; color: #c2c6d6;">unfold_more</span>
            </div>

            <div style="
                display: flex;
                align-items: center;
                gap: 8px;
                background: #0b1c30;
                border: 1px solid rgba(66, 71, 84, 0.3);
                padding: 4px 12px;
                border-radius: 6px;
                color: #c2c6d6;
                width: 260px;
            ">
                <span class="material-symbols-outlined" style="font-size: 16px;">search</span>
                <span style="font-size: 12px; flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Cmd + K to jump or run...</span>
                <kbd style="background: #26364a; padding: 2px 5px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 10px; border: 1px solid rgba(66, 71, 84, 0.3);">⌘K</kbd>
            </div>
        </div>

        <!-- Right Section: Live Telemetry, Extraction Button & Profile -->
        <div style="display: flex; align-items: center; gap: 16px;">
            <div style="
                display: flex;
                align-items: center;
                gap: 8px;
                background: #102034;
                padding: 4px 10px;
                border-radius: 6px;
                border: 1px solid rgba(66, 71, 84, 0.2);
                font-family: 'JetBrains Mono', monospace;
                font-size: 11px;
                color: #c2c6d6;
            ">
                <span style="width: 7px; height: 7px; border-radius: 50%; background: #4edea3; display: inline-block; box-shadow: 0 0 8px #4edea3;"></span>
                <span style="color: #d3e4fe;">{active_workers}/{total_workers} Workers Active</span>
                <span style="color: #424754;">•</span>
                <span style="color: #adc6ff;">{req_rate} req/s</span>
            </div>

            <div style="display: flex; align-items: center; gap: 12px; border-left: 1px solid rgba(66, 71, 84, 0.3); padding-left: 12px;">
                <button type="button" style="
                    background: transparent;
                    border: none;
                    color: #c2c6d6;
                    cursor: pointer;
                    position: relative;
                    padding: 4px;
                    display: flex;
                    align-items: center;
                ">
                    <span class="material-symbols-outlined" style="font-size: 20px;">notifications</span>
                    <span style="position: absolute; top: 3px; right: 3px; width: 6px; height: 6px; border-radius: 50%; background: #ffb4ab;"></span>
                </button>

                <div style="position: relative; display: flex; align-items: center;">
                    <img src="{USER_AVATAR_URL}" alt="Profile" style="width: 32px; height: 32px; border-radius: 50%; object-fit: cover; border: 1px solid rgba(66, 71, 84, 0.4);" />
                    <span style="position: absolute; bottom: 0; right: 0; width: 8px; height: 8px; border-radius: 50%; background: #4edea3; border: 2px solid #000f21;"></span>
                </div>
            </div>
        </div>
    </div>
    """)
