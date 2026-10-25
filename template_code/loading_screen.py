import streamlit as st
import streamlit.components.v1 as components
from concurrent.futures import ThreadPoolExecutor, wait
from PIL import Image, ImageOps
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except Exception:
    pass
from io import BytesIO
import requests
import base64
import time
import os
import re

# ========================================================================
# KONFIGURASI TATA SURYA JORDAN - UBAH FOTO DI SINI
# ========================================================================

FOTO_MENTOR = "https://drive.google.com/uc?export=view&id=1XSOLkGiiUzZG4DWbOTatlkscwcaFhrty"
NAMA_MENTOR  = "Kak Yollanda Agustina"

DURASI_MINIMUM  = 3.2 # detik (optimal: animasi planet terasa mulus & tidak membuat pengguna menunggu lama)
DURASI_MAKSIMUM = 5.0 # detik (batas maksimal preload agar transisi ke web tetap responsif)

# Foto 13 anggota: bebas isi link Google Drive (format apa pun) atau nama file lokal.
# Jika dikosongkan (""), otomatis memakai avatar inisial sesuai warna orbitnya.
FOTO_ANGGOTA = {
    "Bintang": "https://drive.google.com/uc?export=view&id=1KPiPBu6qnc-7uAcvTlfVxfvw3P3ojjPY",
    "Najwa":   "https://drive.google.com/uc?export=view&id=1TWNgccBsATeQyTnJdCx30lPXOk-lF0JP",
    "Rafli":   "https://drive.google.com/uc?export=view&id=1CUqKHr8nql3b9ifOLu0-cvcwrUxVe0L5",
    "Abyan":   "https://drive.google.com/uc?export=view&id=1i9oSkeFZT1sL0SJmMWmZb4l_qPCxAV-4",
    "Bayu":    "https://drive.google.com/uc?export=view&id=1AeNI3iwCdGOXgrjncpYatIqfuv4qvZ3W",
    "Mojes":   "https://drive.google.com/uc?export=view&id=114wxxW8dyiUPBz87C3IyQJOyyl2M29kw",
    "Iva":     "https://drive.google.com/uc?export=view&id=1Kz0h3yq36ZDbBLIovx6MtEHTXlD_Nj5r",
    "Astrit":  "https://drive.google.com/uc?export=view&id=1D-_sGW7jHoUpCms068h97XYi4fdLxHMc",
    "Septi":   "https://drive.google.com/uc?export=view&id=15eNIKvQctlDzyoHUjK5GI55pAKK8F3g2",
    "Fildzah": "https://drive.google.com/uc?export=view&id=13yOwhEQH_zVkrbuGiohD--90zVLc_zQK",
    "Lintar":  "https://drive.google.com/uc?export=view&id=1fkdAu5a7UGyEBMMcIcysaN3f04fM2PVd",
    "Biwa":    "https://drive.google.com/uc?export=view&id=16JerAO1bW_lVSKEYSVi8qSo3qeWCqfzO",
    "Bening":  "https://drive.google.com/uc?export=view&id=1wqq9-YkpFJ7D6_WQyKqKsg6UWvXzku-4",
}

# Daftar URL aset Halaman Utama yang ikut di-preload selama loading screen berjalan
PRELOAD_URLS_HALAMAN_UTAMA = [
    "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx",  # Logo HMSD
    "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb",  # Logo PSDA
    "https://drive.google.com/uc?export=view&id=1LyKEh4RgNJDA0LM8yzFdpslHhCVzi3fs",  # Foto Konstelasi Jordan
]

# Data 13 Anggota Jordan
ANGGOTA_JORDAN = [
    {"nama":"Bintang","full":"Bintang Mahardika","badge":"Palu","c1":"#ffd740","c2":"#ff8f00","ring":True,"sz":46,"orb":1,"d":0},
    {"nama":"Najwa","full":"Sayyidina Najwa Syahra","badge":"Bulu","c1":"#ff4081","c2":"#c2185b","ring":False,"sz":44,"orb":1,"d":-8},
    {"nama":"Rafli","full":"Muhammad Rafli Raditya","badge":"","c1":"#40c4ff","c2":"#0288d1","ring":False,"sz":46,"orb":2,"d":0},
    {"nama":"Abyan","full":"M Abyan Alghaniyyu","badge":"","c1":"#69f0ae","c2":"#00bfa5","ring":False,"sz":44,"orb":2,"d":-8},
    {"nama":"Bayu","full":"Rahmad Bayu Ridho","badge":"","c1":"#00e5ff","c2":"#0091ea","ring":True,"sz":46,"orb":2,"d":-16},
    {"nama":"Mojes","full":"Mojes Wijaya","badge":"","c1":"#ffab40","c2":"#ff6d00","ring":False,"sz":46,"orb":3,"d":-3},
    {"nama":"Iva","full":"Iva Aulia Sofia","badge":"","c1":"#ff80ab","c2":"#f50057","ring":False,"sz":44,"orb":3,"d":-14},
    {"nama":"Astrit","full":"Astrit Aisya Rahmi","badge":"","c1":"#b388ff","c2":"#651fff","ring":False,"sz":44,"orb":3,"d":-24},
    {"nama":"Septi","full":"Septi Widia Arini","badge":"","c1":"#ff5252","c2":"#d50000","ring":False,"sz":44,"orb":4,"d":-5},
    {"nama":"Fildzah","full":"Fildzah Cahya Kamila","badge":"","c1":"#7c4dff","c2":"#304ffe","ring":False,"sz":44,"orb":4,"d":-19},
    {"nama":"Lintar","full":"Lintar Abhinaya Putra Zulmi","badge":"","c1":"#ffd54f","c2":"#f57f17","ring":False,"sz":46,"orb":4,"d":-33},
    {"nama":"Biwa","full":"Ahda Nabiwa","badge":"","c1":"#1de9b6","c2":"#00897b","ring":True,"sz":46,"orb":5,"d":-10},
    {"nama":"Bening","full":"Bening Arianti","badge":"","c1":"#80d8ff","c2":"#0091ea","ring":False,"sz":44,"orb":5,"d":-37},
]


# ========================================================================
# HELPERS: PENGUNDUH GAMBAR GOOGLE DRIVE & LOKAL -> BASE64 (ANTI BLOKIR)
# ========================================================================

_PRELOAD_RAW_CACHE = {}


def _extract_drive_id(url: str) -> str:
    """Ekstrak file ID dari berbagai bentuk URL Google Drive."""
    if not url:
        return ""
    url = url.strip()
    for pat in (r"[?&]id=([\w-]{10,})", r"/file/d/([\w-]{10,})", r"/d/([\w-]{10,})"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    if re.fullmatch(r"[\w-]{20,}", url):
        return url
    return ""


def _download_raw_bytes(url: str, timeout: float = 6.0):
    """Unduh bytes gambar dari URL/Google Drive dengan fallback endpoint agar tidak terblokir browser."""
    if not url or not url.strip():
        return None
    url = url.strip()
    if url in _PRELOAD_RAW_CACHE:
        return _PRELOAD_RAW_CACHE[url]

    gid = _extract_drive_id(url)
    candidates = [url]
    if gid:
        candidates = [
            f"https://drive.google.com/thumbnail?id={gid}&sz=w600",
            f"https://lh3.googleusercontent.com/d/{gid}=w600",
            f"https://drive.google.com/uc?export=view&id={gid}",
        ]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for cand in candidates:
        try:
            resp = requests.get(cand, headers=headers, timeout=timeout)
            ctype = resp.headers.get("Content-Type", "").lower()
            if resp.status_code == 200 and resp.content and "html" not in ctype:
                # Pastikan benar-benar file gambar yang bisa dibuka PIL (bukan halaman HTML error Drive)
                Image.open(BytesIO(resp.content)).verify()
                if len(_PRELOAD_RAW_CACHE) >= 28:
                    _PRELOAD_RAW_CACHE.pop(next(iter(_PRELOAD_RAW_CACHE)), None)
                _PRELOAD_RAW_CACHE[url] = resp.content
                return resp.content
        except Exception:
            continue
    return None


def _pil_to_square_b64(img: Image.Image, max_dim: int = 140, quality: int = 75) -> str:
    """Potong gambar menjadi persegi proporsional (agak ke atas untuk wajah), kecilkan, dan ubah ke Base64."""
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = int((h - side) * 0.18) if h > w else (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    img.thumbnail((max_dim, max_dim), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{b64}"


def _resolve_source_to_b64_worker(src: str, max_dim: int = 140) -> str:
    """
    Ubah file lokal ATAU link Google Drive/HTTP menjadi data URI Base64.
    Dengan Base64 langsung dari Python, foto dijamin 100% tampil di iframe tanpa diblokir CORB browser.
    """
    if not src or not src.strip():
        return ""
    src = src.strip()

    # 1. Cek jika berupa path file lokal
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for candidate_path in (src, os.path.join(base_dir, src)):
        if os.path.exists(candidate_path) and os.path.isfile(candidate_path):
            try:
                return _pil_to_square_b64(Image.open(candidate_path), max_dim=max_dim)
            except Exception:
                pass

    # 2. Cek jika berupa URL (Google Drive / HTTP) atau ID Google Drive
    if src.startswith("http") or _extract_drive_id(src):
        raw = _download_raw_bytes(src, timeout=6.0)
        if raw:
            try:
                return _pil_to_square_b64(Image.open(BytesIO(raw)), max_dim=max_dim)
            except Exception:
                pass

    return ""


@st.cache_data(ttl=86400, max_entries=32, show_spinner=False)
def _resolve_source_to_b64(src: str, max_dim: int = 140) -> str:
    return _resolve_source_to_b64_worker(src, max_dim=max_dim)


def _get_mentor_b64() -> str:
    if not FOTO_MENTOR:
        return ""
    return _resolve_source_to_b64(FOTO_MENTOR, max_dim=200)


def _resolve_photo(nama: str, color_hex: str, preloaded_map: dict) -> str:
    if nama in preloaded_map and preloaded_map[nama]:
        return preloaded_map[nama]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        for folder in ("", os.path.join(base_dir, "assets", "faces"), base_dir):
            local = os.path.join(folder, f"{nama.lower()}{ext}") if folder else f"{nama.lower()}{ext}"
            if os.path.exists(local):
                b64 = _resolve_source_to_b64(local, max_dim=128)
                if b64:
                    return b64

    bg = color_hex.replace("#", "")
    return f"https://ui-avatars.com/api/?name={nama}&background={bg}&color=fff&size=96&bold=true&rounded=true"


_LOADING_B64_CACHE = {}

def _prepare_all_loading_photos() -> tuple[str, dict]:
    """Unduh foto Mentor dan 13 Anggota secara paralel; hanya menyimpan ke cache jika berhasil (anti-cache kosong saat offline)."""
    tasks = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        if FOTO_MENTOR and FOTO_MENTOR.strip():
            if not _LOADING_B64_CACHE.get("__mentor__"):
                tasks["__mentor__"] = pool.submit(_resolve_source_to_b64_worker, FOTO_MENTOR.strip(), 200)
        for nama, url_or_path in FOTO_ANGGOTA.items():
            if url_or_path and url_or_path.strip():
                if not _LOADING_B64_CACHE.get(nama):
                    tasks[nama] = pool.submit(_resolve_source_to_b64_worker, url_or_path.strip(), 128)

    for key, fut in tasks.items():
        try:
            res = fut.result(timeout=7.5)
        except Exception:
            res = ""
        if res:
            _LOADING_B64_CACHE[key] = res

    mentor_b64 = _LOADING_B64_CACHE.get("__mentor__", "")
    member_b64_map = {nama: _LOADING_B64_CACHE.get(nama, "") for nama in FOTO_ANGGOTA}
    return mentor_b64, member_b64_map


# ========================================================================
# HTML BUILDER - OPTIMIZED
# ========================================================================

def _build_html(mentor_src: str, member_b64_map: dict, dur_sec: float) -> str:
    ring_specs = {
        1: {"r": 115, "p": 16},
        2: {"r": 178, "p": 24},
        3: {"r": 240, "p": 32},
        4: {"r": 305, "p": 42},
        5: {"r": 370, "p": 54},
    }

    planets_html = ""
    for idx, m in enumerate(ANGGOTA_JORDAN):
        sp = ring_specs[m["orb"]]
        r, period = sp["r"], sp["p"]
        sz, hs = m["sz"], m["sz"] / 2
        delay = m["d"]
        photo = _resolve_photo(m["nama"], m["c1"], member_b64_map)
        ring_el = f'<div class="p-ring" style="border-color:{m["c1"]}"></div>' if m.get("ring") else ""
        badge_el = f'<span class="p-badge">{m["badge"]}</span>' if m.get("badge") else ""

        planets_html += f"""<div class="o-arm" style="width:{r*2}px;height:{r*2}px;margin:-{r}px 0 0 -{r}px;animation:cw {period}s linear infinite {delay}s">
<div class="p-h" style="top:0;left:50%;margin:-{hs}px 0 0 -{hs}px;width:{sz}px;height:{sz}px" title="{m['full']}">
<div class="p-i" style="animation:ccw {period}s linear infinite {delay}s">
{ring_el}
<div class="p-card" id="c{idx}">
<div class="c-f" style="background:radial-gradient(circle at 35% 35%,{m['c1']},{m['c2']})"></div>
<div class="c-b" style="border-color:{m['c1']}"><img src="{photo}" class="m-ph" alt="{m['nama']}" onerror="this.onerror=null;this.src='https://ui-avatars.com/api/?name={m['nama']}&background=1a1a2e&color=ffd740&size=96&bold=true'"></div>
</div>
<div class="p-lbl"><span class="p-nm">{m['nama']}</span>{badge_el}</div>
</div></div></div>
"""

    tracks = ""
    for _, sp in ring_specs.items():
        r = sp["r"]
        tracks += f'<div class="o-trk" style="width:{r*2}px;height:{r*2}px;margin:-{r}px 0 0 -{r}px"></div>\n'

    sun_fallback = f"https://ui-avatars.com/api/?name={NAMA_MENTOR.replace(' ', '+')}&background=ffd740&color=0f0a21&size=160&bold=true"
    sun_face = (
        f'<img src="{mentor_src}" class="sun-img" alt="{NAMA_MENTOR}" onerror="this.onerror=null;this.src=\'{sun_fallback}\'">'
        if mentor_src
        else '<div style="font-size:40px">&#9728;&#65039;</div>'
    )

    dur_ms = int(max(1, dur_sec) * 1000)

    import random
    rng = random.Random(42)
    shadows = []
    for _ in range(50):
        x = rng.randint(0, 2000)
        y = rng.randint(0, 1200)
        s = rng.choice([1, 1, 1, 2])
        shadows.append(f"{x}px {y}px 0 {s-1}px rgba(255,255,255,{rng.uniform(0.3, 0.9):.2f})")
    star_shadows = ",".join(shadows)

    return f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:100%;height:100%;overflow:hidden;background:#04030a;font-family:'Poppins',sans-serif;user-select:none}}

/* Antariksa: 1 DOM element, 50 bintang via box-shadow */
#sp{{position:fixed;inset:0;background:radial-gradient(ellipse at center,#12082a 0%,#07041a 50%,#030209 100%);z-index:0}}
#sp::after{{content:'';position:absolute;width:1px;height:1px;box-shadow:{star_shadows};animation:tw 4s ease-in-out infinite alternate}}
@keyframes tw{{0%{{opacity:.5}}100%{{opacity:1}}}}

/* Komet: ringan, jarang tampil */
.comet{{position:absolute;top:12%;left:85%;width:100px;height:1.5px;background:linear-gradient(90deg,#ffd740,transparent);transform:rotate(-35deg);opacity:0;animation:sh 9s ease-in-out infinite}}
@keyframes sh{{0%{{opacity:0;transform:translate(0,0) rotate(-35deg)}}4%{{opacity:.8}}10%{{transform:translate(-500px,350px) rotate(-35deg);opacity:0}}100%{{opacity:0}}}}

/* Tata Surya Container */
.sol{{position:fixed;top:50%;left:50%;width:840px;height:840px;transform:translate(-50%,-50%) scale(var(--sc,1));z-index:1;pointer-events:none;transition:opacity .8s,transform .8s}}

/* Orbit tracks */
.o-trk{{position:absolute;top:50%;left:50%;border-radius:50%;border:1px dashed rgba(255,215,64,.18);pointer-events:none}}

/* Orbit rotasi - GPU accelerated */
@keyframes cw{{to{{transform:rotate(360deg)}}}}
@keyframes ccw{{to{{transform:rotate(-360deg)}}}}
.o-arm{{position:absolute;top:50%;left:50%;border-radius:50%;will-change:transform;pointer-events:none}}
.p-h{{position:absolute;pointer-events:auto;cursor:pointer}}
.p-i{{width:100%;height:100%;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;will-change:transform}}

/* 3D Flip Card */
.p-card{{width:100%;height:100%;position:relative;transform-style:preserve-3d;transition:transform .8s cubic-bezier(.34,1.56,.64,1);border-radius:50%}}
.p-card.flipped{{transform:rotateY(180deg)}}
.p-h:hover .p-card{{transform:scale(1.25) rotateY(180deg);z-index:99}}

.c-f,.c-b{{position:absolute;inset:0;border-radius:50%;backface-visibility:hidden;overflow:hidden;display:flex;align-items:center;justify-content:center}}
.c-f{{box-shadow:inset -3px -3px 8px rgba(0,0,0,.6),0 0 12px rgba(255,215,64,.35)}}
.c-b{{transform:rotateY(180deg);border:2.5px solid;background:#0f0a21}}
.m-ph{{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}}

/* Cincin Saturnus */
.p-ring{{position:absolute;top:50%;left:50%;width:170%;height:48%;margin:-24% 0 0 -85%;border-radius:50%;border:1.5px solid;opacity:.7;transform:rotate(-25deg);pointer-events:none;z-index:5}}

/* Label nama */
.p-lbl{{position:absolute;top:104%;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;white-space:nowrap;pointer-events:none;margin-top:2px}}
.p-nm{{font-size:9px;font-weight:700;color:#ffd740;text-shadow:0 1px 3px rgba(0,0,0,.9),0 0 6px rgba(255,215,64,.6)}}
.p-badge{{font-size:7px;font-weight:800;color:#0f0a21;background:#ffd740;padding:1px 5px;border-radius:7px;margin-top:1px;box-shadow:0 0 4px rgba(255,215,64,.6)}}

/* MATAHARI (Kak Yollanda Agustina) - Aura emas hangat */
@keyframes sun-p{{0%,100%{{transform:scale(1);opacity:.85}}50%{{transform:scale(1.08);opacity:1}}}}
@keyframes sun-w{{0%,100%{{transform:rotate(0deg)}}50%{{transform:rotate(4deg)}}}}

.sun-aura{{position:absolute;top:50%;left:50%;width:180px;height:180px;margin:-90px 0 0 -90px;border-radius:50%;background:radial-gradient(circle,rgba(255,215,64,.38) 0%,rgba(255,109,0,.16) 55%,transparent 72%);animation:sun-p 3s ease-in-out infinite;pointer-events:none;z-index:10}}
.sun-core{{position:absolute;top:50%;left:50%;width:96px;height:96px;margin:-48px 0 0 -48px;border-radius:50%;border:3.5px solid #ffd740;box-shadow:0 0 25px rgba(255,215,64,.8),0 0 55px rgba(255,145,0,.5),0 0 90px rgba(255,61,0,.25);overflow:hidden;z-index:12;background:#1a0f2e;animation:sun-w 4s ease-in-out infinite;display:flex;align-items:center;justify-content:center}}
.sun-img{{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}}
.sun-tag{{position:absolute;top:50%;left:50%;transform:translate(-50%,54px);z-index:15;background:rgba(15,10,30,.85);border:1px solid rgba(255,215,64,.65);color:#ffd740;font-size:9.5px;font-weight:800;letter-spacing:1px;padding:3px 10px;border-radius:10px;white-space:nowrap;box-shadow:0 0 10px rgba(255,215,64,.4)}}

/* Progress bar - minimal */
.pbar-wrap{{position:fixed;bottom:0;left:0;right:0;height:3px;background:rgba(255,255,255,.06);z-index:99999}}
.pbar{{height:100%;width:0%;background:linear-gradient(90deg,#ffd740,#ff9100,#ff3d00);box-shadow:0 0 8px #ffd740;transition:width .25s linear}}
</style></head><body>

<div id="sp"><div class="comet"></div></div>

<div class="sol" id="sol">
{tracks}
<div class="sun-aura"></div>
<div class="sun-tag">✦ {NAMA_MENTOR} ✦</div>
<div class="sun-core">{sun_face}</div>
{planets_html}
</div>

<div class="pbar-wrap"><div class="pbar" id="pb"></div></div>

<script>
(function(){{
var sc=function(){{var s=Math.min(1,Math.min(innerWidth/860,innerHeight/860));if(s<.4)s=.4;document.documentElement.style.setProperty('--sc',s)}};
addEventListener('resize',sc);sc();

setTimeout(function(){{
var c=document.querySelectorAll('.p-card');
c.forEach(function(e,i){{setTimeout(function(){{e.classList.add('flipped')}},i*90)}});
}},1600);

var D={dur_ms},s=Date.now(),pb=document.getElementById('pb'),sol=document.getElementById('sol'),dn=false;
function f(){{if(dn)return;var e=Date.now()-s,p=Math.min(100,e/D*100);if(pb)pb.style.width=p+'%';
if(e>=D){{dn=true;if(sol){{sol.style.opacity='0';sol.style.transform='translate(-50%,-50%) scale(calc(var(--sc,1)*1.12))'}};return}};requestAnimationFrame(f)}};
requestAnimationFrame(f);
}})();
</script></body></html>"""


# ========================================================================
# FUNGSI UTAMA (DENGAN DURASI_MINIMUM, DURASI_MAKSIMUM & PRELOAD AKTIF)
# ========================================================================

def show_loading_screen():
    if st.session_state.get("loading_screen_done", False):
        return
    st.session_state["loading_screen_done"] = True

    st.markdown("""
    <style>
    .stApp { background: #04030a !important; }
    [data-testid="stHeader"],
    [data-testid="stSidebar"],
    [data-testid="stStatusWidget"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    #MainMenu, footer { display: none !important; }
    section[data-testid="stMain"] > div:first-child { padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    section[data-testid="stMain"] iframe {
        position: fixed !important;
        top: 0 !important; left: 0 !important;
        width: 100vw !important; height: 100vh !important;
        border: none !important; z-index: 999999 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    t_start = time.perf_counter()
    min_dur = max(1.0, float(DURASI_MINIMUM))
    max_dur = max(min_dur, float(DURASI_MAKSIMUM))

    # 1. Siapkan foto Matahari (Mentor) & 13 Planet (Anggota) dalam bentuk Base64 agar tidak diblokir browser
    mentor_b64, member_b64_map = _prepare_all_loading_photos()

    # 2. Tampilkan animasi tata surya di layar pengguna
    elapsed_prep = time.perf_counter() - t_start
    remaining_min = max(2.5, min_dur - elapsed_prep)
    html = _build_html(mentor_b64, member_b64_map, dur_sec=remaining_min)
    components.html(html, height=800, scrolling=False)

    # 3. Selagi animasi berputar di layar, preload aset Halaman Utama di background
    #    Dibatasi paling lama hingga DURASI_MAKSIMUM detik agar tidak pernah stuck!
    preload_targets = list(PRELOAD_URLS_HALAMAN_UTAMA) + [
        u.strip() for u in FOTO_ANGGOTA.values() if u and u.strip().startswith("http")
    ]
    unique_targets = list(dict.fromkeys(preload_targets))

    with ThreadPoolExecutor(max_workers=6) as pool:
        futs = [pool.submit(_download_raw_bytes, u, 5.0) for u in unique_targets]
        rem_max = max(0.2, max_dur - (time.perf_counter() - t_start))
        wait(futs, timeout=rem_max)

    # 4. Pastikan durasi tampil minimal mencapai DURASI_MINIMUM, tapi tidak melebihi DURASI_MAKSIMUM
    elapsed_total = time.perf_counter() - t_start
    if elapsed_total < min_dur:
        time.sleep(min_dur - elapsed_total)

    st.rerun()


def reset_loading_screen():
    st.session_state.pop("loading_screen_done", None)


def get_cached_bytes(url: str):
    """Kembalikan bytes gambar yang sudah di-preload selama loading screen (dipakai oleh halaman_utama.py)."""
    if not url:
        return None
    raw = _PRELOAD_RAW_CACHE.get(url)
    if raw is not None:
        return raw
    gid = _extract_drive_id(url)
    if gid:
        for k, v in list(_PRELOAD_RAW_CACHE.items()):
            if gid in k:
                return v
    return None


# ========================================================================
# SHARED GLOBAL CACHE UNTUK 13 HALAMAN BUKU KATING (HEMAT RAM SERVER)
# ========================================================================
@st.cache_data(ttl=7200, max_entries=180, show_spinner=False)
def shared_kating_image_b64(url: str) -> str:
    """Satu cache terpusat untuk seluruh 13 halaman Buku Kating agar tidak duplikasi 13x di RAM."""
    if not url:
        return ""
    raw = _download_raw_bytes(url, timeout=8.0)
    if not raw:
        return ""
    try:
        img = Image.open(BytesIO(raw))
        img = ImageOps.exif_transpose(img).resize((280, 374))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        buf = BytesIO()
        img.save(buf, format="JPEG", quality=80, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception:
        return ""


@st.cache_data(ttl=7200, max_entries=48, show_spinner=False)
def shared_kating_image_pil(url: str):
    if not url:
        return None
    raw = _download_raw_bytes(url, timeout=8.0)
    if not raw:
        return None
    try:
        img = Image.open(BytesIO(raw))
        img = ImageOps.exif_transpose(img).resize((280, 374))
        return img
    except Exception:
        return None
