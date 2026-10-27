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
            "https://drive.google.com/uc?export=view&id=14VNqTqu-26uuqY90BcDKQ3yGC5P_6GWV",
            "https://drive.google.com/uc?export=view&id=1Ta3xp-gx50zUjKvOxudovrvY0jkXslr8",
            "https://drive.google.com/uc?export=view&id=1z0_usfqOKi66hvxHrL7AMI2moRNIcb1w",
            "https://drive.google.com/uc?export=view&id=1MV-5Uhc5okjjL1nXfygPUCu99Jfe-pvS",
            "https://drive.google.com/uc?export=view&id=1Cz2rtO-3Yo-UO7FafWyu3gcd76GLuyUa",
            "https://drive.google.com/uc?export=view&id=1MXoA1YZBKdh967DhJaKrmjoY8y8F-9u_",
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
                "kesan": "Abangnya keren banget, baik juga ramah, asyik klo dia ajak ngobrol.",  
                "pesan": "Semangat terus ya bang dan pantang menyerah!"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangny seru banget, baikdan juga ramah, keren juga abangnya",  
                "pesan": "Terus semangat ya bang dan sukses selalu."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya cantikkk manis jugaa, suka deh kalo ngeliat kakaknya.",  
                "pesan": "Semangat terus ya kak dan pantang menyerah, sukses selalu."
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "AAbangnya asyik kalo diajak ngobrol, baik juga dan ramah.",  
                "pesan": "Pantang menyerah dan tetap semangat ya bang"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakakmya baikk dan ramah, cantikk juga terus imutt.e",  
                "pesan": "Semangat ya kak menghadapi perkuliahan san tugas tugas, sukses selalu"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya cantik dan baik, terus imut juga ramah lagi",  
                "pesan": "Suskes selalu ya kak semoga nilai A terus."
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
            "https://drive.google.com/uc?export=view&id=1Em4MGBTIYNZO7fzu_kwhkTSTdnZdH0Dk",
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
                "kesan": "Kakaknya kerenn, baikk ramah juga, maniss suka deh.",  
                "pesan": "Semangat terus ya kak dan pantang menyerah menghadapi tantangan."# 1
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)

        with tab2:
            gambar_urls_biro_aspirasi= [
            "https://drive.google.com/uc?export=view&id=1K-Cno2hj9cE2Yhyvu7GFlRvyfd8C7NsW",
            "https://drive.google.com/uc?export=view&id=1euYqbAl3DVwJQK_oEJIy0sVSaSytdLpW",
            "https://drive.google.com/uc?export=view&id=1Qg7bifTk-kcHeCcURt2b84EpPquLPU07",
            "https://drive.google.com/uc?export=view&id=1G7fW0VyhnyRtT3r3-e6G5yI4CTXcKrh-",    
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
                "kesan": "Abangnya ramah banget,baikk lucuuu kalo diajak ngobrol nyambung.",  
                "pesan":"Tetap semangat ya bang menghadapi perkuliahan."# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Abangnya seruuu, baikk lagi dan ramahh, jokesnya masuk lagi.",  
                "pesan":"Semangat terus ya bang dan semoga sukses selalu."# 1
            },
            {
                 "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya cantik, manis lagi, baik juga dan ramah banget.",  
                "pesan":"Semangat terus ya kakk dan sukses selalu."# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya kalem, baikk dan juga ramah, seru jugaa.",  
                "pesan":"Sukses selalu ya bang dan pantang menyerah."# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)

        with tab3:
            gambar_urls_biro_kajian= [
            "https://drive.google.com/uc?export=view&id=15FGtq2iFRKpp-Ivp3XFrv9t1iiTm3fSz",
            "https://drive.google.com/uc?export=view&id=1lObpNmkM9-mWiE208nZxEPeoRRy2c9vJ",
            "https://drive.google.com/uc?export=view&id=1VyGvytHLnudYUCUuXv4LEKJqjDiHVSa2",
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
                "kesan": "Kakaknya baikk ramah jugaa, imut banget dehh sukaa.",  
                "pesan":"Tetap semangat ya kakkk semoga suskes selalu dan pantang menyerah."# 1
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakaknya cantik banget, ramah dan baik jugaa, asyik juga orangnya.",  
                "pesan":"Terus semangat ya kak untuk menghadapi setiap rintangan."# 1
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Abangnya baik dan ramah, manis jugaa. Asyik orangnya.",  
                "pesan":"Terus semangat ya bang dan pantang menyerah."# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)

        with tab4:
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1SFElZnpJ90vValrC_m3V-0H1ShWWQXlO",
            "https://drive.google.com/uc?export=view&id=1Hg6FSGKsbrRwsr_1c10w45zwnbjXhQGY",
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
                "kesan": "Kakaknya imut banget dan baik jugaa, ramah dan cantik.",  
                "pesan":"Tetap semangat ya kakk menghadapi perkuliahan dan semoga nilainya A terus"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakaknya kalem, baikkk dan ramah, suka mehliat kakakny imut.",  
                "pesan":"Semangat terus ya kak menghadapi tugas yang banyak."# 1
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
            "https://drive.google.com/uc?export=view&id=1v5A7ia0uj2oSfyGe-iXQp6qwks4sO9La",
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
            "kesan": "Abangnya manis kalo senyum, baik jugaa seru lagi kalo diajak ngobrol.",  
            "pesan": "Semangat terus bang menghadapi tugas dan perkuliahan."
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1ARIbcIrMbunUKOzWOnw3OKHA9ePZ9PxU",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "Kakaknya cantikkk imutt lucu lagi, asyik banget klo diajak ngobrol.",  
            "pesan": "Pantang menyerah ya kak dan tetap semangat kuliahnya."
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1_6bLgzknjuyKSwDWUKxOGKtikusM2ZNC",
            "https://drive.google.com/uc?export=view&id=1jnVbGfOfCFt2612QACjrriJApszvVJi1",
            "https://drive.google.com/uc?export=view&id=15ZSbRmEL7qafcGRCUmXwZcRiUdSZlmYI",
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
            "kesan": "Abangnya kalem bawaanya tuh adem ayem gitu, baik jugaaa ramah.",  
            "pesan": "Semangat terus ya bang mengejar prestasi dan kuliahnya."
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "Abangnya baik, ramah lagii asyik juga kalo diajak ngobrol.",  
            "pesan": "Semangat ya bang menghadapi perkuliahan."
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "Kakaknya manisss banget, cantikk baikk jugaa.",  
            "pesan": "Terus semangat ya kakkk dan pantang menyerah."
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1-f8unCeK2nz9gjDnDaXukwJ62a7efCu4",
                "https://drive.google.com/uc?export=view&id=14G37ZoseSQSrdRO0V1EFsvKZZ9v1i3Vx",
                "https://drive.google.com/uc?export=view&id=1C4uGnjB2yYO3rcqp19YYN59nxqxeceJd",
                "https://drive.google.com/uc?export=view&id=193T_kJHoSHLbfqO3iK2T_862U-tXUuWI",
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
            "kesan": "Abangnya manis apalagi pas senyum ada lesung pipinya, baik jugaa ramah lagi.",  
            "pesan": "Semangat terus ya banggg buat kuliahnya."
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "Kakaknya cantikkk lucu ramah diajak ngobrol seruu.",  
            "pesan": "Tetap semangat ya kak semoga sukses selalu."
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "Kakaknya cantik, imut bangett senyunya manis jadi meleleh.",  
            "pesan": "Semangat terus ya kakk kuliahnya dan pantang menyerah."
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "Abangnya baik banget, ramah jugaaa, seru kalo diajak ngobrol.",  
            "pesan": "Pantang menyerah bang dan terus semangat."
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=1MT2yBv-krIrhU_Y6YQ8EBZVWQT1R56q5",
                "https://drive.google.com/uc?export=view&id=1p9Pou9nOByXLjRf9Zv4ez66zrEbtlOu9",
                "https://drive.google.com/uc?export=view&id=177nv6cCAhX05xgXivRPuLqpBhA5IUx1_",
                "https://drive.google.com/uc?export=view&id=19dDEqcDyPJuuBebLrUxQ8QInavo1KKFl",
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
            "kesan": "Kakaknya lucuu, maniss baik jugaa, imut lagi.",  
            "pesan": "Tetap semangat kak menghadapi perkuliahan."
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "Abangnya asyik banget, jokesnya dapet banget, klo ngobrol nyambung, baik dan ramah.",  
            "pesan": "Semangat terus ya bang buat kuliah dan mencapai keinginan."
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "Kakaknya manis kalo senyum tambah manis, ramahh juga baik.",  
            "pesan": "Tetap semangat ya kak dan pantang menyerah."
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "Kakakmya imut banget, cantikkk baik, kalemm adem ayem.",  
            "pesan": "Semangat terus ya kak semoga sukses selalu."
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
            "https://drive.google.com/uc?export=view&id=1RpAwwJ0w3y8etjyxEqmhA_K6427ktq2v",
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
            "kesan": "abangnya seru, terus baik sama ramah juga, cuman kemarin sedikit ngobrol sama abangnya.",
            "pesan": "Semangat terus bang dan terima kasih sudah meluangkan waktu saat wawancara"# 1
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)


        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1veN_EzyGYOD9qPBUFVl4cslBQF-Pe8vN",]
            data_list_sekretaris_departemen_minbak = [ 
            {
            "nama": "Gusti Putu Ferazka Dhiyamika",
            "nim": "123450046",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Dadi",
            "hobbi": "Mendaki",
            "sosmed": "@ferazkaa",
            "kesan": "Kakaknya baik banget, cantik juga imut, kayak ada jepang jepangnya gitu.",
            "pesan": "Makasih kak buang waktu luangnya dan tetap semangat ya kak menjalani perkuliahan."# 1            
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)            

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [            
            "https://drive.google.com/uc?export=view&id=1BCniVaHlMy3yxm45bevJJdOTE7bbQN_0",
            "https://drive.google.com/uc?export=view&id=1Qym3X4XS2EDI_sjpz80elUnfw466vAkQ",
            "https://drive.google.com/uc?export=view&id=1UOcN5rYhJICrDnZ5rOcw3cMMq1Jm9CPL",
            "https://drive.google.com/uc?export=view&id=1Nh7PbLjDCb26so_qmPjiP1vpsytvmJ41",
            "https://drive.google.com/uc?export=view&id=1SHar-RCHALI4skHEVZismD6PIZvhScCW",
            "https://drive.google.com/uc?export=view&id=1TFJcy-uG3wBw5K1-3TwqjCzR61yh-6ZU",
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
            "kesan": "Abangnya asyik, seru banget jokesnya masuk, pas kemarin ngobrolnya santai.",
            "pesan": "Tetap semangat ya bang kuliahnya dan pantang menyerah."# 1
            },
            {
            "nama": "Ayu Andriani Parlina Wati",
            "nim": "124450058",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Airan",
            "hobbi": "Belajar + menghitung uang",
            "sosmed": "@aayuandriani_",
            "kesan": "Kakaknya pas senyum manis, cantik lagi, kalem banget bawaanya adem kalo diliat.",
            "pesan": "Semangat terus kakkk dan pantang menyerah, semoga yang diinginkan tercapai."# 1
            },
            {
            "nama": "Dafa Elpriza",
            "nim": "124450131",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Kandis",
            "hobbi": "Jogging",
            "sosmed": "@dafaelpriza_",
            "kesan": "Abangnye seruu, ngobrolnya nyambung, sama asyik jugaaa.",
            "pesan": "Tetap semangat abang untuk mencapai apa yang dinginkan."# 1
            },
            {
            "nama": "Juwita Sari",
            "nim": "124450066",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Pemda",
            "hobbi": "Mancing",
            "sosmed": "@ju.juwitaaa_",
            "kesan": "Kakaknya manis sama imutt bawaannya adem ayem gitu.",
            "pesan": "Tetap semangat ya kakak menjalani hari dan perkuliahan."
            },
            {
            "nama": "Muhammad Afdal Luthfi",
            "nim": "124450047",
            "umur": "19",
            "asal": "Lampung Tengah",
            "alamat": "Jl. Pulau Damar",
            "hobbi": "Memantau dl tugas",
            "sosmed": "@afdall.03",
            "kesan": "Abangnya kalem banget, terlihat chill, baik abagnyaaa.",
            "pesan": "Semangat terus ya bang walaupun dunia sedang tidak baik baik saja."# 1
            },
            {
            "nama": "Salsabila Nazwa Putri",
            "nim": "124450002",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Korpri",
            "hobbi": "Nongkrong di kopken",
            "sosmed": "@slbnzw_",
            "kesan": "Kakaknya cantikk, baik jugaaaa terus ramahhh, lucu deh.",
            "pesan": "Pantang menyerah ya kak dan tetap semangat berkuliah walaupun tugas banyak."# 1
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
            "https://drive.google.com/uc?export=view&id=18LgYR3ZMaMSPTW3kkPjwprQoURVrCp7y",
            "https://drive.google.com/uc?export=view&id=1oLJsjm7CLUtOZrLq60eYny5FzsujqiZz",
            "https://drive.google.com/uc?export=view&id=1TDvhKeHRXtHB7VlSIrYq_58KtYQ6myem",
            "https://drive.google.com/uc?export=view&id=1_n3H3z-Nu2RVr9XTqeAHncXxEhWT3GGd",
            "https://drive.google.com/uc?export=view&id=1IErXOlQ2G-rP_qVtqniLZUSWVAiArYsF",
            "https://drive.google.com/uc?export=view&id=1C6S-7vdvX2vFnk8Nyl91WvHkoGQV1S99",
            "https://drive.google.com/uc?export=view&id=1AYZx-VsQYvuFwg1UmDeKy7Eb5_84WLzD",
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
            "kesan": "Abangnya seruu ramah jugaaa asyik lagi kalo diajak ngobroll.",
            "pesan": "Semangat terus kuliahnya bang."
            },
            {
            "nama": "Andra Ilham Bintang",
            "nim": "124450060",
            "umur": "18",
            "asal": "Sumatera Selatan",
            "alamat": "Kotabaru",
            "hobbi": "Main rubik",
            "sosmed": "@andra.lhm",
            "kesan": "Abangnya seru banget, asyik banget juga, jokesnya dapet banget, nyambung klo diajak ngobrol, sangat mengayomi anak anak kelompoknya, bestlah pokoknya. lop abang sekebon",
            "pesan": "Semangat terus banggg dengan perkuliahan dan tugas yang banyak. sehat sehat terus juga bangg"
            },
            {
            "nama": "Bryan Paskah Telaumbanua",
            "nim": "124450003",
            "umur": "20",
            "asal": "Nias",
            "alamat": "Belwis",
            "hobbi": "Live tiktok",
            "sosmed": "@bryantel_",
            "kesan": "Abangnya baik ramah juga terus asyik orangnya.",
            "pesan": "Semangat terus bang kuliahnya."
            },
            {
            "nama": "Ghiyats Thabularasa Meardhy",
            "nim": "124450067",
            "umur": "17",
            "asal": "Surabaya",
            "alamat": "Kemiling",
            "hobbi": "Nanem Sawit",
            "sosmed": "@meardhy_ghiyats",
            "kesan": "Baik abangnya, ramah.. seruuu nyambung klo jokes.",
            "pesan": "Tetap semangat ya bang selama kuliah."
            },
            {
            "nama": "Indah Julia Mawar Pratiwi",
            "nim": "124450055",
            "umur": "20",
            "asal": "Pringsewu",
            "alamat": "Airan",
            "hobbi": "Bengong",
            "sosmed": "@indahjuliaa",
            "kesan": "Kakaknya cantik.. manisss lucu lagii sukaa seru juga kalo diajak ngobrol.",
            "pesan": "Semangat terus kak dan pantang menyerah."
            },
            {
            "nama": "Jacinda Kesya Alvara",
            "nim": "124450023",
            "umur": "18",
            "asal": "Kalimantan Barat",
            "alamat": "Korpri",
            "hobbi": "Nyapu depan gacoan",
            "sosmed": "@cacalvra",
            "kesan": "Kakaknya asyikkk, cantik banget.. lucu lagii seru jugaa.",
            "pesan": "Semangat terus ya kak kuliahnya walau tugas seabrek."# 1
            },
            {
            "nama": "Muhammad Rafka Fatih Ghathfaan",
            "nim": "124450089",
            "umur": "20",
            "asal": "Padang",
            "alamat": "Kotabaru",
            "hobbi": "Bangun pagi",
            "sosmed": "@muhammdrafka_",
            "kesan": "Abangnya seruuu, baik lagi ramah jugaa jokesnya dapet.",
            "pesan": "Semangat ya bang menghadapi perkuliahan dan pantang menyerah."
            }
            ]
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)  

    Departemen_Minbak()       

elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Storage Sains Data</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
            "https://drive.google.com/uc?export=view&id=1lSMruRdm-udWfjMbG-2V9bObs8N_mAS3",
            ]
            data_list_Kadep_ssd = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan ta",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Abangnya baik, ramah juga obrolannya juga nyambung.",
                "pesan": "Semangat terus bang dan pantang menyerah.",
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1zQZ9P3a8wqYIvxv-Sw-F9F8aKxyUONN5",
            ]
            data_list_sekdep_ssd = [
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450000",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "Kakaknya imutt, baikkk dan ramah.. senyumnya manis lagi.",
                "pesan": "Terus semangat ya kak dan pantang menyerah.",
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=12pBy8QV8t71RsqjhXjCL-IUr2FoKvTz_",
            "https://drive.google.com/uc?export=view&id=1glu9hJpvVOBJIEdJ6DWBaim6Jgav_lZs",
            "https://drive.google.com/uc?export=view&id=19ho6-trZu4NteGQJFJY3J_WebARzJtJu",
            "https://drive.google.com/uc?export=view&id=1IL3N6LRwqxshMRbvECSpfbgYgbbLfZ7z",
            "https://drive.google.com/uc?export=view&id=1_DJ-jyonECyKDvgBLFigfv52APdHmSru",
            ]
            data_list_kemitraan = [
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "@fifah_zy",
                "kesan": "Kakaknya kalem, hawanya adem ayem gituu, baik juga ramah.",
                "pesan": "Semoga sukses selalu dan pantang menyerah ya kak.",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "@hasan.ramadan08",
                "kesan": "Abangnya asyik bangett, baik dan juga ramah lagi, ngobrolnya seru.",
                "pesan": "Sukses selalu bang dan tetap semangat ya.",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakaknya baik dan ramah, kalem jugaa, Manis lagi.",
                "pesan": "Terus semangat ya kak dan pantang menyerah.",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Abangnya kerenn, baik dan juga ramah suka deh, asyik jugaa.",
                "pesan": "Semangat terus ya bang semogas sukses selalu dan A selalu.",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakaknya imut, cantik jugaa baik dan ramahh.",
                "pesan": "Terus semangat ya kak menjalani hari dan perkuliahan.",
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1wfTO5JbMnS82ANvwTfXtLWasAWoEfHxa",
            "https://drive.google.com/uc?export=view&id=1KxIwQRILcUtSxYrtsEg0uebaMt6WylKr",
            "https://drive.google.com/uc?export=view&id=1oo8ex_syGXZT-kfFneewRQ4L0_Rcf2To",
            "https://drive.google.com/uc?export=view&id=1njbTawsWA3laqf-xSjs-zA3hZIx6Ulqc",
            "https://drive.google.com/uc?export=view&id=1XTcXnrM91liTd0VqmdmXc12_9r6xxC6A"
            ]
           
            data_list_kewirausahaan = [
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakaknya lucu, imut jugaa manis lagi, asyik juga orangnya.",
                "pesan": "Semangat terus ya kak menghadapi perkuliahan dan tugas tugas.",
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Abangnya seruu banget, baik juga ramah lagi, seru pokoknya.",
                "pesan": "Semoga sukses selalu dan nilai A selalu.",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Abangnya asyikk dan seruu, baik juga ramah juga.",
                "pesan": "Pantang menyerah ya bang dan sukses terus.",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "Belwis",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakaknya imut banget, cantikkk suka deh ngeliatnya, baik lagi.",
                "pesan": "Semangat terus kak dan sukses selalu."  
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakaknya cantik banget, imut deh.. sukaa baik dan ramah juga.",
                "pesan": "Sukses selalu ya kak dan tetap semangat menghadapi perkuliahan.",
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
            "https://drive.google.com/uc?export=view&id=126RxzYmpZ-sxOLQAFLx6yBfvrFrp1xS0",
            ]
            data_list_Kadep_medkraf = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kakaknya cantik, abik juga terus ramah lagi",
                "pesan":"tetap semangat berkuliahnya kakak dan pantang menyerah yaa"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1Ldg9NFGlWStiS7H98UkNRtZ_FFdkO86C",
            ]
            data_list_sekdep_medkraf = [
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "Kakaknya imut banget, baikk suka deh",
                "pesan": "pantang menyerah kkak dan tetap semnagat menjalani perkuliahan"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1IlKHxn0ndilezKy-NGtEguYH-VVC4vwg",
            "https://drive.google.com/uc?export=view&id=1Mv6-TZjxJppXwP6sXwmk71dqKI0HAuan",
            "https://drive.google.com/uc?export=view&id=17O9c6rrJ94eqDLoOmDkuOMKTr8MB7b2W",
            "https://drive.google.com/uc?export=view&id=1QN9JnhlpWuBdDz0U3gXiNCnX9vifYXl_",
            ]
            data_list_Divisi_dokumentasi = [
            {
                "nama": "Labo Napitupulu",
                "nim": "37",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Tong setan",
                "sosmed": "noerruuu",
                "kesan": "abangnya manis, ramah dan baik",
                "pesan": "Semangatt terus bangg kuliahnya dan pantang menyerah"
            },

            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "kakaknya mansi banget plus cantik, paket lengkap",
                "pesan": "jaga kesehatan kak walau terbantai matkul dan praktikum"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "felisyanbl__",
                "kesan": "Kakaknya imut,lucu juga",
                "pesan": "Jaga kesehatan selalu kakaa, semoga sukses selalu"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "muh_razan_",
                "kesan": "abangnya manis apalgi berkacamata",
                "pesan": "Semangattt terus banggg menghadapi perkuliahan"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1VjatoaLpRlh63Ev2Z7hxBG_wx0C7SK2h",
            "https://drive.google.com/uc?export=view&id=1XR3Uwa_wtMzJ-MSL2jRL0TGoJm2UgmJy",
            "https://drive.google.com/uc?export=view&id=1SUIsPH8frIqjEMXqLiSj83YTOMrffIe-",
            "https://drive.google.com/uc?export=view&id=1ZeL40SLbQAx_WdTe8ApG1eUzOxc4kUnn",
            "https://drive.google.com/uc?export=view&id=1nvcPUScrLlf4sDPS8suL4K5mHGqp2S8n",
            "https://drive.google.com/uc?export=view&id=15L2CC-2waaYMpsoPIfiJJgWTcAa9bnZl",
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan ruang prodi",
                "sosmed": "saniayyllstr",
                "kesan": "kakaknya imup bangettt",
                "pesan": "semoga dapet nilai A selalu ya kak"
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "kesan": "kakaknya manis bangettt, menawan sukaaa",
                "pesan": "Terus semangat ya kak kuliahnya dan pantang menyerah"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu roda",
                "sosmed": "alya.rmdhnti",
                "kesan": "kakaknya gemes banget,lucu",
                "pesan": "sukses selalu ya kak untuk kedepannya"
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "bungaclrssf",
                "kesan": "Ramah bangett, baikk, imut dan lucu",
                "pesan": "sehat sehat selalu ya kak, pantang menyerrah"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "difanyhsa_",
                "kesan": "imuppp ,gemassss",
                "pesan": "smenagat ya kak mengejar mimpi dan keinginananya"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "cantik banget,lucuuu dan baik",
                "pesan": "semnagat terus menjalani hari hari dan tugas yang menumpuk"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1u2RodHxM349O6JkXweZR4QBSZPagFJqR",
            "https://drive.google.com/uc?export=view&id=1Eg5QgplKVN47HfDjFLLIdAC4RMzQuivi",
            "https://drive.google.com/uc?export=view&id=1uRE_7xXxXBGrdezkNmGxU9lmVVa8B54V",
            "https://drive.google.com/uc?export=view&id=1IWwIIXwpwAhSt7OMnqMhvlQmB2sUdcNL",
            "https://drive.google.com/uc?export=view&id=14UcEDgxBMEM6VO2afWmfux7QHAPf_-rg",
            "https://drive.google.com/uc?export=view&id=1jvc6u7lvhhA3G8sMjJYSSTPdCrrojlVt",
            ]
            data_list_Divisi_Visual_Design = [
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "kesan": "kakaknya baik terus ramah juga",
                "pesan": "Semoga apa yang diinginkan tercapai, semnagat kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Nyuluh manuk",
                "sosmed": "@daffascript_",
                "kesan": "abangnya manis, lucu juga terus baik dan rramah",
                "pesan": "Sehat selalu ya bang dan terus semnagat"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "edsel_0712",
                "kesan": "abangnya baik terus ramah juga",
                "pesan": "sehat sehat selalu abang terus semangat"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "luciarachel_",
                "kesan": "kacamata kakanya lucu banget ada warna kuningnya",
                "pesan": "semangat ya kak dan pantang menyerah"
                ""
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis, menulis",
                "sosmed": "@_shaazzh",
                "kesan": "Kakanya imut dan ramah",
                "pesan": "Semangatt terus kak, semoga selalu menddapat nilai A"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "Xifasky",
                "kesan": "baik dan ramahhh",
                "pesan": "Semangattt kaa untuk kuliah dan organisasinyaa!!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()

elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
            "https://drive.google.com/uc?export=view&id=1rg0ojvTocjxSwah_hUMmqhSHv-DJSorP",
            ]
            data_list_Kadep_internal = [
            {
                "nama": "Haikal Fransisko SImbolon",
                "nim": "123450106",
                "umur": "20",
                "asal":"Sidikalang",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "abangnya bak, lucu banget gk boong, suka bangets ama jokesnya nyambung",  
                "pesan":"Semangat terus ya bang untuk TA nya, semoga wisuda tepat waktu aamiin"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=1MeOIei-eNpxPWuPqaiNXCmS58OvN3Mw3",
            ]
            data_list_sekdep_internal = [
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Cantik, baikkk, imut bangettt kakaknya kalem suka deh",  
                "pesan":"sehat sehat terus jangan lupa jaga kesehatan untuk menghadapi TA"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=1cLKiZlCsl9Gda7q4gAb302AKxb5T2Vbj",
            "https://drive.google.com/uc?export=view&id=1j_mX-tZCDJ_Hx6o_xtEDtwEsdgZ5MgX2",
            "https://drive.google.com/uc?export=view&id=1dW6kQReeaQrm-kZ-wBqr-uQD0bq6JwXY",
            "https://drive.google.com/uc?export=view&id=19bbO1iaBCP1Ogz8kklXYDbpy0BtShpi0",
            "https://drive.google.com/uc?export=view&id=1JN6oOBh1Kf1-7qVD6wohshkl1kR4yHs7",
            "https://drive.google.com/uc?export=view&id=19L5le9i7JVTYwos0NB6eOhlc_uGvXPFW",
            "https://drive.google.com/uc?export=view&id=13A8ub7n_7KNKrsc559d5m0yAuzKAJlc7",
            "https://drive.google.com/uc?export=view&id=1LPvjZzf8X-A0D_3mWXoWm3-yC39XsFM-",
            ]
            data_list_keharmonisasian = [
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpa ITERA",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "kakanya seru buangeeettt, sangat membaur and i like it so much",  
                "pesan": "Semangat selalu ya kakak untuk menghadapi perkuliahan dan tugas yang menumpuk"# 1
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhnghnii",
                "kesan": "abangnya keren bangettt,a baik lagiiii",  
                "pesan":"Sehat selalu ya bangg dan pantang menyerah!"# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Menulis wishlist",
                "sosmed": "@aisyahkhair",
                "kesan": "Kakanya seru bangettt, asyikkk dehh cantik lagi ramah pula",  
                "pesan":"Sehat selalu ya kak semoga selalu dapat nilai A aamiin"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap Liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "kakaknya baik banget ramahhhh, imutt buangett",  
                "pesan":"Sehat selalu kak dan semangat kuliahnyaa"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal": "Kisaran City",
                "alamat": "Pemda",
                "hobbi": "Kick Boxing",
                "sosmed": "@jay.saputratmb",
                "kesan": "abangnya sangat asyikkk, suangat seruu, lucu lagi , baik and ramah",  
                "pesan": "Semangatt kuliahnya bangg dan jaga kesehatana ya perjalanan masih panjang"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Nonton ASMR",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya tuh vibesnya kalem dan sdem, senyum juga manis",  
                "pesan":"Semangatt terus ka kuliahnyaa"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin Harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Abang bsikkk dan ramah terus lucyuuu",  
                "pesan":"Semangatt bang menjalani perkuliahan dan sehat selalu"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan" : "kakanya imuttt suka deh,my tutorrr",  
                "pesan":"semangat terus ya kak jadi astut LMD semoga ilmunya selalu bermanfaat"# 1
            },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=1GDfEIFoniGRGQc4k9JaIdAdF3IFYto6d",
            "https://drive.google.com/uc?export=view&id=15mdlgxX8_ysho5T1twAJeO4nUvNqZPBp",
            "https://drive.google.com/uc?export=view&id=1h13qfiKNziTEhC57Mb0ZQNIjh1l4eo9K",
            "https://drive.google.com/uc?export=view&id=1KYnTqQ-fRuQKjrpL45pk9MF3g38mz599",
            "https://drive.google.com/uc?export=view&id=1GGspIurot-wMWyWKB4IV4sqiSNy7LhCJ",
            "https://drive.google.com/uc?export=view&id=1Ps51sbIUnKCBV3NrchHOk3k9F1EbfUMD",
            ]
           
            data_list_kerohanian = [
            {
                "nama": "Muhammad Hanif Dzaky Arifi",
                "nim": "124450064",
                "umur": "21",
                "asal": "Sumatera Barat",
                "alamat": "Way Kandis",
                "hobbi": "Nonton Film",
                "sosmed": "@hnfdzky_",
                "kesan": "Abangnya ramah, seruuu tapi juga kalemm",  
                "pesan":"Semangattt bang kuliahnyaa dan pantang menyerah ya"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Baik dan ramah,kalem positive vibesss",  
                "pesan":"Sehat selalu dan semangat kuliahnya kakk!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "@cikamrbn",
                "kesan": "Baik dan lucuu, imuttt gemesss deh",  
                "pesan":"Sehat selalu ya kak meski tugas membantai"# 1
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakanya baik ramah juga jadi suka deh",  
                "pesan":"terus semnagat untuk meraih cita cita"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "@muhvinz_",
                "kesan": "abangnyaa terlihat kalemm dan adem, i like it",  
                "pesan":"Semangattt kuliahnya yaa bangg, pantang menyerah"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nginep di rumah Yollanda",
                "sosmed": "@snasaa._",
                "kesan": "suka banget ama vibes kakanya yang adem ayem dan kalem ini, lop",  
                "pesan":"Semangat terus ya kakakkk, jangan mudah menyerah"# 1
            },
        ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
    internal()

elif menu == "Departemen Eksternal":
    def eksternal():
        st.markdown("<h3 style='text-align: center;'>Departemen Eksternal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Hubungan Luar", "Divisi Pengabdian Masyarakat"])

        with tab1:
            gambar_urls_Kadep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1TyL-R2TilDYe5HGkv_0dMQnWtGlhUzea",
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
                "jabatan": "Kepala Departemen",
                "kesan": "Kakaknya tuh vibesnya idependent women, sukaaa",
                "pesan": "sehat sehat ya kak tetap semangat"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1eiXPCmRegfWdOdn_ZiFAAKmKNvPxWztS",
            ]
            data_list_sekdep_eksternal = [
	        {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Jalan lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "jabatan": "Sekretaris",
                "kesan": "kakaknya tuh imoet cantik and menggemaskan",
                "pesan": "tetap semnagat dan terus jalanni perkuliahan"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [            
            "https://drive.google.com/uc?export=view&id=1J0hffXytwuq-6cNTTV4SXU4n9cN4XIjZ",
            "https://drive.google.com/uc?export=view&id=1PGKIMQDX6Rjr1PY4VACFvaT8Dqf7r6S3",
            "https://drive.google.com/uc?export=view&id=1x4ubhiEXWFHOpeHWNbxbW-Jmiv1vmzv2",
            "https://drive.google.com/uc?export=view&id=1cYTGhUdb7CZ1gYouvxDVCYpmIDBpsLp_",
            "https://drive.google.com/uc?export=view&id=1bAo7KKETlPuqhtA-mhDWU0zwG857q9ia",
            "https://drive.google.com/uc?export=view&id=1qY-3LL4DmQWKBiYEg3IhNikmS9myWtQ4",
            "https://drive.google.com/uc?export=view&id=15eWuNyHjqCG2SrxaW3exLYUUypOo3TUU",
            "https://drive.google.com/uc?export=view&id=19XINEUvV6Uvu2qYf9gZTXleW5RAbUDUh",
            "https://drive.google.com/uc?export=view&id=1kedEThxxxvScme-l04w0fwrs-gy0dSnc",
            "https://drive.google.com/uc?export=view&id=1Mac40xGGmcfGCEyAgCfdpGkgaVi1dIel",
            ]
            data_list_hubungan_luar = [
            {
                "nama": "Khoirul Muttoharoh",
                "nim": "123450021",
                "umur": "21",
                "asal": "Lampung barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "kakaknya imut",
                "pesan": "Sehat selalu ya kak agar bisa menjalani perkuliahan dengan baik"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "abangnya keren bangettt, manis jugaaa",
                "pesan": "terus semanagt ya menghadapi perkuliahan dan tugas yang suka menumpuk"
            },
	        {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Sukabumi",
                "hobbi": "Mancing",
                "sosmed": "@khaindaa_",
                "kesan": "Kakanya imut dan cantik",
                "pesan": "sehat selalu dan semangatt kuliahnyaa!"
            },
	 {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "-",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "abangnya keren dan baik",
                "pesan": "Semangat terus bang kuliahnyaa"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfayabiyi",
                "kesan": "abangnya baik dan ramah",
                "pesan": "Semangattt bang kuliahnyaa dan pantang menyerah"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton Film",
                "sosmed": "@asemeilani",
                "kesan": "imut dan cantik kakanyaa",
                "pesan": "Sukses selalu kak dan selalu mendapat nilai A!!"
            },
	        {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Kerennn dan ramah abangnya",
                "pesan": "Semangatt terus ya bangg kuliahnya meski bbanyak tugas"
            },
	        {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing",
                "sosmed": "@khaindaa_",
                "kesan": "Baik dan ramah juga kakaknya",
                "pesan": "sehat selalu dan selalu sukses ya kak"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Gemass, imup dan lucyuuu",
                "pesan": "Jaga kesehatan ya kaadan pantang menyerah"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Jati Agung",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "kakaknya baik banget dan juga ramah",
                "pesan":"semangat terus menjalani perkuliahan dan kepanitiaan ya kaakkk"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
        "https://drive.google.com/uc?export=view&id=1ZGZ89VCy0Mxx7qRVImtso38Rhp79KQmZ",
            "https://drive.google.com/uc?export=view&id=1Px7fGOd5MEo7HQfK4UQPXEpY6Yu9I3ry",
            "https://drive.google.com/uc?export=view&id=1gcRw0G6IiDqMDQC6mlY36KNdvaqMUbn0",
            "https://drive.google.com/uc?export=view&id=1JhhLYObO-T_8uZLVQJ3ZeaRMWTurnvcf",
            "https://drive.google.com/uc?export=view&id=1kF1oBkqkXZ5xyoHlORXvOw7qqojgWHwE",
            "https://drive.google.com/uc?export=view&id=1ePJMh1_PkZqgGoHeH81JgNBhgRlVA5ky",
            "https://drive.google.com/uc?export=view&id=1CkIlVGWsI8hKZ6iqwDBebCtADX1ojZEu",
            "https://drive.google.com/uc?export=view&id=1mREVXSOrJzzLSZ0X3ysuh3uRb51X6QGb",
            "https://drive.google.com/uc?export=view&id=1WEtd-4xeX4GNVeUAXdg_LwgRnuu_pq5k",
            "https://drive.google.com/uc?export=view&id=1Y74xEtVti2YFokIK0BgriqfvuIO0VEAr",
            ]
           
            data_list_pengabdian_masyarakat = [
	        {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "22",
                "asal": "Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Baik, ramah juga terus seru",
                "pesan": "terus semnagat ya bang menjalani perkuliahan"
            },
	        {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "Kakanya manis dan imut",
                "pesan": "Jaga kesehatan ya kaa, dan terus semangat"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "Manis dan imuuutt",
                "pesan": "Sukses selalu ya kak untuk kedepannya"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal": "Sini",
                "alamat": "Jauh pokoknya",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "kakanya baik dan juga ramah",
                "pesan": "sehat selalu ya kak janganlupa jaga kesehatan"
            },
	        {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "19",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "abangnya keren dan baik juga",
                "pesan": "Semangat kuliahnya dan jaga kesehatannya bangg!"
            },
	        {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "19",
                "asal": "Swiss",
                "alamat": "Main Game",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "abangnya maniss terus lucu juga",
                "pesan": "semangatt menjalani perkuliahannya ya"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "20",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "Abangnya keren banget terus manis apalagi pas senyum",
                "pesan": "semangat terus ya bang meski tugas selalu numpuk"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "main layangan waktu ujan",
                "sosmed": "@jaldii._",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "abangnya sanagt keren dan juga ramah",
                "pesan": "sehat sehat ya bang dan terus semangat"
            },
	        {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "...",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "Kakanya imut, ramah dan cantik",
                "pesan": "semoga selalu dapat nniali A"
            },
	        {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "divisi" : "Pengabdian Masyarakat",
                "jabatan": "Anggota",
                "kesan": "vibes kakanya kalem dan cantikk",
                "pesan": "semangat ya kak dan pantang menyerah, keep strong"
            },
        ]
            display_images_with_data(gambar_urls_pengabdian_masyarakat, data_list_pengabdian_masyarakat)
    eksternal()

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
            "https://drive.google.com/uc?export=view&id=1GDkYwqctdM_mG4lrSDi3X2g6peytSxYJ",
            ]
            data_list_Kadep_psda = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Dekat Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakanya cantik banget dan manis banget",  
                "pesan":"Ssemangat terus kakak untuk menjalani hari dan menghadapi TA"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1HX2R2msHFXD4uiiHdkxdlE7SATTM3lUB",
            ]
            data_list_sekdep_psda = [
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "kakaknya manis dan juga tegas",  
                "pesan":"Sehat selalu ya kak dan terus sukses"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/uc?export=view&id=1l-8EDawflSC88A2raU116qs6Axz-TdoQ",
            "https://drive.google.com/uc?export=view&id=1v_Qtir4NJ3zLF7T5k428ZaFsKnYZBErc",
            "https://drive.google.com/uc?export=view&id=1RQ7llpFjX1XlN6ME-3UlgeRbTjM-qDFB",
            "https://drive.google.com/uc?export=view&id=1qM4dU9IN4oY0LFLSWOi_08cHEAsh_XqD",
            "https://drive.google.com/uc?export=view&id=17k34dK8LFmgQOTU6420CB0ZHGw3YR0U5",
            "https://drive.google.com/uc?export=view&id=1P1w1L4CMrm2S8rkozbKI0IiUd8w_wTU2",
            "https://drive.google.com/uc?export=view&id=1ynq8snajigqVQWRZ6r0KjDjapWzyq6hS",
            "https://drive.google.com/uc?export=view&id=194eStma6NzdzqkNxHeFbD7l8DV5AaQES",
            ]
            data_list_Divisi_Kaderisasi = [
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "abangnya keren bsnget, penyampaian saat materi bagus banget",  
                "pesan": "terus semnagat ya bang dan semoga selalu diberi kemudhan dan kelancaran"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "abangnya tuh manis dan baik, stylish",  
                "pesan":"sukses selalu ya bang dan tetap semnagat"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "abangnya baik banget dan kelihatan tegas",  
                "pesan":"terus semangat ya bang menghadapi tugas tugas"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "abangnya tegas banget",  
                "pesan":"semangat terus ya bang untuk menjalankan perkuliahan"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "kakaknya baik ramah juga",  
                "pesan": "Semangat kuliahnyaa, walaupun semakin bertambah semester semakin bikin ga semangat #CRI, oh iya sama kaa kalau kaka lagi stress jangan dialihin emosinya ke orang lain ya.."# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "abangnya keren, asyik juga",  
                "pesan":"Sehat selaluvya bang agar selalu siap menghadapi tuugas yang buanyak"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Sabang",
                "alamat": "Nomaden",
                "hobbi": "Duduk samping Henry",
                "sosmed": "@putrimannaa",
                "kesan" : "kakanya cantik nan imut, gemass",  
                "pesan":"semoga selalu dapat nilai A ya kak dan yang terbaik"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "Kakanya manis banget apalgi pas senyum tapi kadang tatapannya tajam",  
                "pesan":"sehat sehat ya kak dan terus semnagat meski tugas selalu bbanyak"# 1
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1qvrhgacXDxIj1SlDO5FUHlqIeSyeeMBb",
            "https://drive.google.com/uc?export=view&id=13b3fCqmdRyfvB6T4yDE-a8TK5Qj6VT2D",
            "https://drive.google.com/uc?export=view&id=1g7wm67XpJ-kRI4gkJwdoH66Y5zv9QsJy",
            "https://drive.google.com/uc?export=view&id=1zAPGzymvBOw0gE0kiandOdcZFOWRgBed",
            "https://drive.google.com/uc?export=view&id=1gbVMXX2symHC1C4nqlGAhwviz9r6JNpo",
            "https://drive.google.com/uc?export=view&id=1DpWjVMasM5PP31QD3tODs56bapZCSJFz",
            "https://drive.google.com/uc?export=view&id=1tsl-4bBPEft4cTzYjkNAMK6QtL8XH86m",
            ]
            data_list_Divisi_Peningkatan_Mutu_Anggota = [
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "17",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Bermusik",
                "sosmed": "@desmannhal_",
                "kesan": "abangnya seruu dan asyikk",  
                "pesan":"Semoga lancar selalu TA nya ya bang dan wisuda tepat waktu"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "Kakanya cantik and imoettt",  
                "pesan":"Semoga kaka selalu sukses yaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakaknya baikkk dan jugaa ramah",  
                "pesan":"pantang menyerrah dan terus semangat kuliahnya kak"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "Abangnya lucu asyik jugaa",  
                "pesan":"Semangat kuliahnya bangg semoga selalu dapet A"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakanya lucyuuu dan ramah",  
                "pesan":"Jangan lupa jaga kesehatan dan semnangat kuliahnya kaa!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Tembung",
                "alamat": "Belwis Tengah",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "abangnya manis bangettt dan lucuuu",  
                "pesan":"Semangattt kuliahnya ya bangg dan sehat selalu"# 1
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "gemes bangett dan lucuu",  
                "pesan":"Sehat selalu yya kak dan dimudahkan segala urusannya"# 1
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
            "https://drive.google.com/uc?export=view&id=1cZ9Tag6vz9UrtIPrUg-NdpOJ1u7Dbngd",
            ]
            data_list_kepala_departemen_mikfes = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game & travel",
                "sosmed": "@biyokcb",
                "kesan": "abangnya keren bangett dan asyikk",
                "pesan": "Semangat terus ya bang dan pantang menyerah"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1_5k6e0PPGURuRtO6Gozt6G-sfHHRKjJ1",]
            data_list_sekretaris_mikfes = [ 
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "kakanya gemesss banget dan lucyuuuu",
                "pesan":"sehat selalu ya kak untuk menjalani kuliah dan TA"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1uGkiANIVrdlgp483TeMCyIJLUKLvPnu8",
            "https://drive.google.com/uc?export=view&id=1vPEfAV3rbUN3bqei2tGOBWDmJ337PPzI",
            "https://drive.google.com/uc?export=view&id=1HSBFN1x64xqcVgS7B604goY78BpOU6r-",
            "https://drive.google.com/uc?export=view&id=1iU8ir2PQEfOCcHU7oLlVzuQZqX7E5iOK",
            "https://drive.google.com/uc?export=view&id=1D97TZadKandGYpPCALxNFQ7kbEUS36jD",
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
                "kesan": "abangnya baikkkkk buangett, ramahhhh",
                "pesan" : "semoga semua amal perbuatan baik yang abang lakukan diterima disisi Allah SWT "
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "abangnya kerenn banget",
                "pesan": "terus semnagat ya bangg"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakaknya cantik banget",
                "pesan": "Kaka semangat terus ya kak kuliahnya"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "kakaknya imut dehh",
                "pesan": "sehat sehat ya kak dan tetap semnagat"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "kakaknya baik dan ramah banget",
                "pesan": "keep strong dan pantang menyerah"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Cantik dan imut bangett",
                "pesan": "Sukses selalu ya kak dan semoga selalu dapat A"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            "https://drive.google.com/uc?export=view&id=1lXPf4ItHAOEXM4qnYrPQjkTnMvhCCdn6",
            "https://drive.google.com/uc?export=view&id=11D-yF7-Kh6tgaEDspiwubdVd1sbBnQw5",
            "https://drive.google.com/uc?export=view&id=1Qo4FqRyWyOrk5Y41MC9mc9yCdSLr2Hn-",
            "https://drive.google.com/uc?export=view&id=1-0hrjUOqtnKFDnMVODU5xC1J6DJaTc8Q",
            "https://drive.google.com/uc?export=view&id=1m5IlKtILxSBb0xuGXnc1D9EU224tTVox",
            "https://drive.google.com/uc?export=view&id=1YZ2rOBkRE_Ae7v5RzN_mtmKaA8kc1BJS",
            ]
            data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            {
                "nama": "Akeyla Fairus Shafi",
                "nim": "123450119",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandara Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "abangnya manis, kalem dan baik",
                "pesan": "Semoga abang wisuda tepat waktu ya bang, semnagat"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "kakaknya asyik banget dan seru, ceriaaa",
                "pesan": "selalu semangat dan pantang menyerah ya kak"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kakaknya baik dan keliatan kalem adem ayem",
                "pesan": "semangat terus kak and keep strong"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Kakaknya baik dan ramah",
                "pesan": "Semangat terus ya kakak menjalani perkkuliahan"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abangnya baik dan kerenn deh",
                "pesan": "Sehat selalu ya bang dan sukses selalu"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "kakanya cantik,imut, lucu gemas, pokoknya pakeet lengkap",
                "pesan": "jaga kesehatan ya kak biar siap menghadapi perkuliahan"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_Divisi_Research_Development = [
            "https://drive.google.com/uc?export=view&id=1kky4LQhEcIXWYZPDxoL19t4qu2DyYNiz",
            "https://drive.google.com/uc?export=view&id=1FzXDTxENpUqNTXCp3fVQqHnoIbUUwhVV",
            "https://drive.google.com/uc?export=view&id=1WM7Bttv3W8QvC7l1z31Z6JCmS6bHY3T-",
            "https://drive.google.com/uc?export=view&id=1Fa1uQ-6PJKTnt6P8PD0YpErwahOALEW-",
            "https://drive.google.com/uc?export=view&id=1-q8mUFcz5_7O2rapbPRsEWl0rKNyuWYy",
            "https://drive.google.com/uc?export=view&id=1NdQvklyVsyBdMsP-IxRsHmeCnmdhgwBS",
            "https://drive.google.com/uc?export=view&id=13yE80oo4pB7nmzDIUuHYyt8cVh6I6mad",
            "https://drive.google.com/uc?export=view&id=1EfpM5qUNbAcUp-zMbdGik867uJjVobRH",
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
                "kesan": "abangnya keren dan ramah juga",
                "pesan": "Semangat terus ya bang untuk perkuliahanntya"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "kakanya kerenn banget dan ramah",
                "pesan": "pantang menyerah ya kak dan keep strong buat ngadapin segala ha"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya baik dan juga ramah",
                "pesan": "Semangatttt kuliahnya bangg dan sukses selalu"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "abangnya asyik dan juga ramahhh,kerennnn",
                "pesan": "tetap semnagat ya bang dan sukses terus untuk kedepannya"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "abangnya keren banget apalgi soal ngoding",
                "pesan": "semnagat terus bang ngodingnya dan sehat selalu ya bang"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "kakaknya imut dan menggemaskan banget",
                "pesan": "Semangatt terus ya kak kuliahnyaaa"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "abangnya keren keren banget dan asyik juga",
                "pesan": "sukses selalu ya bang, sehat selalu"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "abangnya baik dan asyikk banget",
                "pesan": "terus semangat ya bang dan pantang menyerah"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Research_Development, data_list_Divisi_Research_Development)
    mikfes()