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
            "Bason",
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
            "nav-link-selected": {"background-color": "#3FBAD8"},
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

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bZ70IqPONIoXJpJcRVRuu5pKkn4A_m-q",
            "https://drive.google.com/uc?export=view&id=1zCjI8tSxAlLXw_ozqqXIuGDpauHd-Fdm",
            "https://drive.google.com/uc?export=view&id=1_1KAjKjUSeY-UX_dp2rj1sF6PMlSkkO0W1",
            "https://drive.google.com/uc?export=view&id=1k36lXwVGs5ljYjl_dcKK1qPr6iBm8GHS",
            "https://drive.google.com/uc?export=view&id=1UVoy2vf21D-gJhDPapyJB5EPoEvvBZd3",
            "https://drive.google.com/uc?export=view&id=1IpRAQft9HxUmxzfYb71Us80Z_bU-3KWH",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Keren dan berwibawa, keren banget manage waktunya",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad  Aqil Ramadhan",
                "nim": "1223450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil111",
                "kesan": "Abangnya chill bangett, dan memperoleh banyak ilmu dari sekjen",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya seruuuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaaemdhn",
                "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            "https://drive.google.com/uc?export=view&id=1stIJh8GpzoJtJPaFnaIA5NlwuqjepMMw",
			"https://drive.google.com/uc?export=view&id=1BUFWaShMmF_XB0yozNhncdYolsaCVSJh",
            
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha",  
                "pesan":"Semangat bang TA nyaa, semoga dilancarkan semuanya dan lulus tepat waktu ya bangg. Anak magang baleg selalu mendoakan yang terbaik untuk ayah dido"# 1
            },
            {
                "nama": "Juesi Aprilia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marvel",
                "sosmed": "@j_eesie",
                "kesan": "GEMASSSSS! beneran imut kakanya dan seru banget dengerin storytelling ka juee, karena kayak sivia the catchup club cara kaka ngomong",  
                "pesan":"Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupun api Baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Pinter bnaget abangg, tips and trik mapres bangg",  
                "pesan":"Semangat kuliah dan TA nya, semoga dimudahkan seluruh urusannya, aamiin!"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD musang",
                "sosmed": "@me._kael",
                "kesan": "Lucu banget jokes jokes abangnyaa",  
                "pesan":"Semangat terus kuliah dan organisasinya!"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "18",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Imutt sekali kakanyaaa",  
                "pesan":"Semangattt kaa kuliahnyaa, kaka imut balegg"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip chill banget orangnyaa dan seruu",  
                "pesan":"Semangat terus bang kuliahnya dan semoga dimudahkan TA nya ya banggg, Aamiin!"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Public speakingnya bagus, aku dukung kaka jadi the next kadiv komisi 2 #YIPPIE",  
                "pesan":"Semangat kaa kuliah dan organisasinyaa!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "24",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu dan gemas bangettt",  
                "pesan":"Semangat ka menghadapi bang Ridhoo, semoga dilancarkan semua urusannya kaaa!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Keren dan berwibawa",  
                "pesan":"Semangat bang kuliahnyaaa!"# 1
            },
            {
               "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Lucu, gemas, tapi tegas",  
                "pesan":"Semangat kaa kuliah dan organisasinyaaa!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Lucu abangnya, jokes jokesnya juga fresh",  
                "pesan":"Semangat abang kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Tegas tapi chill juga",  
                "pesan":"Semangat terus ka kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Lemah lembut sekaliii",  
                "pesan":"Semangat kaa TA dan kuliahnyaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Bason":
    def Bason():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cpgYi7s-PdGAJcCCxZY_ynTQlFfwI_78",
            "https://drive.google.com/uc?export=view&id=1VfWOJ3OAUUL_wMCSB0eNvrxUMXh3ZxXI",
            "https://drive.google.com/uc?export=view&id=1a86FT6r-kQyawn6dPrKqGIKD1z1umKOD",
            "https://drive.google.com/uc?export=view&id=1pId4s2cr_-1IrV_FAGjhmjhpRWOhMbXu",
            "https://drive.google.com/uc?export=view&id=1mVkpAjGRe05SDIypyCEM1cE5Km5WoIVe",
            "https://drive.google.com/uc?export=view&id=1TzkMBCGPxVWAOUO0E-hfhrjgIoJwmJXV",
            "https://drive.google.com/uc?export=view&id=1lqQI5rM8uaPNJleb1KpNqZgzO84r9TR1",
            "https://drive.google.com/uc?export=view&id=194GlwFAucF-1pLT3hBXn3vPbdqZSiUky",
            "https://drive.google.com/uc?export=view&id=1_X8n4YUEKc8fVny5L7zsc05Io9rAgd7C",
            "https://drive.google.com/uc?export=view&id=1SlIDJy0kb_KOBd3_pubon7R0R5Wxfhw6"
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": "Inspired girl, beneran keren bangettttt",  
                "pesan": "Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": "Duta melet, lucuuuu",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Chill banget kakanyaa",  
                "pesan":"Semanagat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Sumpah style baju kakanya keren kerennn",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Welcome sekali abangnya, apapun pose yang diminta beneran diiyain #GEMAS",  
                "pesan":"Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Banyak ilmu mengenai Strategis dan Propaganda yg aku peroleh dari kakaaa",  
                "pesan":"Semangat kak TA nyaa, semoga dimudahkan jalannya yaa!!"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Modis dan keren banget style stylenyaa, dan imup bangett",  
                "pesan":"Semangat terus kuliahnya kaa!"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "kece euyyy, style abang beneran keren bangett",  
                "pesan":"Semangat terus bang kuliah dan organisasinya!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Welcome sekali kakanyaaa, dan cara penyampaian materinya juga mudah dipahami",  
                "pesan":"Semangat terus kuliahnya kaa!!"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Gemass kakanyaa",  
                "pesan":"Semangat terus kaa kuliahnyaa!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Bason() 

#SSD
if menu == "Departemen SSD":
    def Ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Qi-nHIYW3kgrZY_l_8bLNtNt-zMGIl4X",
            "https://drive.google.com/uc?export=view&id=1Tn-Ui69HGudGWGM31LoOmSzirp32Co_u",
            "https://drive.google.com/uc?export=view&id=1KxVCSGEbXlnkyXoFj-7KMWLGkn-QanBd",
            "https://drive.google.com/uc?export=view&id=1aVFCDzb6Z_Nt5qDpe-zcZrHpqrkEjgRS",
            "https://drive.google.com/uc?export=view&id=1wLZCDzX6pajeFYr9Qs78TS4iP-nuOv4s",
            "https://drive.google.com/uc?export=view&id=1Rf9K_PgxBv2CXjephelQ9kIWyJdY8Nqq",
            "https://drive.google.com/uc?export=view&id=1ta4lE-5QQb-1jTXRM3Z_SAfeL-JCTQ7e",
            "https://drive.google.com/uc?export=view&id=1GT0y_EUGXgsxhv_JTPHvm8WEk3kmgTPQ",
            "https://drive.google.com/uc?export=view&id=1Y57H8CIBLlF_VkmlLJN7KtzUKxqkeS7l",
            "https://drive.google.com/uc?export=view&id=1PPZhaSYsWZuwFytIN4XQmAIGwkJiW83E",
            "https://drive.google.com/uc?export=view&id=1jMylRFmw9M_m87mXnJC3PB1c2mA8e1Ud",
            "https://drive.google.com/uc?export=view&id=1ZOOGOX8RkLyww_jyeuqBMz-N8P0mo2r2"
        ]
        data_list = [
            # --- Pimpinan & Sekretaris ---
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450000",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            # --- Divisi Kemitraan ---
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            # --- Divisi Kewirausahaan ---
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Ssd()


# Minat dan Bakat
elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
            "https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
			"https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
			"https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
			"https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
			"https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
			"https://drive.google.com/uc?export=view&id=1X74cb1NXooum7dOixdb3zvyEwxNA65ro",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
            "https://drive.google.com/uc?export=view&id=1q9hxDbkF7lpwFusDeM39JGCBO5FtsXN2",
        ]
        data_list = [
		    {
		        "nama": "Kevin Antonio Junior",
		        "nim": "123450109",
		        "umur": "23",
		        "asal": "Sulawesi Tengah",
		        "alamat": "Panjang",
		        "hobbi": "Mancing",
		        "sosmed": "@kevinaja__",
		        "kesan": "Sangat menginspirasi dan memimpin dengan baik",
		        "pesan": "Semangat terus kak!"
		    },
		    {
		        "nama": "Gusti Putu Ferazka Dhiyamika",
		        "nim": "123450046",
		        "umur": "21",
		        "asal": "Bekasi",
		        "alamat": "Way Dadi",
		        "hobbi": "Mendaki",
		        "sosmed": "@ferazkaa",
		        "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
		        "pesan": "Sukses selalu kak!"
		    },
		    {
		        "nama": "Ali Aristo Muthahhari Parisi",
		        "nim": "123450088",
		        "umur": "21",
		        "asal": "Lampung Timur",
		        "alamat": "Gang Sakum Belwis",
		        "hobbi": "Nonton F1",
		        "sosmed": "@ali_parisi3",
		        "kesan": "Keren dan selalu memberikan arahan yang jelas",
		        "pesan": "Semangat menjalankan tugasnya kak!"
		    },
		    {
		        "nama": "Ayu Andriani Parlina Wati",
		        "nim": "124450058",
		        "umur": "20",
		        "asal": "Lampung Barat",
		        "alamat": "Airan",
		        "hobbi": "Belajar + menghitung uang",
		        "sosmed": "@aayuandriani_",
		        "kesan": "Sangat ramah dan aktif berkontribusi",
		        "pesan": "Tetap semangat dan sukses terus!"
		    },
		    {
		        "nama": "Dafa Elpriza",
		        "nim": "124450131",
		        "umur": "21",
		        "asal": "Bekasi",
		        "alamat": "Way Kandis",
		        "hobbi": "Jogging",
		        "sosmed": "@dafaelpriza_",
		        "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
		        "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
		    },
		    {
		        "nama": "Juwita Sari",
		        "nim": "124450066",
		        "umur": "19",
		        "asal": "Lampung Barat",
		        "alamat": "Pemda",
		        "hobbi": "Mancing",
		        "sosmed": "@ju.juwitaaa_",
		        "kesan": "Sangat baik dan murah senyum",
		        "pesan": "Semangat terus kuliahnya!"
		    },
		    {
		        "nama": "Muhammad Afdal Luthfi",
		        "nim": "124450047",
		        "umur": "19",
		        "asal": "Lampung Tengah",
		        "alamat": "Jl. Pulau Damar",
		        "hobbi": "Memantau dl tugas",
		        "sosmed": "@afdall.03",
		        "kesan": "Sangat bertanggung jawab dan fokus",
		        "pesan": "Semangat terus kakak!"
		    },
		    {
		        "nama": "Salsabila Nazwa Putri",
		        "nim": "124450002",
		        "umur": "20",
		        "asal": "Metro",
		        "alamat": "Korpri",
		        "hobbi": "Nongkrong di kopken",
		        "sosmed": "@slbnzw_",
		        "kesan": "Sangat asik dan ceria",
		        "pesan": "Tetap semangat kuliahnya ya kak!"
		    },
		    {
		        "nama": "Muhammad Ridwan",
		        "nim": "123450091",
		        "umur": "21",
		        "asal": "Lampung Tengah",
		        "alamat": "Belwis",
		        "hobbi": "Badminton",
		        "sosmed": "@mridwaan_22",
		        "kesan": "Sangat mengayomi dan membimbing dengan sabar",
		        "pesan": "Semangat terus memimpin divisinya kak!"
		    },
		    {
		        "nama": "Andra Ilham Bintang",
		        "nim": "124450060",
		        "umur": "18",
		        "asal": "Sumatera Selatan",
		        "alamat": "Kotabaru",
		        "hobbi": "Main rubik",
		        "sosmed": "@andra.lhm",
		        "kesan": "Sangat kreatif dan pintar",
		        "pesan": "Sukses selalu kuliahnya!"
		    },
		    {
		        "nama": "Bryan Paskah Telaumbanua",
		        "nim": "124450003",
		        "umur": "20",
		        "asal": "Nias",
		        "alamat": "Belwis",
		        "hobbi": "Live tiktok",
		        "sosmed": "@bryantel_",
		        "kesan": "Sangat menghibur dan ramah",
		        "pesan": "Semangat terus berkarya kak!"
		    },
		    {
		        "nama": "Ghiyats Thabularasa Meardhy",
		        "nim": "124450067",
		        "umur": "17",
		        "asal": "Surabaya",
		        "alamat": "Kemiling",
		        "hobbi": "Nanem Sawit",
		        "sosmed": "@meardhy_ghiyats",
		        "kesan": "Sangat unik dan bersemangat",
		        "pesan": "Tetap semangat dan sukses selalu!"
		    },
		    {
		        "nama": "Indah Julia Mawar Pratiwi",
		        "nim": "124450055",
		        "umur": "20",
		        "asal": "Pringsewu",
		        "alamat": "Airan",
		        "hobbi": "Bengong",
		        "sosmed": "@indahjuliaa",
		        "kesan": "Sangat baik dan bersahabat",
		        "pesan": "Sukses terus perkuliahannya kak!"
		    },
		    {
		        "nama": "Jacinda Kesya Alvara",
		        "nim": "124450023",
		        "umur": "18",
		        "asal": "Kalimantan Barat",
		        "alamat": "Korpri",
		        "hobbi": "Nyapu depan gacoan",
		        "sosmed": "@cacalvra",
		        "kesan": "Sangat ceria dan menyenangkan",
		        "pesan": "Semangat terus ya kak!"
		    },
		    {
		        "nama": "Muhammad Rafka",
		        "nim": "124450089",
		        "umur": "20",
		        "asal": "Padang",
		        "alamat": "Kotabaru",
		        "hobbi": "Bangun pagi",
		        "sosmed": "@muhammdrafka_",
		        "kesan": "Sangat disiplin dan dapat diandalkan",
		        "pesan": "Sukses selalu buat perkuliahannya!"
		    }
		]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()
