"""Left pane: Extraction schema and selector rules matching Stitch node bb592e1f18264b76811e85fc518f909f."""
import streamlit as st
from src.theme import GPU_PREVIEW_IMG

def render_schema_pane(first_record=None):
    """Renders the left pane containing schema selector rules, pagination config, and preview card."""
    record_title = first_record.get("title", "GeForce RTX 4090 OC 24GB Titanium") if first_record else "GeForce RTX 4090 OC 24GB Titanium"
    record_price = first_record.get("price", 1699.99) if first_record else 1699.99
    record_rating = first_record.get("rating_score", 4.9) if first_record else 4.9
    record_status = first_record.get("stock_status", "In Stock") if first_record else "In Stock"

    st.html(f"""
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <!-- Panel Header -->
        <div style="display: flex; align-items: center; justify-content: space-between; background: #0b1c30; padding: 12px 16px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2);">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span class="material-symbols-outlined" style="font-size: 18px; color: #adc6ff;">data_object</span>
                <span style="font-size: 16px; font-weight: 600; color: #d3e4fe;">Extraction Schema</span>
                <span style="padding: 2px 6px; background: #26364a; color: #adc6ff; font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; border-radius: 4px;">5 Fields</span>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; padding: 4px 10px; background: #ca8100; color: #3e2400; font-weight: 600; border-radius: 6px; font-size: 11px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                <span class="material-symbols-outlined" style="font-size: 14px;">auto_awesome</span>
                <span>AI Auto-Detect</span>
            </div>
        </div>

        <!-- Field Selector Rules -->
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <!-- Field 1: Title -->
            <div style="background: #0b1c30; padding: 12px; border-radius: 10px; border: 1px solid rgba(66, 71, 84, 0.2);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600; color: #adc6ff;">title</span>
                        <span style="background: #26364a; color: #c2c6d6; font-size: 10px; font-family: 'JetBrains Mono', monospace; padding: 2px 6px; border-radius: 4px;">String</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3; display: flex; align-items: center; gap: 4px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span> 48 matches
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #000f21; padding: 6px 10px; border-radius: 6px;">
                    <span style="font-size: 10px; font-weight: 700; color: #ffb95f; font-family: 'JetBrains Mono', monospace;">CSS</span>
                    <code style="font-size: 11px; color: #d3e4fe; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">h1.product-title, .p-name</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6; cursor: pointer;">filter_center_focus</span>
                </div>
            </div>

            <!-- Field 2: Price -->
            <div style="background: #0b1c30; padding: 12px; border-radius: 10px; border: 1px solid rgba(66, 71, 84, 0.2);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600; color: #adc6ff;">price</span>
                        <span style="background: #26364a; color: #c2c6d6; font-size: 10px; font-family: 'JetBrains Mono', monospace; padding: 2px 6px; border-radius: 4px;">Currency / Float</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3; display: flex; align-items: center; gap: 4px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span> 48 matches
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #000f21; padding: 6px 10px; border-radius: 6px;">
                    <span style="font-size: 10px; font-weight: 700; color: #adc6ff; font-family: 'JetBrains Mono', monospace;">XPATH</span>
                    <code style="font-size: 11px; color: #d3e4fe; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">//span[contains(@class,'price-tag')]/text()</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6; cursor: pointer;">filter_center_focus</span>
                </div>
            </div>

            <!-- Field 3: Stock Status -->
            <div style="background: #0b1c30; padding: 12px; border-radius: 10px; border: 1px solid rgba(66, 71, 84, 0.2);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600; color: #adc6ff;">stock_status</span>
                        <span style="background: #26364a; color: #c2c6d6; font-size: 10px; font-family: 'JetBrains Mono', monospace; padding: 2px 6px; border-radius: 4px;">Enum</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3; display: flex; align-items: center; gap: 4px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span> 48 matches
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #000f21; padding: 6px 10px; border-radius: 6px;">
                    <span style="font-size: 10px; font-weight: 700; color: #ffb95f; font-family: 'JetBrains Mono', monospace;">CSS</span>
                    <code style="font-size: 11px; color: #d3e4fe; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">.availability-badge</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6; cursor: pointer;">filter_center_focus</span>
                </div>
            </div>

            <!-- Field 4: Rating Score -->
            <div style="background: #0b1c30; padding: 12px; border-radius: 10px; border: 1px solid rgba(66, 71, 84, 0.2);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600; color: #adc6ff;">rating_score</span>
                        <span style="background: #26364a; color: #c2c6d6; font-size: 10px; font-family: 'JetBrains Mono', monospace; padding: 2px 6px; border-radius: 4px;">Regex / Number</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #ffb95f; display: flex; align-items: center; gap: 4px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #ffb95f;"></span> 46 matches (2 null)
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #000f21; padding: 6px 10px; border-radius: 6px;">
                    <span style="font-size: 10px; font-weight: 700; color: #ffb4ab; font-family: 'JetBrains Mono', monospace;">REGEX</span>
                    <code style="font-size: 11px; color: #d3e4fe; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">/([0-9.]+) out of 5/</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6; cursor: pointer;">filter_center_focus</span>
                </div>
            </div>

            <!-- Field 5: Image URL -->
            <div style="background: #0b1c30; padding: 12px; border-radius: 10px; border: 1px solid rgba(66, 71, 84, 0.2);">
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 600; color: #adc6ff;">image_url</span>
                        <span style="background: #26364a; color: #c2c6d6; font-size: 10px; font-family: 'JetBrains Mono', monospace; padding: 2px 6px; border-radius: 4px;">URL</span>
                    </div>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4edea3; display: flex; align-items: center; gap: 4px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #4edea3;"></span> 48 matches
                    </span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; background: #000f21; padding: 6px 10px; border-radius: 6px;">
                    <span style="font-size: 10px; font-weight: 700; color: #ffb95f; font-family: 'JetBrains Mono', monospace;">CSS ATTR</span>
                    <code style="font-size: 11px; color: #d3e4fe; flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">img.gallery-main::attr(src)</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6; cursor: pointer;">filter_center_focus</span>
                </div>
            </div>
        </div>

        <!-- Add Field Button -->
        <button type="button" style="
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            background: #102034;
            border: 1px solid rgba(66, 71, 84, 0.3);
            color: #d3e4fe;
            padding: 8px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 500;
            cursor: pointer;
            width: 100%;
        ">
            <span class="material-symbols-outlined" style="font-size: 16px;">add</span>
            <span>Add Field Mapping</span>
        </button>

        <!-- Pagination, Depth & Crawl Limits Settings Card -->
        <div style="background: #0b1c30; padding: 14px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2);">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span class="material-symbols-outlined" style="font-size: 16px; color: #c2c6d6;">route</span>
                    <span style="font-size: 14px; font-weight: 600; color: #d3e4fe;">Crawl &amp; Pagination Engine</span>
                </div>
                <span style="padding: 2px 6px; background: rgba(78, 222, 163, 0.15); color: #4edea3; font-size: 10px; font-family: 'JetBrains Mono', monospace; font-weight: 600; border-radius: 4px;">ACTIVE</span>
            </div>
            <div style="margin-bottom: 8px;">
                <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Next Page Selector</span>
                <div style="display: flex; align-items: center; background: #000f21; padding: 6px 10px; border-radius: 6px; margin-top: 4px;">
                    <code style="font-size: 11px; color: #4edea3; flex: 1;">a[rel='next'], button.load-more-btn</code>
                    <span class="material-symbols-outlined" style="font-size: 14px; color: #c2c6d6;">touch_app</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div style="background: #102034; padding: 8px; border-radius: 8px;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Max Depth</span>
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 2px;">
                        <span style="font-size: 14px; font-weight: 600; color: #d3e4fe; font-family: 'JetBrains Mono', monospace;">50 pages</span>
                        <span class="material-symbols-outlined" style="font-size: 14px; color: #adc6ff;">auto_stories</span>
                    </div>
                </div>
                <div style="background: #102034; padding: 8px; border-radius: 8px;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; text-transform: uppercase;">Rate Limit</span>
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 2px;">
                        <span style="font-size: 14px; font-weight: 600; color: #d3e4fe; font-family: 'JetBrains Mono', monospace;">8.0 req/sec</span>
                        <span class="material-symbols-outlined" style="font-size: 14px; color: #4edea3;">speed</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Visual Sample Extraction Preview Card -->
        <div style="background: #0b1c30; padding: 14px; border-radius: 12px; border: 1px solid rgba(66, 71, 84, 0.2); display: flex; align-items: center; gap: 14px;">
            <img src="{GPU_PREVIEW_IMG}" alt="Sample Match GPU" style="width: 76px; height: 76px; border-radius: 8px; object-fit: cover; background: #26364a; flex-shrink: 0;" />
            <div style="flex: 1; min-width: 0;">
                <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="font-size: 10px; font-family: 'JetBrains Mono', monospace; background: rgba(78, 222, 163, 0.15); color: #4edea3; padding: 2px 6px; border-radius: 4px;">First Record Match</span>
                    <span style="font-size: 11px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6;">ID: #0829-RTX</span>
                </div>
                <h4 style="font-size: 13px; font-weight: 600; color: #d3e4fe; margin: 4px 0 2px 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                    {record_title}
                </h4>
                <div style="display: flex; align-items: center; gap: 8px; font-size: 11px; font-family: 'JetBrains Mono', monospace; color: #c2c6d6; margin-top: 4px;">
                    <span style="color: #4edea3; font-weight: 600;">${record_price:,.2f}</span>
                    <span>•</span>
                    <span style="color: #ffb95f;">★ {record_rating}/5</span>
                    <span>•</span>
                    <span style="color: #4edea3;">{record_status}</span>
                </div>
            </div>
        </div>
    </div>
    """)
