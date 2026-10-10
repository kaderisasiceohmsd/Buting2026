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
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PaFVMM16zVLGAH5tC0fo8er7lcC0viI0",
            "https://drive.google.com/uc?export=view&id=1yCUD3uOmKTBl99yWejErFkethZMhpeJO",
            "https://drive.google.com/uc?export=view&id=1CXFOYQL0KK06gOXczNQJbLDTiZgiiYYl",
            "https://drive.google.com/uc?export=view&id=11JYhRq75vmupS7Fc93D2kQ5xFawdMrp1",
            "https://drive.google.com/uc?export=view&id=1OxMRDhINlMD0wbPadm5aYPSm9C8zVHtA",
            "https://drive.google.com/uc?export=view&id=1If9CVnfUGnvrYzaBOGioQ-ICAksX3ovD",
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
                "kesan": "Kahim asik hebat, berwibawa, dan mantap",  
                "pesan":"Semangat terus bang!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Sekjen yang baik hati dan jago steal bola baasket di LW",  
                "pesan":"Ayo Bang Aqil steal bola lagi! Semangat kuliahnya bang"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik, ramah, dan tampak baik hati",  
                "pesan":"semangat terus kuliahnya kak Efii"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "My Kakak NIM gweh, terlihat pintar asik dan ramah",  
                "pesan":"Semangat Kuliahnya Bangkuu!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak yang asik baik, hebat, ramah",  
                "pesan":"semangat terus kuliahnya kakaaaakkkkkkkk!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak yang baik, asik, ramah, hebat, mantap",  
                "pesan":"semangat terus kuliahnya kakak, dan tetaplah tersenyum kaakkk!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Tk-bJkKgzNMA-fm6OzLHKI6JBhpXYzi0",
            "https://drive.google.com/uc?export=view&id=1gFdiwtYuvhlucS-aG2ZqAqWG3XSPdR8f",
            "https://drive.google.com/uc?export=view&id=1lSnt4kHwVsefEtE5BpOqLOwA0gTVpI30",
            "https://drive.google.com/uc?export=view&id=1t30318dKeFArSSOGzg9zL3w8H02ECwfx",
            "https://drive.google.com/uc?export=view&id=1wtV5XGs-jc_B9FFd1BHPHV8OXZZeiRtw",
            "https://drive.google.com/uc?export=view&id=17AVkVCwdmhkiWhWgZGXTsOV8cRUpU4Ga",
            "https://drive.google.com/uc?export=view&id=1PdH3t9f6056847Z70yJ-Y0h53HHnpPQk",
            "https://drive.google.com/uc?export=view&id=1iRW7v7Su6lpURaFClHrFtx90nlfk8IFW",
            "https://drive.google.com/uc?export=view&id=1kPhDXJYVHB4WD19PTKSc9VhG6922TZiv",
            "https://drive.google.com/uc?export=view&id=18EGYQyL1pKeLgmmeL0_VvhE-AWDSGAb9",
            "https://drive.google.com/uc?export=view&id=1T3sv7gqjt0u6EHFaUn0T84r2iDbehJW9",
            "https://drive.google.com/uc?export=view&id=1fJNUW-uDrq-Mev2l-eLs3eYrJRG59bN3",
            "https://drive.google.com/uc?export=view&id=1ZkEfG9l4uOBmw_D-TY6Ueopt915vVu1F",
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
                "asal": "Tanggerang",
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

if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11SPNjtTzTXODqCtXKM2n7_a6LSDJ_xxu",
            "https://drive.google.com/uc?export=view&id=1dF4TAZE8WWOzKA77BMBo4Axtg2Tbtgmf",
            "https://drive.google.com/uc?export=view&id=1HH38KaJOHcAoQFsr3wg9CyrcRg7rULWK",
            "https://drive.google.com/uc?export=view&id=1EsxQ3vnQl3xssWpvIEDrsIP-tKRKg6Sq",
            "https://drive.google.com/uc?export=view&id=1HtjZB4BXt-Nkz5NIFTcHXN2Yf8Bscxa_",    
            "https://drive.google.com/uc?export=view&id=19MOjim3ecksjmg5D6q3L1RItrE9FMIqU",
            "https://drive.google.com/uc?export=view&id=1sj72ppDfSP2Gsb2OmRi9iCUgSUTADvq9",
            "https://drive.google.com/uc?export=view&id=1kAzNX33-iBiopIJS8lpofQVAgrc0qlWp",
            "https://drive.google.com/uc?export=view&id=1BTtrxCIJz_-KeuAK8nyw0svL9tuELoRu",
			"https://drive.google.com/uc?export=view&id=1raMhfhs03xggsGjGd2OIUocdKNrf4CRi",
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
        display_images_with_data(gambar_urls, data_list)
    Senator()
	
if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
            "https://drive.google.com/uc?export=view&id=.",
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
		        "kesan": "Bang Kevin keren abangnyaa, semangat terus bangg",
				"pesan": "Semangat terus bang Kevin, semoga kuliahnya lancar dan sukses selalu bangg!!"
		    },
		    {
		        "nama": "Gusti Putu Ferazka Dhiyamika",
		        "nim": "123450046",
		        "umur": "21",
		        "asal": "Bekasi",
		        "alamat": "Way Dadi",
		        "hobbi": ".",
		        "sosmed": "@ferazkaa",
				"kesan": "Bang Gusti keren bangett, baik bangett, asik orangnyaa",
				"pesan": "Semangat terus bang Gusti, semangat kuliahnyaa abangg"
		    },
		    {
		        "nama": "Ali Aristo Muthahhari Parisi",
		        "nim": "123450088",
		        "umur": "21",
		        "asal": "Lampung Timur",
		        "alamat": "Gang Sakum Belwis",
		        "hobbi": "Nonton F1",
		        "sosmed": "@ali_parisi3",
				"kesan": "Bang Ali keren bangett, apalagi hobinya nonton F1 wkwk",
				"pesan": "Semangat terus bang Ali ngejalanin tupoksinya, semoga kuliahnya lancar jugaa bangg"

		    },
		    {
		        "nama": "Ayu Andriani Parlina Wati",
		        "nim": "124450058",
		        "umur": "20",
		        "asal": "Lampung Barat",
		        "alamat": "Airan",
		        "hobbi": "Belajar + menghitung uang",
		        "sosmed": "@aayuandriani_",
		        "kesan": "Kakaknyaa cantik bangett, sangat ramah dan asik orangnyaa",
		        "pesan": "Semangat terus kak ayuu, semoga kuliah dan semua kegiatannya lancar kak"
		    },
		    {
		        "nama": "Dafa Elpriza",
		        "nim": "124450131",
		        "umur": "21",
		        "asal": "Bekasi",
		        "alamat": "Way Kandis",
		        "hobbi": "Jogging",
		        "sosmed": "@dafaelpriza_",
		        "kesan": "Abangnya baik banget, keren jugaa, asik orangnyaa",
		        "pesan": "Semangat abanggg kuliah dan latihannyaa"
		    },
		    {
		        "nama": "Juwita Sari",
		        "nim": "124450066",
		        "umur": "19",
		        "asal": "Lampung Barat",
		        "alamat": "Pemda",
		        "hobbi": "Mancing",
		        "sosmed": "@ju.juwitaaa_",
		        "kesan": "Kakaknya lucu bangett, asik juga diajak ngobrol",
		        "pesan": "Semangat kakak cantik kuliah dan menjalankan tupoksinyaa"
		    },
		    {
		        "nama": "Muhammad Afdal Luthfi",
		        "nim": "124450047",
		        "umur": "19",
		        "asal": "Lampung Tengah",
		        "alamat": "Jl. Pulau Damar",
		        "hobbi": "Memantau dl tugas",
		        "sosmed": "@afdall.03",
		        "kesan": "Abangnya seruu, baik bangett jugaaa",
		        "pesan": "Semangat bang afdal kuliahnyaa"
		    },
		    {
		        "nama": "Salsabila Nazwa Putri",
		        "nim": "124450002",
		        "umur": "20",
		        "asal": "Metro",
		        "alamat": "Korpri",
		        "hobbi": "Nongkrong di kopken",
		        "sosmed": "@slbnzw_",
		        "kesan": "Kakaknya cantik bangett, ceria bangett, keren bangett",
		        "pesan": "Kakak semangat kuliahnya yaa kak"
		    },
		    {
		        "nama": "Muhammad Ridwan",
		        "nim": "123450091",
		        "umur": "21",
		        "asal": "Lampung Tengah",
		        "alamat": "Belwis",
		        "hobbi": "Badminton",
		        "sosmed": "@mridwaan_22",
		        "kesan": "Abangnya baik bangett, sabar bangett, asik seruu diajak ngobrol",
		        "pesan": "Semangat terus abang menjalankan tupoksinya dan ngerjain TA nyaa"
		    },
		    {
		        "nama": "Andra Ilham Bintang",
		        "nim": "124450060",
		        "umur": "18",
		        "asal": "Sumatera Selatan",
		        "alamat": "Kotabaru",
		        "hobbi": "Main rubik",
		        "sosmed": "@andra.lhm",
		        "kesan": "Abangda mentor gridicuwikuki yang paling keren, paling baik. paling ganteng, paling pintar, paling masyallah tabarakallah alhamdulillah dapat mentor kek abangda",
		        "pesan": "Semangat abang baik kuliah dan latihan basketnyaa. Semoga ditengah jalan nemu laporan KP, Jurnal 5 tahun terakhir, judul TA terus TA nya 1 bulan selesai"
		    },
		    {
		        "nama": "Bryan Paskah Telaumbanua",
		        "nim": "124450003",
		        "umur": "20",
		        "asal": "Nias",
		        "alamat": "Belwis",
		        "hobbi": "Live tiktok",
		        "sosmed": "@bryantel_",
		        "kesan": "Bang bryan baikk bangett, seruu, asik jugaa",
		        "pesan": "Nanti aku join live tiktoknya bang"
		    },
		    {
		        "nama": "Ghiyats Thabularasa Meardhy",
		        "nim": "124450067",
		        "umur": "17",
		        "asal": "Surabaya",
		        "alamat": "Kemiling",
		        "hobbi": "Nanem Sawit",
		        "sosmed": "@meardhy_ghiyats",
		        "kesan": "Abangnya kerenn, baik banget dan asik jugaa pas wawancara",
		        "pesan": "Infokan kebun sawit buat dipalingin bang"
		    },
		    {
		        "nama": "Indah Julia Mawar Pratiwi",
		        "nim": "124450055",
		        "umur": "20",
		        "asal": "Pringsewu",
		        "alamat": "Airan",
		        "hobbi": "Bengong",
		        "sosmed": "@indahjuliaa",
		        "kesan": "Kakaknya cantikk banget, kerenn terus seruu banget kakaknyaa",
		        "pesan": "Semangat kakak cantik kuliahnyaa, semangat jugaaa menjalankan tupoksinyaa"
		    },
		    {
		        "nama": "Jacinda Kesya Alvara",
		        "nim": "124450023",
		        "umur": "18",
		        "asal": "Kalimantan Barat",
		        "alamat": "Korpri",
		        "hobbi": "Nyapu depan gacoan",
		        "sosmed": "@cacalvra",
		        "kesan": "Kakaknya ceria bangett, cantik bangett, keren bangett",
		        "pesan": "Semangat terus yaa kakak cantik kuliahnyaa"
		    },
		    {
		        "nama": "Muhammad Rafka",
		        "nim": "124450089",
		        "umur": "20",
		        "asal": "Padang",
		        "alamat": "Kotabaru",
		        "hobbi": "Bangun pagi",
		        "sosmed": "@muhammdrafka_",
		        "kesan": "Abangnyaa baik bangett, keren banget jugaaa",
		        "pesan": "Sukses terus abangg, semangat yaa abang kuliahnyaaa"
		    }
		]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()
# Tambahkan menu lainnya sesuai kebutuhan
