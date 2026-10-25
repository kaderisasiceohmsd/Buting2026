import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64
import html
import re
import os
from pathlib import Path
from urllib.parse import urlparse, parse_qs

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Mengubah background utama menjadi terang (krem/beige) seperti foto pertama */
    .stApp {
        background-color: #F8F5F2;
        color: #000000; 
    }

    /* Buat header transparan agar tombol sidebar tetap ada */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* Pastikan warna ikon tombol penutup tab menjadi gelap agar terlihat di background terang */
    [data-testid="collapsedControl"] {
        color: #bd411b !important;
    }

    /* Memberikan warna solid pada sidebar (Oranye dari foto kedua) */
    [data-testid="stSidebar"] {
        background-color: #bd411b !important;
    }
    
    /* Memastikan teks di dalam sidebar berwarna putih */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Memaksa elemen teks di dalam tab menjadi gelap karena background sekarang terang */
    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: #000000 !important;
    }
    
    /* Mengubah warna garis bawah pada tab yang sedang aktif menggunakan aksen oranye */
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: #bd411b !important;
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
                "color": "black",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#e3651e", "color": "white"},
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
        
        # Menggunakan langsung fungsi load_image dengan URL yang sudah teruji di atas
        foto_kelompok_url = "https://drive.google.com/uc?export=view&id=1dP4Em_9mhiLc8DxjcHDX1glRZD39y8WB"
        img_bg = load_image(foto_kelompok_url)
        
        img_b64 = ""
        if img_bg is not None:
            buffered = BytesIO()
            img_bg.convert("RGB").save(buffered, format="JPEG")
            img_b64 = base64.b64encode(buffered.getvalue()).decode()
        
        # 1. HERO SECTION (Dengan z-index dan posisi absolut yang benar agar overlay & teks muncul)
        parallax_html = f"""
        <div style="
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)), url('data:image/jpeg;base64,{img_b64}');
            height: 550px;
            background-size: cover;
            background-position: 35% center;
            background-repeat: no-repeat;
            border-radius: 16px;
            margin-bottom: 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        ">
            <h1 style="color: white; font-size: 3.5rem; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); text-align: center; padding: 20px; margin: 0;">
                Hola, welcome to GreedyCuwiKuki!
            </h1>
        </div>
        """
        st.markdown(parallax_html, unsafe_allow_html=True)
        
        # Teks Visi & Misi Kelompok
        st.markdown(
            """<div style="text-align: center; font-size: 1.1rem; margin: 0 10%; line-height: 1.6;">
            Satu tim dengan satu visi: Pantang pulang sebelum selesai, pantang menyerah sebelum optimal! 
            Kami anggota Greedy menganut sifat greedy yaitu selalu haus akan proses belajar dan eksplorasi. Di setiap langkah, kami selalu cari cara terbaik 
            untuk berkembang bersama!!<br><br>
            <b style="color: #bd411b; font-size: 1.2rem;">Greedy, Grab the best, Reach the TOP!!</b>
            </div>""",
            unsafe_allow_html=True,
        )
        
        st.markdown("<hr style='margin: 40px 0;'>", unsafe_allow_html=True)
        
        # 2. ZIG-ZAG GALLERY SECTION (Kilas Balik Perjalanan Kami)
        st.markdown("<h2 class='centered-title' style='margin-bottom: 40px;'>Kilas Balik Perjalanan Kami</h2>", unsafe_allow_html=True)
        
        def img_to_b64(img):
            if img is None: return ""
            buf = BytesIO()
            img.convert("RGB").save(buf, format="JPEG")
            return base64.b64encode(buf.getvalue()).decode()

        momen_list = [
            {
                "judul": "Kami",
                "deskripsi": "Satu orang bisa berjalan cepat, tapi bersama-sama kita bisa melangkah jauh. Inilah kami kumpulan satu orang yang saling mendukung.",
                "url": "https://drive.google.com/uc?export=view&id=1Ht5eDNnenv5kNSWGOL2o72PfwaNB_cbB"
            },
            {
                "judul": "First Meet Kelompok",
                "deskripsi": "Awal mula pertemuan seru kita di mana semua cerita, canda tawa, dan kekompakan pertama kali diukir bersama.",
                "url": "https://drive.google.com/uc?export=view&id=16DMsInK6W9uWK2Gi3u4AumUREqAwl6A_"
            },
            {
                "judul": "Langkah Pertama",
                "deskripsi": "Langkah awal penuh tantangan dan semangat baru dalam menjalani rangkaian proses kaderisasi bersama tim tercinta.",
                "url": "https://drive.google.com/uc?export=view&id=1fSAXH0QwK2nQVcy_IGzVs7qtDW1TsYLE"
            },
            {
                "judul": "Kerja Kelompok",
                "deskripsi": "Sesi lembur produktif penuh perjuangan, diskusi panjang, dan kerja sama tim yang solid untuk hasil yang optimal.",
                "url": "https://drive.google.com/uc?export=view&id=1EMMDL1QuIvIALCNzr6mvbwk5ZVkbUrve"
            },
            {
                "judul": "Keseruan & Kebersamaan",
                "deskripsi": "Kenangan manis di luar jam tugas yang merekatkan ikatan persahabatan kita sebagai satu keluarga besar Greedy.",
                "url": "https://drive.google.com/uc?export=view&id=1dP4Em_9mhiLc8DxjcHDX1glRZD39y8WB"
            },
        ]

        st.markdown("""
        <style>
        .wix-card-text {
            background-color: #F3EFEA;
            border-radius: 16px;
            padding: 40px;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            margin-bottom: 25px;
        }
        .wix-card-img {
            border-radius: 16px;
            overflow: hidden;
            height: 320px;
            margin-bottom: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        .wix-card-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        </style>
        """, unsafe_allow_html=True)

        for idx, item in enumerate(momen_list):
            img = load_image(item["url"])
            img_b64_momen = img_to_b64(img)
            
            text_block = f"""
            <div class="wix-card-text">
                <h3 style="color: #1a1a1a; margin-bottom: 15px; font-size: 1.8rem;">{item['judul']}</h3>
                <p style="color: #555555; font-size: 1rem; line-height: 1.6; margin: 0;">{item['deskripsi']}</p>
            </div>
            """
            
            img_block = f"""
            <div class="wix-card-img">
                <img src="data:image/jpeg;base64,{img_b64_momen}">
            </div>
            """
            
            col1, col2 = st.columns(2, gap="large")
            
            if idx % 2 == 0:
                with col1:
                    st.markdown(img_block, unsafe_allow_html=True)
                with col2:
                    st.markdown(text_block, unsafe_allow_html=True)
            else:
                with col1:
                    st.markdown(text_block, unsafe_allow_html=True)
                with col2:
                    st.markdown(img_block, unsafe_allow_html=True)

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