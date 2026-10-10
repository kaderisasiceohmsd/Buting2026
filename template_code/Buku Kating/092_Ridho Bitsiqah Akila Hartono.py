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
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#8d4c06a6"},
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

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1weAoCsP8r9dmgGlMph7bfxN6Wvke1a5W",
            "https://drive.google.com/uc?export=view&id=1uDzsskuhLNinqtZTQVyIEg7VRBiuKDfJ",
            "https://drive.google.com/uc?export=view&id=1wOcoDJ1Rho1-VkKO9WcgImL1b1ZTC-Tq",
            "https://drive.google.com/uc?export=view&id=1uX2fzeDjxYagle5yHDBlXhf9w6QJ_Fij",
            "https://drive.google.com/uc?export=view&id=1b90e-qA9oqgcwYgpRB8w83FTFbXPFH9M",
            "https://drive.google.com/uc?export=view&id=1eTSN1GRqJqRsD2uivyd5W5lPViLnaE7Z",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "push rank sampe imo",
                "sosmed": "@jars_mrp",
                "kesan": "Abangnya keren, kalem, asik juga waktu jadi pemateri",
                "pesan": "Semangat terus bang semoga skripsinya dimudahkan"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal": "Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya asik, lucu, suka bercanda juga, kalau jadi pemateri asik",
                "pesan": "Sehat selalu bang semoga dimudahkan segala urusan"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya baik sama kalem",
                "pesan": "Semangat terus dan sehat selalu kak"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keren, kalem, lucu",
                "pesan": "Semangat bikin bikin suratnyaa bang, semoga jadi mudah bikin skripsinya"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu Kesekjenan",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya cantik, baik, kalem, asik juga",
                "pesan": "Semangat terus kak, sehat selalu"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Airan",
                "hobbi": "Mintain Duit",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya lucu, baik, keren, asik juga",
                "pesan": "Semoga dimudahkan selalu ya kak segala urusannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakaknya cantik, baik, kalem, keren",
                "pesan": "Sehat selalu kak, semoga lancar skripsinya"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Tanya Bapas",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Abangnya seru, asik, lucu",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya baik, asik, kalem",
                "pesan": "Semoga selalu dimudahkan bang"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya kalem dan baik",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Abangnya asik, keren, pinter juga",
                "pesan": "Sehat selalu bang, semangat terus juga"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia,h_264",
                "kesan": "Kakaknya lucu, asik juga",
                "pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya lucu, keren juga",
                "pesan": "Semoga kelompoknya nambah gacor kak"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren, asik juga",
                "pesan": "Semoga sukses bang"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakaknya cantik, ramah, baik",
                "pesan": "Semangat terus kak, semoga kuliahnya lancar"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca Buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Mencari dan membaca jurnal, 2 minggu mewawancarai anak kader angkatan 25 Datavora tercinta, mencari pak Luki",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya lucu dan asik",
                "pesan": "Semangat skripsinya lancar bang"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Sehat selalu, semangat terus kak"
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Belakang PB",
                "hobbi": "Ngumpulin data sama nonton Marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Semangat terus ya kak"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124550012",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kost Ayake",
                "hobbi": "Scroll Facebook",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Abangnya baik dan santai",
                "pesan": "Semoga sukses bang"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124550016",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menonton Film",
                "sosmed": "@lay.inr_",
                "kesan": "Kakaknya ramah dan baik",
                "pesan": "Semangat terus ya kak"
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya kalem dan baik",
                "pesan": "Sehat terus bang"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakaknya ramah dan baik",
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Kost The Icon",
                "hobbi": "Belajar",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya pinter dan ramah",
                "pesan": "Sukses terus kak, semoga kuliahnya lancar"
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Oku, Sumatera Selatan",
                "alamat": "Airan",
                "hobbi": "Godain cewe bang Homey",
                "sosmed": "@pomest_",
                "kesan": "Abangnya lucu, asik dan seru",
                "pesan": "Semangat terus bang, semoga skripsinya lancar"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124550008",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Samping Kost Rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Abangnya baik dan asik",
                "pesan": "Semoga sehat terus bang"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124550009",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Menonton Kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakaknya ramah dan baik",
                "pesan": "Sehat selalu dan semangat terus kak"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari",
                "hobbi": "Lagi suka olahraga",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Sehat selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakaknya baik, ramah, asik juga",
                "pesan": "Semoga sehat selalu kak, semangat terus juga"
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya asik, baik, seru",
                "pesan": "Sehat selalu kak, semoga skripsinya lancar"
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Jakarta Utara, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Buka Tutup Laptop",
                "sosmed": "@noerruuu",
                "kesan": "Abangnya baik, ramah",
                "pesan": "Semoga sehat terus kak"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Ballet",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik, ramah, asik juga",
                "pesan": "Semoga sehat selalu kak, semangat kak"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing emosi",
                "sosmed": "felisyanbl",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Dukung silver arrow alias mercedes",
                "sosmed": "@muh_razan_",
                "kesan": "Abangnya baik, ramah",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "17",
                "asal": "Bali",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan prodi",
                "sosmed": "saniayyllstr",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "3 Tahun",
                "asal": "Surga",
                "alamat": "Rumah Asha",
                "hobbi": "Ice skating",
                "sosmed": "@aallishaa.aa",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Mengkoding",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "7.137 hari per hari ini",
                "asal": "Sumsel",
                "alamat": "Kafe Kali",
                "hobbi": "Bobo cantik",
                "sosmed": "@difanyhsa",
                "kesan": "Kakaknya ramah dan asik",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mimpi diatas kasur",
                "sosmed": "nzlhauly_",
                "kesan": "Kakaknya baik dan asik",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sukses terus kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@daffascript_",
                "kesan": "Abangnya asik dan ramah",
                "pesan": "Semoga dimudahkan urusannya bang"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scrolling Fesbuk",
                "sosmed": "@eddel_0712",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nonton Star Wars",
                "sosmed": "luciarachel_",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "Sehat terus, semangat terus kak"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga semngat dan sehat terus kak"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Unila",
                "hobbi": "Tidur",
                "sosmed": "@xifasky",
                "kesan": "Kakaknya kalem dan ramah",
                "pesan": "Semoga sehat selalu kak"
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20",
                "asal": "Tangerang Kota",
                "alamat": "Gerbang Barat",
                "hobbi": "Begadang",
                "sosmed": "@haikalsbln_",
                "kesan": "Abang ini asik dan keren",
                "pesan": "semangat abang, sehat selalu"
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "kakaknya cantik dan baik",
                "pesan": "semangat terus kuliahnya kakak, semangat skripsi"
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Membaca Novel",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik dan baik",
                "pesan": "semangat terus kuliahnya kakak semangat skripsi"
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450067",
                "umur": "22",
                "asal": "Tetangga Singapore",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya asik dan seru",
                "pesan": "semangat terus kuliahnya abang"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Indragirihulu",
                "alamat": "Samping Kuburan",
                "hobbi": "Sleep Call",
                "sosmed": "@aisyahkhair._",
                "kesan": "kakaknya cantik dan ramah",
                "pesan": "semangat kakak, sehat selalu"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Semarang",
                "alamat": "Belwis",
                "hobbi": "Manjat pohon kelapa",
                "sosmed": "@cerine_ipynb",
                "kesan": "kakaknya cantik dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Pemda",
                "hobbi": "Main Biola",
                "sosmed": "@jay.saputra.tmb",
                "kesan": "abangnya ASIK BANGET, seru orangnya",
                "pesan": "semangat terus kuliahnya abang semangat menugas"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Nonton asmr",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Badminton",
                "sosmed": "@rozakramdani_",
                "kesan": "Abangnya seru dan baik",
                "pesan": "semoga sehat selalu abang"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Memasak",
                "sosmed": "@christiani8872",
                "kesan": "kakanya baik, seru orangnya",
                "pesan": "semoga selalu dikelilingi orang baik"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "",
                "asal": "Padang",
                "alamat": "Way Kandis",
                "hobbi": "Nonton MU",
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya seru dan asik",
                "pesan": "semoga sehat selalu bang"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya asik dan baik",
                "pesan": "semangat terus kuliahnya kakak"
            },
            {
                "nama": "Cika Adelia BR Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Samping Kuburan",
                "hobbi": "Scroll tiktok",
                "sosmed": "@cikambrn",
                "kesan": "Kakaknya seru dan baik",
                "pesan": "Jaga kesehatan kakak, semoga bahagia selalu"
            },
            {
                "nama": "Gustin H Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "kakanya baik, seru orangnya",
                "pesan": "semoga selalu dikelilingi orang baik"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nangkap lele",
                "sosmed": "@muhvinz_",
                "kesan": "Abangnya seru dan asik",
                "pesan": "semoga sehat selalu bang"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Main game di HP temen",
                "sosmed": "@muhvinz_",
                "kesan": "Abangnya seru dan asik",
                "pesan": "semoga sehat selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    Internal()