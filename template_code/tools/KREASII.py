import streamlit as st

# ============================================================
#            KREASII — JORDAN MEMORIES 📸🎬
# ============================================================

# ===== CSS — Full-width, borderless, cinematic =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    /* ---------- FULL-WIDTH: hapus semua padding Streamlit ---------- */
    .block-container,
    .stMainBlockContainer,
    [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* ---------- HERO SECTION — Full viewport ---------- */
    .hero-fullscreen {
        width: 100%;
        min-height: 100vh;
        background: linear-gradient(180deg, #050510 0%, #0a0a1a 30%, #0f0f20 60%, #12122a 100%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem 1rem;
        position: relative;
        overflow: hidden;
    }
    .hero-fullscreen::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: radial-gradient(ellipse at 50% 30%, rgba(255,215,64,0.04) 0%, transparent 60%);
        pointer-events: none;
    }
    .hero-text {
        text-align: center;
        position: relative;
        z-index: 2;
        margin-bottom: 2rem;
    }
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 4.5em;
        font-weight: 900;
        background: linear-gradient(135deg, #ffd740, #ffab40, #ff6e40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 5px;
        margin: 0;
        line-height: 1.1;
    }
    .hero-subtitle {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.2em;
        color: #78909c;
        margin-top: 0.8rem;
        letter-spacing: 1px;
    }

    /* Video container di dalam hero */
    .hero-video-wrap {
        position: relative;
        z-index: 2;
        width: 85%;
        max-width: 960px;
        aspect-ratio: 16 / 9;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid rgba(255,215,64,0.15);
        box-shadow: 0 20px 80px rgba(0,0,0,0.6), 0 0 60px rgba(255,215,64,0.05);
    }
    .hero-video-wrap iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    .video-placeholder-inner {
        width: 100%;
        height: 100%;
        background: linear-gradient(145deg, #0d0d1a, #161630);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: #546e7a;
    }
    .video-placeholder-inner .play-icon {
        font-size: 4em;
        margin-bottom: 0.8rem;
        opacity: 0.7;
    }
    .video-placeholder-inner .play-text {
        font-size: 1em;
        font-weight: 500;
    }
    .video-placeholder-inner .play-hint {
        font-size: 0.78em;
        margin-top: 0.5rem;
        color: #37474f;
    }

    /* Scroll indicator */
    .scroll-indicator {
        position: relative;
        z-index: 2;
        text-align: center;
        margin-top: 2.5rem;
        animation: bounce 2s ease-in-out infinite;
    }
    .scroll-indicator span {
        color: rgba(255,215,64,0.4);
        font-size: 1.5em;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(10px); }
    }

    /* ---------- CONTENT SECTIONS ---------- */
    .content-section {
        padding: 3rem 5%;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Section title */
    .mem-section-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.2em;
        font-weight: 700;
        margin: 0 0 0.3rem 0;
        background: linear-gradient(90deg, #ffd740, #ffab40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .mem-section-desc {
        text-align: center;
        color: #78909c;
        font-size: 0.92em;
        margin-bottom: 2rem;
        font-style: italic;
    }

    /* Dividers */
    .gold-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 0 auto;
        max-width: 300px;
        border: none;
    }
    .section-gap {
        height: 2rem;
    }

    /* Photo placeholder cards */
    .photo-drop {
        background: linear-gradient(145deg, #13132a, #1a1a35);
        border: 2px dashed rgba(255,215,64,0.15);
        border-radius: 14px;
        aspect-ratio: 4 / 3;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        margin-bottom: 0.6rem;
    }
    .photo-drop:hover {
        border-color: rgba(255,215,64,0.35);
        background: linear-gradient(145deg, #1a1a35, #222245);
    }
    .photo-drop-icon {
        font-size: 2em;
        margin-bottom: 0.3rem;
        opacity: 0.5;
    }
    .photo-drop-label {
        color: #546e7a;
        font-size: 0.8em;
        text-align: center;
        line-height: 1.4;
    }

    /* Kating department card */
    .dept-card {
        background: linear-gradient(145deg, #13132a, #1a1a35);
        border: 1px solid rgba(255,215,64,0.1);
        border-radius: 16px;
        overflow: hidden;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
    }
    .dept-card:hover {
        border-color: rgba(255,215,64,0.3);
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    }
    .dept-photo-area {
        aspect-ratio: 4 / 3;
        background: linear-gradient(145deg, #0d0d1a, #161630);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .dept-photo-area .photo-drop-icon { opacity: 0.35; font-size: 2.2em; }
    .dept-info {
        padding: 0.8rem 1rem;
        text-align: center;
    }
    .dept-name {
        font-family: 'Poppins', sans-serif;
        font-size: 0.85em;
        font-weight: 600;
        color: #ffd740;
        margin-bottom: 0.15rem;
    }
    .dept-abbr {
        font-size: 0.72em;
        color: #546e7a;
    }

    /* Footer */
    .footer-memories {
        text-align: center;
        color: #37474f;
        font-size: 0.78em;
        padding: 2rem 1rem 3rem 1rem;
    }
</style>
""", unsafe_allow_html=True)


# ====================================================================
#              HERO SECTION — FULL SCREEN VIDEO
# ====================================================================
# =====================================================================
#   CARA MENGGANTI VIDEO:
#   Ganti blok <div class='video-placeholder-inner'>...</div>
#   dengan iframe YouTube atau Google Drive:
#
#   YouTube:
#     <iframe src="https://www.youtube.com/embed/VIDEO_ID"
#             allowfullscreen></iframe>
#
#   Google Drive:
#     <iframe src="https://drive.google.com/file/d/FILE_ID/preview"
#             allow="autoplay" allowfullscreen></iframe>
# =====================================================================

st.markdown("""
<div class='hero-fullscreen'>
    <div class='hero-text'>
        <h1 class='hero-title'>JORDAN<br>MEMORIES</h1>
        <p class='hero-subtitle'>"Dari awal kader hingga akhir, cerita kita abadi."</p>
    </div>

    <div class='hero-video-wrap'>
        <!-- GANTI BAGIAN INI DENGAN IFRAME VIDEO ASLI -->
        <div class='video-placeholder-inner'>
            <div class='play-icon'>▶️</div>
            <div class='play-text'>After Movie — Jordan Memories</div>
            <div class='play-hint'>Ganti placeholder ini dengan video asli</div>
        </div>
    </div>

    <div class='scroll-indicator'>
        <span>▼</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ====================================================================
#              SECTION 1 — FOTO BARENG JORDAN (Photo Dump)
# ====================================================================

st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='content-section'>
    <div class='mem-section-title'>📸 Foto Bareng Jordan</div>
    <div class='mem-section-desc'>Semua momen kebersamaan kita, dari awal sampai akhir</div>
</div>
""", unsafe_allow_html=True)

# =====================================================================
#   CARA MENAMBAHKAN FOTO:
#   Ganti placeholder di setiap kolom dengan:
#     st.image("URL_FOTO", use_container_width=True)
#
#   Google Drive:
#     st.image("https://drive.google.com/uc?export=view&id=FILE_ID",
#              use_container_width=True)
#
#   Tambah/kurangi baris sesuai jumlah foto yang ada.
# =====================================================================

def photo_placeholder(label="Tambahkan foto"):
    """Render placeholder card untuk foto."""
    st.markdown(f"""
    <div class='photo-drop'>
        <div class='photo-drop-icon'>📷</div>
        <div class='photo-drop-label'>{label}</div>
    </div>""", unsafe_allow_html=True)


# --- Row 1 ---
r1c1, r1c2, r1c3 = st.columns(3)
with r1c1:
    photo_placeholder()
with r1c2:
    photo_placeholder()
with r1c3:
    photo_placeholder()

# --- Row 2 ---
r2c1, r2c2, r2c3 = st.columns(3)
with r2c1:
    photo_placeholder()
with r2c2:
    photo_placeholder()
with r2c3:
    photo_placeholder()

# --- Row 3 ---
r3c1, r3c2, r3c3 = st.columns(3)
with r3c1:
    photo_placeholder()
with r3c2:
    photo_placeholder()
with r3c3:
    photo_placeholder()

# --- Row 4 ---
r4c1, r4c2, r4c3 = st.columns(3)
with r4c1:
    photo_placeholder()
with r4c2:
    photo_placeholder()
with r4c3:
    photo_placeholder()


# ====================================================================
#        SECTION 2 — FOTO DENGAN KATING DEPARTEMEN (9 Dept)
# ====================================================================

st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)

st.markdown("""
<div class='content-section'>
    <div class='mem-section-title'>🤝 Bersama Kating Departemen</div>
    <div class='mem-section-desc'>Kenangan bersama para kakak kating dari setiap departemen HMSD Adyatama</div>
</div>
""", unsafe_allow_html=True)

# =====================================================================
#   CARA MENAMBAHKAN FOTO KATING:
#   Ganti placeholder di setiap kolom dengan:
#     st.image("URL_FOTO", caption="Departemen ...", use_container_width=True)
#
#   Ganti nama departemen sesuai kebutuhan.
# =====================================================================

departemen_list = [
    ("Kesekjenan", "BPH"),
    ("Badan Kesenatoran", "BASON"),
    ("Badan Legislatif", "BALEG"),
    ("Akademik dan Keprofesian", "MIKFES"),
    ("Media Kreatif", "MEDKRAF"),
    ("Minat dan Bakat", "MINBAK"),
    ("Eksternal", ""),
    ("Internal", ""),
    ("Storage Sains Data", "SSD"),
]


def dept_placeholder(nama, singkatan=""):
    """Render placeholder card untuk foto kating departemen."""
    abbr_html = f"<div class='dept-abbr'>{singkatan}</div>" if singkatan else ""
    st.markdown(f"""
    <div class='dept-card'>
        <div class='dept-photo-area'>
            <div class='photo-drop-icon'>📷</div>
        </div>
        <div class='dept-info'>
            <div class='dept-name'>{nama}</div>
            {abbr_html}
        </div>
    </div>""", unsafe_allow_html=True)


# --- Row 1 (dept 1-3) ---
dc1, dc2, dc3 = st.columns(3)
with dc1:
    dept_placeholder(departemen_list[0][0], departemen_list[0][1])
with dc2:
    dept_placeholder(departemen_list[1][0], departemen_list[1][1])
with dc3:
    dept_placeholder(departemen_list[2][0], departemen_list[2][1])

# --- Row 2 (dept 4-6) ---
dc4, dc5, dc6 = st.columns(3)
with dc4:
    dept_placeholder(departemen_list[3][0], departemen_list[3][1])
with dc5:
    dept_placeholder(departemen_list[4][0], departemen_list[4][1])
with dc6:
    dept_placeholder(departemen_list[5][0], departemen_list[5][1])

# --- Row 3 (dept 7-9) ---
dc7, dc8, dc9 = st.columns(3)
with dc7:
    dept_placeholder(departemen_list[6][0], departemen_list[6][1])
with dc8:
    dept_placeholder(departemen_list[7][0], departemen_list[7][1])
with dc9:
    dept_placeholder(departemen_list[8][0], departemen_list[8][1])


# ===== FOOTER =====
st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.markdown("<div class='gold-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='footer-memories'>
    Made with ❤️ by Kelompok 01 Jordan — CEO HMSD Adyatama ITERA 2026
</div>
""", unsafe_allow_html=True)
