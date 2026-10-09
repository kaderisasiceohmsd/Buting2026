import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

# Bagian judul halaman utama
st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)


# ==========================================
#      SUNTIKAN CSS UNTUK BORDER CARD 
# ==========================================
st.markdown("""
<style>
    /* Mengatur border kontainer (card) biodata agar melengkung, berwarna, dan berbayang halus */
    div[data-testid="stVerticalBlockBorderedTest"] {
        background-color: #ffffff !important;
        border: 2px solid #5C5C9C !important;  /* Warna border ungu lavender */
        border-radius: 16px !important;        /* Sudut melengkung */
        padding: 30px !important;              /* Jarak dari border ke konten di dalamnya */
        box-shadow: 0 6px 18px rgba(92, 92, 156, 0.15) !important; /* Efek bayangan */
        margin-bottom: 30px !important;       /* Jarak antar kartu kating */
    }
    
    /* Styling agar gambar melengkung alami dan memiliki bayangan lembut */
    img {
        border-radius: 12px !important;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1) !important;
        margin-bottom: 15px !important;
    }
    
    /* Merapikan jarak teks di dalam kartu */
    .stMarkdown p {
        line-height: 1.8;
        font-size: 16px;
        margin-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
#      FUNGSI UTAMA (Jangan diubah logikanya)
# ==========================================
@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(f"Gagal memuat gambar: {url}")
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error memuat gambar: {e}")
        return None

# Diubah sedikit agar menggunakan st.container(border=True)
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Membungkus SEMUA isi biodata per orang dalam satu st.container dengan border=True
        with st.container(border=True):
            # Menampilkan gambar di tengah-tengah kolom kontainer
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image(img, use_container_width=True)

            if i < len(data_list):
                # Menampilkan biodata dengan label bercetak tebal (bold)
                st.markdown(f"### **{data_list[i]['nama']}**")
                st.markdown(f"**NIM**: `{data_list[i]['nim']}`")
                st.markdown(f"**Umur**: {data_list[i]['umur']}")
                st.markdown(f"**Asal**: {data_list[i]['asal']}")
                st.markdown(f"**Alamat**: {data_list[i]['alamat']}")
                st.markdown(f"**Hobbi**: {data_list[i]['hobbi']}")
                st.markdown(f"**Sosial Media**: {data_list[i]['sosmed']}")
                st.markdown(f"**Kesan**: {data_list[i]['kesan']}")
                st.markdown(f"**Pesan**: {data_list[i]['pesan']}")
                
    st.write("Semua gambar telah dimuat!")


# ==========================================
#      MENU UTAMA & DATA (Boleh diubah)
# ==========================================
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan", "Baleg", "Senator", "Departemen PSDA", 
            "Departemen MIKFES", "Departemen Eksternal", 
            "Departemen Internal", "Departemen SSD", "Departemen Medkraf"
        ],
        icons=["people-fill"]*9,
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#ffffff",
                "border-radius": "10px",
                "box-shadow": "0 2px 5px rgba(0,0,0,0.1)",
                "margin-bottom": "25px"
            },
            "icon": {"color": "#5C5C9C", "font-size": "14px"},
            "nav-link": {
                "font-size": "12px", 
                "text-align": "center", 
                "margin": "0px",
                "padding": "10px 5px", 
                "--hover-color": "#e0e0f8",
            },
            "nav-link-selected": {
                "background-color": "#5C5C9C", 
                "font-weight": "bold",
                "color": "white"
            },
        },
    )
    return selected

menu = streamlit_menu()

if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xGPANYdh1va2y4_fUP0WdBnA1xDfB2Xb",
            "https://drive.google.com/uc?export=view&id=1CZuWR8cgBUVwATr1WrMIpsUfXDrh3N4b",
            "https://drive.google.com/uc?export=view&id=1rGKMfosDCQltl41Sz2ehjEUQV3LAaw8K",
            "https://drive.google.com/uc?export=view&id=1A9_GD_ng31Z0eTg1uvrwEUQFq-K-b4dL",
            "https://drive.google.com/uc?export=view&id=1fTovPjdfQCSGBXSg_viryFMm8yWEVGvc",
            "https://drive.google.com/uc?export=view&id=1bDcokqXsfus5IqecUG12RU9PS4ISZn4F",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya saya bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya saya bisa mencontoh hal baik dari kakak."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya saya bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya saya bisa tumbuh seperti bang fajar, terimakasih bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()