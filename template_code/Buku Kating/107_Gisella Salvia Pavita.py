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
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#9C6AC0"},
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
            "https://drive.google.com/uc?export=view&id=1n4Dr3NwqGSWJ6ePUZs_nx1rqlLiD0MSv",
            "https://drive.google.com/uc?export=view&id=1JGFXuvt-er7Q0GqgXsYn49tfeDmYJD1S",
            "https://drive.google.com/uc?export=view&id=1Q_X8T6Xf12b0tzagpOYr6YV_6ARXhm2H",
            "https://drive.google.com/uc?export=view&id=1BXPM3Ivv3F-J6-NKQ3Tukxjx1DjBYVjV",
            "https://drive.google.com/uc?export=view&id=1hu6rdYSy6W_qvlwaxiadjrGXIAIvlsZ_",
            "https://drive.google.com/uc?export=view&id=14UuJPYZhQ4RSgSU6wdiumJUqkJUiiLcR",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya sangat humble dan juga baik.",  
                "pesan":"Semoga sukses selalu bang fajar."
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak nya asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya baik banget dan suka deh di ajarin praktikum ads sama ka efi",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "abangnya baik banget",  
                "pesan":"semangat terus kuliahnya abang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "kakak nya baik banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kaka nya baik dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18mLnnbUCg12xnbJWnbmIim86Ml5R2Nm9",
            "https://drive.google.com/uc?export=view&id=1xkljzLzprwqJs2e8OuY-GBfsawk4nH0O",
            "https://drive.google.com/uc?export=view&id=18tEvj4DX_3EN3B-MGoHUpW-qtPOOPGow",
            "https://drive.google.com/uc?export=view&id=1pBXTXSECkyedIT6K617E1C6-mE7uZm9D",
            "https://drive.google.com/uc?export=view&id=1KoBxYHvHpMp22v9DpNYOJtDiLDSoks3v",
            "https://drive.google.com/uc?export=view&id=1QhQ6-giusaF6bFlRgoZ2oXCCG7O-h819",
            "https://drive.google.com/uc?export=view&id=16DgMYKLMqHPp-J4CTtiD-VWv6mTugXn_",
            "https://drive.google.com/uc?export=view&id=1Vs0Zm2DWEoO3qqoSz4Lyd1jRCIMLqDF6",
            "https://drive.google.com/uc?export=view&id=1wzfx9-g65bE_GVEf02HITnWTNkDsokWS",
            "https://drive.google.com/uc?export=view&id=1DjOdoDRL0Jy7247-b9X3DWflrxPImT5W",
            "https://drive.google.com/uc?export=view&id=1z90cxrIxzJZHaqLGwrbMgZ6bjJF35mcJ",
            "https://drive.google.com/uc?export=view&id=1VMBkXPr3Vg_uEoEdLrL-krB84twgd9Bj",
            "https://drive.google.com/uc?export=view&id=1ErpWZ85yidkRFWADsGXkVTlI7pE-19Ek",

        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kuala lumpur",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Abang ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ld7xrgbZs_5Z1uflSi6e_uJnlnIizfVh",
            "https://drive.google.com/uc?export=view&id=1a9y5D2yh4K4rvYVqh2IOLexnehoOTjIG",
            "https://drive.google.com/uc?export=view&id=1-Vk6K-pbY7_jh35fuabrnE96KUmZMem7",
            "https://drive.google.com/uc?export=view&id=1BShh3Lrzh0Hho_osI7uDT-7b5vpqtyed",
            "https://drive.google.com/uc?export=view&id=1C5qTEyK8DJHHnVB5S83uGdMo6yI8uPcL",
            "https://drive.google.com/uc?export=view&id=1AIegfS6Ej2VBg3hiAcVVDoaYqnv90osE",
            "https://drive.google.com/uc?export=view&id=1ryEGHgDBUBO5TC8HDYq5rCH3M1ss5mgn",
            "https://drive.google.com/uc?export=view&id=12OX-sdqe6VaYH7nupoSBPYGFXB1iyC5V",
            "https://drive.google.com/uc?export=view&id=1fMmxFd0qDQh4kdQOlJZqlTKqJo75FP92",
            "https://drive.google.com/uc?export=view&id=1WJZ7PPlzxiHT9s9xH0DuwbXwtc6GcaDo",
            "https://drive.google.com/uc?export=view&id=1MFYOLDlr80Ilte4FJvtULigpZz3Nj-Nq",
            "https://drive.google.com/uc?export=view&id=1e5oTheqHTcvq9mtwBLE2JzkTbGisSpOG",
            "https://drive.google.com/uc?export=view&id=1BzU5a3zhv1J7cYGoRr4Bl5qH191R0uiz",
            "https://drive.google.com/uc?export=view&id=1oh8qn8HTouUujIJqo4lSzuMTnsKq3qe-",
            "https://drive.google.com/uc?export=view&id=1jUkdQ3p9WKKzR9A5_sexlldZtZ3aZowd",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Maluku",
                "alamat": "Panjang",
                "hobbi": "Menari",
                "sosmed": "@kevinaj__",
                "kesan": "Abang ini baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "..",
                "umur": "..",
                "asal":"..",
                "alamat": "..",
                "hobbi": "..",
                "sosmed": "...",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
                
            }
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini asik dan baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini asik dan baik",  
                "pesan":"semangat terus kuliahnya bang !!!"
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()
    
elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=123dTATmdwTUSadPFtqPpFKiLBGYL-1jz",
            "https://drive.google.com/uc?export=view&id=1WbtI870GlQaqSG8E-oxiF1WIjGbgqBaN",
            "https://drive.google.com/uc?export=view&id=1QT1AkScevYkdV0ZClUcJix_PH4C30JZe",
            "https://drive.google.com/uc?export=view&id=15MwxDa0vG8hmUTyKJyOgG9uRPcHtWMT4",
            "https://drive.google.com/uc?export=view&id=1IvsuwH5JPny4co3vy9fCjCpAmqyIcmtp",
            "https://drive.google.com/uc?export=view&id=1C1_qzyTvbgFLxIgUKfN3A84qsjZ9JmrR",
            "https://drive.google.com/uc?export=view&id=1U9J-Ye0aOZO_SGOsLleamKnZkqZECd1b",
            "https://drive.google.com/uc?export=view&id=1P7kOf-Ye6enFcO-2EoRjvS5G6y6Y_YLb",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=19XEAP-6N2Tt8zNprgBXFhEJA_11e9JKR",
            "https://drive.google.com/uc?export=view&id=1jO2MBglLIT-GqFCfyfk6NoTWABYJ8NhT",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1YgXLT1bKMAJilOF6TDMCEOrgxoU9E1CA",
            "https://drive.google.com/uc?export=view&id=1l7-DI_Df6xbSOJJhdh2Rzp43JOCMnzgn",
            "https://drive.google.com/uc?export=view&id=1d0h1kJ-wd_5XI9sMeUWjHuMxftRTJ3Iy",
            "https://drive.google.com/uc?export=view&id=1ccGPVB1zKuK9PMz8mqtsLQfs1Um3kYwU",
            
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450123",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Bang Haikal baik, suka bercerita",  
                "pesan":"Semangat terus bang haikal, semoga kuliahnya lancar sampai lulus"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak inii baikk, humble skalii",  
                "pesan":"semangat terus kuliahnya kakak baik !!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kaka terhumble dan friendly, sangat hangat rasa",  
                "pesan":"Sehat sehat kaka baikk, semoga segala urusan kaka dilancarin ya kakk!"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang farhan baikk",  
                "pesan":"Semoga bang farhan sehat dan bahagia selaluu"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kakak ini baik dan lucuu.",  
                "pesan":"semangat terus kuliahnya kakaaa"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kakak ini lucu banget, baik dan friendly",  
                "pesan":"Bahagia selalu kakaaa, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang jaya baik dan informatif",  
                "pesan":"Semangat terus yaa bang jayaaaaa"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak najla baikk dan imup",  
                "pesan":"Yang semangat ya kakaaa semester ini, semoga sukses selaluu"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Abangnya baik dan sabar",  
                "pesan":"semangat terus kuliahnya abangg !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini ramah senyum bangett",  
                "pesan":"Makasih udah tutorin kita kakkk, semangat teruss"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Abang ini baikkkk",  
                "pesan":"semangat terus kuliahnya abangg !!!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20 tahun",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Bima",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "kak cika lucu nan baik",  
                "pesan":"Semoga lancar terus ya kakk kuliahnya"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak gustin seruu",  
                "pesan":"Semoga kaka sehat dan bahagia selalu ya kakkk"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Abangnya asik dan seruuuw",  
                "pesan":"Sukses terus abanggg, semoga semester ini lancar yaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini baik dan asikkk",  
                "pesan":"semangat terus kuliahnya kak rafa sabinaaaaa!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
    
elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls =[
            "https://drive.google.com/uc?export=1YBYf7bAz47Ynn9RRmMIB_rGLRjuoCjtv",
            "https://drive.google.com/uc?export=1CHaEGGZOt1klaGqfav7WAtOAMR43o1Kq",
            "https://drive.google.com/uc?export=1iyce4R69Tdzp_sVyAYH7BnNfCXkRTk5g",
            "https://drive.google.com/uc?export=1iE348pBH97woz5Gu0f2ar8Dn1ZZ4C55z",
            "https://drive.google.com/uc?export=1-4gERWLvMJec9VOL7tIlOLQc3JVlhh1X",
            "https://drive.google.com/uc?export=1bnHkwaq1i9vwcSFkeIJPbvE8P3lz2bMO",
            "https://drive.google.com/uc?export=1QwVXBL5jhBUrePmOZOvUYVkPPcPILfKX",
            "https://drive.google.com/uc?export=1K6aOm45KXJoh52jalnEEUZcdQArWtIM0",
            "https://drive.google.com/uc?export=13g7AK1wEFcvsAvVjrOeKnNdMwINrHUMP",
            "https://drive.google.com/uc?export=1pwiCeRfFbx--Q0SBJBQ64s6k_w6N16E4",
            "https://drive.google.com/uc?export=16fqLHRc2RzrP_appDgXbeqgvk3SypGBR",
            "https://drive.google.com/uc?export=1Dmkm_AFdHqAYLsnkwaUqWOYmVr8QWE6t",
            "https://drive.google.com/uc?export=1HlFbX3fhfMqImOLYwwt8afT_0cUV2LVt",
            "https://drive.google.com/uc?export=1OjgI1scB9A_Qwepfi2m2mlGkgZsUFUmY",
            "https://drive.google.com/uc?export=1xE_XLWO6RcfUHQkkv_MbRhLBHA8rfXzf",
            "https://drive.google.com/uc?export=1fQjNmRaiXcnxX0pqm5pOkmufC2hoxm3g",
            "https://drive.google.com/uc?export=1FaPEKpJPo5YjkpLik-t2YN1hfOvIt9kv",
         ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak arienta ternyata baikkk, walaupun awalnya keliatan serem.",  
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya."#1
            }
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk, walaupun keliatan judes",  
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya."# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan":"Bang nobel itu orang nya tegas, tapi asik juga ternyata.",  
                "pesan":"Semangat terus ya bang, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orang nya semangat banget apalagi kalo damaskusan",  
                "pesan":"Semangat kuliahnya bang azmii, semoga lancar dan sukses teruss yaaa bang"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake keliatannya paling soft spoken diantara abang dan kaka timder lainnya",  
                "pesan":"Semangat terus yaa bang ayake, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Terlihat sangar, tp ternyata asik juga",  
                "pesan":"Semangat terus yaa bang caesar, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka euodia itu asikkk dan baik juga, tapi keliatan galak pas kader (jujur)",  
                "pesan":"Semangat ya kak, lancar terusss kuliahnya"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal baikk",  
                "pesan":"Semangat terus yaa bang haikal, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kakanya sangat ramah, baik, dan humble",  
                "pesan":"Semangat terus kaka kuliahnya"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kaka ini ramah, humble, dan asik",  
                "pesan":"Semangat terus ya kak, semoga sehat dan sukses selalu!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang nya baik",  
                "pesan":"sukses selalu bang desmannn, semoga lancar sampai lulus ya bangg"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya cantik dan baikk ",  
                "pesan":"Semangat terus ya kak, lancar terus kuliahnya"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "kakanya baik dan asik ",  
                "pesan":"semoga semester ini dilancarinn segala urusannya ya ka"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jeremi ini baik dan humble",  
                "pesan":"Semangat terus abangg kuliahnya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila humble dan talkative",  
                "pesan":"sehat sehat kakaa, bahagia terus yaaa"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini stylishhh",  
                "pesan":"Semangat teruss bang rafli, semoga sehat selalu bahagia selaluu"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak nya baik dan lucu",  
                "pesan":"lancar lancar terus ya ka kuliahnya"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
