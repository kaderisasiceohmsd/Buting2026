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
            "https://drive.google.com/uc?export=view&id=1XVrHSuj9MdWm4xDvo1qHlRBo_iuzF6q6",
            "https://drive.google.com/uc?export=view&id=1_BgX-fzh2eRSelqbbPqCMqtY8agyYu-v",
            "https://drive.google.com/uc?export=view&id=18hajA2n1YVYJ6kTfN-kYOfLo-5DIxJ7m",
            "https://drive.google.com/uc?export=view&id=1IdQ2MQ2XWhdvnXQbaY1txbJnIvCTuMVy",
            "https://drive.google.com/uc?export=view&id=1yOTPHtGBYnlTDqwngS39rAWLjBO4ZJTR",
            "https://drive.google.com/uc?export=view&id=1vjM1xKeYCPd5JWLnNXdQqlyy0UcomTtU",
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
                "kesan": "Abang nya baikk, ramah jugaa, suka ngelucu jugaaa",  
                "pesan": "Semangat terus pokoknya baang"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya ramah, baik, asik jugaaaa",  
                "pesan": "Keep strong baaaanggg"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak nya budah baik ramah juga",  
                "pesan": "Semangaaat ka, semoga apa yang di diharapkan segera terjadi"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Jujur abang nya keliatan pendiem, tapi keren",  
                "pesan": "Semangat baaang, semoga sellau sehat"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya lucuuu",  
                "pesan": "Semangat kaa semoga yang diinginkan cepat didapatkan"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakanya baik bangeeet",  
                "pesan": "keep smile ya kaaa"
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
            "https://drive.google.com/uc?export=view&id=15dX_z7PpNBeroFJl9GFrSgFPn91fWpK8",
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
            "kesan": "Jujur ini abangnya asik banget, ngelucu mulu",  
            "pesan": "Semangat terus bang di senang dan sedihnya"
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1Gg--iHbQNTGLlW1i03jUvxIWJrPTTmPy",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "Ini kaka asuh TPB ku ni TPB 36, Lucuuu kakanyaaa",  
            "pesan": "Semangat terus yaa kaaa, semoga apa yang diusahakan segera tercapai"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1J1Ow3mPnTv1NZuoc5vtWmcrPZNIVovs5",
            "https://drive.google.com/uc?export=view&id=1lVb_DRDLKg3v-K0vaCGfGCuvy8H8Aywe",
            "https://drive.google.com/uc?export=view&id=1e9mbPMxdAnuLs80AjDceH0kKP1ubYpQV",
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
            "kesan": "Abangnya keren jujur, pinter banget, public speaking nya jugaaa bagusss",  
            "pesan": "Keep strong bang (pasti strong sih)"
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "Abangnya baik banget, suka bagi bagi ilmu jugaaa",  
            "pesan": "Pokonya selalu semangat baang, sehat selalu"
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "Kakanya baiiik",  
            "pesan": "Pokoknya semangat buat kakaaaa"
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1A717g1m6Pl_yQkREeN-fy6GNGwZgTpea",
                "https://drive.google.com/uc?export=view&id=1DMPCpnCFfHAsAgXe9gsOLPghm24ppRWA",
                "https://drive.google.com/uc?export=view&id=1l3IEEGrYFXfW9-ZrXDk3DUxOjejU7Jr_",
                "https://drive.google.com/uc?export=view&id=1swlWLuvnhYIuncA3X_jmga-WUrSCDm2e",
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
            "kesan": "Abangnya berwibawa vibesnya, seru jugaaa",  
            "pesan": "Semoga selalu dalam keadaan sehat ya baaang"
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "Kakaknya baik banget sumpaahhh",  
            "pesan": "Sehat sehat yaa kaaa, keep smile"
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "Kakanya ramaaaah",  
            "pesan": "Semangat kaka kuliahnyaaa, semoga bisa mendapatkan hasil yang diinginkan"
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "Abang nya baik banget sumpah ini mah",  
            "pesan": "Semoga apa yang abang harapkan segera terjadi ya baang"
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=11bYc1s3Hdc7SXsymoVoO5xp_fJbWbswa",
                "https://drive.google.com/uc?export=view&id=1U5rFZZlnPF_rL5luJ9Thw-uOT2b62c0J",
                "https://drive.google.com/uc?export=view&id=1Cic7JXesS0nSp855SaBGZ9GtBENJKAOC",
                "https://drive.google.com/uc?export=view&id=1bL_a8gWYvrND2p3KYrqGeW6sslbV5cvU",
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
            "kesan": "Kakanya baik bangeeet",  
            "pesan": "Kakanya keren tetep begitu dan semoga bisa lebih berkembang"
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "Abangnya asik banget, suka ngelucu jugaaa",  
            "pesan": "Selalu semangat baang, keep stooong!!!"
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "Kakanya jujur baik banget",  
            "pesan": "Semangat kaaa, semoga selalu diberikan kesehatan"
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "Kakaknya lucuuuuu",  
            "pesan": "Semangat terus yaaa kaaaa"
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
               "https://drive.google.com/uc?export=view&id=1w3bLa62k0kGRg7zGRGNe09Q2Szp_4SsS",
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
                "kesan": "Kakaknya keren banget sumpah",  
                "pesan": "Semangat menyampaikan aspirasi kami kaa"
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)
        with tab2:
            gambar_urls_biro_aspirasi= [ #belum ganti gambar
                "https://drive.google.com/uc?export=view&id=1ba18uljAh_SmDH5rCQuDfpoNk_CNJW-8",
                "https://drive.google.com/uc?export=view&id=1f2WiomJkzKMRYpp14oc3Gx-wsI4ti-vr",
                "https://drive.google.com/uc?export=view&id=1RTgfa6zxJnqhqS7R3wLXwW_-2r1rumb0",
                "https://drive.google.com/uc?export=view&id=16zCWIbcZx4dxvcZM7sCqr9QO5gW9QTjf",
                "https://drive.google.com/uc?export=view&id=1XDlfiU1_GRKQt1-Oz4V80WeTV78KOdOi",
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
                "kesan": "Abang ini lucu bangett, fotonya maunya melet bliau",  
                "pesan": "Pokoknya semangat terus baaaang"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Jujur seru banget abangnyaaaa",  
                "pesan": "Semangat ya baaang"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakanya baik banget, seru jugaa",  
                "pesan": "Semoga apa yang diinginkan segera tercapai ya kaaa"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya asik bangetttt",  
                "pesan": "Semangat terus bang kuliahnyaaaa"
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)
        with tab3:
            gambar_urls_biro_kajian= [
                "https://drive.google.com/uc?export=view&id=1XDlfiU1_GRKQt1-Oz4V80WeTV78KOdOi",
                "https://drive.google.com/uc?export=view&id=1laahXpYjdVJLUj6vpNg8LRqMcCJ-pDmI",
                "https://drive.google.com/uc?export=view&id=1rKduKEzQMAPM7oR3IFZ1VX38mk7XacKg",

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
                "kesan": "Kakanya lucuu",  
                "pesan": "Semangat ya kaaaaa"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakanya sumpah asik banget, ketawa muluuuu",  
                "pesan": "Semangat terus kaaaaaa"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "abangnya keren banget cool jugaa",  
                "pesan": "Keep strong bang, jaga kesehatan yaaa"
                },
                ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)
        with tab4:
    
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1oouCnXYLzYbyTg60HK-GPBIXAk5OYOKw",
            "https://drive.google.com/uc?export=view&id=1sEvAhZP5yxITkZsekx0s2kZyUy9c4xg2",
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
                "kesan": "Kakanya seruuuu bangeeeeet",  
                "pesan": "keep smile yaa kaaaa"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kakak nya asik bangeeeet",  
                "pesan": "Semangat terus kakaaaaa"
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
            "https://drive.google.com/uc?export=view&id=1l2mlr7vZPK41txxoyWGfxdGzpn2TJGoA",
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
            "kesan": "Jujur kakanya tegas, tapi baik",  
            "pesan":"Semangat terus kaaa, sukses selaluu"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1PF8M1Y58whudIhc83cL6I0uxK-hC5lDp",
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
            "kesan": "Kakanya terlihat tegas tapi pasti baik",  
            "pesan":"Semangattt kaa untuk TA nyaa, jangan lupa jaga kesehatan ya kaa!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
                "https://drive.google.com/uc?export=view&id=1Wo-8soBycLgfDxPR7Rb50iSC7Mj_SW4N",
                "https://drive.google.com/uc?export=view&id=1ZBiVMQIlfOFOO1V17kk2a_uw0tlXSYNH",
                "https://drive.google.com/uc?export=view&id=1gp0_vVYSSZgvk3TuL9o0UHZVdHKjZFjV",
                "https://drive.google.com/uc?export=view&id=17ZvEaWRpllybIOcxFoiANN-zyfhA9CmD",
                "https://drive.google.com/uc?export=view&id=1XHITpW-V7FOZZ9nfDzZTUKlvsfwhiqbp",
                "https://drive.google.com/uc?export=view&id=14j7DPtXOytTM0xGlO8TCjJjmG4W3CPGS",
                "https://drive.google.com/uc?export=view&id=1uYJDjcPPJQJgO4FQhjAGV8dO52qJEqQx"
                
               
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
                "kesan": "Jujur suka pas dikasih materi ama bang Nobel, karna mudah dipahami",  
                "pesan": "semangat terus baaaang!!"
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Abangnya tegas tapi peduli kok",  
                "pesan":"Sehat selalu ya baang!"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Abangnya tegas tapi jujur peduli banget sama kami",  
                "pesan":"Pokoknya buat abang jempol banget dah"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Abang nya suka bagi ilmu kalo ngobrol santai",  
                "pesan":"Semangat terus bang pokoknya"
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya tegas banget, tapi baik kok",  
                "pesan": "Semangat terus kaaa, jaga kesehataan"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Abangnya asik buat diajak diskusi",  
                "pesan":"Keep strong bang, sukses selaluuu!!"# 1
            },
            #{
             #   "nama": "Putri Manna Anantama Simbolon",
             # "nim": "124450056",
             #   "umur": "18",
             #   "asal": "Sabang",
             #   "alamat": "Nomaden",
             #   "hobbi": "Duduk samping Henry",
             #   "sosmed": "@putrimannaa",
             #   "kesan": "Kakanya asik kok, ramah jugaaa",  
             #   "pesan":"Sehat sehat yaa kaaa!!"# 1
            #},
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "Kakanya ramaah",  
                "pesan":"Semangat terus kaaaa!!!"# 1
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1cc-Wlmi94WY19QG1zf35BwW9IWSFRlfa",
            "https://drive.google.com/uc?export=view&id=12hUosoUbyvSkaiuGJflZ1giQxQEDK_nX",
            "https://drive.google.com/uc?export=view&id=1Uw7KgQAlkNLkRxB6hE79jHAv6QU6LNE5",
            "https://drive.google.com/uc?export=view&id=1z_d0ExZuDLRVU01LJmsRcJLH906VWOiH",
            "https://drive.google.com/uc?export=view&id=1P0GLKwFaHTdIrF_qkG-Je7tgM5DcYl99",
            "https://drive.google.com/uc?export=view&id=1J4bgCQNDSpbHz8J_VifkQQ4hIY4oOveD",
            "https://drive.google.com/uc?export=view&id=15J9w3W-oSCsfn2-VefhEpXoyNco1WDCH",
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
                "kesan": "Asik banget jujur abangnya",  
                "pesan":"Semangatt teruss baaanggg!!"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "Kakanya asiiik",  
                "pesan":"Sehat sehat kaaaaa"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kakanya ramah jujur",  
                "pesan":"Jaga kesehatan yaa kaa!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "Abangnya baik banget jujur ini mah serius, makasih bang",  
                "pesan":"Semangat terus dalam menjalanij hidup baaang"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakanya baik banget",  
                "pesan":"Selalu sukses ya kaaa"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Tembung",
                "alamat": "Belwis Tengah",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Ramah dan baik bener abangnya",  
                "pesan":"semangat terus yaa baaang"# 1
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "Kakanya baik dan ramah",  
                "pesan":"Selalu jaga kesehatannya ya kaaaa"# 1
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
            "https://drive.google.com/uc?export=view&id=16munZKU6tcqcBNXAG1htivvE8m68-8oy",
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
                "kesan": "Abangnya keren bangeeet, jujur asik",
                "pesan": "Semangatt terus bang buat apapun itu yang lagi dikerjain"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1g3hGOquO0Vk2mTzpuFkeFE_qsZfLGtWR",]
            data_list_sekretaris_mikfes = [ 
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "Jujur kakanya asik banget, ramah banget",
                "pesan": "Sehat sehat yaa kaaa"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1USO_v5kyXn04m1a4y2YJSl2EdGfHMz27",
            "https://drive.google.com/uc?export=view&id=1_1cCSmvDftcxVdGndW0c1dYC_geNEP3B",
            "https://drive.google.com/uc?export=view&id=1Adxy5FvyzrEp7mezi4IzwfMhTkAOJK7a",
            "https://drive.google.com/uc?export=view&id=1posXR3AUq7bu67EJn03p3wYyrlx4VDlc",     
            "https://drive.google.com/uc?export=view&id=17TielDz96AAJw-cOdN7TBemnQ1kqWb5l",
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
                "kesan": "Baik banget jujur abangnya",
                "pesan": "Semoga tenang di sana bang, semoga apa yang sudah dilakukan di dunia selalu jadi manfaat bagi sekitar"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Baik abangnya inii",
                "pesan": "Sehat selalu baaang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kakak nya asiiiiiikkkk",
                "pesan": "Kakak harus semangat teruuusss!!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Kakanya ramah banget sih ini jujur",
                "pesan": "Semoga selalu sukses yaa kaaa"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Penjelasan dari kakanya jujur bikin tertarik",
                "pesan": "Semoga sukses buat kedepannya ya kaa"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kakanya ramah banget sumpah",
                "pesan": "Semoga apa yang diusahakan bisa tercapai ya kaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
                "https://drive.google.com/uc?export=view&id=1LPPRKC86m8q1ofUylx4J3E5QOtJwzhxe",
                "https://drive.google.com/uc?export=view&id=1dHlWsCKv2lRuAu6IJNP3rgxYgdt89QGk",
                "https://drive.google.com/uc?export=view&id=1S6TwxncHiawHTd0zVTas_yLZCl4gfc9-",
                "https://drive.google.com/uc?export=view&id=17fqO_BxsIKOWOwlLDUUTfJVDqvH61r-z",
                "https://drive.google.com/uc?export=view&id=17SeuopvFKQtxr4BVEvPzbCAhLgXtTbme",
                "https://drive.google.com/uc?export=view&id=1d_t42jgkXW6fzqzTywE_Hp-OXchihQdw",
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
                "kesan": "Abangnya ramah banget ini mah gk bo'ong",
                "pesan": "Semangat buat semua yang sedang dilakukan baang"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Kakanya baik bangeettt",
                "pesan": "Keep strong yaa kaaaa"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakanya baikkk ramah jugaaaa",
                "pesan": "Semangat terus ya kaaaa"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Keren banget kakanyaaaa",
                "pesan": "Jaga kesehatan terus yaa kaaaa"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang nya ramaaaahhh",
                "pesan": "Semoga apa yang direncakan bisa terjalan ya baang"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kakanya baikk bangeeet",
                "pesan": "Semoga selalu dikelilingi hal bak ya kaaaa"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_Divisi_Research_Development = [
                "https://drive.google.com/uc?export=view&id=17LKstMubuAaW3PQ6ZfkrLk8fG0ni3jK1",
                "https://drive.google.com/uc?export=view&id=1g9Qo1--McjHJnwF7PF2LVSmR_8q1N4IM",
                "https://drive.google.com/uc?export=view&id=1NWONC3mArChP0Y9HH7mIINRswUq6xZuj",
                "https://drive.google.com/uc?export=view&id=1tSL1Ik4FLAnoFDtP-lXfCBoQIAUAG47S",
                "https://drive.google.com/uc?export=view&id=1KGOXGyxhcBywsBvlv_H8G9tIQ7Ms8EnB",
                "https://drive.google.com/uc?export=view&id=1C--wAG1AcGWQ30_Aogmk0LAs-gwY2aJU",
                "https://drive.google.com/uc?export=view&id=1gepZbE7n5YjXE6pnrEhQ8ul0V16WCTtt",
                "https://drive.google.com/uc?export=view&id=1NkHFHMS6Ebed7Ciavnl6wGPoMoCB_pbK",
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
                "kesan": "Abangnya pinter bangeeettt",
                "pesan": "keep strong! semangat terus baang"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakanya ramaaah",
                "pesan": "Semoga selalu dipermudah jalannya ka"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abang nya seruuuu",
                "pesan": "Semangat trus yaa baaang"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Abang nya seruuuu",
                "pesan": "Keep strong baaaanggg"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Pinter banget sumpah abangnyaaa",
                "pesan": "Semangat terus yaa baang, keep smilee"
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
                "kesan": "Abangnya ramah bangeeeeetttt, asik jugaaa",
                "pesan": "Semoga apa yang diinginkan segera terwujud yaaaa"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Abangnya baik banget jujur, ramah jugaaa",
                "pesan": "Semoga selalu dikelilingi hal baik"
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
            "https://drive.google.com/uc?export=view&id=1BBm1i8e0VglMYutNd2iHKJCEel15pBV2",
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
                "kesan": "Kakanya asik bangeeett",
                "pesan": "Semangat terus yaa kaaa, sukses selaluuuu"
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
                "alamat": "Jalan lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "Kakanya baiik bangeeet",
                "pesan": "Semangatt terus ka ditengah kesibukannyaaa"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [
            "https://drive.google.com/uc?export=view&id=1-g4lH98N0SgjNCHtetETFMwwN-IYC1nz",
            "https://drive.google.com/uc?export=view&id=1N7-NNlo34872bebOS_qG4GWu0hnGtCwX",
            "https://drive.google.com/uc?export=view&id=1jqVi9DwxvWc8js-mkL_d0oCMi6Cupkk_",
            "https://drive.google.com/uc?export=view&id=10nUFaYpxmtdgE4pOeaDKWgn1r6EQEfCX",
            "https://drive.google.com/uc?export=view&id=1OOZhTn8KkNAjFTBUAzcho1aOm5HQPhis",
            "https://drive.google.com/uc?export=view&id=1L_dxY3dwbLOn4319Yg6cup9R7hzM2dj7",
            "https://drive.google.com/uc?export=view&id=17eNE38GYHUjr64_taynR507SEAF9sR6l",
            "https://drive.google.com/uc?export=view&id=1HQRLZZOj0Jrzz7QHLTIWJX91LQwu6jKN",
            "https://drive.google.com/uc?export=view&id=13A188Ub4dlvqQW1GsPUBnmPorMx07m1U",
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
                "kesan": "Kakanya lucuuuu",
                "pesan": "Semangat terus yaa kaaa walau sibuuk"
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
                "kesan": "Abangnya keren banget, jujur ngepens",
                "pesan": "Sehat sehat ya baanag, semangat teruuus"
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
                "kesan": "baik banget kakanyaaaa",
                "pesan": "keep smile ya kaaaa"
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
                "kesan": "Abangnya baiiik",
                "pesan": "Keep strong yaaaa baaaang"
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
                "kesan": "Abangnya keren bangett",
                "pesan": "Semangattt selalu bang kuliahnya"
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
                "kesan": "Kakaknya ramah dan lucu juga",
                "pesan": "Semangat terus dan semoga sukses selalu kakk"
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
                "kesan": "Abangnya aktif dan keren banget",
                "pesan": "Sehat selalu dan semangat terus bangg"
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
                "kesan": "Kakaknya baikk bangett",
                "pesan": "Semoga kakak selalu happy dan sukses selalu kakk"
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
                "kesan": "Kakak asprak alpro RC kitaa",
                "pesan": "Semoga yang di cita-citakan tercapai ya kakk, semangat terus kak"
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
                "kesan": "Kakaknya baik dan ramah banget",
                "pesan": "Semangat kakak menjalani perkuliahannyaa"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
            "https://drive.google.com/uc?export=view&id=1nqZoNnWMeT9UvBt1lUaqWziIgWe4ps58",
            "https://drive.google.com/uc?export=view&id=1_x4_E2fjbwyGtsIBvIYYo9Z_OgucDZtX",
            "https://drive.google.com/uc?export=view&id=1QJK9dEt6oByaPy-v1d1U2oTJUd_QB47d",
            "https://drive.google.com/uc?export=view&id=1DkippqmT89vhEtJp74Elbx6SxYVjw9aP",
            "https://drive.google.com/uc?export=view&id=1yedrtBIJjjpD-x0RbvslMj87WFeoWaMz",
            "https://drive.google.com/uc?export=view&id=1scOAmIgCuaJTisEn92f6U0kFKhUirxAX",
            "https://drive.google.com/uc?export=view&id=1U-EdJJrTg00L51RWZ6cGkAzl0VS9EXQU",
            "https://drive.google.com/uc?export=view&id=1hV_vWTew8zHkL7IQBYiMjo2RHYUR54kS",
            "https://drive.google.com/uc?export=view&id=1jv3XgAbfHbgaHq3yLQx677D7_U2j4Duq",
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
            "kesan": "Abangnya keren banget, banyak ngasi insight baru juga apalagi selama wawancara",  
            "pesan": "Tetap jadi orang keren bangg"
            },
            {
            "nama": "Fathya Intami Gusda",
            "nim": "123450095",
            "umur": "25",
            "asal": "Tangerang Selatan",
            "alamat": "Sukarame",
            "hobbi": "Baca wattpad",
            "sosmed": "@fatthyaa_",
            "kesan": "Kakaknya baik dan ramah bangett",  
            "pesan": "Semoga hal-hal baik juga kembali ke kakak yaa"
            },
            {
            "nama": "Tarisya Hidayatul Rahmi",
            "nim": "123450052",
            "umur": "25",
            "asal": "Luhak tanah datar",
            "alamat": "Gerbang barat",
            "hobbi": "Jadi orang baik",
            "sosmed": "@tari_sya23",
            "kesan": "Kakaknya juga ramah bangett",  
            "pesan": "Semangat selalu kakk, jangan lupa jaga kesehatan jugaa"
            },
            {
            "nama": "Ashila Islamisahfa Vanisha",
            "nim": "124450028",
            "umur": "20",
            "asal": "Sini",
            "alamat": "Jauh pokoknya",
            "hobbi": "Tidur",
            "sosmed": "@kshigf",
            "kesan": "Kakaknya lucu dan baik banget",  
            "pesan": "Semangat terus kakak menjalani perkuliahannya"
            },
            {
            "nama": "Danil N Fadillah",
            "nim": "124450103",
            "umur": "19",
            "asal": "Karawang",
            "alamat": "Belakang Polda",
            "hobbi": "Ngasih makan ikan cupang",
            "sosmed": "@d4niel_fdlh",
            "kesan": "Abangnya keren bangett",  
            "pesan": "Semangat terus bang dalam segala hal yang direncanakan"
            },
            {
            "nama": "Favian Arkaanda",
            "nim": "124450021",
            "umur": "19",
            "asal": "Swiss",
            "alamat": "Way Halim",
            "hobbi": "Ngesen kanan",
            "sosmed": "@fvnnn05",
            "kesan": "Abangnya aktif dan keren",
            "pesan": "Abang asprak alpro rc semangat terus bangg"
            },
            {
            "nama": "Muhammad Fathiy Zumar Yazid",
            "nim": "124450081",
            "umur": "20",
            "asal": "situlah",
            "alamat": "pohon mulia",
            "hobbi": "nyari hobi",
            "sosmed": "@zydddddd__",
            "kesan": "Abangnya keliatan serius, tapi seru",
            "pesan": "Semangat bang kuliahnya"
            },
            {
            "nama": "Muhammad Rizaldi",
            "nim": "124450093",
            "umur": "Masih muda lah",
            "asal": "Rahim Ibu",
            "alamat": "Pasar lantai 3.5",
            "hobbi": "Main layangan waktu hujan",
            "sosmed": "@jaldii._",
            "kesan": "Abangnya ekstrovert banget",
            "pesan": "Semoga selalu aktif dan semangat terus bang"
            },
            {
            "nama": "Saskia Nova Magdalena",
            "nim": "124450074",
            "umur": "20",
            "asal": "Banyak Begal",
            "alamat": "Pinggir Jalan",
            "hobbi": "nonton thinkerbell",
            "sosmed": "@snova.19",
            "kesan": "Kakaknya baik bangett",
            "pesan": "Semoga selalu dikelilingi orang-orang baik juga kakk"
            },
            {
            "nama": "Selma Siti Aisyah",
            "nim": "123450044",
            "umur": "20",
            "asal": "Lampung",
            "alamat": "Bandara Lampung",
            "hobbi": "Jalan-jalan",
            "sosmed": "@selmasiti_aisyah",
            "kesan": "Kakaknya ramah bangett",
            "pesan": "Semoga sukses dan semangat selalu kakk"
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
            "https://drive.google.com/uc?export=view&id=1czusS-NxxRIw_YlgjbcUxyrJjO6d0DYL",
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
                "kesan": "Abangnya asik banget, keren jugaaa",  
                "pesan":"Semangat kuliahnya baaaang, keep strong"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/uc?export=view&id=1OYpXeJyaycXsG1RjpQ3abm5NIx_uaBV8",
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
                "kesan": "Kakanya ramah bangeeet",  
                "pesan":"Sehat selalu yaa kaaaa"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
            "https://drive.google.com/uc?export=view&id=1sCKyof2w8TwtccKjpn8vo9aV4ghwu90k",
            "https://drive.google.com/uc?export=view&id=17odQZkbpnEcWgz6myzOSQM4xkzvkh2hQ",
            "https://drive.google.com/uc?export=view&id=1YgSUAYHmxIQZ9QpFFJrg3nrYZBnqaxHJ",
            "https://drive.google.com/uc?export=view&id=1mChPWiuYZ161-FIQjAYWXwIO7uCCUYSq",
            "https://drive.google.com/uc?export=view&id=1yb52ULXd-N6QIKXwy3lb8lBVyo27zamz",
            "https://drive.google.com/uc?export=view&id=1R6-7Vhh-4-FFdVyp0ZPIhIONwh4P8N_8",
            "https://drive.google.com/uc?export=view&id=1pnmshMSq7AHQUKrGKWdKixCZu3VwZTNt",
            "https://drive.google.com/uc?export=view&id=1VoRd6NKmeRoOseffizyhOJHqI6-tpqjz",
            ]
            data_list_keharmonisasian = [
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
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/uc?export=view&id=10q_QdVq5WzDj5g4EktxwxJSPB0M_RQDv",
            "https://drive.google.com/uc?export=view&id=1HiJJEQXhqTGMwM6TYcwRuhl6GkFg4ube",
            "https://drive.google.com/uc?export=view&id=1iesVGezgugweMrvUhYhu98EAiXItAsaA",
            "https://drive.google.com/uc?export=view&id=1FX58lA-av_5CzNGwfBlWcr2kDQOMOGCk",
            "https://drive.google.com/uc?export=view&id=13yWlhHXd048_ivIo_5kM4kVM_fsA_cHt",
            "https://drive.google.com/uc?export=view&id=1fhoabuGacEhYPBia1t5Ea_QV032I9k2E",
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
                "kesan": "Abangnya baiiik",  
                "pesan":"Semangattt terus yaaa baaang"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kakanya ramah jujuur",  
                "pesan":"Selalu jaga kesehatan yaa kaaa"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "@cikamrbn",
                "kesan": "Kakanya lucuuu",  
                "pesan":"Semoga selalu dikelilingi hal positif"# 1
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakanya jujur baik banget",  
                "pesan":"Sehat sehat yaa kaa, keep smile"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "@muhvinz_",
                "kesan": "jujur abangnya menyenangkan",  
                "pesan":"semoga bisa menerjang apapun yang ada di depan baang"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nginep di rumah Yollanda",
                "sosmed": "@snasaa._",
                "kesan": "Kakanya baiiik",  
                "pesan":"Semangat terus yaa kaaaa"# 1
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
            "https://drive.google.com/uc?export=view&id=1N4dIHHdB5CeVz8OygZn-hNOX1MjASRk1",
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
                "kesan": "SUMPAH ASIK BANGET BANGET BANGET, TERBAIK",
                "pesan": "SEMANGAT TERUS BANG SALAM SUKSES",
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
                "nim": "123450000",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Korpri",
                "hobbi": "Memasak",
                "sosmed": "@_inayasani",
                "kesan": "KAKANYA BAIK BANGET, RAMAH, ASIK, SEMUANYA POKOKNYA",
                "pesan": "SEMANGAAATTT KAAAAAAAAAA",
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1NdxI7kuTgiEiutow57MPkZtSBkau1lK0",
            "https://drive.google.com/uc?export=view&id=1LNA6K_zrpCh_8B787bIxo8JB1UCWVwl9",
            "https://drive.google.com/uc?export=view&id=1RkhM5S_5A8U0kUtI5wWR2SB3YJCLxHmX",
            "https://drive.google.com/uc?export=view&id=1-Gez_rEpEd6ythfCVh0lvY6w6HcKulyb",
            "https://drive.google.com/uc?export=view&id=1vFEG4uocG4-BNkttz9YjGWBhluRBeDbc",
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
                "kesan": "Kakaknya ramah guys jujur",
                "pesan": "Pokoknya keep strong, semangat terus kaaa!!",
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Abang NIM nih, asik guys abangnya",
                "pesan": "Sehat sehat selalu baaang #013",
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kakak nya asik jujur",
                "pesan": "Semangat yaa kaa dalam menjalani hidup hehe",
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abang asik dan baik ko guys",
                "pesan": "semangat terus yaa baaangggg",
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kakak nya asik banget, banyak dapet ilmu sponsor dari kakanya ",
                "pesan": "Semangaaat kaaa!!",
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
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakaknya baik jujur, asik jugaaa",
                "pesan": "Keep smile, keep strong kaaaa",
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Ini nih, my ayah father bapak aku, asik lucu banget orangnya",
                "pesan": "Jangan bosen bosen yaa baaang",
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Asik banget abangnya, baik jugaa jujur",
                "pesan": "semangat terus yaaa baaaangggg",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kakaknya baik, asik, seru",
                "pesan": "pokonya keep strong kaaaa"  
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kakaknya baik banget jujur, selalu memberi arahan",
                "pesan": "Jaga kesehatan yaaa kaaa!!",
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
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal": "Payakumbuh, Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kaka nya keren sih jujur",
                "pesan": "Semangat terus ya kaaaa"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1hB4PN9eK9z13aE5sxeq218htzjTkEVS9",
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
                "kesan": "ramah banget kakanyaa, baik jugaaa",
                "pesan": "Tetap tersenyum ya kaaaa"
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
                "nama": "Labo Napitupulu",
                "nim": "37",
                "umur": "20",
                "asal": "Jakpus, Medan, Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Tong setan",
                "sosmed": "noerruuu",
                "divisi": "Dokumentasi",
                "kesan": "Abangnya cool",
                "pesan": "Pokonya keep strong ya baaang"
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
                "kesan": "Kakanya ramah bangeeet",
                "pesan": "Keep Strong dalam menghadapi semuanya ya kaaa"
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
                "kesan": "lucuuuuu",
                "pesan": "Semangat terus yaaa kaaaa"
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
                "kesan": "Jujur abangnya baik, keren juga",
                "pesan": "terus semangat ya baaang"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
            "https://drive.google.com/uc?export=view&id=1Vx0Nk2OylnbrRx_L6ZW5JQ6GVqgI3rTQ",
            "https://drive.google.com/uc?export=view&id=1Y-n9WgzEVokH0XimAqDOSa_epwnhnwmZ",
            "https://drive.google.com/uc?export=view&id=14EPMTZua3my48Uqw_m4euIEYLL206lK8",
            "https://drive.google.com/uc?export=view&id=1qLUI-SymckwaduId3Bbk4DEOa0mGPnY9",
            "https://drive.google.com/uc?export=view&id=1m_my97kVsCVPinEGsp19Rg4rFgbUG8S_",
            "https://drive.google.com/uc?export=view&id=1n0jpZiHb2p-lVgL4sXTd76oGO8sfi1Ed",
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
                "kesan": "Kakanya baiiikkkk",
                "pesan": "Semoga selalu dikelilingi hal baik ya kaa"
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
                "kesan": "Kakanya lucu",
                "pesan": "Keep strong pokonya mah"
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
                "kesan": "Kakanya baiiikkkk",
                "pesan": "Pokonya harus tetap strong ya kaa"
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
                "kesan": "Kakanya ramaaaah",
                "pesan": "Semangat terus ya kaaa"
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
                "kesan": "Kakanya lucuuuu",
                "pesan": "Semangattt keep smile ya kaaaa"
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
                "kesan": "lucuuuuuuuu",
                "pesan": "Semoga selalu diberikan kemudahan ya kaaaa"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
            "https://drive.google.com/uc?export=view&id=1reCEDuyMZHRsTIyVFq4x3a7eqVv7HNty",
            "https://drive.google.com/uc?export=view&id=1atZTxIoNLVNQVFRr4CRIL7sWe8SGNYbq",
            "https://drive.google.com/uc?export=view&id=1KSezc8FGz4EDRuYnUxfB0J5kcA6xw1Q3",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1AZeqrWofTPAnMCbqZdGvhoUcoraK6SZt",
            "https://drive.google.com/uc?export=view&id=1xR39p8ryuUsU9tngr4Vb1Cw37p4zQ4y8",
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
                "kesan": "Kakanya baiiiikk",
                "pesan": "Pokonya harus keep strong ya kaa"
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
                "kesan": "Baik, asik, humble abangnyaaa",
                "pesan": "Semoga selalu dikelilingi hal hal positif"
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
                "kesan": "Abangnya ramaahhhh",
                "pesan": "Semangat terus baang di tengah detlai"
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
                "kesan": "Kakanya ramah dan asik",
                "pesan": "Semangat menjalanin kuliahnya kaaa"
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
                "kesan": "Kakanya asiiiiik",
                "pesan": "Keep smiling ya kaaaa"
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
                "kesan": "ramah banget kakanyaaaa",
                "pesan": "Semangat terus yaa kaaaaa!!"
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
            "https://drive.google.com/uc?export=view&id=18x8qz_Lqj6i6PEFA3JUyCfPJlReMZvUB",
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
            "kesan": "Baek banget jujur abangnya",
            "pesan": "Semangat terus yaa baaang!"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1qsEatLS2i26ptSaL9N73Mg8Zr3kBvuCd",]
            data_list_sekretaris_departemen_minbak = [ 
            {
            "nama": "Gusti Putu Ferazka Dhiyamika",
            "nim": "123450046",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Dadi",
            "hobbi": "Mendaki",
            "sosmed": "@ferazkaa",
            "kesan": "Kakanya asik banget, ramah juga",
            "pesan": "Sehat sehat yaa kaaa"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
            "https://drive.google.com/uc?export=view&id=1KCjrYYX695GBHhMlhc5Ay7fM4X0rcray",
            "https://drive.google.com/uc?export=view&id=1RIlVyC4-CUxWubRIhL6adMHNdQl6u2GX",
            "https://drive.google.com/uc?export=view&id=1y4-G6rgI6U1V0RTUpiS6zRi_pDkOLVsR",
            "https://drive.google.com/uc?export=view&id=1_eYRFgBp2AQMI82bDUc4UdsqoWnwL4jM",
            "https://drive.google.com/uc?export=view&id=1V_YJBsavn3kTKejwmJ6hk-ivjNly7J2j",
            "https://drive.google.com/uc?export=view&id=1oHO4Y4CL1xaqk1fIfC_HnFLdZGc4hxe5",
            
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
            "kesan": "Jujur abangnya asik banget, suka ngobrol jugaa",
            "pesan": "Semangat terus yaa baaaang"
            },
            {
            "nama": "Ayu Andriani Parlina Wati",
            "nim": "124450058",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Airan",
            "hobbi": "Belajar + menghitung uang",
            "sosmed": "@aayuandriani_",
            "kesan": "Ramah kakanya, baik jugaaa",
            "pesan": "Sukses terus yaa kaaa"
            },
            {
            "nama": "Dafa Elpriza",
            "nim": "124450131",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Kandis",
            "hobbi": "Jogging",
            "sosmed": "@dafaelpriza_",
            "kesan": "Abangnya baek, ramah jugaaa",
            "pesan": "Selalu jaga kesehatan ya baaang"
            },
            {
            "nama": "Juwita Sari",
            "nim": "124450066",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Pemda",
            "hobbi": "Mancing",
            "sosmed": "@ju.juwitaaa_",
            "kesan": "Kakanya murah senyuuum",
            "pesan": "Semoga bisa selalu bahagia yaa kaaa"
            },
            {
            "nama": "Muhammad Afdal Luthfi",
            "nim": "124450047",
            "umur": "19",
            "asal": "Lampung Tengah",
            "alamat": "Jl. Pulau Damar",
            "hobbi": "Memantau dl tugas",
            "sosmed": "@afdall.03",
            "kesan": "Abangnya ramah, asik jugaaa",
            "pesan": "Keep strong yaa baaang"
            },
            {
            "nama": "Salsabila Nazwa Putri",
            "nim": "124450002",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Korpri",
            "hobbi": "Nongkrong di kopken",
            "sosmed": "@slbnzw_",
            "kesan": "Kakanya baek bangettt, asik lagi",
            "pesan": "Semoga selalu dikelilingi hal baik ya kaa"
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
                "https://drive.google.com/uc?export=view&id=1aueAKLJHP25N45ZiSWgZFIedz0YQRtx-",
                "https://drive.google.com/uc?export=view&id=1O0fPU57LFyUr0bQSX8HofN0bgnjZbGHz",
                "https://drive.google.com/uc?export=view&id=1wojg09H8RB56V8_zAvXtc5VhXALqu-ZK",
                "https://drive.google.com/uc?export=view&id=17NH9Vc1UFPd81rKP1q0Ll6OnKj51Fo7X",
                "https://drive.google.com/uc?export=view&id=18NYYMnIUvEaIuVehyadgt_ig6q9njJqS",
                "https://drive.google.com/uc?export=view&id=1C8_2h67_WKBnPUpwkkTm9AfSi7W2H7_z",
                "https://drive.google.com/uc?export=view&id=1mjHinYhIBpyeWsNWf_jMBdvWHjECt162",
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
                "kesan": "Abangnya baek banget, asik juga",
                "pesan": "Semangat terus yaaa baaanggg"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal": "Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Main rubik",
                "sosmed": "@andra.lhm",
                "kesan": "MY MENTOR ALWAYS IN MY HEARTH!!",
                "pesan": "Pokoknya jangan cape cape ya bang ama kamii heheheh"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live tiktok",
                "sosmed": "@bryantel_",
                "kesan": "Asik kok abangnyaa",
                "pesan": "Semangat terus yaa baaang"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17",
                "asal": "Surabaya",
                "alamat": "Kemiling",
                "hobbi": "Nanem Sawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Abangnya cool banget",
                "pesan": "Keep strong pokoknya baang"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Kakanya asik, ramah jugaa",
                "pesan": "Semoga selalu sukses yaa kaaa"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Asik banget kakanya, baik jugaaa",
                "pesan": "Always smile ya kaaa"
            },
            {
                "nama": "Muhammad Rafka",
                "nim": "124450089",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Kotabaru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya baek, ramah jugaa",
                "pesan": "Semangat terus yaa baaaang"
            }
            ]
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)  

    Departemen_Minbak()