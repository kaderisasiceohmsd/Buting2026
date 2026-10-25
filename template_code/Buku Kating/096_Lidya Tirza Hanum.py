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
            "https://drive.google.com/thumbnail?id=1yytmEPEcKTavC6gKO-BJeq5EJ00UjpoL&sz=w1000",
            "https://drive.google.com/thumbnail?id=197hVCDGTVk2vDMHd3XNrYmAwcf_SUMCm&sz=w1000",
            "https://drive.google.com/thumbnail?id=1reBkWFC84h4EzeN3M6yyw1YdwUCRgZBT&sz=w1000",
            "https://drive.google.com/thumbnail?id=1UKwbcALYQ_dsWjFGGKUWeclnrjqUmjBe&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Yjn--mYbGEHh6P7EYiKZqSiliSD9YRgq&sz=w1000",
            "https://drive.google.com/thumbnail?id=1a3FY4g5G6cDIA22Y1n_FNlnyU63qi_vU&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung", 
                "NIM" : "123450103",
                "Asal" : "Bakinang",
                "Alamat" : "Sekretariat HMSD", 
                "Hobi": "Push Rank",
                "Umur" : "22",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "Kak Ginda tampak tenang dan nyaman diajak berdiskusi.",
                "Pesan" : "Semoga Kak Ginda selalu sehat dan lancar menjalani amanahnya."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan", 
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru", 
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Kak Aqil memberi kesan sopan dan penuh tanggung jawab.",
                "Pesan" : "Semoga ke depannya selalu dimudahkan, Kak Aqil."
            },
            {
                "Nama": "Efi Defiyati", 
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Kak Efi terlihat bersahabat dan aktif dalam berbagai kegiatan.",
                "Pesan" : "Semoga setiap tugas yang dijalani berjalan lancar, Kak Efi."
            },
            {
                "Nama": "Qois Olifio", 
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Kak Qois berkomunikasi dengan jelas dan mudah dipahami.",
                "Pesan" : "Terima kasih atas bimbingannya selama ini, Kak Qois."    
            },
            {
                "Nama": "Hafsa Fazilah Arradhi", 
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung", 
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Kak Hafsa tampak ramah dan terbuka kepada banyak orang.",
                "Pesan" : "Semoga selalu diberi kesehatan dan kemudahan, Kak Hafsa."
            },
            {
                "Nama": "Luthfia Laila Ramadhani", 
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Kak Luthfia terlihat rapi dalam bekerja dan menyenangkan diajak bicara.",
                "Pesan" : "Semoga kegiatan ke depan berjalan baik, Kak Luthfia."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
 
if menu == "Departemen Internal":
    def departemen_internal():
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
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Way Halim",
                "Hobi": "Ngeledek Orang",
                "Sosmed": "@haikalsbln",
                "Kesan": "Kak Haikal memberi kesan santai dan mudah berbaur.",
                "Pesan": "Semoga Kak Haikal selalu semangat dalam setiap kegiatan."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Suka Nolong Orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Kak Risma tampak sabar saat menjelaskan sesuatu.",
                "Pesan": "Semoga studi dan aktivitas Kak Risma berjalan lancar."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Sumatera Utara, kisaran city",
                "Alamat": "Sukarame",
                "Hobi": "Ngabarin Orang Tua",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kak Hanna terlihat peduli terhadap orang di sekitarnya.",
                "Pesan": "Semoga selalu dalam keadaan sehat dan bahagia, Kak Hanna."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "Kak Farhan tampil mantap dan jelas dalam menyampaikan pendapat.",
                "Pesan": "Sukses selalu untuk Kak Farhan dalam setiap rencana."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Kak Aisyah memberi kesan rapi dan teratur.",
                "Pesan": "Semoga Kak Aisyah selalu dimudahkan dalam perkuliahan."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Kak Cerine tampak tenang dan menguasai bidangnya.",
                "Pesan": "Semoga ilmu Kak Cerine terus bertambah dan bermanfaat."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Kak Jaya terlihat tekun dan bersungguh-sungguh.",
                "Pesan": "Semoga usaha Kak Jaya membuahkan hasil yang baik."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kak Najla tampak ceria dan menyenangkan.",
                "Pesan": "Semoga hari-hari Kak Najla selalu dipenuhi hal baik."
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Kak Rozak memberi kesan tepat waktu dan bisa dipercaya.",
                "Pesan": "Semoga Kak Rozak terus konsisten dalam berkegiatan."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Kak Teresa terlihat berwibawa namun tetap ramah.",
                "Pesan": "Semoga Kak Teresa selalu diberi kelancaran dalam urusannya."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Kak Hanif tampak kalem dan bijaksana dalam bersikap.",
                "Pesan": "Semoga Kak Hanif sukses dalam studi maupun organisasi."
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kak Audina terlihat murah hati dan suka membantu.",
                "Pesan": "Semoga Kak Audina selalu sehat dan penuh semangat."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Kak Cika tampak teratur dalam mengelola waktu.",
                "Pesan": "Semoga semua target Kak Cika tercapai dengan baik."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Kak Gustin memberi saran yang terasa masuk akal dan praktis.",
                "Pesan": "Semoga Kak Gustin selalu lancar dalam setiap langkah."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Kak Harvin terlihat terbuka dan mudah diajak bicara.",
                "Pesan": "Semoga Kak Harvin selalu dalam lindungan kesehatan."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Kak Rafa tampak sederhana dan bersahaja.",
                "Pesan": "Semoga Kak Rafa selalu bahagia dalam menjalani hari."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()
 
if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1GM-VtL2Qdyezmp1SRS4LgKKQ0TtoTJQ8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nV1gtHO66OrLDPV98dD4EpqzO9XEw7OR&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ot3basievMXK8Xm1FbqeAwaWq_He856S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
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
                "NIM" : "123450109",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Panjang, Bandar Lampung",
                "Hobi": "Balap",
                "Umur" : "21",
                "Sosmed" : "@kevinaj__",
                "Kesan" : "Kak Kevin terlihat santai dan mudah beradaptasi.",
                "Pesan" : "Semoga Kak Kevin selalu lancar dalam setiap kesibukan."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika", 
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Kak Ferazka berbicara dengan nada tenang dan teratur.",
                "Pesan" : "Semoga wawasan Kak Ferazka terus bertambah luas."
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi", 
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Kak Ari tampak rendah hati dan tidak banyak menuntut.",
                "Pesan" : "Semoga Kak Ari selalu diberi kemudahan dalam berkegiatan."
            },
            {
                "Nama": "Ayu Andriani Parlina Wati", 
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "Kak Ayu terlihat tekun dan serius dalam bekerja.",
                "Pesan" : "Semoga prestasi Kak Ayu terus meningkat."
            },
            {
                "Nama": "Dafa Elpriza", 
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Kak Dafa tampak akrab dengan teman-teman di sekitarnya.",
                "Pesan" : "Semoga pertemanan Kak Dafa selalu hangat dan awet."
            },
            {
                "Nama": "Juwita Sari", 
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Kak Juwita memberi kesan lembut dan penuh perhatian.",
                "Pesan" : "Semoga Kak Juwita selalu merasa tenang dan bahagia."
            },
            {
                "Nama": "Muhammad Afdal Lutfi", 
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Kak Afdal terlihat bersemangat dan kompak bersama rekan-rekannya.",
                "Pesan" : "Semoga Kak Afdal sukses dalam perkuliahan dan organisasi."
            },
            {
                "Nama": "Salsabila Nazwa Putri", 
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Kak Salsa tampak komunikatif dan enak diajak bertukar pikiran.",
                "Pesan" : "Semoga Kak Salsa selalu sehat dan penuh kebahagiaan."
            },
            {
                "Nama": "Muhammad Ridwan", 
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Kak Ridwan memberi kesan bertanggung jawab dan dapat diandalkan.",
                "Pesan" : "Semoga Kak Ridwan selalu dipermudah dalam segala hal."
            },
            {
                "Nama": "Andra Ilham Bintang", 
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Kak Andra terlihat teliti dan hati-hati dalam bekerja.",
                "Pesan" : "Semoga Kak Andra terus berkembang dan sukses."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua", 
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Kak Bryan tampak percaya diri dan pandai mencairkan suasana.",
                "Pesan" : "Semoga Kak Bryan selalu sukses dalam berkarya."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy", 
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Kak Ghiyats terlihat dermawan dan bersahabat.",
                "Pesan" : "Semoga segala kebaikan Kak Ghiyats mendapat balasan yang baik."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi", 
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "20",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Kak Indah memberi kesan tenang dan bersahaja.",
                "Pesan" : "Semoga Kak Indah selalu nyaman menjalani harinya."
            },
            {
                "Nama": "Jacinda Kesya Alvara", 
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Kak Jacinda tampak periang dan punya gaya bercanda yang khas.",
                "Pesan" : "Semoga Kak Jacinda selalu penuh energi positif."
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan", 
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Kak Rafka terlihat disiplin dan teratur dalam keseharian.",
                "Pesan" : "Semoga Kak Rafka terus konsisten meraih tujuannya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=16P86_3b1BGi795QjCOYe7Pxx-IXf4NWG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ApVfZHU1uKwIeLg4ESE1tT6rwLsdVD_S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1HSCttv3HmuJksHcnRhIVrnqPEbORyhs7&sz=w1000",
                "https://drive.google.com/thumbnail?id=13PhRuKFECXCiFdsmkjqVsq5vdUFK1FAM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1AGZYk0N9S2CX5ePXOuWSeDL79BKKULu0&sz=w1000",
                "https://drive.google.com/thumbnail?id=10uEeF6GAlRLMOOg6BKoR4Blgw8W_u2mx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Fc00WIJRsC8Sq9XwxyyuswAX9_beA1uY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ptKTOQCEu95YXsTirrHdKaPYyaOVEKX5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-5WKONIO-nxtMzvp5t31a-0OEr-0TFCh&sz=w1000",
                "https://drive.google.com/thumbnail?id=16Q6aca9jbwYJUQPB2RSycec8hQu56ujn&sz=w1000",
                "https://drive.google.com/thumbnail?id=111rMcaXkulz5vel0B6O433A4T9Tyo6yX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1b5V7IWpfjuhqtDSv5QWmZQCNGL89Ia1p&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hrxjgJ1e8jodtHrsCREr2Y6L3l8lm3ns&sz=w1000",
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
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Kak Fabio terlihat santai dan tidak suka memperumit keadaan.",
                "Pesan" : "Semoga Kak Fabio selalu lancar dalam setiap urusan."
            },
            {
                "Nama": "Tanty Widiyastuti", 
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Kak Tanty tampak cermat dan memperhatikan detail.",
                "Pesan" : "Semoga Kak Tanty terus berhasil dalam studinya."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi", 
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Kak Fadil memberi kesan hangat dan menyukai musik.",
                "Pesan" : "Semoga bakat bermusik Kak Fadil semakin terasah."
            },
            {
                "Nama": "Manuel Frederika", 
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Kak Manuel tampak aktif dan mudah bergaul.",
                "Pesan" : "Semoga Kak Manuel selalu sehat dan bersemangat."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri", 
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Kak Viola terlihat tenang dan memiliki banyak gagasan.",
                "Pesan" : "Semoga setiap ide Kak Viola dapat terwujud."
            },
            {
                "Nama": "Risa Romadona", 
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Kak Risa tampak gesit dan senang mencoba hal baru.",
                "Pesan" : "Semoga Kak Risa selalu mendapat pengalaman yang menyenangkan."
            },
            {
                "Nama": "Vannisa Ramadhani", 
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Kak Vannisa terlihat bersahabat dan murah senyum.",
                "Pesan" : "Semoga hari-hari Kak Vannisa selalu menyenangkan."
            },
            {
                "Nama": "Yulia Cristine Malau", 
                "NIM" : "124450119",
                "Asal" : "Jambi",
                "Alamat" : "Sabah Balau",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@krnylee",
                "Kesan" : "Kak Yulia memberi kesan santun dan menghargai orang lain.",
                "Pesan" : "Semoga Kak Yulia selalu berhasil dalam setiap kegiatan."
            },
            {
                "Nama": "Akeyla Fairuz Shafi", 
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Kak Akeyla tampak pandai mendengarkan dan tidak menghakimi.",
                "Pesan" : "Semoga Kak Akeyla selalu dikelilingi orang-orang baik."
            },
            {
                "Nama": "Elsa Sitorus", 
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "@_els.a",
                "Kesan" : "Kak Elsa terlihat ramah dan nyaman diajak mengobrol.",
                "Pesan" : "Semoga Kak Elsa selalu sehat dan sukses."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini", 
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Kak Fadya tampak telaten dan runtut saat menerangkan.",
                "Pesan" : "Semoga ilmu yang Kak Fadya bagikan terus bermanfaat."
            },
            {
                "Nama": "Lovianora Saragih", 
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kak Lovia memberi kesan kalem namun tetap bersahabat.",
                "Pesan" : "Semoga perkuliahan Kak Lovia berjalan dengan baik."
            },
            {
                "Nama": "M. Alsi Syahrulloh", 
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Kak Alsi terlihat humoris dan suka bercanda.",
                "Pesan" : "Semoga Kak Alsi selalu bisa menyeimbangkan waktu dengan baik."
            },
            {
                "Nama": "Sherena Florencia", 
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "@sher_renna",
                "Kesan" : "Kak Sherena tampak percaya diri dan selalu rapi.",
                "Pesan" : "Semoga Kak Sherena terus berkembang di banyak bidang."
            },
            {
                "Nama": "Razin Hafid Hamdi", 
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Kak Razin terlihat sportif dan senang bekerja sama.",
                "Pesan" : "Semoga Kak Razin selalu kompak bersama timnya."
            },
            {
                "Nama": "Faiza Try Anjani", 
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "@Faizaanjanii",
                "Kesan" : "Kak Faiza tampak sopan dan berhati-hati dalam berbicara.",
                "Pesan" : "Semoga Kak Faiza selalu mendapat kemudahan."
            },
            {
                "Nama": "Gathfan Nadif Ali", 
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Kak Gathfan memberi kesan tenang dan bisa dipercaya.",
                "Pesan" : "Semoga Kak Gathfan selalu berhasil dalam rencananya."
            },
            {
                "Nama": "Hafidz Wahdiansyah", 
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Kak Hafidz terlihat menguasai hal teknis dan terbuka berbagi ilmu.",
                "Pesan" : "Semoga kemampuan Kak Hafidz terus meningkat."
            },
            {
                "Nama": "Kaleb Filbert Istel", 
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Kak Kaleb tampak disiplin menjaga kebugaran.",
                "Pesan" : "Semoga Kak Kaleb selalu bugar dan produktif."
            },
            {
                "Nama": "Melva Shaprina Febrianti", 
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Kak Melva terlihat ceria dan cepat menyesuaikan diri.",
                "Pesan" : "Semoga Kak Melva selalu bahagia dalam menjalani kuliah."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh", 
                "NIM" : "124450099",
                "Asal" : "Lampung Utara",
                "Alamat" : "Asrama TB 3",
                "Hobi": "Membaca",
                "Umur" : "20",
                "Sosmed" : "@syafiqui",
                "Kesan" : "Kak Syafiq tampak pendiam namun dapat diandalkan.",
                "Pesan" : "Semoga Kak Syafiq selalu dimudahkan dalam banyak hal."
            },
            {
                "Nama": "Rifky Henry Ferdianto", 
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "@henryferdianto",
                "Kesan" : "Kak Henry memberi kesan humoris dan berpengalaman.",
                "Pesan" : "Semoga Kak Henry selalu sukses dan sehat."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()
 
if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1x1hLuPtCKIwTvgQG_fkkO7vf2x2cLqpT&sz=w1000",
                "https://drive.google.com/thumbnail?id=10RWPKhkBKiirokfLoNxM92O-czKhzHFQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1r5iJQsAQncMfrew5YxcJYQpy_ntWFUU7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1V2t2fIwbflskLizpws3qx1kHXUhXGM9x&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WAJzA67gnduohGkcXS9fIH3pZT28xkvy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OszSPqnR1q74WCKt9tQ7P5ueE1DVA8Jq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1cPe0ha0hV94i7ZeZxG0C5_nRJYn3lVPi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1I76gzPz2Ga1V7NOOnZ8EIgHim-Kc8jZO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FTiPunTf8FD4miHXtpVSLawsLecBM6Fl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1JJwIUwPWE119qVk9eouzd7VtEvAzAzfV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pID23OW9ehUIfQy4_wGv98EFJ_-Gqwc3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mZvHJirrl8nu4RHC1FWbFWo1aWRMqkay&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QuklkKtVeoHUv2UGX_dHXfVZtjas5EOd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1k2kqP-1QKMk_2_CkXC9L9-in4-be1P5N&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ahsbMqF9Ey9NbSCMkS9Cc8imvS5nMSuL&sz=w1000",
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
                "Kesan" : "Kak Nayla tampak lembut dalam bertutur kata.",
                "Pesan" : "Semoga Kak Nayla selalu sehat dan lancar dalam kegiatan."
            },
            {
                "Nama": "Donna Maya Puspita", 
                "NIM" : "123450028",
                "Asal" : "Bekasi",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Kak Donna terlihat tulus dan pandai mendengarkan.",
                "Pesan" : "Semoga Kak Donna selalu dikelilingi hal-hal baik."
            },
            {
                "Nama": "Labo John Nuel Napitupulu", 
                "NIM" : "123450037",
                "Asal" : "Medan",
                "Alamat" : "Belwis",
                "Hobi": "Motoran",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Kak Labo memberi kesan berpengalaman dan suka bercerita.",
                "Pesan" : "Semoga perjalanan Kak Labo selalu aman dan menyenangkan."
            },
            {
                "Nama": "Anash Tasya Ausyaqila", 
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Way Halim",
                "Hobi": "Nonton",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Kak Anash tampak fokus dan konsisten dalam mengerjakan tugas.",
                "Pesan" : "Semoga Kak Anash terus berhasil dalam studinya."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho", 
                "NIM" : "124450104",
                "Asal" : "Lampung Timur",
                "Alamat" : "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur" : "19",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Kak Felisya terlihat enerjik dan menghidupkan suasana.",
                "Pesan" : "Semoga Kak Felisya selalu ceria setiap hari."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama", 
                "NIM" : "124450031",
                "Asal" : "Jawa Barat",
                "Alamat" : "Korpri",
                "Hobi": "Foto Orang",
                "Umur" : "21",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Kak Razan tampak akrab dengan siapa saja namun tetap sopan.",
                "Pesan" : "Semoga karya fotografi Kak Razan semakin bagus."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari", 
                "NIM" : "123450086",
                "Asal" : "Karawang",
                "Alamat" : "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Kak Sania memberi kesan gigih dan pantang menyerah.",
                "Pesan" : "Semoga tugas akhir Kak Sania dapat selesai dengan baik."
            },
            {
                "Nama": "Allisha", 
                "NIM" : "124450019",
                "Asal" : "Kayangan",
                "Alamat" : "Heaven",
                "Hobi": "Mancing",
                "Umur" : "16",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Kak Allisha terlihat setia kawan dan mudah akrab.",
                "Pesan" : "Semoga Kak Allisha selalu bahagia bersama teman-temannya."
            },
            {
                "Nama": "Alya Ramadhanti", 
                "NIM" : "124450091",
                "Asal" : "Jambi",
                "Alamat" : "Airan",
                "Hobi": "Jalan-jalan",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Kak Alya tampak luwes dan terbuka pada pengalaman baru.",
                "Pesan" : "Semoga Kak Alya terus menemukan hal-hal menarik."
            },
            {
                "Nama": "Bunga Clarisa Sefa", 
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Kak Bunga terlihat tekun dan rajin menuntut ilmu.",
                "Pesan" : "Semoga nilai dan prestasi Kak Bunga selalu baik."
            },
            {
                "Nama": "Difanya Husakina", 
                "NIM" : "124450043",
                "Asal" : "Pagar Alam",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Kak Difanya memberi kesan santun dan menenangkan.",
                "Pesan" : "Semoga Kak Difanya selalu diberi ketenangan hati."
            },
            {
                "Nama": "Nazlah Auliya", 
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Berenang",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Kak Nazlah tampak percaya diri dan elegan.",
                "Pesan" : "Semoga Kak Nazlah selalu sehat dan aktif berolahraga."
            },
            {
                "Nama": "Raihana Adelia Putri", 
                "NIM" : "123450041",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur" : "20",
                "Sosmed" : "@r.hanaap",
                "Kesan" : "Kak Raihana terlihat kalem dan pandai menyusun kata.",
                "Pesan" : "Semoga tulisan-tulisan Kak Raihana terus berkembang."
            },
            {
                "Nama": "Daffa Kharisma Adzana", 
                "NIM" : "124450061",
                "Asal" : "Surabaya",
                "Alamat" : "Sukarame",
                "Hobi": "-",
                "Umur" : "21",
                "Sosmed" : "@daffascript",
                "Kesan" : "Kak Daffa tampak pendiam namun tulus dalam bersikap.",
                "Pesan" : "Semoga Kak Daffa selalu lancar dalam aktivitasnya."
            },
            {
                "Nama": "Edsel Adya Pradipta", 
                "NIM" : "124450098",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Natar",
                "Hobi": "Nonton Anime",
                "Umur" : "20",
                "Sosmed" : "@edsel_0712",
                "Kesan" : "Kak Edsel memberi kesan santai dan humoris.",
                "Pesan" : "Semoga Kak Edsel selalu sukses dan bahagia."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan", 
                "NIM" : "124450085",
                "Asal" : "Bekasi",
                "Alamat" : "Belwis",
                "Hobi": "Tidur",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Kak Lucia terlihat bersemangat dan suka memotivasi.",
                "Pesan" : "Semoga Kak Lucia selalu diberi energi yang cukup."
            },
            {
                "Nama": "Shafa Delaila Azzahra", 
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Kak Shafa tampak natural dan membuat suasana santai.",
                "Pesan" : "Semoga karya-karya Kak Shafa makin dikenal banyak orang."
            },
            {
                "Nama": "Zannuba Arifah Ilman", 
                "NIM" : "124450112",
                "Asal" : "Lampung Timur",
                "Alamat" : "Rajabasa",
                "Hobi": "Begong",
                "Umur" : "18",
                "Sosmed" : "@xifasky",
                "Kesan" : "Kak Zannuba terlihat sopan dan menghormati sesama.",
                "Pesan" : "Semoga Kak Zannuba selalu mendapat banyak kemudahan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()
 
if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=11KYwjNEZ2-TLqdzcxmZ0kiJ3MlMsuOPB&sz=w1000",
                "https://drive.google.com/thumbnail?id=17t4aM6qCY0fQVbmXCjUncqxxn1OVtbHW&sz=w1000",
                "https://drive.google.com/thumbnail?id=11HoRl3CELH5X3-ZIwnzTZfb6LHBIQmrh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aZ3tgcZSZ62vtI0zXCazAB0KubIsHmuU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1IJN8KuBzR6AEVMRkz8kh4phzwYWdQx9B&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bw3qZmk6GyWLzYG7BL44Dt0DzSsW0I1s&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lGcJvKfet64hQCiEjMd5CSxj0lBBTqVs&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vAr6_1YCy_InKYcQKs0JZbl2NBJ4q64A&sz=w1000",
                "https://drive.google.com/thumbnail?id=1P5jvgHtbO-5uttv_Fl8L0mBvKl7XXEoZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wsvp4zjuBrbl_SX3IFNuSEp31c-vEe6W&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Jb9Hd25msu6E-FHAqCVuGCxTnkDMo7MI&sz=w1000",
                "https://drive.google.com/thumbnail?id=1l8ipVbREFmESgEPSXtApszWP54w1Zhvm&sz=w1000",
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
                "Kesan": "Kak Ihsan terlihat santai namun serius dalam hal akademik.",
                "Pesan": "Semoga riset dan studi Kak Ihsan berjalan lancar."

            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kak Hanifah tampak ramah dan menyenangkan diajak berbincang.",
                "Pesan": "Semoga Kak Hanifah selalu sehat dan penuh semangat."    
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kak Afifah memberi kesan menyenangkan dan mudah diajak bicara.",
                "Pesan": "Semoga Kak Afifah selalu lancar dalam perkuliahan." 
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Kak Hasan tampak tenang dan cakap dalam bidang teknis.",
                "Pesan": "Semoga proyek-proyek Kak Hasan selalu berjalan mulus."
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kak Layina terlihat pekerja keras dan menyenangkan.",
                "Pesan": "Semoga usaha Kak Layina membuahkan hasil yang baik."
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Kak Iqbal tampak bersahabat dan mudah akrab.",
                "Pesan": "Semoga Kak Iqbal selalu sehat dan sukses kuliahnya."
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Kak Talitha memberi kesan kalem dan nyaman.",
                "Pesan": "Semoga Kak Talitha selalu dalam keadaan prima."
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kak Anadia terlihat ceria dan rajin dalam bekerja.",
                "Pesan": "Semoga kegiatan Kak Anadia berjalan lancar terus."
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "Kak Fikri tampak lincah dan sportif.",
                "Pesan": "Semoga Kak Fikri selalu bugar dan berprestasi."
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Kak Afdhal terlihat sabar dan nyaman diajak bertukar cerita.",
                "Pesan": "Semoga Kak Afdhal selalu diberi kelancaran dalam studinya."
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kak Anggun memberi kesan hangat dan periang.",
                "Pesan": "Semoga Kak Anggun selalu bahagia dalam keseharian."
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Kak Della tampak ramah dan menyenangkan.",
                "Pesan": "Semoga Kak Della selalu mendapat hal-hal baik."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1cH6HWBi6LINpxWdR_zyXPZ1gx8MOJQT6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Zlt7nV3ukvAvOo0tCcRa2Dsx4fuk7FMC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rJN1ReS6OE58DACRNmmKkg_E-gZ21sgA&sz=w1000",
                "https://drive.google.com/thumbnail?id=12SeDzsbYiz_40qI_myUv8VTmeKRL0NY_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1W0FFc0jgixY0FmIQB5cxmznRdb3B_Fkq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=16xETWBD19ihjo-hu9T2LaBGByuJc3TtS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QoTwpr-b829A755pemu_wjrbmUi6-A1A&sz=w1000",
                "https://drive.google.com/thumbnail?id=14UtVjTBVS81JoIXY1LZRi4HBO_QwDWst&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Nusle46g_t1AP1aCWur3Rw9i9EWy18x2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XN0_JdMGOc5XpHqB66qQGf_uY0fC5DBa&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lkRJisyHe-RcYU2NQj9nKkIDb2m3MObI&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
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
                "Kesan": "Kak Arini tampak bersahabat dan nyaman diajak bicara.",
                "Pesan": "Semoga Kak Arini selalu sehat dan berkecukupan waktu istirahat."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Kak Nabyla terlihat riang dan mudah bergaul.",
                "Pesan": "Semoga Kak Nabyla sukses dalam kuliah dan kegiatan lainnya."
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Kak Khoirul memberi kesan santai dan terbuka.",
                "Pesan": "Semoga Kak Khoirul selalu lancar dalam setiap urusan."
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Kak Rizky tampak tenang dan tidak berlebihan.",
                "Pesan": "Semoga Kak Rizky selalu diberi kemudahan dalam berproses."
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Kak Adinda terlihat percaya diri dan penuh antusias.",
                "Pesan": "Semoga Kak Adinda terus berkarya dan berprestasi."
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Kak Bimo tampak santai dan menyenangkan.",
                "Pesan": "Semoga cita-cita Kak Bimo segera tercapai."
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Kak Alfaya memberi kesan riang dan bersahabat.",
                "Pesan": "Semoga Kak Alfaya selalu menjaga kesehatan dengan baik."
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kak Asri terlihat kalem dan nyaman diajak berbincang.",
                "Pesan": "Semoga Kak Asri selalu berhasil dalam kegiatannya."
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Kak Bima tampak humoris dan mudah akrab.",
                "Pesan": "Semoga Kak Bima selalu bersemangat dalam menjalani hari."
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Kak Indah terlihat unik dan punya banyak cerita.",
                "Pesan": "Semoga Kak Indah selalu mendapat pengalaman yang berharga."
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Kak Riska memberi kesan cermat dan dapat dipercaya.",
                "Pesan": "Semoga semua pekerjaan Kak Riska berjalan lancar."
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Kak Yollanda tampak terbuka dan mudah didekati.",
                "Pesan": "Semoga Kak Yollanda selalu sukses dalam berbagai hal."
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Kak Aditya terlihat aktif dan membuat suasana lebih hidup.",
                "Pesan": "Semoga Kak Aditya selalu diberi kelancaran dan kesehatan."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kak Fathya tampak tenang dan menyenangkan.",
                "Pesan": "Semoga Kak Fathya selalu bahagia dalam menjalani hari."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Kak Tarisya memberi kesan baik hati dan bersahaja.",
                "Pesan": "Semoga Kak Tarisya selalu dikelilingi orang-orang baik."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Kak Ashila tampak kalem dan menyenangkan.",
                "Pesan": "Semoga Kak Ashila selalu dalam kondisi sehat."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Kak Dasil terlihat sabar dan penuh ketelatenan.",
                "Pesan": "Semoga Kak Dasil selalu berhasil dalam kegiatannya."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Kak Favian tampak mudah bergaul dan bersahabat.",
                "Pesan": "Semoga Kak Favian selalu lancar menjalani perkuliahan."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Kak Fathiy memberi kesan kreatif dan punya sudut pandang sendiri.",
                "Pesan": "Semoga Kak Fathiy segera menemukan kegiatan yang disukai."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Kak Rizaldi terlihat santai dan suka bercanda.",
                "Pesan": "Semoga Kak Rizaldi selalu sukses dalam berbagai hal."
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Kak Saskia tampak ramah dan asyik diajak berbincang.",
                "Pesan": "Semoga Kak Saskia selalu mendapat hari-hari yang menyenangkan."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Kak Selma terlihat hangat dan bersahabat.",
                "Pesan": "Semoga Kak Selma selalu diberi kemudahan di setiap perjalanan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=15dJ84cv73-6d_uz_b0chVx5zwj1obzsV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mdLw0ZyRIeOdUJpFGhGaHpRPsTJCzh3y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Bklf6QcW5ZGGJErRxDhutxVBnIGMcaFB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Nf4E3YCwDDuLi-UCgpj80GtptMTSJBcW&sz=w1000",
                "https://drive.google.com/thumbnail?id=10DXkTMJfCpyqXQtF3GsbgBbHQARyNKeM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=19tjC52KV-Sol0FRdHB5hdzQ-1zYKRQ98&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qhOIdS0QOk8X8IaUjPjccZeEZKoHabkt&sz=w1000",
                "https://drive.google.com/thumbnail?id=1n6KpN22NRnarO3j7KPeWvj1HXQEsGdxq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WGINm2kERt3LZlhIs4-t3rKeLS_Mi7gJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EDpWd8WEsKhxJQcqcV0dutsDK0G9WUUM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DbZ8EybZ8CR7bKfWRha_KsPzK1Y01DWF&sz=w1000",
                "https://drive.google.com/thumbnail?id=15PKXeWQgvxpotNgnyuJ1jK4whE42kM61&sz=w1000",
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
                "Kesan": "Kak Ridho tampak kalem dan rajin.",
                "Pesan": "Semoga Kak Ridho selalu dimudahkan dalam setiap kegiatan."
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Kak Juessi terlihat menyukai musik dan enak diajak bertukar cerita.",
                "Pesan": "Semoga Kak Juessi selalu lancar dalam studi dan kegiatan."
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Kak Dharu memberi kesan ramah dan punya minat yang unik.",
                "Pesan": "Semoga Kak Dharu selalu sukses dalam perkuliahan."
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "Kak Mikael tampak santai dan menyenangkan untuk diajak bermain.",
                "Pesan": "Semoga Kak Mikael selalu bersemangat dalam setiap hal."
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "Kak Siti terlihat periang dan punya hobi yang menarik.",
                "Pesan": "Semoga koleksi Kak Siti terus bertambah."
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Kak Givaro tampak santai dan asyik diajak bercengkerama.",
                "Pesan": "Semoga Kak Givaro selalu sehat dan lancar kuliahnya."
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Kak Afghanis memberi kesan mudah bergaul dan hangat.",
                "Pesan": "Semoga persahabatan Kak Afghanis selalu terjaga."
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Kak Hani terlihat ramah dan punya banyak topik pembicaraan.",
                "Pesan": "Semoga Kak Hani selalu diberi kesehatan dan kemudahan."
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Kak Jeremia tampak bersahabat dan menyenangkan.",
                "Pesan": "Semoga bakat dan kesehatan Kak Jeremia selalu terjaga."
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "Kak Monica terlihat telaten dan hangat.",
                "Pesan": "Semoga karya rajutan Kak Monica semakin indah."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Kak Jona memberi kesan tertib dan punya ketertarikan khusus.",
                "Pesan": "Semoga Kak Jona selalu sehat dan koleksinya terus bertambah."
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Kak Sekar tampak tenang dan nyaman diajak berbicara.",
                "Pesan": "Semoga Kak Sekar selalu merasa damai dan bahagia."
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "Kak Nashwa terlihat unik dan menyenangkan dalam bercerita.",
                "Pesan": "Semoga Kak Nashwa selalu lancar di masa mendatang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1nxQ2kvYYqK-lrTdtRuLf3-DhKAXjnYGY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1orfIakChkVYPdQ7V4Un3XdjuiE7Jy7QJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zZgLbV1_zhgWmi045Rw9S-UdzahsNYuj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Er_w6kEUiNZqsg7FwjvvoVOcwYz7upXu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1O0VSAFcT-R4N1oeVpBYEV6KTY4ysh_sH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uSpKXUiqCwku8Zxq3eJqA1NX51_oJ8pK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F3lM6YxR9zxLMJDeJ4q8we3ApY3PGp0p&sz=w1000",
                "https://drive.google.com/thumbnail?id=1W2wkUgv_AJlwugH9wukVhI1fB-rQtrej&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WeOPBc7at8rlnRr7vLlD3vtAK9_cZlOH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1llY4OlJU3ooJOvOJUjLngOQ1v3IgAwJr&sz=w1000",
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
                "Kesan": "Kak Fathinah tampak ramah dan gemar menuangkan ide lewat tulisan.",
                "Pesan": "Semoga tulisan Kak Fathinah terus berkembang dan dibaca banyak orang."
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Kak Helmy memberi kesan santai dan mudah akrab.",
                "Pesan": "Semoga Kak Helmy selalu lancar dalam studinya."
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Kak Fernando terlihat aktif dan sportif.",
                "Pesan": "Semoga Kak Fernando selalu bugar dan berprestasi."
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia___",
                "Kesan": "Kak Suci tampak periang dan nyaman diajak mengobrol.",
                "Pesan": "Semoga Kak Suci selalu mendapat banyak kebahagiaan."
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Kak Wielman terlihat bersahaja dan mudah bergaul.",
                "Pesan": "Semoga Kak Wielman selalu sehat dan sukses kuliahnya."
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Kak Lia tampak ramah kepada siapa pun.",
                "Pesan": "Semoga Kak Lia selalu diberi kelancaran dalam berkegiatan."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kak Aqila memberi kesan teliti dan menyenangkan.",
                "Pesan": "Semoga pekerjaan Kak Aqila selalu berjalan rapi dan lancar."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Kak Hazel terlihat unik dan punya banyak pengalaman menarik.",
                "Pesan": "Semoga Kak Hazel selalu berhasil dalam segala rencana."
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kak Nadya tampak tenang dan enak diajak berbincang.",
                "Pesan": "Semoga Kak Nadya selalu mendapat hari yang menyenangkan."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kak Dwi memberi kesan kalem dan punya banyak bahan obrolan.",
                "Pesan": "Semoga Kak Dwi selalu sukses dalam belajar dan berkegiatan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1RI-nHdjDQveH0Q5jRvOLfht4V2bq2GMs&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1a4IhWvGMzXOAzIeS7UctGFF9eYvp4IxE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1w0zezSGs7Rzf2kIMduNgrpZFRWdX61cx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qUklr_XocprShFTLXhuNNNRTc5RhRu4S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uQwqbiwwgbjnZrsvg-rKFbl63YB8cWCM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Std-1C57mHXbEiQfcKn7qW59nyonbE3B&sz=w1000",
                "https://drive.google.com/thumbnail?id=1gCtrF5sY4ceKk4sy9ZwfUIdKjFVu_8ke&sz=w1000",
                "https://drive.google.com/thumbnail?id=1a30xKaIlpjybeZDqVtB1GUutGynrPnNt&sz=w1000",
                "https://drive.google.com/thumbnail?id=12AoJUae7XBFeEwRUgFdP3PfWQyaW8NyN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1018VDldSyQCxbd7AFoae0F-pP9wdGTFA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1p9AdYKD3srbVG1RBQcx_jqXg_us7zt28&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1knZqEDmPbYsaKdZE8HGthumVjIIb0OQx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DtKGQRBtgVrhNHZe0O9vs0R2qFQz0mSv&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ItY4-aQt4HxW3Eq-r-R1lg0mT1dsKIQm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KlX1H2-rb-7MUASxxojfz-upbQ3mQQq-&sz=w1000",
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
                "Kesan": "Kak Arienta terlihat supel dan mudah akrab.",
                "Pesan": "Semoga Kak Arienta selalu lancar dan sehat dalam kuliah."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Kak Vany tampak tenang dan nyaman diajak berbicara.",
                "Pesan": "Semoga setiap urusan Kak Vany berjalan dengan baik."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "-",
                "Sosmed": "@nobelnizam",
                "Kesan": "Kak Nobel memberi kesan sopan dan kalem.",
                "Pesan": "Semoga Kak Nobel selalu konsisten dalam belajar."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "Kak Afriza tampak santai dan menyenangkan.",
                "Pesan": "Semoga Kak Afriza selalu bersemangat menjalani hari."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Kak Ayake terlihat mudah bergaul dengan banyak orang.",
                "Pesan": "Semoga Kak Ayake selalu dimudahkan dalam kuliahnya."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Kak Caesar memberi kesan santai dan enak diajak mengobrol.",
                "Pesan": "Semoga Kak Caesar selalu mendapat waktu istirahat yang cukup."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Kak Euodia tampak aktif dan penuh antusias.",
                "Pesan": "Semoga Kak Euodia terus berkembang dan meraih keberhasilan."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Kak Haikal terlihat dewasa dan dapat dipercaya.",
                "Pesan": "Semoga Kak Haikal selalu sehat dan lancar dalam kegiatan."
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450065",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Nomandenl",
                "Hobi": "Mancing emosi",
                "Sosmed": "@putrimannaa",
                "Kesan": "Kak Putri tampak ceria dan menyenangkan diajak bercanda.",
                "Pesan": "Semoga Kak Putri selalu positif dalam menjalani studi."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Kak Queenta memberi kesan hangat dan perhatian.",
                "Pesan": "Semoga seluruh rencana Kak Queenta berjalan baik."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Kak Desman terlihat humoris dan pandai mencairkan suasana.",
                "Pesan": "Semoga Kak Desman selalu rendah hati dan sukses."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Kak Azzelya tampak teratur dan peduli pada kesehatan.",
                "Pesan": "Semoga Kak Azzelya selalu bugar dan konsisten."
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Kak Charrlindah terlihat gigih dan penuh tanggung jawab.",
                "Pesan": "Semoga Kak Charrlindah selalu punya waktu untuk beristirahat."
            },
            {
                "Nama": "Jeremi Marolop Partogi Situmorang",
                "NIM": "124450111",
                "Umur": "16",
                "Asal": "Berlin",
                "Alamat": "Samping kos Rafli",
                "Hobi": "Mengembala anak ayam",
                "Sosmed": "@jemarrro",
                "Kesan": "Kak Jeremi tampak santai dan mudah berbaur.",
                "Pesan": "Semoga Kak Jeremi selalu mendapat pengalaman belajar yang baik."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Kak Nabila terlihat ramah dan mudah diajak berteman.",
                "Pesan": "Semoga Kak Nabila selalu sehat dan lancar dalam kuliah."
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "20",
                "Asal": "Sibolga",
                "Alamat": "Samping kos Haikal",
                "Hobi": "Nonton",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Kak Rafli memberi kesan kalem dan bersahabat.",
                "Pesan": "Semoga Kak Rafli selalu berhasil dalam kegiatannya."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "Kak Salavi tampak sederhana dan tenang.",
                "Pesan": "Semoga Kak Salavi selalu sehat dan bahagia."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()