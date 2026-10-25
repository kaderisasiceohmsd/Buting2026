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
        nama = clean(data.get("nama"), "Tanpa Nama")
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

        umur = clean(data.get("umur"))
        umur_text = f"{umur} Tahun" if umur.isdigit() else umur
        sosmed = clean(data.get("Sosmed"))
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
            "https://drive.google.com/uc?export=view&id=1erwcdW2OSk2EHluafxh7g_sq0Rh9jnPo",
            "https://drive.google.com/uc?export=view&id=1KYhvRbnMIO0S2S4FSm5lvo5qEaFoc23Z",
            "https://drive.google.com/uc?export=view&id=17er9A0OVeDNNyJCFLd7xrBklWmnzGi5T",
            "https://drive.google.com/uc?export=view&id=1EJrwajIoDoLCzc0sOAYtv1qGDaZIHzH4",
            "https://drive.google.com/uc?export=view&id=1BcFZFrEuzuTjZ6V0xtOspubiKB-8XY7s",
            "https://drive.google.com/uc?export=view&id=1A3Zo9AZjmoIjguZqVU5-nMUrjPTzUrro",
            
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Bang Ginda berwibawa sekali,nampak banget aura sibuk nya.",  
                "pesan":"Semangat nge TA sambil mengkepalai Himpunan bg."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil juga ga kalah keren! Btw,aku mulet terinspirasi dari bg aqil.",  
                "pesan":"semangat terus kuliah nya bg,tetap jadi orang keren!!!"# 2
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik banget meski jarang ketemu, tapi kakaknya selalu ramah dan welcome banget",  
                "pesan":"Semangat terus kuliah nya kak!"# 3
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois orangnya humble banget, ramah.Nampaknya si sedikit pendiam hehe",  
                "pesan":"Semangat Nge TA nya ka!"# 4
            },
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya baik banget dan humble, ramah juga,lihat kakanya seperti melihat uang",  
                "pesan":"Semangat terus kuliah nya kak!"# 5
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya baik,pokoknya keren banget deh, ramah juga",  
                "pesan":"Semangat kuliah dan menjaga uangnya ka heheh"# 6
            },                      
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xX5xZzfgo0YDPwwbrSFrKi7lgwQ-kVdv",
            "https://drive.google.com/uc?export=view&id=1UEY6eUBmefJnUdzEjQxLi0IfDgssihvW",
            "https://drive.google.com/uc?export=view&id=1gNBesG19vBN49uRG74sQxz-nJIs_2Nw_",
            "https://drive.google.com/uc?export=view&id=1kNQ86zfTja8MzETJjXG4OmcXAJoISPvk",
            "https://drive.google.com/uc?export=view&id=1D6Hb2IVfecYJ_rOLMZtnQWJs7Klocg4E",
            "https://drive.google.com/uc?export=view&id=1AJzdcl_Xw1anSBzkBjUew6wIRzyMiwpA",
            "https://drive.google.com/uc?export=view&id=1NMMz0q0yNyR9L231OIzcTtqQuuxKv7DX",
            "https://drive.google.com/uc?export=view&id=19_9PyVwtj51UW1ymFD2vr39hu5o7JXhy",
            "https://drive.google.com/uc?export=view&id=11oFbrtdVUOQkH4vJkCP89U7xLPYr8ux2",
            "https://drive.google.com/uc?export=view&id=1A3Zo9AZjmoIjguZqVU5-nMUrjPTzUrro",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya cantik, baik, kalem, keren,wanita paling berwibawa yang pernah aku temui",
                "pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Tanya Bapas",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Abangnya seru, asik, lucu,dan sudah pernah satu divisi di natal Sains Data",
                "pesan": "Semangat terus bang Helmy,semoga makin jago Gitarannya"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya baik, asik, dan king nya badminton di Data",
                "pesan": "Semoga selalu dimudahkan bang Fernando,kapan kapan sparing ya bang"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya asik,sudah pernah jadi partner mc di sains data mengabdi",
                "pesan": "Sehat selalu ya kak,terima kasih ilmu mc nyaa kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya asik, keren, pinter juga pastinya,dan abang ini kasra lantaiku dulu.",
                "pesan": "Sehat selalu bang, semangat terus menjaga asrama bg"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia,h_264",
                "kesan": "Kakaknya lucu,ramah,asik,dan cantik banget wkwk",
                "pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak mentor aku.Kalau Messi itu pemain bola terbaik,kalau ka Aqila ini mentor terbaik sepanjang masa. Kakak ini baik banget,dan asik banget pastinya.",
                "pesan": "Semoga segala hal berjalan baik untuk kakak,semoga kakak selalu sehat dan bahagia,semoga kuliahnya lancar kak,semoga semakin bersinar seperti bunga matahari kakak,dan jangan lupa sama dodol-dodol kakak ini yaa ka,we love you ka."
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren, mulet nya menawan banget, dan asik juga pastinya",
                "pesan": "Semoga sukses selalu bang,semoga aku next tuplak scienfest"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya cantik, ramah, baik hati pula",
                "pesan": "Semangat terus kak, semoga kuliahnya lancar dan cepat lulus"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca Buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya keren, humble, dan asik banget.",
                "pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_iPcLG7nq0NQxMILOrG9J1O8RTB1hfft",
            "https://drive.google.com/uc?export=view&id=18cXKrXhO_wKD-3xjp2OIe3GIdgeFk1MQ",
            "https://drive.google.com/uc?export=view&id=134yZZFcwQmIdUx985QuEeYWDopslWUaC",
            "https://drive.google.com/uc?export=view&id=1q-ne5XjrI4e3VlVcIWBD3oDooBQoQ8H-",
            "https://drive.google.com/uc?export=view&id=1at8AOga0Jh9_vTDeiuKmbiedcT4_txbI",
            "https://drive.google.com/uc?export=view&id=1564Ps6ViL9QSKOjaAOg53z_38o6M_eKs",
            "https://drive.google.com/uc?export=view&id=1fYdwn3qmDYrwkoWDnlO08b5ljmnqtKF6",
            "https://drive.google.com/uc?export=view&id=1PquoD8A9Rz_UszUm5tbWM_Q3aTfdlO73",
            "https://drive.google.com/uc?export=view&id=1fkPiFGyy4CbEyUWXMWxKcjHtAdENmS7T",
            "https://drive.google.com/uc?export=view&id=1cQNoI6KdUxFqNDrDD6ByHZl0obbjrQg3",
            "https://drive.google.com/uc?export=view&id=1Dy5278ma_6FlXsF2oglR5pEeiPHbWtIm",
            "https://drive.google.com/uc?export=view&id=1G-9WncVzkXmhDTO0PHCiL-qQ0eCeh6Xm",
            "https://drive.google.com/uc?export=view&id=19AtJbFz5XshQH4p15O6Midzekb65WOUI",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kuala lumpur",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya asik banget dan paling kece lah, to the point dan penjelasan yang di kasih sangat mudah dipahami",  
                "pesan":"Semoga main futsal nya makin jago bg hahah"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnyaaa asik banget, lucuu,dan peduli banget orangnya.",  
                "pesan":"Semoga Kedepannya kak jue selalu diberi kelancaran dalam segala hal, dan juga selalu diberikan kesehatan, Terimakasih kak sudah jadi kaka asuh aku di TPB ka"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble,dan cantik.",  
                "pesan":"Semoga kuliah lancar ya kaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya asik banget,vibes belajar nyaituloh,bangga banget kenal sama bg dharu,Mapres,PKM,satu kerjaan lagi.",
                "pesan": "Semangat terus kuliahnya, Bang! Semoga tugas lancar, nilai aman, dan cepat lulus bg"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael orangnya humble dan asik, auranya presidiumnya kenceng banget.",
                "pesan": "Selamat atas terpilihnya sebagai Kabaleg ya bang"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya asik,outfit nya juga selalu keren",
                "pesan": "Semoga kuliahnya lancar,semoga cepat lulus ya bang"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal": "City Earth",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya asik dan ramah. keliatan soft spoken banget",  
                "pesan":"Semoga kedepannya kak hani selalu diberi kesehatan dan kelancaran dalam segala hal yaa kak ."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya seperti peniam,tapi suaranya gapernah gagal saat tampil",  
                "pesan":"Semoga semakin sering nyanyi di event event ya bang."# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona sebenarnya orangnya asik,meski sedikit galak saat saat itu hahah.",  
                "pesan":"semangat terus kuliahnya bang,selamat udah juara 1 Nasional bg, SUKSEEES !!!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica orangnya murah senyum, baik dan lucu,masih ingat waktu motor kakak nya mogok di asrama",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu,dan cepat lulus ya kak"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar orangnya baik banget, humble, dan tegas, tapi perhatian",  
                "pesan":"semangat terus kuliahnya kak,dan jangan galak galak haha"# 1
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakaknya baik dan seru,dan kakaknya wong palembang",
                "pesan": "Semoga kuliahnya lancar terus,info tutorial belajar bahasa palembang."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya seruuu asik dan humbleee banget.",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bfeoLdTPLcR84j0tNaTIqoQScIAn-5M3",
            "https://drive.google.com/uc?export=view&id=1MgV1KtBTwKLl5xlQdQyEA_YrUeYCPqd3",
            "https://drive.google.com/uc?export=view&id=1atakdZfVuFQkbAtu2immCu27wQiWa2f9",
            "https://drive.google.com/uc?export=view&id=1824Ysb1cab3IV7sruKTcHn5pa-sZywYN",
            "https://drive.google.com/uc?export=view&id=1WbKnDhWcWL39GyfmIzSCFfdQxnpm6r6j",
            "https://drive.google.com/uc?export=view&id=19DOs7BzUsgjhNp1gXFWdaGS97ESEeMWk",
            "https://drive.google.com/uc?export=view&id=1LzgnhSE97uGtMW3VjKdTGyhGpfx_mzMc",
            "https://drive.google.com/uc?export=view&id=1VrpVJsvnTq3LYi4ckm6OT7rxznPIoqSF",
            "https://drive.google.com/uc?export=view&id=13SfsKaXDnZipnQK9CBCrSpHWD_8RdgjU",
            "https://drive.google.com/uc?export=view&id=1f9QHeWyzKSCN9WgGpFQtkIWjbnAirdYD",
            "https://drive.google.com/uc?export=view&id=1_PngtFGyHyVKgwnEoNeuFsljMk0drPq4",
            "https://drive.google.com/uc?export=view&id=1AEO2eUsPD3vTiVh2AgRcLESynTJ62T5B",
            "https://drive.google.com/uc?export=view&id=10x1T3fQYlKnTg71xnh2z0ohgcA6Qex1Z",
            "https://drive.google.com/uc?export=view&id=19dwnIzMegc3Uh8mbOTa3CPzLug2LwXs1",
            "https://drive.google.com/uc?export=view&id=1St8VoUGESYZYqWElikgyDRDi33zjTuR2",
            "https://drive.google.com/uc?export=view&id=1cbG84MOmaMX4yVEtpN1K_itP0TnBzUAT",
            "https://drive.google.com/uc?export=view&id=1viKl2p9qwDDPJoINHVrJj1HB-83TGNn_",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta orangnya keren banget, profesional, dan juga cantik bangettt",  
                "pesan":"Semoga kuliah ka arienta lancar dan sukses ya kak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya juga profesional, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya."# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "1234500117",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orangnya tegas,dan keras, tapi juga baik dan sangat peduli.",  
                "pesan":"Semoga kuliah nya lancar bang,semoga kami adek didikmu bisa bersinar nantinya"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi orangnya kerenn, to the point dan sangat profesional.",  
                "pesan":"Semoga kuliahnya lancar bang,nilai nya A semua,Amin."
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake orangnyaa humble,profesional, kerenn, tegas dan baikk",  
                "pesan":"Semoga bang ayake dilancarkan kuliahnya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar orangnya galak, tegas,humble,dan profesional",  
                "pesan":"Semoga bang caesar diberi kesehatan dan kelancaran dan jangan galak galak lagi ya bang"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia orangnya seru, tegas , dan juga baikk,",  
                "pesan":"Semoga kak euodia selalu didekatkan hal-hal baikk,dan dilancarkan segala hal"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal orangnya kerenn, tegas ,baikk, dan juga ramahh",  
                "pesan":"Semoga kuliahnya lancar bang haikal,infokan marmitu sesekali bg"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "Oiya Cefa",
                "hobbi": "Jalan kaki gaboleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri orangnya profesional banget,dia galak sekaligus cantik",  
                "pesan":"Semoga kuliahnya lancar ya ka putri"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@quenntanaabilaa",
                "kesan": "Kak Queenta orangnya baik, humble, dan perhatian",  
                "pesan":"Semoga kak queenta sehat selalu dan dilancarkan segala hal"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk,dan sangat persuasif.Banyak orang bilang kami mirip.",  
                "pesan":"Semoga bang desman selalu diberkati Tuhan,dan semoga cepat lulus ya bang."# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
                "pesan":"Semoga kuliah ka Azzel selalu dilancarkan dan dimudahkan"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah,awalnya kakak ini kukira orang batak",  
                "pesan":"Semoga kak charlindah sehat selalu dan kuliahnya lancar"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya kerenn,ramah,dan ga nyangka kalau abang ini orang batak",  
                "pesan":"Semoga bang jeremi dilancarkan kuliahnya,dan terima kasih sudah rispek sama saya bang"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila sehat selalu dan kuliahnya lancar"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi orangnya seru, dan juga baik hati, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K-BWBGPPPaX3Oj6uyr3JKQuqzFzeyeJb",
            "https://drive.google.com/uc?export=view&id=1CU2bPjPbr_QMto1Fi9qM-Ii99TUJy0nb",
            "https://drive.google.com/uc?export=view&id=1piJ-EMgPPFY_qTlbzAzwdeV4Oc29u4lO",
            "https://drive.google.com/uc?export=view&id=1xQ4iu8VVktxap2ESyBsaDEXDb6vViERM",
            "https://drive.google.com/uc?export=view&id=1LMT3puy9pZR0auxHN8G6nm1w3S3GX2-N",
            "https://drive.google.com/uc?export=view&id=1VJiK9Rd4Irp7vDpavxWYI5TS_ZKCz3Eb",
            "https://drive.google.com/uc?export=view&id=1ReLlGv2VIiTlNt8F8VBm8VtbRxi1ftfC",
            "https://drive.google.com/uc?export=view&id=1UxlZ-MyAVjtIlwjpLJM0ehiugkaG9cwI",
            "https://drive.google.com/uc?export=view&id=1_5YrgGvHBhmxY2uRh4zSG1IjWZaaUJQe",
            "https://drive.google.com/uc?export=view&id=1oqDLqcZWo73Tg3eVpXWvzuJoRnfHZY1T",
            "https://drive.google.com/uc?export=view&id=10qUhDsA5q3ivgW-B2B1eg1vfPKZnsxKg",
            "https://drive.google.com/uc?export=view&id=10QjP2upeOtr40APRjPEOMy8nHiAe7JHP",
            "https://drive.google.com/uc?export=view&id=1H3XrhHc8VlwpmR4WrAmlefifblUsUUka",
            "https://drive.google.com/uc?export=view&id=1aLEdJRahrMGbrzCs4i-I4IcVkfdWm-KX",
            "https://drive.google.com/uc?export=view&id=17dwiMCh8nSMufTS36AKTz2p-JuBzIbsw",
            "https://drive.google.com/uc?export=view&id=1CnRAaty2SAD0HWb_VZE1R6vxknV-BACO",
            "https://drive.google.com/uc?export=view&id=1EgRDUQXT8fFYhlWYBJqYZFQBTuxY6isL",
            "https://drive.google.com/uc?export=view&id=1HGpd9n1-lhZ3z3TapAF_eg4KhydYVfV3",
            "https://drive.google.com/uc?export=view&id=1zxrAoSo7ijtdQHIhB-4hRddjej873QiP",
            "https://drive.google.com/uc?export=view&id=1VLjUzeo8rZCyEWhraMlBTyBoRjD-hXv0",
            "https://drive.google.com/uc?export=view&id=1roXyKLX_IgiA2q0Q6EH_oNhu0mfmPxgv",
            "https://drive.google.com/uc?export=view&id=1dRPhhJzyOsddkwe4GPklStCdciBi8zG9",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim" : "12340104",
                "asal" : "Bandar Lampung",
                "alamat" : "Kedaton",
                "hobbi": "Tidur",
                "umur" : "21",
                "sosmed" : "@biyokcb",
                "kesan" : "Abangnya keren,pintar,dan sangat asik",
                "pesan" : "Jangan ngejar saya bang hahah,perasaan ketemu mulu"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim" : "123450094",
                "asal" : "Lampung",
                "alamat" : "Airan Raya",
                "hobbi": "Membaca",
                "umur" : "21",
                "sosmed" : "@tvnty_",
                "kesan" : "Tenang dan sangat lucu,sampai mikfes punya gaya ka Tanty",
                "pesan" : "Semangat terus ka,semoga cepat lulus ya ka Tanty"
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampungku",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "Panutan saya,jago public speaking dalam bahasa ingris",
                "pesan" : "Semoga bang Fadil bahagia disana."
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa saja,dan selalu ramah",
                "pesan" : "Tetap semangat dan jangan berubah bg,Terima kasih atas ilmu-ilmu nyaa."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim" : "124450005",
                "asal" : "Bali",
                "alamat" : "Nusa Penida",
                "hobbi": "Menghayal",
                "umur" : "12",
                "sosmed" : "Violaadrtr_",
                "kesan" : "Meski jarang berinteraksi sepertinya kakaknya baih dan ramah",
                "pesan" : "Semoga kuliah nya lancar ya kaa,semoga aku juga bisa ke bali"
            },
            {
                "nama": "Risa Romadona",
                "nim" : "124450127",
                "asal" : "Natar",
                "alamat" : "Natar",
                "hobbi": "Rolling skate",
                "umur" : "20",
                "sosmed" : "risarmdna",
                "kesan" : "Orang nya baik hati dan ramah",
                "pesan" : "Semoga kuliah nya lancar dan nilai nya bagus semua"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan baik hati meski terlihat seperti pendiam.",
                "pesan" : "Semangat kuliahnya ka,semoga kakak sehat selalu ."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "124450119",
                "asal" : "Jambi",
                "alamat" : "Sabah Balau",
                "hobbi": "Belajar",
                "umur" : "20",
                "sosmed" : "@krnylee",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim" : "123450119",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "umur" : "21",
                "sosmed" : "@keyashafi",
                "kesan" : "bg akeyla ramah,sopan dan baik hat.",
                "pesan" : "Tetap semangat bang,semoga cepat lulus"
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum,baik hati,dan sangat aktif di kepanitiaan",
                "pesan" : "Tetap jadi kakak yang aktif ka,dan jangan lupa membimbing kami untuk acara-acara berikutnya"
            },
            {
                "nama": "Fadya Izzatul Aini",
                "nim" : "124450062",
                "asal" : "Pringsewu",
                "alamat" : "Airan",
                "hobbi": "Mancing",
                "umur" : "20",
                "sosmed" : "fadyaizzatul_",
                "kesan" : "Kaka ini baik hati dan ramah sekali,juga murah tersenyum",               
                "pesan" : "Tetap jadi orang ramah ya kaaa"
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kakak ini juga panutan aku,karena dia selalu aktif di kegiatan kegiatan kepanitiaan",
                "pesan" : "Lancar terus kuliah nya ya kaa,semoga kakak sehat selalu"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim" : "124450092",
                "asal" : "Kalianda",
                "alamat" : "Kotabaru",
                "hobbi": "Main Game, Tidur",
                "umur" : "20",
                "sosmed" : "@aluccy_",
                "kesan" : "Abang ini jarang ketemu,tapi abangnya baik kok",
                "pesan" : "Semoga kuliah nya lancar selalu ya bang"
            },
            {
                "nama": "Sherena Florencia",
                "nim" : "124450027",
                "asal" : "Bengkulu Selatan",
                "alamat" : "Belwis",
                "hobbi": "Make up",
                "umur" : "19",
                "sosmed" : "sher_renna",
                "kesan" : "Kakak ini juga keren banget, udh ambil 24 sks full pulak jadi asdos",
                "pesan" : "Semangat kuliah padatnya ka,semoga hasilnya yang terbaik"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim" : "123450096",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Futsal",
                "umur" : "21",
                "sosmed" : "@razyn.hfd",
                "kesan" : "Abangnya keren, orangnya humble ke orang orang",
                "pesan" : "Semangat bang menempuh semester akhirnya."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim" : "124450075",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Membaca Novel",
                "umur" : "19",
                "sosmed" : "FAIZAANJANII",
                "kesan" : "Kakak orangnya terbuka, murah senyum",
                "pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim" : "124450001",
                "asal" : "Bandar Lampung",
                "alamat" : "Rajabasa",
                "hobbi": "Main game",
                "umur" : "20",
                "sosmed" : "@gathfannadif",
                "kesan" : "Abangnya santai tapi tetap bertanggung jawab pada tugasnya.",
                "pesan" : "Terus jaga semangat dan konsistenya bang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim" : "124450064",
                "asal" : "Metro",
                "alamat" : "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "umur" : "20",
                "sosmed" : "@apiszzaja_",
                "kesan" : "Abangnya seru diajak ngobrol dan tidak pelit informasi",
                "pesan" : "Tetap menjadi abang yang selalu terbuka untuk semua orang."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Beh ini mah udah setara bodybuilder nya mikfes",
                "pesan" : "Bang, tolong berikan set workoutnya bang, dan semangat mengejar MLOpsnya bang"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim" : "124450087",
                "asal" : "Sumsel",
                "alamat" : "Sukarame",
                "hobbi": "Scroll",
                "umur" : "19",
                "sosmed" : "@melva_fbrt",
                "kesan" : "Kakak ini baik dan murah hati",
                "pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Kota Bumi",
                "alamat" : "Asrama",
                "hobbi": "belum tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "Ku kira abang ini serius banget, tapi ternyata orangnya lawak banget",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()


if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12XoIWTrEbd78PVO_pkh2rlQRTN4rqZcJ",
            "https://drive.google.com/uc?export=view&id=1PhtBOSKo0HKx7JJbGuN9R-2oK_tFdCeG",
            "https://drive.google.com/uc?export=view&id=1P3FvUBN8egEX8d76DOhLVriHr7cxnl9O",
            "https://drive.google.com/uc?export=view&id=1hlqv8VSh93vfr7iPzmbQvCU_sMcANXWo",
            "https://drive.google.com/uc?export=view&id=1XIseKqKErK63WTfboQGiOWFUFAiptZfJ",
            "https://drive.google.com/uc?export=view&id=1AYtjOHCGXWeBjwhfbKlVN2BPxAn8qyGW",
            "https://drive.google.com/uc?export=view&id=1g8kyjJp11lSFKJXYPAfQe5q_mYxFuAje",
            "https://drive.google.com/uc?export=view&id=148IPzn8eGkxLF_mK0A0hE0L2CcVvRA5K",
            "https://drive.google.com/uc?export=view&id=1TuJrqmU2-TNDJS-IRHBqtZjeEkPR9676",
            "https://drive.google.com/uc?export=view&id=113Q-WHA0W5yRasDc3-EYDE94aIyoKy4X",
            "https://drive.google.com/uc?export=view&id=1fbo7jnYKU09E5oq30C9ofTV33czs9IMN",
            "https://drive.google.com/uc?export=view&id=1n2IjM653m0LO2J-dMV77MJ6wuS-D5OaB",
            "https://drive.google.com/uc?export=view&id=1Y4brYTTmY88XHVxHZKbOLCOv1hMfXElJ",
            "https://drive.google.com/uc?export=view&id=1BlUmSUdX8pEKsEtQXxaG-YiIPVsm4E7W",
            "https://drive.google.com/uc?export=view&id=1-F0Toruv7FwRnNDXJAuTlOZluLSTpVzV",
            "https://drive.google.com/uc?export=view&id=1Em42LwmmqsdJA0iHISJQQ2PxrpxFCqh1",
            "https://drive.google.com/uc?export=view&id=1ETzfcISbFZHQgjJnrg-EtgDUSL5zeifT",
            "https://drive.google.com/uc?export=view&id=1KzLg-U13HBMlHCJ83vnBJBqZYVpdlUUO",
            "https://drive.google.com/uc?export=view&id=13pgw3qDKKOXy094EHCmMu75f1GsOeuS_",
            "https://drive.google.com/uc?export=view&id=1BGSdirqm4KH5z6lsd7J1yUOuaZNi-ovj",
            "https://drive.google.com/uc?export=view&id=1rpni-yakf3atLMDlConsaANhaL15ftQm",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik dan selalu optimis",  
                "pesan": "semangat terus kak untuk semester akhirnya" 
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak orangnya selalu bahagia dan tidak patah semangat",  
                "pesan":"Semangat kak, aku percaya kakak bisa"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main...",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Orangnya disiplin dan tetap selalu semangat ",  
                "pesan": "Goodluck bang, abang pasti bisa menyelesaikan studi ini dan mendapatkan gelar S.Sid"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21 Tahun",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abang ini sangat berani untuk menyuarakan aspirasinya untuk kebaikan bersama",  
                "pesan": "Konsistenlah terus bang, kami butuh orang seperti abang untuk berani menyuarakan aspirasinya "
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya terbuka dan sangat informan ",  
                "pesan": "Semangat kak menjalani tugas di divisinya, dan tetap konsisten pada akademiknya"  
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abang ini tinggi dan keinginan taunya sangat tinggi",  
                "pesan": "Semangat terus abang tiang listrik, semoga habit abang terus konsisten ada hingga semester akhir"
            }, 
            { 
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Wew sangat paham benar dengan histori dunia per F1-an",  
                "pesan": "Semoga performa akademik abang bisa kayak performa driver F1"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak Asri orangnya baik banget dan informan kepada adek adeknya",  
                "pesan": "Semangat terus kak, jangan lupa dengan usahanya juga"
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abang orangnya baik dan humoris seperti hobinya",  
                "pesan": "Lanjutkan terus bang untuk menyebarkan kehumorisan abang ke orang orangnya"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakak ini kok bisa mancing kecebong, kok keren",  
                "pesan": "Semangat kak mancing kecebongnya, ajarin aku dong"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Nge follow up chat itu mulia kak, pasti kakak sering dibutuhin sama orang orang",  
                "pesan": "Kak saran ku buka jasa nge follow up chat, kayaknya bakal untung"
            },  
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Senyum terus kakak ini dalam kondisi apapun, walaupun marah kakak ini, masih tetap senyum",  
                "pesan": "Aku minta tolog untuk konisten terus senyumnya ya kak, karena itu mencairkan suasana"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang, abang yang dulu sempat nyamar jadi maba kan bang waktu jadi verbek? hayooo",  
                "pesan": "Semangat terus bang kuliahnya, nanti akt 2027 abang nyamar jadi maba baru lagi ya bang"
            },            
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini murah hati dan mudah senyum",  
                "pesan": "Semangat terus ya kak, semuanya pasti berlalu jika dijalani"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak ini sangat mulia dengan hobinya dan dampaknya ke semua orang",  
                "pesan": "Hobi kakak semoga selalu kosnisten menjadi orang baik"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakak ini tidurnya cukup teru dan begadang di jadwalnya pasti tidak ada",  
                "pesan": "Semoga kakak hobinya tidur terus, tapi jangan lupa dengan akademiknya juga ya kak:)"
                
            }, 
            { 
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abangnya ternyata pernah berantemin ikan cupang dengan ikan cupang yang lainnya (keren)",  
                "pesan": "Semoga pelet abang buat pakan ikan cupangnya terus banyak dan tidak telat ngasih makan ikan cupangnya (hait hati gerd ikan cupangnya bang)"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Euuhhh abang ini orangnya gak pernah ngesen kiri (kayaknya)",  
                "pesan": "Semoga abang pergi kemana mana tujuannya selalu disebelah kanan, kalau misalnya tujuannya dikiri, lawan arah aja ya bang (semoga selamat sentosa)"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari Hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Abang ini selalu optimis dengan keadaan apa aja",  
                "pesan": "Semoga abang dapat menemukan hobi abang yang keren (coba hobinya ngasih makan ayam bang, kalau ngasih makan ikan cupang, udah di ambil sama abang Danil)"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Sangat ramah dengan orang orang dan adik adiknya",  
                "pesan": "Semoga abang selalu optimis untuk kedepannya"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak ini orangnya sangat suka dengan disney loh yeah",  
                "pesan": "Semoga kakak dapat bertemu dengan disney princessnya yeah"            
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakak orangnya keinginan taunya sangat tinggi",  
                "pesan": "Semoga kakak rasa penasarannya konsisten ada hingga mendapatkan gelar S.Sid-nya"
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UDW1zfCEo3QeE90YpY9_XwSyytOstH7_",
            "https://drive.google.com/uc?export=view&id=1U5oqjgWhSPrXXy7zzDeAuc-Y6KKjtUNW",
            "https://drive.google.com/uc?export=view&id=1JLYzOdoNs9wsyomEyAFoZveQFQJ4kAE1",
            "https://drive.google.com/uc?export=view&id=1ixgB4z8bmQVfc3-R_16gbUGpGqtmo8q0",
            "https://drive.google.com/uc?export=view&id=15En31ghDdk6wESP8t-7HwUVjoKyw9ee_",
            "https://drive.google.com/uc?export=view&id=1YDFyH46GQRZiDKAtzi5hZN0hRQ3myW3k",
            "https://drive.google.com/uc?export=view&id=1Br6mpshKHlmg6lJIgxDj5pLy3rY7P0Ub",
            "https://drive.google.com/uc?export=view&id=1VOy94Y_KM5PnXT7ijv-OliQcYUwCWoLO",
            "https://drive.google.com/uc?export=view&id=1Fy4T8QEQjb3_-X_kRAOXqEp1ZZ6bCWB1",
            "https://drive.google.com/uc?export=view&id=1R7N3shNrPVCj0IN773Qbefha2U8aREaI",
            "https://drive.google.com/uc?export=view&id=1iDVzuBn8oZPxBJK2GkTwzvSg-BHMxDSv",
            "https://drive.google.com/uc?export=view&id=1_jM8LMhzRZD-3Mp_wxytd52Y7UzdHVB-",
            "https://drive.google.com/uc?export=view&id=1OWz0XtiMBUv5gu10ca2rLmRbixqSfQ7o",
            "https://drive.google.com/uc?export=view&id=1sBVcmh-ZVV1JSKVUHxscaVmd3C7zH7wu",
            "https://drive.google.com/uc?export=view&id=1k9hH3BEjMw74VFScqh61MLvP4wOFKE9l",
            "https://drive.google.com/uc?export=view&id=1wjLddHAoU9gR4t_yO7vcZHdHwY7-ga63",
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450123",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang haikal orangnya seruu banget.",  
                "pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru, baikk, lucu ",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "@cerine.ipynb",
                "kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "MainML",
                "sosmed": "@njlanursyifat",
                "kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
                "pesan":"Semoga semua keinginan kak najla tercapi secepatnya"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"lampung selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
                "pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"riau",
                "alamat": "belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
                "pesan":"Semoga bang hanif selalu menjadi yang terbaik"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"sumbar",
                "alamat": "sukarame",
                "hobbi": "main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
                "pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
                "pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak gustin selalu didekat hal-hal baik"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
                "pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasha._",
                "kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KtXyg2KyvsXBErR8Sf7BVwK5cWzEt8jp",
            "https://drive.google.com/uc?export=view&id=1o0lfXsNPNhEDaIY-zRcWpJPoX5doD8-X",
            "https://drive.google.com/uc?export=view&id=1jFpeb4u-lwAPbMlYU8Y3dIz9Afbedo0x",
            "https://drive.google.com/uc?export=view&id=1knOClFLdzto3Kyy1rhxtkhNFLKU6H1Hu",
            "https://drive.google.com/uc?export=view&id=1NlEj5wMWmHiVCaKqRag1DKx0Z6Bgq6Xq",
            "https://drive.google.com/uc?export=view&id=1jTFXyGOLCFG90e6PX_pMHlN61ti8k8iI",
            "https://drive.google.com/uc?export=view&id=1NlEj5wMWmHiVCaKqRag1DKx0Z6Bgq6Xq",
            "https://drive.google.com/uc?export=view&id=1ps1rcyrZDI9a1_RVD0rfpdE_KNoywiYs",
            "https://drive.google.com/uc?export=view&id=12hymD1uz4sqjEYdti3r5I0Y93jDuWyhu",
            "https://drive.google.com/uc?export=view&id=1YX9SYNSd71vVROf9cyM-bwuEHWkRMQ7D",
            "https://drive.google.com/uc?export=view&id=1KsV_F9C7u_7SRdZyGEO80JEqJZMqWtji", 
            "https://drive.google.com/uc?export=view&id=19BZmt6qEEE3N9orRTsQA1USNyDJJO9lT",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abang ini informan dan penuh dengan pengetahuan umum",  
                "pesan": "Semoga abang juga nanti traktir saya ya bang, dan semoga nular hobinya abang :)"
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini pemurah hati dan baik bangettt",  
                "pesan": "Pesan sushi mentai satu kak (becanda ya kak), semoga kakak konsisten terus sampe bisa buka cabang kopdes"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini orangnya luar biasa aktif dan informan bangett", 
                "pesan": "Goodluck terus ya kak, btw Iron Man jadi Doctor Doom kak"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal": "lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Abang ini orangnya ngomong selalu berdasarkan fakta asli dan sering berbagi informasi",  
                "pesan": "Semangat bang main gamenya dan jangan lupa akademiknya juga yeah"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini orangnya baik dan luar biasa optimis",  
                "pesan": "(kakak suka lee min ho gak?) semoga kakak konsisten terus dengan hobinya dan semangat dengan akademiknya" 
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Orangnya gacor banget dan baik hati",  
                "pesan": "Semoga abang dapat mengejar gelar S.Sid-nya"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Orangnya selalu segar dan hidupnya sehat",  
                "pesan": "Semoga kakak dapat tidur walaupun deadline sudah mepet"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak orangnya penuh dengan critical thinking dalam problem solving",  
                "pesan": "Semoga kakak selalu mempunyai konsep pemikiran yang dapat menjadi pintu cuan"
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Abang orangnya sangat fit dan manajemennya waktunya bagus",  
                "pesan": "Semoga abang selalu konsisten dengan jadwal sehari hari abang dan dapat mencapai gelar S.Sid"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Abang ini orangnya selalu sabar dan sangat tau momentum",  
                "pesan": "Semoga abang mendapatkan Arapaima di Embung E dan selalu sabar dalam kondisi apapun"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini orangnya penuh dengan komitmen dan tanggungjawab atas pekerjaan",  
                "pesan": "Semoga kakak dapat memberikan dampak yang baik ke orang orang sekitar"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini 4 sehat 5 sempurna dan selalu happy",  
                "pesan": "Semoga kakak sering melakukan olahraganya dan kurangi dikit untuk makan manisnya yeah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oMTwLxqIaWp_qrsBQR7cuWOl3MxwHNsi",
            "https://drive.google.com/uc?export=view&id=1sCNOmxnzLu16WRYUa5O-sO1lQr_nPPaw",
            "https://drive.google.com/uc?export=view&id=1_eJU59tzPHesQruuX3fxhl-GHXFRiIMc",
            "https://drive.google.com/uc?export=view&id=1r9oKQSjElSCtAtCF7vSF_P1EypzO05yu",
            "https://drive.google.com/uc?export=view&id=1wCusvCcjKDn0psiMoOxMjNk4m_rjQJcX",
            "https://drive.google.com/uc?export=view&id=1pYR_q4aUT6P0xYKPTqavsa2VBbTeJk7t",
            "https://drive.google.com/uc?export=view&id=1BtV6cXvp1O0g7D5DFGWQoYF_9cdEob__",
            "https://drive.google.com/uc?export=view&id=1xK4r721fkFc3pMCOV73t4j1xvrnWgBzN",
            "https://drive.google.com/uc?export=view&id=1sC-lJ9aU-cZ_T1OkmESFPLncUw-cwdXe",
            "https://drive.google.com/uc?export=view&id=1Y_TAKrLxtbbLms9wiU_NEMAAKXn9u1UE",
            "https://drive.google.com/uc?export=view&id=19pzp1O5fwZZ_WUBUCOO_4q7oVQ_oYP5b",
            "https://drive.google.com/uc?export=view&id=1RowqUGSBgzg0iPUplifS9L_fD0wCdOkC",
            "https://drive.google.com/uc?export=view&id=1rnfrZTZ7kbM1DhP1vlhNUysI-lpROSPm",
            "https://drive.google.com/uc?export=view&id=1cPl-oAZhP3A9qku27R8WRmdWGHQgAlqP",
            "https://drive.google.com/uc?export=view&id=1qzmuhkBit2hGfB9jorIV_RX8OspXXkHT",
            "https://drive.google.com/uc?export=view&id=1hFKAKMr2UMqxi7T43ZSNAQolUlIkZpN1",
            "https://drive.google.com/uc?export=view&id=1oRpcrPdbLTL7n8z_B2dhD5S-1IjSGFDi",
            "https://drive.google.com/uc?export=view&id=1IUhTebMSmdEkzAtEAzC0HV3ngj--hwzm",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylAsalsabilaa._",
                "kesan": "Kakak orangnya bisa manajemen waktu dengan baik",  
                "pesan": "Semoga kakak tahun depan dapat gelar S.Sid nya yeah"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donNamaya.p",
                "kesan": "Kakak orangnya selalu kuat dan tegar jika dihadpkan masalah",  
                "pesan": "Semoga kakak selalu sering berenang dan dapat menyelesaikannya TA-nya"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Abang ini suka tantangan dan berani untuk menghadapi apa yang akan datang",  
                "pesan": "Semoga abang dapat gelar S.Sidnya tahun depan dan jangan lupa trek trekan tong setan (jujur saran saya di Embung E enak loh bang)"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak orangnya baik hati dan optimis bangett",  
                "pesan": "Viva Kimi Antonelli, semoga kakak performa akademiknya sama kayak Lando Norris tahun kemarin"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakak ini orangnya baik banget dan sabar",  
                "pesan": "Request mancing biawak di Embung E kak hehehe, semoga kakak sabar untuk kedepannya terus "
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Abang ini orangnya sangat aktif mengganggu orang",  
                "pesan": "Semangat terus bang bully orangnya, goodluck untuk akademiknya bang"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal": "karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini sangat ambis untuk mengejar tanggungjawabnya",  
                "pesan": "Semoga kakak dapat dipermudah dalam bimbingan dan TAnya hingga mendapatkan gelar S.Sidnya"
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakak ini sangat aktif dan baik",  
                "pesan": "Semoga kakak konsisten dengan hobi kakak (jangan gebuk meja juga yeah kak)"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakak ini sangat optimis dan luar biasa baik",  
                "pesan": "Semoga kakak selalu seimbang dengan hobi dan akademiknya yeah"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini super ambis dan dapat membagi waktu dengan baik",  
                "pesan": "Semoga kakak konsisten dengan apa yang kakak lakukan"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini informan dan baik banget",  
                "pesan": "Semoga kakak selalu konsisten dengan hobi kakak"
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakak ini sangat teliti orangnya",  
                "pesan": "Semoga kakak tingkat akurasinya sangat tinggi dan sesuai dengan akurasi tingkat akademiknya "
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak ini orangnya komitmen dengan tanggungjawabnya",  
                "pesan": "Semoga kakak orangnya selalu komitmen dalam tanggungjawab kedepannya"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Kakak orangnya eksploratif dan keinginan tahunya tinggi",  
                "pesan": "Semoga kakak orangnya selalu konsisten dengan hobinya (unik yeah kak)"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Abang ini orangnya baik hati dan ramah terhadap semua orang",  
                "pesan": "Semoga abangb selalu di rangkul dengan orang orang baik"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakak ini sangat baik dan informan",  
                "pesan": "Semoga kakak sehat selalu"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakak orangnya tingkat problem solvingnya bagus banget",  
                "pesan": "Semoga kakak dihindari dengan bug bug aneh pada codingannya"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakak ini orangnya selalu segar dan optimis dalam menjalani sehari harinya",  
                "pesan": "Semoga tidak ketiduran di kelas dan selalu tidur 8 jam"
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

if menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15W17dEyb-v1hSFaYlv5Dv_P-wFGGBF9g",
            "https://drive.google.com/uc?export=view&id=1RHpw7ryMsOMwMopyqqQvzgeENaEag3O0",
            "https://drive.google.com/uc?export=view&id=1ja9fNTnss5ZJxaVvp_6fD_OXLhoErB4b",
            "https://drive.google.com/uc?export=view&id=1f4m1abuyDW7hiY-_cN6tG16Ezp0jq1W7",
            "https://drive.google.com/uc?export=view&id=1YgJLjn1PUQDQHItLyk_mIYe4otVubnUv",
            "https://drive.google.com/uc?export=view&id=1ZKHTy-U119e1EzoR669g4d17XyI6Y2Y9",
            "https://drive.google.com/uc?export=view&id=1b-0b-63w6qIKUsibm_I1wPBQ9FS8kDEz",
            "https://drive.google.com/uc?export=view&id=1-4MYdUhnuEdzP-4Pbg0i5c86O2ih-QUi",
            "https://drive.google.com/uc?export=view&id=1d0qHI5JivsZSDXPyO-7Kh5C4V60hAhRm",
            "https://drive.google.com/uc?export=view&id=1fBDO2ke1DU23EJ-UeHPZia9bNGaQrkPw",
            "https://drive.google.com/uc?export=view&id=1-jGOT72fb07ubgOPueI6h2_1mAtPIDGd",
            "https://drive.google.com/uc?export=view&id=1r0o81bVM41kJSW9oyaPTBHVOnCFESNlk",
            "https://drive.google.com/uc?export=view&id=1LaGOlqx7aNOqwr8w9O34vElmZklyrX08",
            "https://drive.google.com/uc?export=view&id=1KmwR97fsP9gARlDQAT5A_k7UcUhQD74u",
            "https://drive.google.com/uc?export=view&id=1YyE9zNqBr_7Av3ULgg7nqJx7B9_qZvyL",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "23",
                "asal": "Sulawesi Tengah",
                "alamat": "Panjang",
                "hobbi": "Mancing",
                "sosmed": "@kevinaja__",
                "kesan": "Sangat menginspirasi dan memimpin dengan baik",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
                "pesan": "Sukses selalu kak!"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Keren dan selalu memberikan arahan yang jelas",
                "pesan": "Semangat menjalankan tugasnya kak!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar + menghitung uang",
                "sosmed": "@aayuandriani_",
                "kesan": "Sangat ramah dan aktif berkontribusi",
                "pesan": "Tetap semangat dan sukses terus!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Jogging",
                "sosmed": "@dafaelpriza_",
                "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
                "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Mancing",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Sangat baik dan murah senyum",
                "pesan": "Semangat terus kuliahnya!"
            },
            {
                "nama": "Muhammad Afdal Luthfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Memantau dl tugas",
                "sosmed": "@afdall.03",
                "kesan": "Sangat bertanggung jawab dan fokus",
                "pesan": "Semangat terus kakak!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Sangat asik dan ceria",
                "pesan": "Tetap semangat kuliahnya ya kak!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Sangat mengayomi dan membimbing dengan sabar",
                "pesan": "Semangat terus memimpin divisinya kak!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "Sangat kreatif dan pintar",
                "pesan": "Sukses selalu kuliahnya!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Sangat menghibur dan ramah",
                "pesan": "Semangat terus berkarya kak!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Sangat unik dan bersemangat",
                "pesan": "Tetap semangat dan sukses selalu!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Sangat baik dan bersahabat",
                "pesan": "Sukses terus perkuliahannya kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Sangat ceria dan menyenangkan",
                "pesan": "Semangat terus ya kak!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Sangat disiplin dan dapat diandalkan",
                "pesan": "Sukses selalu buat perkuliahannya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

# Tambahkan menu lainnya sesuai kebutuhan


    




# Tambahkan menu lainnya sesuai kebutuhan


    




# Tambahkan menu lainnya sesuai kebutuhan
