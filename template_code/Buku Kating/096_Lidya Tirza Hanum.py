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

# ============================================================
# KESEKJENAN
# ============================================================
if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/thumbnail?id=1_0SudVzwuYzvGZKpqFz2do2ubFN_lo5e&sz=w1000",
        "https://drive.google.com/thumbnail?id=197hVCDGTVk2vDMHd3XNrYmAwcf_SUMCm&sz=w1000",
        "https://drive.google.com/thumbnail?id=1reBkWFC84h4EzeN3M6yyw1YdwUCRgZBT&sz=w1000",
        "https://drive.google.com/thumbnail?id=1UKwbcALYQ_dsWjFGGKUWeclnrjqUmjBe&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Yjn--mYbGEHh6P7EYiKZqSiliSD9YRgq&sz=w1000",
        "https://drive.google.com/thumbnail?id=1a3FY4g5G6cDIA22Y1n_FNlnyU63qi_vU&sz=w1000", 
    ]

    data_list = [
        {
            "Nama": "Ginda Fajar Riadi Marpaung",
            "NIM": "123450103",
            "Umur": "17",
            "Asal": "Batam",
            "Alamat": "Sekretariat HMSD",
            "Hobi": "Push imo",
            "Sosmed": "@jars_mrp",
            "Kesan": "Abang sangat keren sekali dan baik hati",
            "Pesan": "etap semangat abang dan keren selalu",
        },
        {
            "Nama": "Muhammad Aqil Ramadhan",
            "NIM": "123450066",
            "Umur": "22",
            "Asal": "Riau",
            "Alamat": "Kotabaru",
            "Hobi": "Dzikir",
            "Sosmed": "@Muhammadaqil1111",
            "Kesan": "abangnya sangat menyenangkan.",
            "Pesan": "Semoga makin jaya selalu.",
        },
        {
            "Nama": "Efi Defiyati",
            "NIM": "123450005",
            "Umur": "21",
            "Asal": "Lampung Timur",
            "Alamat": "Airan",
            "Hobi": "Membaca",
            "Sosmed": "@eeffiidefi",
            "Kesan": "Kakaknya itu baik banget.",
            "Pesan": "Semoga selalu bahagia, Kak!",
        },
        {
            "Nama": "Qois Olifio",
            "NIM": "123450067",
            "Umur": "22",
            "Asal": "Batam",
            "Alamat": "Kotabaru",
            "Hobi": "Mainin surat",
            "Sosmed": "@qoisolifio_",
            "Kesan": "Abangnya sedikit pendiam dan ramah.",
            "Pesan": "tetap keren yaa, Bang.",
        },
        {
            "Nama": "Hafsa Fazilah Arradhi",
            "NIM": "123450079",
            "Umur": "21",
            "Asal": "Bandar Lampung",
            "Alamat": "Bandar Lampung",
            "Hobi": "Bertemu luluk",
            "Sosmed": "@hafsafazilahh",
            "Kesan": "Kakaknya baik dan asik sekali",
            "Pesan": "semoga sukses selalu, kakak.!.",
        },
        {
            "Nama": "Luthfia Laila Ramadhani",
            "NIM": "123450004",
            "Umur": "20",
            "Asal": "Bengkulu",
            "Alamat": "Airan",
            "Hobi": "Keliling Balam",
            "Sosmed": "@luthhifiarmdhni",
            "Kesan": "Kakaknya seru banget",
            "Pesan": "Semoga semua proses kuliah lancar!.",
        },
    ]

    display_images_with_data(gambar_urls, data_list)


# ============================================================
# DEPARTEMEN INTERNAL
# ============================================================
if menu == "Departemen Internal":
    gambar_urls = [
        "https://drive.google.com/thumbnail?id=1TM3PUiicM_8gDH9YlG1VBXItzGZFBEMF&sz=w1000",
        "https://drive.google.com/thumbnail?id=1BL5V99GCHG0fK5zGStaW2gLs05qpNBpO&sz=w1000",
        "https://drive.google.com/thumbnail?id=1d5no5DBNkqYSbY6Km7M1BPvDcrvNlEu7&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Y4u3O_FiLC44ExOHuuTLOYBkjWxJ2Vmc&sz=w1000",
        "https://drive.google.com/thumbnail?id=1zwd4Zw1w7c1glyliaOIlJ_kBeqpXD2DO&sz=w1000",
        "https://drive.google.com/thumbnail?id=1mYzVKDOuxQ6-k7ADsqAZ6rSq8P6Gv4r4&sz=w1000",
        "https://drive.google.com/thumbnail?id=1JtqPmNu9OLBwPt6R1_SYDNkgSl39jK0u&sz=w1000",
        "https://drive.google.com/thumbnail?id=1grw-Fn1WIxh5ceJ_gvS-I7UbbipIC_NQ&sz=w1000",
        "https://drive.google.com/thumbnail?id=1YBOGbDRxybQ_Vbq71sxbJMD1xOdVsYM9&sz=w1000",
        "https://drive.google.com/thumbnail?id=116fzmlYkWdJiDHgdX_PPBfjwtspIDh_4&sz=w1000",
        "https://drive.google.com/thumbnail?id=16dNKbNyT7rkUL0q4IbtQj1RZSB2X2L2E&sz=w1000",
        "https://drive.google.com/thumbnail?id=14pLKcyzh-QJJ3aHox5URNUUxComm3QL1&sz=w1000",
        "https://drive.google.com/thumbnail?id=17GU3l7ll-W1tXw5gd5TXMy3oXZz-AFkO&sz=w1000",
        "https://drive.google.com/thumbnail?id=10pqqzRF0Mifi06bMOQX0hKzgf8Xn2hDG&sz=w1000",
        "https://drive.google.com/thumbnail?id=1fvE0WfgK8SAOmn8_roKgfXYOrJl6RukA&sz=w1000",
        "https://drive.google.com/thumbnail?id=1kaCiw9BrNBEPuSuLPEAX19nFoS_V-S75&sz=w1000",
    ]

    data_list = [
        {
            "Nama": "Haikal Fransisko Simbolon",
            "NIM": "123450106",
            "Umur": "21",
            "Asal": "Jambi",
            "Alamat": "Jatimulyo",
            "Hobi": "Ngeroasting orang",
            "Sosmed": "@haikalsbln_",
            "Kesan": "Humornya sederhana tapi bikin akrab.",
            "Pesan": "Jaga suasana cair tanpa berlebihan.",
        },
        {
            "Nama": "Kharisma Mustika Sari",
            "NIM": "123450034",
            "Umur": "21",
            "Asal": "Way Kanan",
            "Alamat": "Untung Senopati",
            "Hobi": "Menolong orang",
            "Sosmed": "@rismaa.mustika_",
            "Kesan": "Cara bicaranya lembut tapi tegas.",
            "Pesan": "Jangan ragu terus membimbing kami dengan sabar.",
        },
        {
            "Nama": "Hanna Gresia Sinaga",
            "NIM": "123450038",
            "Umur": "21",
            "Asal": "Kisaran City",
            "Alamat": "Sukarame",
            "Hobi": "Menyapa satpam ITERA",
            "Sosmed": "@hanna_g_sinaga",
            "Kesan": "Perhatiannya ke adik tingkat sangat besar.",
            "Pesan": "Semoga kebaikan Kakak selalu kembali.",
        },
        {
            "Nama": "Ahmad Farhan Ghani",
            "NIM": "123450121",
            "Umur": "21",
            "Asal": "Kemiling",
            "Alamat": "Kemiling",
            "Hobi": "Supporteran",
            "Sosmed": "@farhanghani",
            "Kesan": "Tegas saat mengambil keputusan.",
            "Pesan": "Tetap adil dan pertimbangkan banyak hal.",
        },
        {
            "Nama": "Aisyah Khairun Nisa",
            "NIM": "124450096",
            "Umur": "18",
            "Asal": "Indragiri",
            "Alamat": "Samping Makam Perwira 2",
            "Hobi": "Nyicipin Makanan",
            "Sosmed": "@aisyahkhair._",
            "Kesan": "kakak lemah lembut dan baik hati",
            "Pesan": "Tetap jadi kakak yang mengayomi yaa.",
        },
        {
            "Nama": "Cerine Sihotang",
            "NIM": "124450049",
            "Umur": "20",
            "Asal": "Medan",
            "Alamat": "Belwis",
            "Hobi": "Suka Ngoding pakai R",
            "Sosmed": "@cerine_ipynb",
            "Kesan": "Kakak ceria banget",
            "Pesan": "kakak semoga dilancarka selalu dalam perkuliahan",
        },
        {
            "Nama": "Jaya Saputra Tamba",
            "NIM": "124450094",
            "Umur": "18",
            "Asal": "Medan",
            "Alamat": "Pemda",
            "Hobi": "Mencari Nafkah",
            "Sosmed": "@jay.saputra.mb",
            "Kesan": "kakak tinggi dan seru",
            "Pesan": "Semoga kakak tetap semangat",
        },
        {
            "Nama": "Najla Nursyifa",
            "NIM": "124450051",
            "Umur": "20",
            "Asal": "Sumatra Barat",
            "Alamat": "Belwis",
            "Hobi": "Nonton ASMR",
            "Sosmed": "@njlanursyifa",
            "Kesan": "kakak punya positif vibe dan seru.",
            "Pesan": "Jaga energi positif kakak selalu.",
        },
        {
            "Nama": "Rozak Ramdani",
            "NIM": "124450100",
            "Umur": "19",
            "Asal": "Kalianda, Lampung Selatan",
            "Alamat": "Korpri Raya",
            "Hobi": "Berantemin Kucing",
            "Sosmed": "@rozakrabbani__",
            "Kesan": "Seru dan sedikit canggung diawal",
            "Pesan": "semoga kakak sehat selalu",
        },
        {
            "Nama": "Teresa Christiani Purba",
            "NIM": "124450046",
            "Umur": "19",
            "Asal": "Riau",
            "Alamat": "Belwis",
            "Hobi": "Masak",
            "Sosmed": "@kristiani8872",
            "Kesan": "kakak sangat ceria dan bahagia",
            "Pesan": "semoga kakak tetap diberikan kebahagiann selalu",
        },
        {
            "Nama": "Muhammad Hanif Dzaky Arifin",
            "NIM": "123450064",
            "Umur": "21",
            "Asal": "Padang",
            "Alamat": "Way Kandis",
            "Hobi": "Nonton F1 & MotoGP",
            "Sosmed": "@hnfdzky_",
            "Kesan": "abang itu sedikit pendiam",
            "Pesan": "semoga abang semangat selalu",
        },
        {
            "Nama": "Audina Fitria",
            "NIM": "124450038",
            "Umur": "20",
            "Asal": "Sumatra Barat",
            "Alamat": "Sukarame",
            "Hobi": "Masak",
            "Sosmed": "@audinaf_03",
            "Kesan": "kakak sedikit pendiam, tapi senyumnya manis",
            "Pesan": "semogaa kakak dierikan kelancaran selalu",
        },
        {
            "Nama": "Cika Adelia Br Marbun",
            "NIM": "124450107",
            "Umur": "20",
            "Asal": "Bagan Batu, Riau",
            "Alamat": "Belwis",
            "Hobi": "Dengerin Musik",
            "Sosmed": "@cikamrbn",
            "Kesan": "kakak semangat dan senyumnya ceria",
            "Pesan": "senyum kakak akan membuat kami bahagia",
        },
        {
            "Nama": "Gustin H Tampubolon",
            "NIM": "124450068",
            "Umur": "21",
            "Asal": "Sumatera Utara",
            "Alamat": "Airan",
            "Hobi": "Nonton",
            "Sosmed": "@gustinhaleluya",
            "Kesan": "kakak cantik dan ramah sekali",
            "Pesan": "Terus jadi kakak yang baik bagi kami.",
        },
        {
            "Nama": "Muhammad Harvinsyah",
            "NIM": "124450128",
            "Umur": "20",
            "Asal": "Sumatera Selatan",
            "Alamat": "Belwis",
            "Hobi": "Ngadu Ikan Cupang",
            "Sosmed": "@muhvinz_",
            "Kesan": "Ramah ke semua orang dan sedikit pendiam.",
            "Pesan": "semoga hari kakak selalu seru.",
        },
        {
            "Nama": "Rafa Sabina Fahimah",
            "NIM": "124450036",
            "Umur": "20",
            "Asal": "Natar",
            "Alamat": "Natar",
            "Hobi": "Nonton Drakor",
            "Sosmed": "@snasaa._",
            "Kesan": "kakak baik dan ramah",
            "Pesan": "Pertahankan sikap ramah itu.",
        },
    ]

    display_images_with_data(gambar_urls, data_list)


# ============================================================
# DEPARTEMEN MINBAK
# ============================================================
if menu == "Departemen Minbak":
    gambar_urls = [
        "https://drive.google.com/thumbnail?id=1GM-VtL2Qdyezmp1SRS4LgKKQ0TtoTJQ8&sz=w1000",
        "https://drive.google.com/thumbnail?id=1nV1gtHO66OrLDPV98dD4EpqzO9XEw7OR&sz=w1000",
        "https://drive.google.com/thumbnail?id=1ot3basievMXK8Xm1FbqeAwaWq_He856S&sz=w1000",
        "https://drive.google.com/thumbnail?id=1_puG0XTESXC3F6OrOeOSvXygCZixd83I&sz=w1000",
        "https://drive.google.com/thumbnail?id=1z4rFEtCWmSU16NmIUuLY2uWYsiaSCqnu&sz=w1000",
        "https://drive.google.com/thumbnail?id=1xH0vzEFk9ijMcE1xPzs59auvhKZ6MxuN&sz=w1000",
        "https://drive.google.com/thumbnail?id=1m9Tt9zWhCsommkrwjct1A-tFpItBWvh2&sz=w1000",
        "https://drive.google.com/thumbnail?id=1XD3U8k76_Wu7qrClMpQRPsA1xohFPBYC&sz=w1000",
        "https://drive.google.com/thumbnail?id=192xUyeqfPbGpwJA9gNh6xut7O-vsckOs&sz=w1000",
        "https://drive.google.com/thumbnail?id=1ed6QZiXRuAErF-Y3vGcyLbdd-iSexLlc&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Y3D_i-42UDv1JyU2Es212LxgkE_bxJKB&sz=w1000",
        "https://drive.google.com/thumbnail?id=10rX7vBNWihW93IVzSgMs2Vt4TzvnVahe&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Xfr50HwZd1hwOSuiPdHbwGPgvKVgOKFm&sz=w1000",
        "https://drive.google.com/thumbnail?id=172vFp5MLnEL_QosEFRX45t3q47Sm1K8K&sz=w1000",
        "https://drive.google.com/thumbnail?id=1wqTaj7uH6Vqq1uqnX-YpO1GHdMH_Vbk2&sz=w1000",
    ]

    data_list = [
        {
            "Nama": "Kevin Antonio Junior",
            "NIM": "123450109",
            "Umur": "21",
            "Asal": "Bandar Lampung",
            "Alamat": "Panjang, Bandar Lampung",
            "Hobi": "Balap",
            "Sosmed": "@kevinaj__",
            "Kesan": "kelihatan tegas dan berwibawa, jadi sedikit segan diawal",
            "Pesan": "semoga kakak bisa lebih santai dan tersenyum.",
        },
        {
            "Nama": "Gusti Putu Ferazka Dhiyamika",
            "NIM": "123450046",
            "Umur": "21",
            "Asal": "Lampung Utara",
            "Alamat": "Way Halim",
            "Hobi": "Baca",
            "Sosmed": "@ferazkaa",
            "Kesan": "kukira kakak pendiam, ternyta seru.",
            "Pesan": "semoga kita bisa lebih dekat kakak.",
        },
        {
            "Nama": "Ari Aristo Muthahari Parisi",
            "NIM": "123450088",
            "Umur": "21",
            "Asal": "Lampung Timur",
            "Alamat": "Gang Sakum, Belwis",
            "Hobi": "Nonton F1",
            "Sosmed": "@ali_parisi3",
            "Kesan": "kelihatan santai tapi juga punya sisi tegas",
            "Pesan": "Tetap jadi pribadi yang ramah, Kak.",
        },
        {
            "Nama": "Ayu Andriani Parlina Wati",
            "NIM": "124450058",
            "Umur": "20",
            "Asal": "Lampung Barat",
            "Alamat": "Airan",
            "Hobi": "Belajar",
            "Sosmed": "@aayuandrianni_",
            "Kesan": "orangnya baik dan perhatian",
            "Pesan": "Semangat belajarnya,Kak.",
        },
        {
            "Nama": "Dafa Elpriza",
            "NIM": "124450131",
            "Umur": "21",
            "Asal": "Bekasi",
            "Alamat": "Way Kandis",
            "Hobi": "Nemenin Bryan live TikTok",
            "Sosmed": "@dafaelpriza_",
            "Kesan": "orangnya santai dan baik.",
            "Pesan": "Jangan berubah, tetap baik hati Kak.",
        },
        {
            "Nama": "Juwita Sari",
            "NIM": "124450066",
            "Umur": "19",
            "Asal": "Lampung Barat",
            "Alamat": "Pemda",
            "Hobi": "Lihat bulan",
            "Sosmed": "@ju.juwitaaa_",
            "Kesan": "Sikapnya lembut dan senyumnya manis.",
            "Pesan": "Tetap semangat, Kak.",
        },
        {
            "Nama": "Muhammad Afdal Lutfi",
            "NIM": "124450047",
            "Umur": "19",
            "Asal": "Lampung Tengah",
            "Alamat": "Jl Pulau Damar",
            "Hobi": "Taptap layar kalo Bryan live",
            "Sosmed": "@afdall.03",
            "Kesan": "Ceria dan ramah",
            "Pesan": "Terus maju meskipun banyak rintangan, Kak.",
        },
        {
            "Nama": "Salsabila Nazwa Putri",
            "NIM": "124450002",
            "Umur": "20",
            "Asal": "Metro",
            "Alamat": "Korpri",
            "Hobi": "Nongkrong di Kopken",
            "Sosmed": "@slbnzw_",
            "Kesan": "Mudah akrab dan menyenangkan",
            "Pesan": "Tetap jadi kakak yang terbuka ke adik tingkat, ya, Kak.",
        },
        {
            "Nama": "Muhammad Ridwan",
            "NIM": "123450091",
            "Umur": "21",
            "Asal": "Lampung Tengah",
            "Alamat": "Belwis",
            "Hobi": "Nganterin Datasena ke gedung F",
            "Sosmed": "@mridwaan_22",
            "Kesan": "Bertanggung jawab dan baik hati.",
            "Pesan": "Jangan lelah tetap semangat, Kak.",
        },
        {
            "Nama": "Andra Ilham Bintang",
            "NIM": "124450060",
            "Umur": "18",
            "Asal": "Sumatera Selatan",
            "Alamat": "Kota Baru",
            "Hobi": "Ngitungin kelopak bunga di kebun",
            "Sosmed": "@andra.lhm",
            "Kesan": "lucu dan ceria",
            "Pesan": "Tetap semangat, Kak.",
        },
        {
            "Nama": "Bryan Paskah Telaumbanua",
            "NIM": "124450003",
            "Umur": "22",
            "Asal": "Nias",
            "Alamat": "Belwis",
            "Hobi": "Live TikTok",
            "Sosmed": "@bryantel_",
            "Kesan": "orangnya santai dan tenang",
            "Pesan": "Tetap jadi pribadi yang menenangkan, Kak.",
        },
        {
            "Nama": "Ghiyats Thabularasa Meardhy",
            "NIM": "124450067",
            "Umur": "17",
            "Asal": "Bekasi",
            "Alamat": "Korpri",
            "Hobi": "Ngegift live Bryan",
            "Sosmed": "@meardhy_ghiyats",
            "Kesan": "baik hati dan seru",
            "Pesan": "Semoga dilancarkan perkulianannya",
        },
        {
            "Nama": "Indah Julia Mawar Pratiwi",
            "NIM": "124450055",
            "Umur": "Belum Tahu",
            "Asal": "Pringsewu",
            "Alamat": "Airan",
            "Hobi": "Bengong",
            "Sosmed": "@indahjuliaa",
            "Kesan": "Pembawaannya adem dan asik diajak bicara",
            "Pesan": "Tetap jadi diri sendiri, Kak.",
        },
        {
            "Nama": "Jacinda Kesya Alvara",
            "NIM": "124450023",
            "Umur": "18",
            "Asal": "Kalimantan Barat",
            "Alamat": "Korpri",
            "Hobi": "Nyapu depan gacoan",
            "Sosmed": "@cacalvra",
            "Kesan": "baik, ceria dan unik.",
            "Pesan": "Terus semangat, Kak.",
        },
        {
            "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
            "NIM": "124450089",
            "Umur": "20",
            "Asal": "Padang",
            "Alamat": "Kota Baru",
            "Hobi": "Bangun pagi",
            "Sosmed": "@muhammdrafka_",
            "Kesan": "ramah, baik hati dan sedikit canggung diawal",
            "Pesan": "semoga kakak bahagia selalu, Kak.",
        },
    ]

    display_images_with_data(gambar_urls, data_list)


# ============================================================
# DEPARTEMEN MIKFES
# ============================================================
if menu == "Departemen MIKFES":
    gambar_urls = [
        "https://drive.google.com/thumbnail?id=16P86_3b1BGi795QjCOYe7Pxx-IXf4NWG&sz=w1000",
        "https://drive.google.com/thumbnail?id=1ApVfZHU1uKwIeLg4ESE1tT6rwLsdVD_S&sz=w1000",
        "https://drive.google.com/thumbnail?id=1LQ260VO1lEHSDT4L1ovzhueIUDGM1ota&sz=w1000",
        "https://drive.google.com/thumbnail?id=1HSCttv3HmuJksHcnRhIVrnqPEbORyhs7&sz=w1000",
        "https://drive.google.com/thumbnail?id=13PhRuKFECXCiFdsmkjqVsq5vdUFK1FAM&sz=w1000",
        "https://drive.google.com/thumbnail?id=1AGZYk0N9S2CX5ePXOuWSeDL79BKKULu0&sz=w1000",
        "https://drive.google.com/thumbnail?id=10uEeF6GAlRLMOOg6BKoR4Blgw8W_u2mx&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Ul8mECvym0lehudDwmr1C9BElXnAWvB_&sz=w1000",
        "https://drive.google.com/thumbnail?id=1ptKTOQCEu95YXsTirrHdKaPYyaOVEKX5&sz=w1000",
        "https://drive.google.com/thumbnail?id=1-5WKONIO-nxtMzvp5t31a-0OEr-0TFCh&sz=w1000",
        "https://drive.google.com/thumbnail?id=16Q6aca9jbwYJUQPB2RSycec8hQu56ujn&sz=w1000",
        "https://drive.google.com/thumbnail?id=111rMcaXkulz5vel0B6O433A4T9Tyo6yX&sz=w1000",
        "https://drive.google.com/thumbnail?id=1b5V7IWpfjuhqtDSv5QWmZQCNGL89Ia1p&sz=w1000",
        "https://drive.google.com/thumbnail?id=1CjS7vRZNpAGXn3HT89B640JJDe24zcVt&sz=w1000",
        "https://drive.google.com/thumbnail?id=1Ok5rAv2UOM3dTT7XX8yDJaaNSP4e7E6C&sz=w1000",
        "https://drive.google.com/thumbnail?id=18tEnxO0FDy7_Wi10uxkpNbj8dVme0KVP&sz=w1000",
        "https://drive.google.com/thumbnail?id=1XKVIXETcA7ozVAtmeHPVQuoDnOHGL-tf&sz=w1000",
        "https://drive.google.com/thumbnail?id=19yNvpHJTOaeDrnHlQehmbBmn24pRjWhC&sz=w1000",
        "https://drive.google.com/thumbnail?id=1bw-zu70NRKD3nYBenyHubGadGhcV0E3K&sz=w1000",
        "https://drive.google.com/thumbnail?id=1_T7iDKOjbyrJg8ulVcsbf_eH5yPScMhP&sz=w1000",
        "https://drive.google.com/thumbnail?id=1bV28UPLDDkRSIU2HqsABK6_hlsG4Ckkb&sz=w1000",
        "https://drive.google.com/thumbnail?id=1-2cGiKD08V4gj4AUODl7Cs1mkumIg9Zw&sz=w1000",
    ]

    data_list = [
        {
            "Nama": "Fabio Banyu Cyto",
            "NIM": "12340104",
            "Umur": "21",
            "Asal": "Bandar Lampung",
            "Alamat": "Kedaton",
            "Hobi": "Tidur",
            "Sosmed": "@biyokcb",
            "Kesan": "Pembawaan abangnya santai dan pengertian.",
            "Pesan": "Jangan berubah dan tetap jadi abang yang baik",
        },
        {
            "Nama": "Tanty Widiyastuti",
            "NIM": "123450094",
            "Umur": "21",
            "Asal": "Lampung",
            "Alamat": "Airan Raya",
            "Hobi": "Membaca",
            "Sosmed": "@tvnty_",
            "Kesan": "ceria, lucu dan menyenangkan.",
            "Pesan": "semoga keceriaan kakak terjaga selalu",
        },
        {
            "Nama": "Fadil Prasetyo Alfaritzi",
            "NIM": "123450048",
            "Umur": "21",
            "Asal": "Bandar Lampungku",
            "Alamat": "Bandar Lampung",
            "Hobi": "Gitar",
            "Sosmed": "@fadilalfarizzii",
            "Kesan": "abang menyenangkan dan baik hati",
            "Pesan": "semoga hari kakak menyenangkan selalu",
        },
        {
            "Nama": "Manuel Frederika",
            "NIM": "124450039",
            "Umur": "20",
            "Asal": "Batam",
            "Alamat": "Way Kandis",
            "Hobi": "Tenis meja",
            "Sosmed": "@manuelfdk_",
            "Kesan": "baik, ramah dan tegas.",
            "Pesan": "Tetap diberikan kelancaran selalu, Kak.",
        },
        {
            "Nama": "Ni Made Okta Viola Darma Putri",
            "NIM": "124450005",
            "Umur": "12",
            "Asal": "Bali",
            "Alamat": "Nusa Penida",
            "Hobi": "Menghayal",
            "Sosmed": "Violaadrtr_",
            "Kesan": "Pembawaannya menenangkan dan senyumnya manis",
            "Pesan": "Semoga kakak bahagia selalu.",
        },
        {
            "Nama": "Risa Romadona",
            "NIM": "124450127",
            "Umur": "20",
            "Asal": "Natar",
            "Alamat": "Natar",
            "Hobi": "Rolling skate",
            "Sosmed": "risarmdna",
            "Kesan": "Aktif dan menyenngkan.",
            "Pesan": "Terus berani melangkah, Kak.",
        },
        {
            "Nama": "Vannisa Ramadhani",
            "NIM": "124450078",
            "Umur": "19",
            "Asal": "Kepulauan Riau",
            "Alamat": "Teluk Betung",
            "Hobi": "Nonton KHW",
            "Sosmed": "@vunnycaa",
            "Kesan": "nyaman diajak bicara dan selalu terlihat ceria.",
            "Pesan": "Tetap jadi pribadi yang ceria",
        },
        {
            "Nama": "Yulia Cristine Malau",
            "NIM": "Belum Tahu",
            "Umur": "Belum Tahu",
            "Asal": "Belum Tahu",
            "Alamat": "Belum Tahu",
            "Hobi": "Belum Tahu",
            "Sosmed": "Belum Tahu",
            "Kesan": "Baik hati dan menghargai orang lain.",
            "Pesan": "Semoga sukses selalu, Kak.",
        },
        {
            "Nama": "Akeyla Fairuz Shafi",
            "NIM": "1234501",
            "Umur": "21",
            "Asal": "Bandar Lampung",
            "Alamat": "Bandar Lampung",
            "Hobi": "Dengerin Musik",
            "Sosmed": "@keyashafi",
            "Kesan": "Pendengar yang baik dan ramah",
            "Pesan": "Tetap jadi diri sendiri, Kak.",
        },
        {
            "Nama": "Elsa Sitorus",
            "NIM": "124450088",
            "Umur": "21",
            "Asal": "Sumatera Utara",
            "Alamat": "Pemda",
            "Hobi": "Rebahan",
            "Sosmed": "_els.a",
            "Kesan": "Murah senyum dan nyaman diajak bicara",
            "Pesan": "Tetap jadi kakak yang hangat, ya, Kak.",
        },
        {
            "Nama": "Fadya Izzatul Aini",
            "NIM": "124450062",
            "Umur": "20",
            "Asal": "Pringsewu",
            "Alamat": "Airan",
            "Hobi": "Mancing",
            "Sosmed": "fadyaizzatul_",
            "Kesan": "Sabar dan menyenangkan.",
            "Pesan": "Jangan lelah membimbing kami",
        },
        {
            "Nama": "Lovianora Saragih",
            "NIM": "124450105",
            "Umur": "19",
            "Asal": "Sumatera Utara",
            "Alamat": "Way Huwi",
            "Hobi": "Dengerin Musik",
            "Sosmed": "_loviaa",
            "Kesan": "Ceria dan punya positif vibe",
            "Pesan": "Semoga selalu dimudahkan dalam kuliahnya, Kak.",
        },
        {
            "Nama": "M. Alsi Syahrulloh",
            "NIM": "124450092",
            "Umur": "20",
            "Asal": "Kalianda",
            "Alamat": "Kotabaru",
            "Hobi": "Main Game, Tidur",
            "Sosmed": "@aluccy_",
            "Kesan": "Humoris dan baik",
            "Pesan": "tetap fokus kuliah dan sukses selalu, Kak.",
        },
        {
            "Nama": "Sherena Florencia",
            "NIM": "124450027",
            "Umur": "19",
            "Asal": "Bengkulu Selatan",
            "Alamat": "Belwis",
            "Hobi": "Make up",
            "Sosmed": "sher_renna",
            "Kesan": "selalu tampil percaya diri.",
            "Pesan": "Tetap jadi panutan bagi adik tingkat, Kak.",
        },
        {
            "Nama": "Razin Hafid Hamdi",
            "NIM": "123450096",
            "Umur": "21",
            "Asal": "Padang",
            "Alamat": "Belwis",
            "Hobi": "Futsal",
            "Sosmed": "@razyn.hfd",
            "Kesan": "Sportif dan seru",
            "Pesan": "Terus ajak kami aktif bersama, Kak.",
        },
        {
            "Nama": "Faiza Try Anjani",
            "NIM": "124450075",
            "Umur": "19",
            "Asal": "Padang",
            "Alamat": "Belwis",
            "Hobi": "Membaca Novel",
            "Sosmed": "FAIZAANJANII",
            "Kesan": "Tutur katanya sopan dan pengertian.",
            "Pesan": "Tetap jadi kakak yang pengertian, Kak.",
        },
        {
            "Nama": "Gathfan Nadif Ali",
            "NIM": "124450001",
            "Umur": "20",
            "Asal": "Bandar Lampung",
            "Alamat": "Rajabasa",
            "Hobi": "Main game",
            "Sosmed": "@gathfannadif",
            "Kesan": "Santai tapi tetap ada batasan.",
            "Pesan": "Terus jaga keseimbangan itu, Kak.",
        },
        {
            "Nama": "Hafidz Wahdiansyah",
            "NIM": "124450064",
            "Umur": "20",
            "Asal": "Metro",
            "Alamat": "Metro Kibang, Lampung Timur",
            "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
            "Sosmed": "@apiszzaja_",
            "Kesan": "Baik dan menyenangkan",
            "Pesan": "tolong ajari kami, Kak.",
        },
        {
            "Nama": "Kaleb Filbert Istel",
            "NIM": "124450053",
            "Umur": "20",
            "Asal": "Bandar Lampung",
            "Alamat": "Campang Raya",
            "Hobi": "Ngegym, baca novel",
            "Sosmed": "@kelelep_comberan",
            "Kesan": "Asik, tenang dan menyenangkan",
            "Pesan": "semoga bahagia selalu, Kak.",
        },
        {
            "Nama": "Melva Shaprina Febrianti",
            "NIM": "124450087",
            "Umur": "19",
            "Asal": "Sumsel",
            "Alamat": "Sukarame",
            "Hobi": "Scroll",
            "Sosmed": "@melva_fbrt",
            "Kesan": "Ceria dan ramah",
            "Pesan": "Tetap jadi sseorang yang ramah",
        },
        {
            "Nama": "Muhammad Syafiqul Falakh",
            "NIM": "Belum Tahu",
            "Umur": "Belum Tahu",
            "Asal": "Belum Tahu",
            "Alamat": "Belum Tahu",
            "Hobi": "Belum Tahu",
            "Sosmed": "@syaafiqui",
            "Kesan": "Pendiam tapi punya sisi tegas.",
            "Pesan": "tetap terus melangkah meskipun ada rintangan, Kak.",
        },
        {
            "Nama": "Rifky Henry Ferdianto",
            "NIM": "124450115",
            "Umur": "28",
            "Asal": "Kobum",
            "Alamat": "Rajabasa",
            "Hobi": "Lari dari kenyataan",
            "Sosmed": "henryferdianto",
            "Kesan": "Humornya asik dan baik hati.",
            "Pesan": "Semoga dilancarkan selalu kuliahnya, Kak.",
        },
    ]

    display_images_with_data(gambar_urls, data_list)


# ============================================================
# DEPARTEMEN MEDKRAF
# ============================================================
if menu == "Departemen Medkraf":
    # CATATAN: baru ada 10 foto untuk 18 data orang (lihat data_list).
    gambar_urls = [
        "https://drive.google.com/thumbnail?id=1x1hLuPtCKIwTvgQG_fkkO7vf2x2cLqpT&sz=w1000",
        "https://drive.google.com/thumbnail?id=10RWPKhkBKiirokfLoNxM92O-czKhzHFQ&sz=w1000",
        "https://drive.google.com/thumbnail?id=1r5iJQsAQncMfrew5YxcJYQpy_ntWFUU7&sz=w1000",
        "https://drive.google.com/thumbnail?id=1YwZG0lmahBYmtQ9HGBUd6X0VG9sezB6X&sz=w1000",
        "https://drive.google.com/thumbnail?id=1V2t2fIwbflskLizpws3qx1kHXUhXGM9x&sz=w1000",
        "https://drive.google.com/thumbnail?id=1WAJzA67gnduohGkcXS9fIH3pZT28xkvy&sz=w1000",
        "https://drive.google.com/thumbnail?id=1OszSPqnR1q74WCKt9tQ7P5ueE1DVA8Jq&sz=w1000",
        "https://drive.google.com/thumbnail?id=1cPe0ha0hV94i7ZeZxG0C5_nRJYn3lVPi&sz=w1000",
        "https://drive.google.com/thumbnail?id=1rsliFVHQSh1kHnYU-xcAujz2wdujEL3Y&sz=w1000",
        "https://drive.google.com/thumbnail?id=1I76gzPz2Ga1V7NOOnZ8EIgHim-Kc8jZO&sz=w1000",
        "https://drive.google.com/thumbnail?id=1FTiPunTf8FD4miHXtpVSLawsLecBM6Fl&sz=w1000",
        "https://drive.google.com/thumbnail?id=1JJwIUwPWE119qVk9eouzd7VtEvAzAzfV&sz=w1000",
        "https://drive.google.com/thumbnail?id=1UpQeEjFQb8mmjAQ_T42kGckL9_vq3icW&sz=w1000",
        "https://drive.google.com/thumbnail?id=1pID23OW9ehUIfQy4_wGv98EFJ_-Gqwc3&sz=w1000",
        "https://drive.google.com/thumbnail?id=1mZvHJirrl8nu4RHC1FWbFWo1aWRMqkay&sz=w1000",
        "https://drive.google.com/thumbnail?id=1QuklkKtVeoHUv2UGX_dHXfVZtjas5EOd&sz=w1000",
        "https://drive.google.com/thumbnail?id=1k2kqP-1QKMk_2_CkXC9L9-in4-be1P5N&sz=w1000",
        "https://drive.google.com/thumbnail?id=1ahsbMqF9Ey9NbSCMkS9Cc8imvS5nMSuL&sz=w1000",
    ]

    data_list = [
        {
            "Nama": "Nayla Salsabila Fathianisa",
            "NIM": "123450082",
            "Umur": "20",
            "Asal": "Payakumbuh, Sumatera Barat",
            "Alamat": "Belum Tahu",
            "Hobi": "Rebahan",
            "Sosmed": "@naylasalsabilaa._",
            "Kesan": "Ramah dan enak diajak ngobrol.",
            "Pesan": "Tetap jadi kakak yang baik hati, ya, Kak.",
        },
        {
            "Nama": "Donna Maya Puspita",
            "NIM": "123450028",
            "Umur": "21",
            "Asal": "Bekasi dan Lampung",
            "Alamat": "Belum Tahu",
            "Hobi": "Mendengarkan musik",
            "Sosmed": "@donnamaya.p",
            "Kesan": "Pendengar yang baik dan ceria.",
            "Pesan": "Terus jadi kakak yang ceria untuk kami",
        },
        {
            "Nama": "Labo John Nuel Napitupulu",
            "NIM": "37",
            "Umur": "20",
            "Asal": "Medan, Jakut, Palembang",
            "Alamat": "Belum Tahu",
            "Hobi": "Berburu burung",
            "Sosmed": "@noerruuu",
            "Kesan": "ramah, tinggi dan menyenangkan",
            "Pesan": "semoga kakak di berikan kebahagiaan",
        },
        {
            "Nama": "Anash Tasya Ausyaqila",
            "NIM": "124450050",
            "Umur": "20",
            "Asal": "Bandar Lampung",
            "Alamat": "Belum Tahu",
            "Hobi": "Ngoding",
            "Sosmed": "@anshtsyaaql",
            "Kesan": "Baik hati dan nyamaan diajak bicara",
            "Pesan": "Semoga kakak diberikan kemudahaan dalam hidup",
        },
        {
            "Nama": "Felisya Nabila Putri Nugroho",
            "NIM": "124450104",
            "Umur": "18",
            "Asal": "Bekasi",
            "Alamat": "Belum Tahu",
            "Hobi": "Ngejahilin mama",
            "Sosmed": "@felisyanbl__",
            "Kesan": "menyenangkan dan bikin suasana hidup.",
            "Pesan": "Tetap jadi pribadi yang ceria",
        },
        {
            "Nama": "Muhammad Razan Maulana Pratama",
            "NIM": "124450031",
            "Umur": "18",
            "Asal": "Sibolga",
            "Alamat": "Belum Tahu",
            "Hobi": "Jahilin Felisya",
            "Sosmed": "@muh_razan_",
            "Kesan": "baik dan seru.",
            "Pesan": "semoga kakak diberikan kesehatan selalu.",
        },
        {
            "Nama": "Sania Dwi Ayu Lestari",
            "NIM": "123450086",
            "Umur": "21",
            "Asal": "Bandung",
            "Alamat": "Belum Tahu",
            "Hobi": "Bimbingan TA",
            "Sosmed": "@saniayyllstr",
            "Kesan": "seru dan baik hati",
            "Pesan": "Semoga dilancar selalu di perkuliahannya",
        },
        {
            "Nama": "Allisha",
            "NIM": "124450019",
            "Umur": "6",
            "Asal": "Rahim ibu",
            "Alamat": "Belum Tahu",
            "Hobi": "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah",
            "Sosmed": "@aallishaa.a",
            "Kesan": "Gampang akrab,enerjik dan ceria terus",
            "Pesan": "Tetap jadi teman yang asyik bagi kita semua",
        },
        {
            "Nama": "Alya Ramadhanti",
            "NIM": "124450091",
            "Umur": "19",
            "Asal": "Kota banyak sawit",
            "Alamat": "Belum Tahu",
            "Hobi": "Apa aja",
            "Sosmed": "@alya.rmdhnti",
            "Kesan": "baik,cantik dan seru.",
            "Pesan": "tetap semangat menjalani hari",
        },
        {
            "Nama": "Bunga Clarisa Sefa",
            "NIM": "124450097",
            "Umur": "20",
            "Asal": "Lampung Selatan",
            "Alamat": "Belum Tahu",
            "Hobi": "Belajar",
            "Sosmed": "@bungaclrssf",
            "Kesan": "baik,ramah dan menenangkan",
            "Pesan": "semoga kakak diberikan kelancaran segala urusan.",
        },
        {
            "Nama": "Difanya Husakina",
            "NIM": "124450043",
            "Umur": "20",
            "Asal": "Deket Kebun Teh",
            "Alamat": "Belum Tahu",
            "Hobi": "Alhamdulillah Dzikir dan sholawatan",
            "Sosmed": "@difanyhsa",
            "Kesan": "asik dan nyaman untuk bicara",
            "Pesan": "Tetap menjadi teladan bagi kami.",
        },
        {
            "Nama": "Nazlah Auliya",
            "NIM": "124450054",
            "Umur": "20",
            "Asal": "Bandar Lampung",
            "Alamat": "Belum Tahu",
            "Hobi": "Ballet",
            "Sosmed": "@nzlhauly_",
            "Kesan": "ramah dan penuh percaya diri.",
            "Pesan": "Terus kejar impianmu dengan semangat, Kak.",
        },
        {
            "Nama": "Raihana Adelia Putri",
            "NIM": "123450041",
            "Umur": "20",
            "Asal": "Lampung Tengah",
            "Alamat": "Airan Raya 1",
            "Hobi": "Menulis, membaca",
            "Sosmed": "@r.hanaap",
            "Kesan": "Tenang dan pemikiran terbuka",
            "Pesan": "tetap jadi panutan bagi kami",
        },
        {
            "Nama": "Daffa Kharisma Adzana",
            "NIM": "Belum Tahu",
            "Umur": "Belum Tahu",
            "Asal": "Belum Tahu",
            "Alamat": "Belum Tahu",
            "Hobi": "Belum Tahu",
            "Sosmed": "Belum Tahu",
            "Kesan": "Kalem, tapi ramah diajak bicara",
            "Pesan": "semoga semakin akrab dengan kelompok kami",
        },
        {
            "Nama": "Edsel Adya Pradipta",
            "NIM": "098",
            "Umur": "20",
            "Asal": "Lampung Selatan, Natar",
            "Alamat": "Belum Tahu",
            "Hobi": "Scroll Fesbuk",
            "Sosmed": "@edsel_0712",
            "Kesan": "Santai dan seru.",
            "Pesan": "Tetap semangat kuliahnya.",
        },
        {
            "Nama": "Lucia Advencia Rachel Nainggolan",
            "NIM": "124450085",
            "Umur": "20",
            "Asal": "Bekasi",
            "Alamat": "Belwis",
            "Hobi": "Lari",
            "Sosmed": "@luciarachel_",
            "Kesan": "Energik dan baik hati",
            "Pesan": "semoga kakak harinya menyenangkan selalu",
        },
        {
            "Nama": "Shafa Delaila Azzahra",
            "NIM": "124450124",
            "Umur": "20",
            "Asal": "Lampung Tengah",
            "Alamat": "Belum Tahu",
            "Hobi": "Makan tempe mentah",
            "Sosmed": "@_shaazzh",
            "Kesan": "baik hati dan ramah",
            "Pesan": "Tetap jadi kakak yang ramah",
        },
        {
            "Nama": "Zannuba Arifah Ilman",
            "NIM": "Belum Tahu",
            "Umur": "Belum Tahu",
            "Asal": "Belum Tahu",
            "Alamat": "Belum Tahu",
            "Hobi": "Belum Tahu",
            "Sosmed": "Belum Tahu",
            "Kesan": "ramah dan menyenangkan",
            "Pesan": "Semoga selalu dimudahkan dalam menggapai impian kakak",
        },
    ]

    display_images_with_data(gambar_urls, data_list)