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
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gz29g4ZheL2ptfHtiOuOHzkT2OcN7xdX",
            "https://drive.google.com/uc?export=view&id=1oOokKC-9HrvMtwhMDfZ845Er7utXkDv6",
            "https://drive.google.com/uc?export=view&id=1q-UAXLn8KyzeeOw5X6LLcvK54uL0MqdW",
            "https://drive.google.com/uc?export=view&id=1CZRErWQKlSJw6-c3apdM1bok_bMvRJC8",
            "https://drive.google.com/uc?export=view&id=11U24HDdKaxvWlOVtrJ2so7OcOXs8ifyF",
            "https://drive.google.com/uc?export=view&id=1qW3TNaljd0CTUzYWnXzRuk46OeSq49ml",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push IMO, Menyuci",
                "sosmed": "@jars_mrp",
                "kesan":"Abangnya ternyata orang batak, kirain orang asli Lampung.",  
                "pesan":"Semangat terus kuliahnya bang, tetap jadi orang yang asik ya."# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bangkinang, Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya asik, lucu, dan kok kayaknya nggak asing, ternyata sering ketemu waktu DSS.",  
                "pesan":"Semangat kuliahnya bang, makin jago ya main basketnya."# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450079",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya asik, nyambung banget kalo ngobrol trus kelihatan pintarnya",  
                "pesan":"Semangat kuliah dan ngaspak ADS di kelas RA ya kak."# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya agak pendiem tapi lama kelamaan kok jadi asik.",  
                "pesan":"Semangat terus kuliahnya bang, semoga kuat sampe tamat."
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya asik, seru dan make up-nya on point banget.",  
                "pesan":"Semangat terus kuliahnya kak, semoga tercapai semua cita-citanya."
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Airan",
                "hobbi": "Bertemu Haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya seru dan imut banget.",  
                "pesan":"Semangat terus kuliahnya kak, tetap jadi orang yang lucu dan imut."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cMl-rv25rqjLv2FonGv_hw2GbCLz_v4P",
            "https://drive.google.com/uc?export=view&id=19AEB_2glJ0dAMsNyaJokKlOZTKOp6IW5",
            "https://drive.google.com/uc?export=view&id=19oaWaFxpQ1ts5Vnppys81sSEojsjkhNq",
            "https://drive.google.com/uc?export=view&id=1N2tPzAdbgxYWJoiAlG1oQCDz_xA6Mtu-",  # Bang Michael
            "https://drive.google.com/uc?export=view&id=1CCaYj1jSiFCoiq-T5hkJ72kcLD7g899R", # Kak Siti
            "https://drive.google.com/uc?export=view&id=113GxFv78gaCm_RX8sj1ghHiAAeUTRDm6",  # Bang Givaro
            "https://drive.google.com/uc?export=view&id=1w0sKHMaRnqz4F3QFy3-IVBKs1s5lcMfD",  # Kak Afganis
            "https://drive.google.com/uc?export=view&id=1EFzM5WW5P5wzqYd7848fnaIr2JU0uciw",  # Kak Hani
            "https://drive.google.com/uc?export=view&id=1yV9QvX0Waxj3O5XrWvcmJSIQrZHIGcnv", # Bang Jeremi
            "https://drive.google.com/uc?export=view&id=1Do0zByhJoHa50D7I5LOgslndjQQDQ6cZ", # Kak Monica
            "https://drive.google.com/uc?export=view&id=1H5Z2zw_8fi56mgbg4QhUVloOeCnH44e-", # Bang Jona
            "https://drive.google.com/uc?export=view&id=1ejDQfKhpoRbXM3iHwpBz-8tzkSiG89ob", # Kak Sekar
            "https://drive.google.com/uc?export=view&id=1Ylo5O4JuwB3dJyV7kSKnZ4sHuPs1kk7w", # Kak Wan Nashwa
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan":"Abangnya asik, seru, naturally funny.",
                "pesan":"Semangat terus kuliahnya bang, semangat ngasprak ADS di kelas RA ya."# 1
            },
            {
                "nama": "Juesi Aprilia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Ngerepeat lagu begin again Taylor Swift di Spotify",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya cantik banget, ramah dan asik.",
                "pesan":"Semangat terus kuliahnya kak Juesi, jangan bosan dengerin begin again ya."# 1
            },
            {
                "nama": "Dharu Cahyo Aji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton AGZ tapi udah tamat",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya ternyata Mapres kemarin dan style-nya kece banget.",
                "pesan":"Semangat kuliahnya bang, cari tontonan lain ya kalau AGZ-nya dah tamat."# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jatimulyo",
                "hobbi": "Jogging malam hari",
                "sosmed": "@me._kael",
                "kesan": "Abangnya lucu, asik tapi agak pendiam.",
                "pesan":"Semangat terus kuliahnya bang, semoga apa yang dicita-citakan tercapai."
                                },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboiboy",
                "sosmed": "@rizkyfadil_",
                "kesan": "Kakaknya kayak galak galak tapi ternyata asik dan baik banget.",
                "pesan":"Semangat kuliahnya kak siti, mau liat koleksi kartu boboiboynya."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "@givarooo",
                "kesan": "Abangnya keren, semangat banget dan seru.",
                "pesan":"Semangat terus kuliahnya bang, jangan lupa jaga kesehatan."
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Padang, Sumbar",
                "alamat": "Kedaton",
                "hobbi": "Memburu",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya cantik, baik hati dan ramah.",
                "pesan":"Semangat terus kuliahnya kak, semoga lancar perkuliahannya."
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya cantik, kalem dan ramah.",
                "pesan":"Semangat kuliahnya kak, rekomendasikan AU yang bagus dong."
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Ngoding",
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya keren, pendiam dan baru sadar kalo kemarin pernah nyayi di datapudi.",
                "pesan":"Semangat terus kuliahnya bang dan tipsnya biar ngoding bisa jadi hobi ."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya baik, ramah dan asik.",
                "pesan":"Semangat terus kuliahnya kak, semoga tidurnya selalu cukup."
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatse",
                "kesan": "Kakaknya kayak galak galak tapi ternyata asik dan baik banget.",
                "pesan":"Semangat kuliahnya kak siti, mau liat koleksi kartu boboiboynya."
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya kayak galak gitu tapi ternyata asik, seru dan baik banget.",
                "pesan":"Semangat kuliahnya kak, semoga selalu sehat dan bahagia."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Mamuju",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nagatse",
                "kesan": "Kakaknya asik, kelihatan lemah lembut dan matanya cantik.",
                "pesan":"Semangat kuliahnya kak, semoga apa yang dicitakan terwujud."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oozUACxbe0Fcr3sGmysue09HFNSxU1qt", # Kak Fathinah
            "https://drive.google.com/uc?export=view&id=1kp_hrCYjmXRT64YJmKki8K0argXOjhF5", # Bang Helmy
            "https://drive.google.com/uc?export=view&id=10vQ5FXdBQOLM851UxqJGJuOG6bu0A5UT", # Bang Fernando
            "https://drive.google.com/uc?export=view&id=1xAAzndTTn1KEz5gmHJbAYNAnxyuXic1G", # Kak Suci
            "https://drive.google.com/uc?export=view&id=1CZERyVIBD64haO-6GdMeZiQxlSMonih1", # Bang Wielman
            "https://drive.google.com/uc?export=view&id=1MkAYWyeetfNTnYlVgdoyvMnixcd0jpkV", # Kak Lia
            "https://drive.google.com/uc?export=view&id=1ja6C3i4GgZD7OpUgnWUERtKxU18tkCwl", # Kak Aqila
            "https://drive.google.com/uc?export=view&id=14crbJx7owyLxKXT-neMJzssnPZmqEBcL", # Bang Hazel
            "https://drive.google.com/uc?export=view&id=1vD_awGVF6X9HXLFfjoYNCqEAjaUPfljU", # Kak Nadya
            "https://drive.google.com/uc?export=view&id=1TeeGTh-F1qQliHv3Q4fmZYztqvjNTa9H", # Kak Dwi
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Airan",
                "hobbi": "Tidur",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya keren dan berwibawa banget.",
                "pesan":"Semangat terus kuliahnya kak dan jangan lupa istirahat yang cukup."
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kotabaru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Abangnya baik banget, ramah, dan beneran naturally funny.",
                "pesan":"Semangat kuliahnya bang, bahagia selalu."
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatse",
                "kesan": "Abangnya baik, kayaknya sih pendiem, ramah dan asik.",
                "pesan":"Semangat kuliahnya bang, lancar pendidikannya."
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Pesisir Barat",
                "alamat": "Kotabaru",
                "hobbi": "Kameramen",
                "sosmed": "@sciia__",
                "kesan": "Kakaknya asik, kalau ngobrol nyambung dan enak diobrolin.",
                "pesan":"Semangat kuliahnya kak, jaga kesehatan ya."
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "123450077",
                "umur": "20",
                "asal":"Mamuju",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nagatse",
                "kesan": "Kakaknya asik, kelihatan lemah lembut dan matanya cantik.",
                "pesan":"Semangat kuliahnya kak, semoga apa yang dicitakan terwujud."
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Ngejar deadline",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya seru dan ternyata asprak ADS di kelas RA.",
                "pesan":"Semangat terus kuliahnya kak, selamatin nilai ADS ku ya kak."
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayyes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya baik, cantik, dan lucu banget.",
                "pesan":"Semangat terus kuliahnya kak, jangan lupa istirahat yang cukup."
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@fernando_dimetrius",
                "kesan": "Kakaknya kayak galak galak tapi ternyata asik dan baik banget.",
                "pesan":"Semangat kuliahnya kak siti, mau liat koleksi kartu boboiboynya."
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",   
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadiaanzani",
                "kesan": "Kakaknya asik, cantik, ramah dan seru.",
                "pesan":"Semangat terus kuliahnya kak, jangan meneyerah sampe lulus."
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Belwis",
                "hobbi": "tidur",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya santai banget dan seru kalo diajak ngobrol.",
                "pesan": "Semangat menjalani perkuliahan ini kak, jangan lupa istirahat yang cukup."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
            