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

    if not images or not data_list:
        return

    # --- TATA LETAK MENTOR (Data ke-1) ---
    st.markdown("### Mentor")
    # Menggunakan rasio 1:2 agar mirip dengan card atas di referensi
    mentor_col1, mentor_col2 = st.columns([1, 2]) 
    with mentor_col1:
        st.image(images[0], use_container_width=True)
    with mentor_col2:
        st.subheader(data_list[0]['nama'])
        st.write(f"**Sebagai:** {data_list[0]['sebagai']}")
        st.write(f"**NIM:** {data_list[0]['nim']}")
        st.write(f"**Fun Fact:** {data_list[0]['fun_fact']}")
        st.write(f"**Motto Hidup:** {data_list[0]['motto_hidup']}")
        
    st.markdown("---") # Garis pemisah
    st.markdown("### Anggota Kelompok")
    
    # --- TATA LETAK ANGGOTA (12 Data Selanjutnya) ---
    # Membuat grid 4 kolom sesuai dengan screenshot
    num_cols = 4
    cols = st.columns(num_cols)
    
    # Looping dimulai dari index 1 (karena index 0 sudah dipakai mentor)
    for i in range(1, len(images)):
        # Menentukan di kolom mana data akan ditempatkan
        col_idx = (i - 1) % num_cols 
        
        with cols[col_idx]:
            # Menampilkan Card Anggota
            st.image(images[i], use_container_width=True)
            if i < len(data_list):
                st.markdown(f"**{data_list[i]['nama']}**")
                st.caption(f"{data_list[i]['sebagai']}")
                st.write(f"NIM: {data_list[i]['nim']}")
                st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
                st.write(f"Motto: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
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
            "<h1 class='centered-title'>Hola, Welcome to GreedyCuwiKuki-!</h1>", unsafe_allow_html=True
        )
        
        st.markdown(
            """<div style="text-align: justify;">
            Satu tim dengan satu visi: pantang pulang sebelum selesai,
            pantang menyerah sebelum optimal!

            Kami anggota Greedy menganut sifat greedy, yaitu selalu haus
            akan proses belajar dan eksplorasi. Di setiap langkah, kami
            selalu mencari cara terbaik untuk berkembang bersama!

            Greedy, Grab the best, Reach the TOP!!
            </div>""",
            unsafe_allow_html=True,
        )

        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1rbivE1TuHa3baKFVMcQ2MV0AVto2Or-a",
            "https://drive.google.com/uc?export=view&id=1dzJTYgV_KVWQIsgJakqeBx-s5ntf0tSq",
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
                "nama": "Andra Ilham Bintang",
                "sebagai": "Mentor",
                "nim": "124450060",
                "fun_fact": "...",
                "motto_hidup": "...",
            },
            {
                "nama": "Andrew Chayadi",
                "sebagai": "Pak Lurah",
                "nim": "125450067",
                "fun_fact": "...",
                "motto_hidup": "...",
            },
            {
                "nama": "Wardah Aliya Lubis",
                "sebagai": "Bu Lurah",
                "nim": "1254500121",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Faiz Hikmawan",
                "sebagai": "Anggota",
                "nim": "125450013",
                "fun_fact": "nyemilin es bata",
                "motto_hidup": "mantap",
            },
            {
                "nama": "Valen Uswatun Fauziyah Putri",
                "sebagai": "Anggotaa",
                "nim": "125450014",
                "fun_fact": "nyemilin",
                "motto_hidup": "jalanin dulu aja",
            },
            {
                "nama": "Zharifa Azizah Yudistira",
                "sebagai": "Anggotaa",
                "nim": "12545044",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Theofani Saragih",
                "sebagai": "Anggotaa",
                "nim": "125450046",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Muchamad Fahrell",
                "sebagai": "Anggotaa",
                "nim": "125450077",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Nickolas Filbert Kartika",
                "sebagai": "Anggotaa",
                "nim": "125450081",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Muhammad Ayyas Haidar Farros",
                "sebagai": "Anggotaa",
                "nim": "125450105",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Rasya Zahira Umardi",
                "sebagai": "Anggotaa",
                "nim": "125450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Nadia Callysta Putri",
                "sebagai": "Anggotaa",
                "nim": "125450111",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
            },
            {
                "nama": "Muhammad Alifatih Freedom Haq",
                "sebagai": "Anggotaa",
                "nim": "125450120",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu kele",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()