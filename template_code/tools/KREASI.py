import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from datetime import datetime
from PIL import Image, ImageOps
from io import BytesIO
import requests
import hashlib
import threading
import time
import random
import json
import os
import re

# ==============================================================================
#        KREASI I - JORDAN ASTRAL ARCADE & AI SANDBOX (5 MINI GAMES)
# ==============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Poppins:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');

    /* Lebarkan kontainer utama agar semua game punya ruang bernafas yang lega */
    .main .block-container,
    [data-testid="stMainBlockContainer"],
    [data-testid="stAppViewBlockContainer"] {
        max-width: 1120px !important;
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
    @media (max-width: 640px) {
        .main .block-container,
        [data-testid="stMainBlockContainer"],
        [data-testid="stAppViewBlockContainer"] {
            padding-left: 0.65rem !important;
            padding-right: 0.65rem !important;
        }
    }

    /* Pastikan semua iframe komponen game 100% lebar penuh dan tidak pernah terpotong */
    [data-testid="stCustomComponentV1"],
    .stCustomComponentV1,
    .element-container,
    iframe {
        width: 100% !important;
        min-width: 100% !important;
        max-width: 100% !important;
        border: none !important;
    }

    .arcade-hero {
        text-align: center;
        padding: 1.8rem 1.5rem 1.2rem 1.5rem;
        background: radial-gradient(ellipse at 50% 15%, rgba(255, 215, 64, 0.12) 0%, rgba(12, 14, 28, 0) 72%);
        border-radius: 18px;
        border: 1px solid rgba(255, 215, 64, 0.24);
        margin-bottom: 1.4rem;
    }
    .arcade-badge {
        display: inline-block;
        padding: 4px 16px;
        border-radius: 20px;
        background: rgba(255, 215, 64, 0.12);
        border: 1px solid rgba(255, 215, 64, 0.35);
        color: #ffd740;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.74em;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .arcade-title {
        font-family: 'Cinzel', 'Poppins', serif;
        font-size: 2.5em;
        font-weight: 800;
        background: linear-gradient(135deg, #fff6d6 0%, #ffd740 50%, #ffab40 85%, #ff6e40 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 2.5px;
        margin: 0;
    }
    .arcade-subtitle {
        font-family: 'Poppins', sans-serif;
        color: #b0bec5;
        font-size: 0.95em;
        margin-top: 0.4rem;
    }

    /* Survival Quiz Styling (Spacious & Breathing Room) */
    .quiz-shell {
        background: linear-gradient(160deg, #13152c 0%, #090b18 100%);
        border: 1px solid rgba(255, 215, 64, 0.32);
        border-radius: 18px;
        padding: 1.8rem 2rem;
        margin: 1rem 0 1.6rem 0;
        box-shadow: 0 12px 34px rgba(0, 0, 0, 0.55);
    }
    .quiz-hud {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        padding-bottom: 1.2rem;
        margin-bottom: 1.4rem;
        border-bottom: 1px solid rgba(255, 215, 64, 0.18);
    }
    @media (max-width: 700px) {
        .quiz-hud { grid-template-columns: repeat(2, 1fr); }
    }
    .hud-pill {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 215, 64, 0.26);
        border-radius: 12px;
        padding: 10px 14px;
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.86em;
        color: #ffd740;
        font-weight: 700;
    }
    .clue-stage-card {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 215, 64, 0.24);
        border-left: 4px solid #ffd740;
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 14px;
    }
    .clue-stage-locked {
        background: rgba(255, 255, 255, 0.015);
        border: 1px dashed rgba(255, 255, 255, 0.18);
        border-radius: 14px;
        padding: 14px 20px;
        margin-bottom: 14px;
        color: #90a4ae;
        font-size: 0.9em;
    }
    .clue-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.76em;
        font-weight: 700;
        color: #ffab40;
        letter-spacing: 1.3px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .clue-body {
        font-size: 1.02em;
        color: #eceff1;
        font-weight: 500;
        line-height: 1.65;
    }

    /* Leaderboard Table (Full Width & Spacious) */
    .lb-card {
        background: linear-gradient(160deg, #121428 0%, #090a16 100%);
        border: 1px solid rgba(255, 215, 64, 0.3);
        border-radius: 16px;
        padding: 1.2rem 1.6rem;
        margin-top: 1rem;
    }
    .lb-row {
        display: grid;
        grid-template-columns: 54px 1fr 160px 110px;
        align-items: center;
        gap: 12px;
        padding: 12px 14px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.07);
        font-size: 0.94em;
    }
    @media (max-width: 640px) {
        .lb-row { grid-template-columns: 40px 1fr 90px; }
        .lb-group { display: none; }
    }
    .lb-row:last-child {
        border-bottom: none;
    }
    .lb-rank {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 800;
        color: #ffd740;
        font-size: 1.05em;
    }
    .lb-name {
        font-weight: 600;
        color: #ffffff;
    }
    .lb-group {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78em;
        color: #80d8ff;
        background: rgba(128, 216, 255, 0.1);
        border: 1px solid rgba(128, 216, 255, 0.25);
        padding: 4px 10px;
        border-radius: 8px;
        text-align: center;
    }
    .lb-score {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 800;
        color: #ffd740;
        font-size: 1.02em;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='arcade-hero'>
    <div class='arcade-badge'>✦ STELLAR SANCTUARY • STAR STREAM &amp; SEFIRAH CASTLE ARCHIVE ✦</div>
    <h1 class='arcade-title'>🎮 JORDAN ASTRAL ARCADE</h1>
    <p class='arcade-subtitle'>Lima Skenario Konstelasi &amp; Simulasi Kecerdasan Buatan di Bawah Langit Kelompok 01 Jordan</p>
</div>
""", unsafe_allow_html=True)

# ===== MENU LAZY-LOAD (Hanya merender 1 game yang sedang dibuka agar super ringan) =====
active_game = option_menu(
    menu_title=None,
    options=[
        "Survival Quiz",
        "Neon Tactics AI",
        "Pathfinding Race",
        "Gauss-Jordan Puzzle",
        "Ball Battle Arena",
    ],
    icons=[
        "trophy-fill",
        "grid-3x3-gap-fill",
        "compass-fill",
        "calculator-fill",
        "lightning-charge-fill",
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
            "font-size": "13px",
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
# DATA HELPER UNTUK GAME 1 (ANGGOTA JORDAN + 151 KATING HMSD + LEADERBOARD)
# ==============================================================================
ANGGOTA_JORDAN = [
    {"nama": "Bintang Mahardika", "jabatan": "Pak Lurah Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Pimpinan Kelompok", "nim": "125450106", "asal": "Lampung", "hobi": "Eksplorasi Sains Data", "foto": ""},
    {"nama": "Sayyidina Najwa Syahra", "jabatan": "Bu Lurah Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Pimpinan Kelompok", "nim": "125450002", "asal": "Lampung", "hobi": "Membaca & Organisasi", "foto": ""},
    {"nama": "Muhammad Rafli Raditya", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450095", "asal": "Indonesia", "hobi": "Coding & AI Engineering", "foto": "https://drive.google.com/uc?export=view&id=1eRqS2Dm2UYeKTpmixAU5WmjmWMqqW1co"},
    {"nama": "M Abyan Alghaniyyu", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450104", "asal": "Indonesia", "hobi": "Sains Data & Teknologi", "foto": ""},
    {"nama": "Rahmad Bayu Ridho", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450093", "asal": "Indonesia", "hobi": "Olahraga & Musik", "foto": ""},
    {"nama": "Mojes Wijaya", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450094", "asal": "Indonesia", "hobi": "Gaming & Analisis", "foto": ""},
    {"nama": "Iva Aulia Sofia", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450062", "asal": "Indonesia", "hobi": "Desain & Kuliner", "foto": ""},
    {"nama": "Astrit Aisyah Rahmi", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450036", "asal": "Indonesia", "hobi": "Fotografi & Musik", "foto": ""},
    {"nama": "Septi Widia Arin", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450055", "asal": "Indonesia", "hobi": "Menulis & Membaca", "foto": ""},
    {"nama": "Fildzah Cahya Kamila", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450040", "asal": "Indonesia", "hobi": "Seni & Kreativitas", "foto": ""},
    {"nama": "Lintar Abhinaya Putra Zulmi", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450064", "asal": "Indonesia", "hobi": "Teknologi & Strategi", "foto": ""},
    {"nama": "Ahda Nabiwa", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450069", "asal": "Indonesia", "hobi": "Diskusi & Eksplorasi", "foto": ""},
    {"nama": "Bening Arianti", "jabatan": "Anggota Kelompok 01 Jordan", "departemen": "Kelompok 01 Jordan", "divisi": "Anggota Orbit Jordan", "nim": "125450068", "asal": "Indonesia", "hobi": "Musik & Traveling", "foto": ""},
]

DAFTAR_KELOMPOK_RESMI = [
    "01 - Jordan",
    "02 - Jacobi",
    "03 - Tensor",
    "04 - Anova",
    "05 - Markov",
    "06 - Pandas",
    "07 - Poisson",
    "08 - COSVAL",
    "09 - Bayesian",
    "10 - Greedy",
    "Kating / Pengurus HMSD",
]

# Filter kata tidak pantas menggunakan dataset publik GitHub + API eksternal + SHA-256 one-way digest
# (Tidak ada satu pun kata kasar yang tertulis di dalam kode sumber ini)
_GITHUB_PROFANITY_SOURCES = (
    "https://raw.githubusercontent.com/chucknorris-io/swear-words/master/id",
    "https://raw.githubusercontent.com/chucknorris-io/swear-words/master/en",
    "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en",
)
_PROFANITY_SHA256_DIGESTS = frozenset((
    "071621bbcb", "08aac36ac2", "13eac7480f", "1408d3d8b3", "16441d60ac",
    "2054739eed", "27ce018175", "2bdc3f25f1", "3149cb1026", "328c32e125",
    "37ea6c07cb", "3c2e9b8a86", "47912dfbbe", "4f182ed6c0", "527c13a8ff",
    "52ee19420d", "594bdfa59f", "5d60419e04", "60ec059800", "611308736d",
    "6171dcb864", "737ca80b24", "787bfcbecd", "7bad870be9", "7f93b2da7f",
    "83b19e57a9", "8770c78858", "8ab815134c", "9180e18c81", "98500ad3f6",
    "9a4b34df97", "ae8be83497", "b4d2a2a041", "b9d53efddd", "bcea5d79d8",
    "bf6a5effda", "c01aa176ab", "c9580f4fd0", "c9f392a422", "cb5ca495e5",
    "d2487d3316", "d261cd5329", "df14ce932f", "e78f34b9d9", "f3e0a855ac",
    "f856680d7d", "fab59b97cf", "fb369efc62", "fec2cad1ce", "ff0ee0cf4f",
))
_LEET_MAP = str.maketrans({"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "@": "a", "$": "s", "!": "i"})


@st.cache_data(ttl=86400, max_entries=1, show_spinner=False)
def _load_github_profanity_set() -> frozenset:
    words = set()
    for url in _GITHUB_PROFANITY_SOURCES:
        try:
            r = requests.get(url, timeout=3.5)
            if r.status_code == 200:
                for line in r.text.splitlines():
                    w = line.strip().lower()
                    if len(w) >= 3 and " " not in w:
                        words.add(w)
        except Exception:
            continue
    return frozenset(words)


def _check_purgomalum_api(text: str) -> bool:
    try:
        r = requests.get(
            "https://www.purgomalum.com/service/containsprofanity",
            params={"text": text},
            timeout=2.0,
        )
        return r.status_code == 200 and r.text.strip().lower() == "true"
    except Exception:
        return False


def is_profane_text(raw_text: str) -> bool:
    if not raw_text:
        return False
    norm = raw_text.lower().translate(_LEET_MAP)
    tokens = re.findall(r"[a-z]{3,}", norm)
    compact = re.sub(r"[^a-z]", "", norm)
    candidates = set(tokens)
    if len(compact) >= 3:
        candidates.add(compact)
        for ln in range(3, min(9, len(compact) + 1)):
            for i in range(len(compact) - ln + 1):
                candidates.add(compact[i : i + ln])

    for cand in candidates:
        digest = hashlib.sha256(("jrd_" + cand).encode("utf-8")).hexdigest()[:10]
        if digest in _PROFANITY_SHA256_DIGESTS:
            return True

    remote_words = _load_github_profanity_set()
    if remote_words and (any(t in remote_words for t in tokens) or compact in remote_words):
        return True

    return _check_purgomalum_api(raw_text)


def sanitize_player_name(raw_name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s\.\-\_]", "", (raw_name or "")).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)[:16]
    if not cleaned or len(cleaned) < 2:
        return ""
    return cleaned


def _extract_drive_id_quiz(url: str) -> str:
    """Ekstrak ID Google Drive dari berbagai variasi URL atau string ID langsung."""
    if not url:
        return ""
    url = str(url).strip()
    for pat in (r"[?&]id=([\w-]{10,})", r"/file/d/([\w-]{10,})", r"/d/([\w-]{10,})"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    if re.fullmatch(r"[\w-]{20,}", url):
        return url
    return ""


@st.cache_data(ttl=3600, show_spinner=False)
def load_quiz_photo(url: str):
    """
    Unduh gambar dari Google Drive lewat server Python agar tidak diblokir browser (anti broken image).
    Mendukung Googleusercontent lh3, Drive thumbnail CDN cepat, dan export=view dengan header browser.
    """
    if not url or not str(url).strip():
        return None
    url = str(url).strip()
    gid = _extract_drive_id_quiz(url)
    candidates = [url]
    if gid:
        candidates = [
            f"https://lh3.googleusercontent.com/d/{gid}=w500",
            f"https://drive.google.com/thumbnail?id={gid}&sz=w500",
            f"https://drive.google.com/uc?export=view&id={gid}",
        ]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for cand in candidates:
        try:
            resp = requests.get(cand, headers=headers, timeout=8)
            ctype = resp.headers.get("Content-Type", "").lower()
            if resp.status_code == 200 and resp.content and "html" not in ctype:
                img = Image.open(BytesIO(resp.content))
                img = ImageOps.exif_transpose(img)
                img = img.resize((260, 340))
                return img
        except Exception:
            continue
    return None


@st.cache_data(ttl=3600, show_spinner=False)
def _load_kating_quiz_pool_cached(_mtime: float = 0.0):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    statis_path = os.path.join(base_dir, "Data", "Data_statis", "data_anggota_hmsd_2026.json")
    if not os.path.exists(statis_path):
        statis_path = os.path.join(base_dir, "Data", "data_statis", "data_anggota_hmsd_2026.json")
    
    dinamis_dir = os.path.join(base_dir, "Data", "Data_dinamis")
    if not os.path.isdir(dinamis_dir):
        dinamis_dir = os.path.join(base_dir, "Data", "data_dinamis")

    foto_map = {}
    if os.path.isdir(dinamis_dir):
        # Prioritas file sumber foto: bintang, rafli, buku_kating, lalu semua file anggota lainnya
        all_files = os.listdir(dinamis_dir)
        priority_order = ["bintang.json", "rafli.json", "buku_kating.json", "najwa.json", "septi.json", "biwa.json"]
        ordered_files = [f for f in priority_order if f in all_files] + [f for f in all_files if f not in priority_order and f.endswith(".json") and f != "leaderboard_jordan.json"]
        for fn in ordered_files:
            fp = os.path.join(dinamis_dir, fn)
            try:
                with open(fp, "r", encoding="utf-8-sig") as f:
                    content = json.load(f)
                entries = content if isinstance(content, list) else [content]
                for ent in entries:
                    if not isinstance(ent, dict):
                        continue
                    for item in ent.get("data", []):
                        nk = str(item.get("nama_kating", "")).strip().lower()
                        gid = str(item.get("foto_massal_gdrive_id", "")).strip()
                        if nk and gid and gid != "1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_":
                            if nk not in foto_map:
                                foto_map[nk] = gid
            except Exception:
                pass

    pool = []
    if os.path.exists(statis_path):
        try:
            with open(statis_path, "r", encoding="utf-8-sig") as f:
                s_json = json.load(f)
            for m in s_json:
                nama = (m.get("nama") or "").strip()
                if not nama:
                    continue
                hobi_list = m.get("hobi", [])
                hobi_str = ", ".join(hobi_list) if isinstance(hobi_list, list) and hobi_list else "-"
                
                # Pencocokan foto: exact -> normalized token / substring match
                n_low = nama.lower()
                gid_found = foto_map.get(n_low, "")
                if not gid_found:
                    n_tokens = [w for w in re.sub(r"[^a-z0-9\s]", "", n_low).split() if len(w) >= 3]
                    for k, gid in foto_map.items():
                        k_tokens = [w for w in re.sub(r"[^a-z0-9\s]", "", k).split() if len(w) >= 3]
                        common = len(set(n_tokens) & set(k_tokens))
                        if common >= 2 or (len(n_tokens) == 1 and common == 1) or n_low.startswith(k) or k.startswith(n_low):
                            gid_found = gid
                            break

                pool.append({
                    "nama": nama,
                    "nim": str(m.get("nim") or "-"),
                    "asal": str(m.get("asal") or "-"),
                    "hobi": hobi_str,
                    "departemen": str(m.get("departemen") or "HMSD Adyatama"),
                    "divisi": str(m.get("divisi") or "Pimpinan / BPH"),
                    "jabatan": str(m.get("jabatan") or "Pengurus"),
                    "foto": gid_found,
                })
        except Exception:
            pass
    return pool


def load_kating_quiz_pool():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    statis_path = os.path.join(base_dir, "Data", "Data_statis", "data_anggota_hmsd_2026.json")
    if not os.path.exists(statis_path):
        statis_path = os.path.join(base_dir, "Data", "data_statis", "data_anggota_hmsd_2026.json")
    dinamis_dir = os.path.join(base_dir, "Data", "Data_dinamis")
    if not os.path.isdir(dinamis_dir):
        dinamis_dir = os.path.join(base_dir, "Data", "data_dinamis")

    mt = os.path.getmtime(statis_path) if os.path.exists(statis_path) else 0.0
    if os.path.isdir(dinamis_dir):
        for fn in ("bintang.json", "rafli.json"):
            fp = os.path.join(dinamis_dir, fn)
            if os.path.exists(fp):
                mt += os.path.getmtime(fp)
    return _load_kating_quiz_pool_cached(mt)


def get_client_device_fp() -> str:
    """
    Buat sidik jari perangkat (Device Fingerprint SHA-256) dari kombinasi IP jaringan + spesifikasi browser/OS.
    Tetap konsisten meski pengguna menekan F5, membuka tab baru, atau mengganti nama berkali-kali di 1 laptop.
    """
    try:
        hdrs = st.context.headers or {}
    except Exception:
        hdrs = {}
    ip = (
        hdrs.get("X-Forwarded-For", "").split(",")[0].strip()
        or hdrs.get("X-Real-Ip", "").strip()
        or hdrs.get("Remote-Addr", "").strip()
        or "local_ip"
    )
    ua = hdrs.get("User-Agent", "ua")
    ch_ua = hdrs.get("Sec-Ch-Ua", "")
    plat = hdrs.get("Sec-Ch-Ua-Platform", "")
    lang = hdrs.get("Accept-Language", "")
    raw_sig = f"jordan_fp|{ip}|{ua}|{ch_ua}|{plat}|{lang}"
    fp = hashlib.sha256(raw_sig.encode("utf-8")).hexdigest()[:16]
    st.session_state.setdefault("jordan_device_fp", fp)
    return st.session_state["jordan_device_fp"]


# ==============================================================================
# INTEGRASI GOOGLE APPS SCRIPT / GOOGLE SHEETS & NORMALISASI TANGGAL
# ==============================================================================
LEADERBOARD_APPSCRIPT_URL = "https://script.google.com/macros/s/AKfycby6nEH8KWQuSLTnsQSJvUr3T_MISaRh-53TyBA4WTOOrHWqkiaDKRrWa9KPI8QNVLLJ/exec"


def _get_appscript_url() -> str:
    """Ambil URL Google Apps Script dari st.secrets atau variabel lokal."""
    try:
        if "LEADERBOARD_APPSCRIPT_URL" in st.secrets:
            u = st.secrets["LEADERBOARD_APPSCRIPT_URL"].strip()
            if u.startswith("http"):
                return u
    except Exception:
        pass
    if LEADERBOARD_APPSCRIPT_URL and LEADERBOARD_APPSCRIPT_URL.strip().startswith("http"):
        return LEADERBOARD_APPSCRIPT_URL.strip()
    return ""


def _normalize_month_str(raw_val) -> str:
    """Mengubah format bulan apa pun (Date object string Google Sheets, '2026-10', 'Oct 2026', dll.) menjadi 'YYYY-MM'."""
    if not raw_val:
        return ""
    s = str(raw_val).strip()
    m = re.search(r"(\d{4})[-/.](\d{1,2})", s)
    if m:
        return f"{m.group(1)}-{int(m.group(2)):02d}"
    m_mo = re.search(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Agu|Okt|Des)", s, re.IGNORECASE)
    m_yr = re.search(r"\b(20\d{2})\b", s)
    if m_mo and m_yr:
        month_map = {
            "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "mei": 5,
            "jun": 6, "jul": 7, "aug": 8, "agu": 8, "sep": 9, "oct": 10,
            "okt": 10, "nov": 11, "dec": 12, "des": 12,
        }
        mo_num = month_map.get(m_mo.group(1).lower()[:3], 10)
        return f"{m_yr.group(1)}-{mo_num:02d}"
    return s[:7]


def _format_clean_date(raw_val) -> str:
    """Format string tanggal apa pun jadi format ringkas '26 Okt 2026'."""
    if not raw_val:
        return ""
    s = str(raw_val).strip()
    m1 = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(20\d{2})", s)
    if m1:
        return f"{int(m1.group(1))} {m1.group(2)[:3].title()} {m1.group(3)}"
    m2 = re.search(r"([A-Za-z]{3,})\s+(\d{1,2})\s+(20\d{2})", s)
    if m2:
        return f"{int(m2.group(2))} {m2.group(1)[:3].title()} {m2.group(3)}"
    m3 = re.search(r"(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})", s)
    if m3:
        mo_names = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
        mo_idx = max(0, min(11, int(m3.group(2)) - 1))
        return f"{int(m3.group(3))} {mo_names[mo_idx]} {m3.group(1)}"
    return s[:12]

@st.cache_resource
def _get_leaderboard_store():
    """
    Menyimpan Prasasti Skor Abadi & Skor Bulanan di RAM Server dengan Thread Lock
    serta membaca/menulis ke Data/Data_dinamis/leaderboard_jordan.json.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lb_file = os.path.join(base_dir, "Data", "Data_dinamis", "leaderboard_jordan.json")

    default_entries = [
        {"nama": "Bintang Mahardika", "kelompok": "Konstelasi Jordan", "kategori": "player", "skor": 540, "streak": 6, "bulan": "2026-10", "tanggal": "18 Okt 2026", "protected": True},
        {"nama": "Sayyidina Najwa", "kelompok": "Konstelasi Jordan", "kategori": "player", "skor": 510, "streak": 5, "bulan": "2026-10", "tanggal": "18 Okt 2026", "protected": True},
        {"nama": "M Rafli Raditya", "kelompok": "Konstelasi Jordan", "kategori": "player", "skor": 480, "streak": 5, "bulan": "2026-10", "tanggal": "18 Okt 2026", "protected": True},
        {"nama": "M Abyan Alghaniyyu", "kelompok": "Konstelasi Jordan", "kategori": "player", "skor": 410, "streak": 4, "bulan": "2026-10", "tanggal": "18 Okt 2026", "protected": True},
        {"nama": "Kak Yollanda A.", "kelompok": "Kating / Pengurus HMSD", "kategori": "kating", "skor": 720, "streak": 8, "bulan": "2026-10", "tanggal": "18 Okt 2026", "protected": True},
    ]

    lock = threading.Lock()
    if os.path.exists(lb_file):
        try:
            with open(lb_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, list) and loaded:
                return {"entries": loaded[:40], "path": lb_file, "lock": lock, "rate_map": {}}
        except Exception:
            pass

    try:
        with open(lb_file, "w", encoding="utf-8") as f:
            json.dump(default_entries, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    return {"entries": default_entries, "path": lb_file, "lock": lock, "rate_map": {}, "mtime": 0.0}


def get_global_leaderboard():
    store = _get_leaderboard_store()
    path = store["path"]
    try:
        mt = os.path.getmtime(path) if os.path.exists(path) else 0.0
        if mt != store.get("mtime", 0.0):
            with open(path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, list) and loaded:
                store["entries"] = loaded[:40]
                store["mtime"] = mt
    except Exception:
        pass
    return store


def save_score_to_leaderboard(nama: str, kelompok: str, skor: int, streak: int) -> tuple[bool, str]:
    clean_name = sanitize_player_name(nama)
    if not clean_name:
        return False, "❌ Nama panggilan harus terdiri dari 2 hingga 16 huruf/angka."
    if is_profane_text(clean_name) or is_profane_text(nama):
        return False, "❌ Nama terdeteksi mengandung kata tidak pantas oleh filter bahasa (GitHub/API). Gunakan nama yang sopan."

    device_fp = get_client_device_fp()
    kategori = "kating" if any(w in kelompok.lower() for w in ("kating", "senior", "mentor")) else "player"
    skor = max(0, int(skor))
    streak = max(0, int(streak))

    store = get_global_leaderboard()
    lock = store.setdefault("lock", threading.Lock())
    rate_map = store.setdefault("rate_map", {})

    with lock:
        now_ts = time.time()
        last_ts = rate_map.get(device_fp, 0.0)
        if now_ts - last_ts < 15.0:
            sisa = int(15.0 - (now_ts - last_ts)) + 1
            return False, f"⏳ Tunggu {sisa} detik sebelum memperbarui skor."

        entries = store["entries"]
        now = datetime.now()
        bulan_str = now.strftime("%Y-%m")
        tanggal_str = now.strftime("%d %b %Y")

        # 1 Perangkat (device_fp) atau Nama+Konstelasi yang sama = 1 Slot di Leaderboard
        matched_item = None
        for item in entries:
            item_cat = "kating" if any(w in str(item.get("kategori", "")).lower() for w in ("kating", "senior", "mentor")) else "player"
            if item_cat != kategori:
                continue
            same_device = bool(item.get("device_fp") and item.get("device_fp") == device_fp)
            same_name = (item.get("nama", "").lower() == clean_name.lower() and item.get("kelompok") == kelompok)
            if same_device or same_name:
                matched_item = item
                break

        saved_entry = None
        if matched_item is not None:
            old_score = int(matched_item.get("skor", 0))
            old_name = matched_item.get("nama", clean_name)
            if skor <= old_score:
                return (
                    False,
                    f"🛡️ **1 Perangkat = 1 Slot Leaderboard:** Perangkat ini sudah tercatat atas nama **{old_name}** dengan skor **{old_score} pts**. Cetak skor di atas **{old_score} pts** untuk memperbarui rekor perangkatmu!",
                )
            matched_item["nama"] = clean_name
            matched_item["kelompok"] = kelompok
            matched_item["skor"] = skor
            matched_item["streak"] = max(streak, int(matched_item.get("streak", 0)))
            matched_item["bulan"] = bulan_str
            matched_item["tanggal"] = tanggal_str
            matched_item["device_fp"] = device_fp
            saved_entry = matched_item
            msg = f"🔥 **Rekor Baru!** Skor perangkatmu diperbarui dari {old_score} pts menjadi **{skor} pts**."
        else:
            saved_entry = {
                "nama": clean_name,
                "kelompok": kelompok,
                "kategori": kategori,
                "skor": skor,
                "streak": streak,
                "bulan": bulan_str,
                "tanggal": tanggal_str,
                "device_fp": device_fp,
            }
            entries.append(saved_entry)
            msg = "🎉 Skor kamu berhasil diabadikan ke Prasasti Leaderboard!"

        rate_map[device_fp] = now_ts
        if len(rate_map) > 500:
            rate_map.clear()

        entries.sort(key=lambda x: x.get("skor", 0), reverse=True)
        del entries[40:]

        try:
            with open(store["path"], "w", encoding="utf-8") as f:
                json.dump(entries, f, ensure_ascii=False, indent=2)
            store["mtime"] = os.path.getmtime(store["path"])
        except Exception:
            pass

        # Kirim update ke Google Sheets secara background thread agar tidak menghambat respons Streamlit
        remote_url = _get_appscript_url()
        if remote_url and saved_entry:
            def _bg_sync(url, item):
                try:
                    requests.post(url, json={"entry": item}, timeout=5.0)
                except Exception:
                    pass
            threading.Thread(target=_bg_sync, args=(remote_url, saved_entry), daemon=True).start()

        return True, msg


# ==============================================================================
# GAME 1: JORDAN SURVIVAL QUIZ (TRUE SURVIVAL + SPEED BONUS + ANTI-FARMING)
# ==============================================================================
if active_game == "Survival Quiz":
    st.markdown("### 🔢 Jordan Survival Quiz: Tiga Petunjuk Rasi Bintang")
    st.caption("Kamu punya **3 nyawa** (bertahanlah sejauh mungkin!). Tiap soal bernilai dasar **100 poin** (+ **Bonus Kecepatan** hingga **+25 poin** & **Bonus Streak**), tapi membuka Clue 2 memotong **30 poin** dan Clue 3 (Foto) memotong **45 poin**.")

    c_mode1, c_mode2 = st.columns([2, 1])
    with c_mode1:
        mode_pool_choice = st.radio(
            "Pilih Arena Soal Survival:",
            [
                "🌌 Ekspedisi Gabungan (13 Anggota Jordan + 151 Kating HMSD)",
                "⭐ Pemanasan Orbit Jordan dulu (13 Anggota, lanjut HMSD jika masih hidup)",
            ],
            horizontal=True,
        )

    kating_pool = load_kating_quiz_pool()
    full_pool = ANGGOTA_JORDAN + kating_pool
    is_jordan_first = "Pemanasan" in mode_pool_choice

    if (
        "surv_lives" not in st.session_state
        or st.session_state.get("surv_mode") != mode_pool_choice
    ):
        st.session_state.surv_mode = mode_pool_choice
        st.session_state.surv_lives = 3
        st.session_state.surv_score = 0
        st.session_state.surv_streak = 0
        st.session_state.surv_best_streak = 0
        st.session_state.surv_round = 1
        st.session_state.surv_used_names = []
        st.session_state.surv_current = None
        st.session_state.surv_options = []
        st.session_state.surv_clue2_open = False
        st.session_state.surv_clue3_open = False
        st.session_state.surv_answered = False
        st.session_state.surv_last_msg = ""
        st.session_state.surv_last_ok = True
        st.session_state.surv_saved = False
        st.session_state.surv_lb_feedback = None
        st.session_state.surv_q_ts = time.time()

    def prepare_next_question():
        # Jika pilih Pemanasan Jordan, 13 ronde pertama khusus Anggota Jordan, lalu ronde 14+ otomatis masuk gelombang 151 Kating HMSD
        # Dengan begitu tidak ada yang bisa farming mengulang 13 orang yang sama terus-menerus!
        if is_jordan_first and len(st.session_state.surv_used_names) < len(ANGGOTA_JORDAN):
            candidate_pool = ANGGOTA_JORDAN
        else:
            candidate_pool = full_pool

        unused = [p for p in candidate_pool if p["nama"] not in st.session_state.surv_used_names]
        if not unused:
            unused = [p for p in full_pool if p["nama"] not in st.session_state.surv_used_names]
        if not unused:
            st.session_state.surv_used_names = []
            unused = full_pool[:]

        target = random.choice(unused)
        st.session_state.surv_used_names.append(target["nama"])
        same_dept = [
            p["nama"] for p in full_pool
            if p["nama"] != target["nama"] and p.get("departemen") == target.get("departemen")
        ]
        other_dept = [
            p["nama"] for p in full_pool
            if p["nama"] != target["nama"] and p.get("departemen") != target.get("departemen")
        ]
        if len(same_dept) >= 3:
            distractors = random.sample(same_dept, 3)
        else:
            distractors = same_dept + random.sample(other_dept, 3 - len(same_dept))
        opts = distractors + [target["nama"]]
        random.shuffle(opts)
        st.session_state.surv_current = target
        st.session_state.surv_options = opts
        st.session_state.surv_clue2_open = False
        st.session_state.surv_clue3_open = False
        st.session_state.surv_answered = False
        st.session_state.surv_q_ts = time.time()

    if st.session_state.surv_current is None:
        prepare_next_question()

    lives = st.session_state.surv_lives
    hearts_str = ("❤️ " * lives + "🖤 " * (3 - lives)).strip()
    c2_open = st.session_state.surv_clue2_open
    c3_open = st.session_state.surv_clue3_open

    penalty = (30 if c2_open else 0) + (45 if c3_open else 0)
    current_question_pts = max(25, 100 - penalty)
    streak_bonus = min(45, st.session_state.surv_streak * 9)

    st.markdown(f"""
    <div class='quiz-shell'>
        <div class='quiz-hud'>
            <div class='hud-pill'>NYAWA: {hearts_str}</div>
            <div class='hud-pill'>RONDE #{st.session_state.surv_round}</div>
            <div class='hud-pill'>🔥 STREAK: {st.session_state.surv_streak}x (+{streak_bonus} Bonus)</div>
            <div class='hud-pill'>🏆 TOTAL SKOR: {st.session_state.surv_score}</div>
        </div>
    """, unsafe_allow_html=True)

    if lives > 0:
        q = st.session_state.surv_current
        if is_jordan_first and st.session_state.surv_round == 14 and not st.session_state.surv_answered:
            st.info("🌊 **Gelombang Lanjutan!** Kamu berhasil melewati 13 Anggota Jordan. Mulai Ronde 14, soal diperluas ke seluruh 151 Kating HMSD!")

        # CLUE 1: 3 Digit Akhir NIM, Asal Daerah, dan Hobi
        raw_nim = str(q.get("nim") or "-").strip()
        nim_3_akhir = f"...{raw_nim[-3:]}" if len(raw_nim) >= 3 and raw_nim != "-" else raw_nim
        st.markdown(f"""
        <div class='clue-stage-card'>
            <div class='clue-title'>✦ CLUE TAHAP 1 (TERBUKA OTOMATIS • NILAI SOAL SAAT INI: {current_question_pts} POIN + BONUS KECEPATAN)</div>
            <div class='clue-body'>
                <b>3 Digit Akhir NIM:</b> <span style='color:#ffd740;font-family:JetBrains Mono,monospace;font-size:1.08em;'>{nim_3_akhir}</span>
                &nbsp;&nbsp;•&nbsp;&nbsp;
                <b>Asal Daerah:</b> <span style='color:#80d8ff;'>{q['asal']}</span><br>
                <b>Hobi / Minat:</b> <span style='color:#cfd8dc;'>{q['hobi']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # CLUE 2: Departemen/Badan & Jabatan (-30 Poin)
        if c2_open:
            div_info = q["divisi"] if q["divisi"] and q["divisi"] != "-" else "Pimpinan / BPH"
            st.markdown(f"""
            <div class='clue-stage-card' style='border-left-color:#80d8ff;'>
                <div class='clue-title' style='color:#80d8ff;'>🔍 CLUE TAHAP 2 (TERBUKA • POTONGAN -30 POIN)</div>
                <div class='clue-body'>
                    <b>Departemen / Badan:</b> <span style='color:#ffd740;'>{q['departemen']}</span> ({div_info})<br>
                    <b>Jabatan:</b> <span style='color:#80d8ff;'>{q['jabatan']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='clue-stage-locked'>
                🔒 <b>Clue Tahap 2 (Departemen/Badan, Biro/Komisi/Divisi &amp; Jabatan)</b> masih terkunci. Buka jika butuh petunjuk tambahan (-30 Poin).
            </div>
            """, unsafe_allow_html=True)

        # CLUE 3: Foto Profil (-45 Poin)
        if c3_open:
            st.markdown("""
            <div class='clue-stage-card' style='border-left-color:#00e676;'>
                <div class='clue-title' style='color:#00e676;'>📸 CLUE TAHAP 3 (TERBUKA • POTONGAN -45 POIN)</div>
            </div>
            """, unsafe_allow_html=True)
            foto_url = q.get("foto", "")
            pil_img = load_quiz_photo(foto_url) if foto_url else None
            c_i1, c_i2, c_i3 = st.columns([1.3, 1, 1.3])
            with c_i2:
                if pil_img is not None:
                    st.image(pil_img, use_container_width=True)
                else:
                    st.markdown("""
                    <div style='padding:2rem;text-align:center;background:#141730;border:1.5px dashed #ffd740;border-radius:14px;color:#ffd740;'>
                        🌟 Foto belum tersedia di Drive untuk sosok ini
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class='clue-stage-locked'>
                🔒 <b>Clue Tahap 3 (Foto Profil)</b> masih terkunci. Buka jika ingin melihat fotonya (-45 Poin).
            </div>
            """, unsafe_allow_html=True)

        # Tombol Buka Clue 2 & Clue 3
        if not st.session_state.surv_answered and (not c2_open or not c3_open):
            b_col1, b_col2 = st.columns(2, gap="medium")
            with b_col1:
                if not c2_open:
                    if st.button("🔍 Buka Clue 2: Departemen & Jabatan (-30 Poin)", use_container_width=True):
                        st.session_state.surv_clue2_open = True
                        st.rerun()
            with b_col2:
                if not c3_open:
                    if st.button("📸 Buka Clue 3: Foto Profil (-45 Poin)", use_container_width=True):
                        st.session_state.surv_clue3_open = True
                        st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        if not st.session_state.surv_answered:
            st.markdown(f"#### 🎯 Siapakah sosok pemilik biodata di atas? *(Nilai Dasar: {current_question_pts} Poin)*")
            opt_cols = st.columns(2, gap="medium")
            for idx, opt_name in enumerate(st.session_state.surv_options):
                with opt_cols[idx % 2]:
                    if st.button(f"✦ {opt_name}", key=f"surv_opt_{idx}", use_container_width=True):
                        elapsed_q = max(0.0, time.time() - st.session_state.get("surv_q_ts", time.time()))
                        if elapsed_q < 0.5:
                            st.warning("⏳ Terlalu cepat! Tunggu sejenak sebelum memilih jawaban.")
                            st.stop()
                        st.session_state.surv_answered = True
                        if opt_name == q["nama"]:
                            # Speed bonus kontinu (1..25 poin) agar skor tersebar alami dan tidak menumpuk di angka bulat yang sama
                            speed_bonus = max(0, min(25, int(round(25.0 - elapsed_q * 1.4))))
                            gained = current_question_pts + streak_bonus + speed_bonus
                            st.session_state.surv_score += gained
                            st.session_state.surv_streak += 1
                            st.session_state.surv_best_streak = max(
                                st.session_state.surv_best_streak, st.session_state.surv_streak
                            )
                            st.session_state.surv_last_ok = True
                            st.session_state.surv_last_msg = (
                                f"✅ **Jawaban Benar!** Itu adalah **{q['nama']}** "
                                f"({q['jabatan']} - {q['departemen']}). Kamu memperoleh **+{gained} Poin** "
                                f"({current_question_pts} Dasar + {speed_bonus} Kecepatan + {streak_bonus} Streak)!"
                            )
                        else:
                            st.session_state.surv_lives -= 1
                            st.session_state.surv_streak = 0
                            st.session_state.surv_last_ok = False
                            st.session_state.surv_last_msg = (
                                f"❌ **Jawaban Salah!** Sosok yang benar adalah **{q['nama']}** "
                                f"({q['jabatan']} - {q['departemen']}). Nyawa berkurang 1!"
                            )
                        st.rerun()
        else:
            if st.session_state.surv_last_ok:
                st.success(st.session_state.surv_last_msg)
            else:
                st.error(st.session_state.surv_last_msg)

            if st.session_state.surv_lives > 0:
                if st.button("➡️ Lanjut ke Soal Berikutnya", type="primary", use_container_width=True):
                    st.session_state.surv_round += 1
                    prepare_next_question()
                    st.rerun()
            else:
                st.rerun()

    else:
        st.markdown("</div>", unsafe_allow_html=True)
        st.error("💥 **NYAWA HABIS! EKSPEDISI SURVIVAL BERAKHIR**")
        st.markdown(
            f"<h3 style='text-align:center;color:#ffd740;'>Skor Akhir Kamu: {st.session_state.surv_score} Poin "
            f"(Streak Terbaik: {st.session_state.surv_best_streak}x)</h3>",
            unsafe_allow_html=True,
        )

        fb = st.session_state.get("surv_lb_feedback")
        if fb:
            ok_fb, msg_fb = fb
            if ok_fb:
                st.success(msg_fb)
            else:
                st.warning(msg_fb)

        if not st.session_state.surv_saved and st.session_state.surv_score > 0:
            with st.form("save_lb_form"):
                st.markdown("#### 🏛️ Abadikan Namamu di Prasasti Leaderboard")
                st.caption("🔒 **Proteksi Otomatis 1 Perangkat = 1 Slot:** Perangkat kamu otomatis dikenali sistem. Jika kamu bermain lagi, hanya rekor tertinggimu yang diperbarui agar papan skor bebas spam.")
                f_c1, f_c2 = st.columns(2)
                with f_c1:
                    in_kelompok = st.selectbox("Pilih Konstelasi / Status Resmi:", DAFTAR_KELOMPOK_RESMI)
                with f_c2:
                    in_nama = st.text_input("Nama Panggilan (Maks 16 Huruf, Sopan):", placeholder="Contoh: Rafli", max_chars=16)
                if st.form_submit_button("💾 Simpan ke Prasasti Skor", type="primary", use_container_width=True):
                    ok_save, msg_save = save_score_to_leaderboard(
                        in_nama,
                        in_kelompok,
                        st.session_state.surv_score,
                        st.session_state.surv_best_streak,
                    )
                    st.session_state.surv_lb_feedback = (ok_save, msg_save)
                    if ok_save:
                        st.session_state.surv_saved = True
                    st.rerun(scope="fragment")

        if st.button("🔄 Mulai Survival Baru (Reset 3 Nyawa)", type="primary", use_container_width=True):
            del st.session_state["surv_lives"]
            st.rerun(scope="app")

    # ===== SEKSI LEADERBOARD DI BAWAH (ISOLASI FRAGMENT AGAR CEPAT & TANPA RELOAD HALAMAN) =====
    @st.fragment
    def _render_leaderboard_section():
        st.markdown("---")
        st.markdown("### 🏆 Prasasti Skor Jordan (Leaderboard)")
        st.caption("Papan peringkat penjelajah bintang Konstelasi Jordan.")
        lb_period = st.radio(
            "Periode Papan Skor:",
            ["🏛️ Prasasti Abadi (All-Time Artefak)", "🔥 Musim Bulan Ini (Monthly)"],
            horizontal=True,
            key="lb_period_radio"
        )
        lb_div = st.tabs(["🎮 Player (10 Konstelasi)", "👑 Senior / Mentor"])

        store = get_global_leaderboard()
        now_month = datetime.now().strftime("%Y-%m")
        raw_entries = store["entries"]
        if "Bulan Ini" in lb_period:
            raw_entries = [e for e in raw_entries if _normalize_month_str(e.get("bulan")) == now_month]

        with lb_div[0]:
            player_list = [e for e in raw_entries if e.get("kategori", "player") in ("player", "kader")][:10]
            if not player_list:
                st.info("Belum ada skor Player pada periode ini. Jadilah yang pertama!")
            else:
                rows_html = ""
                for idx, item in enumerate(player_list, 1):
                    medal = "🥇" if idx == 1 else ("🥈" if idx == 2 else ("🥉" if idx == 3 else f"#{idx:02d}"))
                    clean_tgl = _format_clean_date(item.get("tanggal", ""))
                    tgl_html = f"<span style='font-size:0.78em;color:#78909c;margin-left:6px;'>({clean_tgl})</span>" if clean_tgl else ""
                    rows_html += (
                        f"<div class='lb-row'>"
                        f"<span class='lb-rank'>{medal}</span>"
                        f"<span class='lb-name'>{item['nama']} {tgl_html}</span>"
                        f"<span class='lb-group'>{item['kelompok']}</span>"
                        f"<span class='lb-score'>{item['skor']} pts</span>"
                        f"</div>"
                    )
                st.markdown(f"<div class='lb-card'>{rows_html}</div>", unsafe_allow_html=True)

        with lb_div[1]:
            kating_list = [e for e in raw_entries if e.get("kategori") in ("kating", "senior", "mentor")][:10]
            if not kating_list:
                st.info("Belum ada Senior / Mentor yang mencatatkan skor di periode ini.")
            else:
                rows_html = ""
                for idx, item in enumerate(kating_list, 1):
                    medal = "👑" if idx == 1 else f"#{idx:02d}"
                    clean_tgl = _format_clean_date(item.get("tanggal", ""))
                    tgl_html = f"<span style='font-size:0.78em;color:#78909c;margin-left:6px;'>({clean_tgl})</span>" if clean_tgl else ""
                    rows_html += (
                        f"<div class='lb-row'>"
                        f"<span class='lb-rank'>{medal}</span>"
                        f"<span class='lb-name'>{item['nama']} {tgl_html}</span>"
                        f"<span class='lb-group'>{item.get('kelompok', 'Pengurus HMSD')}</span>"
                        f"<span class='lb-score'>{item['skor']} pts</span>"
                        f"</div>"
                    )
                st.markdown(f"<div class='lb-card'>{rows_html}</div>", unsafe_allow_html=True)

    _render_leaderboard_section()


# ==============================================================================
# GAME 2: NEON TACTICS: TIC-TAC-TOE vs MINIMAX AI (FULL WIDTH, AUTO-FIT IFRAME)
# ==============================================================================
elif active_game == "Neon Tactics AI":
    ttt_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Poppins:wght@400;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
  html, body {
    width: 100%;
    background: transparent;
    color: #e2e8f0;
    font-family: 'Poppins', sans-serif;
    padding: 4px;
    overflow-x: hidden;
    overflow-y: auto;
  }
  .arena-wrap {
    width: 100%;
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 24px;
    background: linear-gradient(160deg, #121428 0%, #090a16 100%);
    border: 1px solid rgba(255, 215, 64, 0.32);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65);
  }
  @media (max-width: 760px) {
    .arena-wrap { grid-template-columns: 1fr; padding: 14px; gap: 16px; }
  }
  .board-col {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .status-banner {
    width: 100%;
    max-width: 360px;
    text-align: center;
    padding: 10px 14px;
    border-radius: 10px;
    background: rgba(255, 215, 64, 0.1);
    border: 1px solid rgba(255, 215, 64, 0.35);
    color: #ffd740;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 16px;
    letter-spacing: 0.8px;
  }
  .grid-3x3 {
    display: grid;
    grid-template-columns: repeat(3, 110px);
    grid-template-rows: repeat(3, 110px);
    gap: 12px;
  }
  @media (max-width: 480px) {
    .grid-3x3 {
      grid-template-columns: repeat(3, 86px);
      grid-template-rows: repeat(3, 86px);
      gap: 8px;
    }
  }
  .cell {
    background: rgba(18, 21, 44, 0.95);
    border: 1.5px solid rgba(255, 215, 64, 0.28);
    border-radius: 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    position: relative;
    transition: all 0.2s ease;
    box-shadow: inset 0 0 16px rgba(0, 0, 0, 0.6);
  }
  .cell:hover:not(.taken) {
    border-color: #ffd740;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(255, 215, 64, 0.2);
  }
  .cell.win-cell {
    background: rgba(255, 215, 64, 0.22);
    border-color: #ffd740;
    box-shadow: 0 0 24px rgba(255, 215, 64, 0.55);
  }
  .mark-x {
    font-size: 44px;
    font-weight: 900;
    color: #ffd740;
    text-shadow: 0 0 14px rgba(255, 215, 64, 0.8);
    animation: popIn 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .mark-o {
    font-size: 42px;
    font-weight: 900;
    color: #80d8ff;
    text-shadow: 0 0 14px rgba(128, 216, 255, 0.8);
    animation: popIn 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  @keyframes popIn {
    from { transform: scale(0.3); opacity: 0; }
    to { transform: scale(1); opacity: 1; }
  }
  .xray-tag {
    position: absolute;
    bottom: 7px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 5px;
    background: rgba(0, 0, 0, 0.68);
  }
  .side-panel {
    display: flex;
    flex-direction: column;
    gap: 14px;
    justify-content: space-between;
  }
  .panel-box {
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(255, 215, 64, 0.22);
    border-radius: 14px;
    padding: 16px 18px;
  }
  .panel-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11.5px;
    font-weight: 700;
    color: #ffd740;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }
  .score-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    text-align: center;
  }
  .score-item {
    background: rgba(0, 0, 0, 0.35);
    border-radius: 10px;
    padding: 10px 6px;
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
  .score-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 22px;
    font-weight: 800;
    color: #ffd740;
  }
  .score-lbl {
    font-size: 11px;
    color: #90a4ae;
    margin-top: 2px;
  }
  .ctrl-btn {
    width: 100%;
    padding: 12px 14px;
    border-radius: 10px;
    border: 1px solid rgba(255, 215, 64, 0.45);
    background: linear-gradient(135deg, #ffd740, #ff9800);
    color: #090a14;
    font-family: 'Poppins', sans-serif;
    font-weight: 800;
    font-size: 13.5px;
    cursor: pointer;
    transition: transform 0.15s ease;
  }
  .ctrl-btn:hover { transform: translateY(-1px); }
  .ctrl-select {
    width: 100%;
    padding: 9px 12px;
    border-radius: 9px;
    background: #0d1022;
    color: #ffd740;
    border: 1px solid rgba(255, 215, 64, 0.35);
    font-family: 'Poppins', sans-serif;
    font-size: 13px;
    font-weight: 600;
  }
  .toggle-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 13px;
    color: #cfd8dc;
    margin-top: 10px;
  }
</style>
</head>
<body>
<div class="arena-wrap" id="root-wrap">
  <div class="board-col">
    <div class="status-banner" id="status">✦ GILIRANMU: TEMPATKAN BINTANG (✦) ✦</div>
    <div class="grid-3x3" id="board"></div>
  </div>
  <div class="side-panel">
    <div class="panel-box">
      <div class="panel-title">📊 TELEMETRI PERTANDINGAN</div>
      <div class="score-row">
        <div class="score-item"><div class="score-val" id="sc-win">0</div><div class="score-lbl">KAMU (✦)</div></div>
        <div class="score-item"><div class="score-val" id="sc-draw" style="color:#cfd8dc;">0</div><div class="score-lbl">SERI</div></div>
        <div class="score-item"><div class="score-val" id="sc-ai" style="color:#80d8ff;">0</div><div class="score-lbl">JORDAN AI (◈)</div></div>
      </div>
    </div>

    <div class="panel-box">
      <div class="panel-title">🧠 KONFIGURASI MINIMAX AI</div>
      <select class="ctrl-select" id="ai-mode">
        <option value="unbeatable">Omniscient Minimax (Mustahil Kalah)</option>
        <option value="tactician">Star Tactician (Menengah)</option>
        <option value="novice">Novice Star (Mudah)</option>
      </select>
      <label class="toggle-row">
        <span>🔬 Tampilkan Skor Pikiran AI (X-Ray)</span>
        <input type="checkbox" id="xray-toggle" checked style="accent-color:#ffd740;width:17px;height:17px;">
      </label>
      <div style="font-size:12px;color:#b0bec5;margin-top:10px;line-height:1.55;">
        Saat <b>X-Ray</b> aktif, setiap kotak kosong menampilkan nilai evaluasi Minimax secara langsung:
        <span style="color:#ff5252;font-weight:700;">+10 (AI Menang)</span>,
        <span style="color:#ffd740;font-weight:700;">0 (Seri)</span>, atau
        <span style="color:#00e676;font-weight:700;">-10 (Kamu Menang)</span>.
      </div>
    </div>

    <button class="ctrl-btn" id="reset-btn">🔄 Mulai Ronde Baru</button>
  </div>
</div>

<script>
(function() {
  // Paksa iframe parent di Streamlit agar 100% lebar penuh dan tinggi pas
  function fitFrame() {
    try {
      if (window.frameElement) {
        window.frameElement.style.width = '100%';
        window.frameElement.style.minWidth = '100%';
        if (window.frameElement.parentElement) {
          window.frameElement.parentElement.style.width = '100%';
        }
        const h = document.getElementById('root-wrap').offsetHeight + 20;
        window.frameElement.style.height = Math.max(460, h) + 'px';
      }
    } catch (e) {}
  }
  window.addEventListener('resize', fitFrame);
  if (typeof ResizeObserver !== 'undefined') { new ResizeObserver(fitFrame).observe(document.body); }
  setTimeout(fitFrame, 50);
  setTimeout(fitFrame, 300);

  const WIN_LINES = [
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ];
  let board = Array(9).fill('');
  let gameOver = false;
  let winCells = [];
  let scores = { win: 0, draw: 0, ai: 0 };

  const boardEl = document.getElementById('board');
  const statusEl = document.getElementById('status');
  const xrayEl = document.getElementById('xray-toggle');
  const modeEl = document.getElementById('ai-mode');

  function getWinner(b) {
    for (const [a, c, d] of WIN_LINES) {
      if (b[a] && b[a] === b[c] && b[a] === b[d]) {
        return { player: b[a], line: [a, c, d] };
      }
    }
    if (!b.includes('')) return { player: 'D', line: [] };
    return null;
  }

  function minimax(b, depth, isMax) {
    const res = getWinner(b);
    if (res) {
      if (res.player === 'O') return 10 - depth;
      if (res.player === 'X') return depth - 10;
      return 0;
    }
    if (isMax) {
      let best = -999;
      for (let i = 0; i < 9; i++) {
        if (!b[i]) {
          b[i] = 'O';
          best = Math.max(best, minimax(b, depth + 1, false));
          b[i] = '';
        }
      }
      return best;
    } else {
      let best = 999;
      for (let i = 0; i < 9; i++) {
        if (!b[i]) {
          b[i] = 'X';
          best = Math.min(best, minimax(b, depth + 1, true));
          b[i] = '';
        }
      }
      return best;
    }
  }

  function evaluateAllMoves(b) {
    const evals = {};
    for (let i = 0; i < 9; i++) {
      if (!b[i]) {
        b[i] = 'O';
        evals[i] = minimax(b, 0, false);
        b[i] = '';
      }
    }
    return evals;
  }

  function render() {
    boardEl.innerHTML = '';
    const showXray = xrayEl.checked && !gameOver;
    const evals = showXray ? evaluateAllMoves(board.slice()) : {};

    for (let i = 0; i < 9; i++) {
      const cell = document.createElement('div');
      cell.className = 'cell' + (board[i] ? ' taken' : '') + (winCells.includes(i) ? ' win-cell' : '');
      if (board[i] === 'X') {
        cell.innerHTML = '<span class="mark-x">✦</span>';
      } else if (board[i] === 'O') {
        cell.innerHTML = '<span class="mark-o">◈</span>';
      } else if (showXray && evals[i] !== undefined) {
        const sc = evals[i];
        const col = sc > 0 ? '#ff5252' : (sc < 0 ? '#00e676' : '#ffd740');
        const prefix = sc > 0 ? '+' : '';
        cell.innerHTML = '<span class="xray-tag" style="color:' + col + '">AI:' + prefix + sc + '</span>';
      }
      cell.addEventListener('click', () => handlePlayerMove(i));
      boardEl.appendChild(cell);
    }
    fitFrame();
  }

  function handlePlayerMove(idx) {
    if (gameOver || board[idx]) return;
    board[idx] = 'X';
    if (checkEnd()) return;

    statusEl.textContent = '◈ JORDAN AI SEDANG MENGHITUNG POHON KEPUTUSAN...';
    render();

    setTimeout(() => {
      const empty = board.map((v, i) => v === '' ? i : -1).filter(i => i !== -1);
      if (!empty.length) return;
      const mode = modeEl.value;
      let chosen = empty[0];

      if (mode === 'novice' || (mode === 'tactician' && Math.random() < 0.45)) {
        chosen = empty[Math.floor(Math.random() * empty.length)];
      } else {
        let bestScore = -999;
        for (const i of empty) {
          board[i] = 'O';
          const sc = minimax(board, 0, false);
          board[i] = '';
          if (sc > bestScore) {
            bestScore = sc;
            chosen = i;
          }
        }
      }
      board[chosen] = 'O';
      if (!checkEnd()) {
        statusEl.textContent = '✦ GILIRANMU: TEMPATKAN BINTANG (✦) ✦';
        render();
      }
    }, 180);
  }

  function checkEnd() {
    const res = getWinner(board);
    if (!res) return false;
    gameOver = true;
    winCells = res.line;
    if (res.player === 'X') {
      scores.win++;
      document.getElementById('sc-win').textContent = scores.win;
      statusEl.textContent = '🏆 LUAR BIASA! KAMU MENGALAHKAN JORDAN AI!';
    } else if (res.player === 'O') {
      scores.ai++;
      document.getElementById('sc-ai').textContent = scores.ai;
      statusEl.textContent = '◈ JORDAN AI MENANG! MINIMAX MENEMUKAN CELAHMU.';
    } else {
      scores.draw++;
      document.getElementById('sc-draw').textContent = scores.draw;
      statusEl.textContent = '⚖️ SEIMBANG (SERI)! PERTAHANAN SEMPURNA.';
    }
    render();
    return true;
  }

  document.getElementById('reset-btn').addEventListener('click', () => {
    board = Array(9).fill('');
    gameOver = false;
    winCells = [];
    statusEl.textContent = '✦ GILIRANMU: TEMPATKAN BINTANG (✦) ✦';
    render();
  });
  xrayEl.addEventListener('change', render);
  render();
})();
</script>
</body>
</html>"""
    components.html(ttt_html, height=480, scrolling=False)


# ==============================================================================

# ==============================================================================
# GAME 3-5: HTML DIPISAH KE FOLDER tools/arcade/ AGAR KREASI.py TETAP RAPI
# ==============================================================================
ARCADE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arcade")


def load_arcade_html(filename: str) -> str:
    path = os.path.join(ARCADE_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"<div style='color:#ff8a80;font-family:sans-serif;padding:20px'>Gagal memuat {filename}: {e}</div>"


# Wajah bola. Kunci = nama bola di game. Nilai = judul artikel Wikipedia ATAU path file lokal.
# DEBUG: kalau wajah tidak muncul, taruh foto manual di template_code/assets/faces/<nama>.jpg (contoh: jordan.jpg)
BALL_FACE_SOURCES = {
    "Jordan": "Camille_Jordan",
    "Jacobi": "Carl_Gustav_Jacob_Jacobi",
    "Poisson": "Siméon_Denis_Poisson",
    "Gauss": "Carl_Friedrich_Gauss",
    "Lagrange": "Joseph-Louis_Lagrange",
    "Laplace": "Pierre-Simon_Laplace",
    "Taylor": "Brook_Taylor",
    "Euler": "Leonhard_Euler",
    "Bayes": "Thomas_Bayes",
}


def _img_to_face_b64(img, top_bias: float = 0.12) -> str:
    """Potong persegi (agak ke atas supaya wajah masuk), kecilkan, lalu jadikan data URL."""
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    s = min(w, h)
    left = (w - s) // 2
    top = int(max(0, min(h - s, (h - s) * 0.5 if w >= h else h * top_bias)))
    img = img.crop((left, top, left + s, top + s)).resize((128, 128), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=82)
    import base64
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")


@st.cache_data(ttl=86400, max_entries=2, show_spinner=False)
def load_ball_faces() -> dict:
    faces = {}
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    local_dir = os.path.join(base_dir, "assets", "faces")
    headers = {"User-Agent": "JordanArcade/1.0 (Buku Kating HMSD ITERA; edukasi)"}
    names = list(BALL_FACE_SOURCES.keys()) + ["Rafli"]
    for name in names:
        # 1) Prioritas: file lokal assets/faces/<nama>.jpg|png
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            p = os.path.join(local_dir, name.lower() + ext)
            if os.path.exists(p):
                try:
                    faces[name] = _img_to_face_b64(Image.open(p))
                except Exception:
                    pass
                break
        if name in faces:
            continue
        try:
            if name == "Rafli":
                foto = next((m["foto"] for m in ANGGOTA_JORDAN if m["nama"].startswith("Muhammad Rafli")), "")
                img = load_quiz_photo(foto) if foto else None
                if img is not None:
                    faces[name] = _img_to_face_b64(img, top_bias=0.05)
                continue
            # 2) Wikipedia: ambil thumbnail potret matematikawan
            title = BALL_FACE_SOURCES[name]
            meta = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}", headers=headers, timeout=8).json()
            src = (meta.get("thumbnail") or meta.get("originalimage") or {}).get("source")
            if not src:
                continue
            r = requests.get(src, headers=headers, timeout=8)
            if r.status_code == 200:
                faces[name] = _img_to_face_b64(Image.open(BytesIO(r.content)))
        except Exception:
            continue
    return faces


if active_game == "Pathfinding Race":
    st.markdown("### 🧭 Pathfinding Lab: Adu Algoritma Pencarian")
    st.caption(
        "Pilih dua algoritma lalu adu di peta yang sama. Bandingkan **Blind Search** (BFS, DFS, UCS) dengan "
        "**Informed Search** (Greedy, A*) di peta graf kampus, medan berbobot, jebakan U, dan labirin. "
        "Atur kecepatan dengan slider atau jalankan per langkah dengan tombol **Step**."
    )
    components.html(load_arcade_html("game3_pathfinding.html"), height=860, scrolling=False)

elif active_game == "Gauss-Jordan Puzzle":
    st.markdown("### 🧮 Gauss-Jordan Puzzle: Jordan Menaklukkan Matriks")
    st.caption(
        "Kelompok Jordan, metode Gauss-**Jordan**. Pakai tiga operasi baris elementer untuk mengubah matriks "
        "menjadi identitas dan temukan solusi SPL. Makin sedikit langkah dan hint, makin tinggi skornya."
    )
    components.html(load_arcade_html("game4_gauss_jordan.html"), height=700, scrolling=False)

elif active_game == "Ball Battle Arena":
    st.markdown("### ⚡ Ball Arena: Race & Fight")
    st.caption(
        "**🏁 Race**: balapan bola jatuh di 3 lintasan. **⚔️ Fight**: tanpa gravitasi, bola memantul sesuai pola. "
        "Pilih *Battle Royale* (power-up) atau *Duel 1v1* (senjata yang makin kuat tiap kena). "
        "Peserta custom disimpan hanya di perangkatmu."
    )
    with st.spinner("Menyiapkan wajah para peserta..."):
        faces = load_ball_faces()
    html = load_arcade_html("game5_ball_arena.html").replace("__FACES_JSON__", json.dumps(faces))
    components.html(html, height=900, scrolling=False)
    missing = [n for n in BALL_FACE_SOURCES if n not in faces]
    if missing:
        st.caption(
            "ℹ️ Wajah belum termuat untuk: " + ", ".join(missing)
            + ". Bola tetap tampil dengan kode nama. Untuk memaksa, taruh foto di `assets/faces/<nama>.jpg`."
        )
