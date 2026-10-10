import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background-color: #701c23 !important;
    }
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] div, 
    [data-testid="stSidebar"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }
    .centered-title {
        text-align: center;
        color: #701c23;
        font-weight: 800;
        margin-bottom: 25px;
    }
    .profile-card {
        background-color: #ffffff;
        padding: 22px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        border-left: 5px solid #701c23;
        margin-bottom: 20px;
    }
    .profile-header {
        font-size: 20px;
        font-weight: bold;
        color: #701c23;
        margin-bottom: 10px;
        border-bottom: 1px solid #eee;
        padding-bottom: 6px;
    }
    .info-label {
        font-weight: 600;
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

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
            "people-fill", "people-fill", "people-fill", 
            "people-fill", "people-fill", "people-fill", 
            "people-fill", "people-fill", "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "5px!important", "background-color": "#ffffff", "border-radius": "10px", "box-shadow": "0 2px 8px rgba(0,0,0,0.05)"},
            "icon": {"color": "#701c23", "font-size": "15px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "center",
                "margin": "2px",
                "padding": "8px 12px",
                "--hover-color": "#f4f0eb",
            },
            "nav-link-selected": {"background-color": "#701c23", "color": "#ffffff"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception:
        return None

def get_cached_images(gambar_urls):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            images.append(img)
    return images

def display_images_with_data(gambar_urls, data_list):
    images = get_cached_images(gambar_urls)

    for i, img in enumerate(images):
        if i < len(data_list):
            col1, col2 = st.columns([1, 2], gap="medium")
            with col1:
                if img is not None:
                    st.image(img, use_container_width=True)
                else:
                    st.warning("Gagal memuat gambar.")
            with col2:
                st.markdown(f"""
                    <div class='profile-card'>
                        <div class='profile-header'>{data_list[i]['nama']}</div>
                        <p><span class='info-label'>NIM:</span> {data_list[i]['nim']}</p>
                        <p><span class='info-label'>Umur:</span> {data_list[i]['umur']} Tahun</p>
                        <p><span class='info-label'>Asal:</span> {data_list[i]['asal']}</p>
                        <p><span class='info-label'>Alamat:</span> {data_list[i]['alamat']}</p>
                        <p><span class='info-label'>Hobbi:</span> {data_list[i]['hobbi']}</p>
                        <p><span class='info-label'>Sosial Media:</span> {data_list[i]['sosmed']}</p>
                        <p><span class='info-label'>Kesan:</span> {data_list[i]['kesan']}</p>
                        <p><span class='info-label'>Pesan:</span> {data_list[i]['pesan']}</p>
                    </div>
                """, unsafe_allow_html=True)
            st.write("---")
            
    st.success("Semua data berhasil dimuat!")

menu = streamlit_menu()

if menu == "Kesekjenan":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=12cWhixrwVc5uEATnocwRJHw5nhRFxCHv",
        "https://drive.google.com/uc?export=view&id=1sv9FBDEIaKNUNrIBN4OJTc6Ovk85jgVP",
         "https://drive.google.com/uc?export=view&id=1uLNAVgSX8A7F_n7IMQBu6KknNouVoF8d",
                "https://drive.google.com/uc?export=view&id=18Bm8mmUYqE7daRUSPf4xEB5JWTY8YEyt",
                "https://drive.google.com/uc?export=view&id=1mMMKw-5pKfFuazXUGLYs2r46INZzCyco",
                "https://drive.google.com/uc?export=view&id=1D6lgpdAEXhaT7OnZ_yv4a606zIIY0NI5"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, asik saat interaksi dan sefrekuensi.", "pesan": "Semangat dan semoga IMO bang!!"},
        {"nama": "Muhammad Aqil Ramadhan", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya asik dan suka bercanda serta interaktif", "pesan": "Sukses selalu dan sehat selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya baik dan lembut", "pesan": "Sukses selalu kak dan perbanyak senyum!"},
        {"nama": "Qois Olifio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya pintar dan beaura", "pesan": "Sukses selalu dan semangat bang!"},
        {"nama": "Hafsa Fazila Arradhi", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, lucu, dan suka duit", "pesan": "Sukses selalu dan semangat kakk!"},
        {"nama": "Luthfia Laila Ramadhani", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, suka dinamikanya sama bang aqil", "pesan": "Sukses selalu dan semangat kakkk!"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Baleg", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1hPcj_YllCfMYzTLQhkN4bXO2qe-Rc4Rz",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=10bcB3fYazfhpa1mGYTJqV7BlbhIsakWS",
        "https://drive.google.com/uc?export=view&id=1TdkaU4mCH3yWhhh7bncOwz5qFlJ-PE4f",
        "https://drive.google.com/uc?export=view&id=1JpYMX2nyOZf9SZ9kEVsYOWDBaIAeDyX6",
        "https://drive.google.com/uc?export=view&id=1mMvmNoSVq0TFxxy0Kl2E0Tar0DvUa4SC",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1ALNb5xUYkND2oKReqOJJOoebu1i9G1Rb",
        "https://drive.google.com/uc?export=view&id=1r51B2mv1ylvCCTPLlKDRRDsdFSAqabcD",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
    ]
    data_list = [
       {"nama": "Fathinah Nur Azizah", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Helmy Surya Pratama", "nim": "124450033", "umur": "20", "asal": "Jakarta", "alamat": "Tanya Bapas", "hobbi": "Ngesen Kiri", "sosmed": "@helmy_inst", "kesan": "Abangnya asik", "pesan": "Terus berkarya!"},
        {"nama": "Fernando Dimetrius Barus", "nim": "122450063", "umur": "21", "asal": "Tangerang Kota", "alamat": "Sebelah kamar Biwa", "hobbi": "Badminton", "sosmed": "@barus.fernando", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Suci Aulia", "nim": "122450034", "umur": "19", "asal": "Jakarta", "alamat": "Kota Baru", "hobbi": "Mancing", "sosmed": "@sciia___", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Wielman Itolo Halawa", "nim": "122450072", "umur": "20", "asal": "Nias Selatan", "alamat": "Asrama TB 3", "hobbi": "Dibonceng", "sosmed": "@wielhawn", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Lia Hana Ichisasmita", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Aqila Zayyan Salsabil", "nim": "124450014", "umur": "19", "asal": "Lampung Utara", "alamat": "Sukarame", "hobbi": "Mendokumentasikan Bayes", "sosmed": "@aqilazayyaan", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Hazel Mahesa Handhaka", "nim": "124450114", "umur": "20", "asal": "Lampung Timur", "alamat": "Gunung Terang", "hobbi": "Giring Ayam", "sosmed": "@hazelhandhaka", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Nadya Ratu Anjani", "nim": "123450083", "umur": "21", "asal": "Bandar Lampung", "alamat": "Sukarame", "hobbi": "Dengar Lagu", "sosmed": "@nadyaanjaani", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Dwi Rahma Fitriani", "nim": "124450084", "umur": "19", "asal": "Tulang Bawang", "alamat": "Jl. Lapas", "hobbi": "Baca buku, nonton film, dengerin musik", "sosmed": "@dwi_rahmftrnii", "kesan": "Informatif", "pesan": "Terus berkarya!"}
    ]    
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen PSDA":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota PSDA", "nim": "122450033", "umur": "20", "asal": "Bogor", "alamat": "Korpri", "hobbi": "Leadership", "sosmed": "@psda", "kesan": "Keren", "pesan": "Semangat PSDA!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen MIKFES":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota MIKFES", "nim": "122450044", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Olahraga", "sosmed": "@mikfes", "kesan": "Solid", "pesan": "Solid terus!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Eksternal":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1jKDOs48NUIKGq1A8Z0xngUZTr1crDCbX",
                "https://drive.google.com/uc?export=view&id=1IflEF9UfvFXL2iyAl2giEARM3Hacf6KG",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1vlyn4P2jCVepwf9Jk4HqcdGDDYWgB_B_",
        "https://drive.google.com/uc?export=view&id=18uWA7YLZ6xz3HcTtI06jZFrh6qYtsLuS",
        "https://drive.google.com/uc?export=view&id=1Q1MVOnXJp8ClRZnaXSvbl_qCZpyy4A48",
        "https://drive.google.com/uc?export=view&id=1VjqstZK3FzFIDp5jtp4S_2Qxq0v19etm",
        "https://drive.google.com/uc?export=view&id=1vXh_tDR2A5EvEp8z07lwVPYVn_LQK5Af",
        "https://drive.google.com/uc?export=view&id=1Nw489fRsyGd-63NoSgFKaRDIonyizgwg",
        "https://drive.google.com/uc?export=view&id=1Kjk1-T1hsYNlcMCJcyVQ2SF2w0qkvqka",
        "https://drive.google.com/uc?export=view&id=1Lj_vIIpVHEZ8tk1sXXTGCg-qX07c_0fW",
        "https://drive.google.com/uc?export=view&id=1axs_QMZ7UZbBaqhTp_JTY9gvdxJcEUB6",
        "https://drive.google.com/uc?export=view&id=19n9kDdp_kWpFFdU4qpYz1DVVO3-fjlbm",
        "https://drive.google.com/uc?export=view&id=1YoLCZA_w9h2t6Lr9w0KKRplgHh0pKvZK",
        "https://drive.google.com/uc?export=view&id=12kzNFYkrUgfPBuOh88dmhgnzrcO0Tp2s",
        "https://drive.google.com/uc?export=view&id=1h5w-XXVSVMOw6lA-RQWOW5ZAXAcy8p8I",
        "https://drive.google.com/uc?export=view&id=1rZMYltF9fVjeEfLvNq2SJeV4XROlMKmx",
        "https://drive.google.com/uc?export=view&id=1SwIXsRxz10A6iuWGPVwb3TxVgha77dhV",
        "https://drive.google.com/uc?export=view&id=1YshCV-3Y01ZA_VkMKjQ55NuAta6ssuuz",
        "https://drive.google.com/uc?export=view&id=1Aaoq3XxCWHAZ1CENfeDTHaZ9Hvo-rFMa",
        "https://drive.google.com/uc?export=view&id=1JIlO5g2WvnVKUWfjhtUeHQXKa2pJLc_5",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

                  ]
    data_list = [
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
                {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"},
        {"nama": "Anggota Eksternal", "nim": "122450055", "umur": "20", "asal": "Palembang", "alamat": "Korpri", "hobbi": "Networking", "sosmed": "@eksternal", "kesan": "Ramah", "pesan": "Jalin relasi luas!"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Internal":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"]
    data_list = [
        {"nama": "Anggota Internal", "nim": "122450066", "umur": "20", "asal": "Tangerang", "alamat": "Sukarame", "hobbi": "Design", "sosmed": "@internal", "kesan": "Keluarga baru", "pesan": "Harmonis selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen SSD":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1QrRxujgmVfZ92lno4la7wxqEyJMvAIt3",
                "https://drive.google.com/uc?export=view&id=1WRK48UMhbQAyWgFJrAzvkl4kM2dVPgeA",
        "https://drive.google.com/uc?export=view&id=1AcPhhoZ9Et2UJS-lIrmhJ2-jPOMvQnpp",
        "https://drive.google.com/uc?export=view&id=1HbqyPODWJS_Tv3TrHXvq9R-JBQi5CfsL",
        "https://drive.google.com/uc?export=view&id=13EKDQxiPgx1riA82sggBf8uO8FQxkZKR",
        "https://drive.google.com/uc?export=view&id=1_Qa8DvVGkjg-4Z7GZ8sFOPa2AaxyuoZH",
        "https://drive.google.com/uc?export=view&id=1yRYAIwml08qlW0ba8IXi1jImunNTbK2u",
        "https://drive.google.com/uc?export=view&id=1tF3x11LnMtJwzjA1nsFj7bWwYxdEQW_9",
        "https://drive.google.com/uc?export=view&id=1IbYZQ-ZRZkN_zMVhrVBXoYJB3NNLcWB-",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=198d96uuot_tGHCiNPq9Mogko-SY3L_4g",
        "https://drive.google.com/uc?export=view&id=1Rw_5EofMIqGr-RsAB9fjNUrsZAH8ixLT"

                  ]
    data_list = [
        {"nama": "Ihsan Maulana Yusuf", "nim": "123450110", "umur": "21", "asal": "Sumatera Barat", "alamat": "Belwis", "hobbi": "Cari dan baca jurnal, cari pak lucky, jualan", "sosmed": "@ihsan.myusuf", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
                {"nama": "Hanifah Inaya Sani", "nim": "123450123", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Masak", "sosmed": "@_inayasani", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afifah Fauziah", "nim": "12345002", "umur": "20", "asal": "Bandung", "alamat": "Airan", "hobbi": "Nonton Marvel", "sosmed": "@fifah.zy", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Hasan Nur Ramadhan", "nim": "1234500", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@hasan.ramadhan08", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Layina Ropiqo", "nim": "124450016", "umur": "19", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "nonton dracin", "sosmed": "@lay.inr_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Moch. Iqbal Az-Zahir", "nim": "122450052", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@iqbalazzahir_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Talitha Justine", "nim": "122450076", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anadia Carana", "nim": "123450019", "umur": "20", "asal": "Palembang", "alamat": "Way Huwi", "hobbi": "Nyari duit", "sosmed": "@nadiacrn_", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Abdillah Fikri Al pome", "nim": "123450062", "umur": "21", "asal": "Baturaja Sumsel", "alamat": "Airan", "hobbi": "Basket", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Afdhal Rahmad Setiawan", "nim": "124450008", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@dhal_setiawan", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggun Nita", "nim": "124450009", "umur": "20", "asal": "Lampung Utara", "alamat": "Belwis", "hobbi": "Nonton kartun", "sosmed": "@anggunitaaaa", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Della Anisa Fitri", "nim": "124450095", "umur": "18", "asal": "Lampung Timur", "alamat": "Margo Lestari", "hobbi": "Lagi ga punya hobi", "sosmed": "@dellaansaftr", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Medkraf":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1tQtKPE33XvtHYFFH9E-JgyNVfJJGs8Oq",
                "https://drive.google.com/uc?export=view&id=1vfm__BjVsYZ2iJ2xYYgAd4js3uT6FWiE",
        "https://drive.google.com/uc?export=view&id=1gCwVluHER9zwNxeRkVS-NwtAOXXh1YPo",
        "https://drive.google.com/uc?export=view&id=1vnBvhaDAaclYUfNZW0CYYOqJrjNMsgtU",
        "https://drive.google.com/uc?export=view&id=1VnZZ0elxkLWc3H4o2M8F0rMjfTjXZMJd",
        "https://drive.google.com/uc?export=view&id=1QZkwiLD3Ogw6CZIfkFXDLjzp5LOoyR-R",
        "https://drive.google.com/uc?export=view&id=1y_EKN7304sdXsA_pcM3C-evtR63tEUQ6",
        "https://drive.google.com/uc?export=view&id=1OS6SbsMIl8rU5aH7k7Po-8oXHSfrmf5J",
        "https://drive.google.com/uc?export=view&id=12UFotzHaPvL2B5bpzxBOhqD2Z7vqg_ka",
        "https://drive.google.com/uc?export=view&id=1Q1fuPrZ0JlRxdQVElfaZt_Z5OKlLysKy",
        "https://drive.google.com/uc?export=view&id=1uldvmHPpTo7KuAq6WxMwvnPH7gyK0n_4",
        "https://drive.google.com/uc?export=view&id=1GtoH93BH3oO8eB5Lcab6g71BhT89nGH3",
        "https://drive.google.com/uc?export=view&id=1c_xEQ_0edrA9TEdpBwM-RckaKoLwJMNP",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1TXczhSAV1e0DFdQ7rBtQ6XwLtOHVaX5M",
        "https://drive.google.com/uc?export=view&id=1jqpe5nWNyJ5HwsJ4ihHdoizx8bkcwEI0",
        "https://drive.google.com/uc?export=view&id=1UKkwqBsLFl62XaN69frWNrLdqYu9OY3p",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

                  ]
    data_list = [
        {"nama": "Nayla Salsabila Fathianisa", "nim": "123450082", "umur": "20", "asal": "Payakumbuh, Sumatera Barat", "alamat": "Way Huwi", "hobbi": "Musingin TA", "sosmed": "@naylasalsabilaa._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Donna Maya Puspita", "nim": "123450028", "umur": "20", "asal": "Bekasi", "alamat": "Way Huwi", "hobbi": "Berenang", "sosmed": "@donnamaya.p", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Labo John Noel Napitupulu", "nim": "123450037", "umur": "20", "asal": "Medan, Jakut, Palembang", "alamat": "Way Huwi", "hobbi": "Buka tutup laptop", "sosmed": "@noerruuu", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anash Tasya Ausyaqila", "nim": "124450050", "umur": "20", "asal": "Bandar Lampung", "alamat": "Way Huwi", "hobbi": "Ballet", "sosmed": "@anshtsyaaql", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Felisya Nabila Putri Nugroho", "nim": "124450104", "umur": "18", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Mancing emosi", "sosmed": "@felisyanbl", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Muhammad Razan Maulana Pratama", "nim": "124450031", "umur": "18", "asal": "Tangerang Selatan", "alamat": "Ryacudu", "hobbi": "Badminton ama tensor 24", "sosmed": "@muh_razan_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Sania Dwi Ayu Lestari", "nim": "123450087", "umur": "21", "asal": "Karawang", "alamat": "Airan", "hobbi": "Nongkrong depan ruang prodi", "sosmed": "@saniayyllstr", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Allisha", "nim": "125450019", "umur": "3", "asal": "Jepang", "alamat": "Cafe Kali", "hobbi": "Jalan bareng my love", "sosmed": "@aallishaa.aa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Alya Ramadhanti", "nim": "124450091", "umur": "19", "asal": "Jambi", "alamat": "Airan", "hobbi": "Main futsal", "sosmed": "@alya.rmdhnti", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Bunga Clarisa Sefa", "nim": "124450097", "umur": "2", "asal": "Sidomulyo", "alamat": "Pemda", "hobbi": "Mengkoding", "sosmed": "@buncaclrssf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Difanya Husakina", "nim": "124450043", "umur": "7.137 hari per hari ini", "asal": "Kalimantan Utara", "alamat": "Deket ITERA", "hobbi": "Mancing mania", "sosmed": "@difanyhsa", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Nazlah Auliya", "nim": "124450054", "umur": "20", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Main badmin lawan razan", "sosmed": "@nzlhauly_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Raihana Adelia Putri", "nim": "123450041", "umur": "20", "asal": "Lampung tengah", "alamat": "Airan Raya 1", "hobbi": "Membaca, menulis", "sosmed": "@n1tg._", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Edsel Adya Pradipta", "nim": "124450098", "umur": "20", "asal": "Lampung Selatan", "alamat": "Natar", "hobbi": "Scrolling Fesbuk", "sosmed": "@eddel_0712", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Lucia Advencia Rachel Nainggolan", "nim": "124450085", "umur": "20", "asal": "Bekasi", "alamat": "Belwis", "hobbi": "Nonton star wars", "sosmed": "@luciarachel_", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Shafa Delaila Azzahra", "nim": "124450124", "umur": "20", "asal": "Lampung tengah", "alamat": "Pemda", "hobbi": "Ngoding", "sosmed": "@_shaazzh", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}

    ]
    display_images_with_data(gambar_urls, data_list)
