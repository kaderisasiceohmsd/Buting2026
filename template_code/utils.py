# utils.py
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from urllib.parse import urlparse, parse_qs
import base64
import html as html_lib

# ============================================================
# 🎨 SUPER PREMIUM CARD CSS (Pink Base)
# ============================================================
PREMIUM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { 
    font-family: 'Inter', sans-serif; 
    color: #222222; 
}

/* Biarkan background mengikuti config.toml (FFD1D1) */
.stApp {
    background-attachment: fixed;
}

.centered-title {
    text-align: center; font-family: 'Playfair Display', serif; font-weight: 900;
    font-size: 3.5em !important; letter-spacing: 2px; margin-bottom: 10px;
    background: linear-gradient(135deg, #4e1318 0%, #a8323d 45%, #4e1318 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    display: block;
    text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
}
.centered-title::after {
    content: ''; display: block; width: 120px; height: 3px; margin: 16px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent); border-radius: 3px;
}

/* 💥 SUPER PREMIUM PROFILE CARD */
.profile-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    padding: 35px 40px; 
    border-radius: 12px; 
    border: 1px solid rgba(255, 255, 255, 0.8);
    box-shadow: 
        0 25px 50px -12px rgba(112,28,35,0.25), /* Shadow luar tebal */
        inset 0 0 0 1px rgba(217,195,163,0.5),  /* Garis emas dalam */
        inset 0 0 20px rgba(255, 209, 209, 0.5); /* Cahaya pink dalam */
    margin-bottom: 25px; 
    position: relative; 
    overflow: hidden;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.profile-card:hover {
    transform: translateY(-5px);
    box-shadow: 
        0 35px 60px -15px rgba(112,28,35,0.35),
        inset 0 0 0 1px rgba(184,145,46,1), 
        inset 0 0 30px rgba(255, 209, 209, 0.8);
}

/* Garis aksen vertikal di kiri */
.profile-card::before {
    content: ''; 
    position: absolute; 
    top: 0; left: 0; 
    width: 8px; 
    height: 100%;
    background: linear-gradient(180deg, #4e1318, #b8912e, #4e1318);
}

/* Kilauan Shimmer (Opsional, sangat premium) */
.profile-card::after {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: linear-gradient(to bottom right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.4) 50%, rgba(255,255,255,0) 100%);
    transform: rotate(45deg);
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.5s ease;
}
.profile-card:hover::after {
    opacity: 1;
    animation: shimmer 1.5s infinite;
}
@keyframes shimmer {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(100%) rotate(45deg); }
}

.profile-header { 
    font-family: 'Playfair Display', serif; 
    font-size: 26px; 
    font-weight: 800; 
    color: #4e1318; 
    margin-bottom: 10px; 
    position: relative; 
    z-index: 2; 
    text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
}
.profile-subheader { 
    display: inline-block; 
    padding: 6px 18px; 
    font-size: 10px; 
    font-weight: 700; 
    letter-spacing: 1.5px; 
    text-transform: uppercase; 
    border-radius: 6px; 
    background: #4e1318; 
    color: #f4f0eb; 
    margin-bottom: 20px; 
    position: relative; 
    z-index: 2; 
    box-shadow: 0 4px 15px rgba(112,28,35,0.3);
}
.profile-subheader.leader { 
    background: linear-gradient(135deg, #b8912e, #d4af37); 
    color: #2d0a0d; 
    box-shadow: 0 4px 15px rgba(184,145,46,0.5);
}
.profile-divider { 
    width: 100%; 
    height: 1px; 
    background: linear-gradient(90deg, transparent, rgba(112,28,35,0.4), transparent); 
    margin: 4px 0 20px 0; 
    position: relative;
    z-index: 2;
}

.info-grid { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 14px 20px; 
    position: relative; 
    z-index: 2; 
}
.info-item { 
    font-size: 13.5px; 
    padding: 12px 16px; 
    border-radius: 8px; 
    background: rgba(255,255,255,0.8); 
    border: 1px solid rgba(112,28,35,0.1); 
    border-left: 4px solid #701c23; 
    transition: all 0.3s ease; 
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.info-item:hover { 
    background: #fff; 
    transform: translateX(5px); 
    box-shadow: 0 6px 15px rgba(112,28,35,0.1); 
    border-left-color: #b8912e;
}
.info-item.full { grid-column: 1 / -1; }
.info-label { 
    display: block; 
    font-weight: 700; 
    color: #701c23; 
    font-size: 9px; 
    margin-bottom: 4px; 
    text-transform: uppercase; 
    letter-spacing: 1.5px; 
}
.info-value { color: #2b2320; font-weight: 500; }

.quote-box { 
    margin-top: 20px; 
    padding: 18px 24px; 
    border-radius: 8px; 
    background: rgba(255, 209, 209, 0.3); 
    border: 1px solid rgba(112,28,35,0.1); 
    position: relative; 
    z-index: 2; 
}
.quote-box::before { 
    content: '"'; 
    position: absolute; 
    top: -10px; left: 12px; 
    font-family: 'Playfair Display', serif; 
    font-size: 52px; 
    color: rgba(112,28,35,0.2); 
}
.quote-label { 
    font-size: 9px; 
    font-weight: 800; 
    color: #701c23; 
    margin-bottom: 8px; 
    text-transform: uppercase; 
    letter-spacing: 1.5px; 
}
.quote-text { 
    font-family: 'Playfair Display', serif; 
    font-style: italic; 
    font-size: 15px; 
    color: #4e1318; 
    line-height: 1.6; 
}

/* 💥 SUPER PREMIUM PHOTO FRAME */
.photo-wrapper {
    position: relative; 
    padding: 10px; 
    border-radius: 12px;
    background: #fff;
    box-shadow: 
        0 20px 40px -10px rgba(112,28,35,0.3), 
        inset 0 0 0 2px #b8912e; /* Bingkai emas tebal */
    margin-bottom: 15px;
    transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.5s ease;
}
.photo-wrapper:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 
        0 30px 60px -15px rgba(112,28,35,0.4), 
        inset 0 0 0 3px #d4af37;
}
.photo-wrapper img {
    display: block; width: 100%; aspect-ratio: 3 / 4; object-fit: cover; border-radius: 6px;
    filter: sepia(0.1) contrast(1.05);
}
/* Sudut ornamen */
.photo-corner {
    position: absolute; width: 30px; height: 30px; border: 2px solid #b8912e; opacity: 1; pointer-events: none;
}
.photo-corner.tl { top: 4px; left: 4px; border-right: none; border-bottom: none; border-top-left-radius: 8px; }
.photo-corner.br { bottom: 4px; right: 4px; border-left: none; border-top: none; border-bottom-right-radius: 8px; }
</style>
"""

# ============================================================
# ⚙️ SETUP PAGE
# ============================================================
def setup_buku_kating_page():
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# ============================================================
# 🔧 UTILITY FUNCTIONS
# ============================================================
def get_drive_file_id(url):
    try:
        parsed = urlparse(url); query = parse_qs(parsed.query)
        if query.get("id"): return query["id"][0]
        parts = parsed.path.split("/")
        if "d" in parts:
            idx = parts.index("d")
            if idx + 1 < len(parts): return parts[idx + 1]
    except: pass
    return None

@st.cache_data(show_spinner=False, max_entries=50)
def load_image(url):
    file_id = get_drive_file_id(url)
    candidate_urls = []
    if file_id:
        candidate_urls.extend([
            f"https://drive.google.com/thumbnail?id={file_id}&sz=w1200",
            f"https://drive.google.com/uc?export=download&id={file_id}",
            f"https://drive.google.com/uc?export=view&id={file_id}",
        ])
    candidate_urls.append(url)
    for candidate in dict.fromkeys(candidate_urls):
        try:
            response = requests.get(candidate, headers={"User-Agent": "Mozilla/5.0"}, timeout=15, stream=True)
            response.raise_for_status()
            img_bytes = BytesIO(response.content)
            
            img = ImageOps.exif_transpose(Image.open(img_bytes))
            img.load(); response.close(); img_bytes.close()
            return img
        except: continue
    return None

@st.cache_data(show_spinner=False, max_entries=80)
def image_data_uri(url, max_dim=800, quality=80):
    img = load_image(url)
    if img is None: return None
    img = img.copy()
    
    has_transparency = False
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        has_transparency = True
        
    if max(img.size) > max_dim: 
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)
        
    buffer = BytesIO()
    
    if has_transparency:
        img.save(buffer, format="PNG", optimize=True)
        mime_type = "image/png"
    else:
        img.convert("RGB").save(buffer, format="JPEG", quality=quality, optimize=True)
        mime_type = "image/jpeg"

    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return f"data:{mime_type};base64,{encoded}"

def render_photo(img_src, alt="Foto"):
    if not img_src:
        st.markdown('<div style="width:100%;aspect-ratio:3/4;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,0.5);border-radius:12px;">Foto tidak tersedia</div>', unsafe_allow_html=True)
        return
    st.markdown(f"""
        <div class="photo-wrapper">
            <div class="photo-corner tl"></div>
            <div class="photo-corner br"></div>
            <img src="{img_src}" alt="{html_lib.escape(alt, quote=True)}">
        </div>
    """, unsafe_allow_html=True)

def render_profile_card(m):
    nama = html_lib.escape(str(m.get("nama", "-")))
    jabatan_raw = str(m.get("jabatan", "")).strip()
    jabatan = html_lib.escape(jabatan_raw) if jabatan_raw else "—"
    nim = html_lib.escape(str(m.get("nim", "-")))
    umur = html_lib.escape(str(m.get("umur", "-")))
    asal = html_lib.escape(str(m.get("asal", "-")))
    alamat = html_lib.escape(str(m.get("alamat", "-")))
    hobbi = html_lib.escape(str(m.get("hobbi", "-")))
    sosmed = html_lib.escape(str(m.get("sosmed", "-")))
    kesan = html_lib.escape(str(m.get("kesan", "-")))
    pesan = html_lib.escape(str(m.get("pesan", "-")))

    gold_keywords = ["ketua", "sekretaris", "senator", "kepala", "bendahara"]
    is_leader = any(k in jabatan_raw.lower() for k in gold_keywords)
    subheader_class = "profile-subheader leader" if is_leader else "profile-subheader"

    html_block = f"""<div class="profile-card">
<div class="profile-header">{nama}</div>
<div class="{subheader_class}">{jabatan}</div>
<div class="profile-divider"></div>
<div class="info-grid">
<div class="info-item"><span class="info-label">NIM</span><span class="info-value">{nim}</span></div>
<div class="info-item"><span class="info-label">Umur</span><span class="info-value">{umur} Tahun</span></div>
<div class="info-item"><span class="info-label">Asal</span><span class="info-value">{asal}</span></div>
<div class="info-item"><span class="info-label">Alamat</span><span class="info-value">{alamat}</span></div>
<div class="info-item full"><span class="info-label">Hobi</span><span class="info-value">{hobbi}</span></div>
<div class="info-item full"><span class="info-label">Sosial Media</span><span class="info-value">{sosmed}</span></div>
</div>
<div class="quote-box"><span class="quote-label">Kesan</span><div class="quote-text">{kesan}</div></div>
<div class="quote-box" style="margin-top:12px;"><span class="quote-label">Pesan</span><div class="quote-text">{pesan}</div></div>
</div>"""
    st.markdown(html_block, unsafe_allow_html=True)

def display_images_with_data(gambar_urls, data_list, batch_size=5, key="default"):
    total_items = min(len(gambar_urls), len(data_list))
    if total_items == 0: return
    state_key = f"loaded_count_{key}"
    if state_key not in st.session_state: st.session_state[state_key] = batch_size
    if st.session_state[state_key] > total_items: st.session_state[state_key] = total_items
    load_until = min(st.session_state[state_key], total_items)
    for i in range(load_until):
        with st.spinner(f"Memuat gambar {i+1} dari {total_items}..."):
            img_src = image_data_uri(gambar_urls[i])
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1: render_photo(img_src, data_list[i].get("nama", "Foto"))
        with col2: render_profile_card(data_list[i])
        st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)
    if load_until < total_items:
        next_batch = min(batch_size, total_items - load_until)
        if st.button(f"📸 Muat {next_batch} Foto Lagi", use_container_width=True, type="primary"):
            st.session_state[state_key] += batch_size
            st.rerun()

def streamlit_menu(default_index=0):
    return option_menu(
        menu_title=None, 
        options=["Kesekjenan", "Baleg", "Senator", "Departemen PSDA", "Departemen MIKFES", "Departemen Eksternal", "Departemen Internal", "Departemen SSD", "Departemen Medkraf", "Departemen MINBAK"],
        icons=["people-fill"] * 10, default_index=default_index, orientation="horizontal",
        styles={
            "container": {"padding": "6px!important", "background-color": "rgba(255, 255, 255, 0.9)", "backdrop-filter": "blur(10px)", "border-radius": "10px", "border": "1px solid rgba(112,28,35,0.15)", "box-shadow": "0 10px 25px rgba(112,28,35,0.1)"}, 
            "nav-link": {"color": "#4e1318", "font-size": "14px", "font-weight": "600"},
            "nav-link-selected": {"background": "#701c23", "color": "#f4f0eb", "box-shadow": "0 4px 12px rgba(112,28,35,0.3)"}
        }
    )

# ============================================================
# 🎨 SETUP SIDEBAR
# ============================================================
SIDEBAR_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');
[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important; 
    border-right: 1px solid rgba(255,209,209,0.2);
}
[data-testid="stSidebar"] *, 
[data-testid="stSidebar"] span, 
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] div, 
[data-testid="stSidebar"] svg {
    color: #f4f0eb !important; 
    fill: #f4f0eb !important; 
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] strong { 
    font-family: 'Playfair Display', serif !important; 
}
#MainMenu { visibility: hidden; }
header { visibility: hidden; }
</style>
"""

def setup_common():
    st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

def setup_halaman_utama_css(custom_css: str):
    setup_common()
    st.markdown(custom_css, unsafe_allow_html=True)
