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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SCwtHz2HqyvQe_rPFmxXMB6mxV6EW5xf",
            "https://drive.google.com/uc?export=view&id=11k208IYsZRYf6balagxJFgynXRtRhaUa",
            "https://drive.google.com/uc?export=view&id=1SacmfYoVUoM3jum3IAZ8ZA4gXGPvaIwl",
            "https://drive.google.com/uc?export=view&id=1bDh95fxOoUmUtutTAMaaMBhapk5x32Ll",
            "https://drive.google.com/uc?export=view&id=18FVRDsJNNnEVDhfMOsOMXtMUzvQoDJB7",
            "https://drive.google.com/uc?export=view&id=1RHlnabZOOEHvoP2rW7SHKKHorcnYlB18",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung ",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "Abangnya asik , ramah , dan aura pemimpin nya menyala heheh",  
                "pesan":" Stay humble ya bangg , semoga lancar luncur untuk kedepannyaa."
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya ada aura aura ustad nya heheh.",  
                "pesan":"Semangat terus bang dan jangan menyerah heheh!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Kakak nya humble dan cantik.",  
                "pesan":"Semoga hal - hal baik selalu datang pada kakak yaa "
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya ramah trus keliatan dewasa hehe",  
                "pesan":"Sukses terus ya bang, semoga semua yang diusahain lancar"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak nya cantik , trus baik juga",  
                "pesan":"Semangatt dan tetap tersenyum kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik, cakepp juga ",  
                "pesan":"Be happy ya kaa heheh"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# BADAN KESENATORAN
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c64PsaYVJM4OTYebgsX_oYX2bH_OCChl",
            "https://drive.google.com/uc?export=view&id=1wMUo-SlRKvKN0f8oHdKSJeJJ4eIRTrEq",
            "https://drive.google.com/uc?export=view&id=1Vya_0DFbHUz7UqW3eBREuFCU1HL8ZaQP",
            "https://drive.google.com/uc?export=view&id=15Gi8f-PIqAcwGblk13JUw7bH8HQhL-cU",
            "https://drive.google.com/uc?export=view&id=1LZ9SBhfbnyutF7M9thr-sUzqwHU4B4HC",
            "https://drive.google.com/uc?export=view&id=15J9Zo3H3NQ5dtRbqi5E2j-b9XnQ3kr7F",
            "https://drive.google.com/uc?export=view&id=1K_XzYfG3oEOJvCGbpNQTVs8gJXgh5xDO",
            "https://drive.google.com/uc?export=view&id=1QIBMd20oB07uP2NsaQWkNSnfGQhpndFg",
            "https://drive.google.com/uc?export=view&id=1D-Pzk1PVjhSh_7TEXbR-bcjSSRMZISR2",
            "https://drive.google.com/uc?export=view&id=1xb2cwi7-CVg15FQUNV2GUMsJib2myDi1",
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
                "kesan": "Kakak nya udah cantik , pintarr lagii , keren kak",  
                "pesan":"Semangat kakak senatorr , hal hal baik menunggu kakak"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak nya cantik , ramah juga ,suka liatnyaa ",  
                "pesan":"Sehat selalu kakak cantik"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta ",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Abang nya asik plss , murah senyum heheh",  
                "pesan":"Always be kind ya bang"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak nya cakep dehh",  
                "pesan":"Semangat kakak cantik"
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abang nya humblee",  
                "pesan":"Semangat dan sehat selalu ya abang"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "MAMIH GUWEH cakepp banget ini mahh ",  
                "pesan":"Semangat ya kakak , kalau cape sini cerita heheh, sayang kakak banyak - banyak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya humble dan welcome nih",  
                "pesan":"Semangat bang , jangan menyerah heheh"
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Wah kakak nya cakep parah",  
                "pesan":"Semangat untuk segalanya kakak cantik"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abang nya kelihatannya pendiem hehe",  
                "pesan":"Semangat selalu abangg"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakanya cantik dan asikk",  
                "pesan":"Sehat selalu kak dan tetap semangat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yheurhi2SDntsUjvc_AfKLNNwAkIIQ9y",
            "https://drive.google.com/uc?export=view&id=1BXZlhZmAfocEDsRiv5-GTpcDkypYVrLz",
            "https://drive.google.com/uc?export=view&id=1HP6D3Vp1c04NDo1WO55IDTMxl21Vv7vL",
            "https://drive.google.com/uc?export=view&id=1J-6X-4ZWXkiFMK9Jz1D1Lyhcpiq_za7v",
            "https://drive.google.com/uc?export=view&id=1wo-wzkT7QUB92rbAtQFfgTUi2764MJAS",
            "https://drive.google.com/uc?export=view&id=1qcydvF1rhMJl8imF4OsIHNz15oMwvfjr",
            "https://drive.google.com/uc?export=view&id=1aPUQy_xXr6pL7Xmjv_fwuxDbWGm6DUAn",
            "https://drive.google.com/uc?export=view&id=1pzoV2n7B4hU9Ze5860Y6AAY1e0HK73-u",
            "https://drive.google.com/uc?export=view&id=12DSy062JaGyhNLcRFx1Q_PWJFPdsVIg1",
            "https://drive.google.com/uc?export=view&id=1iG2BudsZvjZXc-nx1250fmLWtnt05NEs",
            "https://drive.google.com/uc?export=view&id=1uz9rJInvC_W7LqNkdwOY_E4CqGTJjDhq",
            "https://drive.google.com/uc?export=view&id=1CzRY6Rb9WmBVRn-dr0KI8VCJdlYDjxHf",
            "https://drive.google.com/uc?export=view&id=1zMIukkTgQtvcBpvHPzCeonLqD7WQUOe9",
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
                "kesan": "Abang nya humble , asik jugaa",
                "pesan": "Lancar luncur studi nya ya bangg, semangat abangg "
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya cantik parah , ramah jugaa ",
                "pesan": "Semoga hal hal baik selalu menghampiri kakak ya "
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "WIHH ada abang jagoo, keren selalu bawaannya heheh",
                "pesan": "Semoga hal hal baik selalu menghampiri abang ya"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Humble parah abang nya ",
                "pesan": "Semangat selalu abangg"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "KAKAK nya cantikk euyy",
                "pesan": "Semangat teruss kak "
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Baik dan humble abangnya ",
                "pesan": "Semoga hal hal baik selalu menghampiri abang ya"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "kakaknya nya cantikk dan humble",
                "pesan": "Sehat selalu dan tetap semangat kak"
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakanya cantik dan baikk jugaa ",
                "pesan": "Semoga hal hal baik selalu menghampiri kakak ya"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Ramahh dan welcome kaka nya ",
                "pesan": "Sukses terus ya, Kak, semoga semua yang diusahain lancar"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "Abang ini baikk, ramah jugaa ",
                "pesan": "Jangan bosen-bosen buat jadi orang baik yaa bang"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Abang nya baikk, humble juga",
                "pesan": "Jangan bosen-bosen buat jadi orang baik yaa bang"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya humblee ihh sukaa",
                "pesan": "Semangat selalu kakak."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak nya asik dan humble juga",
                "pesan": "Sukses terus ya, Kak, semoga semua yang diusahain lancar "
            },
        ]
        display_images_with_data(gambar_urls, data_list) 
    Baleg()      

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yQ7d9bkO8n-iNf0Wm3N25TSfD9C0_rjU",
            "https://drive.google.com/uc?export=view&id=1rT8Uv1gvcX7RtFCmajVczNc6kkoErM6_",
            "https://drive.google.com/uc?export=view&id=1mohJhTKC6d5smexGVu9WLB_hJDJCp8Js",
            "https://drive.google.com/uc?export=view&id=1eZ5A8Qq0S6a135wmx3wxolpKMWzBYVKQ",
            "https://drive.google.com/uc?export=view&id=1u4iR3h7zs7dSShZk8IFeQrERVnbEp11S",
            "https://drive.google.com/uc?export=view&id=1dIapYXxqnDjaI4h3nS1yjvnPEDi2o1zM",
            "https://drive.google.com/uc?export=view&id=1INI73XgMcZDv2IQPtthSX9cELCpMz2Jb",
            "https://drive.google.com/uc?export=view&id=1yY0xEdiCBVQ9CUjSrzQcyMMFwgN5Kco3",
            "https://drive.google.com/uc?export=view&id=1IcKP3FSAffeJfqErJdh9NHx-YLq-iWDO",
            "https://drive.google.com/uc?export=view&id=1ozFN8f-2rjuyIWNjiGao-x_8IYaqUm2C",
            "https://drive.google.com/uc?export=view&id=1njxHmnOq7HGc-MOI866isFysAYthJ4ox",
            "https://drive.google.com/uc?export=view&id=1hPxU3zNiM6WhB89wZJiiFiFTRHFCS8Ef",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf ",
                "nim": "123450110",
                "umur": "21",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya asik banget, seru diajak ngobrol", 
                "pesan":"Sukses terus ya, Kak, semoga semua yang diusahain lancar"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Vibes kakak nya positif banget",  
                "pesan":"Sehat selalu ya, Kak, jangan terlalu capek sama kesibukannya"
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakanya humblee hehe",  
                "pesan":"Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal":"Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak nya cakep deh",  
                "pesan":"Semoga segala urusannya selalu dipermudah kak"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal":"Lampung Tengah ",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube ",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Abangnya baik dan ramah",  
                "pesan":"Sehat selalu ya, Kak, jangan terlalu capek sama kesibukannya"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Cakep kakak nya ",  
                "pesan":"Spill dracin fav nya dong kak"
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Bang Iqbal asprak alpro seruuwe",  
                "pesan":"Lancar dan semangat terus yaa bang kuliahnya "
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakanya cakep ",  
                "pesan":"Semoga segala urusannya selalu dipermudah kak"
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Baturaja Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Abangnya ramahh heheh",  
                "pesan":"Sehat selalu bang"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "ASIK abangnya",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik kak"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Humble dan cakep kakak nya",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik kak"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal":"Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya ramahh ",  
                "pesan":"Semangat terus kuliahnya, jangan lupa istirahat juga kak "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1M4rAWxTqkOgRrZKDUkB5CFm6IGJweFzL",
            "https://drive.google.com/uc?export=view&id=1gehFZIjlWF09eDpKMdNsqWYxIWHMXbiN",
            "https://drive.google.com/uc?export=view&id=1fmREPFQ-26K10XmGRNlRxrt9_kYapAli",
            "https://drive.google.com/uc?export=view&id=1uXrULd1HV4lK2U6s3gZXMfowttNj8eSk",
            "https://drive.google.com/uc?export=view&id=1OKi2HpFKTHI7Uvp2LrweO_PxB4gzIwUR",
            "https://drive.google.com/uc?export=view&id=1fy-SerzwK41IOv0DNFee2gXS8pIunXSY",
            "https://drive.google.com/uc?export=view&id=1XUiNdaG1_1vTcxAfzp3LvlGmfwY5pOsv",
            "https://drive.google.com/uc?export=view&id=1vev2aiJUyedcbQ3nNk2XIzDfqitAkuco",
            "https://drive.google.com/uc?export=view&id=1izwgrjItGfUddplsphBHtxlTJ11u9cJU",
            "https://drive.google.com/uc?export=view&id=1FEZyHs1Nfb-JJGiUAzB5Rg21xyTtY8Ck",
            "https://drive.google.com/uc?export=view&id=1Berh8_0gShsGG8ctCnx0rj6-q96c_YTL",
            "https://drive.google.com/uc?export=view&id=1RncelyanOUTdTr9MxmPx1v64zH---i7e",
            "https://drive.google.com/uc?export=view&id=1O5xr2IW7JUERQTEfi_289KRqGmW04rD5",
            "https://drive.google.com/uc?export=view&id=19Y9GoKfjhFZWQjPHE1QegNsQi5PcP9NN",
            "https://drive.google.com/uc?export=view&id=1KU3XaVw-vftGLVQk73tHp8Knr8ZsgAcH",
            "https://drive.google.com/uc?export=view&id=1NOensqJBFX_MFTQVmiOldWx3TBLsomUH",
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
                "kesan": "Abang ini asikk bgtt ",  
                "pesan": "Sehat selalu ya, Kak, jangan terlalu capek sama kesibukannya abang."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakanya cantikk baik dan humble",  
                "pesan": "Semoga segala urusannya selalu dipermudah kak"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya RAMAHH bangett ihh terharu dehh",  
                "pesan": "Stay humble ya kakak heheh"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang nya asikk ",
                "pesan": "Jangan lupa bahagia di tengah kesibukan ya, Kak"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Asikk abangnyaa , keren parah ",  
                "pesan": "Semoga segala urusannya selalu dipermudah abangg"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kaka nya cantik dan humble hehe",  
                "pesan": "Always happy ya kakak"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kakak nya humble dan asikkk bgtt",  
                "pesan": "Lancar luncur kakak buat segalanya"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Abangnya asik dan baik bgt ",  
                "pesan": "Semoga selalu dikelilingi orang-orang baik ya bangg"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Humble dan cakep kakanya",  
                "pesan": "Jangan lupa bahagia di tengah banyaknya kesibukan ya, Kak"
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Humble dan asik abangnya ",
                "pesan": "Sehat selalu dan tetap semangat ya bang"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak cantik dan baikk ",
                "pesan": "Semoga segala urusannya selalu dipermudah kak"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Cantik dan ramahh kakanya",
                "pesan": "Semoga selalu dikelilingi orang-orang baik"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Kaka nya maniss dehh",
                "pesan": "Jangan lupa bahagia di tengah banyaknya kesibukan ya, Kak"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Humble kakanya , cantik juga",
                "pesan": "Doa terbaik buat Kakak, semoga sukses selalu"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Abangnya baik dan seruu",
                "pesan": "Lancar luncur buat segalanya ya bang "
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Cakepp kakak nya ",
                "pesan": "Tetap jadi diri sendiri dan jangan gampang nyerah ya, Kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HTBKFbr-qMuhoL3LjLZD5IlAeXvlFMeC",
            "https://drive.google.com/uc?export=view&id=1RWkjjpUkmV1BZLyN-NzBCiaoc8mi1Zrd",
            "https://drive.google.com/uc?export=view&id=1yczQtqWkMCnskkIHF2PGmkFNLk8NUif0",
            "https://drive.google.com/uc?export=view&id=1JpWg-jmzQOFuYpcE4WlOl8_4SsaDUIH2",
            "https://drive.google.com/uc?export=view&id=1q3pgk6BEPfLgTH5vUf8-Of3vcnT4-JmT",
            "https://drive.google.com/uc?export=view&id=1LnsSSV4K2vXsYNpeNVjFaeVVXN1JGL4q",
            "https://drive.google.com/uc?export=view&id=1r7uYfIHGi3_-WuF8OufzMFQmzBeO2zNe",
            "https://drive.google.com/uc?export=view&id=1K0ku-EST9GkKFlvEGt84AP7oyScX69x9",
            "https://drive.google.com/uc?export=view&id=1Iy38Gr9T2ykaDIh2RlWw6Nk-jXkOs7jA",
            "https://drive.google.com/uc?export=view&id=1AW-OODsVO5WY2GZ5GXMYlXmNvwHyR5b3",
            "https://drive.google.com/uc?export=view&id=1Y7Bw0vNkhCK1SgWmC0rmQlHSlSV12J9z",
            "https://drive.google.com/uc?export=view&id=1IyXXcQZhcKnzH-9GryS_jIziz0znskvH",
            "https://drive.google.com/uc?export=view&id=10kXEueyjU6jux83ly7Rqw15V-_mrEqLf",
            "https://drive.google.com/uc?export=view&id=1zqV-IQjwha9lYEESYD9WaBc1LJBrR0_T",
            "https://drive.google.com/uc?export=view&id=1gkERNil5vkX_iSAHFQ6wGWgTqF-f22nH",
            "https://drive.google.com/uc?export=view&id=1ELenmBhtiCuq_mD_A2d_GxbFPOCSnXQI",
            "https://drive.google.com/uc?export=view&id=1kO0lnAbNc5eYIINllb_eCAi0J5TtLzWV",
            "https://drive.google.com/uc?export=view&id=17wKPf6DYsYhLc7qj3h8d2CgTyTPlRfP9",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat ",
                "alamat": "Way Huwi, Jati Agung, Lampung Selatan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Cantik dan humble  ",  
                "pesan":"Sukses terus ya, Kak, semoga semua yang diusahain lancar"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "ASIKK  dan seru kakak nya",  
                "pesan":"Sehat selalu kak "
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abang nya baik , humble juga ",  
                "pesan":"Lancar luncur segalanya bang"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Cantik kakanya",  
                "pesan":"Be happy selalu ya kakak"
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "KAKAK nya asikik",  
                "pesan":"Sehat selalu kakak"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Keren kakak nya ",  
                "pesan":"Semangat dan sehat selalu kakak "
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Humble, cakep jugaa ",  
                "pesan":"Jangan bosen-bosen buat jadi orang baik yaa, Kak"
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Abang nya seruu dan keren ",  
                "pesan":"Sehat selalu ya bangg"
            },
            {    
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak nya cantik dehh",  
                "pesan":"Sukses terus ya, Kak, semoga semua yang diusahain lancar"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "ASIKK dan humble",  
                "pesan":"Sehat selalu ya kak"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "KAKAK nya cakepp",  
                "pesan":"Sehat selalu ya kakak cantik "
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak nya asikk dan ramah",  
                "pesan":"Semoga segala urusannya selalu dipermudah"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakaknya asikk deh",  
                "pesan":"Semoga selalu dikelilingi orang-orang baik kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Humble parahh",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Baikk deh abangnya",  
                "pesan":"Jangan lupa bahagia di tengah banyaknya kesibukan ya bangg"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Ka Lucia cantik dehhh",  
                "pesan":"Jangan lupa bahagia di tengah banyaknya kesibukan ya, Kak "
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@_shaazzh",
                "kesan": "Kakak nya cakepp",  
                "pesan":"Jangan lupa bahagia di tengah banyaknya kesibukan ya, Kak"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kakaknya cantik dan baik deh",  
                "pesan":"Semangat terus ngejalanin hari-harinya, Kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rYecAZoyW2anZ1N0S_hx0RC6WJ8ika4J",
            "https://drive.google.com/uc?export=view&id=1lhR4adr47BPoB6KDq99XExIfqp_gcTwZ",
            "https://drive.google.com/uc?export=view&id=1zl4438J-xeuublGE31muBux9HKuzK3Mz",
            "https://drive.google.com/uc?export=view&id=1CMDhdqJu2OWBTtn-lg1p4i7Dn5ocDvPh",
            "https://drive.google.com/uc?export=view&id=1KgDC9IYSJSS56-1BlWLZlmujUOzrWxPr",
            "https://drive.google.com/uc?export=view&id=1W6iz83nhjPKif0JEcxTKWTGpkURN4QAg",
            "https://drive.google.com/uc?export=view&id=16z5gDPwrkS1yMOHtUDfamPNmLzPlJJya",
            "https://drive.google.com/uc?export=view&id=19se2hy3BLM2HY2LpBcUSd3xDJmH62twX",
            "https://drive.google.com/uc?export=view&id=1dzI09egQ2_dTq6rxCuT1ucz4c13dx5l1",
            "https://drive.google.com/uc?export=view&id=1Yc7te6Q6NJSMR_i_UKP93PNfqyOfM_cy",
            "https://drive.google.com/uc?export=view&id=1h9O40hBHoUWm9-L6DMBkM6VC6_pb_Lys",
            "https://drive.google.com/uc?export=view&id=164eP31w2RRrvkAruTjKP8zmpjtdTFodo",
            "https://drive.google.com/uc?export=view&id=11MA2Lu_ul5kszEM25SSUcgp0bQOkUmr8",
            "https://drive.google.com/uc?export=view&id=1pjZIZvECZYZb0ELADTKs8_QlehCGjaGe",
            "https://drive.google.com/uc?export=view&id=1m4wtEgyPCvh1NWRCMcD2eTaUPAyBBopx",
            "https://drive.google.com/uc?export=view&id=1JoEZ8ezd8Bb0cFY4PWhPj7DHu4X2AzWa",
            "https://drive.google.com/uc?export=view&id=1aSpL2wOjN85SMtDY5o4MKB9xzZD-0KcT",
            "https://drive.google.com/uc?export=view&id=1cjMTiz0w3yO6d4cPxxP0ks8wlBqdGil7",
            "https://drive.google.com/uc?export=view&id=1Rk-E7VQahmGVbEsSLU5Sork5-OTE10CV",
            "https://drive.google.com/uc?export=view&id=1MyEvX3hEOYp0qHXfPxu40C_G5ExDanpM",
            "https://drive.google.com/uc?export=view&id=1Oq21iRTcsBCv-3-gy5GaxepOFJtFizYC",
            "https://drive.google.com/uc?export=view&id=18FKBVlWW9nSZik7ygJ3ADUvHYHgV1sqh",
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
                "kesan": "Kakak ini asik dan humble banget ",
                "pesan": "Semangatt selalu kakakk"
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
                "kesan": "Cakep bgt kakak nya dehh",
                "pesan": "Sehat selalu kakak!"
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
                "kesan": "Humble dan baikk dehh",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
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
                "kesan": "Orang nyaa asikk",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
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
                "kesan": "Humble orangnya dehh",
                "pesan": "Semangat dan sehat selalu kak"
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
                "kesan": "Baik dan humble kakaknya ",
                "pesan": "Sehat selalu dan tetap semangat kak"
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
                "kesan": "Orangnya asik deh",
                "pesan": "Semoga segala urusannya selalu dipermudah"
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
                "kesan": "Kerenn kakanya ",
                "pesan": "Semangat terus kuliahnya ya!"
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
                "kesan": "Baik hati dan humble",
                "pesan": "Semoga dimudahkan dalam segala urusan nyaa"
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
                "kesan": "Asik deh orangnya",
                "pesan": "Tetap jadi Kakak yang asik"
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
                "kesan": "Seru dan asik kakanya",
                "pesan": "Sehat selalu ya kak"
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
                "kesan": "Sangat ramah dan baikk",
                "pesan": "Semoga apa pun yang lagi diperjuangin sekarang bisa berbuah manis"
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
                "kesan": "Cantik kakaknya",
                "pesan": "Semoga apa pun yang lagi diperjuangin sekarang bisa berbuah manis."
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
                "kesan": "Baik hati dan cantikk",
                "pesan": "Semangat dan sehat selalu kak"
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
                "kesan": "Cantik dan baikk deh kakanya ",
                "pesan": "Semoga sukses dan tercapai semua cita-citanya!"
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
                "kesan": "Cakep dan baik",
                "pesan": "Sehat selalu kak"
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
                "kesan": "Orangnya asik dan humble",
                "pesan": "Sehat selalu kak "
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
                "kesan": "Baik dan humblee",
                "pesan": "Sukses terus untuk kedepannya!"
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
                "kesan": "Abang ini baik dan humble",
                "pesan": "Sehat selalu abang"
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
                "kesan": "Keren abangnya",
                "pesan": "Lancar luncur kuliahnya bang"
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
                "kesan": "Cakep kakanya",
                "pesan": "Semangat terus perkuliahannya!"
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
                "kesan": "Kakak ini cantik dan baikk deh",
                "pesan": "Sehat selalu kakak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ceHs16eWvjMHNJTgrHDjg_5dKEQPT9jy",
            "https://drive.google.com/uc?export=view&id=1us5tAkj7r3U8XXtLnyXihPrtvC4DbSuO",
            "https://drive.google.com/uc?export=view&id=1RxxXk9oskRWZhdibjXUP515bllzAk-Hx",
            "https://drive.google.com/uc?export=view&id=1fxWGtgbLEZFaWzn8bf3z3GlqZaPp4Vmq",
            "https://drive.google.com/uc?export=view&id=1y81raxKQAhP7EsX4upC_FvUPISDtrtzk",
            "https://drive.google.com/uc?export=view&id=1YyOIwFvAxqmwXg82LYxYP5uqvRo4IIlv",
            "https://drive.google.com/uc?export=view&id=16jYoQNEdBItZFF8Ksk6n7SLgsSPFQwzR",
            "https://drive.google.com/uc?export=view&id=157WGyhvDPCmvlRCfsdap-sD4WuDP0QQX",
            "https://drive.google.com/uc?export=view&id=1neTqQF07iKn69S6PBbtMr2r-w6hmS02-",
            "https://drive.google.com/uc?export=view&id=1jLRhFIZAINuQjVU2VC18RYbZC5kyLOv0",
            "https://drive.google.com/uc?export=view&id=1WR_UarUkf3ByDbfTWE2-fCq7QURLtOl_",
            "https://drive.google.com/uc?export=view&id=15j0I0JyMB3qvedcmkFRG_ILkAcyC-M-u",
            "https://drive.google.com/uc?export=view&id=1yztElGldvgRcc092uPJZSMvLwoq0Vhju",
            "https://drive.google.com/uc?export=view&id=1ziqzJjqfhJRamkVqo_nfLQ2JFg8v3bEQ",
            "https://drive.google.com/uc?export=view&id=1Tq6i_q985yba2b-rp4d_nAf1-QUI4YJy",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Balap",
                "sosmed": "@kevinaj__",
                "kesan": "Abang ini asik dan keren ",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 tahun",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Baca",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini cantik dehh",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21 tahun",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak nya keren",
                "pesan": "semangat dan sehat selalu kak"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nganterin Datasena ke gedung F",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakak nya keren",
                "pesan": "semangat dan sehat selalu kak"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "sosmed": "@aayuandrianni_",
                "kesan": "Kakak nya asik",
                "pesan": "semangat dan sehat selalu kak!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Nemenin Bryan live TikTok",
                "sosmed": "@dafaelpriza_",
                "kesan": "Kakak nya asik dan humble",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 tahun",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lihat bulan",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak nya keren",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 tahun",
                "asal": "Lampung Tengah",
                "alamat": "JI Pulau Damar",
                "hobbi": "Taptap layar kalo Bryan live",
                "sosmed": "@afdall.03",
                "kesan": "Kakak nya keren",
                "pesan": "semangat dan sehat selalu kak"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak nya baik",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Ngitungin kelopak bunga di kebun",
                "sosmed": "@andra.lhm",
                "kesan": "Kakak nya humble deh",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "22 tahun",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Keren kakak nya ",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Ngegift live Bryan",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Asik kaka nya",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Keren deh kakak nya ",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18 tahun",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Asik kakaknya ",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 tahun",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Keren kakaknya ",
                "pesan": "Semangat terus ngejalanin hari-harinya, Kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ChEaHrGyDW2Di0_fPIBF32gXTIVYT7P3",
            "https://drive.google.com/uc?export=view&id=1byODnxtlL2bVYd6PMEbqG0t9IaOUz-Ek",
            "https://drive.google.com/uc?export=view&id=1tovlWNKtdDl_JaTjN4qBW0nC1DeiYvgJ",
            "https://drive.google.com/uc?export=view&id=1aTYBkPJcLvf_-YTzlgxtWVj_b-LOaglj",
            "https://drive.google.com/uc?export=view&id=179wKh8pTNrqo42L6l0E1Rq0ZyrmSJPq3",
            "https://drive.google.com/uc?export=view&id=1E1vym2RS-15S-rsv8uFieQZQ-e_4QKvZ",
            "https://drive.google.com/uc?export=view&id=11IWgmlz_z-jUSMYFC5O2rHy3ld0o5gId",
            "https://drive.google.com/uc?export=view&id=1eysofuXwgBgKSubVL5N53-UXcUXFwf7Q",
            "https://drive.google.com/uc?export=view&id=1K5LeCeVVifVvIcb6_E9PAXlD4IVEPiYi",
            "https://drive.google.com/uc?export=view&id=1480zdD0S55Sp8xx3JA-ebjGyq8UQJYgt",
            "https://drive.google.com/uc?export=view&id=1aOto9UpQj4Qcql_HFRd_1fcgG1NRfu9q",
            "https://drive.google.com/uc?export=view&id=1pJFG9n5YMQmNtuKByAi6GSFNcqQwjzxW",
            "https://drive.google.com/uc?export=view&id=1tgqqy9WHsuk0VB-9i1tfCuaKSwsCcWA3",
            "https://drive.google.com/uc?export=view&id=1q_63hFZdmLiOPTyEf8WYjpBAPMIRy0N6",
            "https://drive.google.com/uc?export=view&id=1K3YKUDQsxF8SDfPWsuYt4rqMjElTJE7U",
            "https://drive.google.com/uc?export=view&id=1H97bTZd4oDLf8OT6m_WnvSr8WbiUtHzx",
            "https://drive.google.com/uc?export=view&id=1lmzXMbEYwzP2MpiR3RVA6IHmdjXvKEIl",
            "https://drive.google.com/uc?export=view&id=1SoZJ2ZGiEROsIGnWmkTrIpBV_vm3uTxL",
            "https://drive.google.com/uc?export=view&id=1L35OKhyXl2jO_pzZdMPpfcFethtdqFkI",
            "https://drive.google.com/uc?export=view&id=1dFZqOA2RuYa9zss7diZHJPbLDZHuAygO",
            "https://drive.google.com/uc?export=view&id=12_we6Y3v2CuVn6meMifss2LDBVtlEYly",
            "https://drive.google.com/uc?export=view&id=1WW_GGHG3B_Gf3ByGRJCFAwC0Qvdxdsb6",
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
                "kesan": "Orangnya asik banget, seru diajak ngobrol",
                "pesan": "Semangat terus kuliahnya, jangan lupa istirahat juga."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21 tahun",
                "asal": "Lampung",
                "alamat": "Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Orangnya asik banget, seru diajak ngobrol",
                "pesan": "Semangat terus kuliahnya, jangan lupa istirahat juga"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini asik ",
                "pesan": "Doa terbaik buat kakak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@keyashafi_",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Semangat terus kuliahnya, jangan lupa istirahat juga"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Semangat terus kuliahnya, jangan lupa istirahat juga"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20 tahun",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Kakak ini asik dan humble",
                "pesan": "Semangat terus kuliahnya, jangan lupa istirahat juga"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12 tahun",
                "asal": "Bali",
                "alamat": "Nusa Penida",
                "hobbi": "Menghayal",
                "sosmed": "@Violaadrtr_",
                "kesan": "Kakak nya cakep",
                "pesan": "Sehat selalu orang baik"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20 tahun",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19 tahun",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20 tahun",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "@_els.a",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Kakaknya ramah, jadi nggak awkward pas ketemu",
                "pesan": "Sehat selalu kak!"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20 tahun",
                "asal": "Kalianda",
                "alamat": "Kota Baru",
                "hobbi": "Main game, tidur",
                "sosmed": "@aruccy_",
                "kesan": "Kakak ini asik",
                "pesan": "semangat kak!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19 tahun",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakak ini asik ",
                "pesan": "semangat ya kakak !!!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakak ini baik",
                "pesan": "semangat ya kak!"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Kakak ini asik ",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "sosmed": "@apiszzaja_",
                "kesan": "Kakak ini baik",
                "pesan": "semangat terus kak"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Kakak ini keren",
                "pesan": "semangat terus kak"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Scroll",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakak ini keren",
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20 tahun",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@Syaafiqui",
                "kesan": "Kakak ini keren",
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "28 tahun",
                "asal": "Kota bumi",
                "alamat": "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed": "@henryferdianto",
                "kesan": "Kakak ini asik",
                "pesan": "semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XZMkv6wOzBkweakEeIyxPL7_SscsEVv_",
            "https://drive.google.com/uc?export=view&id=1TeapKYypCO-xbNMSnpSiovp4G6hSX31O",
            "https://drive.google.com/uc?export=view&id=1OUgkoXVh0M237wqruqLO2e1vCwDJ9j1-",
            "https://drive.google.com/uc?export=view&id=1mcdSLBFb2xjdDcaium4Hof4jPObAEVnv",
            "https://drive.google.com/uc?export=view&id=1ggfLIkOQWWsEM8B0Y_Zi0sa4HyzszcS1",
            "https://drive.google.com/uc?export=view&id=1yqDyMIcVH53VQzpYoacDctX7iPNHUfPc",
            "https://drive.google.com/uc?export=view&id=18CeiNc9zh1Sa64rW09XzkweGmmUnO7MU",
            "https://drive.google.com/uc?export=view&id=1t44LQrAVqHO5PIwPg1UPYFTxs0TEWOxO",
            "https://drive.google.com/uc?export=view&id=18wQeuXvDKkysxKPcrgTms3S2-GK3OUXc",
            "https://drive.google.com/uc?export=view&id=12WDN0xH7jRBfSRAhVT69yhubz7BGrzED",
            "https://drive.google.com/uc?export=view&id=180f2OIdQJ4gLSdr--yqplx2ahed3FldW",
            "https://drive.google.com/uc?export=view&id=1ESidsS7GRJ6x91vWUDCI0Xti8JaJ6tvo",
            "https://drive.google.com/uc?export=view&id=1oShkT8U6tnJNsuzGYjF0DJC_iVL4TG1C",
            "https://drive.google.com/uc?export=view&id=1ymLEkrqz8RybDhZWVKFOCf9qHs_SZvbv",
            "https://drive.google.com/uc?export=view&id=1qo_3UH18o4lDRpLM2D27cdcZa1QyGmjx",
            "https://drive.google.com/uc?export=view&id=10BLsW-6KJn_MEZG8MdZWwIUVPwaBRC_Q",
            "https://drive.google.com/uc?export=view&id=1S7UDUx95RFmKhlj143a2Is_eQLF5v2-U",
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
                "kesan": "Kakak nya cakep dehh heheh",  
                "pesan":"Sehat selalu kakak , lancar luncur segalanya"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakanya baik dan humble juga",  
                "pesan":"Sehat selalu kak dan tetap semangat"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Abang nya baik , dan asik juga ",  
                "pesan":"Sehat selalu dan tetap semangat ya bang"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang nya asik dan welcome banget",  
                "pesan":"Jangan bosen-bosen buat jadi orang baik yaa, Bang"# 1
            },     
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi asik dan humble juga",  
                "pesan":"Sehat selalu dan tetap semangat ya bang!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Abang nya baik, humble bangettt jugaa",  
                "pesan":"Sehat selalu orang baik semoga lancar luncur kuliahnya ya abangg"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Abang nya baik , lucu juga heheh ",  
                "pesan":"Sehat selalu abang dan be happy!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakak ini baik dan asik jugaa",  
                "pesan":"Jangan bosen-bosen buat jadi orang baik yaa, Kak"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Abang nya baik , humble juga",  
                "pesan":"Sehat selalu bang dan always be happy "# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kaka nya cantik, baik , dan asik jugaa",  
                "pesan":"Sehat selalu kakak , semangat kuliahnya yaa!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kakak nya cantik dan baik bangetttt",  
                "pesan":"Jangan bosen-bosen buat jadi orang baik yaa, Kak"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kakaknya cakeppp",  
                "pesan":"Sehat selalu ya kak!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakak nya baik dan welcome juga",  
                "pesan":"Sehat selalu ya kak!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Abang nya baik dan keren juga",  
                "pesan":"Sehat selalu abang"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila cantik dan baik jugaa ",  
                "pesan":"Sehat selalu kak!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abangnya keren dan baik juga",  
                "pesan":"Tetap semangat dan sehat selalu bang!"# 1
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kakaknya keren deh",  
                "pesan":"Sehat selalu kakak!"# 1
            },                     
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
