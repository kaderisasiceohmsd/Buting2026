import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import html

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
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "16px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
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
            "https://drive.google.com/thumbnail?id=19GLvW4o6gxq2EtgtoVsnaiDZaQ77T1XH&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ygwKJPLJLsgZIbc6rquwcB1l7w6pyxvR&sz=w1000",
            "https://drive.google.com/thumbnail?id=1zjLhTrcu9XGvnM83xb0FjElfRcmm24XN&sz=w1000",
            "https://drive.google.com/thumbnail?id=1QVPAgg4emwipiMSXg0Ue5HRLEb4qe4OF&sz=w1000",
            "https://drive.google.com/thumbnail?id=1pqq5TMy5fKn7hyQPTg1KQQ-gc3Yngm9h&sz=w1000"
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
            "https://drive.google.com/thumbnail?id=1pjDR3eM-p_cv7NDeUdPhLw15CtL80hqh&sz=w1000",
            "https://drive.google.com/thumbnail?id=10mzpyx5t_sSFj6GhjW5PT38EC5s1uiR_&sz=w1000",
            "https://drive.google.com/thumbnail?id=1NRtVdpqDV9F70Ge2Y6bp1MXrP4HkAERd&sz=w1000",
            "https://drive.google.com/thumbnail?id=1qVZTPEvENddV0q8DKQIj1E007e7At9pd&sz=w1000",
            "https://drive.google.com/thumbnail?id=1RYRJ3oi6GJ1kGdVHem5VGRo4D1Ab4_eK&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Yhv6o6VrXEgPT9HLHcI-SD-o4cBGphGV&sz=w1000",
            "https://drive.google.com/thumbnail?id=1sinRQY2RfsR7pwD6Bn_5r5BjeVtfgXrN&sz=w1000",
            "https://drive.google.com/thumbnail?id=1B9-WuFxwOKsWJD_ZK3bEryU1xNzWS-Of&sz=w1000",
            "https://drive.google.com/thumbnail?id=1jUJmiUHTPiWvgoHPTJywe4Ayx6er69r2&sz=w1000",
            "https://drive.google.com/thumbnail?id=1_VuCgnFsewIfgBym6EEtIVFO6HXLY7VR&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1By6kPYMeQs88equDmLXBLaOo7XxV27Js&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1_vDh-5lzZAI7ETRtUadgk3EZW2zr46nu&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Hx-6CrnOYNzfUT9EvAFQvPwj9_Yj5VYj&sz=w1000"
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
            "https://drive.google.com/thumbnail?id=1LzN_W1HPL0tBMX4JO-WKOYSKVnI2DKGZ&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1gLaQsJcn7ZupZSDTAN-3cTWq40KKHCrX&sz=w1000",
            "https://drive.google.com/thumbnail?id=1nw9LIYK1DFf9Ko4pucaipuCjCpUmsihu&sz=w1000",
            "https://drive.google.com/thumbnail?id=1BvM7lrfuZt_Okhc4PMjIXE0j6AYcv0ZH&sz=w1000",
            "https://drive.google.com/thumbnail?id=1RIQJNFLGeoHAQT4FwB7gEDwGX7TtG5GE&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=17vJ3Zr_5UnJwWL9Fm0XgkPboW4y3G3Lp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Qq-1BjayrYSJiyboktiVUjvJuz9cIQtb&sz=w1000",
            "https://drive.google.com/thumbnail?id=1_9JdV_pBHbX4dv06h7YPyRTVuVbQZEgy&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y19Sc1TFX_GkYHAT83AD5WtkRGbjAUGD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1KoiUibTej0sEVDEf8ph2Pcsp5Hdm-bAw&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=16TnEQuehRF5qKcKAf35q3EKYUpeG4ZKC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1qACYM7safm_ejCAX38JpR98TVl5Jwvf2&sz=w1000",
            "https://drive.google.com/thumbnail?id=18VzajSeH0LKfDgIiTao96Js941IZUiCL&sz=w1000",
            "https://drive.google.com/thumbnail?id=1qACYM7safm_ejCAX38JpR98TVl5Jwvf2&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1xCdF1ik8AV11JWc6Jro9w_cGx2M2MBju&sz=w1000",
            "https://drive.google.com/thumbnail?id=1nZk0RALaCEBhBbziBfv6a_RhRYqUdvWV&sz=w1000"
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
            "https://drive.google.com/thumbnail?id=1_pyggC8EbhKFjBDtuyNXpFO4NUqxZXho&sz=w1000",
            "https://drive.google.com/thumbnail?id=1_pyggC8EbhKFjBDtuyNXpFO4NUqxZXho&sz=w1000",
            "https://drive.google.com/thumbnail?id=1cZ953xaIl_umyrCbN4RcJ0Qm-1aOq7Pb&sz=w1000",
            "https://drive.google.com/thumbnail?id=1LkdvWuiCPn9n4qdSn8UNPiFt5I1o5U2E&sz=w1000",
            "https://drive.google.com/thumbnail?id=1BzpnzO5oh-8GqexmDpdhwTpNaOTAKH6T&sz=w1000",
            "https://drive.google.com/thumbnail?id=1xrUIidIiX4znTJpgpEOWYDuSxlXo22ya&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=14i_XFNTCYlvXwenm74c9GYgpxIWqgr1O&sz=w1000",
            "https://drive.google.com/thumbnail?id=1_ocyNYU7lD2NmnCAAf4UgnGkYxCFbFTI&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1SsDyRLtsJK11KRdj01VKR7voT9_Up7Xh&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1YcKBkh3dVDUVI8J2g_-7lJGZCQxGsnjF&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1qu95ChAyw6LCKhlpBHyDUQfYArxtAsc7&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000"
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

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                
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
                "Kesan": "Orangnya santai dan enak diajak ngobrol, apalagi soal jurnal dan riset.",
                "Pesan": "Tetap semangat belajarnya, semoga pencarian jurnal dan Pak Lucy-nya selalu membuahkan hasil."

            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Ramah dan menyenangkan, dan kelihatannya jago masak.",
                "Pesan": "Terus semangat dan jangan lupa bagi-bagi masakannya kalau ada kesempatan."    
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Asyik dan nyambung kalau diajak ngobrol, terutama soal film.",
                "Pesan": "Tetap jadi diri sendiri dan semoga selalu ada film Marvel baru yang seru ditonton." 
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Kalem dan bisa diandalkan, apalagi kalau urusan teknis.",
                "Pesan": "Terus semangat belajar dan semoga container-nya selalu jalan lancar tanpa error."
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Gigih dan pekerja keras, orangnya juga seru.",
                "Pesan": "Semangat terus dalam berusaha, tapi jangan lupa istirahat ya."
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Ramah dan gampang akrab, rekomendasi dramanya pasti banyak.",
                "Pesan": "Tetap semangat kuliahnya, dan jangan begadang kebanyakan gara-gara maraton drakor."
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Orangnya tenang dan menyenangkan.",
                "Pesan": "Semangat kuliahnya, semoga tidurnya selalu cukup dan nyenyak."
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Ceria dan punya semangat kerja yang tinggi.",
                "Pesan": "Tetap semangat dan jaga kesehatan, semoga usahanya lancar terus."
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "Energik dan sportif, seru diajak main bareng.",
                "Pesan": "Terus semangat, jaga kesehatan, dan semoga makin jago main basketnya."
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Sabar dan santai, enak diajak ngobrol.",
                "Pesan": "Semoga hasil pancingannya selalu melimpah dan kuliahnya lancar."
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Ceria dan bikin suasana jadi lebih hangat.",
                "Pesan": "Tetap jadi pribadi yang ceria dan semangat terus kuliahnya."
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Ramah dan seru diajak ngobrol, terutama soal film.",
                "Pesan": "Tetap semangat dan semoga selalu ada waktu buat nonton film favorit."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1t6ri6eO2Qgz6s4RgzopUDkhY0QnbnYyS&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1piQ2hptkuBp3IaV-dNC8dx6Y_vDUJwbV&sz=w1000",
            "https://drive.google.com/thumbnail?id=1cKwR58QcgZHPN1ETicYBFAXh1MRQhS2y&sz=w1000",
            "https://drive.google.com/thumbnail?id=15BUcwgKn802ExKm3Zh3hN_G8puItdksj&sz=w1000",
            "https://drive.google.com/thumbnail?id=1T68uk9VQRs9FY6DIHa9hpNeHoNQoPk5V&sz=w1000",
            "https://drive.google.com/thumbnail?id=1mOqu87TzRABgcns1exYnzn9CcE8Rcfsv&sz=w1000",
            "https://drive.google.com/thumbnail?id=1jTvsrVUwWuKkxaT1tJFK1GjA9VZUR5Pm&sz=w1000",
            "https://drive.google.com/thumbnail?id=14oOSXXTkmC6NVPJNbko8KBCWREbauvW2&sz=w1000",
            "https://drive.google.com/thumbnail?id=1P7a2jInBPnncmUcR37Que5ecLgwpy3Fg&sz=w1000",
            "https://drive.google.com/thumbnail?id=1tPFc0ByrAv2_oUPXk9I-9AbRqjdpbV63&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
            "https://drive.google.com/thumbnail?id=1SBpds2vbjdPCzagJVwZelYIc6FhAOtRN&sz=w1000",
            "https://drive.google.com/thumbnail?id=1IBruXt475oD_kto5NYQtuxsFBzSgtwqg&sz=w1000",
            "https://drive.google.com/thumbnail?id=1BA7XIaOqDyyheaWLkRfjZaNkMO0k-mVN&sz=w1000",
            "https://drive.google.com/thumbnail?id=1EUW1updmuqan7Hy8_j5jQJnFxA34tvX3&sz=w1000",
            "https://drive.google.com/thumbnail?id=1s68WnjlgS7FRfxNo84jeHihCJXjlaXa8&sz=w1000",
            "https://drive.google.com/thumbnail?id=1jTvsrVUwWuKkxaT1tJFK1GjA9VZUR5Pm&sz=w1000",
            "https://drive.google.com/thumbnail?id=1bFwuvhKLKyJO4Yq5KGvzndlJ6DhEyGS2&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000"

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
                "Kesan": "Ramah dan menyenangkan, enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Ceria dan gampang akrab dengan siapa saja.",
                "Pesan": "Semangat terus kuliahnya, semoga jalan-jalannya makin seru."
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Santai dan asyik diajak bergaul.",
                "Pesan": "Terus semangat dan jaga kesehatan."
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Santai dan tidak banyak drama.",
                "Pesan": "Tetap santai tapi jangan lupa produktif juga ya."
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Ceria dan penuh percaya diri.",
                "Pesan": "Tetap semangat dan terus berkarya."
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Santai dan menyenangkan.",
                "Pesan": "Semangat terus, semoga cepat dapat rumah impian."
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Ceria dan menyenangkan.",
                "Pesan": "Tetap semangat, tapi jangan kebanyakan yang manis ya."
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kalem dan enak diajak ngobrol soal film.",
                "Pesan": "Tetap semangat dan semoga filmnya selalu seru."
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Humoris dan enak diajak bercanda.",
                "Pesan": "Tetap jadi pribadi yang menyenangkan dan semangat terus."
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Seru dan punya hobi yang unik-unik.",
                "Pesan": "Tetap semangat, semoga pancingannya selalu dapat hasil."
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Teliti dan bisa diandalkan.",
                "Pesan": "Semangat terus, semoga semua urusan lancar."
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Ramah dan terbuka.",
                "Pesan": "Tetap semangat dan jangan ragu bertanya."
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Orangnya seru dan bikin suasana jadi hidup.",
                "Pesan": "Tetap semangat, dan jangan kebanyakan bikin ribut ya."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Tenang dan menyenangkan diajak ngobrol.",
                "Pesan": "Tetap semangat, semoga cerita favoritnya selalu seru."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Baik hati dan ramah.",
                "Pesan": "Tetap jadi pribadi yang baik dan semangat terus."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Tenang dan kalem.",
                "Pesan": "Semangat kuliahnya, semoga tidurnya selalu cukup."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Sabar dan telaten.",
                "Pesan": "Semangat terus, semoga cupangnya sehat-sehat."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Santai dan gampang akrab.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Kreatif dan punya cara berpikir yang unik.",
                "Pesan": "Semoga cepat ketemu hobi yang cocok, tetap semangat."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Santai dan humoris.",
                "Pesan": "Tetap semangat dan terus jadi pribadi yang menyenangkan."
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Ramah dan seru diajak ngobrol.",
                "Pesan": "Semangat terus, semoga selalu ada tontonan seru."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Ramah dan menyenangkan.",
                "Pesan": "Tetap semangat, semoga jalan-jalannya selalu lancar."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()
if menu == "Baleg":
    def baleg():
        gambar_urls = [
            
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
                "Kesan": "Orangnya kalem dan rajin, enak diajak ngobrol.",
                "Pesan": "Tetap semangat kuliahnya, semoga selalu dimudahkan dalam segala urusan."
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Asyik dan nyambung kalau bahas musik.",
                "Pesan": "Semangat terus kuliahnya, semoga playlist-nya selalu menemani hari yang baik."
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Ramah dan seru, punya selera tontonan yang unik.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus kuliahnya."
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "Santai dan seru, asyik diajak main bareng.",
                "Pesan": "Tetap semangat, dan semoga rank-nya naik terus tanpa lupa kuliah."
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "Ceria dan menyenangkan, koleksinya bikin penasaran.",
                "Pesan": "Semangat terus dan semoga koleksinya makin lengkap."
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Santai dan asyik, cocok diajak nongkrong sambil ngopi.",
                "Pesan": "Terus semangat dan jangan kebanyakan kopi biar tetap sehat."
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Supel dan gampang akrab dengan siapa saja.",
                "Pesan": "Tetap semangat dan jaga pertemanannya ya."
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Ramah dan seru, banyak bahan obrolan yang asyik.",
                "Pesan": "Tetap semangat kuliahnya dan jangan lupa istirahat."
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Ramah dan seru, enak diajak ngobrol.",
                "Pesan": "Tetap semangat, dan semoga suaranya makin merdu serta badannya selalu sehat."
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "Sabar dan telaten, orangnya menyenangkan.",
                "Pesan": "Tetap semangat dan semoga rajutannya makin bagus."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Santai dan disiplin, koleksinya bikin penasaran.",
                "Pesan": "Terus semangat, jaga kesehatan, dan semoga koleksi figurnya makin lengkap."
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Tenang dan hangat, enak diajak ngobrol.",
                "Pesan": "Terus semangat dan semoga bunganya selalu tumbuh subur."
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "Unik dan menyenangkan, selalu ada hal seru dari ceritanya.",
                "Pesan": "Tetap ceria dan semangat, semoga selalu lancar ke depannya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1vInl6JAQbi76RystzNl9Yg8cY0wK9bVx&sz=w1000",
            "https://drive.google.com/thumbnail?id=1fKnUnRxtpVrz_5GUkpk2M6A0OWNtlCFv&sz=w1000",
            "https://drive.google.com/thumbnail?id=1nvH_mi5cbLV0sYBQ-zQSyFjUf4bdKvLl&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Ni6cp3TuGKGwgQVVBJ9oZdOx2iFTyy5I&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Ni6cp3TuGKGwgQVVBJ9oZdOx2iFTyy5I&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ia-nW0NvPiKdHSq6FXvtf7dkJVzR-mEp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ia-nW0NvPiKdHSq6FXvtf7dkJVzR-mEp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1vInl6JAQbi76RystzNl9Yg8cY0wK9bVx&sz=w1000",
            "https://drive.google.com/thumbnail?id=1aAsPz0Tl-TUzFGHPS8Lvp1DjfesW5lzP&sz=w1000"
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
                "Kesan": "Ramah dan enak diajak ngobrol, tulisannya pasti menarik.",
                "Pesan": "Tetap semangat menulis dan jangan lupa istirahat."
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Santai dan humoris, gampang akrab.",
                "Pesan": "Tetap semangat dan jangan lupa fokus kuliah."
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Sportif dan energik, seru diajak main bareng.",
                "Pesan": "Terus semangat, jaga kesehatan, dan semoga makin jago badmintonnya."
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia___",
                "Kesan": "Ceria dan seru diajak ngobrol.",
                "Pesan": "Semangat terus, semoga pancingannya selalu dapat hasil."
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Santai dan enak diajak bergaul.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan."
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Santai dan gampang akrab dengan siapa saja.",
                "Pesan": "Tetap semangat dan semoga selalu ada tontonan seru."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Rajin dan teliti, orangnya juga menyenangkan.",
                "Pesan": "Tetap semangat dan semoga dokumentasinya selalu rapi dan lancar."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Unik dan seru, selalu ada cerita menarik.",
                "Pesan": "Terus semangat dan semoga ayamnya selalu patuh."
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kalem dan menyenangkan, selera musiknya pasti asyik.",
                "Pesan": "Semangat terus kuliahnya, semoga playlist-nya selalu menemani hari yang baik."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Tenang dan menyenangkan, banyak bahan obrolan yang seru.",
                "Pesan": "Terus semangat belajarnya dan tetap jadi diri sendiri."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1vInl6JAQbi76RystzNl9Yg8cY0wK9bVx&sz=w1000",
            "https://drive.google.com/thumbnail?id=1fKnUnRxtpVrz_5GUkpk2M6A0OWNtlCFv&sz=w1000",
            "https://drive.google.com/thumbnail?id=1nvH_mi5cbLV0sYBQ-zQSyFjUf4bdKvLl&sz=w1000",
            "https://drive.google.com/thumbnail?id=1R0rEt4x_BgZ-V-rVuo7XubKQh8Y0giAC&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Ni6cp3TuGKGwgQVVBJ9oZdOx2iFTyy5I&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Ni6cp3TuGKGwgQVVBJ9oZdOx2iFTyy5I&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ia-nW0NvPiKdHSq6FXvtf7dkJVzR-mEp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ia-nW0NvPiKdHSq6FXvtf7dkJVzR-mEp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1vInl6JAQbi76RystzNl9Yg8cY0wK9bVx&sz=w1000",
            "https://drive.google.com/thumbnail?id=1aAsPz0Tl-TUzFGHPS8Lvp1DjfesW5lzP&sz=w1000"
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
                "Kesan": "Ramah dan mudah akrab dengan siapa saja.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan ya."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Tenang dan enak diajak bicara.",
                "Pesan": "Semoga selalu dimudahkan dalam setiap urusan."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "-",
                "Sosmed": "@nobelnizam",
                "Kesan": "Kalem dan sopan, nyaman diajak ngobrol.",
                "Pesan": "Terus semangat dan tetap konsisten dalam belajar."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "Santai dan menyenangkan.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Supel dan gampang bergaul.",
                "Pesan": "Semangat terus kuliahnya, semoga lancar ke depannya."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Orangnya santai dan asyik diajak ngobrol.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat yang cukup."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Aktif dan punya semangat yang tinggi.",
                "Pesan": "Terus berkembang dan semoga selalu sukses."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Dewasa dan bisa diandalkan.",
                "Pesan": "Tetap semangat dan jaga kesehatan."
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450065",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Nomandenl",
                "Hobi": "Mancing emosi",
                "Sosmed": "@putrimannaa",
                "Kesan": "Ceria dan seru diajak bercanda.",
                "Pesan": "Semangat terus belajarnya dan tetap jadi pribadi yang positif."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Ramah dan hangat ke semua orang.",
                "Pesan": "Tetap semangat dan semoga semua rencananya berjalan baik."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Orangnya humoris dan bikin suasana cair.",
                "Pesan": "Terus semangat dan tetap rendah hati."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Disiplin dan menjaga pola hidup sehat.",
                "Pesan": "Pertahankan semangatnya dan tetap konsisten."
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Pekerja keras dan bertanggung jawab.",
                "Pesan": "Semangat terus dan jangan lupa luangkan waktu untuk diri sendiri."
            },
            {
                "Nama": "Jeremi Marolop Partogi Situmorang",
                "NIM": "124450111",
                "Umur": "16",
                "Asal": "Berlin",
                "Alamat": "Samping kos Rafli",
                "Hobi": "Mengembala anak ayam",
                "Sosmed": "@jemarrro",
                "Kesan": "Santai dan mudah bergaul.",
                "Pesan": "Tetap semangat dan terus belajar hal baru."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Ramah dan menyenangkan diajak berteman.",
                "Pesan": "Semoga kuliahnya lancar dan selalu diberi kesehatan."
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "20",
                "Asal": "Sibolga",
                "Alamat": "Samping kos Haikal",
                "Hobi": "Nonton",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Kalem dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan terus jadi pribadi yang baik."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "Tenang dan apa adanya.",
                "Pesan": "Semangat terus dan tetap jaga kesehatan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()
