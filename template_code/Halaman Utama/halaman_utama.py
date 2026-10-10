import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# UI/UX PUNYA POISSON YEAHH
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #701c23;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .main-subtitle {
        text-align: center;
        color: #555555;
        font-weight: 600;
        margin-bottom: 25px;
    }
    .section-title {
        text-align: center;
        color: #701c23;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 25px;
    }
    .content-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #d9c3a3;
        margin-bottom: 35px;
        text-align: justify;
        line-height: 1.8;
        font-size: 15px;
        color: #333333;
    }

    /* --- STYLING PHOTO CARD GRID (HOVER EFFECT) --- */
    .photo-card {
        position: relative;
        overflow: hidden;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(112, 28, 35, 0.12);
        border: 2px solid #701c23;
        margin-bottom: 20px;
        height: 200px;
        background-color: #ffffff;
    }
    .photo-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s ease;
    }
    .photo-card:hover img {
        transform: scale(1.08);
    }
    .photo-card .overlay {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(transparent, rgba(112, 28, 35, 0.95));
        color: #ffffff;
        padding: 15px 12px 10px 12px;
        opacity: 0;
        transition: opacity 0.3s ease;
        text-align: center;
    }
    .photo-card:hover .overlay {
        opacity: 1;
    }
    .photo-card .overlay-title {
        font-weight: 700;
        font-size: 14px;
        color: #f4f0eb;
        margin-bottom: 3px;
    }
    .photo-card .overlay-desc {
        font-size: 12px;
        line-height: 1.3;
    }

    /* --- FLASHCARD FLIP ABOUT US --- */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 380px;
        perspective: 1000px;
        margin-bottom: 25px;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(112, 28, 35, 0.15);
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
        border-radius: 15px;
        padding: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .flip-card-front {
        background-color: #ffffff;
        color: #701c23;
        border: 2px solid #d9c3a3;
    }
    .flip-card-front img {
        width: 160px;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 2px solid #701c23;
    }
    .flip-card-front h4 {
        margin: 5px 0 0 0;
        font-weight: 700;
        color: #701c23;
        font-size: 16px;
    }
    .flip-card-back {
        background-color: #701c23;
        color: #ffffff;
        transform: rotateY(180deg);
        text-align: left;
        align-items: flex-start;
        padding: 20px;
        box-sizing: border-box;
    }
    .flip-card-back h4 {
        color: #d9c3a3;
        font-weight: 700;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(217, 195, 163, 0.4);
        padding-bottom: 6px;
        width: 100%;
        font-size: 17px;
    }
    .flip-card-back p {
        font-size: 13px;
        margin: 4px 0;
        line-height: 1.4;
    }
    .flip-card-back .label {
        font-weight: bold;
        color: #d9c3a3;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        return img
    except Exception:
        return None

# Header Utama
st.markdown("""
    <div>
        <h1 class='main-title' style='font-size: 3em;'>WEBSITE KATING</h1>
        <p class='main-subtitle' style='font-size: 1.3em;'>CEO HMSD Adyatama ITERA 2026</p>
    </div>
""", unsafe_allow_html=True)

url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"

def layout_logo(url):
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    with col2:
        img = load_image(url)
        if img:
            st.image(img, use_container_width=True)

layout_logo(url)
st.write("")
layout_logo(url1)

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "10px!important", 
                "background-color": "#ffffff", 
                "border-radius": "12px", 
                "box-shadow": "0 3px 10px rgba(0,0,0,0.08)",
                "margin-bottom": "35px"
            },
            "icon": {"color": "#701c23", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "0 5px",
                "padding": "10px 20px",
                "border-radius": "8px",
                "--hover-color": "#f4f0eb",
            },
            "nav-link-selected": {"background-color": "#701c23", "color": "#ffffff"},
        },
    )
    return selected

menu = streamlit_menu()

if menu == "Home":
    def home_page():
        st.markdown("<h2 class='section-title'>Deskripsi Kelompok</h2>", unsafe_allow_html=True)
        st.markdown("""
            <div class='content-box'>
                <b>Selamat datang di portal resmi kelompok Poisson!</b><br><br>
                Kelompok kami merupakan wadah kolaborasi, kebersamaan, dan dedikasi tinggi dalam menjalani rangkaian kegiatan pengenalan kampus dan penugasan Buku Kating. Di sini, kami tidak hanya belajar menyelesaikan setiap tantangan akademik secara bersama-sama, tetapi juga membangun ikatan kekeluargaan yang erat, saling mendukung dalam setiap proses adaptasi, serta menjunjung tinggi nilai solidaritas dan profesionalisme sebagai bagian dari keluarga besar HMSD Adyatama ITERA.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<h3 class='section-title' style='font-size:22px;'>Dokumentasi Kegiatan Poisson (2 x 3 Grid)</h3>", unsafe_allow_html=True)
        
        kegiatan_poisson = [
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Mengerjakan Tugas", "desc": "Poisson saat sedang serius berdiskusi menyelesaikan penugasan kelompok bersama."},
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Diskusi Santai", "desc": "Poisson saat sedang nongkrong seru sambil melepas penat di kampus."},
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Sesi Foto", "desc": "Poisson saat sedang kompak mengabadikan momen kebersamaan."},
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Belajar Bersama", "desc": "Poisson saat sedang mempersiapkan materi dan bahan presentasi."},
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Selesai Mentoring", "desc": "Poisson saat sedang merayakan suksesnya sesi mentoring bersama."},
            {"url": "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", "judul": "Poisson Briefing", "desc": "Poisson saat sedang melakukan evaluasi dan arahan mingguan."}
        ]

        for i in range(0, len(kegiatan_poisson), 3):
            cols = st.columns(3)
            for j in range(3):
                idx = i + j
                if idx < len(kegiatan_poisson):
                    item = kegiatan_poisson[idx]
                    with cols[j]:
                        st.markdown(f"""
                            <div class="photo-card">
                                <img src="{item['url']}" alt="{item['judul']}">
                                <div class="overlay">
                                    <div class="overlay-title">{item['judul']}</div>
                                    <div class="overlay-desc">{item['desc']}</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class='content-box'>
                <b>Komitmen Kami:</b><br>
                Kami berkomitmen penuh untuk terus bergerak seirama, saling menguatkan dalam menghadapi dinamika perkuliahan, serta menyelesaikan seluruh rangkaian tanggung jawab dengan hasil yang terbaik dan membanggakan.
            </div>
        """, unsafe_allow_html=True)

    home_page()

elif menu == "About Us":
    def about_page():
        st.markdown("<h2 class='section-title'>About Us</h2>", unsafe_allow_html=True)
        
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_" for _ in range(11)
        ]
        
        data_list = [
            {"nama": "Yobel Imanuel Pasaribu", "sebagai": "Pak Lurah", "nim": "122450016", "fun_fact": "Suka makan pedas, tapi tidak suka efeknya", "motto_hidup": "New semester new me"},
            {"nama": "Siti Rahma", "sebagai": "Bu Lurah", "nim": "122450002", "fun_fact": "Suka nyemilin es bata saat santai", "motto_hidup": "Konsisten adalah kunci sukses"},
            {"nama": "Ahmad Fauzi", "sebagai": "Anggota", "nim": "122450083", "fun_fact": "Hafal seluruh lirik lagu daerah", "motto_hidup": "Tetap semangat pantang menyerah"},
            {"nama": "Dinda Permata", "sebagai": "Anggota", "nim": "122450045", "fun_fact": "Bisa tidur di segala jenis kendaraan", "motto_hidup": "Jalanin dulu aja dengan ikhlas"},
            {"nama": "Rizky Ramadhan", "sebagai": "Anggota", "nim": "122450100", "fun_fact": "Suka begadang demi nonton bola", "motto_hidup": "Usaha tidak mengkhianati hasil"},
            {"nama": "Nabila Zahra", "sebagai": "Anggota", "nim": "122450112", "fun_fact": "Pecinta kucing garis keras", "motto_hidup": "Jadilah versi terbaik dirimu"},
            {"nama": "Kevin Sanjaya", "sebagai": "Anggota", "nim": "122450125", "fun_fact": "Selalu membawa tumbler sendiri", "motto_hidup": "Fokus pada prosesnya"},
            {"nama": "Clarissa Putri", "sebagai": "Anggota", "nim": "122450140", "fun_fact": "Sering salah panggil nama dosen", "motto_hidup": "Senyum adalah ibadah"},
            {"nama": "Bagas Pratama", "sebagai": "Anggota", "nim": "122450155", "fun_fact": "Hobi koleksi sepatu sneakers", "motto_hidup": "Hari ini harus lebih baik"},
            {"nama": "Maya Indah", "sebagai": "Anggota", "nim": "122450168", "fun_fact": "Suka minum es teh manis jumbo", "motto_hidup": "Selalu bersyukur setiap hari"},
            {"nama": "Fajar Hidayat", "sebagai": "Anggota", "nim": "122450180", "fun_fact": "Main game online sampai pagi", "motto_hidup": "Pantang pulang sebelum selesai"}
        ]

        for i in range(0, len(data_list), 3):
            cols = st.columns(3)
            for j in range(3):
                idx = i + j
                if idx < len(data_list):
                    member = data_list[idx]
                    img_url = gambar_urls[idx]
                    
                    with cols[j]:
                        st.markdown(f"""
                            <div class="flip-card">
                                <div class="flip-card-inner">
                                    <div class="flip-card-front">
                                        <img src="{img_url}" alt="{member['nama']}">
                                        <h4>{member['nama']}</h4>
                                        <span style="font-size:11px; color:#888;">(Arahkan kursor untuk balik)</span>
                                    </div>
                                    <div class="flip-card-back">
                                        <h4>{member['nama']}</h4>
                                        <p><span class="label">Sebagai:</span> {member['sebagai']}</p>
                                        <p><span class="label">NIM:</span> {member['nim']}</p>
                                        <p><span class="label">Fun Fact:</span> {member['fun_fact']}</p>
                                        <p><span class="label">Motto:</span> {member['motto_hidup']}</p>
                                    </div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

    about_page()
