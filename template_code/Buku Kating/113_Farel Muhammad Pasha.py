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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak ester",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak B",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak CCc",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IbebTFBPkSyxMkr0d6EINJ9t2NdXM6uF",
            "https://drive.google.com/uc?export=view&id=1hepjAmdngtGvSGRCAAcNz5j-IDqnoBMu",
            "https://drive.google.com/uc?export=view&id=1le945I1B9Qouk17zUfTODlP2KVdtV712",
            "https://drive.google.com/uc?export=view&id=12gXQ0CeJ8Iz3KAj_JxoR4nVS4ZoNqys9",
            "https://drive.google.com/uc?export=view&id=15z0baUvhVwx1KDMipuBCqZzZc3UVYmZE",
            "https://drive.google.com/uc?export=view&id=1hepjAmdngtGvSGRCAAcNz5j-IDqnoBMu",
            "https://drive.google.com/uc?export=view&id=1le945I1B9Qouk17zUfTODlP2KVdtV712",
            "https://drive.google.com/uc?export=view&id=1aCKDCE_C7SEMkQsSU8IvjOO1GkH5kxzy",
            "https://drive.google.com/uc?export=view&id=1IbebTFBPkSyxMkr0d6EINJ9t2NdXM6uF",
            "https://drive.google.com/uc?export=view&id=1hepjAmdngtGvSGRCAAcNz5j-IDqnoBMu",
            "https://drive.google.com/uc?export=view&id=1le945I1B9Qouk17zUfTODlP2KVdtV712",
            "https://drive.google.com/uc?export=view&id=1aCKDCE_C7SEMkQsSU8IvjOO1GkH5kxzy",
        ]
        data_list = [
    {
        "nama": "Ridho Benedictus Togi Manik",
        "nim": "123450066",
        "umur": "20",
        "asal": "Kuala Lumpur",
        "alamat": "GH",
        "hobbi": "Wawancara",
        "sosmed": "@iamridhomanik",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Juesi Apridelia Saragih",
        "nim": "123450085",
        "umur": "19",
        "asal": "Pelangi",
        "alamat": "Singkawang",
        "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
        "sosmed": "@j__eesie",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Dharu Cahyoaji Sasongko",
        "nim": "123450023",
        "umur": "19",
        "asal": "Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Makan mie gomak",
        "sosmed": "@exvoltas & @ddharu",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "GH Mikael Niko A S",
        "nim": "124450079",
        "umur": "20",
        "asal": "Pasir Sakti",
        "alamat": "Jati Agung",
        "hobbi": "Tidur",
        "sosmed": "@me._kael",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Siti Sarifah Sumamah",
        "nim": "124450015",
        "umur": "19",
        "asal": "Bekasi",
        "alamat": "Kedaton",
        "hobbi": "Mancing",
        "sosmed": "@syt.rifa",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Givaro Ananta",
        "nim": "123450078",
        "umur": "21",
        "asal": "Lampung Barat",
        "alamat": "Sukabumi",
        "hobbi": "Minum Kopi",
        "sosmed": "@givarooo",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Afghanis Nursholehatunisa",
        "nim": "124450042",
        "umur": "20",
        "asal": "Kepulauan Mentawai",
        "alamat": "Kadang di kost putri kadang di kost sekar",
        "hobbi": "Memanjat",
        "sosmed": "@afghanisnt_",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Hani Qurrota Aini",
        "nim": "124450020",
        "umur": "20",
        "asal": "City earth",
        "alamat": "Sukarame",
        "hobbi": "Baca AU",
        "sosmed": "@haniqurratuain_",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Jeremia Halim",
        "nim": "124450101",
        "umur": "20",
        "asal": "Tangerang",
        "alamat": "Teluk Betung",
        "hobbi": "Nyanyi, olahraga",
        "sosmed": "jeremia_hm",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Monica Patricia Tanjung",
        "nim": "123450073",
        "umur": "21",
        "asal": "Jakarta Barat",
        "alamat": "Kotabaru",
        "hobbi": "Lari",
        "sosmed": "@monica_tjg",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Jona Timothy Ogatse Panjaitan",
        "nim": "124450121",
        "umur": "20",
        "asal": "Depok",
        "alamat": "Pemda Raya",
        "hobbi": "Nge-gym, koleksi figur",
        "sosmed": "@nagatseee",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Sekar Dini Widya Putri",
        "nim": "124450082",
        "umur": "20",
        "asal": "Metro",
        "alamat": "Pemda",
        "hobbi": "Melukis",
        "sosmed": "@sekardnwp",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Wan Nashwa Alhasni Yuska",
        "nim": "123450077",
        "umur": "20",
        "asal": "Pasay",
        "alamat": "Belwis",
        "hobbi": "Nyapa angin",
        "sosmed": "@nshaysk",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()
# Tambahkan menu lainnya sesuai kebutuhan
