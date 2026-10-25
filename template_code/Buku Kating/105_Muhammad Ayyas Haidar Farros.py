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
    st.markdown("<h3 style='text-align: center;'>Kesekjenan</h3>", unsafe_allow_html=True)
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cxDpeniK2M87cEpIT45yqjQvkElMe6a7",
            "https://drive.google.com/uc?export=view&id=1vNZXH7LXKIAnG06x-WLSqKiI6kfAY627",
            "https://drive.google.com/uc?export=view&id=1ByPKZIySgdkCgVuO4kJCDIEFen9rn8rN",
            "https://drive.google.com/uc?export=view&id=10PcUccRaqv7TBwy741J3tKESmN_t5mHn",
            "https://drive.google.com/uc?export=view&id=1SbEwgqguXv-syb4V0TjOrBQxnMaB9IZ3",
            "https://drive.google.com/uc?export=view&id=1NeTJV1qWfdcvmdibLWHn5tVHDPX1fogA",
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
                "kesan": "Abangnya keren, baek, ramah, dan berwibawa",  
                "pesan": "Terimakasih bang atas semua usahanya dan semangat untuk TA nya bang! "
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya ramah banget dan seru sekali",  
                "pesan": "Semangat terus bang buat kuliahnya dan untuk TA!"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi seru banget dan baikk",  
                "pesan": "Semangat terus ya kakakk"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "abangnya kalem dan kerenn",  
                "pesan": "Semangat bang semoga dilancarkan segala urusannya"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya seru dan asik sekalii",  
                "pesan": "Semangat selaluu ya kak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakaknya asikk ramah dan seruu",  
                "pesan": "Semangat terus kakak buat perkuliahannyaa"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

elif menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg= [
            "https://drive.google.com/uc?export=view&id=1rA3XxgRmWX3gbTlsXGKU5ZojB9cbC8oA",
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
            "kesan": "bang ridho orangnya asik banget gak canggung kalau ketemu",  
            "pesan": "semoga emyu bisa tsunami trophy ya bang GGMU"
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1OwYAoRPYZcSYcbWEjyHInRMDWkquiSVl",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "kakaknya baik ceria dan sangat ramahh sekalii",  
            "pesan": "semoga kakaknya ceria selalu setiap hari"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1LTiRz47gtHhlID-S24XSr9enzeswffKg",
            "https://drive.google.com/uc?export=view&id=1RciCC5iLuDMVe1HSeX69l18q86pm4zrW",
            "https://drive.google.com/uc?export=view&id=1w6xBbRMuIcxkYkLSF3wVtg-e5885VDCH",
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
            "kesan": "bang dharu orangnya seru dan banyak pengalaman",  
            "pesan": "semangat terus ya bang ngidupin api tiktoknya ehehe"
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "bang niko humble parah dan seru banget orangnya",  
            "pesan": "ati-ati bang nanti digigit musang pas COD wkwk"
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "kakaknya asik, seru banget pokoknya",  
            "pesan": "Info spot mancing gacor dong kak"
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1iIf0Mfe36HBL8KL3zrfY_B4TKthwlNXU",
            	"https://drive.google.com/uc?export=view&id=1nEDSFCiAbZrqmeXfJfVrwJUrmjUYW7ba",
            	"https://drive.google.com/uc?export=view&id=1l5qmdb2p0otZFEVkr4xgBGP_SMgoPBA_",
            	"https://drive.google.com/uc?export=view&id=1SYzRdbIeC9JWm3-YEIc7Rd-Bp7deOhxE",
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
            "kesan": "bang givaro ternyata asik banget orangnya",  
            "pesan": "jangan lupa minum air putih bangg"
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "kakaknya seru dan ambis banget",  
            "pesan": "semangat selalu ya kakk ngodingnya"
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "kak hani orangnya ramah banget, seru dan mirip temen sma ku",  
            "pesan": "semangat terus ya kak hani"
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "abangnya ternyata humble dan asik parahh",  
            "pesan": "bolehlah bang kapan-kapan karaoke bareng"
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=1MsaDs6-FDZMbTt7BxngarrRSVTb9bdwJ",
            	"https://drive.google.com/uc?export=view&id=1lFN3s1Uzhy2SoIcjx0ycxFiX6YRN9ku5",
            	"https://drive.google.com/uc?export=view&id=1zoX6B4MZI_g9nvUk7L7gsziMGwh5Q6uI",
            	"https://drive.google.com/uc?export=view&id=1AhyLqnnTweqifExVL5yEg-sC-H4aMUgq",
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
            "kesan": "kakaknyaa asik, baik banget dan ramah",  
            "pesan": "semangat selalu yaa kak"
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "pas mau foto ditanya kalau jadi hewan mau jadi hewan apa",  
            "pesan": "infokan gym bareng bang"
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "kakak ini ramah sekali dan baik",  
            "pesan": "semangat terus ya kakk"
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "orangnya seru banget dan ternyata suka drakor",  
            "pesan": "dah dibales belom sapaannya sama angin kak? wkwk"
            },
            ]
            display_images_with_data(gambar_urls_komisi3, data_list_komisi3)

    Baleg()
    
elif menu == "Badan Kesenatoran":
    def Bason():
        st.markdown("<h3 style='text-align: center;'>Badan Kesenatoran</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Senator", "Biro Aspirasi dan Media Komunikasi", "Biro Kajian Strategis dan Propaganda", "Biro Kesekretariatan"])

        with tab1:
            gambar_urls_senator= [
               "https://drive.google.com/uc?export=view&id=1c7rcAoeiuJZACleva2fIi8vcJzycNMWa",
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
                "kesan": "kak azizah orangnya keren banget dan seru",  
                "pesan": "semangat selalu ya kak kuliahnya"
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)
        with tab2:
            gambar_urls_biro_aspirasi= [
            "https://drive.google.com/uc?export=view&id=12EmYpbHYdixuD_vVuD8d9tUJKtpQqKrF",
    		"https://drive.google.com/uc?export=view&id=1FyCdBLljkIYNWNdoWYDz5xehtHyy277Y",
    		"https://drive.google.com/uc?export=view&id=1gXll5QeSE0aIkr3mbShCZMcQfwoqWYB6",
    		"https://drive.google.com/uc?export=view&id=1JzrhyR840xK6HJiyraLpusDsc2kk-Emq"
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
                "kesan": "bang helmi asprak alpro rb yang baik sekali",  
                "pesan": "semangat terus ya bang helmi"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "abangnya ternyata asik banget",  
                "pesan": "semangat selalu dan harus asik terus bang"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "kakaknya seru banget, mentor cosval nih",  
                "pesan": "semangat selalu ya kakak kuliahnyaa"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "abangnya kalem sekali dan cool",  
                "pesan": "semangatt selalu ya bangg"
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)
        with tab3:
            gambar_urls_biro_kajian= [
            "https://drive.google.com/uc?export=view&id=1uqmLPhPYInNvDT6VgMS8VCX3C-Uh9xzZ",
    		"https://drive.google.com/uc?export=view&id=1JkmjGDtI04GRsjJ83zW5fYHVGU8OidEk",
    		"https://drive.google.com/uc?export=view&id=1hnmahTfDPSugO0mMfl2HORrsOB3l-76P"

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
                "kesan": "kakaknya ramah sekali",  
                "pesan": "pengen ikutan nyari jurnal kak"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "kak aqila mentor bayes ini asik banget dan apa aja suka diketawain wkwkw",  
                "pesan": "semangat terus ya kak aqilaa"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "abangnya keren banget, rambutnya badai sekali jadi pengen ikutan",  
                "pesan": "semangat terus bang hazel kuliahnya"
                },
                ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)
        with tab4:
    
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1SBKGn4XiUmBCSz9GizP-FPjP-IRIu8ae",
    	    "https://drive.google.com/uc?export=view&id=1cVy63GEc06lf8EAIn-y76PQcYuE7GUm3"
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
                "kesan": "kakaknyaa asikk dan seru parah",  
                "pesan": "semangat terus kak buat kuliahnya dan tugas akhir"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "kakaknya baik dan asikk",  
                "pesan": "Semangat terus ya kakk kuliahnyaa"
            }
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_kesekretariatan)
    Bason()

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
            "https://drive.google.com/uc?export=view&id=1RuQveTHuwXn-ko3PqegohyQ97D_d35-G",
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
                "kesan": "kakanyaa seru dan baikk",  
                "pesan":"Semangat buat kuliah dan TA nya kak! semoga diberikan kelancaran"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1wQcFtELJ3M4woSH0jp_IthXFv6jvU_Lv",
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
                "kesan": "kakaknya tegas dan cool",  
                "pesan":"semangat untuk TA nya kak dan sehat selalu kakk!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/uc?export=view&id=1CjicOW8LBqdW3KzrOYBx4HyqwOG_WzGU",
            "https://drive.google.com/uc?export=view&id=1x87sryHTYAHGFIUCP20joxBiSPQ7agKO",
            "https://drive.google.com/uc?export=view&id=1IXBnIr-CrSBEvwumbf-yRxWkfXt2Wziu",
            "https://drive.google.com/uc?export=view&id=1gZz2pM0v5N4rjR0APMfQsagXxpKaRNEf",
            "https://drive.google.com/uc?export=view&id=1z8Wxo6puSY3_kwhPHwAPn2U7y8HdW0pg",
            "https://drive.google.com/uc?export=view&id=1pq7XJ258OVko0qQfkeC45J4lf6Xmuyhx",
            "https://drive.google.com/uc?export=view&id=11wrq_3rLFS1tesgYqfUb7IF4ykeWMaMx",
            "https://drive.google.com/uc?export=view&id=11BFo_LjPSEAvaBJpEhjzCkeg773v7NqZ",
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
                "kesan": "Abang berwibawa sekali dan ternyata jago sulap juga suka mengoleksi kartu",  
                "pesan": "semoga dilancarkan ya bang segala urusannya, dan semangat untuk TA nya bang!"
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "abangnya baik banget, tapi disatu sisi tegas",  
                "pesan":"semangat selalu ya bang dan jaga kesehatan bang!"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "abangnya galak tapi aslinya baik banget dan perhatian",  
                "pesan":"terima kasih ya bang udah mengobati saya waktu sakit, selalu jaga kesehatan ya bang!"
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "abang ini tegas dan galak, tetapi kadang ga galak",  
                "pesan":"jaga kesehatan ya bang dan semangat selalu"
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "kak yudia aslinya ramah bangett",  
                "pesan": "semangat terus kak dan semoga hal-hal baik selalu menyertai kakak!"
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "abangnya keren bangett",  
                "pesan":"semangat terus bang dan semangat buat kuliahnya"
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Sabang",
                "alamat": "Nomaden",
                "hobbi": "Duduk samping Henry",
                "sosmed": "@putrimannaa",
                "kesan": "kaka ini sebenernya ramah banget",  
                "pesan":"semangat terus ya kakk jujur saya terkesan kak"
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "kaka nya baik bangett dan seruu",  
                "pesan":"buat kakanya semangat terus ya kaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1JmoJ9G511RDyRR8HQBYunLOeiZ01nyuZ",
            "https://drive.google.com/uc?export=view&id=1-6vyY4C8ol_SjXeT8tx5QJYqelXvX1I1",
            "https://drive.google.com/uc?export=view&id=17rGxLYE-Tepy3UQvhV7_obQQ4b3d4fQR",
            "https://drive.google.com/uc?export=view&id=1MPzcXd6-eQMNlAj6ZmOlgmSQ9Fg1Kraw",
            "https://drive.google.com/uc?export=view&id=19AIFM4cfLbwjdC-z8UO9LJ8970wnbHea",
            "https://drive.google.com/uc?export=view&id=1sTuQMxz4A16Nd8OjoyC5924xG3h107IB",
            "https://drive.google.com/uc?export=view&id=1WZSQ1ku3YjJjckfPWiJC8h_TBm7PQ6sZ",
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
                "kesan": "abangnya seru banget pas ngobrol dan asikk",  
                "pesan":"semoga dilancarkan ya bangg segala urusannya dan semangat terus bang!"
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "kakaknyaa ramah sekalii",  
                "pesan":"kakaknya semangat terus yaa kak, jangan lupa jaga kesehatan juga kaa"
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "kakaknya seruu dan baik banget",  
                "pesan":"semangatt dan sehat selalu ya kakk!"
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "abangnya keliatan tegas dan ternyata pendukung setia MU",  
                "pesan":"semoga emyu banjir tropi bang dan semangat kuliahnya bang, GGMU!"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakanyaa ramah dan seru sekalii",  
                "pesan":"semangatt kuliahnya kakakk"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Tembung",
                "alamat": "Belwis Tengah",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "abangnya seru banget dan asik",  
                "pesan":"semangat buat kuliahnya ya bangg"
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "kakanyaa ramah, baik banget",  
                "pesan":"semangat teruss kakak kuliahnya!"
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
            "https://drive.google.com/uc?export=view&id=1z92B4F-ZAzoIPsBsQo108F_8P9_nsKJj",
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
                "kesan": "bang fabio orangnya keren parahh, baik banget dan asprak ads yang asik dan ramah",
                "pesan": "semangat buat kuliah dan TA nya bang, abang keren banget jujur"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=10whqGHpU8ciR_2OlKeJ9NpwLMJ2spxYG",]
            data_list_sekretaris_mikfes = [ 
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "kak tanty ini orangnya sangat ceria sekali, ramah dan baik banget",
                "pesan": "Semangat buat Tugas Akhirnya kak dan jangan lupa jaga kesehatan kaa"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1iwu33bdlLHu04f2UfjbMf42wwKi9zOAI",
            "https://drive.google.com/uc?export=view&id=1mNUMEgd3JQU4tDAYgoSi89_AjYDfdj9c",
            "https://drive.google.com/uc?export=view&id=1QitASkW6NPmWqq7eNo5A17d5l-vINnuD",
            "https://drive.google.com/uc?export=view&id=1cEE3MrVtUFtIBB2PTZqwyhgCOGLRLe-W",
            "https://drive.google.com/uc?export=view&id=1CPK9omuyFbLF3MgHhiTPTukdQnLFdG09"
            ]
            data_list_Divisi_Professional_Skill_and_Development = [
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bermain Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang Fadil sungguh menginspiratif banget",
                "pesan": "Makasih banyak atas ilmunya waktu jadi kasuh TPB38, Bang. Masih ga nyangka secepat itu Abang pergi, tapi sekarang Abang udah ga sakit lagi. Doa terbaik untukmu Bang Fadil, Al Fatihah"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "@manuelfdk_",
                "kesan": "Abangnya keren, baik banget dan seru parah",
                "pesan": "Semangat terus ya bang kuliahnya dan jaga kesehatan bang!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "kakanya ramah dan seru parah",
                "pesan": "kaget, karena ternyata kakanya satu kabupaten sama saya hehe"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "kakaknyaa seru dan humblee",
                "pesan": "semangat terus kuliahnya kak ehehe"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "kakanyaa keren banget dan asik parahh",
                "pesan": "semoga terwujud segala keinginannya kak, semangat kuliahnya kak!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "baik banget kakanyaa jujurr",
                "pesan": "semangat buat kuliahnya kakk dan sukses selaluu"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            "https://drive.google.com/uc?export=view&id=1RiHbzPaIy1W7Bem6oWgVU8Fx_wqrc107",
            "https://drive.google.com/uc?export=view&id=1fOwQP6CdBZQllmoh6YMscwQKD-0viw5T",
            "https://drive.google.com/uc?export=view&id=1J9lZTyOSvp3RXMsSx2E-mQMGUQpM4J3c",
            "https://drive.google.com/uc?export=view&id=18AGfh7mKl-2_ignLFdUDzPnEtUntGN0r",
            "https://drive.google.com/uc?export=view&id=1l2cYhX_VVuQlGuzg1DyHKpm_1BEMAuDe",
            "https://drive.google.com/uc?export=view&id=1nkRMxGIevDmV2QkSd-DJR9mCF4H3_6I7"
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
                "kesan": "abangnya keren banget dan seruu",
                "pesan": "Semangat selalu untuk kuliah dan TA nya ya bang!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "kak elsa sangat ramahh dan ternyata ceria sekalii",
                "pesan": "semangat terus kak buat kuliahnya dan jangan lupa jaga kesehatan kakk"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "kakaknyaa ceria banget dan seeru parahh",
                "pesan": "semoga selalu dilancarkan kakk segala urusannya"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "kakak NIM saya yang asikk banget, jadi asprak alpro yang seru parahhh dan MC nya yang ga kalah seruuu",
                "pesan": "Semangat terus kak buat kuliahnya, jaga kesehatannya ya kaaa, terima kasih kakak sudah menjadi kanim yang ramahh dan baikk"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "abangnya baik banget, seru dan keren parahh",
                "pesan": "Semangat buat kuliahnya bang dan jangan lupa jaga kesehatan bangg"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "kakanyaa ramah banget dan baikk",
                "pesan": "semangat selalu kakk buat kuliahnya eheheh"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            gambar_urls_Divisi_Research_Development = [
            "https://drive.google.com/uc?export=view&id=1Li4rk0inYqyUGghMndWMDLGzovEXs46r",
            "https://drive.google.com/uc?export=view&id=164WfwlNWprMVY5bhfvL99cjRzk1T56RD",
            "https://drive.google.com/uc?export=view&id=1p2wjmt9Id2Tiw4nj7V7Ig3hT2Tmq4THi",
            "https://drive.google.com/uc?export=view&id=1NPOGAoAB0sBgWIZ5Jo-bb-83niAggPP4",
            "https://drive.google.com/uc?export=view&id=1FM5tE0EaWFczEn0GotpmDKSsgIZds7rB",
            "https://drive.google.com/uc?export=view&id=1G3yQ0c-U3UGtIYC7go5F53Woj2wjrDbQ",
            "https://drive.google.com/uc?export=view&id=1qVZAgH-4if4I4YoQgu9ErXEK4H18Liio",
            "https://drive.google.com/uc?export=view&id=1NdESzqm55xZggJZtf_iGjtq2POEWJxHL"
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
                "kesan": "abangnya keren banget dan seruu",
                "pesan": "semangat selalu bang buat kuliah dan TA nya!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "jujurr kakaknyaa baik banget ramahh",
                "pesan": "semoga hal baik selalu mengelilingi ya kak dan semangat teruss kak"
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
                "pesan": "semangat selalu buat kuliahnya ya bangg!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "abangnya baik banget dan seru parahh",
                "pesan": "semangat ya bang dan terima kasih sudah mengantarkan saya heheh"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "abangnya pinter dan keren banget, astut ale yang seru parahh",
                "pesan": "Jujurr banyak hal yang saya dapat dari abang waktu belajar ALE, semangat terus ya bang!!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "kakanyaa baik banget dan ramahh",
                "pesan": "semangatt buat kuliahnya kakak"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "jujur abangnya keren dan termasuk orang yang menginspiratif saya",
                "pesan": "semangat untuk kuliah dan kegiatannya bang"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (ril kh bang segini)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "bermain tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "orangnya baik tetapi tegas",
                "pesan": "semangat selalu ya bang semoga hal-hal baik selalu menyertai abang"
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
            "https://drive.google.com/uc?export=view&id=1nsN3TV4twKSbjBdoIzTqW6VYpgxXaJK5",
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
                "kesan": "kakaa ini auranya tegas tapi aslinya baik banget jujur ehehe",
                "pesan": "semangat terus kakk dan lancar-lancar nyusun TA-nya kak!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1LIlJ3cvLC3iqiRl5jszIlZgdPSUeb5Ks",
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
                "kesan": "kakakk ini ramah banget dan seru buat diajak ngobrol",
                "pesan": "semangatt terus kuliahnya kak, jangan lupa jalan-jalan kaa"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [            
            "https://drive.google.com/uc?export=view&id=16GDkmll-3PvpP-ttIugBRAI65l9IyNJl",
            "https://drive.google.com/uc?export=view&id=11G341A7U5F5zGYbkCWCJIYZFTJ5RglhB",
            "https://drive.google.com/uc?export=view&id=1XvGL6VYd1TPZCdzpJmy32soPLnWdhSEK",
            "https://drive.google.com/uc?export=view&id=1FqyUTZKhL4W1WKl5ef8i8mNbi1sqTrcE",
            "https://drive.google.com/uc?export=view&id=12zejeZPIK7WsANjtSnvsEz8n6zfrrxEY",
            "https://drive.google.com/uc?export=view&id=1OpcOJfQy0_W6itjw36geZPg5VRhsKW9x",
            "https://drive.google.com/uc?export=view&id=1xpvZZ3swq-PSyd0Z9u13gvNg3Kl7DJDP",
            "https://drive.google.com/uc?export=view&id=184s84jWhSqVP2Ovwah4b1lsw2BDX7Hk1",
            "https://drive.google.com/uc?export=view&id=15wd5elQvY_3_oCBjsEdTxDuyT-v-_01A",
            "https://drive.google.com/uc?export=view&id=104NEC_quXpOo_TSxAg5e5RFP2JioHS95",
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
                "divisi" : "Hubungan Luar",
                "kesan": "kakanyaa baik banget",
                "pesan": "semangat selalu dan semoga TA nya lancar jaya ya kakk!",
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "Ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "divisi" : "Hubungan Luar",
                "kesan": "kerenn abang ini panutan saya banget dan asik buat sharing.",
                "pesan": "Tetap jaga kesehatan ya bang dan semangat terus abang keren banget jujur!",
            },
	        {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "asal": "Ikut kadep",
                "alamat": "Sukabumi",
                "hobbi": "Mancing",
                "sosmed": "@khaindaa_",
                "divisi" : "Hubungan Luar",
                "kesan": "orangnya asik dan ramah sekalii",
                "pesan": "semangat kuliahnya dan jaga kesehatan kakkk"
            },
	 {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "-",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "Lihat-lihat perumahan",
                "sosmed": "@bimo_arkana",
                "divisi" : "Hubungan Luar",
                "kesan": "abang ini santai tapi tetep keren",
                "pesan": "Semangat terus buat kuliahnya bangg!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan yang manis biar manis",
                "sosmed": "@alfayabiyi",
                "divisi" : "Anggota",
                "jabatan": "Hubungan Luar",
                "kesan": "keren lah pokoknya abang inii",
                "pesan": "ssemangat jalanin semesternya bang, jangan lupa istirahat!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton Film",
                "sosmed": "@asemeilani",
                "divisi" : "Hubungan Luar",
                "kesan": "kaka ini orangnya seru banget dan ramah",
                "pesan": "semangat terus kaa buat kuliahnya !"
            },
	        {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "divisi" : "Hubungan Luar",
                "kesan": "abang nyaa humble dan murah senyum",
                "pesan": "semoga selalu humoriss dan tetep semangat ya bang!"
            },
	        {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "Mancing",
                "sosmed": "@khaindaa_",
                "divisi" : "Hubungan Luar",
                "kesan": "kakak inii baik dan ramahh",
                "pesan": "tetep jadi kating yang asik ya kak terbaik heheh"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "divisi" : "Hubungan Luar",
                "kesan": "kaka ini ramah banget dan seruu",
                "pesan": "semangat terus buat kuliah dan nugasnya kak, jangan lupa bahagia kak heheh"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Jati Agung",
                "hobbi": "Main Futsal",
                "sosmed": "@yollanda_agustina16",
                "divisi" : "Hubungan Luar",
                "kesan": "kakak ini baik banget dan tangguh bener",
                "pesan": "jaga kesehatan dan semangat teruss ya kakk"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1SHfM1-GhkEvvl2PQqaqAgfYjh75dMqOP",
            "https://drive.google.com/uc?export=view&id=11WDmvYZkucoskcocH-xMb2BCip6SZGUM",
            "https://drive.google.com/uc?export=view&id=1DKESK-DXCCvOFnkDlpATQfoSCAAJy61S",
            "https://drive.google.com/uc?export=view&id=1hYO-Yd2aB6FRg1tRce5HfPJywKqgxtND",
            "https://drive.google.com/uc?export=view&id=1-zkcvuYkO_dypwpH17NA5jdoZXzQ4x1w",
            "https://drive.google.com/uc?export=view&id=176iwk6RnVSild1lWmkeb7xcYb7EMIsDP",
            "https://drive.google.com/uc?export=view&id=1Gvfv2iMteN8VQOxPgrbZfQI0a7S1YiCe",
            "https://drive.google.com/uc?export=view&id=1fYZbZ-5T37VJL2vJEEqCBhnqB_Tv2ErS",
            "https://drive.google.com/uc?export=view&id=1G1eeZecXIRQ7nsDhTnbgDxTf58us5lM5",
            "https://drive.google.com/uc?export=view&id=1DPSQfrNDoajMLmwlgVSMH10YtGXnwW_N",
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
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "ramahh dan welcome banget orangnya jujur asik bangett",
                "pesan": "semangat dan lancar terus nyusun TA nya bang"
            },
	        {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25",
                "asal": "Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "kakak ini jujur keren bangett",
                "pesan": "tetep semangat kejar impiannya kak!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "25",
                "asal": "Luhak tanah data",
                "alamat": "Gerbang barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "kakak ini kalem banget ehehe",
                "pesan": "semoga dimudahkan ya kak jalannya heheheh"
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
                "kesan": "kakak inii super duper ramah",
                "pesan": "selalu bahagia teruss ya kakk"
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
                "kesan": "seru banget abangnyaa dan asik diajak ngobroll",
                "pesan": "Semangat buat kuliahnya dan jangan lupa jaga kesehatannya bangg!"
            },
	        {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "19",
                "asal": "Swiss",
                "alamat": "Way Halim",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "abang ini ramah banget super duper raamah pokoknyaaa",
                "pesan": "lancar terus ya bang kuliahnya dan semangat terus bangg"
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
                "kesan": "abang ini aslinya asik asal nggak lagi galak heehe",
                "pesan": "sehat sehat dan semangat selalu bangg"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Membantu Yudia",
                "sosmed": "@jaldii._",
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "abang ini keren banget, dan sangat sangat ramah sekali",
                "pesan": "bang jaldi semangat terus ya dan harus tetap ramahh"
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
                "kesan": "kaka ini ramahh dan murah senyumm",
                "pesan": "ssseemangat terus jalani harinya kak!"
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
                "kesan": "Ramah bangett",
                "pesan": "Stay ceria yaa kakak"
            },
        ]
            display_images_with_data(gambar_urls_pengabdian_masyarakat, data_list_pengabdian_masyarakat)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
            "https://drive.google.com/uc?export=view&id=1JbBIqf3s7PxMWznm0BTgBf6LbwF9aUEF",
            ]
            data_list_Kadep_internal = [
            {
            "nama": "Haikal Fransisko Simbolon",
            "nim": "106",
            "umur": "23",
            "asal": "Jambi",
            "alamat": "Jatimulyo",
            "hobbi": "Ngerosting orang",
            "sosmed": "Haikalsbln_",
            "kesan": "abangnya seru, baik dan berwibawa",  
            "pesan": "semangat terus bang buat kuliah dan buat Tugas Akhir!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=1rQ1HbhpjX3bhaf210juV85FuNtAVCMEV",
            ]
            data_list_sekdep_internal = [
            {
            "nama": "Kharisma Mustikasari",
            "nim": "123450034",
            "umur": "21",
            "asal": "Waikana",
            "alamat": "Untung Seropati",
            "hobbi": "Suka menolong orang",
            "sosmed": "@rismaa.mustika_",
            "kesan": "kakaknyaa baik banget",  
            "pesan": "sering-sering menolong teman ya kak dan semangat terus kak kuliahnya"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=15Z3Ss1ofMoxXEOXLwj5qaJ7YLZmQkS1W",
            "https://drive.google.com/uc?export=view&id=1ZrWkeu89TcmUHtw_OG4unpe-F8CnLJvr",
            "https://drive.google.com/uc?export=view&id=1aFATDzgKIb0aINHwPb-WGn6hB3qWZ1cU",
            "https://drive.google.com/uc?export=view&id=1O-IpfovEldU5YZf9oiKyk6X1EbOiDpX4",
            "https://drive.google.com/uc?export=view&id=1eAo9Yk0YszR1uyjL2zhCIqBn5-NnaNW2",
            "https://drive.google.com/uc?export=view&id=1lgRWjyG7zDFoZHOA-i1C2itpCHzrhyev",
            "https://drive.google.com/uc?export=view&id=1khKOHXtKY9oyNl80ynP5h_NlTGZz7MeS",
            "https://drive.google.com/uc?export=view&id=1waCNdVqwfolWX4TEgkUewZtgVa4e2iVO"
    
            ]
            data_list_keharmonisasian = [
            {
            "nama": "Hanna Gresia Sinaga",
            "nim": "123450038",
            "umur": "21",
            "asal": "Kisaran CV",
            "alamat": "Sukarame",
            "hobbi": "Menyapa satpam ITERA",
            "sosmed": "@hanna_g_sinaga",
            "kesan": "kakaknya ramah banget, positive energy, ceria dan murah senyum",  
            "pesan": "semangat terus untuk kuliahnya dan ceria selalu yaa kak"
            },
            {
            "nama": "Ahmad Farhan Gani",
            "nim": "123450121",
            "umur": "20",
            "asal": "Keliling",
            "alamat": "Kemiling",
            "hobbi": "Olahraga menembak",
            "sosmed": "@farhnghnii",
            "kesan": "jujur saya terkesan bang sama perkusinya",  
            "pesan": "semangat terus bang untuk kuliahnya!"
            },
            {
            "nama": "Aisyah Khairun Nisa",
            "nim": "124450096",
            "umur": "20",
            "asal": "Riau",
            "alamat": "Belwis",
            "hobbi": "Nulis wishlist",
            "sosmed": "@aisyahkhair",
            "kesan": "kakaknyaa seru ramah dan baik banget",  
            "pesan": "sehat selalu ya kakk"
            },
            {
            "nama": "Cerine Sihotang",
            "nim": "124450049",
            "umur": "19",
            "asal": "Medan",
            "alamat": "Belwis",
            "hobbi": "Balap Liar",
            "sosmed": "@cerine_ipynb",
            "kesan": "kakaknya baik banget, waktu pplk kakak medis ini ramah banget",  
            "pesan":"sehat selalu ka cerine dan semangat buat kuliahnya kakk!"
            },
            {
            "nama": "Jaya Saputra Tamba",
            "nim": "125450094",
            "umur": "22",
            "asal": "Kisaran City",
            "alamat": "Pemda",
            "hobbi": "Kick boxing",
            "sosmed": "@jay.saputratmb",
            "kesan": "abangnya baik banget dan humble parah",  
            "pesan": "semangat terus bang kuliahnya dan semoga dilncarkan"
            },
            {
            "nama": "Najla Nursyifa",
            "nim": "124450051",
            "umur": "20",
            "asal": "Aceh",
            "alamat": "Belwis",
            "hobbi": "Nonton ASMR",
            "sosmed": "@njlanursyifa",
            "kesan": "kakaknya ramah sekalii",  
            "pesan":"semangatt terus kak untuk kuliahnya"
            },
            {
            "nama": "Rozak Ramdani",
            "nim": "124450100",
            "umur": "18",
            "asal": "Lampung Selatan",
            "alamat": "Korpri Raya",
            "hobbi": "Isengin Harvin di kelas",
            "sosmed": "@rozakramdani__",
            "kesan": "abangnya ramah banget, keren dan baik",  
            "pesan": "semangat terus ya bang kuliahnya!"
            },
            {
            "nama": "Teresa Christiani Purba",
            "nim": "124450046",
            "umur": "19",
            "asal": "Riau",
            "alamat": "Belwis",
            "hobbi": "Masak",
            "sosmed": "@christiani8872",
            "kesan": "kakak nya seru abis dan baik banget",  
            "pesan": "semangat selalu ya kaka buat kuliahnya."
            }
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=1n1uVqFsZeGIEKq__sKEoCOXOPEUpknqN",
            "https://drive.google.com/uc?export=view&id=1KtSB3Bqd3laMeFBUcq9gat9b1TE-wW44",
            "https://drive.google.com/uc?export=view&id=1ddePbbrX9IKg2arldn3DPX-c4YpqsdZH",
            "https://drive.google.com/uc?export=view&id=1Q9B-AYIZ-9Pt2Hic8d44NjSTwzQ0PxkV",
            "https://drive.google.com/uc?export=view&id=1MYhHRzE_n4BCGNDvUBY5zhQ0AR134BkF",
            "https://drive.google.com/uc?export=view&id=19aTQIsjn4PifNDojyHLAMHc26gp1AZK6"
            ]
            
            data_list_kerohanian = [
            {
            "nama": "Muhammad Hanif Dzaky Arifin",
            "nim": "123450064",
            "umur": "21",
            "asal": "Sumatera Barat",
            "alamat": "Way Kandis",
            "hobbi": "Nonton film",
            "sosmed": "@hnfdzky_",
            "kesan": "abangnya ramah sekali",  
            "pesan": "semangat terus bang kuliahnya!"
            },
            {
            "nama": "Audina Fitria",
            "nim": "124450038",
            "umur": "20",
            "asal": "Sumbar",
            "alamat": "Sukarame",
            "hobbi": "Main air terjun",
            "sosmed": "@audinaf_03",
            "kesan": "kakanya ramah banget, asik dan seru",  
            "pesan": "semangat kakak kuliahnya dan sehat selalu"
            },
            {
            "nama": "Cika Adelia Br Marbun",
            "nim": "124450107",
            "umur": "20",
            "asal": "Pekanbaru",
            "alamat": "Belwis",
            "hobbi": "Dengerin lagu",
            "sosmed": "@chikamrbn",
            "kesan": "kakaknya baik banget dan ramah",  
            "pesan": "semangat kakak buat kuliahnya"
            },
            {
            "nama": "Gustin Haleluya Tampubolon",
            "nim": "124450068",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Airan",
            "hobbi": "Nonton",
            "sosmed": "@gustinhaleluya",
            "kesan": "kakanya baik banget dan ramah sekali",  
            "pesan":"semnangat kuliahnya kakak!"
            },
            {
            "nama": "Muhammad Harvinsyah",
            "nim": "12445128",
            "umur": "20",
            "asal": "Sumsel",
            "alamat": "Belwis",
            "hobbi": "Berburu ayam hutan",
            "sosmed": "@muhvinz_",
            "kesan": "abang ini seru, asik diajak ngobrol dan hobinya out of the box",  
            "pesan": "semangat terus ya bang kuliahnya"
            },
            {
            "nama": "Rafa Sabina Fahimah",
            "nim": "124450036",
            "umur": "20",
            "asal": "Natar",
            "alamat": "Natar",
            "hobbi": "Nanya ke Andra dan Yolanda",
            "sosmed": "@snasaa._",
            "kesan": "kakak ini ramah seru dan baik bangett",  
            "pesan": "semangat terus ya kakk"
            }
            ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
            
    internal()

elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Storage Sains Data</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
            "https://drive.google.com/uc?export=view&id=17L8CVJNZW9CnZT4dFLRbnIJV1hkrECPV",
            ]
            data_list_Kadep_ssd = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Baca jurnal, cari jurnal yang berhubungan dengan TA",
                "sosmed": "@ihsan.myusuf",
                "kesan": "kakanyaa asikk",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=17OaNRDKj0BYWAH9OpE8UAXwA4ASBJfUa",
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
                "kesan": "seru banget kakanya dan asik diajak ngobroll",
                "pesan": "semangat terus kuliahnya ya kakak",
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1A2R07Lt8G7cuuOxv-hNJHdldiRfy6lDK",
            "https://drive.google.com/uc?export=view&id=1km1B_OohbhUAHHf0_MWHqbGuMHrlNEsN",
            "https://drive.google.com/uc?export=view&id=17UnPCowavT-ALp5bAMQawAY0VnMqJ7cg",
            "https://drive.google.com/uc?export=view&id=1U7Mnz5ja1nD-3fqgMI2ySMy9Hw6OgEiJ",
            "https://drive.google.com/uc?export=view&id=12nBhSNeEX3wWfTDroKJGAOA-2X1mFwym"
            ]
            data_list_kemitraan = [
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "18",
                "asal": "Padang",
                "alamat": "Hasan 4",
                "hobbi": "Baca jurnal, nonton Marvel",
                "sosmed": "-",
                "kesan": "Kakak ini asik seruu",
                "pesan": "semangat terus kuliahnya kakak !",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Abang ini baiik bangett",
                "pesan": "semangat terus kuliahnya kakak !",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak ini seru dan ramahh",
                "pesan": "semangat terus kuliahnya kakak !",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak ini asik dan saya seru dengan ilmu yang dia kasii",
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
                "kesan": "abang ini seru dan ramah banget",
                "pesan": "semangat terus kuliahnya bangg",
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1O3lUAM3PjhXKDh9cl6OujsVgWk_on0ux",
            "https://drive.google.com/uc?export=view&id=15Uqz84sKQrh9GaQpz3iwZtUxrEDWkQKw",
            "https://drive.google.com/uc?export=view&id=1TVxfjl3cBWuQ6tWVhiohTEwuXp3ICcPv",
            "https://drive.google.com/uc?export=view&id=1mIXYTa9p3vo3vlWTgaWAX1bCUC_4SVdZ",
            "https://drive.google.com/uc?export=view&id=1eky0oI2Nb1XxFSr8a_TU-GOEP5rNuGXQ",
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
                "kesan": "abangnya seru banget",
                "pesan": "semangat terus kuliahnya banggg!!!",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "abangnya asik banget",
                "pesan": "semangat terus bangg",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakak ini asik banget",
                "pesan": "Semangat terus kakk"  
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakak ini asik parahh",
                "pesan": "semangat terus buat kuliahnya yaa kak !!!",
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
            "https://drive.google.com/uc?export=view&id=1XnqYlumoMW3ErKU7-2rPhDv8_8xbyGBU",
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
                "kesan": "Keren banget kakanya!!",
                "pesan": "Jujur salut sih sama anak medkraf. Walau dikejar deadline desain sana-sini tetep strong. Semangat terus kak!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1qphJD9_aEL_EBbxCmlJN4hmvf1luKkA2",
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
                "kesan": "Nggak kalah keren pokoknya jujurr.",
                "pesan": "Tetap semangat ya kak, semoga semua resolusi dan wishlist-nya bisa kecapai satu per satu!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1UzaT3OLrXrxOu8NN5kMKlqui9ds2Y21d",
            "https://drive.google.com/uc?export=view&id=1tZ9H5GoWy3oa8E2MpXJnbORnkPOWcUL8",
            "https://drive.google.com/uc?export=view&id=1E3qUluphLxIYo275RwEeBKvJxQpn0tAl",
            "https://drive.google.com/uc?export=view&id=1uP5cQ0Acv_EZRfpPeMo9DO8mDZpV9T5W",
            ]
            data_list_Divisi_dokumentasi = [
            {
                "nama": "Labo John Napitupulu",
                "nim": "37",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Tong setan",
                "sosmed": "@noerruuu",
                "divisi": "Dokumentasi",
                "kesan": "Speechless saya bang",
                "pesan": "Semangat terus bang buat kuliahnya"
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "divisi": "Dokumentasi",
                "kesan": "Kakanya super asikk",
                "pesan": "Semangat ngampusnya kak, walaupun beban tugasnya lumayan berat tetep kuat yaa!"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@felisyanbl__",
                "divisi": "Dokumentasi",
                "kesan": "Keren banget pastinya.",
                "pesan": "Sehat-sehat ya kak, jangan lupa cari waktu buat seneng-seneng juga!"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "divisi": "Dokumentasi",
                "kesan": "Kerenn abis bang.",
                "pesan": "Semangat terus bang! Jangan lupa nyempetin waktu buat rehat dari sibuknya organisasi sama kuliah."
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=16Ixm-OD1ARwo1b-PKtjLAoSCM0pIukEs",
            "https://drive.google.com/uc?export=view&id=1TKDm1nGP_fjtK-1sM6_2UnDgZFcAkLoe",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
            "https://drive.google.com/uc?export=view&id=1JgnIhU8IPQKonqDmrfz5BjpijAenVuCg",
            "https://drive.google.com/uc?export=view&id=1zMEjFPzjj0jDRyAKy_e4-a8vtYTJ7jgy",
            "https://drive.google.com/uc?export=view&id=1L33GL_xFWewBx_KtBoCwIEuwj_Xk3e_o",
            ]
            data_list_Divisi_Media_dan_Konten_Spesialis = [
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal": "Karawang",
                "alamat": "Airan",
                "hobbi": "Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Orangnya humble dan ramah puol.",
                "pesan": "Semangat ngampus dan organisasinya kak! Jangan lupa self-reward kalo abis capek nugas."
            },
            {
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal": "Kayangan",
                "alamat": "Heaven",
                "hobbi": "Mancing",
                "sosmed": "@aallishaa.a",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakak ini ramah bangett",
                "pesan": "Stay happy terus ya kak Allishaa!"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu roda",
                "sosmed": "@alya.rmdhnti",
                "divisi": "Media dan Konten Speasialis",
                "kesan": "Vibes-nya cool banget kakak ini",
                "pesan": "Kakanya asik banget deh, semoga kak Alya selalu dikelilingi hal-hal positif ya!"
            },
            {
                "nama": "Bunga Clarissa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": "Belajar",
                "sosmed": "bungaclrssf",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Sopan dan gampang akrab kakak ini",
                "pesan": "Semangat ya kak buat kuliahnya, jaga pola makan biar nggak gampang sakit kak"
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gada yang tau",
                "asal": "Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "difanyhsa_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "kakaknya asik dan ramah bangettt",
                "pesan": "Lancar terus kak kuliahnya, sempet-sempetin istirahat bentar di sela-sela kesibukan hehee"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@nzlhauly_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "aura kakak ini kerenn bangett",
                "pesan": "Semangat jalanin semester ini kak!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=180WUx9wpBIc5BRLBpqE3428BWByI7lNB",
            "https://drive.google.com/uc?export=view&id=1Mck0TU-vJyA_j37wcRM5aSGWJwS0zF8o",
            "https://drive.google.com/uc?export=view&id=1AeAmHO5y6kuG4hJDuut_9pH28MQHNu0S",
            "https://drive.google.com/uc?export=view&id=1_2dn3AhEjlW2oTyQAL5JUP52at51tVdd",
            "https://drive.google.com/uc?export=view&id=14yARTpv7-CKeELfFye_isD_gywwp_1ah",
            "https://drive.google.com/uc?export=view&id=1BLika0YyoJ1-7-rRbLHvHmA4gpJ3b9mL",              ]
            data_list_Divisi_Visual_Design = [
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal": "Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "sosmed": "n1tg._",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "kakaknya super baik dan ternyata rumahnya deket wkwkwk",
                "pesan": "semangat ngampusnyaa kak"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal": "Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Nyuluh manuk",
                "sosmed": "@daffascript_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Orangnya baik banget jujurr",
                "pesan": "Semoga urusannya dilancarin terus ya bang ehehe"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll fesnuk",
                "sosmed": "edsel_0712",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "keren abiss abangnyaa",
                "pesan": "Jaga kesehatan bang dan semangat teruss"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "luciarachel_",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya asik diajak sharing",
                "pesan": "Sehat-sehat terus ya kak!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Melukis, menulis",
                "sosmed": "@_shaazzh",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Ramah banget kakanya dan gampang nyambung",
                "pesan": "Semangat terus kak, semoga dimudahin segalanya"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@xifasky",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "kakaknya ramah banget",
                "pesan": "lancar terus ya kak buat kuliahnya!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()

elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown("<h3 style='text-align: center;'>Departemen Minat dan bakat</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4= st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])
        
        with tab1:
            gambar_urls_kepala_departemen_minbak= [
            "https://drive.google.com/uc?export=view&id=1IAfg-eyjgFacKLuSQ6Cn8DOlaOoO4P2r",
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
            "kesan": "abangnya panutat saya banget, keren dan cool",
            "pesan": "Semangat terus bang buat kuliah dan TA nya!"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1Id5VWCt-nh1UXecEYvcyVxb-TT9yxUPp",]
            data_list_sekretaris_departemen_minbak = [ 
            {
            "nama": "Gusti Putu Ferazka Dhiyamika",
            "nim": "123450046",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Dadi",
            "hobbi": "Mendaki",
            "sosmed": "@ferazkaa",
            "kesan": "kakaknyaa super duper ramahh",
            "pesan": "Sukses selalu yaa kak!"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
            "https://drive.google.com/uc?export=view&id=163xMcgStYtcjtb0wqw9jutLL5jfqd06L",
    	    "https://drive.google.com/uc?export=view&id=1vktQPKLmQg5MXiGZVHiQQcVGYi5bPwD7",
            "https://drive.google.com/uc?export=view&id=1hglE5HX-ZIdJm4nD5gaARzkYOeNG6bTQ",
            "https://drive.google.com/uc?export=view&id=1ksDF8rDjnqxHAt7CIzqBh0D3iN1Yg1Zr",
            "https://drive.google.com/uc?export=view&id=1vD5ZmG9z4JzHPUBUst7eEBvDcMBfAYzo",
            "https://drive.google.com/uc?export=view&id=10hBudaIVNW_p4OYVPx-QJMuW9JTyWbh7"
            
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
            "kesan": "abang ini keren dan ramah banget",
            "pesan": "Semangat menjalankan tugasnya bangg!"
            },
            {
            "nama": "Ayu Andriani Parlina Wati",
            "nim": "124450058",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Airan",
            "hobbi": "Belajar + menghitung uang",
            "sosmed": "@aayuandriani_",
            "kesan": "Sangat ramah dan aktif kak",
            "pesan": "Tetap semangat dan sukses terus yaa kakk"
            },
            {
            "nama": "Dafa Elpriza",
            "nim": "124450131",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Kandis",
            "hobbi": "Jogging",
            "sosmed": "@dafaelpriza_",
            "kesan": "Sangat menyenangkan dan seruu abangnyaa",
            "pesan": "semangat terus bang kuliahnyaa"
            },
            {
            "nama": "Juwita Sari",
            "nim": "124450066",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Pemda",
            "hobbi": "Mancing",
            "sosmed": "@ju.juwitaaa_",
            "kesan": "Sangat baik dan murah senyum kakak inii",
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
            "kesan": "sangat seru abangnya",
            "pesan": "Semangat terus ya bangg!"
            },
            {
            "nama": "Salsabila Nazwa Putri",
            "nim": "124450002",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Korpri",
            "hobbi": "Nongkrong di kopken",
            "sosmed": "@slbnzw_",
            "kesan": "Sangat asik dan ceria kakakk inii",
            "pesan": "Tetap semangat kuliahnya ya kak!"
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
            "https://drive.google.com/uc?export=view&id=1RQHxh93DvWC9FdruF5hBliTdLcbxRGuM",
    		"https://drive.google.com/uc?export=view&id=1SUsszrBpzDpcFcZbjFHqtqcHqv7OyKAr",
    		"https://drive.google.com/uc?export=view&id=1opS3VHz6BDJna4IeoZtuxyaHiEx8_c9D",
    		"https://drive.google.com/uc?export=view&id=1glawA4tNSHwqigzoPMBHsHauGpbYh_TJ",
    		"https://drive.google.com/uc?export=view&id=1nSLI8WlSDkpwsTK_0qpCfG-zhggcZcML",
    		"https://drive.google.com/uc?export=view&id=1JItMDNdug3pLzcykXoqIGLUwwgd8jJoo",
    		"https://drive.google.com/uc?export=view&id=12-lPYPYhXHsuLhRPMk8T-ElHr5WjEiPY"
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
                "kesan": "abang ini sangat humblee dan seruu asik parahh",
                "pesan": "Semangat terus bangg!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "abangnya ternyata ramah banget dan sangat super duper humble makasih ya bang udah ngeluangin waktu dan tempat",
                "pesan": "jujur makasih banyak bang, abang mentor yang paling baik humble dan super baikk makasih ya bang dan jangan lupa istirahat bangg"
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
                "pesan": "Semangat terus banggg"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Sangat bersemangat",
                "pesan": "Tetap semangat dan sukses selalu bangg!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Sangat baik humble dan asik parahh",
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
                "kesan": "Sangat ceria dan ternyata satu kabupatenn",
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
                "pesan": "Sukses selalu bangg buat perkuliahannya!"
            }
            ]
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)  

    Departemen_Minbak()
