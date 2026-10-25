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
# 🍷 PREMIUM CSS — BACKGROUND TEKSTUR KERTAS
# ============================================================
PREMIUM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #222222; }

/* 💥 BACKGROUND TEKSTUR KERTAS */
.stApp {
    background-color: #f4f0eb;
    background-image: url('https://www.transparenttextures.com/patterns/natural-paper.png');
    background-attachment: fixed;
}

.centered-title {
    text-align: center; font-family: 'Playfair Display', serif; font-weight: 800;
    font-size: 3em !important; letter-spacing: 1px; margin-bottom: 8px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    display: block;
}
.centered-title::after {
    content: ''; display: block; width: 90px; height: 3px; margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent); border-radius: 3px;
}
.profile-card {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 28px 32px; border-radius: 20px; border: 1px solid rgba(217,195,163,0.55);
    box-shadow: 0 10px 30px rgba(112,28,35,0.08); margin-bottom: 22px; position: relative; overflow: hidden;
}
.profile-card::before {
    content: ''; position: absolute; top: 0; left: 0; width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.profile-header { font-family: 'Playfair Display', serif; font-size: 22px; font-weight: 700; color: #701c23; margin-bottom: 6px; position: relative; z-index: 1; }
.profile-subheader { display: inline-block; padding: 4px 14px; font-size: 10px; font-weight: 700; border-radius: 999px; background: #701c23; color: #fff; margin-bottom: 16px; position: relative; z-index: 1; }
.profile-subheader.leader { background: #b8912e; color: #4e1318; }
.profile-divider { width: 100%; height: 1px; background: linear-gradient(90deg, transparent, #d9c3a3, transparent); margin: 4px 0 16px 0; }
.info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px 18px; position: relative; z-index: 1; }
.info-item { font-size: 13px; padding: 8px 12px; border-radius: 10px; background: rgba(217,195,163,0.10); border-left: 2px solid #d9c3a3; transition: background 0.3s ease; }
.info-item:hover { background: rgba(217,195,163,0.20); border-left-color: #701c23; }
.info-item.full { grid-column: 1 / -1; }
.info-label { display: block; font-weight: 700; color: #701c23; font-size: 9.5px; margin-bottom: 2px; text-transform: uppercase; }
.info-value { color: #2b2320; font-weight: 500; }
.quote-box { margin-top: 14px; padding: 14px 18px 14px 22px; border-radius: 12px; background: rgba(217,195,163,0.10); border: 1px solid rgba(217,195,163,0.45); position: relative; z-index: 1; }
.quote-box::before { content: '"'; position: absolute; top: -6px; left: 8px; font-family: 'Playfair Display', serif; font-size: 44px; color: rgba(112,28,35,0.15); }
.quote-label { font-size: 9.5px; font-weight: 700; color: #701c23; margin-bottom: 4px; text-transform: uppercase; }
.quote-text { font-family: 'Playfair Display', serif; font-style: italic; font-size: 13.5px; color: #4e1318; }

/* 💥 EFEK FOTO (HOVER, BINGKAI, DAN SUDUT) */
.photo-wrapper {
    position: relative; padding: 6px; border-radius: 18px;
    background: linear-gradient(135deg, #701c23 0%, #d9c3a3 50%, #701c23 100%);
    box-shadow: 0 12px 28px rgba(112,28,35,0.22), 0 4px 10px rgba(112,28,35,0.12);
    margin-bottom: 12px; transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.photo-wrapper:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 38px rgba(112,28,35,0.32), 0 6px 14px rgba(112,28,35,0.18);
}
.photo-wrapper img {
    display: block; width: 100%; aspect-ratio: 3 / 4; object-fit: cover; border-radius: 13px;
}
.photo-corner {
    position: absolute; width: 22px; height: 22px; border: 2px solid #f4f0eb; opacity: 0.9; pointer-events: none;
}
.photo-corner.tl { top: 10px; left: 10px; border-right: none; border-bottom: none; border-top-left-radius: 8px; }
.photo-corner.br { bottom: 10px; right: 10px; border-left: none; border-top: none; border-bottom-right-radius: 8px; }
</style>
"""

def setup_buku_kating_page():
    st.markdown(PREMIUM_CSS, unsafe_allow_html=True)
    st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# (SISA FUNGSI UTILITY DI BAWAH INI TETAP SAMA PERSIS SEPERTI SEBELUMNYA)
# get_drive_file_id, load_image, image_data_uri, render_photo, render_profile_card, display_images_with_data, streamlit_menu
# ... (lanjutkan copy-paste fungsi dari file utils.py kamu yang lama) ...

# ============================================================
# 🎨 SETUP SIDEBAR (KHUSUS MAIN.PY)
# ============================================================
SIDEBAR_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');
[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #701c23 0%, #4e1318 100%) !important; 
}
[data-testid="stSidebar"] *, 
[data-testid="stSidebar"] span, 
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] div, 
[data-testid="stSidebar"] svg {
    color: #ffffff !important; 
    fill: #ffffff !important; 
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
