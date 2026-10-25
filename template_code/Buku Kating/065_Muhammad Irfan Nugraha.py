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
            "https://drive.google.com/uc?export=view&id=1fwLPLl9PiJgDcPgqjfyx_6gcavfnekYV",
            "https://drive.google.com/uc?export=view&id=1mU6-9OLIUSU3lIS7AWkD5lxZZtdtuA3N",
            "https://drive.google.com/uc?export=view&id=1Mjhm_0o6IA391OrLiEUV53D84HUNH0vz",
            "https://drive.google.com/uc?export=view&id=1flmlfqGRuZXo8Pe6kI-TT4Wxd5XznLqw",
            "https://drive.google.com/uc?export=view&id=1ZURwHGl_zZ4XXrPuH2xrWZ5MSbDzGv5c",
            "https://drive.google.com/uc?export=view&id=1N9VhZ383Am2zFn6ZSOvGj8d7T47514xx",
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
                "kesan": "Abangnya seru dan banyak insight yang bisa diambil dari abangnya",  
                "pesan": "Semoga tetap semangat dan sukses dalam menjalani kuliahnya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "21",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Tahajud",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya lucu tapi tetap serius dalam menjalankan tugasnya",  
                "pesan":"Semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik dan sering ngasih tips",  
                "pesan":"Tetap jadi orang baik"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya kalem tapi sering ngelucu",  
                "pesan":"Semoga tetap jadi orang yang kalem"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Basket",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya baik, asik dan seru",  
                "pesan":"Semoga urusan kakaknya lancar dan kuliahnya aman"# 1
            },
            {
                "nama": "Lutfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nemuin Pak Tirta",
                "sosmed": "@Luthfiaarmdhni",
                "kesan": "Kakaknya seru dan lucu, tapi kadang suka kaget",  
                "pesan":"Semoga kakaknya tetap jadi seru dan lucu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mPKsjgdBOBC6SPq0ol2iXFLGOJOT4hps",
            "https://drive.google.com/uc?export=view&id=1wtmxbv7-HJgvOICrx_8gW5qccoj8DJD9",
            "https://drive.google.com/uc?export=view&id=1aXvQV3_PrKRkmoK9uawSS908roc-ISz2",
            "https://drive.google.com/uc?export=view&id=1cyM4IQ0LWaiExqAy_GJOEtZ0GWqf89BX",
            "https://drive.google.com/uc?export=view&id=1-i8AB1ntksWAMPUOXZc2DE8fdfov13G5",
            "https://drive.google.com/uc?export=view&id=1LfFnTe84LiB36Dx1akOgCGqFAQaRNY3V",
            "https://drive.google.com/uc?export=view&id=1IugDIyKQkkiAu1vLRbyxpBPiTwHmjYSN",
            "https://drive.google.com/uc?export=view&id=1cCxGYKIQ8uVJ3ZYO5M3dz_dxpwYzynI6",
            "https://drive.google.com/uc?export=view&id=1PlguIsd6D7fv6_XgBH_Mg_muWbeD1Bga",
            "https://drive.google.com/uc?export=view&id=1oI2dpo8sdGHtDrC1oD7niz3tzH6vQtZc",
            "https://drive.google.com/uc?export=view&id=1Je5PNkWfkATsPcD6__zZxYNry0J08aZ9",
            "https://drive.google.com/uc?export=view&id=1r5jKoBa30AZ3yiBnPxb5Zu-uCeU4z_5Z",
            "https://drive.google.com/uc?export=view&id=1WvMdoQVdUWEw-SGo55DIK71o1GNv_mFC"            
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
                "kesan": "Abang ini lucu banget dan usil kadang-kadang",  
                "pesan":"Semoga selalu jadi orang yang lucu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Repeat lagu if only by skyline setiap hari di jam 8",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya cantik dan lucu, enerjik pokoknya",  
                "pesan":"Semangat selalu kuliahnya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "124450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya udah pinter, aktif lagi",  
                "pesan":"Tetap pertahankan prestasinya bang"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abangnya asik, sering ngelawak juga",
                "pesan":"Semangat terus belajar dan kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "124",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "kakaknya kalem dan lembut orangnya",  
                "pesan":"Semoga tetap semangat kuliahnya kak"# 1
            },
            {
                "nama": "Gh Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal":"Kupang",
                "alamat": "Jatiagung",
                "hobbi": "Main PS",
                "sosmed": "@me._kael",
                "kesan": "Abangnya santai dan ramah sama semua orang",  
                "pesan":"Semoga bisa maen ps bareng abangnya"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Jatiasih",
                "alamat": "Kedaton",
                "hobbi": "Nonton Boboiboy",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya kalem orangnya dan hobinya lucu",  
                "pesan":"Semoga kakaknya selalu semangat dalam kuliahnya"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Indarum",
                "alamat": "Awen kost",
                "hobbi": "Photobooth",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya baik dan sering ngasih tips buat nambah wawasan",  
                "pesan":"Tetap jadi orang baik kak!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal":"Kotabumi",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",                
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya cantik, kalem dan lucu (sering ketawa)",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Sidoarjo",
                "alamat": "Teluk",
                "hobbi": "Konten Mainfullness",                
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya keren, gayanya tegas tapi santai dan asik orangnya",  
                "pesan":"Tetap jadi orang keren bang!!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan koleksi figure",                
                "sosmed": "@nagatseee",
                "kesan": "Abangnya lucu banget dan jokesnya kadang random",  
                "pesan":"Semoga tetap jadi orang yang lucu dan asik"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Membaca buku",                
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya baik, kalem dan kadang ngasih wawasan",  
                "pesan":"Selalu semangat kuliahnya kak!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "124450077",
                "umur": "20",
                "asal":"Pasoy",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",                
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucu, dan diem-diem tapi kadang ngelawak ",  
                "pesan":"Semangat kuliahnya kak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1saGMBw3H37z6EyD-LKd45CFRud8fh3e8",
            "https://drive.google.com/uc?export=view&id=1aURuQZKxTJ3an-asxZHUpLPZBSL8Apaj",
            "https://drive.google.com/uc?export=view&id=1xW78k0TnQ5qG7eilfZOUrnYK0Knd8JrB",
            "https://drive.google.com/uc?export=view&id=1-ztNpztGFjmghg2bO-81J21N8T2B5SJn",
            "https://drive.google.com/uc?export=view&id=1_WKCpgS1MeEQ_cimVika9XJngj76Q3xB",
            "https://drive.google.com/uc?export=view&id=1X4dBwn5IPOrnz6blAev9CpzZclhYbso4",
            "https://drive.google.com/uc?export=view&id=1_fyOoDohsaD8rYxyhhTakmL6HSDzvJe5",
            "https://drive.google.com/uc?export=view&id=1BHiba6gd6cwk7JueaJg6NxDNTxJGzO9Z",
            "https://drive.google.com/uc?export=view&id=1e835zXyzrYJWBqVDfVcjbUkO7-yAb1A9",
            "https://drive.google.com/uc?export=view&id=1PSHp_-CZxxk6tgfzWjuEvYdNWPX8JEmp",
            "https://drive.google.com/uc?export=view&id=1oABfWOBnNoSJqAmDGm_iA8pHskwK9zvJ",
            "https://drive.google.com/uc?export=view&id=1sr7AxvQsrxZcshipI1MBr5i2_9zEv-6z",
            "https://drive.google.com/uc?export=view&id=1jhb6M9bLebEPy-JswthYWWgHW5-SvfU9",
            "https://drive.google.com/uc?export=view&id=1VK43NMLrsbqSASbCX90WemmQxvydZVAp",
            "https://drive.google.com/uc?export=view&id=1n4hmfDl8y-m3jsRVmQRbkd16aiDfloze",
            "https://drive.google.com/uc?export=view&id=1-MnFFCQAIOqu_6mFhIP8RqXQ8Zx_gh6A",
            "https://drive.google.com/uc?export=view&id=1q0md6NQoA_T-tS9XcmooLXjUXVoTyuzl",
            "https://drive.google.com/uc?export=view&id=1ie8VYvJ13BwxTwPiYRPU_EsPiL4MguHf",
            "https://drive.google.com/uc?export=view&id=1SLU5s5X_lgyFQvr8ZQC2OcouYdcpWt4N",
            "https://drive.google.com/uc?export=view&id=1J7tNvd6lUEEQ3sSjXtDOHNAZD8wAONLP",
            "https://drive.google.com/uc?export=view&id=1vcq4SESe-TokAplvob9SpypdlN4Gov3a",
            "https://drive.google.com/uc?export=view&id=1_N--GgHYK6POLwyMyJyrBJtDrZ5UYyfE"
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
                "kesan": "Kakaknya berwibawa tapi tetap seru",  
                "pesan": "Semoga kakaknya sehat selalu dan sukses"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakaknya cantik, kalem dan lucu",  
                "pesan":"Tetap semangat kuliahnya kak"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "Abangnya suka ngerjain dan ngelawak",  
                "pesan":"Semoga tetap jadi orang yang asik bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya pinter dan keren",  
                "pesan":"Selalu semangat kak aktivitasnya"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya banyak ngasih pengalaman dan wawasan",  
                "pesan":"Terus semangat kegiatannya kak"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakak ini kocak dan hobinya banyak (mancing)",  
                "pesan":"Semoga selalu jadi orang yang menghibur kak"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Abangnya keren dan cool",  
                "pesan":"Semoga hari-hari abangnya seru dan lancar"# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Abangnya kalem tapi tetap asik diajak ngobrol apapun",  
                "pesan":"Tetap semangat bang kuliah dan kegiatannya!"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya asik dan kadang ngerjain tapi baik orangnya",  
                "pesan":"Semoga kakaknya semangat selalu!"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak ini aktif banget dan ada dimana aja",  
                "pesan":"Semoga sehat selalu dan tetap jadi pribadi yang seru"# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Selalu semangat menjalani kuliahnya kak!"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya murah senyum banget",  
                "pesan":"Semoga tetap jadi orang yang murah senyum"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya kadang canggung tapi lucu jadinya",  
                "pesan":"Tetap semangat kegiatan dan harinya"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Abangnya keren dan ganteng",  
                "pesan":"Semangat terus bang kuliahnya"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Abangnya cool dan kalem tapi baik banget orangnya",  
                "pesan":"Tetap menjadi orang yang baik bang!"# 1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Abangnya meskipun tegas tapi baik dan sering ngasih tips",  
                "pesan":"Semoga lancar hari-harinya bang"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Abangnya kalem tapi lucu orangnya",  
                "pesan":"Semoga selalu semangat kuliahnya bang"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "Abangnya lucu, kadang random dan aktif (gerak)",  
                "pesan":"Tetap jadi orang yang seru dan asik bang!"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya lucu dan murah senyum",  
                "pesan":"Semangat untuk kegiatannya kak"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya cantik, baik dan lucu",  
                "pesan":"Semangat untuk hari-harinya kak"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abangnya keren dan hebat apalagi pengalamannya",  
                "pesan":"Semoga abangnya terus berkembang"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O1SSqIBGBC49X9b6axtVFTPQMcKF0qSz",
            "https://drive.google.com/uc?export=view&id=1G5EsG8BHFKxUhJqPsSFN3lNYvngr8Yfw",
            "https://drive.google.com/uc?export=view&id=1SBsKSK27r5L6NE9xq_5HanAOLVY3ETY2",
            "https://drive.google.com/uc?export=view&id=1TSFfJi2lyT6dbS8y2DF2HQ7EaUe48wed",
            "https://drive.google.com/uc?export=view&id=1D1LH6yJgyZieBMRqKMvr_nAvgJNYn574",
            "https://drive.google.com/uc?export=view&id=1rro8Tz2DarzU2ZUEM0v_IdmH_5uppyjr",
            "https://drive.google.com/uc?export=view&id=1B-978G1MZvhJ4Z8Jos_zFRvlMTsKko5e",
            "https://drive.google.com/uc?export=view&id=1lyGImhMihOaY_z7-LR6tYpC2MtpAMrk0",
            "https://drive.google.com/uc?export=view&id=1k74AKYyvCXANk3UA6oVdbTXudg4CRf4Z",
            "https://drive.google.com/uc?export=view&id=1AY0PtSy1V-7RNFqzg9U5N67snQx8X7H4",
            "https://drive.google.com/uc?export=view&id=1qG1VM4FpnGW4LUzfQpgCV1oTQShQSb2m",
            "https://drive.google.com/uc?export=view&id=1DjmbSm6oBEPm4K11Uhy9jeOAT3uszLsX"
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
                "kesan": "Abangnya lucu dan selalu ngelawak tapi bisa serius kalau diperlukan",  
                "pesan":"Semoga tambah akur dengan kak Hanifah"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya lucu dan suka becandain orang, tapi baik aslinya",  
                "pesan":"Semoga tambah akur dengan bang Ihsan"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya kalem tapi baik sama orang lain",  
                "pesan":"Tetap jadi orang yang baik"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya murah senyum sama orang lain",  
                "pesan":"Semoga hari-harinya lancar kak"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "Style abangnya keren",  
                "pesan":"Semangat selalu kuliahnya bang"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Abangnya kalem dan lucu",  
                "pesan":"Tetap semangat kegiatannya bang"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya suka ngelucu dan kocak",  
                "pesan":"Semoga tetap jadi orang yang asik"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakaknya kalem dan baik",  
                "pesan":"Semoga tetap semangat hari-harinya"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakaknya kalau bahas sesuatu heboh dan seru",  
                "pesan":"Semoga tetap jadi orang yang seru dan asik kak!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya murah senyum dan suka tertawa",  
                "pesan":"Selalu semangat menjalani aktivitas kak"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Abangnya baik dan suka kalau diajak ngobrol",  
                "pesan":"Semoga hari-hari abangnya lancar"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakaknya kalem dan baik sama orang lain",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zMrHuLAl_ob41NEsjIXpbUCC-VDf66Zj",
            "https://drive.google.com/uc?export=view&id=1WIN2apvbQsShTU1z07xArE2_N58wHem2",
            "https://drive.google.com/uc?export=view&id=1yuE96tiZibIOPwjnKBEHZconQhM8udch",
            "https://drive.google.com/uc?export=view&id=1FYHSmY9qJodPXY_MTeRPzY-doWIHqJz9",
            "https://drive.google.com/uc?export=view&id=1W2JNAhXVfoDOBIXocmmkEDZ1J5mfBThS",
            "https://drive.google.com/uc?export=view&id=1TR38RT9H-1v2vr6BbayuzVqrw35BXDTE",
            "https://drive.google.com/uc?export=view&id=1cY6lljFel-DnUx_wUm4ydZaDhIj18rMm",
            "https://drive.google.com/uc?export=view&id=1hUoRycJt3BgAbjd1dMVmA1oUtSrzpeE8",
            "https://drive.google.com/uc?export=view&id=1Alq5MpjyiYHI_utzccwhXzdxn6zb-r1L",
            "https://drive.google.com/uc?export=view&id=1QC5obWq9C7ZvjZTgO6THTZnkOZIgxIJs",
            "https://drive.google.com/uc?export=view&id=1gfLpBSCkULizuzGSyjY6c4W3CQXtgU-V",
            "https://drive.google.com/uc?export=view&id=1rpxDWVnCzmdrD50iubjRUBW4lAoaQkUm",
            "https://drive.google.com/uc?export=view&id=1e0pVQhVr0cJJwTkGCRFdgGzOR2wLc_Fp",
            "https://drive.google.com/uc?export=view&id=1SEG-KvKUrEAgMLaO5eNzbKPWm8VX38hv",
            "https://drive.google.com/uc?export=view&id=1ReK4q7_I3t4roCxUBarM1TWrkXHKfoyq",
            "https://drive.google.com/uc?export=view&id=1z27avelIPlZh62G67MLZLhLlt1NOMyF7",
            "https://drive.google.com/uc?export=view&id=1jQOZMrEKEHMBTlBBHSkHbjO5miyTFUOP",
            "https://drive.google.com/uc?export=view&id=1RqfIfrhSQ582fDDLzjq0QmBEaKR-S---"
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
                "kesan": "Kakaknya baik dan menambah wawasan",  
                "pesan": "Semangat menjalani hari-hari berkuliahnya"# 1
            },
            {
                "nama": " Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": " Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya kalem dan murah senyum",  
                "pesan": "Semoga kakaknya tetap semangat beraktivitas"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": " Way Huwi",
                "hobbi": " Tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya keren dan ramah serta suka nyapa",  
                "pesan": "Semoga tetap semangat dalam kegiatannya"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"karawang",
                "alamat": "Airan",
                "hobbi": "nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya murah senyum dan kalem orangnya",  
                "pesan": "Semoga hari-harinya lancar kak"# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "Kakaknya cantik dan murah senyum",  
                "pesan": "Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya kalem dan ramah",  
                "pesan": "Semoga selalu lancar aktivitasnya"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": " 124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak ",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa_",
                "kesan": "Kakaknya baik dan murah senyum",  
                "pesan": "Tetap jadi orang yang baik kak"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": " 124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@ felisyanbl__",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semoga selalu semangat kuliahnya"# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": " Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya keren dan jago dokumentasi",  
                "pesan":"Semoga kemampuannya berkembang dan semakin jago"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya baik dan kalem",  
                "pesan":"Lancar selalu hari-harinya kak"# 1
            },
            {
                "nama": " Lucia Advencia Rachel Nainggolan",
                "nim": " 124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": " Mencintai Andrew Garfield",
                "sosmed": "@ luciarachel_",
                "kesan": "Kakaknya cantik, lucu dan baik",  
                "pesan": "Semangat menjalani perkuliahannya"# 1
            },
            {
                "nama": " Edsel Adya Pradipta",
                "nim": " 124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "@edsel_0712",
                "kesan": "Abangnya kalem tapi tetep seru",  
                "pesan": "Semoga tetap jadi orang yang seru"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "Abangnya kocak, diem-diem tapi tiba-tiba ngejokes",  
                "pesan":"Tetap jadi orang yang seru dan lucu"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@ alya.rmdhnti",
                "kesan": "Kakaknya baik dan murah senyum",  
                "pesan": "Selalu lancar kegiatan sehari-harinya"# 1
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya seru dan sering ngajak ngobrol",  
                "pesan":"Semoga semangat terus kuliahnya"# 1
            },
            {
                "nama": "Nazlah Aulia",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memanah",
                "sosmed": "@nzlhauly",
                "kesan": "Kakaknya lucu dan kalem",  
                "pesan":"Selalu semangat menjalani hari-harinya kak!"# 1
            },
            {
                "nama": "shafa delaila azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya baik dan asik",  
                "pesan": "Semoga lancar aktivitasnya"# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Gebuk Snare",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakaknya enerjik dan aktif",  
                "pesan":"Semoga selalu jadi orang yang aktif dan enerjik"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JIX8_QjMgUxhtA-CiP9-PIaZU-gQnlzB",
            "https://drive.google.com/uc?export=view&id=1caqDXjOTj23XTR1mPZP3IObXpzZ4iJmk",
            "https://drive.google.com/uc?export=view&id=1jgBeUn5pVZyXm_lQAHgtfv0HgrS9PbRi",
            "https://drive.google.com/uc?export=view&id=1EYZa7Ttj9OZWphdPde1R-1GjBYqfd-9T",
            "https://drive.google.com/uc?export=view&id=1eqd1xxdpslQLd7OByeeTvsmZqO-ZTQDe",
            "https://drive.google.com/uc?export=view&id=1W1oL1UvD5VysyY3sL8oVdzLKhbyZGbRG",
            "https://drive.google.com/uc?export=view&id=1Kuq5qfmIyGyPfc4NNGdvQDmqvPQ-26vr",
            "https://drive.google.com/uc?export=view&id=1DvIah3ZsvupZletIi1rB96JYxPJv1xJh",
            "https://drive.google.com/uc?export=view&id=1JDI8vTPNeykjBUbAXH0SS3ooyu883t1M",
            "https://drive.google.com/uc?export=view&id=17wlgZkOUf7MZ3_FpHSs3qs3mB6fg5CDZ"
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
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semoga kakaknya lancar kegiatannya"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21 tahun",
                "asal":"Bandar lampung",
                "alamat": "Sukarame",
                "hobbi": "Dengar lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya aktif dan selalu ceria",  
                "pesan":"Semoga hari-hari kakaknya cerah"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21 tahun",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "beres beres",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya pinter dan sering ngajak ngobrol",  
                "pesan":"Semoga bahagia menjalani hari-harinya kak!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20 Tahun",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "ngesen kiri",
                "sosmed": "@helmy.inst",
                "kesan": "Abangnya kocak dan super aktif (gerak)",  
                "pesan":"Semoga abangnya tetap jadi orang yang seru"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21 Tahun",
                "asal":"Tangerang kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Main Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya kadang mendadak ngejokes tapi baik orangnya",  
                "pesan":"Lancar selalu hari-harinya bang!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19 Tahun",
                "asal":"Pesisir Barat",
                "alamat": "Kobar",
                "hobbi": "Dokum hal tidak penting",
                "sosmed": "@sciia__",
                "kesan": "Kakaknya sering ngajak ngobrol dan baik",  
                "pesan":"Tetap semangat menjalani kegiatannya"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya jago banget public speaking",  
                "pesan":"Semoga kemampuan abangnya terus berkembang"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19 tahun",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya cantik, lucu dan suka ketawa",  
                "pesan":"Semoga kakaknya tetap jadi orang yang lucu"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "19 Tahun",
                "asal":"Lamtim timur",
                "alamat": "Gunter terang",
                "hobbi": "Cinematic Datavora",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren dan kocak juga",  
                "pesan":"Semangat terus bang hari-harinya"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya baik dan lemah lembut",  
                "pesan":"Semoga kakaknya lancar aktivitasnya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CwZOETgjjWkFb45RjoN8ILMa-xDlTPXw",
            "https://drive.google.com/uc?export=view&id=1dH0Y8AL-CtQ3Z8rQ1ZN1aHm2nO4FBpgG",
            "https://drive.google.com/uc?export=view&id=12RP8TWEorYlcqAt2pfdKONokRgfc-dtN",
            "https://drive.google.com/uc?export=view&id=1eZ7tfZf8Yyb-WLWthSDs8AU6ZkNoj8BL",
            "https://drive.google.com/uc?export=view&id=1ttbtOtEhSE9LEtBB-1OUTfHaP_IdL2wg",
            "https://drive.google.com/uc?export=view&id=1pw0mA8G3D66XC_yPNVl2BJhDpenia0Gs",
            "https://drive.google.com/uc?export=view&id=1iwFjKoCeNtY-5-OyrN7MOZvu8hI2_CqB",
            "https://drive.google.com/uc?export=view&id=1wxP-cJDX3_LnaQZuLZ_4drcF1ue_w_XE",
            "https://drive.google.com/uc?export=view&id=1byJsht4GKIRN4QrotVk1iRJ0Bblpb7QA",
            "https://drive.google.com/uc?export=view&id=1Ujx8lzMDGj36gOCpN7W1wNQ3sL0B_qwg",
            "https://drive.google.com/uc?export=view&id=1LwRzALIijrz_zD6XfzEetebia1vzHVQ3",
            "https://drive.google.com/uc?export=view&id=1EUw66G2Rpc8DphEP-oXCTVfKYv8OPdWg",
            "https://drive.google.com/uc?export=view&id=1zB3gAgP6BBBTopEYbpb9BylZaBhGjysc",
            "https://drive.google.com/uc?export=view&id=1_fcnIkCTPvt4gc3vbDF63qozQZk7MLD5",
            "https://drive.google.com/uc?export=view&id=1Y7xieM49YXv8WgpyBt5JOHendHc1YjoA"
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
                "kesan": "Abangnya keren dan cool",  
                "pesan": "Semangat kuliahnya bang!"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": " Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya lucu dan suka ketawa",  
                "pesan": "Semoga semangat menjalani kegiatannya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Main badminton sama Yosep",
                "sosmed": "@mridwaan_22",
                "kesan": "Abangnya suka ngajak ngobrol dan bercanda",  
                "pesan": "Tetap semangat beraktivitas bang"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton f1",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya baik dan banyak insight",  
                "pesan": "Lancar terus hari-harinya bang"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "123450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nguras kolam lele",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya cantik dan lucu",  
                "pesan": "Semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Ternak ayam",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya kocak dan seru",  
                "pesan": "Semoga tetap jadi orang yang seru"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": " 124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya keren dan jago futsal",  
                "pesan": "Semoga abangnya semakin jago"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": " 124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live Tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya keren bisa main banyak alat musik",  
                "pesan":"Semoga kemampuannya terus berkembang"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": " Live tiktok bareng Bryan",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakaknya lucu dan murah senyum",  
                "pesan":"Semoga hari-harinya lancar selalu kak"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jl. Pulau Damar",
                "hobbi": "Diving",
                "sosmed": "@afdall.03",
                "kesan": "Abangnya kalem tapi baik orangnya",  
                "pesan":"Semoga lancar terus aktivitasnya"# 1
            },
            {
                "nama": "Dafa Elpriza",
                "nim": " 124450131",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Persis",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya keren dan jago main futsal",  
                "pesan": "Semoga kemampuan abangnya selalu meningkat"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": " 124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya kalem dan ramah sama orang lain",  
                "pesan": "Semoga kakaknya semangat menjalani kegiatannya"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lari",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknya baik dan kalem orangnya",  
                "pesan":"Selalu jadi orang yang baik kak"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@andra.lhm",
                "kesan": "Abangnya asik dan seru diajak ngobrol apa aja",  
                "pesan": "Tetap jadi orang yang asik dan seru"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakaknya baik banget dan murah senyum",  
                "pesan":"Semoga tetap semangat kuliahnya kak!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()
# Tambahkan menu lainnya sesuai kebutuhan
