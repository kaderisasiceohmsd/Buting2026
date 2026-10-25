import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import base64
import re

# Cek preloaded cache dari loading_screen
try:
    from loading_screen import get_cached_bytes as _get_cached
except ImportError:
    _get_cached = lambda url: None


def _extract_drive_id(url: str) -> str:
    if not url:
        return ""
    for pat in (r"[?&]id=([\w-]{10,})", r"/file/d/([\w-]{10,})", r"/d/([\w-]{10,})"):
        m = re.search(pat, url.strip())
        if m:
            return m.group(1)
    return ""


# JANGAN DIUBAH
@st.cache_data(ttl=3600, max_entries=32, show_spinner=False)
def _load_image_valid(url: str):
    cached = _get_cached(url)
    if cached:
        try:
            img = Image.open(BytesIO(cached))
            return ImageOps.exif_transpose(img)
        except Exception:
            pass
    gid = _extract_drive_id(url)
    candidates = [url]
    if gid:
        candidates = [
            f"https://drive.google.com/uc?export=view&id={gid}",
            f"https://drive.google.com/thumbnail?id={gid}&sz=w800",
            f"https://lh3.googleusercontent.com/d/{gid}=w800",
            url,
        ]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for cand in candidates:
        try:
            response = requests.get(cand, headers=headers, timeout=10)
            if response.status_code == 200 and response.content:
                img = Image.open(BytesIO(response.content))
                return ImageOps.exif_transpose(img)
        except Exception:
            continue
    raise ValueError("Image load failed")


def load_image(url):
    try:
        return _load_image_valid(url)
    except Exception:
        return None


@st.cache_data(ttl=3600, max_entries=32, show_spinner=False)
def get_image_base64(url, max_dim=420, _v=2):
    """Ambil gambar, perkecil dimensi & kompres agar sangat ringan saat deploy Streamlit (mendukung HEIC/RAW Drive)."""
    if not url or not url.strip():
        return ""
    url = url.strip()
    raw_candidates = []
    cached = _get_cached(url)
    if cached:
        raw_candidates.append(cached)

    gid = _extract_drive_id(url)
    sz = max(600, int(max_dim))
    url_candidates = [url]
    if gid:
        # Prioritaskan endpoint thumbnail/lh3 karena otomatis mengonversi foto HEIC (iPhone) ke JPEG standar
        url_candidates = [
            f"https://drive.google.com/thumbnail?id={gid}&sz=w{sz}",
            f"https://lh3.googleusercontent.com/d/{gid}=w{sz}",
            f"https://drive.google.com/uc?export=view&id={gid}",
        ]

    headers = {"User-Agent": "Mozilla/5.0"}
    for raw in raw_candidates:
        try:
            img = Image.open(BytesIO(raw))
            img = ImageOps.exif_transpose(img)
            img.thumbnail((max_dim, max_dim), Image.LANCZOS)
            buf = BytesIO()
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img = img.convert("RGBA")
                img.save(buf, format="PNG", optimize=True)
                img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
                return f"data:image/png;base64,{img_b64}"
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(buf, format="JPEG", quality=85, optimize=True)
            img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"data:image/jpeg;base64,{img_b64}"
        except Exception:
            continue

    for cand in url_candidates:
        try:
            response = requests.get(cand, headers=headers, timeout=10)
            if response.status_code != 200:
                continue
            img = Image.open(BytesIO(response.content))
            img = ImageOps.exif_transpose(img)
            img.thumbnail((max_dim, max_dim), Image.LANCZOS)
            buf = BytesIO()
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img = img.convert("RGBA")
                img.save(buf, format="PNG", optimize=True)
                img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
                return f"data:image/png;base64,{img_b64}"
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(buf, format="JPEG", quality=85, optimize=True)
            img_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"data:image/jpeg;base64,{img_b64}"
        except Exception:
            continue

    return url


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")

# JANGAN DIUBAH


# Ambil nama mentor & daftar konstelasi dari session_state (dikirim dari main.py)
NAMA_MENTOR = st.session_state.get("nama_mentor_utama", "Kak Yollanda Agustina")
DAFTAR_KONSTELASI = st.session_state.get("daftar_konstelasi", [])

# ===== CSS DESAIN ORISINAL JORDAN: STELLAR FANTASY (ORV x LOTM) =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Poppins:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&family=Playfair+Display:ital,wght@0,500;0,700;1,400&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
    }

    /* Expand Streamlit block container width and center it properly */
    .main .block-container,
    [data-testid="stMainBlockContainer"],
    [data-testid="stAppViewBlockContainer"] {
        max-width: 1100px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 1.5rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        width: 100% !important;
    }

    /* ===== 1. HERO HEADER PALING ATAS (WEBSITE KATING) - 100% PRESISI TENGAH ===== */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        max-width: 900px;
        margin: 0 auto;
        padding: 0.4rem 1rem 0.6rem 1rem;
    }
    .hero-container [data-testid="stHeaderActionElements"] {
        display: none !important;
    }
    .hero-title {
        font-family: 'Cinzel', 'Poppins', serif;
        font-size: 3.6em;
        font-weight: 800;
        line-height: 1.15;
        text-align: center !important;
        margin: 0 auto !important;
        padding-left: 4px; /* Kompensasi letter-spacing 4px agar presisi di tengah */
        width: 100%;
        display: block;
        background: linear-gradient(135deg, #fff6d6 0%, #ffd740 45%, #ffab40 80%, #ff6e40 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 4px;
        filter: drop-shadow(0 4px 18px rgba(255, 215, 64, 0.22));
    }
    .hero-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.12em;
        color: #b0bec5;
        font-weight: 400;
        letter-spacing: 2.5px;
        padding-left: 2.5px; /* Kompensasi letter-spacing 2.5px agar presisi di tengah */
        text-transform: uppercase;
        margin: 0.3rem auto 0 auto !important;
        text-align: center !important;
        width: 100%;
        display: block;
    }

    /* ===== 2. ASTRAL STATUS BAR (DI BAWAH LOGO HMSD & PSDA) ===== */
    .star-stream-bar {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 8px;
        margin: 0.9rem auto 0.4rem auto;
        max-width: 880px;
    }
    .stream-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 13px;
        background: rgba(11, 13, 28, 0.88);
        border: 1px solid rgba(255, 215, 64, 0.35);
        border-radius: 6px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.71em;
        font-weight: 600;
        color: #ffd740;
        letter-spacing: 1px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }
    .stream-pill.sponsor {
        border-color: rgba(128, 216, 255, 0.45);
        color: #80d8ff;
        background: rgba(10, 18, 34, 0.9);
    }

    /* ===== 3. ASTRAL DIVIDER (COMPACT) ===== */
    .astral-divider {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin: 1.1rem auto;
        max-width: 520px;
    }
    .astral-divider-line {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 215, 64, 0.55), transparent);
    }
    .astral-divider-symbol {
        color: #ffd740;
        font-size: 0.9em;
        letter-spacing: 4px;
    }

    /* ===== 4. MONUMENTAL ASTRAL OBSERVATORY (DESKRIPSI & FOTO KELOMPOK) ===== */
    .jordan-monument {
        position: relative;
        max-width: 940px;
        margin: 1.1rem auto 1.8rem auto;
        background: linear-gradient(165deg, rgba(14, 16, 34, 0.96) 0%, rgba(8, 9, 20, 0.98) 100%);
        border: 1px solid rgba(255, 215, 64, 0.38);
        border-radius: 16px;
        box-shadow: 0 18px 48px rgba(0, 0, 0, 0.72), inset 0 0 0 1px rgba(255, 215, 64, 0.08);
        overflow: hidden;
    }
    .monument-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
        padding: 9px 18px;
        background: linear-gradient(90deg, rgba(255, 215, 64, 0.14), rgba(15, 17, 35, 0.9), rgba(128, 216, 255, 0.12));
        border-bottom: 1px solid rgba(255, 215, 64, 0.28);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72em;
        color: #ffd740;
        letter-spacing: 1.2px;
    }
    .monument-topbar-right {
        color: #80d8ff;
        font-weight: 600;
    }
    .monument-photo-frame {
        position: relative;
        padding: 14px 14px 0 14px;
    }
    .monument-photo-frame img {
        width: 100%;
        height: auto;
        max-height: 620px;
        object-fit: cover;
        object-position: center top;
        border-radius: 10px;
        border: 1px solid rgba(255, 215, 64, 0.35);
        display: block;
    }
    .monument-body {
        padding: 1.3rem 1.8rem 1.5rem 1.8rem;
    }
    .monument-kicker {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72em;
        color: #80d8ff;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 3px;
        text-align: center;
    }
    .monument-heading {
        font-family: 'Cinzel', 'Poppins', serif;
        font-size: 1.95em;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        margin: 0 0 0.75rem 0;
        letter-spacing: 1px;
    }
    .monument-heading span {
        color: #ffd740;
    }
    .monument-desc {
        font-size: 0.94em;
        line-height: 1.75;
        color: #cfd8dc;
        text-align: center;
        max-width: 820px;
        margin: 0 auto 1.2rem auto;
    }
    .monument-pillars {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        border-top: 1px solid rgba(255, 215, 64, 0.18);
        padding-top: 1rem;
    }
    .pillar-box {
        background: rgba(255, 255, 255, 0.025);
        border: 1px solid rgba(255, 215, 64, 0.2);
        border-radius: 10px;
        padding: 10px 12px;
        text-align: center;
    }
    .pillar-val {
        font-family: 'Cinzel', serif;
        font-size: 1.15em;
        font-weight: 800;
        color: #ffd740;
        margin-bottom: 2px;
    }
    .pillar-lbl {
        font-size: 0.74em;
        color: #90a4ae;
        letter-spacing: 0.4px;
    }
    @media (max-width: 700px) {
        .monument-pillars {
            grid-template-columns: 1fr;
        }
    }

    /* ===== 5. SECTION TITLES ===== */
    .section-title {
        text-align: center;
        font-family: 'Cinzel', 'Poppins', serif;
        font-size: 1.85em;
        font-weight: 800;
        margin: 1.1rem 0 0.2rem 0;
        background: linear-gradient(90deg, #fff3c4, #ffd740, #ffab40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 1.5px;
    }
    .section-desc {
        text-align: center;
        color: #90a4ae;
        font-size: 0.9em;
        margin-bottom: 1rem;
    }

    /* ===== 6. KRONIK RASI BINTANG (CONSTELLATION CHRONICLES) ===== */
    .chronicle-card {
        background: linear-gradient(160deg, #111328 0%, #090a16 100%);
        border: 1px solid rgba(255, 215, 64, 0.28);
        border-radius: 14px;
        overflow: hidden;
        margin-bottom: 0.9rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.55);
        transition: transform 0.28s ease, border-color 0.28s ease;
        display: flex;
        flex-direction: column;
    }
    .chronicle-card:hover {
        transform: translateY(-3px);
        border-color: rgba(255, 215, 64, 0.72);
    }
    .chronicle-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 12px;
        background: rgba(255, 215, 64, 0.08);
        border-bottom: 1px solid rgba(255, 215, 64, 0.2);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.67em;
        color: #ffd740;
        letter-spacing: 1.4px;
        text-transform: uppercase;
    }
    .chronicle-visual {
        position: relative;
        width: 100%;
        aspect-ratio: 16/10;
        overflow: hidden;
        background: radial-gradient(circle at 50% 40%, #1d1b3f 0%, #0b0c1a 100%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .chronicle-visual img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center 25%;
        display: block;
    }
    .chronicle-constellation-art {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 5px;
        padding: 0.8rem;
        text-align: center;
    }
    .chronicle-body {
        padding: 10px 13px 12px 13px;
        border-top: 1px solid rgba(255, 255, 255, 0.06);
    }
    .chronicle-title {
        font-family: 'Poppins', sans-serif;
        font-size: 0.98em;
        font-weight: 700;
        color: #ffffff;
        margin: 0 0 3px 0;
    }
    .chronicle-desc {
        font-size: 0.78em;
        color: #b0bec5;
        line-height: 1.45;
        margin: 0;
    }

    /* ===== 7. PRASASTI PUISI (SACRED STARLIGHT SCROLL) ===== */
    .puisi-scroll {
        position: relative;
        max-width: 740px;
        margin: 1.6rem auto;
        padding: 1.8rem 2.2rem;
        background: linear-gradient(180deg, rgba(16, 17, 36, 0.96) 0%, rgba(10, 11, 24, 0.98) 100%);
        border: 1px solid rgba(255, 215, 64, 0.38);
        border-radius: 16px;
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65);
        text-align: center;
    }
    .puisi-scroll-crest {
        display: inline-block;
        padding: 4px 15px;
        border: 1px solid rgba(255, 215, 64, 0.45);
        border-radius: 20px;
        background: rgba(255, 215, 64, 0.08);
        color: #ffd740;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.68em;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .puisi-text {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.02em;
        line-height: 1.9;
        color: #e2e8f0;
        text-align: center;
    }
    .puisi-author {
        text-align: center;
        color: #ffd740;
        font-weight: 700;
        margin-top: 1.1rem;
        font-size: 0.86em;
        letter-spacing: 1px;
    }

    /* ===== 8. ASTRAL CODEX (DAFTAR 10 KELOMPOK) ===== */
    .codex-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-top: 0.5rem;
    }
    .codex-item {
        background: rgba(13, 15, 30, 0.92);
        border: 1px solid rgba(255, 215, 64, 0.22);
        border-radius: 10px;
        padding: 9px 13px;
    }
    .codex-head {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2px;
    }
    .codex-name {
        font-weight: 700;
        font-size: 0.9em;
        color: #ffffff;
    }
    .codex-title {
        font-size: 0.74em;
        font-style: italic;
        color: #ffd740;
        margin-bottom: 3px;
    }
    .codex-desc {
        font-size: 0.77em;
        color: #b0bec5;
        line-height: 1.42;
    }
    @media (max-width: 700px) {
        .codex-grid {
            grid-template-columns: 1fr;
        }
    }

    /* ===== 9. JORDAN CELESTIAL ID CARD (COMPACT & RAPAT) ===== */
    .team-row-2 {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        align-items: stretch !important;
        gap: 18px !important;
        width: 100% !important;
        max-width: 660px !important;
        margin: 0.5rem auto 1rem auto !important;
        position: relative !important;
        z-index: 2 !important;
    }
    .team-row-2 .flip-card {
        width: 300px !important;
        max-width: 300px !important;
        margin: 0 !important;
        flex: 0 0 300px !important;
    }

    .team-row-grid {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 18px !important;
        width: 100% !important;
        max-width: 980px !important;
        margin: 0.5rem auto 1.2rem auto !important;
        position: relative !important;
        z-index: 2 !important;
    }
    .team-row-grid .flip-card {
        width: 300px !important;
        max-width: 300px !important;
        margin: 0 !important;
        flex: 0 0 300px !important;
    }

    .flip-card {
        background-color: transparent;
        width: 300px;
        height: 375px;
        perspective: 1200px;
        cursor: pointer;
        outline: none;
        user-select: none;
        position: relative;
        z-index: 2;
    }
    .flip-card:hover,
    .flip-card:focus-within {
        z-index: 40 !important;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.65s cubic-bezier(0.34, 1.2, 0.64, 1);
        transform-style: preserve-3d;
        border-radius: 14px;
    }
    .flip-card:hover .flip-card-inner,
    .flip-card:focus-within .flip-card-inner {
        transform: rotateY(180deg);
    }
    .flip-card-link {
        position: absolute;
        inset: 0;
        z-index: 25;
        cursor: pointer;
        text-decoration: none !important;
        border-radius: 14px;
    }
    .flip-card:hover .jback-footer {
        color: #ffd740;
        background: rgba(255, 215, 64, 0.12);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 14px;
        box-sizing: border-box;
        overflow: hidden;
    }

    /* SISI DEPAN */
    .flip-card-front {
        background: #0b0c1b;
        border: 1.5px solid rgba(255, 215, 64, 0.42);
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.75);
        display: flex;
        flex-direction: column;
    }
    .flip-card:hover .flip-card-front {
        border-color: #ffd740;
    }
    .jcard-topstrip {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 12px;
        background: rgba(10, 11, 24, 0.95);
        border-bottom: 1px solid rgba(255, 215, 64, 0.28);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65em;
        color: #ffd740;
        letter-spacing: 1px;
        z-index: 3;
    }
    .jcard-photo-box {
        position: relative;
        flex: 1;
        width: 100%;
        overflow: hidden;
        background: #101226;
    }
    .jcard-photo-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }
    .flip-card:hover .jcard-photo-box img {
        transform: scale(1.04);
    }
    .jcard-front-footer {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        background: linear-gradient(to top, rgba(8, 9, 20, 0.98) 0%, rgba(8, 9, 20, 0.85) 58%, transparent 100%);
        padding: 1.6rem 0.9rem 0.75rem 0.9rem;
        text-align: center;
        z-index: 2;
    }
    .jcard-front-name {
        font-family: 'Poppins', sans-serif;
        font-size: 1.02em;
        font-weight: 800;
        color: #ffffff;
        margin: 0 0 5px 0;
        line-height: 1.22;
    }
    .jcard-role-tag {
        display: inline-block;
        padding: 2.5px 12px;
        border-radius: 5px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.64em;
        font-weight: 700;
        letter-spacing: 1.4px;
        text-transform: uppercase;
    }
    .role-pimpinan {
        background: linear-gradient(135deg, #ffd740, #ff9800);
        color: #090a14;
    }
    .role-anggota {
        background: rgba(128, 216, 255, 0.14);
        border: 1px solid rgba(128, 216, 255, 0.5);
        color: #80d8ff;
    }
    .jcard-flip-prompt {
        margin-top: 5px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58em;
        color: rgba(255, 215, 64, 0.78);
        letter-spacing: 1.2px;
    }

    /* SISI BELAKANG (MARGIN RAPAT & PROPORSIONAL) */
    .flip-card-back {
        transform: rotateY(180deg);
        background: linear-gradient(160deg, #13152c 0%, #090a16 100%);
        border: 1.5px solid rgba(255, 215, 64, 0.6);
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.85);
        padding: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-align: left;
    }
    .jback-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 12px;
        background: rgba(255, 215, 64, 0.12);
        border-bottom: 1px solid rgba(255, 215, 64, 0.28);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.64em;
        color: #ffd740;
        letter-spacing: 1px;
    }
    .jback-content {
        padding: 12px 13px;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .jback-identity {
        border-left: 3px solid #ffd740;
        padding-left: 9px;
        margin: 0;
    }
    .jback-bottom-group {
        display: flex;
        flex-direction: column;
        gap: 6px;
        margin-top: auto;
    }
    .jback-name {
        font-size: 1.02em;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.22;
        margin-bottom: 3px;
    }
    .jback-role {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.65em;
        color: #80d8ff;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .jback-field {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 215, 64, 0.2);
        border-radius: 8px;
        padding: 6px 10px;
        margin: 0;
    }
    .jback-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58em;
        font-weight: 700;
        color: #ffd740;
        letter-spacing: 1.1px;
        text-transform: uppercase;
        margin-bottom: 1px;
    }
    .jback-val {
        font-size: 0.77em;
        color: #e2e8f0;
        line-height: 1.34;
        word-break: break-word;
    }
    .jback-nim {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.85em;
        font-weight: 700;
        color: #80d8ff;
    }
    .jback-motto {
        font-style: italic;
        color: #ffe082;
    }
    .jback-footer {
        padding: 5px 12px;
        background: rgba(0, 0, 0, 0.35);
        border-top: 1px solid rgba(255, 255, 255, 0.06);
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.58em;
        color: #90a4ae;
        letter-spacing: 1px;
    }

    /* Tier Divider Headers (COMPACT) */
    .about-tier-header {
        text-align: center;
        margin: 0.8rem auto 0.5rem auto;
        max-width: 620px;
    }
    .tier-badge {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75em;
        font-weight: 700;
        letter-spacing: 1.8px;
        text-transform: uppercase;
        color: #ffd740;
        background: rgba(255, 215, 64, 0.1);
        border: 1px solid rgba(255, 215, 64, 0.4);
        border-radius: 7px;
        padding: 0.3rem 1.1rem;
        margin-bottom: 0.25rem;
    }
    .tier-sub {
        font-size: 0.83em;
        color: #90a4ae;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# ===== 1. PALING ATAS: JUDUL WEBSITE KATING =====
st.markdown("""
<div class='hero-container'>
    <div class='hero-title'>WEBSITE KATING</div>
    <p class='hero-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
</div>
""", unsafe_allow_html=True)

# ===== 2. SETELAHNYA: LOGO HIMPUNAN & LOGO PSDA =====
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


@st.cache_data(ttl=3600, max_entries=8, show_spinner=False)
def get_logo_png_base64(url: str, max_dim: int = 900, _v: int = 2) -> str:
    """Muat logo resolusi tinggi sebagai PNG asli tanpa mengubah warna sedikit pun."""
    gid = _extract_drive_id(url)
    candidates = [url]
    if gid:
        candidates = [
            f"https://drive.google.com/uc?export=view&id={gid}",
            f"https://drive.google.com/thumbnail?id={gid}&sz=w1200",
            f"https://lh3.googleusercontent.com/d/{gid}=w1200",
        ]
    headers = {"User-Agent": "Mozilla/5.0"}
    for cand in candidates:
        try:
            resp = requests.get(cand, headers=headers, timeout=10)
            if resp.status_code == 200 and resp.content:
                img = Image.open(BytesIO(resp.content))
                img = ImageOps.exif_transpose(img).convert("RGBA")
                img.thumbnail((max_dim, max_dim), Image.LANCZOS)
                buf = BytesIO()
                img.save(buf, format="PNG", optimize=True)
                return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
        except Exception:
            continue
    return ""


def layout(url):
    b64 = get_logo_png_base64(url, max_dim=900, _v=2)
    if b64:
        st.markdown(
            f"""
            <div style='display: flex; justify-content: center; align-items: center; width: 100%; margin: 0.5rem auto;'>
                <img src='{b64}' style='max-width: 260px; width: 100%; height: auto; display: block; margin: 0 auto; border-radius: 16px; filter: drop-shadow(0 8px 22px rgba(0,0,0,0.45));'>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        col1, col2, col3 = st.columns([1.2, 1, 1.2])
        with col2:
            img = load_image(url)
            if img is not None:
                st.image(img, use_container_width=True)

layout(url)
layout(url1)

# ===== 3. DI BAWAH LOGO: ASTRAL STATUS BAR & DIVIDER =====
st.markdown(f"""
<div class='star-stream-bar'>
    <span class='stream-pill'>✦ KONSTELASI JORDAN</span>
    <span class='stream-pill sponsor'>★ MENTOR PEMBIMBING : {NAMA_MENTOR.upper()}</span>
    <span class='stream-pill'>◈ Stellar : 13 ANGGOTA</span>
</div>
<div class='astral-divider'>
    <div class='astral-divider-line'></div>
    <div class='astral-divider-symbol'>✦ ◈ ✦</div>
    <div class='astral-divider-line'></div>
</div>
""", unsafe_allow_html=True)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "people"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "5px!important",
                "background-color": "rgba(12, 14, 28, 0.9)",
                "border": "1px solid rgba(255, 215, 64, 0.3)",
                "border-radius": "12px",
            },
            "icon": {"color": "#ffd740", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px 4px",
                "color": "#cfd8dc",
                "border-radius": "8px",
                "--hover-color": "rgba(255,215,64,0.1)",
            },
            "nav-link-selected": {
                "background-color": "#ffd740",
                "color": "#090a14",
                "font-weight": "700",
            },
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1gQp5E_KYHBfFOEepR_Ccxn4tj_VHaNxr"
        foto_kelompok_b64 = get_image_base64(foto_kelompok, max_dim=960)

        # ─── 1. MONUMENTAL ASTRAL OBSERVATORY (DESKRIPSI & FOTO KELOMPOK) ───
        st.markdown(f"""
        <div class='jordan-monument'>
            <div class='monument-topbar'>
                <span>✦ OBSERVATORIUM ASTRAL // KONSTELASI JORDAN</span>
                <span class='monument-topbar-right'>MENTOR: {NAMA_MENTOR.upper()}</span>
            </div>
            <div class='monument-photo-frame'>
                <img src='{foto_kelompok_b64}' alt='Foto Konstelasi Jordan'>
            </div>
            <div class='monument-body'>
                <div class='monument-kicker'>✦ Tiga Belas Bintang, Satu Narasi ✦</div>
                <h2 class='monument-heading'>Kami Adalah <span>JORDAN</span></h2>
                <div class='monument-desc'>
                    Nama konstelasi kami diambil dari dua tokoh besar Sains Data: <b>Wilhelm Jordan</b> (Eliminasi Gauss-Jordan) dan <b>Michael I. Jordan</b> (pelopor Machine Learning dan <i>Jordan Recurrent Neural Network</i>). Jaringan Jordan belajar dari hasil sebelumnya, dan itu yang ingin kami tiru. Kami <b>13 anggota</b> di bawah bimbingan <b>{NAMA_MENTOR}</b>, saling belajar dan berkembang bareng.
                </div>
                <div class='monument-pillars'>
                    <div class='pillar-box'>
                        <div class='pillar-val'>13 Anggota</div>
                        <div class='pillar-lbl'>Tiga belas orang, satu orbit</div>
                    </div>
                    <div class='pillar-box'>
                        <div class='pillar-val'>2 Revolusi Sains Data</div>
                        <div class='pillar-lbl'>Aljabar Linier dan Jaringan Saraf</div>
                    </div>
                    <div class='pillar-box'>
                        <div class='pillar-val'>{NAMA_MENTOR}</div>
                        <div class='pillar-lbl'>Mentor yang memandu Konstelasi Jordan</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ─── 2. KRONIK RASI BINTANG (6 FRAGMEN PERJALANAN JORDAN) ───
        st.markdown("<h2 class='section-title'>✦ Kronik Konstelasi Jordan ✦</h2>", unsafe_allow_html=True)
        st.markdown("<p class='section-desc'>Enam bab perjalanan kami sejauh ini.</p>", unsafe_allow_html=True)

        galeri_momen = [
            {
                "label": "CHRONICLE I",
                "koordinat": "RA 01h 13m",
                "judul": "Titik Awal Konstelasi",
                "deskripsi": "Pertama kalinya tiga belas orang dari latar belakang berbeda dipertemukan dalam satu konstelasi bernama 'Jordan'.",
                "foto": "https://drive.google.com/uc?export=view&id=1X_fo_krBxF4izzlksjOWPBfdcqnkuTyx",
            },
            {
                "label": "CHRONICLE II",
                "koordinat": "RA 03h 42m",
                "judul": "Langkah Penjelajahan",
                "deskripsi": "Nyelesain Tugas Bareng, Capek Bareng DLl.",
                "foto": "https://drive.google.com/uc?export=view&id=1w8iZCZh6xh93viKSvY2XOG26iFnmr08p",
            },
            {
                "label": "CHRONICLE III",
                "koordinat": "RA 07h 19m",
                "judul": "Tumbuh Dalam Feedback",
                "deskripsi": "Seperti Jordan Network, setiap evaluasi dan masukan kami pakai untuk jadi lebih baik.",
                "foto": "https://drive.google.com/uc?export=view&id=1rb2GM4vobHQj0R3QyUWLvhBU3DaDUAyk",
            },
            {
                "label": "CHRONICLE IV",
                "koordinat": "RA 11h 05m",
                "judul": "Harmoni Satu Data",
                "deskripsi": "Ide, kode, dan kreativitas digabung sampai jadi karya yang bikin bangga.",
                "foto": "https://drive.google.com/uc?export=view&id=1RZiQ5NwIoeKRqsZ8HFK7lDYgFjxlfA9a",
            },
            {
                "label": "CHRONICLE V",
                "koordinat": "RA 16h 28m",
                "judul": "Tawa di Balik Layar",
                "deskripsi": "Di sela tugas dan tenggat, selalu ada cerita seru yang bikin kami makin akrab.",
                "foto": "https://drive.google.com/uc?export=view&id=12LeaQ2LaV5xOnKrfps5UWkVJdwWlw7wr",
            },
            {
                "label": "CHRONICLE VI",
                "koordinat": "RA 23h 59m",
                "judul": "Cahaya yang Tak Padam",
                "deskripsi": "CEO HMSD Adyatama 2026, perjalanan panjang kami bisa saja terakhir. tapi nama jordan akan selalu dikenang dilangit.",
                "foto": "https://drive.google.com/uc?export=view&id=1J3LYfGwgNeZptChrGFkg-YJM5mmD3VV2",
            },
        ]

        constellation_svgs = [
            "<svg width='86' height='54' viewBox='0 0 90 60'><line x1='15' y1='45' x2='45' y2='15' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><line x1='45' y1='15' x2='75' y2='35' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><circle cx='15' cy='45' r='3' fill='#fff'/><circle cx='45' cy='15' r='4' fill='#ffd740'/><circle cx='75' cy='35' r='3' fill='#80d8ff'/></svg>",
            "<svg width='86' height='54' viewBox='0 0 90 60'><line x1='15' y1='25' x2='40' y2='45' stroke='#80d8ff' stroke-width='1.2' stroke-opacity='0.6'/><line x1='40' y1='45' x2='75' y2='18' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><circle cx='15' cy='25' r='3' fill='#80d8ff'/><circle cx='40' cy='45' r='3.5' fill='#fff'/><circle cx='75' cy='18' r='4' fill='#ffd740'/></svg>",
            "<svg width='86' height='54' viewBox='0 0 90 60'><polygon points='45,10 20,48 70,48' fill='none' stroke='#ffd740' stroke-width='1.1' stroke-opacity='0.5'/><circle cx='45' cy='10' r='4' fill='#ffd740'/><circle cx='20' cy='48' r='3' fill='#fff'/><circle cx='70' cy='48' r='3' fill='#80d8ff'/></svg>",
            "<svg width='86' height='54' viewBox='0 0 90 60'><line x1='12' y1='30' x2='45' y2='14' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><line x1='45' y1='14' x2='78' y2='30' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><line x1='45' y1='14' x2='45' y2='48' stroke='#80d8ff' stroke-width='1.2' stroke-opacity='0.6'/><circle cx='12' cy='30' r='3' fill='#fff'/><circle cx='45' cy='14' r='4' fill='#ffd740'/><circle cx='78' cy='30' r='3' fill='#fff'/><circle cx='45' cy='48' r='3' fill='#80d8ff'/></svg>",
            "<svg width='86' height='54' viewBox='0 0 90 60'><circle cx='45' cy='30' r='18' fill='none' stroke='#ffd740' stroke-width='1' stroke-dasharray='3,3' stroke-opacity='0.6'/><circle cx='45' cy='30' r='4.5' fill='#ffd740'/><circle cx='27' cy='30' r='2.5' fill='#80d8ff'/><circle cx='63' cy='30' r='2.5' fill='#fff'/></svg>",
            "<svg width='86' height='54' viewBox='0 0 90 60'><line x1='15' y1='42' x2='35' y2='20' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><line x1='35' y1='20' x2='58' y2='38' stroke='#80d8ff' stroke-width='1.2' stroke-opacity='0.6'/><line x1='58' y1='38' x2='78' y2='14' stroke='#ffd740' stroke-width='1.2' stroke-opacity='0.6'/><circle cx='15' cy='42' r='3' fill='#fff'/><circle cx='35' cy='20' r='3.5' fill='#ffd740'/><circle cx='58' cy='38' r='3' fill='#80d8ff'/><circle cx='78' cy='14' r='4' fill='#ffd740'/></svg>",
        ]

        for row in range(2):
            cols = st.columns(3, gap="medium")
            for col_i, col in enumerate(cols):
                idx = row * 3 + col_i
                m = galeri_momen[idx]
                foto_url = m.get("foto", "").strip()

                with col:
                    if foto_url:
                        foto_b64 = get_image_base64(foto_url, max_dim=540)
                        visual_inner = f"<img src='{foto_b64}' alt='{m['judul']}' loading='lazy'>"
                    else:
                        svg_art = constellation_svgs[idx % len(constellation_svgs)]
                        visual_inner = (
                            f"<div class='chronicle-constellation-art'>"
                            f"{svg_art}"
                            f"<span style='font-family:JetBrains Mono,monospace;font-size:0.65em;color:#ffd740;letter-spacing:1.4px;'>ARSIP VISUAL JORDAN</span>"
                            f"</div>"
                        )

                    st.markdown(
                        f"<div class='chronicle-card'>"
                        f"<div class='chronicle-topbar'><span>✦ {m['label']}</span><span>{m['koordinat']}</span></div>"
                        f"<div class='chronicle-visual'>{visual_inner}</div>"
                        f"<div class='chronicle-body'>"
                        f"<div class='chronicle-title'>{m['judul']}</div>"
                        f"<p class='chronicle-desc'>{m['deskripsi']}</p>"
                        f"</div>"
                        f"</div>",
                        unsafe_allow_html=True,
                    )

        # ─── 3. PRASASTI PUISI JORDAN ───
        st.markdown("""
        <div class='puisi-scroll'>
            <div class='puisi-scroll-crest'>✦ PRASASTI SUMPAH TIGA BELAS BINTANG ✦</div>
            <div class='puisi-text'>
                Tiga belas jiwa, satu tekad membara,<br>
                Berjalan bersama di lorong data yang nyata.<br>
                Dari angka-angka yang diam membisu,<br>
                Kami merangkai cerita, menemukan makna yang tak terlihat mata.<br><br>
                Seperti jaringan yang terus belajar,<br>
                Dari setiap kesalahan, kami tumbuh besar.<br>
                Jordan bukan sekadar nama,<br>
                Ia adalah janji, bahwa kami tak pernah berhenti bermimpi.<br><br>
                Di setiap baris kode yang kami tulis,<br>
                Di setiap insight yang kami temukan,<br>
                Tersimpan kenangan yang tak lekang,<br>
                Dari tiga belas hati yang saling menguatkan.
            </div>
            <div class='puisi-author'>✦ Konstelasi Jordan • CEO HMSD Adyatama 2026 ✦</div>
        </div>
        """, unsafe_allow_html=True)

        # ─── 4. KONSTELASI ───
        if DAFTAR_KONSTELASI:
            with st.expander("🛰️ CONSTELLATION CODEX"):
                st.caption(
                    "Sepuluh konstelasi, satu langit yang sama."
                )
                codex_cards = ""
                for item in DAFTAR_KONSTELASI:
                    c = item.get("warna", [255, 215, 64])
                    rgb = f"rgb({c[0]},{c[1]},{c[2]})"
                    rgba_b = f"rgba({c[0]},{c[1]},{c[2]},0.45)"
                    codex_cards += (
                        f"<div class='codex-item' style='border-color:{rgba_b};'>"
                        f"<div class='codex-head'>"
                        f"<span class='codex-name' style='color:{rgb};'>✦ {item.get('nama', '')}</span>"
                        f"<span style='font-family:JetBrains Mono,monospace;font-size:0.7em;color:#90a4ae;'>#{item.get('kode', '')}</span>"
                        f"</div>"
                        f"<div class='codex-title'>« {item.get('gelar', '')} »</div>"
                        f"<div class='codex-desc'>{item.get('deskripsi', '')}</div>"
                        f"</div>"
                    )
                st.markdown(f"<div class='codex-grid'>{codex_cards}</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='astral-divider'>
            <div class='astral-divider-line'></div>
            <div class='astral-divider-symbol'>✦ ◈ ✦</div>
            <div class='astral-divider-line'></div>
        </div>
        """, unsafe_allow_html=True)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown("<h1 class='section-title'>✦ Anggota Konstelasi Jordan ✦</h1>", unsafe_allow_html=True)
        st.markdown(f"<p class='section-desc'>Kenalan sama 13 anggota Konstelasi Jordan di bawah bimbingan {NAMA_MENTOR}!</p>", unsafe_allow_html=True)

        default_foto = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

        # ===== 1. PIMPINAN KONSTELASI (PAK LURAH & BU LURAH) =====
        pimpinan_list = [
            {
                "urut": "01",
                "nama": "Bintang Mahardika",
                "sebagai": "Pak Lurah",
                "nim": "125450106",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@bintang.wav",
                "foto": "https://drive.google.com/uc?export=view&id=1KPiPBu6qnc-7uAcvTlfVxfvw3P3ojjPY",
            },
            {
                "urut": "02",
                "nama": "Sayyidina Najwa Syahra",
                "sebagai": "Bu Lurah",
                "nim": "125450002",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@syydna._",
                "foto": "https://drive.google.com/uc?export=view&id=1TWNgccBsATeQyTnJdCx30lPXOk-lF0JP",
            },
        ]

        # ===== 2. ANGGOTA KONSTELASI (11 ANGGOTA BERSATU) =====
        anggota_list = [
            {
                "urut": "03",
                "nama": "Muhammad Rafli Raditya",
                "sebagai": "Anggota",
                "nim": "125450095",
                "fun_fact": "Aku hidup dan semua orang hidup karena ku",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@glorious_rafli",
                "foto": "",
            },
            {
                "urut": "04",
                "nama": "M Abyan Alghaniyyu",
                "sebagai": "Anggota",
                "nim": "125450104",
                "fun_fact": "Pernah foto Sama Fufufafaa & Pria Solo",
                "motto_hidup": " Hidup Realistis dan jangan lupa Ibadah",
                "sosmed": "@byan_.27",
                "foto": "https://drive.google.com/uc?export=view&id=1i9oSkeFZT1sL0SJmMWmZb4l_qPCxAV-4",
            },
            {
                "urut": "05",
                "nama": "Rahmad Bayu Ridho",
                "sebagai": "Anggota",
                "nim": "125450093",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@rby_sel17",
                "foto": "",
            },
            {
                "urut": "06",
                "nama": "Mojes Wijaya",
                "sebagai": "Anggota",
                "nim": "125450094",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@mojeswwwijaya",
                "foto": "https://drive.google.com/uc?export=view&id=114wxxW8dyiUPBz87C3IyQJOyyl2M29kw",
            },
            {
                "urut": "07",
                "nama": "Iva Aulia Sofia",
                "sebagai": "Anggota",
                "nim": "125450062",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@valifia_",
                "foto": "https://drive.google.com/uc?export=view&id=1Kz0h3yq36ZDbBLIovx6MtEHTXlD_Nj5r",
            },
            {
                "urut": "08",
                "nama": "Astrit Aisya Rahmi",
                "sebagai": "Anggota",
                "nim": "125450036",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@asttritsy",
                "foto": "https://drive.google.com/uc?export=view&id=1D-_sGW7jHoUpCms068h97XYi4fdLxHMc",
            },
            {
                "urut": "09",
                "nama": "Septi Widia Arini",
                "sebagai": "Anggota",
                "nim": "125450055",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@searnn__",
                "foto": "",
            },
            {
                "urut": "10",
                "nama": "Fildzah Cahya Kamila",
                "sebagai": "Anggota",
                "nim": "125450040",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@filzhhy",
                "foto": "",
            },
            {
                "urut": "11",
                "nama": "Bening Arianti",
                "sebagai": "Anggota",
                "nim": "125450068",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@beningarnt",
                "foto": "",
            },
            {
                "urut": "12",
                "nama": "Lintar Abhinaya Putra Zulmi",
                "sebagai": "Anggota",
                "nim": "125450064",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@lintar.abhinaya",
                "foto": "",
            },
            {
                "urut": "13",
                "nama": "Ahda Nabiwa",
                "sebagai": "Anggota",
                "nim": "125450069",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "sosmed": "@na.biwa",
                "foto": "",
            },
        ]

        data_list = pimpinan_list + anggota_list

        # Pre-fetch foto unik secara paralel agar langsung siap
        unique_urls = list({(m.get("foto", "") or default_foto) for m in data_list})
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(lambda u: get_image_base64(u, 420), unique_urls))

        def _build_member_sosmed_url(raw_sosmed: str) -> str:
            s = (raw_sosmed or "").strip()
            if not s or s == "-":
                return ""
            if s.startswith("http://") or s.startswith("https://"):
                return s
            handle = s.split()[0].lstrip("@").strip("/")
            return f"https://www.instagram.com/{handle}/" if handle else ""

        def get_celestial_card_html(m):
            foto_url = m.get("foto", "") or default_foto
            foto_b64 = get_image_base64(foto_url, max_dim=420)
            urut = m.get("urut", "01")
            nama = m.get("nama", "")
            sebagai = m.get("sebagai", "Anggota")
            nim = m.get("nim", "-")
            fun_fact = m.get("fun_fact", "Isi fun fact di sini")
            motto = m.get("motto_hidup", "Isi motto di sini")
            sosmed = (m.get("sosmed") or "").strip()
            sosmed_url = _build_member_sosmed_url(sosmed)

            is_pimpinan = ("lurah" in sebagai.lower())
            role_cls = "role-pimpinan" if is_pimpinan else "role-anggota"
            badge_label = sebagai.upper()
            safe_name = nama.replace(" ", "+")
            avatar_fallback = f"https://ui-avatars.com/api/?name={safe_name}&background=12142b&color=ffd740&size=400&bold=true"
            link_overlay = (
                f"<a class='flip-card-link' href='{sosmed_url}' target='_blank' rel='noopener noreferrer' "
                f"title='Klik untuk membuka Instagram {nama} ({sosmed})'></a>"
                if sosmed_url else ""
            )
            footer_label = f"📸 {sosmed} ↗ • KLIK KARTU UNTUK SOSMED" if sosmed_url else "✦ CEO HMSD ADYATAMA ITERA 2026 ✦"

            return (
                f"<div class='flip-card' tabindex='0'>"
                f"{link_overlay}"
                f"<div class='flip-card-inner'>"
                f"<div class='flip-card-front'>"
                f"<div class='jcard-topstrip'><span>✦ JORDAN #{urut}</span><span>NIM {nim}</span></div>"
                f"<div class='jcard-photo-box'>"
                f"<img src='{foto_b64}' alt='{nama}' loading='lazy' decoding='async' onerror=\"this.onerror=null;this.src='{avatar_fallback}';\">"
                f"<div class='jcard-front-footer'>"
                f"<div class='jcard-front-name'>{nama}</div>"
                f"<div class='jcard-role-tag {role_cls}'>{badge_label}</div>"
                f"<div class='jcard-flip-prompt'>↻ HOVER PROFIL • KLIK BUKA SOSMED ↗</div>"
                f"</div>"
                f"</div>"
                f"</div>"
                f"<div class='flip-card-back'>"
                f"<div class='jback-topbar'><span>✦ ARSIP STELLAR #{urut}</span><span>KONSTELASI JORDAN</span></div>"
                f"<div class='jback-content'>"
                f"<div class='jback-identity'>"
                f"<div class='jback-name'>{nama}</div>"
                f"<div class='jback-role'>{badge_label} • DATAVORA</div>"
                f"</div>"
                f"<div class='jback-bottom-group'>"
                f"<div class='jback-field'><div class='jback-label'>NOMOR INDUK MAHASISWA</div><div class='jback-val jback-nim'>{nim}</div></div>"
                f"<div class='jback-field'><div class='jback-label'>FUN FACT</div><div class='jback-val'>{fun_fact}</div></div>"
                f"<div class='jback-field'><div class='jback-label'>MOTTO HIDUP</div><div class='jback-val jback-motto'>&ldquo;{motto}&rdquo;</div></div>"
                f"</div>"
                f"</div>"
                f"<div class='jback-footer'>{footer_label}</div>"
                f"</div>"
                f"</div>"
                f"</div>"
            )

        # ─── 1. PIMPINAN KELOMPOK (PAK LURAH & BU LURAH) ───
        st.markdown("""
        <div class='about-tier-header'>
            <div class='tier-badge'>👑 PAK LURAH &amp; BU LURAH</div>
            <p class='tier-sub'>Pimpinan Konstelasi Jordan</p>
        </div>
        """, unsafe_allow_html=True)

        pimpinan_html = "".join(get_celestial_card_html(m) for m in pimpinan_list)
        st.markdown(f"<div class='team-row-2'>{pimpinan_html}</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='astral-divider'>
            <div class='astral-divider-line'></div>
            <div class='astral-divider-symbol'>✦ ◈ ✦</div>
            <div class='astral-divider-line'></div>
        </div>
        """, unsafe_allow_html=True)

        # ─── 2. ANGGOTA KONSTELASI (11 ANGGOTA) ───
        st.markdown("""
        <div class='about-tier-header'>
            <div class='tier-badge'>⭐ ANGGOTA KONSTELASI JORDAN</div>
            <p class='tier-sub'>Sebelas Bintang Penjelajah Jordan</p>
        </div>
        """, unsafe_allow_html=True)

        anggota_html = "".join(get_celestial_card_html(m) for m in anggota_list)
        st.markdown(f"<div class='team-row-grid'>{anggota_html}</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='astral-divider'>
            <div class='astral-divider-line'></div>
            <div class='astral-divider-symbol'>✦ ◈ ✦</div>
            <div class='astral-divider-line'></div>
        </div>
        """, unsafe_allow_html=True)

    about_page()
