"""
ui_helper.py
Design System – Buku Kating Digital TENSOR 2026
Dark Violet Theme · Clean, Minimal & Elegant
"""

import base64
import re
from io import BytesIO

import requests
import streamlit as st
from PIL import Image, ImageDraw, ImageOps

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────────────────────────────────────

_GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

/* ── Global Font (Kecuali Material Icons agar ikon sidebar tidak rusak) ── */
html, body, [class*="css"], .stMarkdown p, .stMarkdown div, h1, h2, h3, h4, label {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* ── Lindungi Material Symbols & Icons agar tidak ter-override ── */
[data-testid="stIconMaterial"], 
.material-symbols-rounded, 
.material-icons, 
[class*="material-symbols"] {
    font-family: 'Material Symbols Rounded', 'Material Symbols Outlined', 'Material Icons' !important;
    font-style: normal !important;
    font-weight: normal !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    display: inline-block !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
}

/* ── Custom Scrollbar Halus ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0c0a17; }
::-webkit-scrollbar-thumb { background: rgba(139,92,246,0.35); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(168,85,247,0.6); }

/* ── Typography & Header ── */
.g-title {
    background: linear-gradient(130deg, #ede9fe 10%, #c4b5fd 55%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    letter-spacing: -0.02em;
    text-align: center;
    margin: 0;
    line-height: 1.2;
}

.g-tag {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 14px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 600;
    color: #c4b5fd;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* ── Card Kontainer Serbaguna ── */
.g-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 20px;
    transition: border-color 0.25s ease;
}
.g-card:hover { border-color: rgba(139,92,246,0.45); }

/* ── Foto Kelompok Frame ── */
.photo-frame {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(139,92,246,0.25);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    margin: 10px 0 16px 0;
}

/* ── Efek Kaca (Glassmorphism & Sheen Hover) ── */
.glass-box {
    background: rgba(19, 15, 36, 0.75);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(168, 85, 247, 0.25);
    border-radius: 14px;
    padding: 16px;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.glass-box:hover {
    background: rgba(28, 22, 54, 0.55);
    border-color: rgba(196, 181, 253, 0.6);
    box-shadow: 
        0 12px 32px 0 rgba(139, 92, 246, 0.3),
        inset 0 0 16px 0 rgba(255, 255, 255, 0.1);
    transform: translateY(-4px) scale(1.008);
}

.glass-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 60%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.08), 
        rgba(196, 181, 253, 0.22), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 2;
}

.glass-box:hover::before {
    left: 160%;
    transition: all 0.75s ease-in-out;
}

/* ── Efek Kaca Khusus Foto Kelompok & Anggota ── */
.glass-photo-wrap {
    position: relative;
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(139, 92, 246, 0.25);
    transition: all 0.35s ease;
}

.glass-photo-wrap:hover {
    border-color: rgba(196, 181, 253, 0.65);
    box-shadow: 
        0 14px 36px 0 rgba(139, 92, 246, 0.35),
        inset 0 0 20px 0 rgba(255, 255, 255, 0.12);
    transform: translateY(-4px) scale(1.01);
}

.glass-photo-wrap img {
    transition: transform 0.4s ease;
}

.glass-photo-wrap:hover img {
    transform: scale(1.02);
}

.glass-photo-wrap::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 50%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.15), 
        rgba(216, 180, 254, 0.3), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
    z-index: 3;
}

.glass-photo-wrap:hover::before {
    left: 160%;
    transition: all 0.8s ease-in-out;
}

/* ── Jargon Banner Estetis ── */
.jargon-card {
    background: linear-gradient(135deg, rgba(28, 20, 54, 0.85) 0%, rgba(16, 12, 32, 0.95) 100%);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(168, 85, 247, 0.35);
    border-radius: 14px;
    padding: 24px 28px;
    text-align: center;
    margin: 18px 0 24px 0;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(139, 92, 246, 0.15);
}

.jargon-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -120%;
    width: 50%;
    height: 100%;
    background: linear-gradient(
        90deg, 
        transparent, 
        rgba(255, 255, 255, 0.1), 
        rgba(196, 181, 253, 0.25), 
        transparent
    );
    transform: skewX(-25deg);
    pointer-events: none;
}

.jargon-card:hover::before {
    left: 160%;
    transition: all 0.85s ease-in-out;
}

.jargon-text {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.7;
    background: linear-gradient(130deg, #ffffff 0%, #e9d5ff 40%, #c4b5fd 75%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.01em;
    font-style: italic;
    margin-top: 6px;
}

/* ══════════════════════════════════════════════
   KATING VERTICAL CARD SYSTEM
   (Normal, Elegan, Susunan Rapi Sesuai Aturan)
══════════════════════════════════════════════ */

.stImage img {
    border-radius: 10px;
    border: 1px solid rgba(139,92,246,0.2);
    display: block;
    width: 100%;
}

.logo-wrap .stImage img, .logo-wrap img {
    border: none !important;
    border-radius: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* Biodata Card di bawah foto */
.k-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 14px 16px 16px;
    margin-top: 6px;
    margin-bottom: 24px;
    transition: border-color 0.25s ease;
}
.k-card:hover { border-color: rgba(139,92,246,0.45); }

.k-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #f8fafc;
    margin: 0 0 2px 0;
    line-height: 1.3;
}

.k-nim {
    font-size: 0.78rem;
    font-family: 'Courier New', Courier, monospace;
    color: #a78bfa;
    display: block;
    margin-bottom: 8px;
    letter-spacing: 0.03em;
}

.k-sep {
    height: 1px;
    background: linear-gradient(90deg,
        rgba(139,92,246,0.05) 0%,
        rgba(139,92,246,0.3) 50%,
        rgba(139,92,246,0.05) 100%);
    margin: 8px 0 10px;
}

.k-info {
    display: flex;
    gap: 6px;
    font-size: 0.83rem;
    color: #cbd5e1;
    margin-bottom: 5px;
    line-height: 1.45;
}
.k-info-label {
    min-width: 60px;
    font-weight: 600;
    color: #c4b5fd;
    flex-shrink: 0;
}
.k-info-val { color: #f1f5f9; }

.k-q {
    margin-top: 8px;
    padding: 8px 12px;
    border-radius: 0 8px 8px 0;
    font-size: 0.82rem;
    line-height: 1.55;
    font-style: italic;
    border-left: 2px solid;
}
.k-kesan {
    border-color: #818cf8;
    background: rgba(99,102,241,0.08);
    color: #e0e7ff;
}
.k-pesan {
    border-color: #a855f7;
    background: rgba(168,85,247,0.08);
    color: #f3e8ff;
}
.k-q-label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    opacity: 0.75;
    display: block;
    margin-bottom: 3px;
    font-style: normal;
}

/* ══════════════════════════════════════════════
   ANGGOTA KELOMPOK (ABOUT US) VERTICAL CARDS
══════════════════════════════════════════════ */
.tm-card {
    background: rgba(19, 15, 36, 0.95);
    border: 1px solid rgba(139,92,246,0.2);
    border-radius: 10px;
    padding: 14px 16px;
    margin-top: 6px;
    margin-bottom: 20px;
    transition: border-color 0.25s;
}
.tm-card:hover { border-color: rgba(139,92,246,0.45); }
.tm-name { font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 4px; }
.tm-role {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 99px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.tm-lurah {
    background: rgba(234, 179, 8, 0.15);
    border: 1px solid rgba(234, 179, 8, 0.4);
    color: #fde047;
}
.tm-member {
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.35);
    color: #c4b5fd;
}
.tm-nim { font-size: 0.78rem; font-family: monospace; color: #a78bfa; display: block; margin-bottom: 8px; }

/* ── Input Box Search ── */
[data-testid="stTextInput"] input {
    background: rgba(19, 15, 36, 0.92) !important;
    border: 1px solid rgba(139,92,246,0.25) !important;
    border-radius: 10px !important;
    color: #f8fafc !important;
    padding: 8px 14px !important;
    transition: all 0.2s ease !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: rgba(168,85,247,0.6) !important;
    box-shadow: 0 0 0 3px rgba(168,85,247,0.15) !important;
}
</style>
"""

def inject_custom_css():
    st.markdown(_GLOBAL_CSS, unsafe_allow_html=True)


def extract_gdrive_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url)
    if m:
        return m.group(1)
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if m:
        return m.group(1)
    return ""


def get_fallback_avatar(name: str = "KT", size=(360, 480)) -> Image.Image:
    """Buat avatar placeholder jika foto gagal dimuat."""
    img = Image.new("RGB", size, color=(19, 15, 36))
    draw = ImageDraw.Draw(img)
    w, h = size
    draw.ellipse([w // 4, h // 4, 3 * w // 4, 3 * h // 4], fill=(35, 27, 65))
    initials = "".join(p[0].upper() for p in name.replace("*", "").split()[:2] if p) or "KT"
    tx = w // 2 - len(initials) * 6
    ty = h // 2 - 10
    draw.text((tx, ty), initials, fill=(196, 181, 253))
    return img


@st.cache_data(show_spinner=False)
def load_image(url: str, fallback_name: str = "Kating", keep_ratio: bool = False) -> Image.Image:
    """Muat gambar dari Google Drive/URL dengan caching dan fallback aman.
    Jika keep_ratio=True, gambar tidak akan dipotong (cocok untuk logo)."""
    if not url or not isinstance(url, str):
        return get_fallback_avatar(fallback_name)

    file_id = extract_gdrive_id(url)
    target = f"https://drive.google.com/uc?export=view&id={file_id}" if file_id else url

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko)"
        )
    }
    try:
        r = requests.get(target, headers=headers, timeout=6)
        if r.status_code == 200 and len(r.content) > 512:
            img = Image.open(BytesIO(r.content))
            img = ImageOps.exif_transpose(img)
            if keep_ratio:
                return img
            # Untuk foto kating: 3:4 dengan Lanczos
            img = ImageOps.fit(
                img, (360, 480), method=Image.Resampling.LANCZOS, centering=(0.5, 0.4)
            )
            return img
    except Exception:
        pass
    return get_fallback_avatar(fallback_name)


def clean_text(text: str) -> str:
    return str(text).replace("**", "").strip() if text else ""


def get_menu_styles() -> dict:
    """Style elegan untuk option_menu bernuansa dark purple dengan efek klik aktif."""
    return {
        "container": {
            "padding": "4px 8px",
            "background-color": "rgba(19, 15, 36, 0.95)",
            "border-radius": "10px",
            "border": "1px solid rgba(139,92,246,0.25)",
            "margin-bottom": "20px",
        },
        "icon": {"color": "#c4b5fd", "font-size": "16px"},
        "nav-link": {
            "font-size": "14px",
            "font-weight": "500",
            "text-align": "center",
            "padding": "8px 14px",
            "margin": "2px",
            "border-radius": "8px",
            "color": "#cbd5e1",
            "--hover-color": "rgba(139,92,246,0.15)",
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #6d28d9 0%, #8b5cf6 100%)",
            "color": "#ffffff",
            "font-weight": "600",
            "box-shadow": "0 4px 14px rgba(139, 92, 246, 0.35)",
        },
    }


def render_kating_cards(
    gambar_urls: list,
    data_list: list,
    department_title: str = "Daftar Anggota",
):
    """
    Tampilkan profil kating dalam tata letak vertikal (2 kolom grid):
    Foto di atas, biodata lengkap normal & rapi di bawah.
    """
    inject_custom_css()
    total = len(data_list)

    # Header Bar + Search Filter
    col_t, col_s = st.columns([1, 1.6])
    with col_t:
        st.markdown(
            f"""
            <div style="padding-top: 4px;">
                <span class="g-tag">🏛 {department_title}</span>
                <div style="font-size: 0.8rem; color: #94a3b8; margin-top: 3px;">
                    {total} Kating Terdata
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_s:
        query = st.text_input(
            "",
            placeholder="🔍 Cari nama, NIM, asal, atau alamat...",
            label_visibility="collapsed",
            key=f"ks_{department_title.replace(' ', '_')}",
        )

    # Filter pencarian
    filtered = []
    for i, data in enumerate(data_list):
        url = gambar_urls[i] if i < len(gambar_urls) else ""
        if not query:
            filtered.append((data, url))
        else:
            q = query.strip().lower()
            hay = " ".join([
                str(data.get("nama", "")),
                str(data.get("nim", "")),
                str(data.get("asal", "")),
                str(data.get("alamat", "")),
                str(data.get("hobbi", "")),
            ]).lower()
            if q in hay:
                filtered.append((data, url))

    if not filtered:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 40px 20px; background: rgba(19,15,36,0.6); border-radius: 12px; border: 1px dashed rgba(139,92,246,0.25); margin-top: 15px;">
                <div style="font-size: 2rem; margin-bottom: 8px;">🔍</div>
                <div style="color: #f1f5f9; font-weight: 600;">Tidak ada kating dengan kata kunci "{query}"</div>
                <div style="color: #94a3b8; font-size: 0.85rem; margin-top: 4px;">Coba gunakan nama panggilan, NIM, atau kota asal lainnya.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    if query:
        st.markdown(
            f'<div style="font-size: 0.82rem; color: #a78bfa; margin-bottom: 12px;">✦ Menampilkan {len(filtered)} dari {total} kating</div>',
            unsafe_allow_html=True,
        )

    # Grid 2 Kolom Vertikal (Foto di atas, Biodata di bawah)
    for row in range(0, len(filtered), 2):
        cols = st.columns(2, gap="large")
        for ci in range(2):
            idx = row + ci
            if idx >= len(filtered):
                break
            data, url = filtered[idx]

            nama   = clean_text(data.get("nama", "Kakak Tingkat"))
            nim    = clean_text(data.get("nim", ""))
            umur   = clean_text(data.get("umur", ""))
            asal   = clean_text(data.get("asal", ""))
            alamat = clean_text(data.get("alamat", ""))
            hobbi  = clean_text(data.get("hobbi", ""))
            sosmed = clean_text(data.get("sosmed", ""))
            kesan  = data.get("kesan", "")
            pesan  = data.get("pesan", "")

            with cols[ci]:
                # 1. Foto Vertikal di Atas
                img = load_image(url, fallback_name=nama)
                st.image(img, use_container_width=True)

                # 2. Biodata Rapi di Bawah Foto (Susunan Asli & Normal)
                def _line(label, val):
                    if val and val != "-":
                        return (
                            f'<div class="k-info">'
                            f'<span class="k-info-label">{label}:</span>'
                            f'<span class="k-info-val">{val}</span>'
                            f'</div>'
                        )
                    return ""

                info_body = (
                    _line("NIM", nim)
                    + _line("Umur", f"{umur} Tahun" if umur else "")
                    + _line("Asal", asal)
                    + _line("Alamat", alamat)
                    + _line("Hobbi", hobbi)
                    + _line("Sosmed", sosmed)
                )

                kesan_html = (
                    f'<div class="k-q k-kesan"><span class="k-q-label">Kesan:</span>"{kesan}"</div>'
                    if kesan and kesan not in ("", "-") else ""
                )
                pesan_html = (
                    f'<div class="k-q k-pesan"><span class="k-q-label">Pesan:</span>"{pesan}"</div>'
                    if pesan and pesan not in ("", "-") else ""
                )

                st.markdown(
                    f"""
                    <div class="k-card">
                        <div class="k-name">{nama}</div>
                        <div class="k-sep"></div>
                        {info_body}
                        {kesan_html}
                        {pesan_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
