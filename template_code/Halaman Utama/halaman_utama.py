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
def display_images_two_per_row(gambar_urls, data_list):
    jumlah_data = max(len(gambar_urls), len(data_list))

    for start in range(0, jumlah_data, 2):
        col1, col2 = st.columns(2)

        kolom = [col1, col2]

        for offset, col in enumerate(kolom):
            i = start + offset

            if i >= jumlah_data:
                continue

            with col:
                # Menampilkan foto anggota
                if i < len(gambar_urls):
                    with st.spinner(f"Memuat foto anggota {i + 1}..."):
                        img = load_image(gambar_urls[i])

                    st.image(img, use_container_width=True)

                # Menampilkan biodata anggota
                if i < len(data_list):
                    data = data_list[i]

                    st.markdown(f"### {data['nama']}")
                    st.write(f"**Sebagai:** {data['sebagai']}")
                    st.write(f"**NIM:** {data['nim']}")
                    st.write(f"**Fun Fact:** {data['fun_fact']}")
                    st.write(f"**Motto Hidup:** {data['motto_hidup']}")

                st.divider()
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
            "container": {
                "padding": "5px",
                "background-color": st.get_option("theme.backgroundColor"),
                "border-radius": "10px",
            },
            "icon": {
                "color": st.get_option("theme.textColor"),
                "font-size": "19px",
            },
            "nav-link": {
                "background-color": st.get_option("theme.backgroundColor"),
                "font-size": "16px",
                "font-weight": "600",
                "text-align": "center",
                "margin": "0px 5px",
                "color": st.get_option("theme.textColor"),
                "--hover-color": st.get_option("theme.secondaryBackgroundColor"),
            },
            "nav-link-selected": {
                "background-color": st.get_option("theme.sidebar.secondaryBackgroundColor"),
                "color": st.get_option("theme.sidebar.textColor"),
                "font-weight": "600",
            },
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
            """<div style="text-align: justify;">Pandas, "A"nya apa? ASIK. Kelompok 6 di Kaderisasi CEO HMSD Adyatama ITERA.
            Berisikan berbagai macam orang unik yang berasal dari berbagai daerah. Ada Minang, ada Jawa, ada Lampung, ada Batak,
            namun semua perbedaan itu yang membuat kelompok ini unik, tapi seluruhnya juga punya tujuan yang sama yaitu menjadi 
            lebih baik melalui Kaderisasi ini.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=15_GjrUPEJAT5kQh4hWcxLTr7cID059TL"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Kelompok ini sebenarnya tidak sepenuhnya saling tidak mengenal dari awal.
            Beberapa orang sudah menjadi teman dekat dari awal, namun tidak menutup untuk menjadi lebih terbuka,
            di kelompok ini kami berubah menjadi lebih baik dan terus berkembang.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1rCHpAW7n7XM5J5-78wNuHXaD4B2qr5P8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=10hH3ZahcCSye-uxU9INHp_BOQUbu-08T",
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
                "nama": "Muhammad Haikal Farros",
                "sebagai": "Pak Lurah",
                "nim": "125450049",
                "fun_fact": "Minum espresso 6 shoots (muntah dikit), waktu kecil pernah jatuh di septitank",
                "motto_hidup": "im still standing like a soldier, that is how i survive",
            },
            {
                "nama": "Resti Amanda Ritonga",
                "sebagai": "Bu Lurah",
                "nim": "125450126",
                "fun_fact": "Setiap hari dengar lagu Hindia",
                "motto_hidup": "Hidup hanya sekali, lakukan yang terbaik",
            },
            {
                "nama": "Ridho Bitsiqah Akila Hartono",
                "sebagai": "Anaknya pak lurah",
                "nim": "125450092",
                "fun_fact": "Kalau semingguan ga nyemil manis jadi badmoodan",
                "motto_hidup": "Every step you took there's something to take",
            },
            {
                "nama": "Mayang Nuraini",
                "sebagai": "Anggota",
                "nim": "125450131",
                "fun_fact": "Takut sama jarum suntik",
                "motto_hidup": "Hiduplah seperti Gojo Satoru, tetap semangat walau masalah seberat domain expansion",
            },
            {
                "nama": "Mas Renno Octaviano AR",
                "sebagai": "Anggota",
                "nim": "125450079",
                "fun_fact": "Pernah di tag McD",
                "motto_hidup": "Pilihan sulit memerlukan keyakinan yang kuat",
            },
            {
                "nama": "Zaky Firmansyah",
                "sebagai": "Anggota",
                "nim": "125450027",
                "fun_fact": "Kesurupan kalau liat bulan",
                "motto_hidup": "Fokus pada solusi bukan masalah",
            },
            {
                "nama": "Ivana Ikhsan",
                "sebagai": "Anggota",
                "nim": "125450080",
                "fun_fact": "Suka nonton podcast horor yang banyak dokum asli tapi padahal penakut parah",
                "motto_hidup": "Melambat tidak sama dengan mengalah",
            },
            {
                "nama": "Marcellinus Kevin",
                "sebagai": "Anggota",
                "nim": "125450054",
                "fun_fact": "G pernah pingsan, mimisan, kesurupan",
                "motto_hidup": "Mengalah bukan berarti kalah",
            },
            {
                "nama": "Citra Handayani Pakpahan",
                "sebagai": "Anggota",
                "nim": "125450102",
                "fun_fact": "Seringan rambut pendek dan minimal minum 5 botol Yakult seminggu",
                "motto_hidup": "Menjadi, bukan sekedar ada.",
            },
            {
                "nama": "Hasna Azwa Az Zahra",
                "sebagai": "Anggota",
                "nim": "125450034",
                "fun_fact": "Takut sama boneka",
                "motto_hidup": "Bloom at your own pace.",
            },
            {
                "nama": "",
                "sebagai": "Anggota",
                "nim": "",
                "fun_fact": "",
                "motto_hidup": "",
            },
        ]

        display_images_two_per_row(gambar_urls, data_list)

    about_page()
