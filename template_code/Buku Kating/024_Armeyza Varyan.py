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
 # KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1oyiOtilxOa8dFScyE1Q6Uh8De4wf7bTD&sz=w1000",
            "https://drive.google.com/thumbnail?id=19GLvW4o6gxq2EtgtoVsnaiDZaQ77T1XH&sz=w1000"
        ]

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450103",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Abangya keren dan berwibawa",
                "Pesan" : "terus semangat dalam mengemban tugas sebagai kepala himpunan bang"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Abang ini keren sekali, santai dalam menjelaskan, mantap dalam aksi",
                "Pesan" : "mantap bang terima kasih atas ilmunya"
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "kakak orang yang ceria dan lucu",
                "Pesan" : "Tetap semangat dalam mengemban tugas sebagai sekretaris himpunan kak.."
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Cara bicaranya santai dan ilmunya berisi",
                "Pesan" : "Semangat bang dalam mengemban tugas dan tetap berjuang demi himpunan."
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Kakaknya humble dan baik.",
                "Pesan" : "semangat kak mengemban tugas dan tetaplah membagikan ilmu."
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Sosoknya ramah dan penuh semangat.",
                "Pesan" : "Tetap semangat dalam menjalankan tugas dan terus maju demi himpunan kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

#INTERNAL
if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1D6qoaQyWhZssgUrmmSXbPeD_kAUVstdM&sz=w1000",
            "https://drive.google.com/thumbnail?id=1j839G4eFmy2ggaj7vY05_mT-c7V49Qq8&sz=w1000"

        ]

        data_list = [
            {
              "Nama": "Haikal Fransisko Simbolon",
              "NIM": "",
              "Umur": "",
              "Asal": "",
              "Alamat": "",
              "Hobi": "",
              "Sosmed": "",
              "Kesan": "Komunikatif dan pandai mencairkan suasana.",
              "Pesan": "Tetap jadi pembawa energi positif."
            },
            {
              "Nama": "Kharisma Mustika Sari",
              "NIM": "",
              "Umur": "",
              "Asal": "",
              "Alamat": "",
              "Hobi": "",
              "Sosmed": "",
              "Kesan": "Penyampaian tenang dan enak diajak diskusi.",
              "Pesan": "Pertahankan gaya komunikasi yang suportif."
            },
            {
              "Nama": "Hanna Gresia Sinaga",
              "NIM": "",
              "Umur": "",
              "Asal": "",
              "Alamat": "",
              "Hobi": "",
              "Sosmed": "",
              "Kesan": "Senior yang merangkul dan tulus membimbing.",
              "Pesan": "Sukses terus buat kuliah dan kariernya."
            },
            {
              "Nama": "Ahmad Farhan Ghani",
              "NIM": "123450121",
              "Umur": "21",
              "Asal": "Kemiling",
              "Alamat": "Kemiling",
              "Hobi": "Supporteran",
              "Sosmed": "@farhanghani",
              "Kesan": "Jiwa memimpin kuat dan penuh semangat.",
              "Pesan": "Jaga kesehatan di tengah kesibukan."
            },
            {
              "Nama": "Aisyah Khairun Nisa",
              "NIM": "124450096",
              "Umur": "18",
              "Asal": "Indragiri",
              "Alamat": "Samping Makam Perwira 2",
              "Hobi": "Nyicipin Makanan",
              "Sosmed": "@aisyahkhair._",
              "Kesan": "Santai tapi cermat dan bertanggung jawab.",
              "Pesan": "Terus eksplor hal-hal baru."
            },
            {
              "Nama": "Cerine Sihotang",
              "NIM": "124450049",
              "Umur": "20",
              "Asal": "Medan",
              "Alamat": "Belwis",
              "Hobi": "Suka Ngoding pakai R",
              "Sosmed": "@cerine_ipynb",
              "Kesan": "Analitis dan cepat atasi masalah.",
              "Pesan": "Terus kembangkan skill ngodingnya."
            },
            {
              "Nama": "Jaya Saputra Tamba",
              "NIM": "124450094",
              "Umur": "18",
              "Asal": "Medan",
              "Alamat": "Pemda",
              "Hobi": "Mencari Nafkah",
              "Sosmed": "@jay.saputra.mb",
              "Kesan": "Pekerja keras dan bermental tangguh.",
              "Pesan": "Semoga usaha kerasnya berbuah manis."
            },
            {
              "Nama": "Najla Nursyifa",
              "NIM": "124450051",
              "Umur": "20",
              "Asal": "Sumatra Barat",
              "Alamat": "Belwis",
              "Hobi": "Nonton ASMR",
              "Sosmed": "@njlanursyifa",
              "Kesan": "Humoris dan bikin suasana segar.",
              "Pesan": "Jaga terus keceriaannya."
            },
            {
              "Nama": "Rozak Ramdani",
              "NIM": "124450100",
              "Umur": "19",
              "Asal": "Kalianda, Lampung Selatan",
              "Alamat": "Korpri Raya",
              "Hobi": "Berantemin Kucing",
              "Sosmed": "@rozakrabbani__",
              "Kesan": "Pola pikir unik dan konsisten.",
              "Pesan": "Pertahankan kedisiplinannya."
            },
            {
              "Nama": "Teresa Christiani Purba",
              "NIM": "124450046",
              "Umur": "19",
              "Asal": "Riau",
              "Alamat": "Belwis",
              "Hobi": "Masak",
              "Sosmed": "@kristiani8872",
              "Kesan": "Tegas dan bijak mengambil kendali.",
              "Pesan": "Makin matang dalam memimpin."
            },
            {
              "Nama": "Muhammad Hanif Dzaky Arifin",
              "NIM": "123450064",
              "Umur": "21",
              "Asal": "Padang",
              "Alamat": "Way Kandis",
              "Hobi": "Nonton F1 & MotoGP",
              "Sosmed": "@hnfdzky_",
              "Kesan": "Keren, tenang, dan cepat tanggap.",
              "Pesan": "Tetap fokus capai targetmu."
            },
            {
              "Nama": "Audina Fitria",
              "NIM": "124450038",
              "Umur": "20",
              "Asal": "Sumatra Barat",
              "Alamat": "Sukarame",
              "Hobi": "Masak",
              "Sosmed": "@audinaf_03",
              "Kesan": "Sigap membantu dan terstruktur.",
              "Pesan": "Jangan lupa utamakan istirahat."
            },
            {
              "Nama": "Cika Adelia Br Marbun",
              "NIM": "124450107",
              "Umur": "20",
              "Asal": "Bagan Batu, Riau",
              "Alamat": "Belwis",
              "Hobi": "Dengerin Musik",
              "Sosmed": "@cikamrbn",
              "Kesan": "Sangat disiplin dan menghargai waktu.",
              "Pesan": "Tularkan kebiasaan teraturnya."
            },
            {
              "Nama": "Gustin H Tampubolon",
              "NIM": "124450068",
              "Umur": "21",
              "Asal": "Sumatera Utara",
              "Alamat": "Airan",
              "Hobi": "Nonton",
              "Sosmed": "@gustinhaleluya",
              "Kesan": "Realistis dan solutif saat ada masalah.",
              "Pesan": "Pertahankan pemikiran kritisnya."
            },
            {
              "Nama": "Muhammad Harvinsyah",
              "NIM": "124450128",
              "Umur": "20",
              "Asal": "Sumatera Selatan",
              "Alamat": "Belwis",
              "Hobi": "Ngadu Ikan Cupang",
              "Sosmed": "@muhvinz_",
              "Kesan": "Supel dan gampang berbaur.",
              "Pesan": "Pertahankan sifat ramahnya."
            },
            {
              "Nama": "Rafa Sabina Fahimah",
              "NIM": "124450036",
              "Umur": "20",
              "Asal": "Natar",
              "Alamat": "Natar",
              "Hobi": "Nonton Drakor",
              "Sosmed": "@snasaa._",
              "Kesan": "Kalem dan menyenangkan diajak bicara.",
              "Pesan": "Semoga selalu di lingkungan yang baik."
            }
          ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

# MINBAK
if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1oydxxc_tW_dhrx67iEBOQ0eO2PWXs-Rm&sz=w1000",
            "https://drive.google.com/thumbnail?id=1oWIN2qgDFKYjFtUxVQ_mCSbNIlUy2Cmn&sz=w1000"
        ]

        data_list = [
            {
              "Nama": "Kevin Antonio Junior",
              "NIM": "123450109",
              "Asal": "Bandar Lampung",
              "Alamat": "Panjang, Bandar Lampung",
              "Hobi": "Balap",
              "Umur": "21",
              "Sosmed": "@kevinaj__",
              "Kesan": "Sigap dan bisa diandalkan.",
              "Pesan": "Tetap tegas dan berani."
            },
            {
              "Nama": "Gusti Putu Ferazka Dhiyamika",
              "NIM": "123450046",
              "Asal": "Lampung Utara",
              "Alamat": "Way Halim",
              "Hobi": "Baca",
              "Umur": "21",
              "Sosmed": "@ferazkaa",
              "Kesan": "Berwawasan luas dan kritis.",
              "Pesan": "Terus bagikan ilmunya."
            },
            {
              "Nama": "Ari Aristo Muthahari Parisi",
              "NIM": "123450088",
              "Asal": "Lampung Timur",
              "Alamat": "Gang Sakum, Belwis",
              "Hobi": "Nonton F1",
              "Umur": "21",
              "Sosmed": "@ali_parisi3",
              "Kesan": "Tenang di situasi sulit.",
              "Pesan": "Pertahankan sikap dinginnya."
            },
            {
              "Nama": "Ayu Andriani Parlina Wati",
              "NIM": "124450058",
              "Asal": "Lampung Barat",
              "Alamat": "Airan",
              "Hobi": "Belajar",
              "Umur": "20",
              "Sosmed": "@aayuandrianni_",
              "Kesan": "Tekun dan penuh dedikasi.",
              "Pesan": "Jangan lupa istirahat, Kak."
            },
            {
              "Nama": "Dafa Elpriza",
              "NIM": "124450131",
              "Asal": "Bekasi",
              "Alamat": "Way Kandis",
              "Hobi": "Nemenin Bryan live TikTok",
              "Umur": "21",
              "Sosmed": "@dafaelpriza_",
              "Kesan": "Solider dan seru.",
              "Pesan": "Jaga kekompakan ini."
            },
            {
              "Nama": "Juwita Sari",
              "NIM": "124450066",
              "Asal": "Lampung Barat",
              "Alamat": "Pemda",
              "Hobi": "Lihat bulan",
              "Umur": "19",
              "Sosmed": "@ju.juwitaaa_",
              "Kesan": "Lembut dan empati tinggi.",
              "Pesan": "Tetap jadi penyabar."
            },
            {
              "Nama": "Muhammad Afdal Lutfi",
              "NIM": "124450047",
              "Asal": "Lampung Tengah",
              "Alamat": "Jl Pulau Damar",
              "Hobi": "Taptap layar kalo Bryan live",
              "Umur": "19",
              "Sosmed": "@afdall.03",
              "Kesan": "Ringan tangan membantu.",
              "Pesan": "Pertahankan sifat baiknya."
            },
            {
              "Nama": "Salsabila Nazwa Putri",
              "NIM": "124450002",
              "Asal": "Metro",
              "Alamat": "Korpri",
              "Hobi": "Nongkrong di Kopken",
              "Umur": "20",
              "Sosmed": "@slbnzw_",
              "Kesan": "Ramah dan komunikatif.",
              "Pesan": "Tetap terbuka ke siapa pun."
            },
            {
              "Nama": "Muhammad Ridwan",
              "NIM": "123450091",
              "Asal": "Lampung Tengah",
              "Alamat": "Belwis",
              "Hobi": "Nganterin Datasena ke gedung F",
              "Umur": "21",
              "Sosmed": "@mridwaan_22",
              "Kesan": "Tanggung jawab dan cekatan.",
              "Pesan": "Sukses terus buat Kakak."
            },
            {
              "Nama": "Andra Ilham Bintang",
              "NIM": "124450060",
              "Asal": "Sumatera Selatan",
              "Alamat": "Kota Baru",
              "Hobi": "Ngitungin kelopak bunga di kebun",
              "Umur": "18",
              "Sosmed": "@andra.lhm",
              "Kesan": "Sabar dan teliti.",
              "Pesan": "Pertahankan ketelitiannya."
            },
            {
              "Nama": "Bryan Paskah Telaumbanua",
              "NIM": "124450003",
              "Asal": "Nias",
              "Alamat": "Belwis",
              "Hobi": "Live TikTok",
              "Umur": "22",
              "Sosmed": "@bryantel_",
              "Kesan": "Percaya diri dan ramai.",
              "Pesan": "Terus jadi diri sendiri."
            },
            {
              "Nama": "Ghiyats Thabularasa Meardhy",
              "NIM": "124450067",
              "Asal": "Bekasi",
              "Alamat": "Korpri",
              "Hobi": "Ngegift live Bryan",
              "Umur": "17",
              "Sosmed": "@meardhy_ghiyats",
              "Kesan": "Baik dan royal.",
              "Pesan": "Semoga kebaikanmu berbalas."
            },
            {
              "Nama": "Indah Julia Mawar Pratiwi",
              "NIM": "124450055",
              "Asal": "Pringsewu",
              "Alamat": "Airan",
              "Hobi": "Bengong",
              "Umur": "Belum Tahu",
              "Sosmed": "@indahjuliaa",
              "Kesan": "Kalem dan sederhana.",
              "Pesan": "Tetap apa adanya, Kak."
            },
            {
              "Nama": "Jacinda Kesya Alvara",
              "NIM": "124450023",
              "Asal": "Kalimantan Barat",
              "Alamat": "Korpri",
              "Hobi": "Nyapu depan gacoan",
              "Umur": "18",
              "Sosmed": "@cacalvra",
              "Kesan": "Ceria dan bikin terhibur.",
              "Pesan": "Terus tebar tawa."
            },
            {
              "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
              "NIM": "124450089",
              "Asal": "Padang",
              "Alamat": "Kota Baru",
              "Hobi": "Bangun pagi",
              "Umur": "20",
              "Sosmed": "@muhammdrafka_",
              "Kesan": "Sangat disiplin waktu.",
              "Pesan": "Pertahankan etos kerjanya."
            }
          ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=16oa-kfSJu6E0Cl8qWloAvGdF8TGtvyAy&sz=w1000",
            "https://drive.google.com/thumbnail?id=1LzN_W1HPL0tBMX4JO-WKOYSKVnI2DKGZ&sz=w1000"
        ]

        data_list = [
            {
              "Nama": "Fabio Banyu Cyto",
              "NIM": "12340104",
              "Asal": "Bandar Lampung",
              "Alamat": "Kedaton",
              "Hobi": "Tidur",
              "Umur": "21",
              "Sosmed": "@biyokcb",
              "Kesan": "Santai dan pengertian.",
              "Pesan": "Tetap jadi abang yang baik."
            },
            {
              "Nama": "Tanty Widiyastuti",
              "NIM": "123450094",
              "Asal": "Lampung",
              "Alamat": "Airan Raya",
              "Hobi": "Membaca",
              "Umur": "21",
              "Sosmed": "@tvnty_",
              "Kesan": "Tenang dan detail.",
              "Pesan": "Pertahankan ketelitiannya."
            },
            {
              "Nama": "Fadil Prasetyo Alfaritzi",
              "NIM": "Belum Tahu",
              "Asal": "Bandar Lampungku",
              "Alamat": "Bandar Lampung",
              "Hobi": "Gitar",
              "Umur": "21",
              "Sosmed": "@fadilalfarizzii",
              "Kesan": "Musikal dan bikin nyaman.",
              "Pesan": "Terus berkarya lewat musik."
            },
            {
              "Nama": "Manuel Frederika",
              "NIM": "124450039",
              "Asal": "Batam",
              "Alamat": "Way Kandis",
              "Hobi": "Tenis meja",
              "Umur": "20",
              "Sosmed": "@manuelfdk_",
              "Kesan": "Energik dan cepat baur.",
              "Pesan": "Semangat terus, Kak."
            },
            {
              "Nama": "Ni Made Okta Viola Darma Putri",
              "NIM": "124450005",
              "Asal": "Bali",
              "Alamat": "Nusa Penida",
              "Hobi": "Menghayal",
              "Umur": "12",
              "Sosmed": "Violaadrtr_",
              "Kesan": "Kalem dan imajinatif.",
              "Pesan": "Kembangkan ide-ide kreatifmu."
            },
            {
              "Nama": "Risa Romadona",
              "NIM": "124450127",
              "Asal": "Natar",
              "Alamat": "Natar",
              "Hobi": "Rolling skate",
              "Umur": "20",
              "Sosmed": "risarmdna",
              "Kesan": "Aktif dan berani.",
              "Pesan": "Terus eksplor hal baru."
            },
            {
              "Nama": "Vannisa Ramadhani",
              "NIM": "124450078",
              "Asal": "Kepulauan Riau",
              "Alamat": "Teluk Betung",
              "Hobi": "Nonton KHW",
              "Umur": "19",
              "Sosmed": "@vunnycaa",
              "Kesan": "Ramah dan ceria.",
              "Pesan": "Jaga energi positifnya."
            },
            {
              "Nama": "Yulia Cristine Malau",
              "NIM": "Belum Tahu",
              "Asal": "Belum Tahu",
              "Alamat": "Belum Tahu",
              "Hobi": "Belum Tahu",
              "Umur": "Belum Tahu",
              "Sosmed": "Belum Tahu",
              "Kesan": "Sopan dan santun.",
              "Pesan": "Sukses untuk segala urusannya."
            },
            {
              "Nama": "Akeyla Fairuz Shafi",
              "NIM": "1234501",
              "Asal": "Bandar Lampung",
              "Alamat": "Bandar Lampung",
              "Hobi": "Dengerin Musik",
              "Umur": "21",
              "Sosmed": "@keyashafi",
              "Kesan": "Pendengar yang baik.",
              "Pesan": "Tetap jadi teman cerita yang asyik."
            },
            {
              "Nama": "Elsa Sitorus",
              "NIM": "124450088",
              "Asal": "Sumatera Utara",
              "Alamat": "Pemda",
              "Hobi": "Rebahan",
              "Umur": "21",
              "Sosmed": "_els.a",
              "Kesan": "Murah senyum dan hangat.",
              "Pesan": "Pertahankan keramahannya."
            },
            {
              "Nama": "Fadya Izzatul ‘Aini",
              "NIM": "124450062",
              "Asal": "Pringsewu",
              "Alamat": "Airan",
              "Hobi": "Mancing",
              "Umur": "20",
              "Sosmed": "fadyaizzatul_",
              "Kesan": "Sabar membimbing.",
              "Pesan": "Terus bimbing kami, Kak."
            },
            {
              "Nama": "Lovianora Saragih",
              "NIM": "124450105",
              "Asal": "Sumatera Utara",
              "Alamat": "Way Huwi",
              "Hobi": "Dengerin Musik",
              "Umur": "19",
              "Sosmed": "_loviaa",
              "Kesan": "Kalem tapi ramah.",
              "Pesan": "Lancarkan studinya, Kak."
            },
            {
              "Nama": "M. Alsi Syahrulloh",
              "NIM": "124450092",
              "Asal": "Kalianda",
              "Alamat": "Kotabaru",
              "Hobi": "Main Game, Tidur",
              "Umur": "20",
              "Sosmed": "@aluccy_",
              "Kesan": "Humoris dan seru.",
              "Pesan": "Tetap fokus kuliahnya."
            },
            {
              "Nama": "Sherena Florencia",
              "NIM": "124450027",
              "Asal": "Bengkulu Selatan",
              "Alamat": "Belwis",
              "Hobi": "Make up",
              "Umur": "19",
              "Sosmed": "sher_renna",
              "Kesan": "Rapi dan percaya diri.",
              "Pesan": "Terus jadi inspirasi."
            },
            {
              "Nama": "Razin Hafid Hamdi",
              "NIM": "123450096",
              "Asal": "Padang",
              "Alamat": "Belwis",
              "Hobi": "Futsal",
              "Umur": "21",
              "Sosmed": "@razyn.hfd",
              "Kesan": "Sportif dan kompak.",
              "Pesan": "Pertahankan kerja samanya."
            },
            {
              "Nama": "Faiza Try Anjani",
              "NIM": "124450075",
              "Asal": "Padang",
              "Alamat": "Belwis",
              "Hobi": "Membaca Novel",
              "Umur": "19",
              "Sosmed": "FAIZAANJANII",
              "Kesan": "Sopan dan bijak.",
              "Pesan": "Tetap jadi panutan."
            },
            {
              "Nama": "Gathfan Nadif Ali",
              "NIM": "124450001",
              "Asal": "Bandar Lampung",
              "Alamat": "Rajabasa",
              "Hobi": "Main game",
              "Umur": "20",
              "Sosmed": "@gathfannadif",
              "Kesan": "Santai tapi tanggung jawab.",
              "Pesan": "Jaga terus komitmennya."
            },
            {
              "Nama": "Hafidz Wahdiansyah",
              "NIM": "124450064",
              "Asal": "Metro",
              "Alamat": "Metro Kibang, Lampung Timur",
              "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
              "Umur": "20",
              "Sosmed": "@apiszzaja_",
              "Kesan": "Cekatan dan solutif.",
              "Pesan": "Bagi-bagi ilmunya, Kak."
            },
            {
              "Nama": "Kaleb Filbert Istel",
              "NIM": "124450053",
              "Asal": "Bandar Lampung",
              "Alamat": "Campang Raya",
              "Hobi": "Ngegym, baca novel",
              "Umur": "20",
              "Sosmed": "@kelelep_comberan",
              "Kesan": "Konsisten dan disiplin.",
              "Pesan": "Semangat hidup sehatnya."
            },
            {
              "Nama": "Melva Shaprina Febrianti",
              "NIM": "124450087",
              "Asal": "Sumsel",
              "Alamat": "Sukarame",
              "Hobi": "Scroll",
              "Umur": "19",
              "Sosmed": "@melva_fbrt",
              "Kesan": "Ceria dan adaptif.",
              "Pesan": "Pertahankan sifat supelnya."
            },
            {
              "Nama": "Muhammad Syafiqul Falakh",
              "NIM": "Belum Tahu",
              "Asal": "Belum Tahu",
              "Alamat": "Belum Tahu",
              "Hobi": "Belum Tahu",
              "Umur": "Belum Tahu",
              "Sosmed": "@syaafiqui",
              "Kesan": "Pendiam tapi diandalkan.",
              "Pesan": "Makin terbuka ke tim."
            },
            {
              "Nama": "Rifky Henry Ferdianto",
              "NIM": "124450115",
              "Asal": "Kobum",
              "Alamat": "Rajabasa",
              "Hobi": "Lari dari kenyataan",
              "Umur": "28",
              "Sosmed": "henryferdianto",
              "Kesan": "Lucu dan menghibur.",
              "Pesan": "Sukses terus urusannya."
            }
          ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [

        ]
        data_list = [
                {
                  "Nama": "Nayla Salsabila Fathianisa",
                  "NIM": "123450082",
                  "Asal": "Payakumbuh, Sumatera Barat",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Rebahan",
                  "Umur": "20",
                  "Sosmed": "@naylasalsabilaa._",
                  "Kesan": "Sangat fokus dan selalu siap eksekusi target organisasi.",
                  "Pesan": "Ganjal rasa lelahmu dengan prestasi besar berikutnya."
                },
                {
                  "Nama": "Donna Maya Puspita",
                  "NIM": "123450028",
                  "Asal": "Bekasi dan Lampung",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Mendengarkan musik",
                  "Umur": "21",
                  "Sosmed": "@donnamaya.p",
                  "Kesan": "Tegas, lugas, dan to the point saat mengambil tindakan.",
                  "Pesan": "Asah terus naluri kepemimpinan tajam yang kamu punya."
                },
                {
                  "Nama": "Labo John Nuel Napitupulu",
                  "NIM": "37",
                  "Asal": "Medan, Jakut, Palembang",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Berburu burung",
                  "Umur": "20",
                  "Sosmed": "@noerruuu",
                  "Kesan": "Tipe eksekutor handal yang lebih suka kerja daripada banyak wacana.",
                  "Pesan": "Terus jadi penggerak utama di setiap proyek tim."
                },
                {
                  "Nama": "Anash Tasya Ausyaqila",
                  "NIM": "124450050",
                  "Asal": "Bandar Lampung",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Ngoding",
                  "Umur": "20",
                  "Sosmed": "@anshtsyaaql",
                  "Kesan": "Punya *aura pembawa acara* yang hidup dan pandai memecah keheningan.",
                  "Pesan": "Jangan sembunyikan bakat komunikasimu di balik layar monitor."
                },
                {
                  "Nama": "Felisya Nabila Putri Nugroho",
                  "NIM": "124450104",
                  "Asal": "Bekasi",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Ngejahilin mama",
                  "Umur": "18",
                  "Sosmed": "@felisyanbl__",
                  "Kesan": "Serius, penuh disiplin, dan matang sebelum bertindak.",
                  "Pesan": "Sesekali longgarkan standar tinggimu agar tidak cepat lelah."
                },
                {
                  "Nama": "Muhammad Razan Maulana Pratama",
                  "NIM": "124450031",
                  "Asal": "Sibolga",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Jahilin Felisya",
                  "Umur": "18",
                  "Sosmed": "@muh_razan_",
                  "Kesan": "Tipe pemikir strategis yang sangat memperhitungkan langkah.",
                  "Pesan": "Salurkan kecerdasan taktikmu untuk memimpin agenda besar."
                },
                {
                  "Nama": "Sania Dwi Ayu Lestari",
                  "NIM": "123450086",
                  "Asal": "Bandung",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Bimbingan TA",
                  "Umur": "21",
                  "Sosmed": "@saniayyllstr",
                  "Kesan": "Sangat santai menghadapi tenggat waktu tanpa beban berlebih.",
                  "Pesan": "Bagi rahasia tetap tenangmu di tengah gempuran revisi."
                },
                {
                  "Nama": "Allisha",
                  "NIM": "124450019",
                  "Asal": "Rahim ibu",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah",
                  "Umur": "6",
                  "Sosmed": "@aallishaa.a",
                  "Kesan": "Independen dan sangat berani mengambil kendali sendirian.",
                  "Pesan": "Terus dobrak batasan diri tanpa ragu pada potensimu."
                },
                {
                  "Nama": "Alya Ramadhanti",
                  "NIM": "124450091",
                  "Asal": "Kota banyak sawit",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Apa aja",
                  "Umur": "19",
                  "Sosmed": "@alya.rmdhnti",
                  "Kesan": "Prinsipnya kuat dan punya garis patokan kerja yang sangat jelas.",
                  "Pesan": "Pertahankan keteguhan dalam memegang komitmen awal."
                },
                {
                  "Nama": "Bunga Clarisa Sefa",
                  "NIM": "124450097",
                  "Asal": "Lampung Selatan",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Belajar",
                  "Umur": "20",
                  "Sosmed": "@bungaclrssf",
                  "Kesan": "Jiwa seni dan kreativitas visualnya sangat dominan di lapangan.",
                  "Pesan": "Imbangi teori akademis dengan gebrakan inovasi praktik."
                },
                {
                  "Nama": "Difanya Husakina",
                  "NIM": "124450043",
                  "Asal": "Deket Kebun Teh",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Alhamdulillah Dzikir dan sholawatan",
                  "Umur": "20",
                  "Sosmed": "@difanyhsa",
                  "Kesan": "Punya ambisi tinggi dan daya dobrak pantang mundur.",
                  "Pesan": "Terus pacu prestasimu sampai ke level tertinggi."
                },
                {
                  "Nama": "Nazlah Auliya",
                  "NIM": "124450054",
                  "Asal": "Bandar Lampung",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Ballet",
                  "Umur": "20",
                  "Sosmed": "@nzlhauly_",
                  "Kesan": "Lincah, sigap teknis, dan serba bisa di segala kondisi.",
                  "Pesan": "Pertahankan kelincahanmu dalam menyelesaikan hambatan rumit."
                },
                {
                  "Nama": "Raihana Adelia Putri",
                  "NIM": "123450041",
                  "Asal": "Lampung Tengah",
                  "Alamat": "Airan Raya 1",
                  "Hobi": "Menulis, membaca",
                  "Umur": "20",
                  "Sosmed": "@r.hanaap",
                  "Kesan": "Lugas, ekspresif, dan berani bersuara vokal di muka umum.",
                  "Pesan": "Ubah wawasan tulisanmu menjadi aksi nyata berani."
                },
                {
                  "Nama": "Daffa Kharisma Adzana",
                  "NIM": "Belum Tahu",
                  "Asal": "Belum Tahu",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Belum Tahu",
                  "Umur": "Belum Tahu",
                  "Sosmed": "Belum Tahu",
                  "Kesan": "Sangat ekspresif dan dominan saat bertukar gagasan.",
                  "Pesan": "Jadikan keberanian bicaramu sebagai senjata utama memimpin."
                },
                {
                  "Nama": "Edsel Adya Pradipta",
                  "NIM": "098",
                  "Asal": "Lampung Selatan, Natar",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Scroll Fesbuk",
                  "Umur": "20",
                  "Sosmed": "@edsel_0712",
                  "Kesan": "Perfeksionis dan cermat memantau kekurangan kecil.",
                  "Pesan": "Gunakan insting detailmu untuk mengawal kerapian tim."
                },
                {
                  "Nama": "Lucia Advencia Rachel Nainggolan",
                  "NIM": "124450085",
                  "Asal": "Bekasi",
                  "Alamat": "Belwis",
                  "Hobi": "Lari",
                  "Umur": "20",
                  "Sosmed": "@luciarachel_",
                  "Kesan": "Tenang, terukur, dan penuh ketenangan saat krisis.",
                  "Pesan": "Pertahankan ritme stabilmu untuk perjalanan jangka panjang."
                },
                {
                  "Nama": "Shafa Delaila Azzahra",
                  "NIM": "124450124",
                  "Asal": "Lampung Tengah",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Makan tempe mentah",
                  "Umur": "20",
                  "Sosmed": "@_shaazzh",
                  "Kesan": "Sangat terstruktur, elegan, dan penuh perhitungan formal.",
                  "Pesan": "Bawa terus gaya profesionalis bertaraf tinggi ini."
                },
                {
                  "Nama": "Zannuba Arifah Ilman",
                  "NIM": "Belum Tahu",
                  "Asal": "Belum Tahu",
                  "Alamat": "Belum Tahu",
                  "Hobi": "Belum Tahu",
                  "Umur": "Belum Tahu",
                  "Sosmed": "Belum Tahu",
                  "Kesan": "Kritis, berani mendobrak, dan penuh inisiatif baru.",
                  "Pesan": "Jangan pernah ragu mengguncang zona nyaman sekitar."
                }
              ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()