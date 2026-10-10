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
            "https://drive.google.com/uc?export=view&id=1J-rsWHF5zwQ_-_xqxt7DYWF-5P5ymzKv",
            "https://drive.google.com/uc?export=view&id=137c5EKVfSQvxD8cQ_htbjel-yHPUU_M5",
            "https://drive.google.com/uc?export=view&id=18Tfshe_-1nTp82E9psDJK0f4nk2r0Ke3",
            "https://drive.google.com/uc?export=view&id=1IvA_nI4wpruLlaCVw1ZL-JnDiMi1K03R",
            "https://drive.google.com/uc?export=view&id=1K3sEk-WQWh1kF9zRNe4ajtM_QR37NRiT",
            "https://drive.google.com/uc?export=view&id=1709lIORxWXXRmt_r0Bk0GcYqI55IYWgy",
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
            "https://drive.google.com/uc?export=view&id=1SaJ7ZNPVFadjwwlgPfGSsFlDiSpFRAAR",
            "https://drive.google.com/uc?export=view&id=1hMYya9Olo5DcmvFcxlpNhUAjUw8jjMDI",
            "https://drive.google.com/uc?export=view&id=1AHZe-Olev2nMcFxUfXNBfGHYP5mol0a2",
            "https://drive.google.com/uc?export=view&id=16a_basrR64sJNPViTR8Ye28whFfKwJTD",
            "https://drive.google.com/uc?export=view&id=1GZOwM6sbGafcFP53AyRSKPWowcrbZvJ-",
            "https://drive.google.com/uc?export=view&id=1gFXv2rPWE_x_RZNileT9bc2aIFmF5cSd",
            "https://drive.google.com/uc?export=view&id=1ERK4KMBgClCi7PYpd0Dj3uSZrmWOZvF2",
            "https://drive.google.com/uc?export=view&id=137c5EKVfSQvxD8cQ_htbjel-yHPUU_M5",
            "https://drive.google.com/uc?export=view&id=1ZTbcu2psLWi_pRbrFtDzRcI3qIDDCYHj",
            "https://drive.google.com/uc?export=view&id=1zGWtJ9vEGxBqucijis1fHkD29xQemH1r",
            "https://drive.google.com/uc?export=view&id=1NmTEWJ1JoyEpF6-ysm4h-rOLQtWLtVAa",
            "https://drive.google.com/uc?export=view&id=1HwsQ9006W3oyPfFkOzNrj6fjbW8RedQE",
            "https://drive.google.com/uc?export=view&id=1_mnMLNG7YZXb0FFaenWWXxd_EwwTEtFU",
        ]
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "Nim": "123450060",
                "Umur": "20",
                "Asal":"Manado",
                "Alamat": "Sektariatan HMSD",
                "Hobi": "Bernyanyi",
                "Sosmed": "@iamridhomanik",
                "Kesan": "GG GEMING BANG RIDHO, Cheerful, dan juga Charming",
                "Pesan":"Ditunggu Kabar baiknya bang ridho, semoga sehat selalu ya bang"# 1
            },
            {
                "Nama": "Juesi Apridelia Saragih",
                "Nim": "123450085",
                "Umur": "19",
                "Asal":"Sengkawang",
                "Alamat": "Pelangi",
                "Hobi": "Mendengarkan musik dari Taylor Swift",
                "Sosmed": "@j__eesie",
                "Kesan": "Cantik, imup, lumcu, dan juga ramah",
                "Pesan":"Ditunggu diary berikut-berikutnya, Kak"# 1
            },
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "humble, ramah, baik",  
                "Pesan":"Kak, senyum selalu ya kak"# 1
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "Nim": "123450023",
                "Umur": "19",
                "Asal":"Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Nonton AGZ",
                "Sosmed": "@ddharu_",
                "Kesan": "Jenius, Ambis, dan aktif ya bunnn",  
                "Pesan":"Semangat terus buat kuliah dan PKM nya, Bang DHARU!!!"# 1  
            },
            {
                "Nama": "Gh Mikael Niko Antoni Setiadi",
                "Nim": "12450025",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Jatimulyo",
                "Hobi": "Jogging malam hari",
                "Sosmed": "@me._kael",
                "Kesan": "Wakil Ketua angkatan 2024 dan fun, ramah, dan baik",
                "Pesan":"Selalu happy ya,Bang:)"# 1  
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "Nim": "124450015",
                "Umur": "19",
                "Asal":"Banten",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi Kartu Boboiboy",
                "Sosmed": "@syt.rifa",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Givaro Ananta",
                "Nim": "123450078",
                "Umur": "20",
                "Asal":"Gunung Mesagi",
                "Alamat": "Sukabumi",
                "Hobi": "Minum Kopi",
                "Sosmed": "@givarooo",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "Nim": "124450042",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Kedaton",
                "Hobi": "Memburu",
                "Sosmed": "@afghanisnt",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Hani Qurrota Aini",
                "Nim": "124450020",
                "Umur": "20",
                "Asal":"Kotabumi",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Jeremia Halim",
                "Nim": "124450101",
                "Umur": "20",
                "Asal":"Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngoding",
                "Sosmed": "@jeremia_hm",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "Nim": "124450073",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Kotabaru",
                "Hobi": "Tidur",
                "Sosmed": "@monica_tjg",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "Nim": "124450121",
                "Umur": "20",
                "Asal":"Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "GYM dan Koleksi figure",
                "Sosmed": "@nagatseee",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "Nim": "124450082",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Pemda",
                "Hobi": "Main",
                "Sosmed": "@sekardnwp",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "Nim": "123450077",
                "Umur": "20",
                "Asal":"Mamuju",
                "Alamat": "Belwis",
                "Hobi": "Meyapa Angin",
                "Sosmed": "@nshaysk",
                "Kesan": "humble dan baik",  
                "Pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

