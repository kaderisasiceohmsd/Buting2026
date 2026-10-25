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
            "Departemen Minbak"
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
            "nav-link-selected": {"background-color": "#606060"},
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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P4kFYI0YBBWlZnrh0lPlEVoJUkvEh4nG",
            "https://drive.google.com/uc?export=view&id=1Fat3lB6ifOdyHwd9_X8MqUUPOYYahbnz",
            "https://drive.google.com/uc?export=view&id=14zBFUayji3amYsoTidTwi-kJxyz5qod1",
            "https://drive.google.com/uc?export=view&id=1ZHWCPY0-smYYhPmA5t7PoIn-GMZvZJXh",
            "https://drive.google.com/uc?export=view&id=1o7UmZPwVbEQyFVvrFqHRhG2baHsypvLs",
            "https://drive.google.com/uc?export=view&id=1eq6ADzC8Csf7oIm5Cr49zVsZDQEG8Anf",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Tinggal Sekretariat HMSD",
                "hobbi": "Push Rank Sampai imo",
                "sosmed": "@jars_mrp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Tahajud",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Basket",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lutfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nemuin Pak Tirta",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EgAtu1c6URb7h8fh7aspidSbPSch23jB",
            "https://drive.google.com/uc?export=view&id=1004qh1MoQtQvtWxenhsW4jZg0HsFmGY-",
            "https://drive.google.com/uc?export=view&id=1u2b_N3rc-ZKn7zsdhjCbCwdum03Lpf6n",
            "https://drive.google.com/uc?export=view&id=10dT0nqt9V1WzS57p28babPLxWZTrukxg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1vl8NkuYNhQKSYsikNeu1t5naWsPfpUHF",
            "https://drive.google.com/uc?export=view&id=1-OxEg28n85hDJUZqiixatseQVVinpgWf",
            "https://drive.google.com/uc?export=view&id=1p9goFENucEU3By2qUJcx7noO5yCOd8M4",
            "https://drive.google.com/uc?export=view&id=1QJDVHBKmme88o35lZhB_7rQkL5YSki7M",
            "https://drive.google.com/uc?export=view&id=1XFEoweoZv1Zs6Hl-WyYbL_13OBPIDi4m",
            "https://drive.google.com/uc?export=view&id=176-x5T-M2JIyh6EsraB7Mo4rhinypVM9",
            "https://drive.google.com/uc?export=view&id=1dyy_Pm2vlN7rXrgN9J4xbph50QLnLv1A",
            "https://drive.google.com/uc?export=view&id=1Wgr0FNUJfV20tn908Wl8iqVQGisxyZOH"                       
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Bali",
                "alamat": "GH",
                "hobbi": "Menonton Seminar",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang ini asik parah dan yapping banget dan sedikit npd juga",  
                "pesan":"Semoga cepat selesai TA nya bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Repeat lagu if only by skyline setiap hari di jam 8",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya gemas dan cantik bangett, aku suka banget",  
                "pesan":"Semangat terus belajarnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "124450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya aktif dan keren banget, aku kagum liatnya",  
                "pesan":"semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abangnya asik, baik, dan ternyata receh parah, ketawa mulu",
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "124",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "kakak ini baik banget",  
                "pesan":"Semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Gh Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Jatiasih",
                "alamat": "Kedaton",
                "hobbi": "Nonton Boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Indarum",
                "alamat": "Awen kost",
                "hobbi": "Photobooth",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",                
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Sidoarjo",
                "alamat": "Teluk",
                "hobbi": "Konten Mainfullness",                
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya aktif dan sibuk banget ternyata, tapi baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan koleksi figure",                
                "sosmed": "@nagatseee",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Membaca buku",                
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "124450077",
                "umur": "20",
                "asal":"Pasoy",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",                
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu, asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Sa6f_AT5efY9wm8JTVdY13v4HrQnWRU2",
            "https://drive.google.com/uc?export=view&id=1KHIR7FG8mGsWI7hot1g-1l-MUtUpha3C",
            "https://drive.google.com/uc?export=view&id=1e336w7s_drtr7R9OtO8DdBqXmzZTSqce",
            "https://drive.google.com/uc?export=view&id=1f0AsrSKXTPPi8fHwC9rh4Dxa4o65eaX5",
            "https://drive.google.com/uc?export=view&id=1CFM7RunwDh3uP_D3hPkLTgLpLw954ghu",
            "https://drive.google.com/uc?export=view&id=1mVGTw_XziTbqmXdTtr3qmSFX1pfedr4p",
            "https://drive.google.com/uc?export=view&id=1aMfvMzf9aIgVUToK2tQOS4TXR7a_sqpW",
            "https://drive.google.com/uc?export=view&id=1VOSFLLq832_cQmfvFgdFZFaiRMHyUalq",
            "https://drive.google.com/uc?export=view&id=1hHofwyxzz9l41KxmW8Xp7JPZUuVQLBII",
            "https://drive.google.com/uc?export=view&id=1hQfNmHOnNYCXmij_BlyLPFfPySgh96_I",
            "https://drive.google.com/uc?export=view&id=1d0K7viI7aLWf3pyjYkpvDwjkPRA1r1y8",
            "https://drive.google.com/uc?export=view&id=1oqnrYgWDQcGLMZ2HkJYwzvB3myYb-6PL",
            "https://drive.google.com/uc?export=view&id=1Og3D7ORPmZRuXvFtQmZObGeWQkPlkHmh",
            "https://drive.google.com/uc?export=view&id=1RHJSjwOcCS9p8riO6JxMC2JP1-1pjjdF",
            "https://drive.google.com/uc?export=view&id=1jE6rgJNNyzBSa3SoWVZECHba8G_pLoAR",
            "https://drive.google.com/uc?export=view&id=1dHXXwFK5jH0ph3RhYfYhKc2lQigfLEtA",
            "https://drive.google.com/uc?export=view&id=1On7nR0nJTaN7PT6QyFxton58XDl0360y",
            "https://drive.google.com/uc?export=view&id=1TuJnzXsAZyVfaMjea97xKHxrrnDfZnB0",
            "https://drive.google.com/uc?export=view&id=1jf-XfOI7Reey7nFGQISTa3B-rDcUV3Nn",
            "https://drive.google.com/uc?export=view&id=1DYe8L_n8hFWioAa_JUQX3dpbpLM2iZAs",
            "https://drive.google.com/uc?export=view&id=1O5hWaWIJj_zUUbHWhjclw6qQ1SSh21fz",
            "https://drive.google.com/uc?export=view&id=1nPopBnVK4yTNHaUxqYRX_vcKUwu-G39j"
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LHvm1I4nj1XCX88N8_FUxqGlJd1DtdVC",
            "https://drive.google.com/uc?export=view&id=14kTtB5L8hdi6dY-es18O4o_c7Z365fGr",
            "https://drive.google.com/uc?export=view&id=1hBJ_E8mk-ELrqSkpx3GwV4zgaduSxB6C",
            "https://drive.google.com/uc?export=view&id=1TlqozFNtp0diNedwl3TnpxgyktNOyoTO",
            "https://drive.google.com/uc?export=view&id=1IMqs0UaIIjutYyGkqSPZei5KKaklAfU_",
            "https://drive.google.com/uc?export=view&id=1APklFyP0fNvsOsS1sLgFFKEVpBSSqnO_",
            "https://drive.google.com/uc?export=view&id=1sZq5lgiJ-A25BDEwhc-zyXx_vS5fq90e",
            "https://drive.google.com/uc?export=view&id=195HbNBFMuny42ZfUJ_zioUq2AT7BVaoU",
            "https://drive.google.com/uc?export=view&id=18p-WH15JF0tsAZ5EpmbL9YJHoil4w2Bc",
            "https://drive.google.com/uc?export=view&id=1Zvo4oNHX3g1d--rf9v0bmz_pt6brJJUe",
            "https://drive.google.com/uc?export=view&id=1BXFKKvO9qR1soOvDOCAszlpdzpL84HgT",
            "https://drive.google.com/uc?export=view&id=1X6D_-yh6lIZmQw7dZX_QQML6vGLSi9qr"
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1F5NuYZt85yrWvl20sZmT-nmAWgsqwiSw",
            "https://drive.google.com/uc?export=view&id=1BCfQrLm3OJYF-I6kQ1NNy_BPad8jHxM5",
            "https://drive.google.com/uc?export=view&id=1R0EENzXFftZRB35RsyIsZxhwoC2J4Hee",
            "https://drive.google.com/uc?export=view&id=1daXBGpzK3TlYtEzIsq_ceA-OeHPe54Id",
            "https://drive.google.com/uc?export=view&id=1jc77RUf9W9hOxQU7FmB-ShJZaBmtbI_s",
            "https://drive.google.com/uc?export=view&id=1_Dg3gAuq1f0OG4zs6LZoKZWoNy_kIenb",
            "https://drive.google.com/uc?export=view&id=1wWGsvqglOaDY96HVcCkj7A_KxsE0xWTZ",
            "https://drive.google.com/uc?export=view&id=1xXl2yG8uAM9EdXqiPkQSrh865bJf9Dgv",
            "https://drive.google.com/uc?export=view&id=1HQWWL6MbIjoWahRtnVwS3tJ1fpmG8rMX",
            "https://drive.google.com/uc?export=view&id=1aNl32zQOLzr1RxCYsur5cIkTudCnLLZD",
            "https://drive.google.com/uc?export=view&id=1F94r1OcBvcJcLBbG-aRcSqMst4AiCrEm",
            "https://drive.google.com/uc?export=view&id=1VtgL1muKjgs05D_gSEMrRmO8NkdJKGxf",
            "https://drive.google.com/uc?export=view&id=1G89pYjixJ6nI6PMfcDeq64gqz0252kF7",
            "https://drive.google.com/uc?export=view&id=1x5wzceM3lzkzpCUZV5_UPQViogayySlV",
            "https://drive.google.com/uc?export=view&id=1XzaLcfp6tGac6ItTcy8WxX7strlC3Ilj",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": " Edsel Adya Pradipta",
                "nim": " 124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "shafa delaila azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17MTwMmt35UYUzw3s9V4BESFCQP98htcM",
            "https://drive.google.com/uc?export=view&id=1gLsHWRmeXTmG4Et0KhU-JDsTaH1EE16l",
            "https://drive.google.com/uc?export=view&id=1vR0xz-iP0KC0EVOUaj6EmtQ7Sx4xJsmr",
            "https://drive.google.com/uc?export=view&id=1oP9fmPtHjAeshYexGs63PqqBivJXuT9p",
            "https://drive.google.com/uc?export=view&id=1JCY0WGAjKyFUwBh4QM7q0knvu_YYJzKc",
            "https://drive.google.com/uc?export=view&id=1tDjIGLpUJceX3ex9aGRK2otVZF6YNYlD",
            "https://drive.google.com/uc?export=view&id=16wNU_Q9IedoKP9rXolBjtUOfnfEDjZk3",
            "https://drive.google.com/uc?export=view&id=1Aj0_96CBEINSKD2Vac4rQyWUEEKgP_mZ",
            "https://drive.google.com/uc?export=view&id=1Jc6gvOGgRtGH7iMfyzAjCVPWVkCmTGS2",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21 Tahun",
                "asal":"Jakarta",
                "alamat": "Airan",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "19 Tahun",
                "asal":"Lamtim timur",
                "alamat": "Gunter terang",
                "hobbi": "Cinematic Datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18nhfqYnA7v8X2DtA1QMnumC0IKKSs3aD",
            "https://drive.google.com/uc?export=view&id=1PzF-0FFPj_yWqu2V1BvphbmcYCElLZBV",
            "https://drive.google.com/uc?export=view&id=1t6Fn2V3t0L5txMinnTSB0WBFqmrrRA9o",
            "https://drive.google.com/uc?export=view&id=1C7c8aiM26UpvGSOVXKi9MppiXsDaqtCg",
            "https://drive.google.com/uc?export=view&id=1oLTbUlzo1iDjAUVjy42IOer9P6EGM8iC",
            "https://drive.google.com/uc?export=view&id=1u_ONULML9EQf5hUeK-nD3m5Y78ssjl8Q",
            "https://drive.google.com/uc?export=view&id=1P95J-j2ZUwiX9MZLHvs4aoT5hSqse0n-",
            "https://drive.google.com/uc?export=view&id=1ssJFBbeEWxaTK2yDB36NgSDz72T34pZL",
            "https://drive.google.com/uc?export=view&id=1BsF_-kaMU7SfJBdfNwUAw0IjRG0EVEVc",
            "https://drive.google.com/uc?export=view&id=1zpoYVbQzgSs81VDPGqX5elrsYQe1XVuF",
            "https://drive.google.com/uc?export=view&id=1PjT3vmrNVXkDJsuiG8SEkXfe1y7ywAzC",
            "https://drive.google.com/uc?export=view&id=1dUGivUf0q4VQ-mNRKDiO1Ot2zlfknVUg",
            "https://drive.google.com/uc?export=view&id=1_wGopeESDKGdzkAfrGzANPNcNL1T1OtW",
            "https://drive.google.com/uc?export=view&id=1AmCJxAVter40JigxiL9WeEvMSoiJg4fR",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Sulawesi Tengah",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": " Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main badminton sama Yosep",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton f1",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "123450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nguras kolam lele",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Ternak ayam",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": " 124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": " 124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live Tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": " Live tiktok bareng Bryan",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Diving",
                "sosmed": "@afdall.03",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": " 124450131",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Persis",
                "sosmed": "@dafaelpriza_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": " 124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lari",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@andra.lhm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls= [
            "https://drive.google.com/uc?export=view&id=1aNah9E4hA4I349udzmimji0QBK7439E2",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21 Tahun",
                "asal" :"Kalianda",
                "alamat": "Samping kost bang haikal",
                "hobbi": "Ngerjain TA",
                "sosmed": "@arientakhsnl",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21,5 tahun",
                "asal": "Kuala Lumpur",
                "alamat": "Samping kost kak arienta",
                "hobbi": "Pacaran",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "30 Tahun",
                "asal": "Rumah Sakit",
                "alamat": "Belakang Wardat",
                "hobbi": "Kayak irfan",
                "sosmed": "@nobelnizam",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "17 tahun",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek Orang",
                "sosmed": "@desmanhal",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20 Tahun",
                "asal":"Lampung Tengah",
                "alamat": "Sebelah kost jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450008",
                "umur": "10 Tahun",
                "asal":"Di Bandung",
                "alamat": "Kamar haikal",
                "hobbi": "Goreng ayam",
                "sosmed": "@ykeall",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21 Tahun",
                "asal": "Rahim ibu",
                "alamat": "Diatas kost jemar",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "20 tahun",
                "asal": "Debu Tanah",
                "alamat": "Sebelah pasar",
                "hobbi": "Ngegiring anak ayam",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "17 Tahun",
                "asal": "Batam",
                "alamat": "Sebelah kost jemar atau kak arienta",
                "hobbi": "Ngurus pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18 Tahun",
                "asal": "Kampung Orang",
                "alamat": "Nomaden",
                "hobbi": "Duduk sebelah henry",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Depan Pemancingan",
                "hobbi": "Ngoleksi ayam warna warni",
                "sosmed": "@queentanaabila",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19 Tahun",
                "asal": "Lampung",
                "alamat": "Teluk",
                "hobbi": "Main game",
                "sosmed": "@azzelytn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21 Tahun",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "18 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost haikal",
                "hobbi": "Gembala",
                "sosmed": "@jemarrro",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19 tahun",
                "asal": "Lampung tengah",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20 Tahun",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Tidur",
                "sosmed": "@avi.nhr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",   
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }      
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game & travel",
                "sosmed": "@biyokcb",
                "kesan": "JUJUR KEREN BANGETTTT, saya beneran perlu berguru dengan abang",
                "pesan": "Semangatt TA nya nanti banggg, tapi saya beneran butuh banget banyak belajar ke abang karena ilmu abang DAGING semuaaa"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "First impression ku ke kaka, kaka ceria bangettt beneran gemasss",
                "pesan": "Semangatt TA nya kaa, semoga diberikan kelancaran dalam mengerjakan TA, jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "Inspiratif bangett",
                "pesan": "Masih ga nyangka secepat itu abang kembali ke pangkuan-Nya, tapi sekarang abang udah ga sakit lagi ya.. Doa terbaik untuk mu bang Fadil, fly high and rest in peace a good soul"
            },
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Jujur keren keren bangg proker PIKA, saya beneran terkena marketingnya",
                "pesan": "Semangat nanti TA nya bangg, semoga dipermudah jalan dan urusannyaa!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Pinter bangett, beneran saya perlu banyak belajar dari abangg",
                "pesan": "Semangattt bang nanti TA nyaa, semoga dipermudah dan diperlancar semuanyaa, aamiin"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Proker stecu abang beneran membantu saya-^^",
                "pesan": "Abang keren bangett, dilanjutkan ya bangg. Jangan lupa jaga pola tidur dan makan nya!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kaka cantikk",
                "pesan": "Kaka semangat kuliahnya yaa, jaga pola makan dan pola tidurnyaa, jangan sampe drop yaa!!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Cutee",
                "pesan": "kakaa kerennn, semoga kaka selalu menemukan kebaikan di setiap hal hal kecil yaa! jaga kesehatan kaa!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "waktu kaka menjelaskan proker LEGACY jujur keren bangettt",
                "pesan": "Semoga apapun plan kaka bisa tercapai satu persatu ya kaa, semangat kuliahnya dan jaga kesehatan!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Ceria dan social butterfly bangetttt",
                "pesan": "Kaa walau perkuliahan semakin bertambah sem semakin terasa ngebantainya, tapi tetap semangatt ya kaa, jangan lupa jaga pola makan dan pola tidurnyaa jangan sampe drop-!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Gemassss dan ceria bangett",
                "pesan": "Go semangat goo!! kaa semoga kakak selalu diberikan kemudahan di setiap langkah kakak yaa"
            },
            {
                "nama": "Lovianora Saragih",
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
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang kerennn",
                "pesan": "Semangatt terus ya bang kuliahnyaa, jangan lupa jaga kesehatan jugaaa!!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Cantik imut cutee beneran gemass",
                "pesan": "Semoga dunia selalu berbaik hati dengan kakak yaa, semangattt kuliahnyaa kaa!!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Fisrt impression ku ke kaka beneran kagum dan my role modell",
                "pesan": "Kaka beneran keren bangetttt, dari awal kenal saya kagum sama kakaa, tips n trick cara bagi waktu belajar dan organisasi kaa #helppp"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abang kerennnn",
                "pesan": "Semangatttt kuliahnya banggg, jangan lupa jaga kesehatan yaa!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Kerenn tapi sometimes abangnya jail jugaa",
                "pesan": "Semangatt bang kuliahnyaa!!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Kerennn dan pinter bangett",
                "pesan": "Masih keinget saya momen kelompok saya dibantai oleh pertanyaan dari abang, tapi JUJURRR minat banget berguru mengenai komputasi ke abangg karena ilmu abang DAGING BANGETTT"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "CUTEEE, beneran gemas bangettt",
                "pesan": "Semangatt kaa kuliahnyaaa!!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "Inspiratif person",
                "pesan": "Pengalaman abang beneran keren-keren bangett, semoga plan abang satu per satu bisa tercapai ya bangg, aamiin!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Orang serius yang tidak serius",
                "pesan": "Kocak bangett dah, semoga hal hal baik selalu melingkupi hidup abang yaaa, aamiin!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eAqU32uUNzdfHCy9UX8fjMKlHq-aWYV5",
            "https://drive.google.com/uc?export=view&id=1-gYaBmOQjAIcxCfRlJhhMsHR5R4aXUZM",
            "https://drive.google.com/uc?export=view&id=1qOUrpMf8MRQMl6Jrgt1Jtl9H_Bxf-neR",
            "https://drive.google.com/uc?export=view&id=1UtG7Ucs9IrYGdJ_r4B6EBq8AX2kRzqfz",
            "https://drive.google.com/uc?export=view&id=1B52jHEBwiSib3bB0jGBkwt239y8g043c",
            "https://drive.google.com/uc?export=view&id=1r4L8la-ZbymqmUlsN9LJw06iwOv9Lq9O",
            "https://drive.google.com/uc?export=view&id=169-qzBa7lOBjgO1afv8GBLAB3BTP0-rg",
            "https://drive.google.com/uc?export=view&id=1no2bvXf9Pp45eOWksZIMzaIN0ZANifH7",
            "https://drive.google.com/uc?export=view&id=10-Mzh4S617K3VhMhLcEHSmTvLyYH2wfT",
            "https://drive.google.com/uc?export=view&id=1c_KgDlzjcF8Dz8tvbeXDUjp0D7iCDHhZ",
            "https://drive.google.com/uc?export=view&id=1dkHeqQRrXf2oRUEMxymUTKfcn16i3sQ3",
            "https://drive.google.com/uc?export=view&id=10R2ezP-z_CCE75u9Aj5Iao95o1GdHyAa",
            "https://drive.google.com/uc?export=view&id=16M0BS3mcvAQsLz4eHhzt_XVw2D5c02g_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1xqiSPTu40naEMQ-0B75_zggZWqzAWEBl",
            "https://drive.google.com/uc?export=view&id=17Dgn8TTK5DQLCbL3hk0_6j7wITTSwjwL"           
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450006",
                "umur": "20 Tahun",
                "asal":"Sidikalang, Sumut",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang ini asik parah dan yapping banget dan sedikit npd juga",  
                "pesan":"Semoga cepat selesai TA nya bang"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21 Tahun",
                "asal": "Untung suropati",
                "alamat": "..",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya gemas dan cantik bangett, aku suka banget",  
                "pesan":"Semangat terus belajarnya kak"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "11",
                "asal": "Kisaran",
                "alamat": "Untung",
                "hobbi": "NMenyapa satpam ITERA",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Abangnya aktif dan keren banget, aku kagum liatnya",  
                "pesan":"semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "Perumnas way kandis",
                "hobbi": "Ngikutin drama tiktok",                
                "sosmed": "@hnfdzky_",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Ahamad Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "Abangnya asik, baik, dan ternyata receh parah, ketawa mulu",
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "12450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisahkhair.",
                "kesan": "kakak ini baik banget",  
                "pesan":"Semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir belwis",
                "hobbi": "Suka begadang",
                "sosmed": "@cerine_ipynb",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "1244500094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "1244500051",
                "umur": "20 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",                
                "sosmed": "@rozakramdani_",
                "kesan": "Abangnya aktif dan sibuk banget ternyata, tapi baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",                
                "sosmed": "@christiani8872",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 Tahun",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Masak",                
                "sosmed": "@audina_",
                "kesan": "Abangnya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa minang",                
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21 Tahun",
                "asal": "Toba,Sumut",
                "alamat": "Airan Raya",
                "hobbi": "nonton drakor",                
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakaknya lucu, asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20 Tahun",
                "asal":"Sematera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu",                
                "sosmed": "@Muhvinz_",
                "kesan": "Kakaknya lucu, asik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama aqila",                
                "sosmed": "@snasaa._",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()
# Tambahkan menu lainnya sesuai kebutuhan
