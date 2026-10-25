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
                "https://drive.google.com/thumbnail?id=1uC7DYBlidf-QvOHOZD7b9G1DSiv4OQ0N&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZitP7qCfH-_gq1E9EEfGBQD0_up3JeaE&sz=w1000",
                "https://drive.google.com/thumbnail?id=16yv_00XMpXJR9KDd1TR8HWdFxk8Gm__x&sz=w1000",
                "https://drive.google.com/thumbnail?id=13V7s8zndk1x2foxNN7QLDALEmeAUFCxP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aZ9v4JYO4-yr4TtjqK1G0FOXaxH8c-I5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pUxLxhpeApCaQAjJgY3CCdRhWS1lMO6b&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450103",
                "Asal" : "Bakinang",
                "Alamat" : "Sekretariat HMSD",
                "Hobi": "Push rank",
                "Umur" : "22",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "Abangnya kelihatan sangat humble dan terbuka sama adik tingkat.",
                "Pesan" : "Semoga makin sukses dan lancar terus kuliahnya, Kak."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Abangnya asik diajak ngobrol dan ga bikin merasa sungkan.",
                "Pesan" : "Tetap semangat dalam menjalani rutinitas perkuliahan, Kak."
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "kakaknya ramah dan penuh semangat.",
                "Pesan" : "Sukses terus Kak buat project dan kegiatan yang lagi dipegang!"
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Perhatian dan sabar banget melayani pertanyaan kami.",
                "Pesan" : "Semoga revisian dan urusan akademiknya dipermudah terus, Kak."
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "kating yang bersahabat dan positif vibes.",
                "Pesan" : "Makasih ya Kak udah selalu sabar dan mau direpotin sama kami."
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Pembawaan Kakaknya seru dan bikin kita ga grogi pas diajak ngobrol.",
                "Pesan" : "Jangan lupa istirahat di tengah padatnya jadwal kuliah ya, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1V22xQH4mUlYxtqH3eBT7XSnhhv47YRbG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1syaHgNq-qu7wtUROFH6M4VVs608r65hM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1APl-qgnAxdOAuNaIuM-y54J5jVOeDXzd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hM-10lRPps0GC5dIEor6uyaIhnaqk27M&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rMCvpYBFWI1rTyk_NOPH1FngNsV3TRZq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Il34O22EEVgN8qQ_HcsmZRgeWSsUuIv4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1y7Um_D14sXMbpPCQZ0lSBcrhC3MVGuv8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zQWZMa5Thtgz-fNevOHEabu6Q4pSKW7W&sz=w1000",
                "https://drive.google.com/thumbnail?id=16tx7iQ6G590l_sebE4cd2YSzTLlyfXSp&sz=w1000",
                "https://drive.google.com/thumbnail?id=1w85t4SJ-lYCCfyyXvlx-3oTMJvwvOgUm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Pl5-nXWOqbsNQu6lgo0nomIGvnCYvbYH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1RqgUtREYNCirRI7Pi8Vs6g3LYJ692ui3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1M7ucOqj1pnyLp8lVJeP8I5ZIxYv_HeHl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1IhAfYAVo-gTTStPIE1-ZC_TJ6pdyv658&sz=w1000",
                "https://drive.google.com/thumbnail?id=1RvMX9KZpve0sc6vr7FTjXU5q7DWKHtYi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EpnhcyDkmXvfecuk2p66QkI7yU7VXLEc&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "123450106",
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Way Halim",
                "Hobi": "Ngeledek Orang",
                "Sosmed": "@haikalsbln",
                "Kesan": "Abangnya kelihatan bijak tapi tetep fleksibel dan ga kaku.",
                "Pesan": "Keren banget liat konsistensi dan pencapaian abang selama ini."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Suka Nolong Orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Beliau sosok yang adem, tutur katanya santun, dan menenangkan.",
                "Pesan": "Semoga tugas-tugas semester ini dilancarkan tanpa kendala, Kak."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Sumatera Utara, kisaran city",
                "Alamat": "Sukarame",
                "Hobi": "Ngabarin Orang Tua",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "kakaknya ceria dan baik banget.",
                "Pesan": "Makasih Kak udah selalu ngerangkul dan bimbing saya dari awal."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "Abangnya peka dan selalu siap nuntun pas maba kebingungan.",
                "Pesan": "Sukses selalu Kak, baik di dalam maupun di luar kampus."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Kakaknya sangat asik dan bikin kami merasa dihargai.",
                "Pesan": "Semangat terus Kak, jangan kasih kendor sampai kelulusan!"
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Kakaknya ramah banget tapi agak pendiam.",
                "Pesan": "Semoga makin banyak peluang bagus yang terbuka buat Kakak ke depan."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Abangnya peka dan selalu siap dan ga bikin canggung.",
                "Pesan": "Makasih udah selalu merangkul kami bang."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Katingnya selalu senyum dan kelihatan tulus pas bantu.",
                "Pesan": "Keren terus Kak organisasi dan karyanya, inspiratif banget!"
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Kesan pertama bareng abangnya sangat positif dan berwibawa.",
                "Pesan": "Semoga selalu dikelilingi lingkungan dan teman-teman yang supportive, bang."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "kakaknya baikk banget dan pinter jugaa",
                "Pesan": "Tetap jadi ceria dan semangat terus ya kak."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "abangnya pendiem tapi aslinya baik.",
                "Pesan": "makasih banyak abang udah kasih nasihat yang baik"
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Cara pembawaannya menyenangkan dan ga bikin panik.",
                "Pesan": "Makasih udah bikin suasana jurusan/prodi dapet banget hangatnya, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Kesan pertama sama beliau ramah banget dan murah senyum.",
                "Pesan": "Sehat-sehat terus Kak, biar tetap strong ngelewatin semester ini."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "ramah dan selalu ngasih energi positif.",
                "Pesan": "Semoga makin cemerlang terus prestasinya ya, Kak."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya kelihatan berpengalaman tapi tetep mau dengerin kami.",
                "Pesan": "Semoga dimudahkan segala langkah menuju cita-citanya setelah lulus nanti, bang."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "kakaknya naik pendiem tapi kalo diajak ngobrol nyambung.",
                "Pesan": "Tetap seru dan asik kaya biasa ya Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1qSvD1Bv0J01uyhKloWEFXQjP88q4TzXy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lNTN0BziN1CAUa8v_votXqQ3E1FZVtc3&sz=w1000",
                "https://drive.google.com/thumbnail?id=10JleBkPaZm_aG9IPAtNdIFP_RgR46cy4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QXYGj0YKLyrf0twtb-HvuZxetX_aK2QB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1q5eOMF8ZksAaU64YoXz6WmZfJ--30Hwe&sz=w1000",
                "https://drive.google.com/thumbnail?id=16C7UVcOvDAEIYjyIVMREL1Tf5Od8mUO8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Fm1vxyyJgUBIZYT2u3eh2wh-PQJ5CNtl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1co_pMxnIvWg-moEG1K4VPi2zjTCznKsI&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KPWJuepuSVG2_HdCmrBDiBJMriAyjFTo&sz=w1000",
                "https://drive.google.com/thumbnail?id=12G5fPUs1fGz8bDBiklCkEAOtNcrsNIQA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZxbcOggpbugOt7Z_Qa6hMl4gMnBokKKb&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wECmOuPW9lJ7sM5B1_vM9gds4UAV_pjo&sz=w1000",
                "https://drive.google.com/thumbnail?id=15WPVtaLs3v7J9zXKhfzKBc_5fvYMRNON&sz=w1000",
                "https://drive.google.com/thumbnail?id=10TyOxnlXvwydcBq1FoMHdKF-pdjMRwA4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PFspoZNfBL_oDEw4G7RfkmAwpX4AB53n&sz=w1000",
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
                "Kesan" : "Abangnya pinter banget mecah keheningan pas perkenalan.",
                "Pesan" : "Makasih udah nemenin dan ngarahin kami tanpa bikin canggung."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Sosok kating yang humble dan ga segan buat bagi tips perkuliahan.",
                "Pesan" : "Semoga segala urusan praktikum dan laporan Kakak mulus terus."
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi",
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Ceria dan bikin suasana sekitar jadi makin seru.",
                "Pesan" : "Semangat terus Kak, tinggal dikit lagi menuju gelar sarjana!"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "Rajin dan selalu bersungguh-sungguh dalam bekerja.",
                "Pesan" : "Semoga kebaikan dan bantuan Kakak ke kami dibalas hal-hal baik juga."
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Abangnya penuh perhatian dan selalu tanggap sama pertanyaan kami.",
                "Pesan" : "Tetap jadi panutan yang menyenangkan buat kami semua ya, Kak."
            },
            {
                "Nama": "Juwita Sari",
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Kakaknya pembawaannya dewasa tapi gaya bicaranya santai.",
                "Pesan" : "Semoga makin sukses di setiap project baru yang Kakak jalanin."
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Kakaknya menghargai banget kehadiran maba dan bikin merasa diterima.",
                "Pesan" : "Titip semangat ya Kak, kalau capek istirahat sebentar lalu jalan lagi!"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Pembawaan beliau tegas tapi tetep hangat dan bersahabat.",
                "Pesan" : "Semoga karier impian Kakak sesudah lulus nanti langsung tercapai."
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Katingnya bikin perkenalan ga kerasa tegang sama sekali.",
                "Pesan" : "Luar biasa banget impact yang Kakak bawa di divisi/organisasi kita."
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Abangnya punya pembawaan yang supel dan mudah membaur.",
                "Pesan" : "Selalu suka sama gaya kepemimpinan Kakak yang merangkul semua orang."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Cara bicaranya santun tapi tetep berasa akrab.",
                "Pesan" : "Semoga karier impian Kakak sesudah lulus nanti langsung tercapai."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Kesan pertama sama Abangnya penuh energi positif dan bikin semangat.",
                "Pesan" : "Senang bisa banyak diskusi dan tukar pikiran sama Kakak."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "20",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Kakaknya komunikatif banget dan ga bikin rasa canggung bertahan lama.",
                "Pesan" : "Semoga selalu dikasih kelancaran dan rezeki yang melimpah, Kak."
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Sosok kating yang penyabar dan sangat mengayomi adik tingkatnya.",
                "Pesan" : "Semoga harinya selalu menyenangkan dan minim masalah, Kak!"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Abangnya pinter nempatin diri jadi kating yang fleksibel.",
                "Pesan" : "Tetap pertahankan sifat suportifnya ke adik-adik tingkat ya, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1SZH6wNrTMvD79oaAczNW1iB0Lz42PxN0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rV7SkTtnN0974vJvmdpEaBwrf6TN_f5S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1GD1Sf2oh7zzy94SziIcG0W4r-tGYhBfj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wyDuseObaidGkI3pMZZlgc9F7Qbsqkjo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rhb-J3FbA93_9f4hCsrx84n8p5bPUBB8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1o4nhJtYU4siQLsVChD3OChs80Kh6XXJ_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-nsaBLd1sfnsaxFGVLvVdJKI91comLLN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jh1jv7uNrJgWGwmjnwfXF-aATwe6zEXQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=108j8baPbisZcJhlE7yCuryFWgKTMViyw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1JW3ka4ioHSS-oBPgUkqq-tuDa-MU2Hxu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1m4Yxvw06Ptg85Px0QfWtk1PzIy2OFXkL&sz=w1000",
                "https://drive.google.com/thumbnail?id=114bvui7EIKBLuAfl5C-w8w_4U7EhsBqb&sz=w1000",
                "https://drive.google.com/thumbnail?id=18ZKsEIo93MumvRoWIGitOrbdE71TjuiW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1V-YAaz6qT4_v2tzh87aNg83QjfegYNWG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SIQgD4rD3febS_01V9kwqKE_knDhz3Pg&sz=w1000",
                "https://drive.google.com/thumbnail?id=10or97Tt3ItoBA8bMyhglaZLitHd2yhgI&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YMUd8S3lFe5Fiz9Whg8c8mMQt1Q5r-37&sz=w1000",
                "https://drive.google.com/thumbnail?id=1fMM4OSyejIuuH2sFm5sC_OmQvZ7Shcqu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WQLgcWSNzAU7OTv1yHOYqJoOpdXZiGQd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ILfB5DbSf2Lcj-TLcHFs28SJ52lcNm48&sz=w1000",
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
                "Kesan" : "Sosok kating yang sangat ramah, tenang, dan mengayomi.",
                "Pesan" : "Semoga harinya selalu menyenangkan dan minim masalah, bang!"
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Kating yang sangat humble dan terbuka sama maba.",
                "Pesan" : "Makasih Kak udah selalu senyum dan menginspirasii."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "abangnya keren dan banyak prestasinyaa.",
                "Pesan" : "Semoga abang selalu dapat banyak doa baik dan selalu mendapat keberkahan."
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Pembawaan Abangnya santai tapi tetap terasa berwibawa.",
                "Pesan" : "Semoga ilmu yang udah dialirkan ke kami jadi berkah buat Abang juga."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Pembawaan Kakaknya rapi dan sangat asik.",
                "Pesan" : "Semoga akademiknya selalu lancar ya kak."
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "kakaknyaaa baikk.",
                "Pesan" : "Doa terbaik dari saya untuk kesuksesan Kakak ke depannya!"
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "kakak nya menghargai kami dan ga bikin canggung.",
                "Pesan" : "Semangat ngerjain tugas-tugasnya ya Kak, lancar sampai wisuda!"
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "124450119",
                "Asal" : "Jambi",
                "Alamat" : "Sabah Balau",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@krnylee",
                "Kesan" : "Sopan dan menghargai orang lain.",
                "Pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM": "1234501",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur": "21",
                "Sosmed": "@keyashafi",
                "Kesan": "Abangnya ganteng, keren, dan santai.",
                "Pesan": "Semoga perkuliahan nya lancar terus dan sukses selalu ya, Bang!"
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM": "124450088",
                "Asal": "Sumatera Utara",
                "Alamat": "Pemda",
                "Hobi": "Rebahan",
                "Umur": "21",
                "Sosmed": "@_els.a",
                "Kesan": "Kakaknya manis, murah senyum, dan pembawaannya sangat hangat.",
                "Pesan": "Tetap jadi kating yang bersahabat dan sukses selalu akademiknya, Kak!"
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM": "124450062",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobi": "Mancing",
                "Umur": "20",
                "Sosmed": "fadyaizzatul_",
                "Kesan": "Kakaknya cantik, sabar, telaten, dan jawaban hobinya unik.",
                "Pesan": "Sukses terus perkuliahannya Kak, semoga selalu diberi kemudahan!"
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM": "124450105",
                "Asal": "Sumatera Utara",
                "Alamat": "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur": "19",
                "Sosmed": "_loviaa",
                "Kesan": "Kakaknya manis, kalem, dan pembawaannya sangat menenangkan.",
                "Pesan": "Semoga semua urusan studi dan perkuliahannya dimudahkan ya, Kak!"
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM": "124450092",
                "Asal": "Kalianda",
                "Alamat": "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur": "20",
                "Sosmed": "@aluccy_",
                "Kesan": "Abangnya ganteng, santai, humoris, dan seru diajak ngobrol.",
                "Pesan": "Tetap jadi abang tingkat yang asik dan sukses terus kuliahnya ya, Bang!"
            },
            {
                "Nama": "Sherena Florencia",
                "NIM": "124450027",
                "Asal": "Bengkulu Selatan",
                "Alamat": "Belwis",
                "Hobi": "Make up",
                "Umur": "19",
                "Sosmed": "@sher_renna",
                "Kesan": "Kakaknya cantik, rapi, stylish, dan tampil percaya diri banget.",
                "Pesan": "Semoga makin sukses perkuliahannya dan selalu memancarkan aura positif, Kak!"
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM": "123450096",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobi": "Futsal",
                "Umur": "21",
                "Sosmed": "@razyn.hfd",
                "Kesan": "Abangnya keren, baik, ganteng, dan humorisss.",
                "Pesan": "Sukses terus buat bakat futsalnya Bang, dan lancar akademiknya!"
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM": "124450075",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobi": "Membaca Novel",
                "Umur": "19",
                "Sosmed": "@Faizaanjanii",
                "Kesan": "Kakaknya anggun, pinter, ramah, dan tutur katanya santun banget.",
                "Pesan": "Semangat terus kuliahnya Kak, semoga selalu diberi kelancaran!"
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM": "124450001",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Main game",
                "Umur": "20",
                "Sosmed": "@gathfannadif",
                "Kesan": "Abangnya keren, santai, humble, dan sangat bertanggung jawab.",
                "Pesan": "Semoga perkuliahan dan urusannya selalu dilancarkan ya, Bang!"
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM": "124450064",
                "Asal": "Metro",
                "Alamat": "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur": "20",
                "Sosmed": "@apiszzaja_",
                "Kesan": "Abangnya pinter, keren, cekatan, dan kelihatan jago banget urusan IT.",
                "Pesan": "Semoga kodingan dan perkuliahannya makin sukses tanpa error ya, Bang!"
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM": "124450053",
                "Asal": "Bandar Lampung",
                "Alamat": "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur": "20",
                "Sosmed": "@kelelep_comberan",
                "Kesan": "Abangnya ganteng, keren, badannya bagus, dan berwawasan luas.",
                "Pesan": "Konsisten terus gym-nya Bang, dan semoga sukses selalu di perkuliahan!"
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM": "124450087",
                "Asal": "Sumsel",
                "Alamat": "Sukarame",
                "Hobi": "Scroll",
                "Umur": "19",
                "Sosmed": "@melva_fbrt",
                "Kesan": "Kakaknya cantik, imut, ceria, dan gampang banget membaur.",
                "Pesan": "Tetap jadi sosok yang hangat ya Kak, sukses terus jalani kuliahnya!"
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM": "124450099",
                "Asal": "Lampung Utara",
                "Alamat": "Asrama TB 3",
                "Hobi": "Membaca",
                "Umur": "20",
                "Sosmed": "@syafiqui",
                "Kesan": "Abangnya pinter, rapi, kalem, dan kelihatan sangat bisa diandalkan.",
                "Pesan": "Tetap semangat kuliahnya Bang, semoga ilmunya makin bermanfaat!"
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM": "124450115",
                "Asal": "Kobum",
                "Alamat": "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur": "28",
                "Sosmed": "@henryferdianto",
                "Kesan": "Abangnya keren, dewasa, santai, dan jawaban hobinya unik.",
                "Pesan": "Semoga dipermudah selalu semua langkah dan perjalanan kuliahnya ya, Bang!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=12JHdmISq2dQghh5sih5gt9smiFtJxjK5&sz=w1000",
                "https://drive.google.com/thumbnail?id=16zmG9_NYyequtvcEERy_HSj_0Zl14bIl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tZNKT6ubizlo-lkS1YmvVJxwbfIhQRz0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Pz9o4JUUA16BrFvJvM3oTdTuEEIgK9qZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1GyVkfApP7ReIM7VXpJlOpEOEUtCj42d6&sz=w1000",
                "https://drive.google.com/thumbnail?id=10apRX8kzgwWAfmE8bk9mjXzhrw8_HAjr&sz=w1000",
                "https://drive.google.com/thumbnail?id=16h8xWmtllHCKuRDxyu09MUI1-xRlJISo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dn33_jc8AutxOTYYr46SDuJDpK55l-4_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1z-M32rUSuRNVlxdQtA269oYJsN314jgh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qwTW3lLtYLtpgw7f47bpIzA_SqpSyXvy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xE3RFYhqOB9i89CP24_2-03o99N-IUL4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1_vm7ZEYI3o_nOyTYBHvt_FbP4V2n15A-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oIn70UmWfHD3kbGTnHq7NMCOtoCfr9C8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1q1K93i2JZUuF6EyhN8A3c2jsXbuPLh49&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KBTZLMpcbi8FQesswoiF-iYZBAAXYc4L&sz=w1000",
                "https://drive.google.com/thumbnail?id=1id0QLDTtDT2p19JKCBeFn3lS4AYJJI-4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
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
                "Kesan": "Kakaknya cantik, ramah, dan pembawaannya sangat bersahabat.",
                "Pesan": "Semoga perkuliahan nya selalu lancar dan bahagia terus ya, Kak!"
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM": "123450028",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur": "21",
                "Sosmed": "@donnamaya.p",
                "Kesan": "Kakaknya manis, senyumnya hangat, dan baik banget ke adik tingkat.",
                "Pesan": "Tetap jadi kating yang bersahabat ya Kak, sukses selalu buat akademiknya!"
            },
            {
                "Nama": "Labo John Nuel Napitupulu",
                "NIM": "123450037",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Motoran",
                "Umur": "20",
                "Sosmed": "@noerruuu",
                "Kesan": "Abangnya keren, ganteng, dan pembawaannya santai banget.",
                "Pesan": "Hati-hati pas motoran ya Bang, semoga lancar terus urusan kuliahnya!"
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM": "124450050",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobi": "Nonton",
                "Umur": "20",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya cantik, manis, pinter, dan kelihatan sangat tekun.",
                "Pesan": "Semoga semua target perkuliahan nya tercapai ya Kak, semangat selalu!"
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM": "124450104",
                "Asal": "Lampung Timur",
                "Alamat": "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur": "19",
                "Sosmed": "@felisyanbl__",
                "Kesan": "Kakaknya cantik, ceria, dan pembawaannya bikin suasana jadi hangat.",
                "Pesan": "Tetap jadi kating yang seru dan asik ya Kak, sukses terus kuliahnya!"
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM": "124450031",
                "Asal": "Jawa Barat",
                "Alamat": "Korpri",
                "Hobi": "Foto Orang",
                "Umur": "21",
                "Sosmed": "@muh_razan_",
                "Kesan": "Abangnya ganteng, santai, dan kelihatan berbakat banget.",
                "Pesan": "Sukses terus buat hobinya dan lancar selalu akademiknya ya, Bang!"
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM": "123450086",
                "Asal": "Karawang",
                "Alamat": "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur": "21",
                "Sosmed": "@saniayyllstr",
                "Kesan": "Kakaknya anggun, ramah, dan sangat menyenangkan.",
                "Pesan": "Semoga TA dan perkuliahan nya dilancarkan terus ya, Kak!"
            },
            {
                "Nama": "Allisha",
                "NIM": "124450019",
                "Asal": "Kayangan",
                "Alamat": "Heaven",
                "Hobi": "Mancing",
                "Umur": "16",
                "Sosmed": "@aallishaa.a",
                "Kesan": "Kakaknya imut, manis, supel, dan gampang diajak baur.",
                "Pesan": "Tetap jadi kating yang menyenangkan dan sukses selalu akademiknya, Kak!"
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM": "124450091",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobi": "Jalan-jalan",
                "Umur": "19",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Kakaknya cantik, humble, dan sangat bersahaja.",
                "Pesan": "Semoga jalan-jalannya selalu seru dan lancar terus kuliahnya ya, Kak!"
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM": "124450097",
                "Asal": "Lampung Selatan",
                "Alamat": "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur": "20",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakaknya cantik, pinter, rapi, dan kelihatan rajin banget.",
                "Pesan": "Semangat terus belajarnya Kak, semoga nilainya selalu memuaskan!"
            },
            {
                "Nama": "Difanya Husakina",
                "NIM": "124450043",
                "Asal": "Pagar Alam",
                "Alamat": "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur": "20",
                "Sosmed": "@difanyhsa",
                "Kesan": "Kakaknya anggun, adem, tenang, dan sangat menghargai orang lain.",
                "Pesan": "Semoga kebaikannya dibalas dan sukses terus perkuliahan nya ya, Kak!"
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM": "124450054",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Berenang",
                "Umur": "20",
                "Sosmed": "@nzlhauly_",
                "Kesan": "Kakaknya cantik, percaya diri, dan murah senyum.",
                "Pesan": "Tetap semangat jalani hari-hari kuliahnya dan sukses selalu ya, Kak!"
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM": "123450041",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur": "20",
                "Sosmed": "@r.hanaap",
                "Kesan": "Kakaknya manis, pinter, ramah, dan sangat baik hati.",
                "Pesan": "Semoga sukses perkuliahannya Kak dan lancar terus buat hobinya!"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM": "124450061",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobi": "-",
                "Umur": "21",
                "Sosmed": "@daffascript",
                "Kesan": "Abangnya keren, cool, pinter, dan kelihatan berwawasan luas.",
                "Pesan": "Semoga makin sukses perkuliahan dan kodingannya ya, Bang!"
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM": "124450098",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Nonton Anime",
                "Umur": "20",
                "Sosmed": "@edsel_0712",
                "Kesan": "Abangnya santai, ganteng, humble, dan mudah didekati.",
                "Pesan": "Tetap jadi abang tingkat yang seru dan lancar terus kuliahnya ya, Bang!"
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "NIM": "124450085",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Umur": "20",
                "Sosmed": "@luciarachel_",
                "Kesan": "Kakaknya cantik, ramah, dan penyabar banget.",
                "Pesan": "Semangat terus perkuliahannya ya Kak, sukses selalu buat ke depannya!"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM": "124450124",
                "Asal": "Lampung Tengah",
                "Alamat": "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur": "20",
                "Sosmed": "@_shaazzh",
                "Kesan": "Kakaknya manis, artistik, ramah, dan pembawaannya santai.",
                "Pesan": "Tetap berkarya ya Kak, semoga sukses terus dalam perkuliahan!"
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM": "124450112",
                "Asal": "Lampung Timur",
                "Alamat": "Rajabasa",
                "Hobi": "Begong",
                "Umur": "18",
                "Sosmed": "@xifasky",
                "Kesan": "Kakaknya cantik, imut, sopan, dan sangat mengayomi.",
                "Pesan": "Semoga selalu dimudahkan dalam segala hal dan lancar kuliahnya ya, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1-xIe0PrSCbcfqOI7QcqJdo0NkzCkFnpG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SVZKaHEBj8TGTXTy846quHDacPyfGXhB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1M92oYn0ZX_XGfKKE03FlM-Y7unO7657q&sz=w1000",
                "https://drive.google.com/thumbnail?id=11ydEuHupLLSHwXBNMyhSjQ3GlZ9ht9Ai&sz=w1000",
                "https://drive.google.com/thumbnail?id=1TdYAJDGdQMC-pcB1yWln2Q5GOEmEXnND&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YKXppYN9D-pLY4x8wrwW7c9wk_oYt1CB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ykzrZsZaL2PlD49oyBtOz-2JWNt5aJ0Z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OXWwOhLRO1xit7RuDe5rzXOKY8Nqb-Tq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CanAT3Hcpj3bOpAPWu10WG7uUMtwKI-C&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NT7qBFvdyXvXYnmuzRzedAJr3UGbfDy0&sz=w1000",
                "https://drive.google.com/thumbnail?id=178IHeDYx4wnjCthN-D5pIMco9j2p4v67&sz=w1000",
                "https://drive.google.com/thumbnail?id=1RWgx-yWdF4pUlfxmURv9B241R8Xxup_F&sz=w1000",
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
                "Kesan": "Abangnya pinter, pinter bawa diri, dan kelihatan berwawasan luas banget.",
                "Pesan": "Semangat terus risetnya Bang, semoga pencarian jurnal dan Pak Lucy-nya selalu lancar!"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya cantik, ramah, manis, dan kelihatan pinter bikin masakan enak.",
                "Pesan": "Sukses terus perkuliahan nya Kak, semoga selalu bahagia dan makin jago masak!"
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kakaknya cantik, manis, asik diajak ngobrol, dan selera filmnya keren.",
                "Pesan": "Tetap jadi kating yang seru ya Kak, sukses selalu buat akademiknya!"
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Abangnya pinter, keren, kalem, dan kelihatan jago banget urusan IT.",
                "Pesan": "Sukses terus perkuliahannya Bang, semoga semua project Docker-nya lancar tanpa error!"
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya cantik, gigih, mandiri, dan punya semangat yang keren banget.",
                "Pesan": "Semangat terus menjalani aktivitasnya Kak, semoga rezekinya ngalir lancar selalu!"
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya ganteng, ramah, santai, dan seru pas ditanya-tanya biodata.",
                "Pesan": "Tetap jadi abang yang asik ya Bang, dan semoga sukses terus perkuliahannya!"
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya cantik, manis, kalem, dan pembawaannya sangat menenangkan.",
                "Pesan": "Semoga istirahatnya selalu cukup dan dipermudah terus kuliahnya ya, Kak!"
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya cantik, ceria, supel, dan penuh dengan energi positif.",
                "Pesan": "Tetap jadi sosok yang menginspirasi ya Kak, semoga semua usahanya makin sukses!"
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "Abangnya keren, atletis, ganteng, dan pembawaannya santai banget.",
                "Pesan": "Semoga makin jago main basketnya Bang, dan lancar terus akademiknya!"
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Abangnya ganteng, sabar, humble, dan enak diajak bertukar cerita.",
                "Pesan": "Semoga pancingannya selalu dapat banyak ikan dan kuliahnya dimudahkan, Bang!"
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya cantik, manis, anggun sesuai namanya, dan ramah banget.",
                "Pesan": "Tetap jadi pribadi yang hangat ya Kak, semoga lancar terus perkuliahan nya!"
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kakaknya cantik, imut, ramah, dan pembawaannya sangat menyenangkan.",
                "Pesan": "Semangat terus jalani masa kuliahnya Kak, semoga sukses selalu ke depannya!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1HQh-Bf1xliYryGgHxDyWlC2Y2p6Shr_B&sz=w1000",
                "https://drive.google.com/thumbnail?id=10qP-3eVN5zp271mHcM9VNPpuHWErRnV4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZgsoFPEX3agANAToO9z_WOr0JKkOquNB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1treBoWtYhkSKrerwMXbUvejnHzONHff8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Gx3qaIIhZR0sReVIEXlIQu29auvZ2_K8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1GdS84UI_EH18M4MwWYwAvpBjEPGAsNTM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1AtX-63uhA2zYiE3uRYddI5v4kC2kH7Lw&sz=w1000",
                "https://drive.google.com/thumbnail?id=13Hf_sF5PIiZIe_qPIgBdZUua-jteWT6j&sz=w1000",
                "https://drive.google.com/thumbnail?id=1z8qBvmO_vXDbxU8g9CZkvqh55dONPX5C&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LzdTVXhuh2Q60uAxbzHCCKAdyp9dNKfd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1cDRG48sNb9L9uqAXjZ-d4MblTbfRhQ5n&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uX8Yr27sxE5p8pmbS5NEMGpDKAz9_xkk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wb9P2okyLl2EdUeIyF1ATCIGpa5pyzyq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QgkuimwxanfUqMJ3YZVTKI0yqXGAKdsH&sz=w1000",
                "https://drive.google.com/thumbnail?id=19Y0DeIhKQYaMOR5eyguxu4i9Vd2HKQzn&sz=w1000",
                "https://drive.google.com/thumbnail?id=11KiBKK4mZdf354ibFNXM4kskd44vmFFe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BkBF8uF8r7ItPLFD__mafjjQe6xHIuK_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sUp88lKHUdyYMg2McTLo05QHdaudfDA3&sz=w1000",
                "https://drive.google.com/thumbnail?id=192OXhVLin21-LH6KbOs0a4nLWW6BiVUZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vDBMDP9T4_fE-X8pnLjaqVD3p_mkGyzD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PiPeAO2rELwuerGICS6E1XijqrB0DvWg&sz=w1000",
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
                "Kesan": "Kakaknya cantik, to the point, dan proses fotonya cepet banget.",
                "Pesan": "Semangat terus kuliahnya Kak, sukses selalu buat ke depannya!"
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kakaknya cantik, ceria, supel, dan gampang banget akrab sama maba.",
                "Pesan": "Semoga jalan-jalannya makin seru dan sukses terus perkuliahan nya, Kak!"
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "123450015",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kakaknya manis, pendiam, dan sat-set pas diajak foto.",
                "Pesan": "Tetap semangat kuliahnya Kak, semoga semua urusannya dilancarkan!"
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Abangnya cool, kalem, ga banyak ngobrol tapi tetep ramah.",
                "Pesan": "Tetap semangat kuliahnya ya Bang, sukses selalu buat akademiknya!"
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kakaknya cantik, stylish, penuh percaya diri, dan pembawaannya ceria.",
                "Pesan": "Tetap memancarkan energi positif ya Kak, sukses terus akademiknya!"
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Abangnya ganteng, santai, dan punya topik hobi yang unik banget.",
                "Pesan": "Semoga cepat terwujud rumah impiannya ya Bang, semangat terus kuliahnya!"
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Abangnya ganteng, ramah, dan humornya dapet banget pas ngobrol.",
                "Pesan": "Semangat terus perkuliahannya Bang, tetap manis dan lancar urusannya!"
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kakaknya manis, kalem, dan enak diajak bertukar rekomendasi film.",
                "Pesan": "Semoga kuliahnya lancar terus Kak dan selalu nemu film-film bagus!"
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Abangnya keren, ramah, dan pinter banget mencairkan suasana kaku.",
                "Pesan": "Tetap jadi abang tingkat yang asik dan sukses selalu di perkuliahan ya, Bang!"
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kakaknya cantik, kocak, seru, dan hobinya bener-bener luar biasa unik.",
                "Pesan": "Semoga pancingannya dapat hasil terus ya Kak, sukses selalu kuliahnya!"
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kakaknya anggun, telaten, responsif, dan kelihatan cekatan banget.",
                "Pesan": "Sukses terus perkuliahan nya Kak, semoga semua urusannya dipermudah!"
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "20",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kakaknya manis, terbuka, dan jawaban pas wawancara bikin ngakak.",
                "Pesan": "Tetap jadi sosok yang menghibur dan semangat terus kuliahnya ya, Kak!"
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Abangnya keren, asik, humoris, dan bikin perkenalan ga tegang.",
                "Pesan": "Sukses terus perkuliahan dan organisasinya Bang, tetap seru!"
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kakaknya cantik, dewasa, tenang, dan sangat santun pas ngobrol.",
                "Pesan": "Semoga perkuliahan nya selalu dimudahkan dan sukses terus ya, Kak!"
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "21",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "@tarisyahr",
                "Kesan": "Kakaknya manis, hangat, dan dari caranya menjawab kelihatan baik banget.",
                "Pesan": "Tetap menyebarkan kebaikan ya Kak, semoga sukses selalu akademiknya!"
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kakaknya cantik, kalem, dan pembawaannya sangat menenangkan.",
                "Pesan": "Semoga istirahatnya selalu cukup dan lancar terus kuliahnya ya, Kak!"
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Abangnya ganteng, sabar, dan telaten banget pas diwawancarai.",
                "Pesan": "Semoga ikan cupangnya sehat-sehat dan sukses terus kuliahnya ya, Bang!"
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Abangnya keren, santai, dan cara jawabnya bikin suasana cair.",
                "Pesan": "Tetap jadi abang yang seru dan semoga dipermudah semua urusannya, Bang!"
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Abangnya pinter, unik, humble, dan cara berpikirnya beda dari yang lain.",
                "Pesan": "Semoga cepat nemu hobi baru yang pas dan sukses selalu kuliahnya ya, Bang!"
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "20",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "Membaca",
                "Sosmed": "@jaldii_",
                "Kesan": "Abangnya cool, pinter, ramah, dan jawaban biodatanya out of the box.",
                "Pesan": "Tetap semangat kuliahnya Bang, semoga makin banyak bacaan yang bermanfaat!"
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Kakaknya cantik, ceria, dan humoris banget pas diajak wawancara.",
                "Pesan": "Tetap jadi kating yang menghibur dan sukses terus perkuliahannya ya, Kak!"
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kakaknya manis, ramah, dan pembawaannya sangat bersahabat.",
                "Pesan": "Semoga jalan-jalannya selalu seru dan lancar terus perkuliahannya ya, Kak!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1QalmaW3s_jlA5AEUiQSDysJb7qTxP8-5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vxYt_r9jar9Y4rALSIdW4doQqdIPkTKx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rUUmq6-YWom_Jghzar6m25TdC9E9unVW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DfvpD1bpkLvYQvLgIYy5RB7jboIFb1Jt&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LL1ai36LjiQe_7OXSOzkP3P3pKMcnJ6M&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yLkOHsMaQaE49Xy8NugosI7i6fScNpXG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FJdPi0wARVCrIPWJHeybxd_CMGmMO_tF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Jts66hPKqlbzsRjzoGgeXu8onziYZr71&sz=w1000",
                "https://drive.google.com/thumbnail?id=1V4ElsOcmcj1ENC3cBU5yev94JhcNpVwB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mHKnN4iQVfdRVvKmB5cAg6fttQxwMbS1&sz=w1000",
                "https://drive.google.com/thumbnail?id=1b1PE0yx1OlJmemu22K3iPf-IoXJxCiy0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1cielrH7c7gTHanuVCiKC9QfAqt0mhAgk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QE0w7Fk41xLJcGA3JX2pYaP0NUktE4Zm&sz=w1000",
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
                "Kesan": "Abangnya pinter, keren, rapi, dan rajin banget.",
                "Pesan": "Tetap jadi abang yang bisa diandalkan dan sukses terus kuliahnya ya, Bang."
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Kakaknya cantik, ramah, dan selera musiknya keren banget.",
                "Pesan": "Semangat terus kuliahnya Kak, semoga harinya selalu diwarnai lagu-lagu enak!"
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Abangnya ganteng, humble, dan punya tontonan yang unik.",
                "Pesan": "Sukses selalu perkuliahan dan urusannya ya Bang, tetap keren!"
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "Abangnya keren, santai, dan asik banget diajak ngobrol.",
                "Pesan": "Semoga makin jago main game-nya dan lancar terus kuliahnya ya, Bang."
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "Kakaknya cantik, manis, ceria, dan hobinya unik banget.",
                "Pesan": "Tetap ceria ya Kak, semoga koleksinya makin lengkap dan kuliahnya lancar!"
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Abangnya kelihatan cool, santai, dan karismatik banget.",
                "Pesan": "Tetap semangat kuliahnya Bang, jangan lupa jaga kesehatan pas ngopi!"
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kakaknya cantik, supel, dan hangat banget ke adik tingkat.",
                "Pesan": "Semoga pertemanannya langgeng terus dan sukses selalu kuliahnya ya, Kak!"
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kakaknya anggun, ramah, dan pinter nyambungin obrolan.",
                "Pesan": "Semangat terus Kak kuliahnya, semoga selalu diberi kemudahan!"
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Abangnya ganteng, ramah, dan kelihatan atletis.",
                "Pesan": "Sukses terus buat akademiknya dan semoga sehat selalu ya, Bang."
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kakaknya manis, sabar, telaten, dan kelihatan penyayang.",
                "Pesan": "Semoga hasil rajutannya makin bagus dan kuliahnya dipermudah terus ya, Kak."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Abangnya keren, badannya bagus, dan pembawaannya tenang.",
                "Pesan": "Tetap konsisten nge-gym nya Bang, dan semoga sukses terus akademiknya!"
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kakaknya cantik, stylish, manis, dan asik diajak ngobrol.",
                "Pesan": "Sukses terus perkuliahan nya Kak, tetap keren dan semangat selalu!"
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "Kakaknya cantik, unik, dan pembawaannya ceria banget.",
                "Pesan": "Tetap jadi sosok yang menghibur dan sukses selalu perjalanan kuliahnya ya, Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1AB-g6-uiVFPN4z80LdmTOlS8aWB2OWj-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qb4whlWKuA4XF3dbM0t9JLNZnOLWJXW2&sz=w1000",
                "https://drive.google.com/thumbnail?id=12YlYz4AvEb7B3F0YjBqyzWNCr9StHWeh&sz=w1000",
                "https://drive.google.com/thumbnail?id=10t2dgu4PTEl1thdZxd4tePqndpLagwsQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WhqkeTfc6YW39dprlMtiD6HtccRwRtjp&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wZnElqqvMDiOSQb9j-NS_tX1szgf9pLV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1p0Eu-qPinyCSoGxWNBhkqVabPRff_NQL&sz=w1000",
                "https://drive.google.com/thumbnail?id=18f2D1fcWY_ZrCCoMHOKtlcqJe0XxGoXc&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KVsBFDLY1vRoXDFpE0IdeeE6hsJY2fa3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZSDKG7InqdnyhfshXdd0IYzNERHIePMY&sz=w1000",
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
                "Kesan": "cantik dan keliatan pinter banget.",
                "Pesan": "Tetap berkarya kak dan jangan lupa istirahat."
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "unik humoris, bikin ga canggung.",
                "Pesan": "Tetap semangat bang dan jangan lupa semangat juga kuliah."
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
                "Kesan": "cantik dan seru diajak ngobrol.",
                "Pesan": "Seru diajak ngobrol dan ga pernah pelit senyum."
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
                "Pesan": "Tetap semangat kuliahnya bang jangan lupa jaga kesehatan."
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
                "Pesan": "Tetap jaga kesehatan kak dan semoga tontonan kita sama."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "cantik baik lucu sukaaa kakak iniii.",
                "Pesan": "Tetap banyak energi ya kakkk."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "baik keren ga bikin canggung sama adek tingkat.",
                "Pesan": "semoga abang cepat lulusss."
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kalem dan cantik, suka banget sama kakak ini.",
                "Pesan": "Semangat terus kuliahnya kakak, semoga dimudahkan selalu."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Sederhana, humble, tapi sangat menginspirasi kami semua..",
                "Pesan": "Terus banyak belajarnya kak dan tetap menginspirasi."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1eQdoJoz34yRwEEtTskk4WeLQ7HYzakh9&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ndb2xzRGja1bkKT0RKZY560i-rkUUaPk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uBXUn5Zl0Bl9yxK3lvIUJ4znr5dXFxko&sz=w1000",
                "https://drive.google.com/thumbnail?id=1O1XYVY4PHwTUWs5XA15V5igbXppDt-_j&sz=w1000",
                "https://drive.google.com/thumbnail?id=14z41J6tRrqzN8cb8JTLysFv_Rseu0kYq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Lbx4fBTkY3KU4mk1xcSbowLUEFYgOi74&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BRUwBwlftSpFHIqsliOIHmCXA5huriNa&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZB1hUMfgg-ApKt4kDsXtIhurNONBd8Ag&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wYHK0Ax2lOh60Z9TXP5yRmto4eyir1f_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VxT4skOWhWfHIjhWZssNL3eveRZMz-7p&sz=w1000",
                "https://drive.google.com/thumbnail?id=10i9EBHmoL0WiRtbwWpa4Z2poPVlQzvD_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1U6vKt5pVEGGCf3VXMKWyLLqtKxl-uqYi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Kb4U-iRlWBvLC_Pre04Fuc_iE-WXI0Qs&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rh5_mpW-WM5iOa6LsCS4JFg-geQIyd9m&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nWMQy9X8PDT_r9bh3v-D62DOhnLvrPkw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lokCzJKClOJCLH81v4FH1NnaAQ_8Q5eI&sz=w1000",
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
                "Kesan": "cantik dan mudah akrab sama siapa saja.",
                "Pesan": "semangat terus kuliahnya kakak dan jangan lupa jaga kesehatan ya."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "baik dan mudah diajak bicara.",
                "Pesan": "Semoga dimudahkan dalam setiap urusan kak."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "Belajar & Bermain",
                "Sosmed": "@nobelnizam",
                "Kesan": "Kalem sopan bikin kagum, panutan saya banyak prestasinyaa.",
                "Pesan": "Terus semangat dan semoga banyak pencapaian baru ya abang."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "baik dan agak pendiem tapi jarang senyummm.",
                "Pesan": "Tetap semangat terus abang sukses dan sehat selalu."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "baikkk banget abangnya keren juga.",
                "Pesan": "Semangat abang kuliahnya, semoga sukses teruss."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "abangnya berwibawa tapi asyik diajak ngobrol.",
                "Pesan": "Tetap semangat abang semoga cepat lulusss."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Aktif baik dan bikin kagumm.",
                "Pesan": "Terus berkembang dan sukses terus kakkkk."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Dewasa dan kerenn.",
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
                "Kesan": "Ceria dan cantikk.",
                "Pesan": "Semangat terus kak dan semoga cepat lulus."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Ramah dan murah senyum.",
                "Pesan": "semangat kakak ngejar nilainyaaa sehat sehat teruss."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Orangnya serius tapi humoris jugaa.",
                "Pesan": "Terus semangat dan juga tetap jadi panutanku bang."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "cantik banget senyumnya juga manis banget kak.",
                "Pesan": "Pertahankan semangat dan sehat sehat terus kak."
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
                "Kesan": "Santai dan mudah diajak bercanda.",
                "Pesan": "Tetap semangat bang ngerjain tugasnya."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Ramah dan cantikk.",
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
                "Kesan": "keren dan suaranyaaa lucuu bang.",
                "Pesan": "semangat terus abang dan tetep jadi pribadi yang baik yaa."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "cantik ramah baikkk sukaak.",
                "Pesan": "Semangat terus kakak dan tetap jaga kesehatan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()