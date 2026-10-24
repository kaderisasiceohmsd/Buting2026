import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
from sakura_ui import (
    inject_sakura_css,
    render_home_tab,
    render_polaroid_about_us,
    render_centered_logo,
)

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

inject_sakura_css()

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
    render_centered_logo(url)


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
            "container": {
                "padding": "6px!important",
                "background-color": "#FFF0F5",
                "border": "1.5px solid #F5C2D7",
                "border-radius": "16px",
                "box-shadow": "0 8px 22px rgba(216, 90, 127, 0.08)",
                "max-width": "860px",
                "margin": "0 auto",
            },
            "icon": {"color": "#9E3356", "font-size": "18px"},
            "nav-link": {
                "font-size": "16px",
                "font-weight": "600",
                "color": "#4A2535",
                "text-align": "center",
                "margin": "0px 4px",
                "border-radius": "12px",
                "--hover-color": "#FCE4EC",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #D85A7F 0%, #B23A5E 100%)",
                "color": "#FFFFFF",
                "font-weight": "700",
            },
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1zwDzbQycF6FUnJdc5hM6TK-BnZc9SnC8"
        render_home_tab(foto_kelompok)

    home_page()

elif menu == "About Us":

    def about_page():
        mentor_data = {
            "nama": "Farhanah Hadaya Fatin",
            "sebagai": "Mentor Kelompok 02",
            "nim": "124450026",
            "fun_fact": "Bisa tidur dimana aja kapan aja",
            "motto_hidup": "Risking better than regretting",
            "foto_url": "https://drive.google.com/uc?export=view&id=1CYURN_LuyaB9QmaVCpIStS1VvjfjQksw",  # Masukkan link Google Drive foto Kak Farhanah di sini (jika kosong "", otomatis tampil avatar sakura estetik)
        }

        # FOTO 13 ANGGOTA KELOMPOK 02 JACOBI
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X2KwiLJ1v2Gvc_qN_6_m3ZSZbXcVdkkl",
            "https://drive.google.com/uc?export=view&id=1DtO2eY0GOsxoaVHQb5kwfI9UOv7NoBW4",
            "https://drive.google.com/uc?export=view&id=1fR93yciuJ9ZKr07WJSFW3POJusDkiVI9",
            "https://drive.google.com/uc?export=view&id=1FeCH9VKK6xSXyDOlarBJsz6upKpZkKw6",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1ldYVGXEoWrMVi_QEcTB27_3g9JNVco-R",
            "https://drive.google.com/uc?export=view&id=1DGsviu96SH9ELmkhlNT3c2eVzMorb2do",
            "https://drive.google.com/uc?export=view&id=1Egnh5rSF6GJZdMeEp0Y0rYMM2n_Ja9Bg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1HshxbkzrYbq3cZISXpWunElyB0lCPsCf",
        ]

        # BIODATA 13 ANGGOTA KELOMPOK 02 JACOBI (2 Pemimpin: Ketua/Palu & Wakil/Bulu + 11 Anggota)
        data_list = [
            {
                "nama": "Dandy Romansyah",
                "sebagai": "Palu",
                "nim": "125450006",
                "fun_fact": "Fans Bernadya nomor 1 sedunia dengan jumlah mendengarkan 45.868 menit",
                "motto_hidup": "Pergi keluar untuk mencari referensi, lalu kembali untuk relevansi",
            },
            {
                "nama": "Dea Febryana",
                "sebagai": "Bulu",
                "nim": "125450058",
                "fun_fact": "Kalo nonton drakor atau film harus yg sad ending",
                "motto_hidup": "Let them, it will pass, time will tell",
            },
            {
                "nama": "Krisna Alviansyah",
                "sebagai": "Anggota",
                "nim": "125450089",
                "fun_fact": "Suka ngoleksi photocard JKT48 dan Board game",
                "motto_hidup": "Sekarang atau tidak sama sekali, dan cobalah terus belum gila kan?",
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
                "motto_hidup": "Lakukan apa yang kamu pikirkan, pikirkan apa yang kamu lakukan",
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
                "fun_fact": "Clumsy girl",
                "motto_hidup": "Jangan lupakan Tuhan, Orang tua, dan Tujuan kita",
            },
            {
                "nama": "M.Ramadhan Bagus Ar-Rahman",
                "sebagai": "Anggota",
                "nim": "125450087",
                "fun_fact": "Di Ruqyah 5x",
                "motto_hidup": "I'm not a winner, but I'm not a failure too",
            },
            {
                "nama": "Aura Krisna Azzira",
                "sebagai": "Anggota",
                "nim": "125450119",
                "fun_fact": "Semester 2 kecelakaan 3x",
                "motto_hidup": "Biarlah langkahku membentur batu, daripada mati rasa karena ragu",
            },
            {
                "nama": "Riva Septia Nanda",
                "sebagai": "Anggota",
                "nim": "125450114",
                "fun_fact": "Sarapan = bikin maag kambuh",
                "motto_hidup": "I'm not in a rush, I'm on my path",
            },
            {
                "nama": "Dhani Harianto Pranata",
                "sebagai": "Anggota",
                "nim": "125450076",
                "fun_fact": "Suka nonton kartun Doraemon",
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
        # Menampilkan langsung galeri About Us
        render_polaroid_about_us(gambar_urls, data_list, mentor_data=mentor_data)

    about_page()
