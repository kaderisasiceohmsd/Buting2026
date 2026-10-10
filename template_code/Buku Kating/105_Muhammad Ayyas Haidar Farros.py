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
                "background-color": "#3FBAD8"
            },
        },
    )
    return selected


@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img = img.resize((300, 400))

        return img

    except Exception as e:
        st.warning(f"Gagal memuat gambar: {e}")
        return None


def display_images_with_data(gambar_urls, data_list):
    for i, (url, data) in enumerate(zip(gambar_urls, data_list)):
        with st.spinner(
            f"Memuat gambar {i + 1} dari {len(gambar_urls)}"
        ):
            img = load_image(url)

        if img is not None:
            col1, col2, col3 = st.columns([1, 2, 1])

            with col2:
                st.image(img, use_container_width=True)

        st.write(f"Nama: {data['nama']}")
        st.write(f"NIM: {data['nim']}")
        st.write(f"Umur: {data['umur']}")
        st.write(f"Asal: {data['asal']}")
        st.write(f"Alamat: {data['alamat']}")
        st.write(f"Hobi: {data['hobbi']}")
        st.write(f"Sosial Media: {data['sosmed']}")
        st.write(f"Kesan: {data['kesan']}")
        st.write(f"Pesan: {data['pesan']}")
        st.divider()

    st.write("Semua gambar telah selesai diproses!")


menu = streamlit_menu()


# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cxDpeniK2M87cEpIT45yqjQvkElMe6a7",
            "https://drive.google.com/uc?export=view&id=1vNZXH7LXKIAnG06x-WLSqKiI6kfAY627",
            "https://drive.google.com/uc?export=view&id=1ByPKZIySgdkCgVuO4kJCDIEFen9rn8rN",
            "https://drive.google.com/uc?export=view&id=10PcUccRaqv7TBwy741J3tKESmN_t5mHn",
            "https://drive.google.com/uc?export=view&id=1SbEwgqguXv-syb4V0TjOrBQxnMaB9IZ3",
            "https://drive.google.com/uc?export=view&id=1NeTJV1qWfdcvmdibLWHn5tVHDPX1fogA",
        ]

        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Kakaknya asik dan seru diajak belajar.",
                "pesan": "Semangat terus kuliahnya, semoga lancar sampai lulus!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Orangnya asik dan enak diajak ngobrol.",
                "pesan": "Semangat terus ya kak, jangan lupa istirahat!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik dan enak diajak sharing.",
                "pesan": "Semoga kuliahnya lancar terus ya kak!"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakaknya asik dan orangnya seru.",
                "pesan": "Semangat terus kak, semoga semua urusannya lancar!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya ramah dan asik diajak ngobrol.",
                "pesan": "Semangat terus ya kak, semoga sukses selalu!"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya asik dan baik banget.",
                "pesan": "Semangat kuliahnya kak, semoga cepat sampai tujuan!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    Kesekjenan()


if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rA3XxgRmWX3gbTlsXGKU5ZojB9cbC8oA",
            "https://drive.google.com/uc?export=view&id=1OwYAoRPYZcSYcbWEjyHInRMDWkquiSVl",
            "https://drive.google.com/uc?export=view&id=1LTiRz47gtHhlID-S24XSr9enzeswffKg",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1w6xBbRMuIcxkYkLSF3wVtg-e5885VDCH",
            "https://drive.google.com/uc?export=view&id=1iIf0Mfe36HBL8KL3zrfY_B4TKthwlNXU",
            "https://drive.google.com/uc?export=view&id=1nEDSFCiAbZrqmeXfJfVrwJUrmjUYW7ba",
            "https://drive.google.com/uc?export=view&id=1l5qmdb2p0otZFEVkr4xgBGP_SMgoPBA_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1lFN3s1Uzhy2SoIcjx0ycxFiX6YRN9ku5",
            "https://drive.google.com/uc?export=view&id=1zoX6B4MZI_g9nvUk7L7gsziMGwh5Q6uI",
            "https://drive.google.com/uc?export=view&id=1AhyLqnnTweqifExVL5yEg-sC-H4aMUgq",
        ]

        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kota Manchester",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "Kakaknya asik dan mudah diajak ngobrol.",
                "pesan": "Semangat terus kuliahnya, semoga lancar sampai lulus!"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "Orangnya ramah dan seru.",
                "pesan": "Semangat terus ya kak, semoga sukses selalu!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Kakaknya asik dan punya banyak cerita.",
                "pesan": "Semoga semua urusannya lancar terus ya kak!"
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Orangnya asik dan gampang akrab.",
                "pesan": "Semangat terus kak, semoga kuliahnya lancar!"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya baik dan asik diajak ngobrol.",
                "pesan": "Semoga sukses terus dan lancar sampai wisuda!"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Orangnya santai dan asik.",
                "pesan": "Semangat terus kak, jangan lupa ngopi!"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya keren dan semangat belajar.",
                "pesan": "Semoga coding-nya lancar dan tugasnya cepat selesai!"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Orangnya asik dan seru.",
                "pesan": "Semangat terus ya kak, semoga bahagia selalu!"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Kakaknya asik dan punya banyak energi.",
                "pesan": "Semoga kuliah dan hobinya tetap lancar ya kak!"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Orangnya ramah dan menyenangkan.",
                "pesan": "Semangat terus kak, semoga semua target tercapai!"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Kakaknya unik dan asik diajak ngobrol.",
                "pesan": "Semangat terus kak, semoga sehat dan sukses!"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Orangnya seru dan asik.",
                "pesan": "Semoga kuliahnya lancar dan jangan lupa jajan!"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya asik dan punya ciri khas sendiri.",
                "pesan": "Semangat terus ya kak, semoga sukses ke depannya!"
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    Baleg()
