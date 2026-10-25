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
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bZ70IqPONIoXJpJcRVRuu5pKkn4A_m-q",
            "https://drive.google.com/uc?export=view&id=1zCjI8tSxAlLXw_ozqqXIuGDpauHd-Fdm",
            "https://drive.google.com/uc?export=view&id=1KAjKjUSeY-UX_dp2rj1sF6PMlSkkO0W1",
            "https://drive.google.com/uc?export=view&id=1VZchcOTONFY5Ac-gyoDbeW8Bw6D-FgDD",
            "https://drive.google.com/uc?export=view&id=1UVoy2vf21D-gJhDPapyJB5EPoEvvBZd3",
            "https://drive.google.com/uc?export=view&id=1IpRAQft9HxUmxzfYb71Us80Z_bU-3KWH",
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
                "kesan": "Abangnya keren banget, punya jiwa kepemimpinan yang tegas tapi tetep seru diajak diskusi.",  
                "pesan": "Sehat selalu dan semangat terus kuliahnya bang."
            },
            {
                "nama": "Muhammad  Aqil Ramadhan",
                "nim": "1223450046",
                "umur": "22",
                "asal":"Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil111",
                "kesan": "Abangnya asik banget kalau diajak ngobrol",  
                "pesan":"Semoga sukes selalu abang."
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya ramah dan seru banget",  
                "pesan":"Sehat dan semangat selalu kuliahnya kakak."
            },
             {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya seru dan informatif banget tentang administrasi kesekretariatan",  
                "pesan":"Semangat terus kuliahnya abang."
            },
             {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafadhilaa",
                "kesan": "Kakaknya seru dan informatif banget tentang administrasi kebendaharaan",  
                "pesan":"Semangat terus kuliahnya kakak"
            },
             {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@lutfiaaemdhn",
                "kesan": "Kakaknya aktif dan seru banget kalau diajak ngobrol",  
                "pesan": "Semangat terus kuliahnya kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()


# Badan Legislatif
elif menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg= [
                "https://drive.google.com/uc?export=view&id=1agpykvBsiH-ZeQCGNKu-7s72PQXu3-8h",
            ]
            data_list_kabaleg = [  
                {
                    "nama": "Ridho Benedictus Togi Manik",
                    "nim": "123450060",
                    "umur": "20",
                    "asal":"Palembang",
                    "alamat": "GH",
                    "hobbi": "Wawancara",
                    "sosmed": "@iamridhomanik",
                    "kesan": "Asikk dan lucu bangett abangnya",  
                    "pesan":"Semaangat selalu kuliahnya abangg"
                },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2: 
            gambar_urls_sekretaris = [  
                "https://drive.google.com/uc?export=view&id=1uqbIcv4ueBXc0XI7wyQtgUDiDvcnbIeH",
            ]
            data_list_sekretaris = [ 
                {
                    "nama": "Juesi Aprilia Saragih",
                    "nim": "123450085",
                    "umur": "19",
                    "asal":"Singkawang",
                    "alamat": "Pelangi",
                    "hobbi": "Dengerin lagu semusim dari marvel",
                    "sosmed": "@j_eesie",
                    "kesan": "Kakaknya asik dan keren bangett suka banget sama kakak asuh tpb akuu",  
                    "pesan":"Semangatt terus kakak kuliahnya"
                },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            gambar_urls_komisi1 = [
                "https://drive.google.com/uc?export=view&id=1IVfqvgMhPv4mWXjXULhjj91KlEAWj9_u",
                "https://drive.google.com/uc?export=view&id=1-E6gLTUVv_Hc2ZAl_AZDaLeT9prxFgMo",
                "https://drive.google.com/uc?export=view&id=1gNncmcU1f8zoq75808bt3fhP8uV18EbI",
            ]
            data_list_komisi1 = [
                {
                    "nama": "Dharu Cahyoaji Sasongko",
                    "nim": "123450023",
                    "umur": "19",
                    "asal":"Lampung",
                    "alamat": "Bandar Lampung",
                    "hobbi": "Ngidupun api Baleg di tiktok",
                    "sosmed": "@exvoltas",
                    "kesan": "Abangnya aktif dan keren bangett",  
                    "pesan":"Semangat kuliah dan mengerjakan semua kegiatannya abangg"
                },
                {
                    "nama": "Gh Mikael Niko A S",
                    "nim": "124450025",
                    "umur": "19",
                    "asal":"Jabung",
                    "alamat": "Jati Agung",
                    "hobbi": "COD musang",
                    "sosmed": "@me._kael",
                    "kesan": "Abangnya lucu dan seruu bangett",  
                    "pesan":"Semangat terus kuliahnya abangg"
                },
                {
                    "nama": "Siti Sarifah Sumamah",
                    "nim": "124450015",
                    "umur": "18",
                    "asal":"Banten",
                    "alamat": "Kedaton",
                    "hobbi": "Mancing",
                    "sosmed": "@syt.rifa",
                    "kesan": "Kakaknya ramah bangett",  
                    "pesan":"Semangat kuliahnyaa kakakk"
                },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1ELKvb424mN8cH3_zDvBfWZbR-JcvqG5A",
                "https://drive.google.com/uc?export=view&id=1zMrp-gIUlSSQkdRcMyAaN5NC0KXoebcR",
                "https://drive.google.com/uc?export=view&id=1-XcCitthUyoOa5pEYRbALT8LFWG8M2t8",
                "https://drive.google.com/uc?export=view&id=1TE366QnGMPYfPMncFh67_YoExIXAiryu",
            ]
            data_list_komisi2 = [
                {
                    "nama": "Givaro Ananta",
                    "nim": "123450078",
                    "umur": "23",
                    "asal": "Lampung Barat",
                    "alamat": "Sukabumi",
                    "hobbi": "Minum Kopi",
                    "sosmed": "@givarooo",
                    "kesan": "Abangnya seru dan lucu bangett",  
                    "pesan":"Semangat terus kuliahnya abangg"
                },
                {
                    "nama": "Afghanis Nursholehatunnisa",
                    "nim": "124450042",
                    "umur": "19",
                    "asal": "Kepulauan Mentawai",
                    "alamat": "Owen Kost",
                    "hobbi": "Ngoding",
                    "sosmed": "@afghanisnt_",
                    "kesan": "Kakaknya pinter dan seru bangett",  
                    "pesan":"Semangat selalu kakak kuliahnya"
                },
                {
                    "nama": "Hani Qurrota Aini",
                    "nim": "124450020",
                    "umur": "24",
                    "asal": "CTR",
                    "alamat": "Sukarame",
                    "hobbi": "Baca AU",
                    "sosmed": "@haniquratuain_",
                    "kesan": "Kakaknya cantik bangett",  
                    "pesan":"Semangat selalu kuliahnya kakak"
                },
                {
                    "nama": "Jeremia Halim",
                    "nim": "124450101",
                    "umur": "20",
                    "asal": "Cibaduyut",
                    "alamat": "Teluk",
                    "hobbi": "Nyanyi, olahraga",
                    "sosmed": "@jeremia_hm",
                    "kesan": "Abangnya pinter dan keren bangett",  
                    "pesan":"Semangat selalu abang kuliahnyaa"
                },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=1wbcjBxTzyyjZQ3wijNDwdx6t1X1jg5Hd",
                "https://drive.google.com/uc?export=view&id=1KoD01atLcwhJo4-2vi6eMfvn870vNMrh",
                "https://drive.google.com/uc?export=view&id=1jeAs3WNOPwAyJ0RhrI3xrUwkJq54QAtw",
                "https://drive.google.com/uc?export=view&id=1w1kstXp4ATTA3-pD6c0Pywfa1Vzy_838",
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
                    "kesan": "Kakaknya baik dan ramah bangettt",  
                    "pesan":"Semangat terus kakak kuliahnyaa"
                },
                {
                    "nama": "Jona Timothy Ogatse Panjaitan",
                    "nim": "124450111",
                    "umur": "20",
                    "asal": "Depok",
                    "alamat": "Pemda Raya",
                    "hobbi": "Gym sama Koleksi figure, nafas manual",
                    "sosmed": "@nagatseee",
                    "kesan": "Abangnya seru dan lucu bangett kalau diajak ngobroll",  
                    "pesan": "Sehat selalu dan semangat terus abangg"
                },
                {
                    "nama": "Sekar Dini Widya Putri",
                    "nim": "124450082",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Pemda",
                    "hobbi": "Jajan sama nisa, putri, suci",
                    "sosmed": "@sekardnwp",
                    "kesan": "Kakaknya tegas dan seru sekaliguss",  
                    "pesan":"Semangat terus kakak kuliahnyaa"
                },
                {
                    "nama": "Wan Nashwa Alhasni Yuska",
                    "nim": "123450077",
                    "umur": "20",
                    "asal": "Pasay",
                    "alamat": "Belwis",
                    "hobbi": "Nyapa angin",
                    "sosmed": "@nshaysk",
                    "kesan": "Kakaknya baik dan ramah bangett",  
                    "pesan":"Semangat selalu kuliahnya kakak"
                },
            ]
            display_images_with_data(gambar_urls_komisi3, data_list_komisi3)
    Baleg()


# Badan Kesenatoran
elif menu == "Badan Kesenatoran":
    def Bason():
        st.markdown("<h3 style='text-align: center;'>Badan Kesenatoran</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Senator", "Biro Aspirasi dan Media Komunikasi", "Biro Kajian Strategis dan Propaganda", "Biro Kesekretariatan"])

        with tab1:
            gambar_urls_senator= [
                "https://drive.google.com/uc?export=view&id=1cpgYi7s-PdGAJcCCxZY_ynTQlFfwI_78",
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
                    "kesan": "Kakaknya keren dan inspiratif bangett",  
                    "pesan": "Semangat selalu dalam segala hal kakakk"
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)
      
        with tab2:
            gambar_urls_biro_aspirasi= [
                "https://drive.google.com/uc?export=view&id=1VfWOJ3OAUUL_wMCSB0eNvrxUMXh3ZxXI",
                "https://drive.google.com/uc?export=view&id=1a86FT6r-kQyawn6dPrKqGIKD1z1umKOD",
                "https://drive.google.com/uc?export=view&id=1pId4s2cr_-1IrV_FAGjhmjhpRWOhMbXu",
                "https://drive.google.com/uc?export=view&id=1mVkpAjGRe05SDIypyCEM1cE5Km5WoIVe",
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
                    "kesan": "Abangnya seru dan lucu bangett, satu satunya yang foto wajib melett",  
                    "pesan":"Semangat terus kuliahnya abangg"
                },
                {
                    "nama": "Fernando Dimetrius Barus",
                    "nim": "124450063",
                    "umur": "21",
                    "asal": "Tangerang",
                    "alamat": "Sebelah kamar biwa",
                    "hobbi": "Badminton",
                    "sosmed": "@barus.fernando",
                    "kesan": "Abangnya aktif dan lucu bangett apalagi waktu wawancaraa",  
                    "pesan":"Semangat selalu kuliahnya abangg"
                },
                {
                    "nama": "Suci Aulia",
                    "nim": "124450034",
                    "umur": "19",
                    "asal": "Krui",
                    "alamat": "Kota Baru",
                    "hobbi": "Bikin video random dan upload di second",
                    "sosmed": "@sciia_staff",
                    "kesan": "Kakaknya seru bangett",  
                    "pesan":"Semangat terus kakak kuliahnya!"
                },
                {
                    "nama": "Wielman Itolo Halawa",
                    "nim": "124450072",
                    "umur": "20",
                    "asal": "Nias Selatan",
                    "alamat": "Asrama TB3",
                    "hobbi": "Mancing",
                    "sosmed": "@wielhawny",
                    "kesan": "Abangnya seru dan lucu bangett",  
                    "pesan":"Semangat selalu abang kuliahnya"
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)
       
        with tab3:
            gambar_urls_biro_kajian= [
                "https://drive.google.com/uc?export=view&id=1TzkMBCGPxVWAOUO0E-hfhrjgIoJwmJXV",
                "https://drive.google.com/uc?export=view&id=1lqQI5rM8uaPNJleb1KpNqZgzO84r9TR1",
                "https://drive.google.com/uc?export=view&id=194GlwFAucF-1pLT3hBXn3vPbdqZSiUky",
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
                    "kesan": "Kakaknya seru bangett",  
                    "pesan":"Semangat selalu kuliahnya kakak"
                },
                {
                    "nama": "Aqila Zayyan Salsabil",
                    "nim": "124450014",
                    "umur": "19",
                    "asal": "Lampung Utara",
                    "alamat": "Sukarame",
                    "hobbi": "Mendokumentasikan bayyesian",
                    "sosmed": "@aqilazayyaan",
                    "kesan": "Kakaknya lucu dan gemess bangett",  
                    "pesan":"Semangat selalu kuliahnya kakakk"
                },
                {
                    "nama": "Hazel Mahesa Handhaka",
                    "nim": "124450114",
                    "umur": "20",
                    "asal": "Lampung Timur",
                    "alamat": "Ujung Terang",
                    "hobbi": "Bulu Tangkis",
                    "sosmed": "@hazelhandhaka",
                    "kesan": "Abangnya keren bangett",  
                    "pesan":"Semangat terus kuliahnya abangg"
                },
            ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)
      
        with tab4:
            gambar_urls_biro_kesekretariatan= [
                "https://drive.google.com/uc?export=view&id=1_X8n4YUEKc8fVny5L7zsc05Io9rAgd7C",
                "https://drive.google.com/uc?export=view&id=1SlIDJy0kb_KOBd3_pubon7R0R5Wxfhw6"
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
                    "kesan": "Kakaknya cantik dan seru bangett, love sama kakak gwidii junior",  
                    "pesan":"Semangat selalu kakak kuliahnyaaa"
                },
                {
                    "nama": "Dwi Rahma Fitriani",
                    "nim": "124450084",
                    "umur": "19",
                    "asal": "Tulang Bawang",
                    "alamat": "Jl. Lapas Belwis",
                    "hobbi": "Dengerin musik",
                    "sosmed": "@dwi_rahmftrnii",
                    "kesan": "Kakaknya baik dan ramah bangett",  
                    "pesan":"Semangat terus kaa kuliahnyaa"
                },
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_kesekretariatan)
    Bason()


#SSD
elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
             "https://drive.google.com/uc?export=view&id=1Qi-nHIYW3kgrZY_l_8bLNtNt-zMGIl4X",
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
                    "kesan": "Abangnya seru dan chill bangett diajak ngobro",
                    "pesan": "Semangat terus kuliahnya abangg",
                },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
                "https://drive.google.com/uc?export=view&id=1Tn-Ui69HGudGWGM31LoOmSzirp32Co_u",
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
                    "kesan": "Kakaknya gemess bangett",
                    "pesan": "Semangat selalu kuliahnya kakak",
                },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)

        with tab3:
            gambar_urls_kemitraan = [
                "https://drive.google.com/uc?export=view&id=1KxVCSGEbXlnkyXoFj-7KMWLGkn-QanBd",
                "https://drive.google.com/uc?export=view&id=1aVFCDzb6Z_Nt5qDpe-zcZrHpqrkEjgRS",
                "https://drive.google.com/uc?export=view&id=1wLZCDzX6pajeFYr9Qs78TS4iP-nuOv4s",
                "https://drive.google.com/uc?export=view&id=1Rf9K_PgxBv2CXjephelQ9kIWyJdY8Nqq",
                "https://drive.google.com/uc?export=view&id=1ta4lE-5QQb-1jTXRM3Z_SAfeL-JCTQ7e",
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
                    "kesan": "Kakaknya seru bangett",
                    "pesan": "Semangat terus kuliahnya kakak",
                },
                {
                    "nama": "Hasan Nur Ramadhan",
                    "nim": "124450013",
                    "umur": "25",
                    "asal": "Lamteng",
                    "alamat": "Pemda",
                    "hobbi": "Nonton yutub",
                    "sosmed": "@hasan.ramadan08",
                    "kesan": "Abangnya seruu diajak ngobrol",
                    "pesan": "Semangat terus kuliahnya abangg",
                },
                {
                    "nama": "Layina Ropiqo",
                    "nim": "124450016",
                    "umur": "20",
                    "asal": "Semarang",
                    "alamat": "Balam",
                    "hobbi": "Nonton dracin",
                    "sosmed": "@layinr_",
                    "kesan": "Kakaknya baik dan ramah bangett",
                    "pesan": "Semangat terus kuliahnya kakak",
                },
                {
                    "nama": "Mochammad Iqbal Az-zahir",
                    "nim": "124450052",
                    "umur": "20",
                    "asal": "Bekasi",
                    "alamat": "Natar",
                    "hobbi": "Nonton Drakor",
                    "sosmed": "@iqbalazzahir_",
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Semangat terus kuliahnya abangg",
                },
                {
                    "nama": "Talitha Justine",
                    "nim": "124450076",
                    "umur": "19",
                    "asal": "Sumbar",
                    "alamat": "Pemda",
                    "hobbi": "Nonton",
                    "sosmed": "@talljtine_",
                    "kesan": "Kakaknya lucuu dan seruu",
                    "pesan": "Semangat selalu kuliahnya kakak",
                },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
                "https://drive.google.com/uc?export=view&id=1GT0y_EUGXgsxhv_JTPHvm8WEk3kmgTPQ",
                "https://drive.google.com/uc?export=view&id=1Y57H8CIBLlF_VkmlLJN7KtzUKxqkeS7l",
                "https://drive.google.com/uc?export=view&id=1PPZhaSYsWZuwFytIN4XQmAIGwkJiW83E",
                "https://drive.google.com/uc?export=view&id=1jMylRFmw9M_m87mXnJC3PB1c2mA8e1Ud",
                "https://drive.google.com/uc?export=view&id=1ZOOGOX8RkLyww_jyeuqBMz-N8P0mo2r2"
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
                    "kesan": "Kakaknya seru bangett diajak ngobroll",
                    "pesan": "Semangat terus kakak kuliahnya",
                },
                {
                    "nama": "Abdillah Fikri Al pome",
                    "nim": "124450062",
                    "umur": "21",
                    "asal": "Sumsel",
                    "alamat": "Airan",
                    "hobbi": "Basket",
                    "sosmed": "@pomest",
                    "kesan": "Abangnya seru dan lucu bangett",
                    "pesan": "Semangat selalu abang kuliahnya",
                },
                {
                    "nama": "Afdhal Rahmad Setiawan",
                    "nim": "124450008",
                    "umur": "20",
                    "asal": "Sumbar",
                    "alamat": "Belwis",
                    "hobbi": "Fishing and game",
                    "sosmed": "@Afdhal",
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Semangat selalu kuliahnya abangg",
                },
                {
                    "nama": "Anggun Nita",
                    "nim": "124450009",
                    "umur": "20",
                    "asal": "Lamutara",
                    "alamat": "Belwis",
                    "hobbi": "Nonton kartun",
                    "sosmed": "@anggunitaaa_",
                    "kesan": "Kakaknya asik dan seru bangett",
                    "pesan": "Semangat terus kakak kuliahnya",
                },
                {
                    "nama": "Della Anisa Fitri",
                    "nim": "124450095",
                    "umur": "18",
                    "asal": "Lamtim",
                    "alamat": "Kotabaru",
                    "hobbi": "Olahraga",
                    "sosmed": "@delaanisafitri",
                    "kesan": "Kakaknya seru bangett",
                    "pesan": "Semangat selalu kuliahnya kakak",
                }
            ]
            display_images_with_data(gambar_urls_kewirausahaan, data_list_kewirausahaan)
    ssd()


# Minat dan Bakat
elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown("<h3 style='text-align: center;'>Badan Minat dan bakat</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4= st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])
        
        with tab1:
            gambar_urls_kepala_departemen_minbak= [
                "https://drive.google.com/uc?export=view&id=1NyJ_4DBVum_5PPU2FMtrgDXzxO4rQd5p",
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
                    "kesan": "Abangnya ramah dan seru bangett",
                    "pesan": "Semangat terus kuliahnya abangg"
                },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            gambar_urls_sekretaris_departemen_minbak = [
                "https://drive.google.com/uc?export=view&id=1nrpTGqeKfrYsfdpC_HYIbLMjB0h8sbf-",
            ]
            data_list_sekretaris_departemen_minbak = [ 
                {
                    "nama": "Gusti Putu Ferazka Dhiyamika",
                    "nim": "123450046",
                    "umur": "21",
                    "asal": "Bekasi",
                    "alamat": "Way Dadi",
                    "hobbi": "Mendaki",
                    "sosmed": "@ferazkaa",
                    "kesan": "Kakaknya cantik dan ramah bangett",
                    "pesan": "Semagat terus kakak kuliahnya"
                },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
                "https://drive.google.com/uc?export=view&id=1hBgLsM05ZjZ93SmC32u3avOAUogBBqvY",
                "https://drive.google.com/uc?export=view&id=18eJT124fqSRl8UcCXUFB4S9Cj3x7zSiY",
                "https://drive.google.com/uc?export=view&id=11Ct4vWdDQX0tQBI2EbbpdeTSgr7q8_eP",
                "https://drive.google.com/uc?export=view&id=1w2PG2XNb2OExY19EjoIo2xWjoy5v_QpD",
                "https://drive.google.com/uc?export=view&id=1gR3zMa06-DFnJc7OG8Hxg4mAEhy8Al4I",
                "https://drive.google.com/uc?export=view&id=13pdoDh-vjFyfYpnXrp4zAd7gJpDM-Hov",
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
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Semangat selalu kuliahnya abangg"
                },
                {
                    "nama": "Ayu Andriani Parlina Wati",
                    "nim": "124450058",
                    "umur": "20",
                    "asal": "Lampung Barat",
                    "alamat": "Airan",
                    "hobbi": "Belajar + menghitung uang",
                    "sosmed": "@aayuandriani_",
                    "kesan": "Kakaknya aktif dan seru banget",
                    "pesan": "Semangat dan sukses selalu kakak kuliahnya"
                },
                {
                    "nama": "Dafa Elpriza",
                    "nim": "124450131",
                    "umur": "21",
                    "asal": "Bekasi",
                    "alamat": "Way Kandis",
                    "hobbi": "Jogging",
                    "sosmed": "@dafaelpriza_",
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Semangat dan sukses selalu abangg"
                },
                {
                    "nama": "Juwita Sari",
                    "nim": "124450066",
                    "umur": "19",
                    "asal": "Lampung Barat",
                    "alamat": "Pemda",
                    "hobbi": "Mancing",
                    "sosmed": "@ju.juwitaaa_",
                    "kesan": "Kakaknya ramah bangett",
                    "pesan": "Semangat selalu kakak kuliahnya!"
                },
                {
                    "nama": "Muhammad Afdal Luthfi",
                    "nim": "124450047",
                    "umur": "19",
                    "asal": "Lampung Tengah",
                    "alamat": "Jl. Pulau Damar",
                    "hobbi": "Memantau dl tugas",
                    "sosmed": "@afdall.03",
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Semangat dan sukses selalu abangg"
                },
                {
                    "nama": "Salsabila Nazwa Putri",
                    "nim": "124450002",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Korpri",
                    "hobbi": "Nongkrong di kopken",
                    "sosmed": "@slbnzw_",
                    "kesan": "Kakaknya ramah dan asik bangett",
                    "pesan": "Semoga sukses dan semangat selalu kakak"
                },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [ 
                "https://drive.google.com/uc?export=view&id=1_MfBAjtMdMmQ8tqDx9Jg-27Ryga5oOfU",
                "https://drive.google.com/uc?export=view&id=1xLNZQHgcMFpNmbsVcbAh_cLddYnCPDqw",
                "https://drive.google.com/uc?export=view&id=1J4XCY6Kkk2ZlI11j6ttcQPrgkKUZlgCb",
                "https://drive.google.com/uc?export=view&id=1TbT35lgpEoQPY-sHuRe9_AVEIz4pRdDU",
                "https://drive.google.com/uc?export=view&id=1XISpsRNJauGJOMY4cBBdI-6Igt_mzIEu",
                "https://drive.google.com/uc?export=view&id=1FuviEQ5SjKb80RMB7xIgkYzDiosMbIcC",
                "https://drive.google.com/uc?export=view&id=1ciCEmKohqRvB1XROIJB5qH8IaotU7acL"
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
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Sehat dan semangat selalu abangg"
                },
                {
                    "nama": "Andra Ilham Bintang",
                    "nim": "124450060",
                    "umur": "18",
                    "asal": "Sumatera Selatan",
                    "alamat": "Kotabaru",
                    "hobbi": "Main rubik",
                    "sosmed": "@andra.lhm",
                    "kesan": "Abang Andra seru bangett, loff abangg greedycuwikuki",
                    "pesan": "Sehat selalu dan semangat terus menghadapi kelakuan member greedycuwikuki ini ya abangg!"
                },
                {
                    "nama": "Bryan Paskah Telaumbanua",
                    "nim": "124450003",
                    "umur": "20",
                    "asal": "Nias",
                    "alamat": "Belwis",
                    "hobbi": "Live tiktok",
                    "sosmed": "@bryantel_",
                    "kesan": "Abangnya lucu dan asik diajak ngobroll",
                    "pesan": "Semoga semangat terus dalam segala hal abangg"
                },
                {
                    "nama": "Ghiyats Thabularasa Meardhy",
                    "nim": "124450067",
                    "umur": "17",
                    "asal": "Surabaya",
                    "alamat": "Kemiling",
                    "hobbi": "Nanem Sawit",
                    "sosmed": "@meardhy_ghiyats",
                    "kesan": "Abangnya seru bangett",
                    "pesan": "Tetap semangat dan sukses selalu abangg"
                },
                {
                    "nama": "Indah Julia Mawar Pratiwi",
                    "nim": "124450055",
                    "umur": "20",
                    "asal": "Pringsewu",
                    "alamat": "Airan",
                    "hobbi": "Bengong",
                    "sosmed": "@indahjuliaa",
                    "kesan": "Kakaknya gemess dan asik banget diajak ngobroll",
                    "pesan": "Sukses selalu kakak kuliahnya"
                },
                {
                    "nama": "Jacinda Kesya Alvara",
                    "nim": "124450023",
                    "umur": "18",
                    "asal": "Kalimantan Barat",
                    "alamat": "Korpri",
                    "hobbi": "Nyapu depan gacoan",
                    "sosmed": "@cacalvra",
                    "kesan": "Kakaknya cantik dan gemess bangett",
                    "pesan": "Semangat dan sukses selalu kakakk"
                },
                {
                    "nama": "Muhammad Rafka",
                    "nim": "124450089",
                    "umur": "20",
                    "asal": "Padang",
                    "alamat": "Kotabaru",
                    "hobbi": "Bangun pagi",
                    "sosmed": "@muhammdrafka_",
                    "kesan": "Abangnya seru dan lucu bangett",
                    "pesan": "Semangat dan sukses selalu abangg"
                }
            ]
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat) 
    Departemen_Minbak()


# Akademik dan Keprofesian
elif menu == "Departemen MIKFES":
    def mikfes():
        st.markdown("<h3 style='text-align: center;'>Departemen Akademik dan Keprofeisan</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Professional Skill and Development", "Divisi Pusat Inovasi dan Kajian Akademik", "Divisi Research & Development"])

        with tab1:
            gambar_urls_kepala_departemen_mikfes= [
                "https://drive.google.com/uc?export=view&id=1DE5m6-W5eWlehiDy69lprR3to8dJmRth",
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
                    "kesan": "Abangnya keren dan asikk bangett",
                    "pesan": "Semangat dan sukses selalu abangg dalam segala hal"
                },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            gambar_urls_sekretaris_mikfes = [
                "https://drive.google.com/uc?export=view&id=1_COf8LVe_KZAgV3gCCK8gtlgxczXPH_2",
            ]
            data_list_sekretaris_mikfes = [ 
                {
                    "nama": "Tanty Widiyastuti",
                    "nim": "123450094",
                    "umur": "21",
                    "asal": "Lampung Tengah",
                    "alamat": "Airan",
                    "hobbi": "Mendengarkan Musik",
                    "sosmed": "@tvnty_",
                    "kesan": "Kak Tanty orangnya seru bangett gemess, rajin ngajak buat konten jugaa",
                    "pesan": "Semangatt selalu kakak kuliahnyaa"
                },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            gambar_urls_Divisi_Professional_Skill_and_Development = [
                "https://drive.google.com/uc?export=view&id=1zWt3VYJahGUVVqus3UFqWmyX9sRmd9ZV",
                "https://drive.google.com/uc?export=view&id=1ivwE3nJk_5uMrQJSaRflIsHWrmYZdL30",
                "https://drive.google.com/uc?export=view&id=18hHNVQRogFUzD8Y9C_bM_OObe6aJJYSs",
                "https://drive.google.com/uc?export=view&id=1UUXoA56TVmPR-LCnCGF3ytzb-pNqFDMo",
                "https://drive.google.com/uc?export=view&id=1dUt9wNth5LlJQxw9pwATrlDR2qMPngQU",
                "https://drive.google.com/uc?export=view&id=1gmxUbYM8iK_xqsKcuqh8SOOxrozyrKt2",
            ]
            data_list_Divisi_Professional_Skill_and_Development = [
                {
                    "nama": "Fadil Prasetyo Alfarizzi",
                    "nim": "123450048",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Bandar Lampung",
                    "hobbi": "Bermain gitar",
                    "sosmed": "@fadilalfarizzii",
                    "kesan": "Abangnya keren dan inspiratif bangett",
                    "pesan": "fly high and rest in love abangg"
                },
                {
                    "nama": "Manuel Frederika",
                    "nim": "124450039",
                    "umur": "20",
                    "asal": "Batam",
                    "alamat": "Way kandis",
                    "hobbi": "Katama",
                    "sosmed": "manuelfdk_",
                    "kesan": "Abangnya seru dan mengayomi bangett apalagi selama magang PIKA",
                    "pesan": "Abang keren bangett, semoga sehat selalu dan semangat kuliahnya abangg"
                },
                {
                    "nama": "Ni Made Okta Viola Darma Putri",
                    "nim": "124450005",
                    "umur": "20",
                    "asal": "Lampung Tengah",
                    "alamat": "Korpri",
                    "hobbi": "Travelling",
                    "sosmed": "@violaadrtr_",
                    "kesan": "Kakaknya cantik dan ramah bangett",
                    "pesan": "Semangat terus kakak kuliahnyaa"
                },
                {
                    "nama": "Risa Romadona",
                    "nim": "124450127",
                    "umur": "20",
                    "asal": "Natar",
                    "alamat": "Natar",
                    "hobbi": "rolling skate",
                    "sosmed": "@risarmdna",
                    "kesan": "Kakaknya seru bangett",
                    "pesan": "Semoga sehat selalu dan semangat terus kakakk"
                },
                {
                    "nama": "Vannisa Ramadhani",
                    "nim": "124450078",
                    "umur": "19",
                    "asal": "Kepulauan Riau",
                    "alamat": "Telung Betung",
                    "hobbi": "Nonton KHW",
                    "sosmed": "@vunnycaa",
                    "kesan": "Kakaknya asikk dan informatif bangett waktu magangg, dan langsung salfok karna nama kita samaa",
                    "pesan": "Sehat selalu kakak, dan semoga sukses mencapai cita-citanyaa"
                },
                {
                    "nama": "Yulia Kristine Malau",
                    "nim": "124450119",
                    "umur": "20",
                    "asal": "Jambi",
                    "alamat": "Sabah Balau",
                    "hobbi": "Belajar",
                    "sosmed": "@krnylee",
                    "kesan": "Kakaknya cantikk dan ramah bangett",
                    "pesan": "Semoga semangat dan sukses selalu kakak menjalani perkulihahannya"
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
                "https://drive.google.com/uc?export=view&id=1JXtM4jXJ8farU6MWcafEeEXyuXmHfj4S",
                "https://drive.google.com/uc?export=view&id=1p42LeVz-Eabzfc1feNoe9RZnFSO02Beq",
                "https://drive.google.com/uc?export=view&id=1EhhiCH2O58yyv18hyNwlPnMS6H8eHeOf",
                "https://drive.google.com/uc?export=view&id=1WuQgy_VteB3c2hENuo5rNpZOR2il9Fty",
                "https://drive.google.com/uc?export=view&id=1gCYAxcaEjxHvqXueprR2VS3bjSH7EGU_",
                "https://drive.google.com/uc?export=view&id=1nUTX3QMCyM9uabA3JRAOLf6q2fR4wQxz",
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
                    "kesan": "Abang keya orangnya seru dan keren bangett",
                    "pesan": "When bangg skema lewat live tiktok??"
                },
                {
                    "nama": "Elsa Sitorus",
                    "nim": "124450088",
                    "umur": "21",
                    "asal": "Sumatera Utara",
                    "alamat": "Pemda",
                    "hobbi": "Rebahan",
                    "sosmed": "_els.a",
                    "kesan": "Kak Elsa orangnya asikk banget, langsung nyambung karna ngobrolin drakor thriller",
                    "pesan": "Sehat selalu kakak, wish you all the bestt di perkuliahan ini kakak"
                },
                {
                    "nama": "Fadya Izzatul 'Aini",
                    "nim": "124450062",
                    "umur": "20",
                    "asal": "Pringsewu",
                    "alamat": "Airan",
                    "hobbi": "Makan",
                    "sosmed": "@fadyaizzatul_",
                    "kesan": "Awalmya ngerasa kakaknya introvert bangett ternyata kakaknya seruu",
                    "pesan": "Semangat selalu kakak menjalani perkuliahannya"
                },
                {
                    "nama": "Lovianora Saragih",
                    "nim": "124450105",
                    "umur": "19",
                    "asal": "Sumatera Utara",
                    "alamat": "Way Huwi",
                    "hobbi": "Dengerin musik",
                    "sosmed": "@_loviaa",
                    "kesan": "Kakaknya pinter dan asik bangett, awalnya langsung salfok jugaa karna sama sama saragihh",
                    "pesan": "Semangat selalu kakak mc kerenn"
                },
                {
                    "nama": "M. Alsi Syahrulloh",
                    "nim": "124450092",
                    "umur": "20",
                    "asal": "Kalianda",
                    "alamat": "Gedung Harapan",
                    "hobbi": "Main Game",
                    "sosmed": "@keyashafi",
                    "kesan": "Abangnya keliatan pendiam bangett, tapi aslinya asikk bangett",
                    "pesan": "Semangat dan sukses selalu abang dalam banyak hall"
                },
                {
                    "nama": "Sherena Florencia",
                    "nim": "124450027",
                    "umur": "19",
                    "asal": "Bengkulu Selatan",
                    "alamat": "Belwis",
                    "hobbi": "Make up",
                    "sosmed": "@sher_renna",
                    "kesan": "Kakaknya gemass sekalii",
                    "pesan": "Makasii banyak kakak pembimbing skemaa"
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            gambar_urls_Divisi_Research_Development = [
                "https://drive.google.com/uc?export=view&id=1Z1Umd92c7qsdRmdRunww_07hPCtmF8sq",
                "https://drive.google.com/uc?export=view&id=1QI1ntusafPudmdnQHK-BuTGc6wPsFrt0",
                "https://drive.google.com/uc?export=view&id=1yBN9b2P0fiwrKPqMi89yERJ3G5gpiOjw",
                "https://drive.google.com/uc?export=view&id=1mMLUNfieJhrTl9YqcezE2fh49OCUpv_5",
                "https://drive.google.com/uc?export=view&id=1QGtdVuCAwzuVDYwtR7uWaOI8e5Yhgxui",
                "https://drive.google.com/uc?export=view&id=1BfL6nxwx4hT1UFsMPQP4DHsEwO26oLVc",
                "https://drive.google.com/uc?export=view&id=1NotOgtDJs0I4SCsZ4Y8_MuuEyCtoe0af",
                "https://drive.google.com/uc?export=view&id=1FgVdV9Igt_Jsd95pgjHGOKBmi0AsCsH5"
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
                    "nim": "124450099",
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


#Internal
elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
                "https://drive.google.com/uc?export=view&id=1_22Ot7dURl2Dkcgww2JcaqE54TftXc2u",
            ]
            data_list_Kadep_internal = [
                {
                    "nama": "Haikal Fransisko Simbolon",
                    "nim": "123450106",
                    "umur": "23",
                    "asal": "Jambi",
                    "alamat": "Jatimulyo",
                    "hobbi": "Ngeroasting orang",
                    "sosmed": "@haikalsbln_",
                    "kesan": "",
                    "pesan": ""
                },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
                "https://drive.google.com/uc?export=view&id=1Q4FYjagiTUnquoVoclMmCaAj1t0jVWy-",
            ]
            data_list_sekdep_internal = [
                {
                    "nama": "Kharisma Mustika Sari",
                    "nim": "123450034",
                    "umur": "21",
                    "asal": "Waikana",
                    "alamat": "Untung Seropati",
                    "hobbi": "Suka menolong orang",
                    "sosmed": "@rismaa.mustika_",
                    "kesan": "",
                    "pesan": ""
                },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
                "https://drive.google.com/uc?export=view&id=1TenWgvq3ebI8oxhXnKYPyGhgermj7iN_",
                "https://drive.google.com/uc?export=view&id=1Rb5o6OuJ15DTiSG6BgzpnfOmnkn-6-x5",
                "https://drive.google.com/uc?export=view&id=19JbaZa2qks1WS2EV6jLdoCRLU30HEnGY",
                "https://drive.google.com/uc?export=view&id=18a5e_C5ibhqB10Sy1-RZi-GYabjhv9hx",
                "https://drive.google.com/uc?export=view&id=1FM_XqTZBnwctdV3jSVrwSMy-Vn0s83ZT",
                "https://drive.google.com/uc?export=view&id=1w7x8-KzvlkvfLaH7btqK8yC3BjfNHvWW",
                "https://drive.google.com/uc?export=view&id=1qjPWTUFLBptWjNZ0oD42oAmeXkHS9o2E",
                "https://drive.google.com/uc?export=view&id=1U-wlwZb2o5VA7tUGy-LxEhE1MRb-PuR_",
            ]
            data_list_keharmonisasian = [
                {
                    "nama": "Hanna Gresia Sinaga",
                    "nim": "123450038",
                    "umur": "21",
                    "asal": "Kisaran City",
                    "alamat": "Sukarame",
                    "hobbi": "Menyapa satpam ITERA",
                    "sosmed": "@hanna_g_sinaga",
                    "kesan": "",
                    "pesan": ""
                },
                {
                    "nama": "Ahmad Farhan Ghani",
                    "nim": "12450121",
                    "umur": "20",
                    "asal": "Keliling",
                    "alamat": "Kemiling",
                    "hobbi": "Olahraga menembak",
                    "sosmed": "@farhnghnii",
                    "kesan": "",
                    "pesan": ""
                },
                {
                    "nama": "Aisyah Khairun Nisa",
                    "nim": "124450009",
                    "umur": "20",
                    "asal": "Riau, Air Molek",
                    "alamat": "Belwis",
                    "hobbi": "Menulis whishlist",
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
                    "kesan": "-",
                    "pesan": "-"
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
                    "kesan": "Kakanya gemass bangett",  
                    "pesan":"Semangatt terus ka kuliahnyaa"
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
                    "pesan":"Semangatt bang menjalani perkuliahan dan proker himpunannya!"
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
                    "pesan":"Sumpah terimakasih banyak kaaa udah ngambil kesempatan untuk jadi astut LMD. Saya merasa terbantu bangettt. Maaf juga kemarin aku banyak diamnya pas tutor karena kebetulan waktunya berbarengan dengan wwc dan hal lainnya"
                },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
                "https://drive.google.com/uc?export=view&id=1QCy5E_jcLzRTZN_ass7Ku44iu534TGWi",
                "https://drive.google.com/uc?export=view&id=1FkJT8xsFBryQaLZ5x-yFlV4z47I9g7aj",
                "https://drive.google.com/uc?export=view&id=1kfl0Y3LGpP7qY50nIwMpMmZn0KXUFTCn",
                "https://drive.google.com/uc?export=view&id=1n4kmsvRfcjGumryHfSgb4PZatOtug-y2",
                "https://drive.google.com/uc?export=view&id=1k2l1tERi1SDvxTbN-1h8bGccy1Lo43kh",
                "https://drive.google.com/uc?export=view&id=1A94LLT8sVlEpVKTDpIXeKEQo07PDpnzV"
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
                    "pesan":"Semangattt bang kuliahnyaa!"
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
                    "pesan":"Sehat selalu dan semangat kuliahnya kaa!"
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
                    "pesan":"Semangatt kaa kuliahnyaa!"
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
                    "pesan":"Jangan lupa jaga kesehatan dan semnangat kuliahnya kaa!"
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
                    "pesan":"Semangattt kuliahnya bangg"
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
                    "pesan":"Semangat teruss kaa kuliahnyaa!!"
                },
            ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
    internal()


#Medkraf
elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
                "https://drive.google.com/uc?export=view&id=1L51CvY4QiKMnradQFhEnjIwyo3erc0C-",
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
                    "jabatan": "Kepala Departemen",
                    "kesan": "KAKA KERENN!!",
                    "pesan": "Jujur takjub sih aku untuk orang orang di bidang media kreatif, walaupun dikejar dl desain tapi masih tangguh sekali"
                },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
                "https://drive.google.com/uc?export=view&id=1TqoHfc4de6O6PVN60s-b1aUrWfihnLDf",
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
                    "divisi": "Sekdep",
                    "jabatan": "Sekdep",
                    "kesan": "KEREN JUGA JUJURRR",
                    "pesan": "Tetap semangat terus ya kaaa, semoga apapun wishlist kaka bisa tercapai satu persatuu"
                },
                ]
            display_images_with_data(gambar_urls_sekdep_medkraf, data_list_sekdep_medkraf)

        with tab3:
            gambar_urls_Divisi_dokumentasi = [
                "https://drive.google.com/uc?export=view&id=1aZh1bEQ4sjm7lbMz_YxLtETGfme3r-Xc",
                "https://drive.google.com/uc?export=view&id=1WWlLL4kI5wjDbDF3VsIxEX5FijH42jQ-",
                "https://drive.google.com/uc?export=view&id=16KHE7iGBzFGZFnRzqk3F7qc9ZnZ0bL5B",
                "https://drive.google.com/uc?export=view&id=1PRXTkU3UbOGDlCVYe4Aw89_c36rMhuHX",
            ]
            data_list_Divisi_dokumentasi = [
                {
                    "nama": "Labo Napitupulu",
                    "nim": "123450037",
                    "umur": "20",
                    "asal": "Jakpus, Medan, Palembang",
                    "alamat": "Way Huwi",
                    "hobbi": "Tong setan",
                    "sosmed": "noerruuu",
                    "divisi": "Dokumentasi",
                    "jabatan": "Kepala Divisi",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Kerennnnn",
                    "pesan": "Semangattt terus banggg!! sempetin waktu untuk abang istirahat sejenak dari organisasi dan perkuliahan yaa"
                },
            ]
            display_images_with_data(gambar_urls_Divisi_dokumentasi, data_list_Divisi_dokumentasi)

        with tab4:
            gambar_urls_Divisi_Media_dan_Konten_Spesialis = [
                "https://drive.google.com/uc?export=view&id=1jAjigvOFxbe0slztVsxPGxRqiTC-yqVT",
                "https://drive.google.com/uc?export=view&id=19wxS6Srb2xiLdObpHkTxGUAE9KTpYp0h",
                "https://drive.google.com/uc?export=view&id=1Ou29VazmLZG1ef-e49h8IwS8xka-ihy_",
                "https://drive.google.com/uc?export=view&id=1YNKtLY2Wbs_DgCQCZXX2GM2VNBeLkDge",
                "https://drive.google.com/uc?export=view&id=1Z52mXJVDlFy1eAv-GH6PRqkVLeiIIUct",
                "https://drive.google.com/uc?export=view&id=1bKPTrpHtiKXsvNO-Be7BicQgaXypncQP",
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
                    "jabatan": "Kepala Divisi",
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
                    "jabatan": "Anggota",
                    "kesan": "My kaka cantik, ramah, and imutt",
                    "pesan": "Terus bahagia ya ka Allishaa!"
                },
                {
                    "nama": "Alya Ramadhanti",
                    "nim": "124450091",
                    "umur": "19",
                    "asal": "Jambi",
                    "alamat": "Airan",
                    "hobbi": "Jalan-jalan dengan sepatu roda",
                    "sosmed": "alya.rmdhnti",
                    "divisi": "Media dan Konten Speasialis",
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Gemass",
                    "pesan": "Semangat selalu kaa kuliah dan organisasinyaa"
                }
            ]
            display_images_with_data(gambar_urls_Divisi_Media_dan_Konten_Spesialis, data_list_Divisi_Media_dan_Konten_Spesialis)

        with tab5:
            gambar_urls_Divisi_Visual_Design = [
                "https://drive.google.com/uc?export=view&id=1kN7SpqUYMvb4SMNHJW-L_DBjUptiESmm",
                "https://drive.google.com/uc?export=view&id=1Bz_-Vxvd5-WQsOp6DcdX-JPIQoPS8sVu",
                "https://drive.google.com/uc?export=view&id=1_oMlGbvZTwUD3A7EPRk68P0LYWTtvOxT",
                "https://drive.google.com/uc?export=view&id=1jNMkXUc-F9jWx5_F9gXxo1Q1Tqhd2wW6",
                "https://drive.google.com/uc?export=view&id=1uR9t2h9Nz61sOCiknUUyvcJWjrjoEcwc",
                "https://drive.google.com/uc?export=view&id=1-38NJRyawLG-6GOP_5pK28tOopodbdKj"
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Kakanya baik dan ramah",
                    "pesan": "Semangatt terus ka, semoga selalu berbahagiaa"
                },
                {
                    "nama": "Zannuba Arifah Ilman",
                    "nim": "124450112",
                    "umur": "19",
                    "asal": "Jabung",
                    "alamat": "Rajabasa",
                    "hobbi": "Bobo",
                    "sosmed": "@Xifasky",
                    "divisi": "Media dan Konten Spesialis",
                    "jabatan": "Anggota",
                    "kesan": "Cantik dan ramah sekalii",
                    "pesan": "Semangattt kaa untuk kuliah dan organisasinyaa!!"
                }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()


# Eksternal
elif menu == "Departemen Eksternal":
    def eksternal():
        st.markdown("<h3 style='text-align: center;'>Departemen Eksternal</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen","Divisi Hubungan Luar", "Divisi Pengabdian Masyarakat"])

        with tab1:
            gambar_urls_Kadep_eksternal = [
                "https://drive.google.com/uc?export=view&id=1vps6tIJFvkAamW_3McxlubOMzVYiHA5q",
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
                    "kesan": "Karismatik woman, baik tapi tegas",
                    "pesan": "Sukses selalu kaa kedepannya, dan nanti semangat nyusun TA nyaa!!"
                },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
                "https://drive.google.com/uc?export=view&id=19RknLMprIhukgImx6GM_XobOXP_WCQjj",
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
                    "kesan": "Cantik dan baikk",
                    "pesan": "Semangatt kaa kuliahnyaa dan juga semangatt nyusun TA nya!!"
                },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)

        with tab3:
            gambar_urls_hubungan_luar = [            
                "https://drive.google.com/uc?export=view&id=1jh3L8ZHuy9SBgbbks4WSDYLwdpqchBAE",
                "https://drive.google.com/uc?export=view&id=1ikq2Syi9ZEtYxAHskGG8zGY6wt1pCs7w",
                "https://drive.google.com/uc?export=view&id=1vvMzlaqOqhpouBklqfcXZ0bGv0nKIySy",
                "https://drive.google.com/uc?export=view&id=10GYntdjuCsnHPiiYcSiQXE8oUDChokbM",
                "https://drive.google.com/uc?export=view&id=12aLF_c06D8Rju8D5fRdqTuTA8QN7fEXr",
                "https://drive.google.com/uc?export=view&id=1ShYfa8sB6fDruh40A4s80XFQfIGY66uj",
                "https://drive.google.com/uc?export=view&id=1vqFkfawpF_Z3WMA5NyIJ-3ZIqVDgitAh",
                "https://drive.google.com/uc?export=view&id=1WMJV6xQuO4BIv9xPK6CROdVMjrw92UrC",
                "https://drive.google.com/uc?export=view&id=1XSbu7cdYSl4cwkepqn4_xHpoSRqOUBIE",
                "https://drive.google.com/uc?export=view&id=1FKxfXOtQK98ZeA8kHkVrwzpuGw1tOzvd",
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
                    "jabatan": "Kepala Divisi",
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
                    "jabatan": "Staff Ahli",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Gemass",
                    "pesan": "Jaga kesehatan ya kaa, dan semangat juga kuliahnya!!"
                },
                {
                    "nama": "Yollanda Agustina",
                    "nim": "124450024",
                    "umur": "20",
                    "asal": "Kerangka Bawang Sebelah Barat",
                    "alamat": "Jati Agung",
                    "hobbi": "Bermain futsal",
                    "sosmed": "@yollanda_agustina16",
                    "divisi" : "Hubungan Luar",
                    "jabatan": "Anggota",
                    "kesan": "Semangatt terus ka yollandaaaa, kak yollanda keren hebat and kuattt",
                    "pesan": "Jaga kesehatan ya kaa, apalagi kaka ambil banyak kepanitian. Jangan sampe drop kaa"
                },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)

        with tab4:
            gambar_urls_pengabdian_masyarakat = [
                "https://drive.google.com/uc?export=view&id=1YsDX_BzE2TEx7wWVehey6Czs21pr-OS7",
                "https://drive.google.com/uc?export=view&id=1blcyMnNXd5d12bVhHDy9jxwqVVnGprKx",
                "https://drive.google.com/uc?export=view&id=1t87F5y2fMYCCMUehc0rf-Zylz703cL4N",
                "https://drive.google.com/uc?export=view&id=1htK6I_pgeoHM6F1pjDTUrg5TsLJsQbal",
                "https://drive.google.com/uc?export=view&id=1MDgtiC7Iszi2cwd3VTXYpyTFrfkS7SNd",
                "https://drive.google.com/uc?export=view&id=1TLU43zhPQI4ecU20yAXdGwEor34jGT80",
                "https://drive.google.com/uc?export=view&id=1E254nYVDqHUrRpZ8Bc3fdim2dGkA13cI",
                "https://drive.google.com/uc?export=view&id=139SgWR-USXwXLdupgRbdfiEAMjSzwkcP",
                "https://drive.google.com/uc?export=view&id=1jaYYsgs37iVuKD46DAGPr-vC7e3TbXTo",
                "https://drive.google.com/uc?export=view&id=1dORUH_2mTvrUAGYyP5GO77E2fI31WBh2",
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
                    "jabatan": "Kepala Divisi",
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
                    "jabatan": "Staff Ahli",
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
                    "jabatan": "Staff Ahli",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Keren dan baik",
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
                    "jabatan": "Anggota",
                    "kesan": "Abang keren kalau ga marah-marah",
                    "pesan": "Panjang umur sehat selalu bang, tetep semangat kuliah walau setiap semesternya bikin asam lambung naik"
                },
                {
                    "nama": "Muhammad Rizaldi",
                    "nim": "124450093",
                    "umur": "Masih muda lah",
                    "asal": "Rahim Ibu",
                    "alamat": "Pasar lantai 3.5",
                    "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                    "sosmed": "@jaldii._",
                    "divisi" : "Pengabdian Masyarakat",
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
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
                    "jabatan": "Anggota",
                    "kesan": "Ramah dan cantikk",
                    "pesan": "Vibes kakanya ceria dan positif bangett"
                },
            ]
            display_images_with_data(gambar_urls_pengabdian_masyarakat, data_list_pengabdian_masyarakat)
    eksternal()


# PSDA
elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        # Template Tab Divisi PSDA
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
                "https://drive.google.com/uc?export=view&id=1AYL9sUo_IF_kveguAuldS8RDg4J8E3iP",
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
                "https://drive.google.com/uc?export=view&id=1EaekZH3x1UjypC00hNP9RRbHia54WT9l",
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
                "https://drive.google.com/uc?export=view&id=1RUKNNCd3XbyKI8YOH391xhLxNYSdxZ3Z",
                "https://drive.google.com/uc?export=view&id=1f5M4VB3hA9yNryzoiFP3MoiE1DIBEpfw",
                "https://drive.google.com/uc?export=view&id=1JyDedG_ucJU1exiEiVw2RFQjPp3rhojB",
                "https://drive.google.com/uc?export=view&id=1NmGGQKxNVy2K9h5g7hBwIFuG7dywNMO0",
                "https://drive.google.com/uc?export=view&id=1D4TrQXRhQzV8nTd97Ln_vV3suzVleed4",
                "https://drive.google.com/uc?export=view&id=16qS9fZ1xD21DW5WG9xxSqrTK86SNOX6T",
                "https://drive.google.com/uc?export=view&id=1FB9Ebft5vzR5nss8A2all6fdmTGY261r",
                "https://drive.google.com/uc?export=view&id=1VHsIU-5HLP_oHDEhiNHQeoriPb3pgdoV",
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
                "https://drive.google.com/uc?export=view&id=15VRqGpGb-cW93Y0Zigbc5KiAd3tvEV1w",
                "https://drive.google.com/uc?export=view&id=1em2TMyTrpvevZs56PQJ6wGt8ID4SzmG5",
                "https://drive.google.com/uc?export=view&id=12Wf6Gg9hjF0Ate6KDyjYfqhOu-5_OLip",
                "https://drive.google.com/uc?export=view&id=1nFJiGA3GXbXBkHd7TT8_mg6k3bzCsXj2",
                "https://drive.google.com/uc?export=view&id=1iXvt5it8esozONnWnXCKsz-SEm1cL7kV",
                "https://drive.google.com/uc?export=view&id=14Jory3linmPbywDzYWePDvWWboLpbq_n",
                "https://drive.google.com/uc?export=view&id=162ehBTKe7fp3GyU4qB3vLyaX3HT4txXb"
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