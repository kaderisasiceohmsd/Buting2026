# Halaman Utama/halaman_utama.py
import streamlit as st
from streamlit_option_menu import option_menu
import html

# ─── Import dari utils.py ───
from utils import load_image, image_data_uri


# ============================================================
# 🎨 CUSTOM CSS HALAMAN UTAMA (Utuh seperti aslimu + Tambahan Mentor)
# ============================================================
HALAMAN_UTAMA_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; color: #222222; }
.stApp {
    background: radial-gradient(circle at 15% 10%, rgba(112,28,35,0.06) 0%, transparent 45%),
                radial-gradient(circle at 85% 90%, rgba(217,195,163,0.18) 0%, transparent 50%),
                linear-gradient(180deg, #f4f0eb 0%, #efe8df 100%);
    background-attachment: fixed;
}
.main-title {
    text-align: center; font-family: 'Playfair Display', serif; font-weight: 900;
    font-size: 3.6em !important; letter-spacing: 1px; margin-bottom: 6px;
    background: linear-gradient(135deg, #701c23 0%, #a8323d 45%, #701c23 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-shadow: 0 2px 20px rgba(112,28,35,0.15); position: relative; display: inline-block; width: 100%;
}
.main-title::after {
    content: ''; display: block; width: 90px; height: 3px;
    margin: 14px auto 0; background: linear-gradient(90deg, transparent, #701c23, transparent); border-radius: 3px;
}
.main-subtitle {
    text-align: center; font-family: 'Inter', sans-serif; color: #6b5a52;
    font-weight: 500; font-size: 1.15em !important; letter-spacing: 2.5px;
    text-transform: uppercase; margin-bottom: 30px; margin-top: 6px;
}
.section-title {
    text-align: center; font-family: 'Playfair Display', serif; color: #701c23;
    font-weight: 700; font-size: 1.9em; margin-top: 45px; margin-bottom: 30px; position: relative; display: block;
}
.section-title::before, .section-title::after {
    content: '✦'; color: #d9c3a3; margin: 0 18px; font-size: 0.7em; vertical-align: middle;
}
.content-box {
    background: linear-gradient(135deg, #ffffff 0%, #fdfbf8 100%); padding: 38px 42px;
    border-radius: 20px; box-shadow: 0 10px 30px rgba(112,28,35,0.07);
    border: 1px solid rgba(217,195,163,0.55); margin-bottom: 38px;
    text-align: justify; line-height: 1.95; font-size: 15.5px; color: #3a2f2b; position: relative; overflow: hidden;
}
.content-box::before {
    content: ''; position: absolute; top: 0; left: 0; width: 5px; height: 100%;
    background: linear-gradient(180deg, #701c23, #d9c3a3, #701c23);
}
.content-box b { color: #701c23; font-weight: 700; letter-spacing: 0.2px; }

.photo-card {
    position: relative; overflow: hidden; border-radius: 16px;
    box-shadow: 0 4px 14px rgba(112,28,35,0.10); border: 1px solid rgba(217,195,163,0.7);
    margin-bottom: 22px; height: 210px; background-color: #ffffff; transition: transform 0.4s ease;
}
.photo-card:hover { transform: translateY(-6px); box-shadow: 0 18px 40px rgba(112,28,35,0.22); }
.photo-card img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.7s ease; }
.photo-card:hover img { transform: scale(1.1); }
.photo-card .overlay {
    position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(112,28,35,0.97), transparent);
    color: #ffffff; padding: 26px 14px 14px; opacity: 0; transition: opacity 0.4s ease; text-align: center;
}
.photo-card:hover .overlay { opacity: 1; }
.photo-card .overlay-title { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 15px; }
.photo-card .overlay-desc { font-size: 11.5px; }

/* FLIP CARD ANGGOTA */
.flip-card { background-color: transparent; width: 100%; height: 380px; perspective: 1600px; margin-bottom: 24px; position: relative; }
.flip-card-inner { position: relative; width: 100%; height: 100%; text-align: center; transition: transform 1s; transform-style: preserve-3d; border-radius: 18px; }
.flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
.flip-card-front, .flip-card-back {
    position: absolute; width: 100%; height: 100%; -webkit-backface-visibility: hidden; backface-visibility: hidden; border-radius: 18px; overflow: hidden;
}
.flip-card-front {
    background: linear-gradient(165deg, #ffffff 0%, #fdf9f3 100%); color: #701c23;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    padding: 20px; border: 1px solid rgba(217,195,163,0.75);
}
.flip-card-front .photo-frame {
    width: 148px; height: 180px; margin-bottom: 14px; border-radius: 12px; padding: 4px;
    background: linear-gradient(135deg, #701c23 0%, #d9c3a3 50%, #701c23 100%);
}
.flip-card-front .photo-frame img { width: 100%; height: 100%; object-fit: cover; border-radius: 9px; }
.flip-card-front h4 { margin: 2px 0 6px 0; font-family: 'Playfair Display', serif; font-weight: 700; font-size: 15.5px; }
.flip-card-front .role-badge { padding: 3px 12px; font-size: 9.5px; font-weight: 700; border-radius: 999px; background: #701c23; color: #f4f0eb; }
.flip-card-front .role-badge.anggota { background: #d9c3a3; color: #4e1318; }
.flip-card-front .flip-hint { font-size: 9px; color: #a89790; text-transform: uppercase; margin-top: 5px; }
.flip-card-back {
    background: linear-gradient(150deg, #701c23 0%, #4e1318 100%);
    color: #ffffff; transform: rotateY(180deg); text-align: left; padding: 20px; display: flex; flex-direction: column; justify-content: center;
}
.flip-card-back h4 { font-family: 'Playfair Display', serif; color: #e8c874; margin-bottom: 10px; font-size: 16px; }
.flip-card-back p { font-size: 12px; margin-bottom: 8px; padding: 8px 12px; background: rgba(255,255,255,0.05); border-radius: 8px; border-left: 2px solid #d9c3a3; }
.flip-card-back .label { font-weight: 700; color: #d9c3a3; font-size: 8.5px; text-transform: uppercase; display: block; }

/* ✨ CSS KHUSUS MENTOR ✨ */
.mentor-flip-card { height: 420px; max-width: 400px; margin: 0 auto 40px auto; }
.mentor-flip-card .flip-card-front { border: 2px solid #b8912e; background: linear-gradient(165deg, #fffdf5 0%, #fdf4e3 100%); }
.mentor-flip-card .photo-frame { width: 180px; height: 220px; background: linear-gradient(135deg, #b8912e 0%, #e8c874 50%, #b8912e 100%); }
.mentor-flip-card h4 { font-size: 20px; color: #b8912e; }
.mentor-flip-card .role-badge { background: linear-gradient(135deg, #b8912e, #e8c874); color: #4e1318; font-size: 11px; padding: 5px 16px; }
.mentor-flip-card .flip-card-back { background: linear-gradient(150deg, #b8912e 0%, #8a6a1f 100%); color: #ffffff; }

.hero-image-wrapper {
    position: relative; max-width: 1000px; margin: 0 auto 28px auto; border-radius: 20px; overflow: hidden;
    border: 1px solid rgba(217,195,163,0.65);
}
.hero-image-wrapper img { width: 100%; height: 380px; object-fit: cover; display: block; }
.hero-image-wrapper .hero-caption { position: absolute; bottom: 26px; left: 30px; right: 30px; color: #f4f0eb; }
.hero-image-wrapper .hero-caption h3 { font-family: 'Playfair Display', serif; font-size: 26px; margin: 0; color: #fff; }
.hero-image-wrapper .hero-caption p { font-size: 12.5px; margin-top: 6px; }
</style>
"""

st.markdown(HALAMAN_UTAMA_CSS, unsafe_allow_html=True)


# ============================================================
# HERO IMAGE HELPER
# ============================================================
def hero_image(url, badge="✦ Keluarga Poisson ✦", title="Satu Tim, Satu Cerita", subtitle="Momen kebersamaan yang menjadi awal dari segalanya."):
    img_src = image_data_uri(url, max_dim=1200, quality=85)
    if not img_src:
        return
    st.markdown(f"""
        <div class="hero-image-wrapper">
            <img src="{img_src}" alt="{html.escape(title, quote=True)}">
            <div class="hero-overlay"></div>
            <div class="hero-caption">
                <div class="hero-badge">{html.escape(badge)}</div>
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
# HOME PAGE (Utuh 100% Seperti Aslimu)
# ============================================================
if menu == "Home":
    st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)

    hero_image(
        url="https://drive.google.com/uc?export=view&id=1b38uX_AFwdNc3-03NWQPcOX-TIOdxDee",
        badge="✦ Keluarga Poisson ✦",
        title="Satu Tim, Satu Cerita",
        subtitle="Momen kebersamaan yang menjadi awal dari segalanya."
    )

    st.markdown("""
        <div class='content-box'>
            <b>Selamat datang di portal resmi kelompok Poisson!</b><br><br>
            Kelompok kami merupakan wadah kolaborasi, kebersamaan, dan dedikasi tinggi dalam menjalani rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating. Di sini, kami tidak hanya belajar menyelesaikan setiap tantangan akademik secara bersama-sama, tetapi juga membangun ikatan kekeluargaan yang erat, saling mendukung dalam setiap proses adaptasi, serta menjunjung tinggi nilai solidaritas dan profesionalisme sebagai bagian dari keluarga besar HMSD Adyatama ITERA.
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

    st.markdown("""
        <div class='content-box'>
            <b>Komitmen Kami:</b><br>
            Kami berkomitmen penuh untuk terus bergerak seirama, saling menguatkan dalam menghadapi dinamika perkuliahan, serta menyelesaikan seluruh rangkaian tanggung jawab dengan hasil yang terbaik dan membanggakan.
        </div>
    """, unsafe_allow_html=True)


# ============================================================
# ABOUT US PAGE (Ditambah Card Mentor di Paling Atas)
# ============================================================
elif menu == "About Us":
    st.markdown("<h2 class='section-title'>Our Mentor</h2>", unsafe_allow_html=True)

    # ─── DATA MENTOR ───
    mentor = {
        "nama": "Kakak Mentor Poisson",
        "sebagai": "Mentor Kating",
        "nim": "123456789",
        "fun_fact": "Suka ngasih tugas jam 12 malam",
        "motto_hidup": "Semangat terus, nak kating!"
    }
    # Ganti URL ini dengan foto mentor asli
    mentor_img_url = "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E" 

    # Tampilkan Mentor (Posisi di Tengah)
    col_mid1, col_mid2, col_mid3 = st.columns([1, 2, 1])
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
        "https://drive.google.com/uc?export=view&id=1VZfU_oBz3w68OXo4xKuAQ14wcS7wtC4E",
        "https://drive.google.com/uc?export=view&id=1DF_qQCOIFDvyjG5SEOL8DURaTbjy1OWc",
        "https://drive.google.com/uc?export=view&id=19FctJT5o6JBmGICiSu15NAIwLR4VFhW_",
        "https://drive.google.com/uc?export=view&id=1jDU86oPLsjea0l0FiwbVjF6Esuekw4MG",
        "https://drive.google.com/uc?export=view&id=1OOVOfx6v2WEL_lPFwtqt_2Pnp9dmZNAU",
        "https://drive.google.com/uc?export=view&id=1OcyHkxkcelFVtIa2oc0fF1aO85im1_Vp",
        "https://drive.google.com/uc?export=view&id=1K1XEcndMVCAyAFS2i6j8SlWriPLSNAau",
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
                                        <p><span class="label">NIM</span>{member['nim']}</p>
                                        <p><span class="label">Fun Fact</span>{member['fun_fact']}</p>
                                        <p><span class="label">Motto Hidup</span>{member['motto_hidup']}</p>
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
