
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
            "https://drive.google.com/uc?export=view&id=1_eqne9wh7Vv3r72alnNC09hPcCCcozBA",
            "https://drive.google.com/uc?export=view&id=1A64fxbdMjm5-4tAkRQEfv-4TAvGDudYF",
            "https://drive.google.com/uc?export=view&id=1oI-tT7AdEqI1YOlPBf4vookLQPQvnZ6K",
            "https://drive.google.com/uc?export=view&id=17HrIBmIQ4HNvBWrX2sRAqIkiFLwbnVhT",
            "https://drive.google.com/uc?export=view&id=1-G9OLCTeEkZJT4D_4wEoi8theUGrLRj_",
			"https://drive.google.com/uc?export=view&id=1Kq9LFbKNgmgMMjhaFoaPTnsE7UaxAmlZ",
        ]
        data_list = [
            {
            "nama": "Ginda Fajar Riadi Marpaung",
            "nim": "123450103",
            "umur": "22",
            "asal":"Batam",
            "alamat": "Sekretariat HMSD",
            "hobbi": "Push Rank IMO",
            "sosmed": "@jars_mrp",
            "jabatan" : "Ketua Himpunan",
            "kesan": "cara abang membawa suasana itu the best and motivator terbaik jujur keren bgt",  
            "pesan":"BANYAK BANYAK TERIMAKASIH BUAT ABANG KARENA SUDAH MENJADI KAHIM DI SAINS DATA INI ABANG KEREN BGT AND AMANAH JUGA SEMOGA KEBERUNTUNGAN DAN APAPUNYANG ABANG SEMOGAKAN SELALU DI KABULKAN "# 1
            },
            {
            "nama": "Muhammad Aqil Ramadhan",
            "nim": "123450046",
            "umur": "22",
            "asal":"Bangkinang",
            "alamat": "Sekretariat HMSD",
            "hobbi": "Dzikir",
            "sosmed": "@muhammadaqil1111",
            "jabatan" : "Sekretaris Jendral",
            "kesan": "bisa serius bisa ngelucu juga and ternyata punya jiwa pendengar yg baik",  
            "pesan":" semangat terus bang makasih udah jadi bagian terbaik di himpunan sains data dan semoga urusan abng selalu di permudah bangg! "# 1
            },
            {
            "nama": "Efi Defiyati",
            "nim": "123450005",
            "umur": "21",
            "asal": "Lampung Timur",
            "alamat": "Airan",
            "hobbi": "Membaca",
            "sosmed": "@eeffiidefi",
            "jabatan" : "Sekretaris 1",
            "kesan": "lucuu ",  
            "pesan":"semangat terus ka semoga  skripsi kaka di permudah"# 1
            },
            {
            "nama": "Qois Olifio",
            "nim": "123450067",
            "umur": "22",
            "asal": "Batam",
            "alamat": "Kota Baru",
            "hobbi": "Mainin Surat",
            "sosmed": "@qoisolifio_",
            "jabatan" : "Sekretaris 2",
            "kesan": "vibes aura cowo green flag nya keren parah",  
            "pesan":"terus jadi orang baik ya bang"# 1
            },
            {
            "nama": "Hafsa Fazila Arradhi",
            "nim": "123450079",
            "umur": "21",
            "asal": "Bandar Lampung",
            "alamat": "Bandar Lampung",
            "hobbi": "Berenang",
            "sosmed": "@hafsafazilaa",
            "jabatan" : "Bendahara 1",
            "kesan": "keliatannya pasti orangnya excited bgt",  
            "pesan":"semangat terus kaka bendahara kami semoga apapun yang kaka semogakan tergapai ya ka"# 1
            },
            {
            "nama": "Luthfia Laila Ramadhani",
            "nim": "123450004",
            "umur": "20",
            "asal": "Bengkulu",
            "alamat": "Airan",
            "hobbi": "Bertemu Pak Tirta",
            "sosmed": "@luthfiaarmdhni",
            "jabatan" : "Bendahara 2",
            "kesan": "JUJUR SUKAAAA BGTTTT SAMA KAKA AURA RANGKUL ORANG LAIN ITU KUAT BGT",  
            "pesan":"SEMANGAT TERUS YA KAKA MAKASIH ATAS MOTIVASI YANG UDAH KAK BRIKAN KARNA ITU MASIH NGEBEKAS SAMPAI SEKARANG LOV U KA SEMOGA KEBAHAGIAAN DAN KEBERUNTUNGAN SELALU NGEKOR KAKA"# 1
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
           "https://drive.google.com/thumbnail?id=1_6KnPcmklW2dKWluPneTq_FvB2kURpOC&sz=w1000",
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
            "kesan": "LUCU DAN HUMBLE",  
            "pesan":"semangat untuk ta nya bg semoga ke hokian selalu di pihak abang"# 1
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/thumbnail?id=12tGHXk5XZYU6aKDfLgZuchRZ-Islf3c3&sz=w1000",]           
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "GEMASSSSSHHHH LUCUUUU BAIKKKKKKK BGTTT BGTTT ",  
            "pesan":"JANGANNN CAPE YAPPING YA KA KARNA YAPPINGAN KAK SELALU SERU DAN LUCUUUU SUKAAA SEMANGAT YA KAKA KEBERUNTUNGAN PASTI DIPIHAK KAKA"# 1
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/thumbnail?id=1WEKc_BNw_kXaKNJCDuC_PIGpK0Xz43KF&sz=w1000",
            "https://drive.google.com/thumbnail?id=1zNKRrzQfnbPo2U0dsCc_YZSsLxiftVs1&sz=w1000",
            "https://drive.google.com/thumbnail?id=12cE4CtiOisEyj-7u6Duufk88kSWdVYcr&sz=w1000",
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
                "jabatan" : "Kepala Komisi",
                "kesan": "ORANG KEREN AND TERMOTIVASI DARI ABANG INI",  
                "pesan":"JANGAN CAPE MENCOBA HAL BARU YA BANG SEMOGA SELALU DI KELILINGI ORANG BAIK DAN HAL MENYENANGKAN!"# 1
            },
            {
                "nama": "Gh. Mikael Niko Antoni Setiadi",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jabung",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "jabatan" : " Staff Komisi",
                "kesan": "kirain galak ternyata baik bgt",  
                "pesan": "Semangat bang semangat untuk terus berkembang jadi lebih baik bg"# 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "jabatan" : " Staff Komisi",
                "kesan": "lucu",  
                "pesan":"Semangattt kaa kuliahnyaa "# 1
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)
        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
             "https://drive.google.com/thumbnail?id=1TjmR5Pm515AkhtyqOhvX9FODydhKco2o&sz=w1000",
             "https://drive.google.com/thumbnail?id=1a_1WhQVzrGaqOFW46Vstf1embRZ6mKX5&sz=w1000",
             "https://drive.google.com/thumbnail?id=1MXO2Kn0njwkWBLqgvJsAQz5-4RAHh7S2&sz=w1000",
             "https://drive.google.com/thumbnail?id=1OhquEqDXjSZksruutEczr2VpbvDoIUB4&sz=w1000",
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
                "jabatan" : "Kepala Komisi",
                "kesan": "Bang lucu seru juga",  
                "pesan":"semangat terus bg semoga ta nya cepet kelar!"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "19",
                "asal": "Kepulauan Mentawai",
                "alamat": "Owen Kost",
                "hobbi": "Ngoding",
                "sosmed": "@afghanisnt_",
                "jabatan" : " Staff Komisi",
                "kesan": "cantik and keren",  
                "pesan":"Semangat terus ka semoga ga bosen jadi pentutor rc ya kaa!!"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "CTR",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniquratuain_",
                "jabatan" : " Staff Komisi",
                "kesan": "cantikkkkk bgt bgtt",  
                "pesan":"semoga hal hal baik selalu di pihak kaka!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tanggerang",
                "alamat": "Teluk",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "@jeremia_hm",
                "jabatan" : " Staff Komisi",
                "kesan": "Keren dan cindonya lucu",  
                "pesan":"Semangat bang jangan bosen jadi orang baik ya bg!"# 1
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
           # URL gambar anggota Komisi III
            gambar_urls_komisi3 = [
             "https://drive.google.com/thumbnail?id=1ywSL7RKvA-2f_wHDg599164dp9sQM1xY&sz=w1000",
             "https://drive.google.com/thumbnail?id=1mqNVHl2dlSSJEAf6pOtOb0EDLkBF1r-Q&sz=w1000",
             "https://drive.google.com/thumbnail?id=1TKID95ymIE6mePc7dvTM1Atb54wOHwpQ&sz=w1000",
             "https://drive.google.com/thumbnail?id=1hKRer5d4dOa7ZU0tSuIOxi6JsulJWz4Q&sz=w1000",
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
            "jabatan" : "Kepala Komisi",
            "kesan": "Lucu",  
            "pesan":"semangat ka semoga kata kata acc selalu ngekor ya ka!"# 1
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "jabatan" : " Staff Komisi",
            "kesan": "ABANG NIM TERBAIKKKKKKKKK THE BEST LAH POKOKNYAA",  
            "pesan":"SEMANGAT TERUSS ABANGNIMM TERUSSSS BANG SEMOGA LEBIH BISA SHARING SHARING YA BANG HEHE!"# 1
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "jabatan" : " Staff Komisi",
            "kesan": "Tegas tapi ternyata baik bgt",  
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
            "jabatan" : " Staff Komisi",
            "kesan": "kirain judes ternayta baikkkk bgt",  
            "pesan":"Semangat yaaa kaa Semoga diberi kemudahan dan kelancaran terus!"# 1
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
            "https://drive.google.com/uc?export=view&id=1olgRYQ9NcAy8wij651Kni8UU6wn8325w",
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
                "kesan": "WONDER WOMENKU MOTIVATOR PENG INSPIRASI TERBAIK CANTIK BAIK AND SOLEHAH PULAA",  
                "pesan": "SEMANGAT TERUS KAKA KU YANG CANTIKKKKKK SEDIHHH BGT KARNA KAKA TAHUN INI DAN SELANJUTNYA GA JADI SENATOR HMSD PASTI BAKAL KURANG BGT SEMANGAT YA KA UNTUK TA NYA SEMOGA KEBERUNTUNGAN DAN HAL BAIK SELALU MENGELILINGI KAKAKUUU YANG CANTIK INI LUV U BBANYAK BANYK KAKAAAA"# 1
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)

        with tab2:
            gambar_urls_biro_aspirasi= [
            "https://drive.google.com/uc?export=view&id=1lxXfp8aAfOmpuXvWe_22zGbWzQ5Abiyk",
            "https://drive.google.com/uc?export=view&id=1SO_faxm5V5_r5NFt1FCiqugPThQxlxvu",
            "https://drive.google.com/uc?export=view&id=1ao9tFwYtntSzlFP66MTKQcvzVTtRfUWH",
            "https://drive.google.com/uc?export=view&id=1zum85YU5f5qUu_qKAgyoxx4p_50vJQXG",
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
                "kesan": " lucuuuu BGTTTTTTTTTT ",  
                "pesan":"semaangat teruss bang helmy yang baik semoga nasimu selalu hangat dan bantalnnya selalu dingin bg"# 1
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "KEREN LUCU JUGA ",  
                "pesan":"SEMNAGAT TERUS YA BANG SEMOGA KEBRUNTUNGAN SELALU JADI MILIK ABANG AND BASON IS MEEEE"# 1
            },
            {
                 "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "cantik and baik bgt seruu jugaaa",  
                "pesan":"Semangat terus kak jangan pantang menyerah dan jadi pendengar yang baik ya ka btw kaka cantik bgt kalo pake pasminaaa!"# 1
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "baik bgt abangnnya ",  
                "pesan":"Semangat terus bang kuat kuat jadi kasra dan organisasinya ya bg!"# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)

        with tab3:
            gambar_urls_biro_kajian= [
            "https://drive.google.com/uc?export=view&id=1ZZF5zYy3XHmZloUZ7QvHkaG5phNZXqhU",
			"https://drive.google.com/uc?export=view&id=15p-0fDihk2pvwmG4r13CESQpXFFDSaxB",
			"https://drive.google.com/uc?export=view&id=142oPjv5d9-kPp_d_--17J9T05xUlxkdV",
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
                "kesan": "BAIK BGT LUCUU CANTIK",  
                "pesan":"Semangat ya kak TA nyaajaga kesehatan dan semoga apapun yang kak inginkan tercapai!"# 1
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "gemas lucu cantik baik inimah di borong",  
                "pesan":"Semangat terus kuliahnya semangat terus untuk berkembang ya ka and terus jadi orang yang extrovet dan lucu itu ya kaka"# 1
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "kece and baikkk bgttt",  
                "pesan":"Semangat terus bang semoga keberuntungan ke hokian dan hal hal baik selalu ngekor ya bg!"# 1
            },
            ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)

        with tab4:
            gambar_urls_biro_kesekretariatan= [
            "https://drive.google.com/uc?export=view&id=1JhEsMwYPlFfHXZzClFz-2m_5EuUb2Mm4",
			"https://drive.google.com/uc?export=view&id=1BysBCy1if1wUQCyRkAm0Cw_SwGvLnI4e",
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
                "kesan": "CANTIKNYAAAA ITU LOH BGT BGT BGT BAIKKKKK LUCUUUUU GEMASHHHHHH  THE BEST",  
                "pesan":"SEMANGAT TERUS KAKAKUUUU YANG CANTIK SEMANGAT TA NYA YA SEMOGA DIPERMUDAH YA KAKA AND BAHAGIA TERUS KAKA"# 1
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "LUCUUU GEMAASH ",  
                "pesan":"Semangat terus ka buat di bason and kuliahnya terus jadi orang exctied yg luc ya ka"# 1
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
            "https://drive.google.com/thumbnail?id=1Bq4jSAJ3a2bjtgw6GThCAgwFzAU-ADWM&sz=w1000",
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
            "kesan": "keren bgt",
            "pesan": "Semangatt terus untuk kuliah dan ta nya bg"# 1
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)


        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/thumbnail?id=1Z4FlEQrZ-LOfLsRZH8-NfcFGytgTpXDc&sz=w1000",]
            data_list_sekretaris_departemen_minbak = [ 
            {
            "nama": "Gusti Putu Ferazka Dhiyamika",
            "nim": "123450046",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Dadi",
            "hobbi": "Mendaki",
            "sosmed": "@ferazkaa",
            "kesan": "cantik and lucu",
            "pesan": "Semangatt terus kak kuliah dan TA nya, semoga dimudahkan segala urusannya yaa kaka"# 1            
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)            

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [            
           "https://drive.google.com/thumbnail?id=1P_jL5m4Oc5x-X3X7-xo7vYd9eU3jY3vx&sz=w1000",
           "https://drive.google.com/thumbnail?id=1BtTdZnlVOa4wS2ioWaluQVBqTm88iEIA&sz=w1000",
           "https://drive.google.com/thumbnail?id=1yP_i19ShGmyFxx5dWqZP92Npdxa-NKL1&sz=w1000",
           "https://drive.google.com/thumbnail?id=1dnWnKGhK4hxG3ko0SNEY7K8hSGXWwQkl&sz=w1000",
           "https://drive.google.com/thumbnail?id=13fHo91b1ClWzwrPtD4JRp6_2HhGcaXtC&sz=w1000",
           "https://drive.google.com/thumbnail?id=1-yTo9F3PRr2tGyNkZ4_Uqj3u2WMHOJLl&sz=w1000",
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
            "kesan": "keren",
            "pesan": "Semangatt terus bang semoga di permudah segala urusannya bang"# 1
            },
            {
            "nama": "Ayu Andriani Parlina Wati",
            "nim": "124450058",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Airan",
            "hobbi": "Belajar + menghitung uang",
            "sosmed": "@aayuandriani_",
            "kesan": "aktif",
            "pesan": "keren kaka semangat terus"# 1
            },
            {
            "nama": "Dafa Elpriza",
            "nim": "124450131",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Kandis",
            "hobbi": "Jogging",
            "sosmed": "@dafaelpriza_",
            "kesan": "baik bgt",
            "pesan": "semangat teru bang semoga nilai uts tinggi"# 1
            },
            {
            "nama": "Juwita Sari",
            "nim": "124450066",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Pemda",
            "hobbi": "Mancing",
            "sosmed": "@ju.juwitaaa_",
            "kesan": "ramah bgt",
            "pesan": "Semangat terus kuliahnya kaa, Lulus cepet ya kak, biar gak jenuh.!"
            },
            {
            "nama": "Muhammad Afdal Luthfi",
            "nim": "124450047",
            "umur": "19",
            "asal": "Lampung Tengah",
            "alamat": "Jl. Pulau Damar",
            "hobbi": "Memantau dl tugas",
            "sosmed": "@afdall.03",
            "kesan": "baik dan seru",
            "pesan": "Punya cara sendiri buat bikin ketawa"# 1
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
            "pesan": "Tetap ceria ya kak!"# 1
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
            "https://drive.google.com/thumbnail?id=106bKOVfJZ2AdLn4PW-U3c2hiAkOJfY9q&sz=w1000",
            "https://drive.google.com/thumbnail?id=1th_DDwNN5jPGBCVfyktdCBYKVzVsr-10&sz=w1000",
            "https://drive.google.com/thumbnail?id=1AkPrYM3LRtoDNympasBBqHlcidBz_foK&sz=w1000",
            "https://drive.google.com/thumbnail?id=12H6OWFhxxqXSP8tmKWEwzswlYggavL3K&sz=w1000",
            "https://drive.google.com/thumbnail?id=1PeSsgkxSYFhlsb4h1QenkBlhDyUmbTvp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1mXHpMrfyGWdoiXPhrnv3vJCzAh32tOcI&sz=w1000",
            "https://drive.google.com/thumbnail?id=1FdIu6aeS7RfMRpGyZxuf-QXUOM-ejdsK&sz=w1000",
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
            "kesan": "oarangnya chill",
            "pesan": "Semangat terus memimpin divisinya bang"
            },
            {
            "nama": "Andra Ilham Bintang",
            "nim": "124450060",
            "umur": "18",
            "asal": "Sumatera Selatan",
            "alamat": "Kotabaru",
            "hobbi": "Main rubik",
            "sosmed": "@andra.lhm",
            "kesan": "INIMAHHHH MANUSIA FAVORITNYA GRIWDIIIIIII BAIK BGT LUCUUU GEMASH Punya cara sendiri buat bikin ketawa",
            "pesan": "Semangatt terus ya bang Andra Semoga karirnya cemerlang di kelilingi orang orang baik apapun yang abang inginkan tercapaai keberuntungan ke hokian selalu membututi abang terlalu banyak hal dan pesan untuk sampaikan lewat ketikan ini bang andra intinta apapun itu jangan bosen jadi orang baik ya bang!"
            },
            {
            "nama": "Bryan Paskah Telaumbanua",
            "nim": "124450003",
            "umur": "20",
            "asal": "Nias",
            "alamat": "Belwis",
            "hobbi": "Live tiktok",
            "sosmed": "@bryantel_",
            "kesan": "Kating paling santai tapi, incharge",
            "pesan": "Semangat terus kuliahnya bg!"
            },
            {
            "nama": "Ghiyats Thabularasa Meardhy",
            "nim": "124450067",
            "umur": "17",
            "asal": "Surabaya",
            "alamat": "Kemiling",
            "hobbi": "Nanem Sawit",
            "sosmed": "@meardhy_ghiyats",
            "kesan": "Gemesin kalau lagi serius",
            "pesan": "Bahagia selalu di mana pun berada!"
            },
            {
            "nama": "Indah Julia Mawar Pratiwi",
            "nim": "124450055",
            "umur": "20",
            "asal": "Pringsewu",
            "alamat": "Airan",
            "hobbi": "Bengong",
            "sosmed": "@indahjuliaa",
            "kesan": "Pintar dan multitalenta",
            "pesan": "Semoga dimudahkan jalannya."
            },
            {
            "nama": "Jacinda Kesya Alvara",
            "nim": "124450023",
            "umur": "18",
            "asal": "Kalimantan Barat",
            "alamat": "Korpri",
            "hobbi": "Nyapu depan gacoan",
            "sosmed": "@cacalvra",
            "kesan": "Gaya bicaranya khas dan gampang diingat",
            "pesan": "Semangat terus jalani hari!"# 1
            },
            {
            "nama": "Muhammad Rafka Fatih Ghathfaan",
            "nim": "124450089",
            "umur": "20",
            "asal": "Padang",
            "alamat": "Kotabaru",
            "hobbi": "Bangun pagi",
            "sosmed": "@muhammdrafka_",
            "kesan": "Abangnya seru abis",
            "pesan": "Sukses selalu dan pertahankan ke-asikan nya!"
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
            "https://drive.google.com/thumbnail?id=1P4ruEk7NETFmFwSpA5IasehjcCj_sTyC&sz=w1000",
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
                "kesan": "Humoris tingkat dewa",
                "pesan": "sSemangat terus pejuang wisuda!",
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/thumbnail?id=1Ab61TQ_y6OyEU9lI4-3-zSetyKGKhsLm&sz=w1000",
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
             "https://drive.google.com/thumbnail?id=15isF6NFx2_fp9zXGRDcHM0HEGulMmCdM&sz=w1000",
             "https://drive.google.com/thumbnail?id=1s5GvbYr-xmxzzzr7nDjm63DSaSYOQq7y&sz=w1000",
             "https://drive.google.com/thumbnail?id=1bSOCPQwxcSPGQ_JXWL-4Zwm1OCuweCu4&sz=w1000",
             "https://drive.google.com/thumbnail?id=1l1od4sbdMp2qTCL3ALQhpu5tfnuuDRTT&sz=w1000",
            "https://drive.google.com/thumbnail?id=15YH0V3v18gLUxLPvYazTOvqzIDN1r7fT&sz=w1000",
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
                "kesan": "asik ",
                "pesan": "semangat terus kuliahnya kakak !!!",
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/thumbnail?id=1oMnwYJapXVrMkpQ2psowMlFNltWy4kH2&sz=w1000",
            "https://drive.google.com/thumbnail?id=1fq9orydmm-d4Tc6RRS8OLl4CuyoZLDkS&sz=w1000",
            "https://drive.google.com/thumbnail?id=1LX00iLQB690SPQW2hoJ1kOriump8LWJB&sz=w1000",
            "https://drive.google.com/thumbnail?id=1sECCXB4H_nPKyJX9riNihBRwmSb0imxx&sz=w1000",
            "https://drive.google.com/thumbnail?id=1H926uCv7ZYVnnb3-rL7HJgxDg4ryehiP&sz=w1000",
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
                "kesan": "care",
                "pesan": "Berkah terus rezekinya!",
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kakaknya anggun tapi aslinya seru",
                "pesan": "Semoga makin sukses ke depannya.",
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
                "kesan": "Energik banget",
                "pesan": "Sukses karir dan akademiknya!",
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Ramah banget walau baru kenal sebentar",
                "pesan": "Jaga kesehatan ya kak, jangan kebanyakan begadang nugas mulu.!"  
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kaka pembawaannya tenang",
                "pesan": "emangat terus ngejar impiannya, sukses dan sehat selalu ya kak!",
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
            "https://drive.google.com/thumbnail?id=1o07fmiQzVz4bLjDXXoOkVjCWu1Ne5eot&sz=w1000",
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
                "kesan": "Punya gaya ngomong yang khas ala podcaster professional",
                "pesan": "Keren banget pembawaannya, sukses terus karir public speaking-nya!"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/thumbnail?id=1mxDgGzf8uBH3XK5WRzpvclgn4VU0O8-I&sz=w1000",]
            data_list_sekretaris_mikfes = [ 
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "Kating yang punya senyum paling adem",
                "pesan": "Bahagia terus ya kak, aura positifnya nular"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://www.python.org/static/community_logos/python-logo.png",
            "https://drive.google.com/thumbnail?id=1XtG_ZfrdGQNQ2uo81JfbkgoeNqFWLv_R&sz=w1000",
            "https://drive.google.com/thumbnail?id=1H4AVQDDp3D_SDGRUMDlIuWeetI4JiE-m&sz=w1000",
            "https://drive.google.com/thumbnail?id=1jfZnLSfXikDqysSogDfT-uvQCWIzvYoL&sz=w1000",
            "https://drive.google.com/thumbnail?id=12gls_Lyb_fXck_hN6hyIpPBqXmHg6SQY&sz=w1000",
            "https://drive.google.com/thumbnail?id=1TwHu2IcGviK7BQu_RGGH-4Fn-vVjWsun&sz=w1000",
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
                "kesan": "Inspiratif kuuuu",
                "pesan": "semoga amal ibadah di terima dan abang orang baik mudah mudah di berikan tempat terbaik"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Orangnya asik diajak diskusi soal masa depan",
                "pesan": "Rekomendasinya mantap, sukses terus kuliahnya!"
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
                "pesan": "semangat dan bahagia trs ka!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kakaknya ramah dan baik banget ngerangkul",
                "pesan": "Semangat ngejar impian, sukses selalu ya kak!"
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
            "https://drive.google.com/thumbnail?id=1bHKQ4Tc2hSjGmkyvS9ZgqSyWHDMVjjYn&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Mx4lit-cBsOUp0HBdJweHZtWvH48gncr&sz=w1000",
            "https://drive.google.com/thumbnail?id=1YtLqOG6XFqj0JsPg8rweDNKtq-0_G10W&sz=w1000",
            "https://drive.google.com/thumbnail?id=1a0i6hbYBcdJQM85NXmazjdqwo1SgCZFp&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CjAfhaM3NLp2doxquHIuzSjOX5fwVk5K&sz=w1000",
            "https://drive.google.com/thumbnail?id=1h_b_pd75NDVc4MO3utND8gHe4M9d78kG&sz=w1000",
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
                "pesan": "semangat terus ka elsa cantik Kreativitasnya jangan sampe padam, sukses!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Asik banget diajak diskusi serius maupun becanda",
                "pesan": "Semangat ngejar impian, sukses selalu ya kak!"
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
                "pesan": "Sukses terus hobi dan kuliahnya!"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "ramah banget kesemua orang",
                "pesan": "Semangatt terus ya bang kuliahnya ka"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Suka ngasih rekomendasi",
                "pesan": "Jangan lupa istirahat yang cukup ya kak"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_Divisi_Research_Development = [
            "https://drive.google.com/thumbnail?id=1Mwj4pD2lnxjaIq6F69WPeEpgP_qjjWsd&sz=w1000",
            "https://drive.google.com/thumbnail?id=1u7vSwFTylY80JUU3rqdYqdrz8C5hNU9i&sz=w1000",
            "https://drive.google.com/thumbnail?id=1z6cHQuv_qofh9kHU0hOLpboCnh2z1y8g&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Crkfe788ajSozKZlohdfuEAETtFFlLvo&sz=w1000",
            "https://drive.google.com/thumbnail?id=1aTk_2KuzfLuT40RAW8FPd9gaJUTFfApq&sz=w1000",
            "https://drive.google.com/thumbnail?id=1SB6XUYsXNiL6oL3xqJuZK3vogiyWjD2r&sz=w1000",
            "https://drive.google.com/thumbnail?id=1IM_x_UyBrFtGgXvWB6Z6mbb7duV6Z0hy&sz=w1000",
            "https://drive.google.com/thumbnail?id=1eaHfCzNFPt5mDRl3JVbYrz8fAbsmnkli&sz=w1000",
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
                "kesan": "Pinter bangett",
                "pesan": "Semangattt bang nanti TA semoga dipermudah wisudanya"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "Baik hati, ramah, dan tidak sombong sama sekali",
                "pesan": "ukses karir dan akademiknya"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": " kerennnn",
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
                "kesan": "tingkanya luc",
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
                "pesan": " JUJURRR keren and pinter BGTTT"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": ",CUTEEE",
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
                "kesan": "Inspiratif person INTINYA KEREN ABIS",
                "pesan": "SEMANGAT TERUSS BANG SEMOGA BISA IKUT JEJAK ABANG!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "KEREN BERWIBAWA TAPI LUCU AND HAMORIS",
                "pesan": "semoga kebrruntungan sealu nyasar ke abg!"
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
           "https://drive.google.com/thumbnail?id=1zv7dTAuHCCsODl5dwUmkHV3RbqkXWrAe&sz=w1000",
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
                "pesan":"semangat penjuang ta dan wisuda bg"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
            "https://drive.google.com/thumbnail?id=1jn6VQVYcgSZ0BJMBps9KDzbIdf8XoYdz&sz=w1000",
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
                "kesan": "Cantik dan ramah baik juga",  
                "pesan":"Semangattt kaa untuk TA nyaa, ttp care ke diri sendiri ya ka!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
           "https://drive.google.com/thumbnail?id=1U2KYCEdTwIp-SLQd9hyeWs-1YqHAXQob&sz=w1000",
           "https://drive.google.com/thumbnail?id=1E0cAu65pRitsxtlKICBD5hoPLqWVx3mw&sz=w1000",
           "https://drive.google.com/thumbnail?id=184IE6mM2Y6_d4ysKh4RsgORKEnVkoeJm&sz=w1000",
           "https://drive.google.com/thumbnail?id=1-3j2PT_Zx3c1IbBy4TnLeqvQHRWQtoCs&sz=w1000",
           "https://drive.google.com/thumbnail?id=1-YugqV92HqWA9jAJ2G6t9fVCaUv81G3Q&sz=w1000",
           "https://drive.google.com/thumbnail?id=15UDsHfhRBJNsNGn7yiMagpPzTWuE2rXC&sz=w1000",
           "https://drive.google.com/thumbnail?id=1wPERp0MKgFmaBemnozo4O7ewG84gVzBi&sz=w1000",
           "https://drive.google.com/thumbnail?id=1C6SNGZbcm2_Cf8tI3_rgsvu6u9w6YQxD&sz=w1000",
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
                "kesan": "Positig energy",  
                "pesan": "Semoga kaka selalu dilingkupi kebaikan  yaw kaka!"# 1
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhnghnii",
                "kesan": "asik bgt",  
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
                "kesan": "ucu bgt ",  
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
                "pesan":"sehat terus ya ka!"# 1
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal": "Kisaran City",
                "alamat": "Pemda",
                "hobbi": "Kick Boxing",
                "sosmed": "@jay.saputratmb",
                "kesan": "Asik ",  
                "pesan": "Semangatt kuliahnya bangg, semoga yg abg usahakan bisa di daapaatkan"# 1
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
                "kesan": "Abang keren ",  
                "pesan":"semangat terus bg!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "kirain judes ternyata ngga",  
                "pesan":"semangat terus kaka ttp jaga kesehaatan ya ka"# 1
            },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
            "https://drive.google.com/thumbnail?id=1SGKtZC7j29VK7yGtKcB42BDjEjrevQyi&sz=w1000",
            "https://drive.google.com/thumbnail?id=1DsGK1fRvGGJBwswsqXQv2FjioZ7tDbJz&sz=w1000",
            "https://drive.google.com/thumbnail?id=1rcWBl8wsJa7Dv02MhQlSd1Ig9r8qUcYJ&sz=w1000",
            "https://drive.google.com/thumbnail?id=1gp-v_SHOivEWY7D9kpxd4610LX_IwNAI&sz=w1000",
            "https://drive.google.com/thumbnail?id=1y7azTaS6bmnf2yntG6njFpmKRUX061WE&sz=w1000",
            "https://drive.google.com/thumbnail?id=18JiSS5GrjLCZ5HvOZTAMa8KWBEWDtX1W&sz=w1000",

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
                "kesan": " ramah",  
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
                "kesan": "lucuw",  
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
                "kesan": "punya vibes tersendiri",  
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
                "kesan": "kalem bgt",  
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
            "https://drive.google.com/thumbnail?id=19nyfHlhWF5mBG7ObqcD8sRjAml3MkKj5&sz=w1000"
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
                "kesan": "cantik lucu kayak bonekaaaa ucuwwnyaaa",  
                "pesan":"Semangat TA ka semoga dipermudah wisudanya"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
           "https://drive.google.com/thumbnail?id=14NaMkHnVRPV_MfCb8EreVGHZS1D3zbbx&sz=w1000"
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
                "kesan": " tegas",  
                "pesan":"Semangattt kaa untuk TA nyaa, jangan begadang terus ya ka"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/thumbnail?id=1k6eJ0bziAzxilPPI4_Kqm5pGutKkK6DW&sz=w1000",
            "https://drive.google.com/thumbnail?id=1pjq_tgWfQpRECrYYlS9ln05jyJvBCBj8&sz=w1000",
            "https://drive.google.com/thumbnail?id=1TiQEmPnhPsSr9I2EWdda2eCqqjf7jPTE&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ETRxesreIk7ha5yYZaffMSeW2xzKvv56&sz=w1000",
            "https://drive.google.com/thumbnail?id=1dDunO9XqKOWy34isYZOMlsuSV_wYf3aT&sz=w1000",
            "https://drive.google.com/thumbnail?id=1CFf1FXJ2EldzgcsmWw5d3ChV6-op9b9q&sz=w1000",
            "https://drive.google.com/thumbnail?id=1zSvy-0qpCd2fezbPvjaullfDi2jqiqHr&sz=w1000",
            "https://drive.google.com/thumbnail?id=1jPWO8xmUiNe6A4L-KzIM9iILnGlzItDo&sz=w1000",
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
                "kesan": "berwibawa keren pinter baik",  
                "pesan": "semangat terus pejuang ta dan wisuda!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": " keren",  
                "pesan":"semangat dan ttp care sama diri sendir ya bang"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "tegas tp ternyataa baik bgt",  
                "pesan":"sehat dan sukses selalu"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "sebernya abang ini baik bgt",  
                "pesan":"Jsemangat terus bang semoga di kelilingi hal hal baik "# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": " baik bgt bgt bgt ",  
                "pesan": "Semangat kuliahnyaa ka semoga jalanmu selalu dipermuudah"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "keren?",  
                "pesan":"Semangatt bang kuliahnya, semoga kkeberuntungan selalu ngekor bang"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Sabang",
                "alamat": "Nomaden",
                "hobbi": "Duduk samping Henry",
                "sosmed": "@putrimannaa",
                "kesan": "cantik baik",  
                "pesan":"masih inget bgt kejadian pertama ketemu semangat terus ka"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "tegas",  
                "pesan":"apapun yg kaka semogakan segera tercapai ya ka"# 1
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/thumbnail?id=1KoS8tie8yWe-9Y0tzXtW_-kb8WJ9f2Z0&sz=w1000",
            "https://drive.google.com/thumbnail?id=1DR_HHhsmd-NYf33TJZHIU4YM8zMLct8V&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ZMCVdjm-vcRJ2DYf780Z8NeKmIFZkkDV&sz=w1000",
            "https://drive.google.com/thumbnail?id=1rB9Ktfx4yNtn7Z8gJnZnKNwi4XbKUnQ_&sz=w1000",
            "https://www.python.org/static/community_logos/python-logo.png",
            "https://drive.google.com/thumbnail?id=18mD01fAsKk7nRclcRiE_80hLgz8CLvuA&sz=w1000",
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
                "kesan": "Asik ",  
                "pesan":"Semangatt TA nya nanti bangg"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": " cantik and ramah",  
                "pesan":"Semangattt kaa kuliahnyaa! "# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": " baik and ramahh sekalii",  
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
            "https://drive.google.com/thumbnail?id=1a311EypqybMvfhcNPBVY2aVaE6_JeT9f&sz=w1000",
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
           "https://drive.google.com/thumbnail?id=1Ra4rueLdlTmHWv32J9DaGZSuxhqk5XyV&sz=w1000",
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
             "https://www.python.org/static/community_logos/python-logo.png",
             "https://drive.google.com/thumbnail?id=1XvAERYZfyVzNZmXIgRwy5pjk-JBu4eqJ&sz=w1000",
             "https://drive.google.com/thumbnail?id=1MtqkPIqRYZPNCXKL26OpO23ixEsAKRGa&sz=w1000",
             "https://drive.google.com/thumbnail?id=17c7W8QlFWsM2QeJxLfjlK6mRbkOQb08j&sz=w1000",
             "https://drive.google.com/thumbnail?id=1D77RtjEjWf-mndsu04u3t-EMg4_2mcux&sz=w1000",
             "https://drive.google.com/thumbnail?id=13F1mMLukZQGB9K2AQWGKeWWiQYkc5vH4&sz=w1000",
             "https://drive.google.com/thumbnail?id=1QBv7ru206VoR8UlyCRESGNTsA3mRtJ7o&sz=w1000",
             "https://drive.google.com/thumbnail?id=1rgURQtdB43Z2VbZBFn9mHWb8NY9CN0gN&sz=w1000",
             "https://drive.google.com/thumbnail?id=13tGf_XSSkis9IWVhXn5bBni4v2kRzzC9&sz=w1000",
             "https://drive.google.com/thumbnail?id=10RMcpagA37zCGjxsnfjsZ3wrM5MtoFWv&sz=w1000",
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
                "hobbi": "Tanya bang Henry",
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
            "https://drive.google.com/thumbnail?id=1wPTWISOGQOD39gSBjXjObGQP3D6Rt-ak&sz=w1000",
            "https://drive.google.com/thumbnail?id=1z812fFVV32ayhkq5dfDxTZStNMkBJONE&sz=w1000",
            "https://drive.google.com/thumbnail?id=1TxhU-gQOTtbMLqOI9uxS_LRuP8SS-lxh&sz=w1000",
            "https://drive.google.com/thumbnail?id=1PBbXt7A2ahQFU1pAANkDrZAfMGf-GuzL&sz=w1000",
            "https://drive.google.com/thumbnail?id=1XpM-uDqF0c8AOfFHYL4TaHJSg0uEOjgh&sz=w1000",
            "https://drive.google.com/thumbnail?id=18wVmUcAhXhpw1MrDmGDUS-vKY_NZH_uj&sz=w1000",
            "https://drive.google.com/thumbnail?id=1V0kjXvwrbITq25DWecHAt74kNUUpMX4Y&sz=w1000",
            "https://drive.google.com/thumbnail?id=1zaEq-H1ZcmCB32adbmhdujz4wB1L7J1R&sz=w1000",
            "https://drive.google.com/thumbnail?id=1GrA8SWiH6pYqj9_oEyW4INf5e1YPSdlq&sz=w1000",
            "https://drive.google.com/thumbnail?id=18CtbHiNaT2FMwi3mCokznVjtSc7UC0zB&sz=w1000",
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
                "kesan": "baik",
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


elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/thumbnail?id=1-4eCiorlgMJvr0zz4hamChDrvk2Opm8t&sz=w1000",
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
                "kesan": " KERENN!!",
                "pesan": "smeangat terus kak"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/thumbnail?id=122S8ERj32_JvCyU1ZwzKVUix2slRkVsX&sz=w1000"
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
             "https://drive.google.com/thumbnail?id=1ShhvcuHHUnXlSzGB0Ed6uKf9vTgtUhww&sz=w1000",
             "https://drive.google.com/thumbnail?id=1rPhB3iS5WpRtfbjUdIBS_n33kzOLDpnL&sz=w1000",
             "https://drive.google.com/thumbnail?id=1diXXvJvfKo7LO9IkOJNXbHc93dB1xeZH&sz=w1000",
             "https://www.python.org/static/community_logos/python-logo.png",
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
             "https://drive.google.com/thumbnail?id=1VSY3J1BauGVtB2OUhaH7Og6QJizCKr_S&sz=w1000",
             "https://www.python.org/static/community_logos/python-logo.png",
            "https://drive.google.com/thumbnail?id=1oa-s120H8YRHGpdwh5oCsOHDx7q__WHq&sz=w1000",
            "https://drive.google.com/thumbnail?id=1DYLtGN2YqhZCIaRnMnRXIrigM9lxlnZ9&sz=w1000",
            "https://drive.google.com/thumbnail?id=1Pcqi8Jo5mVdn0HVbGr0ndJkthLpbPukZ&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ZYE9V99EjiePEgO1xIOFcrbL2OKJLcZn&sz=w1000",
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
                "nim": "091",
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
            "https://drive.google.com/thumbnail?id=1U974gXXj5yaAK6o8Sdmskiu7p5wkzOIo&sz=w1000",
    "https://drive.google.com/thumbnail?id=1NuYTfuRzpx3WfK9g7mJn6jiIPgMPTnlJ&sz=w1000",
    "https://drive.google.com/thumbnail?id=1DApZ7GaTx07XDpl23sftJnRlI4ZM-EDv&sz=w1000",
    "https://drive.google.com/thumbnail?id=1JAEO9qZGrqmNWxXXB1sqK6eSxsznfpSy&sz=w1000",
    "https://drive.google.com/thumbnail?id=1rxKYOWH-yAgTZJD8bphtn4r8DHaCrzY-&sz=w1000",
    "https://drive.google.com/thumbnail?id=1hmtih3faPE8vk2MwHFhYV_4r-G-zfX9f&sz=w1000",
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
                "nim": "112",
                "umur": "19",
                "asal": "Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "Xifasky",
                "divisi": "Media dan Konten Spesialis",
                "jabatan": "Anggota",
                "kesan": "Cantik dan ramah sekalii",
                "pesan": "Semangattt kaa untuk kuliah dan organisasinyaa!!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()
