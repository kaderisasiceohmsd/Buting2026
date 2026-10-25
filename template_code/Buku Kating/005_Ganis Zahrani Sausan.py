import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

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

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
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
            "https://drive.google.com/uc?export=view&id=1vdiW2JtgvsWZG3Eq3tJdRNY16Y4EdoWu",
            "https://drive.google.com/uc?export=view&id=1O0uovaBXrthijRnyizKNkZQZb7UTzPpw",
            "https://drive.google.com/uc?export=view&id=1SL9bF5m5wUa4G9ue4PrnmPrLMs3KkLvg", 
            "https://drive.google.com/uc?export=view&id=1oqjkdxMLUWQ02Rrmx1J0iM0eubeEk-Z3", 
            "https://drive.google.com/uc?export=view&id=1Scp2j_9RMq_lAlwfI8ejxLC5crBMefFM",
            "https://drive.google.com/uc?export=view&id=1JLOvxnjBALQImR0MqV3AqMj7iEO6EJWm",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung ",
                "nim": "123450103",
                "umur": "22 Tahun",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya keren dan terlihat berwibawa",  
                "pesan":"Semangat menjalani hari-harinya sebagai kahim bangg dan makin keren bangg!."
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22 Tahun",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya ramah dan baik karena sudah beli jajanan di sentra magangnya ssd",  
                "pesan":"Semangat terus bang kuliahnyaa, jangan lupa beli jajanan di sentra lagii"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21 Tahun",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Kak Efi kakak NIM kuu:D, kakak orangnya cantik dan kerenn.",  
                "pesan":"Sukses terus ya kakk kedepannya dan semoga urusannya di lancarinn:D"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22 Tahun",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Pembawaan abang pas wwc santai.",  
                "pesan":"Semangat ya bangg semoga plan abang kedepannya berjalan sesuai yang abang mau.."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21 Tahun",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa orangnya ramah senyum dan baik",  
                "pesan":"Semangat terus kakk menjalani hari-harinyaa dan makin cantik!"
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20 Tahun",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya lucuu, cantik, dan suka bercandaa",  
                "pesan":"Selalu jadi diri sendiri dan membawa energi positif buat orang-orang sekitar ya kakk:D"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# BADAN KESENATORAN
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jVKdjB9XYVGPQQ-VmTGXL8HFKPx5NXtt",
            "https://drive.google.com/uc?export=view&id=1nCOlmUqpHEXXB6NT_F3buQ2sw9pyWDDi",
            "https://drive.google.com/uc?export=view&id=1Y3iMYKhGpGV7hlGrTU8dJjQEEp4UrzdC",
            "https://drive.google.com/uc?export=view&id=1g0csxC2Ia5kgtKHCEXobKe8gEABAu5c_",
            "https://drive.google.com/uc?export=view&id=15LAbphkFHGoGUOiMP_rDZdTAYR6MRZYV",
            "https://drive.google.com/uc?export=view&id=1Gc0q-O5C096jEVAt-NOMnYDBJNqINJn4",
            "https://drive.google.com/uc?export=view&id=1nfq50IncDtis3Dqol0ruMybPMLKVkJ3E",
            "https://drive.google.com/uc?export=view&id=13HKYH4xUa_URb0Mhpnx3lhXbHd7KoX3L",
            "https://drive.google.com/uc?export=view&id=1Wjnx0nBtAGVLE5vwHpWY5od6SZZH8Pmi",
            "https://drive.google.com/uc?export=view&id=1_j1yR0Zvc8ZQIuXagbEmHRjSEZkNqpu2",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21 Tahun",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Public Speaking kakak keren dan bagus bangett, kakaknya juga cantik bangett",  
                "pesan":"Tutor jaga public speaking kaya kakakk:'"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal": "Jakarta ",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Abangnya asik pas fotbar wwc harus pose melet",  
                "pesan":"Sehat selalu ya bangg, semoga hal baik selalu dateng ke abang"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 Tahun",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak orangnya ramah dan baikk bangettt, ngomongnya juga lembutt",  
                "pesan":"Selalu jadi orang yang lemah lembut yaa kakk, semoga hal baik selalu mengelilingi kakakkk:D"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak cantik banget senyumnya manis jugaakk",  
                "pesan":"Sehat selalu ya kakk semoga segala urusan kuliah kakak dilancarkann"
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya seru, dan kaya ga asing mirip seleb tiktok tapi aku lupa siapa, tapi suka lewat fyp aku",  
                "pesan":"Semoga nanti TA nya di lancarin yaa banggg"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "KAK SUCII KAKAK MENTORKUU, kakak orangnya baik banget dan sabar bangettt",  
                "pesan":"Makasih ya kakk udah mentorin kamii, sukses terus kak kedepannya...."
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20 Tahun",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya baik dan gak sombong pas diajak foto",  
                "pesan":"Semoga abangnya ga pernah sombong kedepannya, keren banget bangg"
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19 Tahun",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya cantik banget dan suka pake bunga matahari",  
                "pesan":"Makasih kak udah udah jadi orang yang ramah, makin cantik ya kakkk"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20 Tahun",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya seruu tapi keliatan sedikit galak jugaa",  
                "pesan":"Semangat teruss ya bangg dan diberi kelancaran kuliah dan segala kegiatan organisasi yang abang jalaninn:D"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19 Tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya ramah cantik dan baikk bangett pas wwc",  
                "pesan":"Jangan bosen jadi orang yang ramah dan baik ya kakkk..."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b4ihvQVkilptoBYxJxn6cN87N22CxZGz",
            "https://drive.google.com/uc?export=view&id=1XLfqqySUI1GZwfvXdimy4xZuXsZ_NPGF",
            "https://drive.google.com/uc?export=view&id=13o553ifaxwZOT4Bl76ivvMw_VIyGeQr1",
            "https://drive.google.com/uc?export=view&id=1FBgogrZafPMTM_tQXKyCMyGCYFTVMYnX",
            "https://drive.google.com/uc?export=view&id=1cnqOzyCER-SLkBKjnJaHHWGqZWyL3Mc3",
            "https://drive.google.com/uc?export=view&id=1qxS9MFBV4or6cxUk2CRrFX3MZejXxjFc",
            "https://drive.google.com/uc?export=view&id=1NmLHZDrNs7zO8JZDW4O_y03ue64YnemN",
            "https://drive.google.com/uc?export=view&id=19dMf3o3wFpvtlhymYKRSMdH6xVJ9HJxF",
            "https://drive.google.com/uc?export=view&id=1NM6rxMGbsSgXQ0OYW7bt77PFWKsEIP3J",
            "https://drive.google.com/uc?export=view&id=1QKeSYxGrfddwvNEJAOx5BY8n2EDVjVn-", 
            "https://drive.google.com/uc?export=view&id=1Kx-bOjd57Sn06TDamVHjEOx6AznhRQPO",
            "https://drive.google.com/uc?export=view&id=1cZV39p1vwSZLVI4XMqZCy6YNG_PF8Pyl",
            "https://drive.google.com/uc?export=view&id=1kzqiJkJobraGw7xSQRl0RIzyb0OY6nwi",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450066",
                "umur": "20 Tahun",
                "asal": "Kuala Lumpur",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya ramah dan seru buat diajak ngobrol pas wwc baleg",
                "pesan": "Makin keren dan ramah selalu yaa banggg kedepannyaa. "
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19 Tahun",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya positive vibes bangett, aku suka pembawaan kakak.",
                "pesan": "Semoga nular positive vibesnya yaa kakk, sukses selalu jugaa disemua kegiatan yang kakak ikutinn"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19 Tahun",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "Bang Dharu orangnya keren abiezzz, pinter, public speakingnya jagoo.",
                "pesan": "Makasih udah ga pelit ilmu sama kami bangg, sukses selalu yaa banggg."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21 Tahun",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abangnya baik trus ramah juga pas wwc",
                "pesan": "Makasih bangg udah share ilmu ke kitaa"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21 Tahun",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya baikk cantikk dan ramahh:DD",
                "pesan": "Makasih buat ilmu yang udah kakak kasih saat wwc"
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20 Tahun",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Abangnya ramah dan baik pas wwc.",
                "pesan": "Semoga makin keren dan sehat selalu yaa banggg"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19 Tahun",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya cantik bangett trus baikk jugaa.",
                "pesan": "Semangattt kakakk semoga semakin banyak pengalaman baik kedepannyaa."
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20 Tahun",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya kerennn, cantikk, ramahh jugaa",
                "pesan": "Sehat selalu yaa kakakkk, semoga makin kerenn dann dilancarkan kuliahnyaa:D"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20 Tahun",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "Abannya kerenn dan suaranya bagus pas nyanyi, aku suka liat abang ngelike postingan kucing bontotss",
                "pesan": "Makin kerenn yaa bangg, sehatt selalu dan dimudahkan segala urusan abangg"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20 Tahun",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Kakaknyaa cantikk trus ramah senyumm",
                "pesan": "Semoga sehat selalu yaa kakk, semoga tercapai semua plan kakakk"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20 Tahun",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Abangnya seru dan suka bikin ekpresi speed",
                "pesan": "Semakin kerenn yaa bangg, kalau ikut lomba lagi semoga menang aamiin"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20 Tahun",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya baikk dan ramahh pas wwc",
                "pesan": "Semangatt teruss kakakk, semoga sehat selalu dan dikeliling orang baikk.."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20 Tahun",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknyaa cantikk, ramah senyum, baikk dan pembawaannya pas wwc juga enakk.",
                "pesan": "Sukses teruss yaa kakk, dilancarin semua urusannya dan semnagat TA nyaa."
            },
        ]
        display_images_with_data(gambar_urls, data_list) 
    Baleg()
        

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18b-muYp4OlHT8sbDEfhBibXUgUycIba0",
            "https://drive.google.com/uc?export=view&id=1cfhKFY_2iNC3m9JkGidFQbQBstKAdkgn",
            "https://drive.google.com/uc?export=view&id=1eZIN41PF0eUTtpWTzY758BT_bipJr21-",
            "https://drive.google.com/uc?export=view&id=12R4--GzbBine7Oe6M2du_B7UFw2wL4eo",
            "https://drive.google.com/uc?export=view&id=1Hm_gO7hb2H8FehL4JEPXt8AvkTG7Ehuo",
            "https://drive.google.com/uc?export=view&id=18_M0PJ9sAoken6d_3j4oyIKOBCMz-82Z",
            "https://drive.google.com/uc?export=view&id=1xOMYTRacsre2-yd2cJTYLh13n04-wZIc", 
            "https://drive.google.com/uc?export=view&id=1EEBVWFEREqvS3vWPSXlLQ83jn8Pv68q3", 
            "https://drive.google.com/uc?export=view&id=14sQ4EZ6w5omsjcfpLFMaA5DGPuG1cFl8",
            "https://drive.google.com/uc?export=view&id=1wD0q83wWe04SI-e064NYxWgdxRGPFs3a",
            "https://drive.google.com/uc?export=view&id=1McXnO2lNfPxdLWvBH4h4j1jKP0_PGzoy", 
            "https://drive.google.com/uc?export=view&id=1rNKLR5a-oNtYxq5lwfhZ4R5H2eE2Fdme",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf ",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "BANG IHSAN BAIK BANGETT, ORANGNYAA SERUUUU SUKA BERCANDAA, DAN SABAR BANGETTT.", 
                "pesan":"Makasiii yaaa bangg udah membimbing kamii selama magangg"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20 Tahun",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakk Nayaa cantikk, lucuuu, baikkk, ramah",  
                "pesan":"Makasih banyak yaa kakk sudah ngajarin kami gimana caranya jualan di sentraa:D"
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20 Tahun",
                "asal":"Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak orangnya cantik baikk dan ramah senyum pas first meet magang SSD",  
                "pesan":"Sukses dan lancar selalu yaa kakkk segala urusan kuliahnyaa"
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21 Tahun",
                "asal":"Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak orangnyaa cantikkk, baikk, dan ramah banget pokoknyaa",  
                "pesan":"Sehat selalu kakakk, dilancarkan TA nyaa, dilancarkan semua urusannya aamiin, makasii banyak kakak sudah ngasih kesempatan aku buat magang di divisi KWU:D"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25 Tahun",
                "asal":"Lampung Tengah ",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube ",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Abangnya seruu dan suka ngobrol sama jhonatan pas first meet",  
                "pesan":"Semogaa makin kerenn yaa bangg, sehat selaluu abangg!"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 Tahun",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Kakaknyaa cantikk, baik, dan ramah, imutt jugaakk:D",  
                "pesan":"Semoga kegiatan kakak dimudahkan yaa kakk, sehat selalu kakakkk.."
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20 Tahun",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Bang Iqbal orangnya seruuu, asprak kamii pas alproo",  
                "pesan":"Makasih udah sabar sama kamii dan makasii bang ilmunyaa"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19 Tahun",
                "asal":"Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak orangnyaa baikk, senyumnya maniss, ramah intinyaa",  
                "pesan":"Makasih udah berbagi ilmu, pengalaman, dan waktu ke kami yaa kakakk:DD"
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21 Tahun",
                "asal":"Baturaja Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Abangnya kocak, seruu, baikk, dan sabarrr terus juga suka cerita ceritaaa",  
                "pesan":"Makasii yaa bangg udah ngajarin kamii, makasii atas ilmunyaa banggg"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20 Tahun",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Bang Afdhal orangnyaa baikk, pembawaannyaa seruu pas gmeett, abangnya juga sabarr",  
                "pesan":"Makasii yaa bangg udah nemenin kami jualan di sentra pas pertama kalinyaa"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20 Tahun",
                "asal":"Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakaknyaa cantikk, lucuu, ramah dan baikk bangett",  
                "pesan":"Semoga kedepannya aku bisa ketemu kakak lagi di divisi inii:D"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18 Tahun",
                "asal":"Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknyaa baikk, ramahh, sabarr, cantikkk, dan suka ngasih makanan ke kamii",  
                "pesan":"Makasii banyakk kakakk udah ngajarin dan bimbing kami selama magangg, luvvv bangettt kakkk:D"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1amuVBrlaXlOicv7R8EGPn0JMHh_BFhuc",
            "https://drive.google.com/uc?export=view&id=124XbxFJHwuwP6tJSLrMbt0z_JKDdP8rI",
            "https://drive.google.com/uc?export=view&id=1PZZLODA3lAnKpMfEBHsNo40GfSEmUViO",
            "https://drive.google.com/uc?export=view&id=1WZQiWEMpBA-Q9tjZxgPJ6gYczEvc-o7k",
            "https://drive.google.com/uc?export=view&id=1a0JEn55FYd5U9gU8HDW0RW7BxdUcu7fm",
            "https://drive.google.com/uc?export=view&id=1zPq2dx6oh19OWMu4Ad2wTWIIzHnMOE9k",
            "https://drive.google.com/uc?export=view&id=1bUgil0sPgttJjSIWvI_9vXbKkp097h27",
            "https://drive.google.com/uc?export=view&id=1eFcNTK_j6KuX2wQ7t2ihPqxLHWEkavoi",
            "https://drive.google.com/uc?export=view&id=1ZUsV9ASavAUFLqsTS979DwTt69ZzyP3W",
            "https://drive.google.com/uc?export=view&id=1lFpDTd0PFq48jDpLw24cAFordAPtvXPV",
            "https://drive.google.com/uc?export=view&id=105r8hSCLAoAbLw7yN3FOQ4LtFTCMq1A7",
            "https://drive.google.com/uc?export=view&id=1nqCPQWKtWS-7brLdTeMRz79SbOkLOHSH",
            "https://drive.google.com/uc?export=view&id=1Hz0l8pxRBVFr0zVMG2UxMjNb4T1bxDRl",
            "https://drive.google.com/uc?export=view&id=1p8xvCONyTPvv-yvaRvXQ7Wbe_gEOl-yL",
            "https://drive.google.com/uc?export=view&id=1v5cxRTyDE2exWzy71nfBsfU_3_4FeDtC",
            "https://drive.google.com/uc?export=view&id=13zWUguzzpToq0JhJFbNj2AUWcmxmMftv",
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20 Tahun",
                "asal": "Jambi",
                "alamat": "Way Halim",
                "hobbi": "Ngeledek orang",
                "sosmed": "@haikalsbln",
                "kesan": "Bang Haikal dari looksnya keren dan sangar",  
                "pesan": "Sukses terus yaa bangg jadi kadep...."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21 Tahun",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma cantikk, imutt, lucuu, baik dan ramahhh",  
                "pesan": "Sehat selalu kakakk, semoga apa yang kakak impikan terkabul:D"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21 Tahun",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanaa pembawaannya seru, ceria dan ramah bangett pas wwc, kakaknya juga enak diajak ngobrol buat tanya jawab",  
                "pesan": "Semoga kakaknya selalu ceriaa ditengah kesibukan kuliahh iniii:D"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "124450064",
                "umur": "21 Tahun",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Hanif orangnya ramah, baikk, dan kalemm",
                "pesan": "Semoga lancar terus yaa bang jadi kadiv kerohaniann"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21 Tahun",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Abangnya kerenn kalo lagi supporteran main bass",  
                "pesan": "Semoga kuliahnya lancar terus yaa bangg, makin jago main alat alatnyaa..."
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18 Tahun",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakaknya cantik, senyumnya maniss, terus baikk bangett MasyaAllah:D",  
                "pesan": "Sehat selalu dan semangat terus ya kakak menjalani hari harinya ditengah kesibukan iniii:'"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19 Tahun",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Cerine sangat ramah senyumm, senyum manis, baikk, cantik, pembawaannya pas wwc juga enak banget untuk diajak diskusi dan tanya jawab",  
                "pesan": "Semoga kakaknya semakinn kerennn dan sukses terus di divisi inii...."
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19 Tahun",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Bang Jaya orangnya asikk dan seruu pas wwc daftar magang ituu",  
                "pesan": "Semoga abang main basketnya makin jago dan menang terus aamiin..."
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20 Tahun",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla orangnya ceriaa, baik dan ramah bangettt",  
                "pesan": "Semoga kakak sehat selalu, semangat kuliahnyaa kakakk..."
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18 Tahun",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Abangnya ramah senyumm pas fotooo",
                "pesan": "Semangat yaa abangg kuliahnyaa dan sehat selaluu aamiin!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19 Tahun",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresaa kakak tutor kamii, kakak orangnya sabar banget pas ngajarin kamii",
                "pesan": "Makasii banyakk kakak sudah mau berbagi ilmu ke kamii, semoga kakaknya semkain pinter dan sukses terus aamiin..."
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak Audinaa cantikk bangett, terus keliatan kalem jugaa",
                "pesan": "Sehat selalu dan semangat teruss kakak kuliahhnyaaa..."
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20 Tahun",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Kak Cikaa orangnya ramahh dan baik bangett pas wwc waktuu ituu, kakaknya juga cantikk",
                "pesan": "Semoga semua tugas dan tanggung jawab kakak di divisi ini berjalan dengan baik aamiinn"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21 Tahun",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin cantikk bangett, ramahh, baikk, dan enak diajak ngobrol",
                "pesan": "Semoga yang kakak impikan selama kuliah tercapai semua yaa kakkk:D"
            },
            {
                "nama": "Muhammad Arvinsyah",
                "nim": "124450128",
                "umur": "20 Tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Bang Arvin kalemm, baikk, ramah dan pembawaannya tenang pas wwc",
                "pesan": "Semangat terus abangg menghadapi kesibukan di masa masa kuliah inii..."
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20 Tahun",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakaknya baik, ramah, trus keliatan positive vibes jugaaa, cantikk",
                "pesan": "Semangatt kakakk nyari duitnyaa:D"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1G99w-W2tKEk2ed6DMsEernEkp3CEGHxo",
            "https://drive.google.com/uc?export=view&id=1eWbKjDk89GgO-SCEJnLPR5iVrbWCJ5NZ",
            "https://drive.google.com/uc?export=view&id=1HnYnkH17-iU48BlayTDAb0_fw_8pp9dq",
            "https://drive.google.com/uc?export=view&id=1CS6P4_nHPyGQxl5wU1ymmWi9Qa9tgZGG",
            "https://drive.google.com/uc?export=view&id=1lOtDm_shKMuQLb6ChcKf8h_wJUq_UPGL",
            "https://drive.google.com/uc?export=view&id=1fThluGqDE2eYDK7dsk-QcA2OVejcaM14",
            "https://drive.google.com/uc?export=view&id=1Gd4WYhaAMVIvzLU8PUnQEHEU-s3VZmE7",
            "https://drive.google.com/uc?export=view&id=1-_rpcqurir34PnRV9v_In2KNelcRa6CB",
            "https://drive.google.com/uc?export=view&id=13jIZvLEtR3vDN0WQMCFtC9XQ33VgnRS3",
            "https://drive.google.com/uc?export=view&id=1iFZoNQPBv_4QrEhxBifngvKBE3MowZMV",
            "https://drive.google.com/uc?export=view&id=1YcJ4TcCADkaEPj67TBSUNJuKCrpyi-v5",
            "https://drive.google.com/uc?export=view&id=1LwkT99n--rIWPPL98USWo9LIdY3yLtSS",
            "https://drive.google.com/uc?export=view&id=1RYO4JdK3R4mLIqcxVzYUmBgHTAqQQB15",
            "https://drive.google.com/uc?export=view&id=1E6D5lPYOSBD0jSdX-OaQ-X3tjtGF-VlL",
            "https://drive.google.com/uc?export=view&id=1G3k7TZPm9fS29BrIMvgEty38LtgHrFg-",
            "https://drive.google.com/uc?export=view&id=1Yd7iMoKHcLJ-fBH7P5hEHn3zodeR5YGt",
            "https://drive.google.com/uc?export=view&id=1yCaDTlqiFpJOYj9vDLGqI6oF14f9C8B4",
            "https://drive.google.com/uc?export=view&id=1CeVKu0U4IiPfadGvm-rQq34emX0eNwT8",
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
                "kesan": "Kak Nayla orangnya ramah bangett pas aku mau minta fotoo, cantikk jugaaa",  
                "pesan":"Semangatt kakakk semoga semakin kerenn, makin jagoo ngeditt"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna baik bangett, cantik dan ga pelit ilmuu",  
                "pesan":"Makasii yaa kakkk sudah ngasih tau kamii tentang departemen inii"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Bang Labo dari looksnya kerenn, trus ramah jugaa",  
                "pesan":"Semangatt yoo bangg, sukses selaluu abangg..."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kak Sania cantikk bangettt, ramahh, baikk",  
                "pesan":"Semoga makin jagoo ngeditnyaa dan banyak ide ide yg terlintass"# 1
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak cantikk bangett, ramahh, kerennn",  
                "pesan":"Semoga makin jago ngedesignnyaa kakakkk:D"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak orangnya sangat positive vibess",  
                "pesan":"Semangat teruss kakkk, istirahat yang cukup!"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kak Felisya cantikk, senyumnya imutt, lucuu, ramah..",  
                "pesan":"Semoga kuliahnya lancar teruss dan makin imut yaa kakakk"# 1
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Bang Razan orangnya baikk, ramahh, dan keliatan kerenn jugaa",  
                "pesan":"Sehat selalu yaa banggg, semangat teruss jalanin tugas tugas kuliahnyaa"# 1
            },
            {   
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakak jagoo bangett main alat musiknya pas supporterann",  
                "pesan":"Tutor main bolaa kakk, semangat belajarnya kakakk:D"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kak Alyaa baikk, cantik, ramahh trus positive vibes jugaa",  
                "pesan":"Semangattt kakakkk janlup istirahatt yang cukupp"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya cantik bangettt, imutt, baikk",  
                "pesan":"Semoga semua urusannya dilancarin yaa kakk, sehat selalu kakk"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Senyum kakaknya maniss terus pembawaan kakak saat wwc juga enak mudah dipahami",  
                "pesan":"Makasii banyakk kakakk ilmunyaa pada saat wwc"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakaknya cantik bangettt, senyumnya maniss, ramah trus baikk.",  
                "pesan":"Semoga dilancarin teruss yaa kakk bikin kontennyaa"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Bang Daffa orangnya baik bangett trus satu kost sama bang Andra",  
                "pesan":"Semoga yang lagi abang jalanin berjalan dengan lancar semuaa yaa banggg"# 1
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya baikk, kalem, pembawaannya juga santai dan tenang ",  
                "pesan":"Makasii bang sudah berbagi ilmu ke kami pas wwc..."# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kakaknya cantikk bangett trus ramahh pas wwc",  
                "pesan":"Semoga semakin banyak ide idenya kakkk"# 1
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya cantik bangett, ramah senyum jugaa",  
                "pesan":"Semoga whislist kakak saat sekarang bisa tercapai yaa kaa aamiinn.."# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kakaknya ramah banget pas diajak foto",  
                "pesan":"Semoga segala sesuatu yang kakak pengen terkabul semua yaa kakk..."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13dirBghzqbk7NDBjvMp6vJKEK5GCE1_Q",
            "https://drive.google.com/uc?export=view&id=1HUu1dmjgW_ILFgZdwpB3aZb20PIpNiYR",
            "https://drive.google.com/uc?export=view&id=14EqKaU2izw79ugRuQ3w8NOTFCHLQOdDY",
            "https://drive.google.com/uc?export=view&id=113KHZJYNMP9rdeJcpc3vLJDS5ZhS57SU",
            "https://drive.google.com/uc?export=view&id=1YMZsNwmknwQ2IpNQ1fwA9dqKVmcLNsfa",
            "https://drive.google.com/uc?export=view&id=1w4ehgJmvbfscAvEHUX0aiHHluKlP59oa",
            "https://drive.google.com/uc?export=view&id=1LeXMLCpwFUpwWRoB9RWTaJeXdCmWyM0b",
            "https://drive.google.com/uc?export=view&id=1BhUlwiC6fW3WNZMI93kBBxObw7Y9D8WA", 
            "https://drive.google.com/uc?export=view&id=19fSeVhh1dXQOOhFkseI2WRUONe4TwMNq",
            "https://drive.google.com/uc?export=view&id=1Swy3Ma1SadyxDkeAXKO4fNrbuvg1gxt1", 
            "https://drive.google.com/uc?export=view&id=1cTTWambWr_bvtLTcxMArR0pvUBbXd7Iv", 
            "https://drive.google.com/uc?export=view&id=1TflM2Vou7U6TvKzEP9Phm14c-SmzQ2Mz", 
            "https://drive.google.com/uc?export=view&id=1_i0dEQbrEg4MMeZdIZIgWZlHvHA8imWF", 
            "https://drive.google.com/uc?export=view&id=1VSef542Y7lhFF0gxRQFXq6zCofksmdHX", 
            "https://drive.google.com/uc?export=view&id=1kCluookbdzlXN1iley66G3pSUMe9_ATc", 
            "https://drive.google.com/uc?export=view&id=1EjL78aeVXJdRf1pkR-lDd9zrfRmp8SMJ",
            "https://drive.google.com/uc?export=view&id=152QhgPwfUVrKOA0d9AgLerpDdR1Fsjvm", 
            "https://drive.google.com/uc?export=view&id=1AHEn6Gr2pL6RqK61f3KKkZGNQ81Wq-Xt",
            "https://drive.google.com/uc?export=view&id=14pDqorBbk-45wwUthwJRpQwDSgBwYovJ",
            "https://drive.google.com/uc?export=view&id=14sb8uHrqkriNrvTM8V76c1YV7ybor_VF",
            "https://drive.google.com/uc?export=view&id=1ywOqnhDwYxMa2nk_nrZqf0lSiMGI8UZj",
            "https://drive.google.com/uc?export=view&id=16nTNYj17-d2t4gkG5Uj_voXXB7t9vsFt",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "-",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kakaknya kerenn bangett dan terlihat seperti independent womenn",
                "pesan": "Semangat yaa kakakk, sukses teruss kakkk"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20 Tahun",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya imutt, baikk, dan ramahh",
                "pesan": "Semangatt yaa kakakk kuliahhnyaa"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "-",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya cantikk trus senyumnya maniss:>",
                "pesan": "Sehat selaluuu kakk dan semua yang diinginkan terkabul aamiin"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15 Tahun",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Abangnya asikk seruu ramahh",
                "pesan": "Semoga abang dikelilingi orang orang baik yaa bang aamiin"
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20 tahun",
                "asal": "lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya cantikk trus ramah dan baikk",
                "pesan": "Semangatt yaa kakakk menjalani harii harinyaa"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20 tahun",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya positive vibes",
                "pesan": "Sehatt selalu kakkk"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20 Tahun",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya ceriaa teruss dan asikk",
                "pesan": "Semangatt kakakk kuliahnyaa dan sehat terusss"
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "-",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya ramah dan baikk",
                "pesan": "Semoga bang bima dilindungi dimanapun berada!"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "-",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abangnya kerenn",
                "pesan": "Semangatt teruss abanggg"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya lucuu dan imutt",
                "pesan": "Sehat selalu kakkk"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya seru mentor jordann, ramah, baikk",
                "pesan": "Semangat yaa kakk, tidur yang cukupp..."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20 tahun",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya baikk dan seruu",
                "pesan": "Sehatt selaluu kakkk semoga dilancarkan urusannya"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25 tahun",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknyaa lucuuu",
                "pesan": "Semoga yang kakak impikan tercapaii yaa kakk"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya cantikk bangett",
                "pesan": "Sehat selalu yaa kakk dan semangattt"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "-",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abangnyaa kerenn dan seruu asikk",
                "pesan": "Semangat bangg jalanin kuliahnyaaa"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "-",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Abangnya seruu diajak ngobrol pas wwc",
                "pesan": "Sukses terus bangg"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15<<1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd_",
                "kesan": "Abangnya baikk, dan ramah jugaa",
                "pesan": "Semangat teruss bangg, sehat teruss"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya seruu dan pembawaannya tenangg",
                "pesan": "Sehatt teruss abangg"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "sosmed": "@jaldii._",
                "kesan": "Abangnya keliatan seru dan asik bangett",
                "pesan": "Ceria dan semangat terus bangg"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20 tahun",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya cantik bangett",
                "pesan": "Semangatt kuliahnyaa kakakkk"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya baikk dan lucuu",
                "pesan": "Sehat selalu kakk jangan lupa istirahatt kakk"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad orangnya keren dan seruu",
                "pesan": "Sukses teruss bang kuliahnyaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1b5bCGDAwJlJVmnFE9jKApIGEvKKOwMMR",
            "https://drive.google.com/uc?export=view&id=1brmJfQ2pfRPq13vX-NC-VD8CsWAyCVAK",
            "https://drive.google.com/uc?export=view&id=1hlVUs_BQ6R4E2QAa4eJUNfBOp75Bi2Mk",
            "https://drive.google.com/uc?export=view&id=11UE2jH3xuhCoVdkIfDXhQQWNwyNg_6ev",
            "https://drive.google.com/uc?export=view&id=1DR4AdO6pjxTQYjUeHzgJEJKSxVrzuxpz",
            "https://drive.google.com/uc?export=view&id=1D4K_VkB4sdK2Xml_qbMekP2LIr-Y1MQG",
            "https://drive.google.com/uc?export=view&id=1ywOCHp8nL-iv__w6PbHVQXlNJYSUvu_k",
            "https://drive.google.com/uc?export=view&id=1KJhKh8sH7P0lJvcjUz9j7_gnTDmvK1g_",
            "https://drive.google.com/uc?export=view&id=1XVJ9dbuhYkqkj6YoQDRipbRJXooehwow",
            "https://drive.google.com/uc?export=view&id=1jE3NdHPgDgsfdOmgncYdnvXfn2mojlHH",
            "https://drive.google.com/uc?export=view&id=11gy_S8RNQdURkiArDLo89QVdcsi7qJdL",
            "https://drive.google.com/uc?export=view&id=1N5_4luyT-NiCtTxCLP7GFY-anIDjuc8k",
            "https://drive.google.com/uc?export=view&id=1pWy6Uuj7ZQFCOdXWzZsXrryPs4IUiOBG",
            "https://drive.google.com/uc?export=view&id=16n0y-anb3RfiGO3pmuUCkYyru3TVi9bx",
            "https://drive.google.com/uc?export=view&id=12lQ7DthAh0Jl8Da33YPiRuvEVXiibDWA",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "21 tahun",
                "asal": "Sulawesi Tengah",
                "alamat": "Panjang",
                "hobbi": "Mancing",
                "sosmed": "@kevinaj__",
                "kesan": "Bang Kevin sepertinya orangnya dinginn tapi enak buat diajak diskusi saat wwc",
                "pesan": "Suksess teruss yaa bangg, semoga pas mancing dapet ikannya yang gede gede."
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknyaa cantikk bangettt, lucuu, dan positive vibes",
                "pesan": "Semoga semakin hari kakaknya makin cantikk"
            },
            {
                "nama": "Ari Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "21 tahun",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya kalem dan baikk",
                "pesan": "Suksess selalu abangg"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Abangnyaa kerenn, ramah, baikk",
                "pesan": "Semangat abang kuliahnyaa semoga semua matkulnya A semua ya bangg:D..."
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar + menghitung uang",
                "sosmed": "@aayuandrianni_",
                "kesan": "Kakaknyaa cantikkk, ramah, dan lucu",
                "pesan": "Semangatt belajarnyaa kakk"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Jogging",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya seruu trus baikk pluss ramahhh",
                "pesan": "Semangatt bangg joggingnyaaa biar sehatt"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 tahun",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Mancing",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknyaa baikk, ramahh jugaa pas wwc digacoan",
                "pesan": "Semoga pas mancing dapet ikannya gacor yaa kakk"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 tahun",
                "asal": "Lampung Tengah",
                "alamat": "JI Pulau Damar",
                "hobbi": "Memantau dl tugas",
                "sosmed": "@afdall.03",
                "kesan": "Abangnya baikk ramahh trus pembawaannya pas wwc enakk",
                "pesan": "Semoga tugasnya ga kelewat dl ya banggg:>"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya maniss, cantik, baikk",
                "pesan": "Sehat selalu kakakk, janlup istirahat yang cukup walau sibukk"
            },
            {      
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "Abangnya seruu, ramah, asikk pokoknyaa, trus baik bangettt, ga espek sama sama suka nonton film horror trus film film yang ditonton 80% samaa uhuyyy",
                "pesan": "Semangat terus bang, dilancarin segala urusannya, semoga kebeli iphone 18 burgundy"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "22 tahun",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya seruu, pembawaannya pas wwc juga enakk",
                "pesan": "Semoga abang dilancarkan kuliahnyaa dan views livenya ribuann ya bangg"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnyaa baikk ramahhh trus seruu pulaa",
                "pesan": "Semangatt jalanin kuliahnya banggg semoga sehat terussss"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakaknya cantikk trus ramah:)",
                "pesan": "Suksess teruss kakk kedepannyaa dan diajuhin dari hal yang ga baik ya kakkk..."
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18 tahun",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya cantik bangettt",
                "pesan": "Sehatt selalu kakkkk dan jangan kecapean..:D"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 tahun",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang Rafka orangnyaa baikk, ramah ke kami pas wwc",
                "pesan": "Semangatt yaa abangg kuliahnyaa semoga selalu bangun pagi dan ga pernah kesiangan buat kuliah..."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cuekKLBzQZofnmnD3U3wdsBj-oOpruoC",
            "https://drive.google.com/uc?export=view&id=1i5WA6gorMgbnfo4ViJrW0mQtZpnntxM-",
            "https://drive.google.com/uc?export=view&id=1JoxM2yNs21tdiwBDe7Q9MRw-_fjCC5Ze",
            "https://drive.google.com/uc?export=view&id=1iqF-M_1sS0KMcmKDGvSQGVQPRpSGZ4qI",
            "https://drive.google.com/uc?export=view&id=1QMpka3kzM1s4yF13vLNzibLmBFnjZWfN",
            "https://drive.google.com/uc?export=view&id=1RFWfadDXFXFFAgrpY-LdYEELcf9ZazDR",
            "https://drive.google.com/uc?export=view&id=1NQWFl5AyNxykqBLSDyPVp_O16qlyJgnb",
            "https://drive.google.com/uc?export=view&id=13IhKzsCG_TsUWpw9opxo1BQcjVFl4LOM",
            "https://drive.google.com/uc?export=view&id=15JGfWfV-M9y2AXD3BiXvs8UKWFfK9odB",
            "https://drive.google.com/uc?export=view&id=1DKni3PqWAO4xbmsTYCvocy35aShjhFad",
            "https://drive.google.com/uc?export=view&id=18j2oF99RpRK_5EJZLJJNuZX30p0Rhy3j",
            "https://drive.google.com/uc?export=view&id=13L3fYpb5ngBGpwkRz7zfSmshvNg7V6FY",
            "https://drive.google.com/uc?export=view&id=1dsJvNP0i68j36F7jDNCw7Lz2BUe5yALg",
            "https://drive.google.com/uc?export=view&id=1QIzFegpBl347GDKvzf36Ke9kxgWoQVE3",
            "https://drive.google.com/uc?export=view&id=10sphsO4VhOMH2biOOV4jdEhzEv9wl8x7",
            "https://drive.google.com/uc?export=view&id=1B58dSAYfKnVpasj12P3pIomi_qPa-mSZ",
            "https://drive.google.com/uc?export=view&id=1P7GubT9Ggm0LQyRl8Z--Umj5hIHYf_KU",
            "https://drive.google.com/uc?export=view&id=1fvWBnBJUauJ0MjbHw80EkoTgzNX6ymeO",
            "https://drive.google.com/uc?export=view&id=1-F3G0R2N2Av0nVTRi_mAI3krcFPIOoYA",
            "https://drive.google.com/uc?export=view&id=15xa7ahBfI7j-33eWPMltjCcb3V43Fn7G",
            "https://drive.google.com/uc?export=view&id=1TqtskbXSjZiSzsIhhw0KT1xQostTHwq6",
            "https://drive.google.com/uc?export=view&id=1ZJ_JUZeqewiv96e6ZHOSOMXU4SrC6bfU",
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton Bandar Lampung",
                "hobbi": "Gangguin bang keya",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio orangnya seruu asikk juga pas wwc",
                "pesan": "Semangatt abang kuliahnyaa, dilancarin teruss:>"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty orangnya kerenn terus pinterr jugaa",
                "pesan": "Semoga kakak dijauhin dari hal burukk yaa kakk soalnya kakak terlihat positive vibes sekaliii:>"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnyaa baikk bangettt terus ramahh poll:)",
                "pesan": "Semoga kebaikan abang jadi ladang pahalaa.."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya soft spoken, baikkk, lucuuu",
                "pesan": "Semoga abangnya makin kerenn dan semakin soft spokenn"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21 tahun",
                "asal": "Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang razin orangnya seruu trus kerenn",
                "pesan": "Abang semangat teruss yaa kuliahnya semoga utsnya 100"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20 tahun",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Abangnya kerenn, baikk, ramah",
                "pesan": "Tutor main gitarr bangg:>"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12 tahun",
                "asal": "Bali",
                "alamat": "Nusa Penida",
                "hobbi": "Menghayal",
                "sosmed": "@Violaadrtr_",
                "kesan": "Kakak NIM akuuu cantikk bangettt, ramahhh puolll",
                "pesan": "SEHAT SELALU KAKAK BAHAGIAA TERUSS YAWWW:>"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20 tahun",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak Rsa orangnya baik, ramahh, lucuu",
                "pesan": "Kakk semangatt teruss yaaa, sehat selaluu okeee"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19 tahun",
                "asal": "Kepulauan Riau",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kak Vannisa baikk, ramah, cantik, lucuuuw",
                "pesan": "Semoga kakak selalu dikelilingi orang baikk selama kuliahh:D"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20 tahun",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakaknya cantik bangettt, baikk, humble",
                "pesan": "Semangatt kakakk kuliahnya semoga uts uas nya A"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "@_els.a",
                "kesan": "Kak Elsa cantikkk dan positive vibes:>",
                "pesan": "Jaga kesehatan kakk, semoga semua matkulnya A di siakad"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main game",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknyaa baikk, cantikk, kerennn",
                "pesan": "Semoga Nilai kakak di uas nanti 100 semuaa ya kakkkk;>"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@_loviaa",
                "kesan": "Kak Loviaa orangnya pinterrr, cantikk, baikkk:>",
                "pesan": "Semangat kakk semoga semakin hari kakaknya semakin pinter yeyy:>"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "18 tahun",
                "asal": "Kalianda",
                "alamat": "Kota Baru",
                "hobbi": "Main game",
                "sosmed": "@aruccy_",
                "kesan": "Abangnya baikk, kerenn, humble pokoknyaa",
                "pesan": "Sehat selalu yaa banggg, jaga kesehatan okeeee"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19 tahun",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknyaa cantikkk, baikk, ramahhh, positive vibes bngt kakk:>",
                "pesan": "Tutor make up kakkk:>"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakk Faizaaa pinterr bangettt, tutor RA, ngajarnya enakk, gampang kami pahamii",
                "pesan": "Sukses teruss kakk semoga semua matkulnya A aamiin"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnyaa seruuu, baikk, kerennn",
                "pesan": "Semangattt terus kuliahnya yaa banggg, semoga sehat terus ga bolong absennya"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnyaa kerenn eyyy",
                "pesan": "Semoga semakin hari semakin jago ngoding bangg"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Bang Kaleb orangnya pinterrr, kerenn bangetttt",
                "pesan": "Tutor jadi pinter kaya abanggg"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknyaa lucuu, cantikkk, baikk yeyy",
                "pesan": "Semangattt kakakkk menjalani hari harinyaa, ceria terus ya kakkk"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20 tahun",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@Syaafiqui",
                "kesan": "Abangnya baikk dan kalau ngajarin kami tutor mudah dipahamii",
                "pesan": "Makasiii yaa bangg udah mau ngajarin kami dan makasii ilmunyaa"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "28 tahun",
                "asal": "Kota bumi",
                "alamat": "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed": "@henryferdianto",
                "kesan": "Bang Henry kerennn, baikk, ramahhh",
                "pesan": "Semoga makin gacor kedepannya yaa bangggg"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RJDxllgydOrKyJXsUgyANFnfQdfqmbGZ",
            "https://drive.google.com/uc?export=view&id=14pWtT5969IBA2yIugZqLxTb6iuCRZvLh",
            "https://drive.google.com/uc?export=view&id=1zdBjDmJBcbiiLlxxOqtFIx6JzDy4y_HW",
            "https://drive.google.com/uc?export=view&id=1C3kvWNBElbDVQr6ptANch3xrg8qefIZn",
            "https://drive.google.com/uc?export=view&id=1sc0XMKyLxC8cmBYiNn8oju_VKrVEikKb",
            "https://drive.google.com/uc?export=view&id=1f7c1hKS08x4il6X6Z505SYKeqycHb05C",
            "https://drive.google.com/uc?export=view&id=19UZmCN9aI2TWsYoJHZeN6oWurso6kKvv",
            "https://drive.google.com/uc?export=view&id=1JxBLa2hp7z6XEriTPudMTZxHaduhpYYy",
            "https://drive.google.com/uc?export=view&id=1vpyLueXS9FzrZOKrIoUc67pq1pLllZG3",
            "https://drive.google.com/uc?export=view&id=1Qx1zub2UW2Z3f20VfjGh3ViOGZkUDTzj",
            "https://drive.google.com/uc?export=view&id=1nidqHfr1c0PSoEP7CSSmfZY5V2JHcEzH",
            "https://drive.google.com/uc?export=view&id=1RdaSY11ma3CUqwNnRQja5HmPuKaGA-U6",
            "https://drive.google.com/uc?export=view&id=1CvDFyKBBL09LQohDX2gj9csD7o8d6-X5",
            "https://drive.google.com/uc?export=view&id=1S0r7To-MIh90-IEnJZtFSEyYl-NNBS4H",
            "https://drive.google.com/uc?export=view&id=1CaitvvLtygPYooSBQDtUTXfILHZsitSL",
            "https://drive.google.com/uc?export=view&id=15ZEZpLVgZA0v_MNe4xLEC0gmcpOpDKQr",
            "https://drive.google.com/uc?export=view&id=1QG8hBup9aopNXEsQoO23s8Hs96YWgq4a",
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
                "kesan": "Kak Arienta orangnya kerenn terus baikk, cantikk",  
                "pesan":"Semangatt selalu kakk semoga urusannya selalu dimudahkann:>"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany cantikk, baikk, terus kerenn jugaa",  
                "pesan":"Sehat selalu kakk, semoga dijauhkan dari orang jahat aamiin"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orangnya kerenn, jago ngoding, berwibawa, dan baik",  
                "pesan":"Semoga selalu dilancarkan kuliahnya ya bangg aamiin, sehat selalu bangg"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman orangnya baikk trus ramah ke kamii",  
                "pesan":"Semoga TA nya lancar bangg..."# 1
            },            
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, kalau supporteran terlihat sangat semangatt",  
                "pesan":"Semoga yang abang inginkan sekarang tercapai ya bangg aamiinn..."# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake orangnya baikkkk bangettt",  
                "pesan":"Semangatt teruss bang kuliahnyaa"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar orangnya baikk, ramah dan keren pokoknyaa",  
                "pesan":"Makasii bangg sudah membimbing kamii..."# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia orangnya ramah, baikk bangettt",  
                "pesan":"Makasii yaa kakk sudah ngajarinn kamii, sehat selalu kakkk"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal orangnyaa kerennn, baikk jugaa intinyaa",  
                "pesan":"Semangatt, jayaa selalu bangg, sehat teruss yaaa"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri cantik banget, baik juga, lucuu",  
                "pesan":"Semoga kuliah kakak lancar teruss ya kakkk:>"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baikk bangett, ramahh trus kaya independent women",  
                "pesan":"Semangatt kakk semoga semua nilainya A"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya ramah pokoknyaa, cantik jugaa",  
                "pesan":"Semangat kakk pilatesnyaa hehee"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakaknya cantikk, baikk trus humble jugaakk",  
                "pesan":"Semoga dijauhi dari orang jahat yaa kakkk:>"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jeremi orangnyaa kerenn, trus ramahhh",  
                "pesan":"Semangatt bangg kuliahnya semoga ga ada tugas yang lewat dl:>"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnyaa baikk, ramahh, cakeppp",  
                "pesan":"Semoga kebeli banyak robux yaa kakkk"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli orangnya kecee, kerenn, baikkk",  
                "pesan":"Sehat selalu yaa banggg, jaga kesehatann"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi cantikk, baikk, lucuu huhuu ",  
                "pesan":"Semoga kakaknyaa sehatt selalu dan sering sering minum air putihh"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
