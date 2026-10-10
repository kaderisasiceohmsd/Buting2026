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

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
    "https://drive.google.com/uc?export=view&id=1lMm2cZotf4Zg5npQZTNsGulE71uamr0G",
    "https://drive.google.com/uc?export=view&id=1L1mV6NSK_dwiOB1dMLtHXVss8YvviGF7",
    "https://drive.google.com/uc?export=view&id=1arEBvurK397f3EPs4YmXihuHpY_0Ngnk",
    "https://drive.google.com/uc?export=view&id=16feqaSynGDSLmG6TwVb8uUt8V9ylEypi",
    "https://drive.google.com/uc?export=view&id=1Iwen8hJLSVc5_-C7sEAhlDoByhm82chK"
]

        data_list = [
            {
                "nama": "Ginda Fajar Marpaung",
                "nim": "1234500fadil",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@gars_mrp",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Muhammad Aqil",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Qois Alfio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoidalfio_",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Evi Defiani",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lamtim",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffifi",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hafsa Fadzilah Arraadhila",
                "nim": "079",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaarmdhn",
                "kesan": "-",
                "pesan": "-"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/file/d/1lMm2cZotf4Zg5npQZTNsGulE71uamr0G",
            "https://drive.google.com/file/d/1L1mV6NSK_dwiOB1dMLtHXVss8YvviGF7",
            "https://drive.google.com/file/d/1arEBvurK397f3EPs4YmXihuHpY_0Ngnk",
            "https://drive.google.com/file/d/16feqaSynGDSLmG6TwVb8uUt8V9ylEypi",
            "https://drive.google.com/file/d/1Iwen8hJLSVc5_-C7sEAhlDoByhm82chK",
            "https://drive.google.com/file/d/112PQJYl9BJ8q5ORQYnSRGyH8n9l32F8E",
            "https://drive.google.com/file/d/1NkMl76Maz1x0FhMtcM1IBmT2SrfIroUj",
            "https://drive.google.com/file/d/1w1Pfz_aCH3SSyhmhkDnHJw02PurUwtoH",
        ]

        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Kota Manchester",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "...",  
                "pesan":"..."# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "...",  
                "pesan":"..."# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/file/d/1GEVx0r0hwY_jXQP3pD4X-uwE0DMZebcI",
            "https://drive.google.com/file/d/1fUMJq1YXVoroSqWkLIL1wXO73H1eEvDJ",
            "https://drive.google.com/file/d/1Qabc-2O6m8ku8oPNsJSFQToiJh6rekMP",
            "https://drive.google.com/file/d/1inHomptv1djGZGSLZo7fg2VHn03O7x13",
            "https://drive.google.com/file/d/173RgfXc3ezh7t14WsWPd49Eddybzjzx0",
            "https://drive.google.com/file/d/1lpeaME0D5oCgx78rV3HNcAOdsu1p1dXs",
            "https://drive.google.com/file/d/1p4Rk4TqyvpxkE5RrXRIzg6fWGzOsQ0qj",
            "https://drive.google.com/file/d/1hPqAx0Th8801yxRCCmmuQ_40z1lBZbBw",
            "https://drive.google.com/file/d/17hJfFqdJ0J9e2fvMAH-I54-nD0WZJ9fF",

        ]

        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "23-060",
                "umur": "20",
                "asal": "Kota Manchester",
                "alamat": "Di GH",
                "hobbi": "Wawancara",
                "sosmed": "@ridhomanik",
                "kesan": "-",
                "pesan": "Ketua Baleg"
            },
            {
                "nama": "Wanaswa Alhani Yuska",
                "nim": "23-77",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Juwesi Aprilia Saragih",
                "nim": "23-085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Semusim dari Marsel",
                "sosmed": "@j__eesie",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Ghifaro Ananta",
                "nim": "23-78",
                "umur": "19",
                "asal": "Lambar",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Afghanis Nur Solehatunnisa",
                "nim": "24-042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "24-20",
                "umur": "20",
                "asal": "CTR?",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Sekardini Lidya Putri",
                "nim": "24-82",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama Nisa, Putri, Suci",
                "sosmed": "@sekardnwp",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Jonna Timothy Ogatse Panjaitan",
                "nim": "24-111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym, koleksi figure, nafas manual",
                "sosmed": "@nagatse",
                "kesan": "-",
                "pesan": "-"
            },
            {
                "nama": "Siti Sarifah",
                "nim": "...-15",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "-",
                "kesan": "-",
                "pesan": "-"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    Departemen_Minbak()

# Tambahkan menu lainnya sesuai kebutuhan
