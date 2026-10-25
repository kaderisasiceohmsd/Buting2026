import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

# ============================================================
# TAMBAHAN CSS TEMA BIRU BAYESIAN (AMAN & TIDAK MERUSAK TEMPLATE)
# ============================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

    .stApp {
        background: 
            radial-gradient(circle at 8% 10%, rgba(142, 197, 252, 0.25), transparent 35%),
            radial-gradient(circle at 92% 80%, rgba(36, 107, 206, 0.12), transparent 40%),
            linear-gradient(180deg, #F7FAFF 0%, #EAF2FC 100%);
        background-attachment: fixed;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #102A56;
    }

    .centered-title {
        text-align: center;
        font-family: 'Playfair Display', serif;
        color: #102A56;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 20px;
    }

    .centered-title::after {
        content: '';
        display: block;
        width: 65px;
        height: 4px;
        margin: 10px auto 0;
        border-radius: 10px;
        background: linear-gradient(90deg, #246BCE, #8EC5FC);
    }

    /* Mempercantik tampilan foto st.image bawaan template */
    div[data-testid="stImage"] img {
        border-radius: 18px;
        box-shadow: 0 10px 28px rgba(16, 42, 86, 0.12);
        border: 2px solid #D8E7FA;
        transition: transform 0.3s ease;
    }

    div[data-testid="stImage"] img:hover {
        transform: scale(1.02);
    }

    /* Kotak teks deskripsi & komitmen bertema biru */
    .blue-card-box {
        background: #FFFFFF;
        border: 1px solid #D8E7FA;
        border-left: 5px solid #246BCE;
        border-radius: 16px;
        padding: 22px 26px;
        text-align: justify;
        line-height: 1.8;
        color: #334963;
        box-shadow: 0 8px 24px rgba(16, 42, 86, 0.06);
        margin-bottom: 20px;
    }

    /* Kartu caption dokumentasi di halaman Home */
    .moment-caption-box {
        background: linear-gradient(135deg, #102A56, #246BCE);
        color: #FFFFFF;
        padding: 12px 18px;
        border-radius: 12px;
        text-align: center;
        margin-top: -8px;
        margin-bottom: 22px;
        box-shadow: 0 6px 18px rgba(36, 107, 206, 0.2);
    }

    .moment-caption-box b {
        font-family: 'Playfair Display', serif;
        font-size: 1.15em;
        display: block;
        margin-bottom: 3px;
    }

    .moment-caption-box span {
        font-size: 0.9em;
        color: #EAF3FF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER UTAMA
# ============================================================
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 4.5em; font-family: "Playfair Display", serif; color: #102A56; margin-bottom: 0;'>WEBSITE KATING</h1>
        <p style='font-size: 1.6em; color: #246BCE; font-weight: 700; letter-spacing: 2px;'>CEO HMSD Adyatama ITERA 2026 — BAYESIAN</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_container_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


# ============================================================
# NAVIGASI MENU (OPTION MENU HORIZONTAL TEMA BIRU)
# ============================================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "6px!important",
                "background-color": "#EAF3FF",
                "border-radius": "14px",
                "border": "1px solid #D8E7FA",
            },
            "icon": {"color": "#102A56", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "color": "#102A56",
                "text-align": "center",
                "margin": "0px 4px",
                "border-radius": "10px",
                "--hover-color": "#D2E4FF",
            },
            "nav-link-selected": {
                "background-color": "#246BCE",
                "color": "#FFFFFF",
                "font-weight": "700",
            },
        },
    )
    return selected


menu = streamlit_menu()

# ============================================================
# HALAMAN HOME
# ============================================================
if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok Bayesian</h1>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """<div class="blue-card-box">
            <b>Selamat datang di portal resmi Kelompok Bayesian!</b><br><br>
            <i>"Gapai Cita, Kejar Mimpi, di Angkasa."</i><br>
            Terinspirasi dari <b>Teorema Bayes</b> dalam Sains Data dan Statistika, kelompok <b>Bayesian</b> melambangkan semangat pembelajaran dan kekeluargaan yang adaptif: setiap pengalaman, tantangan, dan kebersamaan baru adalah bukti nyata yang terus memperbarui serta menguatkan langkah kita untuk bertumbuh bersama di <b>CEO HMSD Adyatama ITERA 2026</b>.
            </div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

        # Foto Utama Kelompok
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"
        layout(foto_kelompok)
        st.markdown(
            """<div class="moment-caption-box">
                <b>✦ Keluarga Bayesian ✦</b>
                <span>Momen kebersamaan yang tidak akan terlupakan.</span>
            </div>""",
            unsafe_allow_html=True,
        )

        # Dokumentasi Kegiatan
        st.markdown(
            "<h2 class='centered-title' style='font-size: 2em;'>Dokumentasi Kegiatan Bayesian</h2>",
            unsafe_allow_html=True,
        )

        kegiatan_Bayesian = [
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
            {"url": "https://drive.google.com/uc?export=view&id=1iC5C15zecDnw5K7ZQDw3Nr41lubTjYSq"},
        ]

        for i in range(0, len(kegiatan_Bayesian), 2):
            col_a, col_b = st.columns(2)
            with col_a:
                item1 = kegiatan_Bayesian[i]
                st.image(load_image(item1["url"]), use_container_width=True)
            with col_b:
                if i + 1 < len(kegiatan_Bayesian):
                    item2 = kegiatan_Bayesian[i + 1]
                    st.image(load_image(item2["url"]), use_container_width=True)

    home_page()

# ============================================================
# HALAMAN ABOUT US
# ============================================================
elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>About Us — Buku Kating Bayesian</h1>",
            unsafe_allow_html=True,
        )

        # 10 URL Gambar sesuai jumlah 10 anggota di data_list
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19KrR82_PA5lsmyDn-8iBcBBVxWqctEp9",  # 1. Thomas Yustio
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 2. Syalom Nauli Jubilate
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 3. Chavia Chairunissa
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 4. Aqila Chika Aurelia
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 5. Sefina Amanda Putri
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 6. Aura Putri Ghefira
            "https://drive.google.com/uc?export=view&id=1SaqIKBazfbklZ87SPixrd5eO0PfvydN3",  # 7. Ezra Hamizan
            "https://drive.google.com/uc?export=view&id=1OPEq99LUbLHfdDUTj95ueH52KCoFkKXo",  # 8. Afdhi Hafiidz Habibie
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 9. Rizqy Ramadhan
            "https://drive.google.com/uc?export=view&id=1SKBh8OuBiB2OKT4M_sBlXcxT9fqwMaZz",  # 10. Alan Garcia Sinaga
        ]

        # Data Lengkap 10 Anggota Bayesian
        data_list = [
            {
                "nama": "Thomas Yustio",
                "sebagai": "Pak Lurah",
                "nim": "125450085",
                "fun_fact": "Saya pernah patah gigi 4x dan saya karbitan",
                "motto_hidup": "Hidup cuma sekali, maka lakukan apa yang kamu mau, misal mancing",
            },
            {
                "nama": "Syalom Nauli Jubilate",
                "sebagai": "Bu Lurah",
                "nim": "125450050",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Chavia Chairunissa",
                "sebagai": "Anggota 01",
                "nim": "125450026",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Aqila Chika Aurelia",
                "sebagai": "Anggota 02",
                "nim": "125450038",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Sefina Amanda Putri",
                "sebagai": "Anggota 03",
                "nim": "125450042",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Aura Putri Ghefira",
                "sebagai": "Anggota 04",
                "nim": "125450047",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
            {
                "nama": "Ezra Hamizan",
                "sebagai": "Anggota 05",
                "nim": "125450052",
                "fun_fact": "Sangat Konyol & Selalu Konyol",
                "motto_hidup": "Cacing-Cacing, Naga-Naga, Go Big Or Go Home",
            },
            {
                "nama": "Afdhi Hafiidz Habibie",
                "sebagai": "Anggota 06",
                "nim": "125450061",
                "fun_fact": "Waktu belajar sepeda pernah nyemplung ke bekas adukan semen",
                "motto_hidup": "Hidup di dunia ini kayak plat Jakarta B aja",
            },
            {
                "nama": "Rizqy Ramadhan",
                "sebagai": "Anggota 07",
                "nim": "125450066",
                "fun_fact": "Selalu dikira orang Kristen Aslinya Islam Alhamdulillah",
                "motto_hidup": "Tetap lah bernafas",
            },
            {
                "nama": "Alan Garcia Sinaga",
                "sebagai": "Anggota 08",
                "nim": "125450091",
                "fun_fact": "--",
                "motto_hidup": "--",
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    about_page()
