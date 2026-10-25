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
    st.markdown("<h3 style='text-align: center;'>Kesekjenan</h3>", unsafe_allow_html=True)
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1twhP1U_DdBCpEx6b7-0vq6CL9OZytjDC",
            "https://drive.google.com/uc?export=view&id=11uG-ovObNWpUqptHqFoaA1y6slz0Bzl5",
            "https://drive.google.com/uc?export=view&id=1_hcR8JrfC1f8xVi1PFowPUnCh0vMXZwz",
            "https://drive.google.com/uc?export=view&id=1k36lXwVGs5ljYjl_dcKK1qPr6iBm8GHS",
            "https://drive.google.com/uc?export=view&id=1Kvp6HnZy2JX2eSACSsz83r4zqI6RCLdD",
            "https://drive.google.com/uc?export=view&id=1l0qNaH-rtBQnHUs7rWxDHoU2UkPVQBzv"
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
            "pesan":"Terimakasii bang udah melalukan banyak perubahan dalam kinerja himpunan di kepemimpinan abang. Selanjutnya semangatt bangg nyusun dann ngerjain TA nyaa, semoga dipermudah segala urusan dalam per TA an ini ya bangg. Aamiin"# 1
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
            "pesan":"Kerennn, setelah ini semangatt nyusun TA nyaa, semoga diberi kelancaran dan lulus secepatnya ya bangg! "# 1
            },
            {
            "nama": "Efi Defiyati",
            "nim": "123450005",
            "umur": "21",
            "asal": "Lampung Timur",
            "alamat": "Airan",
            "hobbi": "Membaca",
            "sosmed": "@eeffiidefi",
            "kesan": "Charismatic woman #TAKJUB",  
            "pesan":"Keren bangetttt, semangatttt kaa ngerjain dan nyusun TA nyaa, semoga diberi kelancaran dan kemudahan sampe selesai nantii. Aamiin"# 1
            },
            {
            "nama": "Qois Olifio",
            "nim": "123450067",
            "umur": "22",
            "asal": "Batam",
            "alamat": "Kota Baru",
            "hobbi": "Mainin Surat",
            "sosmed": "@qoisolifio_",
            "kesan": "Ngurus persuratan jujur keren bangettt",  
            "pesan":"Semangattt bang untuk TA nantii, semoga diberikan kelancaran dan kemudahan sampe usai #aamiin"# 1
            },
            {
            "nama": "Hafsa Fazila Arradhi",
            "nim": "123450079",
            "umur": "21",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Berenang",
            "sosmed": "@hafsafazilaa",
            "kesan": "Vibesnya ceria bangett",  
            "pesan":"Kereennn, semangat kakaa untuk selanjutnya dan semoga diberi kelancarann dan kemudahan dalam menyusun TA nanti. Aamiin"# 1
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
            "pesan":"Tetap ceria terus ya kaa, semoga kaka selalu dikelilingi hal baik juga karena kaka orang baik. Semangatt ka nanti nyusun TA nyaa, smeoga diberi kemudahan dna kelancaran, aamiin"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan
if menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg= [
            "https://drive.google.com/uc?export=view&id=1_BG2EUX_gvYG3PZYMd227eTMCmsbAs4F",
            ]
            data_list_kabaleg = [
            {
            "nama": "Ridho Benedictus Togi Manik",
            "nim": "123450060",
            "umur": "20",
            "asal":"Kota Manchester",
            "alamat": "GH",
            "hobbi": "Wawancara",
            "sosmed": "@iamridhomanik",
            "kesan": "SERU BANGETTT!!! abangnya beneran lucu terus celetukannya, beneran pabrik jargon hahaha",  
            "pesan":"Yahhh di periode selanjutnya orang keren dan berbakat ini udah demis. Btw semangat bang TA nyaa, semoga dilancarkan semuanya dan lulus tepat waktu ya bangg. Anak magang baleg selalu mendoakan yang terbaik untuk abang"# 1
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1a47pGM3ukNaWR_L8YRZZQjyy0POALQG-",]           
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "GEMASSSSS! beneran imut kakanya dan seru banget dengerin storytelling ka juee, karena cara ka jue bercerita kayak sivia the catchup club",  
            "pesan":"Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1CSLAfADxtOChcPhZuHB-RoAhrTONQ1xs",
        	"https://drive.google.com/uc?export=view&id=1-nEDfGpB1Ex_lulubyV-sxtp-miQ60HU",
        	"https://drive.google.com/uc?export=view&id=1_EasNsQ2LHV0tzM8pKg-zhcu6UtcjNsz",
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
                "kesan": "Masyallah, pinter banget abangg, tips and trik mapres bangg",  
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
                "pesan": "Semangat terus kuliah dan organisasinya! Dan selamat atas terpilihnya jadi Kabaleg, abang beneran deserve atas hal tersebut #KERENNN. Nanti jang terlalu dibawa stress ya bangg!"# 1
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
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
        	"https://drive.google.com/uc?export=view&id=1YTPcDC13TrQSBhVAgLy_99OMSug3HWPR",
        	"https://drive.google.com/uc?export=view&id=1HTezkZLq5nueWyFseF7eeK52O7v3O8jc",
        	"https://drive.google.com/uc?export=view&id=1laO1Z0qPKd37fHRwfsykQFFBPqpgeqCL",
        	"https://drive.google.com/uc?export=view&id=10_2urUzNjE71abWnmR2ff2c7k9QL732m",
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
                "pesan":"Semangat bang kuliahnyaaa! Jangan lupa jaga kesehatan!"# 1
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
            "https://drive.google.com/uc?export=view&id=1yEVd7aXbYUoLLuKXli9FI3ZbXTTn1Adc",
        	"https://drive.google.com/uc?export=view&id=1Xw218qPJPAe84LVqXgaQ0jOreAddEgeI",
        	"https://drive.google.com/uc?export=view&id=1sILgZY2FesGpthVYI-Tf8Bw3IqiII7YE",
         	"https://drive.google.com/uc?export=view&id=1ZfIx7ijEVXQlZ-0UZEelV8IBgqHhIhua",
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
            "kesan": "Lucu, gemas, tapi tegas",  
            "pesan":"Semangat kaa kuliah dan organisasinyaaa, dan semoga diberikan kemudahan dan kelancaran dalam mengerjakan TA nya, aamiin!"# 1
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "Lucu abangnya, jokes jokesnya juga fresh, terus juga merangkul anak anak magang",  
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
            "pesan":"Semangat kaa TA dan kuliahnyaa! Semoga diberi kemudahan dan kelancaran sampai selesai nantii, Aamiin!"# 1
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
            "https://drive.google.com/uc?export=view&id=1aZHCXplW5SpgmlWsgEJ9CMz-Cc63zP72",
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
                "kesan": "Inspired girl, beneran keren bangettttt",  
                "pesan": "Salam Jaktim Pride kaa, btw Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)

        with tab2:
            gambar_urls_biro_aspirasi= [
            "https://drive.google.com/uc?export=view&id=1s4Y_J-WUNOKKX-T3d-K_4JN9xKSiD9PP",
            "https://drive.google.com/uc?export=view&id=15WmvhPmC_uVDyMKeLCGKgMu__ebyVphl",
            "https://drive.google.com/uc?export=view&id=1ckA1gO2M6n0FrBpBNCD-fWzO-0N1kH2L",
            "https://drive.google.com/uc?export=view&id=1uiN1uIUJVliOkeWtqFj8Mw_zMoZV4r27",    
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
                "kesan": "Duta melet, lucuuuu",  
                "pesan":"Lucu bangett abangnyaa, semoga abang selalu dikelilingi banyak hal baik yaa"# 1
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
                "pesan":"Abangnya beneran baik banget, selanjutnya semangattt bang kuliah dan organisasinyaa!"# 1
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
                "pesan":"Semangat terus kak kuliahnya! Jangan lupa jaga kesehatannya ya kaa!"# 1
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
                "pesan":"Semangat terus bang kuliahnya! Jaga kesehatan juga yaa!"# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)

        with tab3:
            gambar_urls_biro_kajian= [
            "https://drive.google.com/uc?export=view&id=1OHlSd2BkSICOJiXU_jnPX75Ro7FW63m9",
            "https://drive.google.com/uc?export=view&id=1Dwm4V6jDHF3WKWUxLk7jDcPMgsvzPpo_",
            "https://drive.google.com/uc?export=view&id=15MiDZ0sw9gk5bvcEhJspcOwbzYKvtxoz",
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
                "pesan":"Semangat terus kuliahnya kaa! Semoga kebahagiaan selalu melingkupi kakaa, karena kaka orangnya ceria dan menyebar energi positif #LUV"# 1
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
                "pesan":"Semangat terus bang kuliah dan organisasinya! Semoga abang selalu dikelilingi oleh hal baik yaa!"# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)

        with tab4:
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1ffC4TPfM-HOkmrWTgc6Bag9v_QJ5QKzK",
            "https://drive.google.com/uc?export=view&id=1yCJoXNgAfsawHBucCZa9_l90LxcIV76n",
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
                "kesan": "Welcome sekali kakanyaaa, dan cara penyampaian materinya juga mudah dipahami",  
                "pesan":"Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
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
                "pesan":"Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
            }
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_kesekretariatan)
    Bason()


elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown("<h3 style='text-align: center;'>Departemen Minat dan bakat</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4= st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])
        
        with tab1:
            gambar_urls_kepala_departemen_minbak= [
            "https://drive.google.com/uc?export=view&id=1qJRwzD08676Djt3ZV2UqPS2dovnOT8oG",
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
            "pesan": "Semangatt terus bang kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)


        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1GdBBgsyjIvSDtfb8pzn8IwkOImLD07dC",]
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
            "pesan": "Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1            
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)            

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [            
            "https://drive.google.com/uc?export=view&id=1927jQfW7yeV28jMyGY4iOyVSb6cRSEIC",
            "https://drive.google.com/uc?export=view&id=1EHcJPQvp7pYCjY84_rT7n-0FGzPHGgX3",
            "https://drive.google.com/uc?export=view&id=1E3h2Eb0yUqNMRZBEXLcODGW2-54ObXIV",
            "https://drive.google.com/uc?export=view&id=1zVSku7Mki4SCfdcoxQ0H1LI2DeuXEhBy",
            "https://drive.google.com/uc?export=view&id=1sd6e1uQ6lPt-4o7NlVqWQ48BR8yAHP27",
            "https://drive.google.com/uc?export=view&id=1jE2zDYlM8eOeChu5rmuSrcPSdKSBqhBH",
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
            "pesan": "Semangatt terus bang kuliah dan TA nya, semoga dimudahkan segala urusannya yaa, aamiin"# 1
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
            "pesan": "Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
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
            "pesan": "Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
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
            "pesan": "Semangat terus kuliahnya kaa, semoga kaka selalu diberikan kemudahan!"
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
            "pesan": "Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
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
            "pesan": "Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
            "https://drive.google.com/uc?export=view&id=1VkzXQDX7NJAUdHe2lSlR_Dd5fRB1t55z",
            "https://drive.google.com/uc?export=view&id=1WVVqSEsZl5Ff8ZYKZ3WGGImqzQdnqii4",
            "https://drive.google.com/uc?export=view&id=1a2PpAAvwiHfXVB12iokm8v0bZd2Y9fU9",
            "https://drive.google.com/uc?export=view&id=1mhystJqbH-IjE1aQ8pide77J-GaMJxgv",
            "https://drive.google.com/uc?export=view&id=1aAc-S_iT5iOsZz1ciGc0a8hw585guFZu",
            "https://drive.google.com/uc?export=view&id=1pixd5qOn7Nxgdv3T2jpk0emLtw5lK8oG",
            "https://drive.google.com/uc?export=view&id=1R3sGTA6wb1LNIPRAoTCGvjT2qOoBiNCc",
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
            "pesan": "Semangat terus memimpin divisinya kak! dan Semangat juga nanti nyusun TA nya, semoga diberikan kemudahan dan kelancaran sampai usaii, Aamiin"
            },
            {
            "nama": "Andra Ilham Bintang",
            "nim": "124450060",
            "umur": "18",
            "asal": "Sumatera Selatan",
            "alamat": "Kotabaru",
            "hobbi": "Main rubik",
            "sosmed": "@andra.lhm",
            "kesan": "Baik, gemass #abangimup, mengayomi anak anak gwidi, terbaikkk",
            "pesan": "Semangatt terus ya bang Andra kuliah dan organisasinya, jangan lupa kasih jeda untuk diri abang istirahat dari padetnya jadwal, dan saya harap abang selalu dikelilingi oleh hal baik karena abang pun orang baik jadi abang deserve semua hal baik di dunia ini-!"
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
            "pesan": "Semangat terus berkarya kak! Jangan lupa jaga kesehatan!"
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
            "kesan": "Sangat baik dan bersahabat",
            "pesan": "Sukses terus perkuliahannya kak! Semoga kaka selalu dikelilingi oleh hal baik jugaa"
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
            "pesan": "Semangat terus kaa kuliah dan organisasinya! Jaga kesehatannya di era perkuliahan dan organisasi yang serba padet jadwal"# 1
            },
            {
            "nama": "Muhammad Rafka Fatih Ghathfaan",
            "nim": "124450089",
            "umur": "20",
            "asal": "Padang",
            "alamat": "Kotabaru",
            "hobbi": "Bangun pagi",
            "sosmed": "@muhammdrafka_",
            "kesan": "Sangat disiplin dan dapat diandalkan",
            "pesan": "Sukses selalu buat perkuliahannya! Kasih jeda untuk diri sendiri istirahat ya bang"
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
            "https://drive.google.com/uc?export=view&id=14jFxHpSiQQ-ZdlNPkNn_8JVfcQnGWSvQ",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1ofji2_iq8G4OYsOSs-x2YyQwDp8yOo0A",
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
                "kesan": "Kakak ini asik saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1n0LUuor4_bwmz1QQc8d3k9OLVseEyq_w",
            "https://drive.google.com/uc?export=view&id=1O5a59ai8q_NG4no9v5G5_HnAoHfdwMPr",
            "https://drive.google.com/uc?export=view&id=1HQPg7YwlSRWNirdyumo3VX9HjnLuximV",
            "https://drive.google.com/uc?export=view&id=1AQpRKL0whGttOVWlKqKOeEsT0S6hOpiJ",
            "https://drive.google.com/uc?export=view&id=1L3TyKqZF8i_mh629DreTdRKhuhcesVKc",
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
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1zn2md_RpQ_OCbZrHqL9TX_VR4jpMDDoE",
            "https://drive.google.com/uc?export=view&id=1A6ZSNaUPfZHIi951OzfoSXl-NnSreAXf",
            "https://drive.google.com/uc?export=view&id=1qGm0nwmxknY3RFjpqsYVvgWTUkHD-imo",
            "https://drive.google.com/uc?export=view&id=13uaveV1UZw6w_VG8eSlHYxgCU7tl72Ix",
            "https://drive.google.com/uc?export=view&id=1fMgJJIrNWierk4biwSqw7D9qzs77jrD8",
            ]
           
            data_list_kewirausahaan = [
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
            display_images_with_data(gambar_urls_kewirausahaan, data_list_kewirausahaan)
    ssd()


elif menu == "Departemen MIKFES":
    def mikfes():
        st.markdown("<h3 style='text-align: center;'>Departemen Akademik dan Keprofeisan</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Professional Skill and Development", "Divisi Pusat Inovasi dan Kajian Akademik", "Divisi Research & Development"])

        with tab1:
            gambar_urls_kepala_departemen_mikfes= [
            "https://drive.google.com/uc?export=view&id=183k16AoHkTUktFlI3AZ1_W-MbtNMEA3k",
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
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1gMvVn8mtfgamx9T7ERggSnaRMclwyLy8",]
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
            "https://drive.google.com/uc?export=view&id=1pHe1ymk1ky1yVe8oRPDHB6i2w7f_3QIa",
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
            "https://drive.google.com/uc?export=view&id=1f_2ggNOXI0RS23gtDUytScYXxE_USU-q",
            "https://drive.google.com/uc?export=view&id=1YBGIgwOg0A55qju5mB7VjX37I4R-DW2L",
            "https://drive.google.com/uc?export=view&id=1wCeXyFM2Ke3C-Wtkt6gVr6a_MRO8Qsue",
            "https://drive.google.com/uc?export=view&id=12G_wnWsKMrhhGTYRy_PDioQWtKY8ePDM",
            "https://drive.google.com/uc?export=view&id=1UorSEpoTGfKxwuFxYOASOiNsI1eAQJqe",
            "https://drive.google.com/uc?export=view&id=1f6la1Sts8od4yXwrsk2CSnH7OKMCzHgV",
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
            "https://drive.google.com/uc?export=view&id=1gnWMdoOZ8VdPPDtB16kO2C1wao9EacGi",
            "https://drive.google.com/uc?export=view&id=1MZeJ6i-kxlql0Qufe7ybp8Pxzf0aTq3h",
            "https://drive.google.com/uc?export=view&id=1RovSz6KLqvkodHtt2OhB4LlVI2Ry2AJe",
            "https://drive.google.com/uc?export=view&id=1NNCMcdTACb9SbvhBhTL117BV7VxLgZtL",
            "https://drive.google.com/uc?export=view&id=1BcPSYbRBepnkT4wj69nyqKr83YgH8i3G",
            "https://drive.google.com/uc?export=view&id=1OJT24OYBkSjm1nSBMk_czxfDcDC_lg6H",
            "https://drive.google.com/uc?export=view&id=1hyVOpdSHBJ14uHGnlE0oBmNQeQyawJvJ",
            "https://drive.google.com/uc?export=view&id=16yGIaMQSo42fALYk7pAQfjWANWhWkrmL",
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
                "pesan": "Kocak bangett dah, semoga hal hal baik selalu melingkupi hidup abang yaaa, aamiin!"
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
            "https://drive.google.com/uc?export=view&id=1yY0UcwW0OGe_wjFslLfXidx_p4gdgLtM",
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
            "https://drive.google.com/uc?export=view&id=1iMWWQ-gfJ9Js44b-4WAN1X8jUt0MqhgO",
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
            "https://drive.google.com/uc?export=view&id=14qKtE3QEiRqY0jIFfdDtCSJ40uLRf3LR",
            "https://drive.google.com/uc?export=view&id=1kSzlnSY5d-sk13sjDAJJgCGxb53ZLWog",
            "https://drive.google.com/uc?export=view&id=1zZjq_bHdB3TPOYicpBQwfpv7-TTPoDmV",
            "https://drive.google.com/uc?export=view&id=1mPpQTVwD8gHg3EWuKGhXrm3r6wZB8st5",
            "https://drive.google.com/uc?export=view&id=19Ha4jsx1tN59eAYslpGxJ3HLVLtSjTNu",
            "https://drive.google.com/uc?export=view&id=1ulrI05TtdAZL09sCYfN8AguuPDnwMoOI",
            "https://drive.google.com/uc?export=view&id=14gSC9XO8GLBYL9fp0QRkAafgY0h_XPxy",
            "https://drive.google.com/uc?export=view&id=1vFJx5bFIWHeD-YB6nNOm8IGqXet75nTQ",
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
            "https://drive.google.com/uc?export=view&id=1sx2Hz8O11RR8guj4Dyfp17e1MK1O5jPI",
            "https://drive.google.com/uc?export=view&id=15VRnLJylZ7-BY__0NVK_QkoUeN1GH3Bp",
            "https://drive.google.com/uc?export=view&id=1oVOvVdDEK7E114Td1MiAMJ1ShCRrqClT",
            "https://drive.google.com/uc?export=view&id=1tPs7lmZuffjQJAEqDr7x0yMtiGZUHtn2",
            "https://drive.google.com/uc?export=view&id=1KrXtjMm7GSnzQdnRj9FVaapxIczGvpm5",
            "https://drive.google.com/uc?export=view&id=1M_XC2r0wW-u2C76N8VfdKMkEd2E3Kqcv",

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

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
            "https://drive.google.com/uc?export=view&id=153egJP5i9qz2r7v2CKyXgsdi-UlttKIF",
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
                "kesan": "Cantik dan fashionable",  
                "pesan":"Semangat TA nya kaa, semoga diberi kemudahan dan dilancarkan semua urusannyaa"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1NXugTSOY-v_BtWkdKdohyXlsNxd8kCf9",
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
                "kesan": "Orangnya tegas",  
                "pesan":"Semangattt kaa untuk TA nyaa, jangan lupa jaga kesehatan ya kaa!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/uc?export=view&id=1OBBZKNv4psX_BOu0N4UIop3WBtu2WYXQ",
            "https://drive.google.com/uc?export=view&id=19nT5Io7fK6aJdvYuy_9Z1yP11znF9jCb",
            "https://drive.google.com/uc?export=view&id=1m5pMnXkV4Bpi_OyFS9E6sJKbrwmH_bty",
            "https://drive.google.com/uc?export=view&id=1rXtWe6248SSP-i9hweUM_nX19Dq88TTg",
            "https://drive.google.com/uc?export=view&id=1UHCxZ-14Caq8duvc_dR1gl37ftwMlR6I",
            "https://drive.google.com/uc?export=view&id=1oiK6KPStWdR5aWjgglM4sO9baYMsSOyj",
            "https://drive.google.com/uc?export=view&id=182mgFTgY4NAWYGRgee3jPD0E03WrCILf",
            "https://drive.google.com/uc?export=view&id=1KGrumBz2cAsB1guZPgROqOqQ8fDqRHnV",
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
                "kesan": "Abang kalau ga marah beneran lebih berkharisma, btw materi kader yang disampaikan abang beneran ilmu daging",  
                "pesan": "Semoga abang selalu dilingkupi oleh banyak kebaikan yaa, dan semangat nanti TA nyaa!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "aduhai abang nim ku timder, jujur kaget ga ekspek para abang nim ku orang-orang penting #PRESSURE",  
                "pesan":"Jangan marah-marah mulu bang, btw sukses buat selanjutnya #salampaguyuban110"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Galak tapi kadang baik",  
                "pesan":"Jaga kesehatan bang, kontrol emosinya biar ga jadi penyakit"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Kadang galak banget, kadang galak aja",  
                "pesan":"Jaga pola pikir bang, jangan stress-stress"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Ramah kalau ga marah",  
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
                "kesan": "Ini anak 24 emang suka ayam ya?",  
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
                "kesan": "Omelan kaka hinggap di mimpi saya sampe 3 hari",  
                "pesan":"Ga ekspek ternyata di luar 'itu' kaka ternyata ramah, saya kira memang pemarah"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "Kakanya soft spoken kalau ga marah",  
                "pesan":"Jaga kesehatan kaa, dan semangat kuliahnyaa!"# 1
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1wjiuj_258DE8sx3970aXBjVZjAHlIVJH",
            "https://drive.google.com/uc?export=view&id=1ZouY_InyWDJVSLHgqrputpUtrZ7ifed2",
            "https://drive.google.com/uc?export=view&id=12xpJFu_Ke2EeNVlfE6RIEpaIp6eo5rXD",
            "https://drive.google.com/uc?export=view&id=19i5eLiyk7slfw10Gaje9xA7wDtphVo2B",
            "https://drive.google.com/uc?export=view&id=1p1t4oMSSYDKisRnS-wYDXe63qK62d0VQ",
            "https://drive.google.com/uc?export=view&id=1RBRpOUeX2nDd-BhrkvioRqMonxjAcpBX",
            "https://drive.google.com/uc?export=view&id=105MFnanA0MFLcvjA8FHPo8mbQEgnNhpp",
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
                "kesan": "Asik dan seruu abangnya",  
                "pesan":"Semangatt TA nya nanti bangg, semoga dilancarkan segala urusannya!"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "Kakanya cantik and ramah",  
                "pesan":"Semangattt kaa kuliahnyaa! jangan lupa jaga kesehatan jugaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakanya baik and ramahh sekalii",  
                "pesan":"Sehat selalu dan semangat kuliahnya kaa!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "Abangnya tegas banget, tapi cukup welcome kalau di ajak ngobrol",  
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
                "kesan": "Baik dan asik",  
                "pesan":"Semangattt kuliahnya bangg!"# 1
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "Imut dan lucuu",  
                "pesan":"Semangat teruss kaa kuliahnyaa!!"# 1
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Peningkatan_Mutu_Anggota, data_list_Divisi_Peningkatan_Mutu_Anggota)
    PSDA()


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
                "kesan": "Karismatik woman, baik tapi tegas",
                "pesan": "Sukses selalu kaa kedepannya, dan nanti semangat nyusun TA nyaa!!"
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
                "kesan": "Cantik dan baikk",
                "pesan": "Semangatt kaa kuliahnyaa dan juga semangatt nyusun TA nya!!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [            
            "https://drive.google.com/uc?export=view&id=1xVBHbJxkymxCXI6MKj6DBiS4n9S51jlz",
            "https://drive.google.com/uc?export=view&id=1bOtboNzQUnQuWU3yPd5jtaOaNUUmENe8",
            "https://drive.google.com/uc?export=view&id=1I3e9ufUUa2SeQF7UeN7yezIf_l4OVQBS",
            "https://drive.google.com/uc?export=view&id=15pv1O1bhQKEGWhUkjqdTwdURzTqUF_Oo",
            "https://drive.google.com/uc?export=view&id=1Wxe1-cc8OAJitdOn4divJlNCLB7iEKP3",
            "https://drive.google.com/uc?export=view&id=1EtOAhb1iW2vi5ON5_J5UsOHDfiKRHbtX",
            "https://drive.google.com/uc?export=view&id=1Q0bfgvtRf52KGDtfg73jGykaAVcyYL5p",
            "https://drive.google.com/uc?export=view&id=16_6Hxh5BrrU6sdbhGA18ZDILJE-HleTW",
            "https://drive.google.com/uc?export=view&id=1HWpHXERG9xj-Ortt3qYfVd4LmTObYw24",
            "https://drive.google.com/uc?export=view&id=1oerpvhqKBLxrjWDAptSvaQCtiNUq4le_",
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
                "kesan": "Imutt",
                "pesan": "Semangat kaa nanti nyusun TA nyaa, semoga diberikan kemudahan dalam segala hal. Aamiin"
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
                "kesan": "KERENNNN!!! abang beneran jadi role model saya bangett",
                "pesan": "Jaga kesehatan bangg di negara yang ga sehat ini"
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
                "kesan": "Kakanya ramah dan baik",
                "pesan": "Jaga kesehatan kaa, dan semangatt kuliahnyaa!"
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
                "kesan": "Keren dan ramah",
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
                "kesan": "Kerennnn",
                "pesan": "Semangattt bang kuliahnyaa, jaga kesehatan jugaa!"
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
                "kesan": "Baik dan lucuu kakanyaa",
                "pesan": "Sukses selalu kak untuk ke depannya!!"
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
                "kesan": "Kerennn, baik dan ramah",
                "pesan": "Semangatt terus bangg kuliahnya walau makin tambah semester makin nambah juga stressnya. Jaga kesehatan jugaa!"
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
                "kesan": "Baik dan lucuu",
                "pesan": "Kakk jangan ikut marah-marah kaa, kaka versi medis beneran terbaik banget"
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
                "kesan": "Gemass",
                "pesan": "Jaga kesehatan ya kaa, dan semangat juga kuliahnya!!"
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
                "kesan": "Semangatt terus ka yollandaaaa, kak yollanda keren hebat and kuattt",
                "pesan": "Jaga kesehatan ya kaa, apalagi kaka ambil banyak kepanitian. Jangan sampe drop kaa"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1QwtLVj7LbCImanpLeT3BjBnwNWwH2zNh",
            "https://drive.google.com/uc?export=view&id=19pYqYKE24bNxABF5c2DZN3vshDqYodK4",
            "https://drive.google.com/uc?export=view&id=1Fb2pod6Pd1kcsbe-rpyHDfz1-6nmixTr",
            "https://drive.google.com/uc?export=view&id=1-ylGqoH5ix1iXPT0OUOsTOqoGi7QkGtA",
            "https://drive.google.com/uc?export=view&id=1sq_JPdYFDoRpRK0PjT4mLNjGk5iSCoGA",
            "https://drive.google.com/uc?export=view&id=11l2tKMnP74bIQZImA8jejzO6ojY_50ja",
            "https://drive.google.com/uc?export=view&id=1zFgKAhODhHunfbxIuLM3q8RUj2zlz763",
            "https://drive.google.com/uc?export=view&id=1HC78n-R52FfVX820vhbq0to1lzalcn1z",
            "https://drive.google.com/uc?export=view&id=1vDtAWkEdxpXvoCzI_Lk6WVcIgFvbynSk",
            "https://drive.google.com/uc?export=view&id=167SM0igqIGQlquzXc_LRHi00jWtx0utO",
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
                "kesan": "Baik, ramah, dan welcome bangett",
                "pesan": "Semangatt bang ngerjain TA nya, semoga selalu dipermudah langkah selanjutnyaa, Aamiin!"
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
                "kesan": "Keren banget kakanyaa",
                "pesan": "Jaga kesehatan ya kaa, dan capai imppian kaka satu persatu!"
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
                "kesan": "Manis dan imutt",
                "pesan": "Sukses selalu kaa untuk kedepannya, raih goals kaka satu persatu!"
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
                "kesan": "Cantik dan ramah",
                "pesan": "Jangan lupa untuk berbahagia ya kaa!"
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
                "kesan": "Keren dan baik",
                "pesan": "Semangat kuliahnya dan jaga kesehatannya bangg!"
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
                "kesan": "Mirip influencer si itu siapa namanya",
                "pesan": "Kerenn banggg, semangatt menjalani perkuliahan dan kehidupan #salambinjai"
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
                "kesan": "Abang keren kalau ga marah-marah",
                "pesan": "Panjang umur sehat selalu bang, tetep semangat kuliah walau setiap semesternya bikin asam lambung naik"
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
                "kesan": "KERENNN, jujur inspiring bangett",
                "pesan": "Semangattt terus bang jaldi gapai impian satu persatu!!"
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
                "pesan": "Semangatttttt kaa kuliahnyaaa! GO GOO!!"
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
                "pesan": "Vibes kakanya ceria dan positif bangett"
            },
        ]
            display_images_with_data(gambar_urls_pengabdian_masyarakat, data_list_pengabdian_masyarakat)
    eksternal()


elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1toyGw_Gqe_8nyFR3g6oBarBkuKasHGXj",
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
            "https://drive.google.com/uc?export=view&id=1wqd8jkmYbFetXDiZ4uJoJPscskvnsJJ2",
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
            "https://drive.google.com/uc?export=view&id=1rdaGXtpCkRJZqBP_gmtl_bcxGBhAaIqq",
            "https://drive.google.com/uc?export=view&id=1XwISeKq2Q0dR80M69zYC8J3OCXYguxhE",
            "https://drive.google.com/uc?export=view&id=1rFn5V-KAAd2xebw030JeUIH3DljIDyvi",
            "https://drive.google.com/uc?export=view&id=17utVb__mJqemjGxx89ESYVUdgXX1qvvQ",
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
            "https://drive.google.com/uc?export=view&id=1veteQPSdfI6Knp6HZ2p8ifSLOYA8o2H3",
            "https://drive.google.com/uc?export=view&id=19J8o10gjL94wkO633YyO3t0SkH17QyMy",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1wfS6bryh9_1kZp1xFi4Iz-Df8SVR9hyR",
            "https://drive.google.com/uc?export=view&id=1U5fH9zRe16gy2NulJy6VIuHDbO3kOMSP",
            "https://drive.google.com/uc?export=view&id=1wu0k16qiPhTzyBc-Do3lC8dcB1ders46",
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
            "https://drive.google.com/uc?export=view&id=1Zkxi_pD3RSKmCLQe81Q3GL-Jv1zo1wFP",
            "https://drive.google.com/uc?export=view&id=1sXTRNGI5OMry4kqsT9TmQSykXkqrImWI",
            "https://drive.google.com/uc?export=view&id=1kt1QcJnyrx0AVeZfw55xARHcG5XrQuYP",
            "https://drive.google.com/uc?export=view&id=1RbQRU_XR9Bzp1ujXO0gNBsPcuuOh7tKf",
            "https://drive.google.com/uc?export=view&id=1B1sgmVXyiw1Cvsyk6NoPGVot5wsLxYMK",
            "https://drive.google.com/uc?export=view&id=1ySeDAMEMtHYZoCW8ilVUGHRUp-KYJkeU",
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

