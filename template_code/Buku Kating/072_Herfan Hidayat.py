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
                "umur": "22 tahun",
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
                "umur": "22 tahun",
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
                "umur": "21 tahun",
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
                "umur": "22 tahun",
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
                "umur": "21 tahun",
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
                "umur": "20 tahun",
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
            "https://drive.google.com/uc?export=view&id=1Nm2vnOo1v9fqcdD0yZtKGPghp9okypWx", # Fathinah Nur Azizah
            "https://drive.google.com/uc?export=view&id=1ITE5ACHWnCn3c2T2BsKrwziB1cMe9n1k", # Helmy Surya Pratama
            "https://drive.google.com/uc?export=view&id=1hql9HuVrybkFHQz7bx-9JZVPumwqIXio", # Fernando Dimetrius Barus
            "https://drive.google.com/uc?export=view&id=1mEaTuk6PjtOp5DUMp6GyxLa8ZLGL9Oz_", # Suci Aulia
            "https://drive.google.com/uc?export=view&id=1cK8zeMxgDwjvNUcuDV84IOvYNeAS6Vxq", # Wielman Itolo Halawa
            "https://drive.google.com/uc?export=view&id=1Vr0dKVQk3_T-nT37KwEw41vQj7x0z_Jt", # Lia Hana Ichisasmita
            "https://drive.google.com/uc?export=view&id=1xAEdV5Iqbsy-obR8GMKokWwWmS0LjPuI", # Aqila Zayyan SalsabiL
            "https://drive.google.com/uc?export=view&id=1GYVN_kwyqCKx_h-RNttLVWiwkTKZ1y98", # Hazel Mahesa Handhaka
            "https://drive.google.com/uc?export=view&id=17A6KaycBMlQXQHMaJrr1fIdJy-goXG2V", # Nadya Ratu Anjani
            "https://drive.google.com/uc?export=view&id=141ytkz-wHu7qfjirse2SqjTMnM4kvT2L", # Dwi Rahma Fitriani
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21 tahun",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Orangnya sangat berwibawa, bijak, dan enak diajak berdiskusi tentang organisasi.",
                "pesan": "Semoga makin sukses dan tetap menjadi inspirasi buat teman-teman!",
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 tahun",
                "asal": "Jakarta ",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Keren, asik, dan pintar menghidupkan suasana pas kumpul biro.",
                "pesan": "Sukses terus kinerjanya dan semangat kuliahnya bang!",
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 tahun",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Anaknya santai tapi cekatan kalau dikasih tanggung jawab.",
                "pesan": "Semangat terus kuliah dan main badmintonnya!",
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 tahun",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Ramah banget, selalu senyum kalau ketemu di kampus.",
                "pesan": "Jangan pernah lelah belajar dan sukses selalu ya!",
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20 tahun",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Orangnya seru, asik diajak obrol ringan maupun serius.",
                "pesan": "Tetep jadi orang yang rendah hati dan semangat terus!",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Cerdas, tegas, dan punya pemikiran kritis yang luar biasa.",
                "pesan": "Semoga semua target dan urusan perkuliahan berjalan lancar!",
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Anaknya rajin, teliti, dan cepat paham kalau belajar hal baru.",
                "pesan": "Pertahankan semangat belajarnya, sukses terus!",
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20 tahun",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Humoris, unik, dan selalu bikin suasana jadi cair.",
                "pesan": "Semangat terus jalani hari-hari kuliahnya!",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Sangat rapi, tertata, dan tenang pas ngerjain tugas organisasi.",
                "pesan": "Tetep semangat dan jangan lupa istirahat di tengah kesibukan!",
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19 tahun",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Baik, kalem, dan sangat membantu kawan-kawan sekalian.",
                "pesan": "Semoga makin lancar kuliahnya dan tercapai harapannya!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Senator()

elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DOydiZ_GDHdUxSEKx6nF95KV7FJf9j3C",
            "https://drive.google.com/uc?export=view&id=1KgXtyOoGqfNfPTM03YyMI5ZQWD-n0L_z",
            "https://drive.google.com/uc?export=view&id=12s4vWNuhvOVucU-hDqU-D1t7TkLQIKib",
            "https://drive.google.com/uc?export=view&id=1qmqn1yar_Jvj6vS4-1d9hEg-fMXF4YrM",
            "https://drive.google.com/uc?export=view&id=1hzlr1JvrYwYqj5Ri3nzSsOEGrgD6d7P6",
            "https://drive.google.com/uc?export=view&id=1jdqYo-rOC15W8PJtDPOIb_g3ZffVq8Yv",
            "https://drive.google.com/uc?export=view&id=1I8XqpgbGR4yJEFKjA0Ticn2DIeZQLvJn",
            "https://drive.google.com/uc?export=view&id=1rLFOo6tGyGzngM8zwzs8csKLn2OWj39r",
            "https://drive.google.com/uc?export=view&id=1vOngLaiAqxr9L6JmOzeJ_N8ctLNl4FWh",
            "https://drive.google.com/uc?export=view&id=1VmZdcBYh7B4cjGnKLHzy_kOiuiAc2uQ8",
            "https://drive.google.com/uc?export=view&id=1_z8pfPQ3hgfbDKuZFmc9888g2cuiLNp7",
            "https://drive.google.com/uc?export=view&id=1T6MZW9EFq_y9v1wTMlmuDGzAJIU9EsTl",
            "https://drive.google.com/uc?export=view&id=12kuxocRlYvk_ZFH6EHRUtZIHIY9YGS_E",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450066",
                "umur": "20 tahun",
                "asal": "Kuala Lumpur",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya keren, ramah, pengayom, dan bijaksana",
                "pesan": "Semoga bang Ridho sehat dan sukses selalu, sukses buat kuliahnya bang, semoga lancar luncur. ",
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19 tahun",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnya baik, ramah, murah senyum dan orangnya berdedikasi dan bertanggung jawab, keren deh pokoknya.",
                "pesan": "Tetaplah menjadi sosok pengayom yang ceria dan sabar, Kak. Sukses selalu untuk kuliahnya dan semangat terus!",
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19 tahun",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "Bang Dharu orangnya keren banget sih, pinter, baik, Mapres juga.",
                "pesan": "Semangat terus dan sehat selalu bang, semoga bisa menjadi teladan atau contoh yang baik untuk adik tingkatnya ya bang.",
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20 tahun",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko orangnya baik, asik, ramah.",
                "pesan": "Sehat selalu dan sukses selalu bang Niko",
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19 tahun",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakak ini orangnya baik dan ramah.",
                "pesan": "Semangat dan sukses selalu dimanapun berada kak.",
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21 tahun",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20 tahun",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20 tahun",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20 tahun",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21 tahun",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20 tahun",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20 tahun",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik, baik, dan ramah.",
                "pesan": "Jadilah orang yang selalu ceria kak, sehat dan sukses selalu dimanapun berada.",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Baleg()
elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JZCUC7s2g_iDZhX_38lKET5d0_5Ov2Ou",
            "https://drive.google.com/uc?export=view&id=1Ba-iWTxdRqje0PSNG-_mq-ERMsCF9lKm",
            "https://drive.google.com/uc?export=view&id=1xGuXBcABW0BzV2fdSI8uMyzrOinlG_HQ",
            "https://drive.google.com/uc?export=view&id=17XSxzb9Hn2uQAcyG-cwwaE-gPtsIOwtH",
            "https://drive.google.com/uc?export=view&id=1If--XH0RrX3VeuftO3FySqb2WLkC_G67",
            "https://drive.google.com/uc?export=view&id=1PN-s2mhfa61JgpnD4KIG5MVtD3cNqf-p",
            "https://drive.google.com/uc?export=view&id=1FOawy98J1xQRQF-OVJhf0UAXgJChQgOH",
            "https://drive.google.com/uc?export=view&id=1HVtBDHCDHGOiwHr_6Kz9m-BS_-r49Uuc",
            "https://drive.google.com/uc?export=view&id=1U6BQ5VHy4upzRi1tGY2uXI_fWXgM99OJ",
            "https://drive.google.com/uc?export=view&id=1Mw5X_urhC3VRiOgknD3briSDwCd0lySe",
            "https://drive.google.com/uc?export=view&id=1y66p3M4w93HABwUN5hZrUQAaNhlcpeWm",
            "https://drive.google.com/uc?export=view&id=1Ed9KpgQpvj0DqhiFrx9FK6MMjzbR-0qs",
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
                "kesan": "Bang Ihsan jujur orangnya asik, ramah, baik juga.",
                "pesan": "Semangat terus kuliahnya bang, semoga sukses!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah ",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube ",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_SSD()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iFiZmE4DsfdItk58uq8stE0GAoLezQy3", #Kadep
            "https://drive.google.com/uc?export=view&id=1fHX_8-y2Nr1GJBSjKPTymBDMvLylltWR", #Sekdep
            "https://drive.google.com/uc?export=view&id=1bcpDrlyVZdqLM2_P_sBaDcBDzxLiXraE", #Kadiv Keharmonisasian
            "https://drive.google.com/uc?export=view&id=1BZnHAvygnZbPCrfIl4JuReMHr33ITfcw",
            "https://drive.google.com/uc?export=view&id=1nV2FlmKe5yI0Okts0v_zqwnh-zDl24wa",
            "https://drive.google.com/uc?export=view&id=1RpNOu1XU-xXDLuonBPXZnSwsha3ClV-z",
            "https://drive.google.com/uc?export=view&id=1dDR0E3eBQvit-Xu2-kohFuD11mdDkW8r",
            "https://drive.google.com/uc?export=view&id=1v7JivDA6cEWF2Nz14vntt7LLAkPNNWgN",
            "https://drive.google.com/uc?export=view&id=1At62vJ12fRts1zyqurdx27o2SrmFPAnj",
            "https://drive.google.com/uc?export=view&id=1s5ZS9Yqm6xNni-8ZxnjIXHrLM2UVoT-1",
            "https://drive.google.com/uc?export=view&id=1nynURXRuNeEohiQiG0NAXJHeKBa5ULs4", #Kadiv Kerohanian
            "https://drive.google.com/uc?export=view&id=1gS6QL2kthDgK076NIykSnHJ8y3wqcNkB",
            "https://drive.google.com/uc?export=view&id=1kwPz-oDXGQtlBO3d1xegC8b_u_n30sPB",
            "https://drive.google.com/uc?export=view&id=1sBsGWepLArkKc2yV90T8qZEqdg3X4AY0",
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
                "kesan": "Bang Haikal adalah sosok yang hangat, merangkul, dan peduli dalam menjaga keharmonisan serta hubungan di internal Himpunan",
                "pesan": "Semoga sukses selalu, baik dalam akademik maupun organisasinya.",
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma orangnya baik, ramah, murah senyum",
                "pesan": "Semangat terus dan lancar luncur segala urusannya kak",
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna ini orangnya ramah banget, baik, murah senyum lagi",
                "pesan": "Semangat terus, dan menyala selalu kak!!!",
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren, baik, ramah dan bisa mainin semua alat di DAMASKUS",
                "pesan": "Sehat selalu dan lancar lucur bang buat semuanya!!!",
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kak Aisyah orangnya baik, asik, dan ramah. Pembawaannya juga nyaman.",
                "pesan": "Semoga selalu dikelilingi orang-orang baik dan ketemu banyak hal seru ke depannya !!!"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Cerine orangnya baik dan ramah",
                "pesan": "Semoga semua yang lagi diperjuangin berjalan lancar dan selalu bahagia!"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Bang Jaya orangnya baik, ramah, dan asik.",
                "pesan": "Semoga semua urusan ke depannya lancar !!!"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla imut, lucu, cantik, dan baik banget",
                "pesan": "Semoga selalu ketemu hal-hal baik dan orang-orang baik juga.!"
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Bang Rozaq orangnya baik dan ramah.",
                "pesan": "Semoga kuliah dan semua kesibukannya dilancarkan. Sukses terus ya, Bang!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa orangnya asik dan baik juga.",
                "pesan": "Semoga lancar dan sukses terus urusan perkuliahan dan semuanya kak!"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Hanif orangnya baik. Kiper andalan Futsal Sains Data yang gacor juga",
                "pesan": " Semoga selalu diberi kelancaran untuk semua urusannya bang.!"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": " Kak Audina orangnya baik dan ramah.",
                "pesan": "Semoga semuanya lancar dan makin banyak hal keren yang bisa kakak capai nantinya. Sukses terus ya, Kak!"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Kak Cika orangnya baik dan asik orangnya keliatannya",
                "pesan": "Semoga semua urusannya dipermudah dan kuliahnya lanca!"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin orangnya baik, cantik, dan ramah.",
                "pesan": "Semoga selalu bertemu orang baik dimanapun kakak berada ya kak.!"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Bang Harvin orangnya asik, dan baik",
                "pesan": "Semoga kuliah dan semua kesibukannya serta apa yang ingin di gapai bisa tercapai!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kak Rafa orangnya baik, ramah, dan asik.",
                "pesan": "Semoga segala urusan kakak di permudah dan jalan menuju kesuksesan lancar luncur!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ieYUKILQuldBPH3ROIkOTufe85dmB-bI", #Kadep
            "https://drive.google.com/uc?export=view&id=1v8-7T4SUcyHCY-ScN4uY9iugwgM7aKF8", #Sekdep
            "https://drive.google.com/uc?export=view&id=1_7qUg1BZmYcbOMvhAVbkupG0pcP2Va-X", #Kadiv Dokumentasi
            "https://drive.google.com/uc?export=view&id=1vTbvqW-YUOlQKGoG48ibnim2V52Qc17_",
            "https://drive.google.com/uc?export=view&id=1jOKJcw8a0uFzNaHUJC9mEIBNA0THoYcf",
            "https://drive.google.com/uc?export=view&id=1h9U4Q_NP3LV0kZQieP_Y0Fgv25MFQnQE",
            "https://drive.google.com/uc?export=view&id=1qpSTZwXut6eyqN6_RuSyGYZcSAmMreg6", #Kadiv Media dan konten sepasialis
            "https://drive.google.com/uc?export=view&id=1XNc6WCcCz43Kfc-PBu0FtqfUgGMc_YUZ",
            "https://drive.google.com/uc?export=view&id=1QhWaD-w38piIk4qJs9CfTUNQMsnUcMht",
            "https://drive.google.com/uc?export=view&id=17b3kWEV-bWXcsgpRn8jPoIA5-A9-TAgz",
            "https://drive.google.com/uc?export=view&id=1T4a1vIbzbW2DmeWWagYc6CCFVbKJzPk0",
            "https://drive.google.com/uc?export=view&id=1HJ30nQSvTkQatbQXJfyU44floDNPOdQF",
            "https://drive.google.com/uc?export=view&id=1mvH_h8_Wpm3kIHPsnCwoHZTNbshzzFkb",
            "https://drive.google.com/uc?export=view&id=1WGIar8vH9kVa5SlkQbuOUEI5yqHkiyI2",
            "https://drive.google.com/uc?export=view&id=1qjfUfcFPranvKFHcfIP6WkXwWx9gATKS",
            "https://drive.google.com/uc?export=view&id=1iTXClCqLfHpJHYcIDFZkdA_Mvm6A726u",
            "https://drive.google.com/uc?export=view&id=1gviUgunFGSkTbOZzLzBI5oqf3YveHBCx",
            "https://drive.google.com/uc?export=view&id=1phXsotDUFBlF8FLParX3ifRwn2z_Dd5o",
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
                "kesan": "Kak Nayla orangnya asik, baik, dan ramah",  
                "pesan":"Semangat terus kuliahnya dan lancar luncur semuanya!!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {    
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@Melukis & Menulis",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf() 

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QNbBI3wq2u57eT-EUQjaH7fVYufl6SyB", #Kadep
            "https://drive.google.com/uc?export=view&id=1QD94ReVx_h1cF-yOWESLaSw86cjdBVYR", #Sekdep
            "https://drive.google.com/uc?export=view&id=1Yezent1t6qtP-msXZLZZFABFHalaob53", #Kadiv Hublu
            "https://drive.google.com/uc?export=view&id=1aHy6IJ1aKJkxtinDv-p_sTqs2oEiaXz-", #Kadiv Pengmas
            "https://drive.google.com/uc?export=view&id=1MDH5oAFlqZd-1Mir4YDfjy1sY6mbtUCb",
            "https://drive.google.com/uc?export=view&id=1DNJXKJ_Isxvxn66YfsZ3lqw8wM7kHcEn",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1i_K47XAuPetCeo_0s9yduBQBWcVJT96g",
            "https://drive.google.com/uc?export=view&id=1kctj9csAeGcVTUFxqrfP_GvWGqKrD6Bb",
            "https://drive.google.com/uc?export=view&id=1XOLF_ZNTBwQeLoxDJGqaXA3UQOk7GJ7p",
            "https://drive.google.com/uc?export=view&id=1g_kfbK0NYpYkbJW5lxF59N25Ghgu6IE1",
            "https://drive.google.com/uc?export=view&id=1_3E5Lvy9D0C9A4ywbFLONaXm-rvZf7Yv",
            "https://drive.google.com/uc?export=view&id=1ZPHkBdJorDm2JNxsrv7TlfedP1biIdps",
            "https://drive.google.com/uc?export=view&id=1M_vPpRCzeCt-BoQyiQP2kt7VlClmmih3",
            "https://drive.google.com/uc?export=view&id=12w88PDvXH2gacwEQnOdFbF-jVyg6Dzkc",
            "https://drive.google.com/uc?export=view&id=1J3DYWIlEpD6b04ts6WnvW7rd9eJCAOf1",
            "https://drive.google.com/uc?export=view&id=1CRnbO4_BGjwS73rd84ajX_A1ACySRFCx",
            "https://drive.google.com/uc?export=view&id=12JG6RT1yMueGrIdYOP01CWQ-xGdW5601",
            "https://drive.google.com/uc?export=view&id=1MRkhNjfDjdbNluYgCtvoLXeGHzN8Qce3",
            "https://drive.google.com/uc?export=view&id=1V_cXzGOYQBAVfZA2v2mJGSeRW49IhVOb",
            "https://drive.google.com/uc?export=view&id=1FPLMqD5KwGKTQ5yIEJhhJjLdS35fR4_m",
            "https://drive.google.com/uc?export=view&id=1XgZH_AsL9xgZmt1hzNfsTMWPsAVNRlJ3",
        ]
        data_list = [   
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "hobbi": "Nonton Kartun",
                "umur": "-",
                "tanggal_lahir": "06 Maret 2005",
                "alamat": "Teluk Betung Selatan",
                "asal": "LAMPUNG!!!",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini orangnya asik dan tegas",
                "pesan": "Sehat selalu kak, semoga segala urusannya lancar"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "hobbi": "Jalan - Jalan",
                "umur": "20 Tahun",
                "tanggal_lahir": "5 November 2005",
                "alamat": "Jalan Lapas",
                "asal": "Bengkulu",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla orangnya asik dan baik, dan sama-sama dari Bengkulu kayak saya",
                "pesan": "Doa terbaik kak, semoga yang kakak usahakan selalu berbuah kebaikan nantinya"
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "hobbi": "main",
                "umur": "-",
                "tanggal_lahir": "27 Januari 2005",
                "alamat": "Airan",
                "asal": "Lambar",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kak Moonlight nama ini dapat dari tiktoknya, orangnya asik dan baik",
                "pesan": "Sehat selalu kak, semoga segala urusan, terutama kuliahnya berjalan dengan baik dan lancar "
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "hobbi": "ga ngapa ngapain",
                "umur": "21 Tahun ini alhamdulillah",
                "tanggal_lahir": "16 Agustus 2005",
                "alamat": "GH",
                "asal": "Tangerang Selatan",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang Ahmad orangnya keren jujur, dri masa saya TPB saya tau bang ahmad pada saat beliau naik jadi capresma keren banget sih asli",
                "pesan": "Sehat selalu dan menyala selalu ya bang, tebarkan kebaikan dimanapun berada"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "hobbi": "jadi idol",
                "umur": "cepuyuh tayun",
                "tanggal_lahir": "21 Desember 2005",
                "alamat": "love earth",
                "asal": "ikut kadep",
                "sosmed": "@adindaadma",
                "kesan": "Kak Adinda orangnya baik, cantik, ramah juga",
                "pesan": "Semoga apa yang kakak usahakan nantinya bisa kakak capai"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "hobbi": "lihat lihat perumahan",
                "umur": "-",
                "tanggal_lahir": "23 Juli 2006",
                "alamat": "Balam",
                "asal": "Tanggamus",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang Bimo orangnya keren kelihatan dari tampilannya, gacor bang",
                "pesan": "Semoga selalu sehat dan semangat dalam menjalani semuanya bang"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "hobbi": "makan yang manis biar manis",
                "umur": "nelson piquet",
                "tanggal_lahir": "-",
                "alamat": "balam",
                "asal": "balam",
                "sosmed": "@alfabiyi",
                "kesan": "Bang Alfayya orangnya asik, baik, keren juga",
                "pesan": "Sehat selalu dan lancar luncur kuliah serta karirnya bang"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "hobbi": "menonton film",
                "umur": "20 tahun",
                "tanggal_lahir": "21 Mei 2006",
                "alamat": "Korpri Raya",
                "asal": "Lampung Barat",
                "sosmed": "@asrmeilani",
                "kesan": "Kak Asri Meilani orangnya baik dan ramah",
                "pesan": "Sehat selalu, semangat dan menyala selalu kak"
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "hobbi": "berlaku humoris dan manis",
                "umur": "-",
                "tanggal_lahir": "25 April 2006",
                "alamat": "Balam",
                "asal": "Lampung",
                "sosmed": "@bimayasa_",
                "kesan": "Bang Bima keren dan baik",
                "pesan": "Menyalalah tanpa membuat redup yang lain"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "umur": "20 Tahun",
                "tanggal_lahir": "14 Agustus 2006",
                "alamat": "Disini aja",
                "asal": "Ampera",
                "sosmed": "@khaindaa_",
                "kesan": "Kak Indah orangnya baik, ramah, dan keliatannya asik orangnya",
                "pesan": "Semangat selalu ya kak, lancar untuk semuanya"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "hobbi": "ngefollow up chat",
                "umur": "20 tahun",
                "tanggal_lahir": "15 Juni 2006",
                "alamat": "bebas",
                "asal": "palembang",
                "sosmed": "@erlsriska",
                "kesan": "Kak Riska orangnya pastinya baik, ramah juga",
                "pesan": "Sehat selalu kak gapai semua yang kakak impikan"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "hobbi": "Ikut kepanitiaan",
                "umur": "-",
                "tanggal_lahir": "-",
                "alamat": "Jati Agung",
                "asal": "Kerangka Bawang Sebelah Barat",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak Yollanda orangnya asik, baik, dan ramah dan enak di ajak ngobrol",
                "pesan": "Lakukan lah yang terbaik dan capailah semua dengan penuh keyakinan"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "hobbi": "memancing keributan",
                "umur": "15 Tahun",
                "tanggal_lahir": "15 September 2004",
                "alamat": "belwis",
                "asal": "tetangga kadep",
                "sosmed": "@adityatfq",
                "kesan": "Bang Adit orangnya super ramah dan asik sih",
                "pesan": "Sehat selalu ya bang, semoga semua jalan di permudah untuk menggapai kesuksesan"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "hobbi": "baca wattpad",
                "umur": "25 tahun",
                "tanggal_lahir": "-",
                "alamat": "Sukarame",
                "asal": "Tangsel",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak ini baik, ramah, dan soft spoken sepertinya",
                "pesan": "Sehat selalu kak, semoga sukses!!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "hobbi": "Jadi orang baik",
                "umur": "-",
                "tanggal_lahir": "25",
                "alamat": "Gerbar",
                "asal": "Luhak tanah data",
                "sosmed": "-",
                "kesan": "Kakak ini keren, asprak ADS saya juga, baik dan ramah orangnya",
                "pesan": "Sehat selalu kak, semoga lancar luncur kuliahnya dan lulus sesuai target serta jadi orang sukses"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "hobbi": "tidur",
                "umur": "20 tahun",
                "tanggal_lahir": "28 Mei 2006",
                "alamat": "jauh pokoknya",
                "asal": "sini",
                "sosmed": "@kshigf",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "hobbi": "Ngasih makan ikan cupang",
                "umur": "-",
                "tanggal_lahir": "31 Desember 2006",
                "alamat": "Belakang Polda",
                "asal": "Karawang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang Daniel keren sihh, Duta Genre lagi, gacor bang!",
                "pesan": "Semoga Impian dan cita-cita bang Danil dapat tercapai"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "hobbi": "ngesen kanan",
                "umur": "-",
                "tanggal_lahir": "05 Mei 2006",
                "alamat": "Way Halim",
                "asal": "Swiss",
                "sosmed": "@fvnnn05",
                "kesan": "Bang Favian orangnya baik dan ramah",
                "pesan": "Lancar luncur semua urusannya bang"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "hobbi": "nyari hobi",
                "umur": "20 tahun",
                "tanggal_lahir": "666",
                "alamat": "Jati Agung",
                "asal": "situlah",
                "sosmed": "@zydddddd_",
                "kesan": "Bang Yazid orangnya baik, keren juga",
                "pesan": "Semoga apa yang abang usahakan berbuah hasil yang terbaik ya bang"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "hobbi": "Mainin ikan cupang",
                "umur": "Masih muda lah",
                "tanggal_lahir": "Hari Jum'at",
                "alamat": "Pasar lantai 3.5",
                "asal": "Rahim Ibu",
                "sosmed": "@jaldii._",
                "kesan": "Bang Jaldi orangnya ramah dan asik banget",
                "pesan": "Sehat selalu dan Menyala selalu ya bang Jaldi1"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "hobbi": "nonton thinkerbell",
                "umur": "20 tahun",
                "tanggal_lahir": "18 November 2026",
                "alamat": "Pinggir Jalan",
                "asal": "Banyak Begal",
                "sosmed": "@snova.19",
                "kesan": "Baik hati, ramah banget kalau disapa, dan orangnya selalu kelihatan ceria.",
                "pesan": "Jaga kesehatan selalu, tetep semangat belajarnya, dan jangan lupa istirahat ya!"
              },
              {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "hobbi": "jalan-jalan",
                "umur": "20 tahun",
                "tanggal_lahir": "03 Juni 2006",
                "alamat": "balam",
                "asal": "lampung",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Orangnya asik, seru kalau diajak ngobrol, dan pembawaannya santai.",
                "pesan": "Semoga semua harapan serta rencana kuliahnya berjalan lancar, sukses terus!"
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A-lkY5LQ_7wVCmtOqlZu_7Gah4Y4Dgvk", #Kadep
            "https://drive.google.com/uc?export=view&id=1ErcMHuA7YkkjZ-mv5xUyvJE6TxEO5iBd", #Sekdep
            "https://drive.google.com/uc?export=view&id=1UJLxbzvhUhhU2cF9D2djEro_0oZo7yfF", #Kadiv PSD
            "https://drive.google.com/uc?export=view&id=1Ycec5XGf4190DMeP_mVYfes3PI-MuWRr",
            "https://drive.google.com/uc?export=view&id=1irnJ0vBLbu8O5lcgBJqSuX8PaQebUhVh",
            "https://drive.google.com/uc?export=view&id=1JugpsqzHvKQsd7YD2qejlMtw7wYairJC",
            "https://drive.google.com/uc?export=view&id=1m7wib6JyfvdQfBrFWcqmZ2U4iJvPvPfk",
            "https://drive.google.com/uc?export=view&id=1xZqkLW31S_C7q8KCDoo8kjugHRauwYVu",
            "https://drive.google.com/uc?export=view&id=1kUdP_BJHLxirXvr0svJ74Nj95YOkKPfk", #Kadiv PIKA
            "https://drive.google.com/uc?export=view&id=1V2N1qAU6BXMdgELYmd-l5WteR8toOs_b",
            "https://drive.google.com/uc?export=view&id=1_oYWmDC6xDV39EJ7FfmTNR3cEk8mt8fa",
            "https://drive.google.com/uc?export=view&id=1Hj9eQFRz6MXQe2ZcszWs-HwzBYVG_8Fh",
            "https://drive.google.com/uc?export=view&id=1EwmPNdm2YVN8e2r8zWEzrZqbT7ng20g2",
            "https://drive.google.com/uc?export=view&id=1upBbAcdeDxb9RXdLMygsqcKZPiSbdQ7f",
            "https://drive.google.com/uc?export=view&id=13smbxfJXeMnkI0zcu2N99zNevN9Rt4hZ", #Kadiv RND
            "https://drive.google.com/uc?export=view&id=1errsAK-RkfaiVhp4XHrHLJysjBxSyk7t",
            "https://drive.google.com/uc?export=view&id=1v5NZgO8I3IUDpaLu4BoBaJcPkXW_E-yM",
            "https://drive.google.com/uc?export=view&id=1DKDaU9GpD25fSU8KpAgfa7rlW4mBEP4X",
            "https://drive.google.com/uc?export=view&id=1rwLilYAHFqHP7vlLT0xbwZ5-d4-B-z7Q",
            "https://drive.google.com/uc?export=view&id=1dT_nWSUSbVNSDazrel-rLv9A3xXLu_Yw",
            "https://drive.google.com/uc?export=view&id=1ctefV1o6ONFV05aP9fwZjTFctjmoS4l0",
            "https://drive.google.com/uc?export=view&id=1bpDGkVlzwvBgJcKcHBN7lq3JGxT4EqwF",
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
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XQcEhPXFw5ofIpf274xiTFlwLEsBMo2L", #Kadep PSDA
            "https://drive.google.com/uc?export=view&id=1gtmWwIeZmijt0dINHOgV0qMvmbS9RQaO", #Sekdep PSDA
            "https://drive.google.com/uc?export=view&id=1hjCN-T4IS_anHJNpoaN9stxQlj5iOIjc", #Kadiv Kader
            "https://drive.google.com/uc?export=view&id=1bWxYfqEf8BUmPyL2p0pG2ZTP06V-EMCU",
            "https://drive.google.com/uc?export=view&id=1o-K6LtC2EUsAq9T7KElCcj4kAHAQVqHC",
            "https://drive.google.com/uc?export=view&id=14HsrddSAMU5HX4y-pldfuO97TF230RZL",
            "https://drive.google.com/uc?export=view&id=1aghvxjvOO6MbyHKCAp9YDnjqeu1ULNYA",
            "https://drive.google.com/uc?export=view&id=1e7ZHKC5RAFSLNHI9Tb79peW4fkr7VTkG",
            "https://drive.google.com/uc?export=view&id=1jxiQaqcjDH7_narfy_M3KL_PXAd0Vhfs",
            "https://drive.google.com/uc?export=view&id=1vxR1VGcJFU39Ctr19r92AhSugX0XRJFw",
            "https://drive.google.com/uc?export=view&id=10MQ5Yn7m3b4q-jpZdTQF2-V0KKOEDL0i", #Kadiv PMA
            "https://drive.google.com/uc?export=view&id=1Wr9ygvyqHPfuj6q3XRW5NGxptS9HdxGf",
            "https://drive.google.com/uc?export=view&id=10Wx0BGyLOL1hTgvU5AC1fn9S2gBAdFG5",
            "https://drive.google.com/uc?export=view&id=1aPuLie-3xU9sQHNS39p1uul1ThFuIePz",
            "https://drive.google.com/uc?export=view&id=1YHTcNvndW-x7TWMKh2wKGAaufgTOIQnC",
            "https://drive.google.com/uc?export=view&id=14m7YR5UO8q4E6WrTMs7LNcbAzGuwmzyD",
            "https://drive.google.com/uc?export=view&id=132IUlpLlah3CWl4B4-RqdkG2lpl2qTyf",
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
                "kesan": "Kak Arienta baik, keren, peduli, pemandu lagi",  
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
                "kesan": "Kak Vany baik, berwibawa, dan keren",  
                "pesan":"Semoga selalu diberi kemudahan dan semangat selalu kak!!!"# 1
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
                "kesan": "Bang Azmi keren, gentle, tegas, dan  menyala",  
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
                "kesan": "Bang Ayake orangnya asik, keren, dan role model saya yang gacor",  
                "pesan":"Semoga selalu sehat, bahagia, dan lancar rezeki dan kuliahnya ya bang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar Baik, keren, tegas dan mantap pol lah pokoknya, jiwa-jiwa korlap membara",  
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
                "kesan": "Kak Yudia ramah, cantik, tegas, keren, baik dan sedari jadi komdis pplk udah gacor sih",  
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
                "kesan": "Bang Haikal baik, tegas, jago futsal, dan keren sih aslii ",  
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
                "kesan": "Kak Putri baik, cantik, tegas, keren deh pokoknya!",  
                "pesan":"Semoga selalu diberikan keselamatan dan kebahagiaan serta lancar kuliahnya kak!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baik, cantik, manis orangnya, dan keren sih asli!",  
                "pesan":"Semoga sehat selalu dan menyala selalu kak, dan tetaplah jadi orang yang selalu menyala!!!"# 1
            },            
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman baik, asik, humble, dan ketangnya DATANOVAS yang menyala",  
                "pesan":"Semoga sukses dan segala yang di cita-citakan dapat tercapai bang!!!"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel baik, kalem, dan ramah juga orangnya",  
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
                "kesan": "Kak Charrlindah baik, santai, dan keren kak",  
                "pesan":"Semoga sehat selalu dan kebahagiaan selalu menyertai kak!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar humble, asik, kece, dan calon capo damaskus yang menyala",  
                "pesan":"Semoga selalu kuat dan dapat mecapai cita-citanya ya bang!!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik, santai, dan asik",  
                "pesan":"Semoga selalu dilancarkan dan dimudahkan urusannya ya kak!!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli kece dan keren orangnya",  
                "pesan":"Semoga selalu sehat dan apa yang diusahakan dapat tercapai bang!!!"# 1
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi orangnya, lucu, kalem dan baik",  
                "pesan":"Semoga selalu sehat dan dimanapun berada selalu bertemu dengan yang baik-baik!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
