import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import base64
import json
import os
import re
import time

# Pilihan gaya card kating:
# - "manjang" : Card kating memanjang horizontal (1 kartu utuh menyatu)
# - "klasik"  : Card kating 2 kolom seperti sebelumnya (foto + kesan/pesan di kiri, biodata di kanan)
GAYA_CARD_KATING = "manjang"

# ===== STYLING TEMA HITAM - OREN (DEPARTEMEN SEPERTI SEBELUMNYA + CARD KATING MANJANG) =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
    }

    .kating-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.8em;
        font-weight: 800;
        background: linear-gradient(135deg, #ffd740, #ffab40, #ff6e40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2px;
        margin-bottom: 0.1rem;
    }
    .kating-subtitle {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 1.05em;
        color: #b0bec5;
        font-weight: 300;
        letter-spacing: 1.5px;
        margin-bottom: 0.5rem;
    }
    .fancy-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 1rem auto 1.5rem auto;
        max-width: 450px;
        border: none;
    }

    /* Division section banner (Persis seperti sebelumnya) */
    .division-banner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 2rem 0 1.2rem 0;
        padding: 0.7rem 1.4rem;
        background: linear-gradient(90deg, rgba(255, 171, 64, 0.18), rgba(20, 20, 36, 0.5));
        border-left: 4px solid #ff9800;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    .division-banner-title {
        font-size: 1.2em;
        font-weight: 700;
        color: #ffd740;
        letter-spacing: 0.5px;
    }
    .division-banner-badge {
        font-size: 0.82em;
        font-weight: 600;
        color: #ffd740;
        background: rgba(255, 171, 64, 0.2);
        padding: 4px 10px;
        border-radius: 20px;
        border: 1px solid rgba(255, 171, 64, 0.4);
    }

    /* ===== OPSI 1: CARD KATING MANJANG (DISERASIKAN DENGAN TEMA HITAM-OREN DEPARTEMEN) ===== */
    .astral-dossier {
        position: relative;
        background: linear-gradient(145deg, #161628, #1a1a30);
        border: 1px solid rgba(255, 171, 64, 0.24);
        border-radius: 18px;
        overflow: hidden;
        margin: 0 0 1.25rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }
    .astral-dossier:hover {
        border-color: rgba(255, 171, 64, 0.65);
        box-shadow: 0 12px 44px rgba(255, 152, 0, 0.2);
        transform: translateY(-2px);
    }
    .dossier-card-link {
        position: absolute;
        inset: 0;
        z-index: 6;
        cursor: pointer;
        text-decoration: none !important;
    }
    .astral-dossier:hover .sosmed-chip {
        border-color: rgba(255, 215, 64, 0.55);
        background: rgba(255, 152, 0, 0.14);
    }
    .dossier-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
        padding: 8px 18px;
        background: linear-gradient(90deg, rgba(255, 152, 0, 0.14), rgba(18, 18, 34, 0.9), rgba(255, 215, 64, 0.1));
        border-bottom: 1px solid rgba(255, 215, 64, 0.16);
    }
    .dossier-index {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72em;
        font-weight: 700;
        color: #ffd740;
        letter-spacing: 1.3px;
    }
    .dossier-jabatan {
        font-family: 'Poppins', sans-serif;
        font-size: 0.74em;
        font-weight: 700;
        color: #0f0f1a;
        background: linear-gradient(135deg, #ff9800, #ffab40);
        padding: 3px 14px;
        border-radius: 20px;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3);
    }
    .dossier-body {
        display: grid;
        grid-template-columns: 230px 1fr;
        gap: 18px;
        padding: 16px 18px;
        align-items: start;
    }
    @media (max-width: 768px) {
        .dossier-body {
            grid-template-columns: 1fr;
        }
    }
    .dossier-left {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .dossier-photo-wrap {
        position: relative;
        width: 100%;
        aspect-ratio: 3/4;
        border-radius: 14px;
        overflow: hidden;
        border: 2px solid rgba(255, 152, 0, 0.45);
        background: #121222;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.45);
    }
    .dossier-photo-wrap img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }
    .dossier-id-chip {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.16);
        border-radius: 10px;
        padding: 6px 11px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 6px;
    }
    .chip-key {
        font-size: 0.66em;
        font-weight: 700;
        color: #ff9800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .chip-val {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78em;
        font-weight: 700;
        color: #ffd740;
        text-align: right;
        word-break: break-all;
    }
    .dossier-right {
        display: flex;
        flex-direction: column;
        gap: 9px;
    }
    .dossier-name-block {
        border-left: 3px solid #ff9800;
        padding-left: 11px;
    }
    .dossier-name {
        font-family: 'Poppins', sans-serif;
        font-size: 1.38em;
        font-weight: 700;
        color: #eceff1;
        line-height: 1.24;
        margin: 0 0 2px 0;
    }
    .dossier-subdept {
        font-size: 0.74em;
        font-weight: 600;
        color: #ffab40;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .dossier-stats-row {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 9px;
    }
    @media (max-width: 640px) {
        .dossier-stats-row {
            grid-template-columns: 1fr;
        }
    }
    .stat-cell {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.14);
        border-radius: 11px;
        padding: 8px 12px;
    }
    .stat-label {
        font-size: 0.66em;
        font-weight: 700;
        color: #ff9800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 2px;
    }
    .stat-value {
        font-size: 0.88em;
        color: #cfd8dc;
        line-height: 1.38;
        word-break: break-word;
    }
    .dossier-quotes-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 9px;
    }
    @media (max-width: 640px) {
        .dossier-quotes-grid {
            grid-template-columns: 1fr;
        }
    }
    .starlight-msg-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.15);
        border-left: 3px solid #ff9800;
        border-radius: 11px;
        padding: 9px 12px;
    }
    .starlight-msg-box.pesan-box {
        border-left-color: #ffd740;
    }
    .msg-head {
        font-size: 0.66em;
        font-weight: 700;
        color: #ff9800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 3px;
    }
    .starlight-msg-box.pesan-box .msg-head {
        color: #ffd740;
    }
    .msg-body {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 0.86em;
        color: #cfd8dc;
        line-height: 1.5;
    }

    /* ===== OPSI 2: CARD KATING KLASIK (2 KOLOM SEPERTI SEBELUMNYA) ===== */
    .profile-card {
        position: relative;
        background: linear-gradient(145deg, #161628, #1a1a30);
        border: 1px solid rgba(255, 171, 64, 0.2);
        border-radius: 18px;
        padding: 1.6rem 1.8rem;
        margin: 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
        transition: all 0.3s ease;
    }
    .profile-card:hover {
        border-color: rgba(255, 171, 64, 0.45);
        box-shadow: 0 12px 48px rgba(255, 152, 0, 0.15);
        transform: translateY(-2px);
    }
    [data-testid="stImage"] {
        border-radius: 18px !important;
        border: 2.5px solid rgba(255, 152, 0, 0.45) !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45) !important;
        overflow: hidden !important;
        transition: all 0.3s ease !important;
        background: #161628 !important;
        margin: 0 !important;
    }
    [data-testid="stImage"]:hover {
        border-color: #ff9800 !important;
        box-shadow: 0 12px 40px rgba(255, 152, 0, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    [data-testid="stImage"] img {
        border-radius: 16px !important;
        display: block !important;
        object-fit: cover !important;
        width: 100% !important;
    }
    .profile-header {
        margin-bottom: 1.2rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid rgba(255, 215, 64, 0.12);
    }
    .profile-name {
        font-family: 'Poppins', sans-serif;
        font-size: 1.55em;
        font-weight: 700;
        color: #eceff1;
        margin: 0 0 0.5rem 0;
        letter-spacing: 0.3px;
    }
    .profile-jabatan-badge {
        display: inline-block;
        background: linear-gradient(135deg, #ff9800, #ffab40);
        color: #0f0f1a;
        font-size: 0.78em;
        font-weight: 700;
        padding: 5px 16px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 2px 10px rgba(255, 152, 0, 0.3);
    }
    .info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 1rem;
    }
    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.12);
        border-radius: 12px;
        padding: 10px 14px;
        transition: all 0.2s ease;
    }
    .info-label {
        font-size: 0.7em;
        font-weight: 700;
        color: #ff9800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 3px;
    }
    .info-value {
        font-size: 0.92em;
        color: #cfd8dc;
        font-weight: 400;
        line-height: 1.4;
    }
    .info-box-full {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.12);
        border-radius: 12px;
        padding: 10px 14px;
        margin-bottom: 10px;
    }
    .quote-card {
        background: linear-gradient(145deg, #161628, #1a1a30);
        border: 1px solid rgba(255, 171, 64, 0.2);
        border-radius: 18px;
        padding: 1.2rem 1.4rem;
        margin-top: 14px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
    }
    .quote-card-header {
        font-family: 'Poppins', sans-serif;
        font-size: 0.85em;
        font-weight: 700;
        color: #ff9800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 6px;
        border-bottom: 1px solid rgba(255, 215, 64, 0.1);
        padding-bottom: 6px;
    }
    .quote-inner-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 215, 64, 0.12);
        border-left: 3px solid #ff9800;
        border-radius: 12px;
        padding: 10px 14px;
        margin-bottom: 10px;
    }
    .quote-label {
        font-size: 0.7em;
        font-weight: 700;
        color: #ff9800;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 4px;
    }
    .quote-text {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 0.88em;
        color: #cfd8dc;
        line-height: 1.55;
    }
    .card-separator {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 171, 64, 0.25), transparent);
        margin: 2.2rem 0;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <h1 class='kating-title'>BUKU KATING</h1>
    <p class='kating-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
    <div class='fancy-divider'></div>
</div>
""", unsafe_allow_html=True)


# ===== MENU UTAMA DEPARTEMEN (TEMA HITAM - OREN SEPERTI SEBELUMNYA) =====
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen MINBAK",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "6px 4px!important",
                "background-color": "#12121e",
                "border-radius": "12px",
                "border": "1px solid rgba(255, 171, 64, 0.25)",
                "box-shadow": "0 4px 20px rgba(0, 0, 0, 0.3)",
            },
            "icon": {"color": "#ffd740", "font-size": "17px"},
            "nav-link": {
                "font-size": "13px",
                "font-weight": "500",
                "text-align": "center",
                "margin": "2px",
                "color": "#cfd8dc",
                "--hover-color": "rgba(255, 171, 64, 0.15)",
                "border-radius": "8px",
            },
            "nav-link-selected": {
                "background-color": "#ff9800",
                "color": "#0f0f1a",
                "font-weight": "700",
                "box-shadow": "0 2px 10px rgba(255, 152, 0, 0.35)",
            },
        },
    )
    return selected


# ===== SUB-MENU DIVISI / KOMISI / BIRO (TEMA HITAM - OREN SEPERTI SEBELUMNYA) =====
def divisi_menu(options, dept_key):
    if len(options) <= 1:
        return options[0] if options else "Semua"

    selected_divisi = option_menu(
        menu_title=None,
        options=options,
        icons=["grid-fill"] + ["folder-fill"] * (len(options) - 1),
        orientation="horizontal",
        styles={
            "container": {
                "padding": "4px 2px!important",
                "background-color": "rgba(22, 22, 38, 0.7)",
                "border-radius": "10px",
                "border": "1px solid rgba(255, 215, 64, 0.2)",
                "margin": "1rem 0 1.2rem 0",
            },
            "icon": {"color": "#ffab40", "font-size": "14px"},
            "nav-link": {
                "font-size": "12.5px",
                "font-weight": "500",
                "text-align": "center",
                "margin": "2px 4px",
                "color": "#b0bec5",
                "--hover-color": "rgba(255, 215, 64, 0.15)",
                "border-radius": "6px",
            },
            "nav-link-selected": {
                "background-color": "#ffd740",
                "color": "#0f0f1a",
                "font-weight": "700",
            },
        },
        key=f"sub_divisi_{dept_key}",
    )
    return selected_divisi


_RAW_HTTP_CACHE = {}


def _extract_drive_id(url):
    if not url:
        return ""
    for pat in (r"[?&]id=([\w-]{10,})", r"/file/d/([\w-]{10,})", r"/d/([\w-]{10,})"):
        m = re.search(pat, str(url).strip())
        if m:
            return m.group(1)
    return ""


def _prefetch_raw_bytes(url):
    if not url or url in _RAW_HTTP_CACHE:
        return _RAW_HTTP_CACHE.get(url)
    gid = _extract_drive_id(url)
    candidates = [url]
    if gid:
        candidates = [
            f"https://drive.google.com/thumbnail?id={gid}&sz=w600",
            f"https://lh3.googleusercontent.com/d/{gid}=w600",
            url,
        ]
    headers = {"User-Agent": "Mozilla/5.0"}
    for cand in candidates:
        try:
            response = requests.get(cand, headers=headers, timeout=10)
            if response.status_code == 200 and response.content:
                if len(_RAW_HTTP_CACHE) >= 24: _RAW_HTTP_CACHE.clear()
                _RAW_HTTP_CACHE[url] = response.content
                return response.content
        except Exception:
            continue
    return None


try:
    from loading_screen import shared_kating_image_b64 as _shared_b64, shared_kating_image_pil as _shared_pil
except Exception:
    _shared_b64 = None
    _shared_pil = None


def load_image(url):
    if _shared_pil is not None:
        _RAW_HTTP_CACHE.pop(url, None)
        return _shared_pil(url)
    try:
        raw = _RAW_HTTP_CACHE.pop(url, None) or _prefetch_raw_bytes(url)
        _RAW_HTTP_CACHE.pop(url, None)
        if not raw:
            return None
        img = Image.open(BytesIO(raw))
        return ImageOps.exif_transpose(img).resize((280, 374))
    except Exception:
        return None


def load_image_b64(url):
    if _shared_b64 is not None:
        _RAW_HTTP_CACHE.pop(url, None)
        return _shared_b64(url)
    try:
        raw = _RAW_HTTP_CACHE.pop(url, None) or _prefetch_raw_bytes(url)
        _RAW_HTTP_CACHE.pop(url, None)
        if not raw:
            return ""
        img = Image.open(BytesIO(raw))
        img = ImageOps.exif_transpose(img).resize((280, 374))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=80, optimize=True)
        return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode('utf-8')}"
    except Exception:
        return ""


def _format_unit_label(divisi_raw, departemen_raw):
    """
    Pastikan label sub-unit sesuai badan/departemen:
    - Badan Legislatif (BALEG) -> Komisi (contoh: 'Komisi I Legislasi')
    - Badan Kesenatoran (BASON) -> Biro (contoh: 'Biro Aspirasi dan Media Komunikasi')
    - Departemen lainnya -> Divisi
    """
    div_clean = (divisi_raw or "").strip()
    dept_clean = (departemen_raw or "").strip()
    dept_low = dept_clean.lower()

    if not div_clean or div_clean == "-":
        if "baleg" in dept_low or "legislatif" in dept_low:
            return "PIMPINAN BADAN LEGISLATIF (BALEG)"
        if "bason" in dept_low or "kesenatoran" in dept_low or "senator" in dept_low:
            return "PIMPINAN BADAN KESENATORAN (BASON)"
        if "kesekjenan" in dept_low:
            return "BPH KESEKJENAN HMSD ADYATAMA"
        return f"PIMPINAN {dept_clean.upper()}" if dept_clean else "HMSD ADYATAMA ITERA 2026"

    div_low = div_clean.lower()
    if div_low.startswith("biro") or div_low.startswith("komisi") or div_low.startswith("divisi"):
        return div_clean.upper()

    if "baleg" in dept_low or "legislatif" in dept_low:
        return f"KOMISI {div_clean.upper()}"
    if "bason" in dept_low or "kesenatoran" in dept_low or "senator" in dept_low:
        return f"BIRO {div_clean.upper()}"

    return f"DIVISI {div_clean.upper()}"


def _build_sosmed_url(raw_sosmed: str) -> str:
    """Ubah @username menjadi link Instagram lengkap tanpa membebani performa."""
    s = (raw_sosmed or "").strip()
    if not s or s == "-":
        return ""
    if s.startswith("http://") or s.startswith("https://"):
        return s
    handle = s.split()[0].lstrip("@").strip("/")
    if not handle:
        return ""
    return f"https://www.instagram.com/{handle}/"


def display_images_with_data(gambar_urls, data_list, show_finished_message=True):
    if not data_list:
        return

    def esc(val):
        return str(val).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    # Jika mode "klasik" dipilih, gunakan tampilan 2 kolom seperti sebelumnya
    if GAYA_CARD_KATING == "klasik":
        images = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(_prefetch_raw_bytes, u) for u in gambar_urls]
            for i, url in enumerate(gambar_urls):
                with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
                    t0 = time.perf_counter()
                    futures[i].result()
                    images.append(load_image(url))
                    if time.perf_counter() - t0 < 0.04:
                        time.sleep(0.04)

        for i in range(len(data_list)):
            d = data_list[i]
            img = images[i] if i < len(images) else None

            nama = esc(d.get("nama", "-"))
            nim = esc(d.get("nim", "-"))
            umur = esc(d.get("umur", "-"))
            asal = esc(d.get("asal", "-"))
            alamat = esc(d.get("alamat", "-"))
            hobbi = esc(d.get("hobbi", "-"))
            raw_sosmed = d.get("sosmed", "-")
            sosmed = esc(raw_sosmed)
            sosmed_url = _build_sosmed_url(raw_sosmed)
            kesan = esc(d.get("kesan", "-"))
            pesan = esc(d.get("pesan", "-"))

            link_overlay = (
                f"<a class='dossier-card-link' href='{sosmed_url}' target='_blank' rel='noopener noreferrer' "
                f"title='Klik untuk membuka Instagram {sosmed}'></a>"
                if sosmed_url else ""
            )
            sosmed_display = f"{sosmed} ↗" if sosmed_url else sosmed

            quotes_html = (
                "<div class='quote-card'>"
                "<div class='quote-card-header'>💬 Kesan &amp; Pesan</div>"
                "<div class='quote-inner-box'>"
                "<div class='quote-label'>Kesan</div>"
                f"<div class='quote-text'>{kesan}</div>"
                "</div>"
                "<div class='quote-inner-box' style='margin-bottom: 0;'>"
                "<div class='quote-label'>Pesan</div>"
                f"<div class='quote-text'>{pesan}</div>"
                "</div>"
                "</div>"
            )

            card_html = (
                "<div class='profile-card'>"
                f"{link_overlay}"
                "<div class='profile-header'>"
                f"<div class='profile-name'>{nama}</div>"
                "</div>"
                "<div class='info-grid'>"
                f"<div class='info-box'><div class='info-label'>NIM</div><div class='info-value'>{nim}</div></div>"
                f"<div class='info-box'><div class='info-label'>Umur</div><div class='info-value'>{umur if umur == '-' else umur + ' Tahun'}</div></div>"
                f"<div class='info-box'><div class='info-label'>Asal</div><div class='info-value'>{asal}</div></div>"
                f"<div class='info-box'><div class='info-label'>Alamat</div><div class='info-value'>{alamat}</div></div>"
                "</div>"
                f"<div class='info-box-full'><div class='info-label'>Hobi</div><div class='info-value'>{hobbi}</div></div>"
                f"<div class='info-box-full sosmed-chip'><div class='info-label'>Sosial Media</div><div class='info-value' style='color:#ffd740;font-weight:600;'>{sosmed_display}</div></div>"
                "</div>"
            )

            col_foto, col_info = st.columns([1, 1.35], gap="medium")
            with col_foto:
                if img is not None:
                    st.image(img, use_container_width=True)
                else:
                    st.markdown("""
                    <div style='
                        width: 100%;
                        aspect-ratio: 3/4;
                        background: linear-gradient(135deg, #1a1a2e, #1f1f38);
                        border: 2px dashed rgba(255, 171, 64, 0.3);
                        border-radius: 14px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        color: #78909c;
                        font-size: 0.9em;
                    '>📷 Foto belum tersedia</div>
                    """, unsafe_allow_html=True)
                st.markdown(quotes_html, unsafe_allow_html=True)
            with col_info:
                st.markdown(card_html, unsafe_allow_html=True)

            if i < len(data_list) - 1:
                st.markdown("<div class='card-separator'></div>", unsafe_allow_html=True)

    else:
        # Mode "manjang": Card kating memanjang horizontal, warna serasi dengan header/menu departemen Hitam-Oren
        b64_images = []
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(_prefetch_raw_bytes, u) for u in gambar_urls]
            for i, url in enumerate(gambar_urls):
                with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
                    t0 = time.perf_counter()
                    futures[i].result()
                    b64_images.append(load_image_b64(url))
                    if time.perf_counter() - t0 < 0.04:
                        time.sleep(0.04)

        cards_batch = []
        for i in range(len(data_list)):
            d = data_list[i]
            b64_src = b64_images[i] if i < len(b64_images) else ""

            nama = esc(d.get("nama", "-"))
            jabatan = esc(d.get("jabatan", "Pengurus HMSD"))
            divisi = esc(d.get("divisi", ""))
            departemen = esc(d.get("departemen", ""))
            nim = esc(d.get("nim", "-"))
            umur = esc(d.get("umur", "-"))
            asal = esc(d.get("asal", "-"))
            alamat = esc(d.get("alamat", "-"))
            hobbi = esc(d.get("hobbi", "-"))
            raw_sosmed = d.get("sosmed", "-")
            sosmed = esc(raw_sosmed)
            sosmed_url = _build_sosmed_url(raw_sosmed)
            kesan = esc(d.get("kesan", "-"))
            pesan = esc(d.get("pesan", "-"))

            sub_div_text = _format_unit_label(divisi, departemen)
            idx_str = f"{i + 1:02d}"

            link_overlay = (
                f"<a class='dossier-card-link' href='{sosmed_url}' target='_blank' rel='noopener noreferrer' "
                f"title='Klik untuk membuka Instagram {sosmed}'></a>"
                if sosmed_url else ""
            )
            sosmed_display = f"{sosmed} ↗" if sosmed_url else sosmed

            if b64_src:
                photo_html = f"<img src='{b64_src}' alt='{nama}' loading='lazy' decoding='async'>"
            else:
                photo_html = (
                    "<div style='width:100%;height:100%;display:flex;align-items:center;"
                    "justify-content:center;color:#78909c;font-size:0.85em;'>📷 Foto belum tersedia</div>"
                )

            cards_batch.append(
                f"<div class='astral-dossier'>"
                f"{link_overlay}"
                f"<div class='dossier-topbar'>"
                f"<span class='dossier-index'>✦ PROFIL KATING #{idx_str}</span>"
                f"<span class='dossier-jabatan'>{jabatan}</span>"
                f"</div>"
                f"<div class='dossier-body'>"
                f"<div class='dossier-left'>"
                f"<div class='dossier-photo-wrap'>{photo_html}</div>"
                f"<div class='dossier-id-chip'><span class='chip-key'>NIM</span><span class='chip-val'>{nim}</span></div>"
                f"<div class='dossier-id-chip sosmed-chip'><span class='chip-key'>SOSMED</span><span class='chip-val'>{sosmed_display}</span></div>"
                f"</div>"
                f"<div class='dossier-right'>"
                f"<div class='dossier-name-block'>"
                f"<div class='dossier-name'>{nama}</div>"
                f"<div class='dossier-subdept'>{sub_div_text}</div>"
                f"</div>"
                f"<div class='dossier-stats-row'>"
                f"<div class='stat-cell'><div class='stat-label'>Umur</div><div class='stat-value'>{umur if umur == '-' else umur + ' Tahun'}</div></div>"
                f"<div class='stat-cell'><div class='stat-label'>Asal Daerah</div><div class='stat-value'>{asal}</div></div>"
                f"<div class='stat-cell'><div class='stat-label'>Hobi</div><div class='stat-value'>{hobbi}</div></div>"
                f"</div>"
                f"<div class='stat-cell'><div class='stat-label'>Alamat Domisili</div><div class='stat-value'>{alamat}</div></div>"
                f"<div class='dossier-quotes-grid'>"
                f"<div class='starlight-msg-box'><div class='msg-head'>💬 KESAN</div><div class='msg-body'>&ldquo;{kesan}&rdquo;</div></div>"
                f"<div class='starlight-msg-box pesan-box'><div class='msg-head'>✉️ PESAN</div><div class='msg-body'>&ldquo;{pesan}&rdquo;</div></div>"
                f"</div>"
                f"</div>"
                f"</div>"
                f"</div>"
            )

        st.markdown("".join(cards_batch), unsafe_allow_html=True)

    if show_finished_message and data_list:
        st.markdown(f"""
        <div style='
            text-align: center;
            color: #78909c;
            font-size: 0.85em;
            padding: 1rem 0;
            font-style: italic;
        '>✦ {len(data_list)} kating telah ditampilkan ✦</div>
        """, unsafe_allow_html=True)


menu = streamlit_menu()


# ========================================================================
# PENGAMBILAN & PENGELOLAAN DATA BUKU KATING
# ========================================================================
@st.cache_data(ttl=3600, max_entries=2, show_spinner=False)
def _load_json_data_cached(json_path: str, mtime: float):
    with open(json_path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def load_json_data():
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data/data_statis/data_anggota_hmsd_2026.json")
    if not os.path.exists(json_path):
        json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Data/Data_statis/data_anggota_hmsd_2026.json")
    return _load_json_data_cached(json_path, os.path.getmtime(json_path))

data_anggota = load_json_data()

# Mapping menu label -> departemen name di JSON
DEPT_MAP = {
    "Kesekjenan": "Kesekjenan",
    "Baleg": "Badan Legislatif (BALEG)",
    "Senator": "Badan Kesenatoran (BASON)",
    "Departemen PSDA": "Pengembangan Sumber Daya Anggota (PSDA)",
    "Departemen MIKFES": "Akademik dan Keprofesian (MIKFES)",
    "Departemen Eksternal": "Eksternal",
    "Departemen Internal": "Internal",
    "Departemen SSD": "Storage Sains Data (SSD)",
    "Departemen Medkraf": "Media Kreatif (MEDKRAF)",
    "Departemen MINBAK": "Minat dan Bakat (MINBAK)",
}

def jabatan_sort_key_pimpinan(member, menu_label):
    jab = member.get("jabatan", "").lower().strip()
    if "kesekjenan" in menu_label.lower():
        order = {
            "ketua himpunan": 1, "wakil ketua himpunan": 2,
            "sekretaris jendral": 3, "sekretaris jenderal": 3,
            "sekretaris": 4, "sekretaris 1": 4, "sekretaris 2": 5,
            "bendahara": 6, "bendahara 1": 6, "bendahara 2": 7
        }
        return order.get(jab, 10)
    elif "baleg" in menu_label.lower():
        order = {
            "ketua baleg": 1, "ketua badan legislatif": 1, "wakil ketua legislatif": 2,
            "sekretaris": 3, "sekretaris legislatif": 3, "bendahara legislatif": 4
        }
        return order.get(jab, 10)
    elif "senator" in menu_label.lower():
        order = {
            "senator": 1, "wakil senator": 2, "sekretaris senator": 3, "sekretaris": 3, "bendahara senator": 4
        }
        return order.get(jab, 10)
    else:
        order = {
            "kepala departement": 1, "kepala departemen": 1, "wakil kepala departemen": 2,
            "sekretaris departemen": 3, "sekretaris": 3, "sekretaris 1": 3, "sekretaris 2": 4,
            "bendahara departemen": 5, "bendahara": 5
        }
        return order.get(jab, 10)


def jabatan_sort_key_divisi(member):
    jab = member.get("jabatan", "").lower().strip()
    if "kepala divisi" in jab or "kepala komisi" in jab or "kepala biro" in jab:
        return 1
    if "wakil kepala divisi" in jab or "wakil kepala komisi" in jab or "wakil biro" in jab:
        return 2
    if "sekretaris divisi" in jab or "sekretaris komisi" in jab or "sekretaris biro" in jab:
        return 3
    if "staff ahli" in jab:
        return 4
    if "anggota" in jab or "staff" in jab:
        return 5
    return 6


def get_divisions_for_dept(menu_label):
    """
    Mengambil struktur divisi/komisi/biro dari departemen/badan yang dipilih.
    """
    dept_name = DEPT_MAP.get(menu_label, "")
    members = [m for m in data_anggota if m.get("departemen") == dept_name]
    has_pimpinan = any(not m.get("divisi", "").strip() for m in members)

    unique_divs = []
    for m in members:
        d = m.get("divisi", "").strip()
        if d and d not in unique_divs:
            unique_divs.append(d)

    if "baleg" in menu_label.lower():
        pimpinan_label = "Pimpinan Baleg"
    elif "senator" in menu_label.lower():
        pimpinan_label = "Pimpinan Senator"
    elif "kesekjenan" in menu_label.lower():
        pimpinan_label = "BPH Kesekjenan"
    else:
        pimpinan_label = "Pimpinan Departemen"

    return has_pimpinan, pimpinan_label, unique_divs


# ========================================================================
# DATA DINAMIS: foto massal, kesan, pesan unik per pemilik buku kating
# ========================================================================
PEMILIK = "Biwa"  # <-- GANTI SESUAI NAMA PEMILIK BUKU KATING INI

@st.cache_data(ttl=3600, max_entries=4, show_spinner=False)
def _load_dinamis_data_cached(dinamis_path: str, pemilik_nama: str, mtime: float):
    with open(dinamis_path, "r", encoding="utf-8-sig") as f:
        all_data = json.load(f)
    if isinstance(all_data, dict):
        all_data = [all_data]
    items = []
    for entry in all_data:
        if isinstance(entry, dict) and entry.get("pemilik", "").strip().lower() == pemilik_nama.strip().lower():
            items = entry.get("data", [])
            break
    if not items and len(all_data) == 1 and isinstance(all_data[0], dict) and "data" in all_data[0]:
        items = all_data[0].get("data", [])
    merged = {}
    for item in items:
        k = str(item.get("nama_kating", "")).strip().lower()
        if not k:
            continue
        if k not in merged:
            merged[k] = dict(item)
        else:
            for field in ("foto_massal_gdrive_id", "kesan", "pesan"):
                if not merged[k].get(field) and item.get(field):
                    merged[k][field] = item.get(field)
    return merged


def load_dinamis_data(pemilik_nama):
    dinamis_filename = pemilik_nama.lower().strip().replace(" ", "_") + ".json"
    base_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Data")
    dinamis_path = ""
    for sub in ("Data_dinamis", "data_dinamis"):
        d_dir = os.path.join(base_data, sub)
        if os.path.isdir(d_dir):
            cand = os.path.join(d_dir, dinamis_filename)
            if os.path.exists(cand):
                dinamis_path = cand
                break
            for fn in os.listdir(d_dir):
                if fn.lower() == dinamis_filename.lower():
                    dinamis_path = os.path.join(d_dir, fn)
                    break
        if dinamis_path:
            break
    if not dinamis_path or not os.path.exists(dinamis_path):
        return {}
    return _load_dinamis_data_cached(dinamis_path, pemilik_nama, os.path.getmtime(dinamis_path))

dinamis_map = load_dinamis_data(PEMILIK)


def build_data_for_dept(members):
    default_foto = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

    gambar_urls = []
    data_list = []

    for m in members:
        nama_asli = m.get("nama", "")
        nama_lower = nama_asli.lower().strip()
        mid = str(m.get('id', ''))
        dinamis = dinamis_map.get(nama_lower)
        if not dinamis and mid in dinamis_map:
            dinamis = dinamis_map[mid]
        if not dinamis:
            for k_name, k_data in dinamis_map.items():
                if len(k_name) >= 5 and (k_name in nama_lower or nama_lower.startswith(k_name)):
                    dinamis = k_data
                    break
        if not dinamis:
            dinamis = {}

        gdrive_id = dinamis.get("foto_massal_gdrive_id", "")
        if gdrive_id:
            foto_url = f"https://drive.google.com/uc?export=view&id={gdrive_id}"
        else:
            foto_url = default_foto
        gambar_urls.append(foto_url)

        hobi_list = m.get("hobi", [])
        hobi_str = ", ".join(hobi_list) if hobi_list else "-"

        data_list.append({
            "nama": nama_asli or "-",
            "jabatan": m.get("jabatan", "") or "-",
            "divisi": m.get("divisi", "") or "-",
            "departemen": m.get("departemen", "") or "-",
            "nim": m.get("nim", "") or "-",
            "umur": str(m.get("umur", "")) if m.get("umur") else "-",
            "asal": m.get("asal", "") or "-",
            "alamat": m.get("alamat", "") or "-",
            "hobbi": hobi_str,
            "sosmed": m.get("sosial_media", "") or "-",
            "kesan": dinamis.get("kesan", "") or m.get("kesan", "") or "-",
            "pesan": dinamis.get("pesan", "") or m.get("pesan", "") or "-",
        })

    return gambar_urls, data_list


def render_department_page(menu_label):
    """
    Merender halaman departemen/badan dengan struktur:
    - Baleg -> Komisi
    - Senator (Bason) -> Biro
    - Departemen -> Divisi
    """
    dept_name = DEPT_MAP.get(menu_label, "")
    dept_members = [m for m in data_anggota if m.get("departemen") == dept_name]
    has_pimpinan, pimpinan_label, unique_divs = get_divisions_for_dept(menu_label)

    def get_cat_icon(cat_name):
        cat_lower = cat_name.lower()
        if "pimpinan" in cat_lower or "bph" in cat_lower:
            return "🏛️ "
        if "komisi" in cat_lower or "legislasi" in cat_lower:
            return "📜 "
        if "biro" in cat_lower:
            return "📁 "
        if "wirausaha" in cat_lower or "bisnis" in cat_lower:
            return "💼 "
        if "mitra" in cat_lower:
            return "🤝 "
        if "kader" in cat_lower or "psda" in cat_lower or "mutu" in cat_lower:
            return "🌱 "
        if "kreatif" in cat_lower or "media" in cat_lower or "desain" in cat_lower:
            return "🎨 "
        if "bakat" in cat_lower or "minat" in cat_lower or "olahraga" in cat_lower:
            return "🏆 "
        if "riset" in cat_lower or "research" in cat_lower or "akademik" in cat_lower:
            return "🔬 "
        if "eksternal" in cat_lower or "luar" in cat_lower or "masyarakat" in cat_lower:
            return "🌐 "
        if "internal" in cat_lower or "harmonis" in cat_lower or "rohani" in cat_lower:
            return "✨ "
        return "📂 "

    all_label = "Semua"
    if unique_divs:
        if "baleg" in menu_label.lower():
            all_label = "Semua Komisi"
        elif "senator" in menu_label.lower():
            all_label = "Semua Biro"
        else:
            all_label = "Semua Divisi"

        divisi_options = [all_label]
        if has_pimpinan:
            divisi_options.append(pimpinan_label)
        divisi_options.extend(unique_divs)

        selected_cat = divisi_menu(divisi_options, menu_label)
    else:
        selected_cat = all_label

    if not unique_divs:
        pim_members = [m for m in dept_members if not m.get("divisi", "").strip()]
        pim_members.sort(key=lambda m: jabatan_sort_key_pimpinan(m, menu_label))
        urls, data_items = build_data_for_dept(pim_members)
        display_images_with_data(urls, data_items, show_finished_message=True)
        return

    categories_to_show = []
    if selected_cat == all_label:
        if has_pimpinan:
            categories_to_show.append((pimpinan_label, True))
        for d in unique_divs:
            categories_to_show.append((d, False))
    elif selected_cat == pimpinan_label:
        categories_to_show.append((pimpinan_label, True))
    else:
        categories_to_show.append((selected_cat, False))

    for idx, (cat_name, is_pimpinan) in enumerate(categories_to_show):
        if is_pimpinan:
            members = [m for m in dept_members if not m.get("divisi", "").strip()]
            members.sort(key=lambda m: jabatan_sort_key_pimpinan(m, menu_label))
        else:
            members = [m for m in dept_members if m.get("divisi", "").strip() == cat_name]
            members.sort(key=jabatan_sort_key_divisi)

        if not members:
            continue

        icon = get_cat_icon(cat_name)
        st.markdown(f"""
        <div class='division-banner'>
            <span class='division-banner-title'>{icon}{cat_name}</span>
            <span class='division-banner-badge'>{len(members)} Anggota</span>
        </div>
        """, unsafe_allow_html=True)

        urls, data_items = build_data_for_dept(members)
        is_last = (idx == len(categories_to_show) - 1)
        display_images_with_data(urls, data_items, show_finished_message=is_last)


# ===== RENDER BERDASARKAN MENU YANG DIPILIH =====

if menu == "Kesekjenan":
    def kesekjenan():
        render_department_page("Kesekjenan")
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        render_department_page("Baleg")
    baleg()

elif menu == "Senator":
    def senator():
        render_department_page("Senator")
    senator()

elif menu == "Departemen PSDA":
    def psda():
        render_department_page("Departemen PSDA")
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        render_department_page("Departemen MIKFES")
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        render_department_page("Departemen Eksternal")
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        render_department_page("Departemen Internal")
    internal()

elif menu == "Departemen SSD":
    def ssd():
        render_department_page("Departemen SSD")
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        render_department_page("Departemen Medkraf")
    medkraf()

elif menu == "Departemen MINBAK":
    def minbak():
        render_department_page("Departemen MINBAK")
    minbak()
