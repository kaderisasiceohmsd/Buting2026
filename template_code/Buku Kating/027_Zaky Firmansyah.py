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
            "https://drive.google.com/uc?export=view&id=16Xahmwz8hcC93zT9_PmNEQCy57S2azzK",
            "https://drive.google.com/uc?export=view&id=17uQGf-d6eLSGvIbRHpUE4svLTB-H7wPJ",
            "https://drive.google.com/uc?export=view&id=10XHzrxfBiyBlXAQimCtX-GdJyWeTXKV6",
            "https://drive.google.com/uc?export=view&id=1aXgXCL7sZ4e3DPMHw-P5NiQftbuOZPPk",
            "https://drive.google.com/uc?export=view&id=1b90e-qA9oqgcwYgpRB8w83FTFbXPFH9M",
            "https://drive.google.com/uc?export=view&id=1kwObejpCBPxCAiLcrQYgP1vQMKZDsqPa",
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
                "kesan": "abang ginda walaupun seorang kahim tapi tetap humble dan ramah banget.",
                "pesan": "Semoga semua rencana ke depannya berjalan lancar."
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal": "Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "abang aqil orangnya humble, ramah, dan selalu memberikan arahan yang baik.",
                "pesan": "Tetap semangat mengejar hal-hal yang ingin dicapai."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kelihatan punya energi positif saat berinteraksi.",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran dalam setiap urusan."
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Orangnya seru dan bisa mencairkan suasana.",
                "pesan": "Jangan lupa meluangkan waktu untuk istirahat di tengah kesibukan."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu Kesekjenan",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kesan pertama yang diberikan cukup menyenangkan.",
                "pesan": "Semoga banyak hal baik datang ke depannya."
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Airan",
                "hobbi": "Mintain Duit",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Cara berkomunikasinya nyaman dan mudah dipahami.",
                "pesan": "Sukses selalu untuk setiap langkah dan pilihan yang diambil."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lsmich-Bo22k_ozE2BQ7o72zNBSZpqyw",
            "https://drive.google.com/uc?export=view&id=1lIW4hpLF_alMe6FH9j7qPWVehhXahpVd",
            "https://drive.google.com/uc?export=view&id=1BgTd0vBo_RR4xuuI4cWn4O71eyIw3wYg",
            "https://drive.google.com/uc?export=view&id=1addo9tCKoBagMdcJtUr0uz3LB4QiRcOz",
            "https://drive.google.com/uc?export=view&id=1r-zU25yuAIbwu-Ur2lE1lZYK1xLKmnhN",
            "https://drive.google.com/uc?export=view&id=1ddJwRSxyv134tk3CFNKt5OT30utwl7y0",
            "https://drive.google.com/uc?export=view&id=1-wlMI49EeKcpq5aAhSLHeEYvleCqS5e4",
            "https://drive.google.com/uc?export=view&id=1daTVUupTreHbilUcSlQYHrc326YJagVn",
            "https://drive.google.com/uc?export=view&id=1G_EKJA3MFJ2Rx9RitAchXczNR4tVyQ6i",
            "https://drive.google.com/uc?export=view&id=1WSyKlsEXctpkl6xGiRkvONg1eY54mrLt",
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
                "kesan": "Orangnya terlihat terbuka dan mudah bergaul.",
                "pesan": "Semoga semua usaha yang dilakukan membuahkan hasil terbaik."
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Tanya Bapas",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "Punya pembawaan yang tenang dan menyenangkan.",
                "pesan": "Tetap jadi diri sendiri dan terus berkembang menjadi lebih baik."
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah Kamar Biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Interaksinya terasa santai dan tidak canggung.",
                "pesan": "Semoga urusan sehari-hari selalu dimudahkan."
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Orangnya asik dan memberi kesan yang baik.",
                "pesan": "Terus semangat belajar dan mencoba hal-hal baru."
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "Kelihatan ramah kepada orang-orang di sekitarnya.",
                "pesan": "Semoga apa yang sedang diperjuangkan bisa tercapai."
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia,h_264",
                "kesan": "Pembawaannya positif dan membuat suasana lebih nyaman.",
                "pesan": "Jangan menyerah saat menghadapi tantangan, tetap jalani pelan-pelan."
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasi Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Orangnya komunikatif dan mudah diajak berdiskusi.",
                "pesan": "Semoga ke depannya semakin banyak pengalaman berharga."
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Lampung Timur",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kesan yang diberikan sederhana, ramah, dan menyenangkan.",
                "pesan": "Tetap jaga kesehatan dan semangat dalam menjalani aktivitas."
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@nadyaanjaani",
                "kesan": "Terlihat punya semangat yang baik dalam beraktivitas.",
                "pesan": "Semoga setiap proses membawa pelajaran yang bermanfaat."
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca Buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Orangnya cukup humble dan mudah diajak berinteraksi.",
                "pesan": "Sukses terus dan semoga selalu dikelilingi hal-hal baik."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k5paZx2mHHg6sz0YJN_FNuDtK9d-t-oF",
            "https://drive.google.com/uc?export=view&id=1mDJqGoTvprfzvcDh9KHNDa2Q5H_ss7g7",
            "https://drive.google.com/uc?export=view&id=1K0g3gWqjXagM6OU7QFVOl63X1OeYpLpf",
            "https://drive.google.com/uc?export=view&id=1DffebJ4_rh3tfTB-iJACy8Rb_DeTJhNk",
            "https://drive.google.com/uc?export=view&id=15IJGmxu3EvJwAte0x-tZAXc5lTGo04ld",
            "https://drive.google.com/uc?export=view&id=1fH_QUO6S996l_vKFiqxHss8UzXrTmqkc",
            "https://drive.google.com/uc?export=view&id=1gAdMaJilFrDXUjKDEQPHSqDNjFufHe-g",
            "https://drive.google.com/uc?export=view&id=193kxQZNHDDh_IXVvlE5zEON56bz3rLmH",
            "https://drive.google.com/uc?export=view&id=1DN53h0lsYedQzU-0SuUOO1nqnBw_uhpN",
            "https://drive.google.com/uc?export=view&id=1I6oJxVUVt3foYppdwWXWspidvJq5qKTs",
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
                "kesan": "Bisa membawa suasana jadi lebih santai.",
                "pesan": "Semoga langkah selanjutnya dipenuhi kesempatan yang baik."
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kelihatan menyenangkan saat bekerja bersama.",
                "pesan": "Terus berkembang dan jangan takut mencoba sesuatu yang baru."
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal": "Depok",
                "alamat": "Belakang PB",
                "hobbi": "Ngumpulin data sama nonton Marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Orangnya punya cara bergaul yang baik.",
                "pesan": "Semoga semua target bisa tercapai satu per satu."
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124550012",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sebelah kost Ayake",
                "hobbi": "Scroll Facebook",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "Interaksinya terasa hangat dan menyenangkan.",
                "pesan": "Tetap rendah hati dan pertahankan hal-hal baik yang sudah ada."
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124550016",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Menonton Film",
                "sosmed": "@lay.inr_",
                "kesan": "Pembawaannya bersahabat dan mudah diterima.",
                "pesan": "Semoga selalu diberi kemudahan dalam menjalani berbagai kegiatan."
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Orangnya terlihat percaya diri saat berkomunikasi.",
                "pesan": "Jangan lupa menikmati proses sambil terus berusaha."
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Padang, Sumatera Barat",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kesan yang didapat adalah pribadi yang ramah.",
                "pesan": "Semoga hari-hari ke depan terasa lebih menyenangkan."
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Kost The Icon",
                "hobbi": "Belajar",
                "sosmed": "@anadiacrn_",
                "kesan": "Kelihatan bisa bekerja sama dengan baik.",
                "pesan": "Terus lakukan yang terbaik sesuai kemampuan dan tujuan."
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "nim": "123450062",
                "umur": "21",
                "asal": "Oku, Sumatera Selatan",
                "alamat": "Airan",
                "hobbi": "Godain cewe bang Homey",
                "sosmed": "@pomest_",
                "kesan": "kenal bang pom dari awal basket, dari awal udah merangkul adik adik angkatan 25, dan selalu memberikan arahan yang baik.",
                "pesan": "Semoga semua kerja kerasnya memberikan hasil yang memuaskan."
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124550008",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Samping Kost Rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "Cara berinteraksinya terasa natural dan tidak dibuat-buat.",
                "pesan": "Tetap semangat meskipun prosesnya kadang tidak mudah."
            },
            {
                "nama": "Anggun Nita",
                "nim": "124550009",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Menonton Kartun",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Orangnya mudah diajak ngobrol dalam berbagai suasana.",
                "pesan": "Semoga selalu punya alasan untuk tersenyum dan bersyukur."
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Margo Lestari",
                "hobbi": "Lagi suka olahraga",
                "sosmed": "@dellaansaftr",
                "kesan": "Pembawaannya cukup menarik dan menyenangkan.",
                "pesan": "Jaga semangat, kesehatan, dan keseimbangan dalam beraktivitas."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tITWmfUxOFRcryh7LD5_g4L1JHW76fF8",
            "https://drive.google.com/uc?export=view&id=1_ps5OWTxMaSkP5kNMXDL9UzVqNBpN1zh",
            "https://drive.google.com/uc?export=view&id=1-7xVmXtXxEhHtvFisvtzETtJvQ1FJmeB",
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
                "kesan": "Kelihatan punya sikap yang baik saat berinteraksi.",
                "pesan": "Semoga semakin banyak kesempatan baik yang datang."
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Orangnya memberi kesan yang positif dan mudah diingat.",
                "pesan": "Yang terbaik untuk semua rencana dan perjalanan ke depannya."
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal": "Medan, Jakarta Utara, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Buka Tutup Laptop",
                "sosmed": "@noerruuu",
                "kesan": "Orangnya ramah dan enak diajak ngobrol.",
                "pesan": "Semoga semua rencana ke depannya berjalan lancar."
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Ballet",
                "sosmed": "@anshtsyaaql",
                "kesan": "Pembawaannya santai dan mudah akrab.",
                "pesan": "Tetap semangat mengejar hal-hal yang ingin dicapai."
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing emosi",
                "sosmed": "felisyanbl",
                "kesan": "Kelihatan punya energi positif saat berinteraksi.",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran dalam setiap urusan."
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Dukung silver arrow alias mercedes",
                "sosmed": "@muh_razan_",
                "kesan": "Orangnya seru dan bisa mencairkan suasana.",
                "pesan": "Jangan lupa meluangkan waktu untuk istirahat di tengah kesibukan."
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "17",
                "asal": "Bali",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan prodi",
                "sosmed": "saniayyllstr",
                "kesan": "Kesan pertama yang diberikan cukup menyenangkan.",
                "pesan": "Semoga banyak hal baik datang ke depannya."
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "3 Tahun",
                "asal": "Surga",
                "alamat": "Rumah Asha",
                "hobbi": "Ice skating",
                "sosmed": "@aallishaa.aa",
                "kesan": "Cara berkomunikasinya nyaman dan mudah dipahami.",
                "pesan": "Sukses selalu untuk setiap langkah dan pilihan yang diambil."
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Orangnya terlihat terbuka dan mudah bergaul.",
                "pesan": "Semoga semua usaha yang dilakukan membuahkan hasil terbaik."
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Mengkoding",
                "sosmed": "@bungaclrssf",
                "kesan": "Punya pembawaan yang tenang dan menyenangkan.",
                "pesan": "Tetap jadi diri sendiri dan terus berkembang menjadi lebih baik."
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "7.137 hari per hari ini",
                "asal": "Sumsel",
                "alamat": "Kafe Kali",
                "hobbi": "Bobo cantik",
                "sosmed": "@difanyhsa",
                "kesan": "Interaksinya terasa santai dan tidak canggung.",
                "pesan": "Semoga urusan sehari-hari selalu dimudahkan."
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mimpi diatas kasur",
                "sosmed": "nzlhauly_",
                "kesan": "Orangnya asik dan memberi kesan yang baik.",
                "pesan": "Terus semangat belajar dan mencoba hal-hal baru."
            },
            {
                "nama": "Raihana Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "kesan": "Kelihatan ramah kepada orang-orang di sekitarnya.",
                "pesan": "Semoga apa yang sedang diperjuangkan bisa tercapai."
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "",
                "sosmed": "@daffascript_",
                "kesan": "Pembawaannya positif dan membuat suasana lebih nyaman.",
                "pesan": "Jangan menyerah saat menghadapi tantangan, tetap jalani pelan-pelan."
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scrolling Fesbuk",
                "sosmed": "@eddel_0712",
                "kesan": "Orangnya komunikatif dan mudah diajak berdiskusi.",
                "pesan": "Semoga ke depannya semakin banyak pengalaman berharga."
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Nonton Star Wars",
                "sosmed": "luciarachel_",
                "kesan": "Kesan yang diberikan sederhana, ramah, dan menyenangkan.",
                "pesan": "Tetap jaga kesehatan dan semangat dalam menjalani aktivitas."
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Pemda",
                "hobbi": "Ngoding",
                "sosmed": "@_shaazzh",
                "kesan": "Terlihat punya semangat yang baik dalam beraktivitas.",
                "pesan": "Semoga setiap proses membawa pelajaran yang bermanfaat."
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Unila",
                "hobbi": "Tidur",
                "sosmed": "@xifasky",
                "kesan": "Orangnya cukup humble dan mudah diajak berinteraksi.",
                "pesan": "Sukses terus dan semoga selalu dikelilingi hal-hal baik."
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    medkraf()

elif menu == "Departemen Internal":
    def Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ywDqlv6xIgr7YppoGmCeIPYGPvEnwg0H",
            "https://drive.google.com/uc?export=view&id=1MO4SMWgUuzXuTxo3fM8Bbt2SLPoZxQ2n",
            "https://drive.google.com/uc?export=view&id=1KSL3NtmVjtO3qOZt9ca1203iPQUzVLVu",
            "https://drive.google.com/uc?export=view&id=1D8IfvScH15V18Kxgi_AvfSEszwA1EQRK",
            "https://drive.google.com/uc?export=view&id=1MO4SMWgUuzXuTxo3fM8Bbt2SLPoZxQ2n",
            "https://drive.google.com/uc?export=view&id=1m0hBD7YF19q7miHKGvr53REoOkTdqG2i",
            "https://drive.google.com/uc?export=view&id=1MoHsqhyEJNX313kzvKdPB8nwEF1CtJKc",
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
                "kesan": "Bisa membawa suasana jadi lebih santai.",
                "pesan": "Semoga langkah selanjutnya dipenuhi kesempatan yang baik."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kelihatan menyenangkan saat bekerja bersama.",
                "pesan": "Terus berkembang dan jangan takut mencoba sesuatu yang baru."
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Membaca Novel",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Orangnya punya cara bergaul yang baik.",
                "pesan": "Semoga semua target bisa tercapai satu per satu."
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450067",
                "umur": "22",
                "asal": "Tetangga Singapore",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Interaksinya terasa hangat dan menyenangkan.",
                "pesan": "Tetap rendah hati dan pertahankan hal-hal baik yang sudah ada."
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Indragirihulu",
                "alamat": "Samping Kuburan",
                "hobbi": "Sleep Call",
                "sosmed": "@aisyahkhair._",
                "kesan": "Pembawaannya bersahabat dan mudah diterima.",
                "pesan": "Semoga selalu diberi kemudahan dalam menjalani berbagai kegiatan."
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Semarang",
                "alamat": "Belwis",
                "hobbi": "Manjat pohon kelapa",
                "sosmed": "@cerine_ipynb",
                "kesan": "Orangnya terlihat percaya diri saat berkomunikasi.",
                "pesan": "Jangan lupa menikmati proses sambil terus berusaha."
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "21",
                "asal": "Kisaran",
                "alamat": "Pemda",
                "hobbi": "Main Biola",
                "sosmed": "@jay.saputra.tmb",
                "kesan": "Kesan yang didapat adalah pribadi yang ramah.",
                "pesan": "Semoga hari-hari ke depan terasa lebih menyenangkan."
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "Nonton asmr",
                "sosmed": "@njlanursyifa",
                "kesan": "Kelihatan bisa bekerja sama dengan baik.",
                "pesan": "Terus lakukan yang terbaik sesuai kemampuan dan tujuan."
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Badminton",
                "sosmed": "@rozakramdani_",
                "kesan": "Orangnya santai, tetapi tetap memberi kesan positif.",
                "pesan": "Semoga semua kerja kerasnya memberikan hasil yang memuaskan."
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Memasak",
                "sosmed": "@christiani8872",
                "kesan": "Cara berinteraksinya terasa natural dan tidak dibuat-buat.",
                "pesan": "Tetap semangat meskipun prosesnya kadang tidak mudah."
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "",
                "asal": "Padang",
                "alamat": "Way Kandis",
                "hobbi": "Nonton MU",
                "sosmed": "@hnfdzky_",
                "kesan": "Orangnya mudah diajak ngobrol dalam berbagai suasana.",
                "pesan": "Semoga selalu punya alasan untuk tersenyum dan bersyukur."
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Pembawaannya cukup menarik dan menyenangkan.",
                "pesan": "Jaga semangat, kesehatan, dan keseimbangan dalam beraktivitas."
            },
            {
                "nama": "Cika Adelia BR Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Samping Kuburan",
                "hobbi": "Scroll tiktok",
                "sosmed": "@cikambrn",
                "kesan": "Kelihatan punya sikap yang baik saat berinteraksi.",
                "pesan": "Semoga semakin banyak kesempatan baik yang datang."
            },
            {
                "nama": "Gustin H Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Orangnya memberi kesan yang positif dan mudah diingat.",
                "pesan": "Yang terbaik untuk semua rencana dan perjalanan ke depannya."
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nangkap lele",
                "sosmed": "@muhvinz_",
                "kesan": "Orangnya ramah dan enak diajak ngobrol.",
                "pesan": "Semoga semua rencana ke depannya berjalan lancar."
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "21",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Main game di HP temen",
                "sosmed": "@muhvinz_",
                "kesan": "Pembawaannya santai dan mudah akrab.",
                "pesan": "Tetap semangat mengejar hal-hal yang ingin dicapai."
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    Internal()

elif menu == "Departemen Eksternal":
    def Eksternal():
        gambar_urls = [
                "https://drive.google.com/uc?export=view&id=1WlywEcoDL3jxBDG9ySJhdUhB_1lHW66k",
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1OonIDqz-_Gj7MPdQ7rEyGGmUuHCWc",
                "https://drive.google.com/uc?export=view&id=1OonIDqz-_Gj7MPdQ7rEhyGGmUdOuHCWc",
                "https://drive.google.com/uc?export=view&id=1nPFX0ns53nqzauSYwqP7kQFtqc4Odr_S",
                "https://drive.google.com/uc?export=view&id=19feSAbLAqcJ4dxgBsLVMY2S9BFlxz4vS",
                "https://drive.google.com/uc?export=view&id=1NCDfW2-X368x8OHM8uuIg3IsVbowTpr0", 
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
                "kesan": "Kelihatan punya energi positif saat berinteraksi.",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran dalam setiap urusan."
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-Jalan",
                "sosmed": "@bylaash",
                "kesan": "Orangnya seru dan bisa mencairkan suasana.",
                "pesan": "Jangan lupa meluangkan waktu untuk istirahat di tengah kesibukan."
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Kesan pertama yang diberikan cukup menyenangkan.",
                "pesan": "Semoga banyak hal baik datang ke depannya."
            },
            {
                "nama": "Khoirul",
                "nim": "1234500",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Cara berkomunikasinya nyaman dan mudah dipahami.",
                "pesan": "Sukses selalu untuk setiap langkah dan pilihan yang diambil."
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Orangnya terlihat terbuka dan mudah bergaul.",
                "pesan": "Semoga semua usaha yang dilakukan membuahkan hasil terbaik."
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Punya pembawaan yang tenang dan menyenangkan.",
                "pesan": "Tetap jadi diri sendiri dan terus berkembang menjadi lebih baik."
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Interaksinya terasa santai dan tidak canggung.",
                "pesan": "Semoga urusan sehari-hari selalu dimudahkan."
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20"    ,
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Orangnya asik dan memberi kesan yang baik.",
                "pesan": "Terus semangat belajar dan mencoba hal-hal baru."
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Kelihatan ramah kepada orang-orang di sekitarnya.",
                "pesan": "Semoga apa yang sedang diperjuangkan bisa tercapai."
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal": "Ikut kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi idol cepuyuh tayun",
                "sosmed": "@adindaadma",
                "kesan": "Pembawaannya positif dan membuat suasana lebih nyaman.",
                "pesan": "Jangan menyerah saat menghadapi tantangan, tetap jalani pelan-pelan."
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Orangnya komunikatif dan mudah diajak berdiskusi.",
                "pesan": "Semoga ke depannya semakin banyak pengalaman berharga."
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kesan yang diberikan sederhana, ramah, dan menyenangkan.",
                "pesan": "Tetap jaga kesehatan dan semangat dalam menjalani aktivitas."
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca Wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Terlihat punya semangat yang baik dalam beraktivitas.",
                "pesan": "Semoga setiap proses membawa pelajaran yang bermanfaat."
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Orangnya cukup humble dan mudah diajak berinteraksi.",
                "pesan": "Sukses terus dan semoga selalu dikelilingi hal-hal baik."
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bisa membawa suasana jadi lebih santai.",
                "pesan": "Semoga langkah selanjutnya dipenuhi kesempatan yang baik."
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Kelihatan menyenangkan saat bekerja bersama.",
                "pesan": "Terus berkembang dan jangan takut mencoba sesuatu yang baru."
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "666 Pohon Mulia",
                "hobbi": "Nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "Orangnya punya cara bergaul yang baik.",
                "pesan": "Semoga semua target bisa tercapai satu per satu."
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "-",
                "asal": "Balam balam",
                "alamat": "Nelson Piquet",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Interaksinya terasa hangat dan menyenangkan.",
                "pesan": "Tetap rendah hati dan pertahankan hal-hal baik yang sudah ada."
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "sosmed": "@jaldii._",
                "kesan": "Pembawaannya bersahabat dan mudah diterima.",
                "pesan": "Semoga selalu diberi kemudahan dalam menjalani berbagai kegiatan."
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton Thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Orangnya terlihat percaya diri saat berkomunikasi.",
                "pesan": "Jangan lupa menikmati proses sambil terus berusaha."
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "Menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kesan yang didapat adalah pribadi yang ramah.",
                "pesan": "Semoga hari-hari ke depan terasa lebih menyenangkan."
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Kelihatan bisa bekerja sama dengan baik.",
                "pesan": "Terus lakukan yang terbaik sesuai kemampuan dan tujuan."
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Eksternal()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XOUoeBzyn35QF0LMDpvdTndaPd4MWBR1",
            "https://drive.google.com/uc?export=view&id=1b34TD0lIacrg8pH7puMyIAZnxOQcu9r1",
            "https://drive.google.com/uc?export=view&id=12f5eBUOc8xhnh6z9veZorPh_7ZaKeebc",
            "https://drive.google.com/uc?export=view&id=1fXoWju54cb3jUw4Z1xTBios_PNrGOMxi",
            "https://drive.google.com/uc?export=view&id=1zdmAdF1yIX9Mx6_1P5VexUUnWd6u1JMk",
            "https://drive.google.com/uc?export=view&id=1zshzwL8jTT_ix_z5L20V4_IVohgIdEZD",
            "https://drive.google.com/uc?export=view&id=1itslb_zmlxfDG0R1G-4ao5VD1tBs-5Em",
            "https://drive.google.com/uc?export=view&id=1mrZ4Si6HfQdHVP2siLC5w-i6jKf8xuc5",
            "https://drive.google.com/uc?export=view&id=1V141lNqMAiPJyJq20Sp4719IFmE92M65",
            "https://drive.google.com/uc?export=view&id=1XRjX6QCOkraCrJdsDfE5vgPWh5pAlHc4",
            "https://drive.google.com/uc?export=view&id=1VV2YUIIdDwkXTwZYzHTsnlRXnQuDU8SZ",
            "https://drive.google.com/uc?export=view&id=1O58ubQ3BrDUJHLxM8uYUrezcf47hamy8",
            "https://drive.google.com/uc?export=view&id=1NGv8x4Tf50DWdKP8crcyO1gDwq__a3IT",
            "https://drive.google.com/uc?export=view&id=1g-KpfbA-7DFCV_VUwO2jD7DOPCxTkFQF",
            "https://drive.google.com/uc?export=view&id=1iF8qtQRAUGogzngBE4LXjxNi1d4MCpSO",
            "https://drive.google.com/uc?export=view&id=1_sl2VbFV9kNvOazlbhNiNdpgP2mRQ8sF",
            "https://drive.google.com/uc?export=view&id=16e_sORTiRD3VGwxM9w2UtamjWEgLkIcF",
        ]

        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Kalianda",
                "alamat": "",
                "hobbi": "ngerjain TA",
                "sosmed": "@arientakhnl",
                "kesan": "kakaknya perempuan yang berwibaba dan tegas, tapi tetap ramah dan menyenangkan.",
                "pesan": "Semoga semua kerja kerasnya memberikan hasil yang memuaskan."
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "21",
                "asal": "Sibologa",
                "alamat": "Pudan Kos",
                "hobbi": "Berduaan sama pacar",
                "sosmed": "vany.salsabilaa",
                "kesan": "Cara berinteraksinya terasa natural dan tidak dibuat-buat.",
                "pesan": "Tetap semangat meskipun prosesnya kadang tidak mudah."
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal": "Tanah Indonesia",
                "alamat": "Samping Rumah Henry",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "sang maestro jenius dari semua kelebihan dan kesempurnaan di kaderisasi ini.",
                "pesan": "terimkasih bang sudah memikirkan begitu matang untuk perkembangan adik adikmu ini."
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Dalam pasar",
                "hobbi": "Teriak",
                "sosmed": "Tanya Reno",
                "kesan": "punya gaya yang kerenn dan cool banget.",
                "pesan": "Jaga semangat, kesehatan, dan keseimbangan dalam beraktivitas."
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal": "Paninjauan Solok, Sepuluh Kota, Sumatera Barat, Indonesia",
                "alamat": "Blok D 77, Jalan Manggis 8, Pemda, Jati Agung, Lampung Selatan, Lampung, Indonesia",
                "hobbi": "Mancing",
                "sosmed": "@ykeall",
                "kesan": "diliat dari jauh aja abangnya serem, tapi kalau udah kenal ternyata ramah banget.",
                "pesan": "Semoga semakin banyak kesempatan baik yang datang."
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Tanya Biwa",
                "alamat": "Kontrakan Hijau",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesarozora",
                "kesan": "abang paliing serem kalau udah marah, tapi tetap memberikan ilmu yang bermanfaat.",
                "pesan": "Yang terbaik untuk semua rencana dan perjalanan ke depannya."
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Kampung lama",
                "alamat": "Dibawah turunan",
                "hobbi": "Makan gorengan",
                "sosmed": "yudiameilianaa_",
                "kesan": "kalau di kader kakaknya julid tapi kalau di luar itu ramah banget.",
                "pesan": "Semoga semua rencana ke depannya berjalan lancar."
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450016",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Sebelah kanan rumah Henry",
                "hobbi": "Ngecek makan ayam",
                "sosmed": "_haikaaall",
                "kesan": "tagas dan berwibawa, tapi tetap ramah dan menyenangkan.",
                "pesan": "Tetap semangat mengejar hal-hal yang ingin dicapai."
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Kost Owen",
                "alamat": "Warteg Bahari",
                "hobbi": "Belajar naik motor ke Bandung 94",
                "sosmed": "putrimannaa",
                "kesan": "aura kak putri itu hangat dan positif bangett.",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran dalam setiap urusan."
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal": "Johor Baru",
                "alamat": "Depan Mie Gacoan",
                "hobbi": "Main gitar",
                "sosmed": "queentanaabila",
                "kesan": "keliatan dari muka kakaknya jutekk tapi ternyata ramah dan asik diajak ngobrol.",
                "pesan": "Jangan lupa meluangkan waktu untuk istirahat di tengah kesibukan."
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "19",
                "asal": "Nias",
                "alamat": "Asrama TB 3",
                "hobbi": "Ngejek orang",
                "sosmed": "desmanhall_",
                "kesan": "Kesan pertama yang diberikan cukup menyenangkan.",
                "pesan": "Semoga banyak hal baik datang ke depannya."
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Sukarame",
                "alamat": "Lampung",
                "hobbi": "Makan Ice",
                "sosmed": "azzelytn",
                "kesan": "Cara berkomunikasinya nyaman dan mudah dipahami.",
                "pesan": "Sukses selalu untuk setiap langkah dan pilihan yang diambil."
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cenderawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "charrlnn",
                "kesan": "Orangnya terlihat terbuka dan mudah bergaul.",
                "pesan": "Semoga semua usaha yang dilakukan membuahkan hasil terbaik."
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Sidingkalang",
                "alamat": "Di sebelah kost Haikal",
                "hobbi": "Jadi nelayan",
                "sosmed": "jemarrro",
                "kesan": "Punya pembawaan yang tenang dan menyenangkan.",
                "pesan": "Tetap jadi diri sendiri dan terus berkembang menjadi lebih baik."
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal": "Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "n.bila_a",
                "kesan": "Interaksinya terasa santai dan tidak canggung.",
                "pesan": "Semoga urusan sehari-hari selalu dimudahkan."
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Kota Ikan",
                "alamat": "Disamping Kost Afdal",
                "hobbi": "Memancing",
                "sosmed": "dearfkvmfl",
                "kesan": "Orangnya asik dan memberi kesan yang baik.",
                "pesan": "Terus semangat belajar dan mencoba hal-hal baru."
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "avi.nhr",
                "kesan": "Kelihatan ramah kepada orang-orang di sekitarnya.",
                "pesan": "Semoga apa yang sedang diperjuangkan bisa tercapai."
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    psda()


elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1d5EkpMSTnSYcj3Z-W2r3NBOWvywd8xcG",
            "https://drive.google.com/uc?export=view&id=12d4BBAmFXbdw4y9g4sr5mhw8sqHqBaTp",
            "https://drive.google.com/uc?export=view&id=16yoIC36G6tS7DkmGRJt6JIapsFu4r_O4",
            "https://drive.google.com/uc?export=view&id=1VTe3YJd_qInjXtzFS3R1vPNYZYE3BGSc",
            "https://drive.google.com/uc?export=view&id=1BBE5pb4tGTl5zd_x_FmstznoPUrhZTD7",
            "https://drive.google.com/uc?export=view&id=1vghOfK9orECV2XkTNQzDpaWWr_JFwclF",
            "https://drive.google.com/uc?export=view&id=1gST8aJWPL5ADUPUKKp5nXZ4lsbxybT9Q",
            "https://drive.google.com/uc?export=view&id=1gAUeybrzNj4FjkLBV-3CAbNaeFu9FHYk",
            "https://drive.google.com/uc?export=view&id=1SJT-Ygodq_M5E7SDzPqvvChE9UMxk-P4",
            "https://drive.google.com/uc?export=view&id=1bK-UcxibfLbpyNYxNx5CQ6gI6YUEZ8WR",
            "https://drive.google.com/uc?export=view&id=1xdLftDPRZQ5tPGpe3Us4JYXvFz5nw_E_",
            "https://drive.google.com/uc?export=view&id=1CIXwKMSG5F9fhLg0-aZYLSPX3-sYnB4J",
            "https://drive.google.com/uc?export=view&id=1bhCyfFuE4a33lE94FCfahrcHjNbGQCoj",
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
                "kesan": "abang paling asik di baleg, bisa buat suasana santai dan lucu tapi tetap bisa serius kalau lagi kerja",
                "pesan": "Jangan menyerah saat menghadapi tantangan, tetap jalani pelan-pelan."
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Sikawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin Lagu Pilihlah Aku dari Krisdayanti",
                "sosmed": "@j_eesie",
                "kesan": "kakaknya sangatt excited dan energinya banyak banget",
                "pesan": "Semoga ke depannya semakin banyak pengalaman berharga."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api Baleg di tiktok",
                "sosmed": "@ddharu_",
                "kesan": "style nya asik, orangnya ramah, dan pintarr banget",
                "pesan": "Tetap jaga kesehatan dan semangat dalam menjalani aktivitas."
            },
            {
                "nama": "GH Mikael Niko AS",
                "nim": "124450025",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "bang niko orangnya asik, ramah, dan gampang akrab sama orang baru",
                "pesan": "nanti mohon bimbingannya bang kalau saya udah masuk baleg"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "kakaknya kalem tapi tetap ramah.",
                "pesan": "Sukses terus dan semoga selalu dikelilingi hal-hal baik."
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "@givarooo",
                "kesan": "sosok paling kerenn di baleg, wibawa nya dapet tapi tetap santai",
                "pesan": "Semoga langkah selanjutnya dipenuhi kesempatan yang baik."
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "18",
                "asal": "Kepulauan Mentawai, Lampung",
                "alamat": "Kadang di kos Sekar, kadang di kos Putri",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "mentorr kebanggaan ghwehh, segala pujian rerbaik untuk Kak Nissa pokoknya",
                "pesan": "Terus berkembang dan jangan takut mencoba sesuatu yang baru."
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City Earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "kak hani keliatan penyabar banget yaa, cantik juga",
                "pesan": "Semoga semua target bisa tercapai satu per satu."
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Bernyanyi",
                "sosmed": "@jeremia_hm",
                "kesan": "suara abang keren kaya orkestra gitu",
                "pesan": "Tetap rendah hati dan pertahankan hal-hal baik yang sudah ada."
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jabar",
                "alamat": "Kota Baru",
                "hobbi": "lari",
                "sosmed": "@monica_tjg",
                "kesan": "Dari awal kenal kak monica orangnya ramah, dan murah senyum.",
                "pesan": "Semoga selalu diberi kemudahan dalam menjalani berbagai kegiatan."
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge gym dan koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "kenal bang jona waktu main basket bareng, emang dari dulu udahh asikk",
                "pesan": "Jangan lupa menikmati proses sambil terus berusaha."
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Main sama Kak Nisa",
                "sosmed": "@sekardnwp",
                "kesan": "awal nya keliatan galak karena siring liat di kader, tapi ternyata kakaknya asikkk",
                "pesan": "Semoga hari-hari ke depan terasa lebih menyenangkan."
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa Angin",
                "sosmed": "@nshaysk",
                "kesan": "kak wawa orangnya cantikk, suaranya bagus, dan asik diajak ngobrol",
                "pesan": "Terus lakukan yang terbaik sesuai kemampuan dan tujuan."
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
                "kesan": "Orangnya santai, tetapi tetap memberi kesan positif.",
                "pesan": "Semoga semua kerja kerasnya memberikan hasil yang memuaskan."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Cara berinteraksinya terasa natural dan tidak dibuat-buat.",
                "pesan": "Tetap semangat meskipun prosesnya kadang tidak mudah."
            },
            {
                "nama": "Fadil Prasetyo",
                "nim": "123450048",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Orangnya mudah diajak ngobrol dalam berbagai suasana.",
                "pesan": "Semoga selalu punya alasan untuk tersenyum dan bersyukur."
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Pembawaannya cukup menarik dan menyenangkan.",
                "pesan": "Jaga semangat, kesehatan, dan keseimbangan dalam beraktivitas."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "17",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Tidur",
                "sosmed": "@violaadrtr_",
                "kesan": "Kelihatan punya sikap yang baik saat berinteraksi.",
                "pesan": "Semoga semakin banyak kesempatan baik yang datang."
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling skate",
                "sosmed": "risarmdna",
                "kesan": "Orangnya memberi kesan yang positif dan mudah diingat.",
                "pesan": "Yang terbaik untuk semua rencana dan perjalanan ke depannya."
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton film action Tom Cruise, Liam Neeson, Jackie Chan",
                "sosmed": "@vunnycaa",
                "kesan": "Orangnya ramah dan enak diajak ngobrol.",
                "pesan": "Semoga semua rencana ke depannya berjalan lancar."
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124540119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Main alat musik",
                "sosmed": "krnylee",
                "kesan": "Pembawaannya santai dan mudah akrab.",
                "pesan": "Tetap semangat mengejar hal-hal yang ingin dicapai."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Kelihatan punya energi positif saat berinteraksi.",
                "pesan": "Semoga selalu diberi kesehatan dan kelancaran dalam setiap urusan."
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Orangnya seru dan bisa mencairkan suasana.",
                "pesan": "Jangan lupa meluangkan waktu untuk istirahat di tengah kesibukan."
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main ML",
                "sosmed": "fadyaizzatul_",
                "kesan": "Kesan pertama yang diberikan cukup menyenangkan.",
                "pesan": "Semoga banyak hal baik datang ke depannya."
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@from_loviaa",
                "kesan": "Cara berkomunikasinya nyaman dan mudah dipahami.",
                "pesan": "Sukses selalu untuk setiap langkah dan pilihan yang diambil."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Kotabaru",
                "hobbi": "Main game, tidur, dengerin musik",
                "sosmed": "aruccy_",
                "kesan": "Orangnya terlihat terbuka dan mudah bergaul.",
                "pesan": "Semoga semua usaha yang dilakukan membuahkan hasil terbaik."
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Menunda Pekerjaan",
                "sosmed": "sher_renna",
                "kesan": "Kakak NIM 027, Orangnya cantik dan manis,ramah, murah senyum, dan asik diajak ngobrol.",
                "pesan": "Tetap jadi diri sendiri dan terus berkembang menjadi lebih baik."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Interaksinya terasa santai dan tidak canggung.",
                "pesan": "Semoga urusan sehari-hari selalu dimudahkan."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "faizaanjanii",
                "kesan": "Orangnya asik dan memberi kesan yang baik.",
                "pesan": "Terus semangat belajar dan mencoba hal-hal baru."
            },
            {
                "nama": "Gathfan Nadhif Ali",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "@gathfannad",
                "kesan": "Kelihatan ramah kepada orang-orang di sekitarnya.",
                "pesan": "Semoga apa yang sedang diperjuangkan bisa tercapai."
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang, LamTim",
                "hobbi": "Ngoding & Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Bang hafidz orangnya asik dan mudah bergaul.",
                "pesan": "Jangan menyerah saat menghadapi tantangan, tetap jalani pelan-pelan."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "abangnya berotot dan pintar banget",
                "pesan": "Semoga ke depannya semakin banyak pengalaman berharga."
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumsel",
                "alamat": "Sukarame",
                "hobbi": "Nari",
                "sosmed": "@melva_fbrt",
                "kesan": "Kesan yang diberikan sederhana, ramah, dan menyenangkan.",
                "pesan": "Tetap jaga kesehatan dan semangat dalam menjalani aktivitas."
            },
            {
                "nama": "Muhammad Stafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@syaafiqui",
                "kesan": "Terlihat punya semangat yang baik dalam beraktivitas.",
                "pesan": "Semoga setiap proses membawa pelajaran yang bermanfaat."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "2000",
                "asal": "Kota Bumi",
                "alamat": "Rajabasa",
                "hobbi": "Nongkrong",
                "sosmed": "henryferdianto",
                "kesan": "Orangnya cukup humble dan mudah diajak berinteraksi.",
                "pesan": "Sukses terus dan semoga selalu dikelilingi hal-hal baik."
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()
