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

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vfjOJqTM3P0D8T7hSm8aea22gbMg-zOX",
            "https://drive.google.com/uc?export=view&id=1_mXB5AUDN2W8AKzxUL9EgOCn-IDCAWh4",
            "https://drive.google.com/uc?export=view&id=1XzlbGX4qZIqmrhh3pCwz7x6fFXWDxnXm",
            "https://drive.google.com/uc?export=view&id=11aQzjpJpG45cQe6nrD6FiNO8dCl3fIB2",
            "https://drive.google.com/uc?export=view&id=1tqawXYrLEd78veTqpmcNMF0v7Kd-B00j",
            "https://drive.google.com/uc?export=view&id=1VAUMxL9qcV2J_v87vbJjTkPr_V1QQQ16",
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
                "kesan": "Abang nya baik dan sangat menginspirasi saya, time management nya keren sehingga balance antara organisasi dan kuliah",  
                "pesan":"semangat kuliahnya lancar luncur TA nya bang"
            },
            {
                "nama": "Muhammad  Aqil Ramadhan",
                "nim": "1223450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil111",
                "kesan": "JUJURR abang ini kerenn, gatau tapi keren banget",  
                "pesan":"semangat terus bang aqill"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kak efi seruu dan asikk banget",  
                "pesan":"semangat terus kuliahnya kakak !"
            },
             {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini seru dan baikk",  
                "pesan":"semangat kuliahnya bangg, dilancarin TA nyaa"
            },
             {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya seruuuu bangettttttt",  
                "pesan":"semangat terussss kakkkkkk!"
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaaemdhn",
                "kesan": "Lucuuu kakanya, dan insight how to survive every semesternya sangat menarikk",  
                "pesan":"semangat untuk mengejar S.Si.d kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

if menu == "Badan Legislatif":
    def Badan_Legislatif():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wvjMspPNTj_J0Htm997XlA4286Ns8Sov",
            "https://drive.google.com/uc?export=view&id=13ABZMJyRy9gAVZ9gGLJtDi4mzzWXK7pk",
            "https://drive.google.com/uc?export=view&id=1o1GV_Qg21efXDOYVnHNOQRXfOY7LtDoh",
            "https://drive.google.com/uc?export=view&id=1xBhPDTUug5boE3rNMHQOjHDNvfSeMVK7",
            "https://drive.google.com/uc?export=view&id=1Xilvxl2vOtq_MxKqX8LVIZm-vLKOv_oo",
            "https://drive.google.com/uc?export=view&id=1H1xQiz19odx6qFP1bH1UE9jUnhVT_JX7",
            "https://drive.google.com/uc?export=view&id=1pQA_z8QfFsoNcOS4iXybH6n6w-FX1Nh1",
            "https://drive.google.com/uc?export=view&id=12_Ut3PqF9pBqr5USKQN5YQGNBu6EyLJQ",
            "https://drive.google.com/uc?export=view&id=1ddvj__X00Tz7POvYRw-1oiFqr6GwngSW",
            "https://drive.google.com/uc?export=view&id=1XYVb0EQhHmhgINhiViag0apUjiIqFr97",
            "https://drive.google.com/uc?export=view&id=1PRBnlsZzRt6Ifipy9Tf9nklMlSjSYTrE",
            "https://drive.google.com/uc?export=view&id=1b2523S6IFKxf9peZVoKuXmlDOC2KUNit",
            "https://drive.google.com/uc?export=view&id=1phbdcONvBgffVhMV008skAjB3aJbEmVw",
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
                "kesan": "Bang ridho suka asbun nya random bgt",  
                "pesan":"Semangat terus ya bang sudah memasuki semester tua ini"# 1
            },
            {
                "nama": "Juesi Aprilia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal":"Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu semusim dari marvel",
                "sosmed": "@j_eesie",
                "kesan": "LUCUU BANGETT, feminim energy nya adaa banget kalo ngobrol kaya ngidupin suasana gitu",  
                "pesan":"Semangatt terussss kaa jueee, ditengah ke hectic an semester ini"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Ngidupun api Baleg di tiktok",
                "sosmed": "@exvoltas",
                "kesan": "sangat keren dan gacorr parah, mapres + lolos pkm sampe nasional emezing",  
                "pesan":"Semangat selalu bangg dimanapun & kapanpunn!"# 1
            },
            {
                "nama": "Gh Mikael Niko A S",
                "nim": "124450025",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD musang",
                "sosmed": "@me._kael",
                "kesan": "takut kirain abangnya galak, tapi ternyataa baikk",  
                "pesan":"Semangat anmul nya bang"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "18",
                "asal":"Banten",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": "gemecc kakaknya, baik banget",  
                "pesan":"Semangattt kaa menjalani hari hari di semster 5 ini"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang gip mirip apdi suer, abang nya asik",  
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
                "kesan": "jujur first impresion aku kakak kaya galak banget pas waktu asis magenta, tapi aku ga asing banget eh ternyata kita satu SMA ",  
                "pesan":"Semangat terusssss kaaaaaaaaaaaaaaaaa"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "24",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "kesan": "Kakak nya imut gemasss",  
                "pesan":"Semangat selalu kakak imut"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "sangat berwibawa dan baik",  
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
                "kesan": "baik banget kakaknya",  
                "pesan":"Semangat terusss kaa!"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450111",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym sama Koleksi figure, nafas manual",
                "sosmed": "@nagatseee",
                "kesan": "abang nya lucu, suka bgt random question",  
                "pesan":"Semangat selalu bang jonn, katanya kemaren abis bantai TO yh"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Jajan sama nisa, putri, suci",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak nya baik",  
                "pesan":"Semangat terus ka kuliah!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kakaknya lucuu",  
                "pesan":"Semangat selaluu kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Badan_Legislatif()

if menu == "Badan Kesenatoran":
    def Badan_Kesenatoran():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=144OLza95GAekPOBxGgf5iV0YrfPAO3wO",
            "https://drive.google.com/uc?export=view&id=1ti5G9u8nC48HMh2i0xnQIU7IXbncNqDh",
            "https://drive.google.com/uc?export=view&id=1ee71ypuJulpD1dHfDEq51ZfKt4e4YLvc",
            "https://drive.google.com/uc?export=view&id=1_euaDlNkTtg1QlZ4iij9TkeJPYYePXoD",
            "https://drive.google.com/uc?export=view&id=1_FiQCpmTcUax6PFJZwpGVq-aCbdg4QDO",
            "https://drive.google.com/uc?export=view&id=1ol262wLvlED086kCg2VI7SE_j-z3ortl",
            "https://drive.google.com/uc?export=view&id=1STc5hjoZ981ZF9MJq3XB1mKOOfNJV--7",
            "https://drive.google.com/uc?export=view&id=1oOgL3dBt84N6eLmDO_vjATJLneAqVrnY",
            "https://drive.google.com/uc?export=view&id=1xFk6JKp_CFkNRSDebwnxNNGXV23wrtY0",
            "https://drive.google.com/uc?export=view&id=1QapfDxJK2oKljFX6qkZ0rWFbRZQuUcab",
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
    Badan_Kesenatoran()

if menu == "Departemen Minbak":

    def departemen_minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "pesan": "Semangat terus kak!",
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": (
                    "Sangat rapi dan cekatan dalam mengelola administrasi"
                ),
                "pesan": "Sukses selalu kak!",
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
                "pesan": "Semangat menjalankan tugasnya kak!",
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
                "pesan": "Tetap semangat dan sukses terus!",
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
                "pesan": "Sukses terus perkuliahan dan aktivitasnya!",
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
                "pesan": "Semangat terus kuliahnya!",
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
                "pesan": "Semangat terus kakak!",
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
                "pesan": "Tetap semangat kuliahnya ya kak!",
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
                "pesan": "Semangat terus memimpin divisinya kak!",
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
                "pesan": "Sukses selalu kuliahnya!",
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
                "pesan": "Semangat terus berkarya kak!",
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
                "pesan": "Tetap semangat dan sukses selalu!",
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
                "pesan": "Sukses terus perkuliahannya kak!",
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
                "pesan": "Semangat terus ya kak!",
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
                "pesan": "Sukses selalu buat perkuliahannya!",
            },
        ]

        display_images_with_data(gambar_urls, data_list)

    departemen_minbak()

if menu == "Departemen SSD":

    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QEUHUaN_dGhgTuA5nvivmU_KzEK9v1J2",
            "https://drive.google.com/uc?export=view&id=1Owf1TBgzAQB3gPzioiivO6jl2tYaMcym",
            "https://drive.google.com/uc?export=view&id=1sYfhXWQUoiyEp67N4Czp3a19hYZA60Ag",
            "https://drive.google.com/uc?export=view&id=1TwsIuS5Sl-yWkM_1ZS3NRoONSHvVMufJ",
            "https://drive.google.com/uc?export=view&id=16O85y4s3Q53hGyAfSNJqwkFbKMw6wvj7",
            "https://drive.google.com/uc?export=view&id=1eh8of4BlGxSssEg3w1hUdOK33li1XdjU",
            "https://drive.google.com/uc?export=view&id=1h7SMMOYRPVGVCICKFpNYFUo-5-AJ02Yf",
            "https://drive.google.com/uc?export=view&id=121QMttPCldvK3X9_9uuZ_S8vefNVJyAB",
            "https://drive.google.com/uc?export=view&id=1ogN6eKKhQg9F0K_r3UYelBMk8nPnUsMn",
            "https://drive.google.com/uc?export=view&id=1bFUSmM1KjQ8khwI9C10Gi6bCD62PiJwA",
            "https://drive.google.com/uc?export=view&id=1wkAWCeMTy3HpCk7XgkDRYiFUVMrdAwPa",
            "https://drive.google.com/uc?export=view&id=1GElwoyB_a3_Q9YQOoVhtFghuDXjySldb",
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
            # --- Divisi Kewirausahaan ---
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
                "pesan": "semangat terus kuliahnya kakak !!!",
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

elif menu == "Departemen Eksternal":
    def eksternal():
        st.markdown("<h3 style='text-align: center;'>Departemen Eksternal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Hubungan Luar", "Divisi Pengabdian Masyarakat"])

        with tab1:
            gambar_urls_Kadep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1dcttpmEvapTkf3--jzW9KO8mCBYlo6u8",
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
                "kesan": "Kakak nya tegas tapi baikk bangettt seruu",
                "pesan": "Semangat dan suksess teruss ka kedepannya"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1hFUIF5msavl-xX5pZjSoSCeTYzplyvYh",
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
                "kesan": "Kakak cantik, imut, baikk bangett ",
                "pesan": "Semangatt teruss kaa nab disemester yang super duper hectic ini, maafin erbe kalo suka ribut pas praktikum adees tercinta"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [            
            "https://drive.google.com/uc?export=view&id=1wNkwUVM7B50ixxiOCvRhCbpM9K0posMd",
            "https://drive.google.com/uc?export=view&id=1h2vS7F-uFdmXxNcP3KAQkFi2G8q6Hkal",
            "https://drive.google.com/uc?export=view&id=1PslCrtV6VKuhKrMyO_U9x5QejwFqbLYr",
            "https://drive.google.com/uc?export=view&id=192a84EIV9FAF-20f1N4N9Ou4MGLoAmtT",
            "https://drive.google.com/uc?export=view&id=1ni0cA91ToQSGRGtVWAPnV2Gp6k_9q2F5",
            "https://drive.google.com/uc?export=view&id=1D9Mbm4GOfjy9PHQaPB4PObRZIB_o7lot",
            "https://drive.google.com/uc?export=view&id=1fsRJHzq6LOHjG2CcPkOhGJBY1585_4hV",
            "https://drive.google.com/uc?export=view&id=1boLr-SzbzVJ8LKqd5Bg6nCmkk5Zx2Lts",
            "https://drive.google.com/uc?export=view&id=1JJ1sXOr56xFS3udIF7FAZIdsSd7BgAKT",
            "https://drive.google.com/uc?export=view&id=1C_fuX0dELgk7tZLIRIa4l3RwrewdJgfA",
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
                "kesan": "Ka mutt keren,mantap, gacor bgtt seruuu",
                "pesan": "Semangat kaa exvoltas dan kuliahnya, semoga lancar selalu kaaa"
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
                "kesan": "KERENNNN BANGETT BANG",
                "pesan": "Semangat teruss bangg dan sehat selalu"
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
                "kesan": "Kak dindaa baik ramahh",
                "pesan": "Semangat selalu di semester yang banyak gedebag gedebug ini kaa"
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
                "kesan": "bang bimo baikk dan ramah",
                "pesan": "Semangat terus bang kuliahnyaa, jaga kesehatan juga!!"
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
                "kesan": "bang alfa baikk, asik, seru orangnya",
                "pesan": "Semangatt buat rd eduvisit nya bang, kataku sih mending tolnya pas pulang aja yakann"
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
                "kesan": "Aduhh ibu peri ini..baik,suka menolong dan rajin menabung",
                "pesan": "KAKK MEII semangat kuliah nya, sehat selalu, semogaa kkn nyaa lancarr yaa kaaaa!!"
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
                "kesan": "Bang abim baik kok, ramahh bgt bintang 5 ga boong",
                "pesan": "Semangatt terus bang semoga semua yang lagi dikejar dilancarkan semuanya, jaga kesehatan nya dan tolong tips n trick menjawab adees bang help "
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
                "kesan": "OEMJII KAK INDAHH kakaknya baikk, ramah, lucu, imupp, suka tolong menolong antar sesama",
                "pesan": "Kakk indah jangan marah marah lagi ka, SEMANGATTTT TERUSSS KAKKK DISEMESTER YANG PENUH HURU HARA ENIHH..tenang aja ka TO dan anmulnya masi bisa dibales di UAS kak SEMANGATTT"
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
                "kesan": "Gemass,baikk,ramahh bgt",
                "pesan": "Ka riska semangatt kuliahnyaa ditengah ke hectic an semester 5 ini jaga kesehatannya ya kakk"
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
                "kesan": "Kak yol aktif bgt dikepanitian, baikkk jugakkk",
                "pesan": "Semangat terusss yaa ka yoll, jaga kesehatannyaa jujurr kakak kerennn BANGETT"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1TVMgVQCI7zOWQ2zsirF9tIFYua6C3L9E",
            "https://drive.google.com/uc?export=view&id=1vf_P3Gnn3q492ZCPDvwsydGsn1CmkJDm",
            "https://drive.google.com/uc?export=view&id=1brubxTdnMgZEoVVK5Btj5Zac-CkcmQZf",
            "https://drive.google.com/uc?export=view&id=1QsuXBrM3KfvG76iD5xpLViMS8UQ25pS0",
            "https://drive.google.com/uc?export=view&id=1Wu-Ebsk1JG6_AnTjMN7ZwXeiBIDENrZN",
            "https://drive.google.com/uc?export=view&id=1DRgFy_nSIVYeWTuYeslmDDXXKliewsT1",
            "https://drive.google.com/uc?export=view&id=1iRRsvRfIjAjeSuZ_sa_K7z7jygOBUeQi",
            "https://drive.google.com/uc?export=view&id=1INF-HqCreUkgS9aLeh7DbxgRWCPpozJs",
            "https://drive.google.com/uc?export=view&id=1t29uzZgNfPdh6kCxmnPFUyY-9X7B2ThV",
            "https://drive.google.com/uc?export=view&id=14pHQbGCJi8ZVUcUKq4jDLzITddV6Avbr",
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
                "kesan": "Baik, ramah abangnya seruu",
                "pesan": "Semangatt yaa bangg disemester 7 inii!"
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
                "kesan": "Asikk kakak nya seruu baik juga",
                "pesan": "Semangattt teruss kaaaa semoga TA nya dilancarin yaa"
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
                "kesan": "Baik seruu dan ramah ",
                "pesan": "Sukses selalu dan dilancarin semuanya yaa kaa"
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
                "kesan": "Ramah asik dan baikkk",
                "pesan": "Jangan lupa istirahat ya kaa, semangat kuliahnya"
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
                "kesan": "Keren first impresionnya ramah disuru folow ig nya pas data pudi",
                "pesan": "Semangat kuliahnyaa bangg"
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
                "kesan": "Lucu abang nyaa baikk pertama kali kenal pas fg 2025 pas mau foto bang pian masuk frame wkwk",
                "pesan": "Kerenn bangg semangat dan selamat menikmati hari hari disemester 5 ini, nanti kita itung jarak itera-PTBA lagi"
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
                "kesan": "Abang nya baik kalau lagi ga marah marah jujur takut",
                "pesan": "Semangat kuliahnyaa ya banggg "
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Main layangan waktu hujan",
                "sosmed": "@jaldii._",
                "divisi" : "Pengabdian Masyarakat",
                "kesan": "Abangg nyaa seruuu bangeett,kadang suka asbun lagi",
                "pesan": "Semangat dan sukses selalu bang jaldi mengejar S.Si.D"
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
                "kesan": "Kakanya imut dan ramah",
                "pesan": "Semangat kuliahnyaa yaa kakkk sass jaga kesehatan jugak"
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
                "kesan": "Ramah dan cantikk",
                "pesan": "Semangat kuliahnya kak"
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
            "https://drive.google.com/uc?export=view&id=1Ee-k_6JWhJTGWBpTfDiMZ2OMkM3xyXUZ",
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
                "kesan": "Kakak nya cantik",  
                "pesan":"Semangatt teruss kaa di semster penghujung ini"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1RrrP9DYGp8kApCtU5jECSCMyuxkMBbh4",
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
                "kesan": "kakaknya galak tapi baikkk",  
                "pesan":"Semangattt teruss kaa semoga TA nya dilancarin"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/uc?export=view&id=1L1feTvQcGLLVbkFicnat1pusbaREPWpa",
            "https://drive.google.com/uc?export=view&id=17rCSNgHeqYyi8mO6HM-tHDdTI84MwW_Z",
            "https://drive.google.com/uc?export=view&id=1UopTTf-rhnjsLERTyvdAgOH0SflHmxJs",
            "https://drive.google.com/uc?export=view&id=1gQ9mlDpPEqrvgOy17w4KeqVbbo9dCnyt",
            "https://drive.google.com/uc?export=view&id=1gEbP46Ssj2a6oNme2JPwU6AhCk01Drjt",
            "https://drive.google.com/uc?export=view&id=1eajgUDjcoO21U6M445hlGBPPmjQNgQoh",
            "https://drive.google.com/uc?export=view&id=1miiOMIn84spni87yGpHzxDpx5rhiuTB3",
            "https://drive.google.com/uc?export=view&id=1HHmXmbu32F-3Exnh5c6KcvfKkgKLtdg7",
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
                "kesan": "Abang nya jago ngoding dari waktu BISA CYUKK",  
                "pesan": "Semangat kuliah nya bang, sukses selalu"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Serem kalo lagi marah marah",  
                "pesan":"Semangat selalu bang di semester 5 ini"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Seremm tapi bang yake baik",  
                "pesan":"Semangat terus ya bangg, lancar selalu urusannya"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Serem dari pas masi jadi  komdis",  
                "pesan":"Semangat terus bang, jaga kesehatannyaa!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Seru asik bgt dulu, sekarang serem kalo gi marah marah",  
                "pesan": "Semangat kuliahnyaa kaa menghadapi anmul itu"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "abang nya baik tapi serem kalo marah",  
                "pesan":"Semangatt bang kuliahnya, semoga kebaikan selalu melingkupi abang"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Sabang",
                "alamat": "Nomaden",
                "hobbi": "Duduk samping Henry",
                "sosmed": "@putrimannaa",
                "kesan": "takut tatepannya serem ey tapi baik pas itu aku sakit",  
                "pesan":"semangat selalu ya ka, semoga semuanya dilancarin apapun itu"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "first impresion kakaknya judes banget tapi ternyata baik bangett",  
                "pesan":"semangat kuliahnyaa dan jaga kesehatan kaa"# 1
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1RjtjbVXeJtHsE-B7Rd5dYG8q-kRbpNBJ",
            "https://drive.google.com/uc?export=view&id=1Oc_FuO3nQpAxpoSneE4TMJ5R94QK9OXf",
            "https://drive.google.com/uc?export=view&id=1kTR3jugyjI83mHSLcCsD11wQaa7rIQ1b",
            "https://drive.google.com/uc?export=view&id=1XTRKD0dLD1lTqWeR43si4HV9w9O_YXrk",
            "https://drive.google.com/uc?export=view&id=1itaLtWQj6x9J7cjUw0_t3C9XPTLQUBMT",
            "https://drive.google.com/uc?export=view&id=1XZB6xQOjxbbr6xxKCvTGo-zcPDgL33m5",
            "https://drive.google.com/uc?export=view&id=1TyKG4NFAt2zTrN-SM-BnOezWQjI_n1pr",
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
                "kesan": "Baik asikk banget, suka denger cerita dan masukan dari bang desman",  
                "pesan":"Sehat selalu dan semangat teruss ya bang di semester penghujung ini"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "Kakanya baik ramah juga",  
                "pesan":"Semangattt terus ka kuliahnyaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakanya ramah bangetttt",  
                "pesan":"Semangat selalu ya kaaa"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "Bang jemar ",  
                "pesan":"Semangat kuliahnya bangg, sehat sehat!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakanya baik dan ramah",  
                "pesan":"semangat selalu kaa kuliahnyaa"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Tembung",
                "alamat": "Belwis Tengah",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "abang mirip teman saya bang",  
                "pesan":"Semangattt menjalani hari hari di semester 5 ini bangg!"# 1
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "kakak nya ramah",  
                "pesan":"Semangat kuliahnya kakak cantik"# 1
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
            "https://drive.google.com/uc?export=view&id=1OXGszt6A8rUpkl9xzB_2xAb0Q6pGcwsy",
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
                "kesan": "JUJUR KEREN BANGETTTT, saya beneran perlu berguru dengan abang",
                "pesan": "Semangatt TA nya nanti banggg, tapi saya beneran butuh banget banyak belajar ke abang karena ilmu abang DAGING semuaaa"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1s2lwAWdsf-G9YISQS90lp54-Pu62pJBs",]
            data_list_sekretaris_mikfes = [ 
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
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1J7d6tipC56U4-3SfYIUUvh9HoBxvheGn",
            "https://drive.google.com/uc?export=view&id=1ImQ0gXGwohFHTi3cwIlUmoCmAJUbh8S6",
            "https://drive.google.com/uc?export=view&id=1xSWqGUiOcVDYFQTU2p34KT5fwvsTOKwI",
            "https://drive.google.com/uc?export=view&id=1w-Oh5snYg_CC7ahsZTG0IsZTYQJeT2BU",
            "https://drive.google.com/uc?export=view&id=1tteWOH9PzMjkBylNkVzbZlWVk5oHc7l9",
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
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Cantik dan ramah sekaliii",
                "pesan": "Sukses selalu kaa kedepannya, semoga apapun plan kakak bisa tercapai satu persatu yaa!"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            "https://drive.google.com/uc?export=view&id=1GMRiY2uPvxJ47TBO1SirVSl79Al6eY9c",
            "https://drive.google.com/uc?export=view&id=1nZ-Dfvhc80GsqZb37rN_GxDpZCWg8i_K",
            "https://drive.google.com/uc?export=view&id=1W0844H-BWn9wrf6plxcnSsJpA3ZZyJsh",
            "https://drive.google.com/uc?export=view&id=1BdqToXk8sJxJooeUBLhQ5jT4gNI5ZNZR",
            "https://drive.google.com/uc?export=view&id=1VP4m_xVmvF2E0ROLI_56iByj4sPkutkd",
            "https://drive.google.com/uc?export=view&id=1uS-8uwHUEuVfo0oaOv7InI10NuC7NooL",
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
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Kerennn",
                "pesan": "Semangat terus kaa capai impian kaka satu persatuu!"
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
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_Divisi_Research_Development = [
            "https://drive.google.com/uc?export=view&id=1GQvVyuLx0bXGWFLjid9g9RbIXC4A5Sri",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_d8XfSmg982uoxBMTWTUKsx0xlKvSnxp",
            "https://drive.google.com/uc?export=view&id=1hPVOO1spMGZVK7dsKtmQh4evT3Of6kxU",
            "https://drive.google.com/uc?export=view&id=1a1Rjjs1amQ5Yepf-3GklyLyprHUt7l74",
            "https://drive.google.com/uc?export=view&id=1_ujKPc6dlMo3U4sVeuvM0RygKePGnrzn",
            "https://drive.google.com/uc?export=view&id=1xXYlWbEo0v6gY6FOCJuNrGnvV49HJyYK",
            "https://drive.google.com/uc?export=view&id=1pl_DoKNJnrxBakihHxTnWfMZeUjcS9Fr",
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
                "pesan": "Kocak bangett dah, semoga hal hal baik selalu melingkupi hidup abang yaaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Research_Development, data_list_Divisi_Research_Development)
    mikfes()

elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kerenn",  
                "pesan":"Semangat TA nya bangg, semoga diberi kemudahan dan dilancarkan semua urusannyaa"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Cantik dan ramah",  
                "pesan":"Semangattt kaa untuk TA nyaa, jangan lupa jaga kesehatan yaa!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Positig energy bangettt",  
                "pesan": "Semoga kaka selalu dilingkupi oleh banyak kebaikan yaa, dan semangat nanti TA nyaa!"# 1
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhnghnii",
                "kesan": "Skill perkusi nya kerenn bangg",  
                "pesan":"Sehat selalu bangg dan semangat TA nyaa!"# 1
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Menulis wishlist",
                "sosmed": "@aisyahkhair",
                "kesan": "Kakanya gemas bangett dan ramahh",  
                "pesan":"Sehat-sehat ya kaaa!"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap Liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Lucuuu",  
                "pesan":"Sehat selalu kaa, dan semangat kuliahnyaa!"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal": "Kisaran City",
                "alamat": "Pemda",
                "hobbi": "Kick Boxing",
                "sosmed": "@jay.saputratmb",
                "kesan": "Asik dan ramah",  
                "pesan": "Semangatt kuliahnya bangg, semoga plan abang bisa tercapai satu-persatu"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Nonton ASMR",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakanya gemass bangett",  
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
                "kesan": "Abang keren dan ramah",  
                "pesan":"Semangatt bang menjalani perkuliahan dan proker himpunannya!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "My kaka tutorr",  
                "pesan":"Sumpah terimakasih banyak kaaa udah ngambil kesempatan untuk jadi astut LMD. Saya merasa terbantu bangettt. Maaf juga kemarin aku banyak diamnya pas tutor karena kebetulan waktunya berbarengan dengan wwc dan hal lainnya"# 1
            },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
                "kesan": "Abangnya ramah",  
                "pesan":"Semangattt bang kuliahnyaa!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Baik dan ramah",  
                "pesan":"Sehat selalu dan semangat kuliahnya kaa!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "@cikamrbn",
                "kesan": "Baik dan lucuu",  
                "pesan":"Semangatt kaa kuliahnyaa!"# 1
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakanya baik dan ramah",  
                "pesan":"Jangan lupa jaga kesehatan dan semnangat kuliahnya kaa!"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "@muhvinz_",
                "kesan": "Seruu abangnyaa",  
                "pesan":"Semangattt kuliahnya bangg"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nginep di rumah Yollanda",
                "sosmed": "@snasaa._",
                "kesan": "Anggun banget vibesnya",  
                "pesan":"Semangat teruss kaa kuliahnyaa!!"# 1
            },
        ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
    internal()


elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "KAKA KERENN!!",
                "pesan": "Jujur takjub sih aku untuk orang orang di bidang media kreatif, walaupun dikejar dl desain tapi masih tangguh sekali"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "KEREN JUGA JUJURRR",
                "pesan": "Tetap semangat terus ya kaaa, semoga apapun wishlist kaka bisa tercapai satu persatuu"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "divisi": "Dokumentasi",
                "kesan": "TAKJUB",
                "pesan": "Semangatt terus bangg kuliah dan organisasinyaa!"
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
                "kesan": "Gemes bangettt",
                "pesan": "Tetap semangat ya kaa walau beban tugas kaka sometimes cukup beratt!"
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "18",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "felisyanbl__",
                "divisi": "Dokumentasi",
                "kesan": "Kerennn",
                "pesan": "Jaga kesehatan selalu kakaa, jangan lupa bahagia jugaa!!"
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "124450031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "muh_razan_",
                "divisi": "Dokumentasi",
                "kesan": "Kerennnnn",
                "pesan": "Semangattt terus banggg!! sempetin waktu untuk abang istirahat sejenak dari organisasi dan perkuliahan yaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Ramah sekaliii",
                "pesan": "Semangattt ka kuliah dan organisasinyaa, sempatin waktu untuk self reward yaa"
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
                "kesan": "My kaka cantik, ramah, and imutt",
                "pesan": "Terus bahagia ya ka Allishaa!"
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "091",
                "umur": "19",
                "asal": "Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu roda",
                "sosmed": "alya.rmdhnti",
                "divisi": "Media dan Konten Speasialis",
                "kesan": "Gemass",
                "pesan": "Kakanya ramah bangett, semoga kaka selalu dikelilingi oleh hal hal baik yaa!"
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
                "kesan": "Ramah bangettt",
                "pesan": "Semangatt ka kuliah dan organisasinyaa, jaga pola makan dan jangan stress-stress yaa"
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
                "kesan": "Lucuu",
                "pesan": "Semangattt teruss ka kuliah dan organisasinyaa, sempatkan waktu untuk rehat sejenak yaa"
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
                "kesan": "Gemass",
                "pesan": "Semangat selalu kaa kuliah dan organisasinyaa"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semangatt kuliah dan organisasinya kaa, jangan lupa berbahagiaa!"
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
                "kesan": "Baik banget abangnya",
                "pesan": "Semoga abang selalu dilingkupi oleh kebaikan"
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
                "kesan": "Kerenn",
                "pesan": "Jangan lupa jaga kesehatann dan jangan lupa berbahagia"
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
                "kesan": "Kakanya asik",
                "pesan": "Sehat selalu kaka"
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
                "kesan": "Kakanya baik dan ramah",
                "pesan": "Semangatt terus ka, semoga selalu berbahagiaa"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "Xifasky",
                "divisi": "Media dan Konten Spesialis",
                "kesan": "Cantik dan ramah sekalii",
                "pesan": "Semangattt kaa untuk kuliah dan organisasinyaa!!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()