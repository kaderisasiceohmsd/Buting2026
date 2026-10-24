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
            "https://drive.google.com/uc?export=view&id=1yTQXcTH83raL-W2XrWy0rk1pWtkvPfnN",
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
                "nama": "Luthfia Laila Ramadhani",
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
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal":"Surabaya ",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya keren banget, pasti punya kebon sawit berhektar-hektar",
                "pesan": "OTW jadi CEO SAWIT!!! semangat menjalankan tugas di minbak, "# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik dan menggemaskan",
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri ",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "pertama kali liat kakak ini waktu tampil nari dan tariannya baguss sekali",
                "pesan": "semangat buat terus nari kak, ajarin aku buat lenturin tubuh alias nari"# 1
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

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10THDRFrASaZqfU7CMYPD6d2dulx--dKu",
            "https://drive.google.com/uc?export=view&id=1CAb_i33T70AAWRL0nj2Jgs0Qvyap7vYc",
            "https://drive.google.com/uc?export=view&id=1ZyfKgosUnJ8muHjG4-AczNan6dZxhjwt",
            "https://drive.google.com/uc?export=view&id=1nJYJJ9nqDlAqBcLyhOh0yLEdNKvajxJg",
            "https://drive.google.com/uc?export=view&id=1rP5vrYd98QjzT1HQG22GOh5g_uTqN5sN",
            "https://drive.google.com/uc?export=view&id=1JktHBHab4vyJgKjVmMNMBIhUaC6KXYfE",
            "https://drive.google.com/uc?export=view&id=1-MNpbJ5_hbhhr9yc2cDmQi_DTCGbUYD0",
            "https://drive.google.com/uc?export=view&id=1-go5r3IetELJcyNLR7hvMqOc2pt5PTHL",
            "https://drive.google.com/uc?export=view&id=1pWnpamlFT_hmAND2uxT2v7PcExhkiIJn",
            "https://drive.google.com/uc?export=view&id=1FqD2cjM4FPwp3m3oRuyL63J8oHv2S4rk",
            "https://drive.google.com/uc?export=view&id=1diY1o8sNPJIa7CNDmUVImjqZdMda56mR",
            "https://drive.google.com/uc?export=view&id=1Rk51cdfbm-vyqwxWoCCNfrjwkG-9qLkV",
            "https://drive.google.com/uc?export=view&id=1pmvMlWsT65oISgRsYqGXHdpomdmtOhKb",
            "https://drive.google.com/uc?export=view&id=1ROYDtighL4KSBYtFUe_pZlItg5A0Txt6",
            "https://drive.google.com/uc?export=view&id=1VEVusLuXldZJVHsAkXIOZkPoY80rESJ8",
            "https://drive.google.com/uc?export=view&id=13s9gdpC8KrM3thOLnWmzQw2sk-WOKjG0",

        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "bang haikal orangnya asik sekali dan jokesnya ituloh yang buat lucu.",
                "pesan":"jangan kebanyakan merokok bang"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini cantik sekali dan vibenya seperti bungaa matahari",
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
                "kesan": "Kakak ini ekstrovet sekali dan senyumnya ituloh manis bangett",
                "pesan":"semoga kakak selalu dikelilingi hal-hal yang bisa membuat kakak bahgia selalu"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Farhan orangnya keren sekali apalagi saat damaskusan.",
                "pesan":"semoga ipknya bagus terus"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Kak aisyah orangnya mudah untuk berbaur.",
                "pesan":"semangat dalam menggapai cita-citanya kak"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "orangnya lucu banget apa lagi waktu dia manggil aku hey polkadot karna baju aku.",
                "pesan": "tetep ceria ya kak"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang jaya orangnya baik dan perhatian.",
                "pesan":"jangan lupa untuk selalu mengandalkan Tuhan didalam kehidupan"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "kakaknya cantik dan cute.",
                "pesan": "Semangat kuliahnya mengejar sampai ujung dunia"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri",
                "hobbi": "Isengin Harvin di kelas",
                "sosmed": "@rozakramdani_",
                "kesan": "abang ini lucu dan humble",
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak ini cantik,gemes,dan seru jika diajak bercerita",
                "pesan":"semoga lulus tepat waktu kkak"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "abang ini kalem dan baikk",
                "pesan":"semoga abang lulus tepat waktu"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "kakak audiana baik,lucu,dan vibenya kalem",
                "pesan":"semangat dalam menjalani hari-harinya kak"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakak ini asik dan ramah",
                "pesan":"jangan lupa untuk selalu mengandalkan Tuhan ya kak"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara ",
                "alamat": "airan",
                "hobbi": "nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakak lucu dan cute bangettt",
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "abang harvin humble dan seruu",
                "pesan":"semoga dipermudahkan jalannya untuk menggapai cita-citanya"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nginep di rumah kak yolannda",
                "sosmed": "@snasha",
                "kesan": "Kakak ini ini lembut sekali kalau ngomong dan ramah",
                "pesan":"semangat terus kuliahnya kak sabina"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aIPkY8AF7WO-83F42t0ObAUKq0MVGZbz",
            "https://drive.google.com/uc?export=view&id=16Qjj4a96uEbkJURI7sr2_4qhiZJTtcOP",
            "https://drive.google.com/uc?export=view&id=1DQ9D9Zl8HyyBhuvFvLGA4F5rqQEcXEdJ",
            "https://drive.google.com/uc?export=view&id=1FMdt6nb1tNAZS0KqDtf0ISL362lfMQI_",
            "https://drive.google.com/uc?export=view&id=19yLqriA3gqUPQP-6X5eoGq3EcgA3Hvvm",
            "https://drive.google.com/uc?export=view&id=1KHG6UvjsLMd1eSDr9ypWxNAEEwjKhomD",
            "https://drive.google.com/uc?export=view&id=1O5phrPaE--O2V4L0Q_8ITi54Tt9N2FPK",
            "https://drive.google.com/uc?export=view&id=16Q2F5W_yb67pksp-DT_g03K7sfGBVR6O",
            "https://drive.google.com/uc?export=view&id=1fsueztCDBKHODPctbSsTQtguauJAVWEe",
            "https://drive.google.com/uc?export=view&id=1xUPHvyBd_HD6DZcYMtRPMYoHvhl1LdY-",
            "https://drive.google.com/uc?export=view&id=1kpnllCdWLJvq65vVyjbldWMNBCdXRZEE",
            "https://drive.google.com/uc?export=view&id=1jQzdp_D_LSMWSu6Ruxe1B9yojnDI0Y9Y",
            "https://drive.google.com/uc?export=view&id=1vwQmnp3iG5GTvkQTtZONgF3Yv0XQw5Wo",
            "https://drive.google.com/uc?export=view&id=1JaUCzPIl2__IDRvzhJPUHMgAsL8alFx3",
            "https://drive.google.com/uc?export=view&id=15rKHkYilFNe6jJGb1lZW1oCP87Wrqjt5",
            "https://drive.google.com/uc?export=view&id=1ltmhZVKc_L-vLrJ9A1OmzYNaZ4PVSJ2b",
            "https://drive.google.com/uc?export=view&id=1-nO-zcd88D45tFSPA9I4JdYOX3o4SMak",


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
                "kesan": "suka ngeliat kak arienta senyum karena senyumnya maniss",
                "pesan":"jangan lupa untuk jaga kesehatan ya kak"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakak vany awalnya ku kira judes tapi ternyata orangnya ramah dan baik ",
                "pesan":"semoga ipknya selalu bagus ya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "bang nobel ternyata jago sulap",
                "pesan":"tipsnya dong bang supaya bisa sulap"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "bang azmi orangnya tuh baik",
                "pesan":"semangat bang kuliahnyaa"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "bang ayake serem kali waktu awal ketemu tapi dibalik itu abang ini perhatian ",
                "pesan":"semangat bang dalam mencapai cita-citanya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "abang ini kalau senyum manis",
                "pesan":"semoga selalu diberikan kebahagian"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "pertama kenal kakak ini di pplk 2025  dan awal ketemu memang agak takut kena marah tapi dibalik itu kakak ini baik",
                "pesan":"semoga sehat selalu"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "bang haikal orangnya kelihatan serius",
                "pesan":"suskse terus buat kedepannya"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "Jalan kaki ga boleh naik motor",
                "sosmed": "@putrimannaa",
                "kesan": "kak putri ramah dan perhatian",
                "pesan":"semoga dapat pekerjaan dengan gaji 3 digit"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "awalnya ngira kakak ini dari wajahnya judes gitu tapi engga kok malahan baik ",
                "pesan":"semoga selalu dikelilingi dengan orang-orang baik"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main Musik",
                "sosmed": "@dsmanhal",
                "kesan": "abang ini kelihatan seperti orang dewasa",
                "pesan":"jangan lupa untuk berdoa"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya cantik dan manis",
                "pesan":"semangat kuliahnya kak"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrln",
                "kesan": "kak charrlindah vibenya cewe badas",
                "pesan":"semoga hari-hari kakak penuh dengan cerita baik"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "bang jeremi tipe orang yang serius dan ngelawak",
                "pesan":"semoga semakin sukses kedepannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakak ini cantik dan pengertian",
                "pesan":"jangan lupa jaga kesehatan"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "abang ini baik dan seruu",
                "pesan":"semoga cita-citanya tercapai"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "kakak ini baik dan ramah",
                "pesan":"semoga lulus tepat waktu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()

    elif menu == "Senator":
    def DepartemenSenator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CLViWe4r6l6emrCXK15RYzeoK7iw2wLG",
            "https://drive.google.com/uc?export=view&id=1J5bHQdyVZn4DFX-_J5yaNcKzSQYb4DHd",#helmy
            "https://drive.google.com/uc?export=view&id=1GZUoRqQJVI1cxCf9BlpsQIhmFyJsPLWR",
            "https://drive.google.com/uc?export=view&id=1r_eTZMxr1Rjhbi_xF6e5AH-7e7qImz2Q",
            "https://drive.google.com/uc?export=view&id=1NFEXtIVt6XbztKwM4r_MTJ5Aab1r_vyL",
            "https://drive.google.com/uc?export=view&id=1xfvy139vk_b95Rd5KYbmIYXW53xPq5Cz",
            "https://drive.google.com/uc?export=view&id=1dZ9oY-kKidfs2nvUh5rjdIzAw6dj2SYB",
            "https://drive.google.com/uc?export=view&id=1hdNg75BBub-ZqisWNSHVJ6fEAYTN1isV",
            "https://drive.google.com/uc?export=view&id=1P9lrqHXCQ5KFuLyusF69DlknujcImQ_3",
            "https://drive.google.com/uc?export=view&id=10d5eSd-icmBBqJGvsL4p72lxXcmziOHd",
       ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta ",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kak azizah orangnya seru bangett",
                "pesan": "Makasih kak atas penjelasan materi tentang Kesenatoran, Semangat kuliahnya kak!!."# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal":"Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Nemenin Wielman MC",
                "sosmed": "@barus.fernando",
                "kesan": "Bang fernando keren banget, hobinya sangat menyenangkan sepertinyaa",
                "pesan": "Semangat buat selalu nemenin bang wielman nge-MC"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru ",
                "hobbi": "Baca",
                "sosmed": "@sciia__",
                "kesan": "kaa suci orangnya asik banget omgggg, keren deh",
                "pesan": "Semangat terus kaka kuliahnya, dan selalu jadi MC ya kak karna asik banget bawainnya"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "jadi MC",
                "sosmed": "@wielhawn",
                "kesan": "Terpukau sama nada MC yang nge-MC banget keren sihhh bang omggg",
                "pesan": "Jangan sampai suara emasnya hilang bang!!!!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "main hp",
                "sosmed": "@lia.h_264",
                "kesan": "Aku suka banget ngeliat kakak pas bawain materi",
                "pesan": "Semangat kuliahnya kak!! terbang setinggi mungkin"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Mentor bayesmup yang sering ketawa, dan identik dengan bunga mataharinya",
                "pesan": "Semangat buat jadi mentornya kakkk, dan tetap ceriaaa"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "jadi sekjen",
                "sosmed": "@hazelhandhaka",
                "kesan": "keren banget waktu jadi ketuplak",
                "pesan": "Semangat kuliahnya bang!!!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                 "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya cute, cantik",
                "pesan": "semoga hal-hal baik akan selalu datang ke kak nadya"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani ",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang ",
                "alamat": "Jl. Lapas",
                "hobbi": "nonton film,musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakanya humble, cantik dan senyumnya manis",
                "pesan": "semangat kuliahnya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSenator()

elif menu == "Departemen Eksternal":
    def DepartemenEksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NYiGmSercqTHVEhOlDOFoYKiBlJlz6OV",
            "https://drive.google.com/uc?export=view&id=1MoV27g5Rj3f_BBegLoMXOc5isEKX0fn9",
            "https://drive.google.com/uc?export=view&id=1bmCfdrLOOS7kXSaeuT7EAswC79Nd20fJ",
            "https://drive.google.com/uc?export=view&id=1OQgqZut7ttlzjhpvDEgHEfao_jNNs_W1",#Fathya
            "https://drive.google.com/uc?export=view&id=11SAoRAf7pEGj2BydsXvBlAf9gVHo5KJP",
            "https://drive.google.com/uc?export=view&id=1X7T2yckm9LnHgAe6MRdHiZIUSIrZhpYi",
            "https://drive.google.com/uc?export=view&id=1-AxKHQ4k377zpEq2YfWncdL9bVylmLBK",
            "https://drive.google.com/uc?export=view&id=17_-7-ebHA-RxAJNc00Xtemf32v5WbKDi",
            "https://drive.google.com/uc?export=view&id=10Uw7gdK6hQ97-m4P_BBz2irolfHEJlVP",
            "https://drive.google.com/uc?export=view&id=14rc20GI-JfvWM4tn5O-08WJgerRR9zNn",
            "https://drive.google.com/uc?export=view&id=1qc8GQETcntSsYKsLdXk727G9J7Ia3B9r",
            "https://drive.google.com/uc?export=view&id=1rXV5iY3LykiLoeTcioyRI3xo2YnbwO2p",
            "https://drive.google.com/uc?export=view&id=1pXl2E4LCIqFDYT42B4RNXUgnuoahNi4j",
            "https://drive.google.com/uc?export=view&id=1-oLIbLMy95icoDgl07oN9FKWthV0ASZI",
            "https://drive.google.com/uc?export=view&id=1P9K2QuT2YFo-RFtNs03M9l07jypeLjV1",
            "https://drive.google.com/uc?export=view&id=1kFttXgpLpK3ta2tyY9d5l2AG14UnA7bq",
            "https://drive.google.com/uc?export=view&id=1ibW9MmhplSRKniRBSA5rw-6uYBP2qdw8",
            "https://drive.google.com/uc?export=view&id=1wJBuhKaDdz0SreXmUmehSb8JrR-r74xC",
            "https://drive.google.com/uc?export=view&id=1NiJ5B5HFIANOWzbUJ5qNbZplpymEWI7Y",
            "https://drive.google.com/uc?export=view&id=1N8pbZceeU6LpjEQciM468NgnihZncC9Q",
            "https://drive.google.com/uc?export=view&id=1JWhUk_dXMvbE33Zf64NvXUg5N4q5Pro6",
            "https://drive.google.com/uc?export=view&id=1qc8GQETcntSsYKsLdXk727G9J7Ia3B9r",

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
                "kesan": "ngeliat kak arini tuh kawa wanita carier banget",
                "pesan": "Semangat dan semoga lancar TA nyaa "# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya manis banget suka ngeliatnyaaa",
                "pesan": "always senyum yaa kaa"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "orangnya seruuu banget apa lagi kalo di ajakin gibahh omgg",
                "pesan": "cerita yang waktu itu belom kelar bang, esok kalo ketemu lanjutkan ceritanya"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal":"Tanggerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kak fathya ceria banget orangnya omggg sukaa",
                "pesan": "semangat menjalani hari-harinya kakk"# 1
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                 "nim": "123450052",
                "umur": "-",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "tari_",
                "kesan": "kakanya baik, ramah jugaa",
                "pesan": "semangat menjali semester akhirnya kak"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "kakanya lucu , ramah dan gemass",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "20",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "baru tau kalo bang danil ternyata yang masuk ITERA ganteng itu tohhh",
                "pesan": "semoga ikan cupangnya sehat ya bangg"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "makasih bang yang selalu gercep kalo ada yang sakit selama rangkaian",
                "pesan": "semoga selalu bahagia dan ayo badmin lagi bangg"# 1
            },
            {
               "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "((15≪1) & 31) ⊕ 10",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "aku kira orangnya galak, ternyata asik juga kalo lagi ngobrol dan ternyata anak smanda",
                "pesan": "rajin-rajin pulang yuk banggg"# 1
            },
            {
               "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah ",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "tanyain sama yuder",
                "sosmed": "@jaldii._",
                "kesan": "orangnya asikk banget dan ada aja yang dibuat lelucon",
                "pesan": "semangat mc nya banggg"# 1
            },
            {
               "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kaknya cantik, lucu dan ramahh",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
             {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "kakanya cantik dan senyumnya maniss",
                "pesan": "semangat kuliahnya kak selma"# 1
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kak mut lucu dan gemass, keren banget sihh bisa lolos pimnas",
                "pesan": "semangat pimnasnya semoga menang ya kakkk"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                 "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "keren bang ahmad dengan segala prestasinya",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "makasih kak dah bantu kallo sakit selama rangkaian, seneng bisa kenal di hublu juga",
                "pesan": "energinya jangan pernah habis ya kak buat selalu heboh, tetap semangat untuk Kakak dalam menyelesaikan tugas"# 1
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung ",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "jujur serem liat bang abim waktu di kotbar karna mukanya serius banget dan aku ga terlalu jelas ngeliatnya",
                "pesan": "makasih bang atas ilmu yang di beri saat magang hublu"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus ",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "hobinya sangat keren sihh bang, pasti mau bangun claster yaaa",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "21",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "kakanya cantik banget suka ngeliatnyaaa omgg",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "mentor yang baik dan ceriaa bangettt",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                 "umur": "20",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "pertama kenal waktu jadi asprak alpro, ternyata lanjut jadi mentor kesayangan tensor",
                "pesan": "makasih kak udah perhatian ke tensor, dah mau dengerin cerita keluh kesah ku dan kasih saran yang terbaik, dan banyak hal lagi yang ga bisa ku unggkapkan lewat kata-kata kakk"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "hobbinya sangat mengundang semut sih itu bang",
                "pesan": "Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kak mei cantik banget suka ngeliatnyaa omgg, baik hati banget lagi",
                "pesan": "semoga selalu bahagia dan ceria ya kakk, Tetap semangat untuk Kakak dalam menyelesaikan tugas"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenEksternal()

   elif menu == "Departemen MIKFES":
    def DepartemenMIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rjv6opjEN77uleywdpteJ3tzaTRx7Tis",
            "https://drive.google.com/uc?export=view&id=1nzotmd-SPb7zbNeRAzlsV0Pd8OvVyoy1",
            "https://drive.google.com/uc?export=view&id=",#fadil prasetyo
            "https://drive.google.com/uc?export=view&id=19YLqgazXlru2QJgj9ax0owM5SlE83jTN",
            "https://drive.google.com/uc?export=view&id=1GL1T3S5rvdxWYLSpsOTfbr33tgDBCFXM",#ni made
            "https://drive.google.com/uc?export=view&id=1O_WS2vm8L4v1eXCAx3ZiWgTbGix86Bgi",
            "https://drive.google.com/uc?export=view&id=1IgMZCqOPRcRB_4KYoIKXYiPOItFOmWyj",
            "https://drive.google.com/uc?export=view&id=1IewPM24X6bBleKFmv92lZbUhJ64O8i9c",#yulia
            "https://drive.google.com/uc?export=view&id=1DJF-WbNRH2U-pA27E_c5IviCXr_EAoCJ",
            "https://drive.google.com/uc?export=view&id=1wZLTWDnvNNmxjgpKYfEVHHVQvzBNB-IT",
            "https://drive.google.com/uc?export=view&id=1zf9fBYENg6M4lE5BlekU7oOCw4jLkvna",
            "https://drive.google.com/uc?export=view&id=1YW_b1PiYt8EO18LKJm0CNQ4wQbh1k90G",
            "https://drive.google.com/uc?export=view&id=1k2F9QtIE0HIaxo0LjS0DQQEqDiA4xuzQ",
            "https://drive.google.com/uc?export=view&id=1P5YxZxOSnYB-ldN9-sfq-raO1Mwmc_2B",#sherena
            "https://drive.google.com/uc?export=view&id=1cjouzguReuyyWf13XXJjTqN597W1TZt1",
            "https://drive.google.com/uc?export=view&id=11rH8LvddIDnuROnO1cqbb1zXBJpyPfYf",#Faiza
            "https://drive.google.com/uc?export=view&id=1n4gx_uh_Q00T5RzGnImAZK0OM7xA9gpE",
            "https://drive.google.com/uc?export=view&id=1JeuLgfZwnnGLvQIwX3Nfxv9jDjsnRZY3",
            "https://drive.google.com/uc?export=view&id=1CQFfgHbIMZCWvWgXCbvWVHVZliBrcIGp",
            "https://drive.google.com/uc?export=view&id=17F0OOgVr5GpwLmeZwxXbzsHLzQBvc41Y",#melva
            "https://drive.google.com/uc?export=view&id=1VV6BX7Az4kEnvFS1o68Zho0M8EDrpbb9",
            "https://drive.google.com/uc?export=view&id=1HfKrYGUARWhMfpyDZR6IX2tASQwGmQEB",

        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton Bandar Lampung ",
                "hobbi": "Gangguin bang keya",
                "sosmed": "@biyokcb ig",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya",
                "hobbi": "Nonton film",
                "sosmed": "@tvnty_",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak."# 1
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "...",
                "pesan": "Tetap semangat menjalani pengobatannya yang bang semoga lekas sembuh, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis ",
                "hobbi": "Gitar",
                "sosmed": "@manuelfdk_",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12",
                "asal": "Bali",
                "alamat": "nusa peninda",
                "hobbi": "menghayal",
                "sosmed": "@violaadrtr_",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "natar",
                "alamat": "natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "..",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "1244500078",
                "umur": "19",
                "asal": "kepulauan riau",
                "alamat": "teluk betung",
                "hobbi": "nonton khw",
                "sosmed": "@vunnycaa",
                "kesan": "....",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                 "nim": "123450119",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@keyashafi_",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."# 1
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara ",
                "alamat": "Pemda",
                "hobbi": "Sibuk",
                "sosmed": "@_els.a",
                "kesan": "...",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "airan",
                "hobbi": "mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "...",
                "pesan": "...."# 1
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "sumatera utara",
                "alamat": "way huwi",
                "hobbi": "dengering musik",
                "sosmed": "@_loviaa",
                "kesan": "....",
                "pesan": "Semoga ilmu dan kebaikan yang Kakak bagikan ke kami menjadi berkah untuk perjalanan Kakak"# 1
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "kalianda",
                "alamat": "kota baru",
                "hobbi": "main game, tidur",
                "sosmed": "@aluccy_",
                "kesan": "...",
                "pesan": ".Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal":"Bengkulu Selatan ",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "...",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                 "umur": "21",
                "asal":"Padang",
                "alamat": "Jl. Lapas",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel ",
                "sosmed": "@faizaanjanii",
                "kesan": "...",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Rajabasa Raya",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur ",
                "hobbi": "3N ( Ngoding , Ngegame, Nyibukin Diri)",
                "sosmed": "@apiszzaja",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Campang Raya, Sukabumi",
                "hobbi": "Gym, membaca, dan bermain",
                "sosmed": "@kelelep_comberan",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                 "umur": "19",
                "asal":"Sumatera Selatan ",
                "alamat": "Sukarame ",
                "hobbi": "Memasak",
                "sosmed": "@melva_fbrt",
                "kesan": "..",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syafiqui",
                "kesan": "...",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "-",
                "asal":"Kotabumi",
                "alamat": "Rajabasa",
                "hobbi": "Ngerecokin nuel",
                "sosmed": "@henryferdianto",
                "kesan": "....",
                "pesan": "Tetap semangat menginspirasi banyak orang ya bang, semoga sukses selalu menyertai abang."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMIKFES()

    elif menu == "Departemen SSD":
    def DepartemenSSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XPp3MgzYGEu1tallFkKG1Mkoizu9DtI2",
            "https://drive.google.com/uc?export=view&id=13WvVDLQ7tXfK9g4n0eDxPX7243XXZLek",
            "https://drive.google.com/uc?export=view&id=1zvk_mpsKEoGVOAd4lY7TyrFfYFeAZ9Zl",
            "https://drive.google.com/uc?export=view&id=1yskD7IIpcIXtSpnoS4Dr3GTXHOLPSRl2",
            "https://drive.google.com/uc?export=view&id=1TFIzadEnW8-BW8I5a5_BwoHb0LiEouOS",
            "https://drive.google.com/uc?export=view&id=10oqirw2d1isTNOGaes_CjsbaB79HA7r9",
            "https://drive.google.com/uc?export=view&id=1SEnT0UThKJ0BT3zst5uBfsyxn4wvZmME",
            "https://drive.google.com/uc?export=view&id=1elEL6rdoFwTJqXcMVUHfI-YRjEiHVFKg",
            "https://drive.google.com/uc?export=view&id=1gpyzyZ1gNC0bvstw0MupueRkVLdH45Fc",
            "https://drive.google.com/uc?export=view&id=1FdR21xyxaHXZ69WMTAfk41gOLhU95EIW",#bang afdal
            "https://drive.google.com/uc?export=view&id=1FdR21xyxaHXZ69WMTAfk41gOLhU95EIW",
            "https://drive.google.com/uc?export=view&id=1jf5Lr53LoPwyj0o7wJwhl5KlGl0RRZlG",


        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "hanifah inaya sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "20",
                "asal": "Bandung",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin",
                "sosmed": "@lay.inr_",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "....",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton ",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "...",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Abdilah Fikri Alpome",
                 "nim": "123450062",
                "umur": "21",
                "asal": "Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket",
                "sosmed": "@pomest__",
                "kesan": "...",
                "pesan": ".Selamat melanjutkan aktivitas kuliah! Semoga IPK semester ini memuaskan dan sesuai harapan.."# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": "",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi dilancarkan sampai lulus"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenSSD()

elif menu == "Departemen Medkraf":
    def DepartemenMedkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nUNxROBdpDSqDGui0BTZ39g994bsWqu7",
            "https://drive.google.com/uc?export=view&id=18OGsGIuJI5zxz4OudNla8gbo2ME6IxFk",
            "https://drive.google.com/uc?export=view&id=1tdbmeSBGKZfs-p0jBUFwYok5GozrnNFc",
            "https://drive.google.com/uc?export=view&id=1YG_aRBHXYBHma4Ch3clPoXfmcf9ojIPH",
            "https://drive.google.com/uc?export=view&id=10qw21HZwDEcNtARHRNbIdDCnVBfrHDaf",
            "https://drive.google.com/uc?export=view&id=1qzRm7BQEGYPy9TRIPsPvpDc-mRbB2hER",
            "https://drive.google.com/uc?export=view&id=1u633h_Q6JRUXjNortX16PNg-L3cGZ9Wi",
            "https://drive.google.com/uc?export=view&id=1vybJMvLyszpfy4_Y3-FKVrp4j7cNdvHT",
            "https://drive.google.com/uc?export=view&id=1L5Bk9W0CvJOsXWwGQnX5xotf-tdSy5Gb",
            "https://drive.google.com/uc?export=view&id=15UV_01akv5WVlE3-OortCtmpFNzdKceX",
            "https://drive.google.com/uc?export=view&id=1ln2s4dnSTtwvOEoGd32BDrzKUqSw--3V",
            "https://drive.google.com/uc?export=view&id=1nVt97qQWWMUjcwySjedsVF2YkMDZQq0P",
            "https://drive.google.com/uc?export=view&id=17HmhtER0NYrX7wf0KlKJ_bJ6mEmVTfvL",
            "https://drive.google.com/uc?export=view&id=1dgNWoiKpEUN1R9K5BJKacd5a9QOaUfJ3",
            "https://drive.google.com/uc?export=view&id=1IdQ9Si76___AQ29Yegz9ZZttn6fOphto",
            "https://drive.google.com/uc?export=view&id=15YQHPy6iS-RbvzRE41nWZtxbhtOK5DSH",
            "https://drive.google.com/uc?export=view&id=",#shafa
            "https://drive.google.com/uc?export=view&id=1SFyKYbASpmxcoJiqAhJuWBLg1W8W2lec",

        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi, Jati Agung, Lampung Selatan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "..",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "...",
                "pesan": "Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu ",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran ",
                "sosmed": "@noerruuu",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung ",
                "alamat": "Way Halim ",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."
            },
            {
                "nama": "Felisya Nabila Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal": "Lampung Timur ",
                "alamat": "Kota Baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "21",
                "asal": "Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Sania DWi Ayu Lestari",
                "nim": "124450086",
                "umur": "21",
                "asal": "Karawang ",
                "alamat": "Airan Raya",
                "hobbi": "Nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "pertama kali liat waktu pplk, kakanya cantik dan cute",
                "pesan": "Selamat melanjutkan aktivitas kuliah, Kak! Semoga IPK semester ini memuaskan dan sesuai harapan."# 1
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Alya Ramadhanti",
                 "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kakanya cantik, ramahh dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Lampung Selatan",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "kakaaa cantik banget aku suka ngeliatnya",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal": "Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Alquran",
                "sosmed": "@difanyhsa_",
                "kesan": "...",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang ",
                "sosmed": "@nzlhauly_",
                "kesan": "kakanya cantik dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Aira Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "@n1tg._",
                "kesan": "kakanya cantik,ramhhh dan cute",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame ",
                "hobbi": "-",
                "sosmed": "@daffascript",
                "kesan": "..",
                "pesan":".."
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "...",
                "pesan": "..."# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "cute, gemass banget waktu liatnya karna  cantik bgt",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis dan menulis",
                "sosmed": "@_shaazzh",
                "kesan": "kakanya cantik dan ramah",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal": "Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "kakanya cantik,ramahh dan baikk",
                "pesan": "Semoga segala urusan akademis, organisasi, dan skripsi Kakak dilancarkan sampai lulus."
            }

        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMedkraf()


# Tambahkan menu lainnya sesuai kebutuhan
