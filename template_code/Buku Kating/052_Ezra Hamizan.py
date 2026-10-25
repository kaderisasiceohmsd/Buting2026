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
# CSS
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

/* kesan/pesan panjang: klik untuk memperpanjang */
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
    """Untuk link Google Drive, coba beberapa format URL sampai ada yang berhasil."""
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
    """Unduh semua gambar secara paralel dan simpan di cache."""
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
    """Ubah nilai kosong / placeholder ('...', '@....', '-') menjadi default."""
    text = str(value if value is not None else "").strip()
    if not text or not text.strip(" .@-_"):
        return default
    return text


def initials(nama):
    parts = [p for p in re.split(r"\s+", nama.strip()) if p]
    return "".join(p[0].upper() for p in parts[:2]) or "?"


def _flatten_html(s):
    """Hapus indentasi & baris kosong agar Markdown tidak menganggapnya code block."""
    return "".join(line.strip() for line in s.splitlines() if line.strip())


def _tile(icon, label, value_html):
    return (
        f"<div class='info-tile'>"
        f"<div class='info-label'><span>{icon}</span>{label}</div>"
        f"<div class='info-value'>{value_html}</div>"
        f"</div>"
    )


QUOTE_LIMIT = 110  # lebih dari ini, teks dipotong dan muncul tombol "Baca selengkapnya"


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
# JABATAN TAMBAHAN (TERPISAH DARI BIODATA ASLI)
# ==================================================
# Label jabatan diambil dari data kepengurusan; daftar foto dan biodata asli tidak disentuh.
JABATAN_BY_NAMA = {
    "Ginda Fajar Riadi Marpaung": "Ketua Himpunan",
    "Muhammmad Aqil Ramadhan": "Sekretaris Jenderal",
    "Efi Defiyati": "Sekretaris 1",
    "Qois Olifio": "Sekretaris 2",
    "Hafsa Fazila Arradhi": "Bendahara 1",
    "Luthfia Laila Ramadhani": "Bendahara 2",
    "Ridho Benedictus Togi Manik": "Ketua Badan Legislatif",
    "Juesi Apridelia Saragih": "Sekretaris Badan Legislatif",
    "Dharu Cahyoaji Sasongko": "Kepala Komisi I Legislasi",
    "Gh Mikael Niko A S": "Staf Komisi I Legislasi",
    "Siti Sarifah Sumamah": "Staf Komisi I Legislasi",
    "Givaro Ananta": "Kepala Komisi II Pengawasan",
    "Afghanis Nursholehatunnisa": "Staf Komisi II Pengawasan",
    "Hani Qurrota Aini": "Staf Komisi II Pengawasan",
    "Jeremia Halim": "Staf Komisi II Pengawasan",
    "Monica Patricia Tanjung": "Kepala Komisi III Aspirasi dan Media Informasi",
    "Sekar Dini Widya Putri": "Staf Komisi III Aspirasi dan Media Informasi",
    "Jona Timothy Ogatse Panjaitan": "Staf Komisi III Aspirasi dan Media Informasi",
    "Wan Nashwa Alhasni Yuska": "Staf Komisi III Aspirasi dan Media Informasi",
    "Fathinah Nur Azizah": "Senator",
    "Nadya Ratu Anjani": "Kepala Biro Kesekretariatan",
    "Dwi Rahma Fitriani": "Staff Biro Kesekretariatan",
    "Helmy Surya Pratama": "Kepala Biro Aspirasi dan Media Komunikasi",
    "Fernando Dimetrius Barus": "Staff Biro Aspirasi dan Media Komunikasi",
    "Suci Aulia": "Staff Biro Aspirasi dan Media Komunikasi",
    "Wielman Itolo Halawa": "Staff Biro Aspirasi dan Media Komunikasi",
    "Lia Hana Ichisasmita": "Kepala Biro Kajian Strategis dan Propaganda",
    "Aqila Zayyan Salsabil": "Staff Biro Kajian Strategis dan Propaganda",
    "Hazel Mahesa Handhaka": "Staff Biro Kajian Strategis dan Propaganda",
    "Arienta Khusnul Ananda": "Kepala Departemen PSDA",
    "Vany Salsabila Putri": "Sekretaris Departemen PSDA",
    "Nobel Nizam Fathirizki": "Kepala Divisi Kaderisasi",
    "Afriza Azmi": "Staf Kaderisasi",
    "Ayake Alfatih Ramadan": "Staf Kaderisasi",
    "Caesar Ozora Alrando": "Staf Kaderisasi",
    "Euodia Meiliana Fredita": "Staf Kaderisasi",
    "Haikal Seventino Tamba": "Staf Kaderisasi",
    "Putri Manna Anantama Simbolon": "Staf Kaderisasi",
    "Queenta Thifaal Nabila": "Staf Kaderisasi",
    "Desman Velius Halawa": "Kepala Divisi Peningkatan Mutu Anggota",
    "Azzelya Thianandry": "Staf Peningkatan Mutu Anggota",
    "Charrlindah": "Staf Peningkatan Mutu Anggota",
    "Jeremi Marolop P. Situmorang": "Staf Peningkatan Mutu Anggota",
    "Nabila Nur Azizah": "Staf Peningkatan Mutu Anggota",
    "Rafli Al Mansyah Tambunan": "Staf Peningkatan Mutu Anggota",
    "Salavi Naharani": "Staf Peningkatan Mutu Anggota",
    "Fabio Banyu Cyto": "Kepala Departemen Mikfes",
    "Tanty Widiyastuti": "Sekretaris Departemen Mikfes",
    "Fadil Prasetyo Alfaritzi": "Kepala Divisi Professional Skill Development",
    "Manuel Frederika": "Anggota Professional Skill Development",
    "Ni Made Okta Viola Darma Putri": "Anggota Professional Skill Development",
    "Risa Romadona": "Anggota Professional Skill Development",
    "Vannisa Ramadhani": "Anggota Professional Skill Development",
    "Yulia Cristine Malau": "Anggota Professional Skill Development",
    "Akeyla Fairuz Shafi": "Kepala Divisi Pusat Inovasi dan Kajian Akademik",
    "Elsa Sitorus": "Anggota Pusat Inovasi dan Kajian Akademik",
    "Fadya Izzatul ‘Aini": "Anggota Pusat Inovasi dan Kajian Akademik",
    "Lovianora Saragih": "Anggota Pusat Inovasi dan Kajian Akademik",
    "M. Alsi Syahrulloh": "Anggota Pusat Inovasi dan Kajian Akademik",
    "Sherena Florencia": "Anggota Pusat Inovasi dan Kajian Akademik",
    "Razin Hafid Hamdi": "Kepala Divisi Research & Development",
    "Faiza Try Anjani": "Anggota Research & Development",
    "Gathfan Nadif Ali": "Anggota Research & Development",
    "Hafidz Wahdiansyah": "Anggota Research & Development",
    "Kaleb Filbert Istel": "Anggota Research & Development",
    "Melva Shaprina Febrianti": "Anggota Research & Development",
    "Muhammad Syafiqul Falakh": "Anggota Research & Development",
    "Rifky Henry Ferdianto": "Anggota Research & Development",
    "Arini Puteri Elandra": "Kepala Departemen Eksternal",
    "Nabyla Sharfina": "Sekretaris Departemen Eksternal",
    "Khoirul Muttoharoh": "Kepala Departemen Hubungan Luar",
    "Ahmad Rizky": "Staff Ahli Hubungan Luar",
    "Adinda Deswita Maharani": "Anggota Hubungan Luar",
    "Ahmad Bimo Akbar Arkana": "Anggota Hubungan Luar",
    "Alfaya Abiyyi": "Anggota Hubungan Luar",
    "Asri Meilani": "Anggota Hubungan Luar",
    "Bima Ekayasa": "Anggota Hubungan Luar",
    "Indah Khairunnisa": "Anggota Hubungan Luar",
    "Riska Erlis Dayu Tiara": "Anggota Hubungan Luar",
    "Yollanda Agustina": "Anggota Hubungan Luar",
    "Aditya Taufiqurrohman": "Kepala Divisi Pengabdian Masyarakat",
    "Fathya Intami Gusda": "Staff Ahli Pengabdian Masyarakat",
    "Tarisya Hidayatul Rahmi": "Staff Ahli Pengabdian Masyarakat",
    "Ashila Islamisahfa Vanisha": "Anggota Pengabdian Masyarakat",
    "Danil N Fadillah": "Anggota Pengabdian Masyarakat",
    "Favian Arkaanda": "Anggota Pengabdian Masyarakat",
    "Muhammad Fathiy Zumar Yazid": "Anggota Pengabdian Masyarakat",
    "Muhammad Rizaldi": "Anggota Pengabdian Masyarakat",
    "Saskia Nova Magdalena": "Anggota Pengabdian Masyarakat",
    "Selma Siti Aisyah": "Anggota Pengabdian Masyarakat",
    "Haikal Fransiskus Simbolon": "Kepala Departemen Internal",
    "Kharisma Mustika Sari": "Sekretaris Departemen Internal",
    "Hanna Gresia Sinaga": "Kepala Departemen Keharmonisasian",
    "Ahmad Farhan Ghani": "Staff Ahli Keharmonisasian",
    "Aisyah Khairun Nisa": "Anggota Keharmonisasian",
    "Cerine Sihotang": "Anggota Keharmonisasian",
    "Jaya Saputra Tamba": "Anggota Keharmonisasian",
    "Najla Nursyifa": "Anggota Keharmonisasian",
    "Rozak Ramdani": "Anggota Keharmonisasian",
    "Teresa Christiani Purba": "Anggota Keharmonisasian",
    "Muhammad Hanif Dzaky Arifin": "Kepala Divisi Kerohanian",
    "Audina Fitria": "Anggota Kerohanian",
    "Cika Adelia Br Marbun": "Anggota Kerohanian",
    "Gustin H. Tampubolon": "Anggota Kerohanian",
    "Muhammad Harvinsyah": "Anggota Kerohanian",
    "Rafa Sabina Fahimah": "Anggota Kerohanian",
    "Ihsan Maulana Yusuf": "Kepala Departemen SSD",
    "Hanifah Inaya Sari": "Sekretaris Departemen SSD",
    "Afifah Fauziah": "Kepala Divisi Kemitraan",
    "Hasan Nur Ramadhan": "Anggota Kemitraan",
    "Layina Ropiqo": "Anggota Kemitraan",
    "Moch. Iqbal Az-Zahir": "Anggota Kemitraan",
    "Talitha Justine": "Anggota Kemitraan",
    "Anadia Carana": "Kepala Divisi Kewirausahaan",
    "Abdillah Fikri Al pome": "Staf Ahli Kewirausahaan",
    "Afdhal Rahmad Setiawan": "Anggota Kewirausahaan",
    "Anggun Nita": "Anggota Kewirausahaan",
    "Della Anisa Fitri": "Anggota Kewirausahaan",
    "Nayla Salsabila Fathianisa": "Kepala Departemen Medraf",
    "Donna Maya Puspita": "Sekretaris Departemen Medkraf",
    "Labo John Noel Napitupulu": "Kepala Divisi Dokumentasi",
    "Anash Tasya Ausyaqila": "Anggota Dokumentasi",
    "Felisya Nabila Putri Nugroho": "Anggota Dokumentasi",
    "Muhammad Razan Maulana Pratama": "Anggota Dokumentasi",
    "Sania Dwi Ayu Lestari": "Kepala Divisi Media dan Konten Spesialis",
    "Allisha": "Anggota Media dan Konten Spesialis",
    "Alya Ramadhanti": "Anggota Media dan Konten Spesialis",
    "Bunga Clarisa Sefa": "Anggota Media dan Konten Spesialis",
    "Raihana Adelia Putri": "Kepala Divisi Visual Design",
    "Nazlah Aulia": "Anggota Media dan Konten Spesialis",
    "Difanya Husakina": "Anggota Media dan Konten Spesialis",
    "Daffa Kharisma Adzana": "Anggota Visual Design",
    "Edsel Adya Pradipta": "Anggota Visual Design",
    "Lucia Advencia Rachel Nainggolan": "Anggota Visual Design",
    "Shafa Delaila Azzahra": "Anggota Visual Design",
    "Zannuba Arifah Ilman": "Anggota Visual Design",
    "Kevin Antonio Junior": "Kepala Departemen Minat & Bakat",
    "Gusti Putu Ferazka Dhiyamika": "Sekretaris Departemen Minat & Bakat",
    "Ali Aristo Muthahhari Parisi": "Kepala Divisi Manajemen Aktivitas dan Kompetisi",
    "Ayu Andriani Parlina Wati": "Anggota Manajemen Aktivitas dan Kompetisi",
    "Dafa Elpriza": "Anggota Manajemen Aktivitas dan Kompetisi",
    "Juwita Sari": "Anggota Manajemen Aktivitas dan Kompetisi",
    "Muhammad Afdal Luthfi": "Anggota Manajemen Aktivitas dan Kompetisi",
    "Salsabila Nazwa Putri": "Anggota Manajemen Aktivitas dan Kompetisi",
    "Muhammad Ridwan": "Kepala Divisi Manajemen Minat dan Bakat",
    "Andra Ilham Bintang": "Anggota Manajemen Minat dan Bakat",
    "Bryan Paskah Telaumbanua": "Anggota Manajemen Minat dan Bakat",
    "Ghiyats Thabularasa Meardhy": "Anggota Manajemen Minat dan Bakat",
    "Indah Julia Mawar Pratiwi": "Anggota Manajemen Minat dan Bakat",
    "Jacinda Kesya Alvara": "Anggota Manajemen Minat dan Bakat",
    "Muhammad Rafka Fatih Al Ghathfaan": "Anggota Manajemen Minat dan Bakat",
}


# ==================================================
# FUNGSI MENAMPILKAN PROFIL (DESAIN BARU, DATA ASLI)
# ==================================================
def display_images_with_data(gambar_urls, data_list):
    # URL dan urutan foto tidak diubah; setiap foto tetap berpasangan dengan biodata pada indeks yang sama.
    images = load_images_b64(tuple(gambar_urls))

    st.markdown(
        f"<div class='section-head'><h2>{esc(menu)}</h2>"
        f"<span class='count-chip'>{len(data_list)} anggota</span></div>",
        unsafe_allow_html=True,
    )

    query = st.text_input(
        "Cari",
        placeholder="🔍  Cari nama, asal, atau hobi...",
        label_visibility="collapsed",
        key=f"cari_{menu}",
    )
    q = query.strip().lower()
    st.write("")

    shown = 0
    for i, data in enumerate(data_list):
        nama = clean(data.get("Nama"), "Tanpa Nama")
        if q:
            haystack = " ".join(
                str(data.get(k, "")) for k in ("Nama", "NIM", "Asal", "Alamat", "Hobi", "Sosmed", "Kesan", "Pesan")
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

        umur = clean(data.get("Umur"))
        umur_text = f"{umur} Tahun" if umur.isdigit() else umur
        sosmed = clean(data.get("Sosmed"))
        sosmed_html = f"<span class='social-chip'>{esc(sosmed)}</span>" if sosmed != "-" else "-"

        tiles = "".join([
            _tile("🪪", "NIM", esc(clean(data.get("NIM")))),
            _tile("🎂", "Umur", esc(umur_text)),
            _tile("📍", "Asal", esc(clean(data.get("Asal")))),
            _tile("🏠", "Alamat", esc(clean(data.get("Alamat")))),
            _tile("🎯", "Hobi", esc(clean(data.get("Hobi")))),
            _tile("📸", "Sosial Media", sosmed_html),
        ])
        quotes = (
            _quote("💬 Kesan", clean(data.get("Kesan"), ""))
            + _quote("✉️ Pesan", clean(data.get("Pesan"), ""))
        )

        jabatan = clean(JABATAN_BY_NAMA.get(nama), "Jabatan belum tersedia")
        jabatan_badge = (
            f"<div class='jabatan-badge'><span class='jabatan-star'>✦</span>{esc(jabatan)}</div>"
        )

        card_html = _flatten_html(f"""
        <div class='profile-card'>
            <div class='photo-pane'>
                <div class='card-index'>{i + 1:02d}</div>
                {photo}
            </div>
            <div class='info-pane'>
                <div>
                    <div class='profile-name'>{esc(nama)}</div>
                    {jabatan_badge}
                </div>
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

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=129sLrNkwocy-TWad2v30ElQ2wLnUJVld", # fajar
            "https://drive.google.com/uc?export=view&id=1g1ds2keXijPbW0-LgWHmhUsquKLaBgyS", # aqil
            "https://drive.google.com/uc?export=view&id=1NULBvdisNF5qOJu2_-YmdFI_nVO-N5th", # efi
            "https://drive.google.com/uc?export=view&id=1DWcMya75dsgt-zLeWuBgle7JfihPpovS", # qois
            "https://drive.google.com/uc?export=view&id=13S1AbQ5l8oz4NT8Qq8qF4RS2HAOBLXkF", # hafsa
            "https://drive.google.com/uc?export=view&id=1Nd9fsmdb2oj6mTY0KkXRu9sjDdfRqzh7", # luthfia
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM": "123450103",
                "Umur": "22",
                "Asal": "Batam",
                "Alamat": "Kesektariatan HMSD",
                "Hobi": "Push IMO",
                "Sosmed": "@jars_mrp",
                "Kesan": "bang him gacor parah, Kesannya berwibawa banget bang him",  
                "Pesan":"semangat terus bang him sampai semhas"# 1
            },
            {
                "Nama": "Muhammmad Aqil Ramadhan",
                "NIM": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariatan HMSD",
                "Hobi": "Dzikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "keren banget bang jen & menginspirasi, auranya sangar",  
                "Pesan":"gas terus bang jen, sehat selalu sampai tamat"# 1
            },
            {
                "Nama": "Efi Defiyati",
                "NIM": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "kakaknya ramah dan agaknya sangat mengerti keuangan",  
                "Pesan":"lancar selalu kuliahnya kak sampai Te A"# 1
            },
            {
                "Nama": "Qois Olifio",
                "NIM": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobi": "Mainin Surat",
                "Sosmed": "@qoisolifio",
                "Kesan": "bang qois orangnya ramah kelihatannya dan kayak orang bener kata temen saya bang",  
                "Pesan":"sehat selalu abang qois sampai tamat game kuliahnya"# 1
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "NIM": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Bertemu lulu",
                "Sosmed": "@Hafsafazilaa",
                "Kesan": "baik banget kakaknya dan ramah, sepertinya seru berbicara tentang uang-uangan dengan beliau",  
                "Pesan":"sehat selalu mengelola keuangan pribadinya kak sampai tamat"# 1
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM": "123450004",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobi": "Keliling Balam",
                "Sosmed": "@luthfiaarmdhni",
                "Kesan": "kadang lucu, kadang galak, kadang kiding, tapi baik banget kak lulu ini coy",  
                "Pesan":"sehat selalu dan semoga keuangan pribadi tidak boncos selama TA"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10z3HaZqfwXFWQWd1zlGqKZrDr3XJ-eE5", # Ridho
            "https://drive.google.com/uc?export=view&id=1G7JtBI_6xwXAtLifCijkZRXieMB2HSu9", # Juesi
            "https://drive.google.com/uc?export=view&id=1Igf1c9RNYW0PgDhDSeutWpM-C5rFu5Ij", # Afghanis
            "https://drive.google.com/uc?export=view&id=1hBCKDCGMYggtk6TrsrqCdHKVyvpTnEU3", # Dharu blm
            "https://drive.google.com/uc?export=view&id=1N6g-CikmtxCW6zK1NHUhCLUW1d1WW9PN", # Mikael
            "https://drive.google.com/uc?export=view&id=1kxYxz9kUkiuwFibdpiGvNwXIL0srqSXz", # Givaro
            "https://drive.google.com/uc?export=view&id=17ZjOZcMgNGV7oP4V-wDa5YLGyDURpN4e", # Hani
            "https://drive.google.com/uc?export=view&id=17HLZnX4SCbRTr2G9hkipt51LNR18Rme8", # Jeremia
            "https://drive.google.com/uc?export=view&id=1AXZFsWG2U7LX6BGdm1bvp7122NxheKPI", # Jona
            "https://drive.google.com/uc?export=view&id=1ZEsMMmg0qvm7scSuKmVXDAnj0kvJN6mE", # Monica
            "https://drive.google.com/uc?export=view&id=1-7oPk3m7ktKEhyoPORe9FVkhpGZmX7V9", # Sekar
            "https://drive.google.com/uc?export=view&id=1Mnw9FIYATL_0S0snHRpDYRYwfiDWauZ-", # Siti
            "https://drive.google.com/uc?export=view&id=1r55ASLWhR1nctcAGEguAnnDnOmS4JmH4", # Wan Nashwa

        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal": "Kuala lumpur",
                "Alamat": "GH",
                "Hobi": "Bernyanyi",
                "Sosmed": "@iamridhomanik",
                "Kesan": "abang kabaleg satu ini lucu dan baik serta asik, minusnya dibilang npd sama kakaknya",  
                "Pesan":"semoga selalu tetap stay always dipertahankan gaya percaya dirinya itu bang, mau saya contoh soalnya"# 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Singkawang",
                "Alamat": "Pelangi",
                "Hobi": "ngerepeat lagu lover dari taylor swift",
                "Sosmed": "@j__eesie",
                "Kesan": "kakaknya ramah banget, baik banget, asik banget, serba banget banget pokoknya",  
                "Pesan":"semoga vibes positifnya nular ke saya kak"# 1
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal":"Krui",
                "Alamat": "Jatimulyo",
                "Hobi": "Memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "sesuai dugaan, kakaknya ramah dan baik, apalagi pas tutor metnum (saya gapaham si sebenernya)",  
                "Pesan":"semoga dilancarkan segala urusan dan sehat selalu kaka"# 1
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Suka nonton AGZ",
                "Sosmed": "@ddharu_",
                "Kesan": "baik dan ramah banget kelihatannya, agaknya seru ngobrol bang dharu ini",
                "Pesan": "sehat selalu bang dharu, lancar selalu PKM nya"
            },
            {
                "Nama": "GH. Mikael Niko Antoni Setiadi",
                "NIM": "123450025",
                "Umur": "20",
                "Asal":"Jabung",
                "Alamat": "Jatiagung",
                "Hobi": "Jalan-jalan nyari mangsa",
                "Sosmed": "@me._kael",
                "Kesan": "kating kedua yang tiba-tiba spawn di wardat, waketang datasena yang aing kira serius brutal mode fokus on aktif, ternyata tidak jauh-jauh konyolnya sama saya sendiri, bedanya beda agama",
                "Pesan": "sehat selalu hubungan tembok tingginya bos niko, terimakasih pisangnya, semoga lancar meng-kabalegnya, moga banyak gebrakan wong kok uniknya bang awokawok"
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "20",
                "Asal":"Gunung Pesagi",
                "Alamat": "Sukabumi",
                "Hobi": "Minum Kopi",
                "Sosmed": "@givarooo",
                "Kesan": "bang givaro ini ngeri banget mukanya ga boong bang, kirain serius parah orangnya, ternyata salah besar saya",
                "Pesan": "sehat selalu bang giv, lancar sampai selesai game berjudul kuliahnya"
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "19",
                "Asal":"City Eart",
                "Alamat": "Sukarame",
                "Hobi": "Baca Au",
                "Sosmed": "@haniquratuain_",
                "Kesan": "kakak ini peminat nomor 1 bang ridho agaknya dalam menanggapi kepedean beliau, rispek banget saya kak",  
                "Pesan":"semoga yang dimau disemogakan kak"# 1
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal":"Beijing",
                "Alamat": "Teluk",
                "Hobi": "Olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "entah kenapa saya liat abang ini mirip Lo Kheng Hong bang, baik dan ramah gitu bang",  
                "Pesan":"sehat selalu bang jeremia kedua datasena bang"# 1
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Ngegym dan Koleksi Figure",
                "Sosmed": "@nagatseee",
                "Kesan": "gaya abang ini serius, kadang serius, kadang kiding ehehe",  
                "Pesan":"sehat selalu bang motoin orang yang tidur (bagi foto saya bang pls)"# 1
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "kakaknya ramah dan baik serta murah senyum kata teman saya kak",  
                "Pesan":"semoga selalu bahagia dan sehta selalu kak monica"# 1
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Pemda",
                "Hobi": "Main",
                "Sosmed": "@sekardnwp",
                "Kesan": "kak sekar ngeri kata orang, menurut saya biasa aja padahal, agak tegas tapi baik sekali sepertinya",  
                "Pesan":"sehat selalu kak, jangan tegas tegas amat kak, ngeri saya"# 1
            },
            {
                "Nama": "Siti Sarifah Sumamahsa",
                "NIM": "124450015",
                "Umur": "18",
                "Asal":"Palembang",
                "Alamat": "Kedaton",
                "Hobi": "Bikin Pempek",
                "Sosmed": "@syt.sarifa",
                "Kesan": "kakaknya kalem dan lucu pas dateng wwc, kirain lagi ngejokes kak maap heheh",
                "Pesan": "cepat sembuh kak, semoga selalu sehat kedepannya"
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "123450077",
                "Umur": "20",
                "Asal":"Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa",
                "Sosmed": "@nshaysk",
                "Kesan": "pas awal ketemu di pplk ramah banget kak wawa ini, baik banget juga",  
                "Pesan":"semoga selalu bahagia dan cepat tamat game kuliahnya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gv4XflB8QYJzK0zWRJEIY7uA9VPSPhkI",
            "https://drive.google.com/uc?export=view&id=1lywiJCx-TDSMUwE6EepcYSUZoBAmzvnk",
            "https://drive.google.com/uc?export=view&id=1Li-ErDRJIYJFgyT4p2C1BdA37ncklBvz",
            "https://drive.google.com/uc?export=view&id=1EccUlLrzWDpsrPCWZjUOTnqbpXBGYR16",
            "https://drive.google.com/uc?export=view&id=135J4MiaT7cyIgQjmoUUvgfZt6Qnb-ykF",
            "https://drive.google.com/uc?export=view&id=1JjByNCqRP2Gfg8BbogtePV1rggp6VHhd",
            "https://drive.google.com/uc?export=view&id=1IL0Zq5vcZm2zPXdINdRm5GLKX9GI07xs",
            "https://drive.google.com/uc?export=view&id=1YNx_0mQfzdVWZu0SQujrqkI6JkwrRe4V",
            "https://drive.google.com/uc?export=view&id=1DXy4MCZCWPOYZsA-5d8VAqTeBub-GJQe",
            "https://drive.google.com/uc?export=view&id=1AMT-zQObGWJzpk4G558GCm8ZKbwmrfnq",
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "kak jijah ini kalo dilihat auranya serius banget on aktif jadi ngeri saya, ternyata ngga sengeri itu geyz kakak senator kita",
                "Pesan": "semoga selalu enjoy dan tidak stress bermain game berjudul 'politik kampus'-nya kak, dan semoga yang diinginkan disemogakan"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "abang mister tuan kakak papa helmy ternyata bisa diajak ngejokes, kirain seriusnya terus terusan mode on aktif bang eheh",
                "Pesan": "semoga BYD nya dijauhkan dari marabahaya orang konyol yang berkendara di jalan bang"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "11 12 bang Helmy menurut saya, sama-sama baik dan ramah, kirain kaku ternyata asik coy bang nando ini",
                "Pesan": "sehat selalu bang, semoga workbenchnya dijauhkan dari error dan update tidak jelas"
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "dulu saya takut sama Kak Suci ini entah mengapa, ngeri gitu bawaannya kak, ternyata salah lagi saya, baik, ramah, anak kesayangan papa helmy juga sepertinya kak suci ini",
                "Pesan": "semangat selalu dalam mementorkan Cosval kak, semoga lancar selalu juga kuliahnya kak"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "public sepiking abang ini ngeri banget, jadi iri saya, sepertinya seru berdebat dengan bang wielman ini",
                "Pesan": "sehatt selalu abang wielman, moga debatnya menang terus dan moga nular pablik sepikingnya"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "kak ichi ini sekali serius alam semesta pun bisa dibuat bijak sepertinya, tapi kalo udah cape langsung balik ke setelan awal agaknya",
                "Pesan": "lancar selalu dalam semua hal yang dilakukan kak ichi, moga cepat tamat game 'kuliahnya'"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "kakak ini sunflowernya nge-sunflower banget loh ya, jujur agak males pas beliau ini ngajak dokum, tapi sebagai orang baik saya turuti, kadang kadang, kadang kiding & excited sendiri tapi tetap rispek saya",
                "Pesan": "semoga yang dimau disemogakan, maaf kalo banyak kurang ajarnya kak jujur cuma becanda (sumpa becanda kak, merasa salah saya), lancar selalu di semua hal yang dilakukan, dan maap kalo ngeselin serta belum sempurna dalam pelajaran menghargai serta memanusiakan mentor (kata-kata dari lubuk hati terdalam ini kak)"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "mister hazel sok cool sok keren kata temen aing bang (boong ini), sosok entitas yang tetiba muncul di kos kirain mau menindak saya (mukanya serius pas dateng pertama), ternyata ga jauh konyol dari saya, bedanya lebih gondrong aja",
                "Pesan": "kalo lagi yapping selipin punchline bang, kasian saya liat bang niko nge-punchline terus, pas kader serius, di kos misterius, gayanya sok keras, giliran di gas saya yang diem"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "kakanya ketawa mulu pas saya di wwc (jadi pengen ketawa juga sayanya), baik, ramah, template sih Kesannya ini kak, kirain misterius banget kakaknya ini, ternyata 11 12 sama kak jijah & kak ichi",
                "Pesan": "semangat selalu dengerin cerita golden retriever kami kak, moga tidak bosan-bosan mendengarkannya, sehat selalu dan semoga selalu dilancarkan dalam semua hal, dan semoga file surat-surat & template di bason tidak terhapus"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "kakaknya pendiem saya kira, ternyata salah lagi saya, baik, ramah, murah senyum, ka dwi ini penerus kak nadya banget ini",
                "Pesan": "semangat selalu kuliahnya kak terutama tugas yang disuruh meng-anukan workbench Mr. Ardika"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14XJ42fUwzVqn0ej6lWHzqGC_jwesJV5C",
            "https://drive.google.com/uc?export=view&id=1qSvkpChMK23IHL1aFahbAJfGmmsLaQcR",
            "https://drive.google.com/uc?export=view&id=1Hu8sNSqXyDnjVQ8NMcn75vj7J-7_3ugw",
            "https://drive.google.com/uc?export=view&id=1zJuSSv5E40fnuMqJryVfrruX-WckdXVE",
            "https://drive.google.com/uc?export=view&id=1zKp0pckhLjo44r9x8Pkg4QygfDiJqHcs",
            "https://drive.google.com/uc?export=view&id=147AFQknzFdbqn7S-DTHEMv-GLjfNXQqH",
            "https://drive.google.com/uc?export=view&id=1kKeTZDTjLfuMfsCqsBo233Xct_HbUC8z",
            "https://drive.google.com/uc?export=view&id=1IAd48iZguZ_OhM_i_sEkxHF9hqLvOD5Q",
            "https://drive.google.com/uc?export=view&id=1FE_-eDOUr77SF1mbRjptm1LMv0C-egCT",
            "https://drive.google.com/uc?export=view&id=1N1gXDGjxHw4PY9W9yHB5fepJK9IRtOX7",
            "https://drive.google.com/uc?export=view&id=1YhJo3siYdd8w34LOhFN4CLWBnIIjJIdl",
            "https://drive.google.com/uc?export=view&id=1z0SfBp31xJ1zwjulb0jVd3U2kvTMfZjd",
            "https://drive.google.com/uc?export=view&id=1gHuM-oquLBYCPRX6CKeA4k2E1SjBfXi4",
            "https://drive.google.com/uc?export=view&id=1IjJBixveNdc2bGRaQfiNZBEbgHZMYHdP",
            "https://drive.google.com/uc?export=view&id=1q9KjcgoTf0dm2PkVffummmes8zQm_WyS",
            "https://drive.google.com/uc?export=view&id=18dKyhT-6UsujRHTiVmy2Erio9nrYGrz1",
            "https://drive.google.com/uc?export=view&id=1hXE1szpfaHyp3rpMtZQsquHaH40PTbTT",
        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal":"Deket pantai",
                "Alamat": "Samping kos capo",
                "Hobi": "ngerjain tugas",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "kak arienta jujur keren tapi agak ngeri juga saya",  
                "Pesan":"semoga selalu semangat dan bahagia kakak kadep PSDA"# 1
            },
            {
                "Nama": "Vany Salsabila Putri",
                "NIM": "123450022",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Pudan Kost",
                "Hobi": "pacaran",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Kakak sekdep ini baik, keren, ramah, pas banget kak jadi partner kaka kadep",  
                "Pesan":"sehat dan happy terus ya kak"# 3
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Puri",
                "Hobi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "PROFESIONAL (testimoni ini bang), kalo baik ya baik banget, kalo jahat kayaknya gapernah (gokil)",  
                "Pesan":"ajarin ngoding & berfiekier krieties dong bang, sulap juga boleh kalo mau ngajarin bang"# 4
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "21",
                "Asal":"Malang",
                "Alamat": "Samping Pasar",
                "Hobi": "duel boxing sama reno",
                "Sosmed": "@friezaazmi",
                "Kesan": "bang azmi baik, kalo tegas ngeri banget men, tapi ternyata masih ada sisi fun-nya",  
                "Pesan":"sehat selalu bang Azmi, semoga tidak risih kalo pas maen ke kos saya ikut NIMbrung eheh"# 5
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450059",
                "Umur": "21",
                "Asal":"Solok",
                "Alamat": "Samping kost Ezra",
                "Hobi": "Masak ayam",
                "Sosmed": "@ykeall",
                "Kesan": "abang awak satu ini banyak betul kata-kata bijaknya, kata-kata anehnya pun juga banyak, tapi jujur sangat membantu baik akademik maupun perkembangan diri saya (mode yapping ini bang)",  
                "Pesan":"sehat selalu abang awak, semoga sehat selalu, anak kadernya sehat abangnya juga harus sehat la (mana katanya mau stop nganu lagi bang)"# 6
            },                      
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "20",
                "Asal":"Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Giring anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "bang caesar ini ngeri banget saya liat, tapi boong, asik asik aja abang caesar ini, mau sharing-sharing dan seru kalo diajak menganukan sesuatu",  
                "Pesan":"sehat selalu bang caesar, semoga lancar apa yang sedang dilakukan, saya tagih jawaban pas di wardat nanti bang kalo selesai tapi"# 7
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "18",
                "Asal":"Adam dan Hawa",
                "Alamat": "Depan kontrakan Yazid",
                "Hobi": "nonjokin orang",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "kak yud baik, kalo lagi lucu ya lucu",  
                "Pesan":"semangat selalu ya kak"# 8
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450032",
                "Umur": "18",
                "Asal":"Jambi",
                "Alamat": "Belakang Pemancingan",
                "Hobi": "Goreng ayam",
                "Sosmed": "@_haikaaall",
                "Kesan": "bang haikal baik, asik betul abang ini, mantabla pokoknya",  
                "Pesan":"semoga sehat dan selalu dilancarkan dalam segala hal bang"# 9
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450056",
                "Umur": "19",
                "Asal": "Rumah sakit",
                "Alamat": "Arga Kost 1 jalan Way Huwi gang Mawar Raya",
                "Hobi": "liatin bang Nobel main sulap",
                "Sosmed": "@putrimannaa",
                "Kesan": "kaka ini baik banget aslinya, rill testimonial no hoak hoak",  
                "Pesan":"semoga selalu bahagia dan sehat selalu kak putrii"# 10
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "18",
                "Asal": "Lampung Tengah",
                "Alamat": "Gang Cendrawasih",
                "Hobi": "Makan di wardat",
                "Sosmed": "@quenntanaabilaa",
                "Kesan": "Kak queenta baik dan ramah orangnya",  
                "Pesan":"Semangat terus ya kak kuliahnya & happy teruss!"# 10
            },  
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "1234500114",
                "Umur": "21",
                "Asal":"Nias",
                "Alamat": "GH Raya",
                "Hobi": "lompat batu",
                "Sosmed": "@desmanhal_",
                "Kesan": "bang desman baik, keren juga, berwibawa bang",  
                "Pesan":"sehat selalu bang desman!"# 11
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak azzel baik dan ramah",  
                "Pesan":"Semoga semua keinginan kak azzel tercapai"# 12
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450041",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cendrawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlln",
                "Kesan": "kakaknya baik",   
                "Pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 13
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "NIM": "124450111",
                "Umur": "17",
                "Asal":"Jayapura",
                "Alamat": "RS airan",
                "Hobi": "Nonton a day in my life",
                "Sosmed": "@jemarrro",
                "Kesan": "mister Jemar orangnya asik banget loh ya, kadang kidinng biasanya, kalo serius ngeri banget abang ini",  
                "Pesan":"semoga mister Jemar sehat selalu dan segala halnya diapakan dulu biar ga apakali yakan bang"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal":"Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main Roblox",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "Pesan":"Semoga kak nabila kuliahnya lancar"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "18",
                "Asal":"Sibolga",
                "Alamat": "Belwis",
                "Hobi": "Membaca peraturan rektor",
                "Sosmed": "@dearrfkvmfl",
                "Kesan": "Bang Rafli itu humble dan mudah berbaur dengan siapa saja terutama yang bikin peraturan rektorf",  
                "Pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@afi.nhr",
                "Kesan": "Kak Salavi seru, baik, ramah tamah, murah senyum",  
                "Pesan":"Semoga kak salavi selalu tercapai yang diselalukan"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k9qOgC8Jy5T1GmbUjAK9l40qnkTaiMEX",
            "https://drive.google.com/uc?export=view&id=11wUEBPV45C0U0Esc8qnXqPz1erOPp5DA",
            "https://drive.google.com/uc?export=view&id=1V08FJPHJT5_nqYunlbkbz_jwn_XhJQJD",
            "https://drive.google.com/uc?export=view&id=1iGumeR1S3U9yQqaU0i1G7Xco2Nhd1n_B",
            "https://drive.google.com/uc?export=view&id=1YGUPHII8Hy1woOPzwfTk8s8tg-I2Yu6C",
            "https://drive.google.com/uc?export=view&id=1a8_PVXZ_c_3i-Xewc-LenPHVuOHzy_K-",
            "https://drive.google.com/uc?export=view&id=11YvNKZTlvu3uzVQzu-9TZ_r-Pe0beaif",
            "https://drive.google.com/uc?export=view&id=1Z3NYAirEDmU1vcbMm1fyZjK9C75ug9gU",
            "https://drive.google.com/uc?export=view&id=1XQsULfmrta_F3nzPAK9_jocW53pkEil4",
            "https://drive.google.com/uc?export=view&id=1UGuUsRwoAog_sizQz65VhOxGOrJTcqYZ",
            "https://drive.google.com/uc?export=view&id=1vPPuZI7OaCHaMBm3VKq6o6nYC1dDaa35",
            "https://drive.google.com/uc?export=view&id=1Z7cgq9vQLJ_RwSZFEHui5IDNSdnSt8rg",
            "https://drive.google.com/uc?export=view&id=1peO0hywNeSkOEAT5ZkuPvV4OtiMtHMk5",
            "https://drive.google.com/uc?export=view&id=1jWQgs9QAwL39MDuqeGqYXPJnWxcQP4YT",
            "https://drive.google.com/uc?export=view&id=1bg8RNbkT-gPkKy7ErOLtg4ClUwPbfneZ",
            "https://drive.google.com/uc?export=view&id=1qRNbe8S3luyI5dWXcLgjlp8KL9cYJm1J",
            "https://drive.google.com/uc?export=view&id=1XOkAyTkb6Rsq6hpIzoUpd3bFwYMUtYw5",
            "https://drive.google.com/uc?export=view&id=1wQi2i23XB40jzw40NXj1vp-niCnsHbr1",
            "https://drive.google.com/uc?export=view&id=1Syvj3tiV0Ify1LocU0_WbAaMgbS-zfbj",
            "https://drive.google.com/uc?export=view&id=12QaAByzynw6Ypldj6Vr09W_e1oX8xRQW",
            "https://drive.google.com/uc?export=view&id=1yMPPAoBc73_E1sqJtKVBr2nByChgHbab",
            "https://drive.google.com/uc?export=view&id=10Ry3gAfbHgGUn6MKy3rsJRcXyxqC6E8a",
        ]
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "123450104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Main Game dan Travel",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Bang Fabio keren dan bikin kagum dengan kemampuan beliaw",
                "Pesan" : "Sukses selalu bang Fabio dan semoga apa yang dicita-citakan bisa terwujud satu per satu"
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Menonton",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Kak Tanty orangnya lucu bangett, #T for Kak Tanty",
                "Pesan" : "Semangat terus kak Tanty dalam menjalani hari"
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Main Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Bang Fadil orangnya baik banget ga pelit ilmu dan suka sharing-sharing the best lah pokoknya ",
                "Pesan" : "Terima kasihh bang Fadil atas ilmu yang telah diberikan"
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Gitar",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Bang Nuell orang nya cerdas, baik, dan punya kapabilitas luar biasa muantab",
                "Pesan" : "semangat selalu abangdaa"
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "@Violaadrtr_",
                "Kesan" : "Orangnya keren banget, baik, murah senyum",
                "Pesan" : "Sehat dan semangat selalu kak Vio"
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "@risarmdna",
                "Kesan" : "Kak Risaa, orangnya baik banget, keren, murah senyum juga dan banyak ngebantu selama proses magang di psd",
                "Pesan" : "Terima kasih banyak kak Risa mohon maaf kalo belum bisa ngasih hal yang maksimal selama magang di psd ini"
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Jatimulyo",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Kak vani orangnya ramah dan suka sharing mengenai pengalaman-pengalaman yang telah dilalui",
                "Pesan" : "Tetap semangat kak Vani dalam menjalani perkuliahannya"
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "124450119",
                "Asal" : "Jambi",
                "Alamat" : "Sabah Balau",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@krnylee",
                "Kesan" : "Orangnya baik banget dan humble.",
                "Pesan" : "Semoga kak Yule selalu diberikan kesehatan dan semangat terus untuk menjalani perkuliahannya"
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM" : "12345001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Abangnya keren banget gokill",
                "Pesan" : "Semangat terus bang semoga segala urusannya dapat dipermudah oleh Tuhan"
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "@_els.a",
                "Kesan" : "Kakaknya murah senyum, baik dan humble",
                "Pesan" : "Semoga kak Elsa selalu diberikan kesehatan dan semangatnya harus dijaga"
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Makan",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Kakanya keren, baik, dan murah senyum",
                "Pesan" : "Semangat terus kak Fadya semoga segala keinginannya dapat tercapai"
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kak Lovi keren bangett melihat dan mendengar pengalamannya saat mengikuti pkm saya jadi sedikit termotivasi",
                "Pesan" : "Semangat terus kak Lovi, semoga segala urusannya dapat dipermudah"
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Gedung Harapan",
                "Hobi": "Main Game",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Bang Alsi ni keren bangett Gokillll!!",
                "Pesan" : "Sehat selalu bang Alsi dan semangat selalu"
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Kak Sherena orangnya murah senyum, baik, dan humble",
                "Pesan" : "Semangat dan sehat selalu buat Kak Sheren"
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Pertama kali liat bang Razin kirain Pak Tirta mirip banget soalnya wkwkw",
                "Pesan" : "Semangat selalu bang Razin dan semoga selalu lancar dalam mengerjakan tugas akhirnya"
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "@faizaanjani",
                "Kesan" : "Kakaknya lucu, baik dan murah senyum",
                "Pesan" : "Semangat terus kak Faiza dalam menjalani perkuliahannya"
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Abangnya keren banget gokilll mana gokil!!",
                "Pesan" : "Semangat terus bang Gathfan semoga selalu dilancarkan dalam segala urusannya"
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Orangnya humble banget, baik, keren terbaiklah pokoknya dan suka bercanda abangnya",
                "Pesan" : "Ayo bang ajakin saya sama Fadil buat turnamen epep"
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Bang Kaleb keren banget, melihat dari pengalaman-pengalamannya saya menjadi termotivasi",
                "Pesan" : "Semangat terus buat bang Kaleb dan semangat untuk selalu mencetak prestasi"
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Orangnya murah senyum dan baik",
                "Pesan" : "Semangat terus kak Melvaaa"
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "124450099",
                "Asal" : "Lampung Utara",
                "Alamat" : "Asrama",
                "Hobi": "Membaca",
                "Umur" : "20",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Orangya keren banget apalagi pas jadi MC di pplk th 2025",
                "Pesan" : "Semangat selalu bang Syafiq semoga selalu dilancarkan dalam segala urusan"
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Nongkrong",
                "Umur" : "28",
                "Sosmed" : "@henryferdianto",
                "Kesan" : "Tau bang Henry dari pplk karena abangnya dapet OZT Award keren banget, kemarin termotivasi juga buat dapetin penghargaan itu tapi gagal hehehe",
                "Pesan" : "Teruslah menjadi abang yang kerenn"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U5-4DhMQ1YDpT12-G4noTbDmCG0ABfid",
            "https://drive.google.com/uc?export=view&id=1xNz8wJnDtR57sxgt1oY24TYP85Oj29fF",
            "https://drive.google.com/uc?export=view&id=16XuEjuXGneSSkbAB1xeApnQVihmwJHA5",
            "https://drive.google.com/uc?export=view&id=1h-7z6FKN36Dj1_xW9wD9DWEF_hnis2eh",
            "https://drive.google.com/uc?export=view&id=1Rnl1kb7TiSJyKBjJynwFeAEm7CwT5Qqv",
            "https://drive.google.com/uc?export=view&id=13Otio40lZ7U0GrT3wt8a8EuNshrKK-5K",
            "https://drive.google.com/uc?export=view&id=1E4GXFkECfCkWvm0lltSYs9a0DdKTay3C",
            "https://drive.google.com/uc?export=view&id=1jhwzBurn2mRP_kWD5owNrohv84FjJdrf",
            "https://drive.google.com/uc?export=view&id=1kdwLxMssuWt42qDyQVaW_RQYU5lzgw_S",
            "https://drive.google.com/uc?export=view&id=1c3nNKbmqecgJB93g3pjsv7gkjjQyUgTs",
            "https://drive.google.com/uc?export=view&id=1gXeA93pt6BYuYhZNwThRn7TI-3Pqy6bN",
            "https://drive.google.com/uc?export=view&id=1PzMXmnV1y2FMNwuBM4vyBQu4XIL3Ylt9",
            "https://drive.google.com/uc?export=view&id=1OrBwE1HWPGELsF38yU2t5zjkncdmdQOm",
            "https://drive.google.com/uc?export=view&id=1QPFzqkF9KjGHSy4Hg8XVn3g6oUPwItxA",
            "https://drive.google.com/uc?export=view&id=15anWQsfSIOB6lBUwM7pTbvZMgqk28ETp",
            "https://drive.google.com/uc?export=view&id=1Ml_kv1ykJzYhCrZbibWBmb6fTf8F6OUe",
            "https://drive.google.com/uc?export=view&id=1oyqS5cw_vU_9WBO15-7etbOOGLdCxfae",
            "https://drive.google.com/uc?export=view&id=1lZfit_A85bJGc78g61mUZ2kzILwXSPrE",
            "https://drive.google.com/uc?export=view&id=1n2egtU3OUCTn3nrgan_D3mQmpY-p1AVr",
            "https://drive.google.com/uc?export=view&id=10NKF9wCduTHC1uj1btWv-ZL6rRkPehNC",
            "https://drive.google.com/uc?export=view&id=1DQP0Q5v6lbgt1xnGx8Fu99SVVGKmGJjX",
            "https://drive.google.com/uc?export=view&id=1xh50OuMGjLPw4vzokm7o4KWe2O7xIC20",
        ]
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Kak Arini orangnya tegas dan baik banget",  
                "Pesan": "Semangat terus buat kak Arini dalam perkuliahan dan tugas akhirnya nanti"  # 1
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kakak nya baik banget karena pernah nutorin ALE buat kelas RC penjelasan kakanya mudah banget makannya ALE saya A hehehe",  
                "Pesan":"semangat terus kak Nabyla dan semangat selalu"# 1
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "123450021",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakaknya keren banget dan baik juga",  
                "Pesan":"Semangat selalu kak Khoirulll"# 1
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21 Tahun ini alhamdulillah",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Bang Ahmad keren banget sejak kapan sih beliau ga pernah keren dari pengalaman dan cerita nya membuat saya tercengang",  
                "Pesan":"Semangat terus buat bang Ahmad semoga keinginan yg diinginkan bisa segera tercapai"# 1
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "10",
                "Asal": "Ikut kadep",
                "Alamat": "Love Earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakaknya murah senyum dan baik ",  
                "Pesan":"Semangat terus buat kak Adinda dalam menjalani perkuliahannya"# 1  
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat-lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Bang Bimo menggokil abisss kerennn ",  
                "Pesan":"Semoga bang Bimo selalu diberikan kesehatan jasmani dan rohani"# 1
            }, 
            { 
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "nelson piquet",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Bang Alfaya orangnya baik dan humble",  
                "Pesan":"Semangat dan sehat selalu buat bang Alfaya"# 1
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kak Asri orangnya murah senyum dan baik hati",  
                "Pesan":"Semangat terus kak Asri tetaplah menjadi orang kerenn"# 1
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Bang Bima orangnya humble dan baik ",  
                "Pesan":"Semoga apa yang diimpikan oleh bang Bima bisa tercapai"# 1
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakak nya gampang senyum dan baik",  
                "Pesan":"Semangat terus kuliahnya kak Indah "# 1
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kak Riska baik banget banyak banget ngebantu waktu Praktikum Alpro kemarin",  
                "Pesan":"semangat dan sukses selalu kak"# 1
            },  
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "20",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kak Yolanda juga orangnya murah senyum dan humble",  
                "Pesan":"Selalu dijaga semangatnya ya kakk"# 1
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga Kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "Waktu pertama kali ketemu pas saya pplk bang adit ngakunya anak mesin wkwk",  
                "Pesan":"Sehat selalu buat bang adit"# 1
            },            
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakaknya baik, humble, dan ramah",  
                "Pesan":"Semangat dalam menjalani perkuliahannya"# 1
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "25",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "Orangnya baik sesuai dengan hobinya",  
                "Pesan":"Tetaplah menjadi orang yang baik ya kakk"# 1
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh Pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Orangnya humble, baik, toppp pokoknya",  
                "Pesan":"Semoga dikelas tidak melakukan hobinya ya kak takut ditegur dosen"# 1
                
            }, 
            { 
                "Nama": "Danil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Bang Danil orangnya gokill dan humble",  
                "Pesan":"Info tempat jual ikan cupang terbaik"# 1
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "Bang Pian ini banyak membantu saya waktu praktikum alpro kemarin jadi Kesan saya ke abang ini baik ",  
                "Pesan":"Jangan lupa kalo belok kiri pake sen kiri ya bangg"# 1
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari Hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "Bang Yazid gokill dan humble sesuai dengan departemennya",  
                "Pesan":"Semoga hobinya cepat ditemukan"# 1
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "Masih muda lah",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@jaldii._",
                "Kesan": "MC pplk 2025 kemarin keren banget jadi saya memberi Kesannya kerennn",  
                "Pesan":"Kurang-kurangin makan makananan yang manis ya bangg biar ga kena diabetes"# 1
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "Kakaknya baik dan humble",  
                "Pesan":"Info nonton thinkerbell"# 1
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "123450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kak selma keren banget hobinya traveling",  
                "Pesan":"Info wisata lampung terbaik"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nZM6DY46uUmhQEqUSqE24Fbh__5wM8wd",
            "https://drive.google.com/uc?export=view&id=1TGBE7Jn5Pt3TpIIbBHtnnSSUc8wI35oM",
            "https://drive.google.com/uc?export=view&id=17V3WkyQM7y4Op1CR404BdkVJn3weIBZ3",
            "https://drive.google.com/uc?export=view&id=1i_y49WoxpzdLCeH8Jxk94V6flqkn7tfv",
            "https://drive.google.com/uc?export=view&id=1QosLKRw7gGUUENEBRCXhRa8Bhg5xeyI2",
            "https://drive.google.com/uc?export=view&id=1_lf8AOUNHi3D6qrwBQbkRqba2HbrsfCa",
            "https://drive.google.com/uc?export=view&id=17RXMkQY_eIGhHmeBVwTSKXre54tGgzyY",
            "https://drive.google.com/uc?export=view&id=1Qow1fc5_6jdfpSF16uVsuGsHj_WA5APA",
            "https://drive.google.com/uc?export=view&id=1Hi_cBFPMGeFk43h2ceofAZbqXZ6aPjar",
            "https://drive.google.com/uc?export=view&id=1L1Ymf8S6pVNjEo5UZfaHQhQSTU8659zh",
            "https://drive.google.com/uc?export=view&id=1q5VCRiqWh4SYi9dDKRp0nYNCm0DgslfB",
            "https://drive.google.com/uc?export=view&id=15qLgJia3n98DXJFqFp6tmH1OzgJn1nOI",
            "https://drive.google.com/uc?export=view&id=1BPVoclvvfWTD4fjnF4Z47r8SRJYWDk7o",
            "https://drive.google.com/uc?export=view&id=1aATPWI4NYWNHTiNe6O6dipi75C5mAgwc",
            "https://drive.google.com/uc?export=view&id=1DfPBf8U7gLo_yWb4QSPokMsYNXrqkHk5",
            "https://drive.google.com/uc?export=view&id=15u9MHTIdueZI7rD-DnhqrDzxmWI-4IVz",
        ]
        data_list = [
            {
                "Nama": "Haikal Fransiskus Simbolon",
                "NIM": "123450123",
                "Umur": "23",
                "Asal": "Bengkulu",
                "Alamat": "Belwis",
                "Hobi": "Ngoding",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Bang haikal enjoy banget orangnya dan gaull",  
                "Pesan":"Codinganku error bangg"# 1
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "untung suropat",
                "Hobi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kakaknya baik suka menolong orang",  
                "Pesan":"Tetap jadi orang yang baik ya kak"# 1
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobi": "menyapa satpam gedung f",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakaknya humble suka menyapa satpam ",  
                "Pesan":"Teruslah menyapa orang orang ya kakk"# 1
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "19",
                "Asal":"Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Olahraga Menembak",
                "Sosmed": "@farhanghani",
                "Kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "Pesan":"Info lapangan tembak terdekat"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Samping Kuburan Belwis",
                "Hobi": "Suka Eksperimen",
                "Sosmed": "@aisyahkhair",
                "Kesan": "kakaknya keren banget suka bereksperimen",  
                "Pesan":"Bakal eksperimen apa lagi nih kak"# 1
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "19",
                "Asal":"Medan",
                "Alamat": "Pesisir Belwis",
                "Hobi": "Begadang",
                "Sosmed": "@cerine.ipynb",
                "Kesan": "Kakaknya baik banget dan humble",  
                "Pesan":"Begadangnya dikurangin ya kakk"# 1
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "19",
                "Asal":"kisaran city",
                "Alamat": "Pemda city",
                "Hobi": "Buat lagu",
                "Sosmed": "@jay_saputra_tmb",
                "Kesan": "Bang Jaya berwibawa banget waktu wwc kerennn",  
                "Pesan":"Kapan nih bang lagunya rilis di spotify"
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Belwis",
                "Hobi": "main ML",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Pasti kakaknya jago main Mobile legend",  
                "Pesan":"Semoga cepat IMO"# 1
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "18",
                "Asal":"lampung selatan",
                "Alamat": "korpri raya",
                "Hobi": "isengin harvin di kelas",
                "Sosmed": "@rozakramdani__",
                "Kesan": "Jahil sesuai smaa hobinya",  
                "Pesan":"Semoga bang Harvin ga ngambek"# 1
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal":"riau",
                "Alamat": "belwis",
                "Hobi": "jadi asprak",
                "Sosmed": "@christiani8872",
                "Kesan": "Karena kakak hobinya jadi asprak jadi saya simpulkan Kesan ke kakak itu keren",  
                "Pesan":"Tutor jadi asprak kak"# 1
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal":"Padang",
                "Alamat": "Perumnas Way Kandis",
                "Hobi": "Ngikutin drama tiktok",
                "Sosmed": "@hndfzky_",
                "Kesan": "Gokill sih bang hanif jawabannya mudah dimengerti saat wwc",  
                "Pesan":"Drama yang lagi hot sekarang apa bangg"# 1
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal":"sumbar",
                "Alamat": "sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Tampilannya seperti chef profesional",  
                "Pesan":"Semoga skill masaknya berkembang seperti chef Renata"# 1
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Dina ngomong bahasa minang",
                "Sosmed": "@Cikamrbn",
                "Kesan": "Karena hobinya lucu Kesannya juga lucu",  
                "Pesan":"Semoga kakak selalu betah dengerin kak Dina ngomong pake bahasa minang"# 1
            },
            {
                "Nama": "Gustin H. Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Kak Gustin orangnya cinephile banget",  
                "Pesan":"Rekomendasi film yang bagus"# 1
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Berkuda",
                "Sosmed": "@Muhvnz_",
                "Kesan": "Mirip Ezra",  
                "Pesan":"Yang sabar ya bang kalo dijailin sama bang Rozak"# 1
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "natar",
                "Alamat": "natar",
                "Hobi": "nitip makan sama Aqila",
                "Sosmed": "@snasha._",
                "Kesan": "Kakaknya baik banget dan humble",  
                "Pesan":"Semoga kak Aqila nitipin makananannya lebih"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VXMooslLY5QE2nBf2WQwOr5fw_uRpw-X",
            "https://drive.google.com/uc?export=view&id=1CVSG3ah2UyyPb8RPQHsYxtGeihHTfq5_",
            "https://drive.google.com/uc?export=view&id=1IqJC8v2UCADPBrPmyCeOogm7ZiBBx_oS",
            "https://drive.google.com/uc?export=view&id=1NCW8SfQnfE1KD8o9G3-oucwLOqdTqQqr",
            "https://drive.google.com/uc?export=view&id=1O_G7m-ZYSmpdZ-9ebdDn9wMUFuXa4bOQ",
            "https://drive.google.com/uc?export=view&id=1zWSMHRtBhKmrUmYB9iHbW0xvuWHspCAz",
            "https://drive.google.com/uc?export=view&id=1hImiEgJ_IiyMSpBfuoz3uxjngko8a4xY",
            "https://drive.google.com/uc?export=view&id=1hpABQVcO40hhLyC_zhKcSKfvBhQv7cne",
            "https://drive.google.com/uc?export=view&id=116MOZHTufQvguy5tiNaA81ROnaNMLbLf",
            "https://drive.google.com/uc?export=view&id=1gs0hRsRBginfVw8gu9FMg7kyOdVGdCl3",
            "https://drive.google.com/uc?export=view&id=1-l3-5wgudpCOW3_pFJRu8OLqNslAaZ8I",
            "https://drive.google.com/uc?export=view&id=1qSwAq_iKydbXlPf56AgwyVD4oJeAvMXv",
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21 Tahun",
                "Asal":"Sumbar",
                "Alamat": "Belwis",
                "Hobi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Bang Ihsan ini wawasannya luas banget jadi Kesannya keren",  
                "Pesan":"Mau juga dong ditraktir sama bang Ihsan"# 1
            },
            {
                "Nama": "Hanifah Inaya Sari",
                "NIM": "123450123",
                "Umur": "21",
                "Asal":"Balam",
                "Alamat": "Balam",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya keren jago masak",  
                "Pesan":"semangat terus kuliahnya kakak dan tingkatkan terus skill memasaknya biar bisa nyaingin chef Renata !!!"# 1
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "19",
                "Asal":"Padang",
                "Alamat": "Hasan 4",
                "Hobi": "Nonton Marvel, Tidur",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakak keren suka nonton Marvel",  
                "Pesan":"Semoga kak Afifah tidak menjalankan hobinya di kelas yaa"# 1
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "NIM": "124450012",
                "Umur": "21",
                "Asal":"lampung",
                "Alamat": "Pemda",
                "Hobi": "Main game",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Abangnya gokill jago main game",  
                "Pesan":"Info mabar game FPS bangg"# 1
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "124450016",
                "Umur": "19 tahun",
                "Asal":"Semarang",
                "Alamat": "Balam",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya baik banget dan murah senyum",  
                "Pesan":"Semoga kakaknya bisa liburan ke Korea yaa"# 1
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Natar",
                "Hobi": "Mancing",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya Jago dan Gokilll dalam hal mancing",  
                "Pesan":"Info Spot terbaik di sekitaran ITERA"# 1
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal":"Sumbar",
                "Alamat": "Kelengkeng 5",
                "Hobi": "Tidur",
                "Sosmed": "@talithaaajtine",
                "Kesan": "Kakak sangat antusias saat wwc kemarin gokill",  
                "Pesan":"semoga tidak melakukan hobinya saat di kelas"# 1
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal":"Palembang",
                "Alamat": "Wayhui",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknay keren bangett soalnya hobinya nyari duit",  
                "Pesan":"semangat terus kak buat nyari duitnya"# 1
            },
            {
                "Nama": "Abdillah Fikri Al pome",
                "NIM": "123450062",
                "Umur": "21",
                "Asal":"Sumsel",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest_",
                "Kesan": "Abangnya sangat terlihat bugar",  
                "Pesan":"Semangat terus bang dalam menjalani perkuliahannya"# 1
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal":"Sumbar",
                "Alamat": "Samping kost rafli",
                "Hobi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Abangnya keren sama kayak bang Iqbal",  
                "Pesan":"Semoga kalo mancing sama bang Iqbal bisa dapet ikan yang banyak"# 1
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal":"Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakak keren karena jago masak",  
                "Pesan":"Terus tingkatkan kakk skill memasaknya biar bisa kayak chef Renata"# 1
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Nargo Lestari",
                "Hobi": "Olahraga, Makan makanan manis",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakaknya keren suka olahraga karena menjaga kesehatan tubuh",  
                "Pesan":"Kurang-kurangin makan manisnya ya kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LMYHm5agT8vjCJPIJPPWUtQakSy_XYXU",
            "https://drive.google.com/uc?export=view&id=1F8ggVI3UVGsaGTPWvK2z2xI4KNh5io-p",
            "https://drive.google.com/uc?export=view&id=1fGOipCVp4ZDVUnD45HWuz_J95oRUqt1g",
            "https://drive.google.com/uc?export=view&id=1JQ4cJGUo8tjyNmtyzg-FAsoxYJhUUeYK",
            "https://drive.google.com/uc?export=view&id=13gnMamimJ-jVHFXjSC2Ee6kPAMsIts1h",
            "https://drive.google.com/uc?export=view&id=1RDfjBMq4iai13ChWSKdfkT-IlqUvywTl",
            "https://drive.google.com/uc?export=view&id=1HaVVKmlexe1-RksSKmZMINNCzPHIjWCD",
            "https://drive.google.com/uc?export=view&id=1W4E5NosBriq_xIFboK--G1a--6BlDazF",
            "https://drive.google.com/uc?export=view&id=1J_m1aOLwZMPaX3Y2GlklAu3uqhG-qS2y",
            "https://drive.google.com/uc?export=view&id=1SbOdPrphk47wNP22uof8EpBzX75skNRn",
            "https://drive.google.com/uc?export=view&id=1cyze3DIkEkGQNYEGO9OFIPvEyhe6SqBG",
            "https://drive.google.com/uc?export=view&id=1Bmj4_k1_ctAdhzCs5uLkXcz9UXvzXzLr",
            "https://drive.google.com/uc?export=view&id=1BSX4_6TeaNRgN2KJO0-d6Xm4pD26TdJt",
            "https://drive.google.com/uc?export=view&id=1TAqmLKfZBi7UcnbLqf9w8WtDRQGv1ddH",
            "https://drive.google.com/uc?export=view&id=18QPizjpndVMx1L1h8KP0Uh9BcM9ZcMuv",
            "https://drive.google.com/uc?export=view&id=1pNZK4jYxYaqs9P-820Pye19agaaJPR-7",
            "https://drive.google.com/uc?export=view&id=1LqFclna_uZ9ACrnT15ZUjbo18WvJGsbM",
            "https://drive.google.com/uc?export=view&id=1gPPXO9sOzrwxUnt7sneW1mv6e-SA2TG8"
        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM": "123450082",
                "Umur": "20",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Musingin TA",
                "Sosmed": "@naylAsalsabilaa._",
                "Kesan": "Kakaknya baik banget waktu ngejelasin mengenai Departemen Medkraf ",  
                "Pesan": "Semangat terus kak jangan sampe lupa makan karena mikirin TA"# 1
            },
            {
                "Nama": " Donna Maya Puspita",
                "NIM": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": " Berenang",
                "Sosmed": "@donNamaya.p",
                "Kesan": "Kakaknya baik banget apalagi pas ngejelasin materi LMD karena kakaknya Pentutor kelas RC",  
                "Pesan": "Semangat terus kakk maaf ya kalo RC banyak tingkahnya"# 1
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "NIM": "123450037",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": " Way Huwi",
                "Hobi": " Nonton Tong setan",
                "Sosmed": "@noerruuu",
                "Kesan": "Bang labo keren banget karena pas materi dirangkaian kemarin mudah untuk memahami isi dari materi tersebut",  
                "Pesan":"Semangat terus bang Labo semoga dipermudah saat mengerjakan TA"# 1
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton F1",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya keren banget hobinya nonton F1",  
                "Pesan": "Semoga kakaknya bisa nonton F1 secara langsung"# 1
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": " 124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mancing",
                "Sosmed": "@ felisyanbl__",
                "Kesan": "Kakaknya jago, baik dan keren",  
                "Pesan":"Info Spot gacor di belwis kakk"# 1
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "124450031",
                "Umur": "18",
                "Asal": "Rumah",
                "Alamat": "Ryacudu",
                "Hobi": " Bully Felisya Nabila Nugroho",
                "Sosmed": "@muh_razan_",
                "Kesan": "Jail sama kayak hobinya ",  
                "Pesan":"Jangan membully lagi ya bang"# 1
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Umur": "21",
                "Asal":"karawang",
                "Alamat": "Airan",
                "Hobi": "nongkrong depan ruang prodi",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Orangnya baik banget dan murah senyum",  
                "Pesan": "Semoga dilancarkan ya kak dalam mengerjakan TA nya"# 1
            },
            {
                "Nama": "Allisha",
                "NIM": "124450019",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukabumi",
                "Hobi": "Gebuk Snare",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Kakak keren banget apalagi pas damaskus",  
                "Pesan":"Semangat terus kak Allisha"# 1
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Kakaknya lucu, murah senyum",  
                "Pesan": "Hati hati ya kak kalo jalan jalan pake sepatu roda takut jatuh"# 1
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobi": "Belajar",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kak Bunga pintar sesuai dengan hobinya",  
                "Pesan":"Pertahankan hobi belajarnya ya kakk"# 1
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM": "123450041",
                "Umur": "20",
                "Asal":"Terbanggi Besar",
                "Alamat": "Airan Raya 1",
                "Hobi": "menulis, membaca",
                "Sosmed": "@n1tg._",
                "Kesan": "Kakak keren sudah terlihat dari hobinya",  
                "Pesan": "Pertahankan ya kak untuk hobinyaaa"# 1
            },
            {
                "Nama": "Nazlah Aulia",
                "NIM": "124450054",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Memanah",
                "Sosmed": "@nzlhauly",
                "Kesan": "Wih kakaknya keren banget hobinya aja memanah",  
                "Pesan":"Semangat terus kak semoga selalu diberikan kelancaran"# 1
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": " 124450043",
                "Umur": "Gada yang tau",
                "Asal": "Rumah bapak ",
                "Alamat": "Gedung F",
                "Hobi": "Ngitungin beras di karung",
                "Sosmed": "@difanyhsa_",
                "Kesan": "Kakaknya sabar banget pasti karena suka ngitung beras di karung ",  
                "Pesan": "Info ngitung beras bareng kakk"# 1
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Umur": "21",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobi": "nyuluh manuk",
                "Sosmed": "@daffascript_",
                "Kesan": "Keren hobinya nyari burung",  
                "Pesan":"Semoga dapet burung yang Rare bangg"# 1
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Scroll fesnuk",
                "Sosmed": "@edsel_0712",
                "Kesan": "Kakaknya lucu sudah terlihat dari hobinya scroll fesnuk",  
                "Pesan": "Info yang lagi hot di fesnuk kakk"# 1
            },
            {
                "Nama": " Lucia Advencia Rachel Nainggolan",
                "NIM": " 124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": " Mencintai Andrew Garfield",
                "Sosmed": "@ luciarachel_",
                "Kesan": "Kakaknya baik hati sudah terlihat dari hobinya yaitu mencintai",  
                "Pesan": "Semoga cintanya bisa diterimaa ya Kakk"# 1
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "Kakanya Pinter jago ngoding",  
                "Pesan": "Info line error ada di line keberapa kak"# 1
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "124450112",
                "Umur": "19",
                "Asal": "Jabung",
                "Alamat": "Rajabasa",
                "Hobi": "bobo",
                "Sosmed": "@Xifasky",
                "Kesan": "Kakaknya baik dan keren banget",  
                "Pesan":"Semoga hobinya tidak dilakukan saat di kelas"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=186-9rxTIYENao-aVOUKCRF2RqS104Yj6",
            "https://drive.google.com/uc?export=view&id=1i6tD9A7_flVQVEf6sLx-jUjMB6FdKEEX",
            "https://drive.google.com/uc?export=view&id=1UrqMKXhGoZZ8kRdwbXehsaWKd52auIbG",
            "https://drive.google.com/uc?export=view&id=1PBmjwLq66UzlvcYfkwAS7ATeVnWgjS9X",
            "https://drive.google.com/uc?export=view&id=12PjLbff4Zn1Ha0P0396ogEH7zpq11Hpl",
            "https://drive.google.com/uc?export=view&id=1jTQ1G-3uNH8X-p_GygYyxFQauHjeKVFf",
            "https://drive.google.com/uc?export=view&id=1ZiHQmCpK1aGExNm6qa8iibBA4szoLL-9",
            "https://drive.google.com/uc?export=view&id=1gyBus5LXcUqXnvbvd__XFr4RnwZxvHK2",
            "https://drive.google.com/uc?export=view&id=1YPqR0zshfW1VA6nrAa4UFlAJ_O28ushP",
            "https://drive.google.com/uc?export=view&id=1OSx-Rm7oDs0mUDgIxOw9ZqipoHgF2b1W",
            "https://drive.google.com/uc?export=view&id=1YVL8ywMbsiWPkASoYzOaKbl-eLuleLnb",
            "https://drive.google.com/uc?export=view&id=1nJ-OPM-X119oh9W-GkFGVEixhQUNeurN",
            "https://drive.google.com/uc?export=view&id=1Yy64vhdTxEXIg0xKaklfbHs7pHtbFwA5",
            "https://drive.google.com/uc?export=view&id=1mRJGkX35zHqizAgdPVho0oFz7_HOLnUp",
            "https://drive.google.com/uc?export=view&id=1D-1oSk-Ps0RWz0qoFyfVmKGPPi7I57Ww"
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "NIM": "123450109",
                "Umur": "23",
                "Asal": "Sulawesi Tengah",
                "Alamat": "Panjang",
                "Hobi": "Mancing",
                "Sosmed": "@kevinaja__",
                "Kesan": "Bang Kevin keren banget pas wwc pemaparannya mudah dipahami",
                "Pesan": "Semangat terus bang Kevin semoga selalu dilancarkan urusannya"
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM": "123450046",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Way Dadi",
                "Hobi": "Mendaki",
                "Sosmed": "@ferazkaa",
                "Kesan": "Kakaknya keren banget dan murah senyum",
                "Pesan": "Semangat terus kak semoga yang diimpikan bisa tercapai"
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "NIM": "123450088",
                "Umur": "21",
                "Asal": "Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "Gokill abangnya suka nonton F1",
                "Pesan": "Semnangat terus bang semoga apa yang diupayakan dapat tercapai!"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM": "124450058",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Airan",
                "Hobi": "Belajar + menghitung uang",
                "Sosmed": "@aayuandriani_",
                "Kesan": "Kakaknya keren sudah terlihat dari hobinya",
                "Pesan": "Semangat terus kak semoga semuanya dapat berjalan dengan lancar"
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM": "124450131",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Way Kandis",
                "Hobi": "Jogging",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Abangnya bugar mungkin karena sering jogging",
                "Pesan": "Sehat selalu buat bang Dafa"
            },
            {
                "Nama": "Juwita Sari",
                "NIM": "124450066",
                "Umur": "19",
                "Asal": "Lampung Barat",
                "Alamat": "Pemda",
                "Hobi": "Mancing",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Kakaknya keren dan sabar karena hobinya mancing",
                "Pesan": "Semangat terus kak dan sehat selalu"
            },
            {
                "Nama": "Muhammad Afdal Luthfi",
                "NIM": "124450047",
                "Umur": "19",
                "Asal": "Lampung Tengah",
                "Alamat": "Jl. Pulau Damar",
                "Hobi": "Memantau dl tugas",
                "Sosmed": "@afdall.03",
                "Kesan": "Abangnya fokus banget terlihat dari hobinya memantau dl tugas",
                "Pesan": "Semangat terus bang dalam memantau dl tugas"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM": "124450002",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobi": "Nongkrong di kopken",
                "Sosmed": "@slbnzw_",
                "Kesan": "Kakaknya asik suka nongkrong",
                "Pesan": "Semangat terus kakk untuk perkuliahannya"
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM": "123450091",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Belwis",
                "Hobi": "Badminton",
                "Sosmed": "@mridwaan_22",
                "Kesan": "Bang Ridwa gokil dan keren",
                "Pesan": "Sehat selalu bang Ridwan dan semangat terus"
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM": "124450060",
                "Umur": "18",
                "Asal": "Sumatera Selatan",
                "Alamat": "Kotabaru",
                "Hobi": "Main rubik",
                "Sosmed": "@andra.lhm",
                "Kesan": "Keren dan jago main rubik",
                "Pesan": "Semangat terus buat bang Andra"
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM": "124450003",
                "Umur": "20",
                "Asal": "Nias",
                "Alamat": "Belwis",
                "Hobi": "Live tiktok",
                "Sosmed": "@bryantel_",
                "Kesan": "Abangnya gaul suka live tiktok",
                "Pesan": "Semangat terus bang dan semoga live nya makin rame"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM": "124450067",
                "Umur": "17",
                "Asal": "Surabaya",
                "Alamat": "Kemiling",
                "Hobi": "Nanem Sawit",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Kesannya wow suka nanem sawit soalnya",
                "Pesan": "Semoga sawitnya subur ya kak"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM": "124450055",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobi": "Bengong",
                "Sosmed": "@indahjuliaa",
                "Kesan": "Kakaknya suka bengong",
                "Pesan": "Jangan keseringan bengog ya kak"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM": "124450023",
                "Umur": "18",
                "Asal": "Kalimantan Barat",
                "Alamat": "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Sosmed": "@cacalvra",
                "Kesan": "kakaknya keren banget dan aktif",
                "Pesan": "Semangat terus ya kak dan semoga apa yang dimau bisa dimaukan"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM": "124450089",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Kotabaru",
                "Hobi": "Bangun pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "morning person abis bang rafka ini",
                "Pesan": "semoga bangun pagi terus bang biar solat subuh terus, jadi kepengen hobinya saya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

# Tambahkan menu lainnya sesuai kebutuhan
