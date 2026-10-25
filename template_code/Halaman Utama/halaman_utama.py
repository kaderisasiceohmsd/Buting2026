import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Mengubah background utama menjadi gradasi */
    .stApp {
        background: linear-gradient(to bottom right, #ff9a22, #e14627);
        color: white; 
    }

    /* Buat header transparan agar tombol sidebar tetap ada */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Pastikan warna ikon tombol penutup tab menjadi putih agar terlihat */
    [data-testid="collapsedControl"] {
        color: white !important;
    }

    /* Memberikan warna solid pada sidebar */
    [data-testid="stSidebar"] {
        background-color: #bd411b !important;
    }
    
    /* Memastikan teks di dalam sidebar berwarna putih */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Memaksa elemen teks di dalam tab menjadi putih */
    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: white !important;
    }
    
    /* Mengubah warna garis bawah pada tab yang sedang aktif */
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: white !important;
    }

    /* Animasi gambar */
    .gambar-timbul {
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        cursor: pointer;
    }
    .gambar-timbul:hover {
        transform: translateY(-8px) scale(1.03); 
        box-shadow: 0 10px 20px rgba(0,0,0,0.3); 
    }
    </style>
    """,
    unsafe_allow_html=True
)

def image_to_html_link(img, url_ig, img_width="100%"):
    buffered = BytesIO()
    img = img.convert("RGB")
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    html_code = f"""
    <div style="width: {img_width};">
        <a href="{url_ig}" target="_blank" style="text-decoration: none;">
            <img src="data:image/jpeg;base64,{img_str}" class="gambar-timbul">
        </a>
    </div>
    """
    return html_code

# JANGAN DIUBAH 
@st.cache_data
def load_image(url):
    try:
        response = requests.get(url)
        if 'text/html' in response.headers.get('Content-Type', ''):
            return None
        
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        return img
    except Exception as e:
        return None

def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    if not images or not data_list:
        return

    st.markdown("### Mentor")
    mentor_col1, mentor_col2 = st.columns([1, 3.5]) 
    with mentor_col1:
        st.markdown(image_to_html_link(images[0], data_list[0].get('ig', '#'), img_width="100%"), unsafe_allow_html=True)
    with mentor_col2:
        st.subheader(data_list[0]['nama'])
        st.write(f"**Sebagai:** {data_list[0]['sebagai']}")
        st.write(f"**NIM:** {data_list[0]['nim']}")
        st.write(f"**Fun Fact:** {data_list[0]['fun_fact']}")
        st.write(f"**Motto Hidup:** {data_list[0]['motto_hidup']}")
        
    st.markdown("---")
    st.markdown("### Anggota Kelompok")
    
    num_cols = 4
    cols = st.columns(num_cols, gap="large") 
    
    for i in range(1, len(images)):
        col_idx = (i - 1) % num_cols 
        
        with cols[col_idx]:
            if i < len(data_list):
                st.markdown(image_to_html_link(images[i], data_list[i].get('ig', '#'), img_width="80%"), unsafe_allow_html=True)
                
                st.markdown(f"**{data_list[i]['nama']}**")
                st.caption(f"{data_list[i]['sebagai']}")
                st.write(f"NIM: {data_list[i]['nim']}")
                st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
                st.write(f"Motto: {data_list[i]['motto_hidup']}")
            st.write("") 

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

# Fungsi baru untuk logo atas dan bawah
def layout_logos_atas_bawah(url_1, url_2):
    # Membagi menjadi 3 kolom: kiri (kosong), tengah (untuk logo), kanan (kosong)
    # Anda bisa mengatur rasio [2, 1.5, 2] untuk memperbesar/memperkecil ukuran logonya
    c1, c2, c3 = st.columns([1.5, 1, 1.5]) 
    
    with c2:
        # Menampilkan logo pertama di atas
        st.image(load_image(url_1), use_container_width=True)
        # Menampilkan logo kedua tepat di bawahnya
        st.image(load_image(url_2), use_container_width=True)

# Memanggil fungsi
layout_logos_atas_bawah(url, url1)

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
            "nav-link-selected": {"background-color": "#e3651e"},
        },
    )
    return selected

menu = streamlit_menu()

if menu == "Home":

    def layout(url):
        col1, col2, col3 = st.columns([2, 1.5, 2])  
        with col2:
            st.image(load_image(url), use_container_width=True)
    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Hola, welcome to GreedyCuwiKuki!</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Satu tim dengan satu visi: Pantang pulang sebelum selesai, pantang menyerah sebelum optimal! 
            Kami anggota Greedy menganut sifat greedy yaitu selalu haus akan proses belajar dan eksplorasi. Di setiap langkah, kami selalu cari cara terbaik 
            untuk berkembang bersama!!
             
            Greedy, Grab the best, Reach  the TOP!!</div>""",
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
            "https://drive.google.com/uc?export=view&id=1VHIRvPCdaDsop3n_T_J7gVKBQbhSKt5O",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1OLYzTHsfElGfjBXvzUUoMg24zf8W7QD9",
            "https://drive.google.com/uc?export=view&id=1C6pkVy5sjsffTqdeOSv1M5zff_1zZL8f",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1jflu-Tr_51LeSApGIa6cLeiSVWIrpQ6d",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1rJgFY2x3IdAR-Ps-qmX_hyi2exeAHOi8",
            "https://drive.google.com/uc?export=view&id=1TeIvYb5pBbI8m4rFIAlKZ7ZZwZT4nZ8Q",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        
        data_list = [
            {
                "nama": "Andra Ilham Bintang",
                "sebagai": "Mentor",
                "nim": "124450060",
                "fun_fact": "Mau tidur jam berapapu tetep bangun jam 7 pagi",
                "motto_hidup": "Tidak ada penyesalan, hanya ada pelajaran",
                "ig": "https://www.instagram.com/andra.lhm?utm_source=ig_web_button_share_sheet&obrf=ZDNlZDc0MzIxNw==" 
            },
            {
                "nama": "Andrew Chayadi",
                "sebagai": "Pak Lurah",
                "nim": "125450067",
                "fun_fact": "Kalo cape suka ngehalu",
                "motto_hidup": "...",
                "ig": "https://www.instagram.com/drewwszz?utm_source=ig_web_button_share_sheet&dlrf=ZDNlZDc0MzIxNw=="
            },
            {
                "nama": "Wardah Aliya Lubis",
                "sebagai": "Bu Lurah",
                "nim": "1254500121",
                "fun_fact": "Ska ngajak ngobrol benda mati",
                "motto_hidup": "Tetap jadikan dunia di tanganmu, akhirat di tangan mu",
                "ig": "https://www.instagram.com/aliyaaalbs?utm_source=ig_web_button_share_sheet&psln=ZDNlZDc0MzIxNw=="
            },
            {
                "nama": "Faiz Hikmawan",
                "sebagai": "Anggota",
                "nim": "125450013",
                "fun_fact": "Gap year karna lupa pencet finalisasi data",
                "motto_hidup": "Coba semuanya dulu, kalo ga ccocok baru skip",
                "ig": "https://www.instagram.com/izhik__/"
            },
            {
                "nama": "Valen Uswatun Fauziyah Putri",
                "sebagai": "Anggotaa",
                "nim": "125450014",
                "fun_fact": "",
                "motto_hidup": "Majulah dengan persiapan agar turun dengan penghormatan",
                "ig": "https://www.instagram.com/_vlntz02_?utm_source=ig_web_button_share_sheet&dlrf=ZDNlZDc0MzIxNw=="
            },
            {
                "nama": "Zharifa Azizah Yudistira",
                "sebagai": "Anggotaa",
                "nim": "12545044",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/zhrfazia/"
            },
            {
                "nama": "Theofani Saragih",
                "sebagai": "Anggotaa",
                "nim": "125450046",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/fanii.ly_?utm_source=ig_web_button_share_sheet&dlrf=ZDNlZDc0MzIxNw=="
            },
            {
                "nama": "Muchamad Fahrell",
                "sebagai": "Anggotaa",
                "nim": "125450077",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/mmuchaell/"
            },
            {
                "nama": "Nickolas Filbert Kartika",
                "sebagai": "Anggotaa",
                "nim": "125450081",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/nickolas_303/"
            },
            {
                "nama": "Muhammad Ayyas Haidar Farros",
                "sebagai": "Anggotaa",
                "nim": "125450105",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/yyassst/"
            },
            {
                "nama": "Rasya Zahira Umardi",
                "sebagai": "Anggotaa",
                "nim": "125450110",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/citydoyxl?utm_source=ig_web_button_share_sheet&exln=ZDNlZDc0MzIxNw=="
            },
            {
                "nama": "Nadia Callysta Putri",
                "sebagai": "Anggotaa",
                "nim": "125450111",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu keles",
                "ig": "https://www.instagram.com/nadiaclyst/"
            },
            {
                "nama": "Muhammad Alifatih Freedom Haq",
                "sebagai": "Anggotaa",
                "nim": "125450120",
                "fun_fact": "nyemilin es bata, kiko",
                "motto_hidup": "jalanin dulu kele",
                "ig": "https://www.instagram.com/thefreedomhaq/"
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()