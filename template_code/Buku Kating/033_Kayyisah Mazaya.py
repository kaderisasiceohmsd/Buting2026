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
        "https://drive.google.com/uc?export=view&id=1rQKJe_Zt68A83KD8ywHtxynzHyFWnxh3",
        "https://drive.google.com/uc?export=view&id=1UUb42OuOEfD4fel9_FVInxiU_v2YBkpK",
         "https://drive.google.com/uc?export=view&id=1Yaq6RbQMCJjCDltE8fKGnpUUsCypcuKg",
                "https://drive.google.com/uc?export=view&id=1VexjFKg4cxJvh4VboZS9Qo836WUAtnZg",
                "https://drive.google.com/uc?export=view&id=1I9O_OInTjfCaeMklmbScrIaERp8tXDEb",
                "https://drive.google.com/uc?export=view&id=1mwupEwMqo1IFeRVyyk3MX6NmfMf3tVH_"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "nim": "123450103", "umur": "20", "asal": "Medan", "alamat": "Korpri", "hobbi": "Main Game, Futsal", "sosmed": "@jars_mrp", "kesan": "Sangat seru", "pesan": "Semangat terus bang dalam menjalankan tugas dan kuliahnyaaa!"},
        {"nama": "Muhammad Aqil Ramadhan", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya lucuuu bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu bang semangat menjalankan tugas dan kuliahnya"},
        {"nama": "Efi Defiyati", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya imut murah senyum", "pesan": "Sukses selalu kak dan semangat kuliahnyaa!"},
        {"nama": "Qois Olifio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya soft spoken dan pendiam", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum", "pesan": "Sukses selalu dan semangat kuliahnya kaaakk!"},
        {"nama": "Luthfia Laila Ramadhani", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baiiik", "pesan": "Sukses selalu dan semangat kuliahnya kaakaaa!"}


    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Baleg":
    gambar_urls = ["https://drive.google.com/uc?export=view&id=1hVTbtc8kxw9Wojmbhew4gyMOoxh7L161",
                  "https://drive.google.com/uc?export=view&id=1QLzcWiphn8KdE4v8pm60SVUiZ-JEIpOq",
                   "https://drive.google.com/uc?export=view&id=1sYlhu5R3qMOfH4pnmi0EhrpAQzloEejr",
                   "https://drive.google.com/uc?export=view&id=1ijKwJuwSKMGKLbTohWnkPgL-PSE0RfRm",
                   "https://drive.google.com/uc?export=view&id=15d1k5edAzugMWb2Iiy_tNc2LbuTUyMbG",
                   "https://drive.google.com/uc?export=view&id=1p_meLyOVdpXopypWO1W5XF6RlSTUCLFg",
                   "https://drive.google.com/uc?export=view&id=1Dih47_xH9Apljkfo9HiNpGKoakSt7nG6",
                   "https://drive.google.com/uc?export=view&id=1ZSFbiRIsyvcWeJ7DGlJIEEtodJPeP8zL",
                   "https://drive.google.com/uc?export=view&id=1Pm-_1tU-kqs7aTtqjVczPcHoxR-37agJ",
                   "https://drive.google.com/uc?export=view&id=1K4H3ozJQlLvghqIGkhvUPAur1eFWKcI1"
                  ]
    data_list = [
        {"nama": "Anggota Baleg", "nim": "12245001", "umur": "20", "asal": "B. Lampung", "alamat": "Way Halim", "hobbi": "Organisasi", "sosmed": "@baleg", "kesan": "Mantap", "pesan": "Jaya selalu!"}
    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Senator":
    gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1enHDKPtCOJOcop2buBK1XrKToVI4xZRu",
         "https://drive.google.com/uc?export=view&id=1sTM68iTeccY1N_HNK8-l67p0X_C-MxML",
        "https://drive.google.com/uc?export=view&id=1fOA1GgkNbl8GD90SDJ2ze3r6E74dWhea",
        "https://drive.google.com/uc?export=view&id=15yg4LkBDNLIK3vtCUcJ5nsH6Q7xXXatv",
        "https://drive.google.com/uc?export=view&id=1kZAXlYUaPhu0uugLMid1W18_QCr9bdD0",
        "https://drive.google.com/uc?export=view&id=1eMUs2LR1894MEr5geYNnF0PLnFzu2Kdg",
        "https://drive.google.com/uc?export=view&id=1BnqiSFg1OYXtZt_qa4DcN5WY1law1NSn",
        "https://drive.google.com/uc?export=view&id=16DGXpCnk-Edumj3KBfbouhGXh698N3pQ",
        "https://drive.google.com/uc?export=view&id=10iYQkpIOJKCnkXoej6Mzc6R6VL4WAvug"

    ]
    data_list = [
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
                {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"}

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
        "https://drive.google.com/uc?export=view&id=1nBgLRiaIw9HHjM4X1iJ8bAJFknr4xqSS",
         "https://drive.google.com/uc?export=view&id=163qgyzrWISiEhRRSAC6bD9XwJR1zYAq5",
        "https://drive.google.com/uc?export=view&id=1dfRSs0BjMiXKFI4pluvi7pMKW467s5MQ",
        "https://drive.google.com/uc?export=view&id=1_BnmumkHSgvb52Q2WSzeaLaN5OY25_BZ",
        "https://drive.google.com/uc?export=view&id=1VvAgehftFcbgfMCXXrQ7b8tJiBJpczrl",
        "https://drive.google.com/uc?export=view&id=1EQFGvE0KBRvikwBcY-vzMAHxN9_l5UC3",
        "https://drive.google.com/uc?export=view&id=1rFJy2hRQxpoqC4v0cjfCnEYzQ3_Pfg4I",
        "https://drive.google.com/uc?export=view&id=1Hj0x16wRE9p1HKHBd_f7lmuU8H3x5G9s",
        "https://drive.google.com/uc?export=view&id=1HuvPh-rcPfpZbIshComYyQBSuLq66N2L",
        "https://drive.google.com/uc?export=view&id=1PoQL9uRZmAWRchGHa0cWigYhecVv0LX3",
        "https://drive.google.com/uc?export=view&id=1HO5XYAGzBZ9XiDVa0j5S82s31dBoLsXW",
        "https://drive.google.com/uc?export=view&id=1debXmEkqbMc90mUiMCXKFAFqkaruDtVv",
        "https://drive.google.com/uc?export=view&id=17Ec_HDubmMD4v13Hd4xg0Bp19t8zDHPD",
        "https://drive.google.com/uc?export=view&id=1_ZUoy6n8_pL5lI7iWHVU17pcdmd1OKUl",
        "https://drive.google.com/uc?export=view&id=1chH4Ykv6-yfM-Zg9Qe1VU4KtBGweHneU",
        "https://drive.google.com/uc?export=view&id=1gHn_Qu9N-fahwtXkVfZfuHpXjf5gUCDT",
        "https://drive.google.com/uc?export=view&id=1_ga069Zy0JZExhaclkcNZHkDsaHKiDNf",
        "https://drive.google.com/uc?export=view&id=1h9i8zxq8MTeyQovBL8ztIOcpcOOUB2jo",
        "https://drive.google.com/uc?export=view&id=1r-d0gPCHn6cEQb70YPiSCifB9q3OSCWj",
        "https://drive.google.com/uc?export=view&id=1DoDAEgPCQSvA7hxh-InwWAINe5oYsR60",
        "https://drive.google.com/uc?export=view&id=1RNA9Reg6EkvXzXB8HVzlGXALtCJ5cqzD",
        "https://drive.google.com/uc?export=view&id=15bGwYV3FSBkXi5GJskpuXT7iyMq0i1mP"

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
        "https://drive.google.com/uc?export=view&id=192FNfcYuc5q9OsvORkkWWordUqZSqapl",
         "https://drive.google.com/uc?export=view&id=1pclsgM1sJtOcQLA1-DWX1mjKbuw0u4LE",
        "https://drive.google.com/uc?export=view&id=1aR1jv-4z698LHJzCXtSYfip_IEnj83pM",
        "https://drive.google.com/uc?export=view&id=1pJ1l5lKpaB5qaYd99mHBanldCHu6i_wX",
        "https://drive.google.com/uc?export=view&id=1w8q9B9qMhdESsjqIYa0ET0tlrNDJjZ9f",
        "https://drive.google.com/uc?export=view&id=1XioMqKOay16dTBS7ocrfioj9IChE31dK",
        "https://drive.google.com/uc?export=view&id=1qs7jkIZ2XlmG2hqm2ubP4h-5EV4Z67Ft",
        "https://drive.google.com/uc?export=view&id=1CSQKtNQ5GDGDmAji4EJASXHZMh-YWsH8",
        "https://drive.google.com/uc?export=view&id=1whS3EDf9omJIiUUO4oiUVNsNPpP8nvqJ",
        "https://drive.google.com/uc?export=view&id=1OsZsT1gdVWiL-nRavT_bG7m_CzOyj_Ot",
        "https://drive.google.com/uc?export=view&id=1R-pUvNb3vBVWHkIeeRMEXyD9H65j7b0h"

                  ]
    data_list = [
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
                {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"},
        {"nama": "Anggota SSD", "nim": "122450077", "umur": "20", "asal": "Depok", "alamat": "Korpri", "hobbi": "Coding", "sosmed": "@ssd", "kesan": "Inovatif", "pesan": "Ciptakan solusi!"}

    ]
    display_images_with_data(gambar_urls, data_list)

elif menu == "Departemen Medkraf":
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
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"

                  ]
    data_list = [
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
                {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"},
        {"nama": "Anggota Medkraf", "nim": "122450088", "umur": "20", "asal": "Yogyakarta", "alamat": "Airan", "hobbi": "Editing & Foto", "sosmed": "@medkraf", "kesan": "Kreatif banget", "pesan": "Karya tanpa batas!"}

    ]
    display_images_with_data(gambar_urls, data_list)
