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
            "https://drive.google.com/uc?export=view&id=1m1cQkaJpDncqJCJvfOf5dVOuzJMqdan0",
            "https://drive.google.com/uc?export=view&id=16-8EutSEIHVLuoxbcqpoh4dmPpIc_N5L",
            "https://drive.google.com/uc?export=view&id=12mmvbhn_a3CNZBp2-C1CNtnOM5Za_pja",
            "https://drive.google.com/uc?export=view&id=1hHcAzb2_cugwDJkKU4mVTVX7RfpvGPxU",
            "https://drive.google.com/uc?export=view&id=1mPC9ZSdw6bZhOXTJXaEfnf0Yw-u8ngK6",
            "https://drive.google.com/uc?export=view&id=1Y_tCuB9n0PNpex6mCtz-ch-LZTThztwv",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Saya melihat bang Fajar sebagai sosok pemimpin yang berwibawa dan tegas.  ",  
                "pesan":"Semoga bang Fajar selalu diberi kelancaran dalam menjalankan amanah dan tetap semangat dalam mengerjakan Tugas Akhirnya!! "# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya baik, asik dan memberikan kesan yang positif selama saya berinteraksi dengan bang Aqil.",  
                "pesan":"Semoga bang Aqil selalu diberikan kelancaran dalam menjalani perkuliahan dan tetap semangat dalam mengerjakan Tugas Akhirnya!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefffiidefi",
                "kesan": "Kak Efi orangnya ramah dan murah senyum.",  
                "pesan":"Semoga kak Efi selalu diberikan kelancaran dan semangat dalam mengerjakan Tugas Akhirnya!!"# 1
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
                "hobbi": "Bertemu Luluk",
                "sosmed": "@hafsafazilahh",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthhifiarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450020",
                "umur": "20",
                "asal":"Cambridge",
                "alamat": "GH",
                "hobbi": "wawancara",
                "sosmed": "@@imridhomanik",
                "kesan": "Bang Ridho orangnya pintar, banyak pengalaman, dan menginspirasi",  
                "pesan":"Semangat terus bang menjadi kabaleg bagi kami, dan semangat terus kuliahnya"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "1234450021",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengar lagu duhai sayang",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnya asik, baik, dan pengertian",  
                "pesan":"Semoga kak Jue sehat selalu, semangat, dan sukses di semua hall"# 1
            },
            {
                "nama": "Dharu Cahyo",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@exvoltas",
                "kesan": "Bang Dharu orangnya asik, keren, dan pintar apalagi exvoltas yang keren bangett",  
                "pesan":"Semangat PKM nya bang, semoga sukses dan menular ke kami"# 1
            },
            {
                "nama": "Ghifaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi Balam",
                "hobbi": "Ngopi tiap hari",
                "sosmed": "@gifarooo",
                "kesan": "Bang Ghifaro orangnya keren, kece, mantaplah pokoknyaa",  
                "pesan":"Semangat terus bang, semoga sukses kuliahnya dan semuanyaa"# 1   
            },    
            {
                "nama": "Wan Nazwa al Hasti Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Hafsa orangnya baik, ramah, dan keren banget",  
                "pesan":"Semoga kakak sehat selalu, sukses kuliah dan himpunannyaa"# 1   
            },    
            {
                "nama": "Siti Sarifah",
                "nim": "124450015",
                "umur": "18",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kak Siti kerenn, aku mau seperti kak sitii",  
                "pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Cibaduyut",
                "alamat": "Teluk Betung",
                "hobbi": "Makan Pedas",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik, keren, dan pintar, dan juga keren nyanyinya",  
                "pesan":"Semangat terus bang, semoga sukses dan sehat selalu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan koleksi figur",
                "sosmed": "@nagatse",
                "kesan": "Bang Jona orangnya keren, kece, absolute cinemaaa pokoknyaa",  
                "pesan":"Semoga sehat terus bang, semangat kuliahnya, gym nya jugaa"# 1   
            },    
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko keren banget, kayak adeknya ezra",  
                "pesan":"Semangat terus bang semoga sukses di baleg terus sampai tahun selanjutnya"# 1   
            },    
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@syt.rifah",
                "kesan": "Kak Siti kerenn, aku mau seperti kak sitii",  
                "pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "hobbi": "Nulis di Medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah orangnya asik, keren, berwawasan, dan keren sebagai senator",  
                "pesan":"Semangat terus kakak menjadi senat bagi kami, dan semangat terus kuliahnya"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "1234450021",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengar lagu duhai sayang",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnya asik, baik, dan pengertian",  
                "pesan":"Semoga kak Jue sehat selalu, semangat, dan sukses di semua hall"# 1
            },
            {
                "nama": "Dharu Cahyo",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@exvoltas",
                "kesan": "Bang Dharu orangnya asik, keren, dan pintar apalagi exvoltas yang keren bangett",  
                "pesan":"Semangat PKM nya bang, semoga sukses dan menular ke kami"# 1
            },
            {
                "nama": "Ghifaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Sukabumi Balam",
                "hobbi": "Ngopi tiap hari",
                "sosmed": "@gifarooo",
                "kesan": "Bang Ghifaro orangnya keren, kece, mantaplah pokoknyaa",  
                "pesan":"Semangat terus bang, semoga sukses kuliahnya dan semuanyaa"# 1   
            },    
            {
                "nama": "Wan Nazwa al Hasti Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Hafsa orangnya baik, ramah, dan keren banget",  
                "pesan":"Semoga kakak sehat selalu, sukses kuliah dan himpunannyaa"# 1   
            },    
            {
                "nama": "Siti Sarifah",
                "nim": "124450015",
                "umur": "18",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Kak Siti kerenn, aku mau seperti kak sitii",  
                "pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Cibaduyut",
                "alamat": "Teluk Betung",
                "hobbi": "Makan Pedas",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik, keren, dan pintar, dan juga keren nyanyinya",  
                "pesan":"Semangat terus bang, semoga sukses dan sehat selalu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan koleksi figur",
                "sosmed": "@nagatse",
                "kesan": "Bang Jona orangnya keren, kece, absolute cinemaaa pokoknyaa",  
                "pesan":"Semoga sehat terus bang, semangat kuliahnya, gym nya jugaa"# 1   
            },    
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko keren banget, kayak adeknya ezra",  
                "pesan":"Semangat terus bang semoga sukses di baleg terus sampai tahun selanjutnya"# 1   
            },    
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@syt.rifah",
                "kesan": "Kak Siti kerenn, aku mau seperti kak sitii",  
                "pesan":"Semangat terus kak, semoga sukses kuliahnya, sehat selalu, dan ya semangat terus kakk"# 1   
            },     
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
