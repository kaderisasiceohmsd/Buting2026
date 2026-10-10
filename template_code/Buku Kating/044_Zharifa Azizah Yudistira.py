
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
            "Badan Legislatif",
            "Badan Kesenatoran",
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

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12c4HoUv_7ybIIRiVUarGlOrPdvmP-UJp",
            "https://drive.google.com/uc?export=view&id=1uBQjMofh6xoZ3a2qa6oLWTici0hKOzGw",
            "https://drive.google.com/uc?export=view&id=1md8uzDaCwQD7S83jP1PpYbRiv-DFfXmj",
            "https://drive.google.com/uc?export=view&id=1msXyEAAoRiWRbkl6fTG4d2BraUUAu3KC",
            "https://drive.google.com/uc?export=view&id=117IVKdyqqu7V-qYanyZMnb1YoQj36iaq",
            "https://drive.google.com/uc?export=view&id=11BWvexjOAk9uBYCZJkqujxpIRqqD7khu",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Ginda kesannya baik, seru, asik juga dan ternyata sesuai sama kesannya, terus pas wawancara juga jawaban abangnya keren",  
                "pesan": "Semangat abang kahim, semoga cepat selesai TA nyaa"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya baik, terus kalo ngajar materi juga seru, keren juga kalo ngasih petuah bijak banget jujur",  
                "pesan": "Semangat abang sekjen kita semester 7 nyaa, semoga TA cepet selesaii ketemu di riuh wisudah nanti kitaa abang"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak cantik sekali, baik jugaa, ramah, cantik pokoknya",  
                "pesan": "Semangat kakak sekre kita yang paling cantik, semoga TA nya cepat selesaii"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keren, baik banget saat wawancara, seruu banget jugaa",  
                "pesan": "Semangat abang menjalankan tupoksinya dan semangat juga untuk TA nya abangg"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya cantik terus seru jugaa pas wawancara, kerenn kakaknyaa",  
                "pesan": "Semangat kakak bendaharaa, semoga TA nya cepat selesai kakak"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya cantik terus lucuu banget hobi ketemu pak tirtaa",  
                "pesan": "Semangat kakak mengerjakan TA, meet sama pak tirta + menjalankan tupoksinya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1S9a3wfmCNtl92iDQJkLRL91Pg7jakU5v",
            "https://drive.google.com/uc?export=view&id=1etH0Xb1VCQJZPbm7kg7OqqWXB2KzfWzR",
            "https://drive.google.com/uc?export=view&id=12MogNBBIACViZGMsZOWaFaDuK7R9gwj9",
            "https://drive.google.com/uc?export=view&id=1ietblJPahxJvnt4rXvx9NSqyzEzA_B7F",
            "https://drive.google.com/uc?export=view&id=1O4JgbsL6Q8j5SnUy7xwnO_rTvYaDk8HP",
            "https://drive.google.com/uc?export=view&id=1sWA_T1boU0EqUpgt4D50fMaflw0a5UMP",
            "https://drive.google.com/uc?export=view&id=1VvuV7sATqepvEryDH3B2g2SpT3UiKqNp",
            "https://drive.google.com/uc?export=view&id=14U22QTQSkLCPTsWM8NZ6aizeQ8BKOH72",
            "https://drive.google.com/uc?export=view&id=1PsFMYho5W7nljge2w7T1_W0X34Dq-FVR",
            "https://drive.google.com/uc?export=view&id=1otrqRKrjN9ttaoKjJkwIGWdZcvul2FkK",
            "https://drive.google.com/uc?export=view&id=1-SIM2lZ10K1y3iziCPtDTOhcIivZsATU",
            "https://drive.google.com/uc?export=view&id=1ZBk4ifw3E84sSeR5ysMLRWD81oXaSCq4",
            "https://drive.google.com/uc?export=view&id=1_cxnAWxAQ1sgiP5uGCKVysQYLIPrZDHD",
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
                "kesan": "Kesan pertama kali liat bang dido kek serem abangnya, ternyata baik banget, seru, asik, sangat masyallah tabarakallah",  
                "pesan": "Semangat bang dido main futsalnya, hati-hati dijalan jangan lupa live nyaa wkwk"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya cantikk banget, suka kalo ngobrol sama kak jue banyak obrolannya terus kakaknya seru banget jugaa",  
                "pesan": "Semangat kakak cantik TA dan penyiarannyaa, aku fans berat kakak, ditunggu cerita-cerita seru lainnyaa"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Abang ini keren banget pas KDP, aku ngefans bang, terus pintarnya pintar banget (wajar ozt ini)",  
                "pesan": "Infokan tutor mapress nya dong abangdaa"# 1
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Bang niko baik banget, sangat chill, sangat baik, sangat keren",  
                "pesan": "Semangat abangg kuliahnyaa, infokan tutor jadi pimsit"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Kakaknya cantik, terus kaget karena nama kami mirip, kakaknya sarifah aku zharifa, sama sama dipanggil rifa lagi",  
                "pesan": "Semangat kakak rifa kuliahnya - dari adik rifa"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip seru banget orangnya, asik, baik bangett juga, penjelasan studi kasusnya masuk akal",  
                "pesan": "Tutorkan kiat jadi kepala komisi II banggg"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya cantik dan baik bangett pas ngewawancarai aku, seru jugaa, terus kakaknya pas ngejawab pertanyaan di kelas masuk akal banget",  
                "pesan": "Kakak pj kami semangat yaa ngejalanin tupoksinyaa, semangat juga menghadapi huru hara semester 5 nyaa"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak ini cantik bangett, suka kalo ngeliat kakak ini karena cantik banget pas aku di semester 1",  
                "pesan": "Semangat kak hani kuliahnyaa, semangat juga di baleg nya, kelompok greedy cinta kakak kokk"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang ini keren banget kalo nyanyii udah kek lagi di Orkestra Sydney",  
                "pesan": "Abang semangat kuliahnya, semangat ketok ketok palunyaa, semangat abangg"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica keren banget pas ngejawab kalo dikasih pertanyaan, sukaa kerenn, cantik banget kakaknya jugaa",  
                "pesan": "Kak monica semangat kuliahnyaa, semangat jugaa di baleg, kamu keren kak cantik bangett"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Abangnya asik banget, baik banget, keren banget, palu nya juga keren banget",  
                "pesan": "Abang semangat kuliahnyaa, semangat ngebalegnyaa, infokan tutor ketok-ketok palunya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Kakaknya baik bangett, seru ngobrol sama kakaknya, terus ternyata kakaknya di baleg keren bangettt",  
                "pesan": "Semangat kak sekar pdd-in balegnyaa, semangat juga kuliahnyaa kakak"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya cantik banget, ceria banget, suka kalo ngobrol sama kakak soalnya kakaknya seru banget pas diajak ngobrol",  
                "pesan": "Kak Nashwa semangat yaa TA nyaa, sehat sehat kakak semester 7 dan kakak baleg"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Badan Kesenatoran":
    def bason():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kfsDzh0GuhsMEzhDdFSLlMpaDbTFM9j7",
            "https://drive.google.com/uc?export=view&id=16sCBm1YpXgr3jPky-NQJLlX2vR2Mx_ko",
            "https://drive.google.com/uc?export=view&id=1xw3BMBt23OFcnN2QueVk8IthDltpi3ix",
            "https://drive.google.com/uc?export=view&id=1vgsu3sIq-r98fQcVRsdPZvjpuVImOCy8",
            "https://drive.google.com/uc?export=view&id=17L2NMq0Ks5w9g4dpRLldpS8zPsgEtN5b",
            "https://drive.google.com/uc?export=view&id=1XBnNkDEgsaeUu-PUr1ip9A_kN4sK6b5f",
            "https://drive.google.com/uc?export=view&id=1DSqeVvOR4b3r-jhWnbzYtn-MC-r7f8xH",
            "https://drive.google.com/uc?export=view&id=1numH0a1kzhVRH7XmeyCfdBeN0nHdT0d_",
            "https://drive.google.com/uc?export=view&id=16vhK-aUqvcEfZeqliAgdXGMbE16ABHGv",
            "https://drive.google.com/uc?export=view&id=1jCPM0UQ-rDZfuzQXvi7tqfuWp6FPUla0",
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
                "kesan": "Kakaknya keren banget jujur, hebat banget bisa jadi senator terus kakaknya cantik banget",  
                "pesan": "Semangat kakak cantikk kuliahnyaa, semangat juga menyampaikan aspirasi kami kakak dan terimakasih"# 1
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": "Abang ini lucu bangett pas wawancaraa #dutamelet, baik banget jujur, asik banget juga",  
                "pesan": "Semangat abang baik kuliahnyaa, kamu keren bangg"# 1
            },
	 {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang nando baik orangnya, seru jugaa, keren juga, masyallah sekali",  
                "pesan": "Semangatt abang kuliahnyaaa"# 1
            },
	 {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya cantik bangett, pertama kali ketemu kakaknya aku kaget karena cantik nya cantik banget",  
                "pesan": "Semangat kak sucii kuliah dan mendampingi cosvalnyaa, jangan lupa senyum kakak cantik"# 1
            },
	 {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya asik bangettt seruuuuuu, baik banget banget jugaa, seru ngobrol sama abangnya",  
                "pesan": "Semangat bang wielman kuliahnyaa, semangat juga agenda mancingnyaa"# 1
            },
	 {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia itu keren bangett pas nyampaikan materi, keren banget, aku kagumm",  
                "pesan": "Semangat kak lia kuliahnyaa, semangat juga ngerjain TA nyaa semoga cepat selesai"# 1
            },
	 {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak qila itu cantik banget gemasss, lucu juga kakaknyaa",  
                "pesan": "Semangat kuliahnyaa kakakn cantik secantik bunga matahari"# 1
            },
	 {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang hazel keren bangett, baik jugaa, ngefans aku bang",  
                "pesan": "Semangat abangg kuliahnyaa, semangat basonnyaa, semangatt"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak nadya cantik banget, keren bangett pas materii",  
                "pesan": "Kakak semangat yaaa kuliahnyaa kamu keren bangett"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Ibu mentor yang cantik, baik, imup nan lucu sekaliii",  
                "pesan": "Semangat kak dwiiii kuliahnyaaa, greedy cinta kamu kakakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    bason()
