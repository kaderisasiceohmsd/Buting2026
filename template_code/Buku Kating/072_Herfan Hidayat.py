from io import BytesIO
from PIL import Image, ImageOps
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# Stylings Khusus: Kombinasi Krem Warm + Aksens Cokelat Tembaga
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Inter:wght@400;500;600&display=swap');

    /* Background Utama Krem Soft */
    .stApp {
        background-color: #f7f3eb !important;
        color: #2b2623;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar dengan Tampilan Clean */
    [data-testid="stSidebar"] {
        background-color: #ede6d5 !important;
        border-right: 1px solid rgba(140, 110, 75, 0.2);
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #2b2623 !important;
        font-weight: 500;
    }

    /* Judul Utama */
    .centered-title {
        text-align: center;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #3e3228;
        margin-top: 10px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)


# Bagian menu navigasi
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
            "container": {
                "padding": "6px!important",
                "background-color": "#ebdcc4",
                "border-radius": "12px",
            },
            "icon": {"color": "#3e3228", "font-size": "16px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "center",
                "margin": "3px",
                "border-radius": "8px",
                "color": "#3e3228",
                "--hover-color": "#dfcbab",
            },
            "nav-link-selected": {
                "background-color": "#8c6d46 !important",
                "color": "#ffffff !important",
                "font-weight": "600",
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
    # CSS Custom untuk Tampilan Kartu Foto & Biodata
    st.markdown(
        """
        <style>
        /* Tampilan Foto dengan Frame & Soft Shadow */
        [data-testid="stImage"] img {
            border-radius: 14px !important;
            border: 3px solid #ffffff;
            box-shadow: 0px 8px 20px rgba(62, 50, 40, 0.15);
            transition: transform 0.2s ease;
        }

        /* Kontainer Utama Gulungan */
        .scroll-wrapper {
            max-width: 420px;
            margin: 15px auto;
            position: relative;
            filter: drop-shadow(0px 6px 10px rgba(0, 0, 0, 0.2));
        }

        /* Roll Atas & Bawah */
        .scroll-roller {
            height: 22px;
            background: linear-gradient(90deg, #4a341e 0%, #7c5835 20%, #d4a76a 50%, #7c5835 80%, #4a341e 100%);
            border-radius: 11px;
            border: 1px solid #2b1d0f;
            box-shadow: inset 0 2px 4px rgba(255,255,255,0.3), inset 0 -2px 4px rgba(0,0,0,0.5);
            position: relative;
            z-index: 2;
        }

        /* Badan Kertas Kuno */
        .scroll-body {
            background: radial-gradient(circle, #fcf5e3 0%, #edd8a4 85%, #d9bd7e 100%);
            border-left: 2px dashed #9c7b45;
            border-right: 2px dashed #9c7b45;
            padding: 20px 24px;
            box-shadow: inset 0 0 18px rgba(115, 77, 20, 0.3);
            margin: -4px 10px;
            position: relative;
            z-index: 1;
        }

        /* Teks Biodata */
        .scroll-body p {
            color: #3b2712 !important;
            font-family: 'Georgia', serif;
            font-size: 0.93em;
            line-height: 1.5;
            margin-bottom: 6px;
            border-bottom: 1px dashed rgba(140, 90, 30, 0.2);
            padding-bottom: 4px;
        }

        .scroll-body p:last-child {
            border-bottom: none;
        }

        /* Merapikan Expander Streamlit */
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


menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1t6c7Jh2SU1ddMVOc1uEOUT9hWYmhgnEB",
            "https://drive.google.com/uc?export=view&id=1hHkU_Cj_57R9LMpFM4AQZwVTrk5zi3dn",
            "https://drive.google.com/uc?export=view&id=19mER4p7m4uxI0WJSGFWnWQDAWAGcmHi1",
            "https://drive.google.com/uc?export=view&id=1Lu_q3RS4-S8T-oSxfTSCb6RAr7-WAok0",
            "https://drive.google.com/uc?export=view&id=10Zig-hBqe6bSJIdWhwOf1uyINh5TcS_E",
            "https://drive.google.com/uc?export=view&id=1S9JxRyxkr5fuED4HvofHVAPpoKaU5Qsv",
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
                "kesan": "Bang Fajar orangnya ramah, baik, dan keren juga, the best lah pokoknya",
                "pesan": "Semoga ke depannya dapat terus berkembang menjadi lebih baik dan membawa HMSD ke arah yang lebih maju dan jadi orang yang sukses.",
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal": "Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren, baik, dan the best juga tentunya.",
                "pesan": "semangat terus bang, sukses dimanapun berada!",
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Kagum dengan kerja Kakak yang selalu rapi, teratur, dan sangat cekatan dalam mengurus administrasi.",
                "pesan": "Terima kasih sudah membagikan contoh kerja yang baik buat kami, Kak. Semoga dilancarkan urusan magang dan skripsinya",
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
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
            "https://drive.google.com/uc?export=view&id=1mEaTuk6PjtOp5DUMp6GyxLa8ZLGL9Oz_",
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
        gambar_urls =
