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
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
            "https://drive.google.com/uc?export=view&id=1Thnh2F0RstPDOR_Bc885HnzBH0Y9_PHD",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Abang nya baik dan sangat menginspirasi saya, time management nya keren sehingga balance antara organisasi dan kuliah",  
                "pesan":"semangat kuliahnya lancar luncur TA nya bang"# 1
            },
            {
                "nama": "Muhammad  Aqil Ramadhan",
                "nim": "1223450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil111",
                "kesan": "JUJURR abang ini kerenn, gatau tapi keren banget",  
                "pesan":"semangat terus bang aqill"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi seruu dan asikk banget",  
                "pesan":"semangat terus kuliahnya kakak !"# 1
            },
             {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini seru dan baikk",  
                "pesan":"semangat kuliahnya bangg, dilancarin TA nyaa"# 1
            },
             {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya seruuuu bangettttttt",  
                "pesan":"semangat terussss kakkkkkk!"# 1
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaaemdhn",
                "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk",  
                "pesan":"semangat untuk mengejar S.Si.d kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1agpykvBsiH-ZeQCGNKu-7s72PQXu3-8h",
            "https://drive.google.com/uc?export=view&id=1uqbIcv4ueBXc0XI7wyQtgUDiDvcnbIeH",
            "https://drive.google.com/uc?export=view&id=1IVfqvgMhPv4mWXjXULhjj91KlEAWj9_u",
            "https://drive.google.com/uc?export=view&id=1-E6gLTUVv_Hc2ZAl_AZDaLeT9prxFgMo",
            "https://drive.google.com/uc?export=view&id=1gNncmcU1f8zoq75808bt3fhP8uV18EbI",
            "https://drive.google.com/uc?export=view&id=1ELKvb424mN8cH3_zDvBfWZbR-JcvqG5A",
            "https://drive.google.com/uc?export=view&id=1zMrp-gIUlSSQkdRcMyAaN5NC0KXoebcR",
            "https://drive.google.com/uc?export=view&id=1-XcCitthUyoOa5pEYRbALT8LFWG8M2t8",
            "https://drive.google.com/uc?export=view&id=1TE366QnGMPYfPMncFh67_YoExIXAiryu",
            "https://drive.google.com/uc?export=view&id=1wbcjBxTzyyjZQ3wijNDwdx6t1X1jg5Hd",
            "https://drive.google.com/uc?export=view&id=1KoD01atLcwhJo4-2vi6eMfvn870vNMrh",
            "https://drive.google.com/uc?export=view&id=1jeAs3WNOPwAyJ0RhrI3xrUwkJq54QAtw",
            "https://drive.google.com/uc?export=view&id=1w1kstXp4ATTA3-pD6c0Pywfa1Vzy_838",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha",  
                "pesan":"Semangat bang TA nyaa, semoga dilancarkan semuanya dan lulus tepat waktu ya bangg. Anak magang baleg selalu mendoakan yang terbaik untuk ayah dido"# 1
            },
            {
                "nama": "Juesi Aprilia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marvel",
                "sosmed": "@j_eesie",
                "kesan": "GEMASSSSS! beneran imut kakanya dan seru banget dengerin storytelling ka juee, karena kayak sivia the catchup club cara kaka ngomong",  
                "pesan":"Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupun api Baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Pinter bnaget abangg, tips and trik mapres bangg",  
                "pesan":"Semangat kuliah dan TA nya, semoga dimudahkan seluruh urusannya, aamiin!"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD musang",
                "sosmed": "@me._kael",
                "kesan": "Lucu banget jokes jokes abangnyaa",  
                "pesan":"Semangat terus kuliah dan organisasinya!"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "18",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Imutt sekali kakanyaaa",  
                "pesan":"Semangattt kaa kuliahnyaa, kaka imut balegg"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip chill banget orangnyaa dan seruu",  
                "pesan":"Semangat terus bang kuliahnya dan semoga dimudahkan TA nya ya banggg, Aamiin!"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Public speakingnya bagus, aku dukung kaka jadi the next kadiv komisi 2 #YIPPIE",  
                "pesan":"Semangat kaa kuliah dan organisasinyaa!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "24",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu dan gemas bangettt",  
                "pesan":"Semangat ka menghadapi bang Ridhoo, semoga dilancarkan semua urusannya kaaa!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Keren dan berwibawa",  
                "pesan":"Semangat bang kuliahnyaaa!"# 1
            },
            {
               "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Lucu, gemas, tapi tegas",  
                "pesan":"Semangat kaa kuliah dan organisasinyaaa!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Lucu abangnya, jokes jokesnya juga fresh",  
                "pesan":"Semangat abang kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Tegas tapi chill juga",  
                "pesan":"Semangat terus ka kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Lemah lembut sekaliii",  
                "pesan":"Semangat kaa TA dan kuliahnyaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

# Tambahkan menu lainnya sesuai kebutuhan
