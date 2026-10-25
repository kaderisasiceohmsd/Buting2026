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
            "https://drive.google.com/uc?export=view&id=1Qv4gW5yUECqPqx5RyLDK_4GrRCwdqDg9",
            "https://drive.google.com/uc?export=view&id=1xRn8-gDihbrmkXhZV4wIKdy00L2jxq7V",
            "https://drive.google.com/uc?export=view&id=1UJniVLXFBmLdxF5i4l-TGeDJQlClViQQ",
            "https://drive.google.com/uc?export=view&id=1NtK6MZmUl5YbIZViJXVp55z5dUwEvpGA",
            "https://drive.google.com/uc?export=view&id=18u2easkmpaYtWffL-VwDZe7irQrHkxEt",
            "https://drive.google.com/uc?export=view&id=1GqzgWAXiXTb_HYCXId22DmGoq2B269d7",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung ",
                "nim": "123450103",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "Abang ini baik banget",
                "pesan": "Semangat terus bang Kahim",
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal": "Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren!",
                "pesan": "Semangat terus kuliah nya bang",
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Banyak yang saya pelajari dari kak Efi.",
                "pesan": "Semoga kakak lulus tanpa hambatan.",
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang Qois asik, ngerti terus sama apa yang dia jelaskan",
                "pesan": "Semoga kuliah nya dilancar kan bang.",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik dan humble",
                "pesan": "Semangat terus kuliah nya kak.",
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini paling asik sih",
                "pesan": "Kak apapun masalah nya jangan menyerah.",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

elif menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Nm2vnOo1v9fqcdD0yZtKGPghp9okypWx",
            "https://drive.google.com/uc?export=view&id=1ITE5ACHWnCn3c2T2BsKrwziB1cMe9n1k",
            "https://drive.google.com/uc?export=view&id=1hql9HuVrybkFHQz7bx-9JZVPumwqIXio",
            "https://drive.google.com/uc?export=view&id=1s3WZ3TtBNuNFtOXDeJTVyF49LIBgad4T",
            "https://drive.google.com/uc?export=view&id=1cK8zeMxgDwjvNUcuDV84IOvYNeAS6Vxq",
            "https://drive.google.com/uc?export=view&id=1Vr0dKVQk3_T-nT37KwEw41vQj7x0z_Jt",
            "https://drive.google.com/uc?export=view&id=1xAEdV5Iqbsy-obR8GMKokWwWmS0LjPuI",
            "https://drive.google.com/uc?export=view&id=1GYVN_kwyqCKx_h-RNttLVWiwkTKZ1y98",
            "https://drive.google.com/uc?export=view&id=17A6KaycBMlQXQHMaJrr1fIdJy-goXG2V",
            "https://drive.google.com/uc?export=view&id=141ytkz-wHu7qfjirse2SqjTMnM4kvT2L",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
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
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Senator()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k4nv_Glyznt90Kgtg66hOhDSi780ff3Z",
            "https://drive.google.com/uc?export=view&id=1dS0TBTfQJeP9Ui0evpFeAYSVRf8yRKsM",
            "https://drive.google.com/uc?export=view&id=1o-agR_izPjw7qg2w0HbS6uEIxPSrMy-3",
            "https://drive.google.com/uc?export=view&id=1vInIKWE1hbqfbfwRzp2biij1xPPpLX1d",
            "https://drive.google.com/uc?export=view&id=1Jn4vdUIe_KPVQNhNensvPxRz35lDTSm0",
            "https://drive.google.com/uc?export=view&id=1LiEgNuXXKgb_1LYynQY1UxVuRK0PybKf",
            "https://drive.google.com/uc?export=view&id=1iIr1yEzSLZZqpfLArOExwAWbDAgFFwdI",
            "https://drive.google.com/uc?export=view&id=1F5zBCX4nEWK_btl8Ko-UrOiMpVFk5FaW",
            "https://drive.google.com/uc?export=view&id=1SsdIjEcS13UytHNtkX45u0Syw5D8ep8W",
            "https://drive.google.com/uc?export=view&id=1ep-ijLicWk3YcILP6Zxa6UYJSSnD7z34",
            "https://drive.google.com/uc?export=view&id=1jp_JOBSg9Y722BxmpMTP-2QMzvZH49Iq",
            "https://drive.google.com/uc?export=view&id=1S7A6lPRkfJY-fajifj4C286pJhEEyzSU",
            "https://drive.google.com/uc?export=view&id=1wGSixnQ84qwQBB3jugyba8u5SKfOwOW3",
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
                "kesan": "Abang ini jauh bgt asal nya",
                "pesan": "Sehat terus bang. ",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "Kakak jue lucu banget orang nya",
                "pesan": "Jaga kesehatannya kak",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "Bang dharu pinter banget",
                "pesan": "Ajarin biar jenius dong bang",
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Bang niko ini keren banget",
                "pesan": "Semangat terus bang kuliah nya",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakak ini selalu happy dan baik banget",
                "pesan": "Semoga happy terus kak",
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abang ini teman dari temannya saya",
                "pesan": "Semangat terus kuliah nya bang",
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak ini jago jadi pentutor",
                "pesan": "Makasi kak",
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Kakak hani paling lucu banget si cantik lagi",
                "pesan": "Jaga kesehatan dan jangan lupa makan ya kak",
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "Abang ini aura nya keren sih",
                "pesan": "Semoga happy terus bang",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini baik, lucu dan bisa ngerangkul",
                "pesan": "Jaga kesehatannya kak",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Jujur abang ini lucu sih",
                "pesan": "Semoga cepat lulus kuliah nya bang",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini selalu happy",
                "pesan": "Jangan lupa makan ya kak",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik dan ramah lagi",
                "pesan": "Semoga selama kakak kuliah gada hambatan nya",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Baleg()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bdiSqiM7dihrd0sNMiLiJAIH0fj7-sSJ",
            "https://drive.google.com/uc?export=view&id=1fHndOEriE_ppt1YuFPUcbMjO2glNHDIM",
            "https://drive.google.com/uc?export=view&id=1hntPE-joZDWxhxewbDQyheEx4r8TmqfK",
            "https://drive.google.com/uc?export=view&id=15TcPVGSjwIef6v-ZOhss2ZoWudOn3Ijm",
            "https://drive.google.com/uc?export=view&id=1-RiJb9TBncwLKbSq_IlV5MQA1yOkgEBe",
            "https://drive.google.com/uc?export=view&id=1HjHf59czKyg3FRpDRDwR4yjEKmjcRcMa",
            "https://drive.google.com/uc?export=view&id=1occM8KNf_Yfo83bHXvLCCCV9SBKZM3YK",
            "https://drive.google.com/uc?export=view&id=1K5ga4vWmm8y9vfFjuG9PNDYOAFj0Rogf",
            "https://drive.google.com/uc?export=view&id=1hMEvZkxJaWv86FT3A71K6m_sHLkxoP4N",
            "https://drive.google.com/uc?export=view&id=1Mw5X_urhC3VRiOgknD3briSDwCd0lySe",
            "https://drive.google.com/uc?export=view&id=1gBOJTYN14KXpAvxRHYpehDldTnESVNsA",
            "https://drive.google.com/uc?export=view&id=1il5Uv5pjKM9NKUxayu1OcIJQCk0cyfZV",
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
                "kesan": "Bang Ihsan asik banget urang awak",
                "pesan": "Semangat terus bang ihsan",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini baik banget",
                "pesan": "Semoga kuliah nya dilancar kan kak.",
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Banyak yang saya pelajari dari kakak ini",
                "pesan": "Jangan lupa makan kak",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah ",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube ",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang hasan ini ter lalu keren",
                "pesan": "Semangat terus bang.",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini bikin saya tau banyak hal",
                "pesan": "Fix pasti lancar kuliah nya kak",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Banyak hal yang saya pelajari dari bang iqbal ini",
                "pesan": "Jangan lupa makan bang.",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "-",
                "kesan": "Kakak ini asik banget",
                "pesan": "Semoga kuliah nya dilancarkan kak",
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Banyak yang saya pelajari dari kakak ini",
                "pesan": "Semoga kak Anadia Happy selalu.",
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Abang pome keren banget",
                "pesan": "Ajarin cara jago basket bang",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Berkat bang Afdhal saya tau banyak hal",
                "pesan": "Semangat terus bang walaupun hidup banyak tantangan.",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Fix kakak ini paling asik sih",
                "pesan": "Jangan lupa makan 3x sehari kak",
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak della cantik banget iya",
                "pesan": "Semoga hal yang kakak mau capai cepat tercapai",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_SSD()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hlN43tP27shUcnySQ7j6Ld5wg9TdhLzm",
            "https://drive.google.com/uc?export=view&id=1DgY_Jhwts7wYdk2MOI9rq88-YUoGPD67",
            "https://drive.google.com/uc?export=view&id=1afD1mc-yTctguGqzob8BPijFZgjMtOuB",
            "https://drive.google.com/uc?export=view&id=1OCG2KVzYFGzLMNQuNzAPs-Vo7WAlzSGI",
            "https://drive.google.com/uc?export=view&id=1f9F8XF-rttIMPfN4YKHymmMtrcNe5kRm",
            "https://drive.google.com/uc?export=view&id=1zoHlDcMdKOvriSNJfWbrd2DS-pADPNy4",
            "https://drive.google.com/uc?export=view&id=1RHGgJ0vvQPQ_MKpf4B2-N-rwWukpEj9P",
            "https://drive.google.com/uc?export=view&id=1s7yxZsYBWzoh0futx8ysH_5_G3C1SZrf",
            "https://drive.google.com/uc?export=view&id=1At62vJ12fRts1zyqurdx27o2SrmFPAnj",
            "https://drive.google.com/uc?export=view&id=1At62vJ12fRts1zyqurdx27o2SrmFPAnj",
            "https://drive.google.com/uc?export=view&id=1backw4RUa_evXsf9hPC9PQzmXB59m1fa",
            "https://drive.google.com/uc?export=view&id=1At62vJ12fRts1zyqurdx27o2SrmFPAnj",
            "https://drive.google.com/uc?export=view&id=1oIJSHVNA7vy5qlMQiYSRqNCIdEe2RXKS",
            "https://drive.google.com/uc?export=view&id=1At62vJ12fRts1zyqurdx27o2SrmFPAnj",
            "https://drive.google.com/uc?export=view&id=1MV7Grl0DyacD_8_ynsLzr0KJM68jJb3O",
            "https://drive.google.com/uc?export=view&id=1xOSLDmK0J9GFgAJMYK6-yKuK6xxvpfJ1",
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
                "kesan": "Bang Haikal orang nya sangat hangat dan merangkul",  
                "pesan": "Sehat selalu abangku"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini cantik banget",  
                "pesan": "Semoga kakak happy terus"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "banyak yang aku tau karena kakak ini",  
                "pesan": "Semangat terus kuliah nya kak"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Abang ini keren karena selalu semangat damaskus",  
                "pesan": "Sehat sehat terus bang jaga kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakak ini asik banget",  
                "pesan": "Jangan lupa makan nasi kak"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kakak asik banget dan lucu juga",  
                "pesan": "Semoga khayalan kakak tercapai ya"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Abang ini jago main basket",  
                "pesan": "Ajarin dong bang"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakak iini asik dan bisa ngerangkul",  
                "pesan": "Jaga kesehatan nya kak"
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Abang ini terlalu ramah",
                "pesan": "Semangat terus bang walaupun hidup itu berat."
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Banyak yang aku tau setelah kenal kakak ini",
                "pesan": "Kak sehat selaluu"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Abang ini ramah banget",
                "pesan": "Sukses terus bang semoga impian nya tercapai dengan mudah"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kakak ini suka ke curug",
                "pesan": "Pasti kakak suka nanjak juga"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Kakak ini keliatan ceria terus",
                "pesan": "Happy terus ya kak"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Banyak hal yang aku pelajari setelah kenal kakak ini",
                "pesan": "Sukses terus kuliah nya kak"
            },
            {
                "nama": "Muhammad Arvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Hangan dan humble",
                "pesan": "Semangat terus kuliahnya dan sukses selalu!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakak yang selalu happy",
                "pesan": "Jangan lupa makan kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1vP-e7g8u3wlQk68qDBOf3iRstIfEMNdI",
            "https://drive.google.com/uc?export=view&id=1oSnhAEr2f3niAJxb7wPjZmUIcH_EpD_8",
            "https://drive.google.com/uc?export=view&id=1veAKB--uS541WKBO9yrdt3Mxu-xFqyKu",
            "https://drive.google.com/uc?export=view&id=1O9bVaoModfnMZx1INdsP1g-OtzU_e7Wu",
            "https://drive.google.com/uc?export=view&id=1iXiCC8oe6Y7Efkl_GDxmkqml1zfdPunn",
            "https://drive.google.com/uc?export=view&id=1PGYf-QJmrMgNOZu-9Osj6ijpiOX8YEEg",
            "https://drive.google.com/uc?export=view&id=1jLV0KNO6YnRLOJ4dQkRTM5oS7NsiWeSd",
            "https://drive.google.com/uc?export=view&id=11r1tFpSdvfRGge46WBkbaqfi0mIDPN1w",
            "https://drive.google.com/uc?export=view&id=1KclV-RlyzYqS2RhTjsW7JeWhgTLScuKH",
            "https://drive.google.com/uc?export=view&id=15k70ElxQVvP27iJV4rvLY3nFXix5YtLG",
            "https://drive.google.com/uc?export=view&id=1v-9yZRA0J2RBo6ZFtfT-RHzhSmBPbOJQ",
            "https://drive.google.com/uc?export=view&id=12TJALBWRHByJ_y7ZuDdlWu234aSjStjD",
            "https://drive.google.com/uc?export=view&id=1e16b_itBTHuq5TtYDwDBNRWE9TmfZXgJ",
            "https://drive.google.com/uc?export=view&id=1tPfp28sWU_LSNDwqGZQQ9nc4dqqG0ka4",
            "https://drive.google.com/uc?export=view&id=1so6-RCNa1akGLfXUbBILIfp9tB0uQqfQ",
            "https://drive.google.com/uc?export=view&id=1dnYvO9E6abVQRKn7OIyHVmwN1u8kvVQQ",
            "https://drive.google.com/uc?export=view&id=1cZikru9vk_5aXTzmFKqMmEPMHCIacZO2",
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
                "kesan": "Kakak ini asik saya suka belajar dari dia",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini jago nerangin materi saat tutor",  
                "pesan":"Jangan lupa makan kak"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Abang ini keliatan happy terus",  
                "pesan":"Jangan lupa senyum tiap hari bang"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak ini baik, cantik lagi",  
                "pesan":"Semangat terus kak walaupun hidup itu berat"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kakak ini sangat ceria dan baik",  
                "pesan":"semoga yang disemogakan tersemogakan kak"# 1
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Bang razan ini baik banget",  
                "pesan":"Semoga kuliah nya dilacar kan bang"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini keliatan ceria tiap hari",  
                "pesan":"Jangan lupa makan 3x sehari kak"# 1
            },
            {    
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini baik dan cantik juga",  
                "pesan":"Semangat kuliah nya kak"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Banyak hal yang saya pelajari karena kakak ini",  
                "pesan":"Semangat kak jangan lupa makan"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini ceria dan happy banget tiap hari",  
                "pesan":"Kakak jangan lupa makan ya"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak ini banyak memberi saya pelajaran",  
                "pesan":"Semoga kuliah nya tidak ada hambatan kak"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakak ini asik banget, dan ga sombong",  
                "pesan":"Hati hati kalau berpergian kak"# 1
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "Tiap hari kakak ini happy terus",  
                "pesan":"Jangan makan ayam geprek terus kak"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Abang ini yang pertama mengajak saya bicara saat FG",  
                "pesan":"Semoga Sehat selalu bang"# 1
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Kakak ini baik, cantik dan ga sombong",  
                "pesan":"Kuliah nya semoga dilancarkan kak"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kakak ini baik banget,hangat dan ceria",  
                "pesan":"Jangan lupa makan nasi ya kak"# 1
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@Melukis & Menulis",
                "kesan": "Kakak ini yang ibkin saya tau banyak hal",  
                "pesan":"Jangan malas kuliah kak"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Banyak yang saya tau setelah mengenal kakak ini",  
                "pesan":"Tetap semangat walaupun hidup itu berat kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf() 

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w3zxsuNgVz3qoRknT-NdwtmX4GvYVJi2",
            "https://drive.google.com/uc?export=view&id=1uU8AScxMTpRTJZrRNeWZ-OcG-b4Hggoi",
            "https://drive.google.com/uc?export=view&id=1xASApW7_uFoZeAaE8Zcu1FNO4Bw5QgST",
            "https://drive.google.com/uc?export=view&id=1Dq_RZXYnGTfdgDM7PuGzgJDm4Vley05i",
            "https://drive.google.com/uc?export=view&id=1IKZPvTTLaXQqrCHGC48vNDzO5wdHNaOA",
            "https://drive.google.com/uc?export=view&id=1XqyM9uWET9sc_c4rSf5dhix1sHHjlKRq",
            "https://drive.google.com/uc?export=view&id=1P3QEOWfrKN4lA-vj2UwNd3_3zKffZET_",
            "https://drive.google.com/uc?export=view&id=1wL5QOsRBCPU6Z4--I3VqvGOEJeNeKD8G",
            "https://drive.google.com/uc?export=view&id=1jLE2Xc2i8XHKFoWAW2xkY2sp7O_FcqIp",
            "https://drive.google.com/uc?export=view&id=1OJjqhNzZnY8YQmCxl8P-ReWaoVZi8g8s",
            "https://drive.google.com/uc?export=view&id=12Mt7PyG85Fu81TI76M-oc3uw4prtAdjo",
            "https://drive.google.com/uc?export=view&id=1fkCIptLTazmIUMRUhImmh42mgbdwEgTT",
            "https://drive.google.com/uc?export=view&id=1eYVU6QhAFRzWaDUQPUT7pfa-rJ8S-qrl",
            "https://drive.google.com/uc?export=view&id=1nC1o58oidrLpfZIaLpMVdH-KRvlAYfsn",
            "https://drive.google.com/uc?export=view&id=1TkMy-VeLPUTO7IBirok_MZG4_K8QuRTC",
            "https://drive.google.com/uc?export=view&id=1XOq0ZZKYn-K53jRQuB33JaT3oYMmESoP",
            "https://drive.google.com/uc?export=view&id=1v1xze2wW36nEFNMOwmiYEzWQ4PnrJ6NS",
            "https://drive.google.com/uc?export=view&id=1Ytyg09eCmCfNRNRJj_O8xNTERwDFne82",
            "https://drive.google.com/uc?export=view&id=1NsRIa1TXsWFc82yvzrTlRpogtyzl1QO8",
            "https://drive.google.com/uc?export=view&id=166CsyfZLhrzjiLljJ_dsg5dcAwpnEMJM",
            "https://drive.google.com/uc?export=view&id=146Se-tf6K6arbt90epSphHkvbIW8UjDM",
            "https://drive.google.com/uc?export=view&id=1ygv83D64BRrQqpt2n-Z6x4062xVoF87B",
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
                "kesan": "kakak ini keren dan sangat baik",
                "pesan": "Semangat terus kuliah nya kak"
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
                "kesan": "Kakak ini baik dan cantik",
                "pesan": "Jangan lupa makan nasi kak"
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
                "kesan": "Kakak ini selalu ceria",
                "pesan": "Semanagat terus walaupun hidup tu berat kak"
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
                "kesan": "Abang ini santai dan asik banget orang nya",
                "pesan": "Semoga di lancarkan kuliah nya bang"
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
                "kesan": "Kakak ini asik banget",
                "pesan": "Tetap semangat ya kak"
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
                "kesan": "Abang ini orang nya ramah",
                "pesan": "Sukses terus bang"
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
                "kesan": "Abang ini selalu membawa kehangatan",
                "pesan": "Jangan lupa makan 3x sehari bang"
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
                "kesan": "Kakak ini baik dan keren",
                "pesan": "Semangat terus kuliah nya kak"
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
                "kesan": "Abang ini baik banget orang nya",
                "pesan": "Petahankan terus bang semangatnya"
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
                "kesan": "Ceria banget kakak ini tiap hari",
                "pesan": "Jangan lupa senyum tiap hari kak"
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
                "kesan": "Kakak ini orang nya asik banget ",
                "pesan": Jaga kesehatan nya kak"
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
                "kesan": "Kakak ini orang nya baik banget",
                "pesan": "Sukses terus kedepannya kak"
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
                "kesan": "Banyak hal yang saya pelajari sesudah mengenal abang ini",
                "pesan": "Jaga kesehatannya bang"
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
                "kesan": "Kakak ini baik hati dan tidak sombong",
                "pesan": "Jangan lupa makan nasi ya kak"
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
                "kesan": "Kakak ini slealu ceria dan cantik",
                "pesan": "Semangat kak untuk mennggapai cita cita nya"
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
                "kesan": "Kakak ini asik dan ramah banget",
                "pesan": "Semangat terus kak walaupun hidup ini sangat berat"
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
                "kesan": "Abang ini aisk banget dan humble",
                "pesan": "Semoga kuliah nya dilancarkan bang"
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
                "kesan": "Abang ini orang nya suka ketawa",
                "pesan": "Semoga segala hambatan hilang bang"
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
                "kesan": "ASik diajak ngobrol seru orang nya",
                "pesan": "Sehat selalu ya bang"
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
                "kesan": "Abang ini seru dan asik orangnya",
                "pesan": "Semangat terus bang walaupun hidup ini berat"
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
                "kesan": "Kakak ini keliatan ceria tiap hari",
                "pesan": "Senyum terus ya kak"
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
                "kesan": "Kakak ini ramah dan asik",
                "pesan": "Sukses terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 tahun",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Baca",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ari Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "21 tahun",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "sosmed": "@aayuandrianni_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Nemenin Bryan live TikTok",
                "sosmed": "@dafaelpriza_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 tahun",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lihat bulan",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 tahun",
                "asal": "Lampung Tengah",
                "alamat": "JI Pulau Damar",
                "hobbi": "Taptap layar kalo Bryan live",
                "sosmed": "@afdall.03",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nganterin Datasena ke gedung F",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Ngitungin kelopak bunga di kebun",
                "sosmed": "@andra.lhm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "22 tahun",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Ngegift live Bryan",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18 tahun",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 tahun",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

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
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@biyokcb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21 tahun",
                "asal": "Lampung",
                "alamat": "Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20 tahun",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19 tahun",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20 tahun",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@keyashafi_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "@_els.a",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20 tahun",
                "asal": "Kalianda",
                "alamat": "Kota Baru",
                "hobbi": "Main game, tidur",
                "sosmed": "@aruccy_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19 tahun",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "sosmed": "@apiszzaja_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Scroll",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20 tahun",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@Syaafiqui",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "28 tahun",
                "asal": "Kota bumi",
                "alamat": "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed": "@henryferdianto",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
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
                "kesan": "Kak Arienta baik, keren, peduli, dan humble bangetttt",  
                "pesan":"Semoga diberi kesuksesan dan kesehatan selalu ya kak!!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baik, berwibawa, dan disiplin banget",  
                "pesan":"Semoga selalu diberi kemudahan ya kakak!!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel Berwibawa, Asik dan jago banget sulap, baik, tegas, dan keren banget",  
                "pesan":"Semogaa sukses dan berkah selalu ya bang!!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, gentle, tegas, dan energik bangetttt",  
                "pesan":"Semoga selalu diberikan kesehatan dan kekuatan ya bang!!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake humoris, asik, humble dan baik bangetttt",  
                "pesan":"Semoga selalu sehatt, bahagia, dan lancar rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar Baik, keren dan imut, serta suka berbagi ilmu",  
                "pesan":"Semoga selalu diberikan kelancaran ya bang!!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah, tegas, keren, baik dan humble bangetttt",  
                "pesan":"Semoga selalu semangat dan bahagia ya kak!!!"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, tegas, asik, jago futsal, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan terhindar dari segala penyakit ya bang!!!"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri baik, lucu, imut, dan humble bangetttt",  
                "pesan":"Semoga selalu diberikan keselamatan dan kebahagiaan ya kak!!!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baik, ber aura, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat, bahagia dan diberi keselamatan ya kak!!!"# 1
            },            
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman baik, asik, humble, dan jago bangetttt deffense futsalnya",  
                "pesan":"Semoga selalu semangat dan sukses ya bang!!!"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel baik, kalem, dan humble bangetttt",  
                "pesan":"Semoga bahagia dimanapun kakak berada ya kak!!!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan bahagia ya kak!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jere humble, asik, kece, dan baik bangetttt",  
                "pesan":"Semoga selalu kuat dan sehat ya bang!!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu dilancarkan urusannya ya kak!!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli kece, rambutnya keren terus, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan doa nya diwujudkan ya bang!!!"# 1
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi baik, lucu, kalem dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan dilancarkan urusannya ya kak!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
