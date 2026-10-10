import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
 
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
            "Departemen Medkraf"
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
            "people-fill"
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
            "nav-link-selected": {"background-color": "#3FBAD8"},
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
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/thumbnail?id=1CW2dOGRDAdmxS_dOx3aBg9l8uz5oXtbo&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CXE7XIPSOTLMp3k-JL3Hfvritll9hZy_&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CZrj0IxMeoHzl4qXwQtlpC7S39d-Jq_J&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CWvGVLqdZ_VkpeUFTvSd30c5dsGUs2S8&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CYKfd-hQFF5oiKh809wAXjHB9tclJ9V-&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CWttHpQO9l_YmNTticXwrEA1fZN06mt&sz=w1000"
          ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450103",
                "Asal" : "Batam",
                "Alamat" : "Sekretariat HMSD",
                "Hobi": "Push imo",
                "Umur" : "17",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "bang ginda seru banget, ramah, dan sabar",
                "Pesan" : "semangat terus abang buat TA nya"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "bang aqil seru dan menginspirasi.",
                "Pesan" : "keren selalu bang sekjen"
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Cantik bangett lucuu dan gemes cara ngomongnya lucu banget",
                "Pesan" : "Sehat dan sukses selalu ya Kak, terima kasih"
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "ternyata sama sama dari batam",
                "Pesan" : "semangat bang mengerjakan TA."
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "cantik, baik dan ramah",
                "Pesan" : "Tetap jadi kakak yang ramah, ya, Kak."
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "cantik, baik dan ramah",
                "Pesan" : "Sehat dan sukses selalu ya Kak, terima kasih"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

#INTERNAL
if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
           "https://drive.google.com/thumbnail?id=1Zd9hjH9A9G61kq0Kl02uJB0YA44E9DvW&sz=w1000"
           "https://drive.google.com/thumbnail?id=1EhcTUBIYd-F6_XB3flycrh1OlpJahubf&sz=w1000",
           "https://drive.google.com/thumbnail?id=1E2gdrKtKhZ2XqqoS7cBF4LJmsztzIrT&sz=w1000",
           "https://drive.google.com/thumbnail?id=1F2OFxZj6rvyRSjNM86uFTIHIfp59HX&sz=w1000",
           "https://drive.google.com/thumbnail?id=1EtInaQAuVvmHRIzlwSicSFpblXHFXBfE&sz=w1000",
           "https://drive.google.com/thumbnail?id=1EwWd0Z7U0K4PDgFSSamleh4RnUig3jJP&sz=w1000",
           "https://drive.google.com/thumbnail?id=1E2qSOIWUGjrtOcuvDCeoo8EzgXdAtk1N&sz=w1000",
           "https://drive.google.com/thumbnail?id=1FAiG-qYlbJJiuLblHQELzvqxhJyE5-2T&sz=w1000",
           "https://drive.google.com/thumbnail?id=1E9W-SnnvTVQ3uloc9HhAZuJjED4wUL2y&sz=w1000",
           "https://drive.google.com/thumbnail?id=1EiHCFQHlwF9c7r_0PXh5Xvx3rQRcaPA8&sz=w1000",
           "https://drive.google.com/thumbnail?id=1EGxQhD4at2l1SH5tcW-pI5HE45GSGBWO&sz=w1000",
           "https://drive.google.com/thumbnail?id=1FFdqPD-UP82w_At5hYHwflalVZFhQ2QI&sz=w1000",
           "https://drive.google.com/thumbnail?id=1F0ZxoYM2CcXBGFI1OscqfjcEtSr3a9a_&sz=w1000",
           "https://drive.google.com/thumbnail?id=1F3VL0IpscbSUD1q_RIUfzvMi_7esvjb&sz=w1000",
           "https://drive.google.com/thumbnail?id=1FLLf0IhTsRS8UGzxRrFF8It3hYQ94Y3&sz=w1000",
           "https://drive.google.com/thumbnail?id=1Ep0r9-o4rdKIDwxbijw1f5de2bxxxoY2&sz=w1000",
           "https://drive.google.com/thumbnail?id=1F2mNscGCnav4_tTPMF3oJX4IGnndlN4W&sz=w1000"
        ]
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "lucu dan berwibawa.",
                "Pesan": "semangat bang mengerjakan TA."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Cara bicaranya lembut dan cantik.",
                "Pesan": "semangat kuliahnya kak."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "talkactive dan lucu",
                "Pesan": "selalu ceria kak hana."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "oh ini abang yang selalu di dasmaskus .",
                "Pesan": "keren terus bang semangat TA nya."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "cantik, baik dan ramah.",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "cantik, baik dan ramah.",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "keren dan cakep.",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "cantik, baik dan ramah.",
                "Pesan": "Semangat kuliahnya"
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "ramah bintang 5.",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "cantik, baik dan ramah",
                "Pesan": "Semangat kuliahnya"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "ramah dan imut",
                "Pesan": "Semangat kuliahnya"
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "cantik, baik dan ramah",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "cantik, baik dan ramah",
                "Pesan": "Semangat kuliahnya"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "cantik, baik dan ramah",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "lucu dan ramah",
                "Pesan": "Semangat kuliahnya."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Ramah ke semua orang. dan baik cantik",
                "Pesan": "Semangat kuliahnya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()



# MINBAK
if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
               "https://drive.google.com/thumbnail?id=1G4FL5_7GyDYE2h0_svyynjpelBUpuC5E&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FU2P0xmiCg2mrow4VMEtqFMKMdzgE9j&sz=w1000",
               "https://drive.google.com/thumbnail?id=1G8msJUickmLU7niB3fNsunEDMJY_Pkz&sz=w1000",
               "https://drive.google.com/thumbnail?id=1GBqQFrKmEWBLy7J6XLjBx7YVFUPxC61n&sz=w1000",
               "https://drive.google.com/thumbnail?id=1GHOZIzmViOg8U5sTJrjbrMCWP5yQwts&sz=w1000",
               "https://drive.google.com/thumbnail?id=1G60ebJ3iErzCwNTiclhkg2FZ-wTlaVI2&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FOZR-yBKqILc6cp80LMZse6fQr0TaFg-&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FkfdzWnBCZvmVp8zj22EH1kvaJYI7cbV&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FhBnhrxId3k6cA8t86A4IddU4Ax_5klNw&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FYNCMa3QbgeMaMy7KZKwZu-4YxKxG2BJ&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FZOXL0ljn4ao-CB4O8vEQViZ8gtQGz8b&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FM9a7HYdqCW_JS6kb8xAjRxuM-K9Q-yo&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FisNLismnAhrI4ID_6NxJo9F8A6bTOLr&sz=w1000",
               "https://drive.google.com/thumbnail?id=1FbYbK_Uo2M6htCk1_QXM6ayYV8J0ASMI&sz=w1000",
               "https://drive.google.com/thumbnail?id=1G5-I8iW0wlt1TRwMO5VR9k6p0W97JlJr&sz=w1000"
            ]

        data_list = [
            {
                "Nama": "Kevin Antonio Junior",
                "NIM" : "123450109",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Panjang, Bandar Lampung",
                "Hobi": "Balap",
                "Umur" : "21",
                "Sosmed" : "@kevinaj__",
                "Kesan" : "keren banget dan tinggi banget",
                "Pesan" : "Semangat kuliahnya.."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "cantik banget.",
                "Pesan" : "Semangat kuliahnya. cantik teruss"
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi",
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Orangnya kalem dan serius",
                "Pesan" : "Semangat kuliahny keren teruss"
            },
            {
                "Nama": "Ayu Andriani Parlina Wati",
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "keliatan rajin dan lucu.",
                "Pesan" : "Semangat kuliahnya. cantik teruss."
            },
            {
                "Nama": "Dafa Elpriza",
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "ramah sekali.",
                "Pesan" : "Semangat kuliahnya. keren teruss."
            },
            {
                "Nama": "Juwita Sari",
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "imut dan lucu sekali",
                "Pesan" : "Semangat kuliahnya. cantik teruss."
            },
            {
                "Nama": "Muhammad Afdal Lutfi",
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "ramah poll asik juga.",
                "Pesan" : "Semangat kuliahnya. keren teruss."
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "cantik banget manis juga.",
                "Pesan" : "Semangat kuliahnya. cantik teruss"
            },
            {
                "Nama": "Muhammad Ridwan",
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : " ramah dan keren",
                "Pesan" : "Semangat kuliahnya. keren teruss"
            },
            {
                "Nama": "Andra Ilham Bintang",
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : " baik bangettt dan keren bangett.",
                "Pesan" : "Semangat kuliahnya. jadi orang teruss."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua",
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "lucuuu dan imut.",
                "Pesan" : "Semangat kuliahnya. keren teruss"
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy",
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "cool sekali keren",
                "Pesan" : "Semangat kuliahnya. keren teruss"
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi",
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Pembawaannya adem dan  kakaknya fadyl",
                "Pesan" : "Semangat kuliahnya. cantik teruss "
            },
            {
                "Nama": "Jacinda Kesya Alvara",
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "kecil banget fashion nya oke cantik.",
                "Pesan" : "Semangat kuliahnya. cantik teruss"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "ramah dan baik.",
                "Pesan" : "Semangat kuliahnya. cantik teruss"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [

         "https://drive.google.com/thumbnail?id=12oMbNPXXTVKrwyC_TDQV87AG7vw-9_OP&sz=w1000",
         "https://drive.google.com/thumbnail?id=12ExEF78HIECdr58V1tk4WYFIBzfzfrEo&sz=w1000",
         "https://drive.google.com/thumbnail?id=1GIOhbFzno6gby2an47RMBXJd7wm8pEcz&sz=w1000",
         "https://drive.google.com/thumbnail?id=11ffvbX2CjWa2HTq5scQP8WTllauiURPa&sz=w1000",
         "https://drive.google.com/thumbnail?id=12359hqXccdvJao_9Lt2_ek0JEbelUi8R&sz=w1000",
         "https://drive.google.com/thumbnail?id=11su8LZC4SAvt4dAHB7w6Cj5ZVizGUpbY&sz=w1000",
         "https://drive.google.com/thumbnail?id=11q8y-7m2PO008Wfly9BBMBF5qtxhkNbH&sz=w1000",
         "https://drive.google.com/thumbnail?id=1GlkONip6Tv6zETETR4YZiESsmaBI5Akb&sz=w1000",
         "https://drive.google.com/thumbnail?id=12mkGropXd2emtSH50j_7b00-g10LHsFX&sz=w1000",
         "https://drive.google.com/thumbnail?id=12mkGropXd2emtSH50j_7b00-g10LHsFX&sz=w1000",
         "https://drive.google.com/thumbnail?id=12tlPZ8ti7mxtW1jS7-U94bFWcBaXSKBV&sz=w1000",
         "https://drive.google.com/thumbnail?id=12xlP31xEqSdHHM6Y14A91BK7ov_6kZ5G&sz=w1000",
         "https://drive.google.com/thumbnail?id=12u5wOexE0gBjBvAUl6s6_41EX8ruNTfD&sz=w1000",
         "https://drive.google.com/thumbnail?id=1GUht6T_xrgAn1l-CzgeDKZQJPGrskv12&sz=w1000",
         "https://drive.google.com/thumbnail?id=12NgSRrzw6_ep3-4SyyD-fmgdxx_xLcl6&sz=w1000",
         "https://drive.google.com/thumbnail?id=1GVBs7Kvt6p0pY-ffWsUyCkhRhG9ANOVr&sz=w1000",
         "https://drive.google.com/thumbnail?id=12PZPt4aS4K-GdKOGJ1fXLKWXI_MpMp7&sz=w1000",
         "https://drive.google.com/thumbnail?id=12GDzxf4_XTnqBQNXn1qH1VouW6vloBL&sz=w1000",
         "https://drive.google.com/thumbnail?id=12fnBtXySikaqBFPKXqkYaDy9xyR4Frhe&sz=w1000",
         "https://drive.google.com/thumbnail?id=14lgirqXHiw-9Ic-Pieshin5-IKTD_wEV&sz=w1000",
         "https://drive.google.com/thumbnail?id=12SMd5fl03xQQash8U9bWi-N1KLXjlKI6&sz=w1000",
         "https://drive.google.com/thumbnail?id=12UtyUk3_IAS9COJU2KjbQw2dCs0FIE9F&sz=w1000"
]

        data_list = [
            {
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Gayanya santai dan tengil",
                "Pesan" : "asik selalu bang"
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Vibes-nya tuh adem bgt, tapi giliran detail-detail kecil pasti dia paling peka.",
                "Pesan" : "lucu selalu ya."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "sangat inspiratif dan keren",
                "Pesan" : "keren selalu bang"
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : " keren dan ramah",
                "Pesan" : "Tetap semangat bang kuliahnya."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri",
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Vibes-nya tuh adem bgt, tapi giliran detail-detail kecil pasti dia paling baik.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Risa Romadona",
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Aktif dan berani mencoba hal baru.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Ramah dan selalu terlihat ceria.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Yulia Cristine Malau",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Sopan dan menghargai orang lain.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi",
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Elsa Sitorus",
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Murah senyum dan enak diajak bicara.",
                "Pesan" : "Semangat kuliahnya kak.."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini",
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "Pesan" : "Semangat kuliahnya kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Humoris dan gampang bikin tawa.",
                "Pesan" : "Jangan lupa tetap fokus kuliah juga, bang"
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Rapi dan selalu tampil percaya diri.",
                "Pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "Pesan" : "Terus ajak kami aktif bersama, bang"
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "Pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali",
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Santai tapi tetap bertanggung jawab.",
                "Pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "Nama": "Hafidz Wahdiansyah",
                "NIM" : "tanya lintar",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "imut kayak kucing.",
                "Pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "abang kocak mentor ale rb.",
                "Pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "Nama": "Melva Shaprina Febrianti",
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Ceria dan mudah menyesuaikan diri.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "Pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "Nama": "Rifky Henry Ferdianto",
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "keren banget.",
                "Pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                gambar_urls = [
         "https://drive.google.com/thumbnail?id=16NMJZ-r564jd6Elsd2mSPY1l0OcUTPQs&sz=w1000",
         "https://drive.google.com/thumbnail?id=16t8oQsAZEuD8uQ7krdRZACaU0k02yyUJ&sz=w1000"
]
        ]

        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "NIM" : "123450082",
                "Asal" : "Payakumbuh, Sumatera Barat",
                "Alamat" : "Belum Tahu",
                "Hobi": "Rebahan",
                "Umur" : "20",
                "Sosmed" : "@naylasalsabilaa._",
                "Kesan" : "Bicaranya halus dan enak diajak ngobrol.",
                "Pesan" : "Tetap jadi kakak yang sabar, ya, Kak."
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM" : "123450028",
                "Asal" : "Bekasi dan Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "keren bangett pertama kali ketemu pas kelas kdp",
                "Pesan" : "Terus jadi teman berbagi yang nyaman, Kak."
            },
            {
                "Nama": "Labo John Nuel Napitupulu",
                "NIM" : "37",
                "Asal" : "Medan, Jakut, Palembang",
                "Alamat" : "Belum Tahu",
                "Hobi": "Berburu burung",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Wawasannya luas dan cerita pengalamannya seru.",
                "Pesan" : "Sering-sering bagi cerita perjalananmu, Kak."
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ngoding",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Fokus dan tekun kalau sudah mengerjakan sesuatu.",
                "Pesan" : "Semoga ilmu codingmu terus berkembang, Kak."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "NIM" : "124450104",
                "Asal" : "Bekasi",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ngejahilin mama",
                "Umur" : "18",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Usilnya menyenangkan dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "NIM" : "124450031",
                "Asal" : "Sibolga",
                "Alamat" : "Belum Tahu",
                "Hobi": "Jahilin Felisya",
                "Umur" : "18",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Jahilnya bikin akrab, tapi tetap tahu batas.",
                "Pesan" : "Jaga kekompakan sama teman-teman, Kak."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "NIM" : "123450086",
                "Asal" : "Bandung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Bimbingan TA",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Gigih dan tidak mudah menyerah.",
                "Pesan" : "Semoga TA-nya lancar dan cepat selesai, Kak."
            },
            {
                "Nama": "Allisha",
                "NIM" : "124450019",
                "Asal" : "Rahim ibu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah",
                "Umur" : "6",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Gampang akrab dan setia sama teman-temannya.",
                "Pesan" : "Tetap jadi teman yang asyik buat semua, Kak."
            },
            {
                "Nama": "Alya Ramadhanti",
                "NIM" : "124450091",
                "Asal" : "Kota banyak sawit",
                "Alamat" : "Belum Tahu",
                "Hobi": "Apa aja",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Fleksibel dan mau mencoba apa saja.",
                "Pesan" : "Jangan berhenti penasaran sama hal baru, Kak."
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Rajin dan disiplin dalam belajar.",
                "Pesan" : "Bagi tips belajarmu ke kami juga, ya, Kak."
            },
            {
                "Nama": "Difanya Husakina",
                "NIM" : "124450043",
                "Asal" : "Deket Kebun Teh",
                "Alamat" : "Belum Tahu",
                "Hobi": "Alhamdulillah Dzikir dan sholawatan",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Tutur katanya santun dan menyejukkan.",
                "Pesan" : "Tetap istiqamah dan jadi teladan, Kak."
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ballet",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Anggun dan penuh percaya diri.",
                "Pesan" : "Terus kejar hobimu dengan semangat, Kak."
            },
            {
                "Nama": "Raihana Adelia Putri",
                "NIM" : "123450041",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur" : "20",
                "Sosmed" : "@r.hanaap",
                "Kesan" : "Tenang dan pandai merangkai kata.",
                "Pesan" : "Tetap menulis dan bagikan idemu ke kami, Kak."
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Kalem dan tidak banyak bicara, tapi tulus.",
                "Pesan" : "Jangan sungkan bergabung ngobrol bareng, Kak."
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "NIM" : "098",
                "Asal" : "Lampung Selatan, Natar",
                "Alamat" : "Belum Tahu",
                "Hobi": "Scroll Fesbuk",
                "Umur" : "20",
                "Sosmed" : "@edsel_0712",
                "Kesan" : "Santai dan punya selera humor yang khas.",
                "Pesan" : "Tetap jadi kakak yang gampang diajak bercanda, Kak."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "NIM" : "124450085",
                "Asal" : "Bekasi",
                "Alamat" : "Belwis",
                "Hobi": "Lari",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Energik dan selalu menyemangati sekitar.",
                "Pesan" : "Terus tularkan semangat larimu ke kami, Kak."
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belum Tahu",
                "Hobi": "Makan tempe mentah",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Apa adanya dan bikin suasana tidak kaku.",
                "Pesan" : "Tetap jadi diri sendiri, ya, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Sopan dan selalu menghargai orang lain.",
                "Pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()