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
            "https://drive.google.com/uc?export=view&id=1bZ_xsql6N9tEc9GICgZnbxH5SLuIOi_z",
            "https://drive.google.com/uc?export=view&id=1u_pc0wsPKMzpLWBxcL8hGeXGsp_Q_rLn",
            "https://drive.google.com/uc?export=view&id=1UyBqB5j3JygoQiE2PWJoncvmEKb6xQD0",
            "https://drive.google.com/uc?export=view&id=1Dlwb4YNyEfnFSI7RTW9wxWV3RVcrlLju",
            "https://drive.google.com/uc?export=view&id=1B1f8IpWM7ph6eFoInAYMfyokqeFf_iCD",
            "https://drive.google.com/uc?export=view&id=1Z1VIi2sd9fW0bptDTn7Jn_wXZipAsgeZ",
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
                "kesan": "Baik sekali, humble, best pokoknya bang him",  
                "pesan":"keren terus bang ginda #1"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau, Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Keren baget, humble, ga seseram yang dikira",  
                "pesan":"sukses selalu bang aqil"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "baik asprak ads hehhe",  
                "pesan":"selamatkan ads ku kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "baik sekali, keliatan suart menyurat diluar kepala",  
                "pesan":"sukses terus bang qois"# 1  
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "baik banget, humble, cantik sekali",  
                "pesan":"jangan keliatan galak kak, senyum terus kak"# 1  
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "keliatan paling gemes, humble, seru",
                "pesan":"sukses terus kak luthfia"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Lnni0Xtz9kp1xPa0oqXraV16CHMF8381",
            "https://drive.google.com/uc?export=view&id=11d-q2YCTGhzrLmSFLZLOfNIv3_QtYzJw",
            "https://drive.google.com/uc?export=view&id=1mN8qt17K_C6vJfJ9e2MPh07JbiMKSRLy",
            "https://drive.google.com/uc?export=view&id=1T4tw5drFW0JMz1V6yxyCI9J13iURv7Ai",
            "https://drive.google.com/uc?export=view&id=1cl7s3vBGuXGfHHsRHd9JxJUEnMI5arS3",
            "https://drive.google.com/uc?export=view&id=1t4x9Acs4lR9yIvNLQykwAuADf8ijet0u",
        ]

        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH, Sektariatan HMSD",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "baik, ramah",  
                "pesan":"keren terus bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Sekawang",
                "alamat": "Kos Pelangi",
                "hobbi": "repeat lagu Taylorswift",
                "sosmed": "@j__eesie",
                "kesan": "cantik banget kak jue, baik, humble, kreatif",  
                "pesan":"sukses selalu ya kak jue, semoga kebaikan selalu mengelilingi kak jue,"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Banddar Lampung",
                "hobbi": "Nonton AGZ, tapi udah tamat",
                "sosmed": "@ddharu_",
                "kesan": "baik, bagus banget komunikasinya, humble",  
                "pesan":"terus mengudara bang dharu"# 1
            },
            {
                "nama": "Gh Mikael Niko Antoni S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jatimulyo",
                "hobbi": "Jogging malam hari",
                "sosmed": "@me._kael",
                "kesan": "cool banget",  
                "pesan":"pasang muka cute terus ya bang"# 1  
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboby",
                "sosmed": "@s",
                "kesan": "baik, humble",  
                "pesan":"sukse selalu ya kak"# 1  
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagih",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "@givaroo ",
                "kesan": "baik sekali, cute jujur",  
                "pesan":"semangat bang givaro"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

