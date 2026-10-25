import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import html

st.markdown("""
    <style>
    .centered-title {
        text-align: center;
    }
    .stApp {
            background: linear-gradient(160deg, #DCE8D2 0%, #E9F0DE 50%, #F1F2E3 100%);
            background-attachment: fixed;
            color: var(--bark);
    }
    [data-testid="stHeader"] {
        background: linear-gradient(160deg, #DCE8D2 0%, #E9F0DE 50%, #F1F2E3 100%) !important;
        background-attachment: fixed !important;
    }
    </style>
""", unsafe_allow_html=True)
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
            "Departemen Minbak",
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
            "people-fill"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#FBF8F0"},
            "icon": {"color": "#C08552", "font-size": "16px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#E3EDD9",
            },
            "nav-link-selected": {"background-color": "#6B8F5E"},
        },
    )
    return selected

CSS_BIODATA = """
<style>
.bio-nama {font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0 0.6rem 0;}
.bio-row {display: flex; gap: 0.6rem; font-size: 0.92rem; line-height: 1.5; padding: 3px 0;}
.bio-lbl {min-width: 80px; color: #6b7280; font-weight: 600;}
.bio-val {flex: 1; word-break: break-word;}
</style>
"""

FIELD_BIODATA = ["NIM", "Umur", "Asal", "Alamat", "Hobi", "Sosmed", "Kesan", "Pesan"]


@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img).convert("RGB")
        return ImageOps.fit(img, (400, 500), Image.LANCZOS)
    except Exception:
        return None


def tampilkan_kartu(img, data):
    with st.container(border=True):
        if img is not None:
            st.image(img, use_container_width=True)
        else:
            st.info("Foto tidak tersedia")

        baris = f'<div class="bio-nama">{html.escape(data["Nama"])}</div>'
        for field in FIELD_BIODATA:
            baris += (
                f'<div class="bio-row">'
                f'<span class="bio-lbl">{field}</span>'
                f'<span class="bio-val">: {html.escape(str(data[field]))}</span>'
                f'</div>'
            )
        st.markdown(baris, unsafe_allow_html=True)


def display_images_with_data(gambar_urls, data_list):
    st.markdown(CSS_BIODATA, unsafe_allow_html=True)

    with st.spinner("Memuat foto..."):
        images = [load_image(url) for url in gambar_urls]

    pasangan = list(zip(images, data_list))

    for i in range(0, len(pasangan), 2):
        cols = st.columns(2, gap="medium")
        for col, (img, data) in zip(cols, pasangan[i:i + 2]):
            with col:
                tampilkan_kartu(img, data)
                
menu = streamlit_menu()

if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=14gLX2vsGmh_L9brrI7zq6y05Q2luJMWN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EfrZA3ODDNIq1AZpvJkj9H3E2IsdaUUL&sz=w1000",
                "https://drive.google.com/thumbnail?id=116eOprB8fk1p62Hk9tUOjeWctbqtrsMS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Jxrfrq7sAcbKkXLvjSJS4OO4FxxWQ0e0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DTV94ka3bDfTqjCAe_VHFTsmfyT4XIzX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1v8Uub1z1ckefuwftbRUsEIjKQOdxaPCB&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450103",
                "Asal" : "Batam",
                "Alamat" : "Sekretariat HMSd",
                "Hobi": "Push imo",
                "Umur" : "17",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "Abangnya hangat dan gampang diajak ngobrol, bikin betah.",
                "Pesan" : "Sukses terus, Bang, semoga cepat lulus dan makin lancar urusannya."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Tenang dan menyenangkan, enak banget diajak berdiskusi.",
                "Pesan" : "Semoga selalu diberi kelancaran dan keberkahan, Bang."
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Kakaknya ramah dan perhatian sama adik-adik tingkat.",
                "Pesan" : "Semoga selalu sehat dan sukses dalam semua rencananya, Kak."
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Abangnya seru dan santai, gampang akrab.",
                "Pesan" : "Tetap semangat dan jaga kesehatan ya, Bang."
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Kakaknya sabar dan baik hati, nyaman diajak bicara.",
                "Pesan" : "Semoga semua urusannya dimudahkan, Kak."
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Kakaknya ceria dan bikin suasana jadi menyenangkan.",
                "Pesan" : "Tetap semangat dan semoga kuliahnya lancar terus, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1GsjMZTMiXUodGtHVN1PN-REdfUK2urjJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1MJrO93aEfdPV_e4YFNCM3ySMCZTHC8Su&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZOAcw1NLERIYS31CNVim6V9Q_38XPXvh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PJVWnhMz53VQGceN-Qp7JxY6dIUBV-GV&sz=w1000",
                "https://drive.google.com/thumbnail?id=15ifab3L65bznW_1J1fZdCg52jsKwf8zr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yFgUzujETAR85TdmXKt4kKzJyat9I04I&sz=w1000",
                "https://drive.google.com/thumbnail?id=11G56oZGnQgdN4hdEZk4lWIY6T_ar2oup&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uZxIIZawRwz5k6aEXk3dJ9EDAiYimTJD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=14C_IdcO4kKBQZIlO8oKFL3buXbt34Ick&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bNYcwEYSmAU-7PpC8wPIX111unvhypq0&sz=w1000",
                "https://drive.google.com/thumbnail?id=18xoQXUD55Pw5TX1TVPSkxjLWgTFayS4I&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hMXT0moG7TksrPqzJz4ZCDm7PqraaIji&sz=w1000",
                "https://drive.google.com/thumbnail?id=18d_7wmmf4MSnfWvGUhSI8gY2ttwENrFW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PzUdNAYWjLa2bpC3kGfk6OV_cHCCQdqB&sz=w1000",
                "https://drive.google.com/thumbnail?id=18d_7wmmf4MSnfWvGUhSI8gY2ttwENrFW&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "1250106",
                "Umur": "23",
                "Asal": "Jambi",
                "Alamat": "Jatimulyo",
                "Hobi": "Ngeroasting orang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abangnya humoris dan bikin suasana jadi akrab.",
                "Pesan": "Tetap jadi abang yang asyik dan semangat terus, Bang."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kakaknya baik dan suka membantu.",
                "Pesan": "Semoga kuliahnya lancar dan kebaikan Kakak dibalas berlipat."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Kisaran City",
                "Alamat": "Sukarame",
                "Hobi": "Menyapa satpam ITERA",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Awalnya terlihat tegas, tapi ternyata hangat dan asyik.",
                "Pesan": "Tetap jadi kakak yang ramah dan semangat terus, Kak."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "Abangnya tegas tapi tetap enak diajak ngobrol.",
                "Pesan": "Semoga selalu sukses dan sehat, Bang."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Kakaknya rapi, sopan, dan menyenangkan.",
                "Pesan": "Semangat terus kuliahnya, Kak, semoga lancar."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Kakaknya pintar dan sabar kalau diajak diskusi.",
                "Pesan": "Semoga ilmunya terus berkembang dan makin sukses, Kak."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Abangnya pekerja keras dan suka membantu.",
                "Pesan": "Tetap semangat dan jaga kesehatan ya, Bang."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kakaknya ceria dan bikin suasana jadi nyaman.",
                "Pesan": "Tetap jadi pribadi yang positif dan semangat terus, Kak."
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Abangnya disiplin dan bisa diandalkan.",
                "Pesan": "Semoga selalu lancar dalam setiap kegiatan, Bang."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Kakaknya tegas dan bertanggung jawab.",
                "Pesan": "Semoga makin sukses dan tetap semangat, Kak."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Abangnya berwibawa tapi tetap ramah.",
                "Pesan": "Tetap jadi panutan yang baik ya, Bang."
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kakaknya baik dan suka menolong tanpa pamrih.",
                "Pesan": "Jangan lupa istirahat dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Kakaknya disiplin dan enak diajak kerja sama.",
                "Pesan": "Semangat terus dan semoga kuliahnya lancar, Kak."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Kakaknya pandai memberi saran yang berguna.",
                "Pesan": "Terus jadi kakak yang solutif dan semangat ya, Kak."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya ramah ke semua orang.",
                "Pesan": "Tetap jadi pribadi yang terbuka dan semangat terus, Bang."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Kakaknya ramah dan rendah hati.",
                "Pesan": "Semoga selalu sehat dan sukses, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1V7SKNscbtwlpNVdqS-Oe3jrCFxNQJSW-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aY59DT9njecfNDEMgROnvHlDyHNH9qaO&sz=w1000",
                "https://drive.google.com/thumbnail?id=14rflosL3bnTqrqzZYg6L4283OuP7TQU9&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wHR2ddLrAVDXaME_LASTMS09AA2e3sGq&sz=w1000",
                "https://drive.google.com/thumbnail?id=19-qMXbyNazlpljcNFA71Vk5wvTsmMUi-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VrfZ07ljx7hiJMlfmSR4IFwszbB5-DUV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1u0Nm8vT0q0BxYYT8evWr0RvONsrsajfc&sz=w1000",
                "https://drive.google.com/thumbnail?id=1f7NpiFpZjz0o5OWqV1gsDPPjeogZb0Ip&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PQXOacOc2p3o3gXjRDou0djyXTcBDpuQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EpeyCK67IMkjGNyl5Jnp-Pi4vux_N-w6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LFlSxZDGjJHeO1UtqJWKuiJpHjw022bV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BVmqRNFF6fWvjI7-uKzscvfWI5U6FSwc&sz=w1000",
                "https://drive.google.com/thumbnail?id=18dsvJzei3iQO73Hxrj-Wl0C9KA3_eoRn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1w2gFPBSCozoWl6iZ6SDJiNgbwzvmZ2ZZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EKo-sRzMCc9hfOJ_eNXT14okie7yR_W6&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "NIM" : "123450109",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Panjang, Bandar Lampung",
                "Hobi": "Balap",
                "Umur" : "21",
                "Sosmed" : "@kevinaj__",
                "Kesan" : "Abangnya santai, gampang akrab, dan bisa diandalkan.",
                "Pesan" : "Semangat terus kuliahnya, Bang, semoga lancar."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Abangnya tenang dan wawasannya luas.",
                "Pesan" : "Tetap semangat belajar dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Ali Aristo Muthahari Parisi",
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Abangnya kalem dan rendah hati.",
                "Pesan" : "Semoga selalu lancar dalam setiap urusan, Bang."
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "Kakaknya rajin dan sungguh-sungguh dalam bekerja.",
                "Pesan" : "Semoga semangat belajarnya terus terjaga, Kak."
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Abangnya setia kawan dan bikin suasana seru.",
                "Pesan" : "Tetap jadi teman yang asyik ya, Bang."
            },
            {
                "Nama": "Juwita Sari",
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Kakaknya lembut dan menenangkan.",
                "Pesan" : "Semangat terus dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Abangnya ceria dan kompak sama teman-temannya.",
                "Pesan" : "Terus semangat dan jaga kekompakannya, Bang."
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Kakaknya mudah akrab dan enak diajak diskusi.",
                "Pesan" : "Tetap jadi kakak yang terbuka dan semangat terus, Kak."
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Abangnya bertanggung jawab dan siap membantu.",
                "Pesan" : "Semoga selalu sehat dan sukses, Bang."
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Abangnya teliti dan sabar.",
                "Pesan" : "Tetap semangat dan jangan lupa istirahat, Bang."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Abangnya percaya diri dan menghibur.",
                "Pesan" : "Tetap jadi pribadi yang asyik dan semangat terus, Bang."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Abangnya murah hati dan baik ke teman.",
                "Pesan" : "Semoga kebaikannya selalu dibalas, Bang."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Kakaknya adem dan apa adanya.",
                "Pesan" : "Tetap jadi diri sendiri dan semangat terus, Kak."
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Kakaknya ceria dan punya humor yang khas.",
                "Pesan" : "Terus tebar keceriaan ke sekitar, Kak."
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Abangnya disiplin dan rajin.",
                "Pesan" : "Semoga selalu konsisten dan sukses, Bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1IxHDZ28tJbvUsNi3BS4qQhsL5sv1zkL9&sz=w1000",
                "https://drive.google.com/thumbnail?id=1REPKmZjLeQrNhFGrDwy46n3UlgwattNv&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1guFH06kl-sZz-BWOTyUImand56IGi9SC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ki2EbcmgFWaxMG2TgDyTvFJbZOXiaKbN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oVsz4xtYUxcZ4DR0jj53wx3mVrlN1iY7&sz=w1000",
                "https://drive.google.com/thumbnail?id=18Zg6jfko7skJIx24o_ANh6-wIq9sfJFm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tq4WWCTkQZ_hIIZuQHSfw6F4iMQlahDq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1i1KiWqxUwr3E5eo1q8lY6b0TEwEr45jl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1giTpHNT6kC8TigDF0PVw6pUZtw0bc4uE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1z6f247Lr0bI41VyHD-GxpX6MWOnWQXXF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VhDNTQC6lThfWLQ-8vw--5aBUEUQCSC_&sz=w1000",
                "https://drive.google.com/thumbnail?id=18qbK3nGD4PHSY1k524_4Np3dC8Oit5fS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BQxbFkHIoMqeYsXfir-TIID5NA5FO8Pj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZnEoZaamRgrVzPz7o2suXvJUIM8BleDS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KNfZwpN7WpV3Ss54szaNxUH7twwMuyyy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zkY422qQXnZX-0F98e9Ca4Ku-S34eVtD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jCMHZQy3WS8RbAv4Zj6-Tjy1HuVbwov2&sz=w1000",
                "https://drive.google.com/thumbnail?id=16t5VWBLyH1t7Anf2T6QPn_8ZlC2hJDJm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A_DFAqhjCzKUFOKDLS4zk3-gdjk9z-zD&sz=w1000",
                "https://drive.google.com/thumbnail?id=14e2LWzhnyIne7ErWSK5e_rcs5n1DAnot&sz=w1000"
        ]

        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Abangnya santai, pengertian, dan enak diajak ngobrol.",
                "Pesan" : "Tetap jadi abang yang baik dan semangat terus, Bang."
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Kakaknya tenang dan teliti.",
                "Pesan" : "Semoga kuliahnya lancar dan selalu sehat, Kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Abangnya kalem dan menyenangkan.",
                "Pesan" : "Semangat terus dan tetap berkarya, Bang."
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Kakaknya energik dan cepat akrab.",
                "Pesan" : "Tetap semangat dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Kakaknya kalem dan ramah.",
                "Pesan" : "Semoga selalu sukses dan sehat, Kak."
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Kakaknya aktif dan berani mencoba hal baru.",
                "Pesan" : "Terus semangat dan jangan takut melangkah, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Kakaknya ramah dan selalu ceria.",
                "Pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Kakaknya sopan dan menghargai orang lain.",
                "Pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Kakaknya pendengar yang baik dan nyaman diajak cerita.",
                "Pesan" : "Tetap jadi pribadi yang hangat, Kak."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Kakaknya murah senyum dan enak diajak bicara.",
                "Pesan" : "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Kakaknya sabar dan telaten kalau menjelaskan.",
                "Pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kakaknya kalem tapi tetap hangat.",
                "Pesan" : "Semoga studinya lancar terus, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Abangnya humoris dan gampang bikin suasana cair.",
                "Pesan" : "Tetap semangat kuliahnya, Bang."
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Kakaknya rapi dan percaya diri.",
                "Pesan" : "Tetap jadi inspirasi buat adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Abangnya sportif dan kerja samanya bagus.",
                "Pesan" : "Semangat terus dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Kakaknya sopan dan bijaksana.",
                "Pesan" : "Semoga selalu sukses, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Abangnya santai tapi bertanggung jawab.",
                "Pesan" : "Tetap semangat dan jaga keseimbangannya, Bang."
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Abangnya cekatan soal teknis dan mau berbagi ilmu.",
                "Pesan" : "Semoga ilmu codingnya makin berkembang, Bang."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Abangnya konsisten menjaga pola hidup sehat.",
                "Pesan" : "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Kakaknya ceria dan mudah menyesuaikan diri.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Abangnya kalem dan bisa diandalkan.",
                "Pesan" : "Semangat terus kuliahnya, Bang."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "Abangnya humoris dan bikin suasana cair.",
                "Pesan" : "Semoga selalu sehat dan sukses, Bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/file/d/1hPF4sBBBo2NT6BiPoW61UKMB2-V_9Y4X/view?usp=drive_link",
                "https://drive.google.com/file/d/1IJlMnVTFsnav6X-YbTqOxdGr2PbtR7j2/view?usp=drive_link",
                "https://drive.google.com/file/d/1b-tVBH7WJSaf_utxLlGnCLuwp7Y7hPFG/view?usp=drive_link",
                "https://drive.google.com/file/d/1tll3Kv1m4QPArsu0z73pNKO9m54J4zKi/view?usp=drive_link",
                "https://drive.google.com/file/d/1BV7cdcjDG3FcqPxZD72GEvwoOYhES2V7/view?usp=drive_link",
                "https://drive.google.com/file/d/1uixfalAHL0VhDTxjhH7Z7XCuXEGi9L9U/view?usp=drive_link",
                "https://drive.google.com/file/d/1mwvg1jEvTIfIbYvW3eE5bufkziQ9rfdG/view?usp=drive_link",
                "https://drive.google.com/file/d/1wJgqwZiv5w_4NVZsUAoKCl4O61UiFq8z/view?usp=drive_link",
                "https://drive.google.com/file/d/1pm6vWnXieBbrMPmUUdCO9fHeydQ0vRNP/view?usp=drive_link",
                "https://drive.google.com/file/d/1ulqa7-kxVgW5xiM88nA1RnrYwPBXFPi_/view?usp=drive_link",
                "https://drive.google.com/file/d/1BzGfQs6QFK7VtihZ7p7YA6tFLY49crMv/view?usp=drive_link",
                "https://drive.google.com/file/d/11gwoxZeXHEktovTCb98R6L2XUQNRMSSs/view?usp=drive_link"
        ]

        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobi": "Mencari dan membaca jurnal, mencari pak lucy",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Abangnya santai, enak diajak ngobrol, dan wawasannya luas.",
                "Pesan": "Tetap semangat belajarnya, Bang, semoga risetnya lancar."
 
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya ramah dan menyenangkan.",
                "Pesan": "Terus semangat dan semoga selalu sehat, Kak."    
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kakaknya asyik dan nyambung kalau diajak ngobrol.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus, Kak." 
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Abangnya kalem dan bisa diandalkan.",
                "Pesan": "Terus semangat belajar dan semoga sukses, Bang."
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya gigih dan pekerja keras.",
                "Pesan": "Semangat terus dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya ramah dan gampang akrab.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya tenang dan menyenangkan.",
                "Pesan": "Semangat kuliahnya dan semoga selalu sehat, Kak."
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya ceria dan semangat kerjanya tinggi.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "Abangnya energik dan sportif.",
                "Pesan": "Terus semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Abangnya sabar dan enak diajak ngobrol.",
                "Pesan": "Semoga kuliahnya lancar terus, Bang."
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya ceria dan bikin suasana hangat.",
                "Pesan": "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kakaknya ramah dan seru diajak ngobrol.",
                "Pesan": "Tetap semangat dan sukses terus, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=11VDwF5bKQM76eHup4RMuWSUM8Cfo15z4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uufuN5MFG2iJZqqUJTKIPxM1grsF9Pwp&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vvjVvpKReUjricMWRdLsw33D8VuZwLJh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aU65wU2OPVv9h1qDuCD6mjOovJdt2sgh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CKBx_WI3ThnvhMp-lDzWb9sZeXra0rg_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oxowYVokXUcg4dwITjpBI3PF2g3LJyAk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oYoZMRcM-DFLu8COeukjt1idAgwjOtr8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vhs04fZfvvhcyLsYg_v-onJo8RKPqo6u&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wse-_2njttJF9pi86GLi8r6wjtd-7AIi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D-tk4by71i1mV0UCM1wo7PaenXTNgqfl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Qpo8V09sXUCz9h1kF8bB-SuoTKsmJl7R&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ff87ib_wftm-IOKFIJX5_mnDWm4qu5qT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1REeOZtBuhLIJqUHDG4VYFf3oYBSwWYlu&sz=w1000",
                "https://drive.google.com/thumbnail?id=16Ms9LAB93IsmUwOFWA9QCQZtdGUHzsxZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ne5q9fO8y-O6jvvEUjqjF_6gNZDLC9yI&sz=w1000",
                "https://drive.google.com/thumbnail?id=15OV4g0UAmqsr2Fr9D9qd6W76ev5zoh7x&sz=w1000",
                "https://drive.google.com/thumbnail?id=1c8mdQXhZ2IQdKRIgmrc0D2S7P220v3kn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1MJ08aHK2GOui52GNRwDaD5uBtWucdLHe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1siaoAaQJhZD4LzPe9kYR-FRinrkSxX1X&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WSczqL-wC3OCeK65C20NHZ0sljD3Tv2o&sz=w1000",
                "https://drive.google.com/thumbnail?id=1a8SbFqqWDcf2xuXtnaMlzNkeRJu_QqCe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dpfyzHRR1T0SGlJqEkGE93P0jwD3a9KF&sz=w1000",       
        ]
        
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Kakaknya baik banget,tegas banget.",
                "Pesan": "Semoga selalu lancar kuliahnya dan lulus tepat waktu."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Ga cuma cantik tapi juga pinter.",
                "Pesan": "Semangat terus kuliahnya kakak cantik."
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakaknya cantik banget, seru banget kalo udah ngobrol dan baik.",
                "Pesan": "Keren banget kakak masuk pimnas."
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Abangnya baik banget, asik banget kalo ngobrol.",
                "Pesan": "Keren bang semangat terus kuliahnya."
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Cantik banget baik, lucuu.",
                "Pesan": "Semangat dan lancar terus kuliahnya ya kak."
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Abangnya baik banget, seru juga.",
                "Pesan": "Seamangat terus kuliahnya."
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Abangnya asik banget.",
                "Pesan": "Semangat terus bang."
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Cantik banget my mami, ga cuma cantik tapi juga asik banget.",
                "Pesan": "Lancar terus kuliahnya my mami."
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Sesuai funfact abangnya, selain manis tapi juga humoris.",
                "Pesan": "Lancar terus kuliahnya semoga IPK semester ini 4.00."
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Seru dan asik banget kakanya.",
                "Pesan": "Jangan dingerin omongan orang lain bikin sakit hati ya kak."
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Cantik banget, gemass.",
                "Pesan": "Semangat terus, semoga kuliahnya lancar."
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakaknya ramah dan terbuka.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Abangnya seru dan bikin suasana hidup.",
                "Pesan": "Tetap semangat dan sukses terus, Bang."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakaknya tenang dan menyenangkan diajak ngobrol.",
                "Pesan": "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Kakaknya baik hati dan ramah.",
                "Pesan": "Tetap jadi pribadi yang baik dan semangat terus, Kak."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kakaknya tenang dan kalem.",
                "Pesan": "Semangat kuliahnya dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Abangnya sabar dan telaten.",
                "Pesan": "Semangat terus kuliahnya, Bang."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Abangnya santai dan gampang akrab.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Abangnya kreatif dan punya cara pandang yang unik.",
                "Pesan": "Semangat terus dan sukses selalu, Bang."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Abangnya santai dan menyenangkan.",
                "Pesan": "Tetap semangat dan jadi pribadi yang asyik, Bang."
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Kakaknya ramah dan seru diajak ngobrol.",
                "Pesan": "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kakaknya ramah dan menyenangkan.",
                "Pesan": "Tetap semangat dan sukses selalu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=12XzdAVA23j-raYfoq5qa7YkJbaKevFxK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XYrrhXkwHdo3L2d1XSMotkFre6HQ3ePO&sz=w1000",
                "https://drive.google.com/thumbnail?id=16qyWeTTvCOknp0xZ72R1-qdxlLqpMMGJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZGVUyfgmOaCCfuSxLi-F0WxIUx-DbUdU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1L0xvgeG26Ua9wW9pscoYWx-MHOkcd2jK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1JS1n2eyUFqVx8ZVNLOd9bTuROn1ALBYz&sz=w1000",
                "https://drive.google.com/thumbnail?id=1fDOO8rlgRpjt_YYv-GThqaaHWxW-Pavo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FHbNFQhgjKZKwRZs22sUqBnmOHEWBX9u&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VD5Xkce8zrLw6x5aRcqj-z9EVIZXi9hK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vnEJuSm5TcDmxiHLRtlFSMH5f2CFtdID&sz=w1000",
                "https://drive.google.com/thumbnail?id=11BfeFR83M5LPQRxgMxKBFvm5lKMYYOpJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yEQ5psX75R_ztWkTccVub650NERyw3Z0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oXIG1aMh-xyl800SztE6-p1lr9662Wll&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal": "Bukittinggi",
                "Alamat": "Gh",
                "Hobi": "Cuci baju",
                "Sosmed": "@iamridhomanik",
                "Kesan": "Abangnya kalem, rajin, dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat kuliahnya dan semoga dimudahkan, Bang."
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Kakaknya cantik dan asik.",
                "Pesan": "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Abangnya ramah dan seru.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus, Bang."
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "Abangnya santai dan asyik diajak main bareng.",
                "Pesan": "Tetap semangat dan jangan lupa kuliah, Bang."
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "Kakaknya ceria dan menyenangkan.",
                "Pesan": "Semangat terus, Kak, semoga koleksinya makin lengkap."
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Abangnya santai dan asyik diajak nongkrong.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kakaknya supel dan gampang akrab.",
                "Pesan": "Tetap semangat dan jaga pertemanannya, Kak."
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kakaknya ramah dan seru diajak ngobrol.",
                "Pesan": "Semangat kuliahnya dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Abangnya ramah dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kakaknya sabar dan telaten.",
                "Pesan": "Semangat terus dan semoga selalu sehat, Kak."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Abangnya santai dan disiplin.",
                "Pesan": "Terus semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakaknya tenang dan hangat.",
                "Pesan": "Terus semangat dan sukses selalu, Kak."
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "Kakaknya unik dan menyenangkan.",
                "Pesan": "Tetap ceria dan semangat, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1i_SLs3K1qVszBC2y6HKEDOASh4u2eyxE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1M5eNC41EXWcGZGJCD1MdeRcecoBSw_ym&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-jU4_sFQVyelUqhbYResJywLR6V6pCJ0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lJQ78rrp8Cwpx9zS61ycbYev3vq6qjPw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-mCqas6ObHPGaifYOZighpIONMJp69WK&sz=w1000",
                "https://drive.google.com/thumbnail?id=14aSP81fmYCNP0Yngzx7cogmxMkaQzdAL&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OxN1A1aJ9lxsSnrXSBI1xbznm9RFi_6C&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CmvBpNjeNtiS-IdXptoNrmfoW6ci4Ra_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nc2i4sygradGLCS5om41hNxOCLZ8BSTw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CJpmg7ydQJJkvUmyHK1fV2JLAR_5JGYQ&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya ramah dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat menulis dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Abangnya santai, humoris, dan gampang akrab.",
                "Pesan": "Tetap semangat dan fokus kuliah, Bang."
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya sportif dan energik.",
                "Pesan": "Terus semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia___",
                "Kesan": "Kakaknya ceria dan seru diajak ngobrol.",
                "Pesan": "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya santai dan enak diajak bergaul.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Kakaknya santai dan gampang akrab.",
                "Pesan": "Tetap semangat dan sukses selalu, Kak."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Cantik banget, oufitnya lucu lucu, selain baik dan ramah kakanya juga asikk banget.",
                "Pesan": "Tetep jadi kak aqila yang aku kenal ya kak."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Selain cakep abangnya asik banget kalo waktu ngobrol walaupun sedikit serem kalo ngeliatin.",
                "Pesan": "Kapan bang potong rambut lagi?."
            },
            {
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya kalem dan menyenangkan.",
                "Pesan": "Semangat terus kuliahnya, Kak."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kakaknya tenang dan menyenangkan.",
                "Pesan": "Terus semangat belajarnya dan tetap jadi diri sendiri, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=16BPs0k3o8MGIr_mtlYXWslL1mGOfhfdq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-5zvZGtE_GLjRdTnlRp6esugoGXbG6HU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sNKVcslusYizS1bZYGGSEDI8cp9HLwjK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iAwmRFXzJn-33VUpSBsYSq3JyqjZuscH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YEhPzueV-0NwOlcquKIK0u-WmVu_Ha-o&sz=w1000",
                "https://drive.google.com/thumbnail?id=1f_ey9n4Oi6Cz3sXRcH3ZRkpkvaYZXof0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xdM_RLbR4nxoSCH1ue_caKEQ8bzsljpX&sz=w1000",
                "https://drive.google.com/thumbnail?id=15Xwo56iOed8UpGp_KWijuxlO_vuw8B27&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XFOA2gE58PIYZZVfu_csmeMMkAuTOQje&sz=w1000",
                "https://drive.google.com/thumbnail?id=13MpdvjkgHWBIJLG_gGldtAuNYxGsg6e2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SAx1DiCXo4EUxzv8y6j0CNyUiSnzaF-3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Us76x8rXJNJz6VFOKhzpxEL-Ox3YCpg8&sz=w1000",
                "https://drive.google.com/thumbnail?id=19CrKxtFuvJBakjfwT97cRtngjvQ2xhhI&sz=w1000",
                "https://drive.google.com/thumbnail?id=10ED_o_YG8MhrdWsJx7x_XMMK0oxgg4xB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1M51XeOc9ZKhVyIcZWIBXNflGWQQokEvF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tH80KmUWyXFwLoRQOdjapJSmaion7KwW&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal": "Kalianda",
                "Alamat": "Samping kost Haikal",
                "Hobi": "Naksir cowo cakep",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Kakaknya ramah dan mudah akrab.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Kakaknya tenang dan enak diajak bicara.",
                "Pesan": "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "-",
                "Sosmed": "@nobelnizam",
                "Kesan": "Abangnya kalem, sopan, dan nyaman diajak ngobrol.",
                "Pesan": "Terus semangat dan konsisten belajar, Bang."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "Abangnya santai dan menyenangkan.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus, Bang."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Abangnya supel dan gampang bergaul.",
                "Pesan": "Semangat terus kuliahnya, semoga lancar, Bang."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Abangnya santai dan asyik diajak ngobrol.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat, Bang."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kakaknya aktif dan penuh semangat.",
                "Pesan": "Terus berkembang dan sukses selalu, Kak."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Abangnya dewasa dan bisa diandalkan.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450065",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Nomandenl",
                "Hobi": "Mancing emosi",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kakaknya ceria dan seru diajak bercanda.",
                "Pesan": "Semangat terus belajarnya dan tetap positif, Kak."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Kakaknya ramah dan hangat ke semua orang.",
                "Pesan": "Semoga semua rencananya berjalan lancar, Kak."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Abangnya humoris dan bikin suasana cair.",
                "Pesan": "Terus semangat dan tetap rendah hati, Bang."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kakaknya disiplin dan menjaga pola hidup sehat.",
                "Pesan": "Pertahankan semangatnya ya, Kak."
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Kakaknya pekerja keras dan bertanggung jawab.",
                "Pesan": "Semangat terus dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Jeremi Marolop Partogi Situmorang",
                "NIM": "124450111",
                "Umur": "16",
                "Asal": "Berlin",
                "Alamat": "Samping kos Rafli",
                "Hobi": "Mengembala anak ayam",
                "Sosmed": "@jemarrro",
                "Kesan": "Abangnya santai dan mudah bergaul.",
                "Pesan": "Tetap semangat dan terus belajar hal baru, Bang."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kakaknya ramah dan menyenangkan diajak berteman.",
                "Pesan": "Semoga kuliahnya lancar dan selalu sehat, Kak."
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "20",
                "Asal": "Sibolga",
                "Alamat": "Samping kos Haikal",
                "Hobi": "Nonton",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Abangnya kalem dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan jadi pribadi yang baik, Bang."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "Kakaknya tenang dan apa adanya.",
                "Pesan": "Semangat terus dan jaga kesehatan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1MWqGW20ZyW4EfLcgMqt-ex9vrleLJrQr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1B63LIP_t2W5UHHYcp7M4f1MndQi9N86B&sz=w1000",
                "https://drive.google.com/thumbnail?id=1K01_dacpNrReJIeeDgJWJufZ-zVfGkai&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nkooGAkJ4CJ5gctXjVIEgWh9ps_zVphm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WrJt4N06LmIuFZRdnQ6ML8DQf0koAUyz&sz=w1000",
                "https://drive.google.com/thumbnail?id=1TIssnVc2Kg6ZPB6lfL6r-vROL4ZVBeDb&sz=w1000",
                "https://drive.google.com/thumbnail?id=1IyyZJwi0aQFCWcWZBFdAph7Rj1jMNcUK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XwFSsJxPMedkirDR4XMxraV4RXaaya7G&sz=w1000",
                "https://drive.google.com/thumbnail?id=1deSBvAthulJjGOBXCNlc9opPU54hW4ZA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1u-sMuJ9kJi_7XYHWezaNdDEuzeQT4D8c&sz=w1000",
                "https://drive.google.com/thumbnail?id=1e1RYCxnHf2qga9G42CNqYNpIb7d3y4id&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wDXrqF_YARQf0SLRzc2FeBUQCihOPHjo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Vx8KBYDImBAeDZ43_sbbIcke8yBA7sDV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1T0HY3uNIcVWrsuYEvDm6_baemqQTo1aC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zXUS0S-dgvr4pVSDOXKWBHwGhTaKjr2Q&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BW_mfgFvWNtdNu1QcjwlqMjgx-2Y7In2&sz=w1000",
                "https://drive.google.com/thumbnail?id=17qBJO0JdYoCY71I6J2LdooQw00-ELRfQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1K4cRdhiUSUcJ25F4-mcTAiMFBCVwUIks&sz=w1000"
        ]

        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM": "123450082",
                "Asal": "Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur": "20",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "Orangnya lembut dan punya cara bicara yang bikin nyaman.",
                "Pesan": "Semoga selalu bahagia dan tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM": "123450028",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur": "21",
                "Sosmed": "@donnamaya.p",
                "Kesan": "Orangnya perhatian dan bisa bikin orang lain merasa didengarkan.",
                "Pesan": "Semoga semua hal baik selalu menyertai Kakak dan semua urusannya dilancarkan."
            },
            {
                "Nama": "Labo John Nuel Napitupulu",
                "NIM": "123450037",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Motoran",
                "Umur": "20",
                "Sosmed": "@noerruuu",
                "Kesan": "Orangnya asyik dan punya banyak cerita menarik buat dibagikan.",
                "Pesan": "Semoga makin banyak pengalaman seru dan sukses terus ke depannya, Kak."
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton",
                "Umur": "20",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Orangnya serius kalau mengerjakan sesuatu dan kelihatan bertanggung jawab.",
                "Pesan": "Semoga semua usaha Kakak membuahkan hasil yang terbaik dan makin jago coding."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": "124450104",
                "Asal": "Lampung Timur",
                "Alamat": "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur": "19",
                "Sosmed": "@felisyanbl__",
                "Kesan": "Orangnya seru, suka bercanda, dan bisa bikin suasana jadi lebih ramai.",
                "Pesan": "Jangan pernah kehilangan sisi ceria Kakak dan tetap semangat menjalani hari."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "124450031",
                "Asal": "Jawa Barat",
                "Alamat": "Korpri",
                "Hobi": "Foto Orang",
                "Umur": "21",
                "Sosmed": "@muh_razan_",
                "Kesan": "Orangnya humoris dan gampang mencairkan suasana saat lagi kumpul.",
                "Pesan": "Semoga makin sukses, makin kompak sama teman-teman, dan jangan berhenti berkarya, Kak."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Asal": "Karawang",
                "Alamat": "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur": "21",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Orangnya punya semangat yang kuat dan kelihatan tekun dalam menjalani tanggung jawab.",
                "Pesan": "Semoga selalu diberi kelancaran, terutama untuk TA-nya, dan bisa segera wisuda, Kak."
            },
            {
                "Nama": "Allisha",
                "NIM": "124450019",
                "Asal": "Kayangan",
                "Alamat": "Heaven",
                "Hobi": "Mancing",
                "Umur": "16",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Orangnya mudah bergaul dan punya pembawaan yang bikin suasana jadi akrab.",
                "Pesan": "Semoga selalu dikelilingi orang-orang baik dan makin banyak pengalaman menyenangkan."
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan-jalan",
                "Umur": "19",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Orangnya terbuka dengan hal baru dan punya semangat buat mencoba banyak hal.",
                "Pesan": "Semoga bisa terus berkembang, berani mencoba hal baru, dan meraih apa yang dicita-citakan."
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Asal": "Lampung Selatan",
                "Alamat": "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur": "20",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Orangnya rajin dan punya kemauan yang kuat untuk terus belajar.",
                "Pesan": "Semoga ilmu yang didapat selalu bermanfaat dan semua target belajarnya tercapai, Kak."
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": "124450043",
                "Asal": "Pagar Alam",
                "Alamat": "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur": "20",
                "Sosmed": "@difanyhsa",
                "Kesan": "Orangnya sopan dan pembawaannya tenang saat berinteraksi dengan orang lain.",
                "Pesan": "Semoga selalu diberi kesehatan, ketenangan hati, dan kemudahan dalam setiap urusan."
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM": "124450054",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Berenang",
                "Umur": "20",
                "Sosmed": "@nzlhauly_",
                "Kesan": "Orangnya punya pembawaan yang anggun dan terlihat percaya diri.",
                "Pesan": "Semoga makin percaya diri, terus berkembang, dan semua impiannya bisa tercapai, Kak."
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM": "123450041",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur": "20",
                "Sosmed": "@r.hanaap",
                "Kesan": "Orangnya tenang dan punya cara tersendiri untuk menyampaikan pikiran.",
                "Pesan": "Semoga tulisan dan ide-ide Kakak bisa terus berkembang dan menginspirasi banyak orang."
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobi": "-",
                "Umur": "21",
                "Sosmed": "@daffascript",
                "Kesan": "Orangnya kalem dan punya pembawaan yang santai saat bersama teman-teman.",
                "Pesan": "Semoga makin nyaman berinteraksi dengan siapa saja dan sukses selalu ke depannya, Kak."
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Nonton Anime",
                "Umur": "20",
                "Sosmed": "@edsel_0712",
                "Kesan": "Orangnya santai dan punya selera humor yang bikin obrolan jadi seru.",
                "Pesan": "Semoga selalu punya alasan buat tertawa dan semua kegiatannya berjalan lancar, Kak."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "NIM": "124450085",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Umur": "20",
                "Sosmed": "@luciarachel_",
                "Kesan": "Orangnya penuh energi dan bisa membawa semangat positif ke sekitarnya.",
                "Pesan": "Semoga semangatnya selalu terjaga, sehat terus, dan makin banyak hal seru yang bisa dicoba."
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "124450124",
                "Asal": "Lampung Tengah",
                "Alamat": "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur": "20",
                "Sosmed": "@_shaazzh",
                "Kesan": "Orangnya apa adanya dan punya cara yang bikin orang lain merasa santai.",
                "Pesan": "Semoga terus berkarya lewat lukisan dan tulisan, serta tetap jadi diri sendiri, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "124450112",
                "Asal": "Lampung Timur",
                "Alamat": "Rajabasa",
                "Hobi": "Begong",
                "Umur": "18",
                "Sosmed": "@xifasky",
                "Kesan": "Orangnya sopan dan bisa menghargai orang-orang di sekitarnya.",
                "Pesan": "Semoga selalu diberi kemudahan dalam menjalani aktivitas dan semua keinginannya tercapai, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()