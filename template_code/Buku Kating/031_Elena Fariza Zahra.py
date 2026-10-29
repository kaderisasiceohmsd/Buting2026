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
            "Departemen Minbak"
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
            "nav-link-selected": {"background-color": "#606060"},
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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vt4Ul7yLIr4ccAOvOcQKDMx9CX6QvLIE",
            "https://drive.google.com/uc?export=view&id=1OnHEVce_KXdA7KZXrlUQRUx2ofhKfhpH",
            "https://drive.google.com/uc?export=view&id=1iKhdTk8fyd8gKGVsBLosb4CjDOCbiMhU",
            "https://drive.google.com/uc?export=view&id=1Qh0SWrQcPn1zQyO32MqWQhgWGgjZH2zz",
            "https://drive.google.com/uc?export=view&id=1hWjE3y4PfNWjv_KoSaiyRghzf-dekdvx",
            "https://drive.google.com/uc?export=view&id=1q9GaH2jo8Ws0WkiP24_sMe9vEoQPs4N3"
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Tinggal Sekretariat HMSD",
                "hobbi": "Push Rank Sampai imo",
                "sosmed": "@jars_mrp",
                "kesan": "Bang fajar keren banget, dan ramah.",  
                "pesan":"Semoga dilancarkan segala urusannya, dan juga cepet imo."# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Tahajud",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya baik, dan juga ramahh.",  
                "pesan":"Semangat terus kuliahnya bang dan selalu diberi kesehatan."# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya cantik dan tenang banget orangnya.",  
                "pesan":"Semoga banyak hal-hal baik yang menyertai kakakk."# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya baik dan soft spoken.",  
                "pesan":"Semangat terus ngerjain TA nya bangg."# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Basket",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak hafsa seruu dan baik banget.",  
                "pesan":"Semangat terus ya kak kuliahnya dan semoga selalu bahagia."# 1
            },
            {
                "nama": "Lutfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nemuin Pak Tirta",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kak luthfia asik dan positive vibesss.",  
                "pesan":"Sehat selalu ya kak dan semangat nemuin pak Tirtanya hehehe."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PVuPM-LqRj77Xv9lffQuFo5Mte6zourJ",
            "https://drive.google.com/uc?export=view&id=1QJi9y6CBThXydH9IWxXDoB5VPDmeSu_5",
            "https://drive.google.com/uc?export=view&id=1AfyX9dSYwbFMSsQDAmitnH216fWqzlw7",
            "https://drive.google.com/uc?export=view&id=1bK0ems6xIipnLwkJiw4Q0z66kh8WiLgG",
            "https://drive.google.com/uc?export=view&id=10yYNxf5l3mU7YH9usCxj3PFCYYoyJdPE",
            "https://drive.google.com/uc?export=view&id=1tgQ6Ibmww-4_AIMm0bdJh1Op-r7oUzRr",
            "https://drive.google.com/uc?export=view&id=1CSKqI78w_6_IqgD90XBB2w3KqCUGi_cP",
            "https://drive.google.com/uc?export=view&id=1-UuhhSRKUEy4w9FYniNDS7cmAFNHUFs3",
            "https://drive.google.com/uc?export=view&id=1I8dNyW-DSwrvo_K2NeK0a7LlHwFqPH-X",
            "https://drive.google.com/uc?export=view&id=1Q3_C68ljoviKFxRamDCb5DtospNhCvTn",
            "https://drive.google.com/uc?export=view&id=1VKITfJlwUKg8cQiy9Arqv9cm8mKGALOY",
            "https://drive.google.com/uc?export=view&id=13zgEAqCJN5HoP2yzf4jy4o3o3W26M4CK",
            "https://drive.google.com/uc?export=view&id=1CbnCnDsk2nZ_l73IAspozA_qWfkXJCf4"            
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Bali",
                "alamat": "GH",
                "hobbi": "Menonton Seminar",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya seruu banget dan kocakk aslinya.",  
                "pesan":"Semangat terus bang ngerjain TA nya."# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Repeat lagu if only by skyline setiap hari di jam 8",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue cantik dan imut. Selain itu juga asikk bangett",  
                "pesan":"Jangan lupa Repeat lagu if only by skyline di jam 8 ya kakk hehehhe."# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "124450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya keren banget jadi mapres, publik speakingnyaa juga keren bnagett.",  
                "pesan":"Semoga bahagia selalu dan selalu berdampak untuk orang lain."# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro keliatannya pendiam tapi ternyata aslinya asikk banget.",
                "pesan":"Semoga selalu bahagia bang, dan diberikan kelancaran dalam hal baik."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "124",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "Kak monica soft spoken banget dan jugaa baikk bangett.",  
                "pesan":"Semangat terus ya kakk dan jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Gh Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "Abangnya asik dan juga seruuww",  
                "pesan":"Semoga api semangatnya terus berkobarrr!!"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Jatiasih",
                "alamat": "Kedaton",
                "hobbi": "Nonton Boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "kakaknya cantikk bangett, dan juga soft spoken.",  
                "pesan":"Semangat terus kakk kuliahnya dan jangan lupa nonton boboiboy."# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Indarum",
                "alamat": "Awen kost",
                "hobbi": "Photobooth",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisaa baikk banget, dan jugaa kerenn",  
                "pesan":"Semoga selalu sehat dan semoga banyak hal-hal baik yang berdatangan."# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",                
                "sosmed": "@haniquratuain_",
                "kesan": "kakaknya cantik, ramahh, dan jugaaa imutt",  
                "pesan":"Semoga sehat selalu dan dlancarkan kuliahnya."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Sidoarjo",
                "alamat": "Teluk",
                "hobbi": "Konten Mainfullness",                
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya baik banget dan publik speakingnya baguss.",  
                "pesan":"Semangat selalu bangg, dan sehat selalu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan koleksi figure",                
                "sosmed": "@nagatseee",
                "kesan": "Bang jona orangnya baik dan juga ramah.",  
                "pesan":"Semangat terus kuliahnya ya bang dan bahagia selalu."# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Membaca buku",                
                "sosmed": "@sekardnwp",
                "kesan": "Kak sekar baik banget dan perhatian",  
                "pesan":"Semoga sehat selalu ya kakk, dan bahagia selalu."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasoy",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",                
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu, asik, dan kecee.",  
                "pesan":"Bahagia selalu ya kak dan semangat dalam menjalani kuliahnya."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A0mHWHx23jYQ9xK9dFC59egL9Ypd3yit",
            "https://drive.google.com/uc?export=view&id=1jDxGELEi7-RjLI2rRngBisDpnhFnid2g",
            "https://drive.google.com/uc?export=view&id=1VtwvTBLM1K33D3GNy86dcCqy55Gd_ndh",
            "https://drive.google.com/uc?export=view&id=193EHz9-wNQxKMnSOLMlN71YDAhfjtTIM",
            "https://drive.google.com/uc?export=view&id=1FM3WuSyZjkhrPE25AQkkiimB4CTBX8f8",
            "https://drive.google.com/uc?export=view&id=1VkXbGdt7cXHNjrxU_YC9cjq0P_WH48wB",
            "https://drive.google.com/uc?export=view&id=1_inLaSuz8NSLWYcSwYAJmKocBGLl0b-V",
            "https://drive.google.com/uc?export=view&id=16OYXkbReCCOfQs5y3K_YAftZVtUzM2WJ",
            "https://drive.google.com/uc?export=view&id=1nqtM3nUiSYMzPlsukxVSuZnC35j8hgY-",
            "https://drive.google.com/uc?export=view&id=1zT3aEb9-YVh5utKTnZ-Qyb7EU5gf3ohp",
            "https://drive.google.com/uc?export=view&id=1u6uFbX52xLO0T7RVZBGf-8cqkBodBweE",
            "https://drive.google.com/uc?export=view&id=1fQl8tz8OJ741JEZO22M_cwO06F6ejeUT",
            "https://drive.google.com/uc?export=view&id=1a0xbXJFOHHQjiglueSR45S7pBlVmdUKW",
            "https://drive.google.com/uc?export=view&id=1FNql0Nm0wVlqzMtoPoyC_X5wY4y8mzR9",
            "https://drive.google.com/uc?export=view&id=1XCqCmTm-ZQICw4toQ0pH0dYmlolbdEqV",
            "https://drive.google.com/uc?export=view&id=1jzaBoPUPVthzTNsUtNqrBqmwKa62kspV",
            "https://drive.google.com/uc?export=view&id=1wLiQn75RPExkvOjkti_3di3-wI2l3Roa",
            "https://drive.google.com/uc?export=view&id=1WelXUzARspwFqWZG5bGmAEJ6XII3Fb6U",
            "https://drive.google.com/uc?export=view&id=1-shKX1NlMWwjIFRCnEldvGIOZQ-aECch",
            "https://drive.google.com/uc?export=view&id=1Vvf0FfqxQLrM5Lf9mjwNnrK0L-U6ruUN",
            "https://drive.google.com/uc?export=view&id=1ny56Uc3UXFempTkgn-FI1FlVdFWU4_hN",
            "https://drive.google.com/uc?export=view&id=1zkKcQMrmcT1km0NvISd9bOcI3tbBsERx"
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kak arini cantik dan jugaa asikk bangett.",  
                "pesan": "Semoga selalu diberi kebahaiaan dan jugaa diberi kelancaran dalam hal-hal baik."  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla kerenn dan juga kagum publik speakingnya bagus.",  
                "pesan":"Semoga selalu bahaigia dan selalu semangat dalam menjalani hari."# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Abangnya asik dan juga kocak",  
                "pesan":"Semoga abang sehat selalu dan diberikan kebahagiaan."# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya cantikk, imut dan jugaa kerenn bangett.",
                "pesan":"Lancar selalu ya kak untu hal-hal yang sedang dilakukan."# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya lucuuu dan jugaa ramahh.",  
                "pesan":"Sehat selalu dan dilancarkan urusan kuliahnya."# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya baikk dan jugaa seruuuu.",  
                "pesan":"semangat terus kuliahnya ya kakk."# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kak indah ramah dan juga asik bangett.",  
                "pesan":"Semangat terus kak mancingnyaaa!"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya aslinya seruu dan juga asikk.",  
                "pesan":"Semangat trus kulianya bang dan juga jangan lupa terus Berlaku humoris."# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abangnya baikk dan jugaa ramahhh.",  
                "pesan":"Semoga abang selalu bahagia dandiberi kelancarannn dalam hal apapun."# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik bangett dan juga ramah.",  
                "pesan":"Lancar terus ya kak kuliahnya, semogaa cepat debut jadi idol hehehehe."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak yolanda asik banget dan juga ekstrovert, bisa berbaur dengan siapa saja.",  
                "pesan":"Semoga selalu ceriaa ya kakk."# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kak riska asik dan juga baik, kereen jugaa",  
                "pesan":"semangat terus kuliahnya kaaa."# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya asikk, baikk dan jugaa ramahh.",  
                "pesan":"semoga apa yang diinginkan dapat terwujud."# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya baik bangett, mau diajak posee imuppp.",  
                "pesan":"Semoga hal baik yang kakak lakukan dapat berbalik ke kakak sendiri."# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang danil ramahh danjuga kalcerr",  
                "pesan":"semangat terus bangg dalam menjalankan kuliahnya."# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Abangnya kerenn dan juga jago coding",  
                "pesan":"Semangat bangg kuliahnya dan semoga selalu lancar."# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya kocak, dan seruuu",  
                "pesan":"Semoga cepet ketemu yang bang hobinyaa."# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Abangnya keren banget publik speakingnya, keren banget jadi mc.",  
                "pesan":"semoa apa yang diinginkan daat dicapai."# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakakny positive vibes dan juga baik bangett.",  
                "pesan":"semogaa hari-hari yang dilalui selalu menyenangkan."# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Bang ahmad keren, aktif dalam banyak kegiatan, dan baik.",  
                "pesan":"semoga hal-hal baik yang telah dilakukan dapat balik ke abang dan selalu dilancarkan dalam menjalankan perkuliahannya."# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I62qdp3yGE1fDMk8Q8ECqa-0w8M_1Rvw",
            "https://drive.google.com/uc?export=view&id=1zegOsXUM9y27-Ge1SjExOQZkKmJ_z6Qm",
            "https://drive.google.com/uc?export=view&id=14fK4wvybPOSvbQS6nkBQCfQ7rs5bg1L3",
            "https://drive.google.com/uc?export=view&id=14hcScJtOpVe2fBzzzD67LynIX9njmgxv",
            "https://drive.google.com/uc?export=view&id=1gcMha35fsMG2gptv6xrr9DG0qj4S-s06",
            "https://drive.google.com/uc?export=view&id=1PexIe6_mVsNJMncVf_jUTfouNhATxazQ",
            "https://drive.google.com/uc?export=view&id=1uXH5ek4qOs6s3CGbB09RrUHM_3J_LIsh",
            "https://drive.google.com/uc?export=view&id=1vqotyB71DEaP-rWjbb5vk-7HXSZmC_RU",
            "https://drive.google.com/uc?export=view&id=1Ph6klNjTRCV9kzoav6RN5_sxZheF7ghZ",
            "https://drive.google.com/uc?export=view&id=1qOPejt1mF_KfOoTJ6SnUzVWrjfnzLesz",
            "https://drive.google.com/uc?export=view&id=182d2OnGjbAoRD6fqaNuSM9u6W4ZsfT_F",
            "https://drive.google.com/uc?export=view&id=13DzMfrcE9wg9o-Yn3t53Mex7mynspGRB"
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya asikk dan juga chill, suka mencairkan suasana.",  
                "pesan":"semoga selalu ceria dan hari-harinya selalu diberi kelancaran"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya cantik, ramah, dan juga imutt.",  
                "pesan":"semangat terus ya kak kuliahnya, mauu juga diajarin masak sama kakak."# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak Anadia aslinya ramah dan seruuu diajak ngobrol.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baikk,murah senyumm dan jugaa ramahh.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Abangnya seru dan juga kocakk ngajak dope unik.",  
                "pesan":"Semangat terus dalam menjalankan hari-harinya bang."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Abangnya asik aslinya, dan suka ngejokes.",  
                "pesan":"semangat terus bang dalam menjalankan hari-harinya."# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya asikk, kocakk aslinya.",  
                "pesan":"Semoga abang selalu diberi kebahagiaan dan "# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak layina asik dan jugaa baik bangett.",  
                "pesan":"semangat terus yaa kuliahnya kaakk"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak anggun imutt dan juga asikk diajak ngobrol.",  
                "pesan":"semoga selalu bahagia dalam menjalani hari-hari."# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak della cantikk dan jugaa imuppp.",  
                "pesan":"semoga selalu dilancarkan ya kakk segala urusannya."# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Abangnya baikk dan jugaa seruuww.",  
                "pesan":"semogaa hari-hari yang dilalui selalu bahagia ya bang."# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakaknyaa cantiikk, dan baddie. sukaaaa.",  
                "pesan":"semoga hal-hal baik yang dilakukan kakak dapat berbalik ke kakak sendiri"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s1vQgFVFO2fqqs26qSaBBBddOd5sQGo0",
            "https://drive.google.com/uc?export=view&id=1gJ5-SkbUpEDeDJ5Yrzd5yvh6qqaS72Kv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=vuew&id=1ov9svOVT5rbq6jYMeMgSy8A-xFV7ocb2",
            "https://drive.google.com/uc?export=view&id=1PQ6ReXClHp1j0udELJ2-HW7VlNjRHrRw",
            "https://drive.google.com/uc?export=view&id=1qJNNHwAf34CV-HEDeZVwqQFCBfGx_kQm",
            "https://drive.google.com/uc?export=view&id=1QJ6RJ9FxmyvM4-hkIADWhAaURr2Y8Irs",
            "https://drive.google.com/uc?export=view&id=1nxVNI6qWQ5W6Vmf6pMmlYAJdEAwthC5y",
            "https://drive.google.com/uc?export=view&id=1oC3HDy-3It12ZJM-coDb9-uypBWd0EM3",
            "https://drive.google.com/uc?export=view&id=10Gtp0FccREe1TwbKSIqv150LRrTQrL0N",
            "https://drive.google.com/uc?export=view&id=19RPsCx348CWMABaVwm-trv5_rpU9LmD6",
            "https://drive.google.com/uc?export=view&id=1ctvleLcB-JLxO_5Z7S2K9XhrLr0bZ7AS",
            "https://drive.google.com/uc?export=view&id=1q8qv-XTMMDOoqx93-avDoNI2NXXSHYOt",
            "https://drive.google.com/uc?export=view&id=16h2Wu3vvpA7LM-WcDMoZE6AYGhrUwraZ",
            "https://drive.google.com/uc?export=view&id=1zbIGI3J2Ypd6Bx_0ixhWvdnjVESLolun",
            "https://drive.google.com/uc?export=view&id=1_nkUVKUPu1PVo8LoQidow7ReuybNQ_Dy",
            "https://drive.google.com/uc?export=view&id=1TE5SMghkD1Ix2Rn6b-6WWE-2sbHt7TGD",
            "https://drive.google.com/uc?export=view&id=1oK9_uVFaUcJbb_Bl3jrzVxYCde5zwIQO"
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakak nayla baikk bangett dan cantikkk",  
                "pesan": "Semangat ya kak TA nya, semoga selalu lancar dan jangan lupa bahagia."# 1
            },
            {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak dona baik banget, soft spoken,ramah, dan jugaa perhatiann.",  
                "pesan": "Semogaa lancarr teruss yaa kakkk hari-hari yang dilalui."# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya baikdan juga sik.",  
                "pesan": "Semangat terus bang kuliahnya."# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kak rai cantik bangett dan jagoo designnya.",  
                "pesan": "Semoga selalu lancar yaa kak hari-hari yang dijalani."# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik banget dan juga soft spoken",  
                "pesan": "Semoga banyak hal-hal baik yang berdatangan ke kakak."# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakaknya cantik banget dan juga kerenn.",  
                "pesan": "Semoga selalu sehat dan bahagia ya kakk."# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakaknya cantik, dan juga baik.",  
                "pesan":"Semoga selalu diberik kesehatan, dan juga kebahagiaan."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya baik, dan juga soft spoken.",  
                "pesan":"Semoga selalu ceria hari-hari yang dilalui."# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kak ifa cantik, ramah, dan seruu jugaa orangnyaaa",  
                "pesan":"Sehat selalu kak dan juga selalu ceria ya."# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakaknya cantik, dan juga baik, akuu suka sama kacamatanya",  
                "pesan": "Semoga dilancarkan kuliahnya dan juga urusan lainnya."# 1
            },
            {
                "nama": " Edsel Adya Pradipta",
                "nim": " 124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya baik, suka melong, dan juga jago design.",  
                "pesan": "Semoga banyakk hal menyenangkan yang abang lalui setiap harinya"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Bang daffa asikk banget, chill juga, dan kerenn jago design.",  
                "pesan":"Semangat terus bang designnya."# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakaknya cantik dan juga asik",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya imutt, cantik dan juga ramahh.",  
                "pesan":"Semoga selalu ceria ya kak."# 1
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakaknya imut, soft spoken dan juga baik banget.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "shafa delaila azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kak shafa imut, lucu dan jugaa asikk diajak ngobrol.",  
                "pesan": "Semangat terus kuliahnya kakkk."# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakaknya imutt dan jago main perkusi.",  
                "pesan":"semoga selalu ceria dan bahagia kakkk."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IbBz3h2OHclA9jqCUDnJQdjgFgIfcthT",
            "https://drive.google.com/uc?export=view&id=1aZABb2kvBNmwVwcKWbJu86sSkwBXq87q",
            "https://drive.google.com/uc?export=view&id=1oHOQmEC-ezE8f9BFICAyIhrIiTpCFtOp",
            "https://drive.google.com/uc?export=view&id=1QZ79Ki88fRulkZkeu2pqhBZwjq-buRTN",
            "https://drive.google.com/uc?export=view&id=1hrWwujDBao-McQg0V-N7IGdfadjVIMMY",
            "https://drive.google.com/uc?export=view&id=18h9KoKNgJclF1-0RVbnF1elBWcLGF7aw",
            "https://drive.google.com/uc?export=view&id=1MLSJgnqzukTyKIjg2VMTL2Bu0UB_zsQH",
            "https://drive.google.com/uc?export=view&id=1vTTgs9bgR9qfDVB4_RV9FZGPdButJvVC",
            "https://drive.google.com/uc?export=view&id=1GaVnzYvOC0aOBfupnSDjxlOAIS6j4LrV",
            "https://drive.google.com/uc?export=view&id=16deUkZlZ1CcmViC3j61zuUkxn4a4u1Pf"
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21 Tahun",
                "asal":"Jakarta",
                "alamat": "Airan",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya cantik banget, tegas tapi asik diajak ngobrol.",  
                "pesan":"semoga dilancarkan kuliahnya dan dihindari dari hal-hal buruk ya kakk."# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya kerenn dan jugaa ramah bangettt",  
                "pesan":"semangat yaa kakk kuliahnya"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Bang helmi asik, suka melet, dan teman kak bina.",  
                "pesan":"Semangat bangg kuliahnya dan jangan lupa matiin sen."# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya asik bangett dan jugaa kerennn.",  
                "pesan":"Selalu bahagia ya bang dan diberi keceriaan."# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kak suci imutt, ramah, dan cantikk",  
                "pesan":"semoaga hal-hal baik menyertai kakak."# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya kerenn bangett publik speakingnyaa.",  
                "pesan":"semangat terus bangg dalam hal-hal yang sedang dijalani."# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak aqila cantik, imut, dan juga ceria.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "19 Tahun",
                "asal":"Lamtim timur",
                "alamat": "Gunter terang",
                "hobbi": "Cinematic Datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya baik dan juga keren",  
                "pesan":"Sehat selalu dan juga bahagia selalu bang."# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya baik dan juga murah senyum.",  
                "pesan":"Semogaa banyak menemukan hal-hal baik."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1I1Z2tc5AkxjfktbxHQ-rTNtzsdfX7lwt",
            "https://drive.google.com/uc?export=view&id=1xvzFAPpREaUM95BdEiHZyHbMZeM3_V3_",
            "https://drive.google.com/uc?export=view&id=1f5yYJ1yJKgUF0rvgWP3RAgVYC-sno7Vj",
            "https://drive.google.com/uc?export=view&id=1jnnzU8j22W4dWGbSN1WdBY30tDO3iWNP",
            "https://drive.google.com/uc?export=view&id=1JBV-pfZGuUs6_Ce0lBKcuh6ZcMnB3c3m",
            "https://drive.google.com/uc?export=view&id=1WuBfQVGjwY7PcL_6W6HCtemh0bd5Sm6V",
            "https://drive.google.com/uc?export=view&id=1n5Q9p2NmABp8kLFJMJ6VDOIdH1r_TvjQ",
            "https://drive.google.com/uc?export=view&id=1O5LB_J5QlZ3BDchR2Eyr86stJk8dDi05",
            "https://drive.google.com/uc?export=view&id=1gHOrfOr8YuYhJSq8O8dLXbkoUzbWajtQ",
            "https://drive.google.com/uc?export=view&id=1Da8aXXeunAGZnfU1pR6HGsZDZlmgeLw2",
            "https://drive.google.com/uc?export=view&id=1TGVFxLldLOFjUVWY1wdbrkmW5R9Vdhbw",
            "https://drive.google.com/uc?export=view&id=1TpEnpYfwCNKtgGUnTMlSpd51nfsW5BJx",
            "https://drive.google.com/uc?export=view&id=1vMMWDxHpOMzvbmO-wLkuJ2kWma76Gq08",
            "https://drive.google.com/uc?export=view&id=1DQYvmwxJY6KX5z540nO8W-Z0W5_rWEvt",
            "https://drive.google.com/uc?export=view&id=1WbD4HKf7FFx170PtpCVFRoANy3G38eb2"
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Sulawesi Tengah",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Masak",
                "sosmed": "@kevinaj__",
                "kesan": "Abangnya baik, ramah dan juga positive vibes", 
                "pesan": "semangat terus bang TA nya bangg, semoga lancar selalu."# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": " Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya lucuu, dan cantikkk.",  
                "pesan": "semoga bahagia selaluu dan sehat selalu yaa kaaa."# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main badminton sama Yosep",
                "sosmed": "@mridwaan_22",
                "kesan": "Abangnya kocak dan juga asik",  
                "pesan": "Selalu ceria dan dilancarkan kuliahya ya bang."# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton f1",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik dan juga asikk.",  
                "pesan": "Semoga selalu diberi kesehatan dan juga hari-harinya bahagia."# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "123450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nguras kolam lele",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya cantik, imut, dan jugaa kerenn",  
                "pesan": "Semangat ya kakk kuliahnya, dan bahagia selaluu."# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Ternak ayam",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya baik banget danjugaa ramahhh.",  
                "pesan": "Semoga hari-harinya diberikan kebahagiaan, dan bermanfaat bagi orang lain."# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": " 124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnyaa baikkk dan juga asikk.",  
                "pesan": "semaogaa banyak hal-hal baik yang menyertai dan dijauhi dari hal-hal buruk."# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": " 124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live Tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya baik dan juga soft spoken.",  
                "pesan":"Semoga selalu bahagia dan jugaa sehat selaluu"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": " Live tiktok bareng Bryan",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakaknya cantik, baik, dan juga murah senyumm",  
                "pesan":"Semoga hal baik yang kakak lakukan kembali ke kakak."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Diving",
                "sosmed": "@afdall.03",
                "kesan": "Abangnya asik, seru, dan juga kocak.",  
                "pesan":"Semoga selalu ceria dan bahagia ya bang."# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": " 124450131",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Persis",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya baik dan juga soft spoken.",  
                "pesan": "Semoga selalu sehat dan selalu semangatttt."# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": " 124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya asik dan jugaabaikk bangett.",  
                "pesan": "semangat terus yaa kakkk kuliahnyaaa."# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lari",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknya baik, penyabar, dan juga murah senyum.",  
                "pesan":"Sehat selalu dan jugaa bahagiaa selaluu yaaa kakakk."# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@andra.lhm",
                "kesan": "Abangnya baikk dan juga soft spoken.",  
                "pesan": "Semangat terus ya bang kuliahnya dan juga semoga hari-hari yang dilalui selalu lancar."# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Sesuai namanyaa, kakaknya ayuu dan jugaa ramahh bangett",  
                "pesan":"Sehat selalu ya kak, dan bahagia selalu."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen PSDA":
    def PSDA():
        gambar_urls= [
            "https://drive.google.com/uc?export=view&id=1aNah9E4hA4I349udzmimji0QBK7439E2",
            "https://drive.google.com/uc?export=view&id=1-d8v6S5uK27heAgIMWh53lV-HgZ-NU0O",
            "https://drive.google.com/uc?export=view&id=1ybMaYCugYuqGKNsFmOzJ2FkLSgOV7iq4",
            "https://drive.google.com/uc?export=view&id=1RYhNTWzHQd1T_QI9rtZhbUnm8wyLX2kY",
            "https://drive.google.com/uc?export=view&id=12GrNeBtJ53DbTXiRGri3wtRPouNZ4OVQ",
            "https://drive.google.com/uc?export=view&id=1UAafg1nghGHwZXtcecbsWB4Bb0vmhcWE",
            "https://drive.google.com/uc?export=view&id=1rlc1DBvptruef8nRzQ6Z-4IvVOnRGkxp",
            "https://drive.google.com/uc?export=view&id=1f2vXcfOkeT4gaOUyBAYB-F47ziRjRzaI",
            "https://drive.google.com/uc?export=view&id=1z2KIzY9WRomfMcf2dlqMhINfR4gMgyNQ",
            "https://drive.google.com/uc?export=view&id=1--YLepJF0hL0ER__divCtxxJ9E_lujPU",
            "https://drive.google.com/uc?export=view&id=18sRhdG_APRX3EvCteFkdicP6652AXh_X",
            "https://drive.google.com/uc?export=view&id=1F4Y8V6nmoVCc-_EbLbedLJuOQ7HbKabu",
            "https://drive.google.com/uc?export=view&id=1daJ3i7LXJ6bZw2u37yF_l-hjRQe40aNF",
            "https://drive.google.com/uc?export=view&id=17kfXScOPd_vm7L-yLvUohcIvB38itHwN",
            "https://drive.google.com/uc?export=view&id=1VTUjwsDHbpm74XPtf6mpDIfq1KUimAuS",
            "https://drive.google.com/uc?export=view&id=1t5Por2UcuD1ZjKbRx_VW0WbR5T-S8gO2",
            "https://drive.google.com/uc?export=view&id=1wRFnOy-G8bAYDSvIFo7itx4vINvyQRFs"
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21 Tahun",
                "asal" :"Kalianda",
                "alamat": "Samping kost bang haikal",
                "hobbi": "Ngerjain TA",
                "sosmed": "@arientakhsnl",
                "kesan": "Kakaknyaa imutt dan jugaa cantikk",  
                "pesan":"Semangat terus kakkTA nya dan semoga diperlancar dalam pengerjaanya."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21,5 tahun",
                "asal": "Kuala Lumpur",
                "alamat": "Samping kost kak arienta",
                "hobbi": "Pacaran",
                "sosmed": "@lia.h_264",
                "kesan": "Kak vany imutt dan jugaa soft spoken",  
                "pesan":"Semoga banyak hal-hal baik yang menyertai kakak dan juga diberi kelancaran dalam hal apapun"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "30 Tahun",
                "asal": "Rumah Sakit",
                "alamat": "Belakang Wardat",
                "hobbi": "Kayak irfan",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel keren jagoo codingg dan juga tegas.",  
                "pesan":"Semoga sehat selalu, dan diberi kelancaran dalam hal-hal baik."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "17 tahun",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek Orang",
                "sosmed": "@desmanhal",
                "kesan": "Abangnya keren dan juga bijak.",  
                "pesan":"Semoga selalu sehat, bahagia, dan diberi kelancaran dalam segala hal baik."# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20 Tahun",
                "asal":"Lampung Tengah",
                "alamat": "Sebelah kost jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Abangnya ramah, dan kecee",  
                "pesan":"Semangat yaa bang kuliahnya, semoga sehat selalu, dan bahagia selalu."# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450008",
                "umur": "10 Tahun",
                "asal":"Di Bandung",
                "alamat": "Kamar haikal",
                "hobbi": "Goreng ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake keren, baik, dan ramah. ",  
                "pesan":"Semoga sehat selalu, dan hal baik yang abang lakukan dapat berbalik ke abang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21 Tahun",
                "asal": "Rahim ibu",
                "alamat": "Diatas kost jemar",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Abangnyaa keren, tegass, dan kecee.",  
                "pesan":"Semoga dilancarkan kuliahnya dan sehat selalu bang."# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "20 tahun",
                "asal": "Debu Tanah",
                "alamat": "Sebelah pasar",
                "hobbi": "Ngegiring anak ayam",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya asik, outfitnya kecee, dan ramah.",  
                "pesan":"Semangat terus kak dalam menjalani hari-harinya, semoga sehat selaluu."# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "17 Tahun",
                "asal": "Batam",
                "alamat": "Sebelah kost jemar atau kak arienta",
                "hobbi": "Ngurus pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Abangnya baik, dan kacamatanyaa kerenn.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18 Tahun",
                "asal": "Kampung Orang",
                "alamat": "Nomaden",
                "hobbi": "Duduk sebelah henry",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak putri orangnya ramahh, dan jugaa cantikkk.",  
                "pesan":"Semoga hari-harinya selalu dilancarkan dan juga sehat selalu"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Depan Pemancingan",
                "hobbi": "Ngoleksi ayam warna warni",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya cantik, ramahh dan jugaa asik.",  
                "pesan":"Semoga hal baik yang kakak lakukan dapat berbalik ke kakak jugaa, dan jugaa hari-harinya dilancarkan"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19 Tahun",
                "asal": "Lampung",
                "alamat": "Teluk",
                "hobbi": "Main game",
                "sosmed": "@azzelytn",
                "kesan": "Kakaknya cantik banget dan juga soft spokenn.",  
                "pesan":"Semoga hari-harinya selalu bahagia dan juga selalu dikelilingi orang-orag baik."# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21 Tahun",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakaknya ramah, dan jugaa baikk.",  
                "pesan":"Semoga sehat selalu dan bahagia selalu ya kakkk."# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "18 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sebelah kost haikal",
                "hobbi": "Gembala",
                "sosmed": "@jemarrro",
                "kesan": "Abangnya asikk dan juga asikk diajak ngobrol",  
                "pesan":"Semogaa selaluu semangaatt dann cariaa setiap harinya banggg."# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19 tahun",
                "asal": "Lampung tengah",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila cantikk, rambutnya baguss, dan ramahh",  
                "pesan":"Semoga banyakk hall-hal baik yang berdatangan dan jangan lupa bahagia."# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20 Tahun",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abangnya baikk, kerenn, dan ramahh.",
                "pesan": "semoga dilancarkan selama perkuliahann dan sehat selalu."# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20 Tahun",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Tidur",
                "sosmed": "@avi.nhr",
                "kesan": "kakaknya cantik, ramah, danjuga imut.",   
                "pesan":"Semoga selalu ceria dan sehatt selalu kakkk."# 1
            }      
        ]
        display_images_with_data(gambar_urls, data_list)
    PSDA()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qDxieoFDOLgaZ-X461WgHb7MzVemn6VR",
            "https://drive.google.com/uc?export=view&id=1bGPBM_wOVHaPlEzmO8b_lV7pkvYxCjSF",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BGrwAfA0uJIsTprBliBWio2VRJ2bRYEE",
            "https://drive.google.com/uc?export=view&id=1mOOcbUDbZxwusuw6bM5JPVE154MgXHeg",
            "https://drive.google.com/uc?export=view&id=1YvLbDUTXhdXMOHs9n-8hU5QpWCwQ2Uek",
            "https://drive.google.com/uc?export=view&id=1-uzdN5mGwbgzjdrEfN_BnkhNZKeX2wRH",
            "https://drive.google.com/uc?export=view&id=1eR356q7Lof9qg4EUesD6nFgxFDHiPlOe",
            "https://drive.google.com/uc?export=view&id=1QKx7uh5TaOBM_fW6rVFsfYgQwKtNSf4l",
            "https://drive.google.com/uc?export=view&id=1AhP6stxL9WbOPLsNdMjyz3SN2ubMYKGW",
            "https://drive.google.com/uc?export=view&id=1CqzizM2cbt6slp5aywLljyzt918z6ju5",
            "https://drive.google.com/uc?export=view&id=1HifLRfLlna7OxqqtGT49-SThl31BNiPf",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1IgKfA_AGPXLr8CyvSGal5oecaarJRgKx",
            "https://drive.google.com/uc?export=view&id=12Vou23eD73ggZVUmJkFpnepSdg-kPnaX",
            "https://drive.google.com/uc?export=view&id=1H9MX-ebBCoMOhZ6-GQyTD-VLi2TgVdyX",
            "https://drive.google.com/uc?export=view&id=19Ly7a3uDSxZIiwGMVNObUItsyq4RBPG1",
            "https://drive.google.com/uc?export=view&id=1F2ws3AgNmib430waSMLZW01YJWuQx-nU",
            "https://drive.google.com/uc?export=view&id=1g9C8qbW0BjtIbqUOfQq6fYeWxZPejOWS",
            "https://drive.google.com/uc?export=view&id=1QoMbkf5JE3-wtSt6VJBAJeIXpikjR5t7",
            "https://drive.google.com/uc?export=view&id=1AjsBBOXNW7iRuLeFBSIwK_H_Bkokt8n0",
            "https://drive.google.com/uc?export=view&id=1w2PxeuZJhuBTy6en7FikfQrvF_kaLxVT"
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game & travel",
                "sosmed": "@biyokcb",
                "kesan": "Abangnyaa asikk, chill, dan kerenn karena jago codingg.",
                "pesan": "Semangatt TA nya banggg, semoga hal-hal yang dilakukan berjalan lancar"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "kak tanty orangnya ceria bangett dann jugaa ramahh ke semua orang.",
                "pesan": "Semoga dilancarkan kuliahnya dan jangan lupa bahagia ya kakkk."
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "...."
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "abangnya asik banget dan jugaa ramaahhh",
                "pesan": "Semogaa sehat selalu ya bang da jangan lupaa tersenyumm."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakanya cantikk dan juga ramah banget",
                "pesan": "Sehat selalu ya kak dan semoga hari-harinya bahagiaa"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya lucuuu, dann baikk bangett",
                "pesan": "jangan lupa jaga kesehatan dan sehat selalu ya kakkk."
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya keren bangettt dan jugaa baik bangett",
                "pesan": "Semoga banyak hal-hal baik yang berdatangan."
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "Kakaknya lucuu, baik, dan jugaa cantikk",
                "pesan": "Semoga sehat dan bahagiaselalu yaa kakkdalam menjalankan perkuliahan."
            },
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya kerenbaik, dan juga soft spoken.",
                "pesan": "Semangat teruss bangg kuliahnyaa dann semogaa selaluu mendapat hal-hal baik disekeliling abang."
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Kak elsa ceriaa, baik, dan ekstrovert bangett.",
                "pesan": "Semoga selalu bahagia yaa kaa, dan tetap ceria."
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kakaknya gemassss, baik, dan jugaa ceria banget",
                "pesan": "Semangatt kaa menjalanii kehidupan selaa kuliahh, semogaa selalu dilancarkan."
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way huwi",
                "hobbi": "Badminton",
                "sosmed": "@_loviaa",
                "kesan": "Kakaknya asikk,ekstrovert dan jugaa seruuuww.",
                "pesan": "Semoga selaluu semangatt yaa kaaa dan selalu bahagia."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abangnyaa baikk dan juga keren",
                "pesan": "Semangatt terus ya bang kuliahnyaa, semoga selalu bahagiaa ya bangg."
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakakanya cantik, ramah dan jugaa imutt",
                "pesan": "Semoga selalu mendapatkan kebahagiaan disela-sela kesibukan perkuliahan."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya keren, baik, dan juga pinter bangett",
                "pesan": "Semangata ya bang Ta nya, semoga selalu diberikan kelancaran dan juga kebahagiaan"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya cantik dan jugaa imutt, selain ituu keren bangett jugaaa",
                "pesan": "Semogaa apa yang sedag kakak usahakan dapat terwujud, dan mendapat hal-hal baik."
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik, dan jugaa kerenn banget",
                "pesan": "Sehat selalu ya bang, dan bahagia selaluuu"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya asik banget, mudah berbaur dengan orang lain.",
                "pesan": "Semangat ang kuliahnya, semoga selalu lancarr hari-harinya"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Bang kaleb Kerennn, baik, dan juga pinter bangett",
                "pesan": "Sehat selalu bang, dilancarkan juga perkuliaannya, dan jugaa bahagia selalu."
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya lucu, baik, ramah, dan pendiam.",
                "pesan": "Semoga lancar ya kak kuliahnya."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "Abang keren bangett, publik spekingnya jago banget, dan sangat menginspirasi.",
                "pesan": "Semoga tetap menginspirasi dan hal baik selalu datang ke abang."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Orangnya aslinyaa kocakk dan lucuu.",
                "pesan": "Semoga selalu bahagia dan sehat selalu bangg."
            },
        ]
        st.subheader("Departemen Internal")
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15IQhi4xdNz9G0PaxMdDe_UHnJtZ7WQxU",
            "https://drive.google.com/uc?export=view&id=14FRPbTL59EoEg9sDQ45NAl0vUKLiQuXl",
            "https://drive.google.com/uc?export=view&id=1SYZiW975DJTOwg6Rb6Kn3EI81V7bVsyI",
            "https://drive.google.com/uc?export=view&id=1CCnSQz1Xh3VCTs0ctmmE-t5-KMNade6A",
            "https://drive.google.com/uc?export=view&id=1k9o0kSa-L_6jHjk3fO07RSyBsP7byOgL",
            "https://drive.google.com/uc?export=view&id=10f5i79KJAgn8gShnNbKA6ch7UuFYiVc0",
            "https://drive.google.com/uc?export=view&id=14UG2qGSLwr-c0bU0GEZF49Zq_yKdVvc9",
            "https://drive.google.com/uc?export=view&id=1iYFNNNeTVkA40PKOjE8hVlqX0elUi_aG",
            "https://drive.google.com/uc?export=view&id=1xzROCWTMwAY-mVRK1vECe0WIrHknMvSP",
            "https://drive.google.com/uc?export=view&id=1GdeatoU5F-Q-pFflK9zoBji8bY9V1wlW",
            "https://drive.google.com/uc?export=view&id=1HYFijvjFF2xgpdIxFBIpFfWIXo-nMj9N",
            "https://drive.google.com/uc?export=view&id=1RrVLtL1Y1L1U9RlS1x2RK9VXy41Sf1rW",
            "https://drive.google.com/uc?export=view&id=16bCO4bRb4BjGPbMFu1kUbfBGBWNFwDDk",
            "https://drive.google.com/uc?export=view&id=1w-I4QOj2x0Gc4NhuU4yWh_dNwaxvhyN4",
            "https://drive.google.com/uc?export=view&id=1SvDUhvH2FcFy6rqlS4KbMthPcPP6qwjY",
            "https://drive.google.com/uc?export=view&id=1poB9pa7c7-Tq27ShlPew-AVW9luENsuM"           
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450006",
                "umur": "20 Tahun",
                "asal":"Sidikalang, Sumut",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "Abangnya keceee dann kocak.",  
                "pesan":"Semoga selalu bahagia dantetap kece bangg."# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21 Tahun",
                "asal": "Untung suropati",
                "alamat": "..",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya lucuu dann baikk bangett.",  
                "pesan":"Semangat terus ya kuliahnyaaa, dan jangan lupa jaga kesehatan kak"# 1
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "11",
                "asal": "Kisaran",
                "alamat": "Untung",
                "hobbi": "NMenyapa satpam ITERA",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakaknyaa cantikk, senyumnya maniss dan soft spoken.",  
                "pesan":"semangat terus kakk TA nyaa semoga diperlancar"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang, Sumbar",
                "alamat": "Perumnas way kandis",
                "hobbi": "Ngikutin drama tiktok",                
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya asik dan jugaa baikk bangett",  
                "pesan":"Semangat terus dalam menjalani hari-harinya dan juga bahagia selalu."# 1
            },
            {
                "nama": "Ahamad Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "Abangnya baik dan juga soft spokenn.",
                "pesan":"Semangat terus ban Ta nya semoga diperlancar."# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "12450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisahkhair.",
                "kesan": "kakaknya baik bangett, dan jugaa soft spokenn.",  
                "pesan":"Jangan lupa jaga kesehatan dan jangan lupa bahagia ya kakkk."# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir belwis",
                "hobbi": "Suka begadang",
                "sosmed": "@cerine_ipynb",
                "kesan": "kakaknyaa cantikk, murah senyumm dajuga baik bangettt",  
                "pesan":"Semoga dilancarkan ya kakk kuliahnya dan jangann lupaa jaga kesehatan."# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "1244500094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Abangnya receh, kocak, dan jugaa asikk bangettt.",  
                "pesan":"Semangat terus bang kuliah dan semoga banyak hal-hal baik yang didapat."# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "1244500051",
                "umur": "20 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya cantik, baik, dan baik banget",  
                "pesan":"Semangat terus belajar dan kuliahnya kak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",                
                "sosmed": "@rozakramdani_",
                "kesan": "Abangnya baikk dann orangnya tepatt waktuuu",  
                "pesan":"Semangat terus bang menjalani hari-harinyaa."# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",                
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baikk dan juga asik bangettt.",  
                "pesan":"Semoga selalu bahagia dan sehat selalu yaa kakkk."# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 Tahun",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Masak",                
                "sosmed": "@audina_",
                "kesan": "kakaknyaa baikk, cantik, dan jugaa sangat ramahh",  
                "pesan":"Semangatya kakkk kuliahnyaa, semogaa banyak hal baik yang kakak dapatkan"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa minang",                
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya asik, cantik, dan baik banget",  
                "pesan":"Semogaa adaa banyakk hal baik yang kakak dapattkann"
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21 Tahun",
                "asal": "Toba,Sumut",
                "alamat": "Airan Raya",
                "hobbi": "nonton drakor",                
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakaknya lucu, baik, dan jugaa imuttt.",  
                "pesan":"Semogaa banyakk hal baik yang didapat di setiap harinyaa"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20 Tahun",
                "asal":"Sematera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu",                
                "sosmed": "@Muhvinz_",
                "kesan": "Abangnya baikk, ramahh, dan jugaa murah senyum.",  
                "pesan":"Semangat terus ya bangg,semoga dilancarkan kuliahnya."# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama aqila",                
                "sosmed": "@snasaa._",
                "kesan": "Kak bina imut, lucu, baik,soft spoken, suka menolong sesama, ibu anova, dann murah senyummm.",  
                "pesan":"Semangat kak bina kuliahnya dan sehat-sehatt kaaa pp dari natar"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()
# Tambahkan menu lainnya sesuai kebutuhan
