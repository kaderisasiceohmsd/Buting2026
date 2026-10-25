import re
import base64
import html
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor

import requests
import streamlit as st
from PIL import Image, ImageOps
from streamlit_option_menu import option_menu

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================
st.set_page_config(
    page_title="Buku Kating HMSD",
    page_icon="💙",
    layout="wide"
)

# ==================================================
# CSS (Desain dari Afdhi)
# ==================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap');

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
.hero { text-align: center; margin-bottom: 26px; }

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
    font-family: 'Sora', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    font-weight: 800;
    letter-spacing: 3px;
    margin: 0 0 6px 0;
    background: linear-gradient(180deg, #ffffff 30%, #a9cbff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 20px rgba(23, 105, 232, 0.5));
}

.hero-sub { color: var(--light); font-size: 15px; margin: 0; }

/* ---------- JUDUL BAGIAN ---------- */
.section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin: 26px 0 14px 0;
}

.section-head h2 {
    font-family: 'Sora', sans-serif;
    font-size: 1.35rem;
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

/* ---------- INPUT CARI ---------- */
.stTextInput input {
    background: linear-gradient(135deg, #0c1d4a, #081431) !important;
    color: #fff !important;
    border: 1px solid #1f3e82 !important;
    border-radius: 14px !important;
    padding: 12px 16px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}
.stTextInput input:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(23, 105, 232, 0.28) !important;
}

/* ---------- KARTU PROFIL (GRADASI) ---------- */
.profile-card {
    display: grid;
    grid-template-columns: 400px minmax(0, 1fr);
    min-height: 520px;
    border-radius: 28px;
    overflow: hidden;
    background:
        radial-gradient(620px 320px at 100% 0%, rgba(94, 162, 255, 0.30), transparent 62%),
        radial-gradient(520px 320px at 35% 115%, rgba(23, 105, 232, 0.38), transparent 62%),
        linear-gradient(135deg, #1b52c9 0%, #133f99 32%, #0d2c70 68%, #081c50 100%);
    box-shadow:
        inset 0 0 0 1px rgba(120, 175, 255, 0.30),
        inset 0 1px 0 rgba(255, 255, 255, 0.14),
        0 18px 40px rgba(0, 0, 0, 0.42);
    margin-bottom: 32px;
    transition: transform .25s ease, box-shadow .25s ease;
    animation: rise .5s ease both;
}

.profile-card:hover {
    transform: translateY(-4px);
    box-shadow:
        inset 0 0 0 1px rgba(140, 190, 255, 0.55),
        inset 0 1px 0 rgba(255, 255, 255, 0.18),
        0 26px 55px rgba(0, 0, 0, 0.5);
}

@keyframes rise {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ---------- SISI FOTO ---------- */
.photo-pane {
    position: relative;
    min-height: 520px;
    background: linear-gradient(160deg, #2a7bff 0%, #1244a8 55%, #0a2a6e 100%);
    border-right: 1px solid var(--line);
}

.photo-pane img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 18%;
}

.photo-pane::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(180deg, rgba(8, 28, 80, 0.25) 0%, transparent 25%, transparent 62%, rgba(8, 28, 80, 0.7) 100%);
    pointer-events: none;
}

.card-index {
    position: absolute;
    top: 18px;
    left: 18px;
    z-index: 2;
    font-family: 'Sora', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1.5px;
    padding: 6px 12px;
    border-radius: 10px;
    background: rgba(8, 20, 49, 0.72);
    color: #fff;
    border: 1px solid var(--line);
    backdrop-filter: blur(6px);
}

.avatar-fallback {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

.avatar-fallback span {
    font-family: 'Sora', sans-serif;
    font-size: 5.5rem;
    font-weight: 800;
    letter-spacing: 4px;
    color: rgba(255, 255, 255, 0.92);
    text-shadow: 0 6px 24px rgba(5, 20, 70, 0.5);
}

.avatar-fallback small { color: var(--dim); font-size: 12px; letter-spacing: 1px; }

/* ---------- SISI BIODATA ---------- */
.info-pane {
    min-width: 0;
    padding: 40px 48px 40px 56px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 26px;
}

.profile-name {
    font-family: 'Sora', sans-serif;
    font-size: clamp(1.5rem, 2.6vw, 2.2rem);
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 14px 0;
    word-break: break-word;
    background: linear-gradient(180deg, #ffffff 40%, #c4dcff 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---------- LENCANA JABATAN ---------- */
.jabatan-badge {
    position: relative;
    overflow: hidden;
    display: inline-flex;
    align-items: center;
    gap: 9px;
    padding: 9px 20px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #3a2a00;
    background: linear-gradient(135deg, var(--gold1), var(--gold2) 45%, var(--gold3));
    box-shadow: 0 6px 20px rgba(246, 199, 68, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.65);
    margin-bottom: 16px;
}

.jabatan-badge::after {
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

.jabatan-star { font-size: 13px; }

/* ---------- GRID INFO ---------- */
.info-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    padding-top: 24px;
    border-top: 1px solid var(--line);
}

.info-tile {
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.11), rgba(255, 255, 255, 0.03));
    border: 1px solid rgba(163, 196, 243, 0.16);
    border-radius: 14px;
    padding: 13px 15px;
}

.info-label {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--light);
    margin-bottom: 5px;
}

.info-value {
    font-size: 14px;
    font-weight: 600;
    color: #fff;
    line-height: 1.45;
    word-break: break-word;
}

.social-chip {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(23, 105, 232, 0.5), rgba(23, 105, 232, 0.2));
    border: 1px solid rgba(94, 162, 255, 0.6);
    color: #e3eeff;
}

/* ---------- KESAN & PESAN ---------- */
.quote-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
    align-items: start;
}

.quote-box {
    border-radius: 16px;
    padding: 14px 16px 14px 18px;
    background: linear-gradient(135deg, rgba(8, 20, 49, 0.72), rgba(19, 63, 153, 0.28));
    border: 1px solid rgba(163, 196, 243, 0.10);
    border-left: 3px solid var(--sky);
}

.quote-label {
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--light);
    margin-bottom: 6px;
}

.quote-text {
    font-size: 13.5px;
    line-height: 1.6;
    color: var(--dim);
    word-break: break-word;
}

.muted { opacity: .55; font-style: italic; }

.quote-long summary {
    list-style: none;
    cursor: pointer;
    outline: none;
}
.quote-long summary::-webkit-details-marker { display: none; }

.quote-more, .quote-less {
    display: inline-block;
    margin-top: 8px;
    font-size: 12px;
    font-weight: 700;
    color: var(--sky);
}
.quote-long summary:hover .quote-more,
.quote-long summary:hover .quote-less { color: #ffffff; }

.quote-less { display: none; }
.quote-long[open] .quote-more,
.quote-long[open] .quote-preview { display: none; }
.quote-long[open] .quote-less { display: inline-block; margin-top: 0; margin-bottom: 8px; }

.quote-full {
    max-height: 220px;
    overflow-y: auto;
    padding-right: 8px;
    scrollbar-width: thin;
    scrollbar-color: rgba(94, 162, 255, 0.6) transparent;
}
.quote-full::-webkit-scrollbar { width: 6px; }
.quote-full::-webkit-scrollbar-thumb { background: rgba(94, 162, 255, 0.6); border-radius: 6px; }

/* ---------- RESPONSIF ---------- */
@media (max-width: 1100px) {
    .profile-card { grid-template-columns: 340px minmax(0, 1fr); }
    .info-pane { padding: 32px 32px 32px 40px; }
    .info-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (max-width: 820px) {
    .profile-card { grid-template-columns: 1fr; min-height: 0; }
    .photo-pane { min-height: 0; height: 440px; border-right: 0; border-bottom: 1px solid var(--line); }
    .info-pane { padding: 26px 22px; }
    .info-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .quote-grid { grid-template-columns: 1fr; }
    .section-head { flex-direction: column; align-items: flex-start; }
}
[data-testid="stSidebar"], [data-testid="stSidebar"] > div {
    background: #0a1838 !important;
    border-right: 1px solid #1f3e82;
}
[data-testid="stSidebar"] * { color: #cad8f2 !important; }
[data-testid="stSidebarNavLink"] { border-radius: 12px !important; }
[data-testid="stSidebarNavLink"]:hover { background: #15357a !important; }
[data-testid="stSidebarNavLink"][aria-current="page"] { background: #1769e8 !important; }
[data-testid="stSidebarNavLink"][aria-current="page"] * { color: #fff !important; font-weight: 700; }

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='hero'>"
    "<div class='hero-eyebrow'>Himpunan Mahasiswa Sains Data</div>"
    "<h1 class='hero-title'>BUKU KATING</h1>"
    "<p class='hero-sub'>Kenali lebih dekat keluarga besar HMSD</p>"
    "</div>",
    unsafe_allow_html=True
)

# ==================================================
# MENU NAVIGASI
# ==================================================
def streamlit_menu():
    return option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Badan Legislatif",
            "Badan Kesenatoran",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
            "Departemen Minbak",
        ],
        icons=[
            "bank", "journal-text", "award-fill", "people-fill", "lightning-fill",
            "globe2", "house-heart-fill", "cpu-fill", "camera-fill", "star-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "8px",
                "background-color": "#0a1838",
                "border-radius": "18px",
                "box-shadow": "0 5px 20px rgba(0,0,0,0.3)",
                "border": "1px solid #1f3e82",
            },
            "icon": {
                "color": "#a3c4f3",
                "font-size": "15px",
            },
            "nav-link": {
                "font-size": "12.5px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "3px",
                "padding": "11px 12px",
                "border-radius": "12px",
                "color": "#cad8f2",
                "--hover-color": "#15357a",
            },
            "nav-link-selected": {
                "background-color": "#1769e8",
                "color": "#ffffff",
                "font-weight": "700",
            },
        },
    )

# ==================================================
# FUNGSI MEMUAT GAMBAR
# ==================================================
def _candidate_urls(url):
    match = re.search(r"(?:id=|/d/)([\w-]{10,})", url)
    if "drive.google.com" in url and match:
        fid = match.group(1)
        return [
            f"https://lh3.googleusercontent.com/d/{fid}=w800",
            f"https://drive.google.com/thumbnail?id={fid}&sz=w800",
            f"https://drive.google.com/uc?export=view&id={fid}",
        ]
    return [url]

def _fetch_b64(url):
    for candidate in _candidate_urls(url):
        try:
            response = requests.get(
                candidate,
                timeout=15,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            content_type = response.headers.get("content-type", "")
            if response.status_code != 200 or not content_type.startswith("image/"):
                continue

            img = Image.open(BytesIO(response.content))
            img = ImageOps.exif_transpose(img)
            img = img.convert("RGB")
            img.thumbnail((800, 1000))

            buffered = BytesIO()
            img.save(buffered, format="JPEG", quality=82)
            return base64.b64encode(buffered.getvalue()).decode()
        except Exception:
            continue
    return None

@st.cache_data(show_spinner=False, ttl=3600)
def load_images_b64(urls):
    urls = list(urls)
    if not urls:
        return []
    unique = list(dict.fromkeys(urls))
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(unique, pool.map(_fetch_b64, unique)))
    return [results[u] for u in urls]

# ==================================================
# FUNGSI BANTU TAMPILAN
# ==================================================
def esc(value):
    return html.escape(str(value))

def clean(value, default="-"):
    text = str(value if value is not None else "").strip()
    if not text or not text.strip(" .@-_"):
        return default
    return text

def initials(nama):
    parts = [p for p in re.split(r"\s+", nama.strip()) if p]
    return "".join(p[0].upper() for p in parts[:2]) or "?"

def _flatten_html(s):
    return "".join(line.strip() for line in s.splitlines() if line.strip())

def _tile(icon, label, value_html):
    return (
        f"<div class='info-tile'>"
        f"<div class='info-label'><span>{icon}</span>{label}</div>"
        f"<div class='info-value'>{value_html}</div>"
        f"</div>"
    )

QUOTE_LIMIT = 110

def _quote(label, text):
    head = f"<div class='quote-label'>{label}</div>"
    if not text:
        return (
            f"<div class='quote-box'>{head}"
            f"<div class='quote-text'><span class='muted'>Belum diisi</span></div></div>"
        )
    if len(text) <= QUOTE_LIMIT:
        return (
            f"<div class='quote-box'>{head}"
            f"<div class='quote-text'>{esc(text)}</div></div>"
        )
    preview = esc(text[:QUOTE_LIMIT].rsplit(" ", 1)[0]) + "…"
    return (
        f"<details class='quote-box quote-long'>"
        f"<summary>{head}"
        f"<div class='quote-text quote-preview'>{preview}</div>"
        f"<span class='quote-more'>Baca selengkapnya ▾</span>"
        f"<span class='quote-less'>Tutup ▴</span>"
        f"</summary>"
        f"<div class='quote-text quote-full'>{esc(text)}</div>"
        f"</details>"
    )

# ==================================================
# FUNGSI MENAMPILKAN PROFIL
# ==================================================
def display_images_with_data(gambar_urls, data_list, jabatan):
    images = load_images_b64(tuple(gambar_urls))

    st.markdown(
        f"<div class='section-head'><h2>{esc(jabatan)}</h2>"
        f"<span class='count-chip'>{len(data_list)} anggota</span></div>",
        unsafe_allow_html=True,
    )

    query = st.text_input(
        "Cari",
        placeholder="🔍  Cari nama, asal, atau hobi...",
        label_visibility="collapsed",
        key=f"cari_{jabatan}",
    )
    q = query.strip().lower()
    st.write("")

    shown = 0
    for i, data in enumerate(data_list):
        nama = clean(data.get("nama"), "Tanpa Nama")
        if q:
            haystack = " ".join(
                str(data.get(k, "")) for k in ("nama", "nim", "asal", "alamat", "hobbi", "sosmed", "kesan", "pesan")
            ).lower()
            if q not in haystack:
                continue

        img_b64 = images[i] if i < len(images) else None
        if img_b64:
            photo = f"<img src='data:image/jpeg;base64,{img_b64}' alt='Foto {esc(nama)}' loading='lazy'/>"
        else:
            photo = (
                f"<div class='avatar-fallback'><span>{esc(initials(nama))}</span>"
                f"<small>Foto belum tersedia</small></div>"
            )

        umur = clean(data.get("umur"))
        umur_text = f"{umur} Tahun" if umur.isdigit() else umur
        sosmed = clean(data.get("sosmed"))
        sosmed_html = f"<span class='social-chip'>{esc(sosmed)}</span>" if sosmed != "-" else "-"

        tiles = "".join([
            _tile("🪪", "NIM", esc(clean(data.get("nim")))),
            _tile("🎂", "Umur", esc(umur_text)),
            _tile("📍", "Asal", esc(clean(data.get("asal")))),
            _tile("🏠", "Alamat", esc(clean(data.get("alamat")))),
            _tile("🎯", "Hobi", esc(clean(data.get("hobbi")))),
            _tile("📸", "Sosial Media", sosmed_html),
        ])
        quotes = (
            _quote("💬 Kesan", clean(data.get("kesan"), ""))
            + _quote("✉️ Pesan", clean(data.get("pesan"), ""))
        )

        card_html = _flatten_html(f"""
        <div class='profile-card'>
            <div class='photo-pane'>
                <div class='card-index'>{i + 1:02d}</div>
                {photo}
            </div>
            <div class='info-pane'>
                <div class='jabatan-badge'><span class='jabatan-star'>⭐</span> {esc(jabatan)} <span class='jabatan-star'>⭐</span></div>
                <div class='profile-name'>{esc(nama)}</div>
                <div class='info-grid'>{tiles}</div>
                <div class='quote-grid'>{quotes}</div>
            </div>
        </div>
        """)
        st.markdown(card_html, unsafe_allow_html=True)
        shown += 1

    if shown == 0:
        st.info("Tidak ada anggota yang cocok dengan pencarian.")


menu = streamlit_menu()

# ==================================================
# DATA ASLI (DARI FILE YANG KAMU KIRIM)
# ==================================================
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ydZ_OtbYr3NL-hbc5P-BGxDligYL0O0Y",
            "https://drive.google.com/uc?export=view&id=1hfoIOi1lK8iCTzVKd3geGgF4fM4-JhBw",
            "https://drive.google.com/uc?export=view&id=1VV2HbOCcwTvTrEgIOVi2cYmt-_sXnmnf",
            "https://drive.google.com/uc?export=view&id=1V8BhdwZPjHl5EapK9Vb559p21ldEBSiX",
            "https://drive.google.com/uc?export=view&id=1OxtVXw215rIWDxoRLVRAI4JBIpMS2JFm",
            "https://drive.google.com/uc?export=view&id=1hg7bBopnrwvAAsBCJIKZASEo2FZSR1qv",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Ginda sangat menginspirasi aku untuk jadi mahasiswa yang aktif, ga cuma di akademik tapi di kegiatan kegiatan luar akademik",  
                "pesan":"semangat dan sukses terus bangg!! i look up to you"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@Muhammadaqil1111",
                "kesan": "Orang yang juga banyak memotivasi aku untuk jadi mahasiswa aktif",  
                "pesan":"Semoga segala urusannya selalu lancar ya bang"# 1
            },
            {
                "nama": "Efi Defiyanti",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya humble dan asikk!! seru banget denger penjelasannya pas wawancara.",  
                "pesan":"Kak Efi kerenn banget! hope to see you on another occasion :D"# 1
            },
           {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang qios terlihat pendiam tapi ternyata asik jugaa.",  
                "pesan":"aku sendiri jarang liat sekre cowo, big rispect buat bang qois."# 1
            }, 
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakaknya terlihat tegas dan teliti di segala hal, cocok banget bendahara!!",  
                "pesan":"semoga disetiap perhitungannya selalu balance ya kakk, semangat juga TA-nya kak >0<"# 1
            },
            {
                "nama": "Hafsa Fazilah Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "kak hafsa baik bangett dan keliatan excited banget waktu wawancara ^__^",  
                "pesan":"Bahagia selalu kakk, semoga selalu dikelilingi hal baik setiap harinya <33"# 1
            },          
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pat4K9gEqkOTFl0BxUePoEUk-FTCw8Ud",
            "https://drive.google.com/uc?export=view&id=1wKaWBSOOpfQQXavvf_xJi-VitApPZX-k",
            "https://drive.google.com/uc?export=view&id=1pSGYAiAEEZCeL_XgXClsw_Mb96RYzLbu",
            "https://drive.google.com/uc?export=view&id=1a1X9UUpch2r4qJiXR4qH1wGmkyu6nYIy",
            "https://drive.google.com/uc?export=view&id=1gYcOuv6meE0l0qOzxQ6vLepvEzSa309k",
            "https://drive.google.com/uc?export=view&id=1dPKaJUyM2kJ-lH9tC1D8GAsl-Ts604f3",
            "https://drive.google.com/uc?export=view&id=1Y6W9NtmupGct-4mdiUw8VWRvVYLfONRw",
            "https://drive.google.com/uc?export=view&id=1dhdTt-MN6vVavPlPnzPKsGEDJR7nn44y",
            "https://drive.google.com/uc?export=view&id=1rSku6HMaGfl_Oxdii47-gGZbJc7UuTWW",
            "https://drive.google.com/uc?export=view&id=1MUzsy5qWhCD95Hd3jZubJoiyAm-P4lGp",
            "https://drive.google.com/uc?export=view&id=1DipbJ82itZspxnloeDc4TZ38E_FuAZpW",
            "https://drive.google.com/uc?export=view&id=1gFkMA6oUPWPoUzoi3Wciao1btIYkKTLV",
            "https://drive.google.com/uc?export=view&id=13JaNa1XHINU5EY9qJVjJdIJasiYjxm97",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "aku pikir jadi baleg harus nonchalant, ternyata abangnya seru banget! waktu jadi asprak juga ga pernah marah marah ^__^ ",
                "pesan": "salam sehat dan salam sukses bang!!"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "oh how i loOveee her feminime energy! kak juee nyimut bgtt",
                "pesan": "pls stay as lovely as you are <33"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "bang dharu ramah dan baik! looks like orang pinter but still chill",
                "pesan": "sukses terus kedepannya bang dharu!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "kak siti ramah, asikk banget, dan seruuu!",
                "pesan": "Semangat terus menjalani perkuliahannya ya kakk ^__^"  # 1
            },
            {
                "nama": "Wan Naswa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "aura kakaknya lembut bangett, kaya ibu periii :3",
                "pesan": "semoga kakak selalu dikelilingi hal baik ya kak!!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro kerenn, dan orangnya baik!! ",
                "pesan": "Semangat dan sukses terus kedepannya bang"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "suaranya bagus banget!!! abangnya terlihat pendiam dan sepertinya emang pendiam??",
                "pesan": "Semangat terus dalam menjalanin perkuliahan dan segala kesibukannya bang!"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona keliatannya humoris, tapi bisa serius juga",
                "pesan": "semangat terus bang jonaa"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "aku pikir kakaknya galak.. tapi ternyata asik dan lucu jugaa",
                "pesan": "Bahagia selalu kak sekar!! semoga segala halnya dipermudah!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak yang ga kalah nyimutt >0<! soo humble dan kerenn",
                "pesan": "keep shining the way you are kak haniii"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "pertama kali liat bang niko pas PPLK. orangnya pinter dan berpikir kritis, cocok di baleg.",
                "pesan": "sukses terus bang niko!!"  # 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "kak nisa super humblee!! keliatan kerenn bangett.",  
                "pesan":"keep being as amazing as you are kakk!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica kaya independen woman!! lucu dan ramahh juga!",  
                "pesan":"Bahagia selalu ya kakk!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    Baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12TBYpWmW4pJfa8YLz8n_OKkGL9WFdi_f",
            "https://drive.google.com/uc?export=view&id=16blIAa_D3aVq0Ez1GX-PEljWUBcK2_Wy",
            "https://drive.google.com/uc?export=view&id=1YDqqBaL2i1hNTgkdCBATZwN2QYcKzc6e",
            "https://drive.google.com/uc?export=view&id=17bdrluhaQDgcDfTQfD7Nti1r3rAPrZW6",
            "https://drive.google.com/uc?export=view&id=1MwKuqPCjqA5EM75jTeUldyiLmOZx7yr_",
            "https://drive.google.com/uc?export=view&id=10aBIdO4ogGAiyvF5RJ--yfnIVeGq8MI1",
            "https://drive.google.com/uc?export=view&id=1bWYJliQWYBLk_mbtaya_EDtxozfmoqf8",
            "https://drive.google.com/uc?export=view&id=1MFuphjCdmEaIQFfl3NqjJl8AvgIc925z",
            "https://drive.google.com/uc?export=view&id=1HYcJ_5TuNofyAFx2qttb5oxN53kIvTqe",
            "https://drive.google.com/uc?export=view&id=1umzaM6kxAUE5zRKHmPXwH59t9FL9Z8c6",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "you're such a cool person! pembawaanya juga tenang dan kalem ^__^",  
                "pesan":"keep inspiring dan semoga selalu ada mood buat nulis di mediumnya ya kakk :D"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cantikk dan humble",  
                "pesan":"semangat terus menjalani hari harinya kak nadya!!"# 2
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "kak lia keren banget, menginspirasi!! kakaknya juga ramah dan baik hati <33",  
                "pesan":"keep growing dan bahagia selalu ya kakk"# 3
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "keliatannya pendiam, tapi tetep humble dan asikk!",  
                "pesan":"Semoga semua hal baik di dunia ini mendatangi kakak yaa :3"# 4
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "somehow vibesnya intimidating... tapi kak suci ternyata friendly banget",  
                "pesan":"keep smiling and live your life kak suciii!!"# 5
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "waktu pertama kali liat kakak, aku langsung SUKA bgt energy-nya (serius). salah satu orang paling aktif yang ada aja kegiatannya dan keliatan #independenwoman bgt sih aseliii. kakak nyimut, ntik, dubaicuwikuki i just lovee your personality and the way you inspiring people (me) about everything!! waktu aku tau kalo dimentorin sama kak aqilaa, aku super duper happy for reallll! kakak mentor yang selalu ngasih yang terbaik untuk anak-anaknya yaitu bayesian #welovekakaqila dan ternyata banyak juga ya agenda jadi anak kak aqila ahahaha #westilllovekakaqila!! two things yang paling sering aku inget tentang kakak adalah.. bunga matahari (ini sih udah icon) dannn ketawanya yang menggelegar wkwkw plsss ketawa, senyum, dan bahagia terus yaa kakk <33 ",  
                "pesan":"terima kasih udah jadi mentor kami dan bimbing kami selama inii, you've worked so hard and you deserve all the good things in this life. semoga semua kebaikan yang kakak berikan ke kami dan ke semua orang, juga kembali ke kak aqila dengan versi lebih baik lagii! semoga juga kakak ga pernah kehilangan semangat dan rasa excited ke hal-hal yang kakak suka yaa! keep shining as bright as a star andd please jangan lupa istirahat juga!! kalo ada enigma untuk mentor terkeren bakal langsung aku kasih ke kakak dan masuk ig #anakbangga ^____^ big love for you kak aqila zayyan salsabil gapake a >o< aduh ngebayangin bayes bakal jarang main bareng jadi sedih deh akuu..."# 6
            },                      
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "jago nge-MC dann keliatannya bang wiel adalah that one person who knows how to manage time well",  
                "pesan":"Bang ajarin aku nge-MC boleh ga..?"# 7
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "vibes awalnya kaya... galak.. tapi ternyata orangnya chill",  
                "pesan":"jangan lupa senyum walau dunia grasak grusuk :D"# 8
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Orangnya humoris, lucu banget waktu foto minta gaya melet, jujurr ga expect",  
                "pesan":"Jangan lupa ngesen kanan juga ya bang!"# 9
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "bang nando vibesnya kalem banget",  
                "pesan":"Semoga masih bisa ber-badminton di dunia yang penuh huru-hara ini ya bang"# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1srSfLh-CDTcFRY8qzNWxGBOpzJ37OSBp",
            "https://drive.google.com/uc?export=view&id=1DuOb0uY7TwXUA4MOaIB-GY_QJqpKEHw9",
            "https://drive.google.com/uc?export=view&id=1zVC7CTr1FeGHYo6TQzmGuHvEKy1WiVA9",
            "https://drive.google.com/uc?export=view&id=1QOD2ERsxj_WtYEDdz76GYpiYFB5URVP8",
            "https://drive.google.com/uc?export=view&id=1SeH8ispYMRFGeIYVJF4KrAjwiNPdUPhp",
            "https://drive.google.com/uc?export=view&id=1MVUHOtWJUFMowg8EYPNuDcdt5uyvj7f7",
            "https://drive.google.com/uc?export=view&id=1tQ6f8LZvuQIZXPezDEBif3GuDZK2b6j7",
            "https://drive.google.com/uc?export=view&id=1G5Yz2aKuKGrlCoE78UskKHqcvFPaGzKA",
            "https://drive.google.com/uc?export=view&id=1EmaWuZqO6M_xuNg0e7GkDJckjQflFudg",
            "https://drive.google.com/uc?export=view&id=1LzN_IrxMtj77LxmVzP2m-HE4G-pycvXl",
            "https://drive.google.com/uc?export=view&id=1AxGp2Rr57qCgGtMXCXYl6-7GS_nSUr4s",
            "https://drive.google.com/uc?export=view&id=1AA2w567JlNSJ8NMYXxWME1Dsk3EGAHY2",
            "https://drive.google.com/uc?export=view&id=1QBcMd4XMOchHpFxMppMBTnE0Pg_-4GpP",
            "https://drive.google.com/uc?export=view&id=14mDLez8xhcGGpHvhGRJ2vclDEQIkeQ8p",
            "https://drive.google.com/uc?export=view&id=1ZqvuUyl9GcHxKmtWRRua8nPzWErAYPg4",
            "https://drive.google.com/uc?export=view&id=1CUuLY7xTDq2f2BrEi7P0h56J_K97mWgG",
            "https://drive.google.com/uc?export=view&id=1S7Sy2pSq1s8TlsRpkXNgZPhBBacDAYiv",
            "https://drive.google.com/uc?export=view&id=1_HZjhgDMJiSPQoQMkO4QVatEJwdpY7Gk",
            "https://drive.google.com/uc?export=view&id=1SGROZsVQyIFjUVATYn6EByZWgCVXqDvV",
            "https://drive.google.com/uc?export=view&id=1G0fa9cfDTnXaN217imubXuUddXpi18_w",
            "https://drive.google.com/uc?export=view&id=19Qmtaq3kdamYXs1D7l0fa6jthJw3EFse",
            "https://drive.google.com/uc?export=view&id=1QU4Os4byg3EfzNaYb-LRuUQIX4eSqNpV",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "1234501014",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biyokcb",
                "kesan": "Orangnya ramah dan baik bangett! bang bio juga salah satu orang yang menginspirasi dan memotivasi",
                "pesan": "Semoga semua urusannya lancar dan dipermudah ya bangg! semangat terus bang fabioo!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "Kakak tanty baik dan perhatian banget t__t tipe orang yang selalu buat orang lain nyaman <33",
                "pesan": "i hope all the kindness that you give for us, come to you as well ya kak!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya terlihat baik dan softspoken",
                "pesan": "somoga next time kita berkesempatan main uno bareng ya bang hahaha!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Bang apiss lucu bangett, super duper ramah!! selalu keliatan ceria dimanapun",
                "pesan": "jangan lupa istirahat bang!! tetep ceria terus ya :D"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "bang gathfan baik dan ramahh!!",
                "pesan": "semangat terus menjalani hari harinya bang!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Awalnya aku kira bang keya pendiam, ternyataa asikk! kadang suka buat punch line hahaha",
                "pesan": "terimakasih sudah menjadi kadiv PIKA yang chill dan manteplah pokoknya bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "Kalo bang alsi terlihat pendiam, dan memang pendiam sih sepertinya",
                "pesan": "semangat dan sukses terus bang!!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "kak viola cantik bangett! i love your vibes frfr!!",
                "pesan": "Bahagia selalu kak violaa :3"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Make Up",
                "sosmed": "@sher_renna",
                "kesan": "Kakak nyimut-nya mikfes >< super humble!!",
                "pesan": "keep shining as bright as you are kak sheren <33"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "kak risa baik dan ramahh, tapi jujur awal ketemu agak intimidating vibesnya.. hehe ",
                "pesan": "be happy always kak risaa!!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kak fadya yang kalem dan softspoken <33",
                "pesan": "Semoga selalu dikelilingi hal baik ya kakk!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakak asprak PK dan tutor ALE! sabar banget ngajarin kami :3",
                "pesan": "Tetap semangat dan jangan lupa istirahat kak faizaa!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik dan super humble!!",
                "pesan": "Kak melva, sebenernya botol minum kakak masih ada di aku..."
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Kak vannisaa yang keliatan kalem dan tenang",
                "pesan" : "apakah boleh aku ikut nonton khw bareng kak... :3"
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "124450119",
                "asal" : "Jambi",
                "alamat" : "Sabah Balau",
                "hobbi": "belajar",
                "umur" : "20",
                "sosmed" : "krnylee",
                "kesan" : "Kakak cantik yang baik hati",
                "pesan" : "Semoga selalu sukses dalam hal apapun kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "kak elsa lucu banget! punya banyak cerita seruu",
                "pesan" : "Semoga semakin banyak cerita cerita serunya ya kakk!"
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kak lovi yang selalu excited kalo bercerita, dan kalo ketawa susah berhentinya hahah",
                "pesan" : "Semoga semakin banyak hal yang bisa buat kakak tertawa dan tersenyum kakk!!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "emang muka muka orang pinter sih, kerenn banget",
                "pesan" : "semangat terus bang kaleb!."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Lampung Utara",
                "alamat" : "Asrama TB3",
                "hobbi": "Membaca",
                "umur" : "20",
                "sosmed" : "@syaafiqui",
                "kesan" : "oarang yang diem diem jago!!",
                "pesan" : "Big respect buat bang syafiq!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "20",
                "sosmed" : "henryferdianto",
                "kesan" : "bang henry ramah dan emang keliatan banget kaya orang pinter!!",
                "pesan" : "semoga setiap langkah abang selalu dimudahkan ya bangg!!"
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Gitar",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Surprisingly, bang manuel seruu banget!! super humble dan fun pokoknya!",
                "pesan" : "Sukses terus bang! semoga bantal abang selalu dingin."
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "123450048",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "walau cuma punya sedikit kesempatan untuk bertemu bang fadil, i know that he was a good person.",
                "pesan" : "you'll be remembered with kindness, rest peacefully bang."
            },
        ]

        display_images_with_data(gambar_urls, data_list, menu)

    mikfes()
# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gfOQJwtZoAnFS4KmvHi2V4zkYtzgHoqM",
            "https://drive.google.com/uc?export=view&id=1bqaRqcF7k9tJ79esdQeTtRE2lhS3JsPF",
            "https://drive.google.com/uc?export=view&id=13hZWJMAPc-98hgFmOIpfTrJ-YkLePM2R",
            "https://drive.google.com/uc?export=view&id=1PeD_QiHk1V0HibiIFx9izht5BuPCCblz",
            "https://drive.google.com/uc?export=view&id=1uvVew_qfI-rjgwT9WgEH7MBwfK8Hbeoo",
            "https://drive.google.com/uc?export=view&id=1ui1lNQKFedclV5tF7VuJaTA5ZFyXjryK",
            "https://drive.google.com/uc?export=view&id=1c_-pxSQtueTi692b2_BOoONMopxwOu8d",
            "https://drive.google.com/uc?export=view&id=1NDNcSi4ww51CNHFXMdV7b6EVF9vpok9R",
            "https://drive.google.com/uc?export=view&id=1tX9bahrSgZuxjh2E7h6H378aWU6k97MV",
            "https://drive.google.com/uc?export=view&id=1pKxSQdci9hjq64DoEPkox8P1aHmmdz8E",
            "https://drive.google.com/uc?export=view&id=1CZy4V5gThU2f3irXUD_9xEEv3NZmSrGc",
            "https://drive.google.com/uc?export=view&id=1FfoBmLyYzGllO2QFnwy1-yWX7urhjRQV",
            "https://drive.google.com/uc?export=view&id=14GEJJTQakle_pzwjEzjZKIMYsvXQA9XJ",
            "https://drive.google.com/uc?export=view&id=1ztkYZYujsdoei-XGb_bzZNHOOvGlaTnH",
            "https://drive.google.com/uc?export=view&id=103tXgeRpCFuBm-j4ShT-fEO1T_-9-BdA",
            "https://drive.google.com/uc?export=view&id=1S-B3i5Ir9Ps2DwT3C6tUmI1cd9DNlHqB",
            "https://drive.google.com/uc?export=view&id=1e_Sr7EGqLSg3jxMpH-01PB7p6ce9kmWP",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket pantai",
                "alamat": "Samping kos capo",
                "hobbi": "ngerjain tugas",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakak cantik dan independen woman vibes!",  
                "pesan":"semangat terus menjalani hari harinya ya kakk"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semoga segala halnya dipermudah kak vany!"# 3
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel berwibawa dan ramah",  
                "pesan":"Sukses selalu bang!!"# 4
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "Orangnya kalem dan baik",  
                "pesan":"Semangat menjalani hari-harinya bang azmi!"# 5
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake humoris, seru kalo diajak ngobrol",  
                "pesan":"Bahagia dan sukses selalu bang!!"# 6
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "awalnya intimidating, tapi setelah ngobrol seru dan humble!",  
                "pesan":"Semoga bahagia selalu bang!!"# 7
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Terlihat aktif dan selalu bersemangat!",  
                "pesan":"Keep growing stronger kakk!!"# 8
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "keliatannya pendiam, tapi tetap ramah dan baik",  
                "pesan":"Semangat terus menjalani huru hara dunia ya bang!"# 9
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@putrimannaa",
                "kesan": "Kak putri cantikk! baik dan humble!!",  
                "pesan":"keep shining as the way you are kakk"# 10
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@queentanaabila",
                "kesan": "kakaknya baikk banget, selalu ramah dan tersenyum",  
                "pesan":"Bahagia selalu kak! semangattt!!"# 10
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "orangnya asik dan bisa mencairkan suasana",  
                "pesan":"Semoga bang desman selalu didekat hal-hal baik!"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel cantikk dan baik hatii",  
                "pesan":"sehat dan bahagia selalu kakk"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "orangnya baik dan super humble",  
                "pesan":"semoga disetiap perempatan selalu muncul lampu hijau kak"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "keliatannya easy going dan ramahh!",  
                "pesan":"Semangat terus kuliah dan damskusannya bang"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakaknya gemess, ramah, dan terlihat happy selaluu",  
                "pesan":"Semoga selalu dikelilingi hal baik ya kakk"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya asik dan seru",  
                "pesan":"sukses selaluu bang!"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@avi.nhr",
                "kesan": "Kakak nyimut! baik dan kalem",  
                "pesan":"Semangat terus kakak salavi!!"
            }
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RSyOIpG_cPZOyUW5Q8-OtK6b6QuVvSwT",
            "https://drive.google.com/uc?export=view&id=1JC2yjJEF_JgwUHFeH6dMMe5lqLlfbTtj",
            "https://drive.google.com/uc?export=view&id=1zgy9fHd4eJp4vwwHO0jMuTq6Ks5RZ_ac",
            "https://drive.google.com/uc?export=view&id=1ceivkO29XC4TK-mDsmu7pJsOjfUOV3n5",
            "https://drive.google.com/uc?export=view&id=10dW3W_7BLBosSNuPWaTIKW4AkqrArgSt",
            "https://drive.google.com/uc?export=view&id=1Al74rhvsAxTap_JmX0CIlqWNkvIKln5i",
            "https://drive.google.com/uc?export=view&id=1miBRassianhSU3H4HCn-zdUJvyzD6647",
            "https://drive.google.com/uc?export=view&id=16mdq0P9jn3UuJjm2Mjy-72-lXz1cynmb",
            "https://drive.google.com/uc?export=view&id=1tgHo4LVNrluIng9iVUFKxBWjyoqx8iiH",
            "https://drive.google.com/uc?export=view&id=1IB2nmlu0uwD_MwgzDkKJ6h2oOSI5-rsw",
            "https://drive.google.com/uc?export=view&id=1GAKzHlNZwD7VH0fxb7YZNoxK-vQVcwqg",
            "https://drive.google.com/uc?export=view&id=1gUHaieBb7Sd1tAlP-HuT8MWoAJW5EaAp",
            "https://drive.google.com/uc?export=view&id=1WizmYLNF3Qot074PGYPwz7306bUs1l74",
            "https://drive.google.com/uc?export=view&id=1tOp5rmxoGGhL58jgE-RjohaIlnVWyE5Q",
            "https://drive.google.com/uc?export=view&id=18u-EqMmN2VqCrn3R0hEBYgdZILXZfEvd",
            "https://drive.google.com/uc?export=view&id=1KxYnQ6YlzcZL56YnakIrCTp9xYw3rC8T",
            "https://drive.google.com/uc?export=view&id=1lZYliFMG8yr4_K8fhKI33hVGHYwKMsV3",
            "https://drive.google.com/uc?export=view&id=10uRchlRJFjKYiLRtbfDpsR3w-JE_rZ4r",
            "https://drive.google.com/uc?export=view&id=17R8k2CArLTErvIlIsS5J9PSZfYsxEsjH",
            "https://drive.google.com/uc?export=view&id=1RD0Y2dcaE6hhpgGpyTPKVinbAeZ8IXFK",
            "https://drive.google.com/uc?export=view&id=1DS8O3H4IMVmi7wusK42shEUKbmSKwf6L",
            "https://drive.google.com/uc?export=view&id=1frXT5zHoZb6CUP1BSqIwA7Nc4qpUoUZ_",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "kakak arini yang extrovert dan sangat cocok menjadi kadep eksternal",  
                "pesan":"sukses dan semangat 45 terus ya kakk"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya ramah dan seruu",  
                "pesan":"semangat terus kuliahnya kak nabyla!"# 2
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Mancing Keributan",
                "sosmed": "@adityafq",
                "kesan": "abangnya super duper humble dan supel!",  
                "pesan":"semoga bahagia selalu kakakk"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakaknya cantikk dan baik hati",  
                "pesan":"keep shining and keep growing kakakk!"# 4
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak selma imutt, baik, dan humble!",  
                "pesan":"semoga semua kebaikan yang kakak sebar, kembali ke kakak juga!!"# 5
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Pembawaan kakaknya tenang dan kalem",  
                "pesan":"Semangat terus menjalani hari harinya kak!"# 6
            },                      
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya selalu ceria dan ramah!",  
                "pesan":"Semoga ga pernah ada kerikil yang masuk ke sepatu kakak :D"# 7
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "1244500106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "abangnya kalem dan kayanya pendiam sih..",  
                "pesan":"Sukses terus bang bima!"# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "Sebelum liat mukanya aku pikir kembar sama bang bima!",  
                "pesan":"Semangat dan jangan menyerah!"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "kakaknya terlihat kalcer, super humble!",  
                "pesan":"Be happy always kakk!"# 10
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal":"Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "kakak yang selalu ceria dan baik hatii!",  
                "pesan":"Semoga gaada nyamuk yang ganggu pas lagi tidur!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "kakaknya imut dan keliatannya teliti sama hal kecil!",  
                "pesan":"Keep shining dan bahagia selalu kakakk!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya baik hati dan asikk!",  
                "pesan":"Semoga muncul banyak A di indeks setiap nilai ya kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "1234500552",
                "umur": "21",
                "asal":"Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"Semangat terus walau hidup kadang menyebalkan ya kakk!"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "123450103",
                "umur": "19",
                "asal":"Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Orangnya kalem dan baik!!",  
                "pesan":"Bang danil N fadillah siapanya bang daniel caesar!"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abangnya kaya pendiem, tapi asik juga!",  
                "pesan":"Semangat, berjuang, sukses!!!"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "bang yazid ramah dan baikk!",  
                "pesan":"Sehat dan bahagia selalu bang!!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Pertama kali liat waktu PPLK, keliatannya kalem",  
                "pesan":"Semoga nasi nya selalu pulen dan hangat"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "Abang extrovert yang emang eksternallah jiwanya, selalu seru kalo ngobrol bareng!!",  
                "pesan":"Semoga selalu ada hal yang bikin tersenyum ya bang jaldiii"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "123450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya baik dan asikk",  
                "pesan":"Semoga ga pernah kelupaan kerupuknya waktu makan nasgor!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak meiii nyimutt, humble dan seru bangett! banyak juga bakatnya wooww!",  
                "pesan":"keep shining as bright as you are kakakk, big lovee <33!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Keren! selalu inspiratif dan ramah ke semua orang",  
                "pesan":"Teruskan semangatnya bang! semoga semua halnya dipermudah!!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    eksternal()

# INTERNAL
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1INdR_LnD7K_rPi7vdt5hEnFMCwNsPVUX",
            "https://drive.google.com/uc?export=view&id=1d6TrTjnw_8y3C0P0oEWvcVopzdzYDLc0",
            "https://drive.google.com/uc?export=view&id=1YFuxLsYOHnWufxtLrxvnT46vNVWZitkb",
            "https://drive.google.com/uc?export=view&id=12q-16zfV3myeuDUbNO38M3GAR6kVclbt",
            "https://drive.google.com/uc?export=view&id=1ygu-_oxTST6cqs6oYLAcU87_y-71gdj6",
            "https://drive.google.com/uc?export=view&id=1AktRrk6KGzD0bzxwbD0tRXKk302Ghyph",
            "https://drive.google.com/uc?export=view&id=1exRIb9-DBhTf5mXHyYtzweEt6vzgDLbG",
            "https://drive.google.com/uc?export=view&id=1WE8wjCYCtDUouBngtUnFbsgYHZcQZ0Io",
            "https://drive.google.com/uc?export=view&id=1IM1iPQ1LSSkCTY4b_JyBGzSPIsLjOcAr",
            "https://drive.google.com/uc?export=view&id=1j2TnOQWy_O4IB3LbPTcv58CVZaPxa8qg",
            "https://drive.google.com/uc?export=view&id=1ilHEOQSLHwgdKlGrcyG5AZnZlC7G7iCW",
            "https://drive.google.com/uc?export=view&id=1mJm8J-E4bryQMPNsNp3WxcPN86JlBGPU",
            "https://drive.google.com/uc?export=view&id=1d_jdq0z7u3e84H7wMsGeM4635SrXkOEe",
            "https://drive.google.com/uc?export=view&id=1ufI2V6vIME8iZg7kyQn8F_SRf8Xef677",
            "https://drive.google.com/uc?export=view&id=1bIr1OkaSCatUFMbhZzGwY6C-yC46l9mP",
            "https://drive.google.com/uc?export=view&id=1hTm-gSZCl1faZIitOF9rtaheMbUEWl3l",
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450006",
                "umur": "20",
                "asal":"Silikalang Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "awalnya bang haikal keliatan serem, tapi ternyata ramah dan seru!!",  
                "pesan":"sukses dan semangat terus bangg!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Untung Suropati",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@risma.mustika_",
                "kesan": "kakak cantik dan baik hatii!",  
                "pesan":""# 2
            },
            {
                "nama": "Muhammad Hanif Zaky",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang Sumatera Barat",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngikutin drama tiktok",
                "sosmed": "@hnfdzky_",
                "kesan": "ramahh dan vibes abangnya kalem",  
                "pesan":"Semoga dipermudah segala halnya bang!!"# 3
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "emang muka muka internal. aura kakaknya adem banget dan menenangkan!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Cika Adelia Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa Minang",
                "sosmed": "@cikamrbn",
                "kesan": "kakaknya baik dan super humble",  
                "pesan":"Bahagia selalu kak cikaa!"# 5
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "kakak cantik yang ramah ke semua orang!!",  
                "pesan":"Semoga selalu ada hal yang bisa buat tersenyum setiap hari ya kak!"# 6
            },                      
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Ngadu ikan cupang",
                "sosmed": "@muhvins_",
                "kesan": "abangnya baik hati dan humble!",  
                "pesan":"Tetap semangat dan jangan menyerah bang"# 7
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama Aqila",
                "sosmed": "snasaa._",
                "kesan": "another wajah wajah internal, emang cocok banget sih masuk internal!",  
                "pesan":"kakak kerenn! terus semangat ya kak"# 8
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam Itera",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya fun! seru banget kalo ngobrol bareng kak hanna",  
                "pesan":"Semoga dilancarkan segala urusannya ya kakk"# 9
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "one of icon damaskus inii! abangnya ramah dan baik",  
                "pesan":"Semoga semakin semangat kuliah dan damaskusannya bang!"# 10
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan Belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakak imut! keliatan kaya orang yang suka hal terorganisir",  
                "pesan":"Hobinya menarik banget jujur! mau tau dong eksperimennya kakk!"# 11
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "cerine.ipynb",
                "kesan": "lucu, selalu excited, ceritanya juga seruu!!",  
                "pesan":"Jangan lupa tidur kakk! btw username ig nya lucuu"# 12
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Keliatannya extrovert dan punya banyak cerita!!",  
                "pesan":"Mau dong dengerin lagu buatan bang jaya!"# 13
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya seruu dan asik!!",  
                "pesan":"semoga selalu dikelilingi hal baik kakk!"# 14
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal":"Kalianda, Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Berantemin kucing",
                "sosmed": "@rozakrabbani__",
                "kesan": "hobinya unik, abangnya ramah!",  
                "pesan":"Semangat pantang menyerah bang!"# 15
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",
                "sosmed": "@christiani8872",
                "kesan": "kakak asprak yang ga marah marah!",  
                "pesan":"semangat terus ngasprak dan ngastutnya kakk!"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KkouExP--LKinMt9OZhJzBTaMsi1yO9r",
            "https://drive.google.com/uc?export=view&id=1_1H0r-uXwnTXhWyqV9WS-fiBCi-lgaay",
            "https://drive.google.com/uc?export=view&id=14mjK9a82NVkX5jXro0WvgoYUDK1jQX9c",
            "https://drive.google.com/uc?export=view&id=1I6mzqmRLnMvybMvRHEkSlBP7wa9chfW7",
            "https://drive.google.com/uc?export=view&id=1LapJ4H1Wj50BzzieyUfKtBhd3bDhK4-a",
            "https://drive.google.com/uc?export=view&id=1xT_o9evhzXYMDt4gtQNatd9tzXCbQHT7",
            "https://drive.google.com/uc?export=view&id=1jUkybDQ2jGewgH3ghmRaG2XPPRJQjshX",
            "https://drive.google.com/uc?export=view&id=1AlI3-kece9780D690876DUqozybxY0-C",
            "https://drive.google.com/uc?export=view&id=1I7h1oQ-n-SZnjkLh4FkkO3PaRAEYmQ00",
            "https://drive.google.com/uc?export=view&id=1oSwL3JZrr_YxvZgkGb94JStUmte45eD6",
            "https://drive.google.com/uc?export=view&id=1gkhg_XULkMRyZKlX5IIncoqXM1u3X1p9",
            "https://drive.google.com/uc?export=view&id=1y686ZvnNW456zTukhn-8EnyzyoYjmR83",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "bang ihsan asik dan bisa mencairkan suasana",  
                "pesan":"mau ditraktir juga dong bangg!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya imut dan cantik! super humble",  
                "pesan":"keep shining and keep growing stronger kakakk!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "kakaknya seruu, pecinta marvel",  
                "pesan":"mau banget marathon nonton series marvel bareng!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "abang operator, kalem, dan selalu tenang",  
                "pesan":"semangat terus menjalani hari harinya bang!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "keliatannya pendiem, kakaknya juga kalem",  
                "pesan":"semangat kejar mimpi sampai negeri cina!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abang asprak alpro, selalu ramah",  
                "pesan":"semoga segala halnya dilancarkan!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "kakaknya asik dan menyenangkan",  
                "pesan":"semoga tidurnya selalu nyenyak kak!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "kakaknya ramah dan baik hati",  
                "pesan":"semangat terus sampe jadi bilioner ya kakk!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "humoris dan sering buat ketawa pas wawancara",  
                "pesan":"semangat terus dan jangan menyerah bang!!"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "abangnya santai dan kalo ngobrol enjoy aja",  
                "pesan":"partner mancingnya bang iqbal bukan?"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Selalu ceria dan tersenyum",  
                "pesan":"semoga selalu ada hal yang bisa bikin tersenyum setiap hari!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "kakaknya baik dan selalu ramah kesemua orang",  
                "pesan":"semangat terus sampe jadi miliyader!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    ssd()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P4CPvEx5rM91u5tR1eiUtfO8zBQmZMpb",
            "https://drive.google.com/uc?export=view&id=1l2AVFDgb6ySK7PfQoH059Cl2sgmSUm-1",
            "https://drive.google.com/uc?export=view&id=1yy-y9DR_MQlGdY39ixoLHskpihCP3ZWF",
            "https://drive.google.com/uc?export=view&id=1eE0yGXYbZm5n0Imtu33xg-g8eAIRiKSp",
            "https://drive.google.com/uc?export=view&id=1HjH60tsELHzvQh6lkB2jdmSsqhi6SkrD",
            "https://drive.google.com/uc?export=view&id=1hrI9fD-hdNZ5Y3NqPI6xad5KL0rSoUoT",
            "https://drive.google.com/uc?export=view&id=18EyIxnpvmpmotiZuUegA4lgFQaUgMPi3",
            "https://drive.google.com/uc?export=view&id=1V8FuKSg9xrMBArhz1DdYPtUTqWV43eMN",
            "https://drive.google.com/uc?export=view&id=1-zWV2R4eB8SV99oheuUn0rGhw4MrdDB5",
            "https://drive.google.com/uc?export=view&id=15WX2iK_bK2meCYNZ2xaXYVBYXz5128yk",
            "https://drive.google.com/uc?export=view&id=1AaMmXeEw1k4kxHeLh2ousqw-FlPGQBHk",
            "https://drive.google.com/uc?export=view&id=1U4n6rFnz6fVjz76SqVgXtpQmADxnHvEo",
            "https://drive.google.com/uc?export=view&id=1JlPdfI3Qra90yW5_iLaI8IeKSVG6siz1",
            "https://drive.google.com/uc?export=view&id=1m7jZa_El_n9MYVkwT7lbaVvZ22uPhHmn",
            "https://drive.google.com/uc?export=view&id=1vvPk9MJgz7D_l8OlBbER8ae3ZIlpYaBQ",
            "https://drive.google.com/uc?export=view&id=1KyeyspPafr3zknFi_5ilmBas4W422Sz3",
            "https://drive.google.com/uc?export=view&id=1esxtRk7iDdVWE7g4PFbiR5olFqKOTgmA",
            "https://drive.google.com/uc?export=view&id=1esxtRk7iDdVWE7g4PFbiR5olFqKOTgmA",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "penjelasan kakaknya mudah dimengerti",  
                "pesan":"semangat terus ya kak naylaa!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya baik hati dan asikk",  
                "pesan":"semoga segala halnya dipermudah!!"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "abang dokum-coded sih!",  
                "pesan":"ajarin cara ambil foto yang bagus bangg"# 3
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "hobinya unik banget! kakaknya cantik dan ramah",  
                "pesan":"semoga bahagia selalu kakakk!"# 4
            },
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis dan membaca",
                "sosmed": "@n1tg.-",
                "kesan": "kakaknya keliatan punya wawasan luas dibidang ini!",  
                "pesan":"big respect! semangat terus kak"# 5
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakaknya baik dan super humble!",  
                "pesan":"semoga selalu dikelilingi hal baik kakakk"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kak bunga cantik dan cantik juga hatinya alias ramah dan baik!",  
                "pesan":"Semoga setiap isi bensin ga perlu ngantri dulu yahh!"# 7
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "1244500031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "penjelasaan abangnya mudah dimengerti!",  
                "pesan":"semangat dan sukses terus bang!"# 8
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakaknya baik, seru dan asikkk!",  
                "pesan":"jagoannya di F1 siapa tuh kak?"# 9
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450014",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@adindaadma",
                "kesan": "kakaknya imut dan selalu terlihat ceria!",  
                "pesan":"semoga selalu ada waktu untuk mancing ya kakk!"# 10
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gaada yang tau",
                "asal":"Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa",
                "kesan": "kakak cantik yang lucuu dan ramah!!",  
                "pesan":"kalo beras 5kilo berapa lama tuh ngitungnya kak?"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "1244500112",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@Xifasky",
                "kesan": "kakaknya baik hati dan selalu tersenyum!",  
                "pesan":"semoga semakin banyak hal yang bikin senyum kedepannya ya kak!"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "baik hati dan ramah ke semua orang!",  
                "pesan":"udah nonton film bang andrew yang mana aja kak?"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "abangnya ramah dan baik hatii!",  
                "pesan":"Semangat terus menghadapi kehidupan ini bang!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "super humble dan seru kalo ngobrol!",  
                "pesan":"nyuluh manuk itu ngapain bang?"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Piano",
                "sosmed": "@nzlhauly",
                "kesan": "kak nazlah ga sombong dan ramah ke semua orang!",  
                "pesan":"Semoga setiap buka kantong selalu nemu duit ya kak :D"
            },
            {
                "nama": "Allisha",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "kakak medkraf dan kakak damaskus!",  
                "pesan":"Keep growing stronger kak ashaaa!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "kakaknya lucuu kaya hobinya maniss!",  
                "pesan":"kayanya udahan ga sih kak makan manisnya? kakak kan udah manis :D!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    Medkraf()

if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nxVm2UnrkaIvcgLe2JjHNwYX5zoueyXp",
            "https://drive.google.com/uc?export=view&id=1GRkj0tJCkk3P6szYF3h8KgmNgZmN054T",
            "https://drive.google.com/uc?export=view&id=1L0xcfdhjXNB6cN-jGaZbPc3uruPNo9cd",
            "https://drive.google.com/uc?export=view&id=1RcATwyEFyoPiCWwy4SHzTJNTVSDg3gAt",
            "https://drive.google.com/uc?export=view&id=1TiQRYmtFcfKZc7S23jSX8HkWhmbQtIeW",
            "https://drive.google.com/uc?export=view&id=16kGfF_2hYRIOUG4h7q2kknURqePQ-DLR",
            "https://drive.google.com/uc?export=view&id=1cDa8Pqn1H6OCrYbskm7FM-kDzTP7cT3K",
            "https://drive.google.com/uc?export=view&id=1cRfQYgZTsMCi6_0OGvRC_cVbm1GcRmWa",
            "https://drive.google.com/uc?export=view&id=1uatFGfepC7RnwDefbjSdCWxp21Dm2ED-",
            "https://drive.google.com/uc?export=view&id=1tdb2GwUskKkAZiXEKUnREPAsyDqLPIt7",
            "https://drive.google.com/uc?export=view&id=12Ohj0ZtLdtpsAb9U8MVcVOm4VE9b8GKo",
            "https://drive.google.com/uc?export=view&id=1lQ6BMXP1uWdYcaheshjmGjcSiH5a-d0n",
            "https://drive.google.com/uc?export=view&id=15BaHBCnehHh-I5arll4-8NU3ySZ0LL6r",
            "https://drive.google.com/uc?export=view&id=1He0mzVX1chuEv0kvTqra9Hl3taXHrjy2",
            "https://drive.google.com/uc?export=view&id=1O01V3VQqXsQ1qUSGOfQL5vcjinweQXsB",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@kevinaj_",
                "kesan": "pembawaan abangnya tenang dan terlihat dapat diandalkan",  
                "pesan":"semoga segala halnya diperlancar dan dipermudah!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D.",
                "nim": "123450046",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "jujur vibesnya kelcer banget, sporty!! cocok banget di minbak",  
                "pesan":"info gunung untuk pemula dong kak!"# 2
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya kalem dan pendiam!",  
                "pesan":"abang tifosi bukan bang?"# 3
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Super humble dan lembut hati!",  
                "pesan":"Semoga ayam geprek yang dimakan ga pernah keras kaya batu"# 4
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450121",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Motoran bareng bang bryan",
                "sosmed": "@dafaelpriza_",
                "kesan": "bang dafa seru dan penjelasannya juga mudah dimengerti!",  
                "pesan":"Semangat dan sukses terus kedepannya bang!"# 5
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya selalu keliatan ceria dan asikk!",  
                "pesan":"semangat dan jangan pernah menyerah kakak!"# 6
            },                      
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jalan Pulau Damar",
                "hobbi": "Menjawab soal dari dosen dipapan tulis",
                "sosmed": "@afdal.03",
                "kesan": "abang NIM akuu! humoris dan asik orangnya!",  
                "pesan":"yuk kita kobarkan semangat 47 kita bang!"# 7
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "1244500024",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@slbnzw",
                "kesan": "Kakak cantik dan selalu ramah!",  
                "pesan":"Semoga disetiap perempatan selalu ketemu lampu hijau"# 8
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@mridwaan_22",
                "kesan": "keliatan pendiem kayanya emang pendiem sih..",  
                "pesan":"Sukses dan semangat terus bang"# 9
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@andra.lhm",
                "kesan": "super duper asik kalo ngobrol bareng! kalo cerita abangnya juga excited!!",  
                "pesan":"sekarang lagi nonton drakor apa bang andraa?!"# 10
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@bryantel_",
                "kesan": "abangnya kalem dan keliatan introvert",  
                "pesan":"bahagia selalu bang!!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "1244500067",
                "umur": "17",
                "asal":"Semarang",
                "alamat": "Kemiling",
                "hobbi": "Ternak sapi",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "abangnya terlihat pendiam dan cukup unik kalo dilihat dari hobinya!",  
                "pesan":"semoga ternak sapinya sukses sampe kebeli iphone 18 burgundy ya bang!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "kakanya selalu ceria dan tersenyum setiap saat!",  
                "pesan":"be happy always kak indah!!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@cacalvra",
                "kesan": "oh how i love her vibesss! so girly girly omg",  
                "pesan":"pls keep being as lovely as you're kakakk!"
            },
            {
                "nama": "Muhammad Rafka fatih Al Ghathfaan",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Tukang Parkir",
                "sosmed": "@muhammdrafka_",
                "kesan": "kirain abangnya galak... ternyata pendiem dan kalem orangnya!",  
                "pesan":"semoga semua matkul dapet A ya bang!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list, menu)
    Minbak()
