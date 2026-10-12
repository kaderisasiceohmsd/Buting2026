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
            "https://drive.google.com/uc?export=view&id=1JW5Q6J0-l32PUXZ4fmDbIwv-z8uJD-aw",
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
                "kesan": "tegas dan berwibawa bang ginda ituuu",  
                "pesan":"jadi kahim berat bang, semangat menjalankan amanahnya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau, Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "tegas dan berwibawa juga si bang aqil itu",  
                "pesan":"Semangat yowww banggg dengan amanahnya"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangatloh kakak dengan jabatannyaa"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "keliatannya berwibawa banggg",  
                "pesan":"semangat yaa banggg dengan tugas tugas nyaa"# 1  
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "lucuuuuu",  
                "pesan":"semangat trs kakkk"# 1  
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "friendlyyyyyyy",  
                "pesan":"semangat kak dengan tugasnyaa"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=1XNSXzeYpf8dhblsV8pFvjT1yYG18MFhn",
            "https://drive.google.com/uc?export=1i8wsWgHJnUyUvkKDC1tqEzGnEQ82FlmT",
            "https://drive.google.com/uc?export=1CN3B8cT4CHIFU4RDGQbvTJ7osGg-yPzH",
            "https://drive.google.com/uc?export=1DVIWHiNruGq7mzPlTwF-GWQvCVK38lDF",
            "https://drive.google.com/uc?export=1kLzuln39ncDIwiCh-KMUHv8Mtm31ytYx",
            "https://drive.google.com/uc?export=1Fjq65rzSjIOrQ9QKlwVUyA3zyMX62gsj",
            "https://drive.google.com/uc?export=1Cxvy9NgLhTx1JG4GugzjQwYwt2W54xwp",
            "https://drive.google.com/uc?export=1lz9cuT5sq1qIU-jAHOCyRysaQB50LeTv",
            "https://drive.google.com/uc?export=1GR7rcXMVJjBRlD9H0OATbzO8gPng7fy-",
            "https://drive.google.com/uc?export=1VJHORmrZM1NbJmDwTxUtAuLJQrJeRmJn",
            "https://drive.google.com/uc?export=1P7CN9dF8V_-iKQgd2X3VzXS4PDAFbgW9",
            "https://drive.google.com/uc?export=1KG-TG2-t8Yd7qRJm17GpRc53b8qQh4cr",
            "https://drive.google.com/uc?export=1GiBU6W-U9flBGhClMuEM9el3VxQboR0o",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik ",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH",
                "hobbi": "bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sakawang",
                "alamat": "Pelangi",
                "hobbi": "Ngerepeat lagu begin again taylor",
                "sosmed": "@j__eesie",
                "kesan": "lucuuuuu bgtttt",  
                "pesan":"semangat menjalankan amanahnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton ags, tapi udah tamat",
                "sosmed": "@ddharu_",
                "kesan": "lucu suka nonton agssss",  
                "pesan":"semangat menjalankan amanahnya bang"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jatimulyo",
                "hobbi": "Jogging malam hari",
                "sosmed": "@me._kael",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung pesagih",
                "alamat": "sukabumi",
                "hobbi": "minum kopi",
                "sosmed": "@givarooo",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Sumbar,Padang",
                "alamat": "Kedaton",
                "hobbi": "memburu",
                "sosmed": "@afghanisnt_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kota bumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kak"# 1  
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Ngoding",
                "sosmed": "@jeremia_hm",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya bang"# 1  
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym Koleksi Figur",
                "sosmed": "@nagatseee",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Mamuju",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "tegas dan berwibawa",  
                "pesan":"semangat menjalankan amanahnya kakkkk"# 1  
            },
            ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

