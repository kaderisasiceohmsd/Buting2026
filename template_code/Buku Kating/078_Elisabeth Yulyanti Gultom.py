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
