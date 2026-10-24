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

menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
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
                "asal": "Batam",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Push Rank sampe IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Abangnya baek banget sumpah",  
                "pesan": "Semangat bang semoga bisa lulus dengan memuaskan"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya asik, suka ngelawak juga wkwk",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya seruuu heheh",  
                "pesan": "Semangat terus ya kaaa"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keliatan pendiem wkwk, tapi seru koo",  
                "pesan": "Semangat bang, ajarin jadi sekre sih bang wkkw"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya asik bener hehe",  
                "pesan": "Semangat ya kaaaaa"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakanya keliatan pendiem heheh",  
                "pesan": "Semangat terus kaaaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

elif menu == "Badan Kesenatoran":
    def Bason():
        st.markdown("<h3 style='text-align: center;'>Badan Kesenatoran</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Senator", "Biro Aspirasi dan Media Komunikasi", "Biro Kajian Strategis dan Propaganda", "Biro Kesekretariatan"])

        with tab1:
            gambar_urls_senator= [
               "https://drive.google.com/uc?export=view&id=11SPNjtTzTXODqCtXKM2n7_a6LSDJ_xxu",
            ]
            data_list_senator = [
               {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Airan",
                "hobbi": "Nulis Medium",
                "sosmed": "@fathinahnaazh",
                "kesan": "Kakanya keren banget jujurrr",  
                "pesan": "Semangat terus kuliahnya kaaaa"
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)
        with tab2:
            gambar_urls_biro_aspirasi= [
                "https://drive.google.com/uc?export=view&id=1dF4TAZE8WWOzKA77BMBo4Axtg2Tbtgmf",
                "https://drive.google.com/uc?export=view&id=1HH38KaJOHcAoQFsr3wg9CyrcRg7rULWK",
                "https://drive.google.com/uc?export=view&id=1EsxQ3vnQl3xssWpvIEDrsIP-tKRKg6Sq",
                "https://drive.google.com/uc?export=view&id=16zCWIbcZx4dxvcZM7sCqr9QO5gW9QTjf",
                "https://drive.google.com/uc?export=view&id=1HtjZB4BXt-Nkz5NIFTcHXN2Yf8Bscxa_",
            ]
            data_list_biro_aspirasi = [
               {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_ist",
                "kesan": "abangnya kalo diajak foto maunya melet wkwk",  
                "pesan": "Semangat terus ya baaang"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Asik bener abangnya wkwk",  
                "pesan": "Semangat terus baaaang"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya asik sih jujur",  
                "pesan": "Semangat terus ya kaa kuliahnyaaa"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya chill sih ini wkwk",  
                "pesan": "Pokonya semangat terus baaang"
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)
        with tab3:
            gambar_urls_biro_kajian= [
                "https://drive.google.com/uc?export=view&id=19MOjim3ecksjmg5D6q3L1RItrE9FMIqU",
                "https://drive.google.com/uc?export=view&id=1sj72ppDfSP2Gsb2OmRi9iCUgSUTADvq9",
                "https://drive.google.com/uc?export=view&id=1kAzNX33-iBiopIJS8lpofQVAgrc0qlWp",

            ]
            data_list_biro_kajian = [
                {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Nyari jurnal",
                "sosmed": "@lia.h_264",
                "kesan": "Pengen belajar sama kakanyaaa wkwk",  
                "pesan": "Semangat terus kaaaaa"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakanya jujur asik banget, apa aja diketawain wkwkw",  
                "pesan": "Semangat terus kaaaaa"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya keren sih jujur",  
                "pesan": "Semangat terus bang kuliahnya"
                },
                ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)
        with tab4:
    
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1raMhfhs03xggsGjGd2OIUocdKNrf4CRi",
            "https://drive.google.com/uc?export=view&id=1BTtrxCIJz_-KeuAK8nyw0svL9tuELoRu",
            ]   
            data_list_kesekretariatan= [   
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger Lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kakanya baek bangeeet heheh",  
                "pesan": "Semangat terus kaaa"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya lucuuu hehe",  
                "pesan": "Semangat terus ya kaaaa"
            }
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_kesekretariatan)
    Bason()

elif menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg= [
            "https://drive.google.com/uc?export=view&id=1Tk-bJkKgzNMA-fm6OzLHKI6JBhpXYzi0",
            ]
            data_list_kabaleg = [
            {
            "nama": "Ridho Benedictus Togi Manik",
            "nim": "123450060",
            "umur": "20",
            "asal": "Kota Manchester",
            "alamat": "GH",
            "hobbi": "Wawancara",
            "sosmed": "@iamridhomanik",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1gFdiwtYuvhlucS-aG2ZqAqWG3XSPdR8f",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1lSnt4kHwVsefEtE5BpOqLOwA0gTVpI30",
            "https://drive.google.com/uc?export=view&id=1t30318dKeFArSSOGzg9zL3w8H02ECwfx",
            "https://drive.google.com/uc?export=view&id=1wtV5XGs-jc_B9FFd1BHPHV8OXZZeiRtw",
            ]
            data_list_komisi1 = [
            {
            "nama": "Dharu Cahyoaji Sasongko",
            "nim": "123450023",
            "umur": "19",
            "asal": "Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Ngidupin api baleg di tiktok",
            "sosmed": "@exvoltas",
            "kesan": "...",  
            "pesan": "..."
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
            "pesan": "..."
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
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=17AVkVCwdmhkiWhWgZGXTsOV8cRUpU4Ga",
                "https://drive.google.com/uc?export=view&id=1PdH3t9f6056847Z70yJ-Y0h53HHnpPQk",
                "https://drive.google.com/uc?export=view&id=1iRW7v7Su6lpURaFClHrFtx90nlfk8IFW",
                "https://drive.google.com/uc?export=view&id=1kPhDXJYVHB4WD19PTKSc9VhG6922TZiv",
            ]
            data_list_komisi2 = [
            {
            "nama": "Givaro Ananta",
            "nim": "123450078",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Sukabumi",
            "hobbi": "Minum Kopi",
            "sosmed": "@givarooo",
            "kesan": "...",  
            "pesan": "..."
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
            "pesan": "..."
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
            "pesan": "..."
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
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=18EGYQyL1pKeLgmmeL0_VvhE-AWDSGAb9",
                "https://drive.google.com/uc?export=view&id=1T3sv7gqjt0u6EHFaUn0T84r2iDbehJW9",
                "https://drive.google.com/uc?export=view&id=1fJNUW-uDrq-Mev2l-eLs3eYrJRG59bN3",
                "https://drive.google.com/uc?export=view&id=1ZkEfG9l4uOBmw_D-TY6Ueopt915vVu1F",
            ]
            data_list_komisi3 = [
            {
            "nama": "Monica Patricia Tanjung",
            "nim": "123450073",
            "umur": "21",
            "asal": "Jakarta Barat",
            "alamat": "Kotabaru",
            "hobbi": "Lari",
            "sosmed": "@monica_tjg",
            "kesan": "...",  
            "pesan": "..."
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
            "pesan": "..."
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
            "pesan": "..."
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
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_komisi3, data_list_komisi3)

    Baleg()
    
elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12QOfSNfjMqEfLwP3pk5Gg9AjoIcuKE_O",
            "https://drive.google.com/uc?export=view&id=1v4Gx1LnKyMPQ7YXSDYj6cXXJdsvx2h7N",
            "https://drive.google.com/uc?export=view&id=1ukRXDoD9AcY83O8RzjKReZFYzxW2oKmB",
            "https://drive.google.com/uc?export=view&id=1A6UjUE-8JDvoQAzRJsIN04UlNQXxfCj1",
            "https://drive.google.com/uc?export=view&id=19aZL3HXHjIgPNRt4t2afY7BsqNS4QAxC",
            "https://drive.google.com/uc?export=view&id=1UUWG7wy3dw2XCUepwe0v9lcz5JPslfti",
            "https://drive.google.com/uc?export=view&id=1FesizaWmDQGZSFVcVmh_nmtQVNrN_fk5",
            "https://drive.google.com/uc?export=view&id=1LrR9YBcxKwIXTui_CLDIzDT52OGaIjrY",
            "https://drive.google.com/uc?export=view&id=1beTFZVK1JkqqFEluOj8wQTdGEG5newe-",
            "https://drive.google.com/uc?export=view&id=1BzoAEefRUd_6pRibFmr9mfq3ztI2ictU",
            "https://drive.google.com/uc?export=view&id=1XWhKwI0vmASijbtxREkuRt2NjeT8dlVf",
            "https://drive.google.com/uc?export=view&id=1wTj3IEpr0vt_advP1kdQoxlidINfMihJ",
            "https://drive.google.com/uc?export=view&id=1hWFq1yNhPul0IvmasCEmzbUoWUHMgNBR",
            "https://drive.google.com/uc?export=view&id=1LCHVLYPVRj7kRdJzZ7hw8yeb90vk0sk9",
            "https://drive.google.com/uc?export=view&id=1GXwVs1gKStV9ei_5d3Jv7lYxzBejOYhn",
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
        "nama": "Muhammad Rafka",
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

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3= st.tabs(["Inti","Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Inti = [
            "https://drive.google.com/uc?export=view&id=1JJACXP6B30Q7tvxMs8xltgxrue3Md7NJ",
            "https://drive.google.com/uc?export=view&id=1VfrqEqHNT3KFHdcgh9EFPMZexuOdmPhF",
            ]
            data_list_Inti = [
            {
            "nama": "",
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
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Inti, data_list_Inti)

        with tab2:
            gambar_urls_Divisi_Kaderisasi = [
                "https://drive.google.com/uc?export=view&id=1BNCJseiunQJpr7z2TWavHsz-wDeokcMy",
                "https://drive.google.com/uc?export=view&id=1Yd-HFkMvq4CSDQ6W3TgPGpwLv1X9cTyp",
                "https://drive.google.com/uc?export=view&id=1FKzZtv-iDhjZB_ZCI_bV5kmK1IqjbLUL",
                "https://drive.google.com/uc?export=view&id=1hwMvpoPLc4SgNgdcSQOvwFhIM6yzQs9e",
                "https://drive.google.com/uc?export=view&id=13ZKxCk_pOUaiNoq_XNuBCBiXuzs0w4iX",
                "https://drive.google.com/uc?export=view&id=1CzK_qdmB15tqlk-HgJRzv1Xywt7AXMw5",
            ]
            data_list_Divisi_Kaderisasi = [
            {
            "nama": "",
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
            "nama": "",
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
            "nama": "",
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
            "nama": "",
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
            "nama": "",
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
            "nama": "",
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
            "nama": "",
            "nim": "",
            "umur": "",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab3:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1tezAhG2bdA6gOP7Ir1LESWKmGbBPcRam",
            "https://drive.google.com/uc?export=view&id=1yi0snKFlXFzL4Dl_Qdui3zsAEC2XJlRZ",
            "https://drive.google.com/uc?export=view&id=1lP8FqydrgsV05nKcBMaPux-o0264C7-b",
            "https://drive.google.com/uc?export=view&id=1vSYX0aitpovtJhjNrK3pKbzmxaOI1dKI",
            "https://drive.google.com/uc?export=view&id=1Vz4wKISAoes9cNV7M2VCtGoE8BKY1Y_6",
            "https://drive.google.com/uc?export=view&id=18h9zPrV_t4doWuOJ6GliFr-0KILXfYu6",
            "https://drive.google.com/uc?export=view&id=1Pfodd3LlwhHsMorMSa7dQqeReam9AExr"
            ]
            data_list_Divisi_Peningkatan_Mutu_Anggota = [
            {
                "nama": "",
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
                "nama": "",
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
                "nama": "",
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
                "nama": "",
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
                "nama": "",
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
                "nama": "",
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
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Peningkatan_Mutu_Anggota, data_list_Divisi_Peningkatan_Mutu_Anggota)
    PSDA()

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

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14jFxHpSiQQ-ZdlNPkNn_8JVfcQnGWSvQ",
            "https://drive.google.com/uc?export=view&id=1eZXM43pKL5dkqFJKVlWPls7ngHzGN22q",
            "https://drive.google.com/uc?export=view&id=1n0LUuor4_bwmz1QQc8d3k9OLVseEyq_w",
            "https://drive.google.com/uc?export=view&id=1O5a59ai8q_NG4no9v5G5_HnAoHfdwMPr",
            "https://drive.google.com/uc?export=view&id=1HQPg7YwlSRWNirdyumo3VX9HjnLuximV",
            "https://drive.google.com/uc?export=view&id=1AQpRKL0whGttOVWlKqKOeEsT0S6hOpiJ",
            "https://drive.google.com/uc?export=view&id=1L3TyKqZF8i_mh629DreTdRKhuhcesVKc",
            "https://drive.google.com/uc?export=view&id=1zn2md_RpQ_OCbZrHqL9TX_VR4jpMDDoE",
            "https://drive.google.com/uc?export=view&id=1A6ZSNaUPfZHIi951OzfoSXl-NnSreAXf",
            "https://drive.google.com/uc?export=view&id=1qGm0nwmxknY3RFjpqsYVvgWTUkHD-imo",
            "https://drive.google.com/uc?export=view&id=13uaveV1UZw6w_VG8eSlHYxgCU7tl72Ix",
            "https://drive.google.com/uc?export=view&id=1fMgJJIrNWierk4biwSqw7D9qzs77jrD8",
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

elif menu == "Departemen Medkraf":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
