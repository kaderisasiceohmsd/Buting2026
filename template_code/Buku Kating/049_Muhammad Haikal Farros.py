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
            "https://drive.google.com/uc?export=view&id=1tUHzP56vPuf8R4AC60P-f-b2e74ETfTo",
            "https://drive.google.com/uc?export=view&id=1Rcby10Iou9ytL6xNuEJ2UzAqtuLB_zIU",
            "https://drive.google.com/uc?export=view&id=1NhSD53QndrdKausQ36YGQKJpfKnHd1ob",
            "https://drive.google.com/uc?export=view&id=1HcmqRhXJGYd7gtnIJbOHBbDXN9beP6G4",
            "https://drive.google.com/uc?export=view&id=1ZEFOvRpWu5NopIgueXnRCK_igm2PnLRw",
            "https://drive.google.com/uc?export=view&id=1tJ_g4G35BO40JU7Em8vpW9wye-2fNaZl",
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
                "Nama": "Fathinah Nur Azizah",
                "Jabatan": "Senator",
                "Nim": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobbi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kakaknya cantik, baik, kalem, keren",
                "Pesan": "Sehat selalu kak, semoga lancar skripsinya"
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
                "Kesan": "Abangnya seru, asik, lucu",
                "Pesan": "Semangat terus bang"
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
                "Kesan": "Abangnya baik, asik, kalem",
                "Pesan": "Semoga selalu dimudahkan bang"
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
                "Kesan": "Kakaknya kalem dan baik",
                "Pesan": "Sehat selalu kak"
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
                "Kesan": "Abangnya asik, keren, pinter juga",
                "Pesan": "Sehat selalu bang, semangat terus juga"
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
                "Kesan": "Kakaknya lucu, keren juga",
                "Pesan": "Semoga kelompoknya nambah gacor kak"
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
                "Kesan": "Abangnya keren, asik juga",
                "Pesan": "Semoga sukses bang"
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
                "Kesan": "Kakaknya cantik, ramah, baik",
                "Pesan": "Semangat terus kak, semoga kuliahnya lancar"
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
                "Kesan": "Kakaknya baik dan ramah",
                "Pesan": "Sehat selalu dan semangat terus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jgBijFFtqWGiUIpnpzrgqQRJguReX-_O",
            "https://drive.google.com/uc?export=view&id=1Fupws9sW1eXvB_gUPe4WfytqZDmW4Peo",
            "https://drive.google.com/uc?export=view&id=1m1AAOedv0aJMpTxZ9tIxyl3dxi2eFVhh",
            "https://drive.google.com/uc?export=view&id=1UIF5ERMgF3P67u1f40S9Qc_cXw20JdZQ",
            "https://drive.google.com/uc?export=view&id=1z0hbHsPjD1ii0kvWXau1nTuizroAF-ck",
            "https://drive.google.com/uc?export=view&id=1-EUhIxz-a-ORMkzQVU5cIzcQmJ8Aj5x7",
            "https://drive.google.com/uc?export=view&id=1gLnwnCzygoDy5ZRGdphsVHJDmBisGKsg",
            "https://drive.google.com/uc?export=view&id=1WKUUV3nhM6j-aS-iqYAnaKNu71k_YlM_",
            "https://drive.google.com/uc?export=view&id=1HLO6aGCgIiQVvpXb_OsaiDZR06HXGvs1",
            "https://drive.google.com/uc?export=view&id=1NWoIp2eK5Ue8-Buyc3lUdgG_dTn_b4nF",
            "https://drive.google.com/uc?export=view&id=1xCGOc6Id41I0LAqRFjsuCfd9IW91Lfsq",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #sisa
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Nama": "Hanna Gresia Sinaga",
                "Jabatan": "Kepala Divisi Keharmonisasian",
                "Nim": "123450038",
                "Umur": "21",
                "Asal":"Kisaran",
                "Alamat": "Sukarame",
                "Hobbi": "Membaca Novel",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Kakak ini asik dan baik",  
                "Pesan":"semangat terus kuliahnya kakak semangat skripsi",
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
                "Pesan":"semangat terus kuliahnya abang",
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
                "Pesan":"semangat kakak, sehat selalu",
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
                "Pesan":"semangat terus kuliahnya kakak",
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
                "Pesan":"semangat terus kuliahnya abang semangat menugas",
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
                "Pesan":"semangat terus kuliahnya kakak",
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
                "Pesan":"semoga sehat selalu abang",
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
                "Pesan":"semoga selalu dikelilingi orang baik",
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
                "Pesan":"semoga sehat selalu bang",
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
                "Pesan":"semangat terus kuliahnya kakak",
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
                "Pesan":"Jaga kesehatan kakak, semoga bahagia selalu",
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
                "Pesan":"semoga selalu dikelilingi orang baik",
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
                "Pesan":"semoga sehat selalu bang",
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
                "Pesan":"semoga sehat selalu bang",
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