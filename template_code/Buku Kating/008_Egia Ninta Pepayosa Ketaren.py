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
        "https://drive.google.com/uc?export=view&id=14a1iFs8tYHhct_Zgdu8Yyk-V8_YOLhxW",
        "https://drive.google.com/uc?export=view&id=15qWIuv3mlDPwNXMpErLqnwr_rgCFGq-0",
         "https://drive.google.com/uc?export=view&id=1Q4f2LwpDUGVwRb-Jr89pPZ80OWpcIoXU",
                "https://drive.google.com/uc?export=view&id=1fyuCwiyoCbeiyoEGoBA5-gWcUXPG0ppm",
                "https://drive.google.com/uc?export=view&id=d/1trjiCZGnd5ESfCHG2-05s7cdfh2T0jOm",
                "https://drive.google.com/uc?export=view&id=1DG48EvEsHh9q4n30ft76uAAVN789pZpr"
    ]
    data_list = [
        {"nama": "Ginda Fajar Riadi Marpaung", "nim": "123450103", "umur": "22", "asal": "Batam", "alamat": "Kesekretariat HMSD", "hobbi": "Push IMO", "sosmed": "@jars_mrp", "kesan": "Abangnya seruu, dlu pernah jadi kadiv op pas natal SD25 bisa diajak serius dan bercanda.", "pesan": "Semangat dan suksek selalu bangg!!"},
        {"nama": "Muhammad Aqil Ramadhan", "nim": "123450066", "umur": "22", "asal": "Riau", "alamat": "Sekretariat HMSD", "hobbi": "Dzkir", "sosmed": "@muhammadaqil1111", "kesan": "Abangnya seru bisa diajak bercanda dan bisa diajak bicara serius", "pesan": "Sukses selalu serta semangat dalam melaksanakan tugas!"},
        {"nama": "Efi Defiyati", "nim": "123450005", "umur": "21", "asal": "Lampung Timur", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffiidefi", "kesan": "Kakaknya murah senyum", "pesan": "Sukses selalu kak dan semangat!"},
        {"nama": "Qois Olifio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kota Baru", "hobbi": "Mainin surat", "sosmed": "@qoisolifio_", "kesan": "Abangnya sof spoken, lucuu", "pesan": "Sukses selalu dan semangat bang!!"},
        {"nama": "Hafsa Fazila Arradhi", "nim": "123450079", "umur": "21", "asal": "Bandar Lampung", "alamat": "Bandar Lampung", "hobbi": "Bertemu Luluk", "sosmed": "@hafsafazilahh", "kesan": "Kakaknya baik, murah senyum, dan suka duit", "pesan": "Sukses selalu dan semangat kakk!!"},
        {"nama": "Luthfia Laila Ramadhani", "nim": "123450004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Keliling Balam", "sosmed": "@luthhifiarmdhni", "kesan": "Kakaknya seru, lucuu, baikk", "pesan": "Sukses selalu dan semangat kakkk!!"}


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
        "https://drive.google.com/uc?export=view&id=1bwy4U200wjwc6YN3tumWFDSW7LunNfmu",
        "https://drive.google.com/uc?export=view&id=1EJBPN6k5XmLVB8xtMNTgo2nWPEQFUkqv",
        "https://drive.google.com/uc?export=view&id=10s33vUvU34kLCr8nyL8rNZfM1k-Z1WCK",
        "https://drive.google.com/uc?export=view&id=1R77leJE5k8iATcKwvKFiw5nCmq-Ezl8C",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        "https://drive.google.com/uc?export=view&id=1PQpUNK5ZcmAVQ06WLxg8UlpHGsKoPlEC",
        "https://drive.google.com/uc?export=view&id=1_-uYsuZTVLXJ-RgwHKfzpR4r0otEN3Fx",
        "https://drive.google.com/uc?export=view&id=10IDI69GEY5BwBdxi6wm5L5im0UKDLoen",
        "https://drive.google.com/uc?export=view&id=1H77_72UrtmZXICgAMQHerezZ5vIYyYrp"

    ]
    data_list = [
       {"nama": "Fathinah Nur Azizah", "nim": "123450072", "umur": "21", "asal": "Jakarta", "alamat": "Belakang PB", "hobbi": "Nulis di Medium", "sosmed": "@sfathinahnazzh", "kesan": "Informatif", "pesan": "Terus berkarya!"},
         {"nama": "Lia Hana Ichisasmita", "nim": "123450089", "umur": "21", "asal": "Jakarta", "alamat": "Belwis", "hobbi": "Nonton", "sosmed": "@lia.h_264", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
        {"nama": "Anggota Senator", "nim": "122450022", "umur": "21", "asal": "Jakarta", "alamat": "Sukarame", "hobbi": "Debat", "sosmed": "@senator", "kesan": "Informatif", "pesan": "Terus berkarya!"},
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
        "https://drive.google.com/uc?export=view&id=1s2XoLDNkmd79J8wzApnNqw9wA6lk1-cv",
        "https://drive.google.com/uc?export=view&id=1p8c54qe0t-KydPSN1_njmXyec4iIxPv1",
        "https://drive.google.com/uc?export=view&id=180LnphDPRRURP6I5_axl1o8-rMvM0a7v",
        "https://drive.google.com/uc?export=view&id=1OA-b0s0HelPi3sxZVwL8ClhvTZOd6RwS",
        "https://drive.google.com/uc?export=view&id=10bAdfxrD7ocCcavQarvNOlxpMMwvDIfu",
        "https://drive.google.com/uc?export=view&id=1LGW61YoaqD33BADwm6puWEK6OF5o23ZD",
        "https://drive.google.com/uc?export=view&id=1Wg_IKqKz65eAm9Go4sKAnbBnNVsBWr2J",
        "https://drive.google.com/uc?export=view&id=17gTme8LpUJXymPaVakbNlva-dI-9g-I_",
        "https://drive.google.com/uc?export=view&id=1tY19bSlTXLnJlwfmh06rgIiYNlL5MLUY",
        "https://drive.google.com/uc?export=view&id=1fxkhtAJEXXvdsLWEBLxAzJh__G8RMX0y",
        "https://drive.google.com/uc?export=view&id=1SbfGEpQvEF5JRJOr8eCiNm4fcHe6RL0Y",
        "https://drive.google.com/uc?export=view&id=1CXKxYtEPvKZ7-XB4IcGU8Lt6Meu31efF",
        "https://drive.google.com/uc?export=view&id=1iPjdXfvKW7s0ACiTHMRnV3AibnbNFM3c",
        "https://drive.google.com/uc?export=view&id=1Na9ZnS6uwX_Hq1qJVQuT7m_OeL9WPMJx",
        "https://drive.google.com/uc?export=view&id=1aphZKIhFSh1cXrDmGNNBFrW0168bQOup",
        "https://drive.google.com/uc?export=view&id=1gC-G8jGnV141twsV4142tLba2B0HlDgS",
        "https://drive.google.com/uc?export=view&id=1YU37XRd6LfGjBOCMDxhjje91ifITPXvB",
        "https://drive.google.com/uc?export=view&id=14-bA744kvqPIcYDN4fEYbDuH3SPMmaMd",
        "https://drive.google.com/uc?export=view&id=1rl91DQRXnOId12HESf4-i5g7sTtFaGX5",
        "https://drive.google.com/uc?export=view&id=1Z4-9A7vu0SoSH4V26iOOMWkWce1DiamW",
        "https://drive.google.com/uc?export=view&id=1y6G-InpEMk3i3L1lr8VIjuWy2HZoT7N6",
        "https://drive.google.com/uc?export=view&id=1BlMK8yUPvll8ifkluUTZu87WU-ycClyb"

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
