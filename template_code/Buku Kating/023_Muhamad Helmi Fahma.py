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
                "https://drive.google.com/thumbnail?id=1ButGdz7A7wKzxbswVLp9YXOhtBVB2Ivk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1t0cY4HTmKfp-JXXV--n960aFcosM0hFM&sz=w1000",
                "https://drive.google.com/thumbnail?id=187T0pM3_ETe0b3HW6LrQNGzrWUYyng0w&sz=w1000"
        ]
        data_list = [
        {
            "Nama": "Ginda Fajar Riadi Marpaung",
            "NIM": "123450103",
            "Asal": "Belum Tahu",
            "Alamat": "Belum Tahu",
            "Hobi": "Belum Tahu",
            "Umur": "Belum Tahu",
            "Sosmed": "Belum Tahu",
            "Kesan": "Sangat misterius namun selalu membuat penasaran dengan pemikirannya.",
            "Pesan": "Semoga bisa lebih sering berbagi cerita dan berkenalan lebih dekat ke depannya."
        },
        {
            "Nama": "Muhammad Aqil Ramadhan",
            "NIM": "123450066",
            "Asal": "Riau",
            "Alamat": "Kotabaru",
            "Hobi": "Dzikir",
            "Umur": "22",
            "Sosmed": "@Muhammadaqil1111",
            "Kesan": "Aura tenang dan sikap dewasa Kak Aqil selalu berhasil bikin suasana diskusi jadi sejuk.",
            "Pesan": "Tetap konsisten memberikan pembawaan positif dan bimbingan untuk kami semua, Kak."
        },
        {
            "Nama": "Efi Defiyati",
            "NIM": "123450005",
            "Asal": "Lampung Timur",
            "Alamat": "Airan",
            "Hobi": "Membaca",
            "Umur": "21",
            "Sosmed": "@eeffiidefi",
            "Kesan": "Kak Efi orangnya sangat rapi, teliti, dan selalu sigap kalau diajak koordinasi.",
            "Pesan": "Jaga kesehatan di tengah kesibukan kesekjenan ya Kak, jangan lupa luangkan waktu buat hobi membaca."
        },
        {
            "Nama": "Qois Olifio",
            "NIM": "123450067",
            "Asal": "Batam",
            "Alamat": "Kotabaru",
            "Hobi": "Mainin surat",
            "Umur": "22",
            "Sosmed": "@qoisolifio_",
            "Kesan": "Karakternya santai dan humoris, tapi pengetahuannya luas banget saat bicara hal serius.",
            "Pesan": "Semoga makin sukses dan terus jadi sosok penengah yang menyenangkan di tiap kesempatan."
        },
        {
            "Nama": "Hafsa Fazilah Arradhi",
            "NIM": "123450079",
            "Asal": "Bandar Lampung",
            "Alamat": "Bandar Lampung",
            "Hobi": "Bertemu luluk",
            "Umur": "21",
            "Sosmed": "@hafsafazilahh",
            "Kesan": "Sikapnya ramah, mudah bergaul, dan selalu membawa energi ceria pas ketemu.",
            "Pesan": "Tetap pertahankan senyum manis dan keceriaannya ya Kak, sukses terus untuk semua rencananya!"
        },
        {
            "Nama": "Luthfia Laila Ramadhani",
            "NIM": "123450004",
            "Asal": "Bengkulu",
            "Alamat": "Airan",
            "Hobi": "Keliling Balam",
            "Umur": "20",
            "Sosmed": "@luthhifiarmdhni",
            "Kesan": "Sangat cekatan, punya inisiatif tinggi, dan selalu asyik kalau diajak ngobrol santai.",
            "Pesan": "Semoga makin betah eksplor Bandar Lampung dan terus semangat dalam mengemban amanah di kesekjenan."
        }
    ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# INTERNAL
if menu == "Departemen Internal":

    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1g9EZgNq_N3c4nnKBUlLP3VHE6QWqHbz_&sz=w1000",
            "https://drive.google.com/thumbnail?id=1y2-dlyPsQrRMO7ZOXk-Bn5BQlCNHF0fZ&sz=w1000",
        ]

        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": (
                    "Sosok yang mudah mencairkan suasana dengan candaannya yang"
                    " spontan dan menghibur."
                ),
                "pesan": (
                    "Terus bawa keceriaan di mana pun berada, tapi jangan lupa"
                    " jaga kesehatan ya, Bang."
                ),
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": (
                    "Pembawaannya sangat tenang, tutur katanya santun namun"
                    " tetap punya ketegasan yang jelas."
                ),
                "pesan": (
                    "Tetap sabar dan jangan lelah untuk terus menjadi"
                    " penyemangat buat kami adik tingkatnya."
                ),
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": (
                    "Sangat perhatian dan selalu peka saat melihat orang lain"
                    " butuh bantuan atau arahan."
                ),
                "pesan": (
                    "Kebaikan dan kepedulian Kakak sangat berarti, semoga"
                    " sukses dan lancar terus untuk kuliahnya!"
                ),
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Supporteran",
                "sosmed": "@farhanghani",
                "kesan": (
                    "Memiliki jiwa kepemimpinan yang kuat dan selalu penuh"
                    " energi serta loyalitas tinggi."
                ),
                "pesan": (
                    "Semangat supporterannya terus ditularkan ya Bang, dan"
                    " tetap jadi pemimpin yang bijak."
                ),
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Indragiri",
                "alamat": "Samping Makam Perwira 2",
                "hobbi": "Nyicipin Makanan",
                "sosmed": "@aisyahkhair._",
                "kesan": (
                    "Selalu tampil rapi, ceria, dan membawa aura positif"
                    " setiap kali bertemu."
                ),
                "pesan": (
                    "Tetap semangat eksplor kuliner baru dan selalu jadi"
                    " pribadi yang menyenangkan!"
                ),
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Suka Ngoding pakai R",
                "sosmed": "@cerine_ipynb",
                "kesan": (
                    "Kritis dan sangat mahir dalam problem solving, bikin"
                    " kagum kalau lagi bahas project."
                ),
                "pesan": (
                    "Jangan lupa istirahat di tengah kesibukan ngoding R-nya ya"
                    " Kak, makin sukses ke depannya."
                ),
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "18",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Mencari Nafkah",
                "sosmed": "@jay.saputra.mb",
                "kesan": (
                    "Sangat mandiri, memiliki etos kerja yang tinggi, dan"
                    " ringan tangan dalam membantu sesama."
                ),
                "pesan": (
                    "Perjuangan dan kerja kerasmu sangat menginspirasi, Bang."
                    " Semoga rezekinya selalu dilancarkan."
                ),
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Nonton ASMR",
                "sosmed": "@njlanursyifa",
                "kesan": (
                    "Orangnya sangat asyik diajak ngobrol dan punya sense of"
                    " humor yang selalu bikin tersenyum."
                ),
                "pesan": (
                    "Tetap jadi sosok yang santai dan membawa ketenangan buat"
                    " orang-orang di sekitarmu, Kak."
                ),
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal": "Kalianda, Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Berantemin Kucing",
                "sosmed": "@rozakrabbani__",
                "kesan": (
                    "Sangat disiplin, tepat waktu, dan punya cara unik"
                    " tersendiri saat berinteraksi."
                ),
                "pesan": (
                    "Kurang-kurangi usilin kucingnya ya Bang, sukses terus buat"
                    " akademik dan organisasinya!"
                ),
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@kristiani8872",
                "kesan": (
                    "Punya karakter tegas dan lugas, namun sebenarnya sangat"
                    " perhatian pada detail pekerjaan."
                ),
                "pesan": (
                    "Pertahankan ketegasan yang positif itu, Kak, dan semoga"
                    " makin sering eksplor resep masak baru!"
                ),
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Way Kandis",
                "hobbi": "Nonton F1 & MotoGP",
                "sosmed": "@hnfdzky_",
                "kesan": (
                    "Karismatik dan punya pemikiran yang matang saat menghadapi"
                    " situasi sulit."
                ),
                "pesan": (
                    "Tetap melaju kencang meraih cita-cita layaknya balapan F1,"
                    " sukses selalu Bang Hanif!"
                ),
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": (
                    "Sangat rendah hati, tidak banyak bicara tetapi tindakan"
                    " nyata dan bantuan selalu terasa."
                ),
                "pesan": (
                    "Kebaikan dan sifat rendah hatimu sangat dihargai. Sukses"
                    " terus untuk studi dan hobinya ya Kak."
                ),
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Bagan Batu, Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@cikamrbn",
                "kesan": (
                    "Punya manajemen waktu yang rapi dan selalu terorganisir"
                    " dalam menyelesaikan tugas."
                ),
                "pesan": (
                    "Tetap konsisten dan jangan lupa recharge energi lewat"
                    " musik kesukaanmu di waktu luang!"
                ),
            },
            {
                "nama": "Gustin H Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": (
                    "Kritis, berwawasan luas, dan selalu memberikan sudut"
                    " pandang atau solusi yang realistis."
                ),
                "pesan": (
                    "Terus jadi kawan diskusi yang asyik dan pembimbing yang"
                    " solutif untuk adik-adik tingkat."
                ),
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Ngadu Ikan Cupang",
                "sosmed": "@muhvinz_",
                "kesan": (
                    "Sangat supel, mudah membaur dengan siapa saja, dan tidak"
                    " pernah canggung."
                ),
                "pesan": (
                    "Tetap jadi pribadi yang hangat dan makin sukses dengan"
                    " segala hobi unik serta kegiatannya!"
                ),
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@snasaa._",
                "kesan": (
                    "Ramah, murah senyum, dan selalu bisa membuat suasana"
                    " kumpul terasa lebih menyenangkan."
                ),
                "pesan": (
                    "Tetap pertahankan sifat ramahmu dan semoga selalu"
                    " diberikan kelancaran dalam urusan kuliah!"
                ),
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    departemen_internal()

# MINBAK
if menu == "Departemen Minbak":

    def departemen_minbak():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1KHvAJHsZnTtb8MLloY2klT6xvO07myQA&sz=w1000",
            "https://drive.google.com/thumbnail?id=1g_X5b4Da1erPnGY-hoT4NB_JW6dDpK3X&sz=w1000",
        ]

        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "asal": "Bandar Lampung",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Balap",
                "umur": "21",
                "sosmed": "@kevinaj__",
                "kesan": (
                    "Sangat cekatan, punya ketenangan dalam bertindak, dan"
                    " selalu tahu cara meredakan kepanikan."
                ),
                "pesan": (
                    "Tetap melaju kencang mengejar impiannya Kak, dan ingat"
                    " untuk selalu utamakan keselamatan di jalan!"
                ),
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Baca",
                "umur": "21",
                "sosmed": "@ferazkaa",
                "kesan": (
                    "Pengetahuannya sangat luas dan selalu memberikan argumen"
                    " yang rasional serta menenangkan."
                ),
                "pesan": (
                    "Semoga makin banyak rekomendasi buku menarik yang bisa"
                    " dibagikan ke kami ya, Kak!"
                ),
            },
            {
                "nama": "Ari Aristo Muthahari Parisi",
                "nim": "123450088",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "umur": "21",
                "sosmed": "@ali_parisi3",
                "kesan": (
                    "Sosok yang tenang, tidak suka pamer, tapi hasil kerjanya"
                    " selalu memuaskan."
                ),
                "pesan": (
                    "Tetap jadi pribadi yang hangat dan terus nikmati keseruan"
                    " musim balap F1 favoritnya, Kak."
                ),
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "umur": "20",
                "sosmed": "@aayuandrianni_",
                "kesan": (
                    "Punya ambisi belajar yang tinggi dan selalu fokus dalam"
                    " menyelesaikan setiap tugas."
                ),
                "pesan": (
                    "Dedikasi belajar Kakak sangat menginspirasi, tapi jangan"
                    " lupa luangkan waktu untuk istirahat juga ya!"
                ),
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Nemenin Bryan live TikTok",
                "umur": "21",
                "sosmed": "@dafaelpriza_",
                "kesan": (
                    "Orangnya sangat ramah, suportif banget sama teman, dan"
                    " selalu berhasil menghidupkan suasana."
                ),
                "pesan": (
                    "Tetap jadi teman setianya Bryan dan terus tebar energi"
                    " positif ke mana pun pergi, Kak."
                ),
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lihat bulan",
                "umur": "19",
                "sosmed": "@ju.juwitaaa_",
                "kesan": (
                    "Memiliki aura yang sangat lembut, penuh empati, dan selalu"
                    " mendengarkan orang lain dengan baik."
                ),
                "pesan": (
                    "Semoga hari-hari Kakak selalu seindah malam yang dipenuhi"
                    " sinar bulan."
                ),
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "asal": "Lampung Tengah",
                "alamat": "Jl Pulau Damar",
                "hobbi": "Taptap layar kalo Bryan live",
                "umur": "19",
                "sosmed": "@afdall.03",
                "kesan": (
                    "Sangat kompak, menyenangkan, dan selalu totalitas kalau"
                    " mendukung aktivitas teman-temannya."
                ),
                "pesan": (
                    "Semangat taptap layarnya Kak, semoga makin solid dan"
                    " kompak terus dengan lingkaran pertemanannya!"
                ),
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "umur": "",
                "sosmed": "@slbnzw_",
                "kesan": (
                    "Sangat fleksibel, mudah diajak diskusi hal apapun, dan"
                    " komunikatif."
                ),
                "pesan": (
                    "Nanti kalau nongkrong di Kopken lagi, ajak-ajak kami ya"
                    " Kak! Sukses terus untuk studinya."
                ),
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nganterin Datasena ke gedung F",
                "umur": "21",
                "sosmed": "@mridwaan_22",
                "kesan": (
                    "Sangat dapat diandalkan, loyal pada teman, dan tidak"
                    " pernah perhitungan kalau minta tolong."
                ),
                "pesan": (
                    "Kebaikan dan kepedulian Kakak luar biasa, semoga kuliah"
                    " dan urusannya selalu dilancarkan!"
                ),
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Ngitungin kelopak bunga di kebun",
                "umur": "18",
                "sosmed": "@andra.lhm",
                "kesan": (
                    "Detail, teliti, serta punya pemikiran unik yang sering"
                    " membuat orang lain kagum."
                ),
                "pesan": (
                    "Semoga ketelitian dan kesabaran Kakak bisa terus membawa"
                    " kesuksesan di segala bidang."
                ),
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "umur": "22",
                "sosmed": "@bryantel_",
                "kesan": (
                    "Punya bakat alami sebagai entertainer, penuh rasa percaya"
                    " diri, dan selalu bikin senyum."
                ),
                "pesan": (
                    "Makin sukses konten live TikTok-nya Kak, terus jadi sosok"
                    " yang menghibur dan menginspirasi!"
                ),
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Ngegift live Bryan",
                "umur": "17",
                "sosmed": "@meardhy_ghiyats",
                "kesan": (
                    "Sangat dermawan, tidak ragu mengapresiasi orang lain, dan"
                    " punya kepribadian yang asyik."
                ),
                "pesan": (
                    "Tetap jadi orang baik yang suka berbagi kebahagiaan,"
                    " rezeki Kakak pasti mengalir deras!"
                ),
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "umur": "Belum Tahu",
                "sosmed": "@indahjuliaa",
                "kesan": (
                    "Tenang, simpel, dan tidak ribet saat diajak berinteraksi"
                    " maupun berorganisasi."
                ),
                "pesan": (
                    "Jangan kebanyakan bengong ya Kak, tetap semangat dan"
                    " jalani hari-hari dengan penuh keceriaan!"
                ),
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "umur": "18",
                "sosmed": "@cacalvra",
                "kesan": (
                    "Kreatif, enerjik, dan punya humor unik yang selalu"
                    " berhasil mencairkan suasana."
                ),
                "pesan": (
                    "Terus jadi penyebar keceriaan dan jangan pernah lelah"
                    " membawa warna positif di lingkungan sekitar!"
                ),
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "umur": "20",
                "sosmed": "@muhammdrafka_",
                "kesan": (
                    "Punya kedisiplinan dan prinsip hidup yang kuat, patut"
                    " dijadikan contoh oleh yang lain."
                ),
                "pesan": (
                    "Tularkan kebiasaan positif bangun paginya ke kami Kak,"
                    " semoga sukses selalu akademik dan kariernya!"
                ),
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    departemen_minbak()

# MIKFES
if menu == "Departemen MIKFES":

    def departemen_mikfes():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1gr_mv5NM_num63X_uKbwRDG-nhJRxH_5&sz=w1000",
            "https://drive.google.com/thumbnail?id=1cn3gsxtmb5rLZrXtTppvpe1VvxXJZtOZ&sz=w1000",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "12340104",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "umur": "21",
                "sosmed": "@biyokcb",
                "kesan": (
                    "Sangat santai, ramah, dan punya cara pembawaan yang bikin"
                    " orang di sekitarnya merasa nyaman."
                ),
                "pesan": (
                    "Tetap jadi abang yang selalu mengayomi dan salam hangat"
                    " untuk waktu tidurnya yang berkualitas, Bang!"
                ),
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "asal": "Lampung",
                "alamat": "Airan Raya",
                "hobbi": "Membaca",
                "umur": "21",
                "sosmed": "@tvnty_",
                "kesan": (
                    "Sosok yang tenang, sangat teliti, dan selalu memperhatikan"
                    " detail penting yang sering terlewat."
                ),
                "pesan": (
                    "Tetap pertahankan sifat kritis dan telitinya ya Kak,"
                    " sukses terus untuk semua kegiatannya!"
                ),
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim": "Belum Tahu",
                "asal": "Bandar Lampungku",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "umur": "21",
                "sosmed": "@fadilalfarizzii",
                "kesan": (
                    "Punya bakat musik yang keren dan selalu bisa bikin suasana"
                    " kumpul jadi lebih hidup."
                ),
                "pesan": (
                    "Terus berkarya dan jangan sungkan buat sering-sering tampil"
                    " unjuk kebolehan main gitar ya, Kak!"
                ),
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "umur": "20",
                "sosmed": "@manuelfdk_",
                "kesan": (
                    "Penuh energi, komunikatif, dan sangat luwes waktu"
                    " berinteraksi dengan siapa saja."
                ),
                "pesan": (
                    "Semangat terus untuk aktivitasnya Kak, dan semoga hobi"
                    " tenis mejanya makin jago!"
                ),
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "asal": "Bali",
                "alamat": "Nusa Penida",
                "hobbi": "Menghayal",
                "umur": "12",
                "sosmed": "Violaadrtr_",
                "kesan": (
                    "Sangat imajinatif, punya kreativitas tinggi, dan"
                    " pembawaannya sangat lembut."
                ),
                "pesan": (
                    "Terus kembangkan imajinasi dan ide-ide kreatifmu jadi"
                    " karya yang luar biasa ya!"
                ),
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling skate",
                "umur": "20",
                "sosmed": "risarmdna",
                "kesan": (
                    "Sangat aktif, berani keluar dari zona nyaman, dan punya"
                    " jiwa petualang yang keren."
                ),
                "pesan": (
                    "Tetap eksploratif dan berani meluncur mengejar impianmu"
                    " seperti saat bermain rolling skate, Kak!"
                ),
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur": "19",
                "sosmed": "@vunnycaa",
                "kesan": (
                    "Selalu membawa energi positif dan senyuman yang bikin"
                    " suasana di sekitarnya mendadak ceria."
                ),
                "pesan": (
                    "Pertahankan keceriaan dan keramahan itu ya Kak, semoga"
                    " sukses selalu kuliahnya!"
                ),
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim": "Belum Tahu",
                "asal": "Belum Tahu",
                "alamat": "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur": "Belum Tahu",
                "sosmed": "Belum Tahu",
                "kesan": (
                    "Sangat santun, menghargai sesama, dan selalu menjaga"
                    " etika dalam berinteraksi."
                ),
                "pesan": (
                    "Semoga bisa kenal lebih dekat lagi dan sukses untuk semua"
                    " hal yang sedang diusahakan!"
                ),
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "1234501",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "umur": "21",
                "sosmed": "@keyashafi",
                "kesan": (
                    "Sangat suportif, peka terhadap perasaan teman, dan"
                    " selalu siap jadi pendengar yang baik."
                ),
                "pesan": (
                    "Terima kasih sudah selalu jadi sosok yang nyaman diajak"
                    " ngobrol, sukses selalu untuk studinya ya Kak!"
                ),
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "umur": "21",
                "sosmed": "_els.a",
                "kesan": (
                    "Pembawaannya hangat, mudah disapa, dan bikin orang lain"
                    " cepat merasa dekat."
                ),
                "pesan": (
                    "Nikmati waktu rebahannya sebagai penyeimbang kegiatan"
                    " kuliah yang padat, sukses terus Kak!"
                ),
            },
            {
                "nama": "Fadya Izzatul ‘Aini",
                "nim": "124450062",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Mancing",
                "umur": "20",
                "sosmed": "fadyaizzatul_",
                "kesan": (
                    "Sangat sabar, penyabar, dan punya daya tangkap serta fokus"
                    " yang bagus."
                ),
                "pesan": (
                    "Semoga kesabaran dari hobi mancingnya selalu membawa"
                    " keberkahan dan kelancaran dalam kuliah!"
                ),
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur": "19",
                "sosmed": "_loviaa",
                "kesan": (
                    "Sederhana, tidak neko-neko, dan selalu memancarkan"
                    " ketenangan dalam bertindak."
                ),
                "pesan": (
                    "Tetap jadi pribadi yang rendah hati dan semoga hari-harimu"
                    " selalu diwarnai lagu-lagu favorit!"
                ),
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "asal": "Kalianda",
                "alamat": "Kotabaru",
                "hobbi": "Main Game, Tidur",
                "umur": "20",
                "sosmed": "@aluccy_",
                "kesan": (
                    "Sangat kocak, punya lelucon yang spontan, dan tidak pernah"
                    " gagal mencairkan suasana stiff."
                ),
                "pesan": (
                    "Tetap jadi pembawa tawa di kelompok, tapi jangan lupa"
                    " porsi waktu buat game dan kuliahnya tetap seimbang ya,"
                    " Bang!"
                ),
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "umur": "19",
                "sosmed": "sher_renna",
                "kesan": (
                    "Selalu tampil rapi, percaya diri, dan punya estetika diri"
                    " yang dipersiapkan dengan baik."
                ),
                "pesan": (
                    "Terus pancarkan kepercayaan diri itu Kak, dan sukses"
                    " selalu buat hobi serta akademiknya!"
                ),
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "umur": "21",
                "sosmed": "@razyn.hfd",
                "kesan": (
                    "Punya jiwa kepemimpinan di lapangan, sportif, dan selalu"
                    " mengutamakan kerja sama tim."
                ),
                "pesan": (
                    "Tetap jaga kebugaran dan semangat juangnya Kak, baik di"
                    " lapangan futsal maupun di organisasi!"
                ),
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Membaca Novel",
                "umur": "19",
                "sosmed": "FAIZAANJANII",
                "kesan": (
                    "Sangat bijak, kata-katanya tertata rapi, dan selalu"
                    " berpikir sebelum bertindak."
                ),
                "pesan": (
                    "Semoga makin banyak novel menarik yang dibaca dan ilmu"
                    " hikmahnya bisa terus dibagikan!"
                ),
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "umur": "20",
                "sosmed": "@gathfannadif",
                "kesan": (
                    "Tampaknya santai tapi sangat fokus dan bertanggung jawab"
                    " saat diberi tugas."
                ),
                "pesan": (
                    "Pertahankan keseimbangan antara kerja keras dan hobi"
                    " gaming-mu ya Kak!"
                ),
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "umur": "20",
                "sosmed": "@apiszzaja_",
                "kesan": (
                    "Sangat terampil di bidang IT/teknis, produktif, dan tidak"
                    " pelit membagikan ilmunya."
                ),
                "pesan": (
                    "Semangat terus untuk 3N-nya Bang, tapi luangkan waktu buat"
                    " istirahat biar enggak burnout!"
                ),
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur": "20",
                "sosmed": "@kelelep_comberan",
                "kesan": (
                    "Disiplin tinggi, punya kombinasi hobi fisik dan pikiran"
                    " yang seimbang banget."
                ),
                "pesan": (
                    "Tetap konsisten menjaga kebiasaan positifnya Kak,"
                    " pencapaian gym dan akademiknya semoga makin melesat!"
                ),
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "asal": "Sumsel",
                "alamat": "Sukarame",
                "hobbi": "Scroll",
                "umur": "19",
                "sosmed": "@melva_fbrt",
                "kesan": (
                    "Gampang berbaur, selalu update dengan hal-hal baru, dan"
                    " pembawaannya ceria."
                ),
                "pesan": (
                    "Tetap jadi sosok kawan yang asyik dan makin sukses untuk"
                    " studinya di Lampung!"
                ),
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "Belum Tahu",
                "asal": "Belum Tahu",
                "alamat": "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur": "Belum Tahu",
                "sosmed": "@syaafiqui",
                "kesan": (
                    "Tenang dan tidak banyak bicara, tapi kalau diminta bantuan"
                    " selalu siap action."
                ),
                "pesan": (
                    "Jangan ragu buat lebih sering mengutarakan pendapatmu ya"
                    " Kak, ide-idem pasti bermanfaat!"
                ),
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "asal": "Kobum",
                "alamat": "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur": "28",
                "sosmed": "henryferdianto",
                "kesan": (
                    "Punya gaya humor yang out-of-the-box dan selalu berhasil"
                    " membuat suasana ceria."
                ),
                "pesan": (
                    "Jangan lari dari kenyataan terus ya Bang, hadapi dan"
                    " taklukkan dengan candaan khasmu!"
                ),
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    departemen_mikfes()

# MEDKRAF
if menu == "Departemen Medkraf":

    def departemen_medkraf():
        gambar_urls = []

        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Belum Tahu",
                "hobbi": "Rebahan",
                "umur": "20",
                "sosmed": "@naylasalsabilaa._",
                "kesan": (
                    "Pembawaannya lembut, sangat penyabar, dan selalu enak"
                    " diajak bertukar pikiran."
                ),
                "pesan": (
                    "Nikmati porsi rebahannya sebagai penyeimbang padatnya"
                    " tugas, dan sukses terus untuk studinya ya Kak!"
                ),
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "asal": "Bekasi dan Lampung",
                "alamat": "Belum Tahu",
                "hobbi": "Mendengarkan musik",
                "umur": "21",
                "sosmed": "@donnamaya.p",
                "kesan": (
                    "Sangat empati, tulus saat mendengarkan cerita, dan punya"
                    " aura yang bikin nyaman."
                ),
                "pesan": (
                    "Terima kasih selalu jadi tempat cerita yang aman, sukses"
                    " dan bahagia selalu untuk Kak Donna!"
                ),
            },
            {
                "nama": "Labo John Nuel Napitupulu",
                "nim": "37",
                "asal": "Medan, Jakut, Palembang",
                "alamat": "Belum Tahu",
                "hobbi": "Berburu burung",
                "umur": "20",
                "sosmed": "@noerruuu",
                "kesan": (
                    "Pengalamannya luas, cara berceritanya seru, dan selalu"
                    " punya sudut pandang yang unik."
                ),
                "pesan": (
                    "Jangan lelah membagikan cerita petualangan dan"
                    " pengalamannya ke kami ya, Bang!"
                ),
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "asal": "Bandar Lampung",
                "alamat": "Belum Tahu",
                "hobbi": "Ngoding",
                "umur": "20",
                "sosmed": "@anshtsyaaql",
                "kesan": (
                    "Sangat fokus, punya dedikasi tinggi, dan selalu kelihatan"
                    " keren saat berkutat dengan kode."
                ),
                "pesan": (
                    "Makin jago ngodingnya Kak, tapi jangan lupa luangkan waktu"
                    " buat recharge energi juga!"
                ),
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "asal": "Bekasi",
                "alamat": "Belum Tahu",
                "hobbi": "Ngejahilin mama",
                "umur": "18",
                "sosmed": "@felisyanbl__",
                "kesan": (
                    "Karakternya ceria, ekspresif, dan keusilannya selalu"
                    " berhasil memecahkan ketegangan."
                ),
                "pesan": (
                    "Terus tebar keceriaan dan kehangatan di mana pun berada"
                    " ya, Kak!"
                ),
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "asal": "Sibolga",
                "alamat": "Belum Tahu",
                "hobbi": "Jahilin Felisya",
                "umur": "18",
                "sosmed": "@muh_razan_",
                "kesan": (
                    "Orangnya asyik, gampang berbaur, dan selalu punya ide"
                    " candaan yang menghibur."
                ),
                "pesan": (
                    "Jaga kekompakan dan pertemanan seru itu terus ya Bang,"
                    " sukses selalu kuliahnya!"
                ),
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "asal": "Bandung",
                "alamat": "Belum Tahu",
                "hobbi": "Bimbingan TA",
                "umur": "21",
                "sosmed": "@saniayyllstr",
                "kesan": (
                    "Kerja keras dan daya juangnya luar biasa, tidak gampang"
                    " menyerah menghadapi tantangan."
                ),
                "pesan": (
                    "Semoga proses Bimbingan TA-nya lancar tanpa hambatan dan"
                    " segera meraih gelar sarjana ya, Kak!"
                ),
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "asal": "Rahim ibu",
                "alamat": "Belum Tahu",
                "hobbi": (
                    "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah"
                ),
                "umur": "6",
                "sosmed": "@aallishaa.a",
                "kesan": (
                    "Sangat solidaritas, hangat, dan selalu setia menemani"
                    " serta meramaikan circle pertemanannya."
                ),
                "pesan": (
                    "Semoga momen kebersamaan dan keseruan makan bareng"
                    " teman-temannya awet terus ya!"
                ),
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "asal": "Kota banyak sawit",
                "alamat": "Belum Tahu",
                "hobbi": "Apa aja",
                "umur": "19",
                "sosmed": "@alya.rmdhnti",
                "kesan": (
                    "Sangat adaptif, gampang diajak ngapain aja, dan punya rasa"
                    " ingin tahu yang positif."
                ),
                "pesan": (
                    "Pertahankan sifat eksploratif itu Kak, semoga makin"
                    " banyak pengalaman seru yang didapat!"
                ),
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "asal": "Lampung Selatan",
                "alamat": "Belum Tahu",
                "hobbi": "Belajar",
                "umur": "20",
                "sosmed": "@bungaclrssf",
                "kesan": (
                    "Sangat tekun, memiliki ambisi akademik yang positif, dan"
                    " konsisten dalam belajar."
                ),
                "pesan": (
                    "Semangat belajarnya terus dipertahankan Kak, tapi ingat"
                    " untuk jaga kesehatan dan waktu istirahat juga ya!"
                ),
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "asal": "Deket Kebun Teh",
                "alamat": "Belum Tahu",
                "hobbi": "Alhamdulillah Dzikir dan sholawatan",
                "umur": "20",
                "sosmed": "@difanyhsa",
                "kesan": (
                    "Sangat sejuk pembawaannya, tutur katanya sopan, dan"
                    " memancarkan kebaikan."
                ),
                "pesan": (
                    "Tetap jadi pribadi yang menginspirasi dalam kebaikan dan"
                    " membawa ketenangan buat sekitar ya Kak!"
                ),
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "asal": "Bandar Lampung",
                "alamat": "Belum Tahu",
                "hobbi": "Ballet",
                "umur": "20",
                "sosmed": "@nzlhauly_",
                "kesan": (
                    "Tampilannya selalu anggun, percaya diri, dan memiliki"
                    " kedisiplinan yang bagus."
                ),
                "pesan": (
                    "Terus bersinar lewat hobi ballet dan pencapaian"
                    " akademiknya ya Kak!"
                ),
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "umur": "20",
                "sosmed": "@r.hanaap",
                "kesan": (
                    "Berwawasan luas, punya daya imajinasi tinggi, dan sangat"
                    " rapi dalam menyampaikan tulisan."
                ),
                "pesan": (
                    "Semoga karya tulis dan bacaannya semakin menginspirasi,"
                    " sukses terus untuk studinya ya Kak!"
                ),
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "Belum Tahu",
                "asal": "Belum Tahu",
                "alamat": "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur": "Belum Tahu",
                "sosmed": "Belum Tahu",
                "kesan": (
                    "Orangnya tenang, sederhana, tapi selalu menunjukkan"
                    " ketulusan saat berinteraksi."
                ),
                "pesan": (
                    "Semoga ke depannya bisa makin sering ngobrol dan saling"
                    " kenal lebih dekat lagi Kak!"
                ),
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "098",
                "asal": "Lampung Selatan, Natar",
                "alamat": "Belum Tahu",
                "hobbi": "Scroll Fesbuk",
                "umur": "20",
                "sosmed": "@edsel_0712",
                "kesan": (
                    "Humoris dengan style yang khas, santai, dan tidak pernah"
                    " kaku saat bergaul."
                ),
                "pesan": (
                    "Tetap jadi abang yang seru diajak nongkrong dan sukses"
                    " selalu buat kuliahnya!"
                ),
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Lari",
                "umur": "20",
                "sosmed": "@luciarachel_",
                "kesan": (
                    "Penuh daya tahan, enerjik, dan selalu menularkan aura"
                    " positif ke orang sekitarnya."
                ),
                "pesan": (
                    "Semangat berlari mengejar impian dan target-target baiknya"
                    " ya Kak!"
                ),
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "asal": "Lampung Tengah",
                "alamat": "Belum Tahu",
                "hobbi": "Makan tempe mentah",
                "umur": "20",
                "sosmed": "@_shaazzh",
                "kesan": (
                    "Sangat unik, opentested, dan tidak ragu menunjukkan diri"
                    " apa adanya."
                ),
                "pesan": (
                    "Tetap pertahankan kejujuran dan keunikan dirimu Kak,"
                    " sukses terus untuk urusan akademiknya!"
                ),
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "Belum Tahu",
                "asal": "Belum Tahu",
                "alamat": "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur": "Belum Tahu",
                "sosmed": "Belum Tahu",
                "kesan": (
                    "Sangat ramah, selalu menghargai kawan bicaranya, dan"
                    " tutur katanya santun."
                ),
                "pesan": (
                    "Semoga selalu diberi kelancaran dan kemudahan dalam setiap"
                    " langkah kegiatan serta studinya Kak!"
                ),
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    departemen_medkraf()