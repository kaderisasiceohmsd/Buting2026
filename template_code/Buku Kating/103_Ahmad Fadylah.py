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
            "https://drive.google.com/uc?export=view&id=1xGPANYdh1va2y4_fUP0WdBnA1xDfB2Xb",
            "https://drive.google.com/uc?export=view&id=1CZuWR8cgBUVwATr1WrMIpsUfXDrh3N4b",
            "https://drive.google.com/uc?export=view&id=1rGKMfosDCQltl41Sz2ehjEUQV3LAaw8K",
            "https://drive.google.com/uc?export=view&id=1A9_GD_ng31Z0eTg1uvrwEUQFq-K-b4dL",
            "https://drive.google.com/uc?export=view&id=1fTovPjdfQCSGBXSg_viryFMm8yWEVGvc",
            "https://drive.google.com/uc?export=view&id=1bDcokqXsfus5IqecUG12RU9PS4ISZn4F",
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
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya asik dan ramah, penjelasannya juga mudah dipahami, jadi saya bisa lebih mengenal apa itu Kesekjenan.",  
                "pesan":"Semoga ke depannya selalu dilancarkan segala urusannya dan sukses terus, Bang!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya ramah dan baik, penjelasannya juga menambah wawasan saya tentang apa itu peran dan tugas dari Sekretaris.",  
                "pesan":"Semoga ke depannya selalu diberikan kelancaran dan bisa terus menjadi inspirasi bagi orang-orang di sekitarnya, Kak!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya soft gituu, keknya memang suka banget jadi sekre, dari bang qois saya jadi mengenal apa aja tugas dan peran dari sekretaris.",  
                "pesan":"Semoga kedepannya selalu diberikan kesehatan, kebahagiaan, dan kesuksesan. Semangat terus, ya baang!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya humble, dan seru banget , setiap penjelasan yang kakak berikan itu mudah di pahami",  
                "pesan":"Semoga kedepannya kak Hafsa selalu diberi kelancaran dalam segala hal, dan kesehatan ,terimakasih Kak!!"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia orangnya lucu banget, aktif, dan seruu, jadi yang disampaikan oleh kak lutfhia mudah dipahami.",  
                "pesan":"Semoga kedepannya kakak diberikan kelancaran dalam menjalankan amanahnya. Semangat terus, Kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y49NnwlsJgchox-dpAJ_oLGvCRVAKFny",
            "https://drive.google.com/uc?export=view&id=16930zRdf_dMA0Ypql4JHUAELHfN-RWd3",
            "https://drive.google.com/uc?export=view&id=1J7xzHS9TsMFtkhEE03EHuatKGs_5wMpI",
            "https://drive.google.com/uc?export=view&id=1CxT72HLkJ0nW_Bfna0MnoCstRvd2c1WS",
            "https://drive.google.com/uc?export=view&id=1_qgv0owpNP54PdE7Ig-_pV87dlFOaXCD",
            "https://drive.google.com/uc?export=view&id=1mHdZPK_B2QsTuNkAd9KyhztiYe_ZZPtJ",#bang givaro
            "https://drive.google.com/uc?export=view&id=1J4LYA1wkvGzxChY91Ycb9gViQ7dwkHnv",#kak nisa
            "https://drive.google.com/uc?export=view&id=12CQfaIZvka8FgAkJSjjt5bae_EDJhFEY",#kak hani
            "https://drive.google.com/uc?export=view&id=1J4LYA1wkvGzxChY91Ycb9gViQ7dwkHnv",
            "https://drive.google.com/uc?export=view&id=1kgGtDVpPBXi5zOC0Hxi01HeF7G3mgYvV",
            "https://drive.google.com/uc?export=view&id=1YfSz_QrQjcxUaSEn6_3_jjIc2swixEhg",
            "https://drive.google.com/uc?export=view&id=1BE4KMXJSuumEBg3HBV0IEpA5LuzYlmMO",
            "https://drive.google.com/uc?export=view&id=1g9zaiv_IYHB-1F64f9v0cengjHXZ_p0I",

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
                "kesan": "Bang Ridho orangnya asik banget, to the point dan penjelasan yang di kasih mudah dipahami",  
                "pesan":"Semoga kedepannya abang selalu diberi kelancaran dalam segala hal , dan diberi kesehatan, terimakasih bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak Jue orangnyaaa asik banget, lucuu, penyampaian tentang Balegnya juga mudah dipahami",  
                "pesan":"Semoga Kedepannya kak jue selalu diberi kelancaran dalam segala hal, dan juga selalu diberikan kesehatan, Terimakasih kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya asik banget, vibes-nya bikin betah belajar. Kalau ngajarin jangan bosen-bosen ya, Bang, soalnya ilmu dari bang dharu masih banyak yang mau fadyl serap,wkwkkwk.",
                "pesan": "Semangat terus kuliahnya, Bang! Semoga tugas lancar, nilai aman, dan rezeki mengalir deras. Jangan lupa bahagia bang!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael orangnya humble dan asik, auranya presidiumnya kenceng banget.",
                "pesan": "Semoga kuliahnya lancar terus, dan semoga diberi kesehatan dan kelancaran dalam segala hal ya Bang! "
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakaknya baik dan seru, jujur syok pas tau kakaknya orang palembang jugaa.",
                "pesan": "Semoga kuliahnya lancar terus, Kak! Semoga nanti saya bisa nyicip pempek buatan kakak :)"
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya asik, penjelasan yang bang givaro kasih jujur mudah banget dipahami",
                "pesan": "Semoga kuliahnya lancar, Bang! Semoga kopinya selalu enak, dompetnya selalu aman, dan hidupnya jauh dari deadline dadakan."
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya baik, humble, kenal kak nisa udah dari semester satu, kak nisa orangnya sangat sangat bertanggung jawab.",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya asik dan ramah. keliatan soft spoken banget",  
                "pesan":"Semoga kedepannya kak hani selalu diberi kesehatan dan kelancaran dalam segala hal yaa kak ."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Bang Jeremia orangnya asik, dan humble parah.",  
                "pesan":"Semoga Kedepannya Abang selalu diberikan kelancaran dan Kesehatan ya bang."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica orangnya murah senyum, baik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jona orangnya lucu paraaah, seruuu, dan juga suka sharing biskuat kalau abangnya lagi jadi operator.",  
                "pesan":"semangat terus kuliahnya bang, sehat selaluuu ya bang, SUKSEEES !!!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak Sekar orangnya baik banget, humble, dan tegas, tapi perhatian",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya seruuu asik dan humbleee banget.",  
                "pesan":"semangat terus kuliahnya kak, dan sehat selaluu ya kak."# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ouaPh_WXCa7L4UaB1zjcpW1GtpU4chkg",
            "https://drive.google.com/uc?export=view&id=1e3PpoxaPTy4Wbz0LRtD53S3C8y5R92gV",
            "https://drive.google.com/uc?export=view&id=1PcF4IYKT6uaflaYDQqiP2iUqzi5sfcQK",
            "https://drive.google.com/uc?export=view&id=1D_lia9zgl7mJ2WnrFajpgbxFc_bl7hwB",
            "https://drive.google.com/uc?export=view&id=1T0pBCaOoUGWePzplk23vzKIA_inZGs5S",
            "https://drive.google.com/uc?export=view&id=ILhw5Jw6OGFqR9JZXXGl6_ZH8q7EUk",
            "https://drive.google.com/uc?export=view&id=1dEarZTBT7jEC24kqQ9Lm2zPTdGr3ZkJ9",
            "https://drive.google.com/uc?export=view&id=1Q0bzo7yr0D8xh-RSlxK5cYCg8wEstMh",
            "https://drive.google.com/uc?export=view&id=1LFx7gMEf7keEm0HQUrqGsR_UfOJuqT8l",
            "https://drive.google.com/uc?export=view&id=1AnZyWjeehYZsmuiiUFgjlISXfiyn_DJI",
            "https://drive.google.com/uc?export=view&id=1cifStK5BxXbvoLmLc9fnqt_K5X2dOXHZ",
            "https://drive.google.com/uc?export=view&id=1-J_1seNxOKN-f5IbBCnSW9iLuwLis6hb",
            "https://drive.google.com/uc?export=view&id=1ccwodwWoFNGo-INHooISJQFw4TZXsDba",
            "https://drive.google.com/uc?export=view&id=1a7KIM--DVa1kPGydGNACbTyLa8tqJtlD",

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
                "kesan": "Bang Kevin orangnya asik dan lucuu parah.",  
                "pesan":"Semangat terus kuliahnya bangg, dan sehat selalu ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Ferazka orangnya lucuuu parah, dan selalu ngajakin muncak.",  
                "pesan":"semangat terus kuliahnya ya kak, dan semoga kita bisa muncak kak!!"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Bang Ali orangnya baik, seru dan soft spoken.",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kak Ayu orangnya baik dan humble parah".",  
                "pesan":"semangat terus kuliahnnya kak!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa orangnya baik dan asik banget.",  
                "pesan":"Semangat terus ya bang kuliahnya, dan sehat selalu ya bang, terimakasih bang"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kak nazwa orangnya baik dan soft spoken banget.",  
                "pesan":"Semoga kedepannya kakak diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang afdal orangnya lucu dan seruuu banget.",  
                "pesan":"Semangat terus ya bang kuliahnya, dan sehat selalu yaa bang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita orangnya lucu dan baik bangett",  
                "pesan":"Semoga kedepannya kakak diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan orangnya asik dan seru banget, my mentor badminton",  
                "pesan":"semangat terus kuliahnya ya bang !!!"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "BAng andra orangnya lucuu dan seruuu banget",  
                "pesan":"semangat terus kuliahnya yaa bang !!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan orangnya soft spoken dan humble banget",  
                "pesan":"semangat terus kuliahnya ya bangg !!!"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kak indah orangnya asik dan baik bangetttt",  
                "pesan":"semangat terus kuliahnya yaa kak!!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
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
                "kesan": "Bang rafka orangnya baik dan humble banget",  
                "pesan":"semangat terus kuliahnya Bang !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bT1YM9F8WpmBeKP4Yx8pDr8zcCRV14MW",
            "https://drive.google.com/uc?export=view&id=1-FVJcb8_s8YJkq0HkBEhFPGBGQ8xiFub",
            "https://drive.google.com/uc?export=view&id=1F1tFv0fBId9--MGUNvmwrk5nhXVnyuV6",
            "https://drive.google.com/uc?export=view&id=1zBjX3AOuFcsYpyC7OmsMrS_DNRdHPn4v",
            "https://drive.google.com/uc?export=view&id=1ylTjx1jMS2BJyV8LyAIq6eVG9LCLmIg_",
            "https://drive.google.com/uc?export=view&id=1pKnivmS6dH15FFVn3Z9JcJ5QKrtPWTUQ",
            "https://drive.google.com/uc?export=view&id=1TmY6If5h8WyzZgC4llSji1hBn3fSMw97",
            "https://drive.google.com/uc?export=view&id=1LDCbYlttrvSsD_S2r_hAZx67wIvmFvaG",
            "https://drive.google.com/uc?export=view&id=1I0nKh6on9ACRXN2C8OKNB9jwZ3m7E6C_",
            "https://drive.google.com/uc?export=view&id=1d6gIZBL2tLcrKL1BQ0NCLhy2qPRBe8Vj",
            "https://drive.google.com/uc?export=view&id=1bf3h2uGnF2fGb0lhUeMY0ye1DAjut1yh",
            "https://drive.google.com/uc?export=view&id=1myaxcbsKW-_umtwNqzj6bMQAZZVAkQvQ",
            "https://drive.google.com/uc?export=view&id=1GrntdlPBAPoSx_avKHNYakeCVVZ81xml",
            "https://drive.google.com/uc?export=view&id=1wMtEtv90vd06zGpKYmxp-IyF8ANCDEc5",
            "https://drive.google.com/uc?export=view&id=1Cb7ZhFT1e5XbQw6eTcp6to0qdLB_UcKx",
            "https://drive.google.com/uc?export=view&id=1A9W8r_xJLH7wRQZZ9L1356eXscr3a0_4",

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
                "kesan": "Bang haikal orangnya seruu banget.",  
                "pesan":"Semoga kedepannya bang haikal diberi kelancaran dalam segala hal."# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak Kharisma lucuu, baikk, dan juga ramah paraaah",  
                "pesan":"Semoga kak kharisma selalu dikelilingi dengan orang baik"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna seru, baikk, lucu ",  
                "pesan":"Semoga semua yang kak hanna inginkan semuanyaa tercapaii, aamiin"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren, selalu keren pas damaskus",  
                "pesan":"Semoga bang farhan selalu diberi kelancaran dan kesehatan"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak Aisyah orangnya lucuuu, dan juga asikkk sekali",  
                "pesan":"Semoga semua apa yang kakak lakuin sekarang dan nanti diberi kelancaran"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal":"....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Kak Cerine orangnya sangat asikk, humble, dan juga baikk banget",  
                "pesan":"Semoga kak cerine selalu dikelilingi orang orang baikk"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya orangnya keren, baikk, dan seru",  
                "pesan":"Semoga bang jaya diberi kesehatan dan kelancaran dalam segala hal# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kak Najla orangnya baikk, dan juga ramah sekalii",  
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
                "kesan": "Bang Rozak orangnya asik sihh, dan juga murah senyuum",  
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
                "kesan": "Kak Teresa orangnya lucuu, baikk, dan juga ramahh",  
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
                "kesan": "Bang Hanif orangnya baikk, dan juga asikk",  
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
                "kesan": "Kak orangnya Audina lucuu, baikk, dan juga sangat amat ramah",  
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
                "kesan": "Kak Cika orangnya lucuu, baikk, dan juga asikk",  
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
                "kesan": "Kak Gustin orangnya lucuu, baikk, dan juga ramahh",  
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
                "kesan": "Bang Harvin orangnya baiikk , dan soft spoken",  
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
                "kesan": "Kak Sabina orangnya baikk, dan juga sangat ramahh",  
                "pesan":"Semoga kak sabina mendapatkan hal-hal baik teruss"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lIzS74rle4qjVfzhxdgfVNIKjlmETJ_s",
            "https://drive.google.com/uc?export=view&id=1xJ5HsRnxSw74bwoTl2KkIo3MYDerSn4j",
            "https://drive.google.com/uc?export=view&id=13AfDTj6E-wTS76FLp7ZBj42t76KHOfaf",
            "https://drive.google.com/uc?export=view&id=1yGnS0XAtp0dOuYf8nylWcI1eskKpiW6l",
            "https://drive.google.com/uc?export=view&id=1ZytisXJYU7txYU1J7qoPI6VkBDyC4dVX",
            "https://drive.google.com/uc?export=view&id=1R325O4wtuzavloL9bwjUXHE8O7GsMimK",
            "https://drive.google.com/uc?export=view&id=1bb9jPqQ_FlNDOV60Y6s29AT6j9qBBPMi",
            "https://drive.google.com/uc?export=view&id=1wYC5zY_lTSJqO36bauZT9eTvWzy9Fpvg",
            "https://drive.google.com/uc?export=view&id=1BV5lebBanBUnVvrISrfbznmwjOytmPvD",
            "https://drive.google.com/uc?export=view&id=1s2s0fYbCVIpmV7V-9wazL4iS5EeMyn4c",
            "https://drive.google.com/uc?export=view&id=1f5nhmESP5YRRftXYsj8II0EXNMO0NddK",
            "https://drive.google.com/uc?export=view&id=1SoEbXjn1veyzIeor7bXY4zSyFuHF0fUG",
            "https://drive.google.com/uc?export=view&id=1c2c9ZL2C1It7269sQCry1Femrj9WOzf7",
            "https://drive.google.com/uc?export=view&id=1nint9s3ptTAPbJhWEhUJFwCbQkUhD0rZ",
            "https://drive.google.com/uc?export=view&id=1PpXAW5E9hjFsi2qqzt65QVCG2R1KXhTO",
            "https://drive.google.com/uc?export=view&id=1AtP5O1H1g5KF9SKEO0e91kamQFccayyn",
            "https://drive.google.com/uc?export=view&id=1d68jdST1atxpWas85Rr4Ii6F3bp0uxhu",
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
                "kesan": "Kak Arienta orangnya baik, dan juga ramahh",  
                "pesan":"Semoga semua keinginan kak arienta sgera tercapai"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany orangnya humble, dan baik juga",  
                "pesan":"Semoga kak vany mencapai semua keinginannya secepatnya, salam dari orang sesama palembang"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel orangnya kerenn, Tegas,dan juga baiik",  
                "pesan":"Semoga bang nobel selalu diberi kelancaran dan kesehatan dalam segala hal."# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi orangnya kerenn, to the point dan juga baikk",  
                "pesan":"Semoga semua keinginan bang azmi cepat tercapaii"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang Ayake orangnyaa humble , kerenn, Tegas dan baikk",  
                "pesan":"Semoga bang ayake diberi kelancaran dalam segala hal dan semoga selalu diberi kesehatan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar orangnya kereen, Tegas dan Humble",  
                "pesan":"Semoga bang caesar diberi kesehatan dan kelancaran"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Euodia orangnya seru, Tegas , dan juga baikk,",  
                "pesan":"Semoga kak euodia selalu didekatkan hal-hal baikk"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal orangnya kerenn, Tegas ,baikk, dan juga ramahh",  
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
                "kesan": "Kak Putri orangnya baikk, humble dan juga ramah",  
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
                "kesan": "Kak Queenta orangnya baik, humble, dan perhatian",  
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
                "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk",  
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
                "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
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
                "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
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
                "kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
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
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
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
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
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
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

# Tambahkan menu lainnya sesuai kebutuhan
