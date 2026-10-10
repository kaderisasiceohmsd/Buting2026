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
            "https://drive.google.com/uc?export=view&id=1RPRXY1_sjMuAcDhD0A46aDYlfkQ2CnXW",
            "https://drive.google.com/uc?export=view&id=1jdVwET2zp7CHeChA-vVKx9gtzMfUdivU",
            "https://drive.google.com/uc?export=1fuD4xooOTLVZdFMz7hiojychS2CrjbGQ",
            "https://drive.google.com/uc?export=view&id=1xi8ilNCyKhE5IACbKCcjI2XC7mxcGpjU",
            "https://drive.google.com/uc?export=view&id=1wiWYI_oP_P6Ih95sQ1ANvnG9lfnLA448",
            "https://drive.google.com/uc?export=view&id=1-6X5KDbE1W1WC8jKiNFuWCByUKE_Il48",
        ]
        data_list = [
            {
        "nama": "Muhammad Aqil",
        "nim": "123450046",
        "umur": "22",
        "asal": "Bangkinang",
        "alamat": "Sekretariat HMSD",
        "hobbi": "Dzikir",
        "sosmed": "@muhammadaqil1111",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        },
        {
        "nama": "Qois Alfio",
        "nim": "123450067",
        "umur": "22",
        "asal": "Batam",
        "alamat": "Kotabaru",
        "hobbi": "Mainin surat",
        "sosmed": "@qoidalfio_",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        },
        {
        "nama": "Ginda Fajar Riadi Marpaung",
        "nim": "1234500fadil",
        "umur": "22",
        "asal": "Batam",
        "alamat": "Sekretariat HMSD",
        "hobbi": "Push Rank sampe IMO",
        "sosmed": "@gars_mrp",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        },
        {
        "nama": "Evi defiani",
        "nim": "123450005",
        "umur": "21",
        "asal": "Lamtim",
        "alamat": "Airan",
        "hobbi": "Membaca",
        "sosmed": "@eeffifi",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        },
        {
        "nama": "Hafsa Fadzilah Arraadhila",
        "nim": "079",
        "umur": "21",
        "asal": "Balam",
        "alamat": "Balam",
        "hobbi": "Berenang",
        "sosmed": "@hafsafadhilaa",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        },
        {
        "nama": "Luthfia Laila Ramadhani",
        "nim": "004",
        "umur": "20",
        "asal": "Bengkulu",
        "alamat": "Airan",
        "hobbi": "Bertemu pak tirta",
        "sosmed": "@lutfiaarmdhn",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
        }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f54XEKLV5-_iY0Ke1Amy_8n2lsuTpWrB",
            "https://drive.google.com/uc?export=view&id=1Npve-crpQRsbSWWEiarHjDlkXz2v5uMy",
            "https://drive.google.com/uc?export=view&id=1SXlqNcP7PFbzx62UCp6dmh7LCh0or6Ul",
            "https://drive.google.com/uc?export=view&id=1NFnxXH1iKWic5Mp4dbGtTP9Xx4DC68Xh",
            "https://drive.google.com/uc?export=view&id=1C7TLf81OCP5CfwY7wy6O25kc616G6IjH",
            "https://drive.google.com/uc?export=view&id=17dBnXowQY4puKAesvwkom0NmHYtjQOFS",
            "https://drive.google.com/uc?export=view&id=15DoGub_MvMZN1CO6gb_8hOv6lGIgPvu6",
            "https://drive.google.com/uc?export=view&id=1h_syNDUTRwE9yEntGLAMWhtP1A36c5ga",
            "https://drive.google.com/uc?export=view&id=1UvXJs9C6bqp_N9_2Bak2VJxgRj5SrtY8",
            "https://drive.google.com/uc?export=view&id=1MkYZ6i_A643S8bgQmQ8534gt8A5qpvi9",
            "https://drive.google.com/uc?export=view&id=1VLxmWTsL2RbVgRgKKn_WZ0u0lhHyCpMf",
            "https://drive.google.com/uc?export=view&id=1MLgWgxGJy7rWdIox6yUiJ9dgKbpnpkPW",
            "https://drive.google.com/uc?export=view&id=1_ze0SXyd0BWT4qSr5q3RF1DLeARrWyAV",
            
        ]
        data_list = [
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",  
                "pesan":"..."# 1
            },
        
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DB2rHAmkffUqkrya8F8oZcQ5ky-E7IpU",
            "https://drive.google.com/uc?export=view&id=1A9TvLPFQtnaq0BzwKE6JVH1XeyX7bgp-",
            "https://drive.google.com/uc?export=view&id=1OJ7DriS--Ewwl3ZyG0xt4sMTC5quS4r-",
            "https://drive.google.com/uc?export=view&id=1Tybx2D5I_98OnxxCWinZnjk0b8-CO7S5",
            "https://drive.google.com/uc?export=view&id=1eoPRNOiqrHN13VNiao9jjQ0IuEqrIguS",
            "https://drive.google.com/uc?export=view&id=1LNwmAbHuLnCXLpEq8wxWNh40Sz-rLBCA",
            "https://drive.google.com/uc?export=view&id=1CI2P4dAFMDPRsrYErYKJPZP330WA3ORF",
            "https://drive.google.com/uc?export=view&id=1qOmHUqzqldal4GPoOGrFKMXIgXoU_yEm",
            "https://drive.google.com/uc?export=view&id=1dlDTw7hOo-XTSc1X94HK97YtOcmFutm5",
            "https://drive.google.com/uc?export=view&id=1sLE-dVR8G7XK4_y3fAEeF4QfK2BydGKT,
        ]
        data_list = [
        {
            "nama": "Fathinah Nur Azizah",
            "nim": "123450072",
            "umur": "21",
            "asal": "Jakarta",
            "alamat": "Airan",
            "hobbi": "Nulis Medium",
            "sosmed": "@fathinahnaazh",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Helmy Surya Pratama",
            "nim": "124450033",
            "umur": "20",
            "asal": "Jakarta",
            "alamat": "Kedamaian",
            "hobbi": "ngesen kiri",
            "sosmed": "@helmy_inst",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Fernando Dimetrius Barus",
            "nim": "124450063",
            "umur": "21",
            "asal": "Tanggerang kota",
            "alamat": "Sebelah kamar biwa",
            "hobbi": "badminton",
            "sosmed": "@barus.fernando",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Suci Aulia",
            "nim": "124450034",
            "umur": "19",
            "asal": "Krui",
            "alamat": "Kota Baru",
            "hobbi": "Bikin video random dan upload di second",
            "sosmed": "@sciia___",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Wielman Itolo Halawa",
            "nim": "124450072",
            "umur": "20",
            "asal": "Nias Selatan",
            "alamat": "Asrama TB 3",
            "hobbi": "Mancing",
            "sosmed": "@wielhawn",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Lia Hana Ichisasmita",
            "nim": "123450089",
            "umur": "21",
            "asal": "Jakarta Timur",
            "alamat": "Belwis",
            "hobbi": "Nyari jurnal",
            "sosmed": "@lia.h_264",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Aqila Zayyan Salsabil",
            "nim": "124450014",
            "umur": "19",
            "asal": "Lampung Utara",
            "alamat": "Sukarame",
            "hobbi": "Mendokumentasikan Bayyesian",
            "sosmed": "@aqilazayyaan",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Hazel Mahesa Handhaka",
            "nim": "1244500114",
            "umur": "20",
            "asal": "Lampung Timur",
            "alamat": "Ujung Terang",
            "hobbi": "Bulu tangkis",
            "sosmed": "@hazelhandhaka",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Nadya Ratu Anjani",
            "nim": "123450083",
            "umur": "21",
            "asal": "Balam",
            "alamat": "Sukarame",
            "hobbi": "Denger lagu",
            "sosmed": "@nadyaanjani",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
        {
            "nama": "Dwi Rahma Fitriani",
            "nim": "124450084",
            "umur": "19",
            "asal": "Tulang Bawang",
            "alamat": "Jl. Lapas Belwis",
            "hobbi": "Dengerin musik dan nonton film",
            "sosmed": "@dwi_rahmstlnii",
            "kesan": "Kakak ini asik saya suka belajar dengan dia",
            "pesan": "semangat terus kuliahnya kakak !!!",
        },
]

# Contoh menampilkan data
if __name__ == "__main__":
    for index, data in enumerate(data_list, 1):
        print(f"{index}. {data['nama']} ({data['nim']})")
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
        ]
        data_list = [
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
    if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
            "https://drive.google.com/uc?export=view&id=...",
        ]
        data_list = [
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "...",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

# Tambahkan menu lainnya sesuai kebutuhan
