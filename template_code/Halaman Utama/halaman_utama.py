# Halaman Utama/halaman_utama.py
import streamlit as st
from streamlit_option_menu import option_menu
import html

# ─── Import dari utils.py ───
from utils import load_image, image_data_uri


# ============================================================
# 🎨 CUSTOM CSS HALAMAN UTAMA (FIXED & RESPONSIVE)
# ============================================================
HALAMAN_UTAMA_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #222222;
}

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, rgba(217,195,163,0.18) 0%, transparent 50%),
        linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
    background-attachment: fixed;
}

/* --- TITLE & HEADER --- */
.main-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 3.6em !important;
    letter-spacing: 1px;
    margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 2px 20px rgba(112,28,35,0.15);
    position: relative;
    display: inline-block;
    width: 100%;
}
.main-title::after {
    content: '';
    display: block;
    width: 90px;
    height: 3px;
    margin: 14px auto 0;
    background: linear-gradient(90deg, transparent, #701c23, transparent);
    border-radius: 3px;
}
.main-subtitle {
    text-align: center;
    font-family: 'Inter', sans-serif;
    color: #6b5a52;
    font-weight: 500;
    font-size: 1.15em !important;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 30px;
    margin-top: 6px;
}
.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    color: #701c23;
    font-weight: 700;
    font-size: 1.9em;
    margin-top: 45px;
    margin-bottom: 30px;
    position: relative;
    display: block;
}
.section-title::before,
.section-title::after {
    content: '✦';
    color: #d9c3a3;
    margin: 0 18px;
    font-size: 0.7em;
    vertical-align: middle;
}

.content-box {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%);
    padding: 38px 42px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(112,28,35,0.07);
    border: 1px solid rgba(217,195,163,0.55);
    margin-bottom: 38px;
    text-align: justify;
    line-height: 1.95;
    font-size: 15.5px;
    color: #3a2f2b;
    position: relative;
    overflow: hidden;
}
.content-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.content-box b {
    color: #701c23;
    font-weight: 700;
    letter-spacing: 0.2px;
}

/* --- HOME PHOTO CARD --- */
.photo-card {
    position: relative;
    overflow: hidden;
    border-radius: 16px;
    border: 1px solid rgba(217,195,163,0.7);
    margin-bottom: 22px;
    height: 210px;
    background-color: #ffffff;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}
.photo-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(112,28,35,0.22);
}
.photo-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.7s ease;
}
.photo-card:hover img { transform: scale(1.1); }
.photo-card .overlay {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    background: linear-gradient(to top, rgba(112,28,35,0.97), transparent);
    color: #ffffff;
    padding: 26px 14px 14px 14px;
    opacity: 0;
    text-align: center;
    transition: opacity 0.4s ease;
}
.photo-card:hover .overlay { opacity: 1; }
.photo-card .overlay-title { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 15px; }
.photo-card .overlay-desc { font-size: 11.5px; }

/* --- FLIP CARD UTAMA (Tengah & Responsive) --- */
.flip-card {
    background-color: transparent;
    width: 100%;
    max-width: 280px; /* Diperkecil agar tidak terlalu lebar */
    height: 360px;
    perspective: 1600px;
    margin: 0 auto 24px auto; /* Center otomatis */
    position: relative;
}
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s cubic-bezier(0.4, 0.2, 0.2, 1);
    transform-style: preserve-3d;
    border-radius: 18px;
    box-shadow: 0 10px 28px rgba(112,28,35,0.10);
}
.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center; /* Konten ke tengah vertikal */
    align-items: center;     /* Konten ke tengah horizontal */
}
.flip-card-front {
    background: linear-gradient(165deg, #ffffff 0%, #fdf9f3 60%, #f6efe4 100%);
    color: #701c23;
    padding: 20px 16px;
    border: 1px solid rgba(217,195,163,0.75);
}
.flip-card-front .photo-frame {
    position: relative;
    width: 130px; /* Ukuran foto proporsional */
    height: 160px;
    margin-bottom: 14px;
    border-radius: 12px;
    padding: 4px;
    background: linear-gradient(135deg, #701c23 0%, #d9c3a3 50%, #701c23 100%);
    box-shadow: 0 8px 22px rgba(112,28,35,0.26);
}
.flip-card-front .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 9px;
    display: block;
}
.flip-card-front h4 {
    margin: 2px 0 6px 0;
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: #701c23;
    font-size: 16px;
    letter-spacing: 0.3px;
    line-height: 1.25;
    text-align: center; /* Nama center */
    width: 100%;
}
.flip-card-front .role-badge {
    display: inline-block;
    padding: 4px 14px;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    border-radius: 999px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 100%);
    color: #f4f0eb;
    margin-bottom: 4px;
}
.flip-card-front .role-badge.anggota {
    background: linear-gradient(135deg, #d9c3a3 0%, #c4a882 100%);
    color: #4e1318;
}
.flip-card-front .flip-hint {
    font-size: 9px;
    color: #a89790;
    text-transform: uppercase;
    margin-top: 5px;
}

.flip-card-back {
    background: linear-gradient(150deg, #701c23 0%, #4e1318 100%);
    color: #ffffff;
    transform: rotateY(180deg);
    text-align: left;
    padding: 20px;
    justify-content: center;
}
.flip-card-back h4 {
    font-family: 'Playfair Display', serif;
    color: #d9c3a3;
    font-weight: 700;
    margin: 0 0 10px 0;
    font-size: 17px;
    width: 100%;
    text-align: center;
}
.flip-card-back .back-role {
    font-size: 10px;
    font-weight: 700;
    color: #f4f0eb;
    opacity: 0.85;
    margin-bottom: 15px;
    width: 100%;
    text-align: center;
}
.flip-card-back .divider {
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, transparent, #d9c3a3, transparent);
    margin-bottom: 15px;
}
.flip-card-back p {
    font-size: 12px;
    margin: 0 0 8px 0;
    line-height: 1.4;
    color: rgba(255,255,255,0.95);
    padding: 8px 12px;
    border-radius: 8px;
    background: rgba(255,255,255,0.05);
    border-left: 2px solid #d9c3a3;
    width: 100%;
}
.flip-card-back .label {
    display: block;
    font-weight: 700;
    color: #d9c3a3;
    text-transform: uppercase;
    font-size: 9px;
    margin-bottom: 2px;
}

/* --- CSS KHUSUS MENTOR --- */
.mentor-flip-card {
    height: 400px;
    max-width: 320px; /* Sedikit lebih besar dari anggota */
}
.mentor-flip-card .flip-card-front {
    border: 2px solid #b8912e;
    background: linear-gradient(165deg, #fffdf5 0%, #fdf4e3 100%);
}
.mentor-flip-card .photo-frame {
    width: 150px;
    height: 190px;
    background: linear-gradient(135deg, #b8912e 0%, #e8c874 50%, #b8912e 100%);
}
.mentor-flip-card h4 {
    font-size: 19px;
    color: #b8912e;
}
.mentor-flip-card .role-badge {
    background: linear-gradient(135deg, #b8912e, #e8c874);
    color: #4e1318;
    font-size: 11px;
    padding: 6px 18px;
}
.mentor-flip-card .flip-card-back {
    background: linear-gradient(150deg, #b8912e 0%, #8a6a1f 100%);
}
.mentor-flip-card .flip-card-back h4 { color: #ffffff; }
.mentor-flip-card .flip-card-back .label { color: #ffffff; }
.mentor-flip-card .flip-card-back p { border-left-color: #ffffff; }

/* --- HERO IMAGE --- */
.hero-image-wrapper {
    position: relative;
    max-width: 1000px;
    margin: 0 auto 28px auto;
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(217,195,163,0.65);
}
.hero-image-wrapper img {
    width: 100%;
    height: 380px;
    object-fit: cover;
    display: block;
}
.hero-image-wrapper .hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(112,28,35,0.85) 0%, transparent 75%);
    pointer-events: none;
}
.hero-image-wrapper .hero-caption {
    position: absolute;
    bottom: 26px; left: 30px; right: 30px; color: #f4f0eb;
}
.hero-image-wrapper .hero-badge {
    display: inline-block;
    padding: 4px 14px;
    background: rgba(244,240,235,0.15);
    backdrop-filter: blur(8px);
    border-radius: 999px;
    font-size: 10px;
    font-weight: 700;
    color: #f4f0eb;
    margin-bottom: 10px;
}
.hero-image-wrapper .hero-caption h3 {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    margin: 0;
    color: #ffffff;
}
.hero-image-wrapper .hero-caption p {
    font-size: 12.5px;
    margin: 6px 0 0 0;
    color: rgba(244,240,235,0.9);
}
</style>
"""

st.markdown(HALAMAN_UTAMA_CSS, unsafe_allow_html=True)


# ============================================================
# HERO IMAGE HELPER
# ============================================================
def hero_image(url, title="Satu Tim, Satu Cerita", subtitle="Momen kebersamaan."):
    img_src = image_data_uri(url, max_dim=1200, quality=85)
    if not img_src:
        return
    st.markdown(f"""
        <div class="hero-image-wrapper">
            <img src="{img_src}" alt="{html.escape(title, quote=True)}">
            <div class="hero-overlay"></div>
            <div class="hero-caption">
                <div class="hero-badge">✦ Keluarga Poisson ✦</div>
                <h3>{html.escape(title)}</h3>
                <p>{html.escape(subtitle)}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# HEADER & LOGO
# ============================================================
st.markdown("""
    <div>
        <h1 class='main-title'>WEBSITE KATING</h1>
        <p class='main-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
    </div>
""", unsafe_allow_html=True)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"

def layout_logo(url):
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        img = load_image(url)
        if img: st.image(img, use_container_width=True)

layout_logo(url)
st.write("")
layout_logo(url1)
st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================
menu = option_menu(
    menu_title=None, options=["Home", "About Us"], icons=["house-door", "hand-index"], default_index=0, orientation="horizontal",
    styles={
        "container": {"background-color": "rgba(255,255,255,0.85)", "border-radius": "14px", "border": "1px solid rgba(217,195,163,0.6)", "margin-bottom": "38px"},
        "nav-link-selected": {"background": "linear-gradient(135deg, #701c23 0%, #a8323d 100%)", "color": "#ffffff"}
    }
)


# ============================================================
# HOME PAGE
# ============================================================
if menu == "Home":
    st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)
    hero_image("https://drive.google.com/uc?export=view&id=1b38uX_AFwdNc3-03NWQPcOX-TIOdxDee")

    st.markdown("""
        <div class='content-box'>
            <b>Selamat datang di portal resmi kelompok Poisson!</b><br><br>
            Kelompok kami merupakan wadah kolaborasi, kebersamaan, dan dedikasi tinggi dalam menjalani rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-title' style='font-size:22px;'>Dokumentasi Kegiatan Poisson</h3>", unsafe_allow_html=True)

    kegiatan_poisson = [
        {"url": "https://drive.google.com/uc?export=view&id=1XIyLVcQSSkwAItHTyCCSX1WZtmCpdblM", "judul": "First Moment", "desc": "Awal dari cerita yang panjang"},
        {"url": "https://drive.google.com/uc?export=view&id=1Oi4CMuo7gzPc9cobE01SUmZQbR0bcfA2", "judul": "Our Journey", "desc": "Langkah demi langkah bersama"},
        {"url": "https://drive.google.com/uc?export=view&id=1j02Eq5ZqVHUFdGnEvLV5oDiHxZvoLCdc", "judul": "Growing Together", "desc": "Tumbuh bersama melalui setiap proses"},
        {"url": "https://drive.google.com/uc?export=view&id=1Y9aO6QYXVf3dkHCWwpAZPf6KNrLguEmx", "judul": "The Story", "desc": "Setiap foto menyimpan cerita."},
        {"url": "https://drive.google.com/uc?export=view&id=1dDPrlobxQlHnAwMZKdoSuGcJviyfueTn", "judul": "Good Times", "desc": "Keluh kesah, tawa dan cerita yang tak bisa dilupakan"},
        {"url": "https://drive.google.com/uc?export=view&id=1bxRGpALCGFINoBxPCsA9MpiW6cxpyPaa", "judul": "Until Forever", "desc": "Bukan akhir, hanya bagian dari perjalanan"}
    ]

    for i in range(0, len(kegiatan_poisson), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(kegiatan_poisson):
                item = kegiatan_poisson[idx]
                with cols[j]:
                    img_src = image_data_uri(item["url"], max_dim=1200, quality=85)
                    if img_src:
                        st.markdown(f"""
                            <div class="photo-card">
                                <img src="{img_src}" alt="{html.escape(item['judul'], quote=True)}">
                                <div class="overlay">
                                    <div class="overlay-title">{html.escape(item['judul'])}</div>
                                    <div class="overlay-desc">{html.escape(item['desc'])}</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)


# ============================================================
# ABOUT US PAGE
# ============================================================
elif menu == "About Us":
    st.markdown("<h2 class='section-title'>Our Mentor</h2>", unsafe_allow_html=True)

    # ─── DATA MENTOR ───
    mentor = {
        "nama": "Hafidz Wahdiansyah",
        "sebagai": "Mentor",
        "nim": "124450064",
        "fun_fact": "Pernah ngoding sampai 12 jam",
        "motto_hidup": "Motivasi hari ini adalah motivasi untuk esok"
    }
    mentor_img_url = "https://drive.google.com/uc?export=view&id=1UJWhabFk6lWj7fylxUR6apqPbZHvoCoz"

    # Tampilkan Mentor (Posisi di Tengah)
    col_mid1, col_mid2, col_mid3 = st.columns([1, 1.5, 1])
    with col_mid2:
        img_src = image_data_uri(mentor_img_url, max_dim=1200, quality=85)
        if img_src:
            st.markdown(f"""
                <div class="flip-card mentor-flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="photo-frame">
                                <img src="{img_src}">
                            </div>
                            <h4>{mentor['nama']}</h4>
                            <span class="role-badge">{mentor['sebagai']}</span>
                            <div class="flip-hint">hover</div>
                        </div>
                        <div class="flip-card-back">
                            <h4>{mentor['nama']}</h4>
                            <div class="back-role">{mentor['sebagai']}</div>
                            <div class="divider"></div>
                            <p><span class="label">NIM</span>{mentor['nim']}</p>
                            <p><span class="label">Fun Fact</span>{mentor['fun_fact']}</p>
                            <p><span class="label">Motto Hidup</span>{mentor['motto_hidup']}</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<h2 class='section-title'>Anggota Kelompok</h2>", unsafe_allow_html=True)

    # ─── DATA ANGGOTA ───
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1OZWQEzUE1biYVl5igEDRCdqYE1Kdculc",
        "https://drive.google.com/uc?export=view&id=1DF_qQCOIFDvyjG5SEOL8DURaTbjy1OWc",
        "https://drive.google.com/uc?export=view&id=19FctJT5o6JBmGICiSu15NAIwLR4VFhW_",
        "https://drive.google.com/uc?export=view&id=1jDU86oPLsjea0l0FiwbVjF6Esuekw4MG",
        "https://drive.google.com/uc?export=view&id=1OOVOfx6v2WEL_lPFwtqt_2Pnp9dmZNAU",
        "https://drive.google.com/uc?export=view&id=1OcyHkxkcelFVtIa2oc0fF1aO85im1_Vp",
        "https://drive.google.com/uc?export=view&id=1K1XEcndMVCAyAFS2i6j8SlWriPLSNAau",
        "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
        "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
        "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
        "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
    ]

    data_list = [
        {"nama": "Yobel Imanuel Pasaribu", "sebagai": "Pak Lurah", "nim": "125450116", "fun_fact": "Bawa bantal guling dari kecil sampe sekaran", "motto_hidup": "New semester new me"},
        {"nama": "Rena Aprilia", "sebagai": "Bu Lurah", "nim": "125450109", "fun_fact": "Suka nyemilin es batu saat santai", "motto_hidup": "Konsisten adalah kunci sukses"},
        {"nama": "Samuel Kristian", "sebagai": "Anggota", "nim": "125450084", "fun_fact": "Anak ke-9 dari 9 BERSAUDARA!!!", "motto_hidup": "Trying to be better"},
        {"nama": "Nailatun Inayah", "sebagai": "Anggota", "nim": "125450037", "fun_fact": "Bisa tidur di segala jenis kendaraan", "motto_hidup": "Jalanin dulu aja dengan ikhlas"},
        {"nama": "Alfajri Anwar", "sebagai": "Anggota", "nim": "125450074", "fun_fact": "Suka begadang demi nonton bola", "motto_hidup": "Usaha tidak mengkhianati hasil"},
        {"nama": "Inness Eymard Gultom", "sebagai": "Anggota", "nim": "125460075", "fun_fact": "Pecinta kucing garis keras", "motto_hidup": "Jadilah versi terbaik dirimu"},
        {"nama": "Kayyisah Mazaya", "sebagai": "Anggota", "nim": "125450033", "fun_fact": "Selalu membawa tumbler sendiri", "motto_hidup": "Fokus pada prosesnya"},
        {"nama": "Fadhilah Adelyia Putri", "sebagai": "Anggota", "nim": "125450020", "fun_fact": "Sering salah panggil nama dosen", "motto_hidup": "Senyum adalah ibadah"},
        {"nama": "Dzahra Adila Fatma", "sebagai": "Anggota", "nim": "125450028", "fun_fact": "Hobi koleksi sepatu sneakers", "motto_hidup": "Hari ini harus lebih baik"},
        {"nama": "Egia Ninta Pepayosa Ketaren", "sebagai": "Anggota", "nim": "125450008", "fun_fact": "Suka minum es teh manis jumbo", "motto_hidup": "Selalu bersyukur setiap hari"},
        {"nama": "Achmad Fardhan Al Basri Bandarudin", "sebagai": "Anggota", "nim": "125450018", "fun_fact": "Main game online sampai pagi", "motto_hidup": "Pantang pulang sebelum selesai"}
    ]

    for i in range(0, len(data_list), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(data_list):
                member = data_list[idx]
                img_url = gambar_urls[idx]

                with cols[j]:
                    img_src = image_data_uri(img_url, max_dim=1200, quality=85)
                    if img_src:
                        role_class = "anggota" if member["sebagai"].lower() == "anggota" else ""
                        st.markdown(f"""
                            <div class="flip-card">
                                <div class="flip-card-inner">
                                    <div class="flip-card-front">
                                        <div class="photo-frame">
                                            <img src="{img_src}" alt="{html.escape(member['nama'], quote=True)}">
                                        </div>
                                        <h4>{member['nama']}</h4>
                                        <span class="role-badge {role_class}">{member['sebagai']}</span>
                                        <div class="flip-hint">hover</div>
                                    </div>
                                    <div class="flip-card-back">
                                        <h4>{member['nama']}</h4>
                                        <div class="back-role">{member['sebagai']}</div>
                                        <div class="divider"></div>
                                        <p><span class="label">NIM</span>{member['nim']}</p>
                                        <p><span class="label">Fun Fact</span>{member['fun_fact']}</p>
                                        <p><span class="label">Motto Hidup</span>{member['motto_hidup']}</p>
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
