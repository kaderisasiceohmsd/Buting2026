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
            "Baleg",
            "Senator",
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
# FUNGSI MENAMPILKAN PROFIL
# ==================================================
def display_images_with_data(gambar_urls, data_list):
    images = load_images_b64(tuple(gambar_urls))

    st.markdown(
        f"<div class='section-head'><h2>{esc(menu)}</h2>"
        f"<span class='count-chip'>{len(data_list)} anggota</span></div>",
        unsafe_allow_html=True,
    )

    query = st.text_input(
        "Cari",
        placeholder="🔍  Cari nama, jabatan, asal, atau hobi...",
        label_visibility="collapsed",
        key=f"cari_{menu}",
    )
    q = query.strip().lower()
    st.write("")

    shown = 0
    for i, data in enumerate(data_list):
        if q:
            haystack = " ".join(
                str(data.get(k, "")) for k in ("nama", "jabatan", "asal", "alamat", "hobbi", "sosmed")
            ).lower()
            if q not in haystack:
                continue

        nama = clean(data.get("nama"), "Tanpa Nama")
        jabatan = clean(data.get("jabatan"), "")

        # Foto atau avatar inisial
        img_b64 = images[i] if i < len(images) else None
        if img_b64:
            photo = f"<img src='data:image/jpeg;base64,{img_b64}' alt='Foto {esc(nama)}' loading='lazy'/>"
        else:
            photo = (
                f"<div class='avatar-fallback'><span>{esc(initials(nama))}</span>"
                f"<small>Foto belum tersedia</small></div>"
            )

        # Lencana jabatan (disembunyikan kalau kosong)
        badge = (
            f"<div class='jabatan-badge'><span class='jabatan-star'>★</span>{esc(jabatan)}</div>"
            if jabatan else ""
        )

        # Umur: tambah "Tahun" hanya kalau berupa angka
        umur = clean(data.get("umur"))
        umur_text = f"{umur} Tahun" if umur.isdigit() else umur

        # Sosial media
        sosmed = clean(data.get("sosmed"))
        sosmed_html = (
            f"<span class='social-chip'>{esc(sosmed)}</span>" if sosmed != "-" else "-"
        )

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
                <div>
                    <div class='profile-name'>{esc(nama)}</div>
                    {badge}
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


# ==================================================
# PILIH MENU
# ==================================================
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sh-jJCj-9ip7RN0EuLslhsyHznUKiDwK",
            "https://drive.google.com/uc?export=view&id=1G2cPYH26LW1EnJaU-MLqjKb4Pm4kadfD",
            "https://drive.google.com/uc?export=view&id=1vhIHJwUBW1pOpeKVr5RP1_KSrhrZPxgW",
            "https://drive.google.com/uc?export=view&id=1g_M9Z_OdQzzX-OqKgKOndO7KCYd2hZQz",
            "https://drive.google.com/uc?export=view&id=1qiqCtguThFK9DJsaoFM0mgMbBTjk5ulO",
            "https://drive.google.com/uc?export=view&id=10jdr1K2Yf6-nkj7JY6RSPFFOTXDQOUrK",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "bang ginda keren panutan super keren.  ",  
                "pesan":"Semoga TA nya lancar terus yaa bang! "# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil kaya gangster gangster, keren abiezz, terus kaya orang jago gitu loh.",  
                "pesan":"Semoga bang Aqil sehat selalu yaa, happy teruss ta nya lancar"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefffiidefi",
                "kesan": "Kak Efi vibes nya cewe keren bangett.",  
                "pesan":"Semoga kuliah nya lancar terus yaa, bahagia terus kakk"# 1
            },
           {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "kakanya keren bangett, jarang jarang cwo jadi sekre",  
                "pesan":"semangat dan sehat teruss ya kakk"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu Luluk",
                "sosmed": "@hafsafazilahh",
                "kesan": "kak hafsa humble banget.",  
                "pesan":"happy terus ya kak!!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthhifiarmdhni",
                "kesan": "kak lutfia imut banget",  
                "pesan":"lancar lancar ya kak kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kL92wnsyEoYz2qy1Le0deAwXrv3gbffG",
            "https://drive.google.com/uc?export=view&id=1js_7BVgeNmLX0cFnIybVzbkxNVDR0CWQ",
            "https://drive.google.com/uc?export=view&id=14CaGMZoaOe_vbUI4-I6AoEfVYDd_PLXh",
            "https://drive.google.com/uc?export=view&id=1s0yPm4twbVjOMoZU8jct0mZUQWDXwUMM",
            "https://drive.google.com/uc?export=view&id=1wIVkZ8caciA-RizItHmHRKtWQqT9xNk8",
            "https://drive.google.com/uc?export=view&id=1XntscKxFUy5H1kKTTLHVbkM8VZoqbOOF",
            "https://drive.google.com/uc?export=view&id=1bvQKt8algRM-1HduZTPZOudFfcbOF5lS",
            "https://drive.google.com/uc?export=view&id=1pa7BM4k8rYB7XT7rUtbT8yffyN1xvv4h",
            "https://drive.google.com/uc?export=view&id=1n6GP5C4_OenEYBUjmAZ-tw3KkwjhmY0T",
            "https://drive.google.com/uc?export=view&id=1GD1ysL8trSl8ffBqA8qaE6daG99ogII6",
            "https://drive.google.com/uc?export=view&id=1FOZgIT1u4ItS0KFuuy4XSEef-1MrBwWe",
            "https://drive.google.com/uc?export=view&id=1YZeOgSHtcPeNf7W8bEOCe2U_jY5n7nKB",
            "https://drive.google.com/uc?export=view&id=12OYIEQ5prwP2x64qOfVK-uMqCci7kWId",
            
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
                "kesan": "bang ridho baik, lucu juga terus orangnya sangat sangat fun ya ",
                "pesan": "sehat selalu ya bang ridho, sukses teruss"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "kak jue bener bener lucu imut outfit nya gemes banget",
                "pesan": "semangat TA nya ya kak!!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kakak nya baik, lucu juga",
                "pesan": "happy terus ya kak !!!"  # 1
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "outfit kakanya lucu banget gemes",
                "pesan": "happy dan semangat terus yaa kak !!!"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "23",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "bang dharu orangnya baik banget humble juga",
                "pesan": "semangat dan sehat terus ya bang!!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "bang givaro orangnya baik, lucu juga",
                "pesan": "semangat terus TA nya ya bang"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "abangnya baik, outfitnya juga bagus banget",
                "pesan": "happy terus yaa bang  !"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "bang jona lucu banget sih, orangnya baik juga",
                "pesan": "semangat dan sehat selalu ya bang !!!"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "kakaknya keren banget, dan baik banget",
                "pesan": "happy terus ya kak!!!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya dari city earth aka kotabumi, satu kampunk",
                "pesan": "happy dan semangat terus ya kak!!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "abangnya keren banget",
                "pesan": "happy dan semangat terus ya bang !!!"  # 1
            }, 
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica baik lucu juga",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
    

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NNyH3s5-ZgN1MtU5W_DPqlPwYrJK6gGr",
            "https://drive.google.com/uc?export=view&id=1FK9mia17rzt0TYToZz1621UQiHXykaKz",
            "https://drive.google.com/uc?export=view&id=1wkLdr85KLet_qIGhUj74GT6YRtF1fmSj",
            "https://drive.google.com/uc?export=view&id=1WYy-bAC5gReQoFA4xhiOSFOTprjphmkq",
            "https://drive.google.com/uc?export=view&id=1Lu4H8nOTZiExCSSv7tXdy0dCe-UAwlbM",
            "https://drive.google.com/uc?export=view&id=1KXWrm_ldT6-xK_MLAZ3xeJ1TAksgj1Jp",
            "https://drive.google.com/uc?export=view&id=1kQ2GC1UH7xFZPRR6Rzbf8_Nqc5Gelnon",
            "https://drive.google.com/uc?export=view&id=14wIKTYzQVMJEBam8tbqoDunopqo_xXAq",
            "https://drive.google.com/uc?export=view&id=1WdUXIqfbGNSldeDmIFkUmQWfMqR56Fen",
            "https://drive.google.com/uc?export=view&id=1KQAZVUce4lupdlfED8Zj253VlANNF_LE",
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
                "kesan": "kak iza kak zizah, pas awal ketemu tuh emang kaya wah ba wardah banget syui, wangi wangi kasyen wardah, kakanya lucuu banget banget terus hem happy person juga yaa love you kak izaa",
                "pesan": "semoga cepet ehem yh, yyta lah semangat teruss dan happy terus yaa kak"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kak nadya waktu pertama ngeliat kaya bener bener byutipul, masyaAllah banget kaya wah bening banget, kakanya makan apa ya kok bisa sebening itu, so so byutipul",
                "pesan": "happy teruss yaaa, semogaa kuliahnya lancar terus kak !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "KAKK LIAAAA, kakaknyaa lucu bangett ihh, terus ternyata cerewet padahal aku ngiranya kakanya tuh pendiem banget gtu, so fun sih kalo deket kak lia semua hal di ketawain sama dia mah ",
                "pesan": "SEMANGATTT SAKSES SELALU!"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "KaK dwi imut banget, so cute deh, baikk seruu jugaa, TAASSS NYA GEMESS BANGETTTTTTT!",
                "pesan": "semangat teruss yaa kakk kuliahnyaaaaa"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kak suci happy person bangett, bener bener fun orangnya!",
                "pesan": "infokan spot mancing"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "awal ketemu kak aqila pas pertama kali banget supporteran di gsc, kak aqila pake baju coklat, baju panitia sf terus ada satu moment dimna aku dan kak aqila ngobrol, tapi kok aku kaya kenal dia yaa, eh ternyata dia KETUA MPK SMANTRI, kita satu kampung, terus pertemuan ke dua sama kak aqila itu di warkop agam, dia bantuin kita nyusun acara pilketang, dan ternyata pas pengumuman kelompok kader dia ternyata jadi mentor ku, adalah suatu hall yang benar benar ga terduga, kak aqila orang nya bener bener fun, seru, care, ketawanya gede bwanget lucu sih, klo sama kak aqila tuh semua masalah semua tugas tugas tuh kaya kerasa fun aja deh",
                "pesan": "makasi ya kak, kakak harus happy terus ya ketawanya tolong di kecilin kak, gaboleh berhenti jadi happy person, akuu suka kak aqila kalo pake baju kuning, gemes soalnya, love you kakk sarangek, aisiteru"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "bang wielman keren banget jago debat pengen deh jago publik speaking kaya bang wielman",
                "pesan": "Sehat dan semangat terus ya bang wielman"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "ternyata abang nya baik, lucu juga",
                "pesan": "happy terus ya bang ezel!"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "wah ini sih keren banget sih inimah, abang ini makko tanding sih",
                "pesan": "Semangat dann happy teruss bang"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal": "Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "pertama kali tau bang nando karena bang nando oprasional magenta",
                "pesan": "happy terus dan selalu jadi bang abang ope yh"
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
    # PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GIr1rN2MwLUQ0fR2EtSp3HUZ9ZXikQdL",
            "https://drive.google.com/uc?export=view&id=1wIm3JHO1sV77lFPzDXGAjKUCRNktMNfm",
            "https://drive.google.com/uc?export=view&id=10LXA2Vna6XC054gBkk9BAOuYYmWeOnL9",
            "https://drive.google.com/uc?export=view&id=1oatTr0-wdkODSR8KtvDAxPAO48L46HJ4",
            "https://drive.google.com/uc?export=view&id=12NKepI-O7NBPIQtinARjkbfTyhtLJkZc",
            "https://drive.google.com/uc?export=view&id=1fzgj033vC8aCGNK7itMAILU1S-xGAx5n",
            "https://drive.google.com/uc?export=view&id=1eUAY-oxSuf5LbRC4PPA6TDOh8kdu2LD5",
            "https://drive.google.com/uc?export=view&id=1GHaEHkZzQD1gLwdX0azNLEN5XqkHsbh3",
            "https://drive.google.com/uc?export=view&id=1NpWXYOqSCix4Oi3iisrN8fY0TSor3CFX",
            "https://drive.google.com/uc?export=view&id=1NuTkFQmuJcLxA15OHjyXhEr_YaowcA33",
            "https://drive.google.com/uc?export=view&id=1umjMtOImZFMEX9gi4FkcUVHSbAkTknyO",
            "https://drive.google.com/uc?export=view&id=1pq2z-qzLJWsqoaTs-Jbi3Q75F6xv7-p6",
            "https://drive.google.com/uc?export=view&id=1LLyWO13MjsNQZXn5PmrDXHM7i4sbMtyQ",
            "https://drive.google.com/uc?export=view&id=1i9oyRv937PfwJaVv9NxMLEErRLzmgF-_",
            "https://drive.google.com/uc?export=view&id=1yrGQ8aDT5_R4D9pX-BwJDFLJndZbriEw",
            "https://drive.google.com/uc?export=view&id=1hVBXY0c4efMRKDf0WhVSBKCA9IWQCliJ",
            "https://drive.google.com/uc?export=view&id=1s9RS7GKRY3zzfEQ_SBJHSZ-ks4vcb17f",
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
                "kesan": "kak arienta vibes nya bener bener cewe keren",  
                "pesan":"happy dan semangat terus ya kak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan kost",
                "hobbi": "pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baik, cantik, keren",  
                "pesan":"sehat dan happy terus ya kak"# 3
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel super super keren sih!",  
                "pesan":"semangat terus TA nya bang"# 4
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "bang azmi baik, keren banget",  
                "pesan":"happy terus ya bang azmi"# 5
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "bang ayake lucu, ternyata orang nya fun banget!",  
                "pesan":"happy terus ya bang ayake!"# 6
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@wielhawn",
                "kesan": "bang caesar keren banget!",  
                "pesan":"Sehat selalu ya bang caesar"# 7
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak eudia baik, lucu juga orangya juga fun!!",  
                "pesan":"Semangat dan sukses terus ya kak!"# 8
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@helmy_inst",
                "kesan": "bang haikal baik, pinter, keren deh pokonya",  
                "pesan":"semoga sehat dan happy terus ya bang !"# 9
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@putrimanna",
                "kesan": "kak putri cantik  banget, outfitnya juga bener bener lucu!!",  
                "pesan":"happy terus kak putri !"# 10
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kak nabila bener bener baik, cantik, ramah juga",  
                "pesan":"Semangat terus ya kak kuliahnya, happy teruss!"# 10
            },  
            {
                "nama": "Desman Velius Halawa",
                "nim": "1234500114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "GH Raya",
                "hobbi": "lompat batu",
                "sosmed": "@desmanhal_",
                "kesan": "bang desman baik, keren juga",  
                "pesan":"sehat selalu bang desman!"# 11
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel cantikk banget byutipull banget",  
                "pesan":"Semoga semua keinginan kak azzel tercapai, aaamiin"# 12
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "orangnya baikk, dan juga ramah, kak charlindah pernah ngajarin aku ngemc",   
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 13
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya asik banget, lucu juga",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
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
                "pesan":"Semoga kak nabila kuliahnya lancar"
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
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M9Zkza-2FonsbpJT4AuvRrWjmqJRcHVj",
            "https://drive.google.com/uc?export=view&id=1foUQybl9ncvEB5vro7yWv8I1hIfejwvY",
            "https://drive.google.com/uc?export=view&id=1iO0jvULlTIhPqRIZwlidL-vX0zqsM_66",
            "https://drive.google.com/uc?export=view&id=1wECUhrE-bNqTE6ill7r6Y9J9eqrgM9w0",
            "https://drive.google.com/uc?export=view&id=1pECiUXwWt0XYu-JaszXfS9QVnLzhhlsN",
            "https://drive.google.com/uc?export=view&id=19zXlno-kwf5NEsZWUQ5S2x8Yj3iEYOuR",
            "https://drive.google.com/uc?export=view&id=1wQft-mH16rBhsg28PNyXOA7gJdu98uT3",
            "https://drive.google.com/uc?export=view&id=1XIkKFnVBLXTy8McDAvQWYLbwG_ZZETz8",
            "https://drive.google.com/uc?export=view&id=1oybRJar2tAyj5nwe2vRZ0G8qmKoiBfFm",
            "https://drive.google.com/uc?export=view&id=18dXiKNZmiopWzdeEG5cG_ww8wiDRvJOs",
            "https://drive.google.com/uc?export=view&id=10ay-q5mk8dm3m728sfweT-36qXfLzDdE",
            "https://drive.google.com/uc?export=view&id=1W088T77RUIXCceINolX1kUyyf43ZF-rd",
            "https://drive.google.com/uc?export=view&id=1bj0b5ZfKocGsBVH6Kbw5RuJnEhusWO-d",
            "https://drive.google.com/uc?export=view&id=1k14-JtbcdSKFHYpisSfXZzxUYXW4LILq",
            "https://drive.google.com/uc?export=view&id=1jvaxtkKqGLywRSbivcml32MxWZc-Y_cD",
            "https://drive.google.com/uc?export=view&id=1qTJ7tgsx6mzsIL7OpHBEDlMDtJH1wnZT",
            "https://drive.google.com/uc?export=view&id=16jpo4QLo0k7W9hkeRVXGla95hXLkUs5p",
            "https://drive.google.com/uc?export=view&id=1x19xJX6c4DOpbeesyd0ATuF0Xj6faIjx",
            "https://drive.google.com/uc?export=view&id=1iNIwwiejEPShgHiyD70LQeSUBDHslMws",
            "https://drive.google.com/uc?export=view&id=1CLi-XuWRZ5L149SZ1VdrKuvq20LAV_aQ",
            "https://drive.google.com/uc?export=view&id=1Z-aqT7svpnua4o4UqoG1MXdJPp3PcjHE",
            "https://drive.google.com/uc?export=view&id=1JwqwHhcR7ZLrLs3oqcbZgzyjirNvemJe",
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
                "kesan": "bang fabio orang keren sih, keren banget kagum",
                "pesan": "semoga apa yang di semogakan tersemogakan ya bang"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "kakaknya mirip arafah lucu banget",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya ramah banget, baik juga, keren juga",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget sering becandaan, lucu imut bang hafidz gemesss",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik ganteng, keren deh pokonya",
                "pesan": "Semangat dan sukses terus ya bang !"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya baik, ramah, humblke juga",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "abangnya baik, pinter, klo di ajak ngobrol juga nyambung banget",
                "pesan": "Semangat terus dan suskes terus bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kak viola rambut nya cantik banget, so byutipul!",
                "pesan": "Semangat dan sukses terus ya kak!"
            },
            {
                "nama": "sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Msake Up",
                "sosmed": "@sher_renna",
                "kesan": "Kak sherena super duper imut, so cute!",
                "pesan": "Sehat dan semangat terus kuliahnya kak"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak risa outfitnya lucu banget!",
                "pesan": "Semangat dan sehat selalu ya kak"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kak fadya cantik banget!!",
                "pesan": "Semangat dan sukses terus kak!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "aku ngefans banget sama kak faiza, super duper keren cantik!",
                "pesan": "happy terus ya kak faiza!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kak melva imut banget, dulu temen satu kost aku!",
                "pesan": "Sukses selalu ya kak melva!"
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "123450048",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "bang fadil keren banget, pinter, baik",
                "pesan" : "semoga bang fadil tenang di tempat yang sekaranng ya bang"
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "baik, pinter dan super duper keren ",
                "pesan" : "Tetap semangat bang"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah baik dan cantik banget",
                "pesan" : "Tetap jadi happy person ya, Kak."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "124450119",
                "asal" : "jambi",
                "alamat" : "sabah balau",
                "hobbi": "Belajar",
                "umur" : "20",
                "sosmed" : "@krnylee",
                "kesan" : "kak yulia cantik banget.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "kak elsa keren banget, apalagi pas sf",
                "pesan" : "happy terus ya kak elsa"
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kak lovia cantik banget",
                "pesan" : "Semoga selalu happy ya kak."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "bang kaleb keren banget, pinter, baik",
                "pesan" : "semoga selalu sukses ya bang"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "bang syafiq keren banget terus pinter banget",
                "pesan" : "semangat dan sukses selalu ya bang syafiq."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "bang henry super duper keren, bisa membagi waktu aklademik dan organisasi.",
                "pesan" : "Semoga yang di semogakan tersemogakan ya bang."
            },
            
      ]

        display_images_with_data(gambar_urls, data_list)
    mikfes()
    
if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_sljO0hUkuvsTc_1YFJMxqkSnIWwcfDb",
            "https://drive.google.com/uc?export=view&id=1PQMTyOytX3ydqMs7wJZxEFByqmvxFFl1",
            "https://drive.google.com/uc?export=view&id=1m1deWMiqdyE9VJMZO3vzVOjLQvFkBWwf",
            "https://drive.google.com/uc?export=view&id=1H1e5qIEdVbn5YWnV4kQkMQgt5r9KFNMR",
            "https://drive.google.com/uc?export=view&id=1IbbiH7czF16o8TNy85D0R3kWsJZRitpx",
            "https://drive.google.com/uc?export=view&id=1-SLRGklfLxPxjRY48GHuljAkL1HbqWLq",
            "https://drive.google.com/uc?export=view&id=1TUPXtQW0PG_wK_n3tQIpR9G8LF5HekFw",
            "https://drive.google.com/uc?export=view&id=10PPsoZQSeVS1bWl5S4nkxYPUCj6_4V6p",
            "https://drive.google.com/uc?export=view&id=1HEhm00V7f14YLGIVeMAo7DGbkRuBrDkN",
            "https://drive.google.com/uc?export=view&id=1Z-lrkIES_QRc3IsagpJ2bxmmpOZquPz5",
            "https://drive.google.com/uc?export=view&id=1NMZdxHRoIZzwNT4cJK33tqTX3Md73Ub5",
            "https://drive.google.com/uc?export=view&id=1pnPtbbt_Azbq6t3E6jQV_AnSfkoBNah4",
            "https://drive.google.com/uc?export=view&id=1XQS4pFXFYV_JF39wa0RkQLttSQQOTcK7",
            "https://drive.google.com/uc?export=view&id=1xtM1nMbO7_2otrdVUIkDi2nxKwMLEWYU",
            "https://drive.google.com/uc?export=view&id=1t7_V0o1Gxo5gDhaOuvWv0jNDzesoCqMZ",
            "https://drive.google.com/uc?export=view&id=1C52hlxuA9n8h6kw1IB34F9a9eqLhFxg4",
            "https://drive.google.com/uc?export=view&id=1BgQDyPndCpHSmP_rxw2bKnFSCCE31UaF",
            "https://drive.google.com/uc?export=view&id=1bbNUzgblXH7WnPXpQDnq1RhWgcoU9jBS",
            "https://drive.google.com/uc?export=view&id=1m-xqkqrD0saAtcbvmYppRNWdSSC-Vo-1",
            "https://drive.google.com/uc?export=view&id=1XCX0d7e6cmi9QhbsVeI5l727H147S0CW",
            "https://drive.google.com/uc?export=view&id=1VOuHzGbBHQ59IChv7JniXyPi__RZA1oz",
            "https://drive.google.com/uc?export=view&id=1RDCNryVlyH7LuKD2lRdpCZS4oOmzfPmU",            
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
                "kesan": "kak arini baik banget, fun banget orangnya, gasombong juga",  
                "pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kak nabila cantik banget, pinter juga",  
                "pesan":"semangat dan sehat selalu ya kak !!!"# 2
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Mancing Keributan",
                "sosmed": "@adityafq",
                "kesan": "abangnya lucu banget, baik juga",  
                "pesan":"Semangat terus bang"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya imut banget, lucu, dan baik banget",  
                "pesan":"Semoga ceria selalu dan lancar urusannya kak"# 4
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya baik dan cantik banget!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kak asila imut banget, cantik juga!!",  
                "pesan":"happy teus ya kak!"# 6
            },                      
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kak indah baik banget, lucu juga!!",  
                "pesan":"happy terus ya kak!"# 7
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "1244500106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "bang bima keren banget, ramah, dan baik",  
                "pesan":"Semangat terus bang kulaihnya semoga lancar selalu"# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"Semangat terus bang"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik lucu cantik juga",  
                "pesan":"Semangat terus dan happy terus ya kak!"# 10
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal":"Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya baik banget, ngobrol juga ga canggung  kalo sama kak yolanda",  
                "pesan":"sehat terus ya kak!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya super duper baik, eh ternyata kakanya punya kembaran dung!",  
                "pesan":"happy dan semangat terus ya kak"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"Semangat dan sehat selalu ya kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "1234500552",
                "umur": "21",
                "asal":"Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya baik banget, happy person jugaa!!",  
                "pesan":"semoga sehat selalu ya kak!"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "123450103",
                "umur": "19",
                "asal":"Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "abangnya baik banget, keren juga ",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abangnya lucu dan bener bener baik banget!!",  
                "pesan":"happy terus ya bang kuliahnya"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "abang yazid baik, keren juga!!",  
                "pesan":"Sukses selalu ya bang yazid"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "abangnya keren banget!",  
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "bang jaldi baik, lucu juga, imut lagi!",  
                "pesan":"happy terus ya bang"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "123450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakakny cantik dan imut banget!",  
                "pesan":"Semangat dan sukses terus ya kak!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak asri outfit nya bagus banget!",  
                "pesan":"happy terus ya kak!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "bang ahmad super duper keren, panutan lah pokonya",  
                "pesan":"Semangat dan selalu jaga kesehatan ya bang!"
            },                                                                          
       
            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal ()
    
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LFWtTDRbOp75yZWEDUA-VNzdAzmFiQVb",
            "https://drive.google.com/uc?export=view&id=1pbET7HXolz4DiAK7oz9WamzBZLVUEIGw",
            "https://drive.google.com/uc?export=view&id=1m8aaC9L8HHTDhYe7fA5OtkXrv47SIvFP",
            "https://drive.google.com/uc?export=view&id=1BY7Ok2uKKvvMzPJm3igXkk-ljXgxe3Wx",
            "https://drive.google.com/uc?export=view&id=1CpqW5B2SeEcRG7xjGCyTlhXX_1iZCF5G",
            "https://drive.google.com/uc?export=view&id=1D1H-73UumMke6h3Bc7eKsqAgvvghuD04",
            "https://drive.google.com/uc?export=view&id=1s8WGyh75oI7ILPiDrki_H3LbShnGKqkD",
            "https://drive.google.com/uc?export=view&id=1XwTDTTKOcnQU3BXDh7KtHyQ5TnNAnXC3",
            "https://drive.google.com/uc?export=view&id=1yw99mrs6p796OgTauehAJcMiDRwF19hc",
            "https://drive.google.com/uc?export=view&id=1lTyf_gVD9gsMWajVEzHmh8TWX6rNrLyv",
            "https://drive.google.com/uc?export=view&id=1r4U0KCKid-EQOLuJRwi0tKCuor-zZ6bZ",
            "https://drive.google.com/uc?export=view&id=1YU144IgeRQXsGwh9HsDkk0YF8lWQTgZN",
            "https://drive.google.com/uc?export=view&id=1R7jgXD_JNZLlb6uHmZ6kGL_YHJ8wlLbq",
            "https://drive.google.com/uc?export=view&id=1h18jzvBBSmAKmbN0MxkkTLXYHUY6vu7T",
            "https://drive.google.com/uc?export=view&id=1NABUc8VNezuU8irnjpo8fsfypzT_GaFF",
            "https://drive.google.com/uc?export=view&id=1xHDs9fGal7A0L6vjLVW7zbhgjRpnTdYO",
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
                "kesan": "bang haikal orangnya enjoy abiez, lucu juga",  
                "pesan":"sukses selalu ya bang hekal!!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Untung Suropati",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@risma.mustika_",
                "kesan": "Kakaknya baik dan cantik banget!!",  
                "pesan":"Semangat dan happy terus ya kak"# 2
            },
            {
                "nama": "Muhammad Hanif Zaky",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang Sumatera Barat",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngikutin drama tiktok",
                "sosmed": "@hnfdzky_",
                "kesan": "abangnya keren banget",  
                "pesan":"semangat dan sukses terus ya bang!!"# 3
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya baik banget dan ramah!!",  
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
                "kesan": "Kakaknya dan fun banget!!",  
                "pesan":"Semangat dan sehat selalu ya kak!"# 5
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "12445068",
                "umur": "21",
                "asal":"sumatera utara",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@muhvnz",
                "kesan": "abangnya baik dan keren banget, abangnya mirip ezra banget!!",  
                "pesan":"semoga kuliahnya lancar terus ya bang"# 7
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama Aqila",
                "sosmed": "snasaa._",
                "kesan": "Kak bina imut banget!!",  
                "pesan":"happy terus ya kak!"# 8
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam Itera",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak hanna orang nya bener bener ramahh dan seruuu banget!",  
                "pesan":"Semangat dan sukses terus ya kak!"# 9
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "abangnya baik dan ramah banget!!",  
                "pesan":"Sukses selalu ya bang!"# 10
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan Belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakaknya baik dan cantik banget!!",  
                "pesan":"bahagia terus ya kak!"# 11
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "cerine.ipynb",
                "kesan": "kakanya lucu dan gemesin banget!!",  
                "pesan":"happy terus ya kak"# 12
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "bang jaya baik banget, keren!!",  
                "pesan":"Sukses terus ya bang"# 13
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"ceria terus ya kak!"# 14
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin havin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "abangnya baik, kalo ngomong medok jawa banget!!",  
                "pesan":"sehat selalu ya bang"# 15
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik dan pinter banget!!",  
                "pesan":"sukses selalu kak!"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nxT-5LhXQOGlfZM3Kvsk3UJqQH3hLpHY",
            "https://drive.google.com/uc?export=view&id=1A-_e50mWn6ophoNII0UpMoKL4VjbkxmZ",
            "https://drive.google.com/uc?export=view&id=1qUDfx0p4fIuQlTdhp5ToFxFn3W6XLz__",
            "https://drive.google.com/uc?export=view&id=1jADeRoARBR5JTvZ1yQNWx6hIPK5bye-k",
            "https://drive.google.com/uc?export=view&id=1T-zneogq1poqVg9xjRVg48067zwLwgkG",
            "https://drive.google.com/uc?export=view&id=1mhgg_R2f0qLbxPLzUZcCyLhQpUfloIYK",
            "https://drive.google.com/uc?export=view&id=1adsH7l_9a-Px04SM1M9ZBIR4zytJDzSz",
            "https://drive.google.com/uc?export=view&id=1K3ms29katzf35EDkueIhQPGYw3OUzJCv",
            "https://drive.google.com/uc?export=view&id=1otccNkOZKGff0gS1hk69ajMzHqog0aVo",
            "https://drive.google.com/uc?export=view&id=182K0TgTEayl584W8V7OLlRw5nAprdyK7",
            "https://drive.google.com/uc?export=view&id=1Ox6hetAz-9ZRfWpvTR5NHQJ4T9QriGyl",
            "https://drive.google.com/uc?export=view&id=1pJey2s0GL06GysuNwxkEFRlFiY7RL59N",
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
                "kesan": "bang ihsan seru, keren, baik",  
                "pesan":"sukses selalu ya bang !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknyaa imut banget, gemess",  
                "pesan":"happy selalu ya kak!!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya lucu banget, nyambung juga kalo di ajak ngobrol",  
                "pesan":"bahagia dan sukses selalu ya kak !!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "abangnya keren banget",  
                "pesan":"semoga yang di semogakan tersemogakan!!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "kakaknya cantik dan ramah banget",  
                "pesan":"happy terus ya kak !!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "bang iqbal keren banget",  
                "pesan":"sukses terus ya bang!!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "kakaknya super cantik dan ramah banget",  
                "pesan":"semangat dan sukses selalu ya!!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya cantik dan pinter banget",  
                "pesan":"happy terus ya kak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "abangnya keren dan asik banget",  
                "pesan":"sukses selalu ya bang!!!"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "abangnya seru kalo di ajak ngobrol",  
                "pesan":"sukses terus ya bang!!!"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak nya cantik dan imut banget",  
                "pesan":"happy terus ya kak!!!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya baik dan ramah banget",  
                "pesan":"sukses selalu ya kak!!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WHw1qZI8yo7N3clLleHhJOyMgQoPuikC",
            "https://drive.google.com/uc?export=view&id=1m8X2ypJHn1WnjD4eZpRzJw9rxG_q7jmV",
            "https://drive.google.com/uc?export=view&id=18l1kAYGVb6R_FYV2nGo2m9w6ylu_2CNY",
            "https://drive.google.com/uc?export=view&id=1fF0Y0IV3O2G52PlGX5C701XYYls-6has",
            "https://drive.google.com/uc?export=view&id=1GN2g8d_TVy1zVqSbxfSCfDp_mPd03QZa",
            "https://drive.google.com/uc?export=view&id=1c22Qa9aRkt5EtA8olhDg-3GVesGlDskk",
            "https://drive.google.com/uc?export=view&id=1PT1ME2XZSDVX9zSlLM3sovKb_NjZz2Ou",
            "https://drive.google.com/uc?export=view&id=15yoZL0vm4L8GztwezUo8tv298i2v0c0-",
            "https://drive.google.com/uc?export=view&id=1PQ5BIU33KDKQ1iyPS3DD1N099boQM1Rj",
            "https://drive.google.com/uc?export=view&id=1-7kq2VT82xVMeIrOhdZbP9iP_PsAXE4q",
            "https://drive.google.com/uc?export=view&id=1HqK2Nt7cXBSlzZeRxpvwGQDZm_bkUVzn",
            "https://drive.google.com/uc?export=view&id=1YgUDz-reBIt63ICEPRolGFuP5UPkYlu2",
            "https://drive.google.com/uc?export=view&id=1cSOhhSS1AJML_veIGjh24ScZBF34gVmV",
            "https://drive.google.com/uc?export=view&id=16uinVn1ncvOKCDO2j3cEjS7tx0DDUwFe",
            "https://drive.google.com/uc?export=view&id=1zO40Bts5G2Nd13B_lb6NS3ig_MT2I-RC",
            "https://drive.google.com/uc?export=view&id=1GT8OwowD6mI9zQGrNi3ooiWAh_tUmBr-",
            "https://drive.google.com/uc?export=view&id=1VDnxHRAGcIhmD4RmoChp3LfimI7Xjn5s",
            "https://drive.google.com/uc?export=view&id=1cpa40Cebn0dd4PyhtWs8c5ujcXX95PRZ",
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
                "kesan": "kakanya keren banget, cntik banget juga",  
                "pesan":"sukses terus ya kakak!!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya asik dan super duper baik banget",  
                "pesan":"happy terus ya kakak cantik!!"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "bang labo keren banget",  
                "pesan":"happy terus ya bang labo"# 3
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak sania cantik bangettt!!",  
                "pesan":"Sukses selalu ya kak"# 4
            },
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis dan membaca",
                "sosmed": "@n1tg.-",
                "kesan": "Kakaknya ramah,baik dan cantik banget!!",  
                "pesan":"Semangat dan happy selalu ya kak!"# 5
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakaknya imut banget!",  
                "pesan":"sehat selalu ya kak!"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kak bunga cantik, ramah, lucu juga!",  
                "pesan":"Semangat dan sukses terus ya kak!"# 7
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "1244500031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "abangnya pdd abiezzz",  
                "pesan":"Sukses dan happy terus ya bang!"# 8
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"Sukses selalu ya kak!"# 9
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450014",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya imuttt banget banget !!",  
                "pesan":"happy terus ya kak!"# 10
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gaada yang tau",
                "asal":"Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa",
                "kesan": "kakaknya cantik banget, terpesona deh liatnya!!",  
                "pesan":"Semangat dan sehat selalu ya kak!"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "1244500112",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya ramah dan baik banget!",  
                "pesan":"sehat dan happy terus ya kak!"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "kakaknya cantik banget, outfit nya juga lucu banget!!",  
                "pesan":"happy terus ya kak!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "abangnya keren banget!!",  
                "pesan":"happy terus ya bang!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "bang daffa keren dan ramah banget!!",  
                "pesan":"Sehat selalu ya bang!"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Piano",
                "sosmed": "@nzlhauly",
                "kesan": "kakaknya cantik dan ramah banget!!",  
                "pesan":"happy terus ya kak"
            },
            {
                "nama": "Allisha",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "kak alisha super duper byutipul deh!!",  
                "pesan":"happy terus ya kak!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kak shafa imut banget face nya!",  
                "pesan":"sukses selalu ya kak"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1se6XEmiz0mduR3tuj0eoMWnSmvfP9YGt",
            "https://drive.google.com/uc?export=view&id=1j3GIvu_WsQZb781cfNTkcawCjGqIM9j_",
            "https://drive.google.com/uc?export=view&id=11UTF74EPvDyBam18CWgG7WY9YCUjb6Xg",
            "https://drive.google.com/uc?export=view&id=1KXkXgXnfw6qtpF6WDRhhvFESAyYHHQIq",
            "https://drive.google.com/uc?export=view&id=1SYI7tF4WdYqaOofKZdmUYmBnSocC-h94",
            "https://drive.google.com/uc?export=view&id=1YnlMONhdKMrmWDtk6GVbDLPiqwWkT-Jf",
            "https://drive.google.com/uc?export=view&id=1uxRmwygBP391xXvEEedsmbvG-PWwX06q",
            "https://drive.google.com/uc?export=view&id=1bdAFz-ZkLbjzmtYkZMoqQSeOVO-R0HSA",
            "https://drive.google.com/uc?export=view&id=1WmtnsVmJc76Gjq0BoMzjzT9dwHsjDtQZ",
            "https://drive.google.com/uc?export=view&id=1dghCmb-eC0aT0fX9c7su5dwUjGvcUCca",
            "https://drive.google.com/uc?export=view&id=1psLEfqErYllCuBKJ2xbvoOHh7rL9gGt3",
            "https://drive.google.com/uc?export=view&id=1p6cCcg0vB0BFSXzcZzf5TtO0URLA0xdT",
            "https://drive.google.com/uc?export=view&id=1H70NsVlUbwOL58sAsbBeaF-suTvzPRpU",
            "https://drive.google.com/uc?export=view&id=1PaKmkk63CWZ5jygp8QCxSx8tTwswRjJR",
            "https://drive.google.com/uc?export=view&id=1JOzfz07yF3WTT_ou9dsseIVf-2BV_zxE",
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
                "kesan": "abang kevin keren banget",  
                "pesan":"sukses selalu ya bang kevin !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D.",
                "nim": "123450046",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya cantik dan imut bangettt",  
                "pesan":"semoga kuliahnya lancar terus ya"# 2
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik ramah, fun juga orangnya!",  
                "pesan":"Sukses terus ya bang"# 3
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak ayu baik dan ramah banget!!",  
                "pesan":"happy terus ya kak!"# 4
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450121",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Motoran bareng bang bryan",
                "sosmed": "@dafaelpriza_",
                "kesan": "bang daffa keren dan ramah banget!!",  
                "pesan":"happy terus ya bang"# 5
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya imut dan ramah banget!!",  
                "pesan":"happy terus ya kak"# 6
            },                      
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jalan Pulau Damar",
                "hobbi": "Menjawab soal dari dosen dipapan tulis",
                "sosmed": "@afdal.03",
                "kesan": "abangnya baik banget!!",  
                "pesan":"happy terus ya bang"# 7
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "1244500024",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@slbnzw",
                "kesan": "Kakaknya cantik dan ramah banget!!",  
                "pesan":"Semoga lancar terus ya kak kuliahnya !"# 8
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@mridwaan_22",
                "kesan": "abangnya keren banget, ramah juga!!",  
                "pesan":"Sukses terus ya bang"# 9
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@andra.lhm",
                "kesan": "bang amdra baik banget, tidak sombong, semoga bang andra juga rajin menabung ya!!",  
                "pesan":"happy terus ya bang"# 10
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@bryantel_",
                "kesan": "abangnya keren dan jago main musik!",  
                "pesan":"keren selalu bang!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "1244500067",
                "umur": "17",
                "asal":"Semarang",
                "alamat": "Kemiling",
                "hobbi": "Ternak sapi",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "abangnya keren banget!!",  
                "pesan":"sukses terus ya bang"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya baik dan cantik banget!!",  
                "pesan":"sukses terus ya kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya imut bangett, cantik juga!",  
                "pesan":"happy terus ya kak!"
            },
            {
                "nama": "Muhammad Rafka fatih Al Ghathfaan",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Tukang Parkir",
                "sosmed": "@muhammdrafka_",
                "kesan": "abangnya seru dan nyambung kalo ngobrol!!",  
                "pesan":"Sehat selalu ya bang!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Minbak()
