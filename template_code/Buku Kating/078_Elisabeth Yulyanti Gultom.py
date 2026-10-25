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
            "https://drive.google.com/uc?export=view&id=1nGRlsYpTVG2QivPXhN3WquLds9d2yCpT",
            "https://drive.google.com/uc?export=view&id=1CmnTMpU5BxtbNfrr7IRDedqIexLAmyoK",
            "https://drive.google.com/uc?export=view&id=1kRRoROpkOB4OG_8BHRYF-bQrjxNq1J9o",
            "https://drive.google.com/uc?export=view&id=18R84OkdL4agMfexB18F3vdXi-O3Jrsyv",
            "https://drive.google.com/uc?export=view&id=1YUAkKsY2MhLvr0MaUnpbPsrq7wQbFEVH",
            "https://drive.google.com/uc?export=view&id=1m7opKJa6r5tGAoAwQEs8JtydsvvCWCJP"
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
                "kesan": "baik banget, awalnya lihat bang ginda agak seram ternyata orangnya juga ramah",  
                "pesan":"semangat terus bang buat TA nya, semoga semua urusannya dipermudah"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Tahajud",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya ramah dan murah senyum",  
                "pesan":"Semangat bang buat TA nya, cepat lulus dan wisuda"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya asik, baik juga",  
                "pesan":"Lancar terus kak buat studinya!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Waktu pemaparan materi bang qois ramah dan sabar banget selama menjelaskan, suka!",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Basket",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak hafsa orangnya cantik, kelihatan humble juga",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Lutfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nemuin Pak Tirta",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "kakaknya keren, jadi panutan banget sih, apalagi baik juga orangnya",  
                "pesan":"semangat terus kak buat kuliah dan jadi bendaharanya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CknShi_2XWwEP-oObntDMeODaIei1d12",
            "https://drive.google.com/uc?export=view&id=1lRYd3n3rT2u-_aw2eT9xR6zcuHI6N3xs",
            "https://drive.google.com/uc?export=view&id=193UbmSc_0JwQyt6zG2M9CVTyurzag9ng",
            "https://drive.google.com/uc?export=view&id=1k9wxjuOX3oMrCyUOl4T7ygw0AJheljd4",
            "https://drive.google.com/uc?export=view&id=1eub77dGj5U_AaY62wiq30EsFpMECHC01",
            "https://drive.google.com/uc?export=view&id=1-SYA5CBZEzo_ALg2oMF1OFtdcI8S6S4V",
            "https://drive.google.com/uc?export=view&id=1GyViE6zjiIAnrKSgnESbOPreYPwswjzs",
            "https://drive.google.com/uc?export=view&id=1YnDEuD5xeQCxsq42OtSKSIX-GgJeITBT",
            "https://drive.google.com/uc?export=view&id=1x91UZq0TiMFIaaegRzmafBYHHB6GeDrY",
            "https://drive.google.com/uc?export=view&id=1KwN2jFnzRnMLO4CJFVywChsISi11fEz_",
            "https://drive.google.com/uc?export=view&id=1Roopbnta0vgVc-Qyo1tAIzs88NwHn-_E",
            "https://drive.google.com/uc?export=view&id=1RBLrCGMkvQ0Aop5wsQ8Jzo98ZCAU5Bkh"            
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
                "kesan": "Abang ini asik parah dan yapping banget tapi seru juga",  
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
                "pesan":"Semoga selalu sukses dan dilancarkan semua urusannya ya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "124450045",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "kakaknya keliatan kalem dan baik polos gitu", 
                "pesan":"Lancar terus kak studinya, semoga semua harapan dan cita-citanya tercapai"# 1
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
                "pesan":"Semangat terus dan aktif terus bang Semangat terus dan aktif terus bang kuliahnya"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Jatiasih",
                "alamat": "Kedaton",
                "hobbi": "Nonton Boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "Seru bisa kenal kakaknya, kakaknya juga kasih kesan yang baik",  
                "pesan":"Semoga selalu semangat ya kak buat jalanin kuliahnya"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Indarum",
                "alamat": "Awen kost",
                "hobbi": "Photobooth",
                "sosmed": "@afghanisnt_",
                "kesan": "kakaknya kelihatan ramah dan bisa diajak bercanda",  
                "pesan":"Semoga tetap semangat dalam menjalani perkuliahannya"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",                
                "sosmed": "@haniquratuain_",
                "kesan": "First impression ke kakaknya baik karena pembawaan kakaknya juga menyenangkan",  
                "pesan":"Semoga semua targetnya tercapai yaa kak"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Sidoarjo",
                "alamat": "Teluk",
                "hobbi": "Konten Mainfullness",                
                "sosmed": "@jeremia_hm",
                "kesan": "Pembawaan bang jeremi tenang dan kelihatan dewasa",  
                "pesan":"Sukses bang buat kedepannya"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan koleksi figure",                
                "sosmed": "@nagatseee",
                "kesan": "Bang jona ramah, pembawaannya santai, asik, dan keliatan pintar",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik ya bang, semangat!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Membaca buku",                
                "sosmed": "@sekardnwp",
                "kesan": "Keliatan serius dan awalnya tuh ngira kakaknya galak ternyata baik banget selama wawancara",  
                "pesan":"Semoga tetap jadi pribadi yang baik dan rendah hati"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "124450077",
                "umur": "20",
                "asal":"Pasoy",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",                
                "sosmed": "@nshaysk",
                "kesan": "Keliatan kakanya friendly dan mudah diajak ngobrol, serulah pokoknya",  
                "pesan":"Semoga kedepannya makin sukses dan harapannya bisa terwujud"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dcZxS9bA_HKijCc_JDh9UYDTFkldJFsG",
            "https://drive.google.com/uc?export=view&id=1P7kwlC_l_0LfX0_2TQGUNK2EVKWNYj_r",
            "https://drive.google.com/uc?export=view&id=1byNiD5kI4CMMY5-gZt_ZbP7l5Xj2dMjd",
            "https://drive.google.com/uc?export=view&id=1ZEkcoKuXp8tEKc78KoAKjAkfhfwnudry",
            "https://drive.google.com/uc?export=view&id=1I9pEhikxz1SFcqmKxaFhs0-vTwUSdhqk",
            "https://drive.google.com/uc?export=view&id=1eLh12t0BW_Bv-e6LrT_kU0WJ-DsxXM2e",
            "https://drive.google.com/uc?export=view&id=1InLgp7VmzQ9Tq5IO39grDK5nDamyug16",
            "https://drive.google.com/uc?export=view&id=1S0BMrEj87cma68ukOXMW4BlxYTq5odXP",
            "https://drive.google.com/uc?export=view&id=1HLosX05hLwbzL_ZmofjGk8_q5BQX0BFH",
            "https://drive.google.com/uc?export=view&id=1Wu1NxZYMdIIpQMebcOPTQHovbJcUGn_z",
            "https://drive.google.com/uc?export=view&id=1RZz5gxPGFm4BHP-9P-1TC8ZSoM1bCU3V",
            "https://drive.google.com/uc?export=view&id=1pP8RJRG1zvR2kolHI7_sAFRJbdna9An5",
            "https://drive.google.com/uc?export=view&id=15YjPo_hfQF4nk4zPKM2OHHEuhz9yHeki",
            "https://drive.google.com/uc?export=view&id=1FUlr5HNgaRSwBaHVxVu3GrztJnGSqSI9",
            "https://drive.google.com/uc?export=view&id=1sispmKx8NHjCViUdyP6nWWC1_QinfmOq",
            "https://drive.google.com/uc?export=view&id=1gJdZ0srwqa3YApmdlHbj78rltEbH5YKY",
            "https://drive.google.com/uc?export=view&id=1A1yNRHxzDvVt_b9OQQx7GZZlHUNxmGSM",
            "https://drive.google.com/uc?export=view&id=1nqtLH0XeQt5qMNHcp-Le0a5nNH6alEQw",
            "https://drive.google.com/uc?export=view&id=1LTJs5TGtciNsxk0szrCGAhiHHlV3rpfF",
            "https://drive.google.com/uc?export=view&id=14Im92_zayBnoq6ra7RGjp5RnuFTZN89X",
            "https://drive.google.com/uc?export=view&id=1yhGBGCut6ae4Lh4gTFryYFaHIfN54cKD",
            "https://drive.google.com/uc?export=view&id=1DZzCgn4K3r9oNdw9p3argOnNAbgXkrkX"
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
                "kesan": "Awalnya ngira kalau kakanya galak, ternyata aslinya baik juga",  
                "pesan": "Semangat terus kuliahnya kakak!!!"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Keliatan kakaknya ramah dan baik banget",  
                "pesan":"Semoga selalu sehat dan bahagia kak"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Bang adit baik,pengertian, dan bertanggung jawab sama kerjaannya terus tiap ketemu bang adit, abangnya kayak lemah letih lesu ",  
                "pesan":"Semangat menjalani kuliahnya bang, semoga urusan kuliahnya diperlancar buat kedepannya"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakaknya baik, ramah, softspoken, kelihatan aura orang pintar dan aktifnya",  
                "pesan":"semangat terus buat kuliah dan lombanya kak, semoga memperoleh hasil yang terbaik"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak selma baik parah, lembut banget kalau bicara, murah senyum juga, the best deh pokoknya",  
                "pesan":"Lancar buat studinya kak selma, semoga berhasil!"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kak ashila keren, orangnya teratur, dewasa pula",  
                "pesan":"Semangat terus kak ashila!"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya kelihatan baik dan gak sombong",  
                "pesan":"Semangat menjalani kuliah dan organisasinya kak"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Bang bima baik, keren, humble, humoris, mudah diajak bercanda, dan pengertian banget",  
                "pesan":"Semoga tiap urusan kuliah dan organisasinya berjalan lancar ya bang dan bisa balance"# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang bimo orangnya baik dan kelihatan dewasa juga pintar",  
                "pesan":"Semangat terus bang!"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik, cantik, ramah, pengertian dan mau membantu",  
                "pesan":"Semoga semua hal baik ditambahkan ke kakak ya"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak yollanda baik, ramah, dan juga humble",  
                "pesan":"Lancar terus ya kak buat studinya, semoga pertemanannya selalu menyenangkan"# 1
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
                "kesan": "Kak fathya cantik, asik, dan seru banget",  
                "pesan":"Semangat kak menjalani kuliahnya, semoga semua lancar sampai akhir ya"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kak tarisya pendengar yang baik, mau mendengarkan orang lain, terbuka dengan pendapat yang berbeda, intinya kak tarisya orang yang dewasa",  
                "pesan":"Semangat terus kak sampai akhir, semoga semangat kakak nanti bisa bantu meraih impian kakak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang danil keren, bertanggung jawab, kalcer, tidak sombong dan up to date",  
                "pesan":"Semoga selalu keren bang, semangat buat kuliahnya, salam sukses"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Bang vian baik, penolong disaat kesusahan, orangnya bertanggung jawab dan juga murah senyum",  
                "pesan":"Semoga hal-hal baik terus terjadi dalam hidup bang vian, semangat kuliahnya, semangat buat anmulnya"# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "First impression ke bang yazid abangnya menyeramkan, tapi aslinya baik, ramah, dan kelihatan gak pelit ilmu",  
                "pesan":"Semoga hikmat pengetahuannya terus bertambah-tambah bang, semangat terus demi cumlaude yang akan datang"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya baik, tidak sombong, dan kelihatan capek gitu orangnya, tapi tetap semangat bang buat kuliahnya",  
                "pesan":"Semangat terus bang, semoga semua-muanya berjalan dengan baik"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Awal lihat bang zaldi sewaktu abangnya jadi MC PPLK 2025 dan abangnya memperkenalkan diri sebagai mahasiswa sains data, langsung bagus banget kesannya, bang zaldi keren pokoknya",  
                "pesan":"Semangat bang zaldi, tetap jadi orang baik, ramah, dan tidak sombong"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kak kai orang yang baik, sama-sama suka dracin, jadi langsung klop sama kak kai",  
                "pesan":"Semangat kak buat kuliahnya, semoaga sukses di masa depan dan bisa ketemu Yan An, Chenglei, dkk"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakanya baik, ramah, cantik pula, paket lengkat",
                "pesan":"Semoga selalu dikelilingi hal-hal yang baik ya kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang ahmad keren, penuh inpirasi, cocok banget buat dijadiin role model",  
                "pesan":"Semangat terus bang buat menyuarakan keadilan dan isu-isu yang ada"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SCD49RbnK3cj8nnTm85O4Aq899qTyr4v",
            "https://drive.google.com/uc?export=view&id=1IsLfW3hPtBs1dLwhkLQqe3aJZnYB50B2",
            "https://drive.google.com/uc?export=view&id=1UNdfpfd_t6B2sMAkKbC7AVoWTm1CMLES",
            "https://drive.google.com/uc?export=view&id=1_dIi0_prfnevWHgjfYj9TMLBIoopvW_d",
            "https://drive.google.com/uc?export=view&id=1wcB-rYja-TXFju7nSfDMKWbeHZkcasHR",
            "https://drive.google.com/uc?export=view&id=1Bx8y0Qjv5TgS2BSLd_vHrCGEMAWu04Tl",
            "https://drive.google.com/uc?export=view&id=12CZ2B2Ph1BMG9cmg6l9IUlUruzcRTvdY",
            "https://drive.google.com/uc?export=view&id=1IhOxft56bytRSkvQWxozzArvjQc3Pgb4",
            "https://drive.google.com/uc?export=view&id=1qKT8TrYiLnIV-kG_Cu4roM0iFz9QkKPx",
            "https://drive.google.com/uc?export=view&id=15NdkAhO0rACRE3h2lU8A0INtuWv-zMf9",
            "https://drive.google.com/uc?export=view&id=1QgPnmEw0cbjezfHPyEroB3-6MV97np9b",
            "https://drive.google.com/uc?export=view&id=1RI0kaypGcJqSn2Yc5nAlG6jHpenUt7ly"
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
                "kesan": "Bang ihsan baik, pengertian, panjang sabar, dan bisa jaga rahasia",  
                "pesan":"Semangat terus bang, berkah dalem!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "kakaknya baik, ramah, humble, dan orangnya juga cantik",  
                "pesan":"Lancar terus kak kuliah dan juga usahanya"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya baik, ramah, dan bergaya",  
                "pesan":"Semangat kak buat kuliahnya, makin banyak hal baik yang datang yaa"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik, kalem, tipe-tipe penurut dan polos gitu",  
                "pesan":"Semoga apa yang udah kakak targetin bisa segera kakak dapat yaa"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Bang pome baik, ramah, jahil, dan murah senyum",  
                "pesan":"Semoga kuliahnya lancar dan selesai dengan baik ya bang"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Bang afdhal baik, ramah, dan terlihat bukan tipe yang suka nge judge",  
                "pesan":"Semoga baik-baik saja bang sampai akhir"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya baik, cukup humoris dan terlihat menyenangkan",  
                "pesan":"Lancar terus buat studinya bang, don't give up"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "kakaknya baik, mudah diajak ngobrol dan kelihatan dewasa juga",  
                "pesan":"Semangat terus kak, semoga hal-hal baik selalu datang menghampiri kakak "# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak anggun baik, suka menolong, murah senyum, kakaknya tipe-tipe teman yang setia dan selalu ada kalau dibutuhin",  
                "pesan":"Semoga pertemanannya selalu baik-baik dan selalu ada di lingkungan yang ngasih dampak positif juga"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak dela baik, manis, murah senyum, dan wajahnya bukan tipe karakter antagonis, jadi dari awal itu gak ada kepikiran kalau kakaknya jahat atau nyebelin",  
                "pesan":"Semangat dalam menjalani segala hal yang terjadi kak, hwaiting!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Bang hasan baik tapi kelihatan murung dan kurang berekspresi saat awal ketemu di wawancara",  
                "pesan":"Semangat bang, lebih banyak tersenyum lagi ya"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "First impression ke kak talitha itu kakaknya judes dan susah buat diajak temenan gitu, tapi aslinya kakak nya baik, suka membantu lagi",  
                "pesan":"Semangat kak kuliahnya, lancar terus, semoga semester ini ip nya sesuai yan diharapkan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_FisKXAeJ45ZpJ_5ET6t6V9RDgSfa7aL",
            "https://drive.google.com/uc?export=view&id=1LDk4ZCGza7q6qj1jRqtbV6XTimcli2fM",
            "https://drive.google.com/uc?export=view&id=1wfU4vsU-28PTtb71fdOlIfgiMBrzskjy",
            "https://drive.google.com/uc?export=view&id=1fuCPZ3iRVTMwG_RTKXguGbtk4hhBpivq",
            "https://drive.google.com/uc?export=view&id=1C0zYacGJ040YSGnV35IFRJlp2qxvNGBY",
            "https://drive.google.com/uc?export=view&id=1wnYt9rLD4IgW2gfQ-IL0GcEjGgTQvxQZ",
            "https://drive.google.com/uc?export=view&id=19fG0Bt-AaFpJv2GtuaD0iHjYcs2DEPH6",
            "https://drive.google.com/uc?export=view&id=1U4s4SwLr7XI2BbNa4_-1wZKDN61LjvE8",
            "https://drive.google.com/uc?export=view&id=1kutadqzkUmm1HiGJVfnhugcvICogvzA7",
            "https://drive.google.com/uc?export=view&id=1dwy_uBCE87AMqbVkS4As_pYxZUzYWQTK",
            "https://drive.google.com/uc?export=view&id=1vfyrr50Z_fCTLv6je8PZCpA3FUcZRe7m",
            "https://drive.google.com/uc?export=view&id=1wT8ZL81LX4d3ZRLODytjRUw9IVCm0i6J",
            "https://drive.google.com/uc?export=view&id=1a0r8pxFwe2FwqeAut8fdSi9lnqKcSqo-",
            "https://drive.google.com/uc?export=view&id=1oglexUaf0Va1wRyRNNSVwyzFkjUHedGk",
            "https://drive.google.com/uc?export=view&id=15AKJdrw0OvGs3JIbnVOItZUFZCvxGPMo",
            "https://drive.google.com/uc?export=view&id=1IrNBXDgKdNkNqN4GkmtV0AQ7p4ohGOpG",
            "https://drive.google.com/uc?export=view&id=1I0dpsfvWvr1zHTCNd1nCLNljO6eequwk",
            "https://drive.google.com/uc?export=view&id=1V7-IttNl4t0VTkwuX_O6DanfQpJuj2D3"
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
                "kesan": "kakaknya kelihatan punya selera yang unik dan ada kesan percaya diri gitu",  
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
                "kesan": "kakaknya ramah, punya pembawaan yang positif dan terlihat dewasa",  
                "pesan": "Semoga semua apa yang kakak kerjakan sekarang berhasil di kemudian hari"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Orangnya serius dan pembawaan dirinya kelihatan profesional",  
                "pesan": "Semoga sukses di masa depan bang"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "first impression ke kakanya sederhana, tetapi cukup berkesan karena kakanya baik banget",  
                "pesan": "Semoga selalu dikelilingi orang-orang yang baik"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kelihatan kayak orang yang punya ide menarik dan kreatif",  
                "pesan": "Semoga bisa sukses dalam segala hal kakak"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakaknya enak diajak ngobrol, baik juga",  
                "pesan": "Semoga tetap semangat kak menjalani perkuliahannya"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakaknya cantik, lucu juga orangnya",
                "pesan": "Semoga bisa sukses dan berkembang kedepannya"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "kakaknya mini dan murah senyum, suka!",  
                "pesan":"Semoga tiap pengalaman di medkraf jadi salah satu pengalaman terbaik ya kak"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya baik, ramah, dan tidak stecu",  
                "pesan":"Semoga tetap keren dan lancar terus buat semua urusannya bang"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "kakaknya ngasih kesan yang baik dan kelihatan excited gitu orangnya",  
                "pesan":"Lancar terus buat studi nya kak"# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "kakaknya baik, dewasa, gak sombong dan bertanggung jawab sama tugasnya",  
                "pesan": "Semoga rencana dan semua target kakak bisa tercapai"# 1
            },
            {
                "nama": " Edsel Adya Pradipta",
                "nim": " 124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya baik banget, ramah, humble, dan pastinya gak pelit senyum",  
                "pesan": "Semoga sukses dan bahagia selalu bang"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Bang daffa baik, lucu, oke diajak ngobrol, dan ramah pula",  
                "pesan":"Lancar terus buat studi nya bang, semoga dapat ip yang tinggi semester ini"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "kak alya punya kesan yang bikin orang nyaman",  
                "pesan": "Semoga energi positifnya  bisa menular ke orang sekitar"# 1
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Walaupun belum dekat dan baru kenal, kakaknya kelihatan baik dan ramah",  
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
                "kesan": "kakaknya baik, pembawaan dirinya cukup tenang",  
                "pesan":"Semoga selalu dimudahkan dalam tiap hal diperkuliahan"# 1
            },
            {
                "nama": "shafa delaila azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya baik, senyumnya juga manis",  
                "pesan": "Semoga semua beban yang dianggap berat bisa dilalui dengan tenang dan penuh semangat"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kak allisha cantik, kalcer, asik, dan baik juga",  
                "pesan":"Semoga terus semangat dan sukses dalam setiap langkahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nua9Y5KqbjfI7DGQ9qlneyN3RasnqhIP",
            "https://drive.google.com/uc?export=view&id=17WXdrXZ7I91fM_pPq1nsQIjEILD7l4Up",
            "https://drive.google.com/uc?export=view&id=1-epddXkb0_VyjoDaR7Hs5etlc6cLrhLl",
            "https://drive.google.com/uc?export=view&id=1o_eCpr2VVsgRdK_gLjI9U-JcvIp8knFD",
            "https://drive.google.com/uc?export=view&id=1COlsU5amlpNfbdUTR3C9sY-sUN2_YJoP",
            "https://drive.google.com/uc?export=view&id=19U0aj06xZvMC1u1vgLTVGKOL-5CkLcPu",
            "https://drive.google.com/uc?export=view&id=162ZlGa_HQSIGKyiG1r5MqxdSaTRwGlMk",
            "https://drive.google.com/uc?export=view&id=1sEICKxuxEeVEEYEqsDJyoiG4yZmXa3B2",
            "https://drive.google.com/uc?export=view&id=1vnCzNS5v4U6_Vs6o8BXWLffX0znoP7HV",
            "https://drive.google.com/uc?export=view&id=1ifV0JhMyKW3jn1kbh98XX3DxpW5oxnUi"
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
                "kesan": "Kakaknya ramah dan punya pembawaan yang baik, kakak juga dewasa",  
                "pesan":"Semoga selalu semangangat dan sukses terus kedepannya ya kak!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya asik dan menyenangkan",  
                "pesan":"Semoga bisa jadi orang yang membawa pengaruh positif kedepannya"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "First impression ke kak lia hana itu baik, kakaknya kelihatan tegas dan berwibawa gitu",  
                "pesan":"Semoga untuk setiap perjalanan baik kuliah, organisasi dan pekerjaan ke depannya diberikan kelancaran dalam setiap tanggung jawabnya"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Bang helmy asik, periang, agak jahil orangnya dan suka melet",
                "pesan":"sSemoga kedepannya gaya melet abang masuk nominasi gaya terkeren se-internasional"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando baik, lucu, panjang sabar, dan kelihatan bijak",  
                "pesan":"Semoga lancar terus ya bang kuliahnya, fighting!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kakaknya kelihatan santai, tetapi tetap serius kalau emang situasinya lagi serius",  
                "pesan":"Semoga semua urusannya kakak kedepannya dilancarkan, dan sukses terus ya kak buat studinya"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Bang wielman keren, public speakingnya bagus,mulai dari intonasi sama pemilihan kata abangnya wow banget",  
                "pesan":"Semoga tetap rendah hati dan selalu bawa energi positif di tiap situasi ya kak"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "kak aqila orangnya agak centil, tapi lumayan lucu juga, terus pemikirannya juga luas",  
                "pesan":"Lancar terus kak buat kuliah dan organisasinya"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "19 Tahun",
                "asal":"Lamtim timur",
                "alamat": "Gunter terang",
                "hobbi": "Cinematic Datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang hazel sedikit menyeramkan, namun ternyata orangnya baik juga, berwibawa, dan bertanggungjawab",  
                "pesan":"Semangat bang kuliahnya, lancar-lancar semuanya!"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "kak dwi orangnya baik, dan kelihatan aura gak enakannya, selain ramah kakaknya juga menyenangkan",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1q3mY-abltGPp-huiZeSu04VZw9V8hWeP",
            "https://drive.google.com/uc?export=view&id=1yYnaCVHHDVoWi7eLf6oa_DCrhjgi5eXx",
            "https://drive.google.com/uc?export=view&id=1pQn4JYOi3Iqm6nnwhfbCvIvS2gc6_iu5",
            "https://drive.google.com/uc?export=view&id=1X4LoOHKeul9eW54duLsE9dhnSA1BGOJG",
            "https://drive.google.com/uc?export=view&id=1QBy7GNV471MEqznDtDFZbsYydcInsC0e",
            "https://drive.google.com/uc?export=view&id=1YEUwdQABqKA45aVtjbE84K_g9mUgwUO8",
            "https://drive.google.com/uc?export=view&id=1d8ZR8Y4Kw7XXDpHEGuUbbcxhTrLBGdsn",
            "https://drive.google.com/uc?export=view&id=1G9oA75UMh2F7qSwucwccY0BDVBZp5AWl",
            "https://drive.google.com/uc?export=view&id=1Fj_XHiA3uDaRqC7LvORXo_ueI5CNkMNO",
            "https://drive.google.com/uc?export=view&id=1thcefhcZ3U9PB5QGyofLuJEyKgA83N_t",
            "https://drive.google.com/uc?export=view&id=1R_vfymtgA94h-NLU9-CAFx5Wqq7nGnD7",
            "https://drive.google.com/uc?export=view&id=1eyDQ0olN0sEMEbxBqk87P5nAV-Hs8SwI",
            "https://drive.google.com/uc?export=view&id=1-yNfKtPhB-TQnPFzDhms3Si_rzZH2grl",
            "https://drive.google.com/uc?export=view&id=1s6gwcCRbD_GYpIZX6s-uNbdipqNkaN2X",
            "https://drive.google.com/uc?export=view&id=1tqRKxMm5yowjjO8lAlEhmantY-3mEd7G"
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
                "kesan": "Abangnya baik, tipe orang yang bertanggungjawab kalau udah dikasih beban tugas",  
                "pesan": "Lancar terus bang buat studinya, hwaiting!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": " Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya baik, gak sombong dan sedikit moodyan mungkin orangnya",  
                "pesan": "SEMANGAT KAK buat kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main badminton sama Yosep",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan baik dan tidak sombong pula",  
                "pesan": "Semoga bisa terus bertanggungjawab dalam segala hal apapun itu dan bisa seimbang juga waktu istirahatnya"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton f1",
                "sosmed": "@ali_parisi3",
                "kesan": "Bang ali baik, ramah, kelihatan orang yang cukup teliti juga",  
                "pesan": "Semoga kedepannya abang selalu dikelilingi orang-orang yang baik dan dimudahkan dalam segala hal akademik"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "123450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nguras kolam lele",
                "sosmed": "@cacalvra",
                "kesan": "Kak jacinda baik, lucu, dan murah senyum",  
                "pesan": "Semoga tetap jadi pribadi yang menyenangkan ya kak dan sukses selalu"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Ternak ayam",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Awal lihat bang ghiyats agak shock karena tinggi banget kayak tiang listrik",  
                "pesan": "Semangat bang, semoga selalu baik-baik saja"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": " 124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya flat banget mukanya, terus agak irit ngomong, tapi overall abangnya baik",  
                "pesan": "Makin semangat bang"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": " 124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live Tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Bang bryan baik banget pake banget, orangnya gaenakan gitu, dan bener-bener bertanggungjawab", 
                "pesan":"Semoga perjalanan abang, baik itu perkuliahan maupun organisasi selalu diberkati Tuhan"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": " Live tiktok bareng Bryan",
                "sosmed": "@indahjuliaa",
                "kesan": "Kak indah cantik, tidak sombong dan tipe orang yang pengertian",  
                "pesan":"Semangat kak kuliahnya!"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Diving",
                "sosmed": "@afdall.03",
                "kesan": "Bang afdal baik, dan ramah",  
                "pesan":"Lancar terus bang buat studinya, lancar sampai akhir"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": " 124450131",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Persis",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang dafa keren, baik, dan juga ramah",  
                "pesan": "Makin semangat bang dalam segala hal"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": " 124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya baik, tidak sombong dan mudah diajak komunikasi",  
                "pesan": "Semoga lancar jaya kak segala urusan perkuliahannya"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lari",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Pembawaan kakaknya kelihatan sederhana, dan tetap kasih kesan yang baik",  
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
                "kesan": "Abangnya ramah, punya karakter yang unik dan menarik",  
                "pesan": "Semoga kedepannya semua hal-hal baik datang menghampiri abang"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakaknya kasih first impression yang baik karena seramah itu, nada bicaranya juga lembut",  
                "pesan":"Semoga sukses dalam perjalanan akademik dan organisasinya ya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls= [
            "https://drive.google.com/uc?export=view&id=1MYhxtvLgflXdauXUDFHlgDsTR1W8GLK1",
            "https://drive.google.com/uc?export=view&id=10CNpd7bGQI6N3I6czwxRlMVuHW5ya6ej",
            "https://drive.google.com/uc?export=view&id=10dN1NaakLQAcqMnyoH-RalfUDsABKTw7",
            "https://drive.google.com/uc?export=view&id=1z3B0IPVLYC6SfJaIeMhzSCK5xfDoWxo_",
            "https://drive.google.com/uc?export=view&id=1KA5SxFnHortylK2gXLEB9FdHuRIN0Pr9",
            "https://drive.google.com/uc?export=view&id=1MWo5JEAOF90TpEktwYwpcGTRxMYcSd8L",
            "https://drive.google.com/uc?export=view&id=1vKNsWlTbUf0R3v0fVosVfA_LvlgnYcPR",
            "https://drive.google.com/uc?export=view&id=14piLFvr1IHHF8sALthFUVru2ifBq4wCk",
            "https://drive.google.com/uc?export=view&id=1nthqrTv9oN1Ti2Lacumg_NKjJDNhnIlv",
            "https://drive.google.com/uc?export=view&id=1p39fiRVZjpO9qadZfo6P3rlFvon4XdvD",
            "https://drive.google.com/uc?export=view&id=1imQ-8eXDeJgxmUSodU4a3yskCQoftDgI",
            "https://drive.google.com/uc?export=view&id=1JQPijVIRmSWnYUugCMr5cSHG4_oYwIFv",
            "https://drive.google.com/uc?export=view&id=189DGFSPeJAJybc-OjWhBqBZvLCrr-liQ",
            "https://drive.google.com/uc?export=view&id=1fDqONXm2EWi4HUCl6Lvrp_S8JYJRz8N0",
            "https://drive.google.com/uc?export=view&id=1wta-PtdSFkvkXA7jXh8g0iax_FCDEaLj",
            "https://drive.google.com/uc?export=view&id=1IpuqPS1oWfUc7pWnDg36adTe7MXj-1Ye",
            "https://drive.google.com/uc?export=view&id=19ebMqLYYmBS4TKZLx9JD9hX00TzZNhb_"
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
                "kesan": "Kak arienta orangnya tegas, tapi overall kakanya baik dan bertanggungjawab",  
                "pesan":"Semoga selalu semangat dan lancar terus studinya kak!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21,5 tahun",
                "asal": "Kuala Lumpur",
                "alamat": "Samping kost kak arienta",
                "hobbi": "Pacaran",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya kelihatan ramah dan asik",  
                "pesan":"Semoga selalu urusannya dilancarkan dan selalu bahagia ya, kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "30 Tahun",
                "asal": "Rumah Sakit",
                "alamat": "Belakang Wardat",
                "hobbi": "Kayak irfan",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas, berwibawa, pembawaannya tenang dan tidak aur-auran",  
                "pesan":"Semoga ilmu yang abang kasih selama ini bisa bermanfaat bagi banyak orang"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "17 tahun",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek Orang",
                "sosmed": "@desmanhal",
                "kesan": "Bang desman baik, mudah diajak bercanda, friendly, menyenangkan, dan asik",  
                "pesan":"jangan lupa istirahat ditengah kesibukannya bang, lancar studinya!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20 Tahun",
                "asal":"Lampung Tengah",
                "alamat": "Sebelah kost jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi keren meskipun agak serem, punya banyak energi, kayak tiap hari energinya itu terus full ga pernah habis",  
                "pesan":"Semangat bang kuliahnya, semoga apapun yang sekarang abang lagi jalanin, semuanya berakhir baik"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450008",
                "umur": "10 Tahun",
                "asal":"Di Bandung",
                "alamat": "Kamar haikal",
                "hobbi": "Goreng ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake kelihatan sederhana, tapi tetap berkesan, overall abangnya baik",  
                "pesan":"Semoga selalu diberikan kesehatan dan lancar buat setiap aktivitas akademiknya bang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21 Tahun",
                "asal": "Rahim ibu",
                "alamat": "Diatas kost jemar",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang caesar kelihatan orangnya disiplin, bertanggungjawab, dan ada jiwa kepemimpinan yang baik",  
                "pesan":"Semoga studi abang lancar, terus semua rencana kedepannya bisa tercapai"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "20 tahun",
                "asal": "Debu Tanah",
                "alamat": "Sebelah pasar",
                "hobbi": "Ngegiring anak ayam",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak euodia punya semangat yang tinggi, kakaknya juga tegas tapi tetap kasih kesan yang baik",  
                "pesan":"Semoga sukses selalu kak, entah itu dalam akademik ataupun organisasi!"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "17 Tahun",
                "asal": "Batam",
                "alamat": "Sebelah kost jemar atau kak arienta",
                "hobbi": "Ngurus pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal tegas, agak seram, kalem dan kelihatan serius tapi tetap approachable",  
                "pesan":"Semoga kuliahnya lancar, hal-hal baik datang menghampiri dan tidak kekurangan satu apapun"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18 Tahun",
                "asal": "Kampung Orang",
                "alamat": "Nomaden",
                "hobbi": "Duduk sebelah henry",
                "sosmed": "@dellaansaftr",
                "kesan": "Awal ketemu, kakaknya punya kesan yang positif dan menyenangkan, kakanya juga cantik dan stylish",  
                "pesan":"Semoga sukses raih cita-citanya kak"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Depan Pemancingan",
                "hobbi": "Ngoleksi ayam warna warni",
                "sosmed": "@queentanaabila",
                "kesan": "Awal lihat kak Queenta sekilas mirip kak sekar, tapi sekarang udah gak lagi",  
                "pesan":"Tetap semangat kak menjalani perkuliahannya!"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19 Tahun",
                "asal": "Lampung",
                "alamat": "Teluk",
                "hobbi": "Main game",
                "sosmed": "@azzelytn",
                "kesan": "Kak azzelya cantik, baik, ramah, mudah senyum, dan pengertian",  
                "pesan":"Lancar kak buat studinya, hwaiting!"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21 Tahun",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakaknya asik, tidak sombong, dan mau diajak foto berulangkali jadi kesannya ramah",  
                "pesan":"Semangat kak menjalani hari-hari perkuliahannya"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "18 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost haikal",
                "hobbi": "Gembala",
                "sosmed": "@jemarrro",
                "kesan": "Bang jeremi baik, kelihatan humoris dan bisa mencairkan suasana",  
                "pesan":"Semoga selalu sukses dalam perkuliahan, organisasi, dan kehidupan sehari-hari"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19 tahun",
                "asal": "Lampung tengah",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila cantik, pembawaannya kalem waktu pertama kali ketemu",  
                "pesan":"Semoga bahagia selalu kak dan terus berkembang di sains data sampai akhir nanti"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20 Tahun",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang rafli baik, ramah, senyumnya manis, salah satu orang batak yang ganteng yang pernah kutemui",
                "pesan":"Semangat bang kuliahnya, tetap keren, lancar jaya buat semua urusannya"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Tidur",
                "sosmed": "@avi.nhr",
                "kesan": "Kakaknya mini, imut, dan juga lucu",   
                "pesan":"Semoga semangat selalu menjalani hari-harinya dan sukses terus, kak"# 1
            }      
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TjxjPjGBqvsJ4u_RBdGkRbudoblODHuc",
            "https://drive.google.com/uc?export=view&id=17gFJfnkiCebHvvXAGSOzomjX94xjEn9i",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1PJQnmcchswmw-E2IyEpC7zEtUUAF_jhu",
            "https://drive.google.com/uc?export=view&id=1Jbo1bfKpBR6QW9RSFUUk3dxgYGrho4TG",
            "https://drive.google.com/uc?export=view&id=1oq88SRS1vz6PAfQq0CIwVfd1yqhFbmUk",
            "https://drive.google.com/uc?export=view&id=1bdzPLKoPKsNkvrNhvqX0K-QU3oZRjdYw",
            "https://drive.google.com/uc?export=view&id=1siEcd4Ea5J0JIEuuprjp_1ZxL-iLKTym",
            "https://drive.google.com/uc?export=view&id=1-Ngm2IK78qiJXWFNjLiioCtXrxAVGN4M",
            "https://drive.google.com/uc?export=view&id=1Duezu6tYl23isifiC1eTRadNfB-ZSwoF",
            "https://drive.google.com/uc?export=view&id=1c-dkjZUEjMyE1q_nJRaeYF0EuFRM_cXl",
            "https://drive.google.com/uc?export=view&id=1g_z8UMLh86AbCONZpt4bUwo7SS0vO6b6",
            "https://drive.google.com/uc?export=view&id=1EetSLDKAwgL8Iw360ESQphL9vBioYe3A",
            "https://drive.google.com/uc?export=view&id=1ZfPtS8g4U8k7OXI1qV6OK7w4AdU06Y1P",
            "https://drive.google.com/uc?export=view&id=1_mFkl8HcYHnDGNdVmGT2CKTJVZoiwRIK",
            "https://drive.google.com/uc?export=view&id=1t3BYgeXfUKcGQtK4Qc9pyZ3WIvirnaPQ",
            "https://drive.google.com/uc?export=view&id=1E6NFGW2V0qTDN784kl0zOIOTcP7MEuZe",
            "https://drive.google.com/uc?export=view&id=1wKkzoqullBEtZczTe_BWyXTMBdn_MV9V",
            "https://drive.google.com/uc?export=view&id=1CkW-LB1gtjP5wB7Q1QCHbHPgrIodR5W_",
            "https://drive.google.com/uc?export=view&id=1gWwM-vs9P3sw5LRQ4A4SFKPrqXWxGxQE",
            "https://drive.google.com/uc?export=view&id=1NHFyHM4MwSP2PfVVvMJ3eA-RNP84odDF",
            "https://drive.google.com/uc?export=view&id=1QrHJEkon15RarUjblpT2Obsm-cwKOTw9"
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
                "kesan": "Bang fabio keren, pintar, kelihatan bijak juga, punya energi yang positif",
                "pesan": "Semangat buat TA nya nanti bang, semoga semua prosesnya dilancarkan dan tiap usaha yang udah dilakukan bisa kasih hasil yang baik"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya lucu, imut, ceria dan punya energi yang bikin suasana bisa lebih hidup",
                "pesan": "Tetap jadi diri sendiri dan semoga selalu dikelilingi orang-oran yang baik ya kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "Abangnya keren, tiap perjalananya beneran menginspirasi",
                "pesan": "Rest in Peace bang fadil, semua kenangan baik tentang abang akan selalu tetap hidup di hati kami"
            },
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Keren bang proker PIKA nya, bener-bener keren dan kelihatan berwawasan luas serta punya semangat belajar yang tinggi",
                "pesan": "Semangat nanti TA nya bangg, semoga tiap usaha dan kerja kerasnya membuahkan hasil yang memuaskan!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Pinter banget, kelihatannya abangnya teliti dan serius dalam mengerjakan sesuatu",
                "pesan": "Semoga ide-idenya terus bisa dikembangkan dan diwujudkan menjadi sesuatu yang bermanfaat"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Abangnya punya pembawaan yang tenang dan meyakinkan, kelihatan disiplin sama bertanggungjawab",
                "pesan": "Semoga tetap konsisten dalam mengejar target dan lancar terus bang studinya"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakaknya baik, cantik, dan pembawaan kakaknya juga santai, gak terlalu serius-serius amat",
                "pesan": "Kaka semangat kuliahnya yaa, semoga bisa seimbang antara akademik, organisasi, dan kehidupan sehari-hari kakak!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakanya lucu-lucu gitu, baik juga dan gak sombong kalau diajak foto",
                "pesan": "lancar kak studinya!"
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
                "kesan": "kak yulia baik, gak semini itu ternyata, dan murah senyum",
                "pesan": "Semoga kuliahnya lancar-lancar terus ya kak sampai akhir"
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
                "pesan": "tetap jadi orang baik dan asik ya kak!"
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
                "pesan": "Semangat kak fadya buat kuliahnya, love banyak banyak"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Badminton",
                "sosmed": "@_loviaa",
                "kesan": "Kak lovi baik, ramah juga, tipe teman yang bakal ada kalau kita lagi butuh",
                "pesan": "Semangat kak lovi buat kuliahnya, semoga dapat ip yang terbaik ya kak"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang keren, meskipun wajahnya agak flat but gwencahana",
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
                "kesan": "Fisrt impression ku ke kaka beneran kagum dan jujur wow banget",
                "pesan": "Kak faiza beneran defenisi keren itu sendiri, bisa tetap aktif dalam organisasi dan akademik juga oke banget, salute"
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
                "kesan": "Keren, tidak petakilan,dan sedikit jahil",
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
                "kesan": "Beneran keren, pinter, pinternya itu beneran yang sepinter itu",
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
                "kesan": "Pengalaman abang bener-bener menginspirasi banget, suka!",
                "pesan": "Semoga pengalaman dan perjalanan abang selama kuliah bisa jadi isnpirasi bagi tiap banyak orang!"
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
                "pesan": "Semoga tetap semangat bang menjalani hari-hari sebagai ketang 24! keren"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LNJNbGF0k-nlkui9OhqSOlFTNNYlNQ8y",
            "https://drive.google.com/uc?export=view&id=1QvQ1Wp-4eVUK1i3gsOq_CEqfWpwZahrX",
            "https://drive.google.com/uc?export=view&id=1eVxsAvuIm2mUHnDDy1jfTdwZdaIopTDj",
            "https://drive.google.com/uc?export=view&id=1UGvEnlOE3XAPO4C7KYVybFVqmHx2ETV5",
            "https://drive.google.com/uc?export=view&id=1i66Ynjay2yaDIISLEEyDuI3rqRDoqfEK",
            "https://drive.google.com/uc?export=view&id=1lF9M0q0ij9ExHFBOt5JAKnopCYGftJE0",
            "https://drive.google.com/uc?export=view&id=1kAO1wHNulAv4P0RYX-i1FWw-H4zYnlQb",
            "https://drive.google.com/uc?export=view&id=1bRmZrd5AVkyoueTCJOwYVsqG6toaiJ7l",
            "https://drive.google.com/uc?export=view&id=1xVLF0t6w-1UwEEZGkRl2-38O_620YrNg",
            "https://drive.google.com/uc?export=view&id=1i8S880GvKBfe8o_awW0CLRD4HVPujQEf",
            "https://drive.google.com/uc?export=view&id=16nru7lJzYFE0hb5PYjWCEwGm-JtbwHxm",
            "https://drive.google.com/uc?export=view&id=1xnycIkQrIDHlAtovuUaBIRP4fxoiGPFT",
            "https://drive.google.com/uc?export=view&id=1wJDbpXSqynuTZPOqWpzmIcbhRhdtfYy6",
            "https://drive.google.com/uc?export=view&id=1KYazN5o8dpZb_JSKWhen4wHxYVIAutcR",
            "https://drive.google.com/uc?export=view&id=14WQ8jmnj1sw2qoKgs5SQb8jhQ3rGX9OV",
            "https://drive.google.com/uc?export=view&id=1TOyyU2326F26vYk9GydAVgeOAp5HE5jP"           
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
                "kesan": "Bang haikal wow, ramah, keren, freestyle banget, enak diajak menggosip, okelah intinya",  
                "pesan":"Semangat bang nanti TA nya, lancar-lancar yang bang studinya apalagi udah mau akhir gini"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21 Tahun",
                "asal": "Untung suropati",
                "alamat": "..",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya gemas dan cantik banget, ramah, dan bener-bener tenang dan santai gitu",  
                "pesan":"Semangat terus kak, semoga apa yang diharapkan bisa terwujud"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "11",
                "asal": "Kisaran",
                "alamat": "Untung",
                "hobbi": "NMenyapa satpam ITERA",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak hanna cantik, baik, sifat keibuannya juga kelihatan",  
                "pesan":"semangat kak na buat TA nya nanti, semoga semua dilancarkan dan kaka bahagia selalu ya"# 1
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
                "nama": "Ahmad Farhan Ghani",
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
                "kesan": "Kak cerine baik, tipe-tipe orang yang suka kerja mepet deadline ",  
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
                "kesan": "Bang jay baik, ramah, ada jiwa-jiwa pemimpinnya gitu, keren juga tulangku ini",  
                "pesan":"Semangat bang kuliahnya, semoga nilai uts uas nya dapat hasil yang baik dan sesuai apa yang abang harapkan"# 1
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
                "kesan": "Bang rozak kelihatan dewasa, terus disiplin waktu juga orangnya",  
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
                "kesan": "kak teresa baik, murah senyum, dan rajin banget gerejanya, pasti tiap minggu ketemu kak tere di bus tayo itera",  
                "pesan":"Tetap ceria kak, semoga tetap setia dan jadi anak Tuhan terus yaak "# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 Tahun",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Masak",                
                "sosmed": "@audina_",
                "kesan": "Kakaknya baik, gak sombong, gak pelit, dan mau bantu orang kalau kakanya ngelihat",  
                "pesan":"Semoga dilancarkan kak setiap urusan kuliahnya kak"# 1
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
                "kesan": "Kak gustin love banget, suka sama kepribadian kak gustin",  
                "pesan":"Semangat terus kak"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20 Tahun",
                "asal":"Sematera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu",                
                "sosmed": "@Muhvinz_",
                "kesan": "Abangnya baik, ramah, dan terlihat pendiam",  
                "pesan":"Semangat bang kuliahnya, lancar terus untuk urusannya!"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama aqila",                
                "sosmed": "@snasaa._",
                "kesan": "Kak bina baik, mentor paling baik, pengertian, bener-bener membantu Anova dan selalu membersamai kita juga, kak bina panjang sabar, humble, dan beneran sebaik itu, Anova gak pernah dibiarkan berjalan sendiri, love banyak-banyak buat kak bina",  
                "pesan":"Kak bina ceria terus ya, sayang kak bina banyak-banyak, semoga nilai uts dan uas kakak bisa dapat yang terbaik sesuai dengan apa yang udah kakak usahakan"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()
# Tambahkan menu lainnya sesuai kebutuhan
