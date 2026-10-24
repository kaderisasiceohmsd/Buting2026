import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64

st.set_page_config(layout="wide")

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Sembunyikan header bawaan Streamlit untuk tampilan full-screen yang bersih */
    [data-testid="stHeader"] {
        visibility: hidden;
    }

    /* Mengubah background utama menjadi gradasi (terang di kiri atas, gelap di kanan bawah) */
    .stApp {
        background: linear-gradient(to bottom right, #ff9a22, #e14627);
        color: white; 
    }

    /* Memberikan warna solid pada sidebar agar terpisah dari background gradasi */
    [data-testid="stSidebar"] {
        background-color: #bd411b !important; /* Warna oranye gelap */
    }
    
    /* Memastikan teks di dalam sidebar berwarna putih */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Memaksa SEMUA elemen teks di dalam tab menjadi putih */
    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: white !important;
    }
    
    /* Mengubah warna garis bawah pada tab yang sedang aktif agar senada */
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: white !important;
    }

    /* Animasi gambar bawaan Anda */
    .gambar-timbul {
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        cursor: pointer;
    }
    .gambar-timbul:hover {
        transform: translateY(-8px) scale(1.03); 
        box-shadow: 0 10px 20px rgba(0,0,0,0.3); 
    /* KODE UNTUK TAB STREAMLIT */
    /* Mengubah warna teks tab menjadi putih */
    [data-testid="stTabs"] button p {
        color: white !important;
    }
    
    /* Mengubah warna garis bawah tab yang aktif menjadi putih (menggantikan warna biru bawaan) */
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Badan Legislatif",
            "Badan Kesenatoran",
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
            "container": {
                "padding": "10px !important", 
                "background-color": "#c84b22", 
                "border": "none !important", 
                "border-radius": "0 !important", 
                "box-shadow": "none !important" 
            },
            "icon": {
                "color": "white", 
                "font-size": "19px"
            },
            "nav-link": {
                "font-size": "14px",
                "text-align": "center",
                "margin": "5px", 
                "color": "white",
                "background-color": "transparent", 
                "--hover-color": "rgba(255, 255, 255, 0.1)",
            },
            "nav-link-selected": {
                "background-color": "#8c3010", 
                "color": "white",
                "border-radius": "10px" 
            },
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

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XVrHSuj9MdWm4xDvo1qHlRBo_iuzF6q6",
            "https://drive.google.com/uc?export=view&id=1_BgX-fzh2eRSelqbbPqCMqtY8agyYu-v",
            "https://drive.google.com/uc?export=view&id=18hajA2n1YVYJ6kTfN-kYOfLo-5DIxJ7m",
            "https://drive.google.com/uc?export=view&id=1IdQ2MQ2XWhdvnXQbaY1txbJnIvCTuMVy",
            "https://drive.google.com/uc?export=view&id=1yOTPHtGBYnlTDqwngS39rAWLjBO4ZJTR",
            "https://drive.google.com/uc?export=view&id=1vjM1xKeYCPd5JWLnNXdQqlyy0UcomTtU",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Abangnya baek banget sumpah",  
                "pesan": "Semangat bang semoga bisa lulus dengan memuaskan"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya asik, suka ngelawak juga wkwk",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya seruuu heheh",  
                "pesan": "Semangat terus ya kaaa"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keliatan pendiem wkwk, tapi seru koo",  
                "pesan": "Semangat bang, ajarin jadi sekre sih bang wkkw"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya asik bener hehe",  
                "pesan": "Semangat ya kaaaaa"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakanya keliatan pendiem heheh",  
                "pesan": "Semangat terus kaaaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

elif menu == "Badan Kesenatoran":
    def Bason():
        st.markdown("<h3 style='text-align: center;'>Badan Kesenatoran</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Senator", "Biro Aspirasi dan Media Komunikasi", "Biro Kajian Strategis dan Propaganda", "Biro Kesekretariatan"])

        with tab1:
            gambar_urls_senator= [
               "https://drive.google.com/uc?export=view&id=1w3bLa62k0kGRg7zGRGNe09Q2Szp_4SsS",
            ]
            data_list_senator = [
               {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": "Kakanya keren banget jujurrr",  
                "pesan": "Semangat terus kuliahnya kaaaa"
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)
        with tab2:
            gambar_urls_biro_aspirasi= [
                "https://drive.google.com/uc?export=view&id=1ba18uljAh_SmDH5rCQuDfpoNk_CNJW-8",
                "https://drive.google.com/uc?export=view&id=1f2WiomJkzKMRYpp14oc3Gx-wsI4ti-vr",
                "https://drive.google.com/uc?export=view&id=1RTgfa6zxJnqhqS7R3wLXwW_-2r1rumb0",
                "https://drive.google.com/uc?export=view&id=16zCWIbcZx4dxvcZM7sCqr9QO5gW9QTjf",
                "https://drive.google.com/uc?export=view&id=1XDlfiU1_GRKQt1-Oz4V80WeTV78KOdOi",
            ]
            data_list_biro_aspirasi = [
               {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": "abangnya kalo diajak foto maunya melet wkwk",  
                "pesan": "Semangat terus ya baaang"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Asik bener abangnya wkwk",  
                "pesan": "Semangat terus baaaang"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya asik sih jujur",  
                "pesan": "Semangat terus ya kaa kuliahnyaaa"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya chill sih ini wkwk",  
                "pesan": "Pokonya semangat terus baaang"
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)
        with tab3:
            gambar_urls_biro_kajian= [
                "https://drive.google.com/uc?export=view&id=1XDlfiU1_GRKQt1-Oz4V80WeTV78KOdOi",
                "https://drive.google.com/uc?export=view&id=1laahXpYjdVJLUj6vpNg8LRqMcCJ-pDmI",
                "https://drive.google.com/uc?export=view&id=1rKduKEzQMAPM7oR3IFZ1VX38mk7XacKg",

            ]
            data_list_biro_kajian = [
                {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Pengen belajar sama kakanyaaa wkwk",  
                "pesan": "Semangat terus kaaaaa"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakanya jujur asik banget, apa aja diketawain wkwkw",  
                "pesan": "Semangat terus kaaaaa"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren sih jujur",  
                "pesan": "Semangat terus bang kuliahnya"
                },
                ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)
        with tab4:
    
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1oouCnXYLzYbyTg60HK-GPBIXAk5OYOKw",
            "https://drive.google.com/uc?export=view&id=1sEvAhZP5yxITkZsekx0s2kZyUy9c4xg2",
            ]   
            data_list_kesekretariatan= [   
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakanya baek bangeeet heheh",  
                "pesan": "Semangat terus kaaa"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya lucuuu hehe",  
                "pesan": "Semangat terus ya kaaaa"
            }
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_kesekretariatan)
    Bason()

elif menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg= [
            "https://drive.google.com/uc?export=view&id=15dX_z7PpNBeroFJl9GFrSgFPn91fWpK8",
            ]
            data_list_kabaleg = [
            {
            "nama": "Ridho Benedictus Togi Manik",
            "nim": "123450060",
            "umur": "20",
            "asal": "Kota Manchester",
            "alamat": "GH",
            "hobbi": "Wawancara",
            "sosmed": "@iamridhomanik",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1Gg--iHbQNTGLlW1i03jUvxIWJrPTTmPy",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1J1Ow3mPnTv1NZuoc5vtWmcrPZNIVovs5",
            "https://drive.google.com/uc?export=view&id=1lVb_DRDLKg3v-K0vaCGfGCuvy8H8Aywe",
            "https://drive.google.com/uc?export=view&id=1e9mbPMxdAnuLs80AjDceH0kKP1ubYpQV",
            ]
            data_list_komisi1 = [
            {
            "nama": "Dharu Cahyoaji Sasongko",
            "nim": "123450023",
            "umur": "19",
            "asal": "Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Ngidupin api baleg di tiktok",
            "sosmed": "@exvoltas",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1A717g1m6Pl_yQkREeN-fy6GNGwZgTpea",
                "https://drive.google.com/uc?export=view&id=1DMPCpnCFfHAsAgXe9gsOLPghm24ppRWA",
                "https://drive.google.com/uc?export=view&id=1l3IEEGrYFXfW9-ZrXDk3DUxOjejU7Jr_",
                "https://drive.google.com/uc?export=view&id=1swlWLuvnhYIuncA3X_jmga-WUrSCDm2e",
            ]
            data_list_komisi2 = [
            {
            "nama": "Givaro Ananta",
            "nim": "123450078",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Sukabumi",
            "hobbi": "Minum Kopi",
            "sosmed": "@givarooo",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=11bYc1s3Hdc7SXsymoVoO5xp_fJbWbswa",
                "https://drive.google.com/uc?export=view&id=1U5rFZZlnPF_rL5luJ9Thw-uOT2b62c0J",
                "https://drive.google.com/uc?export=view&id=1Cic7JXesS0nSp855SaBGZ9GtBENJKAOC",
                "https://drive.google.com/uc?export=view&id=1bL_a8gWYvrND2p3KYrqGeW6sslbV5cvU",
            ]
            data_list_komisi3 = [
            {
            "nama": "Monica Patricia Tanjung",
            "nim": "123450073",
            "umur": "21",
            "asal": "Jakarta Barat",
            "alamat": "Kotabaru",
            "hobbi": "Lari",
            "sosmed": "@monica_tjg",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi3, data_list_komisi3)

    Baleg()
    
elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown("<h3 style='text-align: center;'>Badan Minat dan bakat</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4= st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])
        
        with tab1:
            gambar_urls_kepala_departemen_minbak= [
            "https://drive.google.com/uc?export=view&id=18x8qz_Lqj6i6PEFA3JUyCfPJlReMZvUB",
            ]
            data_list_kepala_departemen_minbak= [
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
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1qsEatLS2i26ptSaL9N73Mg8Zr3kBvuCd",]
            data_list_sekretaris_departemen_minbak = [ 
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
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
            "https://drive.google.com/uc?export=view&id=1KCjrYYX695GBHhMlhc5Ay7fM4X0rcray",
            "https://drive.google.com/uc?export=view&id=1RIlVyC4-CUxWubRIhL6adMHNdQl6u2GX",
            "https://drive.google.com/uc?export=view&id=1y4-G6rgI6U1V0RTUpiS6zRi_pDkOLVsR",
            "https://drive.google.com/uc?export=view&id=1_eYRFgBp2AQMI82bDUc4UdsqoWnwL4jM",
            "https://drive.google.com/uc?export=view&id=1V_YJBsavn3kTKejwmJ6hk-ivjNly7J2j",
            "https://drive.google.com/uc?export=view&id=1oHO4Y4CL1xaqk1fIfC_HnFLdZGc4hxe5",
            
            ]
            data_list_manajemen_aktivitas_dan_kompetisi = [
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
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
                "https://drive.google.com/uc?export=view&id=1Pa7Bf-cFWhQ6OWOxKgLyTFTpsLNCJcLu",
                "https://drive.google.com/uc?export=view&id=1O0fPU57LFyUr0bQSX8HofN0bgnjZbGHz",
                "https://drive.google.com/uc?export=view&id=1wojg09H8RB56V8_zAvXtc5VhXALqu-ZK",
                "https://drive.google.com/uc?export=view&id=17NH9Vc1UFPd81rKP1q0Ll6OnKj51Fo7X",
                "https://drive.google.com/uc?export=view&id=18NYYMnIUvEaIuVehyadgt_ig6q9njJqS",
                "https://drive.google.com/uc?export=view&id=1C8_2h67_WKBnPUpwkkTm9AfSi7W2H7_z",
                "https://drive.google.com/uc?export=view&id=1mjHinYhIBpyeWsNWf_jMBdvWHjECt162",
            ]
            data_list_manajemen_minat_dan_bakat = [
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
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)  

    Departemen_Minbak()

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
            "https://drive.google.com/uc?export=view&id=1l2mlr7vZPK41txxoyWGfxdGzpn2TJGoA",
            ]
            data_list_Kadep_psda = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1PF8M1Y58whudIhc83cL6I0uxK-hC5lDp",
            ]
            data_list_sekdep_psda = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
                "https://drive.google.com/uc?export=view&id=1Wo-8soBycLgfDxPR7Rb50iSC7Mj_SW4N",
                "https://drive.google.com/uc?export=view&id=1ZBiVMQIlfOFOO1V17kk2a_uw0tlXSYNH",
                "https://drive.google.com/uc?export=view&id=14j7DPtXOytTM0xGlO8TCjJjmG4W3CPGS",
                "https://drive.google.com/uc?export=view&id=1XHITpW-V7FOZZ9nfDzZTUKlvsfwhiqbp",
                "https://drive.google.com/uc?export=view&id=1gp0_vVYSSZgvk3TuL9o0UHZVdHKjZFjV",
            ]
            data_list_Divisi_Kaderisasi = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1cc-Wlmi94WY19QG1zf35BwW9IWSFRlfa",
            "https://drive.google.com/uc?export=view&id=1Uw7KgQAlkNLkRxB6hE79jHAv6QU6LNE5",
            "https://drive.google.com/uc?export=view&id=1P0GLKwFaHTdIrF_qkG-Je7tgM5DcYl99",
            "https://drive.google.com/uc?export=view&id=15J9w3W-oSCsfn2-VefhEpXoyNco1WDCH",
            "https://drive.google.com/uc?export=view&id=12hUosoUbyvSkaiuGJflZ1giQxQEDK_nX",
            "https://drive.google.com/uc?export=view&id=1z_d0ExZuDLRVU01LJmsRcJLH906VWOiH",
            "https://drive.google.com/uc?export=view&id=1J4bgCQNDSpbHz8J_VifkQQ4hIY4oOveD"
            ]
            data_list_Divisi_Peningkatan_Mutu_Anggota = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Peningkatan_Mutu_Anggota, data_list_Divisi_Peningkatan_Mutu_Anggota)
    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
            "https://drive.google.com/uc?export=view&id=1N4dIHHdB5CeVz8OygZn-hNOX1MjASRk1",
            ]
            data_list_Kadep_ssd = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)
            
        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1E3GvqoGWxhja7K_jKk9NpgEVjuLBgrcP",
            ]
            data_list_sekdep_ssd = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1NdxI7kuTgiEiutow57MPkZtSBkau1lK0",
            "https://drive.google.com/uc?export=view&id=1LNA6K_zrpCh_8B787bIxo8JB1UCWVwl9",
            "https://drive.google.com/uc?export=view&id=1RkhM5S_5A8U0kUtI5wWR2SB3YJCLxHmX",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            ]
            data_list_kemitraan = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1TUqVePQ0R95loxH2Zqbb_Le74GsnOxTN",
            "https://drive.google.com/uc?export=view&id=1PhtcoQexxeNPD-B53SSojJ-ieX61ZSpx",
            "https://drive.google.com/uc?export=view&id=1-IhjUPBL9tVC_27_oUq1cquGFobnew_6",
            "https://drive.google.com/uc?export=view&id=17WuUaC_OHDVufacMa_rIau-lXD1zK2GK",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            ]
           
            data_list_kewirausahaan = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
        ]
            display_images_with_data(gambar_urls_kewirausahaan, data_list_kewirausahaan)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1b5BlJfjO0SGyy0XTUPyN8ZOJ8zkvOBUD",
            ]
            data_list_Kadep_medkraf = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1hB4PN9eK9z13aE5sxeq218htzjTkEVS9",
            ]
            data_list_sekdep_medkraf = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1Re_t0YbK2mT-mjnestjAdTS11mGbAtc6",
            "https://drive.google.com/uc?export=view&id=1GSlalGfy31swutJV2zZpWdSRgGK9tlSo",
            "https://drive.google.com/uc?export=view&id=1YEEeDJoyZpavqkCRiyzLAPkp30gGWcJs",
            "https://drive.google.com/uc?export=view&id=1yZWmRobFZhHEX0y-5e0_PH2eJ4LnK748",
            ]
            data_list_Divisi_dokumentasi = [
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1Vx0Nk2OylnbrRx_L6ZW5JQ6GVqgI3rTQ",
            "https://drive.google.com/uc?export=view&id=1Y-n9WgzEVokH0XimAqDOSa_epwnhnwmZ",
            "https://drive.google.com/uc?export=view&id=1qLUI-SymckwaduId3Bbk4DEOa0mGPnY9",
            "https://drive.google.com/uc?export=view&id=1m_my97kVsCVPinEGsp19Rg4rFgbUG8S_",
            "https://drive.google.com/uc?export=view&id=1n0jpZiHb2p-lVgL4sXTd76oGO8sfi1Ed",
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1atZTxIoNLVNQVFRr4CRIL7sWe8SGNYbq",
            "https://drive.google.com/uc?export=view&id=1KSezc8FGz4EDRuYnUxfB0J5kcA6xw1Q3",
            "https://drive.google.com/uc?export=view&id=1AZeqrWofTPAnMCbqZdGvhoUcoraK6SZt",
            "https://drive.google.com/uc?export=view&id=1xR39p8ryuUsU9tngr4Vb1Cw37p4zQ4y8",
            ]
            data_list_Divisi_Visual_Design = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()

