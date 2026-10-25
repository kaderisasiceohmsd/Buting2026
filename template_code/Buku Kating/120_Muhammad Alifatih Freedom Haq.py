
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
            "https://drive.google.com/uc?export=view&id=13uICtUwL-aM5enplnlX_2VZvaHsMJHJ_",
            "https://drive.google.com/uc?export=view&id=1BbQf-5BpzeyuR_RC11WX8mwsnTEFJCGX",
            "https://drive.google.com/uc?export=view&id=15m6l0IV3GJH_NfWYddZmvraS11NHREfI",
            "https://drive.google.com/uc?export=view&id=1ind3WsbXYA0mzV8_G8r86Uq4_tSprZ5Z",
            "https://drive.google.com/uc?export=view&id=1GeDJfc3l7GoK5WkkjVeJOgCYoqDc2AJ4",
            "https://drive.google.com/uc?export=view&id=1uPHwP9WUjPnNm2X8FjUoQOAA9knd6l_y"
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
                "kesan": "Keren dan berwibawa, keren banget manage waktunya",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya chill bangett, dan memperoleh banyak ilmu dari sekjen",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya seruuuu",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mPKvjtuPReWM3NyJ74q18TPOhZ1E2gAY",
        	"https://drive.google.com/uc?export=view&id=1kz0VzpUYdwT2HUizZXM3rxmZaJR3MkQB",
        	"https://drive.google.com/uc?export=view&id=149zm-CpBFt9e_OmC7xZgHoSs_0I98kQx",
        	"https://drive.google.com/uc?export=view&id=1HHQC3Anq4kldQYJ0xOn4l34ROJQbyI8H",
        	"https://drive.google.com/uc?export=view&id=1FJTKIvBq1v-kzxkNGGiPGM948jkB2srn",
        	"https://drive.google.com/uc?export=view&id=1595YDSqXuJ_KVJFTGuHG4NgayssDbpf2",
        	"https://drive.google.com/uc?export=view&id=1_1I26DxT0-9-BYgUbbVZxjIrNXJLlgfT",
        	"https://drive.google.com/uc?export=view&id=1oiGeGpwkjB2wATAfqhyS-R417Y6_6mYN",
        	"https://drive.google.com/uc?export=view&id=1VjxqSTdq2G3_x7b_5owRYt4cxdAp_QR5",
        	"https://drive.google.com/uc?export=view&id=1qPafJsfrNA8A3lrYPm26yy6yga4Plj41",
        	"https://drive.google.com/uc?export=view&id=1f-QGnkcaTXgJXHGB4axk9ZlWU3UuvYpt",
        	"https://drive.google.com/uc?export=view&id=1ela06RiCy4pwPloedYA-qgt3Gh66t5Hg",
         	"https://drive.google.com/uc?export=view&id=1yXUpB4i-lCLZHYr_WuQsyemTtjDBjl95",
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
                "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha",  
            	"pesan":"Semangat bang TA nyaa, semoga dilancarkan semuanya dan lulus tepat waktu ya bangg. Anak magang baleg selalu mendoakan yang terbaik untuk ayah dido"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marsel",
                "sosmed": "@j__eesie",
                "kesan": "GEMASSSSS! beneran imut kakanya dan seru banget dengerin storytelling ka juee, karena kayak sivia the catchup club cara kaka ngomong",  
            	"pesan":"Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupin api baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "Pinter bnaget abangg, tips and trik mapres bangg",  
            	"pesan":"Semangat kuliah dan TA nya, semoga dimudahkan seluruh urusannya, aamiin!"# 1
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Lucu banget jokes jokes abangnyaa",  
            	"pesan": "Semangat terus kuliah dan organisasinya!"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "Imutt sekali kakanyaaa",  
            	"pesan":"Semangattt kaa kuliahnyaa, kaka imut balegg"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "19",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip chill banget orangnyaa dan seruu",  
            	"pesan":"Semangat terus bang kuliahnya dan semoga dimudahkan TA nya ya banggg, Aamiin!"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "kesan": "Public speakingnya bagus, aku dukung kaka jadi the next kadiv komisi 2 #YIPPIE",  
            	"pesan":"Semangat kaa kuliah dan organisasinyaa!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu dan gemas bangettt",  
            	"pesan":"Semangat ka menghadapi bang Ridhoo, semoga dilancarkan semua urusannya kaaa!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Keren dan berwibawa",  
            	"pesan":"Semangat bang kuliahnyaaa!"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Lucu, gemas, tapi tegas",  
            	"pesan":"Semangat kaa kuliah dan organisasinyaaa!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "Lucu abangnya, jokes jokesnya juga fresh",  
            	"pesan":"Semangat abang kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Tegas tapi chill juga",  
            	"pesan":"Semangat terus ka kuliah dan organisasinyaa!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Lemah lembut sekaliii",  
            	"pesan":"Semangat kaa TA dan kuliahnyaa!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()


if menu == "Badan Kesenatoran":
    def Bason():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HZUoRpaiSRpZPuGv-waY0aS9C4j3xjqF",
            "https://drive.google.com/uc?export=view&id=1k2_DcBtU9h1FKm8RoB0KDbtdxN7K2AlK",
            "https://drive.google.com/uc?export=view&id=1Y4hgLEo6WDpQVaPCVeQwDB9-Cre8LUJz",
            "https://drive.google.com/uc?export=view&id=1Ro-dM162HJsf8W7JqZmn0yV8UAINvRHg",
            "https://drive.google.com/uc?export=view&id=1k0xsgWXOTMGHe24wfhPMiqJretLJzbME",    
            "https://drive.google.com/uc?export=view&id=19nWLBZus_xxByEIz7azuKKpwWEFVSZ8p",
            "https://drive.google.com/uc?export=view&id=1BUtMtwPikI8_od5GoZGp1cUsIUQ7FXLI",
            "https://drive.google.com/uc?export=view&id=1ZQM7PMvTGDhKDPljddVbTg-OWKJU1bFW",
            "https://drive.google.com/uc?export=view&id=15c0sdS85UPfmXdCOI6j9gsXk_IJYnd7m",
            "https://drive.google.com/uc?export=view&id=1u0Hlacgo1bqFEo8qVrpBDUemm2j7t4EV",
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
    Bason()


elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dFkoXY5zzFe0Rfa9thtZqq6eTlv--Jzk",
            "https://drive.google.com/uc?export=view&id=1ouZCVGgXTVIRLJpaWdmm45U_359KglCr",
            "https://drive.google.com/uc?export=view&id=1sbOP9gVntI2Fz6jqBxbfgpZTaxp1Yzh9",
            "https://drive.google.com/uc?export=view&id=16_NHdVaA2z7on2J7ohMt5CrtbgzF24cu",
            "https://drive.google.com/uc?export=view&id=1pqdHDBIo7ft2vjWzu4STc-28OWNUHFM7",
            "https://drive.google.com/uc?export=view&id=1lrCl8uaWWW_GqCtPiXAw6PsHjUvCp3pg",
            "https://drive.google.com/uc?export=view&id=1WpAmkzFVMFmCPrT2P5zkuCdMnkQo3BYS",
            "https://drive.google.com/uc?export=view&id=14ayZfsihOL7CWHbHtwEsmsFVCy7azZrR",
            "https://drive.google.com/uc?export=view&id=1TZZlYwcI8zmClsvaxgHjTC5T-6waso_D",
            "https://drive.google.com/uc?export=view&id=1bt2Ip-IeexTc9Z57Yxd6cjgUKBIP9H9k",
            "https://drive.google.com/uc?export=view&id=1iHWbbLnnYsxiRSC-aTUJvPjLhbtAA8o_",
            "https://drive.google.com/uc?export=view&id=1x8mUZaN8Csf7wK_S1HMeNweth6rND00P",
            "https://drive.google.com/uc?export=view&id=1huYkCRMz_ljUNN3e4TjPtuJQwegcfI11",
            "https://drive.google.com/uc?export=view&id=1HWNanbYQChsW9PvuNoeli6RZmCFc76BE",
            "https://drive.google.com/uc?export=view&id=1FLbNMVkhu82bIuXUSJ2NJa2tYai5tQmq",
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
        "kesan": "Sangat menginspirasi dan memimpin dengan baik",
        "pesan": "Semangat terus kak!"
    },
    {
        "nama": "Gusti Putu Ferazka Dhiyamika",
        "nim": "123450046",
        "umur": "21",
        "asal": "Bekasi",
        "alamat": "Way Dadi",
        "hobbi": "Mendaki",
        "sosmed": "@ferazkaa",
        "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
        "pesan": "Sukses selalu kak!"
    },
    {
        "nama": "Ali Aristo Muthahhari Parisi",
        "nim": "123450088",
        "umur": "21",
        "asal": "Lampung Timur",
        "alamat": "Gang Sakum Belwis",
        "hobbi": "Nonton F1",
        "sosmed": "@ali_parisi3",
        "kesan": "Keren dan selalu memberikan arahan yang jelas",
        "pesan": "Semangat menjalankan tugasnya kak!"
    },
    {
        "nama": "Ayu Andriani Parlina Wati",
        "nim": "124450058",
        "umur": "20",
        "asal": "Lampung Barat",
        "alamat": "Airan",
        "hobbi": "Belajar + menghitung uang",
        "sosmed": "@aayuandriani_",
        "kesan": "Sangat ramah dan aktif berkontribusi",
        "pesan": "Tetap semangat dan sukses terus!"
    },
    {
        "nama": "Dafa Elpriza",
        "nim": "124450131",
        "umur": "21",
        "asal": "Bekasi",
        "alamat": "Way Kandis",
        "hobbi": "Jogging",
        "sosmed": "@dafaelpriza_",
        "kesan": "Sangat menyenangkan dan mudah diajak kerja sama",
        "pesan": "Sukses terus perkuliahan dan aktivitasnya!"
    },
    {
        "nama": "Juwita Sari",
        "nim": "124450066",
        "umur": "19",
        "asal": "Lampung Barat",
        "alamat": "Pemda",
        "hobbi": "Mancing",
        "sosmed": "@ju.juwitaaa_",
        "kesan": "Sangat baik dan murah senyum",
        "pesan": "Semangat terus kuliahnya!"
    },
    {
        "nama": "Muhammad Afdal Luthfi",
        "nim": "124450047",
        "umur": "19",
        "asal": "Lampung Tengah",
        "alamat": "Jl. Pulau Damar",
        "hobbi": "Memantau dl tugas",
        "sosmed": "@afdall.03",
        "kesan": "Sangat bertanggung jawab dan fokus",
        "pesan": "Semangat terus kakak!"
    },
    {
        "nama": "Salsabila Nazwa Putri",
        "nim": "124450002",
        "umur": "20",
        "asal": "Metro",
        "alamat": "Korpri",
        "hobbi": "Nongkrong di kopken",
        "sosmed": "@slbnzw_",
        "kesan": "Sangat asik dan ceria",
        "pesan": "Tetap semangat kuliahnya ya kak!"
    },
    {
        "nama": "Muhammad Ridwan",
        "nim": "123450091",
        "umur": "21",
        "asal": "Lampung Tengah",
        "alamat": "Belwis",
        "hobbi": "Badminton",
        "sosmed": "@mridwaan_22",
        "kesan": "Sangat mengayomi dan membimbing dengan sabar",
        "pesan": "Semangat terus memimpin divisinya kak!"
    },
    {
        "nama": "Andra Ilham Bintang",
        "nim": "124450060",
        "umur": "18",
        "asal": "Sumatera Selatan",
        "alamat": "Kotabaru",
        "hobbi": "Main rubik",
        "sosmed": "@andra.lhm",
        "kesan": "Sangat kreatif dan pintar",
        "pesan": "Sukses selalu kuliahnya!"
    },
    {
        "nama": "Bryan Paskah Telaumbanua",
        "nim": "124450003",
        "umur": "20",
        "asal": "Nias",
        "alamat": "Belwis",
        "hobbi": "Live tiktok",
        "sosmed": "@bryantel_",
        "kesan": "Sangat menghibur dan ramah",
        "pesan": "Semangat terus berkarya kak!"
    },
    {
        "nama": "Ghiyats Thabularasa Meardhy",
        "nim": "124450067",
        "umur": "17",
        "asal": "Surabaya",
        "alamat": "Kemiling",
        "hobbi": "Nanem Sawit",
        "sosmed": "@meardhy_ghiyats",
        "kesan": "Sangat unik dan bersemangat",
        "pesan": "Tetap semangat dan sukses selalu!"
    },
    {
        "nama": "Indah Julia Mawar Pratiwi",
        "nim": "124450055",
        "umur": "20",
        "asal": "Pringsewu",
        "alamat": "Airan",
        "hobbi": "Bengong",
        "sosmed": "@indahjuliaa",
        "kesan": "Sangat baik dan bersahabat",
        "pesan": "Sukses terus perkuliahannya kak!"
    },
    {
        "nama": "Jacinda Kesya Alvara",
        "nim": "124450023",
        "umur": "18",
        "asal": "Kalimantan Barat",
        "alamat": "Korpri",
        "hobbi": "Nyapu depan gacoan",
        "sosmed": "@cacalvra",
        "kesan": "Sangat ceria dan menyenangkan",
        "pesan": "Semangat terus ya kak!"
    },
    {
        "nama": "Muhammad Rafka Fatih Al Ghathfaan",
        "nim": "124450089",
        "umur": "20",
        "asal": "Padang",
        "alamat": "Kotabaru",
        "hobbi": "Bangun pagi",
        "sosmed": "@muhammdrafka_",
        "kesan": "Sangat disiplin dan dapat diandalkan",
        "pesan": "Sukses selalu buat perkuliahannya!"
    }
]
  
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()
    
if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CmMENsIg2aupLCIfzJu3npUhP0ENkEwd",
            "https://drive.google.com/uc?export=view&id=1vl3HPdMa95JJZHNe743s8cTG33Tk7yCE",
            "https://drive.google.com/uc?export=view&id=1be33eaRBWzmojsURmFQLlCd782utxra0",
            "https://drive.google.com/uc?export=view&id=1xj0uLa9NrXJxt4VT-FDlS_jKRt3ZR7vW",
            "https://drive.google.com/uc?export=view&id=1KiBtY1Qnlwxbo_N8xdlP7qA356gomBqU",
            "https://drive.google.com/uc?export=view&id=1vlH6265l22eWWAx_py4bhIMxCyluxC2w",
            "https://drive.google.com/uc?export=view&id=1dTSuQ7nyyk2N6IkhZHdojHjtwy_ppvts",
            "https://drive.google.com/uc?export=view&id=1pHz0GOkrkwu7ToUmOe-m35_LnPfSdxEv",
            "https://drive.google.com/uc?export=view&id=1f6e-hSP7qihaAa0hNClHXTkmvCKnXc-O",
            "https://drive.google.com/uc?export=view&id=106_UyztpX07GKIzRpIPuS9D2V_-1cNP4",
            "https://drive.google.com/uc?export=view&id=1Z5zo3p77LVgH1Lu3Piwtv_eavqpt96-_",
            "https://drive.google.com/uc?export=view&id=1A3lHzORWtxs3a67qAUled6iMXZC49sgS",
        ]

        data_list = [
            # --- Pimpinan & Sekretaris ---
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450000",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            # --- Divisi Kemitraan ---
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "Semangat terus kuliahnya kakak !!!"  
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()


if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [ 
            "https://drive.google.com/uc?export=view&id=183k16AoHkTUktFlI3AZ1_W-MbtNMEA3k",
            "https://drive.google.com/uc?export=view&id=1gMvVn8mtfgamx9T7ERggSnaRMclwyLy8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1pHe1ymk1ky1yVe8oRPDHB6i2w7f_3QIa",
            "https://drive.google.com/uc?export=view&id=1vPEfAV3rbUN3bqei2tGOBWDmJ337PPzI",
            "https://drive.google.com/uc?export=view&id=1HSBFN1x64xqcVgS7B604goY78BpOU6r-",
            "https://drive.google.com/uc?export=view&id=1iU8ir2PQEfOCcHU7oLlVzuQZqX7E5iOK",
            "https://drive.google.com/uc?export=view&id=1D97TZadKandGYpPCALxNFQ7kbEUS36jD",
            "https://drive.google.com/uc?export=view&id=1f_2ggNOXI0RS23gtDUytScYXxE_USU-q",
            "https://drive.google.com/uc?export=view&id=1YBGIgwOg0A55qju5mB7VjX37I4R-DW2L",
            "https://drive.google.com/uc?export=view&id=1wCeXyFM2Ke3C-Wtkt6gVr6a_MRO8Qsue",
            "https://drive.google.com/uc?export=view&id=12G_wnWsKMrhhGTYRy_PDioQWtKY8ePDM",
            "https://drive.google.com/uc?export=view&id=1UorSEpoTGfKxwuFxYOASOiNsI1eAQJqe",
            "https://drive.google.com/uc?export=view&id=1f6la1Sts8od4yXwrsk2CSnH7OKMCzHgV",
            "https://drive.google.com/uc?export=view&id=1gnWMdoOZ8VdPPDtB16kO2C1wao9EacGi",
            "https://drive.google.com/uc?export=view&id=1MZeJ6i-kxlql0Qufe7ybp8Pxzf0aTq3h",
            "https://drive.google.com/uc?export=view&id=1RovSz6KLqvkodHtt2OhB4LlVI2Ry2AJe",
            "https://drive.google.com/uc?export=view&id=1NNCMcdTACb9SbvhBhTL117BV7VxLgZtL",
            "https://drive.google.com/uc?export=view&id=1BcPSYbRBepnkT4wj69nyqKr83YgH8i3G",
            "https://drive.google.com/uc?export=view&id=1OJT24OYBkSjm1nSBMk_czxfDcDC_lg6H",
            "https://drive.google.com/uc?export=view&id=1hyVOpdSHBJ14uHGnlE0oBmNQeQyawJvJ",
            "https://drive.google.com/uc?export=view&id=16yGIaMQSo42fALYk7pAQfjWANWhWkrmL",

        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game & travel",
                "sosmed": "@biyokcb",
                "kesan": "JUJUR KEREN BANGETTTT, saya beneran perlu berguru dengan abang",
                "pesan": "Semangatt TA nya nanti banggg, tapi saya beneran butuh banget banyak belajar ke abang karena ilmu abang DAGING semuaaa"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "First impression ku ke kaka, kaka ceria bangettt beneran gemasss",
                "pesan": "Semangatt TA nya kaa, semoga diberikan kelancaran dalam mengerjakan TA, jangan lupa jaga kesehatan!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "Inspiratif bangett",
                "pesan": "Masih ga nyangka secepat itu abang kembali ke pangkuan-Nya, tapi sekarang abang udah ga sakit lagi ya.. Doa terbaik untuk mu bang Fadil, fly high and rest in peace a good soul"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Proker stecu abang beneran membantu saya-^^",
                "pesan": "Abang keren bangett, dilanjutkan ya bangg. Jangan lupa jaga pola tidur dan makan nya!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kaka cantikk",
                "pesan": "Kaka semangat kuliahnya yaa, jaga pola makan dan pola tidurnyaa, jangan sampe drop yaa!!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Cutee",
                "pesan": "kakaa kerennn, semoga kaka selalu menemukan kebaikan di setiap hal hal kecil yaa! jaga kesehatan kaa!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "waktu kaka menjelaskan proker LEGACY jujur keren bangettt",
                "pesan": "Semoga apapun plan kaka bisa tercapai satu persatu ya kaa, semangat kuliahnya dan jaga kesehatan!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Jujur keren keren bangg proker PIKA, saya beneran terkena marketingnya",
                "pesan": "Semangat nanti TA nya bangg, semoga dipermudah jalan dan urusannyaa!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Ceria dan social butterfly bangetttt",
                "pesan": "Kaa walau perkuliahan semakin bertambah sem semakin terasa ngebantainya, tapi tetap semangatt ya kaa, jangan lupa jaga pola makan dan pola tidurnyaa jangan sampe drop-!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Gemassss dan ceria bangett",
                "pesan": "Go semangat goo!! kaa semoga kakak selalu diberikan kemudahan di setiap langkah kakak yaa"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "...",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "...",
                "kesan": "...",
                "pesan": "..."
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang kerennn",
                "pesan": "Semangatt terus ya bang kuliahnyaa, jangan lupa jaga kesehatan jugaaa!!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Cantik imut cutee beneran gemass",
                "pesan": "Semoga dunia selalu berbaik hati dengan kakak yaa, semangattt kuliahnyaa kaa!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Pinter bangett, beneran saya perlu banyak belajar dari abangg",
                "pesan": "Semangattt bang nanti TA nyaa, semoga dipermudah dan diperlancar semuanyaa, aamiin"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Fisrt impression ku ke kaka beneran kagum dan my role modell",
                "pesan": "Kaka beneran keren bangetttt, dari awal kenal saya kagum sama kakaa, tips n trick cara bagi waktu belajar dan organisasi kaa #helppp"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abang kerennnn",
                "pesan": "Semangatttt kuliahnya banggg, jangan lupa jaga kesehatan yaa!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Kerenn tapi sometimes abangnya jail jugaa",
                "pesan": "Semangatt bang kuliahnyaa!!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Kerennn dan pinter bangett",
                "pesan": "Masih keinget saya momen kelompok saya dibantai oleh pertanyaan dari abang, tapi JUJURRR minat banget berguru mengenai komputasi ke abangg karena ilmu abang DAGING BANGETTT"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "CUTEEE, beneran gemas bangettt",
                "pesan": "Semangatt kaa kuliahnyaaa!!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "Inspiratif person",
                "pesan": "Pengalaman abang beneran keren-keren bangett, semoga plan abang satu per satu bisa tercapai ya bangg, aamiin!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Orang serius yang tidak serius",
                "pesan": "Kocak bangett dah, semoga hal hal baik selalu melingkupi hidup abang yaaa, aamiin!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()


elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hsRjcZqsIur3pm4-bEA8ZpDDUUBMcbY5",
            "https://drive.google.com/uc?export=view&id=1a3o2Q7YjnOkLZFOChO3jVQlZps-h7Sfu",
            "https://drive.google.com/uc?export=view&id=1I1iaJuCDBKSDebl6uV2bYJC7PFPWsp8T",
            "https://drive.google.com/uc?export=view&id=1FwUGETSQtrJgiKcRA9LSNOfM6p1RGy6K",
            "https://drive.google.com/uc?export=view&id=1DVVJ5LpxwtVf6N3bnsgTbbqRCythNF1y",
            "https://drive.google.com/uc?export=view&id=1K3jIPU6dDVefn1jFU9SiOlRdDNqVlt8G",
            "https://drive.google.com/uc?export=view&id=1Q9aNH8QdvD2QX1OgKeneEDALZsonR6Ph",
            "https://drive.google.com/uc?export=view&id=15H9gL0G-0vJlxyAPop9chm1GSYlc4FX8",
            "https://drive.google.com/uc?export=view&id=1zcw2jslxpLdolTEt4ls57rh0DW5zxJYH",
            "https://drive.google.com/uc?export=view&id=1BkC3Tr4baD30JdEuIYJSq4rLjOiwt_Km",
            "https://drive.google.com/uc?export=view&id=1D7tZ-p8QlpKHhhfymcArDBetqBcAxMjP",
            "https://drive.google.com/uc?export=view&id=1e1pkIImHb9qH2qZItUA0CoGl2VW1PCPe",
            "https://drive.google.com/uc?export=view&id=1NQFo19cVNrV6vtsB9G_zgG1CWI2ez9v-",
            "https://drive.google.com/uc?export=view&id=1PDnxcYOvhzW0fylCjOJpGyAtIv_Bl7Fx",
            "https://drive.google.com/uc?export=view&id=1xM2-W6u1Zuci3fIk8rmHKQA0tfVr0xt1",
            "https://drive.google.com/uc?export=view&id=143aQZRx0DRXDGiMa3YqM1bLaxCm8MFBF",
        ]

        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Way Halim",
                "hobbi": "Ngeledek Orang",
                "sosmed": "@haikalsbln",
                "kesan": "Bang Haikal adalah sosok yang hangat, merangkul, dan peduli dalam menjaga keharmonisan serta hubungan di internal Himpunan",
                "pesan": "Semoga sukses selalu, baik dalam akademik maupun organisasinya."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Orangnya asik dan ramah",
                "pesan": "Semangat terus kuliahnya!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kakak ini sangat baik dan menyenangkan diajak diskusi",
                "pesan": "Semoga lancar dan sukses terus perkuliahan serta kegiatannya!"
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "Orangnya sangat seru dan gampang berbaur",
                "pesan": "Sukses terus untuk kuliah dan impian-impiannya!"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Sangat ramah dan selalu membawa suasana positif",
                "pesan": "Tetap semangat dan sukses selalu kuliahnya!"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Orangnya asik dan suka bikin suasana jadi ceria",
                "pesan": "Semangat terus perkuliahannya dan makin sukses!"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Orangnya santai dan enak diajak berteman",
                "pesan": "Sukses terus untuk akademik dan aktivitas lainnya!"
            },
            {
                "nama": "Muhammad Arvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Sangat seru dan selalu meramaikan suasana",
                "pesan": "Semangat terus kuliahnya dan sukses selalu!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kakak yang rajin dan sangat menginspirasi",
                "pesan": "Semangat terus nyari cuan dan kuliahnya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()


if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wFHj7FPrWFV_uSDKh92bZ3ARIO6IJsoM",
            "https://drive.google.com/uc?export=view&id=1bosgI-pEUcMxvpB2a6tJ411cdmk1tyiv",
            "https://drive.google.com/uc?export=view&id=1VhqkKO_VxO4iq5dKwCiY9qTc72G6uolf",
            "https://drive.google.com/uc?export=view&id=1IpViB77sfB_WTv53FURha6Uh5e0Ncuy2",
            "https://drive.google.com/uc?export=view&id=1czIs5dT8LhGdqhlD_Bc5UEAFgoDS5b5X",
            "https://drive.google.com/uc?export=view&id=1EkHgWjUhwD5tlbIK2lFzvpcssmS1v5o2",
            "https://drive.google.com/uc?export=view&id=1rh1SWa8JizZP_RgHEenEzuCsmudCxpA-",
            "https://drive.google.com/uc?export=view&id=1jzEZ32B9-2FtNAzJMXpTvmu8mzwJK5d-",
            "https://drive.google.com/uc?export=view&id=1Ksjp63YFrf8aOiFkG7jlGKr-O2gZ6bLs",
            "https://drive.google.com/uc?export=view&id=1Ucbg_4zUz8NCNm1qZ6MlPBjCCL3K4ODf",
            "https://drive.google.com/uc?export=view&id=19I1hpPyYplb4hpaYqGJ0JPmd-0xER0ug",
            "https://drive.google.com/uc?export=view&id=14hh_DaP8qn5U4UpFmBDIlf-79XZbuA8T",
            "https://drive.google.com/uc?export=view&id=1GDkM65zdKUkQtmO3Scws3oVR4MKuSoe5",
            "https://drive.google.com/uc?export=view&id=1xlqk7AYzc4hrynb2OOCSpYLGA9lM0IQ2",
            "https://drive.google.com/uc?export=view&id=1VU92JdMOmRmjXNNwmZB54UIxIgSZmeoj",
            "https://drive.google.com/uc?export=view&id=1uEbBzElrvNkB4AEfajAb6IPIijmajpCv",
            "https://drive.google.com/uc?export=view&id=1LIAOGsgyMPXSfMDNffyt93fymsgdhLBv",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak Arienta baik, keren, peduli, dan humble bangetttt",  
                "pesan":"Semoga diberi kesuksesan dan kesehatan selalu ya kak!!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany baik, berwibawa, dan disiplin banget",  
                "pesan":"Semoga selalu diberi kemudahan ya kakak!!!"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel Berwibawa, Asik dan jago banget sulap, baik, tegas, dan keren banget",  
                "pesan":"Semogaa sukses dan berkah selalu ya bang!!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi keren, gentle, tegas, dan energik bangetttt",  
                "pesan":"Semoga selalu diberikan kesehatan dan kekuatan ya bang!!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake humoris, asik, humble dan baik bangetttt",  
                "pesan":"Semoga selalu sehatt, bahagia, dan lancar rezekinya ya bang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar Baik, keren dan imut, serta suka berbagi ilmu",  
                "pesan":"Semoga selalu diberikan kelancaran ya bang!!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah, tegas, keren, baik dan humble bangetttt",  
                "pesan":"Semoga selalu semangat dan bahagia ya kak!!!"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal baik, tegas, asik, jago futsal, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan terhindar dari segala penyakit ya bang!!!"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri baik, lucu, imut, dan humble bangetttt",  
                "pesan":"Semoga selalu diberikan keselamatan dan kebahagiaan ya kak!!!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "Kak Queenta baik, ber aura, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat, bahagia dan diberi keselamatan ya kak!!!"# 1
            },            
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman baik, asik, humble, dan jago bangetttt deffense futsalnya",  
                "pesan":"Semoga selalu semangat dan sukses ya bang!!!"# 1
            },            
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel baik, kalem, dan humble bangetttt",  
                "pesan":"Semoga bahagia dimanapun kakak berada ya kak!!!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan bahagia ya kak!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jere humble, asik, kece, dan baik bangetttt",  
                "pesan":"Semoga selalu kuat dan sehat ya bang!!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik, santai, dan humble bangetttt",  
                "pesan":"Semoga selalu dilancarkan urusannya ya kak!!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli kece, rambutnya keren terus, dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan doa nya diwujudkan ya bang!!!"# 1
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi baik, lucu, kalem dan humble bangetttt",  
                "pesan":"Semoga selalu sehat dan dilancarkan urusannya ya kak!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
