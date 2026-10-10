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
            "https://drive.google.com/uc?export=view&id=1z-9R-TWHSXeOUNKdDyWvIZVkur2QQLIo",
            "https://drive.google.com/uc?export=view&id=1gNeqpCK5iwwT4W3MONVk-SG_aCy_Pb_N",
            "https://drive.google.com/uc?export=view&id=1PEspklJKSdYAwIBwwPu_dOE1z-G6kmKJ",
            "https://drive.google.com/uc?export=view&id=1er7nIAMXGdKagngyWjh6JOCAmD_A3z0-",
            "https://drive.google.com/uc?export=view&id=1XVBX82MB4QACh8LE2gopBt4D_jILJbHx",
            "https://drive.google.com/uc?export=view&id=1XVBX82MB4QACh8LE2gopBt4D_jILJbHx",
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
                "kesan": "Bang Fajar orangnya keren dan menginspirasi.",  
                "pesan":"Semoga dilancarkan perkulihannya dan bisa lulus tepat waktu"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil ternyata orangnya asik dan suka ngelawak kirain orangnya selalu serius",  
                "pesan":"Semangat bang ngerjainnya TA-nya"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya kaya pendiam gitu tapi kakak cantik poll",  
                "pesan":"Semangat kak dalam berjuang untuk mencapai cita-cita yang diimpikan"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois lucu dn gemas.",  
                "pesan":"Jangan lupa untuk jaga kesehatan ya bang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa cantik banget,vibenya mirip anak kedokteran.",  
                "pesan":"Semoga kakak selalu dikelilingi orang-orang baik"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakak aktif banget buat bercerita.",  
                "pesan":"Semangat kak kuliahnya dan ngerjain TA-nya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jHCbyWhI87We4Y6iqxLFVD-fK0M22kx4",
            "https://drive.google.com/uc?export=view&id=1GPVZdBavUVMiaLMqS-OViuH_7w3Rmy_n",
            "https://drive.google.com/uc?export=view&id=1bP5Am-t5Q4fe-1mehqVUsOWOTc3Uerq0",
            "https://drive.google.com/uc?export=view&id=16TXy_08cjID1olUzU7srgoHaB8XPAUIU",
            "https://drive.google.com/uc?export=view&id=1dOH-rA6tCltYvGc9_xWojYePOElGABTj",
            "https://drive.google.com/uc?export=view&id=1YNHXiOtRjXvZd0ZF7n_k8vCRPSil-bKA",
            "https://drive.google.com/uc?export=view&id=1Rwy2XDRXCnqWBxfI8C4Av2mH_68_bocp",
            "https://drive.google.com/uc?export=view&id=1BeueaDTKrLW_3sdLRp5J4HGMPnq-eJd1",
            "https://drive.google.com/uc?export=view&id=1LVWe_OTwaJLf4c29x0sC2WE2lwZcSDCu",
            "https://drive.google.com/uc?export=view&id=1HqW-rlo4dn7dixNLHIabvL6p8nANHbNu",
            "https://drive.google.com/uc?export=view&id=1DRLxKw3_cc02n4GwDXEHS65ik6ZmhQre",
            "https://drive.google.com/uc?export=view&id=12ojq3lGraOFuiujacSBOmmObJfTIcGLb",
            "https://drive.google.com/uc?export=view&id=1oP8qyyZ5jzlcQSGslfx1I54bWtb4nNr1",

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
                "kesan": "bang ridho hobi ngelawak .",  
                "pesan":"jangan lupa untuk selalu mengandalkan Tuhan"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kak jue cewe kue banget dan suka vibe yang cerianya",  
                "pesan":"jangan lupa untuk selalu tersenyum ya kakk"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Kakak ini pinter sekalii",  
                "pesan":"tipsnya dong kak supaya bisa jadi mapress"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "bang mikael ini vibenya cowo cool.",  
                "pesan":"Semoga kedepannya makin banyak duit"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "kak siti keren .",  
                "pesan":"lancar selalu dan dipermudahkan segala urusan kedepannya kak"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "awalnya ngira bang givaro ini cuek gitu ternya orangnya humble.",  
                "pesan":"semangat kuliahnya bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "kakak ini styel nya keren.",  
                "pesan":"Semoga ipknya bagus terus"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "kakak hani orangnya baik dan ramah.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "bang jeremia asik untuk diajak ngobrol",  
                "pesan":"jangan lupa untuk bahagia"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica cewe keren dan mandiri gitu",  
                "pesan":"tetap semangat kak walaupun menghadapi dunia yg kedebag debug"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Kakak ini asik ",  
                "pesan":"semangat dan semoga dilancarkan perkuliahannya"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "awalnya ngira kakak ini judes gitu ternyata baik dan perhatian",  
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
                "kesan": "ketemu pertama kali di pplk dan kakak ini cantik",  
                "pesan":"semangat terus dalam menjalani hari-harinya"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1akEiXCyio6gObJYV5j_B69PGSAMhClQG",
            "https://drive.google.com/uc?export=view&id=1Gwra7CQKKZQQQM8ps8exnHRKA8KrkFpY",
            "https://drive.google.com/uc?export=view&id=1dQndxwQvwfXOCWc1ZbEV8J1wzPYBC6GT",
            "https://drive.google.com/uc?export=view&id=1Et49rDUOS6jfMigW62A2cw7EvxhjomYS",
            "https://drive.google.com/uc?export=view&id=1KyVGG4b8rg9-5Cb6kiqICsdYaGu12AiM",
            "https://drive.google.com/uc?export=view&id=13sypm68-wONblDXgADwSJw2gu2jCnHqG",
            "https://drive.google.com/uc?export=view&id=1DG-qgMksMoEL13WKKjqmo8eQEu3jK4Mo",
            "https://drive.google.com/uc?export=view&id=11dI7wIZZo0-rFrAfbsWzEtxQBYXGAveC",
            "https://drive.google.com/uc?export=view&id=1U64WgcwWbjzMrLvcNIS5p59c_fWKJUND",
            "https://drive.google.com/uc?export=view&id=1r0bdrFzzwp_25t2NhGePwrTrCFIUrfvF",
            "https://drive.google.com/uc?export=view&id=1qcl6T73S06cQyMRUB8ywpAncaAtrxi-E",
            "https://drive.google.com/uc?export=view&id=12v8-cD8_xdk1ZsHQ395mEe81ha0LokTc",
            "https://drive.google.com/uc?export=view&id=1R8fTQFalcFfZf1RBHoYii35uIP4yp5Z1",
            "https://drive.google.com/uc?export=view&id=1EFZLyD2-XnMcjx_Q0DFZORQSF2AvXMq2",
            "https://drive.google.com/uc?export=view&id=1KbXsxCSh4DOdYorCnvtZ3uepbD2dKVA-",

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
                "kesan": "awal ketemu bang kevin agak segan karena tipe wajahnya kaya galak gitu.",  
                "pesan":"jangan lupa untu senyum setiap harinya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik,ceria,humble",  
                "pesan":"semangat ngerjain TA-nya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "abang ini baik dan mudah untuk berbaur",  
                "pesan":"semoga abang selalu dikelilingi oleh hal-hal baik"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "kakak ini serruu.",  
                "pesan":"jangan keseringan begadang"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang dafa rambutnya tuing-tuing.",  
                "pesan":"jangan lupa untuk jaga kesehatan"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lihat Bila Nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "kakak humble sekalii.",  
                "pesan":"Dilancarkan rejeki kakaknyaa"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "bang afdal lucu dan menggemaskan.",  
                "pesan":"Semoga abangnya sukses selalu"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "kak salsabila orangnya baik,ramah,dan mudah berbaur.",  
                "pesan":"semoga segala hal yang sedang kakak kerjakan membuahkan hasil yang baik"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "bang ridwan orangnya baik dan asikk",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "bang andra orangnya perhatian",  
                "pesan":"semoga hal-hal baik yg abang berikan bisa kembali ke kakak"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abang ini lucu sekali,melawak tapi ekspresinya datar",  
                "pesan":"jangan lupa untuk mengandalkan Tuhan"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "",  
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

# Tambahkan menu lainnya sesuai kebutuhan
