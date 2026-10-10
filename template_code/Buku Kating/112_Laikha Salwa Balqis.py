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
            "https://drive.google.com/uc?export=view&id=1mwTglwSAO6XR-RPpDPlEzEz_my0_t8fd",
            "https://drive.google.com/uc?export=view&id=1RSot8q9RBbGCjSSqsA1BJjiQApzsg9eC",
            "https://drive.google.com/uc?export=view&id=1uGQykTLAbXffdOdSnH6Ay4h8pCRuJ2Ci",
            "https://drive.google.com/uc?export=view&id=19RRGjm139otsg9rIk28xWqoMvl5Pry7E",
            "https://drive.google.com/uc?export=view&id=1I-vOhuR2C9eggs8YX56E7kwuVjhviL_E",
            "https://drive.google.com/uc?export=view&id=1MF1bkPdW0wtoJtJyhwZ-GQeL_UtTDp-V",
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
                "kesan": "Menurut saya, Bang Fajar adalah orang yang mengayomi dan sangat menginspirasi.",  
                "pesan": "Semoga Bang Fajar sukses dan sehat selalu ya bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil seru, santai, dan bisa memastikan semua orang masuk kedalam obrolan",  
                "pesan": "Semangat terus bang Aqilll"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi asyik dan baikkk",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois baik dan kerenn.",  
                "pesan":"Semoga bang qois sukses dan sehat selaluu"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak hafsa orang yang humble.",  
                "pesan":"Semoga kak hafsa sukses dan sehat selaluu"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak luthfia lucu dan asik.",  
                "pesan":"Semangat terus ya kakkk kuliahnya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ag7-igTyHLOvBj43yGBEpKmieCz61t-B",
            "https://drive.google.com/uc?export=view&id=1B1Aij2L3bcAnsRPhJaWEHHLLB-d7Di4t",
            "https://drive.google.com/uc?export=view&id=18AgXt5LNUXQCovMR4O1QdKV_Q8sQMd5G",
            "https://drive.google.com/uc?export=view&id=1Ea9tQVdQZ_uUNCRbAbVqgCpmF_tn3afB",
            "https://drive.google.com/uc?export=view&id=1wiB1UJGqxzXsU8TcLC3JPAfYVqGYt5dD",
            "https://drive.google.com/uc?export=view&id=1Hz9RZMNX1-U57XmCSO70LO_Z90k9_2zi",
            "https://drive.google.com/uc?export=view&id=1H0ckAv5DPPt5P3oU7wU5T_CH9XMYkbTV",
            "https://drive.google.com/uc?export=view&id=1JQCSpxlgzqMfM2pv_mMIThgqW2D2ANi8",
            "https://drive.google.com/uc?export=view&id=1cAMBfPrO75aUP3pPOsm1Pt6HHwm5Ocvi",
            "https://drive.google.com/uc?export=view&id=1e9_aazaxOio0RBjkPV2n39xC2PAPKrWF",
            "https://drive.google.com/uc?export=view&id=1Tt_HZEvvXn9nxe-g1SZ1PhgCcJptvP0Y",
            "https://drive.google.com/uc?export=view&id=1hZjrhNYKd4_T7pywfiJKLWZh7vA04sAx",
            "https://drive.google.com/uc?export=view&id=1yG5AvLHhk3QGdHzf14RCNdt-E7y-nMIX",

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
                "kesan": "Jujur bang rido kocak banget, tapi tetep bisa serius.",  
                "pesan":"Makasih udah bikin ketawa terus bang hahaha, semoga bang rido sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue asik, talkative, dan humble",  
                "pesan":"Semangat kak juee kuliah dan siarannyaa!!"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Jujur bang dharu keren, panutan",  
                "pesan":"Semangat terus bang!! semoga exvoltasnya lancarr"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang niko baikk, informatiff",  
                "pesan":"Semoga bang niko sukses terusss"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kak sarifah lucuu, baik, humble",  
                "pesan":"Semoga kak saripah sukses terus bahagia selaluu"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang givaro jujur humornya kaya receh gitu sering ketawa ngakak, tp abangnya baik dan informatif",  
                "pesan":"Semoga bang givaro bahagia dan sukses selalu"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa baikk dan lucu, such a good organizer sepertinya",  
                "pesan":"Semoga kedepannya laikha bisa kaya kak nisaa"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kak hani kalem, baik, lucu",  
                "pesan":"Sukses terus kak hanii, sehat sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang yang suka nyanyi, looksnya kaya orang pintar dan hebat",  
                "pesan":"semangat terus kuliahnya banggg !!!"# 1
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
                "kesan": "Bang jona baik dan suka ada gerakan tambahan hahaha",  
                "pesan":"semangat terus kuliahnya bang jonaa !!!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak sekarr baikkk, lucu dan kalo udah kenal ternyata ekspresif",  
                "pesan":"Semangat kuliahnya kak sekar semoga lancar terus semua urusannya!!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "ka wawa lucu dan imut",  
                "pesan":"Semoga kuliahnya lancar terus ya kakk!!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ycOMykVCpFeyupvi_LtzsrEEl3x_BPmP",
            "https://drive.google.com/uc?export=view&id=1GudBW4sElvNx8H4B1et-_C6g0F4AkKOx",
            "https://drive.google.com/uc?export=view&id=19yU1LJV_62a6wk7IRMJnDtB45dwP-Uap",
            "https://drive.google.com/uc?export=view&id=1YuQzPAMbSQqWKrZ3cjKrsM3bwbghlHn-",
            "https://drive.google.com/uc?export=view&id=1aqbasPRPlnG3T1FTxDaFcIjkfjvHKaHB",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1r4zVSnpxIYLE3lmWDcBCnSDjmiogaiWA",
            "https://drive.google.com/uc?export=view&id=1lWimSBk4TkOwnSg3xp3PIxw_GHujDDzg",
            "https://drive.google.com/uc?export=view&id=1q-4aEbxKGq7W76VTR9KHMFm9fEscq2vl",
            "https://drive.google.com/uc?export=view&id=1kATfmNQxpwCCws0RA_CjJHTEKoht3De_",
            "https://drive.google.com/uc?export=view&id=1r1bNhzN239GdHbamj8rOP6TtRIahUmO_",
            "https://drive.google.com/uc?export=view&id=1-jJ_A2BNfm2_nHdb5h_Wdtu3OvMtMUok",
            "https://drive.google.com/uc?export=view&id=1Z63-dzVUOt3Fua4NSnD8LeQs13mParzk",
            "https://drive.google.com/uc?export=view&id=1L1p2mlC6JOw2PI3M_lvrOaKrDaQjyTAe",
            "https://drive.google.com/uc?export=view&id=1Hg5BGnyoGlAfMgCWlHQSL2v8AoxocKGo",

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
                "kesan": "Bang kevin keren,baik, namanya bagus",  
                "pesan":"Semoga dilancarin ya bang kuliahnya sampai luluss"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak razka asik, cantik, baik",  
                "pesan":"Semangat terus kak razkaa, semoga sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abang ini asik",  
                "pesan":"Semangattt bang kuliahnyaaa!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini imut dan humble",  
                "pesan":"sehat sehat kakakk, jangan lupa bahagia"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya asik dan baik.",  
                "pesan":"Lancar lancar yaa bang kuliahnya, semoga bahagia teruss"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakanya humble dan murah senyum.",  
                "pesan":"Semoga kakanya sehat teruss yh kakk"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang ini baik dan asik",  
                "pesan":"Semoga abangnya lancar rezekinya yhh, sehat selalu dan juga lancar kuliahnya"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita ini lucuu",  
                "pesan":"Kakkk yang semangat yah kuliahnya semester ini, kaka pasti bisaa"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Dengerin laikha nyanyi",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan baikk dan talkative hahaha",  
                "pesan":"Bang ridwan semangat ya bang semester ini, nnt saya nyanyiin dah kl mumet WKWKWK"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abang terexcited hahaha lucu",  
                "pesan":"Makasih udah excited terus bang andraa, semoga abang sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abang ini diem2 kocak gitu ya kayanya",  
                "pesan":"makasih udah dampingi bandalm latihan terus bang bryannnn"# 1
            },
             {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124",
                "umur": "...",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "....",
                "kesan": "....",  
                "pesan":"Semangattt bang bangg jadi pj game nyaaa hihi"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kaka ini lucuu n imup",  
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
                "kesan": "Kak caca humble dan asikk",  
                "pesan":"Bahagia selalu kakakkk!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini agak kalemm yaa, tapi baikk",  
                "pesan":"semangat terus kuliahnya abanggg !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HdsPQEmwHDzA4-_v_CtfZAVAQ-7-Rp-4",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1HYWfmIn3bCntw40Dww4qn2G3mDecxIXJ",
            "https://drive.google.com/uc?export=view&id=1_qXAoBXJ2XsiloHr5Wq8f6UTMZBRqn-a",
            "https://drive.google.com/uc?export=view&id=1NAJ9DyVnee4cRQ1rYoaYAUMuuN1eOOYR",
            "https://drive.google.com/uc?export=view&id=1ww_jP4geuIKcBfHGHz1USyMe3HAkIbkD",
            "https://drive.google.com/uc?export=view&id=1OANYGffDMxpLbmPymmvD36B4JZQO7rk-",
            "https://drive.google.com/uc?export=view&id=1RieRGmdYfgvObYCWZteqGhVYnCo7-jm1",
            "https://drive.google.com/uc?export=view&id=1Lo8ieDxkAvKjqrCl9BlzmE1SJJrLEYTS",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1IRXQLlGr-wDymGsTh7fw-mPWS3u4jsHz",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1iluGTbzKp9AhVSE4NkMVEIncnif_t_L5",
            "https://drive.google.com/uc?export=view&id=1jgT_4klP2CGbAOhoYPlIiBBtQ8lZBvAg",
            "https://drive.google.com/uc?export=view&id=1KAUzC1cTVRxBB4FrQp_pjnINd7b-E23U",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1H5gMz9Nh5cnlDhhV5m1D47oHsc8XtGp4",
            "https://drive.google.com/uc?export=view&id=1CNUx3P7Tfnm-kPFW9PR1b8kd6ueV2NeB",
            "https://drive.google.com/uc?export=view&id=1XAPqAswqDDMJ56ezH3ohjGYrNiYy904E",
            "https://drive.google.com/uc?export=view&id=1gQEYEs0Kr6-VJK04MWQTVvQSl7Yfn8v8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=16_k4TLlJNoPg2fg3xgGJPCOWVavaZ_h5",
            "https://drive.google.com/uc?export=view&id=11xSlGz5Wbycd5T0Smv7Vn0HljEMqZynO",
            "https://drive.google.com/uc?export=view&id=1J6-KM20_X4JOJifP3bbcurSAlcqQW_kA",
            "https://drive.google.com/uc?export=view&id=15umQ11imTRB49YDtshcubKGQ5qRxx8Hp",
            "https://drive.google.com/uc?export=view&id=1NzD2kwQ_-TqxY7YAHWsjnwvaffCREu0N",
            "https://drive.google.com/uc?export=view&id=1IT3NoxnrA38cEbL9eaaqBHL9GtBHUKKL",
            "https://drive.google.com/uc?export=view&id=11xSlGz5Wbycd5T0Smv7Vn0HljEMqZynO",
            "https://drive.google.com/uc?export=view&id=1QXya5z1UZZHoLHUeXbqkf4iVRYNP50ve",
            "https://drive.google.com/uc?export=view&id=1mb9cnG59FhtyO52O5OAv2IfUHrtck16f",
            "https://drive.google.com/uc?export=view&id=1GZPivq-khQeF-9SgZUILhPm-gwTGjpRo",
            "https://drive.google.com/uc?export=view&id=1uBahgweg7JXHbvvTogL5GB0_54a0U2gu",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
                "kesan": "Kak arienta awalnya keliatan serem hihi, tapi ternyata baikkk",  
                "pesan":"Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk",  
                "pesan":"Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas tapi lama-lama saya ngerasa bang nobel jadi kaya bapak dari datavora",  
                "pesan":"Makasih banyak yaa bang udah jadi kadiv kader, saya beneran jadi banyak berubah jg karna dikaderr "# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi sangat enerjik apalagi kalo damaskusan hehe",  
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
                "pesan":"Semangat terus yaa bang ayake, semoga bahagia dan sehat selaluuuuu"# 1
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
                "pesan":"Sehat selalu dan sukses terusss bang caesaarr"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka ini terlihat asikkk (jujur)",  
                "pesan":"Semangat ya kakaa semester ini, semoga lancar terusss kuliahnya ^^"# 1
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
                "pesan":"Sehat selalu dan sukses terus ya bang haikalll"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Sering ketemu di warteg bahari, kakanya sangat ramah bintang 5",  
                "pesan":"Semangat terus kakaaa kuliahnya, semoga kapan kapan kita bisa makan warteg bareng ya kak hihi"# 1
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
                "kesan": "Abang ini humble",  
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
                "pesan":"Semangat dan sehat selaluu kakaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kaka ini suka nyanyi jugaa, baik, dan cantik mirip nagita slavina",  
                "pesan":"sehat sehat ka cacaa, semoga semester ini dilancarinn segala urusan kaka yaa"# 1
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
                "pesan":"Semangat terus abangg"
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
                "kesan": "Kakak imut dan lucuuuu",  
                "pesan":"sehat sehat dan lancar selalu kakaaa kuliahnyaaa^^"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
