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
                "https://drive.google.com/thumbnail?id=1JtoKjTY33PTRMv5PjuUh4t5V7wvHAmhc&sz=w1000",
                "https://drive.google.com/thumbnail?id=1s_7b9x2qKyJOqrprPb3WRspuiuTWPNXp&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ohRDjedx8cqCjrdYYIG_32UZw4GJuNo3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bZ7UkqtIHDJZIkIRoNJk87HsoEGTq2AE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NFJRqNDoe7l7A4beOpR8A1-5kqr2EgAC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NFJRqNDoe7l7A4beOpR8A1-5kqr2EgAC&sz=w1000"
        ]

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450066",
                "Asal" : "Bakinang",
                "Alamat" : "Sekretariat HMSD",
                "Hobi": "Push Rank",
                "Umur" : "22",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "Sosoknya tenang dan mengayomi.",
                "Pesan" : "Tetap jadi kakak yang bisa diandalkan, Kak."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Abangnya terlihat keren dan berwibawa banget.",
                "Pesan" : "Semangat terus ya bang."
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Sosoknya ramah dan penuh semangat.",
                "Pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Cara bicaranya santai tapi berisi.",
                "Pesan" : "Jangan bosan membagi ilmu ke kami."
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Senyumnya hangat dan bikin suasana cair.",
                "Pesan" : "Tetap jadi kakak yang ramah, ya, Kak."
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
                "Pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1WNutOGPIKaMQDEJ15WnQBiZrzJIBn27Z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dyhhbOXA6a_67mX1msaJMoJQsgCuW6MW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1TwiXGe0q8FwTqxhDOg9ZSCc2VWof6mNF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1UJoq_ra0pOEthOvQwIKfKVRr2gjDEc5c&sz=w1000",
                "https://drive.google.com/thumbnail?id=15cbZqxeVrti5ckT4Dop5Ff6oPL9xe5f-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ywe29tDtyrHSf8I5s0rLjEEhdLmRDQX6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EKv6np_KKHql6An6N4ruedGpJ5aI93Ut&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ximU1BOk4HEeMbQljlKXMgqQk88cEFen&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hhBxLMHpAFAegycSkx1PCUoAU_AtIaoo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pem4kUZsBIrXsxd5ldbqmkhRmnKl7VYH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NPiwo6KIIqL7gAsWsU_emsIBrdPYb84L&sz=w1000",
                "https://drive.google.com/thumbnail?id=1khLrj5EC3uJIvSM5HcMgs-m0euv3EzVM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hnqnnxFe3vz7iJDKvgZGaKSkGLmlO-rS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tZO1_FKLHFgjcK-r52j5CGLt8DcFYUD8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uq8ImIkN0ihpi8YGjl7RnqctgLyquk5E&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iF51-ShWc-PkvHGdmiRPvOCOnmohI30i&sz=w1000"
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
                "Kesan": "Humornya sederhana tapi bikin akrab.",
                "Pesan": "Jaga suasana cair tanpa berlebihan."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Suka Nolong Orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Cara bicaranya lembut tapi tegas.",
                "Pesan": "Jangan ragu terus membimbing kami dengan sabar."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Sumatera Utara, kisaran city",
                "Alamat": "Sukarame",
                "Hobi": "Ngabarin Orang Tua",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Perhatiannya ke adik tingkat sangat besar.",
                "Pesan": "Semoga kebaikan Kakak selalu kembali."
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
                "Pesan": "Tetap adil dan pertimbangkan banyak hal."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Selalu rapi dan enak dilihat.",
                "Pesan": "Tetap jadi panutan tanpa harus menggurui."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Pintar menenangkan saat kami panik.",
                "Pesan": "Terus jadi tempat cerita yang aman."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Suka membantu tanpa pamrih.",
                "Pesan": "Semoga kebaikan Kakak berbuah baik."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Humornya segar dan tidak berlebihan.",
                "Pesan": "Jaga energi positif itu sampai kapan pun."
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Disiplin dan tepat waktu.",
                "Pesan": "Tularkan kebiasaan itu ke adik tingkat."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Tegas saat organisasi butuh keputusan.",
                "Pesan": "Tetap adil dan bijak dalam memimpin."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Berwibawa tanpa harus marah.",
                "Pesan": "Terus jadi panutan yang bijak."
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Suka menolong tanpa banyak bicara.",
                "Pesan": "Jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Disiplin soal waktu.",
                "Pesan": "Ajari kami juga cara mengatur prioritas."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Pandai memberi nasihat praktis.",
                "Pesan": "Terus jadi kakak yang solutif."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Ramah ke semua orang.",
                "Pesan": "Pertahankan sikap terbuka itu."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Ramah ke semua orang.",
                "Pesan": "Pertahankan sikap rendah hati itu."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1j6L99JPX4YPYy0veRXIk5kuGiXX8KS_D&sz=w1000",
                "https://drive.google.com/thumbnail?id=1oefj5vLZsmZCdiIgIj7tjdrTvuVXh5rO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ee_GPvqGEX2cAx7T5t7kYYWvRYLXy452&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-DfR0nGkaTuWVRokLFwBb2_7FgbKqKP-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1G34OGsF_Wm3Whd1Z7BIbTaAzB_cciFcY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XLu5zKpSrN7WZJAnCwPZgVh4wlV5HhcC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1W3ROGSuUAtlW8qQ1QN7tHvtfVGW9kIO3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1W3ROGSuUAtlW8qQ1QN7tHvtfVGW9kIO3&sz=w1000",
                "https://drive.google.com/thumbnail?id=15iehUZkkjW6Tcg8U95_Ph3zaaqcitKcL&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sY5VA4_bvhfXhTdRELSLuwkrrhwihGou&sz=w1000",
                "https://drive.google.com/thumbnail?id=1R7tTmDajmxpPODA-Dv6EvrwDXcudvuN9&sz=w1000",
                "https://drive.google.com/thumbnail?id=1AFSlHMbqQkXIeoqkdEV5VTRxJe1WOmvU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ys9TPzzPmFTsAIvihv2AFmoTJatt7VUA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YYdci_AShj7h6EUE2aGr8dXaS0NPWLL8&sz=w1000",
                "https://drive.google.com/thumbnail?id=12HicG_YLef7-LD1EirK1l3b5nhsDaVGi&sz=w1000"
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
                "Kesan" : "Sosoknya santai tapi tetap bisa diandalkan.",
                "Pesan" : "Tetap jadi kakak yang asyik diajak ngobrol, Kak."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Tutur katanya tenang dan enak didengar.",
                "Pesan" : "Terus bagikan wawasan dari bacaanmu ke kami, Kak."
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi",
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Orangnya kalem dan tidak banyak menuntut.",
                "Pesan" : "Tetap jadi pribadi yang rendah hati, Kak."
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
                "Pesan" : "Semoga semangat belajarnya menular ke kami, Kak."
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Setia kawan dan gampang bikin suasana ramai.",
                "Pesan" : "Jangan berubah, tetap jadi teman yang seru, Kak."
            },
            {
                "Nama": "Juwita Sari",
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Sikapnya lembut dan menenangkan.",
                "Pesan" : "Tetap jadi tempat bercerita yang nyaman, Kak."
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Ceria dan selalu kompak dengan teman-temannya.",
                "Pesan" : "Terus jaga kekompakan itu, Kak."
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Mudah akrab dan enak diajak berdiskusi.",
                "Pesan" : "Tetap jadi kakak yang terbuka ke adik tingkat, ya, Kak."
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Bertanggung jawab dan siap membantu kapan saja.",
                "Pesan" : "Jangan lelah jadi tumpuan kami, Kak."
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Teliti dan sabar dalam mengerjakan sesuatu.",
                "Pesan" : "Tetap semangat dan jangan ragu bertanya ke kami, Kak."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Percaya dirinya tinggi dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang menghibur, Kak."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Royal ke teman dan murah hati.",
                "Pesan" : "Semoga kebaikanmu selalu dibalas, Kak."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "20",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Pembawaannya adem dan tidak neko-neko.",
                "Pesan" : "Tetap jadi pribadi yang apa adanya, Kak."
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Ceria dan punya selera humor yang unik.",
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
                "Kesan" : "Disiplin dan selalu memulai hari lebih awal.",
                "Pesan" : "Ajari kami cara menjaga konsistensi, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=19psHwZ9znuKFiBCCHuuDYXNPx9df3pUJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1m8gmIDAtA5KncwkN996RX4PhAPEOm3i0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1H0h3p_yB2en_pdbVCVjW6NT_swZ8EwpT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dPutH8EIEgp5y_4pjsUMQ5H3Mv6y2rtq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ssEOT036CUmkHuqkbdHVoRau83Ckp_N7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1H9HFituForABUKBJQVg7azBxqUteUcCw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NNiMwWkNiUdnAg5Fhioua9VwZGVGRR1r&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NnTdYJlESOf-Vok1j1zdWIoXu2YNLZkT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1TQnLlzBMI5iUujhDcw2tyk-0R0jsfQqP&sz=w1000",
                "https://drive.google.com/thumbnail?id=17-VUenp8BFNITp6dzyo2GfMjg8w6UrjU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1HPUq4D_CiaJ7IwQYWI4X1VRohPBOoK2V&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Z5ZFBmy0T_T0KIhm9Jg3wPkB9dRWYIPB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iwv-4SHQJQycmPIgAfyDE3jGjHxPHqGP&sz=w1000",
                "https://drive.google.com/thumbnail?id=14lNSP4A8a7YZLA-LC0_3AwfXNhIqM185&sz=w1000",
                "https://drive.google.com/thumbnail?id=1gqbtH8ESODqzBABc1j9z12wwPCBSLVCW&sz=w1000"
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
                "Kesan" : "Gayanya santai dan tidak pernah ribet.",
                "Pesan" : "Tetap jadi kakak yang asyik, Kak."
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "Pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Permainan gitarnya bikin suasana nyaman.",
                "Pesan" : "Sering-sering hibur kami lewat musikmu, Kak."
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "Pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "Pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Aktif dan berani mencoba hal baru.",
                "Pesan" : "Terus berani melangkah, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Ramah dan selalu terlihat ceria.",
                "Pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
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
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "Pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "@_els.a",
                "Kesan" : "Murah senyum dan enak diajak bicara.",
                "Pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "Pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "Pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Humoris dan gampang bikin tawa.",
                "Pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "@sher_renna",
                "Kesan" : "Rapi dan selalu tampil percaya diri.",
                "Pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "Pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "@Faizaanjanii",
                "Kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "Pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Santai tapi tetap bertanggung jawab.",
                "Pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "Pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "Pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Ceria dan mudah menyesuaikan diri.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "124450099",
                "Asal" : "Lampung Utara",
                "Alamat" : "Asrama TB 3",
                "Hobi": "Membaca",
                "Umur" : "20",
                "Sosmed" : "@syafiqui",
                "Kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "Pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "@henryferdianto",
                "Kesan" : "Humornya unik dan bikin suasana cair.",
                "Pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1YepNtHvwTCyrVfAm7577qFzZpQrdx3oX&sz=w1000",
                "https://drive.google.com/thumbnail?id=15vTQ2TdyMqtrlwqkkB_L1bAfacByo7eZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pnQ8boWhIszkZ8uLfya_WMxGuvpJcORT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pmZL7VMD4JUlX5HPDQxzmFhn0L-1YbTj&sz=w1000",
                "https://drive.google.com/thumbnail?id=12QXyg00uJ1NPGtvv972JhpjJLGaVHHS8&sz=w1000",
                "https://drive.google.com/thumbnail?id=125vE-qnunXojIOPfucx_kD3slU15mrBy&sz=w1000",
                "https://drive.google.com/thumbnail?id=162sJ2orVR5OQT4cBv6ZOnZMbpbXbLOqR&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nJeC6CJyn_M7qEUjjWxECN6sFHK1AI9m&sz=w1000",
                "https://drive.google.com/thumbnail?id=18HA49D2tDVgezsxDfqBDbxgNaRkbKT5v&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ynkzrj7glM5tqSGwvOtRAvBHcG4jrzZa&sz=w1000",
                "https://drive.google.com/thumbnail?id=17UD7LvUsjcr14Kdt2Dd7pfOgfOaFvN0Q&sz=w1000",
                "https://drive.google.com/thumbnail?id=1gdvw8IROVhlTtXvZxT26_VSxGZDoiN-v&sz=w1000",
                "https://drive.google.com/thumbnail?id=1kDxTiXyUXmnRPQB4JjeZTk4pg4TktXhr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ktR1MTSJij8xon7dpna0Uuo-c_ehJekX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1u2W1YvrQKmxyDCLHJCqy26qAsKGkDQKU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rurDvC7m2m1Iqr35K7is1WdW94kCOtBT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1kpPo5DIrnHiXnUyXnoHuqT0l5FmkkZKd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BJbljYPlEjXRNhVJp_NcCYhmWvd1Fgar&sz=w1000",
        ]

        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM" : "123450082",
                "Asal" : "Payakumbuh, Sumatera Barat",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "20",
                "Sosmed" : "@naylasalsabilaa._",
                "Kesan" : "Bicaranya halus dan enak diajak ngobrol.",
                "Pesan" : "Tetap jadi kakak yang sabar, ya, Kak."
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM" : "123450028",
                "Asal" : "Bekasi",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Pendengar yang baik dan selalu tulus.",
                "Pesan" : "Terus jadi teman berbagi yang nyaman, Kak."
            },
            {
                "Nama": "Labo John Nuel Napitupulu",
                "NIM" : "123450037",
                "Asal" : "Medan",
                "Alamat" : "Belwis",
                "Hobi": "Motoran",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Wawasannya luas dan cerita pengalamannya seru.",
                "Pesan" : "Sering-sering bagi cerita perjalananmu, Kak."
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Way Halim",
                "Hobi": "Nonton",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Fokus dan tekun kalau sudah mengerjakan sesuatu.",
                "Pesan" : "Semoga ilmu codingmu terus berkembang, Kak."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM" : "124450104",
                "Asal" : "Lampung Timur",
                "Alamat" : "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur" : "19",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Usilnya menyenangkan dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM" : "124450031",
                "Asal" : "Jawa Barat",
                "Alamat" : "Korpri",
                "Hobi": "Foto Orang",
                "Umur" : "21",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Jahilnya bikin akrab, tapi tetap tahu batas.",
                "Pesan" : "Jaga kekompakan sama teman-teman, Kak."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM" : "123450086",
                "Asal" : "Karawang",
                "Alamat" : "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Gigih dan tidak mudah menyerah.",
                "Pesan" : "Semoga TA-nya lancar dan cepat selesai, Kak."
            },
            {
                "Nama": "Allisha",
                "NIM" : "124450019",
                "Asal" : "Kayangan",
                "Alamat" : "Heaven",
                "Hobi": "Mancing",
                "Umur" : "16",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Gampang akrab dan setia sama teman-temannya.",
                "Pesan" : "Tetap jadi teman yang asyik buat semua, Kak."
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM" : "124450091",
                "Asal" : "Jambi",
                "Alamat" : "Airan",
                "Hobi": "Jalan-jalan",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Fleksibel dan mau mencoba apa saja.",
                "Pesan" : "Jangan berhenti penasaran sama hal baru, Kak."
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Rajin dan disiplin dalam belajar.",
                "Pesan" : "Bagi tips belajarmu ke kami juga, ya, Kak."
            },
            {
                "Nama": "Difanya Husakina",
                "NIM" : "124450043",
                "Asal" : "Pagar Alam",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Tutur katanya santun dan menyejukkan.",
                "Pesan" : "Tetap istiqamah dan jadi teladan, Kak."
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Berenang",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Anggun dan penuh percaya diri.",
                "Pesan" : "Terus kejar hobimu dengan semangat, Kak."
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM" : "123450041",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur" : "20",
                "Sosmed" : "@r.hanaap",
                "Kesan" : "Tenang dan pandai merangkai kata.",
                "Pesan" : "Tetap menulis dan bagikan idemu ke kami, Kak."
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM" : "124450061",
                "Asal" : "Surabaya",
                "Alamat" : "Sukarame",
                "Hobi": "-",
                "Umur" : "21",
                "Sosmed" : "@daffascript",
                "Kesan" : "Kalem dan tidak banyak bicara, tapi tulus.",
                "Pesan" : "Jangan sungkan bergabung ngobrol bareng, Kak."
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM" : "124450098",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Natar",
                "Hobi": "Nonton Anime",
                "Umur" : "20",
                "Sosmed" : "@edsel_0712",
                "Kesan" : "Santai dan punya selera humor yang khas.",
                "Pesan" : "Tetap jadi kakak yang gampang diajak bercanda, Kak."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "NIM" : "124450085",
                "Asal" : "Bekasi",
                "Alamat" : "Belwis",
                "Hobi": "Tidur",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Energik dan selalu menyemangati sekitar.",
                "Pesan" : "Terus tularkan semangat larimu ke kami, Kak."
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Apa adanya dan bikin suasana tidak kaku.",
                "Pesan" : "Tetap jadi diri sendiri, ya, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM" : "124450112",
                "Asal" : "Lampung Timur",
                "Alamat" : "Rajabasa",
                "Hobi": "Begong",
                "Umur" : "18",
                "Sosmed" : "@xifasky",
                "Kesan" : "Sopan dan selalu menghargai orang lain.",
                "Pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=150spvIH732frvTykFnAB-vQ8tZKrAMds&sz=w1000",
                "https://drive.google.com/thumbnail?id=1eBoDWfK7UkFWDYaSCC13X3zqGH9RxnDF&sz=w1000",
                "https://drive.google.com/thumbnail?id=159xm8lpWPXGpvkPtfSMGCNTY96qH0R2L&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QvJBsyXh2g71sciaKDZHbKbAFOpivCsY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jHL-gp3mQe2FMLjfXjBTmwJjxRQsY5bL&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qkibTKJUglAY6W-zvXooTEmH7Fc9YbZV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CmQ99pvV8c3k6NEsoj7Ujff57wyqX_pq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hB8Rw-jnnITKTvfJruNQ19Jfp8tszCL-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uBzSuiF7AM59CvaIlmKTthC5o2apTHum&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yTYJr3VEaebrQQrpFhzcFAYqOhEysTxW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Uyl1KLns2JH6wL3HQl19Wc5SFoLWhEyh&sz=w1000",
                "https://drive.google.com/thumbnail?id=19vrCfWo2Z1Lwuvn3wW68wxUbtzitrI3-&sz=w1000"
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
                "https://drive.google.com/thumbnail?id=1FJsnoWtcttzMPOzdKkYEJoW4Q08MHveK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1MAgKxuMgHOvPcTlCrJKPddOlCJ7qCCIV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1v5O2o6sb5tiOIiBmTpmOZsO-dzHed5Fw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1JWcIUDgdN8Y3mzlVkIG9oOq10eSWtR9P&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dMlyWfgccrnzTwPb3XeDvP7mFJnJ5bK7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1fzgJPcsHgCkZVfy61p1JeKyj_jHZU1ZC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bqN3I6skTNV4zIpYpwrT3NPH5LZqNVOq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1cCgZmLU-J-QL2qY2RSoqm1qiCB3j3Cxh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1IJlkVtVEnJ5YGf51XGVpyArdbEOJIpeD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bFIHlhvyJoMb0w3RJkH3mhosuBxOb7_o&sz=w1000",
                "https://drive.google.com/thumbnail?id=1v5O2o6sb5tiOIiBmTpmOZsO-dzHed5Fw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1G9oX8Lts_IQewPdTZmfNueSfUn01Fs-S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rEC5siE07QyorxYrMWGXtDesQQIsvvGx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Rk5h8gyqUSeUnhYVDx0WdRSPKiB0Nviy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1g6P19_T8jWGwottO5w_BylsG3bzCUgYq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LujUJgHl7WR7HLlXoOL30Elnj-B6F_5D&sz=w1000",
                "https://drive.google.com/thumbnail?id=1quj9-JX16DLam2g3J9KywNZ2y6k_I-Ur&sz=w1000",
                "https://drive.google.com/thumbnail?id=1evrVOh1cdJ3a0K3VJ7K5Y0QipDnVoW7z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1evrVOh1cdJ3a0K3VJ7K5Y0QipDnVoW7z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uqNGFaX6mUURrJCb2gR8p8ntNQWCKJdN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sPCtYDPQG4uJmxAgftGM5ueAR5Pq70We&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xccrud1DpzsMPn4uTkLjizxXVBg_ObB3&sz=w1000"
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
                "Kesan": "Kadepp tergacorrr.",
                "Pesan": "Semangatt jadi mahasiswa akhirrr kakkk."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kak Nabylaa sangat amat cantik dan gemeshh bangett.",
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
                "Kesan": "Bang Adit orang nya seru banget dan lucu wkwk.",
                "Pesan": "Selalu jadi orang yang aku kenal ya bang."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Aku kira kak fathyah galak, ternyata baik bangett pwiss.",
                "Pesan": "Selalu jadi orang baik yang saki kenal ya kak, ilove u."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Kakak terbaikk ku, kak tarii.",
                "Pesan": "Sehat sehat ya kak, semoga segera luluss."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kak Ashila baik bangett pwisss.",
                "Pesan": "Selalu jadi kakak yang baik ya kak."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Bang duta yang sangat amat ganteng.",
                "Pesan": "Sehat sehat bang duta, semoga bisa jadi artis dengan folls 785jt."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Bang Vian yang sangat amat royal.",
                "Pesan": "Terimakasih atas ice cream nya ya bang, mantab."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Bang yajidd ganteng dan imut bangett pwiss.",
                "Pesan": "Selalu jadi orang yang suka senyum ya bang, biar semut insecure liat nya."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Asik dan seru banget bang jaldyy no typu typu.",
                "Pesan": "Selalu jadi bang jaldy yang aku kenal ya bang"
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Kak kia baik bangett dan kalem.",
                "Pesan": "Selalu jadi kak kia yang menyenangkan ya kak."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Orang nya baik banget, kek ngerasa punya kaka cewe, dan kak selma cantikk bangett.",
                "Pesan": "TSelalu jadi orang baik dan jadi kakak yang hangatt ya kak, ilove u sm."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=11wiSbMy21CohBLDMDSywJBS039_5lq0M&sz=w1000",
                "https://drive.google.com/thumbnail?id=1_tc8oAGWSkeqit6mgWNccbTt2v2W3igQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1HogG7iyeL3TqsOTVBWQ1k53ky1UqOPrD&sz=w1000",
                "https://drive.google.com/thumbnail?id=17el5w0JwlNaMnmKI9gLBHd795lDu6kZ2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OiRuiEwCGDhxSKmHoJKzwCReaPTSs_wr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QhQPSJ4s9rmRsbQPPzqYCpw0rOw7y0yh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1riqXko0w-eeS32AYpjeRjOPz4XmbDSdj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1T9ouyaHlwpm-wUpO4nSkDnbfdrf96ei1&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BvvrKzWsHJzhpQx5mC4OJQL4ZldYPWfA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1st90r5tvmJnMIjJ0R4RPLk3sDb3ELb2m&sz=w1000",
                "https://drive.google.com/thumbnail?id=19B4q2KtD1FXse8hR0Ct_JcHdQtilSb6S&sz=w1000"
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
                "https://drive.google.com/thumbnail?id=1Z2ur6HPv2fOQytQ8Pp_l-_ou8V13JkID&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y0HcCUOG7La5UUYcGsj3AyiIjDtHyUP7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mN8EhtVzhXUM5lGNfdcaNSGVkEIGer40&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nlThPrJWya0QN8B5M-HtwIsvXqR97Wb0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VvA11ehuUXZRzLQUJepk9yi91iyU8ere&sz=w1000",
                "https://drive.google.com/thumbnail?id=19PDV7bQib4Rj4tZeGCk6NwqI6Pl8kDv4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1astbRDliPjJT_8FZMAK92su0RLnkYKJS&sz=w1000",
                "https://drive.google.com/thumbnail?id=16avNp-l-HGoCr7FZAgThRaw1GYsf8UlZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SAIowt7dyCRCS6XGcnIVb-uUk53IeEJv&sz=w1000",
                "https://drive.google.com/thumbnail?id=16MD4Nnr7zAC_ovsIFr9uExxDjNY8tSj2&sz=w1000",
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
                "https://drive.google.com/thumbnail?id=1JQD2qEHtliU0K8HfVOILL92szfDZoKTM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A-QPO7UNapoQupIDeBfbL9MI3vmG_c6b&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ABRT5_1IyOss6zLUNiENDfyTEcqiJB7W&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YCEv_yQpD0U0ED312t09WgHj_bURQAU1&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yA989KpOmkAQl4edjT0qmY4g8x4TWN9R&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qh5OkR4yrMhAzSts72TBcEgJOFtHhQW9&sz=w1000",
                "https://drive.google.com/thumbnail?id=1MmdqR22fXIqg838N13ektgHk75dfsuX0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jB5HCb8mMVHw1hQ0JADWiAX60WAyl-yy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lArzBcmL3tusiyC-Jj5VXX6rT8qYPB7k&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VnOTnJpDZtq99qAWHGbLha0DZPdXZ_KY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1geiTkbqnLSNDy_oeqGxs9JTwmvYP2Tnr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1H6uwJ-LV9iria56W09oAeftyfX7NBzvC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sP-u73e4-zNk5ehVfGhAILtolSMIeVO5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yOD5D8guPZPMKmZG6JWJoZ0at8OymHZU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1eQvxNgvWDjwJDXMw3TYFRoHzj2XTELfn&sz=w1000",
                "https://drive.google.com/thumbnail?id=19AHcrANZ7HZyq4By5Gd935zpJPmUGgCr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1GjSi66pgz4Nk3kqDDXQMV5cOLLOnDzMM&sz=w1000",
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
