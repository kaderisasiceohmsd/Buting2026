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
            "nav-link-selected": {"background-color": "#606060"},
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
            """<div style="text-align: justify;">Kelompok Anova merupakan penjabaran dari metode statistik
            yang digunakan untuk menguji perbedaan rata-rata antara tiga kelompok atau lebih.
            Filosofi dasar di balik ANOVA adalah untuk mengetahui
            apakah beberapa kelompok memiliki rata-rata yang sama atau tidak,
            pemeriksaan rata-ratanya tidak secara langsung,
            melainkan memeriksa variabilitas atau keragaman dari data yang ada.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1_2RuzY18oqdjj4M4Ue0V50LZBXIga_LQ"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Dengan kata lain, kelompok Anova yang beragam dan bervariasi
            baik itu dari asal daerah, latar belakang, maupun pengalaman yang berbeda-beda diharapkan
            dapat saling melengkapi satu sama lain, memiliki rasa dan pengalaman yang sama
            untuk menghadapi tantangan dan rintangan kedepannya dan dapat menjalin hubungan baik
            serta bahu-membahu menghadapi keadaan atau permasalahan yang ada.</div>""",
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
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1LmYWz88aq2OL749V38x_tlFQJ4MtZ-f1",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Yosep Winarto Sinulingga",
                "sebagai": "Pak Lurah",
                "nim": "125450125",
                "fun_fact": "suka makan pedes, tapi ga suka efeknya",
                "motto_hidup": "new semester new me",
            },
            {
                "nama": "Tiara Amelia",
                "sebagai": "Bu Lurah",
                "nim": "125450015",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Muhammad Rizky Pratama",
                "sebagai": "Anggota",
                "nim": "125450017",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Rasya Rajid Pratama",
                "sebagai": "Anggota",
                "nim": "125450029",
                "fun_fact": "nyemilin",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "Elena Fariza Zahra",
                "sebagai": "Anggota",
                "nim": "125450031",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Muhammad Irfan Nugraha",
                "sebagai": "Anggota",
                "nim": "125450065",
                "fun_fact": "Hobi dengerin musik, tapi ga bisa main alat musik",
                "motto_hidup": "Don't cry because it's over, smile because it happened",
            },
            {
                "nama": "Elisabeth Yulyanti Gultom",
                "sebagai": "Anggota",
                "nim": "125450078",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Zetkin Alando Dzaqwan",
                "sebagai": "Anggota",
                "nim": "125450086",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Jhonatan Best Kingsil Sakerebau",
                "sebagai": "Anggota",
                "nim": "125450108",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Jeanis Nahwadisa",
                "sebagai": "Anggota",
                "nim": "125450117",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Intan Abelia Sari",
                "sebagai": "Anggota",
                "nim": "125450124",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Yunika Br Malau",
                "sebagai": "Anggota",
                "nim": "125450129",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
