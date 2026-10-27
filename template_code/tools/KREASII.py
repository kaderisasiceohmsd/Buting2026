import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from fractions import Fraction
import math

# ==============================================================================
#        KREASII - JORDAN CODEX: SATU NAMA, DUA REVOLUSI SAINS DATA
#          Wilhelm Jordan (1888) & Michael I. Jordan (1986)
# ==============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Poppins:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

    .main .block-container,
    [data-testid="stMainBlockContainer"],
    [data-testid="stAppViewBlockContainer"] {
        max-width: 960px !important;
        width: 100% !important;
        padding-top: 1.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }
    @media (max-width: 640px) {
        .main .block-container,
        [data-testid="stMainBlockContainer"],
        [data-testid="stAppViewBlockContainer"] {
            padding-left: 0.65rem !important;
            padding-right: 0.65rem !important;
        }
    }

    .jordan-hero {
        text-align: center;
        padding: 2rem 1.4rem 1.3rem 1.4rem;
        background: radial-gradient(ellipse at 50% 15%, rgba(255, 215, 64, 0.12) 0%, rgba(12, 14, 28, 0) 72%);
        border-radius: 18px;
        margin-bottom: 1.4rem;
        border: 1px solid rgba(255, 215, 64, 0.24);
    }
    .jordan-badge {
        display: inline-block;
        padding: 4px 16px;
        border-radius: 20px;
        background: rgba(255, 215, 64, 0.12);
        color: #ffd740;
        border: 1px solid rgba(255, 215, 64, 0.35);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.74em;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.55rem;
    }
    .jordan-title {
        font-family: 'Cinzel', 'Poppins', serif;
        font-size: 2.45em;
        font-weight: 800;
        background: linear-gradient(135deg, #fff6d6 0%, #ffd740 50%, #ffab40 85%, #ff6e40 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
        margin: 0;
        line-height: 1.22;
    }
    .jordan-subtitle {
        font-family: 'Poppins', sans-serif;
        color: #b0bec5;
        font-size: 0.95em;
        max-width: 820px;
        margin: 0.55rem auto 0 auto;
        line-height: 1.55;
    }
    .gold-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 1.4rem auto 1.6rem auto;
        max-width: 520px;
        border: none;
    }

    /* Concept & Telemetry Cards */
    .concept-card {
        background: linear-gradient(155deg, rgba(19, 21, 44, 0.92), rgba(10, 11, 24, 0.96));
        border: 1px solid rgba(255, 215, 64, 0.22);
        border-radius: 16px;
        padding: 1.35rem 1.5rem;
        margin-bottom: 1.15rem;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
    }
    .concept-card:hover {
        border-color: rgba(255, 215, 64, 0.42);
    }
    .card-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.18em;
        font-weight: 700;
        color: #ffd740;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .card-text {
        color: #cfd8dc;
        font-size: 0.93em;
        line-height: 1.65;
    }
    .formula-pill {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.88em;
        color: #ffd740;
        background: rgba(255, 215, 64, 0.1);
        border: 1px solid rgba(255, 215, 64, 0.28);
        border-radius: 7px;
        padding: 2px 8px;
        margin: 1px 2px;
    }
    .step-box {
        background: rgba(12, 14, 30, 0.82);
        border: 1px solid rgba(255, 215, 64, 0.2);
        border-left: 4px solid #ffd740;
        border-radius: 12px;
        padding: 0.95rem 1.2rem;
        margin: 0.85rem 0;
    }
    .step-header {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #ffd740;
        font-size: 0.96em;
        margin-bottom: 0.35rem;
    }
    .diagram-box {
        background: linear-gradient(160deg, #0d1024 0%, #070814 100%);
        border: 1px solid rgba(128, 216, 255, 0.28);
        border-radius: 16px;
        padding: 1.1rem;
        text-align: center;
        margin: 0.9rem 0 1.1rem 0;
        box-shadow: inset 0 0 28px rgba(0, 0, 0, 0.6);
    }
    .node-stat-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
        margin: 0.7rem 0 1.2rem 0;
    }
    @media (max-width: 760px) {
        .node-stat-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .jordan-title {
            font-size: 1.85em;
        }
    }
    .node-stat-box {
        background: rgba(15, 18, 38, 0.9);
        border: 1px solid rgba(255, 215, 64, 0.24);
        border-radius: 12px;
        padding: 10px 12px;
        text-align: center;
    }
    .node-stat-lbl {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72em;
        color: #90a4ae;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .node-stat-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.22em;
        font-weight: 800;
        color: #ffd740;
        margin-top: 3px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
#                                HERO HEADER
# ==============================================================================
st.markdown("""
<div class='jordan-hero'>
    <div class='jordan-badge'>✦ ASTRAL CODEX • KONSTELASI JORDAN ✦</div>
    <h1 class='jordan-title'>🌌 JORDAN CODEX: TIGA JORDAN DI SAINS DATA</h1>
    <p class='jordan-subtitle'>
        Satu nama <b>Jordan</b>, tiga tokoh besar. Dua idenya bisa kamu coba langsung di sini: <b>Eliminasi Gauss-Jordan (1888)</b> untuk menyelesaikan sistem persamaan, dan <b>Jordan Recurrent Neural Network (1986)</b> untuk jaringan saraf yang punya ingatan. Tokoh ketiga, <b>Camille Jordan</b>, kami bahas di tab terakhir.
    </p>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
#                   MENU LAZY-LOAD (HANYA MERENDER TAB AKTIF)
# ==============================================================================
active_codex = option_menu(
    menu_title=None,
    options=[
        "Jordan Recurrent Network (JRN)",
        "Eliminasi Gauss-Jordan",
        "Sintesis Tiga Jordan",
    ],
    icons=[
        "cpu-fill",
        "grid-3x3",
        "stars",
    ],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "6px 6px!important",
            "background-color": "#101224",
            "border-radius": "14px",
            "border": "1px solid rgba(255, 215, 64, 0.3)",
            "margin-bottom": "1.4rem",
        },
        "icon": {"color": "#ffd740", "font-size": "15px"},
        "nav-link": {
            "font-size": "13.5px",
            "font-weight": "600",
            "text-align": "center",
            "margin": "2px 4px",
            "color": "#cfd8dc",
            "--hover-color": "rgba(255, 215, 64, 0.14)",
            "border-radius": "9px",
        },
        "nav-link-selected": {
            "background-color": "#ff9800",
            "color": "#090a14",
            "font-weight": "800",
        },
    },
)


# ==============================================================================
#         TAB 1: JORDAN RECURRENT NEURAL NETWORK (MICHAEL I. JORDAN, 1986)
# ==============================================================================
if active_codex == "Jordan Recurrent Network (JRN)":
    st.markdown("""
    <div class='concept-card'>
        <div class='card-title'>🧠 Michael I. Jordan dan Jordan Network (1986)</div>
        <div class='card-text'>
            Tahun 1986, <b>Michael I. Jordan</b> (UC Berkeley) memperkenalkan salah satu <b>Recurrent Neural Network (RNN)</b> pertama lewat makalah <i>"Serial Order: A Parallel Distributed Processing Approach"</i>.<br><br>
            Jaringan <i>feedforward</i> biasa tidak punya ingatan: input masuk, output keluar, selesai. Jordan Network menambahkan <b>Context Unit</b> yang menyimpan jejak output sebelumnya, sehingga keputusan saat ini ikut dipengaruhi oleh tindakan masa lalu:
            <div style='margin-top:0.65rem;display:flex;flex-wrap:wrap;gap:8px;'>
                <span class='formula-pill'>Jordan Network (1986): c(t) = &alpha;&middot;c(t-1) + (1-&alpha;)&middot;y(t-1)</span>
                <span class='formula-pill' style='color:#80d8ff;border-color:rgba(128,216,255,0.35);background:rgba(128,216,255,0.08);'>Elman Network (1990): c(t) = &alpha;&middot;c(t-1) + (1-&alpha;)&middot;h(t-1)</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📐 Lihat Persamaan Matematika Formal Jordan Network vs Elman Network", expanded=False):
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            st.markdown("**1. Jordan Recurrent Network (Output-to-State Feedback):**")
            st.latex(r"c(t) = \alpha \, c(t-1) + (1 - \alpha) \, y(t-1)")
            st.latex(r"h(t) = \tanh\!\left(W_{xh} \, x(t) + W_{ch} \, c(t) + b_h\right)")
            st.latex(r"y(t) = \sigma\!\left(W_{hy} \, h(t) + b_y\right)")
        with f_col2:
            st.markdown("**2. Elman Simple Recurrent Network (Hidden-to-Context Feedback):**")
            st.latex(r"c_{\text{elman}}(t) = \alpha \, c_{\text{elman}}(t-1) + (1 - \alpha) \, h(t-1)")
            st.latex(r"h(t) = \tanh\!\left(W_{xh} \, x(t) + W_{ch} \, c_{\text{elman}}(t) + b_h\right)")
            st.latex(r"y(t) = \sigma\!\left(W_{hy} \, h(t) + b_y\right)")

    # ==========================================================================
    # BAGIAN A: SIMULATOR DINAMIKA MEMORI & INSPEKTOR SINYAL PER LANGKAH WAKTU
    # ==========================================================================
    st.markdown("### 🎛️ Bagian 1: Simulator Dinamika Memori & Inspektor Sinyal JRN")
    st.caption(
        "Ubah jenis sinyal, retensi memori (α), dan bobot umpan balik (W_ch), lalu geser slider t untuk melihat aliran angka di tiap layer pada diagram."
    )

    c_p1, c_p2, c_p3, c_p4 = st.columns([1.4, 1, 1, 1])
    with c_p1:
        signal_type = st.selectbox(
            "Skenario Sinyal Input x(t):",
            [
                "Step Pulse (Denyut Tunggal t=3..6)",
                "Square Wave (Gelombang Kotak Periodik)",
                "Noisy Burst (Sinyal Berderau Acak)",
                "Staircase Regime (Transisi Bertingkat)",
                "Sinusoidal Wave (Gelombang Harmonik)",
            ],
        )
    with c_p2:
        alpha = st.slider(
            "Retensi Memori (α):",
            min_value=0.0,
            max_value=0.95,
            value=0.65,
            step=0.05,
            help="Semakin mendekati 1.0, semakin lama Context Unit menyimpan jejak output masa lalu.",
        )
    with c_p3:
        w_ch = st.slider(
            "Bobot Feedback (W_ch):",
            min_value=-2.0,
            max_value=3.0,
            value=1.6,
            step=0.2,
            help="Positif memperkuat memori (self-sustaining), negatif menciptakan inhibisi/osilasi.",
        )
    with c_p4:
        w_xh = st.slider(
            "Bobot Input (W_xh):",
            min_value=0.4,
            max_value=2.6,
            value=1.3,
            step=0.1,
            help="Kepekaan Hidden Layer terhadap sinyal eksternal x(t).",
        )

    T = 25
    time_steps = np.arange(T)
    x = np.zeros(T)

    if "Step Pulse" in signal_type:
        x[3:7] = 1.0
    elif "Square Wave" in signal_type:
        for t_idx in range(T):
            if (t_idx // 4) % 2 == 1:
                x[t_idx] = 1.0
    elif "Noisy Burst" in signal_type:
        rng_noise = np.random.default_rng(42)
        base_sig = np.where((time_steps >= 3) & (time_steps <= 12), 1.0, 0.0)
        x = np.clip(base_sig + rng_noise.normal(0, 0.28, size=T), 0.0, 1.2)
    elif "Staircase" in signal_type:
        x[2:8] = 0.4
        x[8:14] = 1.0
        x[14:19] = 0.6
    else:
        x = 0.5 + 0.5 * np.sin(2 * np.pi * time_steps / 8.0)

    W_hy = 1.5
    b_h = -0.35

    c_jordan = np.zeros(T)
    h_jordan = np.zeros(T)
    y_jordan = np.zeros(T)

    c_elman = np.zeros(T)
    h_elman = np.zeros(T)
    y_elman = np.zeros(T)

    y_ff = np.zeros(T)

    for t_idx in range(T):
        if t_idx == 0:
            c_jordan[t_idx] = 0.0
            c_elman[t_idx] = 0.0
        else:
            c_jordan[t_idx] = alpha * c_jordan[t_idx - 1] + (1.0 - alpha) * y_jordan[t_idx - 1]
            c_elman[t_idx] = alpha * c_elman[t_idx - 1] + (1.0 - alpha) * (0.5 * (h_elman[t_idx - 1] + 1.0))

        h_jordan[t_idx] = math.tanh(w_xh * x[t_idx] + w_ch * c_jordan[t_idx] + b_h)
        y_jordan[t_idx] = 1.0 / (1.0 + math.exp(-W_hy * h_jordan[t_idx]))

        h_elman[t_idx] = math.tanh(w_xh * x[t_idx] + w_ch * c_elman[t_idx] + b_h)
        y_elman[t_idx] = 1.0 / (1.0 + math.exp(-W_hy * h_elman[t_idx]))

        h_f = math.tanh(w_xh * x[t_idx] + b_h)
        y_ff[t_idx] = 1.0 / (1.0 + math.exp(-W_hy * h_f))

    insp_col1, insp_col2 = st.columns([2.2, 1.2])
    with insp_col1:
        t_inspect = st.slider(
            "🔎 Inspektor Langkah Waktu (t) pada Diagram Jaringan:",
            min_value=0,
            max_value=T - 1,
            value=6,
            step=1,
        )
    with insp_col2:
        arch_view = st.radio(
            "Tampilan Feedback Loop:",
            ["Jordan (Output → Context)", "Elman (Hidden → Context)"],
            horizontal=True,
        )

    is_jordan_view = "Jordan" in arch_view
    cur_x = x[t_inspect]
    cur_c = c_jordan[t_inspect] if is_jordan_view else c_elman[t_inspect]
    cur_h = h_jordan[t_inspect] if is_jordan_view else h_elman[t_inspect]
    cur_y = y_jordan[t_inspect] if is_jordan_view else y_elman[t_inspect]
    prev_src = (
        (y_jordan[t_inspect - 1] if t_inspect > 0 else 0.0)
        if is_jordan_view
        else (0.5 * (h_elman[t_inspect - 1] + 1.0) if t_inspect > 0 else 0.0)
    )

    loop_label = "Jordan Feedback Loop: y(t-1) → c(t)" if is_jordan_view else "Elman Feedback Loop: h(t-1) → c(t)"
    # Koordinat panah umpan balik yang presisi (tidak menabrak isi kotak Context Unit)
    if is_jordan_view:
        loop_path = "M 597 155 L 597 248 L 522 248"
        loop_text_x, loop_text_y = "606", "205"
        loop_anchor = "start"
    else:
        loop_path = "M 385 155 L 385 184 L 427 184 L 427 205"
        loop_text_x, loop_text_y = "436", "192"
        loop_anchor = "start"

    st.markdown(f"""
    <div class='diagram-box'>
        <div style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#ffd740;margin-bottom:6px;letter-spacing:0.8px;">
            ✦ TELEMETRI LANGSUNG PADA LANGKAH WAKTU t = {t_inspect} ({loop_label}) ✦
        </div>
        <svg viewBox="0 0 760 325" width="100%" style="max-height:295px;" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrGold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#ffd740"/>
                </marker>
                <marker id="arrCyan" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#80d8ff"/>
                </marker>
                <marker id="arrPurple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#ea80fc"/>
                </marker>
            </defs>

            <!-- INPUT LAYER -->
            <rect x="35" y="80" width="145" height="75" rx="12" fill="#12152e" stroke="#80d8ff" stroke-width="2.2"/>
            <text x="107" y="106" fill="#80d8ff" font-family="Poppins, sans-serif" font-weight="700" font-size="13" text-anchor="middle">Input Layer x(t)</text>
            <text x="107" y="128" fill="#ffffff" font-family="JetBrains Mono, monospace" font-weight="700" font-size="15" text-anchor="middle">{cur_x:.3f}</text>
            <text x="107" y="145" fill="#90a4ae" font-family="Poppins, sans-serif" font-size="10" text-anchor="middle">Sinyal Eksternal</text>

            <!-- HIDDEN LAYER -->
            <rect x="265" y="80" width="175" height="75" rx="12" fill="#12152e" stroke="#ffd740" stroke-width="2.5"/>
            <text x="352" y="106" fill="#ffd740" font-family="Poppins, sans-serif" font-weight="700" font-size="13" text-anchor="middle">Hidden Layer h(t)</text>
            <text x="352" y="128" fill="#ffffff" font-family="JetBrains Mono, monospace" font-weight="700" font-size="15" text-anchor="middle">{cur_h:+.3f}</text>
            <text x="352" y="145" fill="#cfd8dc" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">tanh(W_xh·x + W_ch·c + b)</text>

            <!-- OUTPUT LAYER -->
            <rect x="520" y="80" width="155" height="75" rx="12" fill="#12152e" stroke="#00e676" stroke-width="2.2"/>
            <text x="597" y="106" fill="#00e676" font-family="Poppins, sans-serif" font-weight="700" font-size="13" text-anchor="middle">Output Layer y(t)</text>
            <text x="597" y="128" fill="#ffffff" font-family="JetBrains Mono, monospace" font-weight="700" font-size="15" text-anchor="middle">{cur_y:.3f}</text>
            <text x="597" y="145" fill="#90a4ae" font-family="Poppins, sans-serif" font-size="10" text-anchor="middle">Prediksi Saat Ini</text>

            <!-- STATE / CONTEXT LAYER -->
            <rect x="340" y="212" width="175" height="74" rx="12" fill="#1b122c" stroke="#ea80fc" stroke-width="2.3" stroke-dasharray="5,3"/>
            <text x="427" y="236" fill="#ea80fc" font-family="Poppins, sans-serif" font-weight="700" font-size="12.5" text-anchor="middle">Context / State Unit c(t)</text>
            <text x="427" y="258" fill="#ffffff" font-family="JetBrains Mono, monospace" font-weight="700" font-size="15" text-anchor="middle">{cur_c:.3f}</text>
            <text x="427" y="275" fill="#ce93d8" font-family="JetBrains Mono, monospace" font-size="10" text-anchor="middle">α={alpha:.2f} | src(t-1)={prev_src:.3f}</text>

            <!-- FORWARD ARROWS -->
            <line x1="180" y1="118" x2="258" y2="118" stroke="#80d8ff" stroke-width="2.5" marker-end="url(#arrCyan)"/>
            <text x="219" y="109" fill="#80d8ff" font-family="JetBrains Mono, monospace" font-size="10.5" text-anchor="middle">W_xh={w_xh:.1f}</text>

            <line x1="440" y1="118" x2="513" y2="118" stroke="#ffd740" stroke-width="2.5" marker-end="url(#arrGold)"/>
            <text x="476" y="109" fill="#ffd740" font-family="JetBrains Mono, monospace" font-size="10.5" text-anchor="middle">W_hy={W_hy:.1f}</text>

            <!-- RECURRENT FEEDBACK ARROW -->
            <path d="{loop_path}" fill="none" stroke="#ea80fc" stroke-width="2.6" marker-end="url(#arrPurple)"/>
            <text x="{loop_text_x}" y="{loop_text_y}" fill="#ea80fc" font-family="Poppins, sans-serif" font-weight="700" font-size="10.5" text-anchor="{loop_anchor}">Umpan Balik ↺</text>

            <!-- CONTEXT TO HIDDEN ARROW -->
            <path d="M 340 248 L 305 248 L 305 162" fill="none" stroke="#ea80fc" stroke-width="2.5" marker-end="url(#arrPurple)"/>
            <text x="262" y="232" fill="#ea80fc" font-family="JetBrains Mono, monospace" font-size="10.5" text-anchor="middle">W_ch={w_ch:+.1f}</text>

            <!-- SELF DECAY LOOP -->
            <path d="M 455 286 C 468 312, 390 312, 402 288" fill="none" stroke="#ffd740" stroke-width="1.8" marker-end="url(#arrGold)"/>
            <text x="428" y="316" fill="#ffd740" font-family="JetBrains Mono, monospace" font-size="9.5" text-anchor="middle">Retensi α={alpha:.2f}</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)

    delta_mem = y_jordan[t_inspect] - y_ff[t_inspect]
    st.markdown(f"""
    <div class='node-stat-grid'>
        <div class='node-stat-box'>
            <div class='node-stat-lbl'>Langkah Waktu</div>
            <div class='node-stat-val' style='color:#ffffff;'>t = {t_inspect}</div>
        </div>
        <div class='node-stat-box'>
            <div class='node-stat-lbl'>Input x(t)</div>
            <div class='node-stat-val' style='color:#80d8ff;'>{x[t_inspect]:.3f}</div>
        </div>
        <div class='node-stat-box'>
            <div class='node-stat-lbl'>Jordan State c(t)</div>
            <div class='node-stat-val' style='color:#ea80fc;'>{c_jordan[t_inspect]:.3f}</div>
        </div>
        <div class='node-stat-box'>
            <div class='node-stat-lbl'>Jordan Output y(t)</div>
            <div class='node-stat-val' style='color:#ffd740;'>{y_jordan[t_inspect]:.3f}</div>
        </div>
        <div class='node-stat-box'>
            <div class='node-stat-lbl'>Efek Memori vs FF</div>
            <div class='node-stat-val' style='color:{"#00e676" if delta_mem >= 0 else "#ff5252"};'>{delta_mem:+.3f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    df_sim = pd.DataFrame({
        "Waktu (t)": time_steps,
        "1. Input Sinyal x(t)": np.round(x, 3),
        "2. Context Memory c(t)": np.round(c_jordan, 3),
        "3. Jordan Output y(t)": np.round(y_jordan, 3),
        "4. Elman Output y_elman(t)": np.round(y_elman, 3),
        "5. Tanpa Memori (Feedforward)": np.round(y_ff, 3),
    }).set_index("Waktu (t)")

    st.line_chart(
        df_sim,
        color=["#80d8ff", "#ea80fc", "#ffd740", "#00e676", "#78909c"],
    )

    half_life = (-1.0 / math.log(alpha)) if 0.01 < alpha < 0.999 else (0.0 if alpha <= 0.01 else 99.0)
    max_hysteresis = float(np.max(np.abs(y_jordan - y_ff)))

    st.markdown(f"""
    <div class='step-box'>
        <div class='step-header'>🔍 Analisis Kuantitatif Dinamika Jordan Network:</div>
        <div class='card-text'>
            &bull; <b>Efek Ingatan (Selisih Puncak = {max_hysteresis:.3f}):</b> Bandingkan kurva kuning (Jordan) dengan kurva abu-abu (tanpa memori). Saat input turun ke 0, feedforward langsung jatuh, sedangkan Jordan Network turun perlahan karena <i>Context Unit</i> masih menyimpan jejak output sebelumnya.<br>
            &bull; <b>Retensi &alpha; = {alpha:.2f} (Bertahan ~{half_life:.1f} langkah):</b> Makin besar &alpha;, makin lama jaringan "mengingat". Karena umpan baliknya berasal dari output y(t-1) yang berada di rentang [0, 1], lintasannya lebih stabil dibanding umpan balik hidden state.
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 Buka Tabel Data Telemetri Lengkap per Langkah Waktu (t = 0..24)"):
        st.dataframe(df_sim, use_container_width=True)

    st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)

    # ==========================================================================
    # BAGIAN B: LABORATORIUM PELATIHAN SEKUENS ASLI MICHAEL I. JORDAN (1986)
    # ==========================================================================
    st.markdown("### 🧪 Bagian 2: Laboratorium Pelatihan Sekuens (Eksperimen *Serial Order* 1986)")
    st.caption(
        "Di makalah aslinya, Jordan menunjukkan bahwa jaringan bisa menghasilkan urutan nilai walau input Plan-nya konstan, "
        "asalkan state c(t) terus diperbarui dari umpan balik output. Coba latih sendiri dan bandingkan dengan feedforward."
    )

    tr_c1, tr_c2, tr_c3 = st.columns([1.5, 1, 1])
    with tr_c1:
        seq_preset = st.selectbox(
            "Pilih Pola Urutan Target y*(t):",
            [
                "Gelombang Orbit Jordan [0.15, 0.35, 0.75, 0.90, 0.65, 0.25, 0.15, 0.45]",
                "Detak Pulsar Astral [0.15, 0.85, 0.85, 0.20, 0.80, 0.15, 0.50, 0.85]",
                "Tangga Konvergensi [0.15, 0.28, 0.42, 0.56, 0.70, 0.82, 0.90, 0.30]",
                "Osilasi Harmonik [0.20, 0.80, 0.25, 0.75, 0.30, 0.70, 0.35, 0.65]",
            ],
        )
    with tr_c2:
        n_epochs = st.slider("Jumlah Epoch Latihan:", min_value=80, max_value=500, value=260, step=20)
    with tr_c3:
        lr = st.slider("Learning Rate (η):", min_value=0.05, max_value=0.60, value=0.28, step=0.02)

    if "Gelombang Orbit" in seq_preset:
        target_seq = np.array([0.15, 0.35, 0.75, 0.90, 0.65, 0.25, 0.15, 0.45])
    elif "Detak Pulsar" in seq_preset:
        target_seq = np.array([0.15, 0.85, 0.85, 0.20, 0.80, 0.15, 0.50, 0.85])
    elif "Tangga Konvergensi" in seq_preset:
        target_seq = np.array([0.15, 0.28, 0.42, 0.56, 0.70, 0.82, 0.90, 0.30])
    else:
        target_seq = np.array([0.20, 0.80, 0.25, 0.75, 0.30, 0.70, 0.35, 0.65])

    @st.cache_data(ttl=3600, max_entries=32, show_spinner=False)
    def train_jordan_vs_ff(target_tuple, epochs: int, learning_rate: float, mem_alpha: float):
        y_true = np.array(target_tuple, dtype=float)
        seq_len = len(y_true)
        rng = np.random.default_rng(18881986)

        # Jaga agar mem_alpha pada eksperimen berada di rentang efektif (0.25..0.75)
        eff_alpha = min(0.75, max(0.25, mem_alpha))
        n_hid = 10
        # Fitur input ke Hidden: [Plan=1.0, c1(t), c2(t), sin_trace(t), cos_trace(t)]
        # Di mana c1 & c2 berevolusi dari recurrent output y(t-1)
        W_in_j = rng.normal(0, 0.55, size=(5, n_hid))
        b_h_j = np.zeros(n_hid)
        W_out_j = rng.normal(0, 0.45, size=(n_hid, 1))
        b_o_j = 0.0

        loss_hist_j = []
        loss_hist_ff = []

        mean_target = float(np.mean(y_true))
        ff_mse = float(np.mean((y_true - mean_target) ** 2))

        for ep in range(epochs):
            c1 = 0.5
            c2 = 0.5
            ep_loss = 0.0
            # Scheduled sampling: transisi mulus dari teacher-guided ke murni output sendiri (closed-loop)
            tf_ratio = max(0.0, 1.0 - (ep / max(1, epochs * 0.65)))
            for t_i in range(seq_len):
                phase_s = math.sin(2.0 * math.pi * t_i / seq_len)
                phase_c = math.cos(2.0 * math.pi * t_i / seq_len)
                inp = np.array([1.0, c1, c2, 0.35 * phase_s, 0.35 * phase_c])

                z_h = inp @ W_in_j + b_h_j
                h_act = np.tanh(z_h)
                z_o = float((h_act @ W_out_j)[0] + b_o_j)
                y_hat = 1.0 / (1.0 + math.exp(-z_o))

                err = y_hat - y_true[t_i]
                ep_loss += err * err

                d_zo = 2.0 * err * y_hat * (1.0 - y_hat)
                d_W_out = np.outer(h_act, [d_zo])
                d_b_o = d_zo

                d_h = (W_out_j[:, 0] * d_zo) * (1.0 - h_act * h_act)
                d_W_in = np.outer(inp, d_h)
                d_b_h = d_h

                W_out_j -= learning_rate * d_W_out
                b_o_j -= learning_rate * d_b_o
                W_in_j -= learning_rate * d_W_in
                b_h_j -= learning_rate * d_b_h

                fb_signal = tf_ratio * y_true[t_i] + (1.0 - tf_ratio) * y_hat
                prev_c1 = c1
                c1 = eff_alpha * c1 + (1.0 - eff_alpha) * fb_signal
                c2 = 0.7 * c2 + 0.3 * prev_c1

            loss_hist_j.append(ep_loss / seq_len)
            loss_hist_ff.append(ff_mse)

        # Evaluasi akhir murni Closed-Loop (menggunakan prediksi y_hat sendiri)
        preds_j = []
        c1 = 0.5
        c2 = 0.5
        for t_i in range(seq_len):
            phase_s = math.sin(2.0 * math.pi * t_i / seq_len)
            phase_c = math.cos(2.0 * math.pi * t_i / seq_len)
            inp = np.array([1.0, c1, c2, 0.35 * phase_s, 0.35 * phase_c])
            h_act = np.tanh(inp @ W_in_j + b_h_j)
            z_o = float((h_act @ W_out_j)[0] + b_o_j)
            y_hat = 1.0 / (1.0 + math.exp(-z_o))
            preds_j.append(y_hat)
            prev_c1 = c1
            c1 = eff_alpha * c1 + (1.0 - eff_alpha) * y_hat
            c2 = 0.7 * c2 + 0.3 * prev_c1

        preds_ff = [mean_target] * seq_len
        return np.array(preds_j), np.array(preds_ff), np.array(loss_hist_j), np.array(loss_hist_ff)

    preds_jrn, preds_ff_const, loss_jrn, loss_ff = train_jordan_vs_ff(
        tuple(target_seq), n_epochs, lr, alpha
    )

    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.markdown("**📈 Hasil Rekonstruksi Urutan Sekuensial:**")
        df_seq = pd.DataFrame({
            "Langkah Urutan": np.arange(1, len(target_seq) + 1),
            "Target Asli y*(t)": np.round(target_seq, 3),
            "Prediksi Jordan Network": np.round(preds_jrn, 3),
            "Feedforward (Tanpa Memori)": np.round(preds_ff_const, 3),
        }).set_index("Langkah Urutan")
        st.line_chart(df_seq, color=["#80d8ff", "#ffd740", "#78909c"])

    with res_col2:
        st.markdown("**📉 Penurunan Error (MSE Loss) Selama Pelatihan:**")
        df_loss = pd.DataFrame({
            "Epoch": np.arange(1, n_epochs + 1),
            "MSE Jordan Network": np.round(loss_jrn, 5),
            "MSE Feedforward (Stagnan)": np.round(loss_ff, 5),
        }).set_index("Epoch")
        st.line_chart(df_loss, color=["#00e676", "#ff5252"])

    final_mse_jrn = float(loss_jrn[-1])
    final_mse_ff = float(loss_ff[-1])
    accuracy_gain = max(0.0, (1.0 - final_mse_jrn / max(final_mse_ff, 1e-6)) * 100.0)

    st.markdown(f"""
    <div class='step-box' style='border-left-color:#00e676;'>
        <div class='step-header' style='color:#00e676;'>🏆 Kesimpulan Eksperimen Serial Order (Reduksi Error: {accuracy_gain:.1f}%):</div>
        <div class='card-text'>
            Tanpa umpan balik ke <i>Context Unit</i>, jaringan <i>feedforward</i> hanya bisa menebak nilai rata-rata konstan (MSE tertahan di <b>{final_mse_ff:.4f}</b>).<br>
            Sebaliknya, <b>Jordan Network</b> memanfaatkan umpan balik state rekuren sehingga mampu merekonstruksi pola urutan dengan MSE turun hingga <b>{final_mse_jrn:.5f}</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
#         TAB 2: ELIMINASI GAUSS-JORDAN (WILHELM JORDAN, 1888)
# ==============================================================================
elif active_codex == "Eliminasi Gauss-Jordan":
    st.markdown("""
    <div class='concept-card'>
        <div class='card-title'>📐 Wilhelm Jordan (1842 - 1899) &amp; Eliminasi Gauss-Jordan</div>
        <div class='card-text'>
            <b>Wilhelm Jordan</b>, ahli geodesi asal Jerman, menyempurnakan eliminasi Gauss lewat bukunya <i>Handbuch der Vermessungskunde</i> (1888) untuk keperluan pemetaan dan jaringan triangulasi.<br><br>
            Eliminasi Gauss biasa hanya mengenolkan elemen <b>di bawah</b> diagonal utama, sehingga masih membutuhkan substitusi mundur. Metode <b>Gauss-Jordan</b> mengenolkan elemen <b>di atas dan di bawah</b> pivot sekaligus sampai terbentuk matriks identitas (<b>RREF</b>), sehingga solusi langsung terbaca.
        </div>
    </div>
    """, unsafe_allow_html=True)

    gj_mode = st.radio(
        "Pilih Laboratorium Komputasi Gauss-Jordan:",
        [
            "🧮 1. Solver Sistem Persamaan Linier [A | B] → [I | X]",
            "🔄 2. Kalkulator Invers Matriks Eksak [A | I] → [I | A⁻¹]",
        ],
        horizontal=True,
    )

    def fmt_frac(f: Fraction) -> str:
        if f.denominator == 1:
            return str(f.numerator)
        if f.numerator < 0:
            return f"-\\frac{{{abs(f.numerator)}}}{{{f.denominator}}}"
        return f"\\frac{{{f.numerator}}}{{{f.denominator}}}"

    def fmt_frac_plain(f: Fraction) -> str:
        if f.denominator == 1:
            return str(f.numerator)
        return f"{f.numerator}/{f.denominator}"

    def fmt_sub_op(row_target: int, factor: Fraction, row_pivot: int) -> str:
        """Format operasi baris R_i <- R_i - factor * R_r dengan tanda + / - yang bersih."""
        if factor > 0:
            fac_str = "" if factor == 1 else f"{fmt_frac(factor)} \\cdot "
            return f"R_{{{row_target}}} \\leftarrow R_{{{row_target}}} - {fac_str}R_{{{row_pivot}}}"
        else:
            abs_fac = abs(factor)
            fac_str = "" if abs_fac == 1 else f"{fmt_frac(abs_fac)} \\cdot "
            return f"R_{{{row_target}}} \\leftarrow R_{{{row_target}}} + {fac_str}R_{{{row_pivot}}}"

    if "1. Solver" in gj_mode:
        col_preset, _ = st.columns([2.2, 1])
        with col_preset:
            preset = st.selectbox(
                "Pilih Skenario Sistem Persamaan Linier (SPL):",
                [
                    "Kasus Standar (Solusi Bulat Unik: x₁=2, x₂=3, x₃=-1)",
                    "Alokasi Resource Data Pipeline (x₁=1, x₂=2, x₃=4)",
                    "Traffic Flow Jaringan Server (x₁=3, x₂=1, x₃=2)",
                    "SPL 2x2 Sederhana (x₁=4, x₂=1)",
                    "Input Matriks Kustom Sendiri",
                ],
            )

        if "Kasus Standar" in preset:
            default_matrix = [[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]]
            var_names = ["x₁", "x₂", "x₃"]
        elif "Alokasi Resource" in preset:
            default_matrix = [[1, 2, 1, 9], [2, 1, -1, 0], [3, 2, 1, 11]]
            var_names = ["x₁", "x₂", "x₃"]
        elif "Traffic Flow" in preset:
            default_matrix = [[1, 1, 1, 6], [0, 2, 5, 12], [2, 5, -1, 9]]
            var_names = ["x₁", "x₂", "x₃"]
        elif "SPL 2x2" in preset:
            default_matrix = [[2, 3, 11], [1, -2, 2]]
            var_names = ["x₁", "x₂"]
        else:
            size_choice = st.radio("Ukuran Matriks:", ["3 Variabel (3x3)", "2 Variabel (2x2)"], horizontal=True)
            if "3" in size_choice:
                default_matrix = [[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 2]]
                var_names = ["x₁", "x₂", "x₃"]
            else:
                default_matrix = [[2, 1, 5], [1, -1, 1]]
                var_names = ["x₁", "x₂"]

        n_rows = len(default_matrix)
        n_cols = len(default_matrix[0])

        st.markdown("**Input Matriks Augmented $[A \\mid B]$:**")
        input_cols = st.columns(n_cols)
        user_mat = []

        for r in range(n_rows):
            row_vals = []
            for c in range(n_cols):
                with input_cols[c]:
                    header = f"Koef {var_names[c]}" if c < n_cols - 1 else "Konstanta B"
                    key = f"mat_{preset}_{r}_{c}"
                    val = st.number_input(
                        f"R{r+1} ({header})",
                        value=float(default_matrix[r][c]),
                        step=1.0,
                        key=key,
                    )
                    row_vals.append(Fraction(str(val)).limit_denominator(1000))
            user_mat.append(row_vals)

        def mat_to_latex(m):
            rows_str = []
            for row in m:
                row_items = [fmt_frac(val) for val in row]
                rows_str.append(" & ".join(row_items))
            body = " \\\\[4pt]\n".join(rows_str)
            cols_align = "c" * (len(m[0]) - 1) + "|c"
            return f"\\left[\\begin{{array}}{{{cols_align}}}\n{body}\n\\end{{array}}\\right]"

        if st.button("🚀 Jalankan Eliminasi Gauss-Jordan (Eksak)", type="primary"):
            m = [row[:] for row in user_mat]
            rows = len(m)
            cols = len(m[0])
            steps = []

            r = 0
            for c in range(cols - 1):
                if r >= rows:
                    break
                pivot_r = r
                while pivot_r < rows and m[pivot_r][c] == 0:
                    pivot_r += 1
                if pivot_r == rows:
                    continue
                if pivot_r != r:
                    m[r], m[pivot_r] = m[pivot_r], m[r]
                    steps.append({
                        "title": f"Tukar Baris R{r+1} dengan R{pivot_r+1}",
                        "latex_op": f"R_{{{r+1}}} \\longleftrightarrow R_{{{pivot_r+1}}}",
                        "explanation": f"Menukar baris {r+1} dan baris {pivot_r+1} agar elemen pivot tidak bernilai nol.",
                        "matrix": [row[:] for row in m],
                    })
                pivot_val = m[r][c]
                if pivot_val != 1:
                    for j in range(cols):
                        m[r][j] /= pivot_val
                    inv_piv = Fraction(1, 1) / pivot_val
                    steps.append({
                        "title": f"Normalisasi Baris Pivot R{r+1}",
                        "latex_op": f"R_{{{r+1}}} \\leftarrow {fmt_frac(inv_piv)} \\cdot R_{{{r+1}}}",
                        "explanation": f"Membagi baris {r+1} dengan {fmt_frac_plain(pivot_val)} supaya pivot utama bernilai 1.",
                        "matrix": [row[:] for row in m],
                    })
                for i in range(rows):
                    if i != r and m[i][c] != 0:
                        factor = m[i][c]
                        for j in range(cols):
                            m[i][j] -= factor * m[r][j]
                        steps.append({
                            "title": f"Eliminasi Kolom {c+1} pada Baris R{i+1}",
                            "latex_op": fmt_sub_op(i + 1, factor, r + 1),
                            "explanation": f"Mengenolkan elemen kolom ke-{c+1} pada baris {i+1} (ciri khas Wilhelm Jordan).",
                            "matrix": [row[:] for row in m],
                        })
                r += 1

            st.markdown("---")
            c_m1, c_m2 = st.columns(2)
            with c_m1:
                st.markdown("#### 📋 Matriks Awal $[A \\mid B]$:")
                st.latex(mat_to_latex(user_mat))
            with c_m2:
                st.markdown("#### 🎯 Hasil Akhir RREF $[I \\mid X]$:")
                st.latex(mat_to_latex(m))

            st.markdown(f"#### ⚙️ Rincian {len(steps)} Langkah Operasi Baris Elementer (OBE):")
            for idx, s in enumerate(steps, 1):
                with st.expander(f"Langkah {idx}: {s['title']}", expanded=(idx == 1 or idx == len(steps))):
                    st.write(s["explanation"])
                    st.latex(s["latex_op"])
                    st.latex(mat_to_latex(s["matrix"]))

            sol = []
            is_consistent = True
            for i in range(rows):
                left_all_zero = all(m[i][j] == 0 for j in range(cols - 1))
                right_val = m[i][-1]
                if left_all_zero and right_val != 0:
                    is_consistent = False
                    break
                elif not left_all_zero:
                    for j in range(cols - 1):
                        if m[i][j] == 1:
                            sol.append((var_names[j], right_val))
                            break

            if not is_consistent:
                st.error("❌ **Sistem Tidak Konsisten**: Tidak memiliki solusi karena terdapat baris `[0 ... 0 | b]` dengan `b ≠ 0`.")
            elif len(sol) < len(var_names):
                st.warning("⚠️ **Solusi Tak Hingga Banyak**: Terdapat variabel bebas (*free variables*).")
            else:
                st.success("✅ **Solusi Eksak Berhasil Ditemukan!**")
                sol_cols = st.columns(len(sol))
                for i, (var, val) in enumerate(sol):
                    with sol_cols[i]:
                        st.metric(label=f"Variabel {var}", value=fmt_frac_plain(val), delta=f"Desimal: {float(val):.4f}")

    else:
        st.caption(
            "Metode Eliminasi Gauss-Jordan menyandingkan matriks persegi $A$ dengan matriks identitas $I$ membentuk $[A \\mid I]$, "
            "lalu mereduksi sisi kiri menjadi $I$ sehingga sisi kanan otomatis menjadi matriks invers $A^{-1}$ secara eksak!"
        )
        inv_preset = st.selectbox(
            "Pilih Matriks Persegi A:",
            [
                "Matriks 3x3 Unimodular (Invers Bilangan Bulat)",
                "Matriks 3x3 Transformasi Ruang Data",
                "Matriks 2x2 Rotasi & Skala",
            ],
        )
        if "Unimodular" in inv_preset:
            def_a = [[1, 2, 1], [2, 5, 2], [1, 3, 2]]
        elif "Transformasi" in inv_preset:
            def_a = [[2, 1, 1], [1, 3, 2], [1, 0, 0]]
        else:
            def_a = [[4, 7], [2, 6]]

        n_dim = len(def_a)
        a_cols = st.columns(n_dim)
        mat_a = []
        for r in range(n_dim):
            row_a = []
            for c in range(n_dim):
                with a_cols[c]:
                    v = st.number_input(
                        f"A[{r+1},{c+1}]",
                        value=float(def_a[r][c]),
                        step=1.0,
                        key=f"inv_{inv_preset}_{r}_{c}",
                    )
                    row_a.append(Fraction(str(v)).limit_denominator(1000))
            mat_a.append(row_a)

        def aug_inv_latex(aug_m, n):
            rows_s = []
            for row in aug_m:
                items = [fmt_frac(x) for x in row]
                rows_s.append(" & ".join(items))
            align = "c" * n + "|" + "c" * n
            body = " \\\\[4pt]\n".join(rows_s)
            return f"\\left[\\begin{{array}}{{{align}}}\n{body}\n\\end{{array}}\\right]"

        if st.button("🔄 Hitung Invers Matriks A⁻¹ dengan Gauss-Jordan", type="primary"):
            aug = [
                mat_a[i][:] + [Fraction(1 if i == j else 0) for j in range(n_dim)]
                for i in range(n_dim)
            ]
            aug_start = [row[:] for row in aug]
            inv_steps = []
            invertible = True

            for c in range(n_dim):
                piv = c
                while piv < n_dim and aug[piv][c] == 0:
                    piv += 1
                if piv == n_dim:
                    invertible = False
                    break
                if piv != c:
                    aug[c], aug[piv] = aug[piv], aug[c]
                    inv_steps.append((f"R_{{{c+1}}} \\longleftrightarrow R_{{{piv+1}}}", [r[:] for r in aug]))
                pval = aug[c][c]
                if pval != 1:
                    for j in range(2 * n_dim):
                        aug[c][j] /= pval
                    inv_piv = Fraction(1, 1) / pval
                    inv_steps.append((f"R_{{{c+1}}} \\leftarrow {fmt_frac(inv_piv)} \\cdot R_{{{c+1}}}", [r[:] for r in aug]))
                for i in range(n_dim):
                    if i != c and aug[i][c] != 0:
                        fac = aug[i][c]
                        for j in range(2 * n_dim):
                            aug[i][j] -= fac * aug[c][j]
                        inv_steps.append((fmt_sub_op(i + 1, fac, c + 1), [r[:] for r in aug]))

            if not invertible:
                st.error("❌ **Matriks Singular (Determinan = 0)**: Matriks tidak memiliki invers karena tidak dapat direduksi menjadi identitas.")
            else:
                st.success(f"✅ **Matriks Invers $A^{{-1}}$ Berhasil Ditemukan dalam {len(inv_steps)} Langkah OBE!**")
                ic1, ic2 = st.columns(2)
                with ic1:
                    st.markdown("**Matriks Awal $[A \\mid I]$:**")
                    st.latex(aug_inv_latex(aug_start, n_dim))
                with ic2:
                    st.markdown("**Hasil Reduksi $[I \\mid A^{-1}]$:**")
                    st.latex(aug_inv_latex(aug, n_dim))

                with st.expander(f"🔎 Lihat Rincian {len(inv_steps)} Langkah Transformasi $[A \\mid I] \\to [I \\mid A^{{-1}}]$"):
                    for idx, (op_tex, snap) in enumerate(inv_steps, 1):
                        st.markdown(f"**Langkah {idx}:**")
                        st.latex(op_tex)
                        st.latex(aug_inv_latex(snap, n_dim))


# ==============================================================================
#         TAB 3: SINTESIS TIGA JORDAN DI LANGIT SAINS DATA
# ==============================================================================
elif active_codex == "Sintesis Tiga Jordan":
    st.markdown("""
    <div class='concept-card'>
        <div class='card-title'>🌟 Mengapa Nama "Jordan" Begitu Istimewa di Sains Data?</div>
        <div class='card-text'>
            Di matematika dan kecerdasan buatan, ada tiga tokoh besar bernama Jordan dari era berbeda. Ketiganya jadi inspirasi <b>Konstelasi Jordan</b>: teliti seperti aljabar, rapi seperti struktur kanonik, dan terus belajar seperti jaringan saraf.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c_j1, c_j2, c_j3 = st.columns(3)

    with c_j1:
        st.markdown("""
        <div class='concept-card' style='border-color:rgba(255,215,64,0.35);height:100%;'>
            <div style='font-size:2.1em;text-align:center;margin-bottom:0.4rem;'>📐</div>
            <div class='card-title' style='justify-content:center;text-align:center;'>Wilhelm Jordan</div>
            <div style='text-align:center;color:#ffd740;font-family:JetBrains Mono,monospace;font-size:0.76em;font-weight:700;margin-bottom:0.75rem;'>
                JERMAN • 1842 - 1899 (GEODESI &amp; MATRIKS)
            </div>
            <div class='card-text'>
                <b>Karya Monumental:</b><br>
                &bull; <b>Eliminasi Gauss-Jordan (1888):</b> Mereduksi matriks hingga bentuk eselon baris tereduksi (RREF).<br>
                &bull; <b>Aplikasi Sains Data:</b> Penyelesaian sistem persamaan linier skala besar, regresi <i>Least Squares</i>, dan inversi matriks eksak.<br>
                &bull; <b>Nilai Konstelasi:</b> Presisi analitis, ketelitian langkah demi langkah, dan ketangguhan fondasi.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_j2:
        st.markdown("""
        <div class='concept-card' style='border-color:rgba(234,128,252,0.35);height:100%;'>
            <div style='font-size:2.1em;text-align:center;margin-bottom:0.4rem;'>🏛️</div>
            <div class='card-title' style='justify-content:center;text-align:center;color:#ea80fc;'>Camille Jordan</div>
            <div style='text-align:center;color:#ea80fc;font-family:JetBrains Mono,monospace;font-size:0.76em;font-weight:700;margin-bottom:0.75rem;'>
                PRANCIS • 1838 - 1922 (ALJABAR &amp; TOPOLOGI)
            </div>
            <div class='card-text'>
                <b>Karya Monumental:</b><br>
                &bull; <b>Jordan Canonical Form (1870) &amp; Teorema Kurva Jordan:</b> Dekomposisi spektral matriks dan dasar topologi modern.<br>
                &bull; <b>Aplikasi Sains Data:</b> Analisis kestabilan sistem dinamis, nilai eigen berulang, dan <i>Jordan Measure</i> pada teori peluang.<br>
                &bull; <b>Nilai Konstelasi:</b> Kemampuan mengurai kerumitan berdimensi tinggi menjadi struktur kanonik yang elegan.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_j3:
        st.markdown("""
        <div class='concept-card' style='border-color:rgba(128,216,255,0.35);height:100%;'>
            <div style='font-size:2.1em;text-align:center;margin-bottom:0.4rem;'>🧠</div>
            <div class='card-title' style='justify-content:center;text-align:center;color:#80d8ff;'>Michael I. Jordan</div>
            <div style='text-align:center;color:#80d8ff;font-family:JetBrains Mono,monospace;font-size:0.76em;font-weight:700;margin-bottom:0.75rem;'>
                AMERIKA SERIKAT • 1956 - SEKARANG (ML &amp; AI)
            </div>
            <div class='card-text'>
                <b>Karya Monumental:</b><br>
                &bull; <b>Jordan Recurrent Network (1986), Latent Dirichlet Allocation (LDA), &amp; Variational Inference:</b> Pelopor <i>Machine Learning</i> modern.<br>
                &bull; <b>Aplikasi Sains Data:</b> Pemodelan runtun waktu, <i>Recurrent Neural Networks</i>, dan jaringan probabilistik.<br>
                &bull; <b>Nilai Konstelasi:</b> Adaptif, terus belajar dari umpan balik masa lalu, dan berorientasi masa depan.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:0.6rem;'></div>", unsafe_allow_html=True)

    st.markdown("### 📊 Peta Perbandingan Paradigma: Aljabar Klasik vs Jaringan Rekuren")
    df_comp = pd.DataFrame({
        "Dimensi Perbandingan": [
            "Tokoh & Tahun",
            "Objek Komputasi Utama",
            "Sifat Sistem",
            "Mekanisme Inti",
            "Peran dalam Sains Data Modern",
        ],
        "Eliminasi Gauss-Jordan": [
            "Wilhelm Jordan (1888)",
            "Matriks Augmented [A | B] & Ruang Vektor",
            "Deterministik, Eksak, Waktu Statis",
            "Operasi Baris Elementer (OBE) menuju RREF Identitas",
            "Fondasi Solver SPL, Inversi Matriks, OLS Regression",
        ],
        "Jordan Recurrent Network (JRN)": [
            "Michael I. Jordan (1986)",
            "Data Sekuensial x(t), Context c(t), Output y(t)",
            "Adaptif, Dinamis, Berbasis Memori Waktu (Temporal)",
            "Umpan Balik Output y(t-1) ke Context Unit c(t)",
            "Fondasi RNN, Sequence Modeling, Kontrol Dinamis & NLP",
        ],
    }).set_index("Dimensi Perbandingan")
    st.table(df_comp)

    st.markdown("""
    <div style='text-align:center;padding:1.4rem 1.6rem;background:rgba(255,215,64,0.05);border-radius:16px;border:1px dashed rgba(255,215,64,0.35);margin-top:1rem;'>
        <div style='color:#ffd740;font-family:"Cinzel","Poppins",serif;font-size:1.25em;font-weight:800;margin-bottom:0.4rem;letter-spacing:1px;'>
            ✦ SATU NAMA, SATU RASI BINTANG, TIGA WARISAN ILMU ✦
        </div>
        <p style='color:#cfd8dc;font-style:italic;max-width:760px;margin:0 auto;font-size:0.94em;line-height:1.6;'>
            Di bawah <b>Konstelasi Jordan</b>, kami menggabungkan ketelitian <b>Wilhelm Jordan</b>, struktur rapi <b>Camille Jordan</b>, dan semangat belajar <b>Michael I. Jordan</b> untuk menjelajahi Sains Data ITERA.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;color:#78909c;font-size:0.82em;padding-bottom:1.6rem;font-family:"JetBrains Mono",monospace;'>
    ✦ KONSTELASI JORDAN • CEO HMSD ADYATAMA ITERA 2026 ✦<br>
    <span style='color:#546e7a;'>"From Linear Foundations to Intelligent Recurrence"</span>
</div>
""", unsafe_allow_html=True)
