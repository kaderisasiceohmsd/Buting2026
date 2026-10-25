import base64
import html
from io import BytesIO

import requests
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageOps
from streamlit_option_menu import option_menu

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================
st.set_page_config(
    page_title="Buku Kating Bayesian",
    page_icon="💙",
    layout="wide",
)


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
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


# ==================================================
# HELPER: gambar -> data URI (supaya bisa dipakai di kartu HTML & buku)
# ==================================================
@st.cache_data(show_spinner=False)
def to_data_uri(url, width, height=None):
    try:
        img = load_image(url).convert("RGB")
        if height:
            img = ImageOps.fit(img, (width, height), Image.LANCZOS, centering=(0.5, 0.2))
        else:
            img.thumbnail((width, width * 2))
        buf = BytesIO()
        img.save(buf, "JPEG", quality=82, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        return ""


# ==================================================
# CSS TEMA BIRU
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Sora:wght@600;700;800&family=Unbounded:wght@500;700;800&family=Space+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');

:root {
    --bg: #0d214d;
    --accent: #1769e8;
    --sky: #5ea2ff;
    --light: #a3c4f3;
    --dim: #cad8f2;
    --line: rgba(163, 196, 243, 0.18);
    --gold1: #fff0b3;
    --gold2: #f6c744;
    --gold3: #d8960f;
}

.stApp {
    background:
        radial-gradient(900px 480px at 10% -10%, rgba(23, 105, 232, 0.34), transparent 60%),
        radial-gradient(800px 460px at 100% 0%, rgba(36, 88, 200, 0.28), transparent 58%),
        linear-gradient(180deg, #0d214d 0%, #0a1a42 100%);
    background-attachment: fixed;
    color: #ffffff;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

header[data-testid="stHeader"] { background: transparent; }
footer, #MainMenu { visibility: hidden; }

.block-container {
    max-width: 1220px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ---------- HERO ---------- */
.hero { text-align: center; margin-bottom: 22px; }

.hero-eyebrow {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--light);
    padding: 6px 16px;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(255,255,255,0.09), rgba(255,255,255,0.02));
    margin-bottom: 14px;
}

.hero-title {
    font-family: 'Unbounded', sans-serif;
    font-size: clamp(2rem, 5vw, 3.6rem);
    font-weight: 800;
    letter-spacing: 2px;
    margin: 0 0 8px 0;
    background: linear-gradient(180deg, #ffffff 30%, #a9cbff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 20px rgba(23, 105, 232, 0.5));
}

.hero-sub { color: var(--light); font-size: 15px; margin: 0; letter-spacing: 1.5px; font-weight: 600; }

/* ---------- LOGO ---------- */
div[data-testid="stImage"] img {
    border-radius: 18px;
}

/* ---------- JUDUL BAGIAN ---------- */
.section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin: 34px 0 16px 0;
}

.section-head h2 {
    font-family: 'Unbounded', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    margin: 0;
    color: #fff;
}

.count-chip {
    font-size: 12px;
    font-weight: 700;
    color: #dbe8ff;
    padding: 6px 14px;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(23,105,232,0.38), rgba(23,105,232,0.12));
    border: 1px solid rgba(94, 162, 255, 0.45);
}

/* ---------- KARTU DESKRIPSI ---------- */
.glass-card {
    position: relative;
    border-radius: 26px;
    padding: 34px 40px;
    background:
        radial-gradient(520px 260px at 100% 0%, rgba(94, 162, 255, 0.28), transparent 62%),
        linear-gradient(135deg, #1b52c9 0%, #133f99 32%, #0d2c70 68%, #081c50 100%);
    box-shadow:
        inset 0 0 0 1px rgba(120, 175, 255, 0.30),
        inset 0 1px 0 rgba(255, 255, 255, 0.14),
        0 18px 40px rgba(0, 0, 0, 0.40);
    color: var(--dim);
    line-height: 1.8;
    font-size: 15px;
    text-align: center;
}
.glass-card b { color: #fff; }
.glass-card .motto {
    display: block;
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-size: 1.9rem;
    line-height: 1.3;
    color: #fff;
    margin: 4px 0 14px 0;
}

.caption-chip {
    text-align: center;
    margin: 14px auto 0 auto;
    max-width: 520px;
    padding: 12px 20px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(23,105,232,0.45), rgba(23,105,232,0.12));
    border: 1px solid rgba(94, 162, 255, 0.45);
}
.caption-chip b {
    display: block;
    font-family: 'Unbounded', sans-serif;
    font-size: 0.95rem;
    margin-bottom: 3px;
}
.caption-chip span { color: var(--dim); font-size: 13px; }

/* ---------- KARTU ANGGOTA ---------- */
.lurah-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 24px;
    margin-bottom: 24px;
}
.member-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 20px;
}

.member-card {
    position: relative;
    display: flex;
    flex-direction: column;
    border-radius: 26px;
    overflow: hidden;
    background:
        radial-gradient(420px 240px at 100% 0%, rgba(94, 162, 255, 0.26), transparent 62%),
        radial-gradient(380px 240px at 20% 115%, rgba(23, 105, 232, 0.36), transparent 62%),
        linear-gradient(150deg, #1b52c9 0%, #133f99 32%, #0d2c70 68%, #081c50 100%);
    box-shadow:
        inset 0 0 0 1px rgba(120, 175, 255, 0.28),
        inset 0 1px 0 rgba(255, 255, 255, 0.14),
        0 16px 34px rgba(0, 0, 0, 0.40);
    transition: transform .28s ease, box-shadow .28s ease;
    animation: rise .55s ease both;
}
.member-card:hover {
    transform: translateY(-6px);
    box-shadow:
        inset 0 0 0 1px rgba(140, 190, 255, 0.6),
        inset 0 1px 0 rgba(255, 255, 255, 0.18),
        0 26px 50px rgba(0, 0, 0, 0.5);
}

@keyframes rise {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

.m-photo {
    position: relative;
    aspect-ratio: 4 / 5;
    background: linear-gradient(160deg, #2a7bff 0%, #1244a8 55%, #0a2a6e 100%);
    overflow: hidden;
}
.featured .m-photo { aspect-ratio: 1 / 1; }

.m-photo img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 20%;
    transition: transform .6s ease;
}
.member-card:hover .m-photo img { transform: scale(1.06); }

.m-photo::after {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(8, 28, 80, 0.30) 0%, transparent 28%, transparent 55%, rgba(8, 20, 60, 0.92) 100%);
    pointer-events: none;
}

.m-index {
    position: absolute;
    top: 14px;
    left: 14px;
    z-index: 2;
    font-family: 'Unbounded', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    padding: 6px 11px;
    border-radius: 10px;
    background: rgba(8, 20, 49, 0.72);
    color: #fff;
    border: 1px solid var(--line);
    backdrop-filter: blur(6px);
}

.m-initial {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Unbounded', sans-serif;
    font-size: 4.5rem;
    font-weight: 800;
    color: rgba(255, 255, 255, 0.9);
    text-shadow: 0 6px 24px rgba(5, 20, 70, 0.5);
}

.m-role {
    position: absolute;
    left: 14px;
    bottom: 14px;
    z-index: 2;
    overflow: hidden;
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 15px;
    border-radius: 999px;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #fff;
    background: linear-gradient(135deg, rgba(94,162,255,0.55), rgba(23,105,232,0.55));
    border: 1px solid rgba(163, 196, 243, 0.5);
    backdrop-filter: blur(6px);
}
.m-role.gold {
    color: #3a2a00;
    border: 0;
    background: linear-gradient(135deg, var(--gold1), var(--gold2) 45%, var(--gold3));
    box-shadow: 0 6px 20px rgba(246, 199, 68, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.65);
}
.m-role.gold::after {
    content: "";
    position: absolute;
    top: 0;
    left: -60%;
    width: 40%;
    height: 100%;
    background: linear-gradient(100deg, transparent, rgba(255, 255, 255, 0.65), transparent);
    transform: skewX(-20deg);
    animation: shine 3.6s ease-in-out infinite;
}
@keyframes shine {
    0%   { left: -60%; }
    55%  { left: 130%; }
    100% { left: 130%; }
}

.m-body {
    padding: 18px 18px 20px 18px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    flex: 1;
}

.m-name {
    font-family: 'Unbounded', sans-serif;
    font-size: 0.98rem;
    font-weight: 700;
    line-height: 1.3;
    margin: 0;
    word-break: break-word;
    background: linear-gradient(180deg, #ffffff 40%, #c4dcff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
.featured .m-name { font-size: 1.2rem; }

.m-nim {
    display: inline-block;
    align-self: flex-start;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.6px;
    padding: 3px 11px;
    border-radius: 999px;
    color: #e3eeff;
    background: linear-gradient(135deg, rgba(23, 105, 232, 0.5), rgba(23, 105, 232, 0.2));
    border: 1px solid rgba(94, 162, 255, 0.6);
}

.m-tile {
    border-radius: 14px;
    padding: 11px 13px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.11), rgba(255, 255, 255, 0.03));
    border: 1px solid rgba(163, 196, 243, 0.16);
}
.m-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: var(--light);
    margin-bottom: 4px;
}
.m-value {
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-size: 16px;
    line-height: 1.35;
    color: #fff;
    word-break: break-word;
}
.m-value.muted { opacity: .5; }

/* ---------- RESPONSIF ---------- */
@media (max-width: 1100px) {
    .member-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 680px) {
    .lurah-grid, .member-grid { grid-template-columns: 1fr; }
    .glass-card { padding: 24px 20px; }
    .section-head { flex-direction: column; align-items: flex-start; }
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# HEADER UTAMA
# ==================================================
st.markdown(
    """<div class="hero">
<div class="hero-eyebrow">CEO HMSD Adyatama ITERA 2026</div>
<h1 class="hero-title">WEBSITE KATING</h1>
<p class="hero-sub">KELOMPOK BAYESIAN</p>
</div>""",
    unsafe_allow_html=True,
)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # rasio 1:2:1
    with col1:
        st.write("")
    with col2:
        st.image(load_image(url), use_container_width=True)
    with col3:
        st.write("")


layout(url)
layout(url1)


# ==================================================
# NAVIGASI MENU
# ==================================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "people"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "6px!important",
                "background": "linear-gradient(135deg, #0c1d4a, #081431)",
                "border-radius": "16px",
                "border": "1px solid #1f3e82",
            },
            "icon": {"color": "#5ea2ff", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "color": "#a3c4f3",
                "text-align": "center",
                "margin": "0px 4px",
                "border-radius": "12px",
                "--hover-color": "#133f99",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #2a7bff, #1244a8)",
                "color": "#FFFFFF",
                "font-weight": "700",
            },
        },
    )
    return selected


menu = streamlit_menu()


# ==================================================
# BUKU DOKUMENTASI (bisa digeser / diklik / pakai panah keyboard)
# ==================================================
BOOK_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700;800&family=Space+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: transparent; font-family: 'Space Grotesk', sans-serif; color: #fff; overflow: hidden; }

.stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 0 0 0;
    user-select: none;
}

.book-wrap {
    perspective: 2200px;
    width: min(430px, 86vw);
    height: 560px;
    position: relative;
    touch-action: pan-y;
    cursor: grab;
}
.book-wrap:active { cursor: grabbing; }

/* tumpukan halaman di belakang (efek tebal buku) */
.book-wrap::before, .book-wrap::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 6px 18px 18px 6px;
    background: #0a2a6e;
    box-shadow: 0 0 0 1px rgba(120,175,255,0.25);
}
.book-wrap::before { transform: translate(7px, 6px); opacity: .55; }
.book-wrap::after  { transform: translate(14px, 12px); opacity: .3; }

.page {
    position: absolute;
    inset: 0;
    transform-origin: left center;
    transform-style: preserve-3d;
    transition: transform .9s cubic-bezier(.65,.05,.25,1), opacity .9s ease;
    border-radius: 6px 18px 18px 6px;
    z-index: 1;
}
.page.flipped {
    transform: rotateY(-115deg);
    opacity: 0;
    pointer-events: none;
}

.face {
    position: absolute;
    inset: 0;
    border-radius: 6px 18px 18px 6px;
    overflow: hidden;
    background: linear-gradient(150deg, #1b52c9 0%, #133f99 35%, #0d2c70 70%, #081c50 100%);
    box-shadow:
        inset 0 0 0 1px rgba(120, 175, 255, 0.35),
        0 18px 40px rgba(0, 0, 0, 0.45);
}
/* lipatan punggung buku */
.face::before {
    content: "";
    position: absolute;
    top: 0; bottom: 0; left: 0;
    width: 26px;
    background: linear-gradient(90deg, rgba(0,0,0,0.45), rgba(0,0,0,0));
    z-index: 5;
    pointer-events: none;
}

.face img.photo {
    position: absolute;
    inset: 14px 14px 14px 26px;
    width: calc(100% - 40px);
    height: calc(100% - 28px);
    object-fit: cover;
    border-radius: 12px;
    border: 1px solid rgba(163,196,243,0.35);
    pointer-events: none;
    -webkit-user-drag: none;
}
.photo-ph {
    position: absolute;
    inset: 14px 14px 14px 26px;
    border-radius: 12px;
    background: linear-gradient(160deg, #2a7bff, #0a2a6e);
}

.cap {
    position: absolute;
    left: 26px; right: 14px; bottom: 14px;
    padding: 46px 20px 18px 20px;
    border-radius: 0 0 12px 12px;
    background: linear-gradient(180deg, transparent, rgba(6, 18, 56, 0.94));
    z-index: 4;
}
.cap b {
    display: block;
    font-family: 'Unbounded', sans-serif;
    font-size: 15px;
    margin-bottom: 4px;
}
.cap span {
    font-family: 'Instrument Serif', serif;
    font-style: italic;
    font-size: 17px;
    color: #cad8f2;
}
.pno {
    position: absolute;
    top: 26px; right: 26px;
    z-index: 6;
    font-family: 'Unbounded', sans-serif;
    font-size: 11px;
    letter-spacing: 1.5px;
    padding: 5px 11px;
    border-radius: 10px;
    background: rgba(8, 20, 49, 0.72);
    border: 1px solid rgba(163,196,243,0.25);
}

/* sampul & penutup */
.cover {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 40px 36px 40px 50px;
    background:
        radial-gradient(360px 260px at 100% 0%, rgba(94,162,255,0.4), transparent 62%),
        radial-gradient(320px 260px at 0% 100%, rgba(23,105,232,0.5), transparent 62%),
        linear-gradient(150deg, #1b52c9 0%, #133f99 35%, #0d2c70 70%, #081c50 100%);
}
.cover .frame {
    position: absolute;
    inset: 16px 16px 16px 30px;
    border: 1px solid rgba(246,199,68,0.55);
    border-radius: 12px;
    pointer-events: none;
}
.cover .eyebrow {
    font-size: 11px; letter-spacing: 3px; font-weight: 700;
    color: #f6c744; text-transform: uppercase; margin-bottom: 18px;
}
.cover h2 {
    font-family: 'Unbounded', sans-serif;
    font-size: 30px; font-weight: 800; line-height: 1.15;
    background: linear-gradient(180deg, #fff 30%, #a9cbff 100%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 14px;
}
.cover p.sub {
    font-family: 'Instrument Serif', serif;
    font-style: italic; font-size: 21px; color: #cad8f2;
}
.cover .gold-line {
    width: 70px; height: 3px; border-radius: 3px; margin: 8px 0 18px 0;
    background: linear-gradient(90deg, #fff0b3, #f6c744, #d8960f);
}
.cover .hint { margin-top: 30px; font-size: 12px; letter-spacing: 1.5px; color: #a3c4f3; }

/* kontrol */
.controls {
    display: flex; align-items: center; justify-content: center; gap: 18px;
    margin-top: 26px;
}
.btn {
    width: 46px; height: 46px; border-radius: 50%;
    border: 1px solid rgba(94,162,255,0.55);
    background: linear-gradient(135deg, rgba(23,105,232,0.55), rgba(23,105,232,0.15));
    color: #fff; font-size: 20px; cursor: pointer;
    transition: transform .2s ease, background .2s ease;
}
.btn:hover:not(:disabled) { transform: scale(1.08); background: linear-gradient(135deg, #2a7bff, #1244a8); }
.btn:disabled { opacity: .3; cursor: default; }
.counter {
    font-family: 'Unbounded', sans-serif; font-size: 12px; letter-spacing: 1.5px;
    min-width: 90px; text-align: center; color: #cad8f2;
}
.dots { display: flex; gap: 7px; margin-top: 14px; }
.dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: rgba(163,196,243,0.3); cursor: pointer;
    transition: all .3s ease;
}
.dot.on { width: 24px; border-radius: 8px; background: linear-gradient(90deg, #5ea2ff, #1769e8); }
</style>
</head>
<body>
<div class="stage">
    <div class="book-wrap" id="book">
__PAGES__
    </div>
    <div class="controls">
        <button class="btn" id="prev" aria-label="Sebelumnya">&#8249;</button>
        <div class="counter" id="counter"></div>
        <button class="btn" id="next" aria-label="Berikutnya">&#8250;</button>
    </div>
    <div class="dots" id="dots"></div>
</div>
<script>
(function () {
    var pages = Array.prototype.slice.call(document.querySelectorAll('.page'));
    var n = pages.length, cur = 0;
    var counter = document.getElementById('counter');
    var dotsBox = document.getElementById('dots');
    var prev = document.getElementById('prev');
    var next = document.getElementById('next');
    var book = document.getElementById('book');
    var dots = [];

    for (var i = 0; i < n; i++) {
        (function (idx) {
            var d = document.createElement('div');
            d.className = 'dot';
            d.addEventListener('click', function () { cur = idx; render(); });
            dotsBox.appendChild(d);
            dots.push(d);
        })(i);
    }

    function render() {
        pages.forEach(function (p, i) {
            if (i < cur) { p.classList.add('flipped'); p.style.zIndex = i + 1; }
            else { p.classList.remove('flipped'); p.style.zIndex = n - i; }
        });
        dots.forEach(function (d, i) { d.classList.toggle('on', i === cur); });
        counter.textContent = (cur + 1) + ' / ' + n;
        prev.disabled = cur === 0;
        next.disabled = cur === n - 1;
    }
    function go(step) {
        var t = cur + step;
        if (t >= 0 && t < n) { cur = t; render(); }
    }

    prev.addEventListener('click', function () { go(-1); });
    next.addEventListener('click', function () { go(1); });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') go(1);
        if (e.key === 'ArrowLeft') go(-1);
    });

    var startX = null;
    book.addEventListener('pointerdown', function (e) { startX = e.clientX; });
    book.addEventListener('pointerup', function (e) {
        if (startX === null) return;
        var dx = e.clientX - startX;
        startX = null;
        if (dx < -40) go(1);
        else if (dx > 40) go(-1);
        else if (Math.abs(dx) < 6) {
            var r = book.getBoundingClientRect();
            if (e.clientX - r.left > r.width / 2) go(1); else go(-1);
        }
    });
    book.addEventListener('pointercancel', function () { startX = null; });

    render();
})();
</script>
</body>
</html>
"""


def build_book(items, judul_cover, sub_cover):
    pages = []
    total = len(items)

    pages.append(
        '<div class="page"><div class="face cover"><div class="frame"></div>'
        '<div class="eyebrow">&#10022; Album Kebersamaan &#10022;</div>'
        f'<h2>{html.escape(judul_cover)}</h2><div class="gold-line"></div>'
        f'<p class="sub">{html.escape(sub_cover)}</p>'
        '<div class="hint">GESER &middot; KLIK &middot; PANAH &rarr;</div></div></div>'
    )

    for i, it in enumerate(items, start=1):
        uri = to_data_uri(it["url"], 760, 960)
        img = f'<img class="photo" src="{uri}" alt="">' if uri else '<div class="photo-ph"></div>'
        pages.append(
            '<div class="page"><div class="face">'
            f'{img}'
            f'<div class="pno">{i:02d} / {total:02d}</div>'
            f'<div class="cap"><b>{html.escape(it["judul"])}</b>'
            f'<span>{html.escape(it["ket"])}</span></div>'
            '</div></div>'
        )

    pages.append(
        '<div class="page"><div class="face cover"><div class="frame"></div>'
        '<div class="eyebrow">&#10022; Terima Kasih &#10022;</div>'
        '<h2>Sampai Jumpa</h2><div class="gold-line"></div>'
        '<p class="sub">Setiap momen memperbarui langkah kita.</p></div></div>'
    )

    return BOOK_TEMPLATE.replace("__PAGES__", "\n".join(pages))


# ==================================================
# HALAMAN HOME
# ==================================================
if menu == "Home":

    def home_page():
        st.markdown(
            '<div class="section-head"><h2>Deskripsi Kelompok Bayesian</h2></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """<div class="glass-card">
<b>Selamat datang di portal resmi Kelompok Bayesian!</b>
<span class="motto">&ldquo;Gapai Cita, Kejar Mimpi, di Angkasa.&rdquo;</span>
Terinspirasi dari <b>Teorema Bayes</b> dalam Sains Data dan Statistika, kelompok <b>Bayesian</b> melambangkan semangat pembelajaran dan kekeluargaan yang adaptif: setiap pengalaman, tantangan, dan kebersamaan baru adalah bukti nyata yang terus memperbarui serta menguatkan langkah kita untuk bertumbuh bersama di <b>CEO HMSD Adyatama ITERA 2026</b>.
</div>""",
            unsafe_allow_html=True,
        )

        # Foto utama kelompok
        st.write("")
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"
        layout(foto_kelompok)
        st.markdown(
            """<div class="caption-chip">
<b>&#10022; Keluarga Bayesian &#10022;</b>
<span>Momen kebersamaan yang tidak akan terlupakan.</span>
</div>""",
            unsafe_allow_html=True,
        )

        # Dokumentasi kegiatan (buku)
        kegiatan_Bayesian = [
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 1", "ket": "Ganti dengan keterangan kegiatan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 2", "ket": "Ganti dengan keterangan kegiatan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 3", "ket": "Ganti dengan keterangan kegiatan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 4", "ket": "Ganti dengan keterangan kegiatan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 5", "ket": "Ganti dengan keterangan kegiatan"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq",
             "judul": "Kegiatan 6", "ket": "Ganti dengan keterangan kegiatan"},
        ]

        st.markdown(
            f'<div class="section-head"><h2>Dokumentasi Kegiatan</h2>'
            f'<span class="count-chip">{len(kegiatan_Bayesian)} Momen</span></div>',
            unsafe_allow_html=True,
        )
        with st.spinner("Menyiapkan buku dokumentasi..."):
            book_html = build_book(kegiatan_Bayesian, "Dokumentasi Bayesian", "Geser untuk membuka halaman")
        components.html(book_html, height=720, scrolling=False)

    home_page()


# ==================================================
# HALAMAN ABOUT US
# ==================================================
elif menu == "About Us":

    def member_card(no, d, uri, featured=False):
        nama = d["nama"]
        inisial = "".join(w[0] for w in nama.split()[:2]).upper()
        gold = featured
        star = "&#9733; " if gold else ""

        if uri:
            foto = f'<img src="{uri}" alt="{html.escape(nama)}">'
        else:
            foto = f'<div class="m-initial">{html.escape(inisial)}</div>'

        def tile(label, value):
            kosong = value.strip() in ("", "--")
            teks = "Belum diisi" if kosong else html.escape(value)
            cls = "m-value muted" if kosong else "m-value"
            return (
                f'<div class="m-tile"><div class="m-label">{label}</div>'
                f'<div class="{cls}">{teks}</div></div>'
            )

        return (
            f'<div class="member-card{" featured" if featured else ""}" style="animation-delay:{no * 0.06:.2f}s">'
            f'<div class="m-photo">{foto}'
            f'<div class="m-index">{no:02d}</div>'
            f'<div class="m-role{" gold" if gold else ""}">{star}{html.escape(d["sebagai"])}</div>'
            f'</div>'
            f'<div class="m-body">'
            f'<h3 class="m-name">{html.escape(nama)}</h3>'
            f'<div class="m-nim">{html.escape(d["nim"])}</div>'
            f'{tile("Fun Fact", d["fun_fact"])}'
            f'{tile("Motto Hidup", d["motto_hidup"])}'
            f'</div></div>'
        )

    def about_page():
        st.markdown(
            '<div class="section-head"><h2>About Us — Buku Kating Bayesian</h2></div>',
            unsafe_allow_html=True,
        )

        # 10 URL gambar sesuai jumlah 10 anggota di data_list
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19KrR82_PA5lsmyDn-8iBcBBVxWqctEp9",  # 1. Thomas Yustio
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 2. Syalom Nauli Jubilate
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 3. Chavia Chairunissa
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 4. Aqila Chika Aurelia
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 5. Sefina Amanda Putri
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 6. Aura Putri Ghefira
            "https://drive.google.com/uc?export=view&id=1SaqIKBazfbklZ87SPixrd5eO0PfvydN3",  # 7. Ezra Hamizan
            "https://drive.google.com/uc?export=view&id=1OPEq99LUbLHfdDUTj95ueH52KCoFkKXo",  # 8. Afdhi Hafiidz Habibie
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 9. Rizqy Ramadhan
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 10. Alan Garcia Sinaga
        ]

        # Data lengkap 10 anggota Bayesian
        data_list = [
            {
                "nama": "Thomas Yustio",
                "sebagai": "Pak Lurah",
                "nim": "125450085",
                "fun_fact": "Saya pernah patah gigi 4x dan saya karbitan",
                "motto_hidup": "Hidup cuma sekali, maka lakukan apa yang kamu mau, misal mancing",
            },
            {
                "nama": "Syalom Nauli Jubilate",
                "sebagai": "Bu Lurah",
                "nim": "125450050",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Chavia Chairunissa",
                "sebagai": "Anggota 01",
                "nim": "125450026",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Aqila Chika Aurelia",
                "sebagai": "Anggota 02",
                "nim": "125450038",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Sefina Amanda Putri",
                "sebagai": "Anggota 03",
                "nim": "125450042",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Aura Putri Ghefira",
                "sebagai": "Anggota 04",
                "nim": "125450047",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Ezra Hamizan",
                "sebagai": "Anggota 05",
                "nim": "125450052",
                "fun_fact": "Sangat Konyol & Selalu Konyol",
                "motto_hidup": "Cacing-Cacing, Naga-Naga, Go Big Or Go Home",
            },
            {
                "nama": "Afdhi Hafiidz Habibie",
                "sebagai": "Anggota 06",
                "nim": "125450061",
                "fun_fact": "Waktu belajar sepeda pernah nyemplung ke bekas adukan semen",
                "motto_hidup": "Hidup di dunia ini kayak plat Jakarta B aja",
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 07",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas",
            },
            {
                "nama": "Alan Garcia Sinaga",
                "sebagai": "Anggota 08",
                "nim": "125450091",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
        ]

        with st.spinner("Memuat foto anggota..."):
            uris = [to_data_uri(u, 640, 800) for u in gambar_urls]

        lurah_html = "".join(
            member_card(i + 1, data_list[i], uris[i], featured=True) for i in range(2)
        )
        anggota_html = "".join(
            member_card(i + 1, data_list[i], uris[i]) for i in range(2, len(data_list))
        )

        st.markdown(
            f'<div class="section-head"><h2>Pimpinan Kelompok</h2>'
            f'<span class="count-chip">2 Orang</span></div>'
            f'<div class="lurah-grid">{lurah_html}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="section-head"><h2>Anggota</h2>'
            f'<span class="count-chip">{len(data_list) - 2} Orang</span></div>'
            f'<div class="member-grid">{anggota_html}</div>',
            unsafe_allow_html=True,
        )

    about_page()
