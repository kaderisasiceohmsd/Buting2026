import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown(
    """<style>.centered-title {text-align: center;}</style>""",
    unsafe_allow_html=True
)
st.markdown(
    "<h1 class='centered-title'>BUKU KATING</h1>",
    unsafe_allow_html=True
)

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
            "container": {
                "padding": "0!important",
                "background-color": "#fafafa"
            },
            "icon": {
                "color": "black",
                "font-size": "19px"
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {
                "background-color": "#9C6AC0"
            },
        },
    )
    return selected


@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))

        return img

    except Exception as e:
        return None


def display_images_with_data(gambar_urls, data_list):
    jumlah_data = max(len(gambar_urls), len(data_list))

    for i in range(jumlah_data):
        img = None

        if i < len(gambar_urls):
            url = gambar_urls[i]

            with st.spinner(
                f"Memuat gambar {i + 1} dari {len(gambar_urls)}"
            ):
                img = load_image(url)

        if img is not None:
            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                st.image(img, use_container_width=True)
        elif i < len(gambar_urls):
            st.warning(
                f"Gambar untuk data ke-{i + 1} gagal dimuat. "
                "Periksa URL atau izin akses Google Drive."
            )

        if i < len(data_list):
            data = data_list[i]

            st.write(f"Nama: {data['nama']}")
            st.write(f"NIM: {data['nim']}")
            st.write(f"Umur: {data['umur']}")
            st.write(f"Asal: {data['asal']}")
            st.write(f"Alamat: {data['alamat']}")
            st.write(f"Hobbi: {data['hobbi']}")
            st.write(f"Sosial Media: {data['sosmed']}")
            st.write(f"Kesan: {data['kesan']}")
            st.write(f"Pesan: {data['pesan']}")
            st.write("---")

    st.write("Semua data telah diproses!")


menu = streamlit_menu()


# BAGIAN SINI YANG HANYA BOLEH DIUBAH
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
                "asal": "Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal": "Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
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
            "https://drive.google.com/uc?export=view&id=1mHdZPK_B2QsTuNkAd9KyhztiYe_ZZPtJ",
            "https://drive.google.com/uc?export=view&id=1J4LYA1wkvGzxChY91Ycb9gViQ7dwkHnv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
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
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal": "City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
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
                "hobbi": "Main",
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
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
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
                "kesan": "bang kevin",
                "pesan": "semoga"
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
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal": "...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
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
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
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
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal": "....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal": "kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",
                "pesan": "Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Jl. Bima",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
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
                "kesan": "........",
                "pesan": "......"
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "........",
                "pesan": "......."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": ".......",
                "pesan": ".........."
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "......",
                "pesan": "........"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal": "Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "..........",
                "pesan": ".........."
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "........",
                "pesan": "......."
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal": "dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": ".......",
                "pesan": "......."
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal": "Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": ".......",
                "pesan": "......"
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "....",
                "umur": "...",
                "asal": "....",
                "alamat": "...",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "......",
                "pesan": "......."
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "......",
                "pesan": "......."
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "...",
                "umur": "...",
                "asal": "....",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "......",
                "pesan": "........"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "......",
                "pesan": "........"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "......",
                "pesan": "........"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "......",
                "pesan": "........"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    DepartemenPSDA()
