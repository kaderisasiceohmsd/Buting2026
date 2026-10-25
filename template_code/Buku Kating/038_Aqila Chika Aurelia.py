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

if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xScs4doDOIethYbxNoWkU73CSdSFkWBB",
            "https://drive.google.com/uc?export=view&id=10EkDtDlWgtyDqGRTliitMHehOxdtAgP8",
            "https://drive.google.com/uc?export=view&id=1u-RH8Z2VgH0lz9DV42JSGxccA6rPLK7i",
            "https://drive.google.com/uc?export=view&id=176-ojVw5_L75IuyN1JnuunTsYRQESerh",
            "https://drive.google.com/uc?export=view&id=1r5v5UOSP7Au0lafHHG000oQgL8NzrPmL",
            "https://drive.google.com/uc?export=view&id=1hv50uvcjIaz-icXOrL1NFRJXmzNYvb9k",
                        
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push imo",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Ginda keren banget, time manageementnya bagus keren",  
                "pesan":"semangat terus kuliahnya bang"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Riau",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil orangnya baik banget, humble, dan ramah",  
                "pesan":"semoga lancar kuliahnya bang!"# 2
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "eeffiidefi",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat terus kak semoga lancar kuliahnya"# 3
            },
            {
                "nama": "Qois olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Bang qois keren banget bisa jadi bagian dari sekjen dan ramah juga orangnya",  
                "pesan":"semoga kuliahnya lancar dan sukses selalu"# 4
            },
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "keliling balam",
                "sosmed": "@luthhifiarmdhni",
                "kesan": "Kak luthfia ramah dan baik banget",  
                "pesan":"semoga sehat selalu dan semangat terus"# 5
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "bertemu luluk",
                "sosmed": "@hafsafazilahh",
                "kesan": "kakaknya cantik banget dan baik juga",  
                "pesan":"semoga urusan perkuliahannya lancar ya kak!"# 6
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wTVxoZAa2x2mKBg4jKil6LgMiz7_EQPj",
            "https://drive.google.com/uc?export=view&id=1894RdrHf6BwKBaOK_snVZOg_TMnuyNIo",
            "https://drive.google.com/uc?export=view&id=1Y0M_7iDNln0fwZKw67wINLcMfyuwpl3K",
            "https://drive.google.com/uc?export=view&id=1wKXY17t0-Zwm_ey3sEyutu6Ku5DD3Y9I",
            "https://drive.google.com/uc?export=view&id=193TDvbH2b5YhiR5A8x2Cqlm3Ixmvp7kb",
            "https://drive.google.com/uc?export=view&id=1F8OLkIFCfTrclWdMJrpJcWl796wyjCcV",
            "https://drive.google.com/uc?export=view&id=1axefxDg3NqoxW_vn9i-GMUtLEzs-N073",
            "https://drive.google.com/uc?export=view&id=1o7zNPdnVjdo7Arg1_19mHOjrqWUWy96Y",
            "https://drive.google.com/uc?export=view&id=1R9u-TmwW9l9qHEc8MbhAcdfSGoIrmJVE",
            "https://drive.google.com/uc?export=view&id=1_MoH0s5-UhiylH867SNSR56PnFLo8axZ",
            "https://drive.google.com/uc?export=view&id=11-TwKo2hQ7T6insZbO-fmBVHAdpmch_E",
            "https://drive.google.com/uc?export=view&id=1JrE8Vj6p08HGSWUs8D-sEoBjchMTh-_r", 
            "https://drive.google.com/uc?export=view&id=1E91EEOSBsAhpkn61Heu_hJa52rig89UJ",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "abang ini asik kalo pas jadi asprak ramah",
                "pesan": "semangat terus kuliahnya bang"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "Kakak ini humble dan extrovert banget",
                "pesan": "semangat terus kuliahnya semoga lancar"  # 2
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "Keren banget suka koleksi kartu boboiboy dan humble banget",
                "pesan": "semoga koleksi kartu nya makin lengkap"  # 3
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "baik, cantik dan keliatan nya pendiem",
                "pesan": "semangat terus kuliahnya kakk"  # 4
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "23",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "abang ini keren banget sering liat di ig",
                "pesan": "semangat terus bang kuliahnya semoga lancar"  # 5
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "baik dan ramah juga",
                "pesan": "semoga sehat selalu dan sukses dalam kuliahnya"  # 6
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "sering liat pas materi rangkaian dan baik juga",
                "pesan": "semoga lancar selalu kuliahnya bang"  # 7
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "abang ini asik, baik dan ga ketebak orangnya",
                "pesan": "semangat terus kuliahnya bang!"  # 8
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "14450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "keliatan nya galak padahal aslinya baik banget dan seru juga",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 9
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "cantik, baik dan ramah banget orangnya",
                "pesan": "semoga sehat selalu dan lancar kuliahnya kak"  # 10
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "pesan": "semangat terus kuliahnya bang!"  # 11
            }, 
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "tidur",
                "sosmed": "@monica_tjg",
                "kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "pesan": "semangat terus kuliahnya kakakkk"  # 12
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "zkrui",
                "alamat": "Jatimulyo",
                "hobbi": "memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "baik, keliatannya pendiem tapi asik juga orangnya",
                "pesan": "semangat terus kuliahnya kak"  # 13
            },                                                              
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18pFYiodYEd07IVviRGEycd-sjtKcNZax",
            "https://drive.google.com/uc?export=view&id=1Ie_cEMbITvBG28KC_fRR9ThBdU_RffXk",
            "https://drive.google.com/uc?export=view&id=1_urTTbpuJ2DLbq9Ym0QkgPwsky69ppL6",
            "https://drive.google.com/uc?export=view&id=1DtJVvMDe6lhO6fSfjzO-uZ6l-RnLeLAD",
            "https://drive.google.com/uc?export=view&id=1Hg9KrexMpQn47sve2xjNq2ywFtRkIN5A",
            "https://drive.google.com/uc?export=view&id=1MZqDfR7xVN0YAym_hzi7M5kf5m89ZYVB",
            "https://drive.google.com/uc?export=view&id=1Wm2zk-qe_eB1e6Zve6oeTdTAh79pj37u",
            "https://drive.google.com/uc?export=view&id=1GJCr6kglIzwOPI9M0oDiges27azaa0VK",
            "https://drive.google.com/uc?export=view&id=1YfVGoB_Y0IKAl6_IXTUl1EBsnIh9uAnB",
            "https://drive.google.com/uc?export=view&id=1on0ASNNX75WvntdQcdgbXWnIVm_97Kl5",
                      
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "kakaknya soft spoken, humble, dan baik banget",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Danger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kak nadya keren, cantik, dan baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya baik",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "kk ini baik banget dan aku melihat ada bintang bintang bersinar di mata kk nya masyaAllah ternyata nama kita samaan masyaAllah happy banget nama aku samaan kaya bidadari. Okay serius ya ini kesan nya, agak kaget waktu pengumuman kelompok mentor aku namanya sama kaya aku wkwk lucu banget jadinya kalo dipanggil dua duanya nengok!! long story short selama kurang lebih 5bulan ini amaze banget sama mentorku yang bener bener perhatian ke mentee nya bahkan sampe aku sendiri berani ceritain masalah pribadi aku karena aku tau kak aqila would be good listener, hari itu aku nangis baca chat dari kamu huhu gemes banget dan aku sangat berterimakasih untuk itu kak it means a lot <3",  
                "pesan":"untuk semua kebaikan yang kamu lakukan semoga berbalik ke kamu ya kak, aku percaya kamu akan selalu dikelilingi hal baik karena kamu such a good person too, gada kata yang bisa aku ucapin selain banyak berterimakasih sama kamu kak, jangan lupa tetap ceria ya kak cause it suits you well!, loveyouuu sm kakkk"# 6
            },                      
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "abangnya humble dan seruuu!",  
                "pesan":"Semangat terus bang"# 7
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "abangnya baik hati",  
                "pesan":"Semangat terus bang kuliahnya"# 8
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang"# 9
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "seru, baik dan humble",  
                "pesan":"semoga lancar kuliahnya bang"# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m97ka3OYag0V_l8csSv2nlfy66ANWFA2",
            "https://drive.google.com/uc?export=view&id=1B3Sf_Ca_iIgPsGE3bBgmkJqw15tQDM-9",
            "https://drive.google.com/uc?export=view&id=1F1mtjj-N63X-porO2lmB3bExI-bCiHfd",
            "https://drive.google.com/uc?export=view&id=1192G1ajQX8Zx4jaOb-Oi3ZWNKSSdNoAI",
            "https://drive.google.com/uc?export=view&id=1iCzkFhAlMglLgkDS5Qmv1sjNZI1Mv1xZ",
            "https://drive.google.com/uc?export=view&id=1cZsxSxAOPBxShCwEfEQLRkSjHfgIleoa",
            "https://drive.google.com/uc?export=view&id=1kUeGLor0It8tAWFw-iVQWN_EgJuvczp6", 
            "https://drive.google.com/uc?export=view&id=1Zq9WbcvuwUrSQqCtUVw1PTlpzvqO9xov",
            "https://drive.google.com/uc?export=view&id=1jc3fcTFkqZggyPN7cMRSUT6x5byGNzey",
            "https://drive.google.com/uc?export=view&id=1X3RFx8-SY5WtssTjo8WBpEUNJrNL2fB0",
            "https://drive.google.com/uc?export=view&id=1tywX8Nlb1C3fIpeEvPKWEUEh0j3VE4UE", 
            "https://drive.google.com/uc?export=view&id=1BoqV-W6coa_fMUYdpp966c6i3uy8M3TE",
            "https://drive.google.com/uc?export=view&id=1z3icSgP3TOwtqFRSIiSL-sXime4ts_x7",
            "https://drive.google.com/uc?export=view&id=13T_p5xu2rIS2aPPz6Igez7hW--JtSiXk",
            "https://drive.google.com/uc?export=view&id=1T8P6ibJPfxVPR3AG2V1Vb4vgZXZE7a7n",
            "https://drive.google.com/uc?export=view&id=1PdFDa2ZHA35Ff5ZCPuEI73JD_PH0D1da",
            "https://drive.google.com/uc?export=view&id=1J_SBF39ebIOQlijqbvSLeUbi5GeDAL8M",
            "https://drive.google.com/uc?export=view&id=1woiOndW1sTlpM5bDKh0tAWEwpuFlmNek",
            "https://drive.google.com/uc?export=view&id=1hyhuZwlvwsvmHBriKcDXkd6RdQaB72M5",
            "https://drive.google.com/uc?export=view&id=16T8hr3WAYGk7BHtbQV4vo7PTXc1T8jTE",
            "https://drive.google.com/uc?export=view&id=1MmhVLsb58dyPw9Z_z24p6IaIRmtn7URl",
            "https://drive.google.com/uc?export=view&id=1yTqNPYh2ExpOoHQTsjELzvQzuL-ZwIWA",
                                
        ]
        

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "1234501014",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biyokcb",
                "kesan": "abangnya baik dan ramah",
                "pesan": "semangat terus kuliahnya bang"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "kakaknya mirip arafah lucu banget",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya ramah banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget sering becandaan",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik banget",
                "pesan": "Semangat terus bang!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya baikk banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "Abangnya baik banget",
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Msake Up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik banget!!",
                "pesan": "Semangat terus kak!"
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "123450048",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "abangnya baik dan ramah",
                "pesan" : "senang bisa sempat kenal abang walau sebentar, al fatihah buat bang fadil"
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa aja",
                "pesan" : "Tetap semangat bang"
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
                "nim" : "124450119",
                "asal" : "Jambi",
                "alamat" : "Sabah Balau",
                "hobbi": "Belajar",
                "umur" : "20",
                "sosmed" : "@krnylee",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum dan enak diajak ngobrol",
                "pesan" : "Tetap semangat dalam menjalani perkuliahan, Kak"
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
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, bang"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "asal" : "Lampung Utara",
                "alamat" : "asrama",
                "hobbi": "membaca",
                "umur" : "20",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, bang."
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
                "pesan" : "Semoga kenyataan selalu ramah padamu, bang."
            },






        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()
# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1AlZvJm1bwqLcTWfzEEWJEGkxGXA10n-4",
            "https://drive.google.com/uc?export=view&id=1ArHMZclOHS0-YkcimTEs-GWPBS7N3M7n",
            "https://drive.google.com/uc?export=view&id=11mrEDtIIIKmVDAueJUWa0xgwPWL9zSiN",
            "https://drive.google.com/uc?export=view&id=1f9SOKyty48p6xXw1UxCVNa8XlWf0KNXW",
            "https://drive.google.com/uc?export=view&id=1qz2keGOjPowE1DS1BCOoE5-gu4bbDocl",
            "https://drive.google.com/uc?export=view&id=17T6PxV_C7ayGNdDRs08FBv6MbB_t_x-s",
            "https://drive.google.com/uc?export=view&id=1tmIe8vLPGmfmMu2Y0qjX4agkpv_oiHjy",
            "https://drive.google.com/uc?export=view&id=13bREMXQu_Dqtxj6QJWrIeqZhwNQrZzsy",
            "https://drive.google.com/uc?export=view&id=1cPJaUANbkFVTX0PbtYpTzhW50xrl-Gjj",
            "https://drive.google.com/uc?export=view&id=1IDI6eDK2HdB5L-2Sz-aZW6SDoL0_K4Or",
            "https://drive.google.com/uc?export=view&id=1srW8VJqN0Y4Pqcq1tucGqiw-BkT99t8a",
            "https://drive.google.com/uc?export=view&id=14ZCNfq5mcPoh0KKg3b9B90mjNgTsGiA4",
            "https://drive.google.com/uc?export=view&id=1-CvPg9gbLrATgukPI_zE6ZJSfg6I2SgD",
            "https://drive.google.com/uc?export=view&id=1MeLDb9sZX64gqoE2mvWoVOEmjSfaP5z_",
            "https://drive.google.com/uc?export=view&id=1hxXGjJTk_1Fxe0DEhgafwnxGdKokEdC_",
            "https://drive.google.com/uc?export=view&id=1QqaAWecIDxyqydkhdgziHrVYFQKvt7zn",
            "https://drive.google.com/uc?export=view&id=1pKWjssA_hNFWkxYgYGsF4sZ702lUePU_",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket pantai",
                "alamat": "Samping kos capo",
                "hobbi": "ngerjain tugas",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakaknya baik dan ramah banget",  
                "pesan":"semangat terus kuliahnya kakak!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya baik banget dan ramah!",  
                "pesan":"semoga kuliahnya berjalan lancar"# 2
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "abangnya baik, ramah dan keren bisa sulap",  
                "pesan":"Semangat terus bang kuliahnya"# 3
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "bang azmi baik dan ramah orangnya",  
                "pesan":"Semangat terus bang"# 4
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "baik, ramah, ga sombong",  
                "pesan":"Semoga sehat selalu dan kuliahnya lancar"# 5
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "abangnya asik dan humoris ",  
                "pesan":"Semangat ya bang kuliahnya"# 6
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya baik banget!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "abangnya baik banget",  
                "pesan":"Semangat terus bang"# 8
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@putrimannaa",
                "kesan": "Kakaknya baik dan ceria lucu banget",  
                "pesan":"Semangat terus ya kak kuliahnya"# 9
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya baik banget waktu pplk sabar banget nganterin aku ke toilet",  
                "pesan":"Semangat terus ya kak kuliahnya, semoga lancar dan lulus tepat waktu!"# 10
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "1234500114",
                "umur": "21",
                "asal":"Nias",
                "alamat": "GH Raya",
                "hobbi": "lompat batu",
                "sosmed": "@desmanhal_",
                "kesan": "abangnya baik banget dan ramah juga",  
                "pesan":"Semangat terus bang"# 11
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya humble, dan juga baik",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 12
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "orangnya baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 13
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya asik banget",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila kuliahnya lancar"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }




    
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iqP_B0ygO6Tws0JHWCxU5tkQkAG69pX0",
            "https://drive.google.com/uc?export=view&id=1E88k_AvviQUKl9v85T9m1WKsOc8yaa9-",
            "https://drive.google.com/uc?export=view&id=1PZof0zTKAHTKNZlfb4AZauxjcj9VKU09",
            "https://drive.google.com/uc?export=view&id=1AEhRBDW8jlyXNJ9Utjy4UxYmrxRanEQV",
            "https://drive.google.com/uc?export=view&id=1ORLcmCMqCKU3HFE7w54KpewMInl9pbjW",
            "https://drive.google.com/uc?export=view&id=1zj6sp8Rkx9INGE_09RCBw1kVNNnrVKhS",
            "https://drive.google.com/uc?export=view&id=1u4GTLT2RHPTwI700m0YIwAD7NokROl3Z",
            "https://drive.google.com/uc?export=view&id=10cfYy87R3zaohpmYEsaTOEOVJaZQpiRD",
            "https://drive.google.com/uc?export=view&id=1liV-H09UE8Vxp0nJahrzKe7rYDMAcm8y",
            "https://drive.google.com/uc?export=view&id=1qoAk_njXOg-E03kuAgYv-DUtu7SyIJv0",
            "https://drive.google.com/uc?export=view&id=1E1z8pi-75U0ExFK-U1OJlxzIQCgEnOVM",
            "https://drive.google.com/uc?export=view&id=1MXJzBa3SCh2LiI-R9IiIVszwf13NCR05",
            "https://drive.google.com/uc?export=view&id=15O83YgCZhwTEsDbn8Jt0jz89Zv3N7mf6",
            "https://drive.google.com/uc?export=view&id=1wh8OJbegbMx3OMoknM_coTCRmUdcpE-v",
            "https://drive.google.com/uc?export=view&id=1hcFgiFm2iHky703-WskIeyYtP8E2_OCF",
            "https://drive.google.com/uc?export=view&id=14C06GZ7dGq33K-yM1Oqg_zyDAT7Jsq41",
            "https://drive.google.com/uc?export=view&id=1OjBSEtxFLNnZ0L4VHTeNLmQCe7xqzedH",
            "https://drive.google.com/uc?export=view&id=1z7FLrR4D2s8-EWpCvIMUgFRQSZMgzqKG",
            "https://drive.google.com/uc?export=view&id=1XBPMIahlQKgcfODsg9OVmuLuKEKtmWSh",
            "https://drive.google.com/uc?export=view&id=1PZgl-0_qIanD8j2-F3CdonnF0-Mpvfr_",
            "https://drive.google.com/uc?export=view&id=1a7aKJNW6nlaDwpVikvirNv8M3j6TP30t",
            "https://drive.google.com/uc?export=view&id=1E3HPrOmqAVmP4h1nUtIPD6adCZQk2Mq2",            
        ]
        data_list = [
            
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "kakaknya baik banget ramah, santai, dan keibuan vibesnya",  
                "pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya lucu banget dan cantik",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Mancing Keributan",
                "sosmed": "@adityafq",
                "kesan": "abangnya baik banget dan ramah",  
                "pesan":"Semangat terus bang"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "Kakaknya imut banget, lucu, dan baik banget",  
                "pesan":"Semoga ceria selalu dan lancar urusannya kak"# 4
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "1244500106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "bang bima keren banget, ramah, dan baik selama magang bang bima mengayomi banget!",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu, aamiin."# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "abangnya baik dan ramah",  
                "pesan":"Semangat terus bang"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya ramah, lucu, dan ceria",  
                "pesan":"Semangat terus kak!"# 10
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal":"Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya baik banget, waktu ngobrol juga asik banget",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kakaknya imutt banget gemes dan ternyata punya kembaran!!",  
                "pesan":"Semangat terus kak kuliahnyaa"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "1234500552",
                "umur": "21",
                "asal":"Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "123450103",
                "umur": "19",
                "asal":"Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "abangnya baik banget",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "abangnya baik banget dan ramah juga!!",  
                "pesan":"Semangat terus bang kuliahnya semoga lancar selalu"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "abangnya baik banget, lucu banget!",  
                "pesan":"Semangat terus bang kuliahnyaa"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "123450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "Abangnya keren banget dan baik",  
                "pesan":"Semangat terus bang menyuarakan aspirasi!"
            },                                                                          
       
            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()
    
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jqY7cNmRU2JO6ofi79lav-PL5xXo3FDt",
            "https://drive.google.com/uc?export=view&id=1wHG6cy64eamI-iR6HaHn8c3g7mUomOdW",
            "https://drive.google.com/uc?export=view&id=1onJBBxK2YOhoiDs_3ZN1YDBnbIimIVuC",
            "https://drive.google.com/uc?export=view&id=1tiubx4Ypd2lRl_9R_LI-NJHo3EJt-GgW",
            "https://drive.google.com/uc?export=view&id=1VILr5PIZ0bJIMY81ZPUWuizEGGqVggUO",
            "https://drive.google.com/uc?export=view&id=1yE12OCokbYgYhkq1Z7ecWWzLkt1gUD5l",
            "https://drive.google.com/uc?export=view&id=131tg0lGQSX9TZWnJpv2Q5nF_fFFVg7o1",
            "https://drive.google.com/uc?export=view&id=1yOtn5zhTk_uydKYgr8Rz7ZhfT3Irp8ld",
            "https://drive.google.com/uc?export=view&id=14td_zgeZQPJoujFI4iuzgRjplPjVbtw_",
            "https://drive.google.com/uc?export=view&id=1LEdoXgrKtKBueSHlrmgpANWqN1SZ4_ni",
            "https://drive.google.com/uc?export=view&id=1MjJ2E3hkHWOUcJPuk6CIS9PEyQSyXGh_",
            "https://drive.google.com/uc?export=view&id=17cagNOMR9jP-mF-YznJ5G-z3MG1eKuZi",
            "https://drive.google.com/uc?export=view&id=1H1G4Q8HtaOi6aDf1BTT2ePr3thO2uhM6",
            "https://drive.google.com/uc?export=view&id=1txgJFvgT-ou5zxx-67lOpVmOa-jZ2Zxu",
            "https://drive.google.com/uc?export=view&id=11hgIJYM1dGTPaxpdXU3ObZyY86uP6eoe",
            "https://drive.google.com/uc?export=view&id=1ss9uTMV9FY7JBEIit1maNExvO1pPEffK",
    
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450006",
                "umur": "20",
                "asal":"Silikalang Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "abangnya ramah banget padahal keliatannya galak ternyata ngga",  
                "pesan":"semangat terus kuliahnya bang" #1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Untung Suropati",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@risma.mustika_",
                "kesan": "Kakaknya baik banget, salfok hobinya nolong orang masyaAllah",  
                "pesan":"tetap jadi orang baik ya kak!"# 2
            },
            {
                "nama": "Muhammad Hanif Zaky",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang Sumatera Barat",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngikutin drama tiktok",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang hanif ramah, baik, dan asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya bang" # 3
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya baik banget, kalem, cantik banget ternyata kakak nim akuu",  
                "pesan":"Semangat terus kak kuliahnya, semoga lancar selalu urusannya" # 4
            },
            {
                "nama": "Cika Adelia Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa Minang",
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya baik banget dan ternyata nama kita samaan!",  
                "pesan":"Semangat terus ya kak kuliahnya"# 5
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "-",
                "umur": "-",
                "asal":"-",
                "alamat": "-",
                "hobbi": "-",
                "sosmed": "@gustin.tpb",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@muhvnz",
                "kesan": "abangnya kalem tapi ramah dan seru juga",  
                "pesan":"Semangat terus bang kuliahnya!"# 7
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama Aqila",
                "sosmed": "snasaa._",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam Itera",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakaknya dari awal foto foto ramah dan welcome banget, funfact kakak ini kanim aku juga",  
                "pesan":"Semoga kak hanna kuliahnya diberi kelancaran dan lulus tepat waktu" # 9
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "abangnya baik banget!!",  
                "pesan":"Semangat terus bang"# 10
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan Belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakaknya baik banget dan ramah",  
                "pesan":"Semangat terus kak!"# 11
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "cerine.ipynb",
                "kesan": "Kakaknya baik banget, dan ngarahin pose foto yang lucu lucu",  
                "pesan":"Semangat terus kak!"# 12
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "abangnya baik, humble, seru juga!",  
                "pesan":"Semangat terus ya bang kuliahnya, sukses selalu!" # 13
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 14
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "korpri raya",
                "hobbi": "isengin havin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "abangnya seru diajak ngobrol, ramah dan baik juga",  
                "pesan":"Semangat terus bang kuliahnya"# 15
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik banget, funfact kk ini asprak alpro dan astut lmd RA!! seru banget kalo kak teresa ngajar!",  
                "pesan":"Semangat terus ya kak kuliahnya semoga kakak sehat selalu"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IImn-bwzrj7vV70MBmk_zh6cfpvGEqXv",
            "https://drive.google.com/uc?export=view&id=1B7DXOKpYlOmg_7N4AGQEDxdxffx3Maw2",
            "https://drive.google.com/uc?export=view&id=13Z5TFq5waedLDBwSLRkw3M7FzuKqxCCg",
            "https://drive.google.com/uc?export=view&id=18mXzlMsfCtWW7w_ZYHSAlJneXV7CnQZh",
            "https://drive.google.com/uc?export=view&id=133EBWrKSlcaiymXnXeJF3RpziWVOO9PH",
            "https://drive.google.com/uc?export=view&id=13ZR7K_g__ndBZCUkk7-7FOl0_2Tr1Wo7",
            "https://drive.google.com/uc?export=view&id=1fd-vmxtK8J29UC16G7bnQECuIW-yXC3t",
            "https://drive.google.com/uc?export=view&id=1Sh5npJ-ecdhCo5QZR5WMIOUC-suHK_4B",
            "https://drive.google.com/uc?export=view&id=1lsexSMeqP_3EZwoJ3zQmZFhfDpbuAdjr",
            "https://drive.google.com/uc?export=view&id=19sWSqL7TWP4kHwDVTcmyuNEZpmkNq_Rb",
            "https://drive.google.com/uc?export=view&id=18bm_0khZDjIvfhsje-VogTBVqVQNGdvQ",
            "https://drive.google.com/uc?export=view&id=1CMfrmUJIe9Ivf2uqs7sz2lut0KPCB_4U",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya asik banget, baik, dan ramah",  
                "pesan":"semangat terus kuliahnya bang!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak nya cantik banget dan kalem",  
                "pesan":"semangat terus kuliahnya kakak" # 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakaknya seru waktu wawancara, ramah, dan baik banget",  
                "pesan":"semangat terus kuliahnya ya kakk"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "abangnya baik, humble, asik",  
                "pesan":"semoga kuliahnya lancar bang!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik dan baik juga",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abangnya asik banget, baik juga, pas jadi asprak sabar banget ngajarin satu satu",  
                "pesan":"semangat terus kuliahnya bang semoga sukses selalu"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak nya baik dan asik juga",  
                "pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakak ini baik, lucu juga pas jawab jawab pertanyaan pas wwc",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "abangnya humoris banget dan asbun nya lucu banget bikin ketawa",  
                "pesan":"semangat terus kuliahnya ya bang"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "abang ini humble, seru, dan baik",  
                "pesan":"semoga sukses selalu bang" # 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini asik, baik, dan cantik",  
                "pesan":"semangat terus kuliahnya kakak"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "kakaknya seru, baik, humble juga",  
                "pesan":"semoga lancar selalu kuliahnya kak, semangat!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1m2rvZSz0qpUXtsy8x2g1AcDR1g_kvNDJ",
            "https://drive.google.com/uc?export=view&id=1W3cvvaj4zcC-o3U_gu4WLSS618R0mFem",
            "https://drive.google.com/uc?export=view&id=1WtJpHfMHmMjYlf5BZ7Z7NPwNpylCVncH",
            "https://drive.google.com/uc?export=view&id=1WtDi1SdPHSaqWj9Bpuz5cOGwFZA6M8kl",
            "https://drive.google.com/uc?export=view&id=1AtKU8BaPsYtO4EQnrr6Sr63ocG6Z9tBM",
            "https://drive.google.com/uc?export=view&id=1jGG1ralwM5Iy7PQTsmGApsWHfDH18W1t",
            "https://drive.google.com/uc?export=view&id=1fm2zZKGdoESow-clgtd5WYKF2H1Zfz0s",
            "https://drive.google.com/uc?export=view&id=1NSwY-NS2t2HG_LUowlUrrCgEBHIVVb4P",
            "https://drive.google.com/uc?export=view&id=15Tqp1GDipeMeb7459e5BmCNNpqJSkUnq",
            "https://drive.google.com/uc?export=view&id=1HOG3BPV4Wpjt8WN2VXL4mOK8fnTZKzb-",
            "https://drive.google.com/uc?export=view&id=15WrpeBWCfwO9UfzkKzjBh31j_f6TXMod",
            "https://drive.google.com/uc?export=view&id=1Z096O3z95Hm8sDUb9KLIrlz3SamJ7NNq",
            "https://drive.google.com/uc?export=view&id=1c4qUjCxCyk7_Eqx78eROUrXF9xgc2uL6",
            "https://drive.google.com/uc?export=view&id=1JY_eN7oI23lhBPjyRxS_6-wnLV8gR-tl",
            "https://drive.google.com/uc?export=view&id=1wpfj5kkLpvCy5tPfae-4VfK2s8f6ITqs",
            "https://drive.google.com/uc?export=view&id=1gAj2QGtqLpG9D9foys0bH3zaFkGdoJVD",
            "https://drive.google.com/uc?export=view&id=1-8mhvvUcdUldYjOpagaW5tAOBguSeXEj",
            "https://drive.google.com/uc?export=view&id=1eigi2t7Dhw1snYqjsKSSt8-Tx3GvPSGR",

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
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"semangat ya kak ngerjain TA-nya!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "kakakmya cantik, baik, humble",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "abangnya baik, kalo jelasin mudah dipahami",  
                "pesan":"Semangat terus bang kuliahnya"# 3
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
                "kesan": "Kakaknya lucu banget imutt",  
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
                "kesan": "orangnya lucu, ramah, cantik!",  
                "pesan":"Semoga selalu bahagia!"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya baik, ramah, dan asik banget!!",  
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
                "kesan": "abangnya baik, kece, keren",  
                "pesan":"Semangat terus bang"# 8
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
                "kesan": "Kakaknya humble, baik, asik",  
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
                "kesan": "Kakaknya cantik, baik, asik",  
                "pesan":"Semoga sukses selalu"
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
                "kesan": "Kakaknya seruu",  
                "pesan":"semoga lancar kuliahnya kakk"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "abangnya kalem, baik, ramah",  
                "pesan":"Semangat terus bang!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "abangnya asik, baik banget!!",  
                "pesan":"Semangat terus ya bang"
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
                "hobbi": "nyari hobi",
                "sosmed": "@aallishaa.a",
                "kesan": "Kakaknya ceria banget, imut, cantik!",  
                "pesan":"Semoga kuliahnya lancar kakk!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@_shaazzh",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()


if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1alkJfuN7M64Fdm-HLF6y3cDkpg3JcoW-",
            "https://drive.google.com/uc?export=view&id=1--PspYPrQmPbmHLYZT_jmPSPi1dFPjRh",
            "https://drive.google.com/uc?export=view&id=1JKb9CbEgbBxhyt6Zd5hGhVAEWHqmtfvQ",
            "https://drive.google.com/uc?export=view&id=1YpNKXtL7tK-xjltoInu8a-FkYVo4vlyE",
            "https://drive.google.com/uc?export=view&id=1yB8sWinY0iqNnquIWCXYoNmp83Cyzqvc",
            "https://drive.google.com/uc?export=view&id=1z1_M9MUpRAkdyFwojzJKlEs_qPFWh1UT",
            "https://drive.google.com/uc?export=view&id=12-z-OFrXUEbuYralALJMMfJjeR1tEdxY",
            "https://drive.google.com/uc?export=view&id=1-zKt5NkXfMMltNoCs-zS2TCleK90VkOz",
            "https://drive.google.com/uc?export=view&id=1142EWm8AK4_AIbhEJZJkq-U1zz79ncJ2",
            "https://drive.google.com/uc?export=view&id=1AfDzz4jsj95HdffDtiSEtXW3brKx_vw0",
            "https://drive.google.com/uc?export=view&id=1zXBEtnuYdAYZCP7sYlcVM5Nq2zfco9L6",
            "https://drive.google.com/uc?export=view&id=12OkUsn8gwgA5b3nC2rXvx60Umf9TU5cX",
            "https://drive.google.com/uc?export=view&id=1SZOdwsAZJpvXnwAjRXtVTzWwQ80tESHA",
            "https://drive.google.com/uc?export=view&id=1pSxJIsavX6gXF1lt2DRG6Sd2bPzWE9Cr",
            "https://drive.google.com/uc?export=view&id=1MKa_yRaJi5t9R6kUnJ0UYDxrNvr2mmrS",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya baik, waktu wwc penjelasan nya mudah dipahami",  
                "pesan":"semangat terus ya bang kuliahnya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D.",
                "nim": "123450046",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kakaknya keren banget outfitnya",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya baik, ramah, asik",  
                "pesan":"Semoga lancar kuliahnya bang"# 3
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
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
                "nama": "Dafa Elpriza",
                "nim": "124450121",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Motoran bareng bang bryan",
                "sosmed": "@dafaelpriza_",
                "kesan": "abangnya seru, baik, asik",  
                "pesan":"Semangat terus kuliahnya bang, sukses selalu!"# 5
            },
            {
                "nama": "Juwita Sari",
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
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jalan Pulau Damar",
                "hobbi": "Menjawab soal dari dosen dipapan tulis",
                "sosmed": "@afdal.03",
                "kesan": "abangnya baik dan asik!",  
                "pesan":"Semangat terus bang!"# 7
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "1244500024",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@slbnzw",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 8
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@mridwaan_22",
                "kesan": "abangnya keren, ramah, asik",  
                "pesan":"Semangat terus bang kuliahnya!"# 9
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@andra.lhm",
                "kesan": "bang andra seru banget selalu ada topik dan cairin suasana",  
                "pesan":"Semangat terus ya bang kuliahnya"# 10
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@bryantel_",
                "kesan": "abangnya baik, asik, seru juga",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "1244500067",
                "umur": "17",
                "asal":"Semarang",
                "alamat": "Kemiling",
                "hobbi": "Ternak sapi",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "abangnya seru, obrolannya asik",  
                "pesan":"Semangat terus bang dan sukses selalu"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
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
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@cacalvra",
                "kesan": "Kakaknya imut, gemes, cantik",  
                "pesan":"Semoga kuliahnya lancar kak"
            },
            {
                "nama": "Muhammad Rafka fatih Al Ghathfaan",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Tukang Parkir",
                "sosmed": "@muhammdrafka_",
                "kesan": "abangnya keliatan cuek dan galak padahal aslinya baik, ramah juga",  
                "pesan":"semoga kuliahnya lancar bang, sukses selalu!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Minbak()
