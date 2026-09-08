"""Top command & configuration bar matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st

def render_command_bar(default_url="https://market-intel.domain.com/v2/catalog?category=gpus&page=1"):
    """
    Renders the Target URL and primary execution row with quick anti-bot config toggles.
    Returns (target_url, execute_clicked, config_dict).
    """
    st.html("""
    <div style="background: #0b1c30; padding: 14px 18px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25); border: 1px solid rgba(66, 71, 84, 0.2); margin-bottom: 16px;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="material-symbols-outlined" style="font-size: 18px; color: #adc6ff;">terminal</span>
                <span style="font-size: 13px; font-weight: 600; color: #d3e4fe; letter-spacing: -0.01em;">Execution Dispatcher & Endpoint Target</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3;">
                <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span>
                <span>200 OK • 286ms</span>
            </div>
        </div>
    """)

    col_method, col_url, col_btn = st.columns([1, 6, 2])

    with col_method:
        method = st.selectbox("HTTP Method", ["GET", "POST"], index=0, label_visibility="collapsed")

    with col_url:
        target_url = st.text_input(
            "Target URL",
            value=default_url,
            placeholder="Enter scrapable URL or API endpoint...",
            label_visibility="collapsed"
        )

    with col_btn:
        execute_clicked = st.button("⚡ Execute Scrape", use_container_width=True)

    # Quick Config Toggles Strip
    st.html("""
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 8px; padding-top: 10px; border-top: 1px solid rgba(66, 71, 84, 0.2); margin-top: 8px;">
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px;">
                <!-- Toggle: JS Rendering -->
                <div style="display: flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 9999px; background: #1b2b3f; color: #4edea3; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 500;">
                    <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span>
                    <span class="material-symbols-outlined" style="font-size: 14px;">javascript</span>
                    <span>Playwright / Chrome 122</span>
                </div>
                <!-- Toggle: Residential Proxy -->
                <div style="display: flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 9999px; background: #102034; color: #d3e4fe; font-family: 'JetBrains Mono', monospace; font-size: 11px;">
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #adc6ff;">public</span>
                    <span>Residential IP (US-East)</span>
                    <span style="color: #c2c6d6; font-size: 10px;">#Pool-B2</span>
                </div>
                <!-- Toggle: Auto Solve CAPTCHA -->
                <div style="display: flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 9999px; background: #1b2b3f; color: #4edea3; font-family: 'JetBrains Mono', monospace; font-size: 11px;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">verified_user</span>
                    <span>Turnstile Auto-Bypass</span>
                </div>
                <!-- Toggle: Fingerprint Spoof -->
                <div style="display: flex; align-items: center; gap: 6px; padding: 4px 10px; border-radius: 9999px; background: #102034; color: #d3e4fe; font-family: 'JetBrains Mono', monospace; font-size: 11px;">
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #ffb95f;">fingerprint</span>
                    <span>Spoof v4 (Canvas + WebGL)</span>
                </div>
            </div>

            <!-- Drawer Triggers -->
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.2);">
                    <span class="material-symbols-outlined" style="font-size: 13px;">tune</span>
                    <span>Headers (4)</span>
                </div>
                <div style="display: flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.2);">
                    <span class="material-symbols-outlined" style="font-size: 13px;">cookie</span>
                    <span>Cookies (2)</span>
                </div>
                <div style="display: flex; align-items: center; gap: 4px; padding: 3px 8px; border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.2);">
                    <span class="material-symbols-outlined" style="font-size: 13px;">timer</span>
                    <span>Wait: 1500ms</span>
                </div>
            </div>
        </div>
    </div>
    """)

    return target_url, execute_clicked
