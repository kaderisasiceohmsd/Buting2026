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
            "https://drive.google.com/uc?export=view&id=1bYf3RVtoPfLwbR0tWmNtLi9q3V7YKAjo",
            "https://drive.google.com/uc?export=view&id=15XbVhzxSkkKl0VkckNkB7zbHzqxBDrap",
            "https://drive.google.com/uc?export=view&id=1RFxZSl06PXALtnH_UvdHZ7910bCN0zXr", 
            "https://drive.google.com/uc?export=view&id=1Xs6KhJdLtZ7LmaQwaXYTFhSbHmyHDric", 
            "https://drive.google.com/uc?export=view&id=1gFgazYBsl7ixEUruZETfpPAdc_hM3-Nk",
            "https://drive.google.com/uc?export=view&id=1ZK21DrH7f_7eqWtiAmgI63YFRSKdflul",
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
                "kesan": "Keren banget abang kahim ini",  
                "pesan":"Semangat terus bang kuliahnya!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kagum banget hobinya sering zikir",  
                "pesan":"Semoga zikirnya ga pernah terputus ya bang"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Looks like kakak-kakak yang baik dan kalem banget ",  
                "pesan": "Semangat dan lancar terus ya kak kuliahnya  "
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang Qois baik mantap",  
                "pesan":"Semangat kuliahnya ya bang Qois, semoga suratnya gampang terselesaikan !"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Ka hafsa cantik banget, terkagum",  
                "pesan":"Kapan-kapan mau liat hasil lukisan Ka Hafsa deh"
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Lancar-lancar ya kak kuliahnya, semoga episode nyari motor Pak Tirta segera berakhir"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# BADAN KESENATORAN
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TV8nSg1CaL_9puPEsG2QMmMLQmGCXH4i",
            "https://drive.google.com/uc?export=view&id=1VieHmzzRMwN-5s7Rbvwc0tmYROaJl5cb",
            "https://drive.google.com/uc?export=view&id=1DrxlmL6O_v_H-Du8ime3SFd17h-twBGe",
            "https://drive.google.com/uc?export=view&id=13Awz43JMNI6BcKHoff2GGTakX-qIqAji",
            "https://drive.google.com/uc?export=view&id=1MO0Mk2WFJPqsMArrw7W-dLlCKHueGbug",
            "https://drive.google.com/uc?export=view&id=1zKTEAIGN4zPdeqvWyDo8iYTCpD-yvEyS",
            "https://drive.google.com/uc?export=view&id=1w0MN9tAjOC40FaDVwRHSIKPz3zwNtv34",
            "https://drive.google.com/uc?export=view&id=1DqFsPOJ2XoBud057TJkb3F557By9zKLa",
            "https://drive.google.com/uc?export=view&id=1Km7NdwxkwPtoNUgoiL4tLYdGTZD3NnWh",
            "https://drive.google.com/uc?export=view&id=1xYJAnC5Ygbh0XkpX-EKnTKORRxDEwCZu",
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
                "kesan": "Hebat, keren banget sumpah aku kagum",  
                "pesan":"Kaka semoga terus membanggakan yaaa kakk, semangat terusss kuliahnya dan semangatt menjadi senator keren di hmsd ini"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Baikk cantikk ramahhh, senang bertemu ka Nadya",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta ",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"Lancar lancarrr perkuliahannya kakkk, semangat teruss nugasnyaa sambil dengerin lagu itu"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Asikk baikk dan ramaahh",  
                "pesan":"Lancar terus ya kaaa kuliahnya supaya selalu bisa nonton dengan tenang, tanpa ada pressure apapun"
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "lusyuu dan seruuu",  
                "pesan":"Semogaaa selalu semangat dan selalu lancar perkuliahannya ya bangg"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "My mentor ku?? Ahhh seru sekali Ka suci ini, fun fun fun",  
                "pesan":"KA SUCI, semogaaa jika kader ini sudah selesai kita tetap bisa kumpul terus bareng Cosval, dan TERIMAKASIH sudah jadi mentor kerennn"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya baik dan seruu",  
                "pesan":"Semangat terus jalanin kuliahnya banggg"
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kaka imup dan cheerful sekali Ka Aqila ini",  
                "pesan":"Semangat terus kuliahnya ka Aqila, tetep jadiii orang yang cheerful ya kak seneng liatnya"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang Hazel dulu terlihat rapih loh sebelum gondrong",  
                "pesan":"Bang bisa kali rambutnya dirapihin, biar freshhhhh, TAPI TETEP keren kok bang, SEMANGAT TERUS BANG"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakanya baik dan seruu",  
                "pesan":"Semangat dan lancar lancar terusss yaa Kaka kuliahnya, semoga hobi-hobi Kaka yang seru itu bisa terus terjalankan!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AqHLDrAJwFszY6jaryF9oypDg4rlmhuv",
            "https://drive.google.com/uc?export=view&id=1uPFVpr1bvgd1-z0Cv21zb0k1LDFGU970",
            "https://drive.google.com/uc?export=view&id=1LukobUVV_d2yWnhCJgefk3TIeYbp-v1N",
            "https://drive.google.com/uc?export=view&id=1LBriF5FH_Sc6E7_9ky5ZDcOYPrHSHwB2",
            "https://drive.google.com/uc?export=view&id=19KN9XQau3DU1lnJngD5tAmdUuwcObXNH",
            "https://drive.google.com/uc?export=view&id=1o4TYl0CxG81dYB3iP59vxWZzBLe3Nshz",
            "https://drive.google.com/uc?export=view&id=1oDykTTM97i34Mayzi-FjelQ6eORA4coc",
            "https://drive.google.com/uc?export=view&id=1QVIXb7GfvHzZ7mBpQrIIj6uD1aPfI3_2",
            "https://drive.google.com/uc?export=view&id=1HKSJUBqvi-sT-GDzDwN9G3ks_YI7s84d",
            "https://drive.google.com/uc?export=view&id=1kjG4Gj_xAF4Khsp8yBJ_HdeO0ZGhwoii", 
            "https://drive.google.com/uc?export=view&id=1KE3vaUA4X3-irVjpZeHXzUw--ilxHmOg",
            "https://drive.google.com/uc?export=view&id=1tMTkDxQ5zm4tDhvCza1_i3MryvpKIbUz",
            "https://drive.google.com/uc?export=view&id=1WDTcfZd1EKyzRL02kVn-SYhdjhr1Tmqw",
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
                "kesan": "Bang ridho asik banget, keren tapi agak tengil gitu yah ",
                "pesan": "Bang Ridho,, lancar-lancar ya bang apapun yang Abang lagi kerjain, semoga hal baik selalu dateng ke bang ridho "
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "Kaka syantik baik ramaahh imup",
                "pesan": "Lancaarr terus ya kakk perkuliahannya"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "Abang keren ini,,, sampe bingung mau ngasih kata-kata apa saking kerennya,, bangga banget",
                "pesan": "SEMANGAT PIMNASNYA BANG DHARU, selalu bangga dengan semua pencapaian abangnya,,, when ya sekeren bang dharu"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Baru menyadari sedikit mirip uan, TP abangnya seru dan asikk",
                "pesan": "Semangat kuliahnyaaa dan lancar-lancar sampe akhir ya bangg"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Baikkk betull aku senangg kakanya ramah",
                "pesan": "Semangat teruss kakak, semoga tetep bisa lari sesuai hobi kaka di tengah ke sibukan semester ini"
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Baik dan ramah abangnya",
                "pesan": "Lancar-lancar di setiap urusannya ya bangg, semangat teruss kuliahnyaa!!"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Ramaahh, cantik betul kaka",
                "pesan": "Kakakk semangat terus kuliahnya, semoga urusan yang sedang dijalankan selalu lancar!!"
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakanya baikkk dan ramah ",
                "pesan": "Semoga kost Kaka ga ngambek karna ditinggal terus ya kakk, lancar terus segala urusannya "
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Ramahh dan asikk Kaka ini",
                "pesan": "Semoga selalu diberi kelancaran dan semangat setiap kuliah yaa kakkk"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "Ramahhh betulll bang jeremii",
                "pesan": "Pengen denger tampil nyanyi lagi lho bang,, semoga ada kesempatan buat tampil nyanyi lagi. SEMANGAT TERUS kuliahnya bang"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Baikk asik dan funny bang Jona",
                "pesan": "Fun fun fun bang jona ini, semangat terus kuliahnya yaa bangg"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Ka Sekar,,, tegas sekali tapi aslinya baikk",
                "pesan": "Semangat terus kakk, lancar-lancar setiap urusannya."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Baikk plus ramah kakanya iniii",
                "pesan": "Selain angin aku juga mau disapa kak,, SEMANGAT terus ya kaakk kuliahnya, lancar terus "
            },
        ]
        display_images_with_data(gambar_urls, data_list) 
    Baleg()
        

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gf_wN9WQQTGbSXYE9fMY9LilBx88vAgk",
            "https://drive.google.com/uc?export=view&id=1MG3dn_OIeTUsh6duOQ626tCek_M6Xlr3",
            "https://drive.google.com/uc?export=view&id=1JQ8HNFwI86yTmZDaCISy7ldcHW2vrHKn", 
            "https://drive.google.com/uc?export=view&id=1dCFSXkBBsHj3kwQSJvkht2hyns1_kbsy",
            "https://drive.google.com/uc?export=view&id=1Z_XAToJYuyiPsKmRkNnsv2Kvt19hYIzA",
            "https://drive.google.com/uc?export=view&id=1xmhV1eyE7BsGQJrjjIvvnksYESsSu6aO", 
            "https://drive.google.com/uc?export=view&id=10Z23WGFpNeAMAJKLBglKRez6-NPL36et",
            "https://drive.google.com/uc?export=view&id=1TM5ACUE6LZIaIgtAoHzryQwgiHnF_SjL", 
            "https://drive.google.com/uc?export=view&id=1gfHn1gEgbHdlm8XEwtWTkabha_tC-KNq",
            "https://drive.google.com/uc?export=view&id=1TxeNy1tcbVrz9ZF_Z2dYcvoLgCMPf6Cn",
            "https://drive.google.com/uc?export=view&id=1O2yRhZsIkycKzUB-kmkr-plXt-rIEy1d", 
            "https://drive.google.com/uc?export=view&id=14JtWY561YQmCeKWE_PTxJx72pKYx1DhD",
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
                "kesan": "Bang Ihsan jokesnya mantep banget", 
                "pesan":"Semoga jualannya laris manis"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Imuppp sama cantik betul kakanya",  
                "pesan":"Semangat kuliahnya ya kak, mau coba masakannya dong"
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakanya baik banget, cantik banget",  
                "pesan":"Semangat terus kak kuliahnya, jadikan menonton Marvel itu reward ya kakk"
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal":"Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Ka anad baik dan ramah betul",  
                "pesan":"Lancar terus ka nyari uangnya, ajarin aku juga plz"
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
                "pesan":"Semangat kuliahnya ya banggg"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Imup deh kakanya, baik juga",  
                "pesan":"Semoga dracin yang ditonton tidak menghalangi semangat belajar kakk"
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
                "kesan": "Kakanya ramahh sama baik betul, aku like",  
                "pesan":"Lancar lancar kuliahnya kakk, biar nontonnya lebih lancar lagi"
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Baturaja Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Bang Pome lucu banget, ada aja jokesnya",  
                "pesan":"Kemaren di cibt keren banget main basketnya bang"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Lucu betul bang afdhal imup",  
                "pesan":"Semangat terus bang, apalagi mancingnya"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Baik dan ramah betul kakanya",  
                "pesan":"Rekomendasi kartun yang seru kak"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal":"Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Baik seru dan cantik kakanya",  
                "pesan":"Ka Della hobinya udah dapet belum kak, semoga hobi yang menyenangkan "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1FmWfr_LVo1VgTmn8NHWIa3tTT2_83k0b",
            "https://drive.google.com/uc?export=view&id=1bfosaYhCnPlrlj7pGNAnphOCCCDc9KOW",
            "https://drive.google.com/uc?export=view&id=1eCyc7SyjqUcnB01IrYujTNstJY3qzZjc",
            "https://drive.google.com/uc?export=view&id=1DjzsoZXOfEwDYDXmcRjeq496cKmMzrl4",
            "https://drive.google.com/uc?export=view&id=1O9y7wHC8X6lvWEZy7akdDk4khfssxEme",
            "https://drive.google.com/uc?export=view&id=14NA7CvmdzkI2IN3jDbBNWrB5iM5b3PVq",
            "https://drive.google.com/uc?export=view&id=1_CIn8iehtD7OkEfN8UpyLT2lFteH0gNe",
            "https://drive.google.com/uc?export=view&id=1Bs4Y6EDIm1tSjdv4N7zQeLgbm5br08kB",
            "https://drive.google.com/uc?export=view&id=16ZlUfFZOKIdOZJFf6_Qxe7tmENcC1Cko",
            "https://drive.google.com/uc?export=view&id=1IxKTGCZ_fK_QuPor8TYs6S6QvdyKqKiu",
            "https://drive.google.com/uc?export=view&id=1PNQiu3S1kxN5mvF_aQXPLzfyVc0vJXOl",
            "https://drive.google.com/uc?export=view&id=1AlQjwrK0WMA4A-xoZY1MXGGqzF8cGvMU",
            "https://drive.google.com/uc?export=view&id=1A7UBzXgiRaT2hBvgpxOVwy7qDoo7VdhG",
            "https://drive.google.com/uc?export=view&id=1Rek_hAMwlh6-uS6jYFhjIpsbQOxY3pb2",
            "https://drive.google.com/uc?export=view&id=1jX__lzaUM36g004kDzM8gz1jvwWi8ZC0",
            "https://drive.google.com/uc?export=view&id=12NpgoUqNn1bKVHLqbuUnoMJV0M2H1EJK",
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
                "kesan": "Seru betul orangnyaa, asikk",  
                "pesan": "Semangat ngerjain TA nya bang, jangan ngeledek orang terus yaa bang"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakanya cantikk baik dan ramah",  
                "pesan": "Semoga karena kaka suka nolong orang, hal baik tersebut balik ke diri kaka ya kak"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Ka Hannaaa positive vibes bangeeett, seru ngobrolnya",  
                "pesan": "Semangat dan lancar terus sampai akhir yaaa kakk, sampe di fase ngabarin orang tua (mau wisuda)"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Baik dan ramah Abang ini",
                "pesan": "Lancar lancar yaaa bang kuliahnya, semangat terus "
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Asikk, seru, damaskus garis keras ya bang",  
                "pesan": "Semangat dan lancar terus bang kuliahnya!!!, jangan balap liar ah ga baik"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kaka cantik dan baik sekali",  
                "pesan": "Semangat terus yaa kak kuliahnya, lancar sampe akhir"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Ka Cerine asik dan ramah betull",  
                "pesan": "Lancar lancar terus yaaa kakk kuliahnya!!"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Bang jaya seru parahhh, asik banget",  
                "pesan": "Bang Jaya semangat terus kuliahnya, tapi bang jaya sepertinya selalu semangat sih orangnya"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Baik dan cantik kakaknya",  
                "pesan": "Lancar terus yaa kak perkuliahannya, semangat terus!!"
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Bang Rozaq baik dan ramah",
                "pesan": "Semangat terus yaa bang kuliahnya, semoga bang harvin diberi kesabaran karna diisengin terus sama banga"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Ka Tere tutor LMD aku, pintar sekaliii",
                "pesan": "Ka Tereee lancar terus kuliahnyaa, supaya hobi masaknya bisa terus dilakuin"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Baik ramah sekalii Kak Audin",
                "pesan": "Kakaak semangat terus dan lancar seterusnya ya kak perkuliahannya "
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Imupp sekali Ka Cika, seruu orangnya",
                "pesan": "Semangat ya kakk kuliahnya, semoga terlambatnya dikurangin hehee "
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakak cantikk dan baik sekali",
                "pesan": "Semangat terus dan lancar lancar yaa kak kuliahnya"
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
                "pesan": "Lancar lancar bang kuliahnya,,, burungnya jangan ditembakin,, kasian "
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Baik dan ramah kakak ini",
                "pesan": "Semangat dan lancar terus yaa kak ngampusnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WwyPFYcmupxsAS5LcMN5WTUA3CB4xS6B",
            "https://drive.google.com/uc?export=view&id=1sJ1ShJN2AbrzgBh-gmCJb3mifxyyKbuF",
            "https://drive.google.com/uc?export=view&id=17Y010grSofOILclKJu3gYH6OoCALYgzm",
            "https://drive.google.com/uc?export=view&id=1M3B8o7miqUyWnAz_HgkS28s87A3m5SwW",
            "https://drive.google.com/uc?export=view&id=14UJW-h9lDbSpYNreR2Dr9uSPoZX0pxtP",
            "https://drive.google.com/uc?export=view&id=1M32xHNXT1m4dHDMethN2iZ4k0c9-S1TB",
            "https://drive.google.com/uc?export=view&id=1odKgCQOYk-D2vFhl9Abl2HYg8rScsGbF",
            "https://drive.google.com/uc?export=view&id=1vv5fcX0YIDH6VN6-ourQOLxL7AiNzVbk",
            "https://drive.google.com/uc?export=view&id=1u35sAQio0ucRdITXRAL1GDwBLyAcuS8V",
            "https://drive.google.com/uc?export=view&id=1m7WBycvbjY2Xvify8yVWaebv7H3wZKRf",
            "https://drive.google.com/uc?export=view&id=1H7OZJT3NfALQ9eMSdTp1HDcwL-F_tkza",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1bzREYYn5-gq63F_3gfWgeomZ0Q59P5f2",
            "https://drive.google.com/uc?export=view&id=15vx3-vynHi1V3nV_BtHVaS_huKcDLvi-",
            "https://drive.google.com/uc?export=view&id=1v_cZ_5Ue7Khg4IoWiWcnA5Yyv47kGPpY",
            "https://drive.google.com/uc?export=view&id=1PeFCXcHLztRAF5MhO8w8F5ekrpSkzkTo",
            "https://drive.google.com/uc?export=view&id=1S8YK9aYEA9vKksBR3aDg5F7K6MO3j3AZ",
            "https://drive.google.com/uc?export=view&id=1EZ0Zv_MTqcKTv_VvuvTXJd2S7urEIpA0",
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
                "kesan": "Baikkk ramah cantikkk sekali ka Nayla ",  
                "pesan":"Ka Nayla ajak aku ke sumbar please. SEMANGAT TERUS YAA KULIAHNYA"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Ka Donna seru sekali, ramahh dan baikk",  
                "pesan":"Mau denger playlist musiknya dong kak, biar belajarnya semangat"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Bang Labo cool parah, ramah juga",  
                "pesan":"Lancar terus bang kuliahnya!! selancar motorannya itu"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Ka Saniaa baik dan supportive sekali",  
                "pesan":"Semangat dan lancar-lancar kuliahnya ya kakkk, supaya bisa nonton tanpa academic pressure hehe"
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakaa ini ramahh betul dan baikk juga",  
                "pesan":"Semangat terus yaaa kakk kuliahnya"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kaka ini baik dan cantik sekali",  
                "pesan":"Kaka semangaaat kuliahnya, supaya nontonnya bisa puasss "
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kaka imupp, ramah dan seruuu ",  
                "pesan":"Semoga bang razan dan ka anash ga digangguin lagi ya kak,,, SEMANGAT TERUS KULIAHNYA!!"
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya seru dan baik",  
                "pesan":"Semoga SDCARD nya luang terus biar bisa foto orang sebanyak mungkin"
            },
            {    
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Ka Allisha asik betul dan ramahh",  
                "pesan":"Semangat terus kuliahnya kakk,,, semoga setiap mancing selalu dapet ikannya!!"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Ka Alya cantik dan seruu",  
                "pesan":"Semangat jalanin kuliahnya kaakk, sesemangat kaka kalau jalan jalan"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Ka Bunga my pj konten, seru dan baikkk",  
                "pesan":"Kalau ka bunga ga perlu disemangatin kuliahnya, hobinya aja belajar, siap membantai UTS UAS "
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Ka Difa seru parah cantik baik",  
                "pesan":"Semoga selalu diberi waktu luang untuk baca Al Qur'an ya kak, biar dunia akhirat balance "
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Imutt banget ka Nazlah, seru juga",  
                "pesan":"Ka Nazlah semangat terusss kuliahnyaaa, kalo renang ajak-ajak dong ka"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Bang Daffa baikk sama ramahh",  
                "pesan":"Semangat terus kuliahnya bang Daffa!!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Baik dan ramah betul abang ini",  
                "pesan":"Lancar lancar terus ya bang kuliahnya, biar nonton animenya tanpa academic pressure "
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Ka Lucia cantik dan baik sekaliii",  
                "pesan":"Semangat kuliahnya ya kakk, semoga tidurnya selalu cukup "
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@_shaazzh",
                "kesan": "Kakanya baik dan ramah betul",  
                "pesan":"Semangat terus kak kuliahnyaa, lancar lancar yaahh"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Baik dan ramah Kaka ini",  
                "pesan":"Semangat terus kak kuliahnya,,, semoga ga suka bengong lagi ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DEbuBwEcFNYnFdNB2i1fpBmAn2cG1J55",
            "https://drive.google.com/uc?export=view&id=1lmgb8WlCdZBLuOrB6MgPu4BHP0ocwvxC",
            "https://drive.google.com/uc?export=view&id=1jnsRS2fgsnt-8M39_tB7_mo6nrCGuQTq",
            "https://drive.google.com/uc?export=view&id=18ZKyH19INHRkCBltFFfRZxG-dF-hKmfx",
            "https://drive.google.com/uc?export=view&id=1eKh-zRRJL7pX0DrKOZ9D8vumC9l8i6Io",
            "https://drive.google.com/uc?export=view&id=1CAzSdhVj5lBY7y1nDlSUCAkvGSA3lLs_",
            "https://drive.google.com/uc?export=view&id=11t7eEXMNZo75OYKGT0gWhSys2PC0Wnew",
            "https://drive.google.com/uc?export=view&id=149sOASEv0UPGlGzrv1AZ9E1AvE418yON",
            "https://drive.google.com/uc?export=view&id=1tdxdTfu5BVO18qP6yIGr1Oh35Ik33Yl-",
            "https://drive.google.com/uc?export=view&id=1aY6sn0po8c5MQEunLXdzNPZ_9tCRRR3d",
            "https://drive.google.com/uc?export=view&id=1nFRGpTstoaAfqn9N3TZ_IeYS2zzKXsOG",
            "https://drive.google.com/uc?export=view&id=1JEzT_GZe_obJte1NpaZgs1B70JDUh0JH",
            "https://drive.google.com/uc?export=view&id=1RRKRYqwqB1TWOLvw3KKTu6DbMHkupUUk",
            "https://drive.google.com/uc?export=view&id=1yZf1PQJiOKiY1xexyJJfwXa-z4xemzOz",
            "https://drive.google.com/uc?export=view&id=1Hgp9h3RO9958RnS43mr5nsFugRFcqqsO",
            "https://drive.google.com/uc?export=view&id=1sA0gKsRRWL1nK5-wwj1CWS46j9fsinRE",
            "https://drive.google.com/uc?export=view&id=1azKa4LbEgpBtmh8H3UmYKj1Fbpt1GnB7",
            "https://drive.google.com/uc?export=view&id=1xFMAOA1iSt4MsGmJw1vOXXycCpUyLLaE",
            "https://drive.google.com/uc?export=view&id=1neRZgV8wivXs-8aXMSYc0uM18YSyll6T",
            "https://drive.google.com/uc?export=view&id=1G5heQn-i0XNqdEev9EJkwHVTpYmQ6bEa",
            "https://drive.google.com/uc?export=view&id=1420M6DB98_2Z1P4RFYb0iyERS3nglf-8",
            "https://drive.google.com/uc?export=view&id=1xEYPX4Xs-WGTF_wyfBJVkymYxvCl2CDi",
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
                "kesan": "Tegass, dan baik ka arini, aku suka to the point",
                "pesan": "Lancar yaa kakk kuliahnya sampe akhir, semangat terus!!!"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20 Tahun",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Baik dan cantik, senangg bertemu kakanya",
                "pesan": "Semangat terusss kakak, semoga lancar terus perkuliahannya supaya bisa jalan jalan terus "
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15 Tahun",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Ramah sama baikkk sekali Abang ini",
                "pesan": "Semangat sampe akhir terus ya bang kuliahnya, semoga ga mancing keributan lagii"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "-",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Udah cantik, keren, pinter betul kaka ini",
                "pesan": "Semangat terusss kak, semoga selalu bisa main di tengah kesibukannya tanpa ada pressure apapun"
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20 tahun",
                "asal": "lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Cantik baik dan ramah sekali",
                "pesan": "Semoga bisa jalan jalan terus kaakk walaupun di kampus ini sangat amat sibuk"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20 tahun",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Baik sekali kaka inii, ramah betul",
                "pesan": "Semoga tidurnya selalu cukup supaya perkuliahannya bisa terus semangat "
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20 Tahun",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Asikkk dan baik ka indah",
                "pesan": "Ka indah,,,, stop mancing-mancingannya kak,,, SEMANGAT terus kuliahnya "
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Lewat terus loh di fyp tiktok ku, keren kerennn",
                "pesan": "Bang Bima, semangat terus kuliahnyaaa belajarnyaa biar bisa bikin jj achievement di tiktok, aku tunggu deh"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "19",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Ramaaah dan baik sekali abangnya",
                "pesan": "Semangat terus belajarnya bang, lancar lancar kuliahnya!!, semoga sesegera mungkin rumah yang diliat bisa kebeli"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakanya baikk dan asikk ",
                "pesan": "Kakaak semangat terus ya kuliahnya,,, sampe jadi idol di sains data ini"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Jati Agung",
                "hobbi": "Ikut kepanitiaan ",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Ka yolann seru diajak ngobrolnyaa",
                "pesan": "Tips supaya lolos kepanitiaan terus kakk, kayanya ga perlu disemangatin kuliahnya kalau Kaka ini mah"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20 tahun",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Ka Riska imupp baik dan ramah sekalii ",
                "pesan": "Semangat terus mem follow up chatnya itu kak, dan semangat terus kuliahnya!!!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25 tahun",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Ramah dan baik betul Kaka ini",
                "pesan": "Ternyata masih ada yang suka baca wattpad ya sekarang ini, SEMANGAT TERUS KA, nanti hobinya berubah jadi baca jurnal"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Imupp dan ramah baik hatii",
                "pesan": "Semangat terus kuliahnya kakkk, lancar-lancar terus pas ngerjain tugasnya "
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abang duta yang fyp lewat itera ganteng, kereenn bang duta",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Way Halim",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Eh baik betul loh Abang ini, informatif walau kadang suka diputer-puter ya kalau nanya....",
                "pesan": "Makasih ya bang tips n trik pplk nya, semoga kuliahnya lansyar terus, when ya kita satu kepanitiaan or satu divisi, tapi kenapa yah setiap ketemu langsung kok kaya orang ga kenal,,, padahal dah aku senyum n sapa loh"
            },    
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "Jati Agung",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd_",
                "kesan": "Bang yazid,, tegas tapi baik ya bang..",
                "pesan": "Sehat terus bang! senyum aja sumpah,, kalo senyum ga keliatan galak"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Baikk dan seru abangnyaa",
                "pesan": "Semangat terus ya bang kuliahnya, lancar-lancar di semua hal!!"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Mainin ikan cupang ",
                "sosmed": "@jaldii._",
                "kesan": "Asikkk banget bang jaldi, seruu",
                "pesan": "Bang Jaldiii semoga tetap cheerful teruss, senang melihat kecheerfulan bang jaldi"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20 tahun",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Baik dan ramah sekali kakanyaa",
                "pesan": "Semangat terus yaa kakk, semoga tetep bisa nonton thinkerbell terus walau banyak kesibukan "
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "CANTIK, baik,,, ramahhh seruuu betul KA mei",
                "pesan": "Ka meiii semangat terus yaa, aku senang melihat ka mei yang ceria itu"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "KEREN BGT BANG AHMAD",
                "pesan": "Semoga ada penerus Bang Ahmad di setiap angkatan,,,, when ya bisa sekeren bang ahmad"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f7ywGop6vWXc-AInvDc110XhZDuM1OL9",
            "https://drive.google.com/uc?export=view&id=15oxRqqvWJ3c1wkyE8K2GT5Dzn59Fw-ZT",
            "https://drive.google.com/uc?export=view&id=1OSF2HtGfK7gLHwiZvskKJq7aHkGKhs5R",
            "https://drive.google.com/uc?export=view&id=1ppxvXAP1Wggni2yVQwX9bX9wyvMaTZHj",
            "https://drive.google.com/uc?export=view&id=1QWx8Mx8S5vdERD6n43nYFmxvPnZ4n7oI",
            "https://drive.google.com/uc?export=view&id=1gYyndGBiaH2qcBF3knd09wh9bisbOnV0",
            "https://drive.google.com/uc?export=view&id=1x_j-T-4-KSz82Fra9hvN8KbOq-IyYnwF",
            "https://drive.google.com/uc?export=view&id=1u0zUcLUTKllNuPcntWUkjEAydo21v4VE",
            "https://drive.google.com/uc?export=view&id=10pL1_Tm77brFYoOv9NEJCp0Cso7Oww5K",
            "https://drive.google.com/uc?export=view&id=1jCpmjeSTtplUtmdj5H5WDJJh-CtzrtbP",
            "https://drive.google.com/uc?export=view&id=1MaUbBj8NH3POaAheaunnRKRbG3uMIbNc",
            "https://drive.google.com/uc?export=view&id=1B9Q-6A_qeU31XLhLmf5OBMmjAWVlr8he",
            "https://drive.google.com/uc?export=view&id=11nQG-JqLd-KX5_mCXcCKoMQl2eGqodPf",
            "https://drive.google.com/uc?export=view&id=1pCNv6lfv0SsCO23WAEectvc3NWFsLEZI",
            "https://drive.google.com/uc?export=view&id=13GdgY1o67d9lQsSiVPpcMIcNjnlAJAzd",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Mancing",
                "sosmed": "@kevinaj__",
                "kesan": "Keren banget, asik juga bang Kevin",
                "pesan": "Lancar terus yaa bangg perkuliahannya, semangat ngejalaninnya seperti semangat memancing itu!!!!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 tahun",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Imup sekali kakakk, baikk dan ramah sekali",
                "pesan": "Kaka semangat teruss kuliahnya, ditunggu update mendakinya yaaa"
            },
            {
                "nama": "Ali Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "21 tahun",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Baikk plus ramah juga bang Ali",
                "pesan": "Semoga bisa nonton F1 secara langsung ya bangg, yang penting sih semangat dulu kuliahnyaaa"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Badminton ",
                "sosmed": "@mridwaan_22",
                "kesan": "Abangnya asik sama seru",
                "pesan": "Semangat terus bangg kuliahnya, semoga tetep bisa badminton rutin walau semester kali ini sibuk betul "
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar + menghitung uang",
                "sosmed": "@aayuandrianni_",
                "kesan": "Baikk sama ramah Kaka inii",
                "pesan": "Smenagat terus kuliahnya kaakk semoga semuanya selalu diberi kelancaran yaa"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Jogging ",
                "sosmed": "@dafaelpriza_",
                "kesan": "Asik plus ramahh bang Dafa, meskipun nama saya dilupain",
                "pesan": "Semangat joggingnya bang, tapi semangat kuliahnya jangan sampe lupa, btw kangen bekasi kaga bang "
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 tahun",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Mancing",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakanya baik dan seruu",
                "pesan": "Semangatt terus kuliahnya kaakk, semoga setiap mancing selalu dapet ikannya biar senanggg"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 tahun",
                "asal": "Lampung Tengah",
                "alamat": "JI Pulau Damar",
                "hobbi": "Memantau dl tugas",
                "sosmed": "@afdall.03",
                "kesan": "Baik terus seru bang afdal",
                "pesan": "Semoga dl tugasnya ga cuma dipantau tapi dikerjain juga ya bangg, semangaaatt"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Asikk dann ramah betulll ka bilaa, senang bertemunya ",
                "pesan": "Kakaaa semoga selalu dihampirin rasa bahagiaaa lewat apapun ituuuu, semangat terus ka bila kuliahnya!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "ASIK bangetttt dan ramah pol bang andra ini",
                "pesan": "BANG ANDRA POKOKNYA SAYA BERDOA semoga semua mua mua muanya dilancarkannnnn, sehat sentosa aamiin"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20 tahun",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Lucu abis itu juga ramahh",
                "pesan": "Semangat dan semoga semuanya selalu lancar ya bang, ditunggu live tiktoknyaa"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal": "Surabaya ",
                "alamat": "Kemiling ",
                "hobbi": "Nanem Sawit ",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Ramah terus baikk Abangnya",
                "pesan": "Semangat terusss bang kuliahnya, lancar segala urusannya, request jangan nanem sawit bang dah kebanyakan"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Baikk, ramah loh ka indah",
                "pesan": "Semoga semua urusan kuliah ataupun di luar kuliah kaka selalu lancar ya kakk, smenagat terus!!!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18 tahun",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Ka Caca imup, fun banget ngobrolnya",
                "pesan": "Semangat dan semoga kancar terus ya ka cacaaa, jadi jadwal nyapu di gacoannya hari apa aja ka!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 tahun",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini cool cool gimana gitu ((alias kalem ya(?))))",
                "pesan": "Kalau yang ini kayanya gausah disemangatin kuliah apalagi kelas pagi, kaann abangnya hobi bangun pagi, tapii semoga semua urusannya selalu dilancarin ya bang "
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1c0sbWwY1gdy-j5As1lQ1OuKXvYqj9YGK",
            "https://drive.google.com/uc?export=view&id=111A6AJ-zlB79fEKL7XERNY9C5Igu213S",
            "https://drive.google.com/uc?export=view&id=1tnW7_bRHe0f5vpR8Bfs6kXsBvF0I4Ldf",
            "https://drive.google.com/uc?export=view&id=1tzYmzQ5c1AQkUoamYkNq_FWvxPYEDQMy",
            "https://drive.google.com/uc?export=view&id=1qAYLl-pe6WfVoeJ_ACjkeiMPLHy_A7R3",
            "https://drive.google.com/uc?export=view&id=17IkGdYRM3-L49bOE4jxAbgsP0vw6vlaQ",
            "https://drive.google.com/uc?export=view&id=1cAgKze_0ZPdZzBdGnxooIwIaA0_SweQ5",
            "https://drive.google.com/uc?export=view&id=1MldwpprfrCOuz86tBjRwCCmHygJktQKI",
            "https://drive.google.com/uc?export=view&id=1CfT0sLRI_VlrTFYwT3AZVuyrzh1oR82X",
            "https://drive.google.com/uc?export=view&id=1s0lXsaWAp3SK1TqDje5a-IafTJzgKbQF",
            "https://drive.google.com/uc?export=view&id=1RwuZ48Z6JDhpivMUVzFrEM4ekU8q1q5L",
            "https://drive.google.com/uc?export=view&id=1SpWqaV1T5ozJHlDyWk4PhGbi7VXitIfU",
            "https://drive.google.com/uc?export=view&id=1AA8oC9LepGDFxeszLZ1XIcINNPj9_xNs",
            "https://drive.google.com/uc?export=view&id=1yEAGHebL9unQp3Q_k9xgteUHPpnYr3S1",
            "https://drive.google.com/uc?export=view&id=1xmzQTCrFZmiH3L3KA5FPo6PZ_9P5DeSc",
            "https://drive.google.com/uc?export=view&id=1ud1mNxzF05R7T5PuNClNDJo9oXZP6NB8",
            "https://drive.google.com/uc?export=view&id=1x0zeX4MI_x2yrGo_rGIeze34PGoxQe5y",
            "https://drive.google.com/uc?export=view&id=1FpJ9TeXe0UTMatXNV-Aogo62O3zur7Rd",
            "https://drive.google.com/uc?export=view&id=1Wpge9juIvv1f4yUm_sUUjZiGXo1hwjkq",
            "https://drive.google.com/uc?export=view&id=1Nik-N5a9Dunt0kifYxiP0izpchVvpJsp",
            "https://drive.google.com/uc?export=view&id=1bm2oZNKyf6UQRKVd-gmjK9-yyXcRjivJ",
            "https://drive.google.com/uc?export=view&id=1_dfAzebMLYKrgPAJyFU7c3nH0sXnFyyP",
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton Bandar Lampung ",
                "hobbi": "Gangguin bang keya",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio keren banget loh, baikk lagi ",
                "pesan": "Lancar terusss sampe akhir yaaa bang Fabio kuliahnyaaa, semoga bang keya selalu sabar karna diusilin terus"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21 tahun",
                "asal": "Lampung Tengah ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tantyyy, cantik betull, keren sekali",
                "pesan": "Lancar-lancar terus sampe akhir kaakk, semoga selalu ada waktu untuk nonton apapun itu"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya baik betul, keren banget dengan segala pencapaiannya a",
                "pesan": "Semoga semua kebaikannya menjadi amal yang baik kelak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@keyashafi_",
                "kesan": "Abang ini keliatan banget cowo pinternya",
                "pesan": "Lancar terus sampe akhir yaa kuliahnya bangg"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21 tahun",
                "asal": "Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya kaya keren bangett, mirip pa tirya",
                "pesan": "Semoga bisa terus main futsal tanpa terganggu akademiknya ya bangg, dan itu pasti sih, abangnya pinter gitu"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20 tahun",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "Keren dan baik ramah abang ini",
                "pesan": "Semangat terus kuliahnya, dan bisa gitaran terus"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12 tahun",
                "asal": "Bali",
                "alamat": "Nusa Penida",
                "hobbi": "Menghayal",
                "sosmed": "@Violaadrtr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20 tahun",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Cantik sekali, baik pulaaa, suka sekali ",
                "pesan": "Seru banget hobinyaa, lancar terus kuliahnyaa, biar bisa jalanin hobi itu terus"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19 tahun",
                "asal": "Kepulauan Riau",
                "alamat": "Jatimulyo ",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kakanya cantik dan baik ",
                "pesan": "Lancar terus kuliahnya kakk, semoga selalu ada waktu buat nonton KHW itu"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20 tahun",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakanya seruuu dan asik baik betul",
                "pesan": "Kakanya seruuu dan asik baik betul"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "@_els.a",
                "kesan": "Ka Elsa seru dan ramah sekalii, aktif gitu ",
                "pesan": "Semangat terus dan lancar terus ya kakk kuliahnya dan ngampusnya"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main game",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kaka ini baik sekali, ramah jugakk",
                "pesan": "Semangat dan lancar terus yaa kuliahnya, supaya main game sepuasanya tanpa academic pressure "
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@_loviaa",
                "kesan": "Kakanya baik dan ramah betul ",
                "pesan": "Lancar lancar terusss ya kak kuliahnya, semangaaatt"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "18 tahun",
                "asal": "Kalianda",
                "alamat": "Kota Baru",
                "hobbi": "Main game",
                "sosmed": "@aruccy_",
                "kesan": "Ramah dan baik betul Abang ini",
                "pesan": "Lancar dan semangat terusss yaa kuliahnya bang"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19 tahun",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Ka Sherenaa, baikk sekalii dan ramah betul, my kaka asprak alpro ku",
                "pesan": "Semoga di waktu yang sibuk-sibuk ini tetap ada waktu untuk bermain make up-make up yaa kakk"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Ka Faizaaa, baik sekali asprak alpro aku, seru dan asik betul",
                "pesan": "Ka Faiza lancar terusss yaaa kak kuliahnyaaa"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Baik dan ramah abangnyaaa",
                "pesan": "Semoga selalu bisa main game tanpa ganggu waktu belajar dan tanpa academic pressure yaaa"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik tapi kaya tegas gitu",
                "pesan": "Hobinya keren banget kagum saya"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Abangnya pinter banget sumpah kagum",
                "pesan": "Semoga selalu stabil kepintarannya atau bahkan meningkatkan ya bang, semoga nular plzz"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "Imutt baikk dan ramahh sekali kakanya",
                "pesan": "Semangat terus yaa kuliahnyaaa, dan semoga hobi masaknya bisa terus dijalanin"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20 tahun",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@Syaafiqui",
                "kesan": "Keren dan baik abangnya, astut metnum ku",
                "pesan": "Semangat dan terusss dimudahkan jalan kuliahnya ya bang"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal": "Kota bumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "Baik dan ramah bang henry ini",
                "pesan": "Lancar-lancar bang kuliahnya, semoga jailnya ke bang nuel dikurangin ya bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OVxZVKz8nP-JFIfH7FGTc78d7BEuFYb1",
            "https://drive.google.com/uc?export=view&id=1DyWZm7Id09h24L0JtW6Cv7mnbmHLbgPX",
            "https://drive.google.com/uc?export=view&id=1reNBBFZJxRmx4TwibYi1g0DdSiXlqBnM",
            "https://drive.google.com/uc?export=view&id=1KF6--IRxMwy-u2zh6BQkcnpJ94QMnIaO",
            "https://drive.google.com/uc?export=view&id=1OaLzuDuS9pX2pwZV1VgK2YVwIYB2qdyz",
            "https://drive.google.com/uc?export=view&id=1ZvBn2pRmohsOeUun7WTOK78moS9jUsK-",
            "https://drive.google.com/uc?export=view&id=1ItfRS37ToalecwNLXZ9jtBM3V38zW55h",
            "https://drive.google.com/uc?export=view&id=15pr0TfJq8XdvQYVtv8HVTXiaMZH638gN",
            "https://drive.google.com/uc?export=view&id=1aNPH3KddK0DQ-HDfI0n6nwyzKN5Xa1T-",
            "https://drive.google.com/uc?export=view&id=12DMpzJCGLy_2JqHlxEXW6981gzmZMdW9",
            "https://drive.google.com/uc?export=view&id=1ICvLpU369n8lmjCY-idthOcEkemNIa6J",
            "https://drive.google.com/uc?export=view&id=1xsPWw0UKCI6OGaNv8L8D4Fd83eX0ra_z",
            "https://drive.google.com/uc?export=view&id=11D7pNu-yLudvX__uWGKcOqB6rwuPh1PD",
            "https://drive.google.com/uc?export=view&id=1zc9eXeOLEjtYqrKilQY5aWdojE-3r3Il",
            "https://drive.google.com/uc?export=view&id=17gLeeWT3Mnt48JvcGYDOXkxN_z_f_KaP",
            "https://drive.google.com/uc?export=view&id=1ysjRWXJ-hYYGZhhEaerW0X7jqmb9yoVK",
            "https://drive.google.com/uc?export=view&id=1l5U3fGvWOxMd6hwl4LxaNOXoUg20ZbZ_",
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
                "kesan": "Selalu salfok dari awal ketemu karna ka arin make up nya flawless bangett sukaa, ramah juga pula ",  
                "pesan":"Semangat dan semoga lancar terus ya kak perkuliahannya, tetap jaga kesehatan ya kak, semoga selalu bahagia kakak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Cantikk plus baik kaka ini",  
                "pesan":"Kaka semangat terus dan semoga lancar terus sampe akhir ya kak perkuliahannya "
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Baikk dan banyak ya jenis sulap yang dibisa",  
                "pesan":"Bang Nobel semangat yaa kuliahnyaa, kapan bisa tampil main sulap di acara sains data lagi bang"
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Seruu ngobrolnya asik, baikk juga abangnyaa",  
                "pesan":"Semangat dan lancar sampe akhir perkuliahannya yaa bangg, jujur masih penasaran soal naik gajah itu"
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Baik dan ramah abangnya, bagus inovasinya buat kader tahun ini",  
                "pesan":"Semangat dan lancar terus ya bang kuliahnya,, jangan lupa minum air putih ya, khawatir suaranya abis soalnya hobinya suka teriak"
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Abang ini kalau di luar rangkaian seru sihh, baik jugaa, tapi di rangkaian juga baik betul lohh",  
                "pesan":"Semangat terus bang kuliahnyaa, lancarr teruss semua hal yang lagi dikerjainnya"
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Vibes komdis pplknya ga ilang-ilang bang caesar nih, TAPI ramah abangnya",  
                "pesan":"Semangat bang kuliahnya!!, sehat dan bahagia terus ya Bang Caesar "
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Ramah sama baik terus seru Ka Yudiaa",  
                "pesan":"Ka Yudia semangat terus kuliahnyaa, semoga semua uang yang lagi dikerjakan diberi kelancaran dan kemudahan "# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Ramah sama baik betul Abang ini",  
                "pesan":"Lancar-lancar kuliahnya ya bang, semangatt teruss, pakan anak ayamnya udah dicari belum bang"
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Asikk dan baikk Kaka ini ",  
                "pesan":"Semangat terus kuliahnya kakk, hati-hati jalan kakinya ya kak, semoga selalu sehat dan diberi kemudahan dan kelancaran "
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Asikk dan ramah betull, enak ngobrolonyaa",  
                "pesan":"Seru banget hobinya ngebaking, semoga tetap ada waktu buat ngelakuin hobinya ya kakk"
            },                        
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kakanya wangii banget salfok, cantikk plus ramahh",  
                "pesan":"Ka Azel semangat terus kuliahnyaa, coba Ka Azel dispill parfumnya, suka banget"
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Cantikk sekali, udah gitu baikk",  
                "pesan":"Semangat terus jalanin kuliahnya kaakk, plus semangat juga ngurus peternakannnya"
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Baikk dan ramah Abang ini",  
                "pesan":"Semangat terus kuliahnya yaa bang, lancar terus segala urusannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Asikk sama ramah kakanya, seru ngobrolnya",  
                "pesan":"Semogaa tetep bisa terus main roblox yaa kak walau semester ini lagi sibuk banget"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abangnyaa baik sama ramah, seru",  
                "pesan":"Semoga setelah suka baca peraturan rektor, di kemudian hari Abang yang jadi rektornya, semangat bangg"
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Baik sekali ramahh, imup kakanyaa",  
                "pesan":"Semangat terus yaa kakk kuliahnya, jangan lupa air putihnya di minum terus yaa kak"
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
