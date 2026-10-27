import os
import sys
_APP_DIR = os.path.dirname(os.path.abspath(__file__))
if _APP_DIR not in sys.path:
    sys.path.insert(0, _APP_DIR)
import json
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="Konstelasi Jordan",
    page_icon="💫",
    layout="wide"
)

from loading_screen import show_loading_screen

# ==============================================================================
# KONFIGURASI UTAMA & DAFTAR BINTANG KONSTELASI 10 KELOMPOK
# ==============================================================================

NAMA_MENTOR_UTAMA = "Kak Yollanda Agustina"

DAFTAR_KONSTELASI_KELOMPOK = [
    {
        "kode": "01",
        "nama": "Konstelasi Jordan",
        "gelar": "The Sovereign of Feedback Loops",
        "deskripsi": "Rasi bintang kita sendiri. Namanya dari Wilhelm Jordan dan Michael I. Jordan, dengan Kak Yollanda Agustina sebagai Sang Bintang Jordan.",
        "warna": [255, 215, 64],  # Kuning Emas
    },
    {
        "kode": "02",
        "nama": "Konstelasi Jacobi",
        "gelar": "The Endless Convergence Seeker",
        "deskripsi": "Iterasi terus sampai konvergen, banyak tapi tetap satu tujuan.",
        "warna": [255, 110, 180],  # Pink
    },
    {
        "kode": "03",
        "nama": "Konstelasi Tensor",
        "gelar": "Architect of Multi-Dimensional Arrays",
        "deskripsi": "Datanya berlapis dan dimensinya banyak, tapi semangat timnya tetap satu frekuensi.",
        "warna": [179, 136, 255],  # Ungu
    },
    {
        "kode": "04",
        "nama": "Konstelasi Anova",
        "gelar": "Arbiter of Variance & Hypotheses",
        "deskripsi": "Hobinya membandingkan rata-rata antar kelompok, banyak tapi tetap kompak sebagai tim.",
        "warna": [176, 190, 197],  # Abu
    },
    {
        "kode": "05",
        "nama": "Konstelasi Markov",
        "gelar": "Weaver of Stochastic Transitions",
        "deskripsi": "Masa depan cuma bergantung pada hari ini. Jadi kerjakan revisinya sekarang.",
        "warna": [76, 217, 100],  # Hijau
    },
    {
        "kode": "06",
        "nama": "Konstelasi Pandas",
        "gelar": "Keeper of Tabular DataFrames",
        "deskripsi": "Bukan beruang, tapi jagonya merapikan tabel dan membersihkan data di Python.",
        "warna": [196, 138, 90],  # Coklat
    },
    {
        "kode": "07",
        "nama": "Konstelasi Poisson",
        "gelar": "Chronicler of Discrete Events",
        "deskripsi": "Ahli menghitung peluang kejadian langka dalam rentang waktu tertentu.",
        "warna": [190, 45, 70],  # Maroon
    },
    {
        "kode": "08",
        "nama": "Konstelasi COSVAL",
        "gelar": "Navigator of Vector Similarity",
        "deskripsi": "Mengukur kemiripan arah antar vektor supaya langkah tim selalu searah.",
        "warna": [245, 230, 196],  # Cream
    },
    {
        "kode": "09",
        "nama": "Konstelasi Bayesian",
        "gelar": "Oracle of Posterior Probability",
        "deskripsi": "Selalu memperbarui keyakinan setiap ada bukti dan pengalaman baru.",
        "warna": [64, 196, 255],  # Biru
    },
    {
        "kode": "10",
        "nama": "Konstelasi Greedy",
        "gelar": "Vanguard of Optimal Local Choices",
        "deskripsi": "Selalu ambil pilihan terbaik yang ada di depan mata, kadang berhasil, kadang tidak.",
        "warna": [255, 152, 0],  # Orange
    },
]

# Simpan di session_state agar dapat dibaca juga oleh Halaman Utama
st.session_state["daftar_konstelasi"] = DAFTAR_KONSTELASI_KELOMPOK
st.session_state["nama_mentor_utama"] = NAMA_MENTOR_UTAMA

# ===== CUSTOM LOADING SCREEN =====
show_loading_screen()

# ===== GLOBAL CSS STYLING (STELLAR) =====
st.markdown("""
<style>
/* ===== FORCE GOLD PRIMARY ACCENT ON TABS & RADIO ===== */
:root {
    --primary-color: #ffd740 !important;
}
[data-baseweb="tab-highlight"] {
    background-color: #ffd740 !important;
}
[data-baseweb="tab"][aria-selected="true"],
[data-baseweb="tab"][aria-selected="true"] p {
    color: #ffd740 !important;
}
[data-testid="stRadio"] label [data-baseweb="radio"] > div:first-child {
    border-color: #ffd740 !important;
}
/* ===== SPINNER ===== */
[data-testid="stSpinner"] {
    color: #ffd740 !important;
    font-weight: 600;
}
[data-testid="stSpinner"] svg {
    stroke: #ffd740 !important;
    filter: drop-shadow(0 0 8px rgba(255, 215, 64, 0.65));
}

/* ===== GLOBAL BACKGROUND TEMA STELLAR ===== */
.stApp {
    background: radial-gradient(ellipse at 20% 10%, #13132b 0%, #090a14 55%, #05050a 100%) !important;
    color: #d8e0e8 !important;
    transition: background 0.45s ease !important;
}

/* ===== MODE SIMPLE (MURNI HITAM POLOS) ===== */
body.jordan-mode-simple .stApp,
html.jordan-mode-simple .stApp {
    background: #050508 !important;
}
body.jordan-mode-simple .stApp::before,
html.jordan-mode-simple .stApp::before,
body.jordan-mode-simple [data-testid="stSidebar"]::before,
html.jordan-mode-simple [data-testid="stSidebar"]::before {
    display: none !important;
    opacity: 0 !important;
}
body.jordan-mode-simple [data-testid="stSidebar"],
html.jordan-mode-simple [data-testid="stSidebar"] {
    background: #08080d !important;
}

/* ===== STATIC STARFIELD CSS ===== */
.stApp::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        radial-gradient(ellipse 55% 45% at 82% 12%, rgba(95,55,195,0.20), transparent 70%),
        radial-gradient(ellipse 50% 40% at 12% 78%, rgba(24,155,215,0.14), transparent 70%),
        radial-gradient(ellipse 40% 35% at 60% 95%, rgba(185,65,115,0.12), transparent 70%),
        radial-gradient(circle at 23% 41%, rgba(255,255,255,0.95) 0.9px, transparent 1.6px),
        radial-gradient(circle at 71% 17%, rgba(255,255,255,0.80) 0.7px, transparent 1.4px),
        radial-gradient(circle at 47% 83%, rgba(170,225,255,0.85) 1.0px, transparent 1.8px),
        radial-gradient(circle at 88% 64%, rgba(255,226,140,0.80) 0.8px, transparent 1.5px),
        radial-gradient(circle at 9% 12%, rgba(255,255,255,0.60) 0.5px, transparent 1.1px),
        radial-gradient(circle at 36% 69%, rgba(255,255,255,0.55) 0.5px, transparent 1.1px),
        radial-gradient(circle at 63% 52%, rgba(200,180,255,0.65) 0.6px, transparent 1.2px),
        radial-gradient(circle at 54% 27%, rgba(255,255,255,0.45) 0.5px, transparent 1px),
        radial-gradient(circle at 15% 93%, rgba(255,255,255,0.50) 0.5px, transparent 1px);
    background-size:
        100% 100%, 100% 100%, 100% 100%,
        397px 331px, 523px 449px, 613px 577px, 719px 661px,
        149px 167px, 191px 211px, 263px 241px, 113px 127px, 173px 139px;
    background-repeat: no-repeat, no-repeat, no-repeat, repeat, repeat, repeat, repeat, repeat, repeat, repeat, repeat, repeat;
    pointer-events: none;
    z-index: 0;
    opacity: 0.85;
    transition: opacity 0.4s ease;
}

.stApp::after {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image:
        radial-gradient(circle at 31% 22%, rgba(255,255,255,1) 1px, rgba(255,255,255,0.25) 2.4px, transparent 3.6px),
        radial-gradient(circle at 74% 58%, rgba(170,225,255,1) 1px, rgba(170,225,255,0.22) 2.4px, transparent 3.6px),
        radial-gradient(circle at 52% 88%, rgba(255,226,140,1) 1px, rgba(255,226,140,0.22) 2.4px, transparent 3.6px);
    background-size: 467px 389px, 641px 557px, 809px 733px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.9;
    animation: jordanTwinkle 5.5s ease-in-out infinite alternate;
}
@keyframes jordanTwinkle {
    0%   { opacity: 0.25; }
    50%  { opacity: 0.95; }
    100% { opacity: 0.45; }
}
@media (prefers-reduced-motion: reduce) {
    .stApp::after { animation: none; opacity: 0.7; }
}
body.jordan-mode-simple .stApp::after,
html.jordan-mode-simple .stApp::after {
    display: none !important;
}

/* ===== PASTIKAN SEMUA ELEMEN KONTEN DI ATAS CANVAS ===== */
[data-testid="stAppViewContainer"] > section[data-testid="stMain"],
.main .block-container,
[data-testid="stMainBlockContainer"] {
    position: relative !important;
    z-index: 2 !important;
}

/* ===== SIDEBAR BACKGROUND ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #080914 0%, #0c0d1c 45%, #101126 100%) !important;
    border-right: 1px solid rgba(255,215,64,0.16) !important;
    z-index: 10 !important;
}
[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        radial-gradient(circle, rgba(255,255,255,0.48) 1px, transparent 1px),
        radial-gradient(circle, rgba(255,215,64,0.35) 1px, transparent 1px);
    background-size: 100px 100px, 170px 170px;
    background-position: 12px 24px, 55px 75px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.28;
}

/* ===== SIDEBAR NAV GROUP LABEL ===== */
[data-testid="stSidebarNavItems"] .st-emotion-cache-j7qwjs,
[data-testid="stSidebarContent"] span.st-emotion-cache-1rtdyuf,
[data-testid="stSidebarContent"] p {
    color: rgba(255,215,64,0.72) !important;
    font-size: 0.72em !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
}

/* ===== SIDEBAR NAV LINKS ===== */
[data-testid="stSidebarNav"] a {
    border-radius: 10px !important;
    transition: background 0.22s ease, padding-left 0.22s ease !important;
    color: #cfd8dc !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(255,215,64,0.09) !important;
    padding-left: 1.15rem !important;
    color: #ffd740 !important;
}
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background: linear-gradient(90deg, rgba(255,215,64,0.16), rgba(255,171,64,0.06)) !important;
    border-left: 3px solid #ffd740 !important;
    color: #ffd740 !important;
    font-weight: 600 !important;
}

/* ===== SIDEBAR TOP TITLE ===== */
[data-testid="stSidebarHeader"] {
    border-bottom: 1px solid rgba(255,215,64,0.14) !important;
    padding-bottom: 0.8rem !important;
}
</style>
""", unsafe_allow_html=True)

# ===== SERIALIZE DATA KONSTELASI KE JSON UNTUK ENGINE LANGIT =====
_konstelasi_json = json.dumps(DAFTAR_KONSTELASI_KELOMPOK, ensure_ascii=False)

# ===== GLOBAL ASTRAL ENGINE (OPTIMIZED, BEHIND CONTENT, 3 MODES) =====
components.html(f"""
<script>
(function() {{
  const CATALOG_DATA = {_konstelasi_json};

  function __runJordanCosmicEngine__(catalog) {{

    // ===== 1. SETUP CANVAS DI BELAKANG KONTEN (zIndex: 0) =====
    const CANVAS_ID = 'jordan-meteor-canvas';
    let cv = document.getElementById(CANVAS_ID);
    if (!cv) {{
      cv = document.createElement('canvas');
      cv.id = CANVAS_ID;
      Object.assign(cv.style, {{
        position: 'fixed', top: '0', left: '0',
        width: '100vw', height: '100vh',
        pointerEvents: 'none', zIndex: '0', display: 'block'
      }});
      const appRoot = document.querySelector('.stApp') || document.body;
      appRoot.insertBefore(cv, appRoot.firstChild);
    }}
    const ctx = cv.getContext('2d', {{ alpha: true }});
    function resize() {{
      cv.width  = window.innerWidth  || 1920;
      cv.height = window.innerHeight || 1080;
    }}
    resize();
    window.addEventListener('resize', resize, {{ passive: true }});

    // ===== 2. SETUP FLOATING HUD TOOLTIP UNTUK KONSTELASI =====
    const HUD_ID = 'jordan-constellation-hud';
    let hudEl = document.getElementById(HUD_ID);
    if (!hudEl) {{
      hudEl = document.createElement('div');
      hudEl.id = HUD_ID;
      Object.assign(hudEl.style, {{
        position: 'fixed',
        top: '0', left: '0',
        width: '310px',
        padding: '12px 15px',
        background: 'linear-gradient(145deg, rgba(10, 11, 24, 0.96), rgba(18, 16, 38, 0.96))',
        border: '1px solid rgba(255, 215, 64, 0.75)',
        borderRadius: '12px',
        boxShadow: '0 10px 30px rgba(0, 0, 0, 0.75), 0 0 18px rgba(255, 215, 64, 0.2)',
        color: '#eceff1',
        fontFamily: 'Poppins, sans-serif',
        pointerEvents: 'none',
        zIndex: '999990',
        opacity: '0',
        transform: 'translateY(6px)',
        transition: 'opacity 0.2s ease, transform 0.2s ease',
        display: 'none'
      }});
      document.body.appendChild(hudEl);
    }}

    // ===== 3. MOUSE TRACKING =====
    let mouseX = -1000, mouseY = -1000;
    if (!window.__jordanMouseBound) {{
      window.__jordanMouseBound = true;
      document.addEventListener('mousemove', function(e) {{
        mouseX = e.clientX; mouseY = e.clientY;
      }}, {{ passive: true }});
    }}

    // ===== 4. SISTEM 3 MODE TAMPILAN: 'astral' | 'reduce' | 'simple' =====
    const MODES = ['astral', 'reduce', 'simple'];
    const MODE_META = {{
      astral: {{ label: '✦ Mode: Astral',  color: '#ffd740', border: 'rgba(255,215,64,0.45)', title: 'Mode Astral (Penuh). Klik untuk pindah ke Mode Reduce.' }},
      reduce: {{ label: '⚡ Mode: Reduce',  color: '#80d8ff', border: 'rgba(128,216,255,0.45)', title: 'Mode Reduce (Ringan, tanpa animasi). Klik untuk pindah ke Mode Simple.' }},
      simple: {{ label: '🌑 Mode: Simple',  color: '#cfd8dc', border: 'rgba(207,216,220,0.35)', title: 'Mode Simple (Background Hitam Polos). Klik untuk kembali ke Mode Astral.' }}
    }};

    if (!window.__jordanVisualMode || MODES.indexOf(window.__jordanVisualMode) === -1) {{
      window.__jordanVisualMode = 'astral';
    }}

    function applyVisualMode(mode) {{
      window.__jordanVisualMode = mode;
      const b = document.body;
      const h = document.documentElement;
      if (mode === 'simple') {{
        b.classList.add('jordan-mode-simple');
        h.classList.add('jordan-mode-simple');
        cv.style.display = 'none';
      }} else {{
        b.classList.remove('jordan-mode-simple');
        h.classList.remove('jordan-mode-simple');
        cv.style.display = 'block';
      }}

      const btn = document.getElementById('jordan-mode-btn');
      if (btn) {{
        const meta = MODE_META[mode];
        btn.textContent = meta.label;
        btn.style.color = meta.color;
        btn.style.borderColor = meta.border;
        btn.title = meta.title;
      }}

      if (mode !== 'astral') {{
        celestialEvents.length = 0;
        clickEntities.length   = 0;
        constellationStars.length = 0;
        if (hudEl) {{ hudEl.style.opacity = '0'; hudEl.style.display = 'none'; }}
        ctx.clearRect(0, 0, cv.width, cv.height);
        if (mode === 'reduce') {{
          cosmicNebula.draw();
        }}
      }} else {{
        if (constellationStars.length === 0) {{
          spawnConstellationStar();
        }}
      }}
    }}

    // Inject tombol mode switcher (Selalu stick di kanan luar sidebar bagian bawah)
    let modeBtn = document.getElementById('jordan-mode-btn');
    if (!modeBtn) {{
      modeBtn = document.createElement('button');
      modeBtn.id = 'jordan-mode-btn';
      const isMobile = window.innerWidth <= 768;
      Object.assign(modeBtn.style, {{
        position: 'fixed',
        bottom: isMobile ? '16px' : '20px',
        left: '260px',
        right: 'auto',
        zIndex: '999999',
        background: 'rgba(9, 10, 22, 0.92)',
        color: '#ffd740',
        border: '1px solid rgba(255,215,64,0.45)',
        borderRadius: '20px',
        padding: isMobile ? '6px 12px' : '7px 16px',
        fontSize: isMobile ? '11px' : '12px',
        fontFamily: 'Poppins, sans-serif',
        fontWeight: '600',
        letterSpacing: '0.5px',
        cursor: 'pointer',
        backdropFilter: 'blur(6px)',
        transition: 'border-color 0.2s ease, color 0.2s ease',
        boxShadow: '0 4px 14px rgba(0,0,0,0.55)'
      }});
      modeBtn.addEventListener('click', function(e) {{
        e.stopPropagation();
        const curIdx = MODES.indexOf(window.__jordanVisualMode);
        const nextMode = MODES[(curIdx + 1) % MODES.length];
        applyVisualMode(nextMode);
      }});
      document.body.appendChild(modeBtn);

      function updateModeBtnPos() {{
        const isMob = (window.innerWidth || 1920) <= 768;
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        let leftPos = 18;
        if (sidebar && !isMob) {{
          const sbRect = sidebar.getBoundingClientRect();
          if (sbRect.right > 20) {{
            leftPos = Math.round(sbRect.right + 18);
          }}
        }}
        modeBtn.style.left = leftPos + 'px';
        modeBtn.style.right = 'auto';
        modeBtn.style.bottom = isMob ? '16px' : '20px';
      }}

      updateModeBtnPos();
      window.addEventListener('resize', updateModeBtnPos, {{ passive: true }});

      // 1. ResizeObserver: mendeteksi real-time saat sidebar ditarik (dipanjang/pendekin)
      const sidebarEl = document.querySelector('[data-testid="stSidebar"]');
      if (sidebarEl && window.ResizeObserver) {{
        if (window.__jordanSidebarResizeObs) window.__jordanSidebarResizeObs.disconnect();
        window.__jordanSidebarResizeObs = new ResizeObserver(updateModeBtnPos);
        window.__jordanSidebarResizeObs.observe(sidebarEl);
      }}

      // 2. MutationObserver: mendeteksi saat tombol collapse/expand diklik
      if (window.__jordanSidebarObserver) window.__jordanSidebarObserver.disconnect();
      window.__jordanSidebarObserver = new MutationObserver(function() {{
        updateModeBtnPos();
        const sb = document.querySelector('[data-testid="stSidebar"]');
        if (sb && window.ResizeObserver && window.__jordanSidebarResizeObs) {{
          window.__jordanSidebarResizeObs.observe(sb);
        }}
        let count = 0;
        const timer = setInterval(function() {{
          updateModeBtnPos();
          if (++count > 15) clearInterval(timer);
        }}, 25);
      }});
      window.__jordanSidebarObserver.observe(document.body, {{
        attributes: true,
        subtree: true,
        attributeFilter: ['aria-expanded', 'style', 'class']
      }});
    }}

    // ===== 5. PAGE VISIBILITY =====
    if (!window.__jordanVisibilityBound) {{
      window.__jordanVisibilityBound = true;
      document.addEventListener('visibilitychange', function() {{
        if (document.visibilityState === 'hidden') {{
          celestialEvents.length = 0;
          clickEntities.length   = 0;
        }}
      }});
    }}

    // ===== 6. DETEKSI ZONA AMAN =====
    function isSafeSkyMargin(x, y) {{
      const sidebar = document.querySelector('[data-testid="stSidebar"]');
      let leftBound = 20;
      if (sidebar) {{
        const sbRect = sidebar.getBoundingClientRect();
        if (sbRect.right > 0) leftBound = sbRect.right + 25;
      }}
      if (x < leftBound || x > cv.width - 25 || y < 55 || y > cv.height - 65) return false;

      const el = document.elementFromPoint(x, y);
      if (!el) return true;
      const forbidden = el.closest(
        '.jordan-monument, .chronicle-card, .puisi-scroll, .flip-card, .profile-card, .quote-card, ' +
        '.concept-card, .step-box, .score-box, .astral-codex, [data-testid="stImage"], ' +
        '[data-testid="stExpander"], [data-testid="stForm"], button, a, input, select, textarea, ' +
        'h1, h2, h3, p, table, iframe'
      );
      return !forbidden;
    }}

    function isHalamanUtama() {{
      try {{
        const activeNav = document.querySelector('[data-testid="stSidebarNav"] a[aria-selected="true"]');
        if (activeNav) {{
          const txt = (activeNav.textContent || '').toLowerCase();
          if (txt.includes('jordan') || txt.includes('utama') || txt.includes('01')) return true;
          return false;
        }}
      }} catch(e) {{}}
      return true;
    }}

    // ========================================================
    // A. SMOOTH DUAL-LAYER NEBULA
    // ========================================================
    class SmoothCosmicNebula {{
      constructor() {{
        this.palettes = [
          {{ c1: [95, 55, 195],  c2: [24, 155, 215] }},
          {{ c1: [24, 155, 215], c2: [38, 195, 130] }},
          {{ c1: [165, 65, 140], c2: [235, 165, 45] }},
          {{ c1: [45, 95, 210],  c2: [145, 70, 220] }},
          {{ c1: [225, 165, 45], c2: [185, 65, 115] }}
        ];
        this.idx = 0;
        this.nextIdx = 1;
        this.t = 0;
        this.colorSpeed = 0.0014;
        this.driftPhase = Math.random() * Math.PI * 2;
      }}
      update() {{
        this.t += this.colorSpeed;
        this.driftPhase += 0.0025;
        if (this.t >= 1) {{
          this.t -= 1;
          this.idx = this.nextIdx;
          this.nextIdx = (this.nextIdx + 1) % this.palettes.length;
        }}
      }}
      draw() {{
        const p1 = this.palettes[this.idx];
        const p2 = this.palettes[this.nextIdx];
        const ease = 0.5 - 0.5 * Math.cos(this.t * Math.PI);
        const lerp = (a, b) => Math.round(a + (b - a) * ease);

        const r1 = lerp(p1.c1[0], p2.c1[0]), g1 = lerp(p1.c1[1], p2.c1[1]), b1 = lerp(p1.c1[2], p2.c1[2]);
        const r2 = lerp(p1.c2[0], p2.c2[0]), g2 = lerp(p1.c2[1], p2.c2[1]), b2 = lerp(p1.c2[2], p2.c2[2]);

        const cx1 = cv.width  * (0.50 + 0.18 * Math.sin(this.driftPhase));
        const cy1 = cv.height * (0.36 + 0.12 * Math.cos(this.driftPhase * 0.8));
        const rad1 = Math.max(cv.width, cv.height) * 0.46;

        const cx2 = cv.width  * (0.55 - 0.16 * Math.cos(this.driftPhase * 0.7));
        const cy2 = cv.height * (0.58 + 0.12 * Math.sin(this.driftPhase * 0.9));
        const rad2 = Math.max(cv.width, cv.height) * 0.40;

        ctx.save();
        const grad1 = ctx.createRadialGradient(cx1, cy1, 20, cx1, cy1, rad1);
        grad1.addColorStop(0,   'rgba(' + r1 + ',' + g1 + ',' + b1 + ',0.13)');
        grad1.addColorStop(0.5, 'rgba(' + r2 + ',' + g2 + ',' + b2 + ',0.06)');
        grad1.addColorStop(1,   'rgba(0,0,0,0)');
        ctx.fillStyle = grad1;
        ctx.beginPath();
        ctx.arc(cx1, cy1, rad1, 0, Math.PI * 2);
        ctx.fill();

        const grad2 = ctx.createRadialGradient(cx2, cy2, 20, cx2, cy2, rad2);
        grad2.addColorStop(0,   'rgba(' + r2 + ',' + g2 + ',' + b2 + ',0.10)');
        grad2.addColorStop(0.6, 'rgba(' + r1 + ',' + g1 + ',' + b1 + ',0.04)');
        grad2.addColorStop(1,   'rgba(0,0,0,0)');
        ctx.fillStyle = grad2;
        ctx.beginPath();
        ctx.arc(cx2, cy2, rad2, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }}
    }}
    const cosmicNebula = new SmoothCosmicNebula();

    // ========================================================
    // B. 10 BINTANG KONSTELASI KELOMPOK
    // ========================================================
    class ConstellationStar {{
      constructor(data, side) {{
        this.data = data;
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        let sbRight = 260;
        if (sidebar) {{
          const r = sidebar.getBoundingClientRect();
          if (r.right > 0) sbRight = r.right;
        }}
        const availW = cv.width - sbRight;
        if (side === 'left') {{
          this.x = sbRight + 35 + Math.random() * Math.max(40, availW * 0.12);
        }} else {{
          this.x = cv.width - 40 - Math.random() * Math.max(40, availW * 0.12);
        }}
        this.y = cv.height * (0.14 + Math.random() * 0.68);
        this.vx = (Math.random() - 0.5) * 0.25;
        this.vy = (Math.random() - 0.5) * 0.25;
        this.life = 0;
        this.maxLife = 520;
        this.r = 3.2;
        this.pulse = Math.random() * Math.PI * 2;
        this.isHovered = false;
      }}
      update() {{
        this.pulse += 0.045;
        this.x += this.vx;
        this.y += this.vy;
        this.isHovered = Math.hypot(mouseX - this.x, mouseY - this.y) < 38;
        if (!this.isHovered) this.life++;
      }}
      draw() {{
        const p = this.life / this.maxLife;
        const a = this.isHovered ? 1.0 : Math.sin(p * Math.PI);
        if (a <= 0.02) return;

        const c = this.data.warna || [255, 215, 64];
        const colStr = 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',';

        ctx.save();
        const glowR = this.isHovered ? 22 : (13 + Math.sin(this.pulse) * 3);
        const g = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, glowR);
        g.addColorStop(0, colStr + (a * 0.85) + ')');
        g.addColorStop(0.4, colStr + (a * 0.30) + ')');
        g.addColorStop(1, colStr + '0)');
        ctx.fillStyle = g;
        ctx.beginPath();
        ctx.arc(this.x, this.y, glowR, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r + 6 + Math.sin(this.pulse) * 2.5, 0, Math.PI * 2);
        ctx.strokeStyle = colStr + (a * (this.isHovered ? 0.9 : 0.42)) + ')';
        ctx.lineWidth = 1.1;
        ctx.stroke();

        const fl = this.isHovered ? 13 : 8;
        ctx.strokeStyle = colStr + a + ')';
        ctx.lineWidth = 1.4;
        ctx.beginPath();
        ctx.moveTo(this.x - fl, this.y); ctx.lineTo(this.x + fl, this.y);
        ctx.moveTo(this.x, this.y - fl); ctx.lineTo(this.x, this.y + fl);
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.fill();

        if (!this.isHovered && a > 0.45) {{
          ctx.font = '600 9px Poppins, sans-serif';
          ctx.fillStyle = colStr + (a * 0.8) + ')';
          ctx.fillText('✦ ' + (this.data.kode || ''), this.x + 11, this.y + 3);
        }}
        ctx.restore();
      }}
      get dead() {{ return this.life >= this.maxLife; }}
    }}

    const constellationStars = [];
    let shuffleBag = [];
    let lastSpawnedKode = null;
    let sideToggle = (Math.random() < 0.5) ? 0 : 1;

    function refillShuffleBag() {{
      if (!catalog || catalog.length === 0) return;
      shuffleBag = catalog.slice();
      for (let i = shuffleBag.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = shuffleBag[i];
        shuffleBag[i] = shuffleBag[j];
        shuffleBag[j] = tmp;
      }}
      if (shuffleBag.length > 1 && lastSpawnedKode && (shuffleBag[0].kode || shuffleBag[0].nama) === lastSpawnedKode) {{
        const swapIdx = 1 + Math.floor(Math.random() * (shuffleBag.length - 1));
        const tmp = shuffleBag[0];
        shuffleBag[0] = shuffleBag[swapIdx];
        shuffleBag[swapIdx] = tmp;
      }}
    }}

    function spawnConstellationStar() {{
      if (!catalog || catalog.length === 0) return;
      if (constellationStars.length >= 2) return;
      if (shuffleBag.length === 0) {{
        refillShuffleBag();
      }}
      const candidate = shuffleBag[0];
      const side = (sideToggle % 2 === 0) ? 'right' : 'left';
      const star = new ConstellationStar(candidate, side);
      if (isSafeSkyMargin(star.x, star.y)) {{
        shuffleBag.shift();
        lastSpawnedKode = candidate.kode || candidate.nama;
        constellationStars.push(star);
        sideToggle++;
      }}
    }}

    function updateConstellationHud() {{
      let hoveredStar = null;
      for (let i = 0; i < constellationStars.length; i++) {{
        if (constellationStars[i].isHovered) {{
          hoveredStar = constellationStars[i];
          break;
        }}
      }}
      if (!hoveredStar || window.__jordanVisualMode !== 'astral') {{
        if (hudEl.style.display !== 'none') {{
          hudEl.style.opacity = '0';
          hudEl.style.display = 'none';
        }}
        return;
      }}
      const d = hoveredStar.data;
      const c = d.warna || [255, 215, 64];
      const rgb = 'rgb(' + c[0] + ',' + c[1] + ',' + c[2] + ')';
      const rgbaBorder = 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',0.75)';

      hudEl.style.borderColor = rgbaBorder;
      hudEl.innerHTML =
        '<div style="font-size:9.5px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;color:' + rgb + ';margin-bottom:4px;">' +
          '✦ KONSTELASI JORDAN ✦' +
        '</div>' +
        '<div style="font-size:13.5px;font-weight:800;color:#ffffff;line-height:1.25;margin-bottom:2px;">' +
          d.nama +
        '</div>' +
        '<div style="font-size:10.5px;font-weight:600;color:' + rgb + ';font-style:italic;margin-bottom:7px;">' +
          '« ' + (d.gelar || 'Constellation') + ' »' +
        '</div>' +
        '<div style="font-size:11px;color:#d0d8e2;line-height:1.45;border-top:1px solid rgba(255,255,255,0.1);padding-top:6px;">' +
          d.deskripsi +
        '</div>';

      hudEl.style.display = 'block';
      hudEl.style.opacity = '1';
      hudEl.style.transform = 'translateY(0)';

      const bw = 310, bh = hudEl.offsetHeight || 110;
      let bx = hoveredStar.x + 20;
      let by = hoveredStar.y - bh / 2;
      if (bx + bw > cv.width - 16) bx = hoveredStar.x - bw - 20;
      if (bx < 16) bx = 16;
      if (by < 16) by = 16;
      if (by + bh > cv.height - 16) by = cv.height - bh - 16;

      hudEl.style.left = Math.round(bx) + 'px';
      hudEl.style.top  = Math.round(by) + 'px';
    }}

    // ========================================================
    // C. BINTANG JATUH HALUS
    // ========================================================
    const PALETTE_STRINGS = [
      'rgba(255,215,64,',
      'rgba(255,255,255,',
      'rgba(160,230,255,',
      'rgba(210,170,255,'
    ];
    function rndColor() {{
      return PALETTE_STRINGS[Math.floor(Math.random() * PALETTE_STRINGS.length)];
    }}

    class SubtleShootingStar {{
      constructor() {{
        const ang = Math.PI / 4 + (Math.random() - 0.5) * 0.18;
        const spd = 7 + Math.random() * 4.5;
        this.vx = Math.cos(ang) * spd;
        this.vy = Math.sin(ang) * spd;
        this.x  = Math.random() * (cv.width * 0.75);
        this.y  = -40 - Math.random() * 60;
        this.tail  = 130 + Math.random() * 80;
        this.color = rndColor();
        this.w     = 1.4 + Math.random() * 0.8;
        this.alpha = 0.65;
      }}
      update() {{
        this.x += this.vx;
        this.y += this.vy;
      }}
      draw() {{
        ctx.save();
        ctx.lineWidth = this.w;
        ctx.lineCap = 'round';
        const s = Math.hypot(this.vx, this.vy), nx = this.vx / s, ny = this.vy / s;
        const tx = this.x - nx * this.tail, ty = this.y - ny * this.tail;
        const grad = ctx.createLinearGradient(tx, ty, this.x, this.y);
        grad.addColorStop(0, this.color + '0)');
        grad.addColorStop(1, this.color + this.alpha + ')');
        ctx.strokeStyle = grad;
        ctx.beginPath();
        ctx.moveTo(tx, ty);
        ctx.lineTo(this.x, this.y);
        ctx.stroke();
        ctx.restore();
      }}
      get dead() {{ return this.x > cv.width + 200 || this.y > cv.height + 200; }}
    }}

    // ========================================================
    // D. STARLIGHT TOUCH
    // ========================================================
    function spawnStarlightTouch(ox, oy) {{
      clickEntities.push({{
        x: ox, y: oy, r: 3, maxR: 42, alpha: 0.75,
        update: function() {{
          this.r += (this.maxR - this.r) * 0.18 + 0.8;
          this.alpha -= 0.04;
        }},
        draw: function() {{
          if (this.alpha <= 0) return;
          ctx.save();
          ctx.lineWidth = 1.3;
          ctx.strokeStyle = 'rgba(255,215,64,' + Math.max(0, this.alpha) + ')';
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
          ctx.stroke();
          ctx.restore();
        }},
        get dead() {{ return this.alpha <= 0; }}
      }});

      for (let i = 0; i < 5; i++) {{
        const ang = (Math.PI * 2 / 5) * i + (Math.random() - 0.5) * 0.4;
        const spd = 1.8 + Math.random() * 2.4;
        clickEntities.push({{
          x: ox, y: oy,
          vx: Math.cos(ang) * spd,
          vy: Math.sin(ang) * spd,
          alpha: 0.85,
          color: rndColor(),
          update: function() {{
            this.x += this.vx;
            this.y += this.vy;
            this.vx *= 0.94;
            this.vy *= 0.94;
            this.alpha -= 0.045;
          }},
          draw: function() {{
            if (this.alpha <= 0) return;
            ctx.save();
            ctx.fillStyle = this.color + Math.max(0, this.alpha) + ')';
            ctx.beginPath();
            ctx.arc(this.x, this.y, 1.6, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          }},
          get dead() {{ return this.alpha <= 0; }}
        }});
      }}
    }}

    // ========================================================
    // E. SCHEDULER & LOOP OPTIMIZED
    // ========================================================
    const celestialEvents = [];
    const clickEntities   = [];

    function scheduleConstellationLoop() {{
      const delay = 10000 + Math.random() * 5000;
      setTimeout(function() {{
        if (document.visibilityState === 'visible' && window.__jordanVisualMode === 'astral') {{
          spawnConstellationStar();
        }}
        scheduleConstellationLoop();
      }}, delay);
    }}

    function scheduleShootingStarLoop() {{
      const delay = isHalamanUtama() ? (9000 + Math.random() * 5000) : (22000 + Math.random() * 12000);
      setTimeout(function() {{
        if (document.visibilityState === 'visible' && window.__jordanVisualMode === 'astral') {{
          if (celestialEvents.length < 2) {{
            celestialEvents.push(new SubtleShootingStar());
          }}
        }}
        scheduleShootingStarLoop();
      }}, delay);
    }}

    setTimeout(function() {{
      if (window.__jordanVisualMode === 'astral') {{
        spawnConstellationStar();
        celestialEvents.push(new SubtleShootingStar());
      }}
    }}, 1200);

    scheduleConstellationLoop();
    scheduleShootingStarLoop();

    if (window.__jordanCosmicClickHandler) {{
      document.removeEventListener('click', window.__jordanCosmicClickHandler, true);
    }}
    window.__jordanCosmicClickHandler = function(e) {{
      if (window.__jordanVisualMode === 'astral') {{
        spawnStarlightTouch(e.clientX, e.clientY);
      }}
    }};
    document.addEventListener('click', window.__jordanCosmicClickHandler, {{ capture: true, passive: true }});

    applyVisualMode(window.__jordanVisualMode);

    let lastFrameTime = 0;
    function loop(now) {{
      window.__jordanCosmicAnimId = window.requestAnimationFrame(loop);
      if (window.__jordanVisualMode !== 'astral' || document.visibilityState !== 'visible') {{
        return;
      }}
      const minInterval = (clickEntities.length > 0 || celestialEvents.length > 0) ? 16 : 32;
      if (now && (now - lastFrameTime < minInterval)) {{
        return;
      }}
      lastFrameTime = now || 0;

      ctx.clearRect(0, 0, cv.width, cv.height);

      cosmicNebula.update();
      cosmicNebula.draw();

      for (let i = constellationStars.length - 1; i >= 0; i--) {{
        constellationStars[i].update();
        constellationStars[i].draw();
        if (constellationStars[i].dead) constellationStars.splice(i, 1);
      }}
      updateConstellationHud();

      for (let i = celestialEvents.length - 1; i >= 0; i--) {{
        celestialEvents[i].update();
        celestialEvents[i].draw();
        if (celestialEvents[i].dead) celestialEvents.splice(i, 1);
      }}

      for (let i = clickEntities.length - 1; i >= 0; i--) {{
        clickEntities[i].update();
        clickEntities[i].draw();
        if (clickEntities[i].dead) clickEntities.splice(i, 1);
      }}
    }}
    window.__jordanCosmicAnimId = window.requestAnimationFrame(loop);
  }}

  // ===== OUTER WRAPPER: inject ke window.parent =====
  try {{
    const pwin = window.parent, pdoc = window.parent.document;
    if (!pwin || !pdoc) return;

    const CURRENT_VERSION = 19;
    if (pwin.__jordanCosmicActive && pwin.__jordanCosmicVersion === CURRENT_VERSION) return;

    if (pwin.__jordanCosmicAnimId) {{
      pwin.cancelAnimationFrame(pwin.__jordanCosmicAnimId);
      pwin.__jordanCosmicAnimId = null;
    }}
    ['jordan-meteor-canvas', 'jordan-cosmic-core', 'jordan-reduce-btn', 'jordan-mode-btn', 'jordan-mode-style', 'jordan-constellation-hud'].forEach(function(id) {{
      const el = pdoc.getElementById(id);
      if (el) el.remove();
    }});

    pwin.__jordanCosmicActive  = true;
    pwin.__jordanCosmicVersion = CURRENT_VERSION;

    const s = pdoc.createElement('script');
    s.id = 'jordan-cosmic-core';
    s.textContent = '(' + __runJordanCosmicEngine__.toString() + ')(' + JSON.stringify(CATALOG_DATA) + ');';
    pdoc.head.appendChild(s);
  }} catch (err) {{
    console.error('Jordan Cosmic mount error:', err);
  }}
}})();
</script>
""", height=0, scrolling=False)


# session state agar ketika pindah page tidak berubah datanya
st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title="01 Jordan",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/002_Sayyidina Najwa Syahra.py",
    title="002 - Sayyidina Najwa Syahra",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/036_Astrit Aisya Rahmi.py",
    title="036 - Astrit Aisya Rahmi",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/040_Fildzah Cahya Kamila.py",
    title="040 - Fildzah Cahya Kamila",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/055_Septi Widia Arini.py",
    title="055 - Septi Widia Arini",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/062_Iva Aulia Sofia.py",
    title="062 - Iva Aulia Sofia",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/064_Lintar Abhinaya Putra Zulmi.py",
    title="064 - Lintar Abhinaya Putra Zulmi",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/068_Bening Arianti.py",
    title="068 - Bening Arianti",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/069_Ahda Nabiwa.py",
    title="069 - Ahda Nabiwa",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/093_Rahmad Bayu Ridho.py",
    title="093 - Rahmad Bayu Ridho",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/094_Mojes Wijaya.py",
    title="094 - Mojes Wijaya",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/095_M Rafli Raditya.py",
    title="095 - M Rafli Raditya",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/104_M Abyan Alghaniyyu.py",
    title="104 - M Abyan Alghaniyyu",
    icon=":material/person:",
)
Mahasiswa13 = st.Page(
    "Buku Kating/106_Bintang Mahardika.py",
    title="106 - Bintang Mahardika",
    icon=":material/person:",
)

KREASI = st.Page("tools/KREASI.py", title="Jordan Astral Arcade", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="Jordan Codex", icon=":material/search:")

if st.session_state.pindah:
    pg = st.navigation(
        {
            "✦ Halaman Utama": [Homepage],
            "📖 Buku Kating": [
                Mahasiswa1,
                Mahasiswa2,
                Mahasiswa3,
                Mahasiswa4,
                Mahasiswa5,
                Mahasiswa6,
                Mahasiswa7,
                Mahasiswa8,
                Mahasiswa9,
                Mahasiswa10,
                Mahasiswa11,
                Mahasiswa12,
                Mahasiswa13,
            ],
            "🔍 Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(")
pg.run()
