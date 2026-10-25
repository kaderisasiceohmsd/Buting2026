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
            "https://drive.google.com/uc?export=view&id=1erwcdW2OSk2EHluafxh7g_sq0Rh9jnPo",
            "https://drive.google.com/uc?export=view&id=1KYhvRbnMIO0S2S4FSm5lvo5qEaFoc23Z",
            "https://drive.google.com/uc?export=view&id=17er9A0OVeDNNyJCFLd7xrBklWmnzGi5T",
            "https://drive.google.com/uc?export=view&id=1EJrwajIoDoLCzc0sOAYtv1qGDaZIHzH4",
            "https://drive.google.com/uc?export=view&id=1BcFZFrEuzuTjZ6V0xtOspubiKB-8XY7s",
            "https://drive.google.com/uc?export=view&id=1QG2bT1IjIT1D2sTe91cH_ojxsei1lhSx",
            
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Bang Ginda berwibawa sekali,nampak banget aura sibuk nya.",  
                "pesan":"Semangat nge TA sambil mengkepalai Himpunan bg."# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xX5xZzfgo0YDPwwbrSFrKi7lgwQ-kVdv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_iPcLG7nq0NQxMILOrG9J1O8RTB1hfft",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "23",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "14450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },                                                       
            
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bfeoLdTPLcR84j0tNaTIqoQScIAn-5M3",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket pantai",
                "alamat": "Samping kos capo",
                "hobbi": "ngerjain tugas",
                "sosmed": "@arientakhsnl_",
                "kesan": "-",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@wielhawn",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@helmy_inst",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },  
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": " Desman Velius Halawa",
                "nim": "123450114",
                "umur": "21",
                "asal": "Nias",
                "alamat": "GH Raya",
                "hobbi": "Lompat Batu",
                "sosmed": "@desmannhal_",
                "kesan": "Abang terbaiklah menurutku,selalu membimbing di prodi,asrama,dll.",
                "pesan": "Semangat kuliahnya bg,semoga terkabul lulus tepat waktunya."  # 1
            },
            {
                "nama": " Rafli armansyah Tambunan",
                "nim": "12450007",
                "umur": "20",
                "asal": "Helvetia",
                "alamat": "Samping kos Afdal"   ,
                "hobbi": "Nonton Film",
                "sosmed": "@dearmkiff",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
         {
                "nama": "Jeremi Marolop",
                "nim": "124450111",
                "umur": "16",
                "asal": "Setia Budi,Medan",
                "alamat": "Samping kos Haikal"   ,
                "hobbi": "Cabutin bulu Rafli",
                "sosmed": "@jemarrro",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },                                                       
            
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1K-BWBGPPPaX3Oj6uyr3JKQuqzFzeyeJb",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "1234501014",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biyokcb",
                "kesan": "-",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya ramah banget!!",
                "pesan": "Semangat terus bang!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget!!",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik banget!!",
                "pesan": "Semangat terus bang!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya baikk banget!!",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "Abangnya baik banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Msake Up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()



    




# Tambahkan menu lainnya sesuai kebutuhan
