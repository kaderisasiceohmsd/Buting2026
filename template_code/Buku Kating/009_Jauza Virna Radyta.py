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
            "https://drive.google.com/uc?export=view&id=1xVOIyVcEWA9aIu_rhjmMrtG54l6VKKph",
            "https://drive.google.com/uc?export=view&id=1TyG2J2lHVCUhmFKcuSOC8i6mSs4QANUr",
            "https://drive.google.com/uc?export=view&id=1eQ3MZJScvHPLMUXEfYwGKXxviL9aplOr",
            "https://drive.google.com/uc?export=view&id=1kbc6pWhzoTIVEmQy9Hln_BuNe8hpVo2s",
            "https://drive.google.com/uc?export=view&id=1_nm-21LBwwNcaFOavgXokGcj1ryhstWK",
            "https://drive.google.com/uc?export=view&id=1EV5SMSozsmYDhoa-PCojVgu3nH4jyhUM",
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
                "kesan": "Bang Fajar keren, tegas, dan juga baik sekalii",  
                "pesan":"Semoga semua keinginan bang fajar cepat terwujud"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil asikk benerr, dan juga keren apalagi pas basket",  
                "pesan":"Semoga bang aqil bisa dapetin yang bang aqil inginkan"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi keren sekali, sangat baikk dan ramah sekalii",  
                "pesan":"Semoga cepat mendapatkan apa yang kak efi inginkan"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois kerenn, sangat humble, dan juga baikk",  
                "pesan":"Semoga bang qois selalu dapet hal-hal baik"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa kerenn, baik jugaa, dan sangat ramahh",  
                "pesan":"Semoga kak hafsa selalu mendapatkan apa yang kak hafsa mau"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfi sangat lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga kak luthfi selalu mendapatkan semua yang hal yang diinginkan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BX8BNHfcyTHiKq_zK-RRLuhx4RJEi5H5",
            "https://drive.google.com/uc?export=view&id=1hnEDNm0H0jP-Kdqs5Md39FQyP90k9NG4",
            "https://drive.google.com/uc?export=view&id=1v5v4oEq29VnWv5GARTEHhWvyHDLIFlCd",
            "https://drive.google.com/uc?export=view&id=1O6ts_ok5mJdBHpTjc-t0I1DE99znRTuG",
            "https://drive.google.com/uc?export=view&id=1VAIQ1RkK5PPl3SWpb2UMwaqYnGUiPk5n",
            "https://drive.google.com/uc?export=view&id=1tX4ynAeCTr0TNwP8t1yXVMw7X8lAz6UV",
            "https://drive.google.com/uc?export=view&id=1-T9rxSCfRayBJbUVW14UPW7nIlR8x8S2",
            "https://drive.google.com/uc?export=view&id=1KwYUzTWb9KFzlN3jmJE-RY6d1nLglZrx",
            "https://drive.google.com/uc?export=view&id=1cAaiTd02s7SulDyp9e-O_sHxOlHIdflx",
            "https://drive.google.com/uc?export=view&id=10bNbwhUIH_CNPOxbRjPyaCr1reKRJevf",
            "https://drive.google.com/uc?export=view&id=1S5pukEDCihA6CQS0cAvu8VeaRxEpkDrR",
            "https://drive.google.com/uc?export=view&id=1TcNu2NTawMrtSagNW4CTpadDOooHSV7U",
            "https://drive.google.com/uc?export=view&id=1aU0xjMdjGW92Qwlrn_NhrrZJxMC0W2xT",

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
                "kesan": "Bang Ridho cool sangat lh, dan juga baikk",  
                "pesan":"Semoga bang ridho selalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Juesi lucuu, humble, dan baik",  
                "pesan":"Semoga kak juesi cepat mendapatkan hal yang diinginkan"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang Dharu asikk, baik, dan juga sangat ramah",  
                "pesan":"Semoga bang dharu selalu didekatkan hal-hal baik"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael sangat kerenn, dan juga baikk apalagi pas pplk",  
                "pesan":"Semoga semua keingininan bang mikael segera terkabulkan"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak Siti lucuu, baik, dan juga sangat ramah",  
                "pesan":"Semoga kak siti selalu mendapatkan hal-hal yang diingingkan"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Giovaro keren sihh, dan juga baikk",  
                "pesan":"Semoga apa yang bang gio semogakan cepat terkabulkan"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak afghanis sangat manis, baik jugaa, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak afghanis cepat terkabulkan"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak Hani lucuu, ramah juga, dan tidak lupa dengan baiknyaa",  
                "pesan":"Semoga kak habi selalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremi keren sih, suaranya baguss, dan juga baikk",  
                "pesan":"Semoga semua keinginan bang jere cepat terkabul"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica sangat baik, lucuu, dan juga ramahh",  
                "pesan":"Semoga kak monica cepat mendapatkan apa yang kak monica inginkan"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona sangat amat kocak, dan baikk",  
                "pesan":"Semoga bang jona selalu mendapatkan semua yang hal yang diinginkan"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar sangat baikk, dan juga maniss",  
                "pesan":"Semoga kak sekar didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa sangat asik, baikk, dan ramah jugaa",  
                "pesan":"Semoga semua keinginan kak nashwa cepat terkabul"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mq7zSb_-Rcd6WrGIpjXA5XtEXCrKyMef",
            "https://drive.google.com/uc?export=view&id=16-18WEmdA5b5e7RnUVH8U-pgnqmPKGDV",
            "https://drive.google.com/uc?export=view&id=1gfAldKEpplPXtYC7KT1i5dteSgabhlwv",
            "https://drive.google.com/uc?export=view&id=1mq-BN2vWE4i2siPXkbgnejBckxU4LoMh",
            "https://drive.google.com/uc?export=view&id=1Kh5Gxz1qM68tpxXOwBMK18k8Jm0TYIxt",
            "https://drive.google.com/uc?export=view&id=19tRYQyOWC0EibBNbmsvUfHu5uWKAWELQ",
            "https://drive.google.com/uc?export=view&id=1DpPmQ89CFSOhqpDTu1k-akEubVW7ACn4",
            "https://drive.google.com/uc?export=view&id=1KeSOw5FJeXfdz3lJemQ0Eh3zeZLAPsyR",
            "https://drive.google.com/uc?export=view&id=1YnE0mw6F-vVFzD-AT97axqX0v3KmAsb8",
            "https://drive.google.com/uc?export=view&id=1NYDTtQwnjd5ntrqY_kzxahMLTalU0lzp",
            "https://drive.google.com/uc?export=view&id=1QaslTCYxCADzGoYe-l98cJ7l820Qu0gC",
            "https://drive.google.com/uc?export=view&id=1zeWR78XroFiBG66j9b-5p_ALyyM31-_-",
            "https://drive.google.com/uc?export=view&id=1i7unJhu3zrtE_lu23ZHnJAmkoe7oYf01",
            "https://drive.google.com/uc?export=view&id=1dg3fGlKxHLtvd8xjRGfjxjBTVH7rEsez",
            "https://drive.google.com/uc?export=view&id=1ovSnuwctxlxs5O0CVskCiaw9s4V9Rlpc",


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
                "kesan": "Bang Kevin sangat amat cool, dan juga baik",  
                "pesan":"Semoga bang kevin mendapatkan apa yang bang kevin inginkan"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Gusti sangat asikkk, dan juga baik sekali",  
                "pesan":"Semoga kak Gusti sealalu didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali sangat keren, dan juga baik",  
                "pesan":"Semoga semua keinginan bang ali cepat terwujud"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak Ayu sangatt baikk, dan juga sangat amat ramahhhh",  
                "pesan":"Semoga semua yang kak ayu mau cepat kak ayu dapat"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa keren, baik apalagi saat mengasprak",  
                "pesan":"Semoga bang dafa selalu mendapatkan apa yang bang dafa mau"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak Salsabila lucuu, baikk, dan ramahh",  
                "pesan":"Semoga kak salsa didekatkan dengan hal-hal baikk"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang Afdal kocak sangat lah, baik jugaa",  
                "pesan":"Semoga kedepannya bang afdal selalu mendapatkan apa yang diinginkan"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak Juwita sangat baikk dan juga ramah",  
                "pesan":"Semoga semua keinginan kak juwita cepat terwujud"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang Ridwan asik sih orangnya, baik, dan ramah jugaa",  
                "pesan":"Semoga bang ridwan didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang Andra baikkk sekalii, dan juga kerennn",  
                "pesan":"Semoga bang andra mendapatkan semua keinginan bang andra"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan sangat kocak, dan juga baikkk",  
                "pesan":"Semoga bang bryan selalu didekatkan dengan hal-hal yang baik"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Indah sangat baikk, dan juga ramah sangatt",  
                "pesan":"Semoga kak indah mendapatkan semua yang diinginkan"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kak Jacinda lucuu, dan juga baikkk",  
                "pesan":"Semoga kak jacinda selalu mendapatkan apa yang kakak inginkan"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang Rafka keren, baikk, dan juga ramahh",  
                "pesan":"Semoga semua keinginan bang rafka cepat terwujud"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tRs700cUp_ltIVDvFe8JK2h1DPQU9s-L",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1KBmKm1uS8nZKyGHn1PkTWcpteHyYr8FV",
            "https://drive.google.com/uc?export=view&id=1qxxSzBalqydJCGw0VZVHuOLhNrNUKpXP",
            "https://drive.google.com/uc?export=view&id=1Vve_ylKSy5ilrRP3gvUEa0pn1sgqNvDq",
            "https://drive.google.com/uc?export=view&id=1L-PF2EgVIYCrgLAeEfVWWYJiHOsVZ2k4",
            "https://drive.google.com/uc?export=view&id=1GcHgRYXdW5zVM5G29xbVDtYl2fQwteCu",
            "https://drive.google.com/uc?export=view&id=1I0DTA9qqcYAnD6YxbDk7zRLxOrbm18FJ",
            "https://drive.google.com/uc?export=view&id=1119djuVLsanaWw_IDWJBoEP0pTT6TUeO",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Lpn4uABtN9Cxqy-1jieIX48CwC-clU0d",
            "https://drive.google.com/uc?export=view&id=1ouP6BhvGNwUVxPyKyuFFBGLq9VkpQsqX",
            "https://drive.google.com/uc?export=view&id=1WaPxkjJLi5CXvxIDFc9ivz1LRj8tMEWP",
            "https://drive.google.com/uc?export=view&id=16SOCLG7UNAG55v3Z2nMD_KPAnDUCYLb1",
            "https://drive.google.com/uc?export=view&id=1b0iLMiiR7vYuojjbJvLGxoHIeRkJOBPm",
            "https://drive.google.com/uc?export=view&id1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
                "kesan": "Bang Haikal kerennn, enak di ajak bercerita, dan juga baikk",  
                "pesan":"Semoga bang haikal selalu bisa mendapatkan hal-hal yang abang inginkan"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru sihhh, baikk, lucu jugaa",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan keren, selalu kece pas damaskus",  
                "pesan":"Semoga bang farhan selalu mendapatkan keinginan abang"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua keinginan kak aisyah cepat terwujud"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kak Cerine sangat asikk, humble, dan juga baikk",  
                "pesan":"Semoga kak cerine selalu dikelilingi hal-hal baikk"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya keren, baikk juga, dan asikk",  
                "pesan":"Semoga bang jaya mencapai semua keinginannya secepatnya"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak Najla sangat baikk, dan juga ramah sekalii",  
                "pesan":"Semoga semua keinginan kak najla tercapi secepatnya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"lampung selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Bang Rozak asik sihh, dan juga senyumnya lebarr sukaa",  
                "pesan":"Semoga bang rozak didekatkan dengan hal-hal baik"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"riau",
                "alamat": "belwis",
                "hobbi": "masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak teresa segera mendapatkan semua keinginannya"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Bang Hanif baikk, dan juga asikk, eh ramah jugaa",  
                "pesan":"Semoga bang hanif selalu menjadi yang terbaik"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"sumbar",
                "alamat": "sukarame",
                "hobbi": "main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak Audina lucuu, baikk, dan juga sangat amat ramah",  
                "pesan":"Semoga kak audin selalu dilingkung yang memiliki hal-hal baik"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak Cika lucuu, baikk, dan juga asikk",  
                "pesan":"Semoga semua keinginan kak cika tercapai secepatnyaaa"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak Gustin lucuu, baikk, dan juga ramahh",  
                "pesan":"Semoga kak gustin selalu didekat hal-hal baik"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang Harvin baiikk sihh, tapi sedikit pendiam",  
                "pesan":"Semoga semua keinginan bang harvin tercapai secepatnyaa"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "nginep di rumah kak yollanda",
                "sosmed": "@snasha._",
                "kesan": "Kak Sabina baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hmnOgiekX0BJuYnBc_7RB2sKiSg-w_Vp",
            "https://drive.google.com/uc?export=view&id=10pxW5IyZ1vxYOxefR7vQU2h7k_-Nn7Sc",
            "https://drive.google.com/uc?export=view&id=1R7Gt5PV3o5Vsh6kpM_0xvmrh36w0NjFx",
            "https://drive.google.com/uc?export=view&id=1w_p7KU_YNdHC0cWUvX9zkh3YAe0uPL3N",
            "https://drive.google.com/uc?export=view&id=1b-poQcRRVmRPitoT5Anvr1vNUReqYKY8",
            "https://drive.google.com/uc?export=view&id=1apj1fn8lmeHxjE_wYdZmkwrPXdAMYiwL",
            "https://drive.google.com/uc?export=view&id=1CgNfVVMX-S9a9iyS-YGYc361fDWUnM32",
            "https://drive.google.com/uc?export=view&id=1t67HOceUW6iH-s_W49NghbTSbI3ZoaEI",
            "https://drive.google.com/uc?export=view&id=1zyu2FvIjlcfPnAVQNf534vpbXE9XhfHr",
            "https://drive.google.com/uc?export=view&id=1yT6Pge6Amnc4QJgOqKPOM8AJGzzmum9Z",
            "https://drive.google.com/uc?export=view&id=1DxdQa1dF-qqxZxiQTEBfgQ8qycHk8BzO",
            "https://drive.google.com/uc?export=view&id=1ImbjAOzVb7oatJyiC_1H-JwMRHu8Y3Ij",
             "https://drive.google.com/uc?export=view&id=1IOIoxVZzr8Wxy3wgtD3Cug-0VmD2dHTx",
            "https://drive.google.com/uc?export=view&id=17-ar6qtPoFKNLWwIQqy9Xmzp9vrOpR6L",
            "https://drive.google.com/uc?export=view&id=1AEyDhbizmv0sRJ5fdqFv-Bbr_P05GFDk",
            "https://drive.google.com/uc?export=view&id=1Nbb8WGasyTbIpMWO0OQMu34OxUbSfXuF",
             "https://drive.google.com/uc?export=view&id=1FQ6Q9msLLdfcUjUFFImAytsqTwQaHrXF",

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
                "kesan": "Kak Arienta lucuu, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak arienta tercapai"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany maniss, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel kerenn, dan juga baiik",  
                "pesan":"Semoga bang nobel selalu didekat hal-hal baik"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi kerenn, dan juga baikk",  
                "pesan":"Semoga semua keinginan bang azmi tercapaii"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake lucuu, kerenn, dan juga baikk",  
                "pesan":"Semoga bang ayake bisa mencapai semua keinginan bang ayake"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar kereen, dan baikk",  
                "pesan":"Semoga bang caesar segera mencapai semua keinginannya"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia maniss, dan juga baikk, lucu juga sihh",  
                "pesan":"Semoga kak euodia selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal kerenn, baikk, dan juga ramahh",  
                "pesan":"Semoga bang haikal mencapai semua hal yang bang haikal inginkan"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450029",
                "umur": "18",
                "asal": "Depok",
                "alamat": "Oiya Cefa",
                "hobbi": "Jalan kaki gaboleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri lucuu, baikk, dan juga ramah",  
                "pesan":"Semoga semua keinginan kak putri segera terwujud"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@quenntanaabilaa",
                "kesan": "Kak Queenta maniss, lucuu, dan juga baikk",  
                "pesan":"Semoga kak queenta selalu bisa mencapai keinginannya"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman kerenn, dan juga asikk, baikk",  
                "pesan":"Semoga bang desman selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel maniss, dan juga baikkk sekali",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jeremi kerenn apalagi saat damaskus",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila maniss, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli manis, baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi lucuu, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan
