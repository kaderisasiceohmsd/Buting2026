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

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2026</p>
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


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify; line-height: 1.6; font-size: 16px;">
            Kami adalah kelompok Tensor yang terdiri dari mahasiswa/i Sains Data angkatan 2025. 
            Melalui website ini, kami bertujuan untuk mendokumentasikan hasil wawancara dan interaksi kami dengan 
            Kakak Tingkat (Kating) dalam rangkaian kegiatan CEO HMSD Adyatama ITERA. 
            Website ini merupakan wujud nyata penerapan ilmu pemrograman Python dan framework Streamlit 
            yang telah kami pelajari.
            </div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        
        # Ganti dengan link foto kelompok yang asli
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1BFaWjCYfj0HFeGBBDB8SmUYsZkxcEvM7"
        layout(foto_kelompok)
        
        st.markdown(
            """<div style="text-align: justify; line-height: 1.6; font-size: 16px;">
            Dalam proses pembuatan buku digital ini, kami belajar banyak hal, mulai dari manajemen proyek menggunakan Git/GitHub, 
            perancangan antarmuka pengguna (UI/UX) sederhana, hingga kolaborasi tim yang solid. 
            Semoga website Buku Kating ini dapat menjadi referensi dan kenang-kenangan yang bermanfaat 
            bagi kami maupun pembaca.
            </div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        
        # --- KODE CSS TAMBAHAN UNTUK TAMPILAN PROFESIONAL ---
        st.markdown("""
        <style>
            /* Styling agar foto membulat sedikit dan memiliki bayangan lembut */
            img {
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                margin-bottom: 10px;
            }
            
            /* Merapikan jarak teks biodata agar lebih lega saat dibaca */
            .stMarkdown p {
                line-height: 1.8;
                font-size: 16px;
                margin-bottom: 5px;
            }
        </style>
        """, unsafe_allow_html=True)
        # ----------------------------------------------------
        
        st.markdown("<h1 class='centered-title'>Anggota Kelompok</h1>", unsafe_allow_html=True)
        
        # Ganti URL ini dengan foto masing-masing anggota kelompokmu
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Foto Anggota 1
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Foto Anggota 2
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Foto Anggota 3
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Foto Anggota 4
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", # Foto Anggota 5
        ]
        
        # Ganti data ini dengan data asli anggota kelompokmu
        data_list = [
            {
                "nama": "**Ahmad Fadylah**",
                "sebagai": "Pak lurah",
                "nim": "124450103",
                "fun_fact": "Suka ngeliatin Sunset",
                "motto_hidup": "Nothing is impossible",
            },
            {
                "nama": "**Nobel Nizam Fathirizki**",
                "sebagai": "Anggota",
                "nim": "124450117",
                "fun_fact": "Suka ngoding sampai pagi",
                "motto_hidup": "Tetap santuy walaupun error banyak",
            },
            {
                "nama": "**[Nama Teman 3]**",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
            {
                "nama": "**[Nama Teman 4]**",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
            {
                "nama": "**[Nama Teman 5]**",
                "sebagai": "Anggota",
                "nim": "12445xxxx",
                "fun_fact": "[Isi Fun Fact]",
                "motto_hidup": "[Isi Motto]",
            },
        ]
        
        # Menampilkan gambar dan data menggunakan fungsi bawaan yang JANGAN DIUBAH
        display_images_with_data(gambar_urls, data_list)

    about_page()