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
        st.markdown("<h3 style='text-align: center;'>Departemen Minat dan bakat</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4= st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])
        
        with tab1:
            gambar_urls_kepala_departemen_minbak= [
            "https://drive.google.com/uc?export=view&id=12QOfSNfjMqEfLwP3pk5Gg9AjoIcuKE_O",
            ]
            data_list_kepala_departemen_minbak= [
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
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1v4Gx1LnKyMPQ7YXSDYj6cXXJdsvx2h7N",]
            data_list_sekretaris_departemen_minbak = [ 
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
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
            "https://drive.google.com/uc?export=view&id=1ukRXDoD9AcY83O8RzjKReZFYzxW2oKmB",
            "https://drive.google.com/uc?export=view&id=1A6UjUE-8JDvoQAzRJsIN04UlNQXxfCj1",
            "https://drive.google.com/uc?export=view&id=19aZL3HXHjIgPNRt4t2afY7BsqNS4QAxC",
            "https://drive.google.com/uc?export=view&id=1UUWG7wy3dw2XCUepwe0v9lcz5JPslfti",
            "https://drive.google.com/uc?export=view&id=1FesizaWmDQGZSFVcVmh_nmtQVNrN_fk5",
            "https://drive.google.com/uc?export=view&id=1LrR9YBcxKwIXTui_CLDIzDT52OGaIjrY",
            
            ]
            data_list_manajemen_aktivitas_dan_kompetisi = [
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
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
                "https://drive.google.com/uc?export=view&id=1beTFZVK1JkqqFEluOj8wQTdGEG5newe-",
                "https://drive.google.com/uc?export=view&id=1BzoAEefRUd_6pRibFmr9mfq3ztI2ictU",
                "https://drive.google.com/uc?export=view&id=1XWhKwI0vmASijbtxREkuRt2NjeT8dlVf",
                "https://drive.google.com/uc?export=view&id=1wTj3IEpr0vt_advP1kdQoxlidINfMihJ",
                "https://drive.google.com/uc?export=view&id=1hWFq1yNhPul0IvmasCEmzbUoWUHMgNBR",
                "https://drive.google.com/uc?export=view&id=1LCHVLYPVRj7kRdJzZ7hw8yeb90vk0sk9",
                "https://drive.google.com/uc?export=view&id=1GXwVs1gKStV9ei_5d3Jv7lYxzBejOYhn",
            ]
            data_list_manajemen_minat_dan_bakat = [
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
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)  

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
            "nama": "Arienta Khusnul Ananda",
            "nim": "123450097",
            "umur": "21",
            "asal": "Deket Pantai Kedu, Kalianda",
            "alamat": "Samping kos capo",
            "hobbi": "Baca jurnal",
            "sosmed": "@arientakhsnl_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Vany Salsabila Putri",
            "nim": "123450022",
            "umur": "20",
            "asal": "Sibolga",
            "alamat": "Pudan Kost",
            "hobbi": "Pacaran",
            "sosmed": "@vany.salsabilaa",
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
                "https://drive.google.com/uc?export=view&id=1CzK_qdmB15tqlk-HgJRzv1Xywt7AXMw5",
                "https://drive.google.com/uc?export=view&id=1CzK_qdmB15tqlk-HgJRzv1Xywt7AXMw5",
            ]
            data_list_Divisi_Kaderisasi = [
            {
            "nama": "Nobel Nizam Fathirizki",
            "nim": "123450117",
            "umur": "123450117",
            "asal": "Bandar Lampung",
            "alamat": "Urip",
            "hobbi": "",
            "sosmed": "@nobelnizam",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Afriza Azmi",
            "nim": "124450110",
            "umur": "20",
            "asal": "Malang",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@friezazmi",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Haikal Seventino Tamba",
            "nim": "124450012",
            "umur": "18",
            "asal": "Solok, Sumatera Barat",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@_haikaaall",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Euodia Meiliana Friedita",
            "nim": "124450029",
            "umur": "18",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@yudiameilianaa_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Ayake Alfatih Ramadan",
            "nim": "124450108",
            "umur": "21",
            "asal": "Solok, Sumatera Barat",
            "alamat": "",
            "hobbi": "Masak ayam",
            "sosmed": "@ykeall",
            "kesan": "",  
            "pesan": ""
            },
             {
           "nama": "Caesar Ozora Alrando",
            "nim": "124450017",
            "umur": "21",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@caesar.oriza",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Putri Manna Anantama Simbolon",
            "nim": "124450056",
            "umur": "18",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@@putrimannaa",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Queenta Thifaal Nabila",
            "nim": "124450059",
            "umur": "18",
            "asal": "Kota Gajah",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@queentanabila",
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
                "nama": "@queentanabila",
                "nim": "123450114",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "desmannhal_",
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

elif menu == "Departemen MIKFES":
    def mikfes():
        st.markdown("<h3 style='text-align: center;'>Departemen Akademik dan Keprofeisan</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Professional Skill and Development", "Divisi Pusat Inovasi dan Kajian Akademik", "Divisi Research & Development"])

        with tab1:
            gambar_urls_kepala_departemen_mikfes= [
            "https://drive.google.com/uc?export=view&id=1rCtgSNBpeJlgEIz3JsWTZ3EZbpWb9XfF",
            ]
            data_list_kepala_departemen_mikfes = [
            {
            "nama": "Fabio Banyu Cyto",
            "nim": "123450104",
            "umur": "21",
            "asal": "Bandar Lampung",
            "alamat": "Kedaton",
            "hobbi": "Tidur",
            "sosmed": "@biyokcb",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1K9487O-Qgrl_z9ggJHdLeBNAeKAJ-UyQ",]
            data_list_sekretaris_mikfes = [ 
            {
            "nama": "Tanty Widiyastuti",
            "nim": "123450094",
            "umur": "21",
            "asal": "Lampung",
            "alamat": "Airan Raya",
            "hobbi": "Membaca",
            "sosmed": "@tvnty_",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1J1Ow3mPnTv1NZuoc5vtWmcrPZNIVovs5",
            "https://drive.google.com/uc?export=view&id=1K9487O-Qgrl_z9ggJHdLeBNAeKAJ-UyQ",
            "https://drive.google.com/uc?export=view&id=18AtZtf7ahz0ge0UVieOGv_k2TK3BFTUE",
            "https://drive.google.com/uc?export=view&id=1G4Qok6YiafAWpW1A0GTjfUMC9kqwkNHd",
            "https://drive.google.com/uc?export=view&id=1KaoL1ruuGH9jT_6SGEWEGpo7cfaLXLJS",
            "https://drive.google.com/uc?export=view&id=1DG8shlDjNnxji-kryZNSNwvJAL-b_hAP",
            ]
            data_list_Divisi_Professional_Skill_and_Development = [
            {
            "nama": "Fadil Prasetyo Alfarizzi",
            "nim": "123450048",
            "umur": "21",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Gitar",
            "sosmed": "@fadilalfarizzii",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Manuel Frederika",
            "nim": "124450039",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Batam",
            "hobbi": "Tenis meja",
            "sosmed": "@manuelfdk_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Ni Made Okta Viola Darma Putri",
            "nim": "124450005",
            "umur": "12",
            "asal": "Bali",
            "alamat": "Nusa Penida",
            "hobbi": "Menghayal",
            "sosmed": "@Violaadrtr_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Risa Romadona",
            "nim": "124450127",
            "umur": "20",
            "asal": "Natar",
            "alamat": "Natar",
            "hobbi": "Natar",
            "sosmed": "@risarmdna",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Vannisa Ramadhani",
            "nim": "124450078",
            "umur": "19",
            "asal": "Bali",
            "alamat": "Teluk Betung",
            "hobbi": "Nonton KHW",
            "sosmed": "@vunnycaa",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Yulia Kristine Malau",
            "nim": "124450119",
            "umur": "20",
            "asal": "Jambi",
            "alamat": "Sabah Balau",
            "hobbi": "Belajar",
            "sosmed": "@krnylee",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
                "https://drive.google.com/uc?export=view&id=1Za-at_KwA9nu02sfpTMC_SC6KlxX3P7X",
                "https://drive.google.com/uc?export=view&id=1ptzssY_Gkkt-73H1C34jMHD3l7MEnKNJ",
                "https://drive.google.com/uc?export=view&id=15XBon1oWrw8tv3fDf7Kz1nmGuK-YkD0p",
                "https://drive.google.com/uc?export=view&id=1yhyTdnnsAsYG9r8i_sWkRBSHeniLvfpo",
                "https://drive.google.com/uc?export=view&id=1swlWLuvnhYIuncA3X_jmga-WUrSCDm2e",
                "https://drive.google.com/uc?export=view&id=1sNQ4_O9pcBOJfuQ1HM7V8cg7uBghZL-4",
            ]
            data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            {
            "nama": "Akeyla Fairuz Shafi",
            "nim": "123450119",
            "umur": "21",
            "asal": "Bandar Lampung",
            "alamat": "Sukabumi",
            "hobbi": "Berenang",
            "sosmed": "@keyashafi_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Elsa Sitorus",
            "nim": "124450088",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Pemda",
            "hobbi": "Rebahan",
            "sosmed": "@_els.a",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Fadya Izzatul 'Aini",
            "nim": "124450062",
            "umur": "20",
            "asal": "Pringsewu",
            "alamat": "Airan",
            "hobbi": "Mancing",
            "sosmed": "@fadyaizzatul_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Lovianora Saragih",
            "nim": "124450105",
            "umur": "19",
            "asal": "Sumatera Utara",
            "alamat": "Way Huwi",
            "hobbi": "Dengerin musik",
            "sosmed": "@_loviaa",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "M. Alsi Syahrulloh",
            "nim": "124450092",
            "umur": "20",
            "asal": "Kalianda",
            "alamat": "Kota Baru",
            "hobbi": "Main game, tidur",
            "sosmed": "@aluccy_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Sherena Florencia",
            "nim": "124450027",
            "umur": "19",
            "asal": "Bengkulu Selatan",
            "alamat": "Belwis",
            "hobbi": "Make up",
            "sosmed": "@sher_renna",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_Divisi_Research_Development = [
                "https://drive.google.com/uc?export=view&id=1ftOW6KLI4wZUDtTiBROw6sJJO_oRmBsF",
                "https://drive.google.com/uc?export=view&id=1FY0YsNf1YdIcCYnGsnxrimz2XSzKzTMq",
                "https://drive.google.com/uc?export=view&id=1ZHYYz6UzqAiLMQzE_ARGjZKzRbz1A0tr",
                "https://drive.google.com/uc?export=view&id=1lfOt31ozH1FxRHcupWxHKWJMIb5Gfj1N",
                "https://drive.google.com/uc?export=view&id=12q0SFvIBYJR-7E-OMI_BonrgBo7_JHc_",
                "https://drive.google.com/uc?export=view&id=1V1_MdlCw0c6e50dpeQEGEEEZ8rnEtPI9",
                "https://drive.google.com/uc?export=view&id=1QL9rfgS3wQmfxRzDfMDK18isZd8o4akI",
                "https://drive.google.com/uc?export=view&id=1NzD8hmdVj_ZSqM2JcRcYJTpqL9gLpkew",
            ]
            data_list_Divisi_Research_Development = [
            {
            "nama": "Razin Hafid Hamdi",
            "nim": "123450096",
            "umur": "21",
            "asal": "Padang",
            "alamat": "Belwis",
            "hobbi": "Futsal",
            "sosmed": "@razyn.hfd",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Faiza Try Anjani",
            "nim": "124450075",
            "umur": "19",
            "asal": "Padang",
            "alamat": "Belwis",
            "hobbi": "Baca novel",
            "sosmed": "@faizaanjanii",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Gathfan Nadif Ali",
            "nim": "124450001",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Rajabasa",
            "hobbi": "Main game",
            "sosmed": "@gathfannadif",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Hafidz Wahdiansyah",
            "nim": "124450064",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Metro Kibang, Lampung Timur",
            "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
            "sosmed": "@apiszzaja_",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Kaleb Filbert Istel",
            "nim": "124450053",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Campang Raya",
            "hobbi": "Ngegym, baca novel",
            "sosmed": "@kelelep_comberan",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Melva Shaprina Febrianti",
            "nim": "124450087",
            "umur": "19",
            "asal": "Sumatera Selatan",
            "alamat": "Sumatera Selatan",
            "hobbi": "Scroll",
            "sosmed": "@melva_fbrt",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Muhammad Syafiqul Falakh",
            "nim": "124450099",
            "umur": "20",
            "asal": "Lampung Utara",
            "alamat": "Asrama TB 3",
            "hobbi": "Membaca",
            "sosmed": "@Syaafiqui",
            "kesan": "...",  
            "pesan": "..."
            },
            {
            "nama": "Rifky Henry Ferdianto",
            "nim": "124450115",
            "umur": "28",
            "asal": "Kota bumi",
            "alamat": "Rajabasa",
            "hobbi": "Lari dari kenyataan",
            "sosmed": "@henryferdianto",
            "kesan": "...",  
            "pesan": "..."
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Research_Development, data_list_Divisi_Research_Development)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        st.markdown("<h3 style='text-align: center;'>Departemen Eksternal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Hubungan Luar", "Divisi Pengabdian Masyarakat"])

        with tab1:
            gambar_urls_Kadep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1N4dIHHdB5CeVz8OygZn-hNOX1MjASRk1",
            ]
            data_list_Kadep_eksternal = [
            {
            "nama": "Arini Puteri Elandra",
            "nim": "123450069",
            "umur": "21",
            "asal": "Lampung",
            "alamat": "Teluk Betung Selatan",
            "hobbi": "Nonton Kartun",
            "sosmed": "@elandraa_",
            "kesan": "",  
            "pesan": "a"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1E3GvqoGWxhja7K_jKk9NpgEVjuLBgrcP",
            ]
            data_list_sekdep_eksternal = [
            {
            "nama": "Nabyla Sharfina",
            "nim": "123450008",
            "umur": "20",
            "asal": "Bengkulu",
            "alamat": "Jalan Lapas",
            "hobbi": "Jalan - jalan",
            "sosmed": "@bylaash",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [
            "https://drive.google.com/uc?export=view&id=1NdxI7kuTgiEiutow57MPkZtSBkau1lK0",
            "https://drive.google.com/uc?export=view&id=1LNA6K_zrpCh_8B787bIxo8JB1UCWVwl9",
            "https://drive.google.com/uc?export=view&id=1RkhM5S_5A8U0kUtI5wWR2SB3YJCLxHmX",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            ]
            data_list_hubungan_luar = [
            {
            "nama": "Khoirul Muttoharoh",
            "nim": "123450021",
            "umur": "21",
            "asal": "Lampung barat",
            "alamat": "Airan",
            "hobbi": "main",
            "sosmed": "@khoirul_muttoharoh",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Ahmad Rizky",
            "nim": "123450050",
            "umur": "21",
            "asal": "Tangerang Selatan",
            "alamat": "GH",
            "hobbi": "ga ngapa ngapain",
            "sosmed": "@ahmad.rizky___",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Indah Khairunnisa",
            "nim": "124450077",
            "umur": "20",
            "asal": "Ampera",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@khaindaa_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Bima Ekayasa",
            "nim": "124450106",
            "umur": "20",
            "asal": "Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "",
            "sosmed": "@bimayasa_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Ahmad Bimo Akbar Arkana",
            "nim": "124450113",
            "umur": "-",
            "asal": "Tanggamus",
            "alamat": "Bandar Lampung",
            "hobbi": "lihat lihat perumahan",
            "sosmed": "@bimo_arkana",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Adinda Deswita Maharani",
            "nim": "124450083",
            "umur": "20",
            "asal": "Ikut kadep",
            "alamat": "love earth",
            "hobbi": "jadi idol",
            "sosmed": "@@adindaadma",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Yollanda Agustina",
            "nim": "124450024",
            "umur": "20",
            "asal": "Kerangka Bawang Sebelah Barat",
            "alamat": "Kayu Mulya",
            "hobbi": "",
            "sosmed": "@yollanda_agustina16",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Riska Erlis Dayu Tiara",
            "nim": "124450022",
            "umur": "20",
            "asal": "Palembang",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@erlsriska",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Alfaya Abiyyi",
            "nim": "124450006",
            "umur": "20",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@alfabiyi",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Asri Meilani",
            "nim": "124450010",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Korpri Raya",
            "hobbi": "",
            "sosmed": "@asrmeilani",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1TUqVePQ0R95loxH2Zqbb_Le74GsnOxTN",
            "https://drive.google.com/uc?export=view&id=1PhtcoQexxeNPD-B53SSojJ-ieX61ZSpx",
            "https://drive.google.com/uc?export=view&id=1-IhjUPBL9tVC_27_oUq1cquGFobnew_6",
            "https://drive.google.com/uc?export=view&id=17WuUaC_OHDVufacMa_rIau-lXD1zK2GK",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            ]
           
            data_list_pengabdian_masyarakat = [
            {
            "nama": "Aditya Taufiqurrohman",
            "nim": "123450032",
            "umur": "22",
            "asal": "",
            "alamat": "Belwis",
            "hobbi": "",
            "sosmed": "@adityatfq",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Fathya Intami Gusda",
            "nim": "123450095",
            "umur": "25",
            "asal": "Tangerang selatan",
            "alamat": "Sukarame",
            "hobbi": "",
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
            "nama": "Selma Siti Aisyah",
            "nim": "123450044",
            "umur": "20",
            "asal": "lampung",
            "alamat": "balam",
            "hobbi": "jalan-jalan",
            "sosmed": "@selmasiti_aisyah",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Ashila Islamisahfa Vanisha",
            "nim": "124450028",
            "umur": "20",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@kshigf",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Danil N Fadillah",
            "nim": "124450103",
            "umur": "19",
            "asal": "",
            "alamat": "",
            "hobbi": "Ngasih makan ikan cupang",
            "sosmed": "@d4niel_fdlh",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Favian Arkaanda",
            "nim": "124450021",
            "umur": "19",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@fvnnn05",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Muhammad Fathiy Zumar Yazid",
            "nim": "124450081",
            "umur": "20",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@jaldii._",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Saskia Nova Magdalena",
            "nim": "124450074",
            "umur": "-",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@snova.19",
            "kesan": "",  
            "pesan": ""
            },
        ]
            display_images_with_data(gambar_urls_pengabdian_masyarakat, data_list_pengabdian_masyarakat)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
            "https://drive.google.com/uc?export=view&id=1N4dIHHdB5CeVz8OygZn-hNOX1MjASRk1",
            ]
            data_list_Kadep_internal = [
            {
            "nama": "Haikal Fransisko Simbolon",
            "nim": "123450106",
            "umur": "23",
            "asal": "Jambi",
            "alamat": "Jatimulyo",
            "hobbi": "",
            "sosmed": "@haikalsbln_",
            "kesan": "",  
            "pesan": "a"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=1E3GvqoGWxhja7K_jKk9NpgEVjuLBgrcP",
            ]
            data_list_sekdep_internal = [
            {
            "nama": "Kharisma Mustika Sari",
            "nim": "123450034",
            "umur": "21",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@rismaa.mustika_",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=1NdxI7kuTgiEiutow57MPkZtSBkau1lK0",
            "https://drive.google.com/uc?export=view&id=1LNA6K_zrpCh_8B787bIxo8JB1UCWVwl9",
            "https://drive.google.com/uc?export=view&id=1RkhM5S_5A8U0kUtI5wWR2SB3YJCLxHmX",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            ]
            data_list_keharmonisasian = [
            {
            "nama": "Hanna Gresia Sinaga",
            "nim": "123450038",
            "umur": "21",
            "asal": "Kisaran City",
            "alamat": "Sukarame",
            "hobbi": "",
            "sosmed": "@hanna_g_sinaga",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Ahmad Farhan Ghani",
            "nim": "123450121",
            "umur": "20",
            "asal": "Kemiling",
            "alamat": "Kemiling",
            "hobbi": "Olahraga menembak",
            "sosmed": "@farhnghnii",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Aisyah Khairun Nisa",
            "nim": "124450096",
            "umur": "20",
            "asal": "Air Molek, Riau",
            "alamat": "Belwis",
            "hobbi": "Menulis Wish list",
            "sosmed": "@aisyahkhair_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Cerine Sihotang",
            "nim": "124450049",
            "umur": "19",
            "asal": "Medan",
            "alamat": "Belwis",
            "hobbi": "Balap liar",
            "sosmed": "@cerine_ipynb",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Jaya Saputra Tamba",
            "nim": "124450094",
            "umur": "22",
            "asal": "Kisaran City",
            "alamat": "Pemda",
            "hobbi": "Kick boxing",
            "sosmed": "@jay.saputratmb",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Najla Nursyifa",
            "nim": "124450051",
            "umur": "20",
            "asal": "Aceh",
            "alamat": "Belwis",
            "hobbi": "Nonton ASMR",
            "sosmed": "@njlanursyifa",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Rozak Ramdani",
            "nim": "124450100",
            "umur": "18",
            "asal": "Lampung Selatan",
            "alamat": "Korpri Raya",
            "hobbi": "Isengin Harvin di kelas",
            "sosmed": "@rozakramdani__",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Teresa Christiani Purba",
            "nim": "124450046",
            "umur": "19",
            "asal": "Riau",
            "alamat": "Belwis",
            "hobbi": "Masak",
            "sosmed": "@christiani8872",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=1TUqVePQ0R95loxH2Zqbb_Le74GsnOxTN",
            "https://drive.google.com/uc?export=view&id=1PhtcoQexxeNPD-B53SSojJ-ieX61ZSpx",
            "https://drive.google.com/uc?export=view&id=1-IhjUPBL9tVC_27_oUq1cquGFobnew_6",
            "https://drive.google.com/uc?export=view&id=17WuUaC_OHDVufacMa_rIau-lXD1zK2GK",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            ]
           
            data_list_kerohanian = [
            {
            "nama": "Muhammad Hanid Dzaky Arifin",
            "nim": "124450064",
            "umur": "21",
            "asal": "Sumatera Barat",
            "alamat": "Way Kandis",
            "hobbi": "Nonton film",
            "sosmed": "@hnfdzky_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Audina Fitria",
            "nim": "124450038",
            "umur": "20",
            "asal": "Sumatera Barat",
            "alamat": "Sukarame",
            "hobbi": "Main ke air terjun",
            "sosmed": "@audinaf_03",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Cika Adelia Br Marbun",
            "nim": "124450107",
            "umur": "20",
            "asal": "Pekanbaru, Riau",
            "alamat": "Belwis",
            "hobbi": "Dengerin lagu",
            "sosmed": "@cikamrbn",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Gustin Haleluya Tampubolon",
            "nim": "124450068",
            "umur": "21",
            "asal": "Toba, Sumatera Utara",
            "alamat": "Airan",
            "hobbi": "Nonton",
            "sosmed": "@gustinhaleluya",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Muhammad Harvinsyah",
            "nim": "124450128",
            "umur": "20",
            "asal": "Sumatera Selatan",
            "alamat": "Belwis",
            "hobbi": "Beburu ayam hutan",
            "sosmed": "@muhvinz_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Rafa Sabina Fahimah",
            "nim": "124450036",
            "umur": "20",
            "asal": "Natar",
            "alamat": "Natar",
            "hobbi": "Nginep di rumah Yollanda",
            "sosmed": "@snasaa",
            "kesan": "",  
            "pesan": ""
            },
        ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Storage Sains Data</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
            "https://drive.google.com/uc?export=view&id=1CSwgJej4dFkWF4nJF_GDXfC4zQlFbMVS",
            ]
            data_list_Kadep_ssd = [
            {
            "nama": "Ihsan Maulana Yusuf",
            "nim": "123450110",
            "umur": "21",
            "asal": "Sumatra Barat",
            "alamat": "Belwis",
            "hobbi": "",
            "sosmed": "@ihsan.myusuf",
            "kesan": "",  
            "pesan": "a"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)
            
        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1E3GvqoGWxhja7K_jKk9NpgEVjuLBgrcP",
            ]
            data_list_sekdep_ssd = [
            {
            "nama": "Hanifah Inaya Sani",
            "nim": "123450123",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Masak",
            "sosmed": "@_inayasani",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1NdxI7kuTgiEiutow57MPkZtSBkau1lK0",
            "https://drive.google.com/uc?export=view&id=1LNA6K_zrpCh_8B787bIxo8JB1UCWVwl9",
            "https://drive.google.com/uc?export=view&id=1RkhM5S_5A8U0kUtI5wWR2SB3YJCLxHmX",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
            ]
            data_list_kemitraan = [
            {
            "nama": "Afifah Fauziah",
            "nim": "125450002",
            "umur": "20",
            "asal": "Bandung",
            "alamat": "Airan",
            "hobbi": "Nonton Marvel",
            "sosmed": "@fifah.zy",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Hasan Nur Ramadhan",
            "nim": "",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Korpri",
            "hobbi": "Coding",
            "sosmed": "",
            "kesan": "",  
            "pesan": "@hasan.ramadhan08"
            },
            {
            "nama": "Layina Ropiqo",
            "nim": "124450016",
            "umur": "19",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Nonton Dracin",
            "sosmed": "",
            "kesan": "",  
            "pesan": "@lay.inr_"
            },
            {
            "nama": "Mochammad Iqbal Az-Zahir",
            "nim": "124450052",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Natar",
            "hobbi": "Nonton drakor",
            "sosmed": "@iqbalazzahir_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Talitha Justine",
            "nim": "124450076",
            "umur": "19",
            "asal": "Jakarta",
            "alamat": "Pemda",
            "hobbi": "Nonton",
            "sosmed": "-",
            "kesan": "",  
            "pesan": ""
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1TUqVePQ0R95loxH2Zqbb_Le74GsnOxTN",
            "https://drive.google.com/uc?export=view&id=1PhtcoQexxeNPD-B53SSojJ-ieX61ZSpx",
            "https://drive.google.com/uc?export=view&id=1-IhjUPBL9tVC_27_oUq1cquGFobnew_6",
            "https://drive.google.com/uc?export=view&id=17WuUaC_OHDVufacMa_rIau-lXD1zK2GK",
            "https://drive.google.com/uc?export=view&id=117nH2xIUY0iEdEL4euoPqw0foc87uK98",
            ]
           
            data_list_kewirausahaan = [
            {
            "nama": "Anadia Carana",
            "nim": "123450019",
            "umur": "20",
            "asal": "Palembang",
            "alamat": "Way Huwi",
            "hobbi": "Nyari duit",
            "sosmed": "@anadiacrn_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Abdillah Fikri Al pome",
            "nim": "123450062",
            "umur": "21",
            "asal": "Baturaja, Sumatera Selatan",
            "alamat": "Belakang PB",
            "hobbi": "Olahraga",
            "sosmed": "@pomest__",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Afdhal Rahmad Setiawan",
            "nim": "124450008",
            "umur": "20",
            "asal": "Sumatera Barat",
            "alamat": "Belwis",
            "hobbi": "Fishing",
            "sosmed": "@dhal_setiawan",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Anggun Nita",
            "nim": "124450009",
            "umur": "20",
            "asal": "Lampung Utara",
            "alamat": "Belwis",
            "hobbi": "Nonton Kartun",
            "sosmed": "@anggunnitaaa_",
            "kesan": "",  
            "pesan": ""
            },
            {
            "nama": "Della Anisa Fitri",
            "nim": "124450095",
            "umur": "17",
            "asal": "Lampung Timur",
            "alamat": "Kota Baru",
            "hobbi": "Berdandan",
            "sosmed": "@dellaansaftr",
            "kesan": "",  
            "pesan": ""
            },
        ]
            display_images_with_data(gambar_urls_kewirausahaan, data_list_kewirausahaan)
    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1b5BlJfjO0SGyy0XTUPyN8ZOJ8zkvOBUD",
            ]
            data_list_Kadep_medkraf = [
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
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1hB4PN9eK9z13aE5sxeq218htzjTkEVS9",
            ]
            data_list_sekdep_medkraf = [
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
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1Re_t0YbK2mT-mjnestjAdTS11mGbAtc6",
            "https://drive.google.com/uc?export=view&id=1GSlalGfy31swutJV2zZpWdSRgGK9tlSo",
            "https://drive.google.com/uc?export=view&id=1YEEeDJoyZpavqkCRiyzLAPkp30gGWcJs",
            "https://drive.google.com/uc?export=view&id=1yZWmRobFZhHEX0y-5e0_PH2eJ4LnK748",
            ]
            data_list_Divisi_dokumentasi = [
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
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1Vx0Nk2OylnbrRx_L6ZW5JQ6GVqgI3rTQ",
            "https://drive.google.com/uc?export=view&id=1Y-n9WgzEVokH0XimAqDOSa_epwnhnwmZ",
            "https://drive.google.com/uc?export=view&id=1qLUI-SymckwaduId3Bbk4DEOa0mGPnY9",
            "https://drive.google.com/uc?export=view&id=1m_my97kVsCVPinEGsp19Rg4rFgbUG8S_",
            "https://drive.google.com/uc?export=view&id=1n0jpZiHb2p-lVgL4sXTd76oGO8sfi1Ed",
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
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
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1atZTxIoNLVNQVFRr4CRIL7sWe8SGNYbq",
            "https://drive.google.com/uc?export=view&id=1KSezc8FGz4EDRuYnUxfB0J5kcA6xw1Q3",
            "https://drive.google.com/uc?export=view&id=1AZeqrWofTPAnMCbqZdGvhoUcoraK6SZt",
            "https://drive.google.com/uc?export=view&id=1xR39p8ryuUsU9tngr4Vb1Cw37p4zQ4y8",
            ]
            data_list_Divisi_Visual_Design = [
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
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()
