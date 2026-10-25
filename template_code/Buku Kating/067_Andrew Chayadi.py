import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import base64

st.set_page_config(layout="wide")

st.markdown("""<style>.centered-title {text-align: center;}</style>""", unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F8F5F2;
        color: #000000; 
    }

    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    [data-testid="collapsedControl"] {
        color: #bd411b !important;
    }

    [data-testid="stSidebar"] {
        background-color: #bd411b !important;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    [data-testid="stTabs"] button, 
    [data-testid="stTabs"] button * {
        color: #000000 !important;
    }
    
    [data-testid="stTabs"] [data-baseweb="tab-highlight"] {
        background-color: #bd411b !important;
    }

    .gambar-timbul {
        width: 100%;
        border-radius: 8px;
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        cursor: pointer;
    }
    .gambar-timbul:hover {
        transform: translateY(-8px) scale(1.03); 
        box-shadow: 0 10px 20px rgba(0,0,0,0.3); 
    }
    </style>
    """,
    unsafe_allow_html=True
)
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
            "container": {
                "padding": "10px !important", 
                "background-color": "#c84b22", 
                "border": "none !important", 
                "border-radius": "0 !important", 
                "box-shadow": "none !important" 
            },
            "icon": {
                "color": "white", 
                "font-size": "19px"
            },
            "nav-link": {
                "font-size": "14px",
                "text-align": "center",
                "margin": "5px", 
                "color": "white",
                "background-color": "transparent", 
                "--hover-color": "rgba(255, 255, 255, 0.1)",
            },
            "nav-link-selected": {
                "background-color": "#8c3010", 
                "color": "white",
                "border-radius": "10px" 
            },
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
@st.cache_data
@st.cache_data
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    def img_to_base64(img):
        import base64
        from io import BytesIO
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    st.markdown("""
    <style>
    .kartu-profil {
        transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }
    .kartu-profil:hover {
        transform: translateY(-8px) !important;
        box-shadow: 0 15px 25px rgba(0,0,0,0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    for i in range(0, len(images), 2):
        cols = st.columns(2)
        
        for j in range(2):
            index = i + j
            if index < len(images):
                with cols[j]:
                    img_b64 = img_to_base64(images[index])
                    data = data_list[index] if index < len(data_list) else {}
                    
                    nama = data.get('nama', '-')
                    nim = data.get('nim', '-')
                    umur = data.get('umur', '-')
                    asal = data.get('asal', '-')
                    alamat = data.get('alamat', '-')
                    hobbi = data.get('hobbi', '-')
                    sosmed = data.get('sosmed', '-')
                    kesan = data.get('kesan', '-')
                    pesan = data.get('pesan', '-')

                    card_html = f"""<div class="kartu-profil" style="display: flex; flex-direction: row; background-color: #ffffff; border-radius: 16px; box-shadow: 0 6px 12px rgba(0,0,0,0.08); overflow: hidden; margin-bottom: 20px; height: 360px;">
<div style="flex: 0 0 45%;">
<img src="data:image/png;base64,{img_b64}" style="width: 100%; height: 100%; object-fit: cover; display: block;">
</div>
<div style="flex: 1; padding: 18px; display: flex; flex-direction: column; justify-content: space-between;">
<div>
<h4 style="margin: 0 0 4px 0; color: #1e1e1e; font-size: 18px; line-height: 1.2;">{nama}</h4>
<p style="margin: 0 0 12px 0; color: #666; font-size: 14px; font-weight: bold;">{nim}</p>
<div style="font-size: 13px; color: #444; line-height: 1.5;">
<b>Umur:</b> {umur}<br>
<b>Asal:</b> {asal}<br>
<b>Alamat:</b> {alamat}<br>
<b>Hobbi:</b> {hobbi}<br>
<b>Sosmed:</b> {sosmed}
</div>
</div>
<div style="background-color: #FFF3E0; padding: 12px; border-radius: 8px; margin-top: 12px;">
<p style="margin: 0 0 4px 0; font-size: 12px; font-style: italic; color: #bd411b;"><b>Kesan:</b> "{kesan}"</p>
<p style="margin: 0; font-size: 12px; font-style: italic; color: #bd411b;"><b>Pesan:</b> "{pesan}"</p>
</div>
</div>
</div>"""
                    
                    st.markdown(card_html, unsafe_allow_html=True)
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
                "kesan": "Abangnya baek banget sumpah, santai namun berwibawa",  
                "pesan": "Semangat bang himm semoga bisa lulus dengan memuaskan"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abang jen yang baik hati, keren, asik, dan lucu.. suka ngelawak",  
                "pesan": "Semangat terus bang, sama latihan basket buat io 2026 bang biar ga dimarahin bang tobi wkwkkw"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya seru, ramah, baik lagi",  
                "pesan": "Semangat terus kakkk"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang nim yang baik hati, dan ramah, asik juga",  
                "pesan": "My Abang Kakak NIM hebat mantap jiwa, semangat bang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya asik, ramah, baik hati",  
                "pesan": "Semangat ya kakk sudah mau semester akhir"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakanya keliatan pendiem, namun baik dan asik",  
                "pesan": "Semangat terus kakk, semoga ga tertekan di semester akhir"
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
                "kesan": "Kakanya keren banget, senator yang menyampaikan aspirasi",  
                "pesan": "Semangat terus kuliahnya kak"
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
                "kesan": "abang melet 11/12 sama kairi, asik",  
                "pesan": "Semangat terus ya bang, biar jadi kairi beneran"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Asik abangnya, jago maen ml pula",  
                "pesan": "Semangat terus bang, kapan mau mabar bang kmaren iya iya aja"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya asik, baik , ramah juga",  
                "pesan": "Semangat terus ya kak kuliahnya, biar ga dapat c kayak saya"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abang chill yang baik",  
                "pesan": "Semangat bang kuliahnya"
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
                "kesan": "kakak lia ni terlihat pintar jujur",  
                "pesan": "Semangat terus kuliahnya kaks"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya asik, ceria sekali, mentor bayes mantap",  
                "pesan": "Semangat kuliahnya kak!"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abang keren berambut ikonik",  
                "pesan": "Semangat terus bang kuliahnya, tutor rambut kek abang si"
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
                "kesan": "Kakaknya baik, asik, ramah",  
                "pesan": "Semangat terus kakaa"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakak asik, baik, ramah",  
                "pesan": "Semangat terus kuliahnya kaks"
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
            "kesan": "Bang ridho yang terlihat serius, kadang misterius",  
            "pesan": "semangat terus banggg"
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
            "kesan": "Kak Jue yang asik, dulu mentor tpb 36 yang sudah keliatan kakaknya asik",  
            "pesan": "Semangat terus kakk"
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
            "kesan": "sangat pintar, mapres gg wow",  
            "pesan": "semangat bang, tutor sepintar abang dong"
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "abang keren, hebat, asik",  
            "pesan": "semangat kuliahnya bang"
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "kakak asik, baik, ramah dan pokoknya best",  
            "pesan": "semangat kuliahnya kakks"
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
            "kesan": "bang givaro yang baik, asik keren",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "kakak pintar, baik hati dan ramah",  
            "pesan": "semangat kak tutorr"
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "kakak baik, asik, ramahh",  
            "pesan": "semangat terus kak kuliahnyaa"
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "abang pinter bener dah",  
            "pesan": "semangat bang pimsid"
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
            "kesan": "baik, ramah, suka lari",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "abang baik asik, suka nafas manual wkkwk",  
            "pesan": "awas kualat bang nyuruh nafas manual mulu"
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "kakak baik asik, pintar",  
            "pesan": "semangat terus kak"
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "kakak baik, asik, jago maen valorant",  
            "pesan": "semangat kak ngejer imo nya wkwkkw"
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
            "kesan": "abang keren, jago basket, tinggi kek tiang listrik",
            "pesan": "semangat terus bang, mendekati semester akhir juga wkwk"
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
            "kesan": "kakak yang sangat rapi dan cekatan dalam mengelola administrasi",
            "pesan": "Semangat terus kak"
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
            "kesan": "abang mankom yang cekatan kalau ada lomba",
            "pesan": "waspada tim saya akan daftar lomba lagi bang wkkwkwk"
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
            "kesan": "baik, ramah, asik, jago futsal",
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
            "kesan": "kakak yang baik, murah senyum, dan pedoman",
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
                "kesan": "abang asik yang gampang diajak ngobrol",
                "pesan": "Semangat terus memimpin divisinya bang!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "abang yang baik, hebat, dan asik",
                "pesan": "my abang mentor gweh semangat kuliahnya bang!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live tiktok",
                "sosmed": "@bryantel_",
                "kesan": "asik, baik dan ramah",
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
                "kesan": "abang asik, keren, ramah",
                "pesan": "kalkulator jangan ilang lagi bang wkwkkw"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "kakak yang sangat baik dan murah senyum",
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
            "kesan": "kakak kadep baik, ramah,",  
            "pesan": "semangat terus kuliahnya kakk"
            },
            {
            "nama": "Vany Salsabila Putri",
            "nim": "123450022",
            "umur": "20",
            "asal": "Sibolga",
            "alamat": "Pudan Kost",
            "hobbi": "Pacaran",
            "sosmed": "@vany.salsabilaa",
            "kesan": "kakak asik, baik, ramahh",  
            "pesan": "semangat terus kak kedepanya"
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
                "https://drive.google.com/uc?export=view&id=10fslg-ZoNCd03opteMzxtm0_0SwCcaJM",
                "https://drive.google.com/uc?export=view&id=19VSpDE7AQc-ElQhWuN21SqtvVS_K-qCK",
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
            "kesan": "berwibawa, asik, baik",  
            "pesan": "ajarin sulap bang hehe"
            },
            {
            "nama": "Afriza Azmi",
            "nim": "124450110",
            "umur": "20",
            "asal": "Malang",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@friezazmi",
            "kesan": "abang baik, asik, keren",  
            "pesan": "semangat terus bang kedepannya"
            },
            {
            "nama": "Haikal Seventino Tamba",
            "nim": "124450012",
            "umur": "18",
            "asal": "Solok, Sumatera Barat",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@_haikaaall",
            "kesan": "abang baek, tampak diam namun menyeramkan",  
            "pesan": "semangat terus kedepannya bang"
            },
            {
            "nama": "Euodia Meiliana Friedita",
            "nim": "124450029",
            "umur": "18",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@yudiameilianaa_",
            "kesan": "kakak yang baik, perhatian, dan asik",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Ayake Alfatih Ramadan",
            "nim": "124450108",
            "umur": "21",
            "asal": "Solok, Sumatera Barat",
            "alamat": "",
            "hobbi": "Masak ayam",
            "sosmed": "@ykeall",
            "kesan": "abang besar tinggi, keren juga, suka jail pula",  
            "pesan": "semangat terus bang!"
            },
             {
           "nama": "Caesar Ozora Alrando",
            "nim": "124450017",
            "umur": "21",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@caesar.oriza",
            "kesan": "abang seram, namun dibaik itu asik",  
            "pesan": "semangat terus abaang"
            },
            {
            "nama": "Putri Manna Anantama Simbolon",
            "nim": "124450056",
            "umur": "18",
            "asal": "",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@@putrimannaa",
            "kesan": "kakak yang asik, cantik, baik pula",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Queenta Thifaal Nabila",
            "nim": "124450059",
            "umur": "18",
            "asal": "Kota Gajah",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@queentanabila",
            "kesan": "berwibawa, tegas dan disiplin",  
            "pesan": "semangat terus kedepannya kakk"
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
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "desmannhal_",
                "kesan": "abang asik, baik juga",  
                "pesan": "semangat bang kedepannya"
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "kakak yang asik, baik dan ramah",  
                "pesan": "semangat kuliahnya kakk"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal": "Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakak yang asik, baik dan ramah",  
                "pesan": "smeangat kuliahnya kakk"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "kakak yang asik, baik dan ramahh",  
                "pesan": "semangat terus kuliahnya kakk"
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "kakak yang asik, baik dan ramah",  
                "pesan": "semangat teruss kuliahnya kakkk"
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Jayapura",
                "alamat": "RS airan",
                "hobbi": "",
                "sosmed": "@jemarrro",
                "kesan": "Abang yang asik, baik dan ramah",  
                "pesan": "Semangat terus abang kuliahnya!!"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal": "Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "abang yang asik, baik dan ramah",  
                "pesan": "semangat terus abangg"
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
            "https://drive.google.com/uc?export=view&id=1g-JXO76tjEz67NFg8eKFjEKBQlPncP6v",
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
            "kesan": "kakak yang asik, baik dan ramah suka ngelawak pula",  
            "pesan": "semangat terus kuliahnya bangg"
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
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kuliahnya kakk"
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
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "Tenang tenang abang di sana yaa, Rest In Piece Abangku"
            },
            {
            "nama": "Manuel Frederika",
            "nim": "124450039",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Batam",
            "hobbi": "Tenis meja",
            "sosmed": "@manuelfdk_",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus kedepannya bang"
            },
            {
            "nama": "Ni Made Okta Viola Darma Putri",
            "nim": "124450005",
            "umur": "12",
            "asal": "Bali",
            "alamat": "Nusa Penida",
            "hobbi": "Menghayal",
            "sosmed": "@Violaadrtr_",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat kuliahnya kakk"
            },
            {
            "nama": "Risa Romadona",
            "nim": "124450127",
            "umur": "20",
            "asal": "Natar",
            "alamat": "Natar",
            "hobbi": "Natar",
            "sosmed": "@risarmdna",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Vannisa Ramadhani",
            "nim": "124450078",
            "umur": "19",
            "asal": "Bali",
            "alamat": "Teluk Betung",
            "hobbi": "Nonton KHW",
            "sosmed": "@vunnycaa",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "Semangat terus kakk"
            },
            {
            "nama": "Yulia Kristine Malau",
            "nim": "124450119",
            "umur": "20",
            "asal": "Jambi",
            "alamat": "Sabah Balau",
            "hobbi": "Belajar",
            "sosmed": "@krnylee",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkkkkk"
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
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat kuliahnya bang!"
            },
            {
            "nama": "Elsa Sitorus",
            "nim": "124450088",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Pemda",
            "hobbi": "Rebahan",
            "sosmed": "@_els.a",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            {
            "nama": "Fadya Izzatul 'Aini",
            "nim": "124450062",
            "umur": "20",
            "asal": "Pringsewu",
            "alamat": "Airan",
            "hobbi": "Mancing",
            "sosmed": "@fadyaizzatul_",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semngat terus kakk"
            },
            {
            "nama": "Lovianora Saragih",
            "nim": "124450105",
            "umur": "19",
            "asal": "Sumatera Utara",
            "alamat": "Way Huwi",
            "hobbi": "Dengerin musik",
            "sosmed": "@_loviaa",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat kuliahnya kak"
            },
            {
            "nama": "M. Alsi Syahrulloh",
            "nim": "124450092",
            "umur": "20",
            "asal": "Kalianda",
            "alamat": "Kota Baru",
            "hobbi": "Main game, tidur",
            "sosmed": "@aluccy_",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Sherena Florencia",
            "nim": "124450027",
            "umur": "19",
            "asal": "Bengkulu Selatan",
            "alamat": "Belwis",
            "hobbi": "Make up",
            "sosmed": "@sher_renna",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat kuliahnya kakk"
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
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Faiza Try Anjani",
            "nim": "124450075",
            "umur": "19",
            "asal": "Padang",
            "alamat": "Belwis",
            "hobbi": "Baca novel",
            "sosmed": "@faizaanjanii",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Gathfan Nadif Ali",
            "nim": "124450001",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Rajabasa",
            "hobbi": "Main game",
            "sosmed": "@gathfannadif",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Hafidz Wahdiansyah",
            "nim": "124450064",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Metro Kibang, Lampung Timur",
            "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
            "sosmed": "@apiszzaja_",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat teru abangg"
            },
            {
            "nama": "Kaleb Filbert Istel",
            "nim": "124450053",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Campang Raya",
            "hobbi": "Ngegym, baca novel",
            "sosmed": "@kelelep_comberan",
            "kesan": "abang yang asik, berotot, baik dan ramah",  
            "pesan": "semangat bang otot"
            },
            {
            "nama": "Melva Shaprina Febrianti",
            "nim": "124450087",
            "umur": "19",
            "asal": "Sumatera Selatan",
            "alamat": "Sumatera Selatan",
            "hobbi": "Scroll",
            "sosmed": "@melva_fbrt",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kuliahnya kakkk"
            },
            {
            "nama": "Muhammad Syafiqul Falakh",
            "nim": "124450099",
            "umur": "20",
            "asal": "Lampung Utara",
            "alamat": "Asrama TB 3",
            "hobbi": "Membaca",
            "sosmed": "@Syaafiqui",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Rifky Henry Ferdianto",
            "nim": "124450115",
            "umur": "28",
            "asal": "Kota bumi",
            "alamat": "Rajabasa",
            "hobbi": "Lari dari kenyataan",
            "sosmed": "@henryferdianto",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bang, kotabumi pride"
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
            "https://drive.google.com/uc?export=view&id=1g-JXO76tjEz67NFg8eKFjEKBQlPncP6v",
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
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kak"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1tbJhrkjRdo3WHIXp7RGhfG6ur0GcljVI",
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
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [
            "https://drive.google.com/uc?export=view&id=1pxQ2X6CxL7TGamYbxewNx0HPyriRSKbv",
            "https://drive.google.com/uc?export=view&id=19byi4aK_pNmzPPtpHilUNUDOnMHJhgMz",
            "https://drive.google.com/uc?export=view&id=1eBg3YzzRjWv5HL-_MdrTYGjUnOCv2MRL",
            "https://drive.google.com/uc?export=view&id=1c6Y9E0EM8NDDF97IOQmY36qyWPr693yY",
            "https://drive.google.com/uc?export=view&id=1zN8-vJAU9rYdVs794mr5lqfwiNyaR03u",
            "https://drive.google.com/uc?export=view&id=10xwMJl3LHaeenET0u6Bk6jshkYN9CUOV",
            "https://drive.google.com/uc?export=view&id=1fiUYgOP67qKokVw9M5S-gPCwSQJjBqm2",
            "https://drive.google.com/uc?export=view&id=19LBMF4gIYEZHZMKEGETi67XPWLM67Ew3",
            "https://drive.google.com/uc?export=view&id=1F0cvNkFTDBePb-Wewt7OEOwqGEy1wckv",
            "https://drive.google.com/uc?export=view&id=1F0cvNkFTDBePb-Wewt7OEOwqGEy1wckv",
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
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Ahmad Rizky",
            "nim": "123450050",
            "umur": "21",
            "asal": "Tangerang Selatan",
            "alamat": "GH",
            "hobbi": "ga ngapa ngapain",
            "sosmed": "@ahmad.rizky___",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Indah Khairunnisa",
            "nim": "124450077",
            "umur": "20",
            "asal": "Ampera",
            "alamat": "Disini aja",
            "hobbi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
            "sosmed": "@khaindaa_",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Bima Ekayasa",
            "nim": "124450106",
            "umur": "20",
            "asal": "Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Berlaku humoris dan manis",
            "sosmed": "@bimayasa_",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Ahmad Bimo Akbar Arkana",
            "nim": "124450113",
            "umur": "20",
            "asal": "Tanggamus",
            "alamat": "Bandar Lampung",
            "hobbi": "lihat lihat perumahan",
            "sosmed": "@bimo_arkana",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Adinda Deswita Maharani",
            "nim": "124450083",
            "umur": "20",
            "asal": "Ikut kadep",
            "alamat": "love earth",
            "hobbi": "jadi idol",
            "sosmed": "@@adindaadma",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Yollanda Agustina",
            "nim": "124450024",
            "umur": "20",
            "asal": "Kerangka Bawang Sebelah Barat",
            "alamat": "Kayu Mulya",
            "hobbi": "futsal",
            "sosmed": "@yollanda_agustina16",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Riska Erlis Dayu Tiara",
            "nim": "124450022",
            "umur": "20",
            "asal": "Palembang",
            "alamat": "Bebas",
            "hobbi": "Ngefollow up chat",
            "sosmed": "@erlsriska",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Alfaya Abiyyi",
            "nim": "124450006",
            "umur": "20",
            "asal": "Balam",
            "alamat": "Balam",
            "hobbi": "Makan yang manis biar manis",
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
            "hobbi": "menonton film",
            "sosmed": "@asrmeilani",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1thhQockQPc81Hrw5T4hBuE4m14TikkfT",
            "https://drive.google.com/uc?export=view&id=1kgAopWkrKxHlqaWVTAiR2IaBBi-UMFGJ",
            "https://drive.google.com/uc?export=view&id=1ONqJaZUIsNrm20hZV3b12qhujhYmRGYU",
            "https://drive.google.com/uc?export=view&id=1WfSjKNl_6PtYoHO6ttGmodpyvuYZD_pd",
            "https://drive.google.com/uc?export=view&id=1EBnJ0ZiLoEJ9YN4DHBb7Nxwyoj_WaCVO",
            "https://drive.google.com/uc?export=view&id=1od7tSpOVLhk5Uuxvl8Of3DfrFnuURQUo",
            "https://drive.google.com/uc?export=view&id=14kUkc2PHfnvIEoTdki-nwm75iHNp8zvP",
            "https://drive.google.com/uc?export=view&id=14S22usYXwhdLTgwKY7wBg6LRHFjS_Wgz",
            "https://drive.google.com/uc?export=view&id=1EJpLmbBsLNtxhTRxsG-k6iQMcoftZcFJ",
            ]
           
            data_list_pengabdian_masyarakat = [
            {
            "nama": "Aditya Taufiqurrohman",
            "nim": "123450032",
            "umur": "22",
            "asal": "Tetangga Kadep",
            "alamat": "Belwis",
            "hobbi": "Memancing Keributan",
            "sosmed": "@adityatfq",
            "kesan": "abang yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Fathya Intami Gusda",
            "nim": "123450095",
            "umur": "25",
            "asal": "Tangerang selatan",
            "alamat": "Sukarame",
            "hobbi": "nonton",
            "sosmed": "@fatthyaa_",
            "kesan": "kakak yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Tarisya Hidayatul Rahmi",
            "nim": "123450052",
            "umur": "25",
            "asal": "Luhak tanah data",
            "alamat": "Gerbar",
            "hobbi": "Jadi orang baik",
            "sosmed": "-",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Selma Siti Aisyah",
            "nim": "123450044",
            "umur": "20",
            "asal": "lampung",
            "alamat": "balam",
            "hobbi": "jalan-jalan",
            "sosmed": "@selmasiti_aisyah",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Ashila Islamisahfa Vanisha",
            "nim": "124450028",
            "umur": "20",
            "asal": "Sini",
            "alamat": "Jauh Pokoknya",
            "hobbi": "Tidur",
            "sosmed": "@kshigf",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Danil N Fadillah",
            "nim": "124450103",
            "umur": "19",
            "asal": "Karawang",
            "alamat": "Belakang Polda",
            "hobbi": "Ngasih makan ikan cupang",
            "sosmed": "@d4niel_fdlh",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Favian Arkaanda",
            "nim": "124450021",
            "umur": "19",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@fvnnn05",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Muhammad Fathiy Zumar Yazid",
            "nim": "124450081",
            "umur": "20",
            "asal": "",
            "alamat": "",
            "hobbi": "Tidur",
            "sosmed": "@jaldii._",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            {
            "nama": "Saskia Nova Magdalena",
            "nim": "124450074",
            "umur": "20",
            "asal": "Banyak Begal",
            "alamat": "Pinggir Jalan",
            "hobbi": "Tidur",
            "sosmed": "@snova.19",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
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
            "https://drive.google.com/uc?export=view&id=1kGtKEzfgls6ef_oKU8gIrCrswMjvm6--",
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
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bang"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=110WGquNZuSQk4nQVn4EDg8SFZzs0zPxy",
            ]
            data_list_sekdep_internal = [
            {
            "nama": "Kharisma Mustika Sari",
            "nim": "123450034",
            "umur": "21",
            "asal": "Way Kanan",
            "alamat": "untung suropat",
            "hobbi": "Suka menolong orang",
            "sosmed": "@rismaa.mustika_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=1V08D2gwf2lZ5hWZRDGzr459YLQXvsEuD",
            "https://drive.google.com/uc?export=view&id=1hNcuCxmSd5TY6TYwnLJBvg0lCCktvtUP",
            "https://drive.google.com/uc?export=view&id=1TMIkLgkIl3v-mPEYOZoaxrz2HZUL7L_5",
            "https://drive.google.com/uc?export=view&id=1UR3TXBnVZ_GvcOiqS9M1306-E35edKG0",
            "https://drive.google.com/uc?export=view&id=1q3lCHc_6mo4REx341E4dLByFr_gn-DIg",
            "https://drive.google.com/uc?export=view&id=19JjgXBZS8JPYcVfvnal5M531Gw4RuVEr",
            "https://drive.google.com/uc?export=view&id=181kFHPoj4VhIaRMAAjP2BiIzE8OJN9EH",
            "https://drive.google.com/uc?export=view&id=1G-rd9MULK5udMN3t6gr61Dh7_YCM1BEj",
            ]
            data_list_keharmonisasian = [
            {
            "nama": "Hanna Gresia Sinaga",
            "nim": "123450038",
            "umur": "21",
            "asal": "Kisaran City",
            "alamat": "Sukarame",
            "hobbi": "menyapa satpam gedung f",
            "sosmed": "@hanna_g_sinaga",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Ahmad Farhan Ghani",
            "nim": "123450121",
            "umur": "20",
            "asal": "Kemiling",
            "alamat": "Kemiling",
            "hobbi": "Olahraga menembak",
            "sosmed": "@farhnghnii",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Aisyah Khairun Nisa",
            "nim": "124450096",
            "umur": "20",
            "asal": "Air Molek, Riau",
            "alamat": "Belwis",
            "hobbi": "Menulis Wish list",
            "sosmed": "@aisyahkhair_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Cerine Sihotang",
            "nim": "124450049",
            "umur": "19",
            "asal": "Medan",
            "alamat": "Belwis",
            "hobbi": "Balap liar",
            "sosmed": "@cerine_ipynb",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Jaya Saputra Tamba",
            "nim": "124450094",
            "umur": "22",
            "asal": "Kisaran City",
            "alamat": "Pemda",
            "hobbi": "Kick boxing",
            "sosmed": "@jay.saputratmb",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Najla Nursyifa",
            "nim": "124450051",
            "umur": "20",
            "asal": "Aceh",
            "alamat": "Belwis",
            "hobbi": "Nonton ASMR",
            "sosmed": "@njlanursyifa",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Rozak Ramdani",
            "nim": "124450100",
            "umur": "18",
            "asal": "Lampung Selatan",
            "alamat": "Korpri Raya",
            "hobbi": "Isengin Harvin di kelas",
            "sosmed": "@rozakramdani__",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Teresa Christiani Purba",
            "nim": "124450046",
            "umur": "19",
            "asal": "Riau",
            "alamat": "Belwis",
            "hobbi": "Masak",
            "sosmed": "@christiani8872",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=1CzlywM4FoisbnlB_MC2jShBWbypLVqNe",
            "https://drive.google.com/uc?export=view&id=1LDgQQXhtg8Mc7vfiE_tNpG9fUVArEq9C",
            "https://drive.google.com/uc?export=view&id=1i4dKfBqIV6D1fUymtAWQHFJaqzW0ZT6N",
            "https://drive.google.com/uc?export=view&id=1J4AGVndTY_BopYy94ahDf-74RuAy1Xkh",
            "https://drive.google.com/uc?export=view&id=1R1NpvxL2QREGXGfuR412OUEQapXCvGhd",
            "https://drive.google.com/uc?export=view&id=1hqcrAfcG2yoGO2b0ED6jrxbr-lptyiWC",
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
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Audina Fitria",
            "nim": "124450038",
            "umur": "20",
            "asal": "Sumatera Barat",
            "alamat": "Sukarame",
            "hobbi": "Main ke air terjun",
            "sosmed": "@audinaf_03",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Cika Adelia Br Marbun",
            "nim": "124450107",
            "umur": "20",
            "asal": "Pekanbaru, Riau",
            "alamat": "Belwis",
            "hobbi": "Dengerin lagu",
            "sosmed": "@cikamrbn",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kak"
            },
            {
            "nama": "Gustin Haleluya Tampubolon",
            "nim": "124450068",
            "umur": "21",
            "asal": "Toba, Sumatera Utara",
            "alamat": "Airan",
            "hobbi": "Nonton",
            "sosmed": "@gustinhaleluya",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kak"
            },
            {
            "nama": "Muhammad Harvinsyah",
            "nim": "124450128",
            "umur": "20",
            "asal": "Sumatera Selatan",
            "alamat": "Belwis",
            "hobbi": "Beburu ayam hutan",
            "sosmed": "@muhvinz_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Rafa Sabina Fahimah",
            "nim": "124450036",
            "umur": "20",
            "asal": "Natar",
            "alamat": "Natar",
            "hobbi": "Nginep di rumah Yollanda",
            "sosmed": "@snasaa",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
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
            "hobbi": "jualan risol",
            "sosmed": "@ihsan.myusuf",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)
            
        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1VgcweaEm_FOHsry3L35EI1jzE5TXcoeF",
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
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kak"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1nbtG_1jK7Jqzh1H16YSNbYFBunHtKvwc",
            "https://drive.google.com/uc?export=view&id=1Hi_5tvUENkU3p8gHDGR1ZkTN_5ADKF2J",
            "https://drive.google.com/uc?export=view&id=1_QlBNJiu10XT8HxDWYVRoFr7S95T1_w4",
            "https://drive.google.com/uc?export=view&id=1_RhbZ1XITJ4-wdlIFKmuGQ_uCaAPIe_E",
            "https://drive.google.com/uc?export=view&id=1MH_NrlYDN6FcxomlqmB9CBsGJJgaV9-I",
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
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Hasan Nur Ramadhan",
            "nim": "124450013",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Korpri",
            "hobbi": "Coding",
            "sosmed": "@hasan.ramadhan08",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Layina Ropiqo",
            "nim": "124450016",
            "umur": "19",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Nonton Dracin",
            "sosmed": "@lay.inr_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            {
            "nama": "Mochammad Iqbal Az-Zahir",
            "nim": "124450052",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Natar",
            "hobbi": "Nonton drakor",
            "sosmed": "@iqbalazzahir_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Talitha Justine",
            "nim": "124450076",
            "umur": "19",
            "asal": "Jakarta",
            "alamat": "Pemda",
            "hobbi": "Nonton",
            "sosmed": "-",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1nbtG_1jK7Jqzh1H16YSNbYFBunHtKvwc",
            "https://drive.google.com/uc?export=view&id=1YFshJlT7D7patOdDFp0JyU2yPCYa8zrE",
            "https://drive.google.com/uc?export=view&id=1kV9ahlwDUQUcsS1CDle6Z6_pFKwp5wik",
            "https://drive.google.com/uc?export=view&id=11eveYhnpHEcAPcCwXoURj_nvbJyUXDla",
            "https://drive.google.com/uc?export=view&id=1fe9zZMbpXUXkdJKmyc5MJCabqMVC1Fcw",
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
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            {
            "nama": "Abdillah Fikri Al pome",
            "nim": "123450062",
            "umur": "21",
            "asal": "Baturaja, Sumatera Selatan",
            "alamat": "Belakang PB",
            "hobbi": "Olahraga",
            "sosmed": "@pomest__",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Afdhal Rahmad Setiawan",
            "nim": "124450008",
            "umur": "20",
            "asal": "Sumatera Barat",
            "alamat": "Belwis",
            "hobbi": "Fishing",
            "sosmed": "@dhal_setiawan",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus banggg"
            },
            {
            "nama": "Anggun Nita",
            "nim": "124450009",
            "umur": "20",
            "asal": "Lampung Utara",
            "alamat": "Belwis",
            "hobbi": "Nonton Kartun",
            "sosmed": "@anggunnitaaa_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
            },
            {
            "nama": "Della Anisa Fitri",
            "nim": "124450095",
            "umur": "17",
            "asal": "Lampung Timur",
            "alamat": "Kota Baru",
            "hobbi": "Berdandan",
            "sosmed": "@dellaansaftr",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakkk"
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
            "https://drive.google.com/uc?export=view&id=1zG0mnwqLUsndMcOJ-mHXW93poVhd2Zrd",
            ]
            data_list_Kadep_medkraf = [
            {
            "nama": "Nayla Salsabila Fathianisa",
            "nim": "123450082",
            "umur": "20",
            "asal": "Payakumbuh, Sumatera Barat",
            "alamat": "Way Huwi",
            "hobbi": "Mendengarkan Musik",
            "sosmed": "@naylasalsabilaa._",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1CXkNVje18wp1E6NujokW6SIkgTV-8fb4",
            ]
            data_list_sekdep_medkraf = [
            {
            "nama": "Donna Maya Puspita",
            "nim": "123450028",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Huwi",
            "hobbi": "Listening to music",
            "sosmed": "@donnamaya.p",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1deLZkPCCb3mB-gxYqvwHyQyyPXVPv9Rq",
            "https://drive.google.com/uc?export=view&id=1P0pMhYZgnZwPxURB6LX92RsLfpYDwIkc",
            "https://drive.google.com/uc?export=view&id=18MJRsS_yBSAzqmWPIh4M6h96QR9GZ0e1",
            "https://drive.google.com/uc?export=view&id=1GNTkKjWa7Y3-2G1XsXHxZe-G47Wi6l_A",
            ]
            data_list_Divisi_dokumentasi = [
            {
            "nama": "Labo John Noel Napitupulu",
            "nim": "123450037",
            "umur": "20",
            "asal": "Medan, Jakut, Palembang",
            "alamat": "Belwis",
            "hobbi": "Motoran",
            "sosmed": "@noerruuu",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Anash Tasya Ausyaqila",
            "nim": "124450050",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Way Halim",
            "hobbi": "Nonton",
            "sosmed": "@anshtsyaaql",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Felisya Nabila Nugroho",
            "nim": "124450104",
            "umur": "19",
            "asal": "Lampung Timur",
            "alamat": "Kota Baru",
            "hobbi": "Mancing emosi",
            "sosmed": "@felisyanbl",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Muhammad Razan Maulana Pratama",
            "nim": "124450031",
            "umur": "21",
            "asal": "Jawa Barat",
            "alamat": "Korpri",
            "hobbi": "Poto orang",
            "sosmed": "@muh_razan_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1bMv7Osx12FyzLL0VDK11Br65tWVHI8tB",
            "https://drive.google.com/uc?export=view&id=1RFmTo_N1IGIryqc-2MMOuNS6RI_pT43X",
            "https://drive.google.com/uc?export=view&id=1uWywpG2jyhTPP3H5rc20jbPcmFb_SWsz",
            "https://drive.google.com/uc?export=view&id=1OYEjcTrTWftCr62ZxFHMoKNv6BNf45iR",
            "https://drive.google.com/uc?export=view&id=1uWywpG2jyhTPP3H5rc20jbPcmFb_SWsz",
            "https://drive.google.com/uc?export=view&id=1qTrWtd_uC-5mpAzcBlF44M5RRDSDclSM",
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
            {
            "nama": "Sania Dwi Ayu Lestari",
            "nim": "124450086",
            "umur": "21",
            "asal": "Karawang",
            "alamat": "Airan Raya",
            "hobbi": "Nonton netflix",
            "sosmed": "@saniayyllstr",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk",
            },
           {
            "nama": "Allisha",
            "nim": "124450019",
            "umur": "16",
            "asal": "Kayangan",
            "alamat": "Heaven",
            "hobbi": "Mancing",
            "sosmed": "@aallishaa.a",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk",
            },
            {
            "nama": "Alya Ramadhanti",
            "nim": "124450091",
            "umur": "19",
            "asal": "Jambi",
            "alamat": "Airan",
            "hobbi": "Jalan jalan",
            "sosmed": "@alya.rmdhnti",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Bunga Clarisa Sefa",
            "nim": "20 ",
            "umur": "",
            "asal": "Lampung Selatan",
            "alamat": "Lampung Selatan",
            "hobbi": "Belajar",
            "sosmed": "@bungaclrssf",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Difanya Husakina",
            "nim": "124450043",
            "umur": "20",
            "asal": "Pagar Alam",
            "alamat": "Airan Raya",
            "hobbi": "Membaca Alquran",
            "sosmed": "@difanyhsa_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Nazlah Auliya",
            "nim": "124450054",
            "umur": "20",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Berenang",
            "sosmed": "@nzlhauly_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1Pej1chcJU40ZlAPZ8xDxxs3d4ujH5-zY",
            "https://drive.google.com/uc?export=view&id=15Lwu-_KkXR6zF1ZMh2LsXFS7XAz_DBVF",
            "https://drive.google.com/uc?export=view&id=1RZV454S_IpTykKKVe9nBNkvBvH8MYkzQ",
            "https://drive.google.com/uc?export=view&id=1x-7ZkdvpvQBcxB8AmO_lRhOFkjLEGsT7",
            "https://drive.google.com/uc?export=view&id=1WtcX03vQv9IxzsoUGcKWSwL7TUQhe6DB",
            "https://drive.google.com/uc?export=view&id=1m4HjYszig5AUUk2zsjww_2WPBCQcvUyp",
            ]
            data_list_Divisi_Visual_Design = [
            {
            "nama": "Raihana Adelia Putri",
            "nim": "123450041",
            "umur": "20",
            "asal": "Lampung Tengah",
            "alamat": "Aira Raya 1",
            "hobbi": "Menulis, membaca",
            "sosmed": "@n1tg._",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Daffa Kharisma Adzana",
            "nim": "124450061",
            "umur": "21",
            "asal": "Surabaya",
            "alamat": "Sukarame",
            "hobbi": "-",
            "sosmed": "@daffascript",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Edsel Adya Pradipta",
            "nim": "124450098",
            "umur": "20",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobbi": "Nonton Anime",
            "sosmed": "@edsel_0712",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus bangg"
            },
            {
            "nama": "Lucia Advencia Rachel Nainggolan",
            "nim": "124450085",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobbi": "Tidur",
            "sosmed": "@luciarachel_",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Shafa Delaila Azzahra",
            "nim": "124450124",
            "umur": "20",
            "asal": "Lampung Tengah",
            "alamat": "Perum Pemda",
            "hobbi": "Melukis dan menulis",
            "sosmed": "@_shaazzh",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            {
            "nama": "Zannuba Arifah Ilman",
            "nim": "124450112",
            "umur": "18",
            "asal": "Lampung Timur",
            "alamat": "Bengong",
            "hobbi": "@xifasky",
            "sosmed": "Rajabasa",
            "kesan": "kakak tingkat yang asik, baik dan ramah",  
            "pesan": "semangat terus kakk"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()
