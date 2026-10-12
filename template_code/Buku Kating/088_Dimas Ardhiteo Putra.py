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
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
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
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-O0PYQwKLb2hemdBhjrnMgFoPYatlw6T",
            "https://drive.google.com/uc?export=view&id=1H15DQzaSmo78aU2gWrfysKoOQOsO4zgh",
            "https://drive.google.com/uc?export=view&id=1lm9RQDR0eqeYvkLDkze_AsKqhiEMD7ga",
            "https://drive.google.com/uc?export=view&id=178yDYLTucGPL5HwwL-D0tzeVJlcSq7iO",
            "https://drive.google.com/uc?export=view&id=1TbqjmnrsOH8MwkMrLaiaCIrRJjLucOPk",
            "https://drive.google.com/uc?export=view&id=1frdlrJLufW0eP7gO05YjR2jHaOJx5tuM",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sektariatan HMSD",
                "hobbi": "push imo, mencuci",
                "sosmed": "@jars_mrp",
                "kesan": "Bang ginda ramahnya gak ketolongan, humble, adem liat bang ginda rasanya",  
                "pesan":"gass cumlaude bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau, Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Keren berkharisma",  
                "pesan":"Lulus tepat waktu ya bang"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "humble, ramah, baik",  
                "pesan":"Kak, senyum selalu ya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Cool, dan keliatan orang yang Sistematis",  
                "pesan":"Bang waktu presentasi jangan terlalu cepat ya bang hehe"# 1  
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "humble dan baik",  
                "pesan":"Selalu happy ya kak :)"# 1  
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "humble dan baik",  
                "pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zh4M-Em2lwM-CmePV3GbnEiicK8zL9af",
            "https://drive.google.com/uc?export=view&id=1j_56jjUXFplAfwI6MsZT_2hRZMPUHM9C",
            "https://drive.google.com/uc?export=view&id=1tyAFkhHMUanbHCvNarJsojELU9S_PpDL",
            "https://drive.google.com/uc?export=view&id=1lm9RQDR0eqeYvkLDkze_AsKqhiEMD7ga",
            "https://drive.google.com/uc?export=view&id=13_D_X0D_4dQVIV0FmQRKCtPtos3IDftB",
            "https://drive.google.com/uc?export=view&id=17RXB64pOkzQlnQsbiR9OoJGRhgCkTk4P",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH",
                "hobbi": "bernyanyi",
                "sosmed": "@iyamridhomanik",
                "kesan": "Bang ridho ramahnya gak ketolongan, humble, adem liat bang ridho rasanya",  
                "pesan":"gass cumlaude bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sekawang",
                "alamat": "pelangi",
                "hobbi": "ngereapet lagu  beegin again Taylor ",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Keren berkharisma",  
                "pesan":"Lulus tepat waktu ya bang"# 1
            },
            {
                "nama": "Dharu Chayoaji Sangsoko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar lampung",
                "hobbi": "nonton agz, tapi udh tamat",
                "sosmed": "@eeffiidefi",
                "kesan": "humble, ramah, baik",  
                "pesan":"Kak, senyum selalu ya kak"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Cool, dan keliatan orang yang Sistematis",  
                "pesan":"Bang waktu presentasi jangan terlalu cepat ya bang hehe"# 1  
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "humble dan baik",  
                "pesan":"Selalu happy ya kak :)"# 1  
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "humble dan baik",  
                "pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
