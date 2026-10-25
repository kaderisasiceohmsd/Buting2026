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
            "icon": {"color": "black", "font-size": "16px"},
            "nav-link": {
                "font-size": "13px",
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
            "https://drive.google.com/thumbnail?id=1CXE7XlPSOTLMp3k-JL3HfvritIl9hZy_&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CZrj0IxMeoHzl4qXwQtIpC7S39d-Jq_J&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CWvGVLqdZ_VkpeUFtvSd3Oc5dsGUs2S8&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CYKfd-hQFF5oiKh809wAXjHB9tclJ9V-&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CWttHpQO9I_YmNTticXwrEA1xFzN06mt&sz=w1000"
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
                "https://drive.google.com/thumbnail?id=1EhcTUBlYd-F6_XB3flYcrh1OlpJahubf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1E2gdrKtKhZ2XqqroS7cBF4LJmsztzlrT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F2OFxZj6rvyRSiNM8t6uFTIHIIfp59HX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EtlnaQAuVvmHRIzlwSicSFpblXHFXBfE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EwWd0Z7U0K4PDgFSSamIeh4RnUig3jJP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1E2qSOlWUGjrtOcuvDcEoo8EzgXdAtk1N&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FAiG-qYIbJJiuLbIHQELzvqxhJyE5-2T&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FAiG-qYIbJJiuLbIHQELzvqxhJyE5-2T&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EiHCFQHlwF9c7r_0PXh5Xvx3rQRcaPA8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EGxQhD4at2l1SH5tcW-pI5HE45GSGBWO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FFdqPD-UP82w_At5hYHwflalVZfHQ2Ql&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F0ZxoYM2CcXBGFI1OscqfjcEtSr3a9a_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F3VL0IpscbSUD1q_RIUfzvvMi_7esvjb&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ShUmz5bC98hRKz4NuyNYX1xFAg5ONyTg&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ep0r9-o4rdKIDwxbijw1f5de2bxxxoY2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F2mNscGCnav4_tTPMF3oJX4IGnndlN4W&sz=w1000", 

 ]
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "123450106",
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Way Halim",
                "Hobi": "Ngeledek Orang",
                "Sosmed": "@haikalsbln",
                "Kesan": "lucu dan berwibawa.",
                "Pesan": "semangat bang mengerjakan TA."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Suka Nolong Orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Cara bicaranya lembut dan cantik.",
                "Pesan": "semangat kuliahnya kak."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Sumatera Utara, kisaran city",
                "Alamat": "Sukarame",
                "Hobi": "Ngabarin Orang Tua",
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
                    "https://drive.google.com/thumbnail?id=1G4FL5_7GyDYE2h0_svyynjpelbUPuC5E&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FU2P0xmiCg2mrow4VMEtqgFMKMdzgE9j&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1G8msJUiCkmLmU7niB3fNsunEDMJY_Pkz&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1GBqQFrKmEWBLy7J6XLjBx7YVFUPxC61n&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1GHOZlzmViOg8U5sTJrjbhrMCWP5yQwts&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1G60ebJ3iErzCwNTiclhkg2FZ-wTlaVI2&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FOZR-yBKqILc6cp80LMZse6fQr0TaFg-&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FkfdzWnBCZvmVp8zj22EH1kvaJYI7cbV&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FhBnhrxl3k6cA8t86A4lDdU4Ax_5kINw&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FYNCMa3QbgeMaMy7KZKwZu-4YxKxG2BJ&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FZOXL0ljn4ao-CB4O8vEQViZ8gtQGz8b&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FM9a7HYdqCW_JS6kb8xAjRxuM-K9Q-yo&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FisNLismnAhrI4ID_6NxJo9F8A6bTOLr&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1FbYbK_Uo2M6htCk1_QXM6ayYV8J0ASMl&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1G5-l8iW0wlt1TRwMO5VR9k6p0W97JlJr&sz=w1000"
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
                "Pesan" : "Semangat kuliahnya teruss"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                    "https://drive.google.com/thumbnail?id=12ExeF78HlECdr58V1tk4WYFIBzfzfrEo&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12oMbNPXXTVKrwyC_TDQV87AG7vw-9_OP&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1GIOhbFzno6gby2an47RMBXjD7wm8peCz&sz=w1000",
                    "https://drive.google.com/thumbnail?id=11ffvbX2CJWa2HTq5scQP8WTllauiURPa&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12359hqXccdvJao_9Lt2_eK0JEbeIUi8R&sz=w1000",
                    "https://drive.google.com/thumbnail?id=11su8lZC4SAvt4dAHB7w6Cj5ZVizGUpbY&sz=w1000",
                    "https://drive.google.com/thumbnail?id=11q8y-7m2pOO08WfIy9BBMBF5QtxhkNbH&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1cxSQXQtwVulbcQCUqNlG8EtuXbgKrv48&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12mkGRopXd2emtSH5Oj_7bO0-g10LHsFX&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12sTFzXKCXEFTxUSribgpqB7zlbfhWipO&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12tlPZ8ti7mxtW1jS7-U94bFWcBaXsKBV&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12xIP31xEqSdHHM6Y14A91BK7ov_6kZ5G&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12u5wOexE0gBjBvAUl6s6_41EX8ruNTfD&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1GUht6T_xrgAn1l-CzgeDKZQJPGRskv12&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12NgSRrzw6_ep3-4SyyD-fmgdxx_xLcl6&sz=w1000",
                    "https://drive.google.com/thumbnail?id=1GVBs7Kvt6p0pY-ffWsUyCkhRhG9ANOVr&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12PZPt4aS4SK-GdKOGJ1fXLKWXI_MpMp7&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12GDzxf4_TXtnqBQNXn1qH1VouW6vIoBL&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12fnBtXySikaqBFPKXqkYaDy9xyR4fRhe&sz=w1000",
                    "https://drive.google.com/thumbnail?id=14lgirqXHiw-9Ic-Pieshin5-IKTD_wEV&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12SMd5fI03xQQash8U9bWi-N1KLXjlKI6&sz=w1000",
                    "https://drive.google.com/thumbnail?id=12UtyUk3_lAS9COJU2KjbQw2dCs0FIE9F&sz=w1000"
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
                "Kesan" : "saya kira dulu nama panggilan abang tu bang banyu,ternyata bang bio",
                "Pesan" : "asik selalu bang tengil selalu"
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
                "https://drive.google.com/thumbnail?id=16NMJZ-r564jd6EIsd2mSPY1l0OcUTPQs&sz=w1000",
                "https://drive.google.com/thumbnail?id=16t8oQsAZEuD8uQ7krdRZAcaU0k02yyUJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=168eRNr5rDLvl-ETEJTK4halUGK-WJZiX&sz=w1000",
                "https://drive.google.com/thumbnail?id=15zshX8Ft9TUIjhOfk0fQzPkuhVmbcWXW&sz=w1000",
                "https://drive.google.com/thumbnail?id=163EdVh3TGLqOauc_FgZwKZgx2qcYAGPF&sz=w1000",
                "https://drive.google.com/thumbnail?id=16tZ1W1llUkniAI2_GYZ76FssWitX5Yqk&sz=w1000",
                "https://drive.google.com/thumbnail?id=16Su1ClJxZCjoP-rCdwVw4fVnp4gNO_rD&sz=w1000",
                "https://drive.google.com/thumbnail?id=16TarxwAa_w_gRXflIkEM-CoyR6fkO1Ot&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OOHz2hJtMXDVLRkvwV5PdqhPYX1N03pt&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=15y2llzEWnP-9j7x8kEMtH1BPc5A7f6tJ&sz=w1000",
                "https://drive.google.com/thumbnail?id=174l-kJ_-RZPAjzQWJst9GfAqBd8SBNSz&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OIz5LZc4qJ-CwctGkc7uFQ-N4Sv4MQJV&sz=w1000",
                "https://drive.google.com/thumbnail?id=151IfZrmIkwpCegnJ23ogcXvaN1gukZmq&sz=w1000",
                "https://drive.google.com/thumbnail?id=16PLatjF0DeYkmwD_VrDm42_CDqbUn-7E&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OOPSa6J9FA060oXKOh7MTmIa2N18tkTX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OK4swl9uEydcEk4jR1MqCmnO8fzjcSGz&sz=w1000"
]
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa", 
                "NIM" : "123450082",
                "Asal" : "Payakumbuh, Sumatera Barat",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "20",
                "Sosmed" : "@naylasalsabilaa._",
                "Kesan" : "Bicaranya halus dan enak diajak ngobrol.",
                "Pesan" : "Tetap jadi kakak yang sabar, ya, Kak."
            },
            {
                "Nama": "Donna Maya Puspita", 
                "NIM" : "123450028",
                "Asal" : "Bekasi",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Pendengar yang baik dan selalu tulus.",
                "Pesan" : "Terus jadi teman berbagi yang nyaman, Kak."
            },
            {
                "Nama": "Labo John Nuel Napitupulu", 
                "NIM" : "123450037",
                "Asal" : "Medan",
                "Alamat" : "Belwis",
                "Hobi": "Motoran",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Wawasannya luas dan cerita pengalamannya seru.",
                "Pesan" : "Sering-sering bagi cerita perjalananmu, Kak."
            },
            {
                "Nama": "Anash Tasya Ausyaqila", 
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Way Halim",
                "Hobi": "Nonton",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Fokus dan tekun kalau sudah mengerjakan sesuatu.",
                "Pesan" : "Semoga ilmu codingmu terus berkembang, Kak."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho", 
                "NIM" : "124450104",
                "Asal" : "Lampung Timur",
                "Alamat" : "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur" : "19",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Usilnya menyenangkan dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama", 
                "NIM" : "124450031",
                "Asal" : "Jawa Barat",
                "Alamat" : "Korpri",
                "Hobi": "Foto Orang",
                "Umur" : "21",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Jahilnya bikin akrab, tapi tetap tahu batas.",
                "Pesan" : "Jaga kekompakan sama teman-teman, Kak."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari", 
                "NIM" : "123450086",
                "Asal" : "Karawang",
                "Alamat" : "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Gigih dan tidak mudah menyerah.",
                "Pesan" : "Semoga TA-nya lancar dan cepat selesai, Kak."
            },
            {
                "Nama": "Allisha", 
                "NIM" : "124450019",
                "Asal" : "Kayangan",
                "Alamat" : "Heaven",
                "Hobi": "Mancing",
                "Umur" : "16",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Gampang akrab dan setia sama teman-temannya.",
                "Pesan" : "Tetap jadi teman yang asyik buat semua, Kak."
            },
            {
                "Nama": "Alya Ramadhanti", 
                "NIM" : "124450091",
                "Asal" : "Jambi",
                "Alamat" : "Airan",
                "Hobi": "Jalan-jalan",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Fleksibel dan mau mencoba apa saja.",
                "Pesan" : "Jangan berhenti penasaran sama hal baru, Kak."
            },
            {
                "Nama": "Bunga Clarisa Sefa", 
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Rajin dan disiplin dalam belajar.",
                "Pesan" : "Bagi tips belajarmu ke kami juga, ya, Kak."
            },
            {
                "Nama": "Difanya Husakina", 
                "NIM" : "124450043",
                "Asal" : "Pagar Alam",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Tutur katanya santun dan menyejukkan.",
                "Pesan" : "Tetap istiqamah dan jadi teladan, Kak."
            },
            {
                "Nama": "Nazlah Auliya", 
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Berenang",
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
                "NIM" : "124450061",
                "Asal" : "Surabaya",
                "Alamat" : "Sukarame",
                "Hobi": "-",
                "Umur" : "21",
                "Sosmed" : "@daffascript",
                "Kesan" : "Kalem dan tidak banyak bicara, tapi tulus.",
                "Pesan" : "Jangan sungkan bergabung ngobrol bareng, Kak."
            },
            {
                "Nama": "Edsel Adya Pradipta", 
                "NIM" : "124450098",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Natar",
                "Hobi": "Nonton Anime",
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
                "Hobi": "Tidur",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Energik dan selalu menyemangati sekitar.",
                "Pesan" : "Terus tularkan semangat larimu ke kami, Kak."
            },
            {
                "Nama": "Shafa Delaila Azzahra", 
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Apa adanya dan bikin suasana tidak kaku.",
                "Pesan" : "Tetap jadi diri sendiri, ya, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman", 
                "NIM" : "124450112",
                "Asal" : "Lampung Timur",
                "Alamat" : "Rajabasa",
                "Hobi": "Begong",
                "Umur" : "18",
                "Sosmed" : "@xifasky",
                "Kesan" : "Sopan dan selalu menghargai orang lain.",
                "Pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()

if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1D1a1fpnAO7ZnOkCicEh1V2C_vgi8bWeZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DaoMiq_hZkw6HT-dNvm6zkYfv3uEgDDG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D9HryEonUFU-rdRcBoDv_x9yCRV_w_D5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DY2Njz7xD0pFb85RDw5ZKHG2zplOeP_T&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DZO3cJy8G0EbTYkzFmO36lxmbch0SV4v&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DBmEyDl2YWnt1hpQygobVY5g1tSRg_As&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D2BTae-lPZ7-OqmzaQHiASngF4qA53O6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Oia-8o9BVX0Wk-pI35Qo0ofupT4Fn8ba&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D_b5p4GbAlu3aS1fNeUn3ccoTUP2p8ju&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DUSUSqp4u3FOA-r6O4-caRUncxUUiSq3&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DKqXHwR-AWiAag-XgvkNx_zeaZdTx8PC&sz=w1000"
]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobi": "Mencari dan membaca jurnal, mencari pak lucy",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Orangnya santai dan enak diajak ngobrol, waktu itu ketemu pas ssd jualan di SF",
                "Pesan": "saya doakan semoga pak lucy selalu bs dihubungi dengan baik bang."

            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Ramah daan baik bangettt gemes.",
                "Pesan": "semangat TA nya kakak."    
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "kakaknya introvet yh kayakyaa... soft bgt suaranya",
                "Pesan": "Tetap jadi diri sendiri dan semoga selalu ada film Marvel baru yang seru ditonton." 
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Kalem dan bisa diandalkan, apalagi kalau urusan teknis.",
                "Pesan": "Terus semangat belajar dan semoga container-nya selalu jalan lancar tanpa error."
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Gigih dan pekerja keras, orangnya juga seru.",
                "Pesan": "Semangat terus dalam berusaha, tapi jangan lupa istirahat ya."
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Ramah dan gampang akrab, rekomendasi dramanya pasti banyak.",
                "Pesan": "Tetap semangat kuliahnya, dan jangan begadang kebanyakan gara-gara maraton drakor."
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Orangnya tenang dan menyenangkan.",
                "Pesan": "Semangat kuliahnya, semoga tidurnya selalu cukup dan nyenyak."
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Ceria dan punya semangat kerja yang tinggi.",
                "Pesan": "Tetap semangat dan jaga kesehatan, semoga usahanya lancar terus."
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "abang palembang jg yh ternyata.",
                "Pesan": "semangat TA Ny bang."
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Sabar dan santai, enak diajak ngobrol.",
                "Pesan": "Semoga hasil pancingannya selalu melimpah dan kuliahnya lancar."
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Ceria dan bikin suasana jadi lebih hangat.",
                "Pesan": "Tetap jadi pribadi yang ceria dan semangat terus kuliahnya."
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Ramah dan seru diajak ngobrol, terutama soal film.",
                "Pesan": "Tetap semangat dan semoga selalu ada waktu buat nonton film favorit."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1Bec-EP3Moijco8NhCZAHbQVCvCjkfkvP&sz=w1000", 
                "https://drive.google.com/thumbnail?id=1C8JpBgkUlbxRe8BKENY8nuO4g2F1xkP7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BpwbJ6WqL4mBxmUMOhrbMFk1BzjVPkDX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CRqnkOQ4MJ2zL4hoTFkTRxIb6lPE1oTM&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CL4hLQRkGvCMs0nRCH6IkNHF-ePUFdiq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BuRw8ux4dBDs6N5XRgmUK5hnN6okn66Q&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Bon5T0M0kMGQD8p-6esdelxfPSF3G9RS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1C9aHI-Pku0FQ5S4GPiwhsi66Ni7kxgWk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CT0oMJifO3KRvFzJr6Ndn85iOv2IxSu6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1C5pUksrLl3kRzE5CnlgwMCHn149auEBy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1yw9i1fbqUu2jXW6qTJeJEjURi6endlvO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CSvK5D_Jd213RYfkywyzW1VKcqK0j32-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BuzIuFkAQ0nxqCfqVIAmqelYUs6GJGPt&sz=w1000"
        ]
        
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal": "Bukittinggi",
                "Alamat": "Gh",
                "Hobi": "Cuci baju",
                "Sosmed": "@iamridhomanik",
                "Kesan": "awalnya ngira cool karena ketua baleg kan ya, TERNYATAAA ENGGGAA ADA COOL COOLNYA",
                "Pesan": "tetap lah menjadi NPD walaupun banyak yang menghate, semangat juga TAnya bang oiya #dukung bang ridho menguasai segala jenis cabor"
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Cantik bangettttt sangat sukaa melihat  kak juee, talkactive",
                "Pesan": "kak jue tolong siarkan radio di london jg (palembang)."
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "OHH ini abang mapres yang diperbicangkan orang orang itu.",
                "Pesan": "semoga moto abang menjadi orang kaya cepat terkabul.. Dan TA nya di permudah Amiin"
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "vibes nya kayak orang keren",
                "Pesan": "beneran keren kok, sukses terus banggg"
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "cakep banget, yang cakep khas indonesia asli gt",
                "Pesan": "semangat kuliahnyaa, keren trusss!"
            },
            {   "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "abang ini selalu ketawa tiap bang ridho ngomong",
                "Pesan": "gapapa bang semoga humor ny receh trus yh, bang kayaknya stiker wa abang bgus smwa, mangats ta nyh bang"
            },
            {"Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Pertama ketemu kak nisa tu pass pilketanggg baik bangetttt mau membimbing dengan sabarrrr",
                "Pesan": "Semangat bantai bantai semester 4 nyh kak ahayyy."
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "cantik bangettt serius,, temen ku jg pada bilang kak hani cantik dan lucu",
                "Pesan": "semoga tdk ad yg membully kakak lg yh #safekakhani pdhl kakak lucu dah"
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Abang yang menyanyikan lagu waktu fg suaranya bagus poll",
                "Pesan": "Semangat kuliah nyh bang, nampaknya abang orang yg ss (sangat sibuk)"
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "aura wanita batak nyh kuat sekali #girlpower, MANIESS BGT KAK BTW KIWW",
                "Pesan": "SEMANGATTTTT TA NYA KAK MONICAAA, OIYAA FEEDS IG KAKAK BAGUSSSS LOVE IT."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Mengenal abang as operator ppt pra kader ganjil.. eh pas kader pindah genap oh nooo.. abang baik sekali trnyt IMUT",
                "Pesan": "username ig abang sangat iconic, bang nagatseee.. semoga username nya itu trs yh bang."
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Jujur awal melihat kak sekar, aku takut bgt krna serem,, kakak komdisss ",
                "Pesan": "trnyt kak sekar imut dan maniss serta baik sekaliii hehehhe... love kak sekar"
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "eh kak cakep bangett seriuss lucuu, vibes nya kayak wanita melayu gt asli pekan apa malay sbrny kak?.",
                "Pesan": "semangat kuliahnyaa kak, semoga lancar selalu urusan nyaaa."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
if menu == "Senator":
    def senator():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1Csk2AwMz5VMbubaCSva1CNncaBvkY-QB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Cm53Ja0qds9Wt7hQ1Y2s01GYlspEpUU6&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Co_qsOcFWSYQYqcYr_7pjYo56te9TFpS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CnaV8ZssaGSswq_EPGkb3t8npkK_-F5z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D-0hPn0a3DE16fiM0Ga5rlLg9Qjj2c-C&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D-njtShIDz9oktyTnsm2vwONjz_i_kAe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CmxDEdoFf2XxYMHhfFuRCtxtyYgiUC7y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1D-ZKU1bY3UCPigbomcArbDaaahA-HUr8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Cvc9se5WklM688h29m13TEEmIQbt7N35&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CtmKgPeF_g9ypnHAW7FNTtkvF-2iAdBX&sz=w1000"
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "SUPER POWER KAK FATHINAH, remind me of fatimah dari ui",
                "Pesan": "tolonggg keren selaluuu kak, suksesss kariir nya"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "teman kating pertama saya pas fg,, sangat humblee TERBAIK LAH BANG MANTAP.",
                "Pesan": "bangg tetap menjadi bang helmy yang kayak gini yahh hehee."
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Sportif dan energik, seru diajak main bareng.",
                "Pesan": "Terus semangat, jaga kesehatan, dan semoga makin jago badmintonnya."
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia___",
                "Kesan": "lucu cantik dan imutttt trs keliatan nya pinterrrr.",
                "Pesan": "Semangat terus, semoga pancingannya selalu dapat hasil."
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Santai dan enak diajak bergaul.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan."
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Santai dan gampang akrab dengan siapa saja.",
                "Pesan": "Tetap semangat dan semoga selalu ada tontonan seru."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Rajin dan teliti, orangnya juga menyenangkan.",
                "Pesan": "Tetap semangat dan semoga dokumentasinya selalu rapi dan lancar."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Unik dan seru, selalu ada cerita menarik.",
                "Pesan": "Terus semangat dan semoga ayamnya selalu patuh."
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Kalem dan menyenangkan, selera musiknya pasti asyik.",
                "Pesan": "Semangat terus kuliahnya, semoga playlist-nya selalu menemani hari yang baik."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Tenang dan menyenangkan, banyak bahan obrolan yang seru.",
                "Pesan": "Terus semangat belajarnya dan tetap jadi diri sendiri."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1iPPUGCuqa2L98pfroGH3AG2SPxuDulAV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OE_IEEvxk4EU-9BJaO2lGX6ncLCXho3T&sz=w1000",
                "https://drive.google.com/thumbnail?id=1O8ffCh0WzksIXHNuNuj8w4G9E1xSOscR&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OEQaJ38w_aWXUyDtkiR1teEPXXQym83V&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iPycFWPo5DNCgnTP5NkKlKzJk5XumbMN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hrOUcMNFX8QcxmDIUGbbDB_wU305nIgE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OBUGOBXtRVjim4Pr3nxje3u6XYn9Ur1d&sz=w1000",
                "https://drive.google.com/thumbnail?id=1h_tReO8SLZG_EvKG4lGzmxWE0MGTXZna&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iC3rX_OMeIYmW57qMpeKYf7_Itlnl25z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hiPFYII9c2cMbkluJDsevbKpiukU0ezx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=14v2WD3j2XJF0IUnwc1X948hRzLq0QO3N&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OF9NIDHWcx9DgkG5RsxLPP2-Ax_yrzrb&sz=w1000",
                "https://drive.google.com/thumbnail?id=1i5vof6d6DHUQ_XWQVtito235QLyQGwiR&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iKX--YyzxR_nlzaVwlny_1TMKPHtcDD5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hrIfpiZXA0tI5WWrkXpkLgwRaMuigVF8&sz=w1000"
        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal": "Kalianda",
                "Alamat": "Samping kost Haikal",
                "Hobi": "Naksir cowo cakep",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Ramah dan mudah akrab dengan siapa saja.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan ya."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Tenang dan enak diajak bicara.",
                "Pesan": "Semoga selalu dimudahkan dalam setiap urusan."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "-",
                "Sosmed": "@nobelnizam",
                "Kesan": "Kalem dan sopan, nyaman diajak ngobrol.",
                "Pesan": "Terus semangat dan tetap konsisten dalam belajar."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "Santai dan menyenangkan.",
                "Pesan": "Tetap jadi diri sendiri dan semangat terus."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Supel dan gampang bergaul.",
                "Pesan": "Semangat terus kuliahnya, semoga lancar ke depannya."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Orangnya santai dan asyik diajak ngobrol.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat yang cukup."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Aktif dan punya semangat yang tinggi.",
                "Pesan": "Terus berkembang dan semoga selalu sukses."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Dewasa dan bisa diandalkan.",
                "Pesan": "Tetap semangat dan jaga kesehatan."
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450065",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Nomandenl",
                "Hobi": "Mancing emosi",
                "Sosmed": "@putrimannaa",
                "Kesan": "Ceria dan seru diajak bercanda.",
                "Pesan": "Semangat terus belajarnya dan tetap jadi pribadi yang positif."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Ramah dan hangat ke semua orang.",
                "Pesan": "Tetap semangat dan semoga semua rencananya berjalan baik."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Orangnya humoris dan bikin suasana cair.",
                "Pesan": "Terus semangat dan tetap rendah hati."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Disiplin dan menjaga pola hidup sehat.",
                "Pesan": "Pertahankan semangatnya dan tetap konsisten."
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Pekerja keras dan bertanggung jawab.",
                "Pesan": "Semangat terus dan jangan lupa luangkan waktu untuk diri sendiri."
            },
            {
                "Nama": "Jeremi Marolop Partogi Situmorang",
                "NIM": "124450111",
                "Umur": "16",
                "Asal": "Berlin",
                "Alamat": "Samping kos Rafli",
                "Hobi": "Mengembala anak ayam",
                "Sosmed": "@jemarrro",
                "Kesan": "Santai dan mudah bergaul.",
                "Pesan": "Tetap semangat dan terus belajar hal baru."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Ramah dan menyenangkan diajak berteman.",
                "Pesan": "Semoga kuliahnya lancar dan selalu diberi kesehatan."
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "20",
                "Asal": "Sibolga",
                "Alamat": "Samping kos Haikal",
                "Hobi": "Nonton",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Kalem dan enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan terus jadi pribadi yang baik."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "cantik dan imut MY KAKAK NIM.",
                "Pesan": "Semangat terus dan tetap jaga kesehatan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1Q2B4uPDqw9lUheDo3s6AOJmKB8b7WLmh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OvAtLbD579PGpqeOTcgGSHEqxoQd136w&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PlAHU9w9Hf-x7-m6b5qVrdmHdRW37_30&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Pu31f1zlD5PfN8ITPiUEATT8nr6Bc13y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PjM8pwBADyaknqAB3D-ZDADpbJaS_ldd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OquHH2gHJNekx4iket71ZEpsrPOyjcmV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OoNNYg8BBigFNLI-YCWfb5CRyrtav1xb&sz=w1000",
                "https://drive.google.com/thumbnail?id=1P4ErCgEVA6AhCjr7FvDq5b2Xc_MKvItT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1P-PGHZ-0ryOx56CrgWvg2-7li98b5CA0&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OrxtUnBedm7o_b6W87IFNErc2DeePywu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OzgXxAYBk5utu1ecQ-nT08ArgguVasBi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OlHmrPqXNdElKGl0Ayb9beXtOLJX_7Vn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PVqcJaieQPG57BmRNEd86F-fjW-Amf4w&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000"
                "https://drive.google.com/thumbnail?id=1PWL21MBCF0RafMPtN7RCoPSiutZMTgx_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PN2J5kS7i0_obcx04Q9kUzfis5ROo0Xj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PQYVEDlF9gdJUXqLInfmYMxHcUB_a6iD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PanZT6rriJG83Pss5AJoVCBc_3Fewy4t&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PX53fBYDtVhEQ6Q-S5u2AugMhlPfdlkU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PDCjxdqNQUNffCMVkxjI02CPQUtGa3vt&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Y2xOvs3kzGce79QisD-iCpuARF_NOZCD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Q056h4N5MyRmN1X8LIMWuUjYtceSNvhi&sz=w1000"
        ]
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Ramah dan menyenangkan, enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Ceria dan gampang akrab dengan siapa saja.",
                "Pesan": "Semangat terus kuliahnya, semoga jalan-jalannya makin seru."
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Santai dan asyik diajak bergaul.",
                "Pesan": "Terus semangat dan jaga kesehatan."
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Santai dan tidak banyak drama.",
                "Pesan": "Tetap santai tapi jangan lupa produktif juga ya."
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Ceria dan penuh percaya diri.",
                "Pesan": "Tetap semangat dan terus berkarya."
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Santai dan menyenangkan.",
                "Pesan": "Semangat terus, semoga cepat dapat rumah impian."
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Ceria dan menyenangkan.",
                "Pesan": "Tetap semangat, tapi jangan kebanyakan yang manis ya."
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Kalem dan enak diajak ngobrol soal film.",
                "Pesan": "Tetap semangat dan semoga filmnya selalu seru."
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Humoris dan enak diajak bercanda.",
                "Pesan": "Tetap jadi pribadi yang menyenangkan dan semangat terus."
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Seru dan punya hobi yang unik-unik.",
                "Pesan": "Tetap semangat, semoga pancingannya selalu dapat hasil."
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Teliti dan bisa diandalkan.",
                "Pesan": "Semangat terus, semoga semua urusan lancar."
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Ramah dan terbuka.",
                "Pesan": "Tetap semangat dan jangan ragu bertanya."
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Orangnya seru dan bikin suasana jadi hidup.",
                "Pesan": "Tetap semangat, dan jangan kebanyakan bikin ribut ya."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Tenang dan menyenangkan diajak ngobrol.",
                "Pesan": "Tetap semangat, semoga cerita favoritnya selalu seru."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Baik hati dan ramah.",
                "Pesan": "Tetap jadi pribadi yang baik dan semangat terus."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Tenang dan kalem.",
                "Pesan": "Semangat kuliahnya, semoga tidurnya selalu cukup."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Sabar dan telaten.",
                "Pesan": "Semangat terus, semoga cupangnya sehat-sehat."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Santai dan gampang akrab.",
                "Pesan": "Tetap semangat kuliahnya dan jaga kesehatan."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Kreatif dan punya cara berpikir yang unik.",
                "Pesan": "Semoga cepat ketemu hobi yang cocok, tetap semangat."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Santai dan humoris.",
                "Pesan": "Tetap semangat dan terus jadi pribadi yang menyenangkan."
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Ramah dan seru diajak ngobrol.",
                "Pesan": "Semangat terus, semoga selalu ada tontonan seru."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Ramah dan menyenangkan.",
                "Pesan": "."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()


