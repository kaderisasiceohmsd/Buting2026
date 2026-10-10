import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    try:
        response = requests.get(
            url,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        st.write("URL:", url)
        st.write("Content-Type:", response.headers.get("Content-Type"))
        st.write("Status:", response.status_code)

        img = Image.open(BytesIO(response.content))
        img.load()
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))

        return img

    except Exception as e:
        st.error(f"Gagal memuat gambar: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Abang nya baik dan sangat menginspirasi saya, time management nya keren sehingga balance antara organisasi dan kuliah",  
                "pesan":"semangat kuliahnya lancar luncur TA nya bang"# 1
            },
            {
                "nama": "Muhammad  Aqil Ramadhan",
                "nim": "1223450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil111",
                "kesan": "JUJURR abang ini kerenn, gatau tapi keren banget",  
                "pesan":"semangat terus bang aqill"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi seruu dan asikk banget",  
                "pesan":"semangat terus kuliahnya kakak !"# 1
            },
             {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini seru dan baikk",  
                "pesan":"semangat kuliahnya bangg, dilancarin TA nyaa"# 1
            },
             {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya seruuuu bangettttttt",  
                "pesan":"semangat terussss kakkkkkk!"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaaemdhn",
                "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk",  
                "pesan":"semangat untuk mengejar S.Si.d kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
