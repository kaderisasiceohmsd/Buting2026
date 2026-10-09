import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img

@st.cache_data
def get_image_base64(url):
    try:
        response = requests.get(url)
        img_b64 = base64.b64encode(response.content).decode("utf-8")
        # Content-Type could be different but data:image/jpeg works for most basic rendering, 
        # or we can use data:image/png. Let's just use data:image/png.
        return f"data:image/png;base64,{img_b64}"
    except Exception:
        return url


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

# ===== CSS Tambahan untuk mempercantik (tidak mengubah fungsi di atas) =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

    .stApp {
        font-family: 'Poppins', sans-serif;
    }

    /* Hero Header */
    .hero-container {
        text-align: center;
        padding: 1.5rem 1rem 0.5rem 1rem;
    }
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.8em;
        font-weight: 900;
        background: linear-gradient(135deg, #ffd740, #ffab40, #ff6e40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 3px;
        margin-bottom: 0;
        animation: shimmer 3s ease-in-out infinite;
    }
    @keyframes shimmer {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.2); }
    }
    .hero-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2em;
        color: #b0bec5;
        font-weight: 300;
        letter-spacing: 2px;
        margin-top: 0.3rem;
    }

    /* Divider */
    .fancy-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #ffd740, #ffab40, transparent);
        margin: 1.5rem auto;
        max-width: 400px;
        border: none;
    }

    /* Puisi Box */
    .puisi-container {
        max-width: 700px;
        margin: 2rem auto;
        padding: 2rem 2.5rem;
        background: linear-gradient(135deg, rgba(255,215,64,0.06), rgba(255,171,64,0.06));
        border-left: 4px solid #ffd740;
        border-radius: 0 16px 16px 0;
    }
    .puisi-text {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.05em;
        line-height: 2;
        color: #cfd8dc;
        text-align: center;
    }
    .puisi-author {
        text-align: right;
        color: #ffd740;
        font-weight: 600;
        margin-top: 1rem;
        font-size: 0.9em;
    }

    /* Section Title */
    .section-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2em;
        font-weight: 700;
        margin: 1.5rem 0 0.3rem 0;
        background: linear-gradient(90deg, #ffd740, #ffab40);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .section-desc {
        text-align: center;
        color: #90a4ae;
        font-size: 0.95em;
        margin-bottom: 1.5rem;
    }

    /* Home Desc */
    .home-desc {
        text-align: justify;
        font-size: 1em;
        line-height: 1.8;
        color: #cfd8dc;
        max-width: 750px;
        margin: 0 auto;
        padding: 0 1rem;
    }

    /* Member Card */
    .member-card {
        background: linear-gradient(145deg, #1a1a2e, #1f1f38);
        border: 1px solid rgba(255,215,64,0.12);
        border-radius: 16px;
        padding: 1.5rem 1rem;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 1rem;
        min-height: 340px;
    }
    .member-card:hover {
        transform: translateY(-6px);
        border-color: rgba(255,215,64,0.4);
        box-shadow: 0 12px 40px rgba(255,215,64,0.1);
    }
    .member-avatar {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid rgba(255,215,64,0.3);
        margin-bottom: 0.8rem;
    }
    .member-card:hover .member-avatar {
        border-color: #ffd740;
    }
    .member-name {
        font-size: 1.05em;
        font-weight: 700;
        color: #e0e6ed;
        margin-bottom: 0.2rem;
    }
    .member-role {
        font-size: 0.82em;
        color: #ffd740;
        font-weight: 500;
        margin-bottom: 0.4rem;
    }
    .member-nim {
        font-size: 0.78em;
        color: #78909c;
        margin-bottom: 0.6rem;
    }
    .member-detail {
        font-size: 0.8em;
        color: #b0bec5;
        line-height: 1.6;
        text-align: left;
        padding: 0.5rem;
        background: rgba(0,0,0,0.15);
        border-radius: 10px;
    }
    .detail-label {
        color: #ffd740;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class='hero-container'>
    <h1 class='hero-title'>WEBSITE KATING</h1>
    <p class='hero-subtitle'>CEO HMSD Adyatama ITERA 2026</p>
</div>
""", unsafe_allow_html=True)


# ===== LOGO HIMPUNAN & PSDA (Logo himpunan di atas PSDA) =====
url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 1, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_container_width=True)
    with col3:
        st.write("")  # Menyisakan kolom kosong


# Menampilkan logo himpunan di atas logo PSDA
layout(url)
layout(url1)

st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#ffd740", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "rgba(255,215,64,0.08)",
            },
            "nav-link-selected": {"background-color": "#ffd740", "color": "#0f0f1a"},
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
            "<h1 class='section-title'>Kami Adalah JORDAN!</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div class="home-desc">Nama kelompok kami terinspirasi dari <b>Mic  hael I. Jordan</b>, salah satu tokoh pelopor paling 
berpengaruh di dunia Data Science dan Machine Learning.
Seperti halnya <b>Jordan Network</b>-arsitektur Recurrent Neural Network yang belajar dari feedback masa lalu 
untuk memberikan hasil terbaik di masa depan-kelompok kami berdedikasi untuk terus belajar, 
beradaptasi, dan mengolah data menjadi wawasan (<i>insight</i>) yang bernilai.
Kami terdiri dari <b>13 orang</b> yang siap mengeksplorasi dunia data, analitik, dan kecerdasan buatan.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=15IbaUl-cN8juWyMiVYjoAWhLlTpw5H7N"
        layout(foto_kelompok)

        st.markdown("""
        <div class='puisi-container'>
            <div class='puisi-text'>
                Tiga belas jiwa, satu tekad membara,<br>
                Berjalan bersama di lorong data yang nyata.<br>
                Dari angka-angka yang diam membisu,<br>
                Kami merangkai cerita, menemukan makna yang tak terlihat mata.<br><br>
                Seperti jaringan yang terus belajar,<br>
                Dari setiap kesalahan, kami tumbuh besar.<br>
                Jordan bukan sekadar nama,<br>
                Ia adalah janji, bahwa kami tak pernah berhenti bermimpi.<br><br>
                Di setiap baris kode yang kami tulis,<br>
                Di setiap insight yang kami temukan,<br>
                Tersimpan kenangan yang tak lekang,<br>
                Dari tiga belas hati yang saling menguatkan.
            </div>
            <div class='puisi-author'>- Kelompok 01 Jordan, CEO HMSD Adyatama 2026 🌟</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='section-title'>About Us</h1>", unsafe_allow_html=True)
        st.markdown("<p class='section-desc'>Kenalan yuk sama 13 anggota kelompok Jordan! 🚀</p>", unsafe_allow_html=True)
        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

        default_foto = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

        data_list = [
            {
                "nama": "Bintang Mahardika",
                "sebagai": "Palu",
                "nim": "125450106",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",  # ← isi link Google Drive foto sendiri (kosong = pakai foto default)
            },
            {
                "nama": "Sayyidina Najwa Syahra",
                "sebagai": "Bulu",
                "nim": "125450002",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Muhammad Rafli Raditya",
                "sebagai": "Anggota",
                "nim": "125450095",
                "fun_fact": "Aku hidup dan semua orang hidup karena ku",
                "motto_hidup": "Isi motto di sini",
                "foto": "https://drive.google.com/uc?export=view&id=1eRqS2Dm2UYeKTpmixAU5WmjmWMqqW1co",
            },
            {
                "nama": "M Abyan Alghaniyyu",
                "sebagai": "Anggota",
                "nim": "125450104",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Rahmad Bayu Ridho",
                "sebagai": "Anggota",
                "nim": "125450093",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Mojes Wijaya",
                "sebagai": "Anggota",
                "nim": "125450094",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Iva Aulia Sofia",
                "sebagai": "Anggota",
                "nim": "125450062",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Astrit Aisyah Rahmi",
                "sebagai": "Anggota",
                "nim": "125450036",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Septi Widia Arin",
                "sebagai": "Anggota",
                "nim": "12545005",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Fildzah Cahya Kamila",
                "sebagai": "Anggota",
                "nim": "125450040",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Lintar Abhinaya Putra Zulmi",
                "sebagai": "Anggota",
                "nim": "125450064",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Ahda Nabiwa",
                "sebagai": "Anggota",
                "nim": "125450069",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
            {
                "nama": "Bening Arianti",
                "sebagai": "Anggota",
                "nim": "154500068",
                "fun_fact": "Isi fun fact di sini",
                "motto_hidup": "Isi motto di sini",
                "foto": "",
            },
        ]


        for row_start in range(0, len(data_list), 3):
            cols = st.columns(3)
            for i, col in enumerate(cols):
                idx = row_start + i
                if idx < len(data_list):
                    m = data_list[idx]
                    foto_url = m.get("foto", "") or default_foto
                    foto_b64 = get_image_base64(foto_url)
                    with col:
                        st.markdown(f"""
                        <div class='member-card'>
                            <img src='{foto_b64}' class='member-avatar' alt='{m["nama"]}'
                                 onerror="this.src='https://ui-avatars.com/api/?name={m["nama"].replace(" ", "+")}&background=1a1a2e&color=ffd740&size=150&bold=true'">
                            <div class='member-name'>{m["nama"]}</div>
                            <div class='member-role'>✦ {m["sebagai"]}</div>
                            <div class='member-nim'>NIM: {m["nim"]}</div>
                            <div class='member-detail'>
                                <span class='detail-label'>🎯 Fun Fact:</span> {m["fun_fact"]}<br>
                                <span class='detail-label'>💬 Motto:</span> {m["motto_hidup"]}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

        st.markdown("<div class='fancy-divider'></div>", unsafe_allow_html=True)

    about_page()
