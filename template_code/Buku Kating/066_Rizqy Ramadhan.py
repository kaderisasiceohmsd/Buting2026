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


# ==================================================
# KESEKJENAN
# ==================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1VK93M9nTbiHl3NkaUJ8H4r-Q_XE6R8oX",
        "https://drive.google.com/uc?export=view&id=1ZOQp3gM-aHjodjSf3zt2Z4L13c8KLLkz",
        "https://drive.google.com/uc?export=view&id=1XJhvpkT-br0AVH-Yu4m2-vSQtQt7PquN",
        "https://drive.google.com/uc?export=view&id=1gPmvCd45a_0LmBiZyxd-AacCYYYl97ka",
        "https://drive.google.com/uc?export=view&id=1YXZyhtWUazvzAKix5ibMj8tJldbTj7UV",
        "https://drive.google.com/uc?export=view&id=1WnEJwOpXt35KfnTGvtTeovYU1km5JrgT",
    ]

    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "jabatan": "Ketua Himpunan", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan sukses selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "jabatan": "Sekretaris Jenderal", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Kesekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius.", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "jabatan": "Sekretaris 1", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum.", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "jabatan": "Sekretaris 2", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken, lucuu.", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "jabatan": "Bendahara 1", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit.", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "jabatan": "Bendahara 2", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk.", "pesan": "Sukses selalu dan semangat kakkk!!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# BALEG
# ==================================================
elif menu == "Baleg":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1vdS84GGW7B8ghDlYTs6MGv1oVvpsN_Sm",
        "https://drive.google.com/uc?export=view&id=1DK_xmFDCLmIaU0-HfuKVkH19D0ii0gDQ",
        "https://drive.google.com/uc?export=view&id=1LBt1DvzTgeNaedPzXwo3An1yD5lEWXWP",
        "https://drive.google.com/uc?export=view&id=1ix-1nwOUtFPbW1YWFCeA6sV6aO2_u18Z",
        "https://drive.google.com/uc?export=view&id=1pHZuCGJv4BhGNFqN5OAjRW1FQHGlotTr",
        "https://drive.google.com/uc?export=view&id=1JnFL3hCzd5UuIY1NfLKy41l0XCV9QiMH",
        "https://drive.google.com/uc?export=view&id=1DlzGlgcCi4sDvU0cFMtddsH_jEnOMqt5",
        "https://drive.google.com/uc?export=view&id=1s2_ksQVAM_lv-4W74RnEd0AJYPhtumyU",
        "https://drive.google.com/uc?export=view&id=1wQMevgpghTaGS27PigkRBX7Rp_QnZfBZ",
        "https://drive.google.com/uc?export=view&id=1O1XM1y_ntAq_KZ9wnLsavfrRIf2-Ymmg",
        "https://drive.google.com/uc?export=view&id=14VwFQ3EM6cGKHq7HXA7CiOp_4159u2UZ",
        "https://drive.google.com/uc?export=view&id=1m8n9tVD808CWzVef-113lrA1UWqsTWtB",
        "https://drive.google.com/uc?export=view&id=1-KPWFcOTb7ex7IfZPnklBoTkuU6yrUTR", 
    ]

    data_list = [
        {"nama": "Ridho Benedictus Togi Manik", "jabatan": "Ketua Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Juesi Apridelia Saragih", "jabatan": "Sekretaris Badan Legislatif", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Dharu Cahyoaji Sasongko", "jabatan": "Kepala Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Gh Mikael Niko A S", "jabatan": "Staf Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Siti Sarifah Sumamah", "jabatan": "Staf Komisi I Legislasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Givaro Ananta", "jabatan": "Kepala Komisi II Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Afghanis Nursholehatunnisa", "jabatan": "Staf Komisi II Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Hani Qurrota Aini", "jabatan": "Staf Komisi II Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jeremia Halim", "jabatan": "Staf Komisi II Pengawasan", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Monica Patricia Tanjung", "jabatan": "Kepala Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Jona Timothy Ogatse Panjaitan", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Sekar Dini Widya Putri", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
        {"nama": "Wan Nashwa Alhasni Yuska", "jabatan": "Staf Komisi III Aspirasi dan Media Informasi", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# SENATOR
# ==================================================
elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=135LqYaR2dogYlLKneMDtC1rxO-FfYSar",
        "https://drive.google.com/uc?export=view&id=1iOKB8fOMkgmLi_XC5Vvrei_RO4Ypwh9O",
        "https://drive.google.com/uc?export=view&id=1ju685qMsF2L9Cj-h5vo2qDjRtVovr2_d",
        "https://drive.google.com/uc?export=view&id=1kiw4g0LkRUKtkrBbIg55cBB6DY5X7uZ6",
        "https://drive.google.com/uc?export=view&id=1AhmvVzwqxgnEqaK4YTanpxXupA9cg4mA",
        "https://drive.google.com/uc?export=view&id=1ge5-JnLO06Q6yfDi-My9eE8uXspgbfw_",
        "https://drive.google.com/uc?export=view&id=1V_6fhp6_RYNytGEOdg0pdY63Zd8sP1jh",
        "https://drive.google.com/uc?export=view&id=1lAM7cCfHlYd04cp7QAisM_tefc8pLAnv",
        "https://drive.google.com/uc?export=view&id=1AVedAKt_wLLgjroT70vA1d9fxXNGDX8r",
        "https://drive.google.com/uc?export=view&id=1iRN4oIwOh-wSX-FYV0WD1CSYUO7og_To",
    ]

    data_list = [
        {"nama": "Fathinah Nur Azizah", "jabatan": "Senator", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "jabatan": "Kepala Biro Kesekretariatan", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "jabatan": "Staff Biro Kesekretariatan", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "jabatan": "Kepala Biro Aspirasi dan Media Komunikasi", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "jabatan": "Staff Biro Aspirasi dan Media Komunikasi", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "jabatan": "Kepala Biro Kajian Strategis dan Propaganda", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "jabatan": "Staff Biro Kajian Strategis dan Propaganda", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN PSDA
# ==================================================
elif menu == "Departemen PSDA":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1VaJn5rnqrzbqAEGgnDp_yslqIs41ikQe",
        "https://drive.google.com/uc?export=view&id=1pULnnJpETfMhXm4Rr-ZLy45R_2cuVYsY",
        "https://drive.google.com/uc?export=view&id=1DrI7DNTRaRDspSawzT8j3GCwB8KtkRiB",
        "https://drive.google.com/uc?export=view&id=1lBuecx_CwX9Xw5fUY87_NbxlusuRlU4s",
        "https://drive.google.com/uc?export=view&id=1MQOVuTNJ2dwoQx8AVY0FwsRRCukgWSig",
        "https://drive.google.com/uc?export=view&id=1jcJqyZEvHzZOVIV-4ATj5FTfzrvlpa8e",
        "https://drive.google.com/uc?export=view&id=1OUfSVUn0LEVvpupqBfcQe9HottK8AQfr",
        "https://drive.google.com/uc?export=view&id=1AWHeggIAICnKu4oXG3pL3VBVm9tEtuKD",
        "https://drive.google.com/uc?export=view&id=1CFw8KBEdjsjEmMxztWl6cEUKh4yfUHAB",
        "https://drive.google.com/uc?export=view&id=1cDHKlKywRK7HU19fsZ-OaHI20CLAzDCn",
        "https://drive.google.com/uc?export=view&id=1Z7GspVrVlp-hrJFxLMszw7fy_gzK6V6x",
        "https://drive.google.com/uc?export=view&id=1ROn65eHppS5t4jC6JddRMCMDmc39Iqbk",
        "https://drive.google.com/uc?export=view&id=1JBdR0z93l35Blf8Ig81-DBhUCd0zHHsw",
        "https://drive.google.com/uc?export=view&id=1zGO8eQgPJFFX7YMh8E-44roUZSpcevYN",
        "https://drive.google.com/uc?export=view&id=1XwRr3DXSp_IuYySZ8uUPXIiyjaPvaFMK",
        "https://drive.google.com/uc?export=view&id=1-kLqiQ1ByImPriwmJwm9CpgbDHRdlfVk",
        "https://drive.google.com/uc?export=view&id=1BLZCo0CmKpo2dqsS4mBJZT9-9NQ2lBGR",
    ]

    data_list = [
        {"nama": "Arienta Khusnul Ananda", "jabatan": "Kepala Departemen PSDA", "nim": "123450097", "umur": "21", "asal": "Pinggir Pantai", "alamat": "Samping Kost Capo", "hobbi": "Ngerjain Anak Kader", "sosmed": "@arientakhsnl_", "kesan": "Kak Arienta orangnya baik, dan juga ramahh", "pesan": "Semoga semua keinginan kak arienta sgera tercapai"},
        {"nama": "Vany Salsabila Putri", "jabatan": "Sekretaris Departemen PSDA", "nim": "123450022", "umur": "20", "asal": "Palembang", "alamat": "Pudan Kost", "hobbi": "Pacaran", "sosmed": "@vany.salsabilaa", "kesan": "Kak vany orangnya humble, dan baik juga", "pesan": "Semoga kak vany mencapai semua keinginannya secepatnya, salam dari orang sesama palembang"},
        {"nama": "Nobel Nizam Fathirizki", "jabatan": "Kepala Divisi Kaderisasi", "nim": "123450023", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Banyak", "sosmed": "@nobelnizam", "kesan": "Bang Nobel orangnya kerenn, Tegas,dan juga baiik", "pesan": "Semoga bang nobel selalu diberi kelancaran dan kesehatan dalam segala hal."},
        {"nama": "Afriza Azmi", "jabatan": "Staf Kaderisasi", "nim": "124450110", "umur": "20", "asal": "Malang", "alamat": "Lapangan", "hobbi": "Berantem", "sosmed": "@friezazmi", "kesan": "Bang Azmi orangnya kerenn, to the point dan juga baikk", "pesan": "Semoga semua keinginan bang azmi cepat tercapaii"},
        {"nama": "Ayake Alfatih Ramadan", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "21", "asal": "Peninjauan X kota diatas solok, Sumatera Barat", "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung", "hobbi": "Cekek Ayam", "sosmed": "@ykeall", "kesan": "Bang Ayake orangnyaa humble , kerenn, Tegas dan baikk", "pesan": "Semoga bang ayake diberi kelancaran dalam segala hal dan semoga selalu diberi kesehatan"},
        {"nama": "Caesar Ozora Alrando", "jabatan": "Staf Kaderisasi", "nim": "124450017", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Pulang Kampung", "sosmed": "@caesar.oriza", "kesan": "Bang Caesar orangnya kereen, Tegas dan Humble", "pesan": "Semoga bang caesar diberi kesehatan dan kelancaran"},
        {"nama": "Euodia Meiliana Fredita", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "18", "asal": "dari mana aja boleh", "alamat": "Didalam Kamar dibalik pintu", "hobbi": "Surving", "sosmed": "@yudiameilianaa_", "kesan": "Kak Euodia orangnya seru, Tegas , dan juga baikk,", "pesan": "Semoga kak euodia selalu didekatkan hal-hal baikk"},
        {"nama": "Haikal Seventino Tamba", "jabatan": "Staf Kaderisasi", "nim": "124450032", "umur": "Tinggi Bang Azmi - 155", "asal": "Jambi", "alamat": "Belakang Pemancingan", "hobbi": "Tidur", "sosmed": "@_haikaaall", "kesan": "Bang Haikal orangnya kerenn, Tegas ,baikk, dan juga ramahh", "pesan": "Semoga bang haikal mencapai semua hal yang bang haikal inginkan"},
        {"nama": "Putri Manna Anantama Simbolon", "jabatan": "Staf Kaderisasi", "nim": "124450029", "umur": "18", "asal": "Depok", "alamat": "Oiya Cefa", "hobbi": "Jalan kaki gaboleh naik gojek", "sosmed": "@putrimannaa", "kesan": "Kak Putri orangnya baikk, humble dan juga ramah", "pesan": "Semoga semua keinginan kak putri segera terwujud"},
        {"nama": "Queenta Thifaal Nabila", "jabatan": "Staf Kaderisasi", "nim": "124450059", "umur": "19", "asal": "Rumah sakit", "alamat": "Depan pemancingan", "hobbi": "Makanin anak ayam", "sosmed": "@quenntanaabilaa", "kesan": "Kak Queenta orangnya baik, humble, dan perhatian", "pesan": "Semoga kak queenta selalu bisa mencapai keinginannya"},
        {"nama": "Desman Velius Halawa", "jabatan": "Kepala Divisi Peningkatan Mutu Anggota", "nim": "123450114", "umur": "23", "asal": "Nias", "alamat": "Airan", "hobbi": "Main musik", "sosmed": "@dsmanhal", "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk", "pesan": "Semoga bang desman selalu didekat hal-hal baikk"},
        {"nama": "Azzelya Thianandry", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450041", "umur": "19", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "pilates", "sosmed": "@azzelytn", "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali", "pesan": "Semoga semua keinginan kak azzel tercapai"},
        {"nama": "Charrlindah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450041", "umur": "21", "asal": "Jakarta Pusat", "alamat": "Cendrawasih 1", "hobbi": "Ngurus peternakan", "sosmed": "@charrlln", "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah", "pesan": "Semoga kak charlindah dikelilingi hal-hal baik"},
        {"nama": "Jeremi Marolop P. Situmorang", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450111", "umur": "17", "asal": "Jayapura", "alamat": "RS airan", "hobbi": "Nonton a day in my life", "sosmed": "@jemarrro", "kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus", "pesan": "Semoga bang jeremi bisa menggapai semua keinginannya"},
        {"nama": "Nabila Nur Azizah", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450048", "umur": "18", "asal": "Lampung", "alamat": "Barokah", "hobbi": "Main Roblox", "sosmed": "@n.bila_a", "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa", "pesan": "Semoga kak nabila mendapatkan hal-hal yang diinginkan"},
        {"nama": "Rafli Al Mansyah Tambunan", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450007", "umur": "18", "asal": "Sibolga", "alamat": "Belwis", "hobbi": "Membaca peraturan rektor", "sosmed": "@dearrfkvmfl", "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah", "pesan": "Semoga bang rafli selalu bisa mencapai semua keinginannya"},
        {"nama": "Salavi Naharani", "jabatan": "Staf Peningkatan Mutu Anggota", "nim": "124450090", "umur": "20", "asal": "Lampung Timur", "alamat": "Jatimulyo", "hobbi": "Minum air putih", "sosmed": "@afi.nhr", "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh", "pesan": "Semoga kak salavi selalu didekatkan dengan hal-hal baikk"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MIKFES
# ==================================================
elif menu == "Departemen MIKFES":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1xT8BLuHwD_RHAvrOcZO9fAXjbRykRyY0",
        "https://drive.google.com/uc?export=view&id=1XcmSaFpXc_FEXMSAcYT6CXD28sDLOBsh",
        "https://drive.google.com/uc?export=view&id=1F2znEqXw00xQ0cP-FE9z78JE-FHW5dZk",
        "https://drive.google.com/uc?export=view&id=1W1B2y8g2g78tD4_Zf8KzEsqHkH5XJ_FQ",
        "https://drive.google.com/uc?export=view&id=1QFE5wigYUr84CN6BQKxcQFBwVuOADPa3",
        "https://drive.google.com/uc?export=view&id=1N4I1ks9sW7tElu2qf2Yshp20wpqffBD0",
        "https://drive.google.com/uc?export=view&id=1RxsRT9vO5FTifsIksbo44OR4xVMpYPaP",
        "https://drive.google.com/uc?export=view&id=1KajpWl69qyIISzdj1WYfDFtnRzBqfjcf",
        "https://drive.google.com/uc?export=view&id=1g-vE252Wrx7xGs7_iVS21H38sq8VtoWY",
        "https://drive.google.com/uc?export=view&id=1DDxYsbWOMsFdAzWgTtj70AT00_ktMyBR",
        "https://drive.google.com/uc?export=view&id=1r-M0TgGCq28QE2oKr3pNomDfLIQquAKr",
        "https://drive.google.com/uc?export=view&id=1FOK8oi8OBnejx23oX028gSlMLC8lF8FV",
        "https://drive.google.com/uc?export=view&id=1fNAZfWLcnySTGOxlXevOuabbiuDYz4lE",
        "https://drive.google.com/uc?export=view&id=1fkIf8v24MY9zZ8tB8Ea1uYcqEX_TYOSL",
        "https://drive.google.com/uc?export=view&id=16BvJOJPrO2i-I9ARVVqVcDBqoPnomcaH",
        "https://drive.google.com/uc?export=view&id=1D1VaSht7sJSfZPDvjYD4k1PuiVecWy-4",
        "https://drive.google.com/uc?export=view&id=1YmsV769urEYZ_bxK-MGd7LRMOXnxdEKw",
        "https://drive.google.com/uc?export=view&id=1wl2p-rSWteWW71ik9gpSWtJwB9rKMDZ9",
        "https://drive.google.com/uc?export=view&id=1Y5RCYnmmAIqHC4UFY6obVwuM-HlHKQw5",
        "https://drive.google.com/uc?export=view&id=1_4NI5WAdgLs_i2mV79_LPjnmtOeJA1LD",
        "https://drive.google.com/uc?export=view&id=1Bhz7_lEw0ELDcfUwVLCASgAgIY5h-vpx",
        "https://drive.google.com/uc?export=view&id=1rHq4zdp8ySAXxXsPFKJFUgCzW8-UzeZb",
    ]

    data_list = [
        {"nama": "Fabio Banyu Cyto", "jabatan": "Kepala Departemen Mikfes", "nim": "123450104", "umur": "21", "asal": "Bandar Lampung", "alamat": "Kedaton Bandar Lampung", "hobbi": "Gangguin bang keya", "sosmed": "@biyokcb ig", "kesan": "...", "pesan": ""},
        {"nama": "Tanty Widiyastuti", "jabatan": "Sekretaris Departemen Mikfes", "nim": "123450094", "umur": "21", "asal": "Lampung Tengah", "alamat": "Airan Raya", "hobbi": "Nonton film", "sosmed": "@tvnty_", "kesan": "...", "pesan": ".."},
        {"nama": "Fadil Prasetyo", "jabatan": "Kepala Divisi Professional Skill Development", "nim": "123450048", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Gitar", "sosmed": "@fadilalfarizzii", "kesan": "...", "pesan": "..."},
        {"nama": "Manuel Frederika", "jabatan": "Anggota Professional Skill Development", "nim": "124450039", "umur": "20", "asal": "Batam", "alamat": "Way Kandis", "hobbi": "Gitar", "sosmed": "@manuelfdk_", "kesan": "...", "pesan": "..."},
        {"nama": "Ni Made Okta Viola Darma Putri", "jabatan": "Anggota Professional Skill Development", "nim": "124450005", "umur": "12", "asal": "Bali", "alamat": "nusa peninda", "hobbi": "menghayal", "sosmed": "@violaadrtr_", "kesan": "...", "pesan": "..."},
        {"nama": "Risa Romadona", "jabatan": "Anggota Professional Skill Development", "nim": "124450127", "umur": "20", "asal": "natar", "alamat": "natar", "hobbi": "rolling skate", "sosmed": "@risarmdna", "kesan": "..", "pesan": "..."},
        {"nama": "Vannisa Ramadhani", "jabatan": "Anggota Professional Skill Development", "nim": "1244500078", "umur": "19", "asal": "kepulauan riau", "alamat": "teluk betung", "hobbi": "nonton khw", "sosmed": "@vunnycaa", "kesan": "....", "pesan": "..."},
        {"nama": "Yulia Kristine Malau", "jabatan": "Anggota Professional Skill Development", "nim": "124450119", "umur": "20", "asal": "Jambi", "alamat": "Sabah Balau", "hobbi": "Belajar", "sosmed": "@krnylee", "kesan": "...", "pesan": "..."},
        {"nama": "Akeyla Fairuz Shafi", "jabatan": "Kepala Divisi Pusat Inovasi dan Kajian Akademik", "nim": "123450119", "umur": "21", "asal": "Depok", "alamat": "Bandar Lampung", "hobbi": "Berenang", "sosmed": "@keyashafi_", "kesan": "...", "pesan": "...."},
        {"nama": "Elsa Sitorus", "jabatan": "Anggota Pusat Inovasi dan Kajian Akademik", "nim": "124450088", "umur": "21", "asal": "Sumatera Utara", "alamat": "Pemda", "hobbi": "Sibuk", "sosmed": "@_els.a", "kesan": "...", "pesan": "......."},
        {"nama": "Fadya Izzatul 'Aini", "jabatan": "Anggota Pusat Inovasi dan Kajian Akademik", "nim": "124450062", "umur": "20", "asal": "Pringsewu", "alamat": "airan", "hobbi": "mancing", "sosmed": "@fadyaizzatul_", "kesan": "...", "pesan": "...."},
        {"nama": "Lovianora Saragih", "jabatan": "Anggota Pusat Inovasi dan Kajian Akademik", "nim": "124450105", "umur": "19", "asal": "sumatera utara", "alamat": "way huwi", "hobbi": "dengering musik", "sosmed": "@_loviaa", "kesan": "....", "pesan": "..."},
        {"nama": "M. Alsi Syahrulloh", "jabatan": "Anggota Pusat Inovasi dan Kajian Akademik", "nim": "124450092", "umur": "20", "asal": "kalianda", "alamat": "kota baru", "hobbi": "main game, tidur", "sosmed": "@aluccy_", "kesan": "...", "pesan": ".."},
        {"nama": "Sherena Florencia", "jabatan": "Anggota Pusat Inovasi dan Kajian Akademik", "nim": "124450027", "umur": "19", "asal": "Bengkulu Selatan", "alamat": "Belwis", "hobbi": "Make up", "sosmed": "@sher_renna", "kesan": "...", "pesan": "..."},
        {"nama": "Razin Hafid Hamdi", "jabatan": "Kepala Divisi Research & Development", "nim": "123450096", "umur": "21", "asal": "Padang", "alamat": "Jl. Lapas", "hobbi": "Futsal", "sosmed": "@razyn.hfd", "kesan": "...", "pesan": "..."},
        {"nama": "Faiza Try Anjani", "jabatan": "Anggota Research & Development", "nim": "124450075", "umur": "19", "asal": "Padang", "alamat": "Belwis", "hobbi": "Baca novel", "sosmed": "@faizaanjanii", "kesan": "...", "pesan": "...."},
        {"nama": "Gathfan Nadif Ali", "jabatan": "Anggota Research & Development", "nim": "124450001", "umur": "20", "asal": "Bandar Lampung", "alamat": "Rajabasa Raya", "hobbi": "Main game", "sosmed": "@gathfannadif", "kesan": "...", "pesan": ".."},
        {"nama": "Hafidz Wahdiansyah", "jabatan": "Anggota Research & Development", "nim": "124450064", "umur": "20", "asal": "Metro", "alamat": "Metro Kibang, Lampung Timur", "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)", "sosmed": "@apiszzaja", "kesan": "...", "pesan": "..."},
        {"nama": "Kaleb Filbert Istel", "jabatan": "Anggota Research & Development", "nim": "124450053", "umur": "20", "asal": "Bandar Lampung", "alamat": "Campang Raya, Sukabumi", "hobbi": "Gym, membaca, dan bermain", "sosmed": "@kelelep_comberan", "kesan": "...", "pesan": "..."},
        {"nama": "Melva Shaprina Febrianti", "jabatan": "Anggota Research & Development", "nim": "124450087", "umur": "19", "asal": "Sumatera Selatan", "alamat": "Sukarame", "hobbi": "Memasak", "sosmed": "@melva_fbrt", "kesan": "..", "pesan": ".."},
        {"nama": "Muhammad Syafiqul Falakh", "jabatan": "Anggota Research & Development", "nim": "124450099", "umur": "20", "asal": "Lampung Utara", "alamat": "Asrama TB 3", "hobbi": "Membaca", "sosmed": "@syafiqui", "kesan": "...", "pesan": "..."},
        {"nama": "Rifky Henry Ferdianto", "jabatan": "Anggota Research & Development", "nim": "124450115", "umur": "-", "asal": "Kotabumi", "alamat": "Rajabasa", "hobbi": "Ngerecokin nuel", "sosmed": "@henryferdianto", "kesan": "....", "pesan": "..."},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN EKSTERNAL
# ==================================================
elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1mahPXdn8k9Osn4Hk0LWETOu8vWsrRbUO",
        "https://drive.google.com/uc?export=view&id=1Cc6BDuF-7P-_slWA512uyOE1dh3umdZU",
        "https://drive.google.com/uc?export=view&id=1WsEypFwVzkByRviPuf9Sb_5ymFlt1SzT",
        "https://drive.google.com/uc?export=view&id=1nfFdRiwKsPc7BbCs-XgqOZSrFeoMsOMf",
        "https://drive.google.com/uc?export=view&id=1bSKuTzOjsRgtHAj5AzU7ueudusV8Hxhd",
        "https://drive.google.com/uc?export=view&id=1B9ilzH-Con1P6xAx4RDDkYc6UfBurCyw",
        "https://drive.google.com/uc?export=view&id=1PTHyBQo64IlCVVAU0cTUyQH-nNV2eO5j",
        "https://drive.google.com/uc?export=view&id=1oYBfOAGoT_Lzd-PGB2DNXW1dZsk84jw2",
        "https://drive.google.com/uc?export=view&id=1zC1pV-ip87UhQoYrlQhwAQ593UtI7Mkj",
        "https://drive.google.com/uc?export=view&id=1IyNtRkRFypYOgPEiYm9PnzRUejE5PhHZ",
        "https://drive.google.com/uc?export=view&id=1duPJsCr7mQbiQ1LcTLklVlUWJ7v5Kws6",
        "https://drive.google.com/uc?export=view&id=1ogX-KjPyj-FHY1SDDiIZRgJzzy3yLw_C",
        "https://drive.google.com/uc?export=view&id=1YNTIkzdGwhdO3zRK5Kdr-eQFjGD9nRVz",
        "https://drive.google.com/uc?export=view&id=1lO6xvJAurQtzH-cs4zgSD6r5NWFhs8uJ",
        "https://drive.google.com/uc?export=view&id=1piK7FXCNRSvop4paYLLa3VTyOz77JfKn",
        "https://drive.google.com/uc?export=view&id=1Q1PvFHHtHHMFEkEk81zVzJruN-Mq0t6x",
        "https://drive.google.com/uc?export=view&id=1rjaSPlvggtsyPlyw7wyHYIzkEdN8ScD2",
        "https://drive.google.com/uc?export=view&id=1DV3bLSFqzXrHiRe2VheIonwbwhahoPFz",
        "https://drive.google.com/uc?export=view&id=1X0PlXI4GOZ12iWwhJyrn0kgg6QjLz_zN",
        "https://drive.google.com/uc?export=view&id=1d1FhW1YP2QGTjWFm0WUFWv9GV6rFn0PG",
        "https://drive.google.com/uc?export=view&id=1XSbbVu7RLFZrwAMiMPdFvSOZHwsh9kvL",
        "https://drive.google.com/uc?export=view&id=1oyPwCOZz7xRGGw_HuplakHg6VmCNW5O-",
    ]

    data_list = [
        {"nama": "Arini Puteri Elandra", "jabatan": "Kepala Departemen Eksternal", "nim": "123450069", "umur": "21", "asal": "LAMPUNG!!!", "alamat": "Teluk Betung Selatan", "hobbi": "Nonton Kartun", "sosmed": "@elandraa_", "kesan": "Kak arienta ternyata baikkk, walau awalnya sedikit serem", "pesan": "Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."},
        {"nama": "Nabyla Sharfina", "jabatan": "Sekretaris Departemen Eksternal", "nim": "123450008", "umur": "20", "asal": "Bengkulu", "alamat": "Jalan Lapas", "hobbi": "Jalan - Jalan", "sosmed": "@bylaash", "kesan": "...", "pesan": "..."},
        {"nama": "Aditya Taufiqurrohman", "jabatan": "Kepala Divisi Pengabdian Masyarakat", "nim": "123450032", "umur": "15", "asal": "tetangga kadep", "alamat": "belwis", "hobbi": "memancing keributan", "sosmed": "@adityatfq", "kesan": "...", "pesan": "..."},
        {"nama": "Fathya Intami Gusda", "jabatan": "Staff Ahli Pengabdian Masyarakat", "nim": "123450095", "umur": "25", "asal": "Tanggerang Selatan", "alamat": "Sukarame", "hobbi": "baca wattpad", "sosmed": "@fatthyaa_", "kesan": "...", "pesan": "...."},
        {"nama": "Tarisya Hidayatul Rahmi", "jabatan": "Staff Ahli Pengabdian Masyarakat", "nim": "123450052", "umur": "-", "asal": "Luhak tanah data", "alamat": "Gerbang Barat", "hobbi": "Jadi orang baik", "sosmed": "-", "kesan": "...", "pesan": "..."},
        {"nama": "Selma Siti Aisyah", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "123450044", "umur": "20", "asal": "Lampung", "alamat": "balam", "hobbi": "jalan-jalan", "sosmed": "@selmasiti_aisyah", "kesan": "...", "pesan": "..."},
        {"nama": "Ashila Islamisahfa Vanisha", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450028", "umur": "20", "asal": "sini", "alamat": "jauh pokoknya", "hobbi": "tidur", "sosmed": "@kshigf", "kesan": "..", "pesan": "..."},
        {"nama": "Danil N Fadillah", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450103", "umur": "20", "asal": "Karawang", "alamat": "Belakang Polda", "hobbi": "Ngasih makan ikan cupang", "sosmed": "@d4niel_fdlh", "kesan": "...", "pesan": "......."},
        {"nama": "Favian Arkaanda", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450021", "umur": "20", "asal": "Swiss", "alamat": "Tanya bapas", "hobbi": "ngesen kanan", "sosmed": "@fvnnn05", "kesan": "Keren sihhh apalagi waktu cerita cerita di wawancara", "pesan": "Tetap semangat untuk kuliahnya bang"},
        {"nama": "Muhammad Fathiy Zumar Yazid", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450081", "umur": "((15≪1) & 31) ⊕ 10", "asal": "situlah", "alamat": "pohon mulia", "hobbi": "nyari hobi", "sosmed": "@zydddddd__", "kesan": "...", "pesan": "..."},
        {"nama": "Muhammad Rizaldi", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450093", "umur": "Masih muda lah", "asal": "Rahim Ibu", "alamat": "Pasar lantai 3.5", "hobbi": "tanyain sama yuder", "sosmed": "@jaldii._", "kesan": "...", "pesan": "..."},
        {"nama": "Saskia Nova Magdalena", "jabatan": "Anggota Pengabdian Masyarakat", "nim": "124450074", "umur": "20", "asal": "Banyak Begal", "alamat": "Pinggir Jalan", "hobbi": "nonton thinkerbell", "sosmed": "@snova.19", "kesan": "...", "pesan": "..."},
        {"nama": "Khoirul Muthoharoh", "jabatan": "Kepala Departemen Hubungan Luar", "nim": "123450021", "umur": "21", "asal": "Lampung Barat", "alamat": "Airan", "hobbi": "main", "sosmed": "@khoirul_muttoharoh", "kesan": "Bang azmi orang yang tegas juga", "pesan": "Terimakasih atas hal yang di berikan selama rangkaian"},
        {"nama": "Ahmad Rizky", "jabatan": "Staff Ahli Hubungan Luar", "nim": "123450050", "umur": "21", "asal": "Tangerang Selatan", "alamat": "GH", "hobbi": "ga ngapa ngapain", "sosmed": "@ahmad.rizky___", "kesan": "...", "pesan": "..."},
        {"nama": "Indah Khairunnisa", "jabatan": "Anggota Hubungan Luar", "nim": "124450077", "umur": "20", "asal": "Ampera", "alamat": "Disini aja", "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang", "sosmed": "@khaindaa_", "kesan": "...", "pesan": "..."},
        {"nama": "Bima Ekayasa", "jabatan": "Anggota Hubungan Luar", "nim": "124450106", "umur": "20", "asal": "Lampung", "alamat": "Balam", "hobbi": "berlaku humoris dan manis", "sosmed": "@bimayasa_", "kesan": "...", "pesan": "..."},
        {"nama": "Ahmad Bimo Akbar Arkana", "jabatan": "Anggota Hubungan Luar", "nim": "124450113", "umur": "20", "asal": "Tanggamus", "alamat": "Balam", "hobbi": "lihat lihat perumahan", "sosmed": "@bimo_arkana", "kesan": "..", "pesan": "..."},
        {"nama": "Adinda Deswita Maharani", "jabatan": "Anggota Hubungan Luar", "nim": "124450083", "umur": "21", "asal": "ikut kadep", "alamat": "love earth", "hobbi": "jadi idol", "sosmed": "@adindaadma", "kesan": "...", "pesan": "..."},
        {"nama": "Yollanda Agustina", "jabatan": "Anggota Hubungan Luar", "nim": "124450024", "umur": "-", "asal": "Kerangka Bawang Sebelah Barat", "alamat": "Kayu Mulya", "hobbi": "Tanya bang Henry", "sosmed": "@yollanda_agustina16", "kesan": "...", "pesan": "..."},
        {"nama": "Riska Erlis Dayu Tiara", "jabatan": "Anggota Hubungan Luar", "nim": "124450022", "umur": "20", "asal": "palembang", "alamat": "bebas", "hobbi": "ngefollow up chat", "sosmed": "@erlsriska", "kesan": "...", "pesan": "..."},
        {"nama": "Alfaya Abiyyi", "jabatan": "Anggota Hubungan Luar", "nim": "124450006", "umur": "nelson piquet", "asal": "balam", "alamat": "balam", "hobbi": "makan yang manis biar manis", "sosmed": "@alfabiyi", "kesan": "...", "pesan": "..."},
        {"nama": "Asri Meilani", "jabatan": "Anggota Hubungan Luar", "nim": "124450010", "umur": "20", "asal": "Lampung Barat", "alamat": "Korpri Raya", "hobbi": "menonton film", "sosmed": "@asrmeilani", "kesan": "....", "pesan": "..."},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN INTERNAL
# ==================================================
elif menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1077xRQCLorC3IyL_KKHTOa01aqdxoMjx",
        "https://drive.google.com/uc?export=view&id=1RpxMfjwoRuPX33ZiyHarocDziA8tSI4N",
        "https://drive.google.com/uc?export=view&id=1z9cgcbyqnl9MRnihm8gsfD56BPDR_ErW",
        "https://drive.google.com/uc?export=view&id=1SoKnEx6j16P9c6tADER-b15cJ8wwWU9X",
        "https://drive.google.com/uc?export=view&id=1wT_940adTO7ibJFJi2-BVMZdPcRyC12C",
        "https://drive.google.com/uc?export=view&id=1mQ41nQ6Zu75IbtOo9KjIf94k9Xswn7s-",
        "https://drive.google.com/uc?export=view&id=15gXdSlESbWusANfabAGgqBLvO2iZ6iXh",
        "https://drive.google.com/uc?export=view&id=1T8y84qJNVS8VZXXq0Vm_nwmhIS7-qebF",
        "https://drive.google.com/uc?export=view&id=1GvC7sOOWON00MFtu7dSEtl94-uJxGD63",
        "https://drive.google.com/uc?export=view&id=18hD8B5Pt3Al-czDlai44p7TnPiubiaA1",
        "https://drive.google.com/uc?export=view&id=1B1LKQnA1wWgpakq_smgPEGzRLkFUZSmr",
        "https://drive.google.com/uc?export=view&id=1aWx4WKPb8NvdujptAbesP7LR7jby3zpa",
        "https://drive.google.com/uc?export=view&id=1RcfHaE2f-3nBezl5sAGlqdLTQYwCtPLb",
        "https://drive.google.com/uc?export=view&id=13O358Ff6_nM5JNvSYATG0TYeYAEuIfFP",
        "https://drive.google.com/uc?export=view&id=1uLAMIXmSlbNqc3_verhvtFZUNz9KvVQ4",
        "https://drive.google.com/uc?export=view&id=1XGDa8qpvXQrapWDc4iQNANCID7XpeCeA",
    ]

    data_list = [
        {"nama": "Haikal Fransiskus Simbolon", "jabatan": "Kepala Departemen Internal", "nim": "123450123", "umur": "23", "asal": "Bengkulu", "alamat": "Belwis", "hobbi": "Merokok", "sosmed": "@haikalsbln_", "kesan": "Bang haikal orangnya seruu banget.", "pesan": "Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."},
        {"nama": "Kharisma Mustika Sari", "jabatan": "Sekretaris Departemen Internal", "nim": "123450034", "umur": "21", "asal": "Way Kanan", "alamat": "untung suropat", "hobbi": "Suka menolong orang", "sosmed": "@rismaa.mustika_", "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah", "pesan": "Semoga kak kharisma selalu dikelilingi dengan orang baik"},
        {"nama": "Hanna Grecia Sinaga", "jabatan": "Kepala Departemen Keharmonisasian", "nim": "123450038", "umur": "21", "asal": "Kisaran", "alamat": "Sukarame", "hobbi": "menyapa satpam gedung f", "sosmed": "@hanna_g_sinaga", "kesan": "Kak Hanna seru, baikk, lucu", "pesan": "Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"},
        {"nama": "Farhan Ghani", "jabatan": "Staff Ahli Keharmonisasian", "nim": "123450121", "umur": "19", "asal": "Kemiling", "alamat": "Kemiling", "hobbi": "Suka motor bukan ngabers", "sosmed": "@farhanghani", "kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus", "pesan": "Semoga bang farhan selalu diberi kelancaran dan kesehatan"},
        {"nama": "Aisyah Khairun Nissa", "jabatan": "Anggota Keharmonisasian", "nim": "124450096", "umur": "18", "asal": "Riau", "alamat": "Belwis", "hobbi": "Ngestalker in orang", "sosmed": "@aisyahkhair", "kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali", "pesan": "Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"},
        {"nama": "Cerine Sihotang", "jabatan": "Anggota Keharmonisasian", "nim": "124450049", "umur": "....", "asal": "....", "alamat": "....", "hobbi": "....", "sosmed": "@...", "kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget", "pesan": "Semoga kak cerine selalu dikelilingi orang orang baikk"},
        {"nama": "Jaya Saputra Tambak", "jabatan": "Anggota Keharmonisasian", "nim": "124450094", "umur": "22", "asal": "kisaran city", "alamat": "Pemda city", "hobbi": "Balap liar", "sosmed": "@jay_saputra_tmb", "kesan": "Bang Jaya orangnya keren, baikk, dan seru", "pesan": "Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal!"},
        {"nama": "Najla Nursyifa", "jabatan": "Anggota Keharmonisasian", "nim": "124450051", "umur": "...", "asal": "...", "alamat": "...", "hobbi": "...", "sosmed": "@...", "kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii", "pesan": "Semoga semua keinginan kak najla tercapi secepatnya"},
        {"nama": "Rozak Ramdani", "jabatan": "Anggota Keharmonisasian", "nim": "124450100", "umur": "18", "asal": "lampung selatan", "alamat": "korpri raya", "hobbi": "isengin harvin di kelas", "sosmed": "@rozakramdani__", "kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum", "pesan": "Semoga bang rozak didekatkan dengan hal-hal baik"},
        {"nama": "Teresa Christiani Purba", "jabatan": "Anggota Keharmonisasian", "nim": "124450046", "umur": "19", "asal": "riau", "alamat": "belwis", "hobbi": "masak", "sosmed": "@christiani8872", "kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh", "pesan": "Semoga kak teresa segera mendapatkan semua keinginannya"},
        {"nama": "Muhammad Hanif Dzaky Arifin", "jabatan": "Kepala Divisi Kerohanian", "nim": "123450064", "umur": "21", "asal": "Padang", "alamat": "Perumnas Way Kandis", "hobbi": "Main game fps", "sosmed": "@hndfzky_", "kesan": "Bang Hanif orangnya baikk, dan juga asikk", "pesan": "Semoga bang hanif selalu menjadi yang terbaik"},
        {"nama": "Audina Fitria", "jabatan": "Anggota Kerohanian", "nim": "124450038", "umur": "20", "asal": "sumbar", "alamat": "sukarame", "hobbi": "main ke air terjun", "sosmed": "@audinaf_03", "kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah", "pesan": "Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"},
        {"nama": "Cika Adelia Br Marbun", "jabatan": "Anggota Kerohanian", "nim": "124450050", "umur": "20", "asal": "Riau", "alamat": "Belwis", "hobbi": "Dengerin Musik", "sosmed": "@Cikamrbn", "kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk", "pesan": "Semoga semua keinginan kak cika tercapai secepatnyaaa"},
        {"nama": "Gustin H. Tampubolon", "jabatan": "Anggota Kerohanian", "nim": "124450068", "umur": "...", "asal": "...", "alamat": "...", "hobbi": "...", "sosmed": "@...", "kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh", "pesan": "Semoga kak gustin selalu didekat hal-hal baik"},
        {"nama": "Muhammad Harvinsyah", "jabatan": "Anggota Kerohanian", "nim": "124450128", "umur": "20", "asal": "Sumatera Selatan", "alamat": "Belwis", "hobbi": "Berkuda", "sosmed": "@Muhvnz_", "kesan": "Bang Harvin orangnya baiikk , dan soft spoken", "pesan": "Semoga semua keinginan bang harvin tercapai secepatnyaa"},
        {"nama": "Rafa Sabina Fahimah", "jabatan": "Anggota Kerohanian", "nim": "124450036", "umur": "20", "asal": "natar", "alamat": "natar", "hobbi": "nginep di rumah kak yollanda", "sosmed": "@snasha._", "kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh", "pesan": "Semoga kak sabina mendapatkan hal-hal baik teruss"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN SSD
# ==================================================
elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1DAWmF9gQ3rFN2k-TReeJ9HIGdtIMlIzZ",
        "https://drive.google.com/uc?export=view&id=10No86FYWYFhTfcrp_xgG_usHHDUMPPd0",
        "https://drive.google.com/uc?export=view&id=1oQxxwZt9xy6Q70YnpapP0V7rxcljwP_U",
        "https://drive.google.com/uc?export=view&id=1oBfC9Uya03L1QEei6Y10ULhG3BUcIY7_",
        "https://drive.google.com/uc?export=view&id=1nx8XPRS-lSDpG935baCrKv2vZgqfosEu",
        "https://drive.google.com/uc?export=view&id=1lb6Pyzw_Di9PUuhA6bkGMbvSqHKm2_fX",
        "https://drive.google.com/uc?export=view&id=1GHdMRoSvgIjDt35S3O3gEqXjuBs4YJXc",
        "https://drive.google.com/uc?export=view&id=1IYR5vqJO-T76lKRekIT4h_lsMETfWkwL",
        "https://drive.google.com/uc?export=view&id=1jHvMGkvRzlHsITSXsmpNfizl3h7bJGL0",
        "https://drive.google.com/uc?export=view&id=1w7je9FFv3WGn8eYiQ4dB_1E0mBlShI9U",
        "https://drive.google.com/uc?export=view&id=1ZOD4M7H4P4UMsVb-xt6q5GPUUH-F_3vX",
        "https://drive.google.com/uc?export=view&id=1Nc2VhJ49h8YN0Xe0iEZ0yKrjoi5a9Ook",
    ]

    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "jabatan": "Kepala Departemen SSD", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Jualan", "sosmed": "@ihsan.myusuf", "kesan": "...", "pesan": "..."},
        {"nama": "Hanifah Inaya Sani", "jabatan": "Sekretaris Departemen SSD", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "...", "pesan": "..."},
        {"nama": "Afifah Fauziah", "jabatan": "Kepala Divisi Kemitraan", "nim": "123450002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton marvel", "sosmed": "@fifah.zy", "kesan": "...", "pesan": "..."},
        {"nama": "Hasan Nur Ramadhan", "jabatan": "Anggota Kemitraan", "nim": "124450013", "umur": "25", "asal": "Lampung Tengah", "alamat": "Sebelah kostan Ayake", "hobbi": "Nonton YouTube", "sosmed": "@hasan.ramdhan08", "kesan": "...", "pesan": "..."},
        {"nama": "Layina Ropiqo", "jabatan": "Anggota Kemitraan", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Nonton dracin", "sosmed": "@lay.inr_", "kesan": "...", "pesan": "..."},
        {"nama": "Mochammad Iqbal Az-zahir", "jabatan": "Anggota Kemitraan", "nim": "124450052", "umur": "20", "asal": "Bekasi", "alamat": "Natar", "hobbi": "Nonton drakor", "sosmed": "@iqbalazzahir_", "kesan": "....", "pesan": "..."},
        {"nama": "Talitha Justine", "jabatan": "Anggota Kemitraan", "nim": "124450076", "umur": "19", "asal": "Jakarta", "alamat": "Pemda", "hobbi": "Nonton", "sosmed": "...", "kesan": "...", "pesan": ".."},
        {"nama": "Anadia Carana", "jabatan": "Kepala Divisi Kewirausahaan", "nim": "123450019", "umur": "21", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@anadiacrn_", "kesan": "...", "pesan": "..."},
        {"nama": "Abdilah Fikri Alpome", "jabatan": "Staf Ahli Kewirausahaan", "nim": "123450062", "umur": "21", "asal": "Baturaja, Sumatera Selatan", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@pomest__", "kesan": "...", "pesan": ".."},
        {"nama": "Afdhal Rahmad Setiawan", "jabatan": "Anggota Kewirausahaan", "nim": "124450008", "umur": "20", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Fishing", "sosmed": "@dhalsetiawan", "kesan": "...", "pesan": "......."},
        {"nama": "Anggun Nita", "jabatan": "Anggota Kewirausahaan", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunnitaaa_", "kesan": "..", "pesan": "..."},
        {"nama": "Della Anisa Fitri", "jabatan": "Anggota Kewirausahaan", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi gak punya hobi", "sosmed": "@dellaansaftr", "kesan": "kakanya cantik dan cute", "pesan": "Semangat buat kuliahnya, sampai lulus"},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MEDKRAF
# ==================================================
elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1H4xJ6bAIcqVHbw9v7LDxCu_XYAqYkNx6",
        "https://drive.google.com/uc?export=view&id=1nwAHwtnJS-7PYeuID8ekF-Xh-S570jx0",
        "https://drive.google.com/uc?export=view&id=1k8r6AXMP2v5YKH2zO5i8pwdLoTmDDtj_",
        "https://drive.google.com/uc?export=view&id=12JvUhziFx3OkSoTDxVaEhlnuMLcIrsGi",
        "https://drive.google.com/uc?export=view&id=1S-ZS_T726leoOrMSgpnP1i3ZYRROPeD_",
        "https://drive.google.com/uc?export=view&id=1ukcj_8UXDzCSy9kJp_nuCtBhN6-GX2mH",
        "https://drive.google.com/uc?export=view&id=1eD9m3X0Jt8NnuKdm17YjXXmpZy9Etxuv",
        "https://drive.google.com/uc?export=view&id=1L9stpCgAD838ljQHDg6qrjUjRdfNCD4G",
        "https://drive.google.com/uc?export=view&id=1Xoe1ooDihg_cWFynRKfgi46a5GDx3PFo",
        "https://drive.google.com/uc?export=view&id=1GARg2ycsJTh5rW4qR_ijXJbawccehJyk",
        "https://drive.google.com/uc?export=view&id=1Q6koQdG6dHXau7pE25j0x0kG31nocwPp",
        "https://drive.google.com/uc?export=view&id=1ZmfpMBwlMEmWeZ-9NyspXzPB6gTpqskL",
        "https://drive.google.com/uc?export=view&id=19TVQMduvpZkRUh0oajdP-cv22eNFc6HW",
        "https://drive.google.com/uc?export=view&id=1WHjzOU27ojepHU1Ju8ELUdEz2HKRre1C",
        "https://drive.google.com/uc?export=view&id=1YJNRGgQCLiTksJHTLSt7N6dZpvRnEeUl",
        "https://drive.google.com/uc?export=view&id=1TWCBMRuME-z3baBWVL8KtCI0dDwS8gZP",
        "https://drive.google.com/uc?export=view&id=1YdmIni_COiuWGHeZz6uCCaslm6L4DpQt",
        "https://drive.google.com/uc?export=view&id=1kEiNRomfsl9b9oGMbzWKlxXJRi1lCYrA",
    ]

    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "jabatan": "Kepala Departemen Medraf", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi, Jati Agung, Lampung Selatan", "hobbi": "Mendengarkan Musik", "sosmed": "@naylasalsabilaa._", "kesan": "..", "pesan": "..."},
        {"nama": "Donna Maya Puspita", "jabatan": "Sekretaris Departemen Medkraf", "nim": "123450028", "umur": "21", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Listening to music", "sosmed": "@donnamaya.p", "kesan": "...", "pesan": "Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"},
        {"nama": "Labo John Noel Napitupulu", "jabatan": "Kepala Divisi Dokumentasi", "nim": "123450037", "umur": "20", "asal": "Medan, Palembang, Jakpus", "alamat": "Belwis", "hobbi": "Motoran", "sosmed": "@noerruuu", "kesan": "...", "pesan": "..."},
        {"nama": "Anash Tasya Ausyaqila", "jabatan": "Anggota Dokumentasi", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Halim", "hobbi": "Nonton", "sosmed": "@anshtsyaaql", "kesan": "...", "pesan": "..."},
        {"nama": "Felisya Nabila Nugroho", "jabatan": "Anggota Dokumentasi", "nim": "124450104", "umur": "19", "asal": "Lampung Timur", "alamat": "Kota Baru", "hobbi": "Gangguin Anash&Razan, jail di grup", "sosmed": "@felisyanbl__", "kesan": "...", "pesan": "..."},
        {"nama": "Muhammad Razan Maulana Pratama", "jabatan": "Anggota Dokumentasi", "nim": "124450031", "umur": "21", "asal": "Jawa Barat", "alamat": "Korpri", "hobbi": "Poto orang", "sosmed": "@muh_razan_", "kesan": "...", "pesan": "..."},
        {"nama": "Sania Dwi Ayu Lestari", "jabatan": "Kepala Divisi Media dan Konten Spesialis", "nim": "124450086", "umur": "21", "asal": "Karawang", "alamat": "Airan Raya", "hobbi": "Nonton netflix", "sosmed": "@saniayyllstr", "kesan": "..", "pesan": "..."},
        {"nama": "Allisha", "jabatan": "Anggota Media dan Konten Spesialis", "nim": "124450019", "umur": "16", "asal": "Kayangan", "alamat": "Heaven", "hobbi": "Mancing", "sosmed": "@aallishaa.a", "kesan": "...", "pesan": "...."},
        {"nama": "Alya Ramadhanti", "jabatan": "Anggota Media dan Konten Spesialis", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Jalan jalan", "sosmed": "@alya.rmdhnti", "kesan": "...", "pesan": "..."},
        {"nama": "Bunga Clarisa Sefa", "jabatan": "Anggota Media dan Konten Spesialis", "nim": "124450097", "umur": "20", "asal": "Lampung Selatan", "alamat": "Lampung Selatan", "hobbi": "Belajar", "sosmed": "@bungaclrssf", "kesan": "kakaaa cantik banget aku suka ngeliatnya", "pesan": "......."},
        {"nama": "Difanya Husakina", "jabatan": "Anggota Media dan Konten Spesialis", "nim": "124450043", "umur": "20", "asal": "Pagar Alam", "alamat": "Airan Raya", "hobbi": "Membaca Alquran", "sosmed": "@difanyhsa_", "kesan": "...", "pesan": ".."},
        {"nama": "Nazlah Auliya", "jabatan": "Anggota Media dan Konten Spesialis", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Berenang", "sosmed": "@nzlhauly_", "kesan": "...", "pesan": ".."},
        {"nama": "Raihana Adelia Putri", "jabatan": "Kepala Divisi Visual Design", "nim": "123450041", "umur": "20", "asal": "Lampung Tengah", "alamat": "Aira Raya 1", "hobbi": "Menulis, membaca", "sosmed": "@n1tg._", "kesan": "...", "pesan": "..."},
        {"nama": "Daffa Kharisma Adzana", "jabatan": "Anggota Visual Design", "nim": "124450061", "umur": "21", "asal": "Surabaya", "alamat": "Sukarame", "hobbi": "-", "sosmed": "@daffascript", "kesan": "..", "pesan": ".."},
        {"nama": "Edsel Adya Pradipta", "jabatan": "Anggota Visual Design", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Nonton Anime", "sosmed": "@edsel_0712", "kesan": "...", "pesan": "..."},
        {"nama": "Lucia Advencia Rachel Nainggolan", "jabatan": "Anggota Visual Design", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Tidur", "sosmed": "@luciarachel_", "kesan": "...", "pesan": "..."},
        {"nama": "Shafa Delaila Azzahra", "jabatan": "Anggota Visual Design", "nim": "124450124", "umur": "20", "asal": "Lampung Tengah", "alamat": "Perum Pemda", "hobbi": "Melukis dan menulis", "sosmed": "@_shaazzh", "kesan": "...", "pesan": "..."},
        {"nama": "Zannuba Arifah Ilman", "jabatan": "Anggota Visual Design", "nim": "124450112", "umur": "18", "asal": "Lampung Timur", "alamat": "Rajabasa", "hobbi": "Bengong", "sosmed": "@xifasky", "kesan": "..", "pesan": ".."},
    ]

    display_images_with_data(gambar_urls, data_list)


# ==================================================
# DEPARTEMEN MINBAK
# ==================================================
elif menu == "Departemen Minbak":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1uGFo7j5vN0D--aYZytwFJBM2LJvRnXb3",
        "https://drive.google.com/uc?export=view&id=1YacyRo73zqcFW0sxpIGypla668E-6Fqy",
        "https://drive.google.com/uc?export=view&id=1I5hzGu7fNRNz-tqfnSesBbLNee-V2U3-",
        "https://drive.google.com/uc?export=view&id=1K2cZgvda4GUrNpWyoYmvnXyL9JXfyKwE",
        "https://drive.google.com/uc?export=view&id=1FtKq5ltlB96IyD5NOJF8DsxLRmKAC6rB",
        "https://drive.google.com/uc?export=view&id=1VxpKuSB9zI2jUc2jEx6RkbdSBXPOj-fz",
        "https://drive.google.com/uc?export=view&id=1M-RoXwGCpJBWoxejh_k3WGQREuXueuGc",
        "https://drive.google.com/uc?export=view&id=1TfuyVdZboEVAo0Hzly5ZEuzo4HlvcACf",
        "https://drive.google.com/uc?export=view&id=1zy8s0C_xVDFF-0c6BK7dIFqHQI5WLGse",
        "https://drive.google.com/uc?export=view&id=16yK-jjV1na6TYejJBKkV-YQT7mWUPObA",
        "https://drive.google.com/uc?export=view&id=12nQT2gnq6olr5uYu2dMT5TJjm5tP3Ebw",
        "https://drive.google.com/uc?export=view&id=1GG0_JarsUu1l0ebHtcz0xmFE6ZOi9ba4",
        "https://drive.google.com/uc?export=view&id=15z3w1H6cRb7T8mEKhR6XQdmQrLj4cEwR",
        "https://drive.google.com/uc?export=view&id=1xV0f8LFG5OQB1_C8jTWeTzYkwZIsd-R_",
        "https://drive.google.com/uc?export=view&id=173tB_eVRb8BleIAId8rqocMoXL_IeLGq",
    ]

    data_list = [
        {"nama": "Kevin Antonio Junior", "jabatan": "Kepala Departemen Minat & Bakat", "nim": "123450109", "umur": "20", "asal": "Maluku", "alamat": "Panjang", "hobbi": "Menari", "sosmed": "@kevinaj__", "kesan": "Bang Kevin orangnya asik dan lucuu parah.", "pesan": "Semangat terus kuliahnya bangg, dan sehat selalu ya bang"},
        {"nama": "Gusti Putu Ferazka Dhiyamika", "jabatan": "Sekretaris Departemen Minat & Bakat", "nim": "123450046", "umur": "21", "asal": "Lampung Utara", "alamat": "Way Halim", "hobbi": "Mendaki", "sosmed": "@ferazkaa", "kesan": "Kak Ferazka orangnya lucuuu parah, dan selalu ngajakin muncak.", "pesan": "semangat terus kuliahnya ya kak, dan semoga kita bisa muncak kak!!"},
        {"nama": "Ali Aristo Muthahhari Parisi", "jabatan": "Kepala Divisi Manajemen Aktivitas dan Kompetisi", "nim": "123450088", "umur": "21", "asal": "Lampung Timur", "alamat": "Gang Sakum Belwis", "hobbi": "Bawa makanan dari Luar", "sosmed": "ali_parisi3", "kesan": "Bang Ali orangnya baik, seru dan soft spoken.", "pesan": "semangat terus kuliahnya bang !!!"},
        {"nama": "Ayu Andriani Parlina Wati", "jabatan": "Anggota Manajemen Aktivitas dan Kompetisi", "nim": "123450025", "umur": "20", "asal": "Jombang", "alamat": "Jatiagung", "hobbi": "Jalan-jalan nyari mangsa", "sosmed": "@me._kael", "kesan": "Kak Ayu orangnya baik dan humble parah", "pesan": "semangat terus kuliahnnya kak!!"},
        {"nama": "Dafa Elpriza", "jabatan": "Anggota Manajemen Aktivitas dan Kompetisi", "nim": "124450131", "umur": "21", "asal": "Bekasi", "alamat": "Way Kandis", "hobbi": "Mancing", "sosmed": "@dafaelpriza_", "kesan": "Bang Dafa orangnya baik dan asik banget.", "pesan": "Semangat terus ya bang kuliahnya, dan sehat selalu ya bang, terimakasih bang"},
        {"nama": "Salsabila Nazwa Putri", "jabatan": "Anggota Manajemen Aktivitas dan Kompetisi", "nim": "124450002", "umur": "20", "asal": "Metro", "alamat": "Korpri", "hobbi": "Pulang Kampung", "sosmed": "@slbnzw_", "kesan": "Kak nazwa orangnya baik dan soft spoken banget.", "pesan": "Semoga kedepannya kakak diberi kelancaran dalam segala hal."},
        {"nama": "Muhammad Afdal Lutfi", "jabatan": "Anggota Manajemen Aktivitas dan Kompetisi", "nim": "124450047", "umur": "19", "asal": "Lampung Tengah", "alamat": "Jln. Pulau Damar", "hobbi": "Surving", "sosmed": "@afdall.03", "kesan": "Bang afdal orangnya lucu dan seruuu banget.", "pesan": "Semangat terus ya bang kuliahnya, dan sehat selalu yaa bang"},
        {"nama": "Juwita Sari", "jabatan": "Anggota Manajemen Aktivitas dan Kompetisi", "nim": "124450066", "umur": "19", "asal": "Lampung Barat", "alamat": "Pemda", "hobbi": "Liat Bila nulis", "sosmed": "@ju.juwitaaa_", "kesan": "Kak juwita orangnya lucu dan baik bangett", "pesan": "Semoga kedepannya kakak diberi kelancaran dalam segala hal."},
        {"nama": "Muhammad Ridwan", "jabatan": "Kepala Divisi Manajemen Minat dan Bakat", "nim": "123450091", "umur": "21", "asal": "Lampung Tengah", "alamat": "Belwis", "hobbi": "Nontonin Fadyl Badminton", "sosmed": "@mridwaan_22", "kesan": "Bang ridwan orangnya asik dan seru banget, my mentor badminton", "pesan": "semangat terus kuliahnya ya bang !!!"},
        {"nama": "Andra Ilham Bintang", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "124450060", "umur": "18", "asal": "Sumatera Selatan", "alamat": "Kota Baru", "hobbi": "Nonton Drama Korea", "sosmed": "@andra.lhm", "kesan": "BAng andra orangnya lucuu dan seruuu banget", "pesan": "semangat terus kuliahnya yaa bang !!!"},
        {"nama": "Bryan Paskah Telaumbanua", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "124450003", "umur": "20", "asal": "Nias", "alamat": "Belwis", "hobbi": "Yoga", "sosmed": "@bryantel_", "kesan": "Bang Bryan orangnya soft spoken dan humble banget", "pesan": "semangat terus kuliahnya ya bangg !!!"},
        {"nama": "Indah Julia Mawar Pratiwi", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "124450055", "umur": "20", "asal": "Pringsewu", "alamat": "Airan", "hobbi": "Main", "sosmed": "@sekardnwp", "kesan": "Kak indah orangnya asik dan baik bangetttt", "pesan": "semangat terus kuliahnya yaa kak!!!"},
        {"nama": "Jacinda Kesya Alvara", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "....", "umur": "..", "asal": "...", "alamat": "....", "hobbi": "...", "sosmed": "@....", "kesan": "Kakak ini asik saya suka belajar dengan dia", "pesan": "semangat terus kuliahnya kakak !!!"},
        {"nama": "Muhammad Rafka Fatih Al Ghathfaan", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "124450089", "umur": "20", "asal": "Padang", "alamat": "Kota Baru", "hobbi": "Bangun Pagi", "sosmed": "@muhammdrafka_", "kesan": "Bang rafka orangnya baik dan humble banget", "pesan": "semangat terus kuliahnya Bang !!!"},
        {"nama": "Ghiyats Thabularasa Meardhy", "jabatan": "Anggota Manajemen Minat dan Bakat", "nim": "124", "umur": "...", "asal": "...", "alamat": "....", "hobbi": "...", "sosmed": "....", "kesan": "....", "pesan": "Semangattt bang bangg jadi pj game nyaaa hihi"},
    ]

    display_images_with_data(gambar_urls, data_list)
