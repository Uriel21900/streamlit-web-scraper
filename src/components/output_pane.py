"""Right pane: Output tabs, formatted JSON viewer, sparkline, and live terminal drawer."""
import json
import streamlit as st

DEFAULT_MOCK_JSON = [
    {
        "item_index": 0,
        "title": "GeForce RTX 4090 OC 24GB Titanium Series",
        "price": 1699.99,
        "currency": "USD",
        "stock_status": "IN_STOCK",
        "rating_score": 4.9,
        "image_url": "https://assets.domain.com/catalog/gpu-titanium-4090.webp",
        "extracted_at": "2025-02-23T14:22:01.590Z",
        "source_meta": {
            "dom_depth": 14,
            "xpath_eval_time_ms": 1.2
        }
    },
    {
        "item_index": 1,
        "title": "Radeon RX 7900 XTX 24GB Vapor-X Gaming Edition",
        "price": 949.50,
        "currency": "USD",
        "stock_status": "LOW_STOCK",
        "rating_score": 4.7,
        "image_url": "https://assets.domain.com/catalog/rx-7900-vapor.webp",
        "extracted_at": "2025-02-23T14:22:01.591Z"
    },
    {
        "item_index": 2,
        "title": "GeForce RTX 4080 Super Ultra 16GB Dual BIOS",
        "price": 1049.00,
        "currency": "USD",
        "stock_status": "IN_STOCK",
        "rating_score": 4.8,
        "image_url": "https://assets.domain.com/catalog/rtx-4080s-ultra.webp",
        "extracted_at": "2025-02-23T14:22:01.592Z"
    }
]

def render_output_pane(records=None, logs=None, payload_size="38.4 KB", parse_time="42ms", peak_latency="312ms"):
    """Renders the execution studio output pane with JSON viewer and streaming terminal."""
    if records is None:
        records = DEFAULT_MOCK_JSON

    total_count = len(records)
    json_formatted = json.dumps(records[:15], indent=2)

    st.html(f"""
    <div style="background: #0b1c30; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2); overflow: hidden; display: flex; flex-direction: column;">
        <!-- Tabbed Header & Export Bar -->
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; background: #000f21; padding: 8px 14px; border-bottom: 1px solid rgba(66, 71, 84, 0.2);">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="display: flex; align-items: center; gap: 6px; padding: 6px 12px; background: #1b2b3f; color: #adc6ff; border-radius: 8px; font-size: 12px; font-weight: 500;">
                    <span class="material-symbols-outlined" style="font-size: 16px;">data_array</span>
                    <span>Parsed JSON</span>
                    <span style="background: rgba(173, 198, 255, 0.2); color: #adc6ff; padding: 1px 6px; border-radius: 9999px; font-size: 10px; font-family: 'JetBrains Mono', monospace;">{total_count}</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; padding: 6px 12px; color: #c2c6d6; font-size: 12px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 16px;">html</span>
                    <span>Response HTML</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; padding: 6px 12px; color: #c2c6d6; font-size: 12px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 16px;">device_hub</span>
                    <span>DOM Tree</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px; padding: 6px 12px; color: #c2c6d6; font-size: 12px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 16px;">monitor_heart</span>
                    <span>Network</span>
                </div>
            </div>

            <!-- Export Controls -->
            <div style="display: flex; align-items: center; gap: 6px;">
                <button type="button" style="display: flex; align-items: center; gap: 4px; padding: 4px 8px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.3); border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">content_copy</span>
                    <span>Copy</span>
                </button>
                <button type="button" style="display: flex; align-items: center; gap: 4px; padding: 4px 8px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.3); border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">download</span>
                    <span>JSON</span>
                </button>
                <button type="button" style="display: flex; align-items: center; gap: 4px; padding: 4px 8px; background: #102034; border: 1px solid rgba(66, 71, 84, 0.3); border-radius: 6px; color: #c2c6d6; font-family: 'JetBrains Mono', monospace; font-size: 11px; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">table_view</span>
                    <span>CSV</span>
                </button>
                <button type="button" style="display: flex; align-items: center; gap: 4px; padding: 4px 8px; background: #4d8eff; color: #00285d; border: none; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 600; cursor: pointer;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">sensors</span>
                    <span>Webhook</span>
                </button>
            </div>
        </div>

        <!-- Telemetry Summary Bar -->
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 8px 14px; background: #102034; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #c2c6d6; border-bottom: 1px solid rgba(66, 71, 84, 0.15);">
            <div style="display: flex; align-items: center; gap: 14px;">
                <span style="color: #4edea3; display: flex; align-items: center; gap: 6px;">
                    <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span>
                    <span>{total_count} Items Extracted</span>
                </span>
                <span>Payload Size: <strong style="color: #d3e4fe;">{payload_size}</strong></span>
                <span>Parsing Time: <strong style="color: #4edea3;">{parse_time}</strong></span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px;">
                <span>Validation:</span>
                <span style="color: #4edea3; background: rgba(78, 222, 163, 0.15); padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">100% Validated</span>
            </div>
        </div>

        <!-- Interactive JSON Viewer -->
        <div style="padding: 14px; background: #000f21; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #d3e4fe; line-height: 1.6; max-height: 280px; overflow-y: auto;">
            <div style="color: rgba(194, 198, 214, 0.4); margin-bottom: 6px;">// Schema execution output: {total_count} items parsed against 5 selector rules</div>
            <pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #d3e4fe;">{json_formatted}</pre>
        </div>

        <!-- Telemetry Execution Sparkline -->
        <div style="padding: 8px 14px; background: #102034; display: flex; align-items: center; justify-content: space-between; border-top: 1px solid rgba(66, 71, 84, 0.2); border-bottom: 1px solid rgba(66, 71, 84, 0.2);">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; color: #c2c6d6;">Execution Timing</span>
                <svg style="width: 120px; height: 20px; color: #adc6ff;" fill="none" viewBox="0 0 120 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M0 18L15 14L30 19L45 8L60 12L75 4L90 10L105 3L120 7" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
                    <circle cx="105" cy="3" fill="#4edea3" r="2.5"></circle>
                </svg>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3;">Peak: {peak_latency}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #c2c6d6;">
                <span>RAM: <strong style="color: #d3e4fe;">142MB</strong></span>
                <span>•</span>
                <span>Thread: <strong style="color: #d3e4fe;">Worker-07</strong></span>
                <span>•</span>
                <span style="color: #4edea3;">TLS 1.3 HTTP/2</span>
            </div>
        </div>

        <!-- Live Terminal Streaming Log Drawer -->
        <div style="padding: 10px 14px; background: #000f21; display: flex; flex-direction: column;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px; font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #c2c6d6;">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span class="material-symbols-outlined" style="font-size: 14px;">terminal</span>
                    <span style="text-transform: uppercase; font-weight: 600;">Live Extraction Worker Stream</span>
                </div>
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span>
                    <span>Streaming Active</span>
                </div>
            </div>

            <div style="background: rgba(16, 32, 52, 0.4); padding: 8px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 11px; max-height: 120px; overflow-y: auto; display: flex; flex-direction: column; gap: 4px;">
                <div style="display: flex; gap: 8px;">
                    <span style="color: #8c909f;">[14:22:01.042]</span>
                    <span style="color: #adc6ff; font-weight: 600;">[INFO]</span>
                    <span style="color: #c2c6d6;">[Worker #7]</span>
                    <span style="color: #d3e4fe;">Dispatching headless Chromium instance (Stealth v2.4, fingerprint profile #402)...</span>
                </div>
                <div style="display: flex; gap: 8px;">
                    <span style="color: #8c909f;">[14:22:01.328]</span>
                    <span style="color: #4edea3; font-weight: 600;">[200 OK]</span>
                    <span style="color: #c2c6d6;">[Worker #7]</span>
                    <span style="color: #4edea3;">Handshake established with target (Latency: 286ms, Cloudflare Turnstile token solved).</span>
                </div>
                <div style="display: flex; gap: 8px;">
                    <span style="color: #8c909f;">[14:22:01.590]</span>
                    <span style="color: #ffb95f; font-weight: 600;">[EXTRACT]</span>
                    <span style="color: #c2c6d6;">[Engine]</span>
                    <span style="color: #d3e4fe;">{total_count} structured records parsed against schema in <span style="color: #4edea3; font-weight: 600;">{parse_time}</span>. Validation: 0 errors.</span>
                </div>
                <div style="display: gap: 8px;">
                    <span style="color: #8c909f;">[14:22:01.612]</span>
                    <span style="color: #adc6ff; font-weight: 600;">[SYNC]</span>
                    <span style="color: #c2c6d6;">[Dispatcher]</span>
                    <span style="color: #d3e4fe;">Staging payload for downstream ingestion pipeline (Buffer: {payload_size}).</span>
                </div>
            </div>
        </div>
    </div>
    """)
