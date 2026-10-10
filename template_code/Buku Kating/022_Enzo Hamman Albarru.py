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
            "https://drive.google.com/uc?export=view&id=1Mvj4tDoyJuPkMWIYokSDNEyRcHUTKoN6",
            "https://drive.google.com/uc?export=view&id=1Kx6f3HY2PN-blpsA5vkhV2wFCf9kxFAm",
            "https://drive.google.com/uc?export=view&id=1K0ARtrEq5RkZBl1qqLC8sv90FAG8soyb",
            "https://drive.google.com/uc?export=view&id=1v3FhepfnYaMfMaVLdrM8cK7dObqhJJtJ",
            "https://drive.google.com/uc?export=view&id=1nSBFxZu3Ne7RWq7Fx5CAETiHynpV6_6-",
            "https://drive.google.com/uc?export=view&id=1XwsNoQHKTeBvDAU7j0NszAx0CA7D3ATB",
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
                "kesan": "Bang Fajar orangnya bijak dan berwibawa banget",  
                "pesan":"Semoga kedepannya Bang Fajar bisa terus mengisnpirasi kita semua"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren banget, asik, idola basket",  
                "pesan":"Semoga kedepannnya terus berdzikir dan menjadi orang keren"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya baik dan ramah",  
                "pesan":"Semoga Kak Efi terus berkembang dan suskes selalu"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya baik dan suka membantu",  
                "pesan":"Semoga kedepannya bisa terus mengispirasi dan menjadi orang yang hebat"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya seru dan baik banget",  
                "pesan":"Semoga kedepannya Kak Hafsa terus menjadi orang yang keren dan sukses"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia orangnya imut dan lucu",  
                "pesan":"Semoga kedepannya Kak Luthfia terus berkembang dan terus menjadi lucu dan imut"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1A9n8cKpNT1QjMeNMMWz6JQLyPs6pAay0",
            "https://drive.google.com/uc?export=view&id=1e44m-C0WWdEUmzKdHlDTU-0IGAAJ8cOd",
            "https://drive.google.com/uc?export=view&id=1WZzOzXuoqzGUZC57292c2M4yQmqunEtt",
            "https://drive.google.com/uc?export=view&id=1tqWRkZlE0naShb568mWwy3jUOpiDl9cs",
            "https://drive.google.com/uc?export=view&id=1vzwAX-Z9ES29rrn6GTiqpCjOEl8BEgDG",
            "https://drive.google.com/uc?export=view&id=1I-kf5KKFOqlzx716yTpWylUGsauMPO0a",
            "https://drive.google.com/uc?export=view&id=1xuGp1UKzJfIry6-6fwN6EhrN2sNxaERj",
            "https://drive.google.com/uc?export=view&id=1xUcPeK7kzME93Ub2P0Li1z_IBYuRhPyy",
            "https://drive.google.com/uc?export=view&id=13tphyUeQ4gKSqzOFJ4N-23SkVkMtgaIN",
            "https://drive.google.com/uc?export=view&id=1ad1uk4q-JlqlcN4PFBcBoNB4_D414cKp",
            "https://drive.google.com/uc?export=view&id=1tyolbY-KsMgsajQFoLQU2giTU0q3ALws",
            "https://drive.google.com/uc?export=view&id=1W3rODDWeH1r7bVnKtdNkfHQ63C5faqNb",
            "https://drive.google.com/uc?export=view&id=1ePUb3hA463FPWMOM6p0fBjLT9Lmca7hP",

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
                "kesan": "Bang Ridho orangnya bijaksana banget dan lucu juga",  
                "pesan":"Semoga kedepannya Bang Ridho makin sukses"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue mentor tpb terbaikk",  
                "pesan":"Semangat terus kak, semoga lulus tepat waktu dan sukses  selalu"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Asik dan seru banget orangnya",  
                "pesan":"Semangat terus bang, semoga projeknya makin sukses"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Keren dan jago basket",  
                "pesan":"Sukses terus, dan lebih berkembang untuk kedepannya"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Ramah dan baik banget kakaknya",  
                "pesan":"Semangat terus kak,sehat selalu dan sukses"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Abang ini keren dan pinter banget",  
                "pesan":"Sukses terus dan semangat kuliahnya bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak ini pinter banget, tutor metnumm fav",  
                "pesan":"Semangat terus, dan semoga perkuliahannya lancar selalu kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semoga kuliahnya lancar dan sukses terus"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Penyanyi handal dan asik abangnya",  
                "pesan":"Sukses terus dan semangat kuliahnya bang"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Baik banget kakaknya",  
                "pesan":"Semoga hidupya diberi keberkahan dan kelancaran selalu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Hobinya keren dan unik",  
                "pesan":"Semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Asik dan baik banget",  
                "pesan":"Semoga kuliahnya selalu lancar dan sukses"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya asik dan seru",  
                "pesan":"Semoga hidupya diberi keberkahan dan dipermudah di segala hal"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cqg2oc5399BNRU_N5vf72JmTQiRjvBxz",
            "https://drive.google.com/uc?export=view&id=1ccLpTN_qsEM2W_K1EOR4Bq5VDHsQb477",
            "https://drive.google.com/uc?export=view&id=1mK5QHtgWM8MqAfcOJ5PkoNJy_X0C2xj7",
            "https://drive.google.com/uc?export=view&id=1w4ZFAdgjb3ejaWj5k6YYx7fbgi-FqXvM",
            "https://drive.google.com/uc?export=view&id=1YIuc9gbI3pkdIf4RwqJjfHqHNpnif3zN",
            "https://drive.google.com/uc?export=view&id=1jSxZ27AUzTDjYep3iihH8TxtMGB-bReq",
            "https://drive.google.com/uc?export=view&id=1--eMSTK6pkST0JPCwsdo3A4rmE-rLrZ_",
            "https://drive.google.com/uc?export=view&id=1pMhnCqlxbWwC3JZecVOo1S6FVJRoqSoD",
            "https://drive.google.com/uc?export=view&id=1Mj-3CkT87ahWIuGVOmc-PgZivA3TiIV1",
            "https://drive.google.com/uc?export=view&id=1n44R8OjCJ3-VxtwUjcYbd_k98kKU3KZt",
            "https://drive.google.com/uc?export=view&id=16Xt1PXIm1VeFCzDC7GSm3EX3JdMG3IMq",#
            "https://drive.google.com/uc?export=view&id=1TAKigJ7_LPXv9hi4MqsfwIiFdQ0MhOF8",
            "https://drive.google.com/uc?export=view&id=14fQZN1kqzNxbjUAuAP0REgKg6qKcyO_Q",
            "https://drive.google.com/uc?export=view&id=1UiSXrUvD1-l193y-Wt8zb6JtfDcCdFoh",
            "https://drive.google.com/uc?export=view&id=1evQIsU_Qlp0LsePkeFZDHd9ldv77Kch3",

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
                "kesan": "Asik dan seru banget, jago basket",  
                "pesan":"Semoga sukses selalu dan makin jago basketnya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya lucu dan asik",  
                "pesan":"Semangat terus dan sehat selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "@ali_parisi3",
                "kesan": "Baik dan seru banget abangnya",  
                "pesan":"Semoga sehat selalu dan sukses perkuliahannya"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakaknya baik dan asik sekali",  
                "pesan":"Semoga makin berkembang dan sukses"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Asik banget abangnya, jago futsal",  
                "pesan":"Sukses dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya lucu dan baik banget",  
                "pesan":"Semoga kuliahnya diberi kelancaran dan sukses selalu"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Lucu dan seru banget abangnya",  
                "pesan":"Makin sukses dan sehat selalu"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknya baik banget dan seru ngobrolnya",  
                "pesan":"Semoga makin berkembang dan sukses terus untuk kakaknya"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Baik dan supportif banget abangnya",  
                "pesan":"Makin sukses dan berkembang terus buat abangnya"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Coach basket fav, seru dan asik banget",  
                "pesan":"Semoga makin sukses dan makin jago main basketnya"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abanya baik, dan lucu",  
                "pesan":"Semangat terus dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "...",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Baik dan lucu banget abangnya",  
                "pesan":"Makin semangat dan makin sukses"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya seruu dan baik banget",  
                "pesan":"Sukses terus buat kakaknya"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@cacalvra",
                "kesan": "Baik dan semangat bangett kakaknya",  
                "pesan":"Semoga makin sukses dan makin berkembang"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Seru dan asik banget abangnya",  
                "pesan":"Semoga makin sukses dan sehat selalu buat abangnya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19KqPt-7G9ox0sduIpoa47ByIRNbJCu1W", #bang haikal
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #kak kharisma
            "https://drive.google.com/uc?export=view&id=1en0vKIQSG3KRWILjicY26LaXm_QrAtw9", #kak hanna
            "https://drive.google.com/uc?export=view&id=1B4W635yKfuwzzxRSuWfK7cebNSOIvYee", #bang farhan
            "https://drive.google.com/uc?export=view&id=1pVEZWfCdnvnZtsgDi7SXWL6E1BCtO1dS", #kak aisyah
            "https://drive.google.com/uc?export=view&id=1jAwSAngD6OYu7YpDlJ0DE7ZF271kFxzY", #kak cerine
            "https://drive.google.com/uc?export=view&id=1_k0MwwnNo2xyaAd9Dao9zxdc5vkkTj9q", #bang jaya
            "https://drive.google.com/uc?export=view&id=1H5yJPC9wGAZXG8jcFJfq43essIwbHCDq", #kak najla
            "https://drive.google.com/uc?export=view&id=10pabq75lQc8JwD_HfHyRnjbqiX57EJ7o", #bang rozak
            "https://drive.google.com/uc?export=view&id=17s0r1MaJ2wNLivgQn3zHj4Ll79bpGaAY", #kak teresa
            "https://drive.google.com/uc?export=view&id=1QZDI7lJUN_OUl0bFoNIHKP9yTuaJXkbq", #bang hanif
            "https://drive.google.com/uc?export=view&id=10u1nPbqA_OqxO-6dqZPrUPFjWQ27cdLo", #kak audina
            "https://drive.google.com/uc?export=view&id=1YY8_S1LAfXUE2NeXpXWUDkEYRggHvZAP", #kak cika
            "https://drive.google.com/uc?export=view&id=1RgTwI_Tvq-e-MAky15m1Jn7dLs8FCqas", #kak gustin
            "https://drive.google.com/uc?export=view&id=1oMlx0Y8Mce8R_HUVpIMDH0JuGxJ_Gpys", #bang harvinsyah
            "https://drive.google.com/uc?export=view&id=1WwbubkFFBu4zqWEw8WpUoyAfVGi7sWPx", #kak rafa

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
                "kesan": "Abangnya asik dan suka merokok",  
                "pesan":"Semoga makin sukses dan sehat selalu buat abangnya"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik, senyumnya lucu banget",  
                "pesan":"Semakin berkembang dan sukses kak"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya asik dan jago basket",  
                "pesan":"Makin sukses dan motornya makin keren"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Baik dan seruu banget kakaknya",  
                "pesan":"Semoga makin sukses dan semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kak cerine orangnya seru dan ceria",  
                "pesan":"Makin berkembang dan sehat selalu buat kakaknya"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya seru dan jago basket juga",  
                "pesan":"Makin sukses dan berkembang untuk kedepannya"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik dan lucu",  
                "pesan":"Makin berkembang dan sukses perkuliahannya"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@rozakramdani__",
                "kesan": "Keren dan asik abangya",  
                "pesan":"Semangat terus buat abangnya"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik banget dan senyumnya lucu",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Seru, asik, dan lucu abangnya",  
                "pesan":"Selalu semangat dan terus berkembang buat abangnya"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "...",
                "asal":"....",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@audinaf_03",
                "kesan": "Lucu dan baik banget kakaknya",  
                "pesan":"Semoga makin sukses dan bahagia selalu"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakaknya baik banget dan asik sekali",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses, dan sehat selalu"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@gustin.tpb",
                "kesan": "Kakaknya lucu, baik, dan ramah sekali",  
                "pesan":"Semangat teruss buat kakaknya, semoga makin berkemban dan sukses"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Abangnya baik dan ramah banget",  
                "pesan":"Semangat dan makin sukses selalu"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@snasaa._",
                "kesan": "Kakaknay seru dan asik",  
                "pesan":"Semangat terus buat kakaknya, semoga makin sukses, dan sehat selalu"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y3vcyfOJQRnFtUQaEqdH3x5KfDKXkCY-", #kak arienta
            "https://drive.google.com/uc?export=view&id=1844MFmmgAKdz2QnHm_NoUN48f8oyrqUp", #kak vany
            "https://drive.google.com/uc?export=view&id=1tjC1fUf4_5_GALWjxZ24M-IXxISa8W0j", #bang nobel
            "https://drive.google.com/uc?export=view&id=17Q7ZY7Jzayrpbw-1Y4S_icnB4IOknH6C", #bang azmi
            "https://drive.google.com/uc?export=view&id=1peZkeZvKPoWv3GCZF19ivu93IECYV4tA", #bang ayake
            "https://drive.google.com/uc?export=view&id=13gY82xeuQH5X4QjjlMrIOe2ynPSeBM1G", #bang caesar
            "https://drive.google.com/uc?export=view&id=1rxyIeYZl-l2_2CA3wVi_-E9uR9SZOCxe", #kak euodia
            "https://drive.google.com/uc?export=view&id=1XQw0X1R6uyCXfMX2KBKuvjQ9lOu6puKn", #bang haikal
            "https://drive.google.com/uc?export=view&id=1PZMDd59U2FmXEGgVk6xNd84kisEOFj3r", #kak putri
            "https://drive.google.com/uc?export=view&id=1HFa7avyd7bEM690PXXLUwvHpTYl8EQxU", #kak queenta
            "https://drive.google.com/uc?export=view&id=1HWrrOHZ52oGxsK2A_WAcUZclwGz5YMVY", #bang desman
            "https://drive.google.com/uc?export=view&id=1o54aiI5ZGcplDNJUWfHEUq-UVSX3L17f", #kak azzelya
            "https://drive.google.com/uc?export=view&id=1FU6F8Fvk8DOl-KEXaCh0zD0S0jkA3qpM", #kak charrlindah
            "https://drive.google.com/uc?export=view&id=16WWclUsSIMkwxMbALOlEhOITpxzvMdo_", #bang jeremi
            "https://drive.google.com/uc?export=view&id=1OH5DsiP4p9o2xBIDcV3Cj5z9GdpQlFPy", #kak nabila
            "https://drive.google.com/uc?export=view&id=1XSg4M-poq0VL4YsSALwfri591NsH13Lo", #bang rafli
            "https://drive.google.com/uc?export=view&id=1QgQjDTJ5IM3vGd4GD0N8cmez4HgkKbpr", #kak salavi

        ]
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "Nim": "123450097",
                "Umur": "21",
                "Asal": "Pinggir Pantai",
                "Alamat": "Samping Kost Capo",
                "Hobbi": "Ngerjain Anak Kader",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Kakaknya baik, dan pembimbing",  
                "Pesan":"Sehat selalu dan dipermudah urusannya"# 1
            },
            {
                "Nama": "Vany Salsabila Putri",
                "Nim": "123450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Pudan Kost",
                "Hobbi": "Pacaran",
                "Sosmed": "@vany.salsabilaa",
                "Kesan": "Baik dan lucu kakaknya",  
                "Pesan":"Makin sukses dan terus berkemmbang buat kakak nim kuh"# 1
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "Nim": "123450023",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Jago sulap dan profesional abangnya",  
                "Pesan":"Semoga makin sukses dan dipermudah segala urusannya"# 1
            },
            {
                "Nama": "Afriza Azmi",
                "Nim": "124450110",
                "Umur": "20",
                "Asal":"Malang",
                "Alamat": "Lapangan",
                "Hobbi": "Berantem",
                "Sosmed": "@friezazmi",
                "Kesan": "Seru dan paling semangat pas supporteran",  
                "Pesan":"Sukses terus dan sehar selalu buat abangnya"# 1
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "Nim": "124450059",
                "Umur": "21",
                "Asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "Alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "Hobbi": "Cekek Ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Ramah dan baik abangnya",  
                "Pesan":"Makin sukses dan sehat selalu"# 1
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "Nim": "124450017",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobbi": "Pulang Kampung",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Humble dan keren abangnya",  
                "Pesan":"Semoga semakin berkembang dan makin sukses"# 1
            },
            {
                "Nama": "Euodia Meiliana Fredita",
                "Nim": "124450029",
                "Umur": "18",
                "Asal":"dari mana aja boleh",
                "Alamat": "Didalam Kamar dibalik pintu",
                "Hobbi": "Surving",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Seru dan asik kakaknya",  
                "Pesan":"Semangat terus dalam menjalani kuliahnya dan makin sukses"# 1
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "Nim": "124450032",
                "Umur": "Tinggi Bang Azmi - 155",
                "Asal":"Jambi",
                "Alamat": "Belakang Pemancingan",
                "Hobbi": "Tidur",
                "Sosmed": "@_haikaaall",
                "Kesan": "Baik dan humble abangnya",  
                "Pesan":"Semangat dan sukses buat abangnya"# 1
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "Nim": "124450056",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "oiya cafe",
                "Hobbi": "jalan kaki ga boleh naik gojek",
                "Sosmed": "@putrimannaa",
                "Kesan": "Baik dan ramah banget kakaknya",  
                "Pesan":"Sehat selalu sehat dan sukses buat kakaknya"# 1
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "Nim": "124450059",
                "Umur": "19",
                "Asal": "Rumah sakit",
                "Alamat": "Depan pemancingan",
                "Hobbi": "Makanin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Kakaknya ramah dan baik dan humble",  
                "Pesan":"Semoga dipermudah segala urusan dan makin sukses"# 1
            },
            {
                "Nama": "Desman Velius Halawa",
                "Nim": "123450114",
                "Umur": "25",
                "Asal": "Nias",
                "Alamat": "Airan",
                "Hobbi": "Main musik",
                "Sosmed": "@dsmanhal",
                "Kesan": "Keren dan asik abangnya",  
                "Pesan":"Sehat selalu dan sukses buat abangnya"# 1
            },
            {
                "Nama": "Azzelya Thianandry",
                "Nim": "124450041",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@azzelytn",
                "Kesan": "Kakaknya baik, ramah, dan lucu",  
                "Pesan":"Semoga makin sukses dan kuliahnya lancar"# 1
            },
            {
                "Nama": "Charrlindah",
                "Nim": "124450041",
                "Umur": "...",
                "Asal": "...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@charrlln",
                "Kesan": "Baik dan ramah dan lucu banget kakaknya",  
                "Pesan":"Dipermudah segala urusan dan semakin sukses"# 1
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "Nim": "...",
                "Umur": "...",
                "Asal":"....",
                "Alamat": "....",
                "Hobbi": "...",
                "Sosmed": "@jemarrro",
                "Kesan": "Keren dan salah satu penyemangat pas supporteran",  
                "Pesan":"Semoga makin sukses dan sehat selalu"# 1
            },
            {
                "Nama": "Nabila Nur Azizah",
                "Nim": "124450048",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@n.bila_a",
                "Kesan": "Baik dan ramah sekali kakaknya",  
                "Pesan":"Dipermudah segala urusan dan makin sukses buat kakaknya"# 1
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "Nim": "124450007",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Keren dan asik banget abangnya",  
                "Pesan":"Sehat selalu dan sukses buat abangnya"# 1
            },
            {
                "Nama": "Salavi Naharani",
                "Nim": "124450090",
                "Umur": "...",
                "Asal":"...",
                "Alamat": "...",
                "Hobbi": "...",
                "Sosmed": "@avi.nhr",
                "Kesan": "Baik dan ramah dan lucu banget kakaknya",  
                "Pesan":"Semoga selalu sehat dan sukses menjalani kuliahnya."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
