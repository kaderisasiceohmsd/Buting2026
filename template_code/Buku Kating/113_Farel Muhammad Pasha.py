import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');

    /* Global Styling - Background Krim dengan Grafik Multi-Layer Bertumpuk */
    .stApp {
        background-color: #fbf9f5;
        background-image: 
            radial-gradient(rgba(181, 142, 75, 0.28) 1.5px, transparent 1.5px), 
            radial-gradient(rgba(92, 64, 51, 0.15) 1.5px, #fbf9f5 1.5px),
            linear-gradient(45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%);
        background-size: 36px 36px, 36px 36px, 60px 60px, 60px 60px;
        background-position: 0 0, 18px 18px, 0 0, 30px 30px;
        background-attachment: fixed;
        color: #1e1b18;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar disesuaikan warnanya agar senada, terang, dan rapi */
    [data-testid="stSidebar"] {
        background-color: #f0e8d5 !important;
        border-right: 2px solid rgba(181, 142, 75, 0.4);
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #1e1b18 !important;
        font-weight: 500;
    }

    /* Gaya Kotak Profil / Konten di halaman person */
    .person-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(246, 240, 226, 0.96) 100%); 
        backdrop-filter: blur(8px);
        border: 2px solid #b58e4b; 
        outline: 2px dashed rgba(181, 142, 75, 0.4);
        outline-offset: -6px;
        padding: 26px; 
        border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(181, 142, 75, 0.15); 
        color: #1e1b18;
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


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
            "nav-link-selected": {
                "background-color": "#FCF0DA !important",
                "color": "#000000 !important",
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
    # CSS Murni untuk Efek Gulungan Kertas (Scroll) Otentik
    st.markdown(
        """
        <style>
        /* Kontainer Utama Gulungan */
        .scroll-wrapper {
            max-width: 420px;
            margin: 20px auto;
            position: relative;
            filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.35));
        }

        /* Roll Atas & Bawah (Batang Kayu/Kertas Gulung) */
        .scroll-roller {
            height: 26px;
            background: linear-gradient(90deg, #5c3818 0%, #8d5b2d 20%, #e0aa68 50%, #8d5b2d 80%, #5c3818 100%);
            border-radius: 13px;
            border: 2px solid #3d230d;
            box-shadow: inset 0 3px 5px rgba(255,255,255,0.3), inset 0 -3px 5px rgba(0,0,0,0.5);
            position: relative;
            z-index: 2;
        }

        /* Badan Kertas Kuno */
        .scroll-body {
            background: #f4e3b1;
            background: radial-gradient(circle, #f9edd1 0%, #e8d08d 85%, #d1b164 100%);
            border-left: 3px dashed #b89547;
            border-right: 3px dashed #b89547;
            padding: 25px 30px;
            box-shadow: inset 0 0 25px rgba(115, 77, 20, 0.45);
            margin: -6px 12px; /* Menyelip halus di antara roller */
            position: relative;
            z-index: 1;
        }

        /* Gaya Teks di Dalam Kertas */
        .scroll-body p {
            color: #3d220a !important;
            font-family: 'Georgia', serif;
            font-size: 0.95em;
            line-height: 1.6;
            margin-bottom: 8px;
            border-bottom: 1px dashed rgba(140, 90, 30, 0.25);
            padding-bottom: 4px;
        }

        .scroll-body p:last-child {
            border-bottom: none;
        }

        /* Merapikan ekspander Streamlit */
        div[data-testid="stExpander"] {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
                with st.expander(f"📜 Buka Biodata: {data_list[i]['nama']}"):
                    st.markdown(
                        f"""
                        <div class="scroll-wrapper">
                            <div class="scroll-roller"></div>
                            <div class="scroll-body">
                                <p><b>Nama:</b> {data_list[i]['nama']}</p>
                                <p><b>NIM:</b> {data_list[i]['nim']}</p>
                                <p><b>Umur:</b> {data_list[i]['umur']}</p>
                                <p><b>Asal:</b> {data_list[i]['asal']}</p>
                                <p><b>Alamat:</b> {data_list[i]['alamat']}</p>
                                <p><b>Hobbi:</b> {data_list[i]['hobbi']}</p>
                                <p><b>Sosmed:</b> {data_list[i]['sosmed']}</p>
                                <p><b>Kesan:</b> {data_list[i]['kesan']}</p>
                                <p><b>Pesan:</b> {data_list[i]['pesan']}</p>
                            </div>
                            <div class="scroll-roller"></div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    st.write("Semua gambar telah dimuat!")
    
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Zk1dBEPcp-D1z_nycnH2V2XfikMP-Bdp",
            "https://drive.google.com/uc?export=view&id=1pivNhCxr-ncaPEGpNVL7vW69-XZB087V",
            "https://drive.google.com/uc?export=view&id=1HYAgyYDPgDxlNrikJXX_sHiu2NB4-iLE", 
            "https://drive.google.com/uc?export=view&id=14E59i2SfGpTZyoQHGcTYYHwmzlZOI869", 
            "https://drive.google.com/uc?export=view&id=1aAZQF2r9eRlSJW-xJOjxeb2vhKnC7MTJ",
            "https://drive.google.com/uc?export=view&id=1LRh-OBcwk4djsmijUjpKxilrm_VtlfY_",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marapaung ",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "Abang ini keren daqn kalem",  
                "pesan":"semangat yaa bang buat kuliahnya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya asik, tinggi, dan nyantuy",  
                "pesan":"Zikirnya semoga lebih rajin lagi ya bangg"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Aura kakanya kalem tapi tegas",  
                "pesan":"semoga lebih semangat lagi ka jadi aspraknyaa"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini kalem sama pendiem tapi asikk juga",  
                "pesan":"semangat terus ya bang kuliahnyaaa"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya positif vibesss",  
                "pesan":"stay positif vibes terus ya kaa"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Ka Luthfia orangnya asik terus gampang seyum jugaa",  
                "pesan":"tetep jadi orang yang asik dan gampang senyum ya kaa"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
    
if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IbebTFBPkSyxMkr0d6EINJ9t2NdXM6uF",
            "https://drive.google.com/uc?export=view&id=1hepjAmdngtGvSGRCAAcNz5j-IDqnoBMu",
            "https://drive.google.com/uc?export=view&id=1le945I1B9Qouk17zUfTODlP2KVdtV712",
            "https://drive.google.com/uc?export=view&id=12gXQ0CeJ8Iz3KAj_JxoR4nVS4ZoNqys9",
            "https://drive.google.com/uc?export=view&id=15z0baUvhVwx1KDMipuBCqZzZc3UVYmZE",
            "https://drive.google.com/uc?export=view&id=1BOo7wwQ7-MG0Fh8tUada95tGVNMGQ4hh",
            "https://drive.google.com/uc?export=view&id=1L2msJ3-vCvmbEvR8rnza1JgYe5oPWsVv",
            "https://drive.google.com/uc?export=view&id=1scO6im0ywM6kaLe4Luzz3_cV5mjMEske",
            "https://drive.google.com/uc?export=view&id=1eRwkhcPvrr1IXffFcjlkcpff_UMBhYo9",
            "https://drive.google.com/uc?export=view&id=1O_mVf05_wzwFJoipMvyjZm4JvXaCaI5e",
            "https://drive.google.com/uc?export=view&id=1WYekiNi3yc0YF56mehCAYhXptWHt4rFm",
            "https://drive.google.com/uc?export=view&id=1r7Qj2lT08UsPRoSVv4QDzXAgGlNM60dj",
            "https://drive.google.com/uc?export=view&id=1EehY6M08V0P1uoFxt8aekKsCk4I3EieO",
        ]
        data_list = [
    {
        "nama": "Ridho Benedictus Togi Manik",
        "nim": "123450066",
        "umur": "20",
        "asal": "Kuala Lumpur",
        "alamat": "GH",
        "hobbi": "Wawancara",
        "sosmed": "@iamridhomanik",
        "kesan": "Bang ridho orangnya asik tapi bisa kalem juga",
        "pesan": "semoga lebih sering ngewawancara ya bang kaya hobbi abang"
    },
    {
        "nama": "Juesi Apridelia Saragih",
        "nim": "123450085",
        "umur": "19",
        "asal": "Pelangi",
        "alamat": "Singkawang",
        "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
        "sosmed": "@j__eesie",
        "kesan": "kakanya positif vibes banget terus ramah jugaa",
        "pesan": "semangat terus kuliahnya kakkk, dan semoga terus ramah"
    },
    {
        "nama": "Dharu Cahyoaji Sasongko",
        "nim": "123450023",
        "umur": "19",
        "asal": "Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Makan mie gomak",
        "sosmed": "@exvoltas & @ddharu",
        "kesan": "Abangnya asik, terus kadang tingkahnya lucu",
        "pesan": "semoga tingkahnya selalu lucu ya bangg"
    },
    {
        "nama": "GH Mikael Niko A S",
        "nim": "124450079",
        "umur": "20",
        "asal": "Pasir Sakti",
        "alamat": "Jati Agung",
        "hobbi": "Tidur",
        "sosmed": "@me._kael",
        "kesan": "Awal ngeliat kirain pendiem, taunya asik abangnya",
        "pesan": "semoga tidurnya lebih nyenyak dari tidur biasanya banggg"
    },
    {
        "nama": "Siti Sarifah Sumamah",
        "nim": "124450015",
        "umur": "19",
        "asal": "Bekasi",
        "alamat": "Kedaton",
        "hobbi": "Mancing",
        "sosmed": "@syt.rifa",
        "kesan": "Kakaknya murah senyum",
        "pesan": "semangat terus ya kaa buat kuliahnyaa"
    },
    {
        "nama": "Givaro Ananta",
        "nim": "123450078",
        "umur": "21",
        "asal": "Lampung Barat",
        "alamat": "Sukabumi",
        "hobbi": "Minum Kopi",
        "sosmed": "@givarooo",
        "kesan": "Abangnya kalem terus keliatan cool abiess",
        "pesan": "semoga bisa nyobain kopi di seluruh dunia ya banggg"
    },
    {
        "nama": "Afghanis Nursholehatunisa",
        "nim": "124450042",
        "umur": "20",
        "asal": "Kepulauan Mentawai",
        "alamat": "Kadang di kost putri kadang di kost sekar",
        "hobbi": "Memanjat",
        "sosmed": "@afghanisnt_",
        "kesan": "Kakak ini kirain jutek, tapi ternyata ramah bangettss",
        "pesan": "semoga selalu dilancarin kuliahnya ya kaaa"
    },
    {
        "nama": "Hani Qurrota Aini",
        "nim": "124450020",
        "umur": "20",
        "asal": "City earth",
        "alamat": "Sukarame",
        "hobbi": "Baca AU",
        "sosmed": "@haniqurratuain_",
        "kesan": "Kakanya lucu plus murah senyum jugaaa",
        "pesan": "semoga vibes kakanya selalu positif ya kaa"
    },
    {
        "nama": "Jeremia Halim",
        "nim": "124450101",
        "umur": "20",
        "asal": "Tangerang",
        "alamat": "Teluk Betung",
        "hobbi": "Nyanyi, olahraga",
        "sosmed": "jeremia_hm",
        "kesan": "Bang Jeremia orangnya kalem dan berwibawa juga, tapi asikk",
        "pesan": "stay cool terus yaa bangg"
    },
    {
        "nama": "Monica Patricia Tanjung",
        "nim": "123450073",
        "umur": "21",
        "asal": "Jakarta Barat",
        "alamat": "Kotabaru",
        "hobbi": "Lari",
        "sosmed": "@monica_tjg",
        "kesan": "Kakaknya baik banget",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Jona Timothy Ogatse Panjaitan",
        "nim": "124450121",
        "umur": "20",
        "asal": "Depok",
        "alamat": "Pemda Raya",
        "hobbi": "Nge-gym, koleksi figur",
        "sosmed": "@nagatseee",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Sekar Dini Widya Putri",
        "nim": "124450082",
        "umur": "20",
        "asal": "Metro",
        "alamat": "Pemda",
        "hobbi": "Melukis",
        "sosmed": "@sekardnwp",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Wan Nashwa Alhasni Yuska",
        "nim": "123450077",
        "umur": "20",
        "asal": "Pasay",
        "alamat": "Belwis",
        "hobbi": "Nyapa angin",
        "sosmed": "@nshaysk",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# BADAN KESENATORAN
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BhJQSROOrBo3TZ3H6pnoMRxMjnkE0m78",
            "https://drive.google.com/uc?export=view&id=11WqFNtxAelGTryhZEzfec5sM3UXd1A9f",
            "https://drive.google.com/uc?export=view&id=1tiRkQG5IirT7wuKV7qT0Iah_PFd1O4Rv",
            "https://drive.google.com/uc?export=view&id=1iGfOjTnHF43zFxXgd4rsbG6AiCItmCd-",
            "https://drive.google.com/uc?export=view&id=1pyoDk0voR0nvQAf47-RLpxOFaXfVor_j",
            "https://drive.google.com/uc?export=view&id=1kg2SyAQd7MqBaIhg9SojZ01XRAIIHXFx",
            "https://drive.google.com/uc?export=view&id=1hWQiTjc1CPnWFiMPwtBrNhjbByJyvgUc",
            "https://drive.google.com/uc?export=view&id=1o6BGjwhDlTsYL1Eo2TOxe36tKlRau-As",
            "https://drive.google.com/uc?export=view&id=1xOnkyFBTidBqDCtrwIQRKN2grcbgraRO",
            "https://drive.google.com/uc?export=view&id=1xeEYGqj4AZfWSPyKx-EL7agDtjGxCqsx",
        ]
        data_list = [
    {
        "nama": "Fathinah Nur Azizah",
        "nim": "123450072",
        "umur": "21",
        "asal": "Jakarta",
        "alamat": "Belakang PB",
        "hobbi": "Nulis di medium",
        "sosmed": "@fathinahnazzh",
        "kesan": "Kak Ziza fix alpha woman banget sih, no debat! Gacor, aktif, keren parah. Pokoknya panutan bangett.",
        "pesan": "Semangat teruss Kak Ziza buat kuliah dan kesibukan lainnya. Bismillah makin banyak achievement keren ke depannya."
    },
    {
        "nama": "Helmy Surya Pratama",
        "nim": "124450033",
        "umur": "20",
        "asal": "Jakarta ",
        "alamat": "Kedamaian",
        "hobbi": "Ngesen kiri",
        "sosmed": "@helmy_inst",
        "kesan": "Awalnya ngira Bang Helmy jaim atau sombong wkwk, eh ternyata pas ngobrol asli seru dan asyik banget woy.",
        "pesan": "Semangat kuliahnya Bang! Moga jalan menuju kelulusan mulus tancap gas tanpa hambatan, amin."
    },
    {
        "nama": "Fernando Diemtrius Barus",
        "nim": "124450063",
        "umur": "21",
        "asal": "Tangerang Kota",
        "alamat": "Sebelah kamar biwa",
        "hobbi": "Badminton",
        "sosmed": "@barus.fernando",
        "kesan": "Bang Fer asyik parah sih, mau ngomongin topik random apa aja tetep nyambung dan gak garing.",
        "pesan": "Gass terus Bang Fer sampe garis finish! Moga skripsi aman, no drama, dan bisa graduated sesuai target wkwk."
    },
    {
        "nama": "Suci Aulia",
        "nim": "124450034",
        "umur": "19",
        "asal": "Jakarta",
        "alamat": "Kotabaru",
        "hobbi": "Mancing",
        "sosmed": "@sciia__",
        "kesan": "Maminya Cosval nih! Mentor terbaik yang beneran tulus banget. Walau lagi capek tetep mau dengerin keluh kesah kami.",
        "pesan": "Moga kebaikan Kak Suci dibalas berlipat-lipat. Semangat TA-nya, stay healthy, dan jangan terlalu diporsir yaa Kak!"
    },
    {
        "nama": "Wielman Itolo Halawa",
        "nim": "124450072",
        "umur": "20",
        "asal": "Nias Selatan",
        "alamat": "Asrama TB3",
        "hobbi": "Dibonceng",
        "sosmed": "@wielhawn",
        "kesan": "Bang Wielman santai tapi public speaking-nya gokil abis! Tiap kali didapuk jadi MC pasti langsung gacor.",
        "pesan": "Semangat terus kuliahnya Bang! Semoga lancar sampe lulus dan impian nge-MC sampe masuk TV kesampaian, amin."
    },
    {
        "nama": "Lia Hana Ichisasmita",
        "nim": "123450089",
        "umur": "21",
        "asal": "Jakarta",
        "alamat": "Belwis",
        "hobbi": "Nonton",
        "sosmed": "@lia.h_264",
        "kesan": "Kak Lia tuh tipe yang kalem dan pembawaannya bikin adem bangett. Diajak ngobrol serasa nyaman aja gitu.",
        "pesan": "Semoga semua hal yang lagi Kakak usahain sekarang hasilnya beneran manis dan bikin bangga ya Kak!"
    },
    {
        "nama": "Aqila Zayyan SalsabiL",
        "nim": "124450014",
        "umur": "19",
        "asal": "Lampung Utara",
        "alamat": "Sukarame",
        "hobbi": "Mendokumentasikan bayes",
        "sosmed": "@aqilazayyaan",
        "kesan": "Kating tergokil dan terasik! Udah cantik imut, bikin suasana sekitarnya dapet energi positif. Yaa walau agak bawel sih hehee",
        "pesan": "Tetap jadi versi terbaik Kak Aqila ya! Semangat ngejar cita-cita, plus kurangi dikit bawelnya wkwk."
    },
    {
        "nama": "Hazel Mahesa Handhaka",
        "nim": "124450114",
        "umur": "20",
        "asal": "Lamtim Timur",
        "alamat": "Gunung Terang",
        "hobbi": "Giring ayam",
        "sosmed": "@hazelhandhaka",
        "kesan": "Lucu emang, beda potongan rambut beda vibes wkwk! Tapi aslinya baik bangett dan pas jadi Ketuplak Scienfest kemarin sabar parah.",
        "pesan": "Tetap jadi orang baik dan humble ya Bang. Semangat terus ngejalanin dinamika perkuliahan ini!"
    },
    {
        "nama": "Nadya Ratu Anjani",
        "nim": "123450083",
        "umur": "21",
        "asal": "Bandar Lampung",
        "alamat": "Sukarame",
        "hobbi": "Denger lagu",
        "sosmed": "@nadyaanjaani",
        "kesan": "Kak Nadya cakep manis bangett, imut jugaa! Terus orangnya seru dan positive vibes parah.",
        "pesan": "Moga semua kerja keras Kak Nadya belakangan ini berbuah hasil yang makin mantap yaa, semangat!"
    },
    {
        "nama": "Dwi Rahma Fitriani",
        "nim": "124450084",
        "umur": "19",
        "asal": "Tulang Bawang",
        "alamat": "Jl. Lapas",
        "hobbi": "Baca buku, nonton film, dengerin musik",
        "sosmed": "@dwi_rahmftrnii",
        "kesan": "Kirain awal-awal Kak Dwi anak yang super introvert atau kalem, ternyata pas diusik asyik jugaa diajak obrol.",
        "pesan": "Semangat kuliahnya Kak! Jangan lupa luangin waktu me time buat hobinya di tengah gempuran tugas!"
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()
# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1q5EBb7ytsZGgrI0Bt-iv6XCz_fWFaI6M",
            "https://drive.google.com/uc?export=view&id=1W--Asmhm_WUiJCi4F68whk6y-UdHXH76",
            "https://drive.google.com/uc?export=view&id=1CsxZU8ZgVdBKaSygWY5UIjZQBK2K95s9", 
            "https://drive.google.com/uc?export=view&id=1ROITU9I7Zgk8y52f9xKdMx2SMEGHQ6ti",
            "https://drive.google.com/uc?export=view&id=14l5wDVlo9JM6k647yUcrkUPIl7-JN7MS",
            "https://drive.google.com/uc?export=view&id=1Kl38sxt52A49mu80s8uUGuIiW9Zc2CEJ", 
            "https://drive.google.com/uc?export=view&id=1UzoIE3GIDyGd_tYWkfiknk9DKIL1MbVH",
            "https://drive.google.com/uc?export=view&id=1qz9HpJFJxZX_qXNYnyJo5Fhxtvj8cJQ7",
            "https://drive.google.com/uc?export=view&id=16oTahsfl8Uaszj2SNLAFmwYMQjIjQVEG", 
            "https://drive.google.com/uc?export=view&id=1n8kJis-28K795EjkWsVmaSNitkWIK-6Z",
            "https://drive.google.com/uc?export=view&id=1oBQsbpwMvZfUt1y4rHjE4sWmzf7iZmvu",
            "https://drive.google.com/uc?export=view&id=1Y6mpyQhgU9w2kHP9kW3lxFLeM36rRd9A",
        ]
        data_list = [
            {
        "nama": "Ihsan Maulana Yusuf ",
        "nim": "123450110",
        "umur": "21",
        "asal": "Sumatera Barat ",
        "alamat": "Belwis ",
        "hobbi": "Jualan",
        "sosmed": "@ihsan.myusuf",
        "kesan": "Bang Ihsan jiwa entrepreneur-nya berasa banget, vibes orang sukses dan rajin nyari peluang.",
        "pesan": "Semangat terus kuliahnya Bang, semoga bisnis dan usahanya makin laris manis dan lancar jaya."
    },
    {
        "nama": "Hanifah Inaya Sani",
        "nim": "123450123",
        "umur": "20",
        "asal": "Bandar Lampung ",
        "alamat": "Bandar Lampung ",
        "hobbi": "Masak",
        "sosmed": "@_inayasani",
        "kesan": "Kak Inaya pembawaannya kalem dan keibuan banget, kelihatan telaten dan ramah kalau diajak ngobrol.",
        "pesan": "Semangat terus kuliahnya Kak Inaya, semoga hobi masaknya makin terasah dan sukses selalu."
    },
    {
        "nama": "Afifah Fauziah ",
        "nim": "123450002",
        "umur": "20",
        "asal": "Bandung ",
        "alamat": "Airan",
        "hobbi": "Nonton marvel",
        "sosmed": "@fifah.zy",
        "kesan": "Kak Fifah seru banget diajak diskusi, vibes-nya asyik dan punya selera tontonan yang keren.",
        "pesan": "Tetap semangat ngejar target kuliahnya Kak, semoga segala urusannya selalu dipermudah."
    },
    {
        "nama": "Hasan Nur Ramadhan",
        "nim": "124450013",
        "umur": "25",
        "asal": "Lampung Tengah ",
        "alamat": "Sebelah kostan Ayake",
        "hobbi": "Nonton YouTube ",
        "sosmed": "@hasan.ramdhan08",
        "kesan": "Bang Hasan sosok senior yang sangat dewasa, pengalamannya banyak dan enak banget diajak sharing.",
        "pesan": "Semangat terus Bang Hasan, semoga impian dan rencana ke depannya bisa tercapai semua."
    },
    {
        "nama": "Talitha Justine",
        "nim": "124450076",
        "umur": "19",
        "asal": "Jakarta",
        "alamat": "Pemda",
        "hobbi": "Nonton",
        "sosmed": "-",
        "kesan": "Kak Talitha pembawaannya santai dan humble banget, tipe yang bikin suasana jadi nyaman.",
        "pesan": "Semangat jalani perkuliahan Kak, semoga selalu diberi kelancaran di setiap semester."
    },
    {
        "nama": "Layina Ropiqo",
        "nim": "124450016",
        "umur": "19",
        "asal": "Bandar Lampung ",
        "alamat": "Bandar Lampung ",
        "hobbi": "Nonton dracin ",
        "sosmed": "@lay.inr_",
        "kesan": "Kak Layina ramah dan baik banget, diajak ngobrolin topik santai langsung nyambung.",
        "pesan": "Semangat terus kuliahnya Kak Layina, semoga tetap ada waktu luang buat marathon dracin."
    },
    {
        "nama": "Mochammad Iqbal Az-zahir",
        "nim": "124450052",
        "umur": "20",
        "asal": "Bekasi",
        "alamat": "Natar",
        "hobbi": "Nonton drakor ",
        "sosmed": "@iqbalazzahir_",
        "kesan": "Bang Iqbal orangnya asyik dan cukup santai, gokil juga hobinya marathon drakor di sela kesibukan.",
        "pesan": "Sukses terus buat kuliahnya Bang, semoga semua tugas dan praktikumnya bisa dilibas lancar."
    },
    {
        "nama": "Anadia Carana ",
        "nim": "123450019",
        "umur": "21",
        "asal": "Palembang ",
        "alamat": "Way Huwi ",
        "hobbi": "Nyari duit",
        "sosmed": "@anadiacrn_",
        "kesan": "Kak Nadia ini keren dan mandiri banget, kelihatan sangat ambis dan pekerja keras.",
        "pesan": "Semangat terus nyari cuan dan kuliahnya Kak, semoga rezeki dan urusannya makin melimpah."
    },
    {
        "nama": "Abdilah Fikri Alpome",
        "nim": "123450062",
        "umur": "21",
        "asal": "Baturaja Sumatera Selatan ",
        "alamat": "Airan ",
        "hobbi": "Basket ",
        "sosmed": "@pomest__",
        "kesan": "Bang Pome vibes-nya sporty dan santai banget, tipikal abang-abang yang seru diajak nongkrong.",
        "pesan": "Semangat terus kuliah dan aktivitas basketnya Bang, semoga bisa lulus tepat waktu tanpa kendala."
    },
    {
        "nama": "Afdhal Rahmad Setiawan",
        "nim": "124450008",
        "umur": "20",
        "asal": "Sumatera Barat ",
        "alamat": "Belwis",
        "hobbi": "Fishing",
        "sosmed": "@dhalsetiawan",
        "kesan": "Bang Afdhal orangnya tenang dan santai, hobinya mancing mencerminkan tingkat kesabarannya.",
        "pesan": "Semangat kuliahnya Bang Afdhal, semoga makin banyak tangkapan dan urusan kuliah lancar."
    },
    {
        "nama": "Anggun Nita",
        "nim": "124450009",
        "umur": "20",
        "asal": "Lampung Utara ",
        "alamat": "Belwis ",
        "hobbi": "Nonton kartun ",
        "sosmed": "@anggunnitaaa_",
        "kesan": "Kak Anggun ceria dan imut banget, hobinya nonton kartun bikin vibes-nya selalu positif.",
        "pesan": "Semangat terus kuliahnya Kak Anggun, tetap jadi pribadi yang ceria dan makin sukses."
    },
    {
        "nama": "Della Anisa Fitri",
        "nim": "124450095",
        "umur": "18",
        "asal": "Lampung Timur ",
        "alamat": "Margo Lestari  ",
        "hobbi": "Lagi gak punya hobi ",
        "sosmed": "@dellaansaftr",
        "kesan": "Kak Della orangnya cukup unik dan santai, gaya bicaranya juga jujur apa adanya.",
        "pesan": "Semangat ngejalanin masa-masa kuliahnya Kak Della, semoga secepatnya nambah hobi baru yang seru."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1frul1FC8tBLIS5oL5RNa72bBZq_SfDED",
            "https://drive.google.com/uc?export=view&id=1Ri9BuOIGuyHakVw_5AlmA2i2qKvlqF_A",
            "https://drive.google.com/uc?export=view&id=1TxBYakQRRNR618y_B4G73D7rQQ-VktbL",
            "https://drive.google.com/uc?export=view&id=18g9D0gue3uAZtWUbHRpanHHPfp_5PG4I",
            "https://drive.google.com/uc?export=view&id=1IKVSl4EODuyvGv7z9LGLbOS5cp3UbrFW",
            "https://drive.google.com/uc?export=view&id=1TlywZMyUW1NQJHWtVacWo3M07PEKi3n5",
            "https://drive.google.com/uc?export=view&id=1QUeKeY0En3EX0-pFQ1pGZJfcFV0K0R_d",
            "https://drive.google.com/uc?export=view&id=1jbda10w3XStpZ6lE7MDGTyTkRE3vW3X6",
            "https://drive.google.com/uc?export=view&id=1u3s7SZrd7X86anTl0BS5ZIdNo1mp2SRT",
            "https://drive.google.com/uc?export=view&id=1-WmbT0YJ66qdRt3EKVKk4yrwxT4NDyzT",
            "https://drive.google.com/uc?export=view&id=1RL8vXp3ud4FmKBJ4I_6eh94QK0ppifyM",
            "https://drive.google.com/uc?export=view&id=1xqtA6tO56LOKHGO6u7wWymWdHKjowg2S",
            "https://drive.google.com/uc?export=view&id=1EG-sVxGkL4BJ6pYXjCIKECsSKRkCLMM_",
            "https://drive.google.com/uc?export=view&id=1l-vKIvzeBTFdchBaonZbPcdFD7SjEahu",
            "https://drive.google.com/uc?export=view&id=1FvpIdqzVkmOZcwwIsQD6VVjJj3MiFTRF",
            "https://drive.google.com/uc?export=view&id=1k34hEQbdoVJ3EZr2Uqe6QyBTLLZCoazG",
        ]
        data_list = [
           {
        "nama": "Haikal Fransisko Simbolon",
        "nim": "123450106",
        "umur": "20",
        "asal": "Jambi",
        "alamat": "Way Halim",
        "hobbi": "Ngeledek orang",
        "sosmed": "@haikalsbln",
        "kesan": "Bang Haikal orangnya jahil dan seru parah, hobinya ngeledek bikin suasana pertemanan gak pernah garing.",
        "pesan": "Semangat terus kuliahnya Bang, kurangi dikit usilnya tapi tetap jadi pencair suasana ya."
    },
    {
        "nama": "Kharisma Mustika Sari",
        "nim": "123450034",
        "umur": "21",
        "asal": "Way Kanan",
        "alamat": "Untung Senopati",
        "hobbi": "Suka nolong orang",
        "sosmed": "@rismaa.mustika_",
        "kesan": "Kak Risma beneran baik dan helpful banget, tipikal kating yang selalu siap bantu kalau adek tingkatnya kebingungan.",
        "pesan": "Semangat terus kuliahnya Kak Risma, semoga kebaikannya selalu dibalas hal-hal baik juga."
    },
    {
        "nama": "Hanna Grecia Sinaga",
        "nim": "123450038",
        "umur": "21",
        "asal": "Sumatra Utara, Kisaran City",
        "alamat": "Sukarame",
        "hobbi": "Ngabarin orang tua",
        "sosmed": "@hanna_g_sinaga",
        "kesan": "Kak Hanna vibes-nya family person banget dan sangat bertanggung jawab, pembawaannya juga ramah.",
        "pesan": "Sukses selalu buat perkuliahan dan urusannya Kak Hanna, semoga makin bikin bangga orang tua."
    },
    {
        "nama": "A Farhan Ghani",
        "nim": "123450121",
        "umur": "21",
        "asal": "Kemiling",
        "alamat": "Kemiling",
        "hobbi": "Balap Liar",
        "sosmed": "@farhanghani",
        "kesan": "Bang Farhan santai dan gokil abis, style sama vibes-nya anak jalanan yang asyik diajak nongkrong.",
        "pesan": "Semangat terus kuliahnya Bang Farhan, tetap hati-hati di jalan dan lancar sampai lulus."
    },
    {
        "nama": "Aisyah Khairun Nisa",
        "nim": "124450096",
        "umur": "18",
        "asal": "Riau",
        "alamat": "Belwis",
        "hobbi": "Ngeliatin orang",
        "sosmed": "@aisyahkhair._",
        "kesan": "Kak Aisyah kelihatannya tenang dan suka mengamati sekitar, tapi kalau udah diajak ngobrol seru juga.",
        "pesan": "Semangat ngejalanin hari-hari kuliahnya Kak Aisyah, semoga makin betah dan sukses terus."
    },
    {
        "nama": "Cerine Sihotang",
        "nim": "124450049",
        "umur": "19",
        "asal": "Medan",
        "alamat": "Belwis",
        "hobbi": "Balap liar",
        "sosmed": "@cerine_ipynb",
        "kesan": "Kak Cerine unik banget, nama sosmed-nya anak data banget tapi hobinya cukup menantang adrenalin.",
        "pesan": "Semangat kuliah dan ngodingnya Kak Cerine, semoga tugas dan praktikumnya selalu running lancar."
    },
    {
        "nama": "Jaya Saputra Tamba",
        "nim": "124450094",
        "umur": "19",
        "asal": "Medan",
        "alamat": "Pemda",
        "hobbi": "Berkebun dan membuat lagu",
        "sosmed": "@jay.saputratmb",
        "kesan": "Bang Jaya jiwa seninya berasa banget, kreatif dan hobinya estetik beda dari yang lain.",
        "pesan": "Semangat terus kuliah dan karya-karyanya Bang Jaya, ditunggu lagu-lagu keren berikutnya."
    },
    {
        "nama": "Najla Nur Syifa",
        "nim": "124450051",
        "umur": "20",
        "asal": "Aceh",
        "alamat": "Belwis",
        "hobbi": "Gangguin cika",
        "sosmed": "@njlanursyifa",
        "kesan": "Kak Najla orangnya asyik dan rame banget, kelihatan dari hobinya yang suka bikin suasana makin hidup.",
        "pesan": "Semangat terus kuliahnya Kak Najla, tetap jadi kating yang seru dan ceria."
    },
    {
        "nama": "Rozaq Ramdani",
        "nim": "124450100",
        "umur": "18",
        "asal": "Lampung Selatan",
        "alamat": "Korpri Raya",
        "hobbi": "Isengin harvin di kelas",
        "sosmed": "@rozaqramdani__",
        "kesan": "Bang Rozaq jahilnya khas anak kelas banget, bikin suasana kuliah jadi gak tegang dan gak ngebosenin.",
        "pesan": "Semangat terus kuliahnya Bang Rozaq, lancar selalu urusan akademik dan pertemanannya."
    },
    {
        "nama": "Teresa Christiani Purba",
        "nim": "124450046",
        "umur": "19",
        "asal": "Riau",
        "alamat": "Belwis",
        "hobbi": "Masak",
        "sosmed": "@christiani8872",
        "kesan": "Kak Teresa pembawaannya lembut dan rajin, tipikal kating yang keibuan dan menyenangkan.",
        "pesan": "Semangat kuliahnya Kak Teresa, semoga hobi masaknya makin terasah dan urusan kampus dimudahkan."
    },
    {
        "nama": "Muhammad Hanif Dzaky",
        "nim": "124450064",
        "umur": "21",
        "asal": "Padang Sumbar",
        "alamat": "Perumnas Way Kandis",
        "hobbi": "Ngedistro",
        "sosmed": "@hnfdzky_",
        "kesan": "Bang Hanif vibes-nya skena dan paham fashion banget, style-nya selalu kelihatan santai tapi keren.",
        "pesan": "Semangat terus kuliahnya Bang Hanif, semoga semua target akademiknya bisa tercapai dengan lancar."
    },
    {
        "nama": "Audina Fitria ",
        "nim": "124450038",
        "umur": "20",
        "asal": "Sumatera Barat",
        "alamat": "Sukarame",
        "hobbi": "Main ke air terjun",
        "sosmed": "@audinaf_03",
        "kesan": "Kak Audina jiwa petualangnya berasa banget, suka alam dan pembawaannya juga santai diajak ngobrol.",
        "pesan": "Semangat terus perkuliahan Kak Audina, semoga tetap ada waktu buat jalan-jalan ke alam di sela tugas."
    },
    {
        "nama": "Cika Adelia Br Marbun",
        "nim": "124450107",
        "umur": "20",
        "asal": "Riau",
        "alamat": "Belwis",
        "hobbi": "Terlambat ",
        "sosmed": "@cikamrbn",
        "kesan": "Kak Cika jujur dan santai banget orangnya, hobinya cukup realistis buat kehidupan mahasiswa.",
        "pesan": "Semangat terus kuliahnya Kak Cika, semoga jam tidurnya makin teratur dan urusan kampus lancar."
    },
    {
        "nama": "Gustin Haleluya Tampubolon",
        "nim": "124450068",
        "umur": "21",
        "asal": "Toba Sumatera Utara",
        "alamat": "Airan",
        "hobbi": "Nonton",
        "sosmed": "@gustinhaleluya",
        "kesan": "Bang Gustin orangnya santai, asyik, dan terkesan enjoy banget ngejalanin masa-masa perkuliahan.",
        "pesan": "Semangat terus kuliahnya Bang Gustin, semoga sukses selalu dan lancar terus sampai lulus."
    },
    {
        "nama": "Muhammad Harvinsyah",
        "nim": "124450128",
        "umur": "20",
        "asal": "Sumatera Selatan",
        "alamat": "Belwis",
        "hobbi": "Nembak Burung",
        "sosmed": "@muhvinz_",
        "kesan": "Bang Harvin orangnya sabar banget walau sering diisengin, tipikal abang-abang yang seru diajak kumpul.",
        "pesan": "Semangat terus kuliahnya Bang Harvin, semoga makin fokus dan segala urusannya selalu dimudahkan."
    },
    {
        "nama": "Rafa Sabina Fahimah",
        "nim": "124450036",
        "umur": "20",
        "asal": "Natar",
        "alamat": "Natar",
        "hobbi": "Cari duit",
        "sosmed": "@snasaa._",
        "kesan": "Kak Rafa ini sangat pekerja keras dan independen, kelihatan ambis dan produktif banget.",
        "pesan": "Semangat nyari cuan dan kuliahnya Kak Rafa, semoga usahanya selalu memuaskan dan bikin bangga."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QKn1SRuuXsvQ4nBNSJOFhkU-ursS8M0M",
            "https://drive.google.com/uc?export=view&id=1ghrXFqnjbRhzcSvDkfwC4w67-QFm-B9z",
            "https://drive.google.com/uc?export=view&id=10kYfHzNeLAONWbJpyIFKc4CqDxz7kk8T",
            "https://drive.google.com/uc?export=view&id=1RpwOI7elHXzSK1CC7dSIKAYT0zq4Bs7r",
            "https://drive.google.com/uc?export=view&id=1_yKzpOHTAkjHF25YOP3Kzz6bD4tw0Fut",
            "https://drive.google.com/uc?export=view&id=1AUH-QOoiwc47WkuVS8envL2QWZpgl-ve",
            "https://drive.google.com/uc?export=view&id=1lZM2LQ0zLdPb5HUmFj_XTtnDowPocCl8",
            "https://drive.google.com/uc?export=view&id=1loIlmx-aT7Svn-RKSDCsoSiAaIG-7a2V",
            "https://drive.google.com/uc?export=view&id=1WYVVCfCFTG4TyUDBlCZ-306Nj6THKYZl",
            "https://drive.google.com/uc?export=view&id=1QRnD-40DccFxNBh84Mz8Nw5aksvtF5oT",
            "https://drive.google.com/uc?export=view&id=1TrfzdevRW0k_oJnr5uRL0y5yzl3JyhXm",
            "https://drive.google.com/uc?export=view&id=1PIF6-8jxTJKFn03jD68WZeOfu5gre5rk",
            "https://drive.google.com/uc?export=view&id=1eIlB9uLUXj41HhLP_KhSxW9bghFk0H7A",
            "https://drive.google.com/uc?export=view&id=14ecm7LF43ZCNgb6iJmFMbC_aFuBAE0kz",
            "https://drive.google.com/uc?export=view&id=19FsR9aQt35M8cRP1iAnBi8ZdNTZ-NnTS",
            "https://drive.google.com/uc?export=view&id=1BqLrWbKXLlxkk3MEyqZ65CcgxM_lR3Ea",
            "https://drive.google.com/uc?export=view&id=14UkZiECKTP8-X4kooniCvmPQuPBdv2zu",
            "https://drive.google.com/uc?export=view&id=1lKbdVWPGAI4GtNWThzFHipT5TXtDfbQA",
        ]
        data_list = [
           {
        "nama": "Nayla Salsabila Fathianisa",
        "nim": "123450082",
        "umur": "20",
        "asal": "Payakumbuh, Sumatera Barat ",
        "alamat": "Way Huwi, Jati Agung, Lampung Selatan",
        "hobbi": "Mendengarkan Musik",
        "sosmed": "@naylasalsabilaa._",
        "kesan": "Kak Nayla orangnya manis dan chill banget, pembawaannya ramah bikin siapapun nyaman ngobrol bareng.",
        "pesan": "Semangat terus kuliahnya Kak Nayla, semoga perkuliahannya lancar dan sukses selalu."
    },
    {
        "nama": "Donna Maya Puspita",
        "nim": "123450028",
        "umur": "21",
        "asal": "Bekasi",
        "alamat": "Way Huwi",
        "hobbi": "Listening to music",
        "sosmed": "@donnamaya.p",
        "kesan": "Kak Donna tuh vibes-nya asyik dan teratur, tipikal kating yang tenang tapi selalu bisa diandalkan.",
        "pesan": "Sukses terus buat urusan perkuliahan dan kariernya Kak Donna, lancar sampai lulus."
    },
    {
        "nama": "Labo John Noel Napitupulu",
        "nim": "123450037",
        "umur": "20",
        "asal": "Medan, Palembang, Jakpus",
        "alamat": "Belwis",
        "hobbi": "Motoran",
        "sosmed": "@noerruuu",
        "kesan": "Bang Noel vibes-nya anak motor yang santai dan super friendly, diajak ngobrolin apa aja selalu nyambung.",
        "pesan": "Semangat terus kuliah dan motorannya Bang, tetap safety riding dan sukses akademiknya."
    },
    {
        "nama": "Anash Tasya Ausyaqila",
        "nim": "124450050",
        "umur": "20",
        "asal": "Bandar Lampung",
        "alamat": "Way Halim",
        "hobbi": "Nonton",
        "sosmed": "@anshtsyaaql",
        "kesan": "Kak Anash orangnya baik dan penyabar banget, walau sering diisengin temen-temennya tetap senyum dan santai.",
        "pesan": "Semangat terus ngejar target kuliahnya Kak Anash, semoga semua urusannya selalu dimudahkan."
    },
    {
        "nama": "Felisya Nabila Putri Nugroho",
        "nim": "124450104",
        "umur": "19",
        "asal": "Lampung Timur",
        "alamat": "kota baru",
        "hobbi": "Gangguin Anash&Razan, jail di grup",
        "sosmed": "@felisyanbl__",
        "kesan": "Kak Felisya usil dan rame banget di grup, keberadaannya bikin suasana tongkrongan gak pernah sepi.",
        "pesan": "Semangat terus kuliahnya Kak Felisya, tetap jadi pencair suasana yang ceria dan seru."
    },
    {
        "nama": "Muhammad Razan Maulana",
        "nim": "124450031",
        "umur": "21",
        "asal": "Jawa Barat",
        "alamat": "Korpri",
        "hobbi": "Poto orang",
        "sosmed": "@muh_razan_",
        "kesan": "Bang Razan punya bakat fotografi yang keren, pembawaannya santai dan estetik abis.",
        "pesan": "Semangat terus kuliahnya Bang Razan, ditunggu jepretan foto-foto keren berikutnya."
    },
    {
        "nama": "Sania Dwi Ayu Lestari",
        "nim": "123450086",
        "umur": "21",
        "asal": "Karawang",
        "alamat": "Airan raya",
        "hobbi": "nonton netflix",
        "sosmed": "@saniayyllstr",
        "kesan": "Kak Sania kelihatan kalem dan santai, tipikal kating yang humble dan asyik diajak obrol.",
        "pesan": "Semangat terus kuliahnya Kak Sania, semoga tetap ada waktu me time buat nonton film kesukaan."
    },
    {
        "nama": "Allisha",
        "nim": "124450019",
        "umur": "16",
        "asal": "Bekasi",
        "alamat": "Gg.sakum",
        "hobbi": "Mainn Bola, Belajar",
        "sosmed": "@i",
        "kesan": "Kak Allisha tergolong muda banget tapi pinter dan produktif, jiwa semangat belajar dan olahraga-nya seimbang.",
        "pesan": "Semangat terus kuliah dan aktivitasnya Kak, semoga karier akademiknya melesat pesat."
    },
    {
        "nama": "Alya Ramadhanti",
        "nim": "124450091",
        "umur": "19",
        "asal": "Jambi",
        "alamat": "Airan",
        "hobbi": "Jalan jalan",
        "sosmed": "@alya.rmdhnti",
        "kesan": "Kak Alya orangnya seru dan suka mengeksplor hal baru, pembawaannya ceria dan energik.",
        "pesan": "Semangat kuliahnya Kak Alya, semoga di sela jadwal padat tetap bisa jalan-jalan refreshing."
    },
    {
        "nama": "Bunga Clarisa Sefa",
        "nim": "124450097",
        "umur": "20",
        "asal": "Lampung Selatan ",
        "alamat": "Lampung Selatan ",
        "hobbi": "Belajar",
        "sosmed": "@bungaclrssf",
        "kesan": "Kak Bunga rajin dan ambis banget dalam hal akademik, sosok kating yang menginspirasi.",
        "pesan": "Semangat terus perkuliahan Kak Bunga, semoga semua hasil kerja kerasnya berbuah manis."
    },
    {
        "nama": "Difanya Husakina",
        "nim": "124450043",
        "umur": "20",
        "asal": "Pagar Alam",
        "alamat": "Airan Raya",
        "hobbi": "Membaca Al-Qur'an",
        "sosmed": "@difanyhsa_",
        "kesan": "Kak Difanya pembawaannya adem, sopan, dan sangat positif, bikin sekitarnya merasa adem juga.",
        "pesan": "Semangat terus perkuliahan Kak Difanya, semoga selalu dalam kemudahan dan keberkahan."
    },
    {
        "nama": "Nazlah Auliya",
        "nim": "124450054",
        "umur": "20",
        "asal": "Bandar Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "berenang",
        "sosmed": "@nzlhauly_",
        "kesan": "Kak Nazlah ramah dan gampang akrab, vibes-nya sporty dan santai diajak obrol apa aja.",
        "pesan": "Semangat terus kuliahnya Kak Nazlah, semoga selalu diberi kelancaran sampai lulus."
    },
    {
        "nama": "Raihana Adelia putri",
        "nim": "123450041",
        "umur": "20",
        "asal": "Lampung Tengah",
        "alamat": "Airan Raya 1",
        "hobbi": "Menulis, Membaca",
        "sosmed": "@n1tg._",
        "kesan": "Kak Raihana pinter dan kelihatannya puitis, wawasannya luas dan pembawaannya tenang.",
        "pesan": "Semangat terus kuliah dan karya tulisnya Kak Raihana, sukses selalu buat ke depannya."
    },
    {
        "nama": "Daffa Kharisma Adzana",
        "nim": "124450061",
        "umur": "21",
        "asal": "Surabaya",
        "alamat": "Sukarame",
        "hobbi": "Dangir",
        "sosmed": "@daffascript",
        "kesan": "Bang Daffa santai dan terkesan lihai di bidang pemrograman, gaya bicaranya juga santai khas Surabaya.",
        "pesan": "Semangat terus ngoding dan kuliahnya Bang Daffa, semoga projek-projeknya sukses lancar."
    },
    {
        "nama": "Edsel Adya Pradipta",
        "nim": "124450098",
        "umur": "20",
        "asal": "Lampung Selatan ",
        "alamat": "Natar",
        "hobbi": "Nonton Anime",
        "sosmed": "@edsel_0712",
        "kesan": "Bang Edsel asyik diajak diskusi tontonan santai, pembawaannya humble dan terkesan chill.",
        "pesan": "Semangat terus ngejar IPK dan lulusnya Bang Edsel, semoga urusan kampusnya lancar."
    },
    {
        "nama": "Lucia Advencia Rachel Nainggolan",
        "nim": "124450085",
        "umur": "20",
        "asal": "Bekasi",
        "alamat": "Belwis",
        "hobbi": "Tidur",
        "sosmed": "@luciarachel_",
        "kesan": "Kakaknya santai dan asik.",
        "pesan": "Semangat terus kuliahnya Kak rachel, semoga waktu istirahatnya seimbang sama gempuran tugas."
    },
    {
        "nama": "Shafa Delaila Azzahra",
        "nim": "124450124",
        "umur": "20",
        "asal": "Lampung Tengah",
        "alamat": "Perum Pemda",
        "hobbi": "Mainn Bola, Belajar",
        "sosmed": "@Melukis & Menulis",
        "kesan": "Kak Shafa sangat berseni dan berbakat, perpaduan hobinya unik antara olahraga dan karya seni.",
        "pesan": "Semangat terus berkarya dan kuliahnya Kak Shafa, sukses selalu di segala bidang."
    },
    {
        "nama": "Zannuba Arifah Ilman",
        "nim": "124450112",
        "umur": "18",
        "asal": "Lampung Timur",
        "alamat": "Rajabasa",
        "hobbi": "Bengong",
        "sosmed": "@xifasky",
        "kesan": "Kak Zannuba orangnya unik dan tenang, cara berpikirnya santai dan nggak ribet.",
        "pesan": "Semangat terus jalani masa-masa kuliahnya Kak Zannuba, semoga sehat dan sukses selalu."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fz8F-4jj6nfNJdKx48FiEYsU5teK_Kxd",
            "https://drive.google.com/uc?export=view&id=1c0AkGk7YPIGeMzZO3lPKk6RNhVb9dEBZ",
            "https://drive.google.com/uc?export=view&id=1ZYRwFdB4vGHBd7F9i9SVPvmUcHPD__sF",
            "https://drive.google.com/uc?export=view&id=1_i5KXzaP9nlftLvG9FN0O_88dqMt88k4",
            "https://drive.google.com/uc?export=view&id=1fjz2NU-_cxMCulJLMEWW31lq1U_A4eT8",
            "https://drive.google.com/uc?export=view&id=10bkhgX26vkzzXNeWuO-rs5ExqiWzsAd5",
            "https://drive.google.com/uc?export=view&id=1ICEgfnOzPn-M_WaI-lRtalIB57-m7YJX",
            "https://drive.google.com/uc?export=view&id=18s4Oh-CRXs5oO7zs2jqgTlFtXqDofobM",
            "https://drive.google.com/uc?export=view&id=1gf_OKklhnyORWy_EmsaFHNJQyM5d42Jw",
            "https://drive.google.com/uc?export=view&id=1GgF-yb1W-lc6veZsJR6pXRmIZh084jFU",
            "https://drive.google.com/uc?export=view&id=1B-iim7DMD1PlT0X9_7hipDbMPxe-7IgV",
            "https://drive.google.com/uc?export=view&id=1yK56EmqO01DzhrSuuk6pEYhGDkxaIfb8",
            "https://drive.google.com/uc?export=view&id=1jMhextugQ7g88n63FYVziW2d6TNd7iwy",
            "https://drive.google.com/uc?export=view&id=1e6EGJXIjMQaGYgqL3ANvClOaHa1zhxn7",
            "https://drive.google.com/uc?export=view&id=15NNdrlWLFSAcuD5HtHnYhP2EDkhatfMf",
            "https://drive.google.com/uc?export=view&id=1xi6FakcM2DDKUhphZmMo87MkFrdKYVWW",
            "https://drive.google.com/uc?export=view&id=15maVjCPBrBxIROLA7YxRp_USu7phx1kx",
            "https://drive.google.com/uc?export=view&id=183dyxB5ZmzO0gMoDU25ZiI4Qc-JD9oaN",
            "https://drive.google.com/uc?export=view&id=144A5DeJcmNAA0jA-ZFtNpokP3J1oaaKx",
            "https://drive.google.com/uc?export=view&id=1UsMdYo29e3m5jmAidIvD1TN_fU-ncQwC",
            "https://drive.google.com/uc?export=view&id=1e7vyA-ckvRH_pNgCAEMcwLpI-QjDVPl1",
            "https://drive.google.com/uc?export=view&id=1S1q2xyzY9IVCapDNl6_hAxlqayLwiuzz",
        ]
        data_list = [
            {
        "nama": "Arini Puteri Elandra",
        "nim": "123450069",
        "umur": "-",
        "tanggal_lahir": "06 Maret 2005",
        "asal": "LAMPUNG!!!",
        "alamat": "Teluk Betung Selatan",
        "hobbi": "Nonton Kartun",
        "sosmed": "@elandraa_",
        "kesan": "Kak Arini seru dan super friendly sama siapa aja.",
        "pesan": "Semangat terus kuliahnya dan lancar semua urusannya Kak."
    },
    {
        "nama": "Nabyla Sharfina",
        "nim": "123450008",
        "umur": "20 Tahun",
        "tanggal_lahir": "5 November 2005",
        "asal": "Bengkulu",
        "alamat": "Jalan Lapas",
        "hobbi": "Jalan - Jalan",
        "sosmed": "@bylaash",
        "kesan": "Orangnya asyik dan enak diajak ngobrol santai.",
        "pesan": "Sukses terus buat kuliah dan jalan-jalannya ya Kak."
    },
    {
        "nama": "Khoirul Muthoharoh",
        "nim": "123450021",
        "umur": "-",
        "tanggal_lahir": "27 Januari 2005",
        "asal": "Lambar",
        "alamat": "Airan",
        "hobbi": "main",
        "sosmed": "@khoirul_muthoharoh",
        "kesan": "Kak Khoirul baik dan positif vibes-nya berasa banget.",
        "pesan": "Semangat terus ngejar cita-citanya ya Kak."
    },
    {
        "nama": "Ahmad Rizky",
        "nim": "123450050",
        "umur": "21 Tahun ini alhamdulillah",
        "tanggal_lahir": "16 Agustus 2005",
        "asal": "Tangerang Selatan",
        "alamat": "GH",
        "hobbi": "ga ngapa ngapain",
        "sosmed": "@ahmad.rizky____",
        "kesan": "Bang Rizky santai abis dan seru diajak nongkrong.",
        "pesan": "Semangat terus Bang, semoga kuliahnya lancar tanpa beban."
    },
    {
        "nama": "Adinda Deswita Maharani",
        "nim": "124450083",
        "umur": "cepuyuh tayun",
        "tanggal_lahir": "21 Desember 2005",
        "asal": "ikut kadep",
        "alamat": "love earth",
        "hobbi": "jadi idol",
        "sosmed": "@adindaadma",
        "kesan": "Kak Dinda seru dan energinya nular banget.",
        "pesan": "Tetap jadi kating yang ceria dan makin sukses."
    },
    {
        "nama": "Ahmad Bimo Akbar Arkana",
        "nim": "124450113",
        "umur": "-",
        "tanggal_lahir": "23 Juli 2006",
        "asal": "Tanggamus",
        "alamat": "Balam",
        "hobbi": "lihat lihat perumahan",
        "sosmed": "@bimo_arkana",
        "kesan": "Bang Bimo ramah dan gampang berbaur sama adek tingkat.",
        "pesan": "Semoga sukses di akademik sama organisasinya Bang."
    },
    {
        "nama": "Alfaya Abiyyi",
        "nim": "124450006",
        "umur": "nelson piquet",
        "tanggal_lahir": "666",
        "asal": "balam",
        "alamat": "balam",
        "hobbi": "makan yang manis biar manis",
        "sosmed": "@alfabiyi",
        "kesan": "Orangnya unik dan seru diajak diskusi topik random.",
        "pesan": "Semangat terus kuliahnya dan jaga kesehatan."
    },
    {
        "nama": "Asri Meilani",
        "nim": "123450010",
        "umur": "20 tahun",
        "tanggal_lahir": "21 Mei 2006",
        "asal": "Lampung Barat",
        "alamat": "Korpri Raya",
        "hobbi": "menonton film",
        "sosmed": "@asrmeilani",
        "kesan": "Kak Asri baik hati dan ramah banget pas disapa.",
        "pesan": "Semoga urusan kampus dan kuliahnya dipermudah ya Kak."
    },
    {
        "nama": "Bima Ekayasa",
        "nim": "124450106",
        "umur": "-",
        "tanggal_lahir": "25 April 2006",
        "asal": "Lampung",
        "alamat": "Balam",
        "hobbi": "berlaku humoris dan manis",
        "sosmed": "@bimayasa_",
        "kesan": "Bang Bima beneran humoris dan sering bikin ketawa.",
        "pesan": "Sukses terus Bang dan pertahankan sifat asyiknya."
    },
    {
        "nama": "Indah Khairunnisa",
        "nim": "124450077",
        "umur": "20 Tahun",
        "tanggal_lahir": "14 Agustus 2006",
        "asal": "Ampera",
        "alamat": "Disini aja",
        "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
        "sosmed": "@khaindaa_",
        "kesan": "Kak Indah rame dan seru abis diajak ngobrol.",
        "pesan": "Semoga makin sukses dan kuliahnya lancar jaya Kak."
    },
    {
        "nama": "Riska Erlis Dayu Tiara",
        "nim": "124450022",
        "umur": "20 tahun",
        "tanggal_lahir": "15 Juni 2006",
        "asal": "palembang",
        "alamat": "bebas",
        "hobbi": "ngefollow up chat",
        "sosmed": "@erlsriska",
        "kesan": "Kak Riska aktif, cekatan, dan ramah banget.",
        "pesan": "Semangat terus perkuliahannya dan jangan lupa istirahat Kak."
    },
    {
        "nama": "Yollanda Agustina",
        "nim": "124450024",
        "umur": "-",
        "tanggal_lahir": "-",
        "asal": "Kerangka Bawang Sebelah Barat",
        "alamat": "Kayu Mulya",
        "hobbi": "Tanya bang Henry",
        "sosmed": "@yollanda_agustina16",
        "kesan": "Kak Yollanda seru dan nyambung diajak tukar pikiran.",
        "pesan": "Semoga sukses terus ke depannya ya Kak."
    },
    {
        "nama": "Aditya Taufiqurrohman",
        "nim": "123450032",
        "umur": "15 Tahun",
        "tanggal_lahir": "15 September 2004",
        "asal": "tetangga kadep",
        "alamat": "belwis",
        "hobbi": "memancing keributan",
        "sosmed": "@adityatfq",
        "kesan": "Bang Adit rame dan pinter bikin suasana hidup.",
        "pesan": "Semangat terus kuliahnya Bang, semoga lancar terus."
    },
    {
        "nama": "Fathya Intami Gusda",
        "nim": "123450095",
        "umur": "25 tahun",
        "tanggal_lahir": "-",
        "asal": "Tangsel",
        "alamat": "Sukarame",
        "hobbi": "baca wattpad",
        "sosmed": "@fathyya.__",
        "kesan": "Kak Fathya lembut dan ramah banget orangnya.",
        "pesan": "Semangat terus ya Kak jalani masa-masa kuliahnya."
    },
    {
        "nama": "Tarisya Hidayatul Rahmi",
        "nim": "123450052",
        "umur": "-",
        "tanggal_lahir": "$\\sum_{k=1}^{n} k + \\int_{0}^{x} 2x \\, dx + \\sqrt{81} + \\log_{10}(100)$",
        "asal": "Luhak tanah data",
        "alamat": "Gerbar",
        "hobbi": "Jadi orang baik",
        "sosmed": "-",
        "kesan": "Kak Tarisya pinter parah dan tetep rendah hati.",
        "pesan": "Semoga semua cita-cita dan targetnya tercapai Kak."
    },
    {
        "nama": "Ashila Islamisahfa Vanisha",
        "nim": "124450028",
        "umur": "20 tahun",
        "tanggal_lahir": "28 Mei 2006",
        "asal": "sini",
        "alamat": "jauh pokoknya",
        "hobbi": "tidur",
        "sosmed": "@kshigf",
        "kesan": "Kak Ashila ramah dan santai banget pembawaannya.",
        "pesan": "Semangat kuliahnya Kak, kurangi tidur pas jam kelas."
    },
    {
        "nama": "Danil N Fadillah",
        "nim": "124450103",
        "umur": "-",
        "tanggal_lahir": "31 Desember 2006",
        "asal": "Karawang",
        "alamat": "Belakang Polda",
        "hobbi": "Ngasih makan ikan cupang",
        "sosmed": "@d4niel_fdlh",
        "kesan": "Bang Danil chill dan seru diajak ngobrol.",
        "pesan": "Sukses terus Bang buat akademik sama hobinya."
    },
    {
        "nama": "Favian Arkaanda",
        "nim": "124450021",
        "umur": "-",
        "tanggal_lahir": "05 Mei 2006",
        "asal": "Swiss",
        "alamat": "Tanya bapas",
        "hobbi": "ngesen kanan",
        "sosmed": "@fvnnn05",
        "kesan": "Bang Favian kocak dan punya selera humor sendiri.",
        "pesan": "Semangat terus kuliahnya Bang, sukses selalu."
    },
    {
        "nama": "Muhammad Fathiy Zumar Yazid",
        "nim": "124450081",
        "umur": "-",
        "tanggal_lahir": "-",
        "asal": "situlah",
        "alamat": "pohon mulia",
        "hobbi": "nyari hobi",
        "sosmed": "@zydddddd_",
        "kesan": "Bang Zid asyik dan mudah diajak berteman.",
        "pesan": "Semoga makin fokus kuliahnya dan sukses terus Bang."
    },
    {
        "nama": "Muhammad Rizaldi",
        "nim": "124450093",
        "umur": "Masih muda lah",
        "tanggal_lahir": "Hari Jum'at",
        "asal": "Rahim Ibu",
        "alamat": "Pasar lantai 3.5",
        "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
        "sosmed": "@jaldii.__",
        "kesan": "Bang Jaldi menghibur banget dan nggak pernah jaim.",
        "pesan": "Semangat terus perkuliahan dan urusannya Bang."
    },
    {
        "nama": "Saskia Nova Magdalena",
        "nim": "124450074",
        "umur": "20 tahun",
        "tanggal_lahir": "18 November 2026",
        "asal": "Banyak Begal",
        "alamat": "Pinggir Jalan",
        "hobbi": "nonton thinkerbell",
        "sosmed": "@snova.19",
        "kesan": "Kak Saskia baik dan selalu senyum sama siapa aja.",
        "pesan": "Tetap semangat kuliahnya ya Kak, sukses selalu."
    },
    {
        "nama": "Selma Siti Aisyah",
        "nim": "123450044",
        "umur": "20 tahun",
        "tanggal_lahir": "03 Juni 2006",
        "asal": "lampung",
        "alamat": "balam",
        "hobbi": "jalan-jalan",
        "sosmed": "@selmasiti_aisyah",
        "kesan": "Kak Selma ramah dan asyik banget diajak obrol.",
        "pesan": "Semangat terus kuliahnya dan makin sukses ya Kak."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_Qc7WP8qRvLvG_lnMePuUA7qARF7H0l7",
            "https://drive.google.com/uc?export=view&id=1XmSOQ6paBK3Q1NgOBRk_LR6AIcd3brJC",
            "https://drive.google.com/uc?export=view&id=1_3CaxVNmrH7ky8b_OXD9TZ6MYYVLWqoI",
            "https://drive.google.com/uc?export=view&id=1MXKuzyJt2N4RxLqeraJBnbHDynaY_x7n",
            "https://drive.google.com/uc?export=view&id=10eXA6-G0vIzoaLeBRUdUKmAkV1rkxi1f",
            "https://drive.google.com/uc?export=view&id=132fahJ1pSbV3vGwHWywnhAgy9F5-lD3S",
            "https://drive.google.com/uc?export=view&id=16QmUrjSmd6g-08BwxnNfsW5Yp6_C73tj",
            "https://drive.google.com/uc?export=view&id=1coKySCpQM3reaOJnsbyRuZ9wpaSr9Yzy",
            "https://drive.google.com/uc?export=view&id=149G_n5OH8djAG5xuphPbIAmlPkmaZMVn",
            "https://drive.google.com/uc?export=view&id=1Ti-32pekfIk0mjD7h1jsL32AyeQ_keLk",
            "https://drive.google.com/uc?export=view&id=1ASWhbTt-vFowNbRltJQF6oU3YGN6Bhac",
            "https://drive.google.com/uc?export=view&id=1FcGZANQBYVm93F-ZztHUv2ji9O3RrEI9",
            "https://drive.google.com/uc?export=view&id=1b98CcQoa4WfuweB9r_GSQPAU9a_PXdcb",
            "https://drive.google.com/uc?export=view&id=1l6vTy5rzK4j6tv6_mvF5dw4ihO57U4oM",
            "https://drive.google.com/uc?export=view&id=1IZH_LrCuJEEVXusENiuF6KpZcYw6LjcH",
        ]
        data_list = [
            {
        "nama": "Kevin Antonio Junior",
        "nim": "123450109",
        "umur": "21 tahun",
        "asal": "Sulawesi Tengah ",
        "alamat": "Panjang",
        "hobbi": "Mancing",
        "sosmed": "@kevinaj__",
        "kesan": "Bang Kevin santai banget orangnya, hobinya mancing mencerminkan kesabarannya.",
        "pesan": "Semangat terus kuliahnya Bang, semoga makin banyak tangkapan dan urusan lancar."
    },
    {
        "nama": "Gusti Putu Ferazka Dhiyamika",
        "nim": "123450046",
        "umur": "21 tahun",
        "asal": "Bekasi",
        "alamat": "Way Dadi",
        "hobbi": "Mendaki",
        "sosmed": "@ferazkaa",
        "kesan": "Bang Ferazka jiwa petualangnya berasa banget, pembawaannya keren dan santai.",
        "pesan": "Semangat terus kuliahnya Bang, semoga puncak akademiknya bisa digapai dengan lancar."
    },
    {
        "nama": "Ali Aristo Muthahari Parisi",
        "nim": "123450088",
        "umur": "21 tahun",
        "asal": "Lampung Timur",
        "alamat": "Gang Sakum, Belwis",
        "hobbi": "Nonton F1",
        "sosmed": "@ali_parisi3",
        "kesan": "Bang Ali seru diajak diskusi, hobinya nonton F1 bikin vibes-nya makin kencang dan keren.",
        "pesan": "Semangat kuliahnya Bang Ali, semoga perjalanan akademiknya selincah pembalap F1."
    },
    {
        "nama": "Ayu Andriani Parlina Wati",
        "nim": "124450058",
        "umur": "20 tahun",
        "asal": "Lampung Barat",
        "alamat": "Airan",
        "hobbi": "Belajar + menghitung uang",
        "sosmed": "@aayuandrianni_",
        "kesan": "Kak Ayu rajin dan ambis banget, kelihatan dari hobinya yang produktif dan berfaedah.",
        "pesan": "Semangat terus kuliahnya Kak Ayu, semoga rezeki dan keuangannya makin melimpah."
    },
    {
        "nama": "Dafa Elpriza",
        "nim": "124450131",
        "umur": "21 tahun",
        "asal": "Bekasi",
        "alamat": "Way Kandis",
        "hobbi": "Jogging ",
        "sosmed": "@dafaelpriza_",
        "kesan": "Bang Dafa gaya hidupnya sehat banget, pembawaannya energik dan ramah diajak ngobrol.",
        "pesan": "Semangat terus kuliah dan jogging-nya Bang, jaga kesehatan selalu sampai lulus."
    },
    {
        "nama": "Juwita Sari",
        "nim": "124450066",
        "umur": "19 tahun",
        "asal": "Lampung Barat",
        "alamat": "Pemda",
        "hobbi": "Lihat bulan",
        "sosmed": "@ju.juwitaaa_",
        "kesan": "Kak Juwita pembawaannya tenang dan estetik, hobinya unik bikin suasana makin adem.",
        "pesan": "Semangat terus kuliahnya Kak Juwita, semoga harinya selalu bersinar terang."
    },
    {
        "nama": "Muhammad Afdal Lutfi",
        "nim": "124450047",
        "umur": "19 tahun",
        "asal": "Lampung Tengah",
        "alamat": "JI Pulau Damar",
        "hobbi": "Memantau dl tugas",
        "sosmed": "@afdall.03",
        "kesan": "Bang Afdal realistis khas mahasiswa, gaya memantau deadline-nya bikin relate.",
        "pesan": "Semangat terus kuliahnya Bang Afdal, semoga tugas-tugasnya selalu selesai tepat waktu."
    },
    {
        "nama": "Salsabila Nazwa Putri",
        "nim": "124450002",
        "umur": "20 tahun",
        "asal": "Metro",
        "alamat": "Korpri",
        "hobbi": "Nongkrong di Kopken",
        "sosmed": "@slbnzw_",
        "kesan": "Kak Salsa santai dan gaul banget, tipikal kating yang asyik diajak nongkrong bareng.",
        "pesan": "Semangat terus perkuliahan Kak Salsa, semoga selalu ada waktu buat ngopi santai."
    },
    {
        "nama": "Muhammad Ridwan",
        "nim": "123450091",
        "umur": "21 tahun",
        "asal": "Lampung Tengah",
        "alamat": "Belwis",
        "hobbi": "Badminton ",
        "sosmed": "@mridwaan_22",
        "kesan": "Bang Ridwan orangnya seru dan sporty, diajak ngobrolin apa aja selalu nyambung.",
        "pesan": "Semangat terus kuliah dan smash badminton-nya Bang, sukses selalu buat akademiknya."
    },
    {
        "nama": "Andra Ilham Bintang",
        "nim": "124450060",
        "umur": "18 tahun",
        "asal": "Sumatera Selatan",
        "alamat": "Kota Baru",
        "hobbi": "Main rubik",
        "sosmed": "@andra.lhm",
        "kesan": "Bang Andra kelihatannya pinter dan cepat mikir, hobinya main rubik kelihatan keren banget.",
        "pesan": "Semangat terus kuliahnya Bang Andra, semoga masalah rumit di kampus secepatnya terpecahkan."
    },
    {
        "nama": "Bryan Paskah Telaumbanua",
        "nim": "124450003",
        "umur": "22 tahun",
        "asal": "Nias",
        "alamat": "Belwis",
        "hobbi": "Live TikTok",
        "sosmed": "@bryantel_",
        "kesan": "Bang Bryan orangnya kalem tapi kreatif, percaya dirinya oke banget pas live.",
        "pesan": "Semangat terus live dan kuliahnya Bang Bryan, semoga followers dan ilmunya makin nambah."
    },
    {
        "nama": "Ghiyats Thabularasa Meardhy",
        "nim": "124450067",
        "umur": "17 tahun",
        "asal": "Surabaya ",
        "alamat": "Kemiling ",
        "hobbi": "Nanem Sawit ",
        "sosmed": "@meardhy_ghiyats",
        "kesan": "Bang Ghiyats orangnya tinggi, kalem, dan hobinya sangat visioner untuk masa depan.",
        "pesan": "Semangat terus kuliahnya Bang, semoga kebun sawit dan studinya sama-sama berkembang luas."
    },
    {
        "nama": "Indah Julia Mawar Pratiwi",
        "nim": "124450055",
        "umur": "20 tahun",
        "asal": "Pringsewu",
        "alamat": "Airan",
        "hobbi": "Bengong",
        "sosmed": "@indahjuliaa",
        "kesan": "Kak Indah ramah dan baik banget, pembawaannya santai dan nggak pernah bikin tegang.",
        "pesan": "Semangat terus kuliahnya Kak Indah, kurangi bengongnya dan perbanyak senyumnya."
    },
    {
        "nama": "Jacinda Kesya Alvara",
        "nim": "124450023",
        "umur": "18 tahun",
        "asal": "Kalimantan Barat",
        "alamat": "Korpri",
        "hobbi": "Nyapu depan gacoan",
        "sosmed": "@cacalvra",
        "kesan": "Kak Caca vibes-nya positif dan ceria, hobinya unik bikin suasana makin rame.",
        "pesan": "Tetap jadi kating yang ramah dan ceria ya Kak Caca, semangat terus kuliahnya."
    },
    {
        "nama": "Muhammad Rafka Fatih Al Ghathfaan",
        "nim": "124450089",
        "umur": "20 tahun",
        "asal": "Padang",
        "alamat": "Kota Baru",
        "hobbi": "Bangun pagi",
        "sosmed": "@muhammdrafka_",
        "kesan": "Bang Rafka orangnya kalem dan disiplin banget, kebiasaan bangun paginya patut dicontoh.",
        "pesan": "Semangat kuliahnya Bang Rafka, kedisiplinannya semoga berbuah nilai IPK yang memuaskan."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MjRSoAKEuhIp1IGxiDE6rAUz4GKGsPj2",
            "https://drive.google.com/uc?export=view&id=1j6Qugb8qWQEhY1nNYEU491Qe_VcRFMUr",
            "https://drive.google.com/uc?export=view&id=13VfQEvAHY-KZuy0yX7Ak1_Bi73wgj-4x",
            "https://drive.google.com/uc?export=view&id=17I-cOdJQa6cycQdV9Y0MJ0Hv5IpJeig-",
            "https://drive.google.com/uc?export=view&id=1zmcf5V8VJ6yaORx_bnv5tqGsvsawBwve",
            "https://drive.google.com/uc?export=view&id=1lA8lJZDihZOHKQDYpIbH1kKpd7uG4HIF",
            "https://drive.google.com/uc?export=view&id=1ZTLpqMRQ_vWwVHkMa-KrutUw8yKncCVW",
            "https://drive.google.com/uc?export=view&id=1FLRmOffmhRKp_idDxz38RmSAGCqpYNio",
            "https://drive.google.com/uc?export=view&id=1RlIFmKd5iKDk3ybaTdZ9ZMUhbPTG_jHD",
            "https://drive.google.com/uc?export=view&id=1pglrTU1iApv940RxsrZ3avw64VZc3x15",
            "https://drive.google.com/uc?export=view&id=14_vuCu-WEZ0B7DUd81tfqVae2k9TQ0Ml",
            "https://drive.google.com/uc?export=view&id=1fsv2XXfrOr5WuqOcdyDKqOiNJ656ezep",
            "https://drive.google.com/uc?export=view&id=1hmgTwL1KBWCtPA9bzyy1fWLiGrm5fYp0",
            "https://drive.google.com/uc?export=view&id=1S6QGH27NldXIZBP4a8_kCrx7nDbroooK",
            "https://drive.google.com/uc?export=view&id=1RpUm47HYqgzuCubinGKOZpPhdhi9SwxC",
            "https://drive.google.com/uc?export=view&id=18DSsNliU5EdEDKyZRde7lcyStnImFjTB",
            "https://drive.google.com/uc?export=view&id=1U1xKqDOeNn3wCdNkhJaNpe4za3FEVfqS",
            "https://drive.google.com/uc?export=view&id=18RoRLs1Xp8aO610tX5TZm6K2lnMpLsYT",
            "https://drive.google.com/uc?export=view&id=1ZiyzvWTjV3PTIvklj2k09RGCUevIANkd",
            "https://drive.google.com/uc?export=view&id=1ehEL_Ny8wzFLdwRa6whe3AETeSwsGR1W",
            "https://drive.google.com/uc?export=view&id=1rdhwHxoJYZpmyfB8Dum7LZzbnlrElY_g",
            "https://drive.google.com/uc?export=view&id=1PV7F9MWN5bSKFXcBkBS2E3oYynNbCkpR",
        ]
        data_list = [
            {
        "nama": "Fabio Banyu Cyto",
        "nim": "123450104",
        "umur": "21 tahun",
        "asal": "Bandar Lampung",
        "alamat": "Kedaton",
        "hobbi": "Tidur",
        "sosmed": "@biyokcb",
        "kesan": "Bang Fabio santai abis, hobinya tidur tapi kalau udah diajak obrol tetep nyambung.",
        "pesan": "Semangat terus kuliahnya Bang, semoga jam tidurnya makin teratur dan sukses."
    },
    {
        "nama": "Tanty Widiyastuti",
        "nim": "123450094",
        "umur": "21 tahun",
        "asal": "Lampung",
        "alamat": "Airan Raya",
        "hobbi": "Membaca",
        "sosmed": "@tvnty_",
        "kesan": "Kak Tanty wawasannya luas, pembawaannya tenang dan ramah banget pas disapa.",
        "pesan": "Semangat terus perkuliahannya Kak Tanty, semoga makin sukses dan lancar terus."
    },
    {
        "nama": "Fadil Prasetyo Alfarizzi",
        "nim": "123450048",
        "umur": "21 tahun",
        "asal": "Bandar Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Gitar",
        "sosmed": "@fadilalfarizzii",
        "kesan": "Bang Fadil vibes-nya anak band yang asyik, diajak ngobrol seru dan gak garing.",
        "pesan": "Semangat terus kuliah dan bermusiknya Bang Fadil, makin sukses ke depannya."
    },
    {
        "nama": "Manuel Frederika",
        "nim": "124450039",
        "umur": "20 tahun",
        "asal": "Batam",
        "alamat": "Way Kandis",
        "hobbi": "Tenis meja",
        "sosmed": "@manuelfdk_",
        "kesan": "Bang Manuel kelihatannya fokus dan sporty, gaya bicaranya santai dan friendly.",
        "pesan": "Semangat terus kuliah dan main tenis mejanya Bang, lancar sampai lulus."
    },
    {
        "nama": "Ni Made Okta Viola Darma Putri",
        "nim": "124450005",
        "umur": "12 tahun",
        "asal": "Bali",
        "alamat": "Nusa Penida",
        "hobbi": "Menghayal",
        "sosmed": "@Violaadrtr_",
        "kesan": "Kak Viola orangnya kreatif dan unik banget, pembawaannya ceria dan ramah.",
        "pesan": "Semangat terus kuliahnya Kak Viola, semoga khayalannya bisa jadi kenyataan."
    },
    {
        "nama": "Risa Romadona",
        "nim": "124450127",
        "umur": "20 tahun",
        "asal": "Natar",
        "alamat": "Natar",
        "hobbi": "Rolling Skate",
        "sosmed": "@risarmdna",
        "kesan": "Kak Risa hobinya keren banget, pembawaannya energik dan asyik diajak obrol.",
        "pesan": "Semangat terus perkuliahannya Kak Risa, semoga hobinya makin jago dan sukses."
    },
    {
        "nama": "Vannisa Ramadhani",
        "nim": "124450078",
        "umur": "19 tahun",
        "asal": "Kepulauan Riau",
        "alamat": "Teluk Betung",
        "hobbi": "Nonton KHW",
        "sosmed": "@vunnycaa",
        "kesan": "Kak Vannisa imut dan ramah, tipikal kating yang asyik diajak tukar cerita.",
        "pesan": "Semangat terus kuliahnya Kak, semoga tontonannya makin seru dan tugas lancar."
    },
    {
        "nama": "Yulia Kristine Malau",
        "nim": "124450119",
        "umur": "20 tahun",
        "asal": "Jambi",
        "alamat": "Sabah Balau",
        "hobbi": "Belajar",
        "sosmed": "@krnylee",
        "kesan": "Kak Yulia rajin dan ambis banget, sosok kating yang panutan di kelas.",
        "pesan": "Semangat terus belajar dan kuliahnya Kak, semoga usahanya berbuah manis."
    },
    {
        "nama": "Akeyla Fairuz Shafi",
        "nim": "123450119",
        "umur": "21 tahun",
        "asal": "Bandar Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Berenang",
        "sosmed": "@keyashafi_",
        "kesan": "Kak Akeyla gampang akrab dan ramah, vibes-nya positif dan bikin nyaman.",
        "pesan": "Semangat terus perkuliahannya Kak Akeyla, sukses selalu buat urusannya."
    },
    {
        "nama": "Elsa Sitorus",
        "nim": "124450088",
        "umur": "21 tahun",
        "asal": "Sumatera Utara",
        "alamat": "Pemda",
        "hobbi": "Rebahan",
        "sosmed": "@_els.a",
        "kesan": "Kak Elsa santai banget orangnya, pilihan hobinya sangat relate buat mahasiswa.",
        "pesan": "Semangat terus kuliahnya Kak Elsa, semoga rebahannya makin berkualitas."
    },
    {
        "nama": "Fadya Izzatul 'Aini",
        "nim": "124450062",
        "umur": "20 tahun",
        "asal": "Pringsewu",
        "alamat": "Airan",
        "hobbi": "Mancing",
        "sosmed": "@fadyaizzatul_",
        "kesan": "Kak Fadya penyabar dan santai, hobinya unik bikin pembawaannya makin chill.",
        "pesan": "Semangat terus kuliahnya Kak Fadya, semoga makin banyak hal baik didapat."
    },
    {
        "nama": "Lovianora Saragih",
        "nim": "124450105",
        "umur": "19 tahun",
        "asal": "Sumatera Utara",
        "alamat": "Way Huwi",
        "hobbi": "Dengerin musik",
        "sosmed": "@_loviaa",
        "kesan": "Kak Lovia pembawaannya adem dan baik hati, enak diajak ngobrol santai.",
        "pesan": "Semangat terus kuliahnya Kak Lovia, semoga harinya selalu diiringi lagu seru."
    },
    {
        "nama": "M. Alsi Syahrulloh",
        "nim": "124450092",
        "umur": "20 tahun",
        "asal": "Kalianda",
        "alamat": "Kota Baru",
        "hobbi": "Main game, tidur",
        "sosmed": "@aruccy_",
        "kesan": "Bang Alsi seru diajak ngobrolin game, orangnya santai dan nggak ribet.",
        "pesan": "Semangat terus kuliah dan main gamenya Bang Alsi, lancar selalu urusannya."
    },
    {
        "nama": "Sherena Florencia",
        "nim": "124450027",
        "umur": "19 tahun",
        "asal": "Bengkulu Selatan",
        "alamat": "Belwis",
        "hobbi": "Make up",
        "sosmed": "@sher_renna",
        "kesan": "Kak Sherena kelihatan rapi dan modis, pembawaannya ramah dan asyik.",
        "pesan": "Semangat terus perkuliahannya Kak Sherena, makin sukses dan menginspirasi."
    },
    {
        "nama": "Razin Hafid Hamdi",
        "nim": "123450096",
        "umur": "21 tahun",
        "asal": "Padang",
        "alamat": "Belwis",
        "hobbi": "Futsal",
        "sosmed": "@razyn.hfd",
        "kesan": "Bang Razin vibes-nya anak futsal yang aktif dan asyik diajak nongkrong.",
        "pesan": "Semangat terus kuliah dan futsalnya Bang Razin, sukses akademiknya."
    },
    {
        "nama": "Faiza Try Anjani",
        "nim": "124450075",
        "umur": "19 tahun",
        "asal": "Padang",
        "alamat": "Belwis",
        "hobbi": "Baca novel",
        "sosmed": "@faizaanjanii",
        "kesan": "Kak Faiza kelihatan tenang dan lembut, pembawaannya ramah banget.",
        "pesan": "Semangat terus kuliahnya Kak Faiza, semoga makin banyak bacaan novel seru."
    },
    {
        "nama": "Gathfan Nadif Ali",
        "nim": "124450001",
        "umur": "20 tahun",
        "asal": "Bandar Lampung",
        "alamat": "Rajabasa",
        "hobbi": "Main game",
        "sosmed": "@gathfannadif",
        "kesan": "Bang Gathfan orangnya santai dan asyik, pinter juga pas diajak diskusi.",
        "pesan": "Semangat terus kuliah dan gamenya Bang, semoga makin lancar akademiknya."
    },
    {
        "nama": "Hafidz Wahdiansyah",
        "nim": "124450064",
        "umur": "20 tahun",
        "asal": "Metro",
        "alamat": "Metro Kibang, Lampung Timur",
        "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
        "sosmed": "@apiszzaja_",
        "kesan": "Bang Hafidz produktif banget, gabungan hobi ngoding sama ngegame-nya keren.",
        "pesan": "Semangat terus 3N-nya Bang, semoga kodingannya running lancar tanpa error."
    },
    {
        "nama": "Kaleb Filbert Istel",
        "nim": "124450053",
        "umur": "20 tahun",
        "asal": "Bandar Lampung",
        "alamat": "Campang Raya",
        "hobbi": "Ngegym, baca novel",
        "sosmed": "@kelelep_comberan",
        "kesan": "Bang Kaleb perpaduan hobinya unik banget, badan kekar tapi suka baca novel.",
        "pesan": "Semangat ngegym dan kuliahnya Bang Kaleb, semoga selalu konsisten dan sukses."
    },
    {
        "nama": "Melva Shaprina Febrianti",
        "nim": "124450087",
        "umur": "19 tahun",
        "asal": "Sumatera Selatan",
        "alamat": "Sukarame",
        "hobbi": "Scroll",
        "sosmed": "@melva_fbrt",
        "kesan": "Kak Melva santai dan kekinian, tipikal kating yang asyik diajak obrol santai.",
        "pesan": "Semangat terus perkuliahannya Kak Melva, sukses selalu buat ke depannya."
    },
    {
        "nama": "Muhammad Syafiqul Falakh",
        "nim": "124450099",
        "umur": "20 tahun",
        "asal": "Lampung Utara",
        "alamat": "Asrama TB 3",
        "hobbi": "Membaca",
        "sosmed": "@Syaafiqui",
        "kesan": "Bang Syafiq pembawaannya teratur dan kritis, pengetahuannya berasa luas.",
        "pesan": "Semangat terus kuliahnya Bang Syafiq, semoga ilmunya makin bermanfaat."
    },
    {
        "nama": "Rifky Henry Ferdianto",
        "nim": "124450115",
        "umur": "28 tahun",
        "asal": "Kota bumi",
        "alamat": "Rajabasa",
        "hobbi": "Lari dari kenyataan",
        "sosmed": "@henryferdianto",
        "kesan": "Bang Henry orangnya humoris parah, candaannya selalu bikin suasana cair.",
        "pesan": "Semangat terus kuliahnya Bang Henry, jangan lari dari kenyataan terus ya."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lzo6ajegSnKwvplVSzmpyq1CUv3H01dp",
            "https://drive.google.com/uc?export=view&id=1QeB4ZERsmZWR6s9r2Tci8GrnpxAcydnH",
            "https://drive.google.com/uc?export=view&id=1SybE6V95cH2GLfQTSI_mcs87x8tAi63_",
            "https://drive.google.com/uc?export=view&id=1HWbcmEaLCqZ-KkYmZV2tEl_1Fj2S2P3P",
            "https://drive.google.com/uc?export=view&id=1XvIr7NS_AJty2bvkhDLoUIlJvXZnLjf8",
            "https://drive.google.com/uc?export=view&id=1Ag7bZuL5VEmmiPEQbMwboJQCN26j4mN1",
            "https://drive.google.com/uc?export=view&id=1sB6xvFZ3ajgiWSwRGxpGIDHy1zULje4f",
            "https://drive.google.com/uc?export=view&id=1GwsJhm4LGvgUT2LVuwbZuEB0AwrGEQgT",
            "https://drive.google.com/uc?export=view&id=1IOr5iCnR0TWK3TL1lQc1R2ZSdJdX9DJE",
            "https://drive.google.com/uc?export=view&id=1XCc7IpAfjphAyuhCc50yG6-D_FPrRh7y",
            "https://drive.google.com/uc?export=view&id=1W3ct2zfnicGrS8Uh1Roux5gJVZjq4wc_",
            "https://drive.google.com/uc?export=view&id=1rveJ8LftxxU_NEmDlhPnSSNlKSVxuV9l",
            "https://drive.google.com/uc?export=view&id=10eZ7ldoUIiWiHhU3-TC91OttEOh-Ylv0",
            "https://drive.google.com/uc?export=view&id=1LuGM_kcjDzZMICxSf-rb9EPQ6aNqrv9E",
            "https://drive.google.com/uc?export=view&id=1jmGobQ6qYNnZoOdqOagxTewjpB2vqGBj",
            "https://drive.google.com/uc?export=view&id=1Y_eFafDI4MxwiDnqNV6K7i5-7lerzIJC",
            "https://drive.google.com/uc?export=view&id=1VzPNC9xzQltUZOksxEu5vnT8HbDiJO9x",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta baik, keren",  
                "pesan":"Semoga diberi kelancaran dan kesuksesan kaa"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baik dan disiplin bangett",  
                "pesan":"Semoga apapun yang kaka gapai kecapai kaa"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel itu baik, terus kalo jelasin materi itu caranya bagus banget",  
                "pesan":"Semogaa sukses dan sehat selalu ya bangg"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi cool terus asik deh",  
                "pesan":"Semoga selalu lancar bang kuliahnya"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake baik, terus ramah juga kalau papasan",  
                "pesan":"Semoga sehat dan banyak rezeki bang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar tegas, disiplin",  
                "pesan":"Semoga selalu diberi kelancaran bang di hal apapun"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia itu tegas, ramah, dan juga alpha woman bangetss",  
                "pesan":"Semoga selalu sehat dan dilipahkan rezeki kaa"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, cool, dan rambutnya keren",  
                "pesan":"Semoga apa yang abang capai di kabulkan"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri baik, ramah",  
                "pesan":"Semoga apa yang kaka pengen kecapai kaa"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta humble, terus baik banget",  
                "pesan":"Semoga selalu sehat dan bahagia ya kaa"# 1
            },            
            {
        "nama": "Desman Velius Halawa",
        "nim": "123450113",
        "umur": "25",
        "asal": "Nias",
        "alamat": "Airan",
        "hobbi": "Main musik",
        "sosmed": "@dsmanhal",
        "kesan": "Bang Desman asyik, humble, dan jago banget defense futsalnya.",
        "pesan": "Semangat terus kuliah dan main musiknya Bang, sukses selalu."
    },
    {
        "nama": "Azzelya Thianandry",
        "nim": "124450041",
        "umur": "19",
        "asal": "Bandar Lampung",
        "alamat": "Sukarame",
        "hobbi": "Pilates",
        "sosmed": "@azzelytn",
        "kesan": "Kak Azzel kalem dan ramah banget pas diajak ngobrol.",
        "pesan": "Semoga selalu bahagia di mana pun berada ya Kak."
    },
    {
        "nama": "Charrlindah",
        "nim": "124450037",
        "umur": "21",
        "asal": "Jakarta Pusat",
        "alamat": "Cendrawasih 1",
        "hobbi": "Ngurus Peternakan",
        "sosmed": "@charrlln",
        "kesan": "Kak Charrlindah santai, baik, dan seru pembawaannya.",
        "pesan": "Semoga selalu sehat dan lancar urusannya ya Kak."
    },
    {
        "nama": "Jeremi Marolop P. Situmorang",
        "nim": "124450111",
        "umur": "17",
        "asal": "Jayapura",
        "alamat": "RS Airan",
        "hobbi": "Nonton a day in my life",
        "sosmed": "@jemarrro",
        "kesan": "Bang Jere kece, asyik, dan humble banget orangnya.",
        "pesan": "Semoga selalu kuat, sehat, dan sukses kuliahnya Bang."
    },
    {
        "nama": "Nabila Nur Azizah",
        "nim": "124450048",
        "umur": "18",
        "asal": "Lampung",
        "alamat": "Barokah",
        "hobbi": "Main roblox",
        "sosmed": "@n.bila_a",
        "kesan": "Kak Nabila santai dan ramah banget kalau disapa.",
        "pesan": "Semoga semua urusan kuliahnya dilancarkan terus ya Kak."
    },
    {
        "nama": "Rafli Al Mansyah Tambunan",
        "nim": "124450007",
        "umur": "18",
        "asal": "Sibolga",
        "alamat": "Belwis",
        "hobbi": "Membaca peraturan rektor",
        "sosmed": "@dearfkvmfl",
        "kesan": "Bang Rafli rambutnya keren terus, gaya bicaranya juga asyik.",
        "pesan": "Semoga sehat selalu dan semua keinginannya terwujud Bang."
    },
    {
        "nama": "Salafi Maharani",
        "nim": "124450090",
        "umur": "20",
        "asal": "Lampung Timur",
        "alamat": "jatimulyo",
        "hobbi": "Minum air putih",
        "sosmed": "@afi.nhr",
        "kesan": "Kak Salafi lucu, kalem, dan asyik diajak ngobrol.",
        "pesan": "Semoga selalu sehat dan dimudahkan segala urusannya ya Kak."
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()


