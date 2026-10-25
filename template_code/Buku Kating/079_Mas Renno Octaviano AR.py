import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
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
            "nav-link-selected": {"background-color": "#8D4C06"},
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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"Jabatan: {data_list[i]['Jabatan']}")
            st.write(f"NIM: {data_list[i]['Nim']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-iCmlRJteY4p3MHy3IeVmmcxSZd3vr1x",
            "https://drive.google.com/uc?export=view&id=1QA4r4oO44y8va91G5kMJJHAQVfhXb8Y_",
            "https://drive.google.com/uc?export=view&id=1fhmHXpkS_0ZgIUtXZZQcbIc5-RW1wkXl",
            "https://drive.google.com/uc?export=view&id=1tsZv6xj1ERjup9ZEMalw_TzM-qDEUj8V",
            "https://drive.google.com/uc?export=view&id=1VAAzOl3j52bsMVaQG3XV9OCJli98cyh-",
            "https://drive.google.com/uc?export=view&id=1FqViu-03d1cQlOodvq5bbbAgp2tWSAYd",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Jabatan" : "Ketua Himpunan",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abang himku ini orangnya kalem dan seru jugaa kalo diajak ngobrol lah",
                "Pesan":"Semoga selalu diberikan kesehatan dan dipermudah yaa bang dari semua urusannya"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Jabatan" : "Sekretaris Jenderal",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Bang Aqil ini jujur ga expect orangnya itu kalem tapi kalo ngobrol itu bisa bikin energik banget lah",  
                "Pesan":"Semoga club bola favoritnya bisa menang treble"
            },
            {
                "Nama": "Efi Defiyati",
                "Jabatan" : "Sekretaris 1",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "kak efi ini jujur ku kira dia orangnya agak galak tapi plot twistnya kalem banget dan asik sih",  
                "Pesan":"semogaa diberikan kesehatan dan nasinya selalu hangat ya kak"
            },
            {
                "Nama": "Qois Olifio",
                "Jabatan" : "Sekretaris 2",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Bang qois ini jujur aku hampir susah membedakan ama bang jay sih tapi kalo diliat emang beda orang",  
                "Pesan":"Perbanyakin makan yaa bangg biar selalu sehat dan dimudahkan ujiannya"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Jabatan" : "Bendahara 1",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakak nimku ini jujur agak shock dan banggaa karena kita punya nim yang sama namun beda 2 tingkat angkatan",  
                "Pesan":"Semoga nim 79 selalu jaya jaya"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Jabatan" : "Bendahara 2",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"Semoga dimudahkan selalu ya kak segala urusannya"
            },                                                  
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gRuoZyPNMWy8G7OhYNoEbLPQkO2oUA3G",
            "https://drive.google.com/uc?export=view&id=1Gccp7QjC-R0e0iwv3VIUS4b-iujiybSo",
            "https://drive.google.com/uc?export=view&id=1LLtnvwy7mBNK9yjqYlKnvlZVVQVlsPwh",
            "https://drive.google.com/uc?export=view&id=10t1Kl3TGsZ8KaVF9bQI39YE5j1qNxh54",
            "https://drive.google.com/uc?export=view&id=1QTBp_cxM_f6dp9x6asOgcxTRxSVynNO3",
            "https://drive.google.com/uc?export=view&id=1cHlzOuQ78ZqEpNdg5504brejeZFwCTL7",
            "https://drive.google.com/uc?export=view&id=1JlkpK6B1Z5dyeNbSQ48DT3W6NtXrmucL",
            "https://drive.google.com/uc?export=view&id=17kiBhTi8YQaahlZd8EDxpBhODbbIGFSf",
            "https://drive.google.com/uc?export=view&id=1AhXdOMSz8EgE3aseqthnfLaZalDJIzHr",
            "https://drive.google.com/uc?export=view&id=10Q87X1iBmr-uMpvW1So_Es7E__mZTHct",
        ]
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "Jabatan": "Senator",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kak zizah ini memberikan vibes indepent woman yang tegas dan mandiri sihh",
                "Pesan": "Sehatt terus yaa kak zizah aku adalah fans beratmu"
            },
            {
                "Nama": "Helmy Surya Pratama",
                "Jabatan": "Kepala Biro Aspirasi dan Media Komunikasi",
                "Nim": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobbi": "Ngesen kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Bang helmi ini asik dan banget dan fun banget orangnya",
                "Pesan": "Semogaa nanti bisa menjadi presiden yang baik dan sukses selalu bang helmi"
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
                "Nim": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah Kamar Biwa",
                "Hobbi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Mentor operasional pas magenta dan membantu bangett bang nando inii",
                "Pesan": "Semogaa selalu sehat dan sukses selalu bang nando"
            },
            {
                "Nama": "Suci Aulia",
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
                "Nim": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota Baru",
                "Hobbi": "Mancing",
                "Sosmed": "@sciia_",
                "Kesan": "Kaka suci ini jujur orangnya tegas namun asik dan baik orangnya",
                "Pesan": "Semogaa cosvall jayaa jayaa"
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "Jabatan": "Staff Biro Aspirasi dan Media Komunikasi",
                "Nim": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Abangnya ramah bangett",
                "Pesan": "Semogaa selalu kerenn yaa bangg dan sukses kedepannya"
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "Jabatan": "Kepala Biro Kajian Strategis dan Propaganda",
                "Nim": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobbi": "Nonton",
                "Sosmed": "@lia,h_264",
                "Kesan": "Kakaknya lucu, asik juga",
                "Pesan": "Semoga kuliahnya lancar ya kak"
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "Jabatan": "Staff Biro Kajian Strategis dan Propaganda",
                "Nim": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Mendokumentasi Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Kak qila ini energik banget mentor bayes ini",
                "Pesan": "Semoga kelompoknya nambah gacor ya kak"
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "Jabatan": "Staff Biro Kajian Strategis dan Propaganda",
                "Nim": "124450114",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Lampung Timur",
                "Hobbi": "Giring Ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Abang awak ini ketuplak sciencefest 2026 dan tegas orangnya serta tenang dalam menghadapi masalah",
                "Pesan": "Semoga sukses terus bang dan sehat selalu"
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "Jabatan": "Kepala Biro Kesekretariatan",
                "Nim": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "kak nadya ini orangnya baik dan ramah banget",
                "Pesan": "Semoga kesehatan kak nadya selalu terjaga dan sukses selalu"
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "Jabatan": "Staff Biro Kesekretariatan",
                "Nim": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobbi": "Baca Buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kak dwi ini orangnya baik dan ramah banget",
                "Pesan": "Semoga sehat selalu kak dwi dan sukses selalu kak dwi"
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
                "Nama": "Ihsan Maulana Yusuf",
                "Jabatan": "Kepala Departemen",
                "Nim": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Mencari dan membaca jurnal, 2 minggu mewawancarai anak kader angkatan 25 Datavora tercinta, mencari pak Luki",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Abangnya lucu dan asik",
                "Pesan": "Semangat skripsinya lancar bang"
            },
            {
                "Nama": "Hanifah Inaya Sani",
                "Jabatan": "Sekretaris Departemen",
                "Nim": "123450123",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Memasak",
                "Sosmed": "@_inayasani",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu, semangat terus kak"
            },
            {
                "Nama": "Afifah Fauziah",
                "Jabatan": "Kepala Divisi Kemitraan",
                "Nim": "123450002",
                "Umur": "19",
                "Asal": "Depok",
                "Alamat": "Belakang PB",
                "Hobbi": "Ngumpulin data sama nonton Marvel",
                "Sosmed": "@fifah.zy",
                "Kesan": "Kakaknya baik dan asik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Hasan Nur Ramadhan",
                "Jabatan": "Staff Divisi Kemitraan",
                "Nim": "124550012",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sebelah kost Ayake",
                "Hobbi": "Scroll Facebook",
                "Sosmed": "@hasan.ramadhan08",
                "Kesan": "Abangnya baik dan santai",
                "Pesan": "Semoga sukses bang"
            },
            {
                "Nama": "Layina Ropiqo",
                "Jabatan": "Staff Divisi Kemitraan",
                "Nim": "124550016",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Menonton Film",
                "Sosmed": "@lay.inr_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Semangat terus ya kak"
            },
            {
                "Nama": "Moch. Iqbal Az-Zahir",
                "Jabatan": "Staff Divisi Kemitraan",
                "Nim": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobbi": "Nonton Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Abangnya kalem dan baik",
                "Pesan": "Sehat terus bang"
            },
            {
                "Nama": "Talitha Justine",
                "Jabatan": "Staff Divisi Kemitraan",
                "Nim": "124450076",
                "Umur": "19",
                "Asal": "Padang, Sumatera Barat",
                "Alamat": "Pemda",
                "Hobbi": "Nonton",
                "Sosmed": "@talljtine_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Anadia Carana",
                "Jabatan": "Kepala Divisi Kewirausahaan",
                "Nim": "123450019",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Kost The Icon",
                "Hobbi": "Belajar",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Kakaknya pinter dan ramah",
                "Pesan": "Sukses terus kak, semoga kuliahnya lancar"
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "Jabatan": "Staff Ahli Divisi Kewirausahaan",
                "Nim": "123450062",
                "Umur": "21",
                "Asal": "Oku, Sumatera Selatan",
                "Alamat": "Airan",
                "Hobbi": "Godain cewe bang Homey",
                "Sosmed": "@pomest_",
                "Kesan": "Abangnya lucu, asik dan seru",
                "Pesan": "Semangat terus bang, semoga skripsinya lancar"
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "Jabatan": "Staff Divisi Kewirausahaan",
                "Nim": "124550008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping Kost Rafli",
                "Hobbi": "Fishing",
                "Sosmed": "@dhal_setiawan",
                "Kesan": "Abangnya baik dan asik",
                "Pesan": "Semoga sehat terus bang"
            },
            {
                "Nama": "Anggun Nita",
                "Jabatan": "Staff Divisi Kewirausahaan",
                "Nim": "124550009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobbi": "Menonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Kakaknya ramah dan baik",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
            {
                "Nama": "Della Anisa Fitri",
                "Jabatan": "Staff Divisi Kewirausahaan",
                "Nim": "124450095",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestari",
                "Hobbi": "Lagi suka olahraga",
                "Sosmed": "@dellaansaftr",
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13A2b8yBRSLxbhbwD8sL2pE2Q8-YdH8Gu",
            "https://drive.google.com/uc?export=view&id=1uV33Wse--NTmQd88MypQMM0e-0IQdxP9",
            "https://drive.google.com/uc?export=view&id=1VYXOHWiLgtT2DeU3jZ9sdyxFG0FP2Ufj",
            "https://drive.google.com/uc?export=view&id=1cmqTCMeT9VdJZuicqA0lBnm4g055eNP7",
            "https://drive.google.com/uc?export=view&id=1K69iKp32E7imb8QqqFBEIAUIg4pbQJoe",
            "https://drive.google.com/uc?export=view&id=1bdmhVeVdLrcaSjfW-jkLcAVGQ05WFRF0",
            "https://drive.google.com/uc?export=view&id=1JCRskfbTGBTwBNNb1g6GH8J_u8tJL25S",
            "https://drive.google.com/uc?export=view&id=1rerqMJDxaDxtmjkx5sZQU6LWoS6iAHi2",
            "https://drive.google.com/uc?export=view&id=1F_0hZIfqOOwkXYyk_PMi06OrgVgvpQcM",
            "https://drive.google.com/uc?export=view&id=1zBldIffxea_dTYKJ-flHRYbwIPAHECs2",
            "https://drive.google.com/uc?export=view&id=1iGTy-wk83WldHPKtS15zNcxQ0GQ-DF4x",
            "https://drive.google.com/uc?export=view&id=1681AzofpN5aBpqf5DFmKPlgc--B42hYk",
            "https://drive.google.com/uc?export=view&id=1zOf15crk5CuPaynIT9DOC2WCheRP_xo9",
            "https://drive.google.com/uc?export=view&id=1YjIBR0Ir0pq5yCgpVsQTQ5diPYKWNyKa",
            "https://drive.google.com/uc?export=view&id=1wzRGeKSOTjuOUAnD64xYO0knx6ookEjf",
            "https://drive.google.com/uc?export=view&id=1B0kwwvgyq-qkxCmFuVVmD8H7_2ml9-s3",
            "https://drive.google.com/uc?export=view&id=ISI_LINK_FOTO_17",  # Kosong untuk nomor 17
        
        ]
        
        data_list = [
            {
               "Nama": "Arienta Khusnul Ananda",
               "Jabatan": "Anggota Departemen PSDA",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobbi": "",
                "Sosmed": "",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Vany Salsabila Putri",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450022",
                "Umur": "21",
                "Asal": "Sibologa",
                "Alamat": "Pudan Kos",
                "Hobbi": "Berduaan sama pacar",
                "Sosmed": "vany.salsabilaa",
                "Kesan": "Kakaknya cantik, baik, dan ramah  ",
                "Pesan": "Semangat selalu kak"
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450117",
                "Umur": "21",
                "Asal": "Tanah Indonesia",
                "Alamat": "Samping Rumah Henry",
                "Hobbi": "Banyak",
                "Sosmed": "@nobelnizam",
                "Kesan": "Abangnya baik",
                "Pesan": "Semangat terus dan sehat selalu bang"
            },
            {
                "Nama": "Afriza Azmi",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "124450110",
                "Umur": "20",
                "Asal": "Malang",
                "Alamat": "Dalam pasar",
                "Hobbi": "Teriak",
                "Sosmed": "",
                "Kesan": "abangnya baik dan ramah",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "124450108",
                "Umur": "21",
                "Asal": "Paninjauan Solok, sepuluh kota diatas, Sumatera Barat, Indonesia",
                "Alamat": "Blok D 77, jalan manggis delapan, pemda, jatiagung, lampung selatan, lampung, indonesia",
                "Hobbi": "Mancing",
                "Sosmed": "@ykeall",
                "Kesan": "Abangnya baik, ramah , asik juga",
                "Pesan": "Sehat selalu bang"
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "Kontrakan Hijau",
                "Hobbi": "Mandiin anak ayam",
                "Sosmed": "@caesarozora",
                "Kesan": "Abangnya baik aslinya, mau ngusahain adik tingkat juga",
                "Pesan": "Sehat selalu bang"
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "124450029",
                "Umur": "18",
                "Asal": "Kampung lama",
                "Alamat": "Dibawah turunan",
                "Hobbi": "Makan gorengan",
                "Sosmed": "yudiameilianaa_",
                "Kesan": "Kakaknya sseruu, asik bangat, ramah juga",
                "Pesan": "Sehat selalu kak dan tetap semangat"
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "124450016",
                "Umur": "21",
                "Asal": "Palembang",
                "Alamat": "Sebelah kanan rumah Henry",
                "Hobbi": "Ngecek makan ayam",
                "Sosmed": "_haikaaall",
                "Kesan": "Abangnya baik aslinya",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "124450056",
                "Umur": "18",
                "Asal": "",
                "Alamat": "kost owen, warteg bahari",
                "Hobbi": "Belajar naik motor ke bandung 94",
                "Sosmed": "putrimannaa",
                "Kesan": "Kakaknya cantikkk, asik, dan sangat ramah",
                "Pesan": "Semangat terus kak, jangan lupa istirahat"
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450059",
                "Umur": "21",
                "Asal": "johor baru",
                "Alamat": "depan mie gacoan",
                "Hobbi": "Main gitar",
                "Sosmed": "queentanaabila",
                "Kesan": "Kakaknya baikk",
                "Pesan": "Sehat selalu kak, semangat terus "
            },
            {
                "Nama": "Desman Velius Halawa (Kepala Divisi PMA)",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450114",
                "Umur": "19",
                "Asal": "Nias",
                "Alamat": "Asrama TB 3",
                "Hobbi": "Ngejek orang",
                "Sosmed": "desmanhall_",
                "Kesan": "Abangnya ramah dan baik",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Azzelya Thianandry",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450041",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobbi": "Makan Ice",
                "Sosmed": "azzelytn",
                "Kesan": "kakaknya kalem, cantik juga",
                "Pesan": "Semangat terus kak"
            },
            {
                "Nama": "Charrlindah",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobbi": "Ngurus Peternakan",
                "Sosmed": "charrlnn",
                "Kesan": "kakaknya cantik, ramah juga",
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Jeremi Marolop P. Situmorang",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450111",
                "Umur": "17",
                "Asal": "Sidingkalang",
                "Alamat": "Di sebelah kost haikal",
                "Hobbi": "Jadi nelayan",
                "Sosmed": "jemarrro",
                "Kesan": "Abangnya baikk",
                "Pesan": "Semangat terus bang"
            },
            {
                "Nama": "Nabila Nur Azizah",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobbi": "Main roblox",
                "Sosmed": "n.bila_a",
                "Kesan": "kakaknya cantikk, baik juga",
                "Pesan": "Semoga lancar kuliahnya"
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450007",
                "Umur": "20",
                "Asal": "Kota Ikan",
                "Alamat": "Disamping Kost Afdal",
                "Hobbi": "Memancing",
                "Sosmed": "dearfkvmfl",
                "Kesan": "abangnya baik",
                "Pesan": "Semangat terus bang, moga lancar kuliahnya"
            },
            {
                "Nama": "Salavi Naharani",
                "Jabatan": "Anggota Departemen PSDA",
                "Nim": "123450090",
                "Umur": "20",
                "Asal": "Lampung timur",
                "Alamat": "Jatimulyo",
                "Hobbi": "Minum air putih",
                "Sosmed": "avi.nhr",
                "Kesan": " kakaknya cantik, imut juga",
                "Pesan": "Semangat kuliahnya kak"
            },                                                  
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "Jabatan" : "Ketua Himpunan",
                "Nim": "123450103",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "push rank sampe imo",
                "Sosmed": "@jars_mrp",
                "Kesan": "Abangnya keren, kalem, asik juga waktu jadi pemateri",  
                "Pesan":"Semangat terus bang semoga skripsinya dimudahkan"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "Jabatan" : "Sekretaris Jenderal",
                "Nim": "123450066",
                "Umur": "22",
                "Asal":"Riau",
                "Alamat": "Sekretariat HMSD",
                "Hobbi": "Zikir",
                "Sosmed": "@muhammadaqil1111",
                "Kesan": "Abangnya asik, lucu, suka bercanda juga, kalau jadi pemateri asik",  
                "Pesan":"Sehat selalu bang semoga dimudahkan segala urusan"
            },
            {
                "Nama": "Efi Defiyati",
                "Jabatan" : "Sekretaris 1",
                "Nim": "123450005",
                "Umur": "21",
                "Asal":"Lampung Timur",
                "Alamat": "Airan",
                "Hobbi": "Membaca",
                "Sosmed": "@eeffiidefi",
                "Kesan": "Kakaknya baik sama kalem",  
                "Pesan":"Semangat terus dan sehat selalu kak"
            },
            {
                "Nama": "Qois Olifio",
                "Jabatan" : "Sekretaris 2",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Batam",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_ ",
                "Kesan": "Abangnya keren, kalem, lucu",  
                "Pesan":"Semangat bikin bikin suratnyaa bang, semoga jadi mudah bikin skripsinya"
            },
            {
                "Nama": "Hafsa Fazila Arradhi",
                "Jabatan" : "Bendahara 1",
                "Nim": "123450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Bertemu Kesekjenan",
                "Sosmed": "@hafsafadhilaa",
                "Kesan": "Kakaknya cantik, baik, kalem, asik juga",  
                "Pesan":"Semangat terus kak, sehat selalu"
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "Jabatan" : "Bendahara 2",
                "Nim": "123450004",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Airan",
                "Hobbi": "Mintain Duit",
                "Sosmed": "@luthfiaarmdhni ",
                "Kesan": "Kakaknya lucu, baik, keren, asik juga",  
                "Pesan":"Semoga dimudahkan selalu ya kak segala urusannya"
            },                                                  
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12sNMlcLrX1nrd9U2DY9qnstiwTqqhJe6",
            "https://drive.google.com/uc?export=view&id=1NmyH1VTKEEf_BGbVg6E6vNW4ULwlr8oh",
            "https://drive.google.com/uc?export=view&id=1wcDPc7B5cGiPnMFEdlrYt-B-8wQ58PnP",
            "https://drive.google.com/uc?export=view&id=1-tngSU1LkSt-yP6fy0LfZAnY8bZohqFz",
            "https://drive.google.com/uc?export=view&id=17xu2uQ5HL5jHvAr1fWuPpY-w-jQcl1al",
            "https://drive.google.com/uc?export=view&id=1KYE0llAgb0-GyiAZHi7Fn1l5LMachQlg",
            "https://drive.google.com/uc?export=view&id=1RBC4iM_JFICr7Ss3Y5yaxNkvDK6k9H6C",
            "https://drive.google.com/uc?export=view&id=1AZOnZunm8glEGRabGCvrx4-vVw7Ti7YX",
            "https://drive.google.com/uc?export=view&id=1Eis2G2UXd1flmYA-grBpkUc5N7HfrH8R",
            "https://drive.google.com/uc?export=view&id=1ADW02iOPrbpQRn9s1eyJy2cJDf7hN54C",
            "https://drive.google.com/uc?export=view&id=1NgQrhQ4ueFsMcroxLrjQQ_xz958pXfQo",
            "https://drive.google.com/uc?export=view&id=1njNaU4CO6XXJj1mScXIG2Klp5mNja24P",
            "https://drive.google.com/uc?export=view&id=1rKwt5zTaBY7AJOpEM-9ZVkyelWD_k2o0",
            "https://drive.google.com/uc?export=view&id=1U_RcUKQbJ_lL5E8KwOhZ9hAJprTC31fv",
            "https://drive.google.com/uc?export=view&id=1AhmVoRS9BKZwRwng958xk1JNEE5Chezl",
            "https://drive.google.com/uc?export=view&id=1igGMDVSWyaMCzryzLU3eY_V0w766YPWb",
            "https://drive.google.com/uc?export=view&id=1XsWF6xYOpQYhT-BHdj5eQKObRGtA8moW",
            "https://drive.google.com/uc?export=view&id=1_vJElHxtvzIbWE-4CiCWQiQwLFpPgkwV",
        ]

        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa",
                "Jabatan": "Kepala Departemen",
                "Nim": "123450082",
                "Umur": "20",
                "Asal": "Payakumbuh, Sumatera Barat",
                "Alamat": "Way Huwu",
                "Hobbi": "Musingin TA",
                "Sosmed": "@naylasalsabilaa._",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Donna Maya Puspita",
                "Jabatan": "Sekretaris Departemen",
                "Nim": "123450028",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Way Huwi",
                "Hobbi": "Berenang",
                "Sosmed": "@donnamaya.p",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Labo John Noel Napitupulu",
                "Jabatan": "Kepala Divisi Dokumentasi",
                "Nim": "123450037",
                "Umur": "20",
                "Asal": "Medan, Jakarta Utara, Palembang",
                "Alamat": "Way Huwi",
                "Hobbi": "Buka Tutup Laptop",
                "Sosmed": "@noerruuu",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Anash Tasya Ausyaqila",
                "Jabatan": "",
                "Nim": "124450050",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Ballet",
                "Sosmed": "@anshtsyaaql",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho",
                "Jabatan": "",
                "Nim": "124450104",
                "Umur": "18",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Mancing emosi",
                "Sosmed": "felisyanbl",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama",
                "Jabatan": "",
                "Nim": "124450031",
                "Umur": "18",
                "Asal": "Bandar Lampung",
                "Alamat": "Way Halim",
                "Hobbi": "Dukung silver arrow alias mercedes",
                "Sosmed": "@muh_razan_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Sania Dwi Ayu Lestari",
                "Jabatan": "Kepala Divisi Media dan Konten Spesialis",
                "Nim": "123450086",
                "Umur": "17",
                "Asal": "Bali",
                "Alamat": "Airan",
                "Hobbi": "Nongkrong depan prodi",
                "Sosmed": "saniayyllstr",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Allisha",
                "Jabatan": "",
                "Nim": "124450019",
                "Umur": "3 Tahun",
                "Asal": "Surga",
                "Alamat": "Rumah Asha",
                "Hobbi": "Ice skating",
                "Sosmed": "@aallishaa.aa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Alya Ramadhanti",
                "Jabatan": "",
                "Nim": "124450091",
                "Umur": "19",
                "Asal": "Jambi",
                "Alamat": "Airan",
                "Hobbi": "Jalan jalan dengan sepatu rodaku",
                "Sosmed": "@alya.rmdhnti",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Bunga Clarisa Sefa",
                "Jabatan": "",
                "Nim": "124450097",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Pemda",
                "Hobbi": "Mengkoding",
                "Sosmed": "@bungaclrssf",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Difanya Husakina",
                "Jabatan": "",
                "Nim": "124450043",
                "Umur": "7.137 hari per hari ini",
                "Asal": "Sumsel",
                "Alamat": "Kafe Kali",
                "Hobbi": "Bobo cantik",
                "Sosmed": "@difanyhsa",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Nazlah Auliya",
                "Jabatan": "",
                "Nim": "124450054",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Bandar Lampung",
                "Hobbi": "Mimpi diatas kasur",
                "Sosmed": "nzlhauly_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Raihana Adelia Putri",
                "Jabatan": "Kepala Divisi Visual Design",
                "Nim": "123450041",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Airan Raya 1",
                "Hobbi": "Menulis, membaca",
                "Sosmed": "n1tg._",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "Jabatan": "",
                "Nim": "124450061",
                "Umur": "21",
                "Asal": "Surabaya",
                "Alamat": "Sukarame",
                "Hobbi": "-",
                "Sosmed": "@daffascript_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Edsel Adya Pradipta",
                "Jabatan": "",
                "Nim": "124450098",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobbi": "Scrolling Fesbuk",
                "Sosmed": "@eddel_0712",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan",
                "Jabatan": "",
                "Nim": "124450085",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Belwis",
                "Hobbi": "Nonton Star Wars",
                "Sosmed": "luciarachel_",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "Jabatan": "",
                "Nim": "124450124",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobbi": "Ngoding",
                "Sosmed": "@_shaazzh",
                "Kesan": "",
                "Pesan": ""
            },
            {
                "Nama": "Zannuba Arifah Ilman",
                "Jabatan": "",
                "Nim": "124450112",
                "Umur": "19",
                "Asal": "Jabung",
                "Alamat": "Unila",
                "Hobbi": "Tidur",
                "Sosmed": "@xifasky",
                "Kesan": "",
                "Pesan": ""
            }
        ]

        display_images_with_data(gambar_urls, data_list)

    Departemen_Medkraf()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AHJgyVgMYQ7GT_UabxfiFlxo9dz8Z0zA",
            "https://drive.google.com/uc?export=view&id=1KAkaHCwWq3zYOM3Qp8UKOBJCk-NYh8Ii",
            "https://drive.google.com/uc?export=view&id=1HwlCn6jz_eqaxa96tZZFAi6DrJ8sqUEh",
            "https://drive.google.com/uc?export=view&id=1TcZPtFeE9g7kOvJu_xMXfl5HPthDmjOM",
            "https://drive.google.com/uc?export=view&id=151xxiXfO8R6aLWUzQyC5kdSB0KbXjfdv",
            "https://drive.google.com/uc?export=view&id=1D9t5GHEWZH35jVQzOty13MbXBL0aOdOF",
            "https://drive.google.com/uc?export=view&id=1BYC0xG3r7iBZGQi0b2myaD1_ZefmI_z_",
            "https://drive.google.com/uc?export=view&id=1DtvJiAQhiZ0BCbbOwTFhPcHrnyPiHFrK",
            "https://drive.google.com/uc?export=view&id=1TgALvPTwpZ_MVHhcpMhBU4mLgqsKdzi1",
            "https://drive.google.com/uc?export=view&id=1VY_wC1S_dwZAZgXieEtNi3u4U2HY8wLt",
            "https://drive.google.com/uc?export=view&id=1MvzMaaUO7o4Te6XZpnDj3EdE7zQGBKS6",
            "https://drive.google.com/uc?export=view&id=1y6iVzbtDGtSRkyA2mUa871Y5IyyHVVt8",
            "https://drive.google.com/uc?export=view&id=1cqr0_cgQL7iKjsa9KsZg79GWVX6FrA-m",
            "https://drive.google.com/uc?export=view&id=1Nkb_y2-KUWqq_kGLwXZPVI6RULg_kNTf",
            "https://drive.google.com/uc?export=view&id=10uFAKxR36v8UOWgntAf3LuI7o08lqv1D",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "Jabatan": "Kepala Departemen",
                "Nim": "123450106",
                "Umur": "20",
                "Asal":"Tangerang Kota",
                "Alamat": "Gerbang Barat",
                "Hobbi": "Begadang",
                "Sosmed": "@haikalsbln_",
                "Kesan": "Abang ini asik dan keren",  
                "Pesan":"semangat abang, sehat selalu"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "Jabatan": "Sekretaris Departemen",
                "Nim": "123450034",
                "Umur": "21",
                "Asal":"Way Kanan",
                "Alamat": "Untung Suropati",
                "Hobbi": "Suka menolong orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "kakaknya cantik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, semangat skripsi"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "Jabatan": "Kepala Divisi Keharmonisasian",
                "Nim": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakak ini asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak semangat skripsi"
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "Jabatan": "Staff Ahli Keharmonisasian",
                "Nim": "123450067",
                "Umur": "22",
                "Asal":"Tetangga Singapore",
                "Alamat": "Kota Baru",
                "Hobbi": "Mainin Surat",
                "Sosmed": "@qoisolifio_",
                "Kesan": "Abangnya asik dan seru",  
                "Pesan":"semangat terus kuliahnya abang"
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450096",
                "Umur": "18",
                "Asal":"Indragirihulu",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Sleep Call",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "kakaknya cantik dan ramah",  
                "Pesan":"semangat kakak, sehat selalu"
            },
            {
                "Nama": "Cerine Sihotang",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450049",
                "Umur": "19",
                "Asal":"Semarang",
                "Alamat": "Belwis",
                "Hobbi": "Manjat pohon kelapa",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "kakaknya cantik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450094",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Pemda",
                "Hobbi": "Main Biola",
                "Sosmed": "@jay.saputra.tmb",
                "Kesan": "abangnya ASIK BANGET, seru orangnya",  
                "Pesan":"semangat terus kuliahnya abang semangat menugas"
            },
            {
                "Nama": "Najla Nursyifa",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450051",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Belwis",
                "Hobbi": "Nonton asmr",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kakaknya asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak"
            },
            {
                "Nama": "Rozak Ramdani",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450100",
                "Umur": "19",
                "Asal":"Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobbi": "Badminton",
                "Sosmed": "@rozakramdani_",
                "Kesan": "Abangnya seru dan baik",  
                "Pesan":"semoga sehat selalu abang"
            },
            {
                "Nama": "Teresa Christiani Purba",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450046",
                "Umur": "19",
                "Asal":"Riau",
                "Alamat": "Belwis",
                "Hobbi": "Memasak",
                "Sosmed": "@christiani8872",
                "Kesan": "kakanya baik, seru orangnya",  
                "Pesan":"semoga selalu dikelilingi orang baik"
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "Jabatan": "Kepala Divisi Kerohanian",
                "Nim": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobbi": "Nonton MU",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang"
            },
            {
                "Nama": "Audina Fitria",
                "Jabatan": "Anggota Kerohanian",
                "Nim": "124450038",
                "Umur": "20",
                "Asal":"Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobbi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kakaknya asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak"
            },
            {
                "Nama": "Cika Adelia BR Marbun",
                "Jabatan": "Anggota Keharmonisasian",
                "Nim": "124450107",
                "Umur": "20",
                "Asal":"Riau",
                "Alamat": "Samping Kuburan",
                "Hobbi": "Scroll tiktok",
                "Sosmed": "@cikambrn",
                "Kesan": "Kakaknya seru dan baik",  
                "Pesan":"Jaga kesehatan kakak, semoga bahagia selalu"
            },
            {
                "Nama": "Gustin H Tampubolon",
                "Jabatan": "Anggota Kerohanian",
                "Nim": "124450068",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobbi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "kakanya baik, seru orangnya",  
                "Pesan":"semoga selalu dikelilingi orang baik"
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "Jabatan": "Anggota Kerohanian",
                "Nim": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobbi": "Nangkap lele",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang"
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "Jabatan": "Anggota Kerohanian",
                "Nim": "124450036",
                "Umur": "21",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobbi": "Main game di HP temen",
                "Sosmed": "@muhvinz_",
                "Kesan": "Abangnya seru dan asik",  
                "Pesan":"semoga sehat selalu bang"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ataip3EazrpgKL2Z-i3snrgNhu9YgVYW",
            "https://drive.google.com/uc?export=view&id=1TygxvBWPNyAn8kc4tzNJp6CIMSeZ1mCS",
            "https://drive.google.com/uc?export=view&id=10RwspWKIKqTNl22DxHYTFF-5ktXLirf-",
            "https://drive.google.com/uc?export=view&id=1exlOlr-08DRshwYJSp69qssmaw6vHtu1",
            "https://drive.google.com/uc?export=view&id=1tTBKFcPqaUVD74hOAdewAeYN6pNS-Egj",
            "https://drive.google.com/uc?export=view&id=1pZRwDgHINjYuwISFZ-mbBMtxtNC81K9Q",
            "https://drive.google.com/uc?export=view&id=1bX4h4v4-Pw2k96Ju17Fn-aj0xms1iQyM",
            "https://drive.google.com/uc?export=view&id=1J73UXSfM5G5TEdjfqKY4hcDn7JPs7Bmu",
            "https://drive.google.com/uc?export=view&id=16-DDb2FqZ0x1x-UPJ8r4TRobJ7gwYDj-",
            "https://drive.google.com/uc?export=view&id=1Y_X1ag3mnf7yQu6B5wx-_rhluGC4dFNq",
            "https://drive.google.com/uc?export=view&id=1Lb6qIr0FfbeeUChIZMgUnVuLySAc9RRJ",
            "https://drive.google.com/uc?export=view&id=1fQatWOWhTZwfR8eNHKO52P2rpfAQ_2ab",
            "https://drive.google.com/uc?export=view&id=1WlqURS56O4jh_8DLhudfeVvpHekcx0RM",
            "https://drive.google.com/uc?export=view&id=1IYhVlErvmNAdJ7yt0NpInZ85qRLYUgSc",
            "https://drive.google.com/uc?export=view&id=1xHS6VqXPQfR_i7SRYfCYMCTa2ZSmBRqW",
            "https://drive.google.com/uc?export=view&id=1lY7iqyAGCayBvJrioxNfm9TiyIimdaTP",
            "https://drive.google.com/uc?export=view&id=1VenJvUOR91-cvE5gwkPleoIjS7N60WQ7",
            "https://drive.google.com/uc?export=view&id=1c3gNuKwVZOf-Pgl4AnIVfkqNxGe_IM6R",
            "https://drive.google.com/uc?export=view&id=1S4v8Kgc-9ox046pcUxVZ5RaI8hwd2Hie",
            "https://drive.google.com/uc?export=view&id=1bI79m7mmtodq81mlObXBn-Ut3R87m8E6",
            "https://drive.google.com/uc?export=view&id=1eCD-MwYdfxAd9rC4BPihYjDtDri_Mrkh",
            "https://drive.google.com/uc?export=view&id=1N08X_9zSwCcb4pR4srp_4kmIEdQxKqkJ",
        ]
        data_list = [
             {
                "Nama": "Arini Puteri Elandra",
                "Jabatan": "Kepala Departemen",
                "Nim": "123450069",
                "Umur": "21",
                "Asal":"Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobbi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "energik banget",  
                "Pesan":"semangat kakak, sehat selalu",
            },
            {
                "Nama": "Nabyla Sharfina",
                "Jabatan": "Sekretaris Departemen",
                "Nim": "123450008",
                "Umur": "20",
                "Asal":"Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobbi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "kakaknya cantik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak, semangat selalu",
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "Jabatan": "Kepala Divisi Pengabdian Masyarakat",
                "Nim": "123450032",
                "Umur": "",
                "Asal": "tetangga kadep",
                "Alamat": "belwis",
                "Hobbi": "memancing keributan",
                "Sosmed": "@adityatfq",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Khoirul",
                "Jabatan": "Kepala Divisi Hubungan Luar",
                "Nim": "1234500",
                "Umur": "",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobbi": "main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Selma Siti Aisyah",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "123450044",
                "Umur": "20",
                "Asal": "lampung",
                "Alamat": "balam",
                "Hobbi": "jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450028",
                "Umur": "20",
                "Asal": "sini",
                "Alamat": "jauh pokoknya",
                "Hobbi": "tidur",
                "Sosmed": "@kshigf",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Indah Khairunnisa",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Bima Ekayasa",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450106",
                "Umur": "",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobbi": "berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450113",
                "Umur": "",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobbi": "lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450083",
                "Umur": "cepuyuh tayun",
                "Asal": "ikut kadep",
                "Alamat": "love earth",
                "Hobbi": "jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Yollanda Agustina",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobbi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450022",
                "Umur": "20",
                "Asal": "palembang",
                "Alamat": "bebas",
                "Hobbi": "ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Fathya Intami Gusda",
                "Jabatan": "Staff Ahli Pengabdian Masyarakat",
                "Nim": "123450095",
                "Umur": "",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobbi": "baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "Jabatan": "Staff Ahli Pengabdian Masyarakat",
                "Nim": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobbi": "Jadi orang baik",
                "Sosmed": "-",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Danil N Fadillah",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450103",
                "Umur": "",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobbi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Favian Arkaanda",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450021",
                "Umur": "",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobbi": "ngesen kanan",
                "Sosmed": "@fvnnn05",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450081",
                "Umur": "((15≪1) & 31) ⊕ 10",
                "Asal": "situlah",
                "Alamat": "pohon mulia",
                "Hobbi": "nyari hobi",
                "Sosmed": "@zydddddd__",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Alfaya Abiyyi",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450006",
                "Umur": "nelson piquet",
                "Asal": "balam",
                "Alamat": "balam",
                "Hobbi": "makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Muhammad Rizaldi",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450093",
                "Umur": "Masih muda lah",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "Sosmed": "@jaldii._",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "Jabatan": "Staff Pengabdian Masyarakat",
                "Nim": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobbi": "nonton thinkerbell",
                "Sosmed": "@snova.19",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Asri Meilani",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobbi": "menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "",
                "Pesan": "",
            },
            {
                "Nama": "Ahmad Rizky",
                "Jabatan": "Staff Hubungan Luar",
                "Nim": "123450050",
                "Umur": "21 Tahun ini alhamdulillah",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobbi": "ga ngapa ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "",
                "Pesan": "",
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
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
                                                
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()