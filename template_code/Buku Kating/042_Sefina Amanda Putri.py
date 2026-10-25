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
            st.write(f"nama: {data_list[i]['nama']}")
            st.write(f"nim: {data_list[i]['nim']}")
            st.write(f"umur: {data_list[i]['umur']}")
            st.write(f"asal: {data_list[i]['asal']}")
            st.write(f"alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"kesan: {data_list[i]['kesan']}")
            st.write(f"pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH

if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dZQGK3Pzfq5_LkehqiK0Io7UhKDusYf9",
            "https://drive.google.com/uc?export=view&id=1ucOSQ5l7L_sSQgUn_8eoEJpxERCtKC-r",
            "https://drive.google.com/uc?export=view&id=1GqUaf_-wGKV2igaBhfNmbdLQK8X3TRB0",
            "https://drive.google.com/uc?export=view&id=1VXbFvp4rEQrZckMvVB8KhQkBqh45MC4a",
            "https://drive.google.com/uc?export=view&id=19WFHb9JzIfjEPDjiapxOoAsXPdha1GM5",
            "https://drive.google.com/uc?export=view&id=1D-FCJ-jzPN9eb1cIW6RNdMGx2vi1uHx-",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya pintar, banyak pengalaman, dan menginspirasi",  
                "pesan":"Semangat terus bang menjadi kahim bagi kami, dan semangat terus kuliahnya"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhamadaqil1111",
                "kesan": "Bang Aqil orangnya asik, baik, dan tegas sebagai sekjen",  
                "pesan":"Semoga bang Aqil sehat selalu dan sukses sebagai sekjen dan sukses dalam kuliah"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak Efi orangnya ramah, pintar, dan keren",  
                "pesan":"Semangat terus kak dalam kuliah, himpunan, dan lainnya diluar kampus"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya ramah, pintar, baik, dan pastinya keren",  
                "pesan":"Semangat terus bang, semoga sukses selalu"# 1   
            },    
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu Luluk",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya asik, baik, dan tentunya ramah",  
                "pesan":"Semoga kakak sehat selalu, dilancarkan kuliahnya, dan sukses selaluu"# 1   
            },    
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kak Luthfia orangnya pintar, baik, dan fun",  
                "pesan":"Semangat terus kak, semoga sehat selalu, lancar kuliahnya, dan sukses kedepannya"# 1   
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()



if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1He3KWlbxUtGpgVb7TuBS0NKiUUDXO3TH",
            "https://drive.google.com/uc?export=view&id=1DuIYYRnDV7hvSo42HUcikdnNPfeWLTua",
            "https://drive.google.com/uc?export=view&id=1CvjcqbwRN0AIG4h5khQzqT8JxxZt6asG",
            "https://drive.google.com/uc?export=view&id=1ggIJ6aTk_CmILp7kLhwYIt7Z-zg_kVvR",
            "https://drive.google.com/uc?export=view&id=1WC6a00MyH6d49fIik9KrynkFLxtQwfh4",
            "https://drive.google.com/uc?export=view&id=1BAnh12PXukeM8c2kWpAiw56reffqQAga",
            "https://drive.google.com/uc?export=view&id=1OgOtWodeoGwX4At1jcgmviIFaBTlZ-O4",
            "https://drive.google.com/uc?export=view&id=1P2v3Das_ybNcaC1nXO_qFhw2iTfmSBeS",
            "https://drive.google.com/uc?export=view&id=1vQOfGX8JlJxb_G8lBCbesax91YiLCRYO",
            "https://drive.google.com/uc?export=view&id=1fzmW9yR1BDk-Cn3D-YytWxofVAvvVFxY",
            "https://drive.google.com/uc?export=view&id=13sIYBCQFvBbPMWbA4qFou-2iiKEjwUIy",
            "https://drive.google.com/uc?export=view&id=1ARhpTyzmkX5I97ajFyxk6gr7fReDvIi-",
            "https://drive.google.com/uc?export=view&id=1dAH0-hdqusnXR7gmang4Gk5AGqmKi6LH",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Manado",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iyanmridhoanik",
                "kesan": "Bang nya seru,baik,ramah,banyak pengalaman",  
                "pesan":"Semangat terus bang untuk berorginasasi, dan tetap semangat juga kuliahnya"# 1
            },
            {
                "nama": "Juesi Aprillia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Sekawang",
                "alamat": "pelangi",
                "hobbi": "Ngereapet lagu beegin again taylor",
                "sosmed": "j__eesie",
                "kesan": "kak jue cantik banget,ramah,seru juga ngobrol waktu wwc",  
                "pesan":"Semangat terus ya kak sehat selalu dan sukses sebagai sekre baleg dan sukses dalam kuliah"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton Agz,tapu sudah tamat",
                "sosmed": "@eeffiidefi",
                "kesan": "Bang orangnya ramah, dan keren",  
                "pesan":"Semangat terus bang dalam kuliah, himpunan, dan sehat selalu"# 1
            },
            {
                "nama": "GHmikael niko antoni setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jatimulyo",
                "hobbi": "Jogging Malam Hari",
                "sosmed": "@me._kael",
                "kesan": "Bang mike orangnya seru banget, baik, dan pastinya keren",  
                "pesan":"Semangat terus bang, dan tetap jaga kesehatan"# 1   
            },    
            {
                "nama": "Siti Sarifah Sumammah",
                "nim": "124450015",
                "umur": "19",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi kartu boboy",
                "sosmed": "@syt.rifa",
                "kesan": "Kak rifa orangnya asik, baik, dan tentunya ramah",  
                "pesan":"Semangat terus kakak sehat selalu, dilancarkan kuliahnya"# 1   
            },    
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagih",
                "alamat": "Sukabumi",
                "hobbi": "Minum kopi",
                "sosmed": "@givarooo",
                "kesan": "bang givaro orangnya baik, dan fun",  
                "pesan":"Semangat terus bang, semoga sehat selalu, lancar kuliahnya"# 1 
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Sumbar,Padang",
                "alamat": "Kedaton",
                "hobbi": "Memburu",
                "sosmed": "@fghnst_",
                "kesan": "kak nisa orang nya seru,baik,ramah,and kakak nim kuu",  
                "pesan":"Semangat terus kak untuk berorginasasi, dan tetap semangat juga kuliahnya"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "123450085",
                "umur": "20",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca au",
                "sosmed": "@haniquratuain_",
                "kesan": "kak hani,ramah,seru juga ngobrol waktu wwc",  
                "pesan":"Semangat terus ya kak sehat selalu dan sukses dalam kuliah"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Tanggersng",
                "alamat": "Teluk Betung",
                "hobbi": "Ngoding",
                "sosmed": "@jeremia-hm",
                "kesan": "Bang jeremi, baik, dan pastinya keren",  
                "pesan":"Semangat terus bang, dan tetap jaga kesehatan"# 1   
            },    
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "KotaBaru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica orangnya asik, baik, dan tentunya ramah",  
                "pesan":"Semangat terus kakak sehat selalu, dilancarkan kuliahnya"# 1   
            },    
            {
                "nama": "Jona Timothy Ogate Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "pemda raya",
                "hobbi": "ngegym dan koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "bang jon orangnya baik, dan ramah",  
                "pesan":"Semangat terus bang, semoga sehat selalu, lancar kuliahnya"# 1 
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@gsekardnwp",
                "kesan": "kak sekar orangnya baik aku kira tipekal orang yang serius ternyata orang nya fun",  
                "pesan":"Semangat terus kak, semoga sehat selalu, lancar kuliahnya"# 1 
            },
            {
                "nama": "Wan Nashwa Alhasni Yusika",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@gsekardnwp",
                "kesan": "kak sekar orangnya baik aku kira tipekal orang yang serius ternyata orang nya fun",  
                "pesan":"Semangat terus kak, semoga sehat selalu, lancar kuliahnya"# 1 
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17VjNmWqx1Z943eAT3x2ZeeqAXV9WRIW2",
            "https://drive.google.com/uc?export=view&id=1AgpQLO0hNqzlMojDQWD7MmVBgq_vOTzi",
            "https://drive.google.com/uc?export=view&id=1C05Fbz3GGsDkwZQ2M9tuNuttHOEuftph",
            "https://drive.google.com/uc?export=view&id=17_W2FbYW1uCQSOm9XVC6G25oC8Qwx0GM",
            "https://drive.google.com/uc?export=view&id=1cvHni0qv3JkubCFNotoQEgSHhACkSqTC",
            "https://drive.google.com/uc?export=view&id=1a7ziRiRBAeKmLMHoZczRNUv6_mRUmcJo",
            "https://drive.google.com/uc?export=view&id=1i77Ojb1JhOKY9tvZIQiuoAad2BU4lTcv",
            "https://drive.google.com/uc?export=view&id=1ylZmElEXrCx9UTjFfgY5FMRjSvwNTsnj",
            "https://drive.google.com/uc?export=view&id=1m2qZS9JEcRubFuhmf9T2AM8RMRonpGyZ",
            "https://drive.google.com/uc?export=view&id=1M-n_7_VNHuJe7e8b889Y4p-dHvCHPfIP",
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
                "kesan": "kak fathinah orang seru,ramah",  
                "pesan": "semangat terus kak untuk berorganisasi dan kuliah nya"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Tanya Bapas",
                "sosmed": "@helmy_ist",
                "kesan": "bang helmi orang nya baik,ramah,seru",  
                "pesan": "semangat terus bang,jangan lupa ngeasprak semester depan"# 1
            },
	 {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "bang nando orang nya baik,ramah",  
                "pesan": "semangat terus bang jangan lupa jaga kesehatan"# 1
            },
	 {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_staff",
                "kesan": "kak suci orang nya baik, murah senyum",  
                "pesan": "semangat terus kak jangan lupa jaga kesehatan "# 1
            },
	 {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Di bonceng",
                "sosmed": "@wielhawny",
                "kesan": "bang wiel orang nya ramah,baik",  
                "pesan": "semangat terus bang untuk berorganisasi dan jangan lupa jaga kesehatan"# 1
            },
	 {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "orang nya baik,ramah",  
                "pesan": "semangat terus ya kak jangan lupa jaga kesehatan"# 1
            },
	 {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "kak aqila orang nya best banget my mentor, selalu mendokumentasikan semua kegiatan bayes",  
                "pesan": "semangat terus ya kak,makasih udah jadi mentor akuu,semoga hari nya menyenangkan dan selalu bahagia"# 1
            },
	 {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Giring Ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": " bang hazel ku kira tipe orang yang serius ternyata ya so so",  
                "pesan": "semangat terus ya bang jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kak nadya orang nya ramah,baik",  
                "pesan": "tetap semangat kak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Baca buku,nonton film,dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kak dwi orang nya baik,ramah",  
                "pesan": "semangat terus kak jangan lupa jaga kesehatan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CqBqamhRW71XiDpHGMsggOfn2JUlQPHM",
            "https://drive.google.com/uc?export=view&id=16DgIvpHVO0ufruR1jxx-W775MKPetaE6",
            "https://drive.google.com/uc?export=view&id=1lchBgxAvCxMBTIia5pJR52uZRcQJ2HDi",
            "https://drive.google.com/uc?export=view&id=152ZGDzrcbqYKTz9LngQ4NWg48iDMhaNe",
            "https://drive.google.com/uc?export=view&id=1kNchPZy3UNs7TCcjJi1PuJZtvSe1J90p",
            "https://drive.google.com/uc?export=view&id=1TJ9LCn9Ohd3yB5OLi2kXKOHXafmcpWyN",
            "https://drive.google.com/uc?export=view&id=19j8aN4ViyoraPadTpjR8v8SRzQH5kOzK",
            "https://drive.google.com/uc?export=view&id=1AusZEs6CYPO2BIgaRMu0aDlaKFXE268n",
            "https://drive.google.com/uc?export=view&id=19tyjRBH7RRzcQLtiLNxNJbWrzdQY7C4e",
            "https://drive.google.com/uc?export=view&id=1Y0BsUXvvdnOhchQqiBguTdICrr1d6W9M",
            "https://drive.google.com/uc?export=view&id=1R8S-BCoenFuvZVwW9F3uTyO9QzsWLcKy",
            "https://drive.google.com/uc?export=view&id=1hiJMhcDimtEgO1aZII0EEPlIUg_0o_R8"
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Bang ihsan orang nya baik,ramah suka ngelawak ",  
                "pesan":"semangat terus bang dan jangan lupa jaga kesehatan!!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak hanifah orang nya baik,seru",  
                "pesan":"semangat terus ya kak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak nadia orang nya ramah,baik",  
                "pesan":"semangat terus ya kak jangan lupa tetap jaga kesehatan!!!"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kak afifah orang nya baik,ramah",  
                "pesan":"semangat terus ya kak kuliah nya jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "awal awal aku kira bang pome tipe orang yang serius ya padahal suka ngelawak asli nya",  
                "pesan":"semangat terus bang kuliah nya tetap jaga kesehatan jangan lupa ngejokes lagi"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "bang afdhal kaya orang yang cool habis tapi  ya asli nya so so lah",  
                "pesan":"semangat terus bang untuk kuliah nya semoga harinya bahagia"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "awal kenal bang iqbal dari ya gitu lah,orang nya asik juga",  
                "pesan":"semangat terus ya bang jangan lupa ngeasprak"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kak nya baik,ramah",  
                "pesan":"semangat terus kuliah semoga hari nya bahagia"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak angun orang nya baik,ramah,asik juga",  
                "pesan":"semangat terus kak kuliah nya semoga harinya bahagia"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "awal ketemu aku kira kakak nya jutek tapi asli nya seru banget btw kak della pj magang akuuu",  
                "pesan":"semangat terus ya kak kuliah nya,thank uuuu sudah jadi pj magang akuu"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "bang hasan orang nya baik,seru,ramah juga",  
                "pesan":"semangat terus ya bang kuliah nya semoga harinya bahagia selalu"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kak talitha orang nya baik,ramah,asik banget",  
                "pesan":"semangat terus ya kak kuliah nya semoga harinya bahagia"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()   

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e499MsVjvdH_irWPb2SULLZUcjnTGady",
            "https://drive.google.com/uc?export=view&id=1AtDW2bg53VR4RDP9qhfbFpOX76og2uvk",
            "https://drive.google.com/uc?export=view&id=1mLU-fz6f4VXT6gg74sOUsK_6heE2Gd1e",
            "https://drive.google.com/uc?export=view&id=16AG-7ML6_oGJYdWDHgSxG6ICVjOhnu2-",
            "https://drive.google.com/uc?export=view&id=1awyPPUiZysVeHoS5we5tRZ2C8bBtzTs7",
            "https://drive.google.com/uc?export=view&id=1hb9kqy5ns_-8DLY9QsxNCWFSdNc_VENk",
            "https://drive.google.com/uc?export=view&id=1VsA-4GBBLo24Gl0O6nNiBkejtDUpRl4n",
            "https://drive.google.com/uc?export=view&id=18c0b-OOBHBNZDkerDQlOMYgeoL83Dwhi",
            "https://drive.google.com/uc?export=view&id=1fes1HL6fHOFfCdA8tAY9CKCr8Y9bSF55",
            "https://drive.google.com/uc?export=view&id=1y3hMsCEElRe6zFJI1jOO_DdFWERopjcG",
            "https://drive.google.com/uc?export=view&id=119bufh4DIbJdOI78w3Skmz6OvYQSojLO",
            "https://drive.google.com/uc?export=view&id=14T5SQrXGEgNCL-Q8ijL4W6mtsAnfiXZW",
            "https://drive.google.com/uc?export=view&id=17ZsTpBWiKhv6njHO85bHh9pIbnqHMxAb",
            "https://drive.google.com/uc?export=view&id=17X6BUlqW9Iv6C6zMv3uNnOSi3NFyRfYQ",
            "https://drive.google.com/uc?export=view&id=1exEkqV10j86-dCs0oTVNFqDwjaF4ZpjC",
            "https://drive.google.com/uc?export=view&id=1L8yUf5xbTdUwoas39ujldGJvne_0Wn4S",
            "https://drive.google.com/uc?export=view&id=1lfnRd-7ok8SRuHibxmKbO42rqBAHKHqi",

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
                "kesan": "Kak arienta awalnya keliatan serem hihi, tapi ternyata baikkk",  
                "pesan":"Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk",  
                "pesan":"Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas tapi lama-lama saya ngerasa tegas itu bisa di ambil sebuah makna",  
                "pesan":"Makasih dan semangat terus bang semoga di permudah segala nya samapi Ta "# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi agak serem si awal awal tapi lama lama asik",  
                "pesan":"Semangat kuliahnya bang azmii, semoga lancar dan sukses teruss yaaa bang"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake awal nya saya agak serem ngeliat nya tapi lama lama sore,maaf ya bang saya sinisin pas eval materi",  
                "pesan":"Semangat terus yaa bang ayake,semoga selalu di kelilingi orang baik kaya abang membuat kebaikan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Terlihat agak menyeram kan tapi maaf ya bang di mata saya masih serem mungkin besok besok engga",  
                "pesan":"Sehat selalu dan sukses terusss bang caesaarr"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kaka ini baik banget pas ngeasprak alpro waktu itu",  
                "pesan":"Semangat terus ya kak untuk kuliah nya jangan lupa ngeasprak lagi"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Bang haikal baikk",  
                "pesan":"Sehat selalu dan sukses terus ya bang haikalll"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "kak putri baik banget,seru murah senyum",  
                "pesan":"semangat terus ya kak kuliah nya semoga di kelilingi orang baik"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kaka ini ramah, humble, dan asik",  
                "pesan":"Semangat terus ya kak, semoga sehat dan sukses selalu!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abang ini humble,waktu itu sempet ngobrol kasih pemasukan buat datavora harus gimna",  
                "pesan":"sukses selalu bang desmannn, dan semangat terus untuk kuliah nya"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kak azzelya cantik dan baikk ",  
                "pesan":"Semangat dan sehat selaluu kakaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kaka ini suka nyanyi jugaa, baik, dan cantik mirip nagita slavina",  
                "pesan":"sehat sehat ka cacaa, semoga semester ini dilancarinn segala urusan kaka yaa"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang jeremi lucu bangettt,seru juga orang nya btw foto buting kita tergemoy ga si bang",  
                "pesan":"Semangat terus abangg,semoga harinya bahagia selalu"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak nabila humble dan talkative",  
                "pesan":"sehat sehat kakaa, bahagia terus yaaa"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abang ini stylishhh",  
                "pesan":"Semangat teruss bang rafli, semoga sehat selalu bahagia selaluu"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakak imut dan lucuuuu",  
                "pesan":"sehat sehat dan lancar selalu kakaaa kuliahnyaaa^^"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YGl8pgBkXKCBSCjxuo3DJgOI_n6Jj6lp",
            "https://drive.google.com/uc?export=view&id=1U2G9ak4J53Z8u9ktoGPa8ZS0CewPkUsx",
            "https://drive.google.com/uc?export=view&id=1xWH4Ni0sO-MrsHNisaEZjqibZCYhXXS9",
            "https://drive.google.com/uc?export=view&id=1L3Chdgz3l1c5i9yLmgIwZRcMKD1X5S1X",
            "https://drive.google.com/uc?export=view&id=1uG-LkNPJ-Aiu8kQ---a0o-UPrSSfl8i5",
            "https://drive.google.com/uc?export=view&id=12YBlDM_QdhWh3EPtBJwYPmk5XTZAVdEm",
            "https://drive.google.com/uc?export=view&id=1AIjoKxXLDmixaabN0JraUTeaL4IwqsIa",
            "https://drive.google.com/uc?export=view&id=12uTu9MCvF29hCi_7gHAfi31xFo_TnDDp",
            "https://drive.google.com/uc?export=view&id=1fFcwsA7J9OyQBghiB_zxKgspn5o3z7NO",
            "https://drive.google.com/uc?export=view&id=11GGMfeOBC7SoUYaZAgqhiI05w1Yp2V9h",
            "https://drive.google.com/uc?export=view&id=1QrzK5HKKwsL182UobIx5HlhcJ1R7Ig7H",
            "https://drive.google.com/uc?export=view&id=1GjNqEcIYHNXJvOhEo7Cq6VQe772BwJHx",
            "https://drive.google.com/uc?export=view&id=1e_orKmG66Xq-wj3W6oTK8eJqg13Wjaz1",
            "https://drive.google.com/uc?export=view&id=1llayjuw2etaakIllznC8yXteHOgwTwg5",
            "https://drive.google.com/uc?export=view&id=1at8aaGG53Rjb4fR56ki46mvr9Szw3sco",
            "https://drive.google.com/uc?export=view&id=1MjGyAqLNOhJ8KS_-81n1in2kM8By3TY1"
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Way Halim",
                "hobbi": "Ngeledek orang",
                "sosmed": "@haikalsbln",
                "kesan": "Bang haikal orang nya baik,seru,ramah",  
                "pesan": "semangat terus ya bang kuliah nya jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kak kharisma orang nya baik banget,seru",  
                "pesan": "semangat terus kuliahnya kak jangan lupa tetap jaga kesehatan"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak hanna orang nya seru banget,bener bener harmonis seperti divisi nya",  
                "pesan": "semangat terus kuliahnya kak dan sehat selalu,terima kasih sudah tersenyum setiap hari"# 1
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "bang farhan orang nya asik bangt",  
                "pesan": "semangat terus bang kuliah nya jangan lupa tetap jaga kesehatan,salam damaskus"# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakak nya asik,baik,ramah",  
                "pesan": "semangat terus kak kuliah nya dan tetap jaga kesehatan ya"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak cerine baik,ramah,seru",  
                "pesan": "semangat terus kak kuliah nya dan jangan lupa tetap jaga kesehatan ya"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "abang nya baik,ramah",  
                "pesan": "semangat terus bang kuliah nya dan tetap jaga kesehatan"# 1
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kaka nya baik,ramah,seru",  
                "pesan": "semangat terus ya kak kuliah nya semoga harinya menyenangkan"# 1
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Abang ini seru,ramah,baik",  
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak teresa baik,ramah",  
                "pesan": "semangat terus kuliahnya kak jangan lupa jaga kesehatan"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "bang hanif orang nya baik,ramah,seru",  
                "pesan": "semangat terus kuliahnya bang dan semoga harinya menyenangkan"# 1
            },
            {
                "nama": "Audina Fitria ",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak nya baik,ramah.asik",  
                "pesan": "semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat ",
                "sosmed": "@cikamrbn",
                "kesan": "Kakak cika baik,seru,ramah",  
                "pesan": "semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak nya baik,seru,ramah juga",  
                "pesan": "semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "bang harvin sodara nya dari anggota kelompok saya, kelaiatan nya asik",  
                "pesan": "semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "bang rafa baik,ramah,seru juga sepertinya",  
                "pesan": "semangat terus kuliahnya bang"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xPz8kEqyDo6aLB3ar6UVSon_RqiPeFqI",
            "https://drive.google.com/uc?export=view&id=11B9aAgqpk-gvh3KfU9Mg6_NXm74xihxa",
            "https://drive.google.com/uc?export=view&id=1ZczZGVO05NpWluhfAlQ5ODJRz2VUTBzM",
            "https://drive.google.com/uc?export=view&id=1md1xDX-3iTdUTQ1-YnddTRDwSxcu24_j",
            "https://drive.google.com/uc?export=view&id=163Wd4-LgHPDdmimeGKAe9Nvw-9ZHOGgE",
            "https://drive.google.com/uc?export=view&id=14fJuRZm-lge_jZ2kc0FQcfbPGD66FcBm",
            "https://drive.google.com/uc?export=view&id=1ZczZGVO05NpWluhfAlQ5ODJRz2VUTBzM",
            "https://drive.google.com/uc?export=view&id=1w_i0TOebRNrxDkkmvzwXA57cmbQ1jtLT",
            "https://drive.google.com/uc?export=view&id=10eF9tl5YHflxpKwnORHKUhLOJ-5b8may",
            "https://drive.google.com/uc?export=view&id=1Dqejl7gnhW7a-J8W227Ie_LIHJFy63r_",
            "https://drive.google.com/uc?export=view&id=1YlpQqz8wEFHbuaIJ4dxjNx_ltA9yWwma",
            "https://drive.google.com/uc?export=view&id=1x6riIymL2ptdv5egeEOFi0kuFvgLT5Dv",
            "https://drive.google.com/uc?export=view&id=1K9M7GSWfAKzDCeS9_YMj7o8tsyS4MY8N",
            "https://drive.google.com/uc?export=view&id=1s34hdS2w8NwlGoWFScFuxGBLdYbRiA2M",
            "https://drive.google.com/uc?export=view&id=1xfHmUAtLF3v1LBRJ518-4wVqx1DFjWzy",

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
                "kesan": "Bang kevin keren,baik, namanya bagus",  
                "pesan":"Semoga dilancarin ya bang kuliahnya sampai luluss"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kak razka asik, cantik, baik",  
                "pesan":"Semangat terus kak razkaa, semoga sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abang ini asik",  
                "pesan":"Semangattt bang kuliahnyaaa!"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak ini imut dan humble",  
                "pesan":"sehat sehat kakakk, jangan lupa bahagia"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abangnya asik dan baik.",  
                "pesan":"Lancar lancar yaa bang kuliahnya, semoga bahagia teruss"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakanya humble dan murah senyum.",  
                "pesan":"Semoga kakanya sehat teruss yh kakk"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang ini baik dan asik",  
                "pesan":"Semoga abangnya lancar rezekinya yhh, sehat selalu dan juga lancar kuliahnya"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak juwita ini lucuu",  
                "pesan":"Kakkk yang semangat yah kuliahnya semester ini, kaka pasti bisaa"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Dengerin laikha nyanyi",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang ridwan baikk dan talkative hahaha",  
                "pesan":"Bang ridwan semangat ya bang semester ini, nnt saya nyanyiin dah kl mumet WKWKWK"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Abang terexcited hahaha lucu",  
                "pesan":"Makasih udah excited terus bang andraa, semoga abang sehat dan bahagia selalu"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "Abang ini diem2 kocak gitu ya kayanya",  
                "pesan":"makasih udah dampingi bandalm latihan terus bang bryannnn"# 1
            },
             {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124",
                "umur": "...",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "....",
                "kesan": "....",  
                "pesan":"Semangattt bang bangg jadi pj game nyaaa hihi"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kaka ini lucuu n imup",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kak caca humble dan asikk",  
                "pesan":"Bahagia selalu kakakkk!!"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abang ini agak kalemm yaa, tapi baikk",  
                "pesan":"semangat terus kuliahnya abanggg !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1y0ub7Fp7CCPpAqKapx1lg8zKIiplouZn",
            "https://drive.google.com/uc?export=view&id=1paxQZxlUmZGcsc7rvl30dsLx63EFZz0I",
            "https://drive.google.com/uc?export=view&id=1ylTCcJxFtJxd7c4Amy_Qi54Drra-j0Ct",
            "https://drive.google.com/uc?export=view&id=1SXlla-CNEi32j1M3Pxm44LctcosP2VCv",
            "https://drive.google.com/uc?export=view&id=1W7rjG_ELsQtRVnGqPvbe61RCiXOYSCjf",
            "https://drive.google.com/uc?export=view&id=1y0ub7Fp7CCPpAqKapx1lg8zKIiplouZn",
            "https://drive.google.com/uc?export=view&id=1SXlla-CNEi32j1M3Pxm44LctcosP2VCv",
            "https://drive.google.com/uc?export=view&id=1FxHlMtMBrnPWKSo6BTHBWYYkFqMgtIcM",
            "https://drive.google.com/uc?export=view&id=1SXlla-CNEi32j1M3Pxm44LctcosP2VCv",
            "https://drive.google.com/uc?export=view&id=1pshWdn-kzMb5EtcFIE4jmpdM5WRT0ghD",
            "https://drive.google.com/uc?export=view&id=1mSzcJ5VpdnXGAaOlt_Zqnd9N2-85SCf8",
            "https://drive.google.com/uc?export=view&id=1t-RbKXsNjhZaXfTCvd_fNuPzj9WFFhrR",
            "https://drive.google.com/uc?export=view&id=1W7rjG_ELsQtRVnGqPvbe61RCiXOYSCjf",
            "https://drive.google.com/uc?export=view&id=1V7GX7sL27nVMEzpfXXwJ333Eba3vY8Qd",
            "https://drive.google.com/uc?export=view&id=1IrgO2zaRcg-_IpO8yC46zs3pvbEbRkhD",
            "https://drive.google.com/uc?export=view&id=1sxGsRbuTXW86GmngzBUWGKiHCsA6OiUR",
            "https://drive.google.com/uc?export=view&id=1gwHKW94er6A3UrooqbSTSpDe56relkim",
            "https://drive.google.com/uc?export=view&id=1rl9AOliC4tWrj3XkqmsbLVRdvhPmIpcZ",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "kak nya baik banget dan humble",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "kak nya baik banget dan humble",  
                "pesan":"semangat terus kuliahnya kakak"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis dan membaca",
                "sosmed": "@n1tg.-",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "1244500031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 9
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450014",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gaada yang tau",
                "asal":"Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "1244500112",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Piano",
                "sosmed": "@nzlhauly",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Allisha",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobbi",
                "sosmed": "@zydddddd__",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1pV-l4VzOcIYDFwNjGtLjsET6v1TdQKyc",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1gFvYRlXtAVDbvyGJQm4VohxKkMHfTMNN",
            "https://drive.google.com/uc?export=view&id=1Yy6xIoiyRZ5dpzc26IA4mo5Mr9zAzfyK",
            "https://drive.google.com/uc?export=view&id=1Nphtcp064KRPkR4xFL0C1t4xrBJ4Neff",
            "https://drive.google.com/uc?export=view&id=1JXQ7DBcux-1lfVf-SVj7rrMakg8yeWVE",
            "https://drive.google.com/uc?export=view&id=16C53mZGM1C5UF-P5-G1ITOoXsDqVZPlx",
            "https://drive.google.com/uc?export=view&id=1W8dJQWmXaxWJwo9KiYBdl5O1fjshIG3i",
            "https://drive.google.com/uc?export=view&id=1awSjKQBSUd0SYKzm5ffO1jd0HzFFgr_G",
            "https://drive.google.com/uc?export=view&id=1B6ehQ6FJGAg1pVe3fRKtou_PeOHlgCvk",
            "https://drive.google.com/uc?export=view&id=1n5YUcapsbKIdq8vFe5Z24eocL9psP0mN",
            "https://drive.google.com/uc?export=view&id=1sRyxOIp_xCqI-Si--i37snfahnII5NE4",
            "https://drive.google.com/uc?export=view&id=1okfOB-TrCpXQ0ItoAzjnPef0TfRT-l83",
            "https://drive.google.com/uc?export=view&id=1kxX-MQPK5L6wu8u7MQodovGkEgJqpprt",
            "https://drive.google.com/uc?export=view&id=1ocmw7-wxQYaVpIBLnsMeAmYVCyzjA5KX",
            "https://drive.google.com/uc?export=view&id=1a3UzdWWswHMVgo7lKR6dG0js0PqrZxAi",
            "https://drive.google.com/uc?export=view&id=1toUtLyoj44nF9R-9si_3_0hSk2ySN-c7",
            "https://drive.google.com/uc?export=view&id=1hLixRrzPCRmMOYd6X609k519qjZCV132",
            "https://drive.google.com/uc?export=view&id=1zbJzP6NskRz0ykKW-DcWYjKvVCDvAYv4",
            "https://drive.google.com/uc?export=view&id=1MV8bZMjzI993-Y50GJDYj5OAUSpCIIAz",
            "https://drive.google.com/uc?export=view&id=1DXUAM9QYHKyrH8LGFOlH8h-SCetMOGBO"
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
                "kesan": "Kak arini baik, ramah, dan asik",  
                "pesan": "semangat terus kak berorganisasi"  # 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakak nabyla orang nya baik ramah dan asik",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing Keributan",
                "sosmed": "@adityatfq",
                "kesan": "abang nya baik dan asik",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "abangnya baik dan asik",  
                "pesan":"semangat terus kuliahny"# 1
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak selma baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh Pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakak ini dan baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya"# 1
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kak indah medis kuu yang baik hatiii",  
                "pesan":"semangat terus kakkk my medis"# 1
            }, 
            { 
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "bang bima asik,baik ramah juga",  
                "pesan":"semangat terus kuliahnya"# 1
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "bang baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Love Earth",
                "hobbi": "Jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kaak adinda baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakak yolanda baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakak riska baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakak fathya baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },             
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakak tarisya baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "bang danil baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya"# 1
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "20",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "bang favian baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak"#1
            }, 
            { 
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "Situlah",
                "alamat": "Pohon mulia",
                "hobbi": "Nyari hobbi",
                "sosmed": "@zydddddd__",
                "kesan": "bang fathiy baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya"# 1
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "asal": "Balam",
                "alamat": "Balam",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kak"# 1
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "-",
                "sosmed": "@jaldii._",
                "kesan": "BANG JALDI ORANG NYA BAIK SERU JUGA RAMAH",  
                "pesan":"semangat terus kuliahnya"# 1
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "Nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakak nya baik,dan ramah",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya baik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "124450050",
                "umur": "21 Tahun ini alhamdulillah",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "bang ahmad orangnya baik, ramah, dan asik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            } 
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x7WbgTW7d6lIO0xxBX6U4Ayv1VSBiTm_", #fabio
            "https://drive.google.com/uc?export=view&id=15VwRAOLcljFTmxV017-pr7o2HywCkTym", #tanty
            "https://drive.google.com/uc?export=view&id=1QDvIoLcuzL9xaYInnaW2eBunmrPfqXdO", #fadyl
            "https://drive.google.com/uc?export=view&id=1UJs5X8Ilhsy-P-r7CAj9JsAeuUU1NHls", #nuel
            "https://drive.google.com/uc?export=view&id=1iiAn3yefi1s5wA-OKxGM4alU11MdgCaS", #viola
            "https://drive.google.com/uc?export=view&id=1OduU21db88woIT83j3G8qYKrv7zrkkGz", #risa
            "https://drive.google.com/uc?export=view&id=1LTp5DKsHI_bLukbrieBGbfVPaKN5QVcZ", #vanisa
            "https://drive.google.com/uc?export=view&id=1LU34K4Dauzrw_sJHtUiQZBUaxNI-RSas", #yulia
            "https://drive.google.com/uc?export=view&id=1hOwN5zL-7hJKO8DYsS-5MJEpU0eREqsG", #akeyla
            "https://drive.google.com/uc?export=view&id=1oNC6CAvWyxC8OBUTC-2f4cp0yYqN4JDD", #elsa
            "https://drive.google.com/uc?export=view&id=1tksSrauskPapvp7D6c8_Du-NKf-D2gxI", # fadya
            "https://drive.google.com/uc?export=view&id=1UH2Svg498rWaZNyXsO-3kBuYkgZCtgRJ", #lovi
            "https://drive.google.com/uc?export=view&id=1rsThU3r6CV806xdBtVVJqf3pOS-sNj3_", # asli
            "https://drive.google.com/uc?export=view&id=1fn21Rs1mBOgL0FfHIY4ybp_dpFoabyLT", #sherena
            "https://drive.google.com/uc?export=view&id=1XX9xJXacR2I_lz9fFfJG_JiA426FfkUl", #razin
            "https://drive.google.com/uc?export=view&id=1Gtkz8gsfACMo4sZ7OCPWEsbnc5D0m78K", #faiza
            "https://drive.google.com/uc?export=view&id=1dtTrAruNXzznR8JwNyXHnpJ9FL8hlNBN", #gathan
            "https://drive.google.com/uc?export=view&id=1bvkYKV6ha9LEALHV0Cn--bEN842Z5I2M", #pidzy
            "https://drive.google.com/uc?export=view&id=1A6EKI0wpoK7VltVt1uXyELF7im2uMwmz", #kaleb
            "https://drive.google.com/uc?export=view&id=1OduU21db88woIT83j3G8qYKrv7zrkkGz", #melva
            "https://drive.google.com/uc?export=view&id=18TCxAq0NOEIEH0VV9t-HL4EACYE-FSb6", #falakh
            "https://drive.google.com/uc?export=view&id=1DhCD2yBkOATvi4njoTCi27stuzNyGBms", #henry
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim" : "12340104",
                "asal" : "Bandar Lampung",
                "alamat" : "Kedaton",
                "hobbi": "Tidur",
                "umur" : "21",
                "sosmed" : "@biyokcb",
                "kesan" : "Abangnya keren suka marvel.",
                "pesan" : "Ayok nobar Doomsday bang."
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim" : "123450094",
                "asal" : "Lampung",
                "alamat" : "Airan Raya",
                "hobbi": "Membaca",
                "umur" : "21",
                "sosmed" : "@tvnty_",
                "kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampungku",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "Kenal pas waktu tpb kak asuh nya ternyata bang fadil.",
                "pesan" : "Tenang disana ya bang, Terimah kasih untuk ilmu yang pernah di berikan."
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim" : "124450005",
                "asal" : "Bali",
                "alamat" : "Nusa Penida",
                "hobbi": "Menghayal",
                "umur" : "12",
                "sosmed" : "Violaadrtr_",
                "kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "nama": "Risa Romadona",
                "nim" : "124450127",
                "asal" : "Natar",
                "alamat" : "Natar",
                "hobbi": "Rolling skate",
                "umur" : "20",
                "sosmed" : "risarmdna",
                "kesan" : "Aktif dan berani mencoba hal baru.",
                "pesan" : "Terus berani melangkah, Kak."
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan selalu terlihat ceria.",
                "pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim" : "1234501",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "umur" : "21",
                "sosmed" : "@keyashafi",
                "kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum dan enak diajak bicara.",
                "pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "nama": "Fadya Izzatul ‘Aini",
                "nim" : "124450062",
                "asal" : "Pringsewu",
                "alamat" : "Airan",
                "hobbi": "Mancing",
                "umur" : "20",
                "sosmed" : "fadyaizzatul_",
                "kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim" : "124450092",
                "asal" : "Kalianda",
                "alamat" : "Kotabaru",
                "hobbi": "Main Game, Tidur",
                "umur" : "20",
                "sosmed" : "@aluccy_",
                "kesan" : "Humoris dan gampang bikin tawa.",
                "pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "nama": "Sherena Florencia",
                "nim" : "124450027",
                "asal" : "Bengkulu Selatan",
                "alamat" : "Belwis",
                "hobbi": "Make up",
                "umur" : "19",
                "sosmed" : "sher_renna",
                "kesan" : "Rapi dan selalu tampil percaya diri.",
                "pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim" : "123450096",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Futsal",
                "umur" : "21",
                "sosmed" : "@razyn.hfd",
                "kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "nama": "Faiza Try Anjani",
                "nim" : "124450075",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Membaca Novel",
                "umur" : "19",
                "sosmed" : "FAIZAANJANII",
                "kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim" : "124450001",
                "asal" : "Bandar Lampung",
                "alamat" : "Rajabasa",
                "hobbi": "Main game",
                "umur" : "20",
                "sosmed" : "@gathfannadif",
                "kesan" : "Santai tapi tetap bertanggung jawab.",
                "pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim" : "124450064",
                "asal" : "Metro",
                "alamat" : "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "umur" : "20",
                "sosmed" : "@apiszzaja_",
                "kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim" : "124450087",
                "asal" : "Sumsel",
                "alamat" : "Sukarame",
                "hobbi": "Scroll",
                "umur" : "19",
                "sosmed" : "@melva_fbrt",
                "kesan" : "Ceria dan mudah menyesuaikan diri.",
                "pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
