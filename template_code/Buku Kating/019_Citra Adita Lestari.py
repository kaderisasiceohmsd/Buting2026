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
            "https://drive.google.com/uc?export=view&id=1DDML3VGRstrbRkXbDMzRxz8ySqqcUNL9",
            "https://drive.google.com/uc?export=view&id=1UZtzzXPiWuucQudgTMYVao6MbVWVFG-7",
            "https://drive.google.com/uc?export=view&id=1Debp6j9envVszBtcdJDZgZI-uTWKAEod",
            "https://drive.google.com/uc?export=view&id=19uIqZFIYAUM2ghM14e-TfyySDIYZKEzt",
            "https://drive.google.com/uc?export=view&id=1X6AIR7_P0md50PcaYpVX70ct8Ikwo81Y",
            "https://drive.google.com/uc?export=view&id=1ALk3zJITEe4XWljCh6abvT12uUjQQ5er",

        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marapaung ",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "bang Ginda asik banget orangnya",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "abangnya asikk bangett",  
                "pesan":"semangat terus kuliahnya bang Aqil !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "kakaknyaa cantik dan imut",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "bang Qois keren banget orangnya",  
                "pesan":"semangat terus kuliahnya yaa kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak Hafsa cantikkk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak Luthfi cantikkk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IoW_OMPDwc379QdodTPIjOhcVZIhbz4I",
            "https://drive.google.com/uc?export=view&id=1nkJTOuQ0wiVFHl2_nPc8yY8bahlSZWgV",
            "https://drive.google.com/uc?export=view&id=18rGvHD2J3vkZ3LgNEFKhDg44ETf3cpbw",
            "https://drive.google.com/uc?export=view&id=1dUVlAtTesYy_JswwZdRBBRl3TGqSl9aw",
            "https://drive.google.com/uc?export=view&id=1TBRejihSG-CxFT4O3JnR0u2E2CvDwQkI",
            "https://drive.google.com/uc?export=view&id=1m2ox7MwfBJGLtV9ScLb0PDDEmLkLEKAM",
            "https://drive.google.com/uc?export=view&id=1awiF7hzJ89zF5MmJuQ1Prxa-aASkApT4",
            "https://drive.google.com/uc?export=view&id=1LQdkvQV6KxKUSnbGfxujc5akmzmTJdfo",
            "https://drive.google.com/uc?export=view&id=14IISs1t98h9CInchkhBf-ol8BL3AeHFe",
            "https://drive.google.com/uc?export=view&id=1qSZJxEChLrDGRlEu7zUGEDZWBdmoRsNa",
            "https://drive.google.com/uc?export=view&id=15d3W-bvZbED_KU5Ijh9VAPNamMxsmOc3",
            "https://drive.google.com/uc?export=view&id=11PI-cn3zrwJST8qhfJZagbO0I1ABLJx8",
            "https://drive.google.com/uc?export=view&id=1gFDzUHAkO1aLV64Xwz2dT0paG-Cej8RQ",

        ]
        data_list = [
    {
        "nama": "Ridho Benedictus Togi Manik",
        "nim": "123450066",
        "umur": "20",
        "asal": "Kuala Lumpur",
        "alamat": "GH",
        "hobbi": "Wawancara",
        "sosmed": "@iamridhomanik",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Juesi Apridelia Saragih",
        "nim": "123450085",
        "umur": "19",
        "asal": "Pelangi",
        "alamat": "Singkawang",
        "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
        "sosmed": "@j__eesie",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Dharu Cahyoaji Sasongko",
        "nim": "123450023",
        "umur": "19",
        "asal": "Lampung",
        "alamat": "Bandar Lampung",
        "hobbi": "Makan mie gomak",
        "sosmed": "@exvoltas & @ddharu",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "GH Mikael Niko A S",
        "nim": "124450079",
        "umur": "20",
        "asal": "Pasir Sakti",
        "alamat": "Jati Agung",
        "hobbi": "Tidur",
        "sosmed": "@me._kael",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Siti Sarifah Sumamah",
        "nim": "124450015",
        "umur": "19",
        "asal": "Bekasi",
        "alamat": "Kedaton",
        "hobbi": "Mancing",
        "sosmed": "@syt.rifa",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Givaro Ananta",
        "nim": "123450078",
        "umur": "21",
        "asal": "Lampung Barat",
        "alamat": "Sukabumi",
        "hobbi": "Minum Kopi",
        "sosmed": "@givarooo",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Afghanis Nursholehatunisa",
        "nim": "124450042",
        "umur": "20",
        "asal": "Kepulauan Mentawai",
        "alamat": "Kadang di kost putri kadang di kost sekar",
        "hobbi": "Memanjat",
        "sosmed": "@afghanisnt_",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Hani Qurrota Aini",
        "nim": "124450020",
        "umur": "20",
        "asal": "City earth",
        "alamat": "Sukarame",
        "hobbi": "Baca AU",
        "sosmed": "@haniqurratuain_",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Jeremia Halim",
        "nim": "124450101",
        "umur": "20",
        "asal": "Tangerang",
        "alamat": "Teluk Betung",
        "hobbi": "Nyanyi, olahraga",
        "sosmed": "jeremia_hm",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Monica Patricia Tanjung",
        "nim": "123450073",
        "umur": "21",
        "asal": "Jakarta Barat",
        "alamat": "Kotabaru",
        "hobbi": "Lari",
        "sosmed": "@monica_tjg",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Jona Timothy Ogatse Panjaitan",
        "nim": "124450121",
        "umur": "20",
        "asal": "Depok",
        "alamat": "Pemda Raya",
        "hobbi": "Nge-gym, koleksi figur",
        "sosmed": "@nagatseee",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Sekar Dini Widya Putri",
        "nim": "124450082",
        "umur": "20",
        "asal": "Metro",
        "alamat": "Pemda",
        "hobbi": "Melukis",
        "sosmed": "@sekardnwp",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    },
    {
        "nama": "Wan Nashwa Alhasni Yuska",
        "nim": "123450077",
        "umur": "20",
        "asal": "Pasay",
        "alamat": "Belwis",
        "hobbi": "Nyapa angin",
        "sosmed": "@nshaysk",
        "kesan": "Kakak ini asik saya suka belajar dengan dia",
        "pesan": "semangat terus kuliahnya kakak !!!"
    }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gFAWAhXZTX-uF48xycr6wP7ZQU_YUkfX",
            "https://drive.google.com/uc?export=view&id=1b7T-1KjnFGjPDXY98rQ2-BWuph-7X_w9",
            "https://drive.google.com/uc?export=view&id=17xJk_Q3cjute8S6KKy93ecivzhfGP_15",
            "https://drive.google.com/uc?export=view&id=1M--QLeqFcAH-v_3ofKRnOJxU9qcmzWdx",
            "https://drive.google.com/uc?export=view&id=1U87Vb1CrpyjL6QXT5l075HcuHTUZgpNB",
            "https://drive.google.com/uc?export=view&id=1uzIun3PUbzwZ-pXTLCcdxklKpE-7Mgoe",
            "https://drive.google.com/uc?export=view&id=1oYanxcOr6YlAEsl0Wf4g4AfTWP7Lk0H3",
            "https://drive.google.com/uc?export=view&id=12Sm0qqncAbWRTw4Mmf6Klml1lJVFh4MR",
            "https://drive.google.com/uc?export=view&id=1WhN_ZrOIEQd9Rj4JvHQxUveAbQqXUWTV",
            "https://drive.google.com/uc?export=view&id=1P1qX1WVAux1v3W5nLUom90nhaz_tIQ8h",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak Fathinah baik, humble, anggun, dan disiplin",  
                "pesan":"Semoga diberi kemudahan di dunia dan akhirat ya kak!!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengerin lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak Nadya cantik, baik, humble dan keren bangetttt",  
                "pesan":"Semoga hal baik selalu bersama kakak!!!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Bang Helmy asik, humble, dan kerennn bangetttt",  
                "pesan":"Semogaa sukses selalu ya bang!!!"# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang Fernando asik, baik, dan kece bangetttt",  
                "pesan":"Semoga selalu dimudahkan rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": "Kak Suci baikk, lucuu, cantik, humblee dan asik bangetttt",  
                "pesan":"Semoga selalu sehatt, bahagia, dan dijauhkan dari marabahaya ya kak!!!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Bang Wielman Baik, keren dan cool",  
                "pesan":"Semoga selalu diberikan kelancaran ya bang!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kak Lia baik, lucu, dan humble bangetttt",  
                "pesan":"Semoga selalu bahagia dimanapun kakak berada ya kak!!!"# 1
            },            
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak Aqila baik, lucu, ceria dan kalo ketawa ikonik bangetttt",  
                "pesan":"Semoga selalu sehat dan selalu ceria ya kak!!!"# 1
            },            
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang Hazel baik, kece, keren, dan humble bangetttt",  
                "pesan":"Semoga selalu diberikan keselamatan ya bang!!!"# 1
            },            
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak Dwi baik, lucu, dan humble bangetttt",  
                "pesan":"Semoga selalu dijauhkan dari kejahatan ya kak!!!"# 1
            },                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EB7H5Vy3Lt1xRj1XdUylDd3paUBiR8MP",
            "https://drive.google.com/uc?export=view&id=11v1OAC9_pEPqME3c8YsmU7wzmavU1GUK",
            "https://drive.google.com/uc?export=view&id=1DokJPgIMzr6RCPl3tV_rqPC8LpIJZAUQ",
            "https://drive.google.com/uc?export=view&id=1nDYzrjn9maxlcqHOMFNPsaC866eSndvc",
            "https://drive.google.com/uc?export=view&id=1Ry_CwPdRT9pYdlHvV5Y0I7BB8wANeRh1",
            "https://drive.google.com/uc?export=view&id=1A7C1an8L9EUUW6m3qOvrvZVyMdHuDoh7",
            "https://drive.google.com/uc?export=view&id=1oKarFtmDHRs_BEVwQV3SWSGIGMQ2boRl",
            "https://drive.google.com/uc?export=view&id=1UeoVfU7wkd5aYGjF6qHY1WydnRQMYI5f",
            "https://drive.google.com/uc?export=view&id=1SzQXxPs910z-665G67ANEyZ1M6ukw0HC",
            "https://drive.google.com/uc?export=view&id=1sfqIl3RIx4Wq1bZDncEJGhhKJtPgEvj2",
            "https://drive.google.com/uc?export=view&id=1-e3GzolRH7bFgcnyKSwloPCiLnbgM4jm",
            "https://drive.google.com/uc?export=view&id=1vEpwmVCRRuEDQWudHSurRKFXLZoppiP3",
            "https://drive.google.com/uc?export=view&id=1PciowHnZNnWzrNQzcVx626PLX07DMtTy",
            "https://drive.google.com/uc?export=view&id=1oYanxcOr6YlAEsl0Wf4g4AfTWP7Lk0H3",
            "https://drive.google.com/uc?export=view&id=12xik-Ah2HH6LfbrZeyyYXtRlVDCHlSD_",
            "https://drive.google.com/uc?export=view&id=1R-dvvPdAikn10BETZC5cRfqZSKgaGd2D",
            "https://drive.google.com/uc?export=view&id=1W_yHcHn5CvgDIrGZ2lMAimcmPcsfCoYm",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta baik, keren, peduli, dan humble bangetttt",  
                "pesan":"Semoga diberi kesuksesan dan kesehatan selalu ya kak!!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baik, berwibawa, dan disiplin banget",  
                "pesan":"Semoga selalu diberi kemudahan ya kakak!!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel Berwibawa, Asik dan jago banget sulap, baik, tegas, dan keren banget",  
                "pesan":"Semogaa sukses dan berkah selalu ya bang!!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, gentle, tegas, dan energik bangetttt",  
                "pesan":"Semoga selalu diberikan kesehatan dan kekuatan ya bang!!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake humoris, asik, humble dan baik bangetttt",  
                "pesan":"Semoga selalu sehatt, bahagia, dan lancar rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar Baik, keren dan imut, serta suka berbagi ilmu",  
                "pesan":"Semoga selalu diberikan kelancaran ya bang!!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah, tegas, keren, baik dan humble bangetttt",  
                "pesan":"Semoga selalu semangat dan bahagia ya kak!!!"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, tegas, asik, jago futsal, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan terhindar dari segala penyakit ya bang!!!"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri baik, lucu, imut, dan humble bangetttt",  
                "pesan":"Semoga selalu diberikan keselamatan dan kebahagiaan ya kak!!!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baik, ber aura, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat, bahagia dan diberi keselamatan ya kak!!!"# 1
            },            
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman baik, asik, humble, dan jago bangetttt deffense futsalnya",  
                "pesan":"Semoga selalu semangat dan sukses ya bang!!!"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel baik, kalem, dan humble bangetttt",  
                "pesan":"Semoga bahagia dimanapun kakak berada ya kak!!!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan bahagia ya kak!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jere humble, asik, kece, dan baik bangetttt",  
                "pesan":"Semoga selalu kuat dan sehat ya bang!!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu dilancarkan urusannya ya kak!!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli kece, rambutnya keren terus, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan doa nya diwujudkan ya bang!!!"# 1
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi baik, lucu, kalem dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan dilancarkan urusannya ya kak!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-6FRhNriyqZ3HDjqdhouvDZLMaMI2Uds",
            "https://drive.google.com/uc?export=view&id=1qYYMrUDdvoS4wWOfW39TEHBUhqhie7Py",
            "https://drive.google.com/uc?export=view&id=1EIoSZHu-ka6zdgaOpwyeFIXrKxFmDk0B",
            "https://drive.google.com/uc?export=view&id=1m0BkZk9DtFjKpg2mmRxoSjjxR_Do4Swq",
            "https://drive.google.com/uc?export=view&id=1sWLLAwiYlQ51hDwR4QKH-UUVUPNuDfzr",
            "https://drive.google.com/uc?export=view&id=1kkkfZlrYjoMFmmtwbxHcEVo46aR6P4EJ",
            "https://drive.google.com/uc?export=view&id=1euv6fpG-mHpfpKJBZJm3AZF6G3jrcS3W",
            "https://drive.google.com/uc?export=view&id=1hy4IQbEVXpYfxLQ7PdKsxCSGZ4XdWF6Z",
            "https://drive.google.com/uc?export=view&id=1BEpZycSlgxD-wH0PGwvs8wnK6a4AsP4s",
            "https://drive.google.com/uc?export=view&id=1PcZnOXaG3ri5yw_KFLtRWveRYlAzcDDv",
            "https://drive.google.com/uc?export=view&id=1lHDYVkviexqFNxIJ2E-rkAYq8ju7yy94",
            "https://drive.google.com/uc?export=view&id=1EAdofTThaP-GdgsICIlWojb7b7nGTwfW",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Bang Ihsan baik, seru, asik, lucu, dan humble bangetttt",  
                "pesan":"Semoga selalu dilancarkan rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Naya baik, perhatian, seru dan humble banget",  
                "pesan":"Semoga selalu diberi keceriaan dan kemudahan ya kakak!!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah baik, kalem, dan humblee banget",  
                "pesan":"Semogaa sukses teruss ya kak!!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal":"Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang Hasan baikk, kalem, dan santay orangnya",  
                "pesan":"Semoga selalu diberikan keselamatan ya bang!!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "Kak Layina baikk, ceria, dan humblee orangnya",  
                "pesan":"Semoga selalu diberikan kebahagiaan ya kak!!!"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Bang Iqbal keren, baik, dan humble banget",  
                "pesan":"Semoga selalu tabah menjalani hidup ini ya bang!!!"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@tallhtine_",
                "kesan": "Kak Talitha baik, ramah, humble bangett",  
                "pesan":"Semoga selalu semangat ya kak!!!"# 1
            },            
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak Nadia lucu, baik, dan humble bangetttt",  
                "pesan":"Semangat terus kak cari duitnya!!!"# 1
            },            
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Baturaja Sumatera Selatan",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "Bang Pome kece, tamvan, keren, dan baik orangnya",  
                "pesan":"Semoga selalu kuat dan tabah ya bang!!!"# 1
            },            
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "Bang Afdhal keren, tamvan, and baik bangett",  
                "pesan":"Semoga selalu sehat, bahagia dan diberi keselamatan ya Bang!!!"# 1
            },            
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Nonton Kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak Anggun baik, humble dan lucu orangnya",  
                "pesan":"Semoga selalu semangat Nonton kartunnya kak!!!"# 1
            },            
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Margo Lestari",
                "hobbi": "Lagi gak punya hobi",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak Della baik, ceria, dan humble bangettt",  
                "pesan":"Semoga bahagia dimanapun kakak berada ya kak!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()
# Tambahkan menu lainnya sesuai kebutuhan

