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
            "people-fill"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#F4E7DB"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#8A5A44"},
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
            "https://drive.google.com/uc?export=view&id=1eLbSQN7oKHPKk5wH8EJH50wGM9XTEmmx",
            "https://drive.google.com/uc?export=view&id=1_12R1o5aqFhnBtNsIuPvrBULoI6OSQYn",
            "https://drive.google.com/uc?export=view&id=1l9nUyqvinm1HjE151H4MAKIIcN86GhtJ",
            "https://drive.google.com/uc?export=view&id=1xHHHzeQ_kng5d84eRKULnpdvk0kTh_zF",
            "https://drive.google.com/uc?export=view&id=1d30KUJ7FAzu4SaNmmYJVv3bCnTKty_Dw",
            "https://drive.google.com/uc?export=view&id=1oOvIjpYqprfkIYE6cKWjPEhN49htPMgk",
            "https://drive.google.com/uc?export=view&id=1alIPZWorvbzsL0zHk-ZRs48tHzRk8ur3",
            "https://drive.google.com/uc?export=view&id=1GwUQssN2axk035uyn3XZHkeP2G2NB9rg",
            "https://drive.google.com/uc?export=view&id=1Sjs86PvPpXJrjiGuXT-IPZwRbHl6vQkQ",
            "https://drive.google.com/uc?export=view&id=18TxTX4rTR-jxIf4X3-yt11gofOdApGtd",
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
            "https://drive.google.com/uc?export=view&id=14NoBOXiTza3JF8t8vYnJyrCE-k1FsOpk",
            "https://drive.google.com/uc?export=view&id=1NzKNfZZvSylDZFKy21WfLbxDvS5GbVJZ",
            "https://drive.google.com/uc?export=view&id=1gAdMaJilFrDXUjKDEQPHSqDNjFufHe-g",
            "https://drive.google.com/uc?export=view&id=1s_CLTgC25r8qMs_DdXSvC5USSOW8nWe9",
            "https://drive.google.com/uc?export=view&id=1iTFAP4Pi1kymygw80aOQ_BhTOQmfxQUv",
            "https://drive.google.com/uc?export=view&id=1fH_QUO6S996l_vKFiqxHss8UzXrTmqkc",
            "https://drive.google.com/uc?export=view&id=1gAdMaJilFrDXUjKDEQPHSqDNjFufHe-g",
            "https://drive.google.com/uc?export=view&id=1oXXrc039NWb5Q8Atdod_6YFGagEbJiCZ",
            "https://drive.google.com/uc?export=view&id=1eCmuMzB-rxDpDar-APXyuIyWLuyYK2Ch",
            "https://drive.google.com/uc?export=view&id=14-gvq9Cm2N34nyM5_FDzm-E9I3lUr0BL",
            "https://drive.google.com/uc?export=view&id=1GZDvxHxfBDkywHkK9rX1V5BRAERpP2zg",
            "https://drive.google.com/uc?export=view&id=1Fz0xvwWBQiSGvFazA-rJNcSTDM9ch8Fk",
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
                "nim": "124450012",
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
                "nim": "124450016",
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
                "nim": "124450008",
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
                "nim": "124450009",
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
                "pesan": "Sehat selalu kak, semoga sukses"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QZEvzFzUtfSPYWj86bmt9q7NYt3SEIsx",
            "https://drive.google.com/uc?export=view&id=1WjCkvrLdNA5Hd6yMBR0RDF9lb0ks6QvC",
            "https://drive.google.com/uc?export=view&id=19LFcuYeWynk_j5azfmqvp2bXSkEwz_xJ",
            "https://drive.google.com/uc?export=view&id=1GbT5eFEoPSmCMIe0V3m5zqttmbV20Mzb",
            "https://drive.google.com/uc?export=view&id=1Stf9ltD054x14Sb1SpI4T9JDN7sRkFWe",
            "https://drive.google.com/uc?export=view&id=18mgRFT27A-jsuqX5TWajig_npJBRI4dI",
            "https://drive.google.com/uc?export=view&id=1Ph1cS6bdn7PVMszuYOc8E2JZ3QAnQtv5",
            "https://drive.google.com/uc?export=view&id=1nQg3vCgHcQzBeBbNs5Af0Pu_zBZkZbTq",
            "https://drive.google.com/uc?export=view&id=1mhwuqs1rV4hFhYl34TtmRX2sAHx9zwvd",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tNFkcONPmnNxEB29z5b8H-4XWU-3ZhJ4",
            "https://drive.google.com/uc?export=view&id=1eo5rwZ-KmW8Ysw4LD9C7F7VT6saebpnL",
            "https://drive.google.com/uc?export=view&id=1PwrfKCBJ68-x9JJ7F6gQ_ea_opJoxntl",
            "https://drive.google.com/uc?export=view&id=1HVPr8Ap4QWW2xCyUZgmdYVcIxsvKscvd",
            "https://drive.google.com/uc?export=view&id=1_wFTL6ZRF57v8ytgWGXNl1wK-TxAPpKB",
            "https://drive.google.com/uc?export=view&id=1bKjFy9_FGv4eig_kJxGtcTpEAaawKGMp",
            "https://drive.google.com/uc?export=view&id=15U8JhEyurtQNZiFOsW4Dm6fGgB-9dc1s",
            "https://drive.google.com/uc?export=view&id=15U8JhEyurtQNZiFOsW4Dm6fGgB-9dc1s"
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
            "https://drive.google.com/uc?export=view&id=18omgW5yvp6x8CI8eCB4l3zmVXow3hzQV",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=197hcrvvy1zxQ7VJB6a9spm6YlPVy9TPy",
            "https://drive.google.com/uc?export=view&id=1d4m5lQyJl1CAHwIRUxjHr2CO_ibUDZsL",
            "https://drive.google.com/uc?export=view&id=1YCHg3EX7kazGMMulwlQw2PrtHHmd3HIQ",
            "https://drive.google.com/uc?export=view&id=1GV43LsN62GhaPyomzo9cvtyIK-tVbI2Q",
            "https://drive.google.com/uc?export=view&id=1ilNjZ3PCndEloow0vBPHrEcghKvZoYL9",
            "https://drive.google.com/uc?export=view&id=1LZJCgDxQ8xI9-nSftMObnyOu3-r-hjpV",
            "https://drive.google.com/uc?export=view&id=1rlBhJylqKRonvDqPZzRR_tQwHaStrQC7",
            "https://drive.google.com/uc?export=view&id=1ZVxdypwArAn3vd3b7rlIiGGKNFGXfp8s",
            "https://drive.google.com/uc?export=view&id=1XBsvwnSe4hcq-UF7wZV83XZOoD8fr3y2",
            "https://drive.google.com/uc?export=view&id=1bpo3PVMk0icKK1jlN__zrQmQ8LhGJ08j",
            "https://drive.google.com/uc?export=view&id=1uIVZlj2o6WHXLfd8cCdpBZBMBeoNQWJb",
            "https://drive.google.com/uc?export=view&id=1rxRvY4kRjfn3bxza30gyASyEWQ2SNuD0",
            "https://drive.google.com/uc?export=view&id=1MN_f6XFONXY9NmbFeHT1kESDmR-KncTv",
            "https://drive.google.com/uc?export=view&id=1euqNJ0S4GVsCkGU9uXiFxl_ShC_OMr5w"
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
                "kesan": "Abang ini asik diajak ngobrol, baik juga",
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
                "kesan": "kakaknya ramah dan baik",
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
                "kesan": "Kakaknya asik dan baik",
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
                "kesan": "kakaknya asik dan ramah",
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
                "kesan": "kakaknya ramah dan baik",
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
                "kesan": "abangnya asik, seru orangnya",
                "pesan": "semangat terus kuliahnya bang semangat menugas"
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
                "kesan": "Abangnya ramah dan baik",
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
                "kesan": "kakaknya baik, seru orangnya",
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
                "kesan": "Abangnya ramah dan asik",
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
                "kesan": "Kakaknya ramah dan baik",
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
                "kesan": "kakaknya ramah dan baik",
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
                "kesan": "Abangnya ramah dan asik",
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
                "kesan": "Kakaknya baik dan asik",
                "pesan": "semoga sehat selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    Internal()

elif menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [
                "https://drive.google.com/uc?export=view&id=1Bs-Y75g3igULoWFcrbu7ikCB5XakH8hC",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1Tpg1jdNUFYqGMUBxMX_KwZarlgifqLfj",
                "https://drive.google.com/uc?export=view&id=1fDt0AVKuws1bX0aq3EjTViSJl-KNk3-3",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1kueeISvFZyQOd6fX1URYVZxqLvAdABp2",
                "https://drive.google.com/uc?export=view&id=1uA_MWaO4Dd20poeZBmAYzQaxZnTZsctT",
                "https://drive.google.com/uc?export=view&id=1Q-EllJO8bz_FdPDlQlBnxjG6d3Mm6qsZ",
                "https://drive.google.com/uc?export=view&id=1-RMw7N6B4m4L_2FxJwb7x45yXxBTWkRU",
                "https://drive.google.com/uc?export=view&id=1KxmQvMjJVHyI7MlikHSQiNLP3Tvcm_Gj",
                "https://drive.google.com/uc?export=view&id=1UCEWSOsq2HZKw1Ini3nNDob--n1WC7ym",
                "https://drive.google.com/uc?export=view&id=11OjnyXnwIg-jrYMZEIxp6DGmWKE1UpCl",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1hUoIqtGfm7x5cEqNLxMlXeOGDDuV_Gpn",  
                "https://drive.google.com/uc?export=view&id=1dMc1lFjg3TfplBf6V_BvKGK90HbCPOxj",
                "https://drive.google.com/uc?export=view&id=1cmtWbGcvDGgR_YLc_Iy76Hn9XWSEeK0r",
                "https://drive.google.com/uc?export=view&id=1BUE7aQkZjOo_MwIE_jGHSXkPIFNufMNF",
                "https://drive.google.com/uc?export=view&id=1UaGFu3xHAl5BEWZ9h-54ykqhewAbmapH",
                "https://drive.google.com/uc?export=view&id=1HGIXb0PMEJTX_-9ttJmwtk-UKIOq0gex",
                "https://drive.google.com/uc?export=view&id=10gCoI6o2D93oQLsP7O5Fr7P9tk8yVbyy",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
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
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-Jalan",
                "sosmed": "@bylaash",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Khoirul",
                "nim": "1234500",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal": "Ikut kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi idol cepuyuh tayun",
                "sosmed": "@adindaadma",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca Wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "666 Pohon Mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "-",
                "asal": "Balam balam",
                "alamat": "Nelson Piquet",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "sosmed": "@jaldii._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton Thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1O4_Ptsnnd9mMlx4u70sqBZmfZ-eoob-2",
            "https://drive.google.com/uc?export=view&id=1b34TD0lIacrg8pH7puMyIAZnxOQcu9r1",
            "https://drive.google.com/uc?export=view&id=13tPuz5fVRBgExU5DHYS26Rgot3aQ6zE3",
            "https://drive.google.com/uc?export=view&id=18vwRWnZuEPAoRceqbcapDw7bHm2pyHIX",
            "https://drive.google.com/uc?export=view&id=1sdtKCSGsHX2HZfhpWi_chHSFy7oQajWS",
            "https://drive.google.com/uc?export=view&id=1K5-HsZeSTbxxdpnDNdlTUY2ZShURW5QA",
            "https://drive.google.com/uc?export=view&id=1Uthp-R3KTwNfI9WzZjSELRUQa3MbeyST",
            "https://drive.google.com/uc?export=view&id=1YOdjdhBR72A6VW865XGOrNl1i2ISBsTl",
            "https://drive.google.com/uc?export=view&id=1oacq9xOyNE3w7IiBNN11dVI7mowLTQ0r",
            "https://drive.google.com/uc?export=view&id=1iZGn72yJQ-ul8G6lQ94YGNVRiMLZ-n3F",
            "https://drive.google.com/uc?export=view&id=1sNFfzWf0NPZmxt37S639QQX0P0YvB2ud",
            "https://drive.google.com/uc?export=view&id=1EOFvM9WJExj-BsGbHHHLwpH3_Rw2xvYF",
            "https://drive.google.com/uc?export=view&id=16kl-lbhMMkW41O_l9kXvtk-Jnx3QMHav",
            "https://drive.google.com/uc?export=view&id=1NacAoueMF33OtC47IFo3yjKx25Nkq7Gc",
            "https://drive.google.com/uc?export=view&id=18rWM2jJNXmndbT4kYLA8boeTkJIAEUJu",
            "https://drive.google.com/uc?export=view&id=1Exq6FaIWVSPcHqlW5hahzQaJ3NjSRY6w",
            "https://drive.google.com/uc?export=view&id=1W0wWiSevZuxttUIYWfyqqxqyRxxo4B8e",
        ]

        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21",
                "asal": "Sibologa",
                "alamat": "Pudan Kos",
                "hobbi": "Berduaan sama pacar",
                "sosmed": "vany.salsabilaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal": "Tanah Indonesia",
                "alamat": "Samping Rumah Henry",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Dalam pasar",
                "hobbi": "Teriak",
                "sosmed": "Tanya Reno",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal": "Paninjauan Solok, Sepuluh Kota, Sumatera Barat, Indonesia",
                "alamat": "Blok D 77, Jalan Manggis 8, Pemda, Jati Agung, Lampung Selatan, Lampung, Indonesia",
                "hobbi": "Mancing",
                "sosmed": "@ykeall",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "",
                "umur": "124450021",
                "asal": "Tanya Biwa",
                "alamat": "Kontrakan Hijau",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesarozora",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Kampung lama",
                "alamat": "Dibawah turunan",
                "hobbi": "Makan gorengan",
                "sosmed": "yudiameilianaa_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450016",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Sebelah kanan rumah Henry",
                "hobbi": "Ngecek makan ayam",
                "sosmed": "_haikaaall",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Kost Owen",
                "alamat": "Warteg Bahari",
                "hobbi": "Belajar naik motor ke Bandung 94",
                "sosmed": "putrimannaa",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal": "Johor Baru",
                "alamat": "Depan Mie Gacoan",
                "hobbi": "Main gitar",
                "sosmed": "queentanaabila",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "19",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek orang",
                "sosmed": "desmanhall_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Sukarame",
                "alamat": "Lampung",
                "hobbi": "Makan Ice",
                "sosmed": "azzelytn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cenderawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "charrlnn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Sidingkalang",
                "alamat": "Di sebelah kost Haikal",
                "hobbi": "Jadi nelayan",
                "sosmed": "jemarrro",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal": "Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "n.bila_a",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Kota Ikan",
                "alamat": "Disamping Kost Afdal",
                "hobbi": "Memancing",
                "sosmed": "dearfkvmfl",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "avi.nhr",
                "kesan": "",
                "pesan": ""
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    psda()


elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=173mbtcpJUHY1--Ein2qCDvXx-eajxNad",
            "https://drive.google.com/uc?export=view&id=16ydAnUuyewAExgBR-5TKMXot8fP3Fuvn",
            "https://drive.google.com/uc?export=view&id=19GoDyO-xuEioLshedM-FI2XZ6VWtRf2E",
            "https://drive.google.com/uc?export=view&id=10Nnxf6KN4waGUqbKRvc25X3nzpGQcf38",
            "https://drive.google.com/uc?export=view&id=1LnDBe5bF1IXNcb6KXHe3tuTgaWhiaPw4",
            "https://drive.google.com/uc?export=view&id=1A6YRzTMhLHbzCu0Dl7ir0AJb818Zsi7a",
            "https://drive.google.com/uc?export=view&id=1U11AW-cfbvhBdfNbz1LA7r5ph-lWWquv",
            "https://drive.google.com/uc?export=view&id=1vBTkCOtqf6jv0EIu-DFIHoTCDg3YFLHb",
            "https://drive.google.com/uc?export=view&id=1ybQP-Gc9yfnOoV8kZML36Xb7AfOx4ZjQ",
            "https://drive.google.com/uc?export=view&id=171t2AyFNkxYcsKHNygb4oZOpdcDU7EcN",
            "https://drive.google.com/uc?export=view&id=18nhpYzmbQ-s4fK16acGLtMofQD0ArhVn",
            "https://drive.google.com/uc?export=view&id=1CIXwKMSG5F9fhLg0-aZYLSPX3-sYnB4J",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]

        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kuala Lumpur",
                "alamat": "GH",
                "hobbi": "Ke Cafe",
                "sosmed": "@iamridhomanik",
                "kesan": "Abangnya lucu, suka becanda, kece tapi",
                "pesan": "Semoga skripsinya ez bang"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Sikawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin Lagu Pilihlah Aku dari Krisdayanti",
                "sosmed": "@j_eesie",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Semoga sehat selalu kak"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api Baleg di tiktok",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya keren, jadi pemateri waktu pra kader, public speakingnya bagus",
                "pesan": "Semoga sukses selalu bang"
            },
            {
                "nama": "GH Mikael Niko AS",
                "nim": "124450025",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "Abangnya asik diajak ngobrol, nyambung juga obrolannya, baik abangnya",
                "pesan": "Semoga sehat selalu bang, makin sukses, makin hebat"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Semoga dimudahkan kak, sehat selalu juga"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "@givarooo",
                "kesan": "Asal abangnya sama kaya saya, asik abangnya, baik juga",
                "pesan": "Semoga dimudahkan urusan skripsinya bang"
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "18",
                "asal": "Kepulauan Mentawai, Lampung",
                "alamat": "Kadang di kos Sekar, kadang di kos Putri",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "My mentor, kakaknya baik, pengertian, suka sharing sama ngebantu juga",
                "pesan": "Semoga dikasih kesehatan terus kak, kuliahnya lancarnya, terus jadi orang sukses"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City Earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Sehat selalu kak, semoga kuliahnya dimudahkan"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Bernyanyi",
                "sosmed": "@jeremia_hm",
                "kesan": "Abangnya asik sama lucu, ngebantuin waktu materi persidangan juga",
                "pesan": "Semoga kuliahnya lancar bang"
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge gym dan koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Abangnya unik, lucu juga, pemateri waktu materi persidangan",
                "pesan": "Sehat sehat bang semoga makin berotot"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Main sama Kak Nisa",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya ramah, baik juga, jadi korlap kalau rangkaian",
                "pesan": "Sehat selalu kak"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@nshaysk",
                "kesan": "",
                "pesan": ""
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    baleg()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bPrQhcmeSEkxGkeQJE_7EpCcjfJ9vvpb",
            "https://drive.google.com/uc?export=view&id=13VRWIkJrKuU7TD6r7vmohehCmY8PGLor",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_townfyl4tFag-Z7eEKs0HwRTJuYWBoN",
            "https://drive.google.com/uc?export=view&id=172DGmzznEDAh5_S6x8tv0vluDw1CQQm4",
            "https://drive.google.com/uc?export=view&id=16BgKTPKgwvLGHroxvaHm6Lwshd6n2alP",
            "https://drive.google.com/uc?export=view&id=1OUop-5QusRb7pmtdoQ4nLE1dGs-PVxFv",
            "https://drive.google.com/uc?export=view&id=1TkwDH41Zma5vhP15LSJnRRWn19NjDe2F",
            "https://drive.google.com/uc?export=view&id=1LfEQPaZJI3TUtT-HVOBHFH_G2Vlr5FPx",
            "https://drive.google.com/uc?export=view&id=1Nyhqh92yfTBe1pxvwPDkwcOXGtmV2SRO",
            "https://drive.google.com/uc?export=view&id=10MQnsEijYtfcWIy3GuIsqir-wwyeLP7r",
            "https://drive.google.com/uc?export=view&id=1qf_EwI_DdY1lPmm1HE-WaXDIyjb9eez7",
            "https://drive.google.com/uc?export=view&id=1XnkXLM4nErojbW-LYbmuMpv_WuNPrlRE",
            "https://drive.google.com/uc?export=view&id=1CbxAMnSog6GM5dFCIj51VeNV8SJgdYZ_",
            "https://drive.google.com/uc?export=view&id=13qbVF3G94yRRCoUSYms9Ovmkc7LfOn_4",
            "https://drive.google.com/uc?export=view&id=1E1eBbagFzg2Yft1KfCY5-RCV0YLcxiF9",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1clJ60u2Sfb39GnW6VwtfG97NaDZOqImt",
            "https://drive.google.com/uc?export=view&id=19ZxbdUnRTEB3jWLTiSsZhYfr7m8Qu7jF",
            "https://drive.google.com/uc?export=view&id=1UajqpnzaAorXXqieBzA7pvb3LchSgg38",
            "https://drive.google.com/uc?export=view&id=1k50OYo8ie2nBDxSoKaLDcOhpit0Gvwxc",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",    
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "124450104",
                "umur": "21",
                "asal": "Balam",
                "alamat": "-5.386541,105.262255",
                "hobbi": "Nyapu wico lantai 2, lantai 3, lantai 4, lantai 5 gedung F",
                "sosmed": "@biyokcb",
                "kesan": "Kece abangnya, kalau jadi pemateri asik, mirip mamasku di kampung",
                "pesan": "Sehat selalu bang, semoga skripsinya lancar, terus jadi sukses"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Kakaknya lucu, asik, baik juga",
                "pesan": "Semoga kuliahnya gampang kak"
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Abangnya keren, hebat juga",
                "pesan": "Rest in Peace bang"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Baik abangnya, keren juga",
                "pesan": "Sukses lalu bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "17",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga sehat selalu kak, dimudahkan urusannya"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling skate",
                "sosmed": "risarmdna",
                "kesan": "Kakaknya baik",
                "pesan": "Semoga kuliahnya dimudahkan kak"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton film action Tom Cruise, Liam Neeson, Jackie Chan",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya asik, baik juga",
                "pesan": "Semoga gampang urusan kuliahnya kak"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124540119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Main alat musik",
                "sosmed": "krnylee",
                "kesan": "Kakaknya baik, ramah juga",
                "pesan": "Smeoga disehatkan terus kak"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya keren",
                "pesan": "Semoga sehat terus bang"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Kakaknya asik, dulu satu kosan sama irfan",
                "pesan": "Semoga sehat terus kak"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main ML",
                "sosmed": "fadyaizzatul_",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semoga urusan kuliahnya dimudahkan kak"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@from_loviaa",
                "kesan": "Kakaknya baik",
                "pesan": "Sehat terus ya kak"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Kotabaru",
                "hobbi": "Main game, tidur, dengerin musik",
                "sosmed": "aruccy_",
                "kesan": "Abang NIMku, baik abangnya",
                "pesan": ""
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Menunda Pekerjaan",
                "sosmed": "sher_renna",
                "kesan": "Kakaknya cantik kata zaki, kakak NIMnya soalnya",
                "pesan": "Sehat terus kak semoga kuliahnya gampang"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya asik, jadi pemateri juga",
                "pesan": ""
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "faizaanjanii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Gathfan Nadhif Ali",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@gathfannad",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, LamTim",
                "hobbi": "Ngoding & Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumsel",
                "alamat": "Sukarame",
                "hobbi": "Nari",
                "sosmed": "@melva_fbrt",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Stafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syaafiqui",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "2000",
                "asal": "Kota Bumi",
                "alamat": "Rajabasa",
                "hobbi": "Nongkrong",
                "sosmed": "henryferdianto",
                "kesan": "",
                "pesan": ""
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()

elif menu == "Departemen Minbak":
    def minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
            "https://drive.google.com/uc?export=view&id=1rjTflKUaeaFwZsTT56xPwTughgrEruKM",
        ]

        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450009",
                "umur": "21",
                "asal": "Sulawesi Selatan",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Main gaplek",
                "sosmed": "@kevinaj_",
                "kesan": "Abangnya kalem, tapi asik, kece juga",
                "pesan": "Sehat terus bang",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki Gunung",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga skripsinya nanti lancar kak",
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Abangnya kalem sama baik",
                "pesan": "Sukses selalu ya bang",
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "sosmed": "@aayuandriani_",
                "kesan": "Kakaknya satu asal sama saya, baik kakaknya",
                "pesan": "Sehat selalu kak, semoga dimudahkan seluruh semesternya",
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450024",
                "umur": "21",
                "asal": "Bandung",
                "alamat": "Way Kandis",
                "hobbi": "Main Futsal",
                "sosmed": "@dafaelpriza_",
                "kesan": "Keren abangnya, kalem, asik",
                "pesan": "Semoga dimudahkan segala urusan bang",
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Muter-muter",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakaknnya baik, satu daerah asal juga sama aku",
                "pesan": "Semoga kedepannya dimudahkan selalu kak",
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal": "Lampung Tengah",
                "alamat": "JL. Pulau Damar",
                "hobbi": "Nemenin Bang Ridwan nonton tinju",
                "sosmed": "@afdall.03",
                "kesan": "Abangnya ramah, asik juga",
                "pesan": "Semoga sehat terus bang",
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@sllbnzw_",
                "kesan": "Kakaknya ramah sama baik",
                "pesan": "Sehat terus kak, semoga dilancarkan segala urusan",
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton tinju",
                "sosmed": "@mridwaan__",
                "kesan": "Abangnya baik, asik juga",
                "pesan": "Semoga skripsinya lancar bang",
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nemenin Bryan nonton tinju",
                "sosmed": "@andra.lhm",
                "kesan": "Asik abangnya, diajak ngobrol juga asik",
                "pesan": "Semoga kuliahnya lancar terus bang",
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Abangnya kalem, asik juga",
                "pesan": "Sehat terus bang",
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Main beiblet",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya lucu, ngomongin ff mulu",
                "pesan": "Semangat terus bang, semoga sukses",
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Memasak",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakaknya baik sama ramah",
                "pesan": "Semoga dilancarkan keinginan dan kemauannya kak",
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Nusa Tenggarang Barat",
                "alamat": "Rajabasa",
                "hobbi": "Nebang Pohon",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya baik, asik juga",
                "pesan": "Sehat selalu kak",
            },
            {
                "nama": "Muhammad Rafka Fatih Al Fatih Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya baik sama kalem",
                "pesan": "Semoga kuliahnya lancar terus jadi orang sukses bang",
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    minbak()