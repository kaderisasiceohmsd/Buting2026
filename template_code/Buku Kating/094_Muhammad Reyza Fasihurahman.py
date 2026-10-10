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
            "https://drive.google.com/uc?export=view&id=1jTt4osiJlmcxLGM6anHugKQ4p6NmDUFu",
            "https://drive.google.com/uc?export=view&id=1lV3AFkRaJ-f8n0ILwYZE7igGiST8LQ5O",
            "https://drive.google.com/uc?export=view&id=1cKoLOVA0C-uGTZAWHK9ij-KJ2kWYZlKU",
            "https://drive.google.com/uc?export=view&id=1ZjJrfHoTdNclPxZOY7iXAIH2Bek7sHtl",
            "https://drive.google.com/uc?export=view&id=1_gi-ChNER8A-MpEIs3noBFLZOO_pdZXO",
            "https://drive.google.com/uc?export=view&id=1zu0Vf0wTxK0GgGLWkhVWilKlgaIQX2Ew",
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
                "kesan": "Bang fajar him orang yang baik, ramah dan rendah hati, belajar banyak hal juga dari bang him",  
                "pesan":"Semoga kedepannya reza bisa mewujudkan apa yang bang fajar harapkan dari saya nantinya, terimakasih bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang aqil jen orang yang ramah, rendah hati, suka sharing ilmu dan peduli antar sesama",  
                "pesan":"Semangat teruss bang aqil, semoga impiannya bisa terwujud"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi baik hati, murah senyum, bisa mengispirasi banyak orang",  
                "pesan":"keep strong kak, semoga keinginannya terwujud!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang qois orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya reza bisa tumbuh seperti bang qois, terimakasih bang"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak hafsa orangnya sangat baik, ramah, dan juga berkesan.",  
                "pesan":"Semoga kedepannya kak hafsa dikelilingi dengan hal baik ya kak"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfia orangnya sangat baik, ramah, dan juga sangat menginspirasi bagi saya karena jadi asprak baik hati.",  
                "pesan":"Semoga kedepannya kak luthfia bisa tumbuh seperti kak luthfia, terimakasih kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hgy9q3amN5Ed-UsxvF3X7ETqlxrXKMAN",
            "https://drive.google.com/uc?export=view&id=1ayKNDuFh7xL76p8l4nFCLyh0iutfT5je",
            "https://drive.google.com/uc?export=view&id=1f-NdOIjLabE45U5idBE5cdRFcyQ_6nze",
            "https://drive.google.com/uc?export=view&id=1muE5178D3qZwbasNm5XDyhcNBizmu80o",
            "https://drive.google.com/uc?export=view&id=12deNFjAzGlr5IJjH4eBB-u93pYsdi1I7",
            "https://drive.google.com/uc?export=view&id=1l_ONFSNbXI4sJmbvhYDwQ6BmPO4CxvHt",
            "https://drive.google.com/uc?export=view&id=1D00XpO2mhmq-6hEgwpIRBBgsBxaG_y99",
            "https://drive.google.com/uc?export=view&id=1LYlY2i1ExdTUKKKKenFAtyVR7faGNduT",
            "https://drive.google.com/uc?export=view&id=1OyQ9zNfDy-m48A0f6HVAoVkXc67PdtDF",
            "https://drive.google.com/uc?export=view&id=1D46Ytn7hSO9EpIX6BIgCPj7k9qyxWvjd",
            "https://drive.google.com/uc?export=view&id=1baq71b6miwzh7f2TTBVZrg_LnajmeMOL",
            "https://drive.google.com/uc?export=view&id=1JlzSUy2Ybrols4BnViuGs06fPqBGZuS1",
            "https://drive.google.com/uc?export=view&id=1NOcecP852f6Hpogp0wxGOMx9z26nVfqN",

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
                "kesan": "Bang Ridho orangnya sangat humble, baik, dan juga sangat berkesan bagi saya.",  
                "pesan":"Semoga kedepannya reza bisa tumbuh seperti bang ridho, terimakasih bang ilmunya"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue yang memberikan banyak insight hal baru, berkesan, baik, ramah",  
                "pesan":"semangat terus kuliahnya kakak dan semoga terus menginspirasi orang banyak yak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang dharu menjadi role model karena prestasi yang membanggakan dan cara berpikir yang baik",  
                "pesan":"semangat menginspirasinya bang dharu, semoga tercapai segala keinginannya yaa"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Niko orangnya sangat humble, baik, dan juga sangat berkesan bagi saya.",  
                "pesan":"Semoga kedepannya bang Niko dikelilingi dengan hal baik ya bang"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak siti orangnya sangat humble, baik, dan juga memiliki energi yang kuat dalam bersosialisasi.",  
                "pesan":"Semoga kedepannya kak siti keinginannya tercapai dan segala hal urusannya dimudahkan"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro orang yang baik, ramah, senang bersosialisasi kepada siapapun.",  
                "pesan":"Semoga kedepannya bang givaro bisa terus menginspirasi dan semangat kuliahnya yak bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya sangat humble, baik, dan juga ramah.",  
                "pesan":"Semoga kak nisa kuliahnya dilancarkan dan segala hal urusannya dimudahkan"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak hani orangnya sangat humble, baik, dan juga berkesan.",  
                "pesan":"Semoga kedepannya kak hani keinginannya tercapai dan kuliahnya dimudahkan"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang jeremia orang yang baik, ramah, menginspirasi banyak orang.",  
                "pesan":"Semoga kedepannya bang jeremia bisa terus menginspirasi dan segala urusannya dimudahkan"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica yang memberikan banyak ilmu hal baru, berkesan, baik, ramah",  
                "pesan":"semangat terus kuliahnya kakak dan semoga sehat as always"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang jona orangnya humble, baik, ramah, dan juga asik dengan semua orang",  
                "pesan":"semangat terus kuliahnya bang, semoga cumlaude biar mantap"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak sekar orangnya baik, ramah, peduli sesama dan juga humble",  
                "pesan":"semangat terus kuliahnya kakak dan semoga usahanya selalu dimudahkan."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kak nashwa yang memberikan banyak insight hal baru, berkesan, baik, ramah",  
                "pesan":"semangat terus kuliahnya kakak dan semoga terus diberi kesehatan"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14YENE-OttLu9t6-K1D3EiVItt9VWgMFi",
            "https://drive.google.com/uc?export=view&id=1dpGP6YKR6uNScQ310uzfGga7y9pyXFHr",
            "https://drive.google.com/uc?export=view&id=1nziGOtWvoE56r050VfNywXLuxqxhjOyb",
            "https://drive.google.com/uc?export=view&id=1CHWAexG6h9pgrF47C39pXCPOwkRW3PK1",
            "https://drive.google.com/uc?export=view&id=1_9LmIb8SHBTmsJzBXV1lS6loX-Uv4wIc",
            "https://drive.google.com/uc?export=view&id=1IVfl9n6xhg6LMNRCK9TcKyfYe8IPiLa6",
            "https://drive.google.com/uc?export=view&id=1x_Tl2UiGCWgXIWLOl3wqf8oZiF-pbbhr",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=1_Ma3wlwjrohrks0QJnbrZxfRMfIJWEbH",
            "https://drive.google.com/uc?export=view&id=1y-jE3qswGgkURBQHg2m6rOp9YIKcI8Y3",
            "https://drive.google.com/uc?export=view&id=1WcqyfQwvpry_pOsTu-lSnlwCOucxQBiW",
            "https://drive.google.com/uc?export=view&id=1v6WwuUUbytkBJS9m6fWfUm6sn1BFi2Rf",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1XgVw4Dk65snrhmCEJPjtIu89C8WstF71",
            "https://drive.google.com/uc?export=view&id=1ps1AIPSHIWjV-Z98SY7bA7xj4Y5BwTUw",

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
                "kesan": "Bang kevin orang yang ramah, baik, suka sharing ilmu dan rendah hati",  
                "pesan":"Semoga kedepannya bang kevin selalu diberikan kemudahan dalam segala hal"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak razka orangnya humble, baik, seru dan berkesan",  
                "pesan":"semangat terus menggapai mimpinya ya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang ali orang yang humble, ramah, senang bersoialisasi dengan siapapun",  
                "pesan":"semangat terus kuliahnya dan menggapai keinginannya bang alii"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak ayu adalah orang yang seru, baik, ramah dan juga senang bersosialisasi dengan banyak orang",  
                "pesan":"Semoga kedepannya kak ayu dimudahkan segala urusannya dan impiannya tergapai"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang dafa orangnya humble, murah senyum, baik, dan suka sharing ilmu.",  
                "pesan":"Semoga kedepannya bang dapa selalu dikelilingi hal baik"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak ayu adalah orang yang seru, baik, ramah dan juga senang bersosialisasi dengan banyak orang",  
                "pesan":"Semoga kedepannya kak ayu dimudahkan segala urusannya dan impiannya tergapai"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang afdal orang yang humble, ramah, dan tegas",  
                "pesan":"semangat terus kuliahnya dan semoga dimudahkan segala urusannya bang afdall"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwi adalah orang yang seru, baik, asik",  
                "pesan":"Semoga kedepannya kak juwi dikelilingi hal baik dan dimudahkan kuliahnya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwa orang yang asik, humble, dan murah senyum",  
                "pesan":"semangat terus dalam menginspirasi dan semoga sehat selalu"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Bang andra orangnya rendah hati, humble, respect each other",  
                "pesan":"semangat terus mengembangkan potensinya bang, dan semoga impiannya kegapai"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang bryan orangnya seru, suka sharing ilmu juga dan asik",  
                "pesan":"semangat terus menghadapi dunia dan sehat selalu"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang ghiyats orangnya humble, suka sharing ilmu juga dan humoris",  
                "pesan":"semangat terus menghadapi dunia dan dimudahkan kuliahnya"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak indah adalah orang yang seru, humble, ramah dan asik",  
                "pesan":"Semoga kedepannya kak ayu dilancarkan kuliahnya dan semoga senang selalu"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kak caca adalah orang yang seru, baik, ramah dan juga murah senyum",  
                "pesan":"Semoga kak caca dimudahkan segala urusannya dan dilancarkan kuliahnya"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Bang rafka orangnya respect each other, humoris dan humble",  
                "pesan":"semangat terus futsalnya bang dan tetap sehat seperti biasanya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZbtFYqRx-UIRexCjvPMg19hbaHNtLEuE",
            "https://drive.google.com/uc?export=view&id=1U-wgpB8AywS5Uigfmbq0p_ngJl1WLpen",
            "https://drive.google.com/uc?export=view&id=178Cjp5REe0ppDV_o7hltZjO7LaZ4RSqy",
            "https://drive.google.com/uc?export=view&id=1PsrHc2055Iq1FHwalxnPL5NTHeOfDAj9",
            "https://drive.google.com/uc?export=view&id=13eDh0BIBZEUkOWj7qh34OyrRCJg9ZA9l",
            "https://drive.google.com/uc?export=view&id=16_rmx71QOIPQItsODJVjZENguCmNCewP",
            "https://drive.google.com/uc?export=view&id=1vrvQiXL0TR4J3kthgXqdmaBSrVNFEFCl",
            "https://drive.google.com/uc?export=view&id=1ltwdCfA44EZsQS43xSv239_49lUj0zsu",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=1FOMOic0Fca9yMv6uLZazbaLclrsAy0BB",
            "https://drive.google.com/uc?export=view&id=1LUweCaL1wL5KTBtbUbYIrwNP2-gXviAR",
            "https://drive.google.com/uc?export=view&id=1SIeaxcCezWHWSgRNM4LCebhkcu1cvOlZ",
            "https://drive.google.com/uc?export=view&id=1cc4c5fIY3N4PJWHp6wFtAziImmEhIdVz",
            "https://drive.google.com/uc?export=view&id=1hclkdQoRLZTnluBOivih1djjnc15hKlh",
            "https://drive.google.com/uc?export=view&id=1Tp24KS-vwTrXWtim3_DHbNli0kYdI7RW",
            "https://drive.google.com/uc?export=view&id=1uZHGxQzH9CwAhHs2N1KUcUa6vvqd60j3",

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
                "kesan": "Bang haikal orangnya seru, asik, baik, dan humoris level up.",  
                "pesan":"Semoga kedepannya bang haikal dimudahkan urusannya dan selalu diberkati"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma orangnya super humble, cukup humoris dan berkesan.",  
                "pesan":"semangat terus menginspirasinya yaa kak"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna orangnya humble, humoris, murah senyum dan ramah.",  
                "pesan":"semangat terus kuliahnya yaa kak dan semoga selalu diberkati"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang farhan orangnya baik hati, ramah, murah senyum, humoris.",  
                "pesan":"Semoga kedepannya bang farhan ddilancarkan rezekinya dan dilancarkan kuliahnya"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya baik, ramah, respect each other dan murah senyum.",  
                "pesan":"semangat terus kuliahnya kak dan semoga dimudahkan segala urusannnya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kak Kharisma orangnya murah senyum, positive energy, baik.",  
                "pesan":"semoga selalu diberi kesehatan dan keberkahan"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang jaya orangnya humble, ramah, senang bersosialisasi, asik.",  
                "pesan":"Semoga bang jaya diberikan umur yang panjang dan selalu diberkati"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak najla orangnya humble, respect each other, low profile dan baik hati.",  
                "pesan":"semoga kak najla hidupnya selalu dikelilingi hal baik yaa kak"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Bang rozak orangnya seru, asik, ramah, dan murah senyum.",  
                "pesan":"Semoga kedepannya bang rozak diberikan umur yang panjang dan selalu dimudahkan urusannya"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak teresa orangnya asik, baik, dan humoris.",  
                "pesan":"semoga selalu dikelilingi hal baik dan semoga selalu diberkati"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan":"Bang hanif orangnya ramah, humble, low profile, dan cukup humoris.",  
                "pesan":"Semoga kedepannya bang hanif dimudahkan urusannya dan rezekinya dilancarkan selalu."# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "...",
                "asal":"....",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak audina orangnya humble, positive energy dan berkesan.",  
                "pesan":"semoga hal baik selalu mengelilingi yaa kak, keep strongg!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kak cika orangnya low profile, ramaah, baik, dan humble.",  
                "pesan":"semoga selalu diberi kesehatan dan diberkati selalu"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak gustin orangnya humble, ramah, baik dan humoris.",  
                "pesan":"semangat terus kuliahnya yaa kak, god bless u"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan":"Bang harvin orangnya seru, asik, baik, dan humoris level up.",  
                "pesan":"Semoga kedepannya bang harvin dimudahkan urusannya dan selalu diberkati"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak bina orangnya baik, cukup humoris, ramah, dan positive energy.",  
                "pesan":"semangat terus kuliahnya kak, dan semoga dilancarkan selalu urusannya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15kkuKeZXvSlIsL03c9BnFAHKhCpH2LWG",
            "https://drive.google.com/uc?export=view&id=1DPACbfL9qKbbjl_68Lu1u8weG0YiHQlN",
            "https://drive.google.com/uc?export=view&id=1_EyoZNucEcdKhdValFp7TlRlM9ZOYC1T",
            "https://drive.google.com/uc?export=view&id=1O9vWJp7UdLzVzEvvIp9GTtWmL7dSZGc7",
            "https://drive.google.com/uc?export=view&id=11l6yKGYxnFONauY1yoyNMkaSPhsE3rfO",
            "https://drive.google.com/uc?export=view&id=1sZvsbrvw3xobNjcAtWvrB7a5ODQ8JHFX",
            "https://drive.google.com/uc?export=view&id=1_9EBsaKR9VJ52thx8MlZ6kNYkl8OCXm4",
            "https://drive.google.com/uc?export=view&id=1xxly_yAEM7BYUjIjYrufvazLrP9a4n62",
            "https://drive.google.com/uc?export=view&id=1iqv6SqyZiD9seFaQJHN_et58M2O-UeIT",
            "https://drive.google.com/uc?export=view&id=1Tzj6Fc6J8wp-IpTomMM_K7ChVatytJRO",
            "https://drive.google.com/uc?export=view&id=1GEgyd4bq77rkjinAHgXT_uT_G2uzhlj6",
            "https://drive.google.com/uc?export=view&id=1XB4MnbquWxxiBDX4CfhtrPxruHasanXw",
            "https://drive.google.com/uc?export=view&id=1atxF4ZINctSc4ETv8wHMII7kTRqL2ftr",
            "https://drive.google.com/uc?export=view&id=10mbFZwLHV5pWk7_DwDW0a9ifeXPVHKDu",
            "https://drive.google.com/uc?export=view&id=1sqeAo7wle6UZbn-0QcjreJRl0ecbTsBl",
            "https://drive.google.com/uc?export=view&id=1UlR-ad508ASzMpMQu-rOnjPrWHS8hx5H",
            "https://drive.google.com/uc?export=view&id=1s6XTjJQiqKqGXwoVfxqP-5GREihCvB44",

        ]
        data_list =[
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kakak NIM baik hati, tidak sombong, lemah lembut, humble, dan ramah",  
                "pesan":"Semangat kuliahnya yaaa kak, semoga selalu dilancarkan rezekinya"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya ramah, humble, cukup humoris",  
                "pesan":"Semangat terus dalam segala hal yaaa kak, semoga selalu dimudahkan urusannya"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel orangnya welcome, baik, humble, dan respect each other",  
                "pesan":"Semangat terus menggapai mimpinya bang, semoga sehat selalu bang"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orangnya humble, humble, low profile, dan ramah",  
                "pesan":"Semangat terus menjalankan kehidupan bang, semoga segala urusannya dipermudah"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang yake orangnya wlcome, low profile, baik, dan menginspirasi",  
                "pesan":"Semangat terus kuliahnya bang, semoga selalu dipermudah urusannya bang"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang caesar orangnya supportif, ramah, humble, dan berkesan",  
                "pesan":"Semangat terus menggapai mimpinya bang, semoga sehat selalu bang."# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak yudia itu baik hati, ramahh, baik hati, humble, dan menginspirasi",  
                "pesan":"Semangat terus dalam menjalankan kehidupan yaaa kak, semoga selalu dilancarkan rezekinya"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal orangnya ramah, low profile, humble, dan menginspirasi",  
                "pesan":"Semoga apapun yang diharapkan terjadi di tahun ini bang"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak putri orangnya humoris, lucu, baik hati, dan low profile",  
                "pesan":"Semangat kuliahnya yaaa kak, god bless u kak"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "Kak bila orangnya baik, murah senyum, ramah, dan sangat interaktif",  
                "pesan":"Semangat terus yaaa kak, semoga dimudahkan segala urusannya."# 1
            },
             {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang ini humble, baik, ramah",  
                "pesan":"sukses selalu bang (coach) desman, semoga lancar sampai lulus ya bangg"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya lucu dan baik, serta ramah ",  
                "pesan":"Semangat dan sehat selaluu kakaa, semoga hal baik selalu berdatangan"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kak caca itu ramah, baik, dan humoris",  
                "pesan":"sehat sehat ka cacaa, semoga semester ini dan kedepannya dilancarinn segala urusan kaka yaa"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jemar ini baik dan humble serta welcome kepada siapapun",  
                "pesan":"Semangat terus bang capo, kece dah udh masuk tiktok itera ganteng"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila humble dan talkative, serta humoris",  
                "pesan":"sehat sehat kakaa, semoga hal baik selalu berdatangan yaaa"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini baik, welcome dan ramah",  
                "pesan":"Semangat teruss bang rafli, semoga sehat selalu bahagia selaluu dan dimudahkan urusannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak imut, lucu, baik, ramah dan talkative",  
                "pesan":"sehat sehat dan lancar luncur kuliahnyaa kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
