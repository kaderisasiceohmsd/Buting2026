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

        card_html = _flatten_html(f"""
        <div class='profile-card'>
            <div class='photo-pane'>
                <div class='card-index'>{i + 1:02d}</div>
                {photo}
            </div>
            <div class='info-pane'>
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

# BAGIAN DATA ASLI MILIK AQILA CHIKA AURELIA
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xScs4doDOIethYbxNoWkU73CSdSFkWBB",
            "https://drive.google.com/uc?export=view&id=10EkDtDlWgtyDqGRTliitMHehOxdtAgP8",
            "https://drive.google.com/uc?export=view&id=1u-RH8Z2VgH0lz9DV42JSGxccA6rPLK7i",
            "https://drive.google.com/uc?export=view&id=176-ojVw5_L75IuyN1JnuunTsYRQESerh",
            "https://drive.google.com/uc?export=view&id=1r5v5UOSP7Au0lafHHG000oQgL8NzrPmL",
            "https://drive.google.com/uc?export=view&id=1hv50uvcjIaz-icXOrL1NFRJXmzNYvb9k",
                        
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobi": "Push imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Bang Ginda keren banget, time manageementnya bagus keren",  
                "Pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobi": "Dzikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil orangnya baik banget, humble, dan ramah",  
                "Pesan":"semoga lancar kuliahnya bang!"# 2
            },
            {
                "Nama": "Efi Defiyati",
                "NIM": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "eeffiidefi",
                "Kesan": "Kakaknya baik banget",  
                "Pesan":"Semangat terus kak semoga lancar kuliahnya"# 3
            },
            {
                "Nama": "Qois olifio",
                "NIM": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kotabaru",
                "Hobi": "mainin surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Bang qois keren banget bisa jadi bagian dari sekjen dan ramah juga orangnya",  
                "Pesan":"semoga kuliahnya lancar dan sukses selalu"# 4
            },
            {
                "Nama": "Luthfia Laila Rahmadhani",
                "NIM": "123450004",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Airan",
                "Hobi": "keliling balam",
                "Sosmed": "@luthhifiarmdhni",
                "Kesan": "Kak luthfia ramah dan baik banget",  
                "Pesan":"semoga sehat selalu dan semangat terus"# 5
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "NIM": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "bertemu luluk",
                "Sosmed": "@hafsafazilahh",
                "Kesan": "kakaknya cantik banget dan baik juga",  
                "Pesan":"semoga urusan perkuliahannya lancar ya kak!"# 6
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wTVxoZAa2x2mKBg4jKil6LgMiz7_EQPj",
            "https://drive.google.com/uc?export=view&id=1894RdrHf6BwKBaOK_snVZOg_TMnuyNIo",
            "https://drive.google.com/uc?export=view&id=1Y0M_7iDNln0fwZKw67wINLcMfyuwpl3K",
            "https://drive.google.com/uc?export=view&id=1wKXY17t0-Zwm_ey3sEyutu6Ku5DD3Y9I",
            "https://drive.google.com/uc?export=view&id=193TDvbH2b5YhiR5A8x2Cqlm3Ixmvp7kb",
            "https://drive.google.com/uc?export=view&id=1F8OLkIFCfTrclWdMJrpJcWl796wyjCcV",
            "https://drive.google.com/uc?export=view&id=1axefxDg3NqoxW_vn9i-GMUtLEzs-N073",
            "https://drive.google.com/uc?export=view&id=1o7zNPdnVjdo7Arg1_19mHOjrqWUWy96Y",
            "https://drive.google.com/uc?export=view&id=1R9u-TmwW9l9qHEc8MbhAcdfSGoIrmJVE",
            "https://drive.google.com/uc?export=view&id=1_MoH0s5-UhiylH867SNSR56PnFLo8axZ",
            "https://drive.google.com/uc?export=view&id=11-TwKo2hQ7T6insZbO-fmBVHAdpmch_E",
            "https://drive.google.com/uc?export=view&id=1JrE8Vj6p08HGSWUs8D-sEoBjchMTh-_r", 
            "https://drive.google.com/uc?export=view&id=1E91EEOSBsAhpkn61Heu_hJa52rig89UJ",
        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "GH",
                "Hobi": "Wawancara",
                "Sosmed": "@iamridhomanik",
                "Kesan": "abang ini asik kalo pas jadi asprak ramah",
                "Pesan": "semangat terus kuliahnya bang"  # 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Singkawang",
                "Alamat": "Pelangi",
                "Hobi": "Dengerin lagu Duhai Sayang",
                "Sosmed": "@j__eesia",
                "Kesan": "Kakak ini humble dan extrovert banget",
                "Pesan": "semangat terus kuliahnya semoga lancar"  # 2
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "12450015",
                "Umur": "18",
                "Asal": "Banten",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi Kartu Boboiboy",
                "Sosmed": "@syt.rifah",
                "Kesan": "Keren banget suka koleksi kartu boboiboy dan humble banget",
                "Pesan": "semoga koleksi kartu nya makin lengkap"  # 3
            },
            {
                "Nama": "Wan Naswa",
                "NIM": "123450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "KotaBaru",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshayka",
                "Kesan": "baik, cantik dan keliatan nya pendiem",
                "Pesan": "semangat terus kuliahnya kakk"  # 4
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "23",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@ddharu_",
                "Kesan": "abang ini keren banget sering liat di ig",
                "Pesan": "semangat terus bang kuliahnya semoga lancar"  # 5
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung Barat",
                "Alamat": "Sukabumi",
                "Hobi": "Ngopi",
                "Sosmed": "@givarooo",
                "Kesan": "baik dan ramah juga",
                "Pesan": "semoga sehat selalu dan sukses dalam kuliahnya"  # 6
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "12450101",
                "Umur": "20",
                "Asal": "Cibaduyut",
                "Alamat": "Teluk",
                "Hobi": "Makan Pedes",
                "Sosmed": "@jeremia_hm",
                "Kesan": "sering liat pas materi rangkaian dan baik juga",
                "Pesan": "semoga lancar selalu kuliahnya bang"  # 7
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Gym dan Koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "abang ini asik, baik dan ga ketebak orangnya",
                "Pesan": "semangat terus kuliahnya bang!"  # 8
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "14450082",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "pemda"   ,
                "Hobi": "Nginep di kos putri",
                "Sosmed": "@sekardnwp",
                "Kesan": "keliatan nya galak padahal aslinya baik banget dan seru juga",
                "Pesan": "semangat terus kuliahnya kakak !!!"  # 9
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "Kota Bumi",
                "Alamat": "pemda"   ,
                "Hobi": "Nginep di kos putri",
                "Sosmed": "@haniquratuain_",
                "Kesan": "cantik, baik dan ramah banget orangnya",
                "Pesan": "semoga sehat selalu dan lancar kuliahnya kak"  # 10
            }, 
            {
                "Nama": "Gh Mikael Niko Antonio",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Jabung",
                "Alamat": "Jati Agung",
                "Hobi": "COD Musang",
                "Sosmed": "@me._kael",
                "Kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "Pesan": "semangat terus kuliahnya bang!"  # 11
            }, 
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Kota Baru",
                "Hobi": "tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "Pesan": "semangat terus kuliahnya kakakkk"  # 12
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "zkrui",
                "Alamat": "Jatimulyo",
                "Hobi": "memancing",
                "Sosmed": "@afghanisnt_",
                "Kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "Pesan": "semangat terus kuliahnya kak"  # 13
            },                                                              
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18pFYiodYEd07IVviRGEycd-sjtKcNZax",
            "https://drive.google.com/uc?export=view&id=1Ie_cEMbITvBG28KC_fRR9ThBdU_RffXk",
            "https://drive.google.com/uc?export=view&id=1_urTTbpuJ2DLbq9Ym0QkgPwsky69ppL6",
            "https://drive.google.com/uc?export=view&id=1DtJVvMDe6lhO6fSfjzO-uZ6l-RnLeLAD",
            "https://drive.google.com/uc?export=view&id=1Hg9KrexMpQn47sve2xjNq2ywFtRkIN5A",
            "https://drive.google.com/uc?export=view&id=1MZqDfR7xVN0YAym_hzi7M5kf5m89ZYVB",
            "https://drive.google.com/uc?export=view&id=1Wm2zk-qe_eB1e6Zve6oeTdTAh79pj37u",
            "https://drive.google.com/uc?export=view&id=1GJCr6kglIzwOPI9M0oDiges27azaa0VK",
            "https://drive.google.com/uc?export=view&id=1YfVGoB_Y0IKAl6_IXTUl1EBsnIh9uAnB",
            "https://drive.google.com/uc?export=view&id=1on0ASNNX75WvntdQcdgbXWnIVm_97Kl5",
                      
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal":"Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "kakaknya soft spoken, humble, dan baik banget",  
                "Pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Danger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "kak nadya keren, cantik, dan baik jugaa",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal":"Jakarta",
                "Alamat": "Belwis",
                "Hobi": "nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Kakaknya baik banget dan ramah!",  
                "Pesan":"Semangat terus kak!"# 3
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftnii",
                "Kesan": "Kakaknya baik banget",  
                "Pesan":"Semangat terus kak!"# 4
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal":"Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Semangat terus kak!"# 5
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "kk ini baik banget dan aku melihat ada bintang bintang bersinar di mata kk nya masyaAllah ternyata nama kita samaan masyaAllah happy banget nama aku samaan kaya bidadari. Okay serius ya ini kesan nya, agak kaget waktu pengumuman kelompok mentor aku namanya sama kaya aku wkwk lucu banget jadinya kalo dipanggil dua duanya nengok!! long story short selama kurang lebih 5bulan ini amaze banget sama mentorku yang bener bener perhatian ke mentee nya bahkan sampe aku sendiri berani ceritain masalah pribadi aku karena aku tau kak aqila would be good listener, hari itu aku nangis baca chat dari kamu huhu gemes banget dan aku sangat berterimakasih untuk itu kak it means a lot <3",  
                "Pesan":"untuk semua kebaikan yang kamu lakukan semoga berbalik ke kamu ya kak, aku percaya kamu akan selalu dikelilingi hal baik karena kamu such a good person too, gada kata yang bisa aku ucapin selain banyak berterimakasih sama kamu kak, jangan lupa tetap ceria ya kak cause it suits you well!, loveyouuu sm kakkk"# 6
            },                      
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal":"Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "abangnya humble dan seruuu!",  
                "Pesan":"Semangat terus bang"# 7
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "abangnya baik hati",  
                "Pesan":"Semangat terus bang kuliahnya"# 8
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Kedamaian",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "abangnya baik banget!!",  
                "Pesan":"Semangat terus bang"# 9
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "19",
                "Asal":"Tangerang kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "seru, baik dan humble",  
                "Pesan":"semoga lancar kuliahnya bang"# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m97ka3OYag0V_l8csSv2nlfy66ANWFA2",
            "https://drive.google.com/uc?export=view&id=1B3Sf_Ca_iIgPsGE3bBgmkJqw15tQDM-9",
            "https://drive.google.com/uc?export=view&id=1F1mtjj-N63X-porO2lmB3bExI-bCiHfd",
            "https://drive.google.com/uc?export=view&id=1192G1ajQX8Zx4jaOb-Oi3ZWNKSSdNoAI",
            "https://drive.google.com/uc?export=view&id=1iCzkFhAlMglLgkDS5Qmv1sjNZI1Mv1xZ",
            "https://drive.google.com/uc?export=view&id=1cZsxSxAOPBxShCwEfEQLRkSjHfgIleoa",
            "https://drive.google.com/uc?export=view&id=1kUeGLor0It8tAWFw-iVQWN_EgJuvczp6", 
            "https://drive.google.com/uc?export=view&id=1Zq9WbcvuwUrSQqCtUVw1PTlpzvqO9xov",
            "https://drive.google.com/uc?export=view&id=1jc3fcTFkqZggyPN7cMRSUT6x5byGNzey",
            "https://drive.google.com/uc?export=view&id=1X3RFx8-SY5WtssTjo8WBpEUNJrNL2fB0",
            "https://drive.google.com/uc?export=view&id=1tywX8Nlb1C3fIpeEvPKWEUEh0j3VE4UE", 
            "https://drive.google.com/uc?export=view&id=1BoqV-W6coa_fMUYdpp966c6i3uy8M3TE",
            "https://drive.google.com/uc?export=view&id=1z3icSgP3TOwtqFRSIiSL-sXime4ts_x7",
            "https://drive.google.com/uc?export=view&id=13T_p5xu2rIS2aPPz6Igez7hW--JtSiXk",
            "https://drive.google.com/uc?export=view&id=1T8P6ibJPfxVPR3AG2V1Vb4vgZXZE7a7n",
            "https://drive.google.com/uc?export=view&id=1PdFDa2ZHA35Ff5ZCPuEI73JD_PH0D1da",
            "https://drive.google.com/uc?export=view&id=1J_SBF39ebIOQlijqbvSLeUbi5GeDAL8M",
            "https://drive.google.com/uc?export=view&id=1woiOndW1sTlpM5bDKh0tAWEwpuFlmNek",
            "https://drive.google.com/uc?export=view&id=1hyhuZwlvwsvmHBriKcDXkd6RdQaB72M5",
            "https://drive.google.com/uc?export=view&id=16T8hr3WAYGk7BHtbQV4vo7PTXc1T8jTE",
            "https://drive.google.com/uc?export=view&id=1MmhVLsb58dyPw9Z_z24p6IaIRmtn7URl",
            "https://drive.google.com/uc?export=view&id=1yTqNPYh2ExpOoHQTsjELzvQzuL-ZwIWA",
                                
        ]
        

        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM": "1234501014",
                "Umur": "21",
                "Asal": "Kedaton",
                "Alamat": "Kedaton",
                "Hobi": "Main game",
                "Sosmed": "@biyokcb",
                "Kesan": "abangnya baik dan ramah",
                "Pesan": "semangat terus kuliahnya bang"
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM": "123450094",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan",
                "Hobi": "Menonton",
                "Sosmed": "@tvnty",
                "Kesan": "kakaknya mirip arafah lucu banget",
                "Pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM": "123450096",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobi": "Futssal",
                "Sosmed": "@razyn.hfd",
                "Kesan": "Abangnya ramah banget",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM": "124450064",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Metro Kibang",
                "Hobi": "Ngegame, ngoding, nyibukin diri",
                "Sosmed": "@apiszzaja_",
                "Kesan": "Abangnya baik banget sering becandaan",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM": "124450001",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Raja Basa",
                "Hobi": "Main Game",
                "Sosmed": "@gathfannadif",
                "Kesan": "Abangnya baik banget",
                "Pesan": "Semangat terus bang!"
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM": "123450119",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@keyashafi_",
                "Kesan": "Abangnya baikk banget",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM": "124450092",
                "Umur": "20",
                "Asal": "Kalianda",
                "Alamat": "Gedung Harapan",
                "Hobi": "Main Game",
                "Sosmed": "@aruccy_",
                "Kesan": "Abangnya baik banget",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM": "124450005",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Korpri",
                "Hobi": "Main Gitar",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "sherena Florencia",
                "NIM": "124450027",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Belwis",
                "Hobi": "Msake Up",
                "Sosmed": "@sher_renna",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Risa Romadona",
                "NIM": "124450127",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Rolling Skate",
                "Sosmed": "@risarmdna",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Fadya Izzatul 'Aini",
                "NIM": "124450075",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobi": "Makan",
                "Sosmed": "@fadyaizzatul_",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM": "124450075",
                "Umur": "19",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobi": "Baca Novel",
                "Sosmed": "@faizaanjanii",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM": "124450087",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Sukarame",
                "Hobi": "Banyak",
                "Sosmed": "@melva_fbrt",
                "Kesan": "Kakaknya baik banget!!",
                "Pesan": "Semangat terus kak!"
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "abangnya baik dan ramah",
                "Pesan" : "senang bisa sempat kenal abang walau sebentar, al fatihah buat bang fadil"
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Energik dan cepat akrab dengan siapa aja",
                "Pesan" : "Tetap semangat bang"
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Ramah dan selalu terlihat ceria.",
                "Pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "124450119",
                "Asal" : "Jambi",
                "Alamat" : "Sabah Balau",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@krnylee",
                "Kesan" : "Sopan dan menghargai orang lain.",
                "Pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Murah senyum dan enak diajak ngobrol",
                "Pesan" : "Tetap semangat dalam menjalani perkuliahan, Kak"
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "Pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "Pesan" : "Tularkan semangat hidup sehatmu ke kami, bang"
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "124450099",
                "Asal" : "Lampung Utara",
                "Alamat" : "asrama",
                "Hobi": "membaca",
                "Umur" : "20",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "Pesan" : "Jangan sungkan berbagi pendapat ke kami, bang."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "Humornya unik dan bikin suasana cair.",
                "Pesan" : "Semoga kenyataan selalu ramah padamu, bang."
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()
# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AlZvJm1bwqLcTWfzEEWJEGkxGXA10n-4",
            "https://drive.google.com/uc?export=view&id=1ArHMZclOHS0-YkcimTEs-GWPBS7N3M7n",
            "https://drive.google.com/uc?export=view&id=11mrEDtIIIKmVDAueJUWa0xgwPWL9zSiN",
            "https://drive.google.com/uc?export=view&id=1f9SOKyty48p6xXw1UxCVNa8XlWf0KNXW",
            "https://drive.google.com/uc?export=view&id=1qz2keGOjPowE1DS1BCOoE5-gu4bbDocl",
            "https://drive.google.com/uc?export=view&id=17T6PxV_C7ayGNdDRs08FBv6MbB_t_x-s",
            "https://drive.google.com/uc?export=view&id=1tmIe8vLPGmfmMu2Y0qjX4agkpv_oiHjy",
            "https://drive.google.com/uc?export=view&id=13bREMXQu_Dqtxj6QJWrIeqZhwNQrZzsy",
            "https://drive.google.com/uc?export=view&id=1cPJaUANbkFVTX0PbtYpTzhW50xrl-Gjj",
            "https://drive.google.com/uc?export=view&id=1IDI6eDK2HdB5L-2Sz-aZW6SDoL0_K4Or",
            "https://drive.google.com/uc?export=view&id=1srW8VJqN0Y4Pqcq1tucGqiw-BkT99t8a",
            "https://drive.google.com/uc?export=view&id=14ZCNfq5mcPoh0KKg3b9B90mjNgTsGiA4",
            "https://drive.google.com/uc?export=view&id=1-CvPg9gbLrATgukPI_zE6ZJSfg6I2SgD",
            "https://drive.google.com/uc?export=view&id=1MeLDb9sZX64gqoE2mvWoVOEmjSfaP5z_",
            "https://drive.google.com/uc?export=view&id=1hxXGjJTk_1Fxe0DEhgafwnxGdKokEdC_",
            "https://drive.google.com/uc?export=view&id=1QqaAWecIDxyqydkhdgziHrVYFQKvt7zn",
            "https://drive.google.com/uc?export=view&id=1pKWjssA_hNFWkxYgYGsF4sZ702lUePU_",
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
                "Kesan": "kakaknya baik dan ramah banget",  
                "Pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "Nama": "Vany Salsabila Putri",
                "NIM": "123450089",
                "Umur": "21",
                "Asal":"Jakarta",
                "Alamat": "Belwis",
                "Hobi": "nonton",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Kakaknya baik banget dan ramah!",  
                "Pesan":"semoga kuliahnya berjalan lancar"# 2
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Puri",
                "Hobi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "abangnya baik, ramah dan keren bisa sulap",  
                "Pesan":"Semangat terus bang kuliahnya"# 3
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "21",
                "Asal":"Malang",
                "Alamat": "Samping Pasar",
                "Hobi": "duel boxing sama reno",
                "Sosmed": "@friezaazmi",
                "Kesan": "bang azmi baik dan ramah orangnya",  
                "Pesan":"Semangat terus bang"# 4
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "21",
                "Asal":"Solo",
                "Alamat": "Samping kost Ezra",
                "Hobi": "Masak ayam",
                "Sosmed": "@ykeall",
                "Kesan": "baik, ramah, ga sombong",  
                "Pesan":"Semoga sehat selalu dan kuliahnya lancar"# 5
            },                      
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450072",
                "Umur": "20",
                "Asal":"Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Giring anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "abangnya asik dan humoris ",  
                "Pesan":"Semangat ya bang kuliahnya"# 6
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "18",
                "Asal":"Adam dan Hawa",
                "Alamat": "Depan kontrakan",
                "Hobi": "nonjokin orang",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kakaknya baik banget!",  
                "Pesan":"Semangat terus kak!"# 7
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "18",
                "Asal":"Jakarta",
                "Alamat": "Sebelah kost kak Vany",
                "Hobi": "Goreng ayam",
                "Sosmed": "@_haikaaall",
                "Kesan": "abangnya baik banget",  
                "Pesan":"Semangat terus bang"# 8
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450063",
                "Umur": "19",
                "Asal":"Tangerang kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "badminton",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kakaknya baik dan ceria lucu banget",  
                "Pesan":"Semangat terus ya kak kuliahnya"# 9
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450063",
                "Umur": "19",
                "Asal":"Tangerang kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "badminton",
                "Sosmed": "@queentanaabila",
                "Kesan": "Kakaknya baik banget waktu pplk sabar banget nganterin aku ke toilet",  
                "Pesan":"Semangat terus ya kak kuliahnya, semoga lancar dan lulus tepat waktu!"# 10
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "1234500114",
                "Umur": "21",
                "Asal":"Nias",
                "Alamat": "GH Raya",
                "Hobi": "lompat batu",
                "Sosmed": "@desmanhal_",
                "Kesan": "abangnya baik banget dan ramah juga",  
                "Pesan":"Semangat terus bang"# 11
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak Azzel orangnya humble, dan juga baik",  
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
                "Kesan": "orangnya baikk, dan juga ramah",  
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
                "Kesan": "Bang Jemar orangnya asik banget",  
                "Pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
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
                "Kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
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
                "Kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "Pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }




    
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iqP_B0ygO6Tws0JHWCxU5tkQkAG69pX0",
            "https://drive.google.com/uc?export=view&id=1E88k_AvviQUKl9v85T9m1WKsOc8yaa9-",
            "https://drive.google.com/uc?export=view&id=1PZof0zTKAHTKNZlfb4AZauxjcj9VKU09",
            "https://drive.google.com/uc?export=view&id=1AEhRBDW8jlyXNJ9Utjy4UxYmrxRanEQV",
            "https://drive.google.com/uc?export=view&id=1ORLcmCMqCKU3HFE7w54KpewMInl9pbjW",
            "https://drive.google.com/uc?export=view&id=1zj6sp8Rkx9INGE_09RCBw1kVNNnrVKhS",
            "https://drive.google.com/uc?export=view&id=1u4GTLT2RHPTwI700m0YIwAD7NokROl3Z",
            "https://drive.google.com/uc?export=view&id=10cfYy87R3zaohpmYEsaTOEOVJaZQpiRD",
            "https://drive.google.com/uc?export=view&id=1liV-H09UE8Vxp0nJahrzKe7rYDMAcm8y",
            "https://drive.google.com/uc?export=view&id=1qoAk_njXOg-E03kuAgYv-DUtu7SyIJv0",
            "https://drive.google.com/uc?export=view&id=1E1z8pi-75U0ExFK-U1OJlxzIQCgEnOVM",
            "https://drive.google.com/uc?export=view&id=1MXJzBa3SCh2LiI-R9IiIVszwf13NCR05",
            "https://drive.google.com/uc?export=view&id=15O83YgCZhwTEsDbn8Jt0jz89Zv3N7mf6",
            "https://drive.google.com/uc?export=view&id=1wh8OJbegbMx3OMoknM_coTCRmUdcpE-v",
            "https://drive.google.com/uc?export=view&id=1hcFgiFm2iHky703-WskIeyYtP8E2_OCF",
            "https://drive.google.com/uc?export=view&id=14C06GZ7dGq33K-yM1Oqg_zyDAT7Jsq41",
            "https://drive.google.com/uc?export=view&id=1OjBSEtxFLNnZ0L4VHTeNLmQCe7xqzedH",
            "https://drive.google.com/uc?export=view&id=1z7FLrR4D2s8-EWpCvIMUgFRQSZMgzqKG",
            "https://drive.google.com/uc?export=view&id=1XBPMIahlQKgcfODsg9OVmuLuKEKtmWSh",
            "https://drive.google.com/uc?export=view&id=1PZgl-0_qIanD8j2-F3CdonnF0-Mpvfr_",
            "https://drive.google.com/uc?export=view&id=1a7aKJNW6nlaDwpVikvirNv8M3j6TP30t",
            "https://drive.google.com/uc?export=view&id=1E3HPrOmqAVmP4h1nUtIPD6adCZQk2Mq2",            
        ]
        data_list = [
            
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal":"Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "kakaknya baik banget ramah, santai, dan keibuan vibesnya",  
                "Pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@bylaash",
                "Kesan": "kakaknya lucu banget dan cantik",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "21",
                "Asal":"Tetangga Kadep",
                "Alamat": "Belwis",
                "Hobi": "Mancing Keributan",
                "Sosmed": "@adityafq",
                "Kesan": "abangnya baik banget dan ramah",  
                "Pesan":"Semangat terus bang"# 3
            },
            {
                "Nama": "Khoirul Mutthoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal":"Lampung Barat",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakaknya imut banget, lucu, dan baik banget",  
                "Pesan":"Semoga ceria selalu dan lancar urusannya kak"# 4
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "123450044",
                "Umur": "20",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 5
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Natar",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 6
            },                      
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Disini aja",
                "Hobi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 7
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "1244500106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "bandar Lampung",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "bang bima keren banget, ramah, dan baik selama magang bang bima mengayomi banget!",  
                "Pesan":"Semangat terus bang kuliahnya semoga lancar selalu, aamiin."# 8
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal":"Tanggamus",
                "Alamat": "Bandar Lampung",
                "Hobi": "lihat lihat perumahan ",
                "Sosmed": "@bimo_arkana",
                "Kesan": "abangnya baik dan ramah",  
                "Pesan":"Semangat terus bang"# 9
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal":"Ikut Kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi Idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakaknya ramah, lucu, dan ceria",  
                "Pesan":"Semangat terus kak!"# 10
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "20",
                "Asal":"Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakaknya baik banget, waktu ngobrol juga asik banget",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kakaknya imutt banget gemes dan ternyata punya kembaran!!",  
                "Pesan":"Semangat terus kak kuliahnyaa"
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "1234500552",
                "Umur": "21",
                "Asal":"Luhak tanah data",
                "Alamat": "Gerbang Barat",
                "Hobi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Danil N Fadillah",
                "NIM": "123450103",
                "Umur": "19",
                "Asal":"Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "abangnya baik banget",  
                "Pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "123450021",
                "Umur": "20",
                "Asal":"Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "abangnya baik banget dan ramah juga!!",  
                "Pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "123450081",
                "Umur": "20",
                "Asal":"situlah",
                "Alamat": "pohon mulia",
                "Hobi": "nyari hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "abangnya baik banget!!",  
                "Pesan":"Semangat terus bang"
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "123450006",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "abangnya baik banget!!",  
                "Pesan":"Semangat terus bang kuliahnya"
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "123450093",
                "Umur": "Masih muda lah",
                "Asal":"Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "makan yang manis biar manis",
                "Sosmed": "@jaldii._",
                "Kesan": "abangnya baik banget, lucu banget!",  
                "Pesan":"Semangat terus bang kuliahnyaa"
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "123450074",
                "Umur": "20",
                "Asal":"Lampung",
                "Alamat": "Pinggir Jalan",
                "Hobi": "nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "123450010",
                "Umur": "20",
                "Asal":"Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "123450050",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Abangnya keren banget dan baik",  
                "Pesan":"Semangat terus bang menyuarakan aspirasi!"
            },                                                                          
       
            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jqY7cNmRU2JO6ofi79lav-PL5xXo3FDt",
            "https://drive.google.com/uc?export=view&id=1wHG6cy64eamI-iR6HaHn8c3g7mUomOdW",
            "https://drive.google.com/uc?export=view&id=1onJBBxK2YOhoiDs_3ZN1YDBnbIimIVuC",
            "https://drive.google.com/uc?export=view&id=1tiubx4Ypd2lRl_9R_LI-NJHo3EJt-GgW",
            "https://drive.google.com/uc?export=view&id=1VILr5PIZ0bJIMY81ZPUWuizEGGqVggUO",
            "https://drive.google.com/uc?export=view&id=1yE12OCokbYgYhkq1Z7ecWWzLkt1gUD5l",
            "https://drive.google.com/uc?export=view&id=131tg0lGQSX9TZWnJpv2Q5nF_fFFVg7o1",
            "https://drive.google.com/uc?export=view&id=1yOtn5zhTk_uydKYgr8Rz7ZhfT3Irp8ld",
            "https://drive.google.com/uc?export=view&id=14td_zgeZQPJoujFI4iuzgRjplPjVbtw_",
            "https://drive.google.com/uc?export=view&id=1LEdoXgrKtKBueSHlrmgpANWqN1SZ4_ni",
            "https://drive.google.com/uc?export=view&id=1MjJ2E3hkHWOUcJPuk6CIS9PEyQSyXGh_",
            "https://drive.google.com/uc?export=view&id=17cagNOMR9jP-mF-YznJ5G-z3MG1eKuZi",
            "https://drive.google.com/uc?export=view&id=1H1G4Q8HtaOi6aDf1BTT2ePr3thO2uhM6",
            "https://drive.google.com/uc?export=view&id=1txgJFvgT-ou5zxx-67lOpVmOa-jZ2Zxu",
            "https://drive.google.com/uc?export=view&id=11hgIJYM1dGTPaxpdXU3ObZyY86uP6eoe",
            "https://drive.google.com/uc?export=view&id=1ss9uTMV9FY7JBEIit1maNExvO1pPEffK",
    
        ]
        data_list = [
            {
                "Nama": "Haikal Fransiskus Simbolon",
                "NIM": "123450006",
                "Umur": "20",
                "Asal":"Silikalang Sumatera Utara",
                "Alamat": "Belwis",
                "Hobi": "Ngoding",
                "Sosmed": "@haikalsbln_",
                "Kesan": "abangnya ramah banget padahal keliatannya galak ternyata ngga",  
                "Pesan":"semangat terus kuliahnya bang" #1
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal":"Untung Suropati",
                "Alamat": "Untung Suropati",
                "Hobi": "Suka menolong orang",
                "Sosmed": "@risma.mustika_",
                "Kesan": "Kakaknya baik banget, salfok hobinya nolong orang masyaAllah",  
                "Pesan":"tetap jadi orang baik ya kak!"# 2
            },
            {
                "Nama": "Muhammad Hanif Zaky",
                "NIM": "123450064",
                "Umur": "21",
                "Asal":"Padang Sumatera Barat",
                "Alamat": "Perumnas Way Kandis",
                "Hobi": "Ngikutin drama tiktok",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Bang hanif ramah, baik, dan asik diajak ngobrol",  
                "Pesan":"semangat terus kuliahnya bang" # 3
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kakaknya baik banget, kalem, cantik banget ternyata kakak nim akuu",  
                "Pesan":"Semangat terus kak kuliahnya, semoga lancar selalu urusannya" # 4
            },
            {
                "Nama": "Cika Adelia Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin dina ngomong bahasa Minang",
                "Sosmed": "@cikamrbn",
                "Kesan": "Kakaknya baik banget dan ternyata nama kita samaan!",  
                "Pesan":"Semangat terus ya kak kuliahnya"# 5
            },
            {
                "Nama": "Gustin H. Tampubolon",
                "NIM": "-",
                "Umur": "-",
                "Asal":"-",
                "Alamat": "-",
                "Hobi": "-",
                "Sosmed": "@gustin.tpb",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 6
            },                      
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal":"Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Berkuda",
                "Sosmed": "@muhvnz",
                "Kesan": "abangnya kalem tapi ramah dan seru juga",  
                "Pesan":"Semangat terus bang kuliahnya!"# 7
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal":"Natar",
                "Alamat": "Natar",
                "Hobi": "Nitip makan sama Aqila",
                "Sosmed": "snasaa._",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 8
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobi": "Menyapa satpam Itera",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "kakaknya dari awal foto foto ramah dan welcome banget, funfact kakak ini kanim aku juga",  
                "Pesan":"Semoga kak hanna kuliahnya diberi kelancaran dan lulus tepat waktu" # 9
            },
            {
                "Nama": "A Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal":"Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Olahraga menembak",
                "Sosmed": "@farhanghani",
                "Kesan": "abangnya baik banget!!",  
                "Pesan":"Semangat terus bang"# 10
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Samping kuburan Belwis",
                "Hobi": "Suka eksperimen",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Kakaknya baik banget dan ramah",  
                "Pesan":"Semangat terus kak!"# 11
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450079",
                "Umur": "19",
                "Asal":"Medan",
                "Alamat": "Pesisir Belwis",
                "Hobi": "Begadang",
                "Sosmed": "cerine.ipynb",
                "Kesan": "Kakaknya baik banget, dan ngarahin pose foto yang lucu lucu",  
                "Pesan":"Semangat terus kak!"# 12
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "19",
                "Asal":"Kisaran city",
                "Alamat": "Pemda city",
                "Hobi": "Buat lagu",
                "Sosmed": "@jay_saputra_tmb",
                "Kesan": "abangnya baik, humble, seru juga!",  
                "Pesan":"Semangat terus ya bang kuliahnya, sukses selalu!" # 13
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Belwis",
                "Hobi": "main ML",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 14
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "18",
                "Asal":"Lampung Selatan",
                "Alamat": "korpri raya",
                "Hobi": "isengin havin di kelas",
                "Sosmed": "@rozakramdani__",
                "Kesan": "abangnya seru diajak ngobrol, ramah dan baik juga",  
                "Pesan":"Semangat terus bang kuliahnya"# 15
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobi": "Jadi asprak",
                "Sosmed": "@christiani8872",
                "Kesan": "Kakaknya baik banget, funfact kk ini asprak alpro dan astut lmd RA!! seru banget kalo kak teresa ngajar!",  
                "Pesan":"Semangat terus ya kak kuliahnya semoga kakak sehat selalu"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IImn-bwzrj7vV70MBmk_zh6cfpvGEqXv",
            "https://drive.google.com/uc?export=view&id=1B7DXOKpYlOmg_7N4AGQEDxdxffx3Maw2",
            "https://drive.google.com/uc?export=view&id=13Z5TFq5waedLDBwSLRkw3M7FzuKqxCCg",
            "https://drive.google.com/uc?export=view&id=18mXzlMsfCtWW7w_ZYHSAlJneXV7CnQZh",
            "https://drive.google.com/uc?export=view&id=133EBWrKSlcaiymXnXeJF3RpziWVOO9PH",
            "https://drive.google.com/uc?export=view&id=13ZR7K_g__ndBZCUkk7-7FOl0_2Tr1Wo7",
            "https://drive.google.com/uc?export=view&id=1fd-vmxtK8J29UC16G7bnQECuIW-yXC3t",
            "https://drive.google.com/uc?export=view&id=1Sh5npJ-ecdhCo5QZR5WMIOUC-suHK_4B",
            "https://drive.google.com/uc?export=view&id=1lsexSMeqP_3EZwoJ3zQmZFhfDpbuAdjr",
            "https://drive.google.com/uc?export=view&id=19sWSqL7TWP4kHwDVTcmyuNEZpmkNq_Rb",
            "https://drive.google.com/uc?export=view&id=18bm_0khZDjIvfhsje-VogTBVqVQNGdvQ",
            "https://drive.google.com/uc?export=view&id=1CMfrmUJIe9Ivf2uqs7sz2lut0KPCB_4U",
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
                "Kesan": "abangnya asik banget, baik, dan ramah",  
                "Pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "Nama": "Hanifah Inaya Sari",
                "NIM": "123450123",
                "Umur": "21",
                "Asal":"Balam",
                "Alamat": "Balam",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakak nya cantik banget dan kalem",  
                "Pesan":"semangat terus kuliahnya kakak" # 1
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "19",
                "Asal":"Padang",
                "Alamat": "Hasan 4",
                "Hobi": "Nonton Marvel, Tidur",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya seru waktu wawancara, ramah, dan baik banget",  
                "Pesan":"semangat terus kuliahnya ya kakk"# 1
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "NIM": "124450012",
                "Umur": "21",
                "Asal":"lampung",
                "Alamat": "Pemda",
                "Hobi": "Main game",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "abangnya baik, humble, asik",  
                "Pesan":"semoga kuliahnya lancar bang!"# 1
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "124450016",
                "Umur": "19 tahun",
                "Asal":"Semarang",
                "Alamat": "Balam",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakak ini asik dan baik juga",  
                "Pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Natar",
                "Hobi": "Mancing",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "abangnya asik banget, baik juga, pas jadi asprak sabar banget ngajarin satu satu",  
                "Pesan":"semangat terus kuliahnya bang semoga sukses selalu"# 1
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal":"Sumbar",
                "Alamat": "Kelengkeng 5",
                "Hobi": "Tidur",
                "Sosmed": "@talithaaajtine",
                "Kesan": "Kakak nya baik dan asik juga",  
                "Pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal":"Palembang",
                "Alamat": "Wayhui",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakak ini baik, lucu juga pas jawab jawab pertanyaan pas wwc",  
                "Pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "Nama": "Abdillah Fikri Al pome",
                "NIM": "123450062",
                "Umur": "21",
                "Asal":"Sumsel",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest_",
                "Kesan": "abangnya humoris banget dan asbun nya lucu banget bikin ketawa",  
                "Pesan":"semangat terus kuliahnya ya bang"# 1
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal":"Sumbar",
                "Alamat": "Samping kost rafli",
                "Hobi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "abang ini humble, seru, dan baik",  
                "Pesan":"semoga sukses selalu bang" # 1
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal":"Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakak ini asik, baik, dan cantik",  
                "Pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Lampung Timur",
                "Alamat": "Nargo Lestari",
                "Hobi": "Olahraga, Makan makanan manis",
                "Sosmed": "@dellaansaftr",
                "Kesan": "kakaknya seru, baik, humble juga",  
                "Pesan":"semoga lancar selalu kuliahnya kak, semangat!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m2rvZSz0qpUXtsy8x2g1AcDR1g_kvNDJ",
            "https://drive.google.com/uc?export=view&id=1W3cvvaj4zcC-o3U_gu4WLSS618R0mFem",
            "https://drive.google.com/uc?export=view&id=1WtJpHfMHmMjYlf5BZ7Z7NPwNpylCVncH",
            "https://drive.google.com/uc?export=view&id=1WtDi1SdPHSaqWj9Bpuz5cOGwFZA6M8kl",
            "https://drive.google.com/uc?export=view&id=1AtKU8BaPsYtO4EQnrr6Sr63ocG6Z9tBM",
            "https://drive.google.com/uc?export=view&id=1jGG1ralwM5Iy7PQTsmGApsWHfDH18W1t",
            "https://drive.google.com/uc?export=view&id=1fm2zZKGdoESow-clgtd5WYKF2H1Zfz0s",
            "https://drive.google.com/uc?export=view&id=1NSwY-NS2t2HG_LUowlUrrCgEBHIVVb4P",
            "https://drive.google.com/uc?export=view&id=15Tqp1GDipeMeb7459e5BmCNNpqJSkUnq",
            "https://drive.google.com/uc?export=view&id=1HOG3BPV4Wpjt8WN2VXL4mOK8fnTZKzb-",
            "https://drive.google.com/uc?export=view&id=15WrpeBWCfwO9UfzkKzjBh31j_f6TXMod",
            "https://drive.google.com/uc?export=view&id=1Z096O3z95Hm8sDUb9KLIrlz3SamJ7NNq",
            "https://drive.google.com/uc?export=view&id=1c4qUjCxCyk7_Eqx78eROUrXF9xgc2uL6",
            "https://drive.google.com/uc?export=view&id=1JY_eN7oI23lhBPjyRxS_6-wnLV8gR-tl",
            "https://drive.google.com/uc?export=view&id=1wpfj5kkLpvCy5tPfae-4VfK2s8f6ITqs",
            "https://drive.google.com/uc?export=view&id=1gAj2QGtqLpG9D9foys0bH3zaFkGdoJVD",
            "https://drive.google.com/uc?export=view&id=1-8mhvvUcdUldYjOpagaW5tAOBguSeXEj",
            "https://drive.google.com/uc?export=view&id=1eigi2t7Dhw1snYqjsKSSt8-Tx3GvPSGR",

        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM": "123450082",
                "Umur": "20",
                "Asal":"Payakumbuh",
                "Alamat": "Way Huwi",
                "Hobi": "Musingin TA",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "Kakaknya baik banget dan ramah!!",  
                "Pesan":"semangat ya kak ngerjain TA-nya!"# 1
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM": "123450028",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": "Berenang",
                "Sosmed": "@donnamaya.p",
                "Kesan": "kakakmya cantik, baik, humble",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "NIM": "123450037",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nonton tong setan",
                "Sosmed": "@noerruuu",
                "Kesan": "abangnya baik, kalo jelasin mudah dipahami",  
                "Pesan":"Semangat terus bang kuliahnya"# 3
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Umur": "21",
                "Asal":"Karawang",
                "Alamat": "Airan",
                "Hobi": " Nongkrong depan ruang prodi",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 4
            },
            {
                "Nama": "Raihanna Adelia Putri",
                "NIM": "123450041",
                "Umur": "20",
                "Asal":"Terbanggi Besar",
                "Alamat": "Airan Raya 1",
                "Hobi": "Menulis dan membaca",
                "Sosmed": "@n1tg.-",
                "Kesan": "Kakaknya lucu banget imutt",  
                "Pesan":"Semangat terus kak!"# 5
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Umur": "19",
                "Asal":"Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan-jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "orangnya lucu, ramah, cantik!",  
                "Pesan":"Semoga selalu bahagia!"# 6
            },                      
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Umur": "20",
                "Asal":"Lampung Selatan",
                "Alamat": "Pemda",
                "Hobi": " Belajar",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakaknya baik, ramah, dan asik banget!!",  
                "Pesan":"Semangat terus kak!"# 7
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "1244500031",
                "Umur": "18",
                "Asal": "Rumah",
                "Alamat": "Ryacudu",
                "Hobi": "Bully Felisya Nabila Nugroho",
                "Sosmed": "@muh_razan_",
                "Kesan": "abangnya baik, kece, keren",  
                "Pesan":"Semangat terus bang"# 8
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton F1",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 9
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": "124450014",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mancing",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakaknya humble, baik, asik",  
                "Pesan":"Semangat terus kak!"# 10
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": "124450043",
                "Umur": "Gaada yang tau",
                "Asal":"Rumah bapak",
                "Alamat": "Gedung F",
                "Hobi": "Ngitungin beras di karung",
                "Sosmed": "@difanyhsa",
                "Kesan": "Kakaknya cantik, baik, asik",  
                "Pesan":"Semoga sukses selalu"
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "1244500112",
                "Umur": "19",
                "Asal":"Jabung",
                "Alamat": "Rajabasa",
                "Hobi": "Bobo",
                "Sosmed": "@Xifasky",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mencintai Andrew Garfield",
                "Sosmed": "@luciarchel_",
                "Kesan": "Kakaknya seruu",  
                "Pesan":"semoga lancar kuliahnya kakk"
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Umur": "20",
                "Asal":"Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Scroll Fesbuk",
                "Sosmed": "@edsel_0712",
                "Kesan": "abangnya kalem, baik, ramah",  
                "Pesan":"Semangat terus bang!"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Umur": "21",
                "Asal":"Surabaya",
                "Alamat": "SUkarame",
                "Hobi": "Nyuluh Manuk",
                "Sosmed": "@daffascript_",
                "Kesan": "abangnya asik, baik banget!!",  
                "Pesan":"Semangat terus ya bang"
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM": "124450054",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Main Piano",
                "Sosmed": "@nzlhauly",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Allisha",
                "NIM": "123450081",
                "Umur": "20",
                "Asal":"situlah",
                "Alamat": "pohon mulia",
                "Hobi": "nyari hobi",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Kakaknya ceria banget, imut, cantik!",  
                "Pesan":"Semoga kuliahnya lancar kakk!"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "123450006",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "makan yang manis biar manis",
                "Sosmed": "@_shaazzh",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()


if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1alkJfuN7M64Fdm-HLF6y3cDkpg3JcoW-",
            "https://drive.google.com/uc?export=view&id=1--PspYPrQmPbmHLYZT_jmPSPi1dFPjRh",
            "https://drive.google.com/uc?export=view&id=1JKb9CbEgbBxhyt6Zd5hGhVAEWHqmtfvQ",
            "https://drive.google.com/uc?export=view&id=1YpNKXtL7tK-xjltoInu8a-FkYVo4vlyE",
            "https://drive.google.com/uc?export=view&id=1yB8sWinY0iqNnquIWCXYoNmp83Cyzqvc",
            "https://drive.google.com/uc?export=view&id=1z1_M9MUpRAkdyFwojzJKlEs_qPFWh1UT",
            "https://drive.google.com/uc?export=view&id=12-z-OFrXUEbuYralALJMMfJjeR1tEdxY",
            "https://drive.google.com/uc?export=view&id=1-zKt5NkXfMMltNoCs-zS2TCleK90VkOz",
            "https://drive.google.com/uc?export=view&id=1142EWm8AK4_AIbhEJZJkq-U1zz79ncJ2",
            "https://drive.google.com/uc?export=view&id=1AfDzz4jsj95HdffDtiSEtXW3brKx_vw0",
            "https://drive.google.com/uc?export=view&id=1zXBEtnuYdAYZCP7sYlcVM5Nq2zfco9L6",
            "https://drive.google.com/uc?export=view&id=12OkUsn8gwgA5b3nC2rXvx60Umf9TU5cX",
            "https://drive.google.com/uc?export=view&id=1SZOdwsAZJpvXnwAjRXtVTzWwQ80tESHA",
            "https://drive.google.com/uc?export=view&id=1pSxJIsavX6gXF1lt2DRG6Sd2bPzWE9Cr",
            "https://drive.google.com/uc?export=view&id=1MKa_yRaJi5t9R6kUnJ0UYDxrNvr2mmrS",
        ]
        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "NIM": "123450109",
                "Umur": "20",
                "Asal":"Payakumbuh",
                "Alamat": "Way Huwi",
                "Hobi": "Lari",
                "Sosmed": "@kevinaj_",
                "Kesan": "abangnya baik, waktu wwc penjelasan nya mudah dipahami",  
                "Pesan":"semangat terus ya bang kuliahnya"# 1
            },
            {
                "Nama": "Gusti Putu Ferazka D.",
                "NIM": "123450046",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Way Dadi",
                "Hobi": "Mendaki",
                "Sosmed": "@ferazkaa",
                "Kesan": "kakaknya keren banget outfitnya",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "NIM": "123450088",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Belwis",
                "Hobi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "abangnya baik, ramah, asik",  
                "Pesan":"Semoga lancar kuliahnya bang"# 3
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM": "123450086",
                "Umur": "21",
                "Asal":"Karawang",
                "Alamat": "Airan",
                "Hobi": " Nongkrong depan ruang prodi",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 4
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM": "124450121",
                "Umur": "21",
                "Asal":"Bogor",
                "Alamat": "Way Kandis",
                "Hobi": "Motoran bareng bang bryan",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "abangnya seru, baik, asik",  
                "Pesan":"Semangat terus kuliahnya bang, sukses selalu!"# 5
            },
            {
                "Nama": "Juwita Sari",
                "NIM": "124450091",
                "Umur": "19",
                "Asal":"Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan-jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 6
            },                      
            {
                "Nama": "Muhammad Afdal Lutfi",
                "NIM": "124450047",
                "Umur": "19",
                "Asal":"Lampung Tengah",
                "Alamat": "Jalan Pulau Damar",
                "Hobi": "Menjawab soal dari dosen dipapan tulis",
                "Sosmed": "@afdal.03",
                "Kesan": "abangnya baik dan asik!",  
                "Pesan":"Semangat terus bang!"# 7
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM": "1244500024",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobi": "Pulang ke Metro",
                "Sosmed": "@slbnzw",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"# 8
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM": "123450091",
                "Umur": "21",
                "Asal":"Lampung Tengah",
                "Alamat": "Belwis",
                "Hobi": "Nonton F1",
                "Sosmed": "@mridwaan_22",
                "Kesan": "abangnya keren, ramah, asik",  
                "Pesan":"Semangat terus bang kuliahnya!"# 9
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM": "124450060",
                "Umur": "18",
                "Asal":"Sumatera Selatan",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@andra.lhm",
                "Kesan": "bang andra seru banget selalu ada topik dan cairin suasana",  
                "Pesan":"Semangat terus ya bang kuliahnya"# 10
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM": "124450003",
                "Umur": "20",
                "Asal":"Nias",
                "Alamat": "Belwis",
                "Hobi": "Motoran",
                "Sosmed": "@bryantel_",
                "Kesan": "abangnya baik, asik, seru juga",  
                "Pesan":"Semangat terus bang"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM": "1244500067",
                "Umur": "17",
                "Asal":"Semarang",
                "Alamat": "Kemiling",
                "Hobi": "Ternak sapi",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "abangnya seru, obrolannya asik",  
                "Pesan":"Semangat terus bang dan sukses selalu"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM": "124450095",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Mencintai Andrew Garfield",
                "Sosmed": "@luciarchel_",
                "Kesan": "Kakaknya baik banget!!",  
                "Pesan":"Semangat terus kak!"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM": "124450098",
                "Umur": "20",
                "Asal":"Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Scroll Fesbuk",
                "Sosmed": "@cacalvra",
                "Kesan": "Kakaknya imut, gemes, cantik",  
                "Pesan":"Semoga kuliahnya lancar kak"
            },
            {
                "Nama": "Muhammad Rafka fatih Al Ghathfaan",
                "NIM": "124450023",
                "Umur": "18",
                "Asal":"Kalimantan Barat",
                "Alamat": "Korpri",
                "Hobi": "Tukang Parkir",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "abangnya keliatan cuek dan galak padahal aslinya baik, ramah juga",  
                "Pesan":"semoga kuliahnya lancar bang, sukses selalu!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Minbak()
