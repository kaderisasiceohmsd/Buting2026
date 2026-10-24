import streamlit as st
from streamlit_option_menu import option_menu
import requests
import re
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
            "Bason",
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
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

def get_direct_image_url(url):
    """Mengubah link berbagi Google Drive menjadi URL unduhan langsung."""
    match = re.search(r"/file/d/([^/?]+)", url)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    match = re.search(r"[?&]id=([^&]+)", url)
    if "drive.google.com" in url and match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    return url


@st.cache_data(show_spinner=False)
def load_image(url):
    """Mengambil dan memvalidasi gambar sebelum ditampilkan."""
    direct_url = get_direct_image_url(url)

    try:
        response = requests.get(
            direct_url,
            timeout=20,
            allow_redirects=True,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()

        # Pastikan respons benar-benar berisi data gambar, bukan halaman HTML.
        content_type = response.headers.get("Content-Type", "").lower()
        if "image" not in content_type:
            try:
                image = Image.open(BytesIO(response.content))
                image.verify()
            except Exception:
                return None

        image = Image.open(BytesIO(response.content))
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((600, 800))
        return image

    except Exception:
        return None


def display_images_with_data(gambar_urls, data_list):
    """Menampilkan setiap data orang dengan gambar yang sesuai."""
    jumlah = max(len(gambar_urls), len(data_list))

    for i in range(jumlah):
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            if i < len(gambar_urls):
                with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
                    img = load_image(gambar_urls[i])

                if img is not None:
                    st.image(img, use_container_width=True)
                else:
                    st.info(
                        f"Gambar ke-{i + 1} tidak dapat dimuat. "
                        "Pastikan link benar dan akses Google Drive diatur "
                        "ke 'Siapa saja yang memiliki link'."
                    )
            else:
                st.info("URL gambar belum ditambahkan.")

        if i < len(data_list):
            orang = data_list[i]
            st.write(f"Nama: {orang.get('nama', '-')}")
            st.write(f"NIM: {orang.get('nim', '-')}")
            st.write(f"Umur: {orang.get('umur', '-')}")
            st.write(f"Asal: {orang.get('asal', '-')}")
            st.write(f"Alamat: {orang.get('alamat', '-')}")
            st.write(f"Hobi: {orang.get('hobbi', '-')}")
            st.write(f"Sosial Media: {orang.get('sosmed', '-')}")
            st.write(f"Kesan: {orang.get('kesan', '-')}")
            st.write(f"Pesan: {orang.get('pesan', '-')}")
            st.divider()

    st.success("Selesai memproses daftar anggota.")



menu = streamlit_menu()

# BAGIAN MENU KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_eqne9wh7Vv3r72alnNC09hPcCCcozBA",
            "https://drive.google.com/uc?export=view&id=1A64fxbdMjm5-4tAkRQEfv-4TAvGDudYF",
            "https://drive.google.com/uc?export=view&id=1oI-tT7AdEqI1YOlPBf4vookLQPQvnZ6K",
            "https://drive.google.com/uc?export=view&id=17HrIBmIQ4HNvBWrX2sRAqIkiFLwbnVhT",
            "https://drive.google.com/uc?export=view&id=1-G9OLCTeEkZJT4D_4wEoi8theUGrLRj_",
            "https://drive.google.com/uc?export=view&id=1Kq9LFbKNgmgMMjhaFoaPTnsE7UaxAmlZ",
        ]

        data_list = [
            {"nama": "Ginda Fajar Marpaung", "nim": "1234500fadil", "umur": "22", "asal": "Batam", "alamat": "Sekretariat HMSD", "hobbi": "Push Rank sampe IMO", "sosmed": "@gars_mrp", "kesan": "-", "pesan": "-"},
            {"nama": "Muhammad Aqil", "nim": "123450046", "umur": "22", "asal": "Bangkinang", "alamat": "Sekretariat HMSD", "hobbi": "Dzikir", "sosmed": "@muhammadaqil1111", "kesan": "-", "pesan": "-"},
            {"nama": "Evi Defiati", "nim": "123450005", "umur": "21", "asal": "Lamtim", "alamat": "Airan", "hobbi": "Membaca", "sosmed": "@eeffifi", "kesan": "-", "pesan": "-"},
            {"nama": "Qois Alfio", "nim": "123450067", "umur": "22", "asal": "Batam", "alamat": "Kotabaru", "hobbi": "Mainin surat", "sosmed": "@qoidalfio_", "kesan": "-", "pesan": "-"},
            {"nama": "Hafsa Fadzilah Arraadhila", "nim": "079", "umur": "21", "asal": "Balam", "alamat": "Balam", "hobbi": "Berenang", "sosmed": "@hafsafadhilaa", "kesan": "-", "pesan": "-"},
            {"nama": "Luthfia Laila Ramadhani", "nim": "004", "umur": "20", "asal": "Bengkulu", "alamat": "Airan", "hobbi": "Bertemu Pak Tirta", "sosmed": "@lutfiaarmdhn", "kesan": "-", "pesan": "-"},
        ]

        display_images_with_data(gambar_urls, data_list)

    kesekjenan()


# BAGIAN MENU BALEG
elif menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GEVx0r0hwY_jXQP3pD4X-uwE0DMZebcI",
            "https://drive.google.com/uc?export=view&id=1fUMJq1YXVoroSqWkLIL1wXO73H1eEvDJ",
            "https://drive.google.com/uc?export=view&id=1Qabc-2O6m8ku8oPNsJSFQToiJh6rekMP",
            "https://drive.google.com/uc?export=view&id=1eJxqhSlWd-vGqvsvbc9KPLPVMHCOK6Fp",
            "https://drive.google.com/uc?export=view&id=173RgfXc3ezh7t14WsWPd49Eddybzjzx0",
            "https://drive.google.com/uc?export=view&id=1lpeaME0D5oCgx78rV3HNcAOdsu1p1dXs",
            "https://drive.google.com/uc?export=view&id=1p4Rk4TqyvpxkE5RrXRIzg6fWGzOsQ0qj",
            "https://drive.google.com/uc?export=view&id=1hPqAx0Th8801yxRCCmmuQ_40z1lBZbBw",
            "https://drive.google.com/uc?export=view&id=17hJfFqdJ0J9e2fvMAH-I54-nD0WZJ9fF",
            "https://drive.google.com/uc?export=view&id=112PQJYl9BJ8q5ORQYnSRGyH8n9l32F8E",
            "https://drive.google.com/uc?export=view&id=1NkMl76Maz1x0FhMtcM1IBmT2SrfIroUj",
            "https://drive.google.com/uc?export=view&id=1w1Pfz_aCH3SSyhmhkDnHJw02PurUwtoH",
        ]

        data_list = [
            {"nama": "Ridho Benedictus Togi Manik", "nim": "123450060", "umur": "20", "asal": "Kota Manchester", "alamat": "GH", "hobbi": "Wawancara", "sosmed": "@iamridhomanik", "kesan": "...", "pesan": "..."},
            {"nama": "Juesi Apridelia Saragih", "nim": "123450085", "umur": "19", "asal": "Singkawang", "alamat": "Pelangi", "hobbi": "Dengerin lagu semusim dari marsel", "sosmed": "@j__eesie", "kesan": "...", "pesan": "..."},
            {"nama": "Dharu Cahyoaji Sasongko", "nim": "123450023", "umur": "19", "asal": "Lampung", "alamat": "Bandar Lampung", "hobbi": "Ngidupin api baleg di tiktok", "sosmed": "@exvoltas", "kesan": "...", "pesan": "..."},
            {"nama": "Gh. Mikael Niko Antoni Setiadi", "nim": "124450025", "umur": "20", "asal": "Jabung", "alamat": "Jati Agung", "hobbi": "COD Musang", "sosmed": "@me._kael", "kesan": "...", "pesan": "..."},
            {"nama": "Siti Sarifah Sumamah", "nim": "124450015", "umur": "19", "asal": "Bekasi", "alamat": "Kedaton", "hobbi": "Mancing", "sosmed": "@syt.rifa", "kesan": "...", "pesan": "..."},
            {"nama": "Givaro Ananta", "nim": "123450078", "umur": "19", "asal": "Lampung Barat", "alamat": "Sukabumi", "hobbi": "Minum Kopi", "sosmed": "@givarooo", "kesan": "...", "pesan": "..."},
            {"nama": "Afghanis Nursholehatunnisa", "nim": "124450042", "umur": "19", "asal": "Kepulauan Mentawai", "alamat": "Owen Kost", "hobbi": "Ngoding", "sosmed": "@afghanisnt_", "kesan": "...", "pesan": "..."},
            {"nama": "Hani Qurrota Aini", "nim": "124450020", "umur": "20", "asal": "CTR", "alamat": "Sukarame", "hobbi": "Baca AU", "sosmed": "@haniquratuain_", "kesan": "...", "pesan": "..."},
            {"nama": "Jeremia Halim", "nim": "124450101", "umur": "20", "asal": "Tanggerang", "alamat": "Teluk", "hobbi": "Nyanyi, olahraga", "sosmed": "@jeremia_hm", "kesan": "...", "pesan": "..."},
            {"nama": "Jona Timothy Ogatse Panjaitan", "nim": "124450111", "umur": "20", "asal": "Depok", "alamat": "Pemda Raya", "hobbi": "Gym sama Koleksi figure, nafas manual", "sosmed": "@nagatseee", "kesan": "...", "pesan": "..."},
            {"nama": "Sekar Dini Widya Putri", "nim": "124450082", "umur": "20", "asal": "Metro", "alamat": "Pemda", "hobbi": "Jajan sama nisa, putri, suci", "sosmed": "@sekardnwp", "kesan": "...", "pesan": "..."},
            {"nama": "Wan Nashwa Alhasni Yuska", "nim": "123450077", "umur": "20", "asal": "Pasay", "alamat": "Belwis", "hobbi": "Nyapa angin", "sosmed": "@nshaysk", "kesan": "...", "pesan": "..."},
        ]

        display_images_with_data(gambar_urls, data_list)

    Baleg()


# BAGIAN MENU DEPARTEMEN SSD
elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
           "https://drive.google.com/uc?export=view&id=1oUCS2tUHoQcpYaGCqxYVyvyE5_3AgQ1L",
            "https://drive.google.com/uc?export=view&id=1oIHqd9w0B5LWTjejJV2FNEsC2OWEOMGc",
            "https://drive.google.com/uc?export=view&id=1qkSQTdaUCDtMiEJEUU7fQ7sCZJ6zbHtD",
            "https://drive.google.com/uc?export=view&id=1OBN4S6MU3V_bOJO9U4V4sULPwq4kNitV",
            "https://drive.google.com/uc?export=view&id=1fuDNw5lovANFywGK3lJF0p_cS49pQzR0",
            "https://drive.google.com/uc?export=view&id=1j6Pb9pQfrDcLFmprpBH2kWNjLIkJprXq",
            "https://drive.google.com/uc?export=view&id=1Bxpc4PUlKHwMfOocW1Ij3zpq5S6pxxjC",
            "https://drive.google.com/uc?export=view&id=1qMHYGCvD8Mdt8qYjT4Xee6dKa7hvcIDi",
            "https://drive.google.com/uc?export=view&id=1jlcNxVJVs8eNxY9u7EdgGMOHBpyuF2yf",
            "https://drive.google.com/uc?export=view&id=18wNtTi3DichJGeTBy0k5OyWFhPL0SS9F",
            "https://drive.google.com/uc?export=view&id=1XSW7bOf4vH12uCCfIhGjwIQibAMaw5Ct",
            "https://drive.google.com/uc?export=view&id=1697LjAARLZzn2zrskHjHczbl1y8eTqxF",
            "https://drive.google.com/uc?export=view&id=1q01hzS4qJCG7QrxdqmGTJXRZEhYB0tSz",
            "https://drive.google.com/uc?export=view&id=1E0Ewz5xdMJDCqpv44dxMK78EZmiyYsSG",
            "https://drive.google.com/uc?export=view&id=1gifkBdha3tiUhf_lqtPP0fzK7E_0pzsl",
        ]

        data_list = [
    {
        "nama": "Kevin Antonio Junior",
        "nim": "123450109",
        "umur": "23",
        "asal": "Sulawesi Tengah",
        "alamat": "Panjang",
        "hobbi": "Mancing",
        "sosmed": "@kevinaja__",
        "kesan": "Sangat menginspirasi dan memimpin dengan baik",
        "pesan": "Semangat terus kak!"
    },
    {
        "nama": "Gusti Putu Ferazka Dhiyamika",
        "nim": "123450046",
        "umur": "21",
        "asal": "Bekasi",
        "alamat": "Way Dadi",
        "hobbi": "Mendaki",
        "sosmed": "@ferazkaa",
        "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
        "pesan": "Sukses selalu kak!"
    },
    {
        "nama": "Ali Aristo Muthahhari Parisi",
        "nim": "123450088",
        "umur": "21",
        "asal": "Lampung Timur",
        "alamat": "Gang Sakum Belwis",
        "hobbi": "Nonton F1",
        "sosmed": "@ali_parisi3",
        "kesan": "Keren dan selalu memberikan arahan yang jelas",
        "pesan": "Semangat menjalankan tugasnya kak!"
    },
    {
        "nama": "Ayu Andriani Parlina Wati",
        "nim": "124450058",
        "umur": "20",
        "asal": "Lampung Barat",
        "alamat": "Airan",
        "hobbi": "Belajar + menghitung uang",
        "sosmed": "@aayuandriani_",
        "kesan": "Sangat ramah dan aktif berkontribusi",
        "pesan": "Tetap semangat dan sukses terus!"
    },
    {
        "nama": "Dafa Elpriza",
        "nim": "124450131",
        "umur": "21",
        "asal": "Bekasi",
        "alamat": "Way Kandis",
        "hobbi": "Jogging",
        "sosmed": "@dafaelpriza_",
        "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
        "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
    },
    {
        "nama": "Juwita Sari",
        "nim": "124450066",
        "umur": "19",
        "asal": "Lampung Barat",
        "alamat": "Pemda",
        "hobbi": "Mancing",
        "sosmed": "@ju.juwitaaa_",
        "kesan": "Sangat baik dan murah senyum",
        "pesan": "Semangat terus kuliahnya!"
    },
    {
        "nama": "Muhammad Afdal Luthfi",
        "nim": "124450047",
        "umur": "19",
        "asal": "Lampung Tengah",
        "alamat": "Jl. Pulau Damar",
        "hobbi": "Memantau dl tugas",
        "sosmed": "@afdall.03",
        "kesan": "Sangat bertanggung jawab dan fokus",
        "pesan": "Semangat terus kakak!"
    },
    {
        "nama": "Salsabila Nazwa Putri",
        "nim": "124450002",
        "umur": "20",
        "asal": "Metro",
        "alamat": "Korpri",
        "hobbi": "Nongkrong di kopken",
        "sosmed": "@slbnzw_",
        "kesan": "Sangat asik dan ceria",
        "pesan": "Tetap semangat kuliahnya ya kak!"
    },
    {
        "nama": "Muhammad Ridwan",
        "nim": "123450091",
        "umur": "21",
        "asal": "Lampung Tengah",
        "alamat": "Belwis",
        "hobbi": "Badminton",
        "sosmed": "@mridwaan_22",
        "kesan": "Sangat mengayomi dan membimbing dengan sabar",
        "pesan": "Semangat terus memimpin divisinya kak!"
    },
    {
        "nama": "Andra Ilham Bintang",
        "nim": "124450060",
        "umur": "18",
        "asal": "Sumatera Selatan",
        "alamat": "Kotabaru",
        "hobbi": "Main rubik",
        "sosmed": "@andra.lhm",
        "kesan": "Sangat kreatif dan pintar",
        "pesan": "Sukses selalu kuliahnya!"
    },
    {
        "nama": "Bryan Paskah Telaumbanua",
        "nim": "124450003",
        "umur": "20",
        "asal": "Nias",
        "alamat": "Belwis",
        "hobbi": "Live tiktok",
        "sosmed": "@bryantel_",
        "kesan": "Sangat menghibur dan ramah",
        "pesan": "Semangat terus berkarya kak!"
    },
    {
        "nama": "Ghiyats Thabularasa Meardhy",
        "nim": "124450067",
        "umur": "17",
        "asal": "Surabaya",
        "alamat": "Kemiling",
        "hobbi": "Nanem Sawit",
        "sosmed": "@meardhy_ghiyats",
        "kesan": "Sangat unik dan bersemangat",
        "pesan": "Tetap semangat dan sukses selalu!"
    },
    {
        "nama": "Indah Julia Mawar Pratiwi",
        "nim": "124450055",
        "umur": "20",
        "asal": "Pringsewu",
        "alamat": "Airan",
        "hobbi": "Bengong",
        "sosmed": "@indahjuliaa",
        "kesan": "Sangat baik dan bersahabat",
        "pesan": "Sukses terus perkuliahannya kak!"
    },
    {
        "nama": "Jacinda Kesya Alvara",
        "nim": "124450023",
        "umur": "18",
        "asal": "Kalimantan Barat",
        "alamat": "Korpri",
        "hobbi": "Nyapu depan gacoan",
        "sosmed": "@cacalvra",
        "kesan": "Sangat ceria dan menyenangkan",
        "pesan": "Semangat terus ya kak!"
    },
    {
        "nama": "Muhammad Rafka",
        "nim": "124450089",
        "umur": "20",
        "asal": "Padang",
        "alamat": "Kotabaru",
        "hobbi": "Bangun pagi",
        "sosmed": "@muhammdrafka_",
        "kesan": "Sangat disiplin dan dapat diandalkan",
        "pesan": "Sukses selalu buat perkuliahannya!"
    }
]

        display_images_with_data(gambar_urls, data_list)

    Departemen_Minbak()


elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P4ruEk7NETFmFwSpA5IasehjcCj_sTyC",
            "https://drive.google.com/uc?export=view&id=15isF6NFx2_fp9zXGRDcHM0HEGulMmCdM",
            "https://drive.google.com/uc?export=view&id=1s5GvbYr-xmxzzzr7nDjm63DSaSYOQq7y",
            "https://drive.google.com/uc?export=view&id=1bSOCPQwxcSPGQ_JXWL-4Zwm1OCuweCu4",
            "https://drive.google.com/uc?export=view&id=1bphBvECJmybGOcAzcVyxL4_gzMWo3ANg",
            "https://drive.google.com/uc?export=view&id=15YH0V3v18gLUxLPvYazTOvqzIDN1r7fT",
            "https://drive.google.com/uc?export=view&id=1oMnwYJapXVrMkpQ2psowMlFNltWy4kH2",
            "https://drive.google.com/uc?export=view&id=1fq9orydmm-d4Tc6RRS8OLl4CuyoZLDkS",
            "https://drive.google.com/uc?export=view&id=1LX00iLQB690SPQW2hoJ1kOriump8LWJB",
            "https://drive.google.com/uc?export=view&id=1sECCXB4H_nPKyJX9riNihBRwmSb0imxx",
            "https://drive.google.com/uc?export=view&id=1H926uCv7ZYVnnb3-rL7HJgxDg4ryehiP",
        ]
        data_list = [
            # Pimpinan & Sekretaris
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },

            # Divisi Kemitraan
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },

            # Divisi Kewirausahaan
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"
            }
        ]

        st.subheader("Departemen SSD")
        display_images_with_data(gambar_urls, data_list)

    Departemen_SSD()
    
elif menu == "Bason":
    def Bason():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1s_w0hubRnMu90OKKfRz_Tz4EpKcLmreU",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": "Inspired girl, beneran keren bangettttt",  
                "pesan": "Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": "Duta melet, lucuuuu",  
                "pesan":"Semangat terus kuliahnya kak!"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Chill banget kakanyaa",  
                "pesan":"Semanagat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Sumpah style baju kakanya keren kerennn",  
                "pesan":"Semangat terus kak kuliahnya!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Welcome sekali abangnya, apapun pose yang diminta beneran diiyain #GEMAS",  
                "pesan":"Semangat terus bang kuliahnya!"# 1
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Banyak ilmu mengenai Strategis dan Propaganda yg aku peroleh dari kakaaa",  
                "pesan":"Semangat kak TA nyaa, semoga dimudahkan jalannya yaa!!"# 1
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Modis dan keren banget style stylenyaa, dan imup bangett",  
                "pesan":"Semangat terus kuliahnya kaa!"# 1
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "kece euyyy, style abang beneran keren bangett",  
                "pesan":"Semangat terus bang kuliah dan organisasinya!"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Welcome sekali kakanyaaa, dan cara penyampaian materinya juga mudah dipahami",  
                "pesan":"Semangat terus kuliahnya kaa!!"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Gemass kakanyaa",  
                "pesan":"Semangat terus kaa kuliahnyaa!!"# 1
            },
        ]
        st.subheader("Badan Senator")
        display_images_with_data(gambar_urls, data_list)

    Bason()

elif menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
        ]

        data_list = [
            {
                "nama": "Kharisma Mustikasari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Waikana",
                "alamat": "Untung Seropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "Rismaa. Mustika_",
                "divisi": "Sekdep",
                "jabatan": "Sekdep",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "106",
                "umur": "23",
                "asal": "Jambi",
                "alamat": "Jatimulyo",
                "hobbi": "Ngerosting orang",
                "sosmed": "Haikalsbln_",
                "divisi": "Belum disebutkan",
                "jabatan": "Kepala Departemen",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Hanna Gressia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran CV",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam ITERA",
                "sosmed": "Hanna_g_sinaga",
                "divisi": "Keharmonisan",
                "jabatan": "Kepala DC Keharmonisan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aisyah Khairun",
                "nim": "124450009",
                "umur": "20",
                "asal": "Riau, Air Molek",
                "alamat": "Belwis",
                "hobbi": "Nulis whitlits",
                "sosmed": "Aisyahkhairun",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Kopri Raya",
                "hobbi": "Isengin Arvin di kelas",
                "sosmed": "Rozakramdani__",
                "divisi": "Keharmonisan",
                "jabatan": "Staf Keharmonisan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Teresa Christiani",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "Christiani8872",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aulina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Main air terjun",
                "sosmed": "Aulinaf_03",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "94",
                "umur": "22",
                "asal": "Kisaran CV",
                "alamat": "Pemda",
                "hobbi": "Tim boxing",
                "sosmed": "Jay_saputra_tmb",
                "divisi": "Harmonisasi",
                "jabatan": "Harmonisasi",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Mhanif Dzky",
                "nim": "123450064",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Perum Way Kandis",
                "hobbi": "Nonton film",
                "sosmed": "Hnsdzkf_",
                "divisi": "Kerohanian",
                "jabatan": "Kadif Kerohanian",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Marvinsyah",
                "nim": "12445128",
                "umur": "20",
                "asal": "Sumsel",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "Muhvinz_",
                "divisi": "Rohani",
                "jabatan": "Staf Rohani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Chika Adelia",
                "nim": "124451007",
                "umur": "20",
                "asal": "Riau, Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "Chikamrbn",
                "divisi": "Rohani",
                "jabatan": "Staf Rohani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafa Sabrina Fahima",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nanya ke Andra dan Yolanda",
                "sosmed": "Snasaa. _",
                "divisi": "Kerohanian",
                "jabatan": "Staf Kerohanian",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Farhan Dani",
                "nim": "12450121",
                "umur": "20",
                "asal": "Keliling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "Rahamdani",
                "divisi": "Damaskus",
                "jabatan": "Staf Damaskus",
                "kesan": "",
                "pesan": ""
            },
        ]

        st.subheader("Departemen Medkraf")
        display_images_with_data(gambar_urls, data_list)

    Departemen_Medkraf()
elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
        ]

        data_list = [
            {
                "nama": "Kharisma Mustikasari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Waikana",
                "alamat": "Untung Seropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "Rismaa. Mustika_",
                "divisi": "Sekdep",
                "jabatan": "Sekdep",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "106",
                "umur": "23",
                "asal": "Jambi",
                "alamat": "Jatimulyo",
                "hobbi": "Ngerosting orang",
                "sosmed": "Haikalsbln_",
                "divisi": "Belum disebutkan",
                "jabatan": "Kepala Departemen",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Hanna Gressia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran CV",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam ITERA",
                "sosmed": "Hanna_g_sinaga",
                "divisi": "Keharmonisan",
                "jabatan": "Kepala DC Keharmonisan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aisyah Khairun",
                "nim": "124450009",
                "umur": "20",
                "asal": "Riau, Air Molek",
                "alamat": "Belwis",
                "hobbi": "Nulis whitlits",
                "sosmed": "Aisyahkhairun",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Kopri Raya",
                "hobbi": "Isengin Arvin di kelas",
                "sosmed": "Rozakramdani__",
                "divisi": "Keharmonisan",
                "jabatan": "Staf Keharmonisan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Teresa Christiani",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "Christiani8872",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aulina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Sukarame",
                "hobbi": "Main air terjun",
                "sosmed": "Aulinaf_03",
                "divisi": "Harmonisasi",
                "jabatan": "Staf Harmonisasi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "94",
                "umur": "22",
                "asal": "Kisaran CV",
                "alamat": "Pemda",
                "hobbi": "Tim boxing",
                "sosmed": "Jay_saputra_tmb",
                "divisi": "Harmonisasi",
                "jabatan": "Harmonisasi",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Mhanif Dzky",
                "nim": "123450064",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Perum Way Kandis",
                "hobbi": "Nonton film",
                "sosmed": "Hnsdzkf_",
                "divisi": "Kerohanian",
                "jabatan": "Kadif Kerohanian",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Marvinsyah",
                "nim": "12445128",
                "umur": "20",
                "asal": "Sumsel",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "Muhvinz_",
                "divisi": "Rohani",
                "jabatan": "Staf Rohani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Chika Adelia",
                "nim": "124451007",
                "umur": "20",
                "asal": "Riau, Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "Chikamrbn",
                "divisi": "Rohani",
                "jabatan": "Staf Rohani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafa Sabrina Fahima",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nanya ke Andra dan Yolanda",
                "sosmed": "Snasaa. _",
                "divisi": "Kerohanian",
                "jabatan": "Staf Kerohanian",
                "kesan": "",
                "pesan": ""
            },

            {
                "nama": "Farhan Dani",
                "nim": "12450121",
                "umur": "20",
                "asal": "Keliling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "Rahamdani",
                "divisi": "Damaskus",
                "jabatan": "Staf Damaskus",
                "kesan": "",
                "pesan": ""
            },
        ]

        st.subheader("Departemen Internal")
        display_images_with_data(gambar_urls, data_list)

    Departemen_Internal()

# Tambahkan menu lainnya sesuai kebutuhan
