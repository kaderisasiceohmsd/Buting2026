import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

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
            "Departemen MINBAK",
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
            "nav-link-selected": {"background-color": "#8D4C06"},
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
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['Nim']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Yro_FiWM13COyTiubMR23sjR5v5EdKZB",
            "https://drive.google.com/uc?export=view&id=16i6ZBe3fFC7PIMT-OxHi-nSfBgLHSTzf",
            "https://drive.google.com/uc?export=view&id=1TPHBkQDDpCpF-uHuOkZkE2j58QgWKesb",
            "https://drive.google.com/uc?export=view&id=1HNkx2-8WrgbVhufU7vIdeKPlkhi66NlR",
            "https://drive.google.com/uc?export=view&id=1mhlOxKmXscotUGYn4hwjj7fO6X6TuBPX",
            "https://drive.google.com/uc?export=view&id=1OUaA6I7TtdOwh1Y_aApoar95wnbYhHcc",
        ] 
        

        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abangnya keren, kalem, asik juga waktu jadi pemateri",  
                "Pesan":"Semangat terus bang semoga skripsinya dimudahkan"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Abangnya asik, lucu, suka bercanda juga, kalau jadi pemateri asik",  
                "Pesan":"Sehat selalu bang semoga dimudahkan segala urusan"
            },
            {
                "Nama": "Efi Defiyati",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakaknya baik sama kalem",  
                "Pesan":"Semangat terus dan sehat selalu kak"
            },
            {
                "Nama": "Qois Olifio",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Abangnya keren, kalem, lucu",  
                "Pesan":"Semangat  bang, semoga lancar bikin skripsinya"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakaknya cantik, baik, kalem, asik juga",  
                "Pesan":"Semangat terus kak, sehat selalu, jangan lupa istirahat"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"Semangat terus kak, semoga dimudahkan kuliahnya kak segala urusannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x6d-BunsI4-mBwmf8BbzzIa4eZB044it",
            "https://drive.google.com/uc?export=view&id=1k8djGjDJrGByw5IxevM6GQ7dPpC1ypID",
            "https://drive.google.com/uc?export=view&id=10lRmV4O8jWfKrWajgXpXCgdoj0ZBNQf5",
            "https://drive.google.com/uc?export=view&id=11Xf7Tdwx2_WlXHvK6Pynh7ttb6FU5P3J",
            "https://drive.google.com/uc?export=view&id=1z0d5DSj0wxZlFbUC5UWJAZoA5SIKLTzQ",
            "https://drive.google.com/uc?export=view&id=1ZJwKIhmpWkY1rXEAv_eLPdxNbeBkmVSc",
            "https://drive.google.com/uc?export=view&id=1ZRWj7EtnH09DCTomZLL5rdh3B8t5wOPG",
            "https://drive.google.com/uc?export=view&id=1i2l8DGp7sjpGejD3enQe1J_qbjhujgCk",
            "https://drive.google.com/uc?export=view&id=1V3MzDHolrVrsxg8Z2oqUGyB_D3EPMtZX",
            "https://drive.google.com/uc?export=view&id=16AqH7RncpBDuJNWUgE7mkZykSIK-9-xs",
        ]

        data_list =[
            {
                "Nama": "Fathinah Nur Azizah",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, pembawaannya adem, positif bangat auranya.",
                "Pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "Nim": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobbi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Abangnya asikkkk, ramah juga",
                "Pesan": "Semangat terus bang, jangan lupa makan"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Abangnya kalem, suka bercanda",
                "Pesan": "Semangat teruss bang"
            },
            {
                "Nama": "Suci Aulia",
                "Nim": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobbi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kakaknya ramah bangatt, baik sama cantikk",
                "Pesan": "Sehat selalu kak, lancar selalu kuliahnya"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "Nim": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya kalem gitu, trus abnagnya kelihatan bangat aura pintarnya",
                "Pesan": "Sehat selalu bang, semangat terus juga"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "Nim": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya baik, ramah jugaa",
                "Pesan": "Semoga kuliahnya lancar ya kak, Semangat teruss pokonya"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kakaknya imuttz, asik juga ",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "Nim": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobbi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abangnya keren, asik juga",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "Nim": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kakaknya cantik, ramah, baik",
                "Pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "Nim": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobbi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kakaknya cantikk, baik dan ramah juga",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xwkUIMV3fL999bHm088cp_NH93kzJfta",
            "https://drive.google.com/uc?export=view&id=1_C76qpPna82TFWLKIg0dzoav49sEE5P2",
            "https://drive.google.com/uc?export=view&id=1Vf-pHC9E3YFfDZhUjMz0nVQcrZY999Jq",
            "https://drive.google.com/uc?export=view&id=1b8yMuQPOcrRzO2CovPdWduQY4Q6ZsB7t",
            "https://drive.google.com/uc?export=view&id=14Of9LVad4xHw2qppq6-_o60Gr959L8la",
            "https://drive.google.com/uc?export=view&id=1RYr-paGITdtu_CuhbREurR9cJhVgejIA",
            "https://drive.google.com/uc?export=view&id=1kaBhTpr66WEz_3dUbWDsjIysuPmgr3SP",
            "https://drive.google.com/uc?export=view&id=1Zok1NtqzafW7f_zUbtkfKmadfdpXrKD2",
            "https://drive.google.com/uc?export=view&id=1w8xWQAztVQQyHX6cm41-We_1J4-IZ1LC",
            "https://drive.google.com/uc?export=view&id=1cVBLZ77vS9g_uN2c1EMyYkgXEQpvGdij",
            "https://drive.google.com/uc?export=view&id=1LfHk8XXaSddwUXk83Od2i0j-04osuFBi",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",  # sisa
        ]
      
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "Nim": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Mencari dan membaca jurnal, 2 minggu mewawancarai anak kader angkatan 25 Datavora tercinta, mencari pak Luki",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Abangnya asik",
                "Pesan": "Semangat terusbang, semoga skripsinya lancar bang"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "Nim": "123450123",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Memasak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya cantik, baik dan ramah",
                "Pesan": "Sehat selalu kak "
            },
            {
                "Nama": "Afifah Fauziah",
                "Nim": "123450002",
                "Umur": "19",
                "Asal": "Depok",
                "Alamat": "Belakang PB",
                "Hobbi": "Ngumpulin data sama nonton Marvel",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya cantik, baik dan asik",
                "Pesan": "Semangat terus ya kak, semoga lancar kuliahnya"
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "Nim": "124550012",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sebelah kost Ayake",
                "Hobbi": "Scroll Facebook",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Abangnya baik dan santai",
                "Pesan": "Semangat terus bang ,Semoga sukses"
            },
            {
                "Nama": "Layina Ropiqo",
                "Nim": "124550016",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Menonton Film",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya cantik, ramah dan baik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "Nim": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobbi": "Nonton Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya kalem dan baik",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Talitha Justine",
                "Nim": "124450076",
                "Umur": "19",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Pemda",
                "Hobbi": "Nonton",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya cantik, ramah, dan baik",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Anadia Carana",
                "Nim": "123450019",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Kost The Icon",
                "Hobbi": "Belajar",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya kelihatan bangat aura pinter dan ramah nya",
                "Pesan": "Sukses terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "Nim": "123450062",
                "Umur": "21",
                "Asal": "Oku, Sumatera Selatan",
                "Alamat": "Airan",
                "Hobbi": "Godain cewe bang Homey",
                "Sosmed": "@pomest_",
                "Kesan": "Abangnya asik dan seru",
                "Pesan": "Semangat terus bang, semoga skripsinya lancar"
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "Nim": "124550008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping Kost Rafli",
                "Hobbi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Abangnya baik dan asik",
                "Pesan": "Jangan lupa bahagia, Semoga sehat terus bang"
            },
            {
                "Nama": "Anggun Nita",
                "Nim": "124550009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobbi": "Menonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya bukan cuman cantik, kakaknya ramah dan baik juga",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
            {
                "Nama": "Della Anisa Fitri",
                "Nim": "124450095",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestari",
                "Hobbi": "Lagi suka olahraga",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Internal":
    def Internal():
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
            
        ]
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "Nim": "123450106",
                "Umur": "20",
                "Asal":"Tangerang Kota",
                "Alamat": "Gerbang Barat",
                "Hobbi": "Begadang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abang asik, baik, sama bisa diajak diskusi",  
                "Pesan":"semangat abang, sehat selalu"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Nim": "123450034",
                "Umur": "21",
                "Asal":"Way Kanan",
                "Alamat": "Untung Suropati",
                "Hobbi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "kakaknya cantik, ramah dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, lancar skripsi"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "Nim": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakaknya cantik, asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak"
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Tetangga Singapore",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Abangnya asik, ramah dan seru",  
                "Pesan":"semangat terus kuliahnya abang"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "Nim": "124450096",
                "Umur": "18",
                "Asal":"Indragirihulu",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Sleep Call",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "kakaknya cantik, asikkkk, dan ramah",  
                "Pesan":"semangat kakak, sehat selalu"
            },
            {
                "Nama": "Cerine Sihotang",
                "Nim": "124450049",
                "Umur": "19",
                "Asal":"Semarang",
                "Alamat": "Belwis",
                "Hobbi": "Manjat pohon kelapa",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "kakaknya asikk, cantik, dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, Sehat selalu"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Nim": "124450094",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Pemda",
                "Hobbi": "Main Biola",
                "Sosmed": "@jay.saputra.tmb",
                "Kesan": "abangnya asik, seru orangnya, ramah jugaa",  
                "Pesan":"semangat selalu bangg, sehat selalu"
            },
            {
                "Nama": "Najla Nursyifa",
                "Nim": "124450051",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Nonton asmr",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kakaknya Cantik, asik, ramah, dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, sehat selalu"
            },
            {
                "Nama": "Rozak Ramdani",
                "Nim": "124450100",
                "Umur": "19",
                "Asal":"Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobbi": "Badminton",
                "Sosmed": "@rozakramdani_",
                "Kesan": "Abangnya seru dan baik",  
                "Pesan":"semoga sehat selalu abang"
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Nim": "124450046",
                "Umur": "19",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobbi": "Memasak",
                "Sosmed": "@christiani8872",
                "Kesan": "kakanya baik, cantik, asik juga kayaknya",  
                "Pesan":"semoga selalu dikelilingi orang baik dan sehat selalu kak"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Nim": "123450064",
                "Umur": "21",
                "Asal" : "Padang",
                "Alamat": "Way Kandis",
                "Hobbi": "Nonton MU",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang, lancar kuliahnya"
            },
            {
                "Nama": "Audina Fitria",
                "Nim": "124450038",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kakaknya cantikk, asik,  dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, sehat selalu"
            },
            {
                "Nama": "Cika Adelia BR Marbun",
                "Nim": "124450107",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Scroll tiktok",
                "Sosmed": "@cikambrn",
                "Kesan": "Kakaknya seru dan baik",  
                "Pesan":"Jaga kesehatan kakak, semoga bahagia selalu"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "Nim": "124450068",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobbi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "kakanya baik, seru orangnya",  
                "Pesan":"semoga selalu dikelilingi orang baik, lancar kuliahnya kak"
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Nangkap lele",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang"
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Nim": "124450036",
                "Umur": "21",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Main game di HP temen",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang, sehat"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Internal()

elif menu == "Departemen Medkraf":
    def medkraf():
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
        ]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "Nim": "123450082",
                "Umur": "20",
                "Asal": "Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwu",
                "Hobbi": "Musingin TA",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "Kakaknya cantik, ramah , dan baik juga",
                "Pesan": "Sehat selaluu kakk"
            },
            {
                "Nama": "Donna Maya Puspita",
                "Nim": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobbi": "Berenang",
                "Sosmed": "@donnamaya.p",
                "Kesan": "Kakaknya ramah bangat, baikk jugaa",
                "Pesan": "Semoga selalu dimudahkan kak, sehat selalu ya"
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "Nim": "123450037",
                "Umur": "20",
                "Asal": "Medan, Jakarta Utara, Palembang",
                "Alamat": "Way Huwi",
                "Hobbi": "Buka Tutup Laptop",
                "Sosmed": "@noerruuu",
                "Kesan": " Abangnya baik",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "Nim": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Ballet",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "Kakaknya cantik dan ramah",
                "Pesan": "Lancar Kuliahnya kakk"
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "Nim": "124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Mancing emosi",
                "Sosmed": "felisyanbl",
                "Kesan": "kakaknya maniss, cantik juga",
                "Pesan": "Lancar kuliahnya kak"
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "Nim": "124450031",
                "Umur": "18",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Dukung silver arrow alias mercedes",
                "Sosmed": "@muh_razan_",
                "Kesan": "Abangnya baik",
                "Pesan": "Semangat terus dan sehat selalu bang"
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "Nim": "123450086",
                "Umur": "17",
                "Asal": "Bali",
                "Alamat": "Airan",
                "Hobbi": "Nongkrong depan prodi",
                "Sosmed": "saniayyllstr",
                "Kesan": "Kakaknya cantikk, ramah juga",
                "Pesan": "Semanagt terus kak"
            },
            {
                "Nama": "Allisha",
                "Nim": "124450019",
                "Umur": "3 Tahun",
                "Asal": "Surga",
                "Alamat": "Rumah Asha",
                "Hobbi": "Ice skating",
                "Sosmed": "@aallishaa.aa",
                "Kesan": "Kakaknya baik, asik juga ",
                "Pesan": "Semoga apa yang kakak inginkan segera terwujud"
            },
            {
                "Nama": "Alya Ramadhanti",
                "Nim": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobbi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "Kakaknya baikkk",
                "Pesan": "Lancar terus kak kulainya, semangat selalu"
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "Nim": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobbi": "Mengkoding",
                "Sosmed": "@bungaclrssf",
                "Kesan": "Kakaknya asik bangat, ramah juga, cantikkk",
                "Pesan": "Semangat terus kakk, semoga sehat selalu"
            },
            {
                "Nama": "Difanya Husakina",
                "Nim": "124450043",
                "Umur": "7.137 hari per hari ini",
                "Asal": "Sumsel",
                "Alamat": "Kafe Kali",
                "Hobbi": "Bobo cantik",
                "Sosmed": "@difanyhsa",
                "Kesan": "Kakaknya cantikkk, ramah, dan baik",
                "Pesan": "Sehat selalu kak, Semangat terus"
            },
            {
                "Nama": "Nazlah Auliya",
                "Nim": "124450054",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Mimpi diatas kasur",
                "Sosmed": "nzlhauly_",
                "Kesan": "kakaknya cantik, baikk, dan ramah",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Raihana Adelia Putri",
                "Nim": "123450041",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobbi": "Menulis, membaca",
                "Sosmed": "n1tg._",
                "Kesan": " Kakaknya cantikk, imutt",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "Nim": "124450061",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@daffascript_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "Nim": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobbi": "Scrolling Fesbuk",
                "Sosmed": "@eddel_0712",
                "Kesan": "Abangnya baik",
                "Pesan": "Sehat selalu bang dan semangat terus"
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "Nim": "124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Nonton Star Wars",
                "Sosmed": "luciarachel_",
                "Kesan": "Kakaknya cantikk",
                "Pesan": "Sehat selalu kak, lancar kuliahnya"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "Nim": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobbi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "Nim": "124450112",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@xifasky",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1frdMeO51QSLe7ipMWz28-4iiPuSl-DPq",
            "https://drive.google.com/uc?export=view&id=1hkdT8H9h16iwtc2t9l_zsqlfaHipx1yK",
            "https://drive.google.com/uc?export=view&id=1GX8H5kB3ax-d8wPFfqZ6a7r73PIDLm03",
            "https://drive.google.com/uc?export=view&id=1Jcfpg2FRcEt-QBVZdQ69olcvPgmgFDSv",
            "https://drive.google.com/uc?export=view&id=16zdym77bREvbbAHI2fWaIZWui5cDBK9s",
            "https://drive.google.com/uc?export=view&id=1KeAA_x-OlSBwO5xRNEu6QawfDT1sEUYT",
            "https://drive.google.com/uc?export=view&id=1euQTIf6d6xukt3ycMTishuzbXfKt3kfi",
            "https://drive.google.com/uc?export=view&id=1yGAS_7qCv-OASGa1XnIDttUYSAHApvCk",
            "https://drive.google.com/uc?export=view&id=16uljZrCAdFhcr5tdx9WEkMSWj0VNiIwL",
            "https://drive.google.com/uc?export=view&id=15r6Cw4Tc1-6k3CS-Oz6ILnwL5vkuGvme",
            "https://drive.google.com/uc?export=view&id=18djGeSmtY3ZxATc-2KZmSqsOUNzIRJFa",
            "https://drive.google.com/uc?export=view&id=1yaM6nLOql9UHkobJSp3vW5gs0inViJVO",
            "https://drive.google.com/uc?export=view&id=11R6_EhHDmZtncRoMQYyElz_Z9yIdwUsn",
            "https://drive.google.com/uc?export=view&id=1QV25uQlFDTjoRWFXDqsPajTfdhtOYQvZ",
            "https://drive.google.com/uc?export=view&id=1H_l7l6F-RbUr969q_zX5vyLIqUCuPbLQ",
            "https://drive.google.com/uc?export=view&id=1EVD1k_cBaRXPaFbmx6AfEcexfDnymP85",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_17",  # Kosong untuk nomor 17
        ]
        
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Vany Salsabila Putri",
                "Nim": "123450022",
                "Umur": "21",
                "Asal": "Sibologa",
                "Alamat": "Pudan Kos",
                "Hobbi": "Berduaan sama pacar",
                "Sosmed": "vany.salsabilaa",
                "Kesan": "Kakaknya cantik, baik, dan ramah  ",
                "Pesan": "Semangat selalu kak"
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "Nim": "123450117",
                "Umur": "21",
                "Asal": "Tanah Indonesia",
                "Alamat": "Samping Rumah Henry",
                "Hobbi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Abangnya baik",
                "Pesan": "Semangat terus dan sehat selalu bang"
            },
            {
                "Nama": "Afriza Azmi",
                "Nim": "124450110",
                "Umur": "20",
                "Asal": "Malang",
                "Alamat": "Dalam pasar",
                "Hobbi": "Teriak",
                "Sosmed": "",
                "Kesan": "abangnya baik dan ramah",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "Nim": "124450108",
                "Umur": "21",
                "Asal": "Paninjauan Solok, sepuluh kota diatas, Sumatera Barat, Indonesia",
                "Alamat": "Blok D 77, jalan manggis delapan, pemda, jatiagung, lampung selatan, lampung, indonesia",
                "Hobbi": "Mancing",
                "Sosmed": "@ykeall",
                "Kesan": "Abangnya baik, ramah , asik juga",
                "Pesan": "Sehat selalu bang"
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "Kontrakan Hijau",
                "Hobbi": "Mandiin anak ayam",
                "Sosmed": "@caesarozora",
                "Kesan": "Abangnya baik aslinya, mau ngusahain adik tingkat juga",
                "Pesan": "Sehat selalu bang"
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "Nim": "124450029",
                "Umur": "18",
                "Asal": "Kampung lama",
                "Alamat": "Dibawah turunan",
                "Hobbi": "Makan gorengan",
                "Sosmed": "yudiameilianaa_",
                "Kesan": "Kakaknya sseruu, asik bangat, ramah juga",
                "Pesan": "Sehat selalu kak dan tetap semangat"
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "Nim": "124450016",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Sebelah kanan rumah Henry",
                "Hobbi": "Ngecek makan ayam",
                "Sosmed": "_haikaaall",
                "Kesan": "Abangnya baik aslinya",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "Nim": "124450056",
                "Umur": "18",
                "Asal": "",
                "Alamat": "kost owen, warteg bahari",
                "Hobbi": "Belajar naik motor ke bandung 94",
                "Sosmed": "putrimannaa",
                "Kesan": "Kakaknya cantikkk, asik, dan sangat ramah",
                "Pesan": "Semangat terus kak, jangan lupa istirahat"
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "Nim": "123450059",
                "Umur": "21",
                "Asal": "johor baru",
                "Alamat": "depan mie gacoan",
                "Hobbi": "Main gitar",
                "Sosmed": "queentanaabila",
                "Kesan": "Kakaknya baikk",
                "Pesan": "Sehat selalu kak, semangat terus "
            },
            {
                "Nama": "Desman Velius Halawa (Kepala Divisi PMA)",
                "Nim": "123450114",
                "Umur": "19",
                "Asal": "Nias",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Ngejek orang",
                "Sosmed": "desmanhall_",
                "Kesan": "Abangnya ramah dan baik",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Azzelya Thianandry",
                "Nim": "123450041",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Makan Ice",
                "Sosmed": "azzelytn",
                "Kesan": "kakaknya kalem, cantik juga",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Charrlindah",
                "Nim": "123450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobbi": "Ngurus Peternakan",
                "Sosmed": "charrlnn",
                "Kesan": "kakaknya cantik, ramah juga",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "Nim": "123450111",
                "Umur": "17",
                "Asal": "Sidingkalang",
                "Alamat": "Di sebelah kost haikal",
                "Hobbi": "Jadi nelayan",
                "Sosmed": "jemarrro",
                "Kesan": "Abangnya baikk",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "Nim": "123450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobbi": "Main roblox",
                "Sosmed": "n.bila_a",
                "Kesan": "kakaknya cantikk, baik juga",
                "Pesan": "Semoga lancar kuliahnya"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "Nim": "123450007",
                "Umur": "20",
                "Asal": "Kota Ikan",
                "Alamat": "Disamping Kost Afdal",
                "Hobbi": "Memancing",
                "Sosmed": "dearfkvmfl",
                "Kesan": "abangnya baik",
                "Pesan": "Semangat terus bang, moga lancar kuliahnya"
            },
            {
                "Nama": "Salavi Naharani",
                "Nim": "123450090",
                "Umur": "20",
                "Asal": "Lampung timur",
                "Alamat": "Jatimulyo",
                "Hobbi": "Minum air putih",
                "Sosmed": "avi.nhr",
                "Kesan": " kakaknya cantik, imut juga",
                "Pesan": "Semangat kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MINBAK":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U3ldzyGfUkintUsoS5U8yghCsvAHPJki",
            "https://drive.google.com/uc?export=view&id=105EdmWQIMoUwmrWwraPzsxY2AWrjOkYT",
            "https://drive.google.com/uc?export=view&id=1b8jnaQRvyS4AOC9HbxY-ysV3FQpKSMhf",
            "https://drive.google.com/uc?export=view&id=17ZVz4LSljv7dVmYRMtNhqWBdJkejRQq_",
            "https://drive.google.com/uc?export=view&id=10gbYmJBr81KU-IUJFzY3-DkBXo1q2too",
            "https://drive.google.com/uc?export=view&id=1LDEB7aSNGcso9UHeSL4wyfpoFtqZUrhi",
            "https://drive.google.com/uc?export=view&id=17PPF-PbOFuW5aNshio_KXphn4z0D8HeY",
            "https://drive.google.com/uc?export=view&id=1I7Ril1ajg7EghKyHBbnSdJkljzMKy9iS",
            "https://drive.google.com/uc?export=view&id=1H1QTwQJJZqNcBx0STD8pyjYz284pvDGw",
            "https://drive.google.com/uc?export=view&id=1cVhe-hO5Lj_SAeWXHVwPqrz0Npq_UFxN",
            "https://drive.google.com/uc?export=view&id=1R19q4WcgPKS83x3XXH6dvOM_FHNUtqwm",
            "https://drive.google.com/uc?export=view&id=1ixlBpOYiUmRneLrCxt37SqP4KC148cqN",
            "https://drive.google.com/uc?export=view&id=19hxc3Dbv_gSlU8RDoPRZE2N8A4fQuAh8",
            "https://drive.google.com/uc?export=view&id=1VFn97aheqsgeQ_XaZnrMj8AsdbUAp4cy",
            "https://drive.google.com/uc?export=view&id=1XnMmyLW9V14YLl3rLo7Vt-BG-rZe6Mcq",
        ]
        
        
        data_list = [
            {
                "Nama": "Kevin Antonio Junior ",
                "Nim": "123450009",
                "Umur": "21",
                "Asal": "Sulawesi Selatan",
                "Alamat": "Panjang, Bandar Lampung",
                "Hobbi": "Main gaplek",
                "Sosmed": "@kevinaj_",
                "Kesan": "Abangnya asik baik juga",
                "Pesan": "Semoga lancar kuliahnya bang"
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika ",
                "Nim": "123450046",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Way Dadi",
                "Hobbi": "Mendaki Gunung",
                "Sosmed": "@ferazkaa",
                "Kesan": "Kakaknya cantikk, baik, dan ramah juga",
                "Pesan": "Sehat selalu kak, lancar kuliahnya"
            },
            {
                "Nama": "Ali Aristo Muthahhari Parisi",
                "Nim": "123450088",
                "Umur": "21",
                "Asal": "Lampung Timur",
                "Alamat": "Gang Sakum Belwis",
                "Hobbi": "Nonton F1",
                "Sosmed": "@ali_parisi3",
                "Kesan": "Abangnya baik, kalem juga",
                "Pesan": "Lancar kuliahnya bang, semangat terus"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "Nim": "124450058",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Airan",
                "Hobbi": "Belajar",
                "Sosmed": "@aayuandriani_",
                "Kesan": "Kakaknya cantikk, baik juga",
                "Pesan": "Sehat terus kak, semangat juga"
            },
            {
                "Nama": "Dafa Elpriza",
                "Nim": "124450024",
                "Umur": "21",
                "Asal": "Bandung",
                "Alamat": "Way Kandis",
                "Hobbi": "Main Futsal",
                "Sosmed": "@dafaelpriza_",
                "Kesan": "Abangnya baik, kalem",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Juwita Sari",
                "Nim": "124450066",
                "Umur": "19",
                "Asal": "Lampung Barat",
                "Alamat": "Pemda",
                "Hobbi": "Muter-muter",
                "Sosmed": "@ju.juwitaaa_",
                "Kesan": "Kakaknya baik dan cantik",
                "Pesan": "Sehat terus kak"
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "Nim": "124450047",
                "Umur": "19",
                "Asal": "Lampung Tengah",
                "Alamat": "JL. Pulau Damar",
                "Hobbi": "Nemenin Bang Ridwan nonton tinju",
                "Sosmed": "@afdall.03",
                "Kesan": "Abangnya asik",
                "Pesan": "Lancar kuliahnya bang"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "Nim": "124550002",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang ke Metro",
                "Sosmed": "@sllbnzw_",
                "Kesan": "Kakaknya baikk dan ramah",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Muhammad Ridwan",
                "Nim": "123450091",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Belwis",
                "Hobbi": "Nonton tinju",
                "Sosmed": "@mridwaan__",
                "Kesan": "Abangnya baik dan asik",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Andra Ilham Bintang",
                "Nim": "124550060",
                "Umur": "18",
                "Asal": "Sumatera Selatan",
                "Alamat": "Kota Baru",
                "Hobbi": "Nemenin Bryan nonton tinju",
                "Sosmed": "@andra.lhm",
                "Kesan": "Abangnya ramah bangattt, asikk, dan baikk",
                "Pesan": "Semoga selalu dimudahkan dan sehat selalu"
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "Nim": "124550003",
                "Umur": "20",
                "Asal": "Nias",
                "Alamat": "Belwis",
                "Hobbi": "Live TikTok",
                "Sosmed": "@bryantel_",
                "Kesan": "Abangnya baik, ramah, dan kalem",
                "Pesan": "Sehat selalu bang dan semangat terus"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "Nim": "124550067",
                "Umur": "17",
                "Asal": "Surabaya",
                "Alamat": "Kemiling",
                "Hobbi": "Main beiblet",
                "Sosmed": "@meardhy_ghiyats",
                "Kesan": "Abangnya asik, baik juga",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "Nim": "124550055",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Memasak",
                "Sosmed": "@indahjuliaa",
                "Kesan": "Kakaknya cantik dan ramah",
                "Pesan": "sehat selalu kak dan semangat terus ya"
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "Nim": "124550023",
                "Umur": "18",
                "Asal": "Nusa Tenggara Barat",
                "Alamat": "Rajabasa",
                "Hobbi": "Nebang Pohon",
                "Sosmed": "@cacalvra",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Semangat terus kak, sehat selalu"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Fatih Ghathfaan",
                "Nim": "124550089",
                "Umur": "20",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Kota Baru",
                "Hobbi": "Bangun Pagi",
                "Sosmed": "@muhammdrafka_",
                "Kesan": "Abangnya baik dan kalem",
                "Pesan": "Semangat terus bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    minbak()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_1",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_2",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_3",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_4",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_5",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_6",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_7",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_8",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_9",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_10",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_11",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_12",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_13",
        ]
        
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik (Kepala Badan Legislatif)",
                "Nim": "123450060",
                "Umur": "20",
                "Asal": "Kuala Lumpur",
                "Alamat": "GH",
                "Hobbi": "Ke Cafe",
                "Sosmed": "@iamridhomanik",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Juesi Apridelia Saragih (Sekretaris Badan Legislatif)",
                "Nim": "123450085",
                "Umur": "19",
                "Asal": "Sikawang",
                "Alamat": "Pelangi",
                "Hobbi": "Dengerin Lagu Pilihlah Aku dari Krisdayanti",
                "Sosmed": "@j_eesie",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko (Kepala Komisi 1 Legislasi)",
                "Nim": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Ngidupin api Baleg di tiktok",
                "Sosmed": "@ddharu_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "GH Mikael Niko AS (Staff Komisi 1)",
                "Nim": "124450025",
                "Umur": "20",
                "Asal": "Pasir Sakti",
                "Alamat": "Jati Agung",
                "Hobbi": "Tidur",
                "Sosmed": "@me._kael",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Siti Sarifah Sumamah (Staff Komisi 1)",
                "Nim": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobbi": "Mancing",
                "Sosmed": "@syt.rifa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Givaro Ananta (Kepala Komisi II)",
                "Nim": "123450078",
                "Umur": "21",
                "Asal": "Lampung Barat",
                "Alamat": "Sukabumi",
                "Hobbi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Afghanis Nursholehatunnisa (Staff Komisi II)",
                "Nim": "124450042",
                "Umur": "18",
                "Asal": "Kepulauan Mentawai, Lampung",
                "Alamat": "Kadang di kos sekar kadang di kos putri",
                "Hobbi": "Memanjat",
                "Sosmed": "@afghanisnt_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Hani Qurrota Aini (Staff Komisi II)",
                "Nim": "124450020",
                "Umur": "20",
                "Asal": "City Earth",
                "Alamat": "Sukarame",
                "Hobbi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Jeremia Halim (Staff Komisi II)",
                "Nim": "124450101",
                "Umur": "20",
                "Asal": "Cibaduyut",
                "Alamat": "Teluk",
                "Hobbi": "Bernyanyi",
                "Sosmed": "@jeremia_hm",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Monica Patricia Tanjung (Kepala Komisi III)",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@monica_tjg",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan (Staff Komisi III)",
                "Nim": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobbi": "Nge gym dan koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Sekar Dini Widya Putri (Staff Komisi III)",
                "Nim": "124450082",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Pemda",
                "Hobbi": "Main sama kak nisa",
                "Sosmed": "@sekardnwp",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska (Staff Komisi III)",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@nshaysk",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_1",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_2",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_3",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_4",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_5",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_6",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_7",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_8",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_9",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_10",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_11",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_12",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_13",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_14",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_15",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_16",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_17",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_18",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_19",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_20",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_21",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_22",
        ]
        
        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "Nim": "124450104",
                "Umur": "21",
                "Asal": "Balam",
                "Alamat": "-5.386541, 105.262255",
                "Hobbi": "Nyapu wico lantai 2, lantai 3, lantai 4, lantai 5 gedung F",
                "Sosmed": "@biyokcb",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Tanty Widiyastuti (Sekretaris Departemen)",
                "Nim": "123450094",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@tvnty_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Fadil Prasetyo (Kepala Divisi Professional Skill Development)",
                "Nim": "123450048",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@fadilalfarizzii",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Manuel Frederika",
                "Nim": "124450039",
                "Umur": "20",
                "Asal": "Batam",
                "Alamat": "Way Kandis",
                "Hobbi": "Tenis meja",
                "Sosmed": "@manuelfdk_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "Nim": "124450005",
                "Umur": "17",
                "Asal": "Lampung Tengah",
                "Alamat": "Korpri",
                "Hobbi": "Tidur",
                "Sosmed": "@violaadrtr_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Risa Romadona",
                "Nim": "124450127",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Rolling skate",
                "Sosmed": "risarmdna",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Vannisa Ramadhani",
                "Nim": "124450078",
                "Umur": "19",
                "Asal": "Kepulauan Riau",
                "Alamat": "Teluk Betung",
                "Hobbi": "Nonton film action tom cruise liam nesson jackie chan",
                "Sosmed": "@vunnycaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Yulia Kristine Malau",
                "Nim": "124450119",
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Sabah Balau",
                "Hobbi": "Main alat musik",
                "Sosmed": "krnylee",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Akeyla Fairuz Shafi (Kepala Divisi Pusat Inovasi dan Kajian Akademik)",
                "Nim": "123450119",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Dengerin Musik",
                "Sosmed": "@keyashafi_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Elsa Sitorus",
                "Nim": "124450088",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Pemda",
                "Hobbi": "Rebahan",
                "Sosmed": "_els.a",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Fadya Izzatul 'Aini",
                "Nim": "124450062",
                "Umur": "20",
                "Asal": "Pringsewu",
                "Alamat": "Airan",
                "Hobbi": "Main ML",
                "Sosmed": "fadyaizzatul_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Lovianora Saragih",
                "Nim": "124450105",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@from_loviaa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "Nim": "124450092",
                "Umur": "20",
                "Asal": "Kalianda",
                "Alamat": "Kotabaru",
                "Hobbi": "Main game, tidur, dengerin musik",
                "Sosmed": "aruccy_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Sherena Florencia",
                "Nim": "124450027",
                "Umur": "19",
                "Asal": "Bengkulu Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Menunda Pekerjaan",
                "Sosmed": "sher_renna",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Razin Hafid Hamdi (Kepala Divisi Research & Development)",
                "Nim": "123450096",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobbi": "Futsal",
                "Sosmed": "@razyn.hfd",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Faiza Try Anjani",
                "Nim": "124450075",
                "Umur": "19",
                "Asal": "Padang",
                "Alamat": "Belwis",
                "Hobbi": "Belajar",
                "Sosmed": "faizaanjanii",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Gathfan Nadhif Ali",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "@gathfannad",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "Nim": "124450064",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Metro Kibang, LamTim",
                "Hobbi": "Ngoding & Ngegame",
                "Sosmed": "@apiszzaja_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "Nim": "124450053",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Campang Raya",
                "Hobbi": "Nge-gym, baca novel",
                "Sosmed": "@kelelep_comberan",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "Nim": "124450087",
                "Umur": "19",
                "Asal": "Sumsel",
                "Alamat": "Sukarame",
                "Hobbi": "Nari",
                "Sosmed": "@melva_fbrt",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Stafiqul Falakh",
                "Nim": "124450099",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Membaca",
                "Sosmed": "@syaafiqui",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "Nim": "124450115",
                "Umur": "20",
                "Asal": "Kota Bumi",
                "Alamat": "Rajabasa",
                "Hobbi": "Nongkrong",
                "Sosmed": "@henryferdianto",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_1",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_2",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_3",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_4",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_5",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_6",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_7",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_8",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_9",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_10",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_11",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_12",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_13",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_14",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_15",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_16",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_17",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_18",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_19",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_20",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_21",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_22",
        ]
        
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "Nim": "123450069",
                "Umur": "06 Maret 2005 (Lahir)",
                "Asal": "LAMPUNG!!!",
                "Alamat": "Teluk Betung Selatan",
                "Hobbi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Nabyla Sharfina",
                "Nim": "123450008",
                "Umur": "20 Tahun",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobbi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "Nim": "123450032",
                "Umur": "15 September 2004 (Lahir)",
                "Asal": "tetangga kadep",
                "Alamat": "belwis",
                "Hobbi": "memancing keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Khoirul",
                "Nim": "1234500",
                "Umur": "27 January 2005 (Lahir)",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobbi": "main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Selma Siti Aisyah",
                "Nim": "123450044",
                "Umur": "20 tahun",
                "Asal": "lampung",
                "Alamat": "balam",
                "Hobbi": "jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "Nim": "124450028",
                "Umur": "20 tahun",
                "Asal": "sini",
                "Alamat": "jauh pokoknya",
                "Hobbi": "tidur",
                "Sosmed": "@kshigf",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Indah Khairunnisa",
                "Nim": "124450077",
                "Umur": "20 Tahun",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Bima Ekayasa",
                "Nim": "124450106",
                "Umur": "25 April 2006 (Lahir)",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobbi": "berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "Nim": "124450113",
                "Umur": "23 July 2006 (Lahir)",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobbi": "lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "Nim": "124450083",
                "Umur": "cepuyuh tayun",
                "Asal": "ikut kadep",
                "Alamat": "love earth",
                "Hobbi": "jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Yollanda Agustina",
                "Nim": "124450024",
                "Umur": "Tanya bang Henry",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobbi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "Nim": "124450022",
                "Umur": "20 tahun",
                "Asal": "palembang",
                "Alamat": "bebas",
                "Hobbi": "ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Fathya Intami Gusda",
                "Nim": "123450095",
                "Umur": "25 tahun",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobbi": "baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "Nim": "124450052",
                "Umur": "21 Tahun (Σk=1^4 k + ∫o^2 2x dx + √81 + log10(100))",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobbi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Danil N Fadillah",
                "Nim": "124450103",
                "Umur": "31 Desember 2006 (Lahir)",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobbi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Favian Arkaanda",
                "Nim": "124450021",
                "Umur": "05 Mei 2006 (Lahir)",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobbi": "ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "Nim": "124450081",
                "Umur": "((15<<1) & 31) ⊕ 10 / 666",
                "Asal": "situlah",
                "Alamat": "pohon mulia",
                "Hobbi": "nyari hobi",
                "Sosmed": "@zydddddd_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Alfaya Abiyyi",
                "Nim": "124450006",
                "Umur": "nelson piquet",
                "Asal": "balam",
                "Alamat": "balam",
                "Hobbi": "makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Rizaldi",
                "Nim": "124450093",
                "Umur": "Masih muda lah (Hari Jum'at)",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "Sosmed": "@jaldii._",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "Nim": "124450074",
                "Umur": "20 tahun",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobbi": "nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Asri Meilani",
                "Nim": "124450010",
                "Umur": "20 tahun",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobbi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Ahmad Rizky",
                "Nim": "123450050",
                "Umur": "21 Tahun ini alhamdulillah",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobbi": "ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "",
                "Pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    