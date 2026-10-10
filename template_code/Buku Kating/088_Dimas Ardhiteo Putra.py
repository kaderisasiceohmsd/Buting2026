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
            "https://drive.google.com/uc?export=view&id=1-O0PYQwKLb2hemdBhjrnMgFoPYatlw6T",
            "https://drive.google.com/uc?export=view&id=1H15DQzaSmo78aU2gWrfysKoOQOsO4zgh",
            "https://drive.google.com/uc?export=view&id=1lm9RQDR0eqeYvkLDkze_AsKqhiEMD7ga",
            "https://drive.google.com/uc?export=view&id=178yDYLTucGPL5HwwL-D0tzeVJlcSq7iO",
            "https://drive.google.com/uc?export=view&id=1TbqjmnrsOH8MwkMrLaiaCIrRJjLucOPk",
            "https://drive.google.com/uc?export=view&id=1frdlrJLufW0eP7gO05YjR2jHaOJx5tuM",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sektariatan HMSD",
                "hobbi": "push imo, mencuci",
                "sosmed": "@jars_mrp",
                "kesan": "Bang ginda ramahnya gak ketolongan, humble, adem liat bang ginda rasanya",  
                "pesan":"gass cumlaude bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau, Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Masak",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Keren berkharisma",  
                "pesan":"Lulus tepat waktu ya bang"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "humble, ramah, baik",  
                "pesan":"Kak, senyum selalu ya kak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Cool, dan keliatan orang yang Sistematis",  
                "pesan":"Bang waktu presentasi jangan terlalu cepat ya bang hehe"# 1  
            },
            {
                "nama": "Haffsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menyanyi",
                "sosmed": "@hafsafazilaa",
                "kesan": "humble dan baik",  
                "pesan":"Selalu happy ya kak :)"# 1  
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450003",
                "umur": "20",
                "asal":"Jawa Barat, Bekasi",
                "alamat": "Airan",
                "hobbi": "Bertemu haffsa",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "humble dan baik",  
                "pesan":"Jangan mudah patah semangat kak :)"# 1  
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zh4M-Em2lwM-CmePV3GbnEiicK8zL9af",
            "https://drive.google.com/uc?export=view&id=1j_56jjUXFplAfwI6MsZT_2hRZMPUHM9C",
            "https://drive.google.com/uc?export=view&id=1tyAFkhHMUanbHCvNarJsojELU9S_PpDL",
            "https://drive.google.com/uc?export=view&id=1lm9RQDR0eqeYvkLDkze_AsKqhiEMD7ga",
            "https://drive.google.com/uc?export=view&id=13_D_X0D_4dQVIV0FmQRKCtPtos3IDftB",
            "https://drive.google.com/uc?export=view&id=17RXB64pOkzQlnQsbiR9OoJGRhgCkTk4P",
            "https://drive.google.com/uc?export=view&id=1hO1376B7sn8zdd5lQYuXgHNpyQTQd2jL",
            "https://drive.google.com/uc?export=view&id=1jkv3ySQFjBP3uKNQmZ7_gBqCBmW87sCg",
            "https://drive.google.com/uc?export=view&id=1aZuCI5tlg6Mr5WGSrkp2pZ0hgthbiOOc",
            "https://drive.google.com/uc?export=view&id=1FajHLFg1Adloc9Qj5KoPmQ97DDAmvDxF",
            "https://drive.google.com/uc?export=view&id=18piDxtnMPi26UDyawQxA_3oDqHyRr8wU",
            "https://drive.google.com/uc?export=view&id=1e8EXbqpnZ9BxLcUjJwRV86WeeMcpGPpM",
            "https://drive.google.com/uc?export=view&id=1pqDKflXiYiV1mYWjA9IY0IcD2sR6dn_E",
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
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yJEP8VtnOKOoHAWxugbBaz2VAwq-sN4d",
            "https://drive.google.com/uc?export=view&id=1UlQC9CZxyzIp1MNRvvrOsap_cE6GxQbh",
            "https://drive.google.com/uc?export=view&id=1NdGByRdXQe7Tz6yOQZllRlLrqMf0Vbl8",
            "https://drive.google.com/uc?export=view&id=16Yk2N2Bow7hbgLcMLEvu9xZ1VrtzLrEd",
            "https://drive.google.com/uc?export=view&id=1Xy5Iyco90lB-FCW79oKYTPJu4enb7WyP",
            "https://drive.google.com/uc?export=view&id=1ijEzT2vPZjJO3UWJ9wRJI-OqLPbE64V4",
            "https://drive.google.com/uc?export=view&id=159ad2J0fyx3r7LLxajURH2q_-UORO_uH",
            "https://drive.google.com/uc?export=view&id=1C4Io47YeEZLSoc7uhVtQLRt6l5AGaJjn",
            "https://drive.google.com/uc?export=view&id=1qAByI5DpNQ24VpC3GU8s-cFU2ejs4KjI",
            "https://drive.google.com/uc?export=view&id=1JMYsZD-7HIprA-G9gLP6A1R6AJ2ZokCd",
            "https://drive.google.com/uc?export=view&id=18piDxtnMPi26UDyawQxA_3oDqHyRr8wU",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": ".",  
                "pesan": "."# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": ".",  
                "pesan": "."# 1
            },
	        {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": ".",  
                "pesan": "."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": ".",  
                "pesan": "."# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": ".",  
                "pesan": "."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()