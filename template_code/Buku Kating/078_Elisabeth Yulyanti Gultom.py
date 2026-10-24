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
            "https://drive.google.com/uc?export=view&id=1lj__cv-LrevkF3jIjD2kQHkMXnhhT9N1",
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
                "pesan":"Semangat menjalani terus bang, semoga urusan kuliahnya diperlancar buat kedepannya"# 1
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kk",
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id="
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
            "https://drive.google.com/uc?export=view&id=1dQIsPUDrKNZ5qT3x2wfA-eqEVmBhw2YR",
            "https://drive.google.com/uc?export=view&id=1X5BW1V9-stpWzLQHZRASvC_Og1u8d7ZK",
            "https://drive.google.com/uc?export=view&id=1_ARir9YPvISTdBYI4VvhI3wWFLqeYbzz"
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
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id="
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
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
# Tambahkan menu lainnya sesuai kebutuhan
