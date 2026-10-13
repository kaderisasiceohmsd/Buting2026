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
            "<h1 class='centered-title'>JACOBIII, BWAAAAAA!!!!!</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Ganti ya deskripsinya!!!!</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1X8ixiPEye7AhBVRrl-Qm5dJ2amaSB3Y5"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Ganti ya deskripsinya!!!</div>""",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Dandy Romansyah",
                "sebagai": "Palu",
                "nim": "12545006",
                "fun_fact": "Fans Bernadya nomor 1 sedunia dengan jumlah mendengarkan 45.868 menit",
                "motto_hidup": "Pergi keluar untuk mencari referensi, lalu kembali untuk relevansi",
            },
            {
                "nama": "Dea Febryana",
                "sebagai": "Bulu",
                "nim": "125450058",
                "fun_fact": "Kalo nonton drakor atau film harus yg sad ending",
                "motto_hidup": "Let them, it will pas, time will tell",
            },
            {
                "nama": "Krisna Alviansyah",
                "sebagai": "Anggota",
                "nim": "125450089",
                "fun_fact": "Suka ngoleksi photocard JKT48 dan Board game",
                "motto_hidup": "sekarang atau tidak sama sekali, dan cobalah terus belum gila kan?",
            },
            {
                "nama": "Laura Brety Br Ginting",
                "sebagai": "Anggota",
                "nim": "125450053",
                "fun_fact": "Suka koleksi Bricks tapi nggak suka nyusunnya",
                "motto_hidup": "Lakukan yang terbaik di mana pun kamu berada",
            },
            {
                "nama": "Halidaziyah Maritoma Hasibuan",
                "sebagai": "Anggota",
                "nim": "125450118",
                "fun_fact": "Nama tengah diambil dari sejarah kampung",
                "motto_hidup": "lakukan apa yang kamu pikirkan apa yang kamu lakukan",
            },
            {
                "nama": "Eyi Adelia",
                "sebagai": "Anggota",
                "nim": "125450004",
                "fun_fact": "Punya Hyperhidrosis jadi sering kesetrum",
                "motto_hidup": "Gapapa pelan yang penting berprogres",
            },
            {
                "nama": "Dimas Ardhiteo Putra",
                "sebagai": "Anggota",
                "nim": "125450088",
                "fun_fact": "Mudah memahami buku jika dibaca dari bab belakang",
                "motto_hidup": "Hidup akan terasa lebih seru dengan melawan arus",
            },
            {
                "nama": "Zahro Khoirunnisa",
                "sebagai": "Anggota",
                "nim": "125450041",
                "fun_fact": "Clamsy girl",
                "motto_hidup": "jangan lupakan Tuhan, Orang tua, dan Tujuan kita",
            },
            {
                "nama": "M.Ramadhan Bagus Ar-Rahman",
                "sebagai": "Anggota",
                "nim": "125450087",
                "fun_fact": "Di Ruqyah 5x",
                "motto_hidup": "Im not winner but im not failure too",
            },
            {
                "nama": "Aura Krisna Azzira",
                "sebagai": "Anggota",
                "nim": "125450119",
                "fun_fact": "Semester 2 kecelakaan 3x",
                "motto_hidup": "Biarlah langkahku membentur baru, daripada mati rasa karena ragu",
            },
            {
                "nama": "Riva Septia Nanda",
                "sebagai": "Anggota",
                "nim": "125450114",
                "fun_fact": "Sarapan = bikin maag kambuh",
                "motto_hidup": "I'm not in rush, I'm on my path",
            },
            {
                "nama": "Dhani Harianto Pranata",
                "sebagai": "Anggota",
                "nim": "125450076",
                "fun_fact": "Suka nonton kartun doraemon",
                "motto_hidup": "Setiap hari adalah kesempatan untuk menjadi lebih baik",
            },
            {
                "nama": "Rahman Syapei",
                "sebagai": "Anggota",
                "nim": "125450130",
                "fun_fact": "Keliatan kalem tapi kalau sudah kenal berisik",
                "motto_hidup": "Teruslah berjuang impianmu menanti dan jadilah orang yang bisa dipercaya",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
