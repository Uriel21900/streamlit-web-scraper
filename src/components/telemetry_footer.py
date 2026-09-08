"""Bottom telemetry widgets and keyboard shortcuts bar matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st

def render_telemetry_footer():
    """Renders the bottom 3 telemetry status cards and shortcut bar."""
    st.html("""
    <!-- Telemetry Cards Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-top: 14px; margin-bottom: 14px;">
        <!-- Card 1: Proxy Health -->
        <div style="background: #0b1c30; padding: 14px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2); display: flex; align-items: center; gap: 14px;">
            <div style="padding: 10px; background: #102034; border-radius: 8px; color: #4edea3; display: flex; align-items: center; justify-content: center;">
                <span class="material-symbols-outlined" style="font-size: 24px;">vpn_lock</span>
            </div>
            <div style="flex: 1; min-width: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Proxy Health</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #4edea3; font-weight: 600;">99.4%</span>
                </div>
                <div style="width: 100%; background: #26364a; height: 5px; border-radius: 9999px; margin-top: 6px; overflow: hidden;">
                    <div style="background: #4edea3; height: 100%; width: 99.4%; border-radius: 9999px;"></div>
                </div>
                <span style="font-size: 11px; color: #c2c6d6; margin-top: 4px; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">US-East IP pool rotated 34s ago</span>
            </div>
        </div>

        <!-- Card 2: Extraction Throughput -->
        <div style="background: #0b1c30; padding: 14px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2); display: flex; align-items: center; gap: 14px;">
            <div style="padding: 10px; background: #102034; border-radius: 8px; color: #adc6ff; display: flex; align-items: center; justify-content: center;">
                <span class="material-symbols-outlined" style="font-size: 24px;">bolt</span>
            </div>
            <div style="flex: 1; min-width: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Throughput</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #adc6ff; font-weight: 600;">1,142 rec/min</span>
                </div>
                <div style="width: 100%; background: #26364a; height: 5px; border-radius: 9999px; margin-top: 6px; overflow: hidden;">
                    <div style="background: #4d8eff; height: 100%; width: 78%; border-radius: 9999px;"></div>
                </div>
                <span style="font-size: 11px; color: #c2c6d6; margin-top: 4px; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Pipeline throttle headroom at 22%</span>
            </div>
        </div>

        <!-- Card 3: Anti-Bot Defense Status -->
        <div style="background: #0b1c30; padding: 14px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2); display: flex; align-items: center; gap: 14px;">
            <div style="padding: 10px; background: #102034; border-radius: 8px; color: #ffb95f; display: flex; align-items: center; justify-content: center;">
                <span class="material-symbols-outlined" style="font-size: 24px;">shield</span>
            </div>
            <div style="flex: 1; min-width: 0;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Defense Clearance</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #ffb95f; font-weight: 600;">Zero Blocks</span>
                </div>
                <div style="width: 100%; background: #26364a; height: 5px; border-radius: 9999px; margin-top: 6px; overflow: hidden;">
                    <div style="background: #ffb95f; height: 100%; width: 100%; border-radius: 9999px;"></div>
                </div>
                <span style="font-size: 11px; color: #c2c6d6; margin-top: 4px; display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">Turnstile + Datadome stealth passing</span>
            </div>
        </div>
    </div>

    <!-- Keyboard Shortcuts & Status Micro-Bar -->
    <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: rgba(194, 198, 214, 0.6); padding: 4px 6px; border-top: 1px solid rgba(66, 71, 84, 0.15);">
        <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
            <span><kbd style="background: #0b1c30; padding: 2px 6px; border-radius: 4px; color: #d3e4fe; border: 1px solid rgba(66, 71, 84, 0.3);">⌘ + ↵</kbd> Run Scrape</span>
            <span><kbd style="background: #0b1c30; padding: 2px 6px; border-radius: 4px; color: #d3e4fe; border: 1px solid rgba(66, 71, 84, 0.3);">⌘ + S</kbd> Save Blueprint</span>
            <span><kbd style="background: #0b1c30; padding: 2px 6px; border-radius: 4px; color: #d3e4fe; border: 1px solid rgba(66, 71, 84, 0.3);">⌥ + P</kbd> Preview Selector</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
            <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span>
            <span>ScrapeFlow Engine Cluster v2.4 • Ready</span>
        </div>
    </div>
    """)
