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

def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def display_images_with_data(gambar_urls, data_list):
    if len(gambar_urls) == 0:
        st.info("Belum ada data untuk bagian ini.")
        return

    images = []
    datas = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)
                datas.append(data_list[i] if i < len(data_list) else {})

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
                    data = datas[index]

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
            "https://drive.google.com/uc?export=view&id=13uICtUwL-aM5enplnlX_2VZvaHsMJHJ_",
            "https://drive.google.com/uc?export=view&id=1BbQf-5BpzeyuR_RC11WX8mwsnTEFJCGX",
            "https://drive.google.com/uc?export=view&id=15m6l0IV3GJH_NfWYddZmvraS11NHREfI",
            "https://drive.google.com/uc?export=view&id=1ind3WsbXYA0mzV8_G8r86Uq4_tSprZ5Z",
            "https://drive.google.com/uc?export=view&id=1GeDJfc3l7GoK5WkkjVeJOgCYoqDc2AJ4",
            "https://drive.google.com/uc?export=view&id=1uPHwP9WUjPnNm2X8FjUoQOAA9knd6l_y",
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
                "kesan": "Selalu Farming Aura, keren pokoknya dah",
                "pesan": "Redupkan dikit bang terlalu menyala !!!",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya santay, dan suaranya mirip babank tamvan",
                "pesan": "no matter what happen, just try to survive",
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya bsia di ajak bercanda",
                "pesan": "jangan lupakan style macan kemayoran !!!",
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abang ini enjoy dan kalem banget = tenang",
                "pesan": "Tetaplah tenang tetapi bergerak dari kegelapan !!!",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya suka pose pak jokowi (saya akan lawan)",
                "pesan": "Jadilah WNI ang baik !!!",
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Imoet dan gak suka terlalu putih",
                "pesan": "Putih Putih imoed !!!",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

elif menu == "Badan Legislatif":
    def Baleg():
        st.markdown("<h3 style='text-align: center;'>Badan Legislatif</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Ketua Badan Legislatif", "Sekretaris", "Komisi I Legislasi", "Komisi II Pengawasan", "Komisi III Aspirasi dan Media Informasi"])

        with tab1:
            gambar_urls_kabaleg = [
                "https://drive.google.com/uc?export=view&id=1mPKvjtuPReWM3NyJ74q18TPOhZ1E2gAY",
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
                    "kesan": "Seronoknyo maen lage-lage",
                    "pesan": "Semangat bang TA nya Abang, semoga dilancarkan rezeki halalnya dan lulus tepat waktu ya bangg.",
                },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            gambar_urls_sekretaris = [
                "https://drive.google.com/uc?export=view&id=1kz0VzpUYdwT2HUizZXM3rxmZaJR3MkQB",
            ]
            data_list_sekretaris = [
                {
                    "nama": "Juesi Apridelia Saragih",
                    "nim": "123450085",
                    "umur": "19",
                    "asal": "Singkawang",
                    "alamat": "Pelangi",
                    "hobbi": "Dengerin lagu semusim dari marsel",
                    "sosmed": "@j__eesie",
                    "kesan": "Menggemaskan kaya kucing",
                    "pesan": "Semangatt terus kak kuliah dan pertahankan gemasnya",
                },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            gambar_urls_komisi1 = [
                "https://drive.google.com/uc?export=view&id=149zm-CpBFt9e_OmC7xZgHoSs_0I98kQx",
                "https://drive.google.com/uc?export=view&id=1HHQC3Anq4kldQYJ0xOn4l34ROJQbyI8H",
                "https://drive.google.com/uc?export=view&id=1FJTKIvBq1v-kzxkNGGiPGM948jkB2srn",
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
                    "kesan": "Aura kepintaran dan publik speakingmya sangat kuat",
                    "pesan": "Tutorkan cara pintar untuk anak ayam seperti saya bang",
                },
                {
                    "nama": "Gh. Mikael Niko Antoni Setiadi",
                    "nim": "124450025",
                    "umur": "20",
                    "asal": "Jabung",
                    "alamat": "Jati Agung",
                    "hobbi": "COD Musang",
                    "sosmed": "@me._kael",
                    "kesan": "Jokes-jokesnya sanagat fresh",
                    "pesan": "terus update jokesnya bang",
                },
                {
                    "nama": "Siti Sarifah Sumamah",
                    "nim": "124450015",
                    "umur": "19",
                    "asal": "Bekasi",
                    "alamat": "Kedaton",
                    "hobbi": "Mancing",
                    "sosmed": "@syt.rifa",
                    "kesan": "Cantik dan manis kakanya",
                    "pesan": "Hayyuk berkembang bersama Datavora !",
                },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1595YDSqXuJ_KVJFTGuHG4NgayssDbpf2",
                "https://drive.google.com/uc?export=view&id=1_1I26DxT0-9-BYgUbbVZxjIrNXJLlgfT",
                "https://drive.google.com/uc?export=view&id=1oiGeGpwkjB2wATAfqhyS-R417Y6_6mYN",
                "https://drive.google.com/uc?export=view&id=1VjxqSTdq2G3_x7b_5owRYt4cxdAp_QR5",
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
                    "kesan": "Jokesnya masuk dan lucu",
                    "pesan": "Semoga dimudahkan TA nya ya banggg, Aamiin!",
                },
                {
                    "nama": "Afghanis Nursholehatunnisa",
                    "nim": "124450042",
                    "umur": "19",
                    "asal": "Kepulauan Mentawai",
                    "alamat": "Owen Kost",
                    "hobbi": "Ngoding",
                    "sosmed": "@afghanisnt_",
                    "kesan": "Tak disangka berasal dari Mentawai",
                    "pesan": "Teman angkt 25 ada yang dari mentawai juga kak!!",
                },
                {
                    "nama": "Hani Qurrota Aini",
                    "nim": "124450020",
                    "umur": "20",
                    "asal": "CTR",
                    "alamat": "Sukarame",
                    "hobbi": "Baca AU",
                    "sosmed": "@haniquratuain_",
                    "kesan": "Cantiknya kelewatan",
                    "pesan": "Gak bisa berkata-kata lagi",
                },
                {
                    "nama": "Jeremia Halim",
                    "nim": "124450101",
                    "umur": "20",
                    "asal": "Tanggerang",
                    "alamat": "Teluk",
                    "hobbi": "Nyanyi, olahraga",
                    "sosmed": "@jeremia_hm",
                    "kesan": "Wujud aseli Sigma",
                    "pesan": "Kok bisa sesigma itu bang!",
                },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=1qPafJsfrNA8A3lrYPm26yy6yga4Plj41",
                "https://drive.google.com/uc?export=view&id=1f-QGnkcaTXgJXHGB4axk9ZlWU3UuvYpt",
                "https://drive.google.com/uc?export=view&id=1ela06RiCy4pwPloedYA-qgt3Gh66t5Hg",
                "https://drive.google.com/uc?export=view&id=1yXUpB4i-lCLZHYr_WuQsyemTtjDBjl95",
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
                    "kesan": "Lucu, gemas, dan disiplin",
                    "pesan": "Tutorkan kepada saya bagaimana caranya disiplin!",
                },
                {
                    "nama": "Jona Timothy Ogatse Panjaitan",
                    "nim": "124450111",
                    "umur": "20",
                    "asal": "Depok",
                    "alamat": "Pemda Raya",
                    "hobbi": "Gym sama Koleksi figure, nafas manual",
                    "sosmed": "@nagatseee",
                    "kesan": "Asiknya beneran asik dan di ajak ngomong apa aja masuk",
                    "pesan": "Semangat abang kuliahnya dan teruslah berkembang",
                },
                {
                    "nama": "Sekar Dini Widya Putri",
                    "nim": "124450082",
                    "umur": "20",
                    "asal": "Metro",
                    "alamat": "Pemda",
                    "hobbi": "Jajan sama nisa, putri, suci",
                    "sosmed": "@sekardnwp",
                    "kesan": "Keliatannya tegas dan galak, tapi sebenernya perhatian banget",
                    "pesan": "jadilah bagian dirimu dengan versi terbaik kak!",
                },
                {
                    "nama": "Wan Nashwa Alhasni Yuska",
                    "nim": "123450077",
                    "umur": "20",
                    "asal": "Pasay",
                    "alamat": "Belwis",
                    "hobbi": "Nyapa angin",
                    "sosmed": "@nshaysk",
                    "kesan": "sangat lemah lembut",
                    "pesan": "tetaplah berkembang kakak!",
                },
            ]
            display_images_with_data(gambar_urls_komisi3, data_list_komisi3)

    Baleg()

elif menu == "Badan Kesenatoran":
    def Bason():
        st.markdown("<h3 style='text-align: center;'>Badan Kesenatoran</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Senator", "Biro Aspirasi dan Media Komunikasi", "Biro Kajian Strategis dan Propaganda", "Biro Kesekretariatan"])

        with tab1:
            gambar_urls_senator = [
                "https://drive.google.com/uc?export=view&id=1HZUoRpaiSRpZPuGv-waY0aS9C4j3xjqF",
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
                    "kesan": "Aura bijaksananya kuat banget",
                    "pesan": "Semoga sukses kak!",
                },
            ]
            display_images_with_data(gambar_urls_senator, data_list_senator)

        with tab2:
            gambar_urls_biro_aspirasi = [
                "https://drive.google.com/uc?export=view&id=1k2_DcBtU9h1FKm8RoB0KDbtdxN7K2AlK",
                "https://drive.google.com/uc?export=view&id=1Y4hgLEo6WDpQVaPCVeQwDB9-Cre8LUJz",
                "https://drive.google.com/uc?export=view&id=1Ro-dM162HJsf8W7JqZmn0yV8UAINvRHg",
                "https://drive.google.com/uc?export=view&id=1k0xsgWXOTMGHe24wfhPMiqJretLJzbME",
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
                    "pesan": "Semangat terus kuliahnya kak!",
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
                    "pesan": "Semanagat terus bang kuliahnya!",
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
                    "pesan": "Semangat terus kak kuliahnya!",
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
                    "pesan": "Semangat terus bang kuliahnya!",
                },
            ]
            display_images_with_data(gambar_urls_biro_aspirasi, data_list_biro_aspirasi)

        with tab3:
            gambar_urls_biro_kajian = [
                "https://drive.google.com/uc?export=view&id=19nWLBZus_xxByEIz7azuKKpwWEFVSZ8p",
                "https://drive.google.com/uc?export=view&id=1BUtMtwPikI8_od5GoZGp1cUsIUQ7FXLI",
                "https://drive.google.com/uc?export=view&id=1ZQM7PMvTGDhKDPljddVbTg-OWKJU1bFW",
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
                    "pesan": "Semangat kak TA nyaa, semoga dimudahkan jalannya yaa!!",
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
                    "pesan": "Semangat terus kuliahnya kaa!",
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
                    "pesan": "Semangat terus bang kuliah dan organisasinya!",
                },
            ]
            display_images_with_data(gambar_urls_biro_kajian, data_list_biro_kajian)

        with tab4:
            gambar_urls_biro_kesekretariatan = [
                "https://drive.google.com/uc?export=view&id=15c0sdS85UPfmXdCOI6j9gsXk_IJYnd7m",
                "https://drive.google.com/uc?export=view&id=1u0Hlacgo1bqFEo8qVrpBDUemm2j7t4EV",
            ]
            data_list_biro_kesekretariatan = [
                {
                    "nama": "Nadya Ratu Anjani",
                    "nim": "123450083",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Sukarame",
                    "hobbi": "Denger Lagu",
                    "sosmed": "@nadyaanjaani",
                    "kesan": "Welcome sekali kakanyaaa, dan cara penyampaian materinya juga mudah dipahami",
                    "pesan": "Semangat terus kuliahnya kaa!!",
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
                    "pesan": "Semangat terus kaa kuliahnyaa!!",
                },
            ]
            display_images_with_data(gambar_urls_biro_kesekretariatan, data_list_biro_kesekretariatan)

    Bason()

elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])

        with tab1:
            gambar_urls_Kadep_psda = [
                "https://drive.google.com/uc?export=view&id=1wFHj7FPrWFV_uSDKh92bZ3ARIO6IJsoM",
            ]
            data_list_Kadep_psda = [
                {
                    "nama": "Arienta Khusnul Ananda",
                    "nim": "123450097",
                    "umur": "21",
                    "asal": "Deket Pantai Kedu, Kalianda",
                    "alamat": "Samping kos capo",
                    "hobbi": "Baca jurnal",
                    "sosmed": "@arientakhsnl_",
                    "kesan": "Agak keliatan galak, tapi ternyata baik dan sedikit jutek",
                    "pesan": "Semoga lebih banyak senyumnya kak!!!",
                },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)

        with tab2:
            gambar_urls_sekdep_psda = [
                "https://drive.google.com/uc?export=view&id=1bosgI-pEUcMxvpB2a6tJ411cdmk1tyiv",
            ]
            data_list_sekdep_psda = [
                {
                    "nama": "Vany Salsabila Putri",
                    "nim": "123450022",
                    "umur": "20",
                    "asal": "Palembang",
                    "alamat": "Pudan Kost",
                    "hobbi": "Nyanyi dan masak ayam",
                    "sosmed": "@vany.salsabilaa",
                    "kesan": "Kak Vany baik, berwibawa, dan disiplin banget",
                    "pesan": "Semoga selalu diberi kemudahan ya kakak!!!",
                },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)

        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
                "https://drive.google.com/uc?export=view&id=1VhqkKO_VxO4iq5dKwCiY9qTc72G6uolf",
                "https://drive.google.com/uc?export=view&id=1IpViB77sfB_WTv53FURha6Uh5e0Ncuy2",
                "https://drive.google.com/uc?export=view&id=1czIs5dT8LhGdqhlD_Bc5UEAFgoDS5b5X",
                "https://drive.google.com/uc?export=view&id=1EkHgWjUhwD5tlbIK2lFzvpcssmS1v5o2",
                "https://drive.google.com/uc?export=view&id=1rh1SWa8JizZP_RgHEenEzuCsmudCxpA-",
                "https://drive.google.com/uc?export=view&id=1jzEZ32B9-2FtNAzJMXpTvmu8mzwJK5d-",
                "https://drive.google.com/uc?export=view&id=1Ksjp63YFrf8aOiFkG7jlGKr-O2gZ6bLs",
                "https://drive.google.com/uc?export=view&id=1Ucbg_4zUz8NCNm1qZ6MlPBjCCL3K4ODf",
            ]
            data_list_Divisi_Kaderisasi = [
                {
                    "nama": "Nobel Nizam Fathirizki",
                    "nim": "123450117",
                    "umur": "21",
                    "asal": "Bandar Lampung",
                    "alamat": "Urip",
                    "hobbi": "Banyak",
                    "sosmed": "@nobelnizam",
                    "kesan": "Bang Nobel Berwibawa, Asik dan jago banget sulap, baik, tegas, dan keren banget",
                    "pesan": "Semogaa sukses dan berkah selalu ya bang!!!",
                },
                {
                    "nama": "Afriza Azmi",
                    "nim": "124450110",
                    "umur": "20",
                    "asal": "Malang",
                    "alamat": "Lapangan",
                    "hobbi": "Teriak",
                    "sosmed": "@friezazmi",
                    "kesan": "Bang Azmi keren, gentle, tegas, dan energik bangetttt",
                    "pesan": "Semoga selalu diberikan kesehatan dan kekuatan ya bang!!!",
                },
                {
                    "nama": "Ayake Alfatih Ramadhan",
                    "nim": "124450081",
                    "umur": "21",
                    "asal": "paninjauan 10 kota di atas solok sumatera barat",
                    "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                    "hobbi": "Memasak",
                    "sosmed": "@_ykeal",
                    "kesan": "Bang Ayake humoris, asik, humble dan baik bangetttt",
                    "pesan": "Semoga selalu sehatt, bahagia, dan lancar rezekinya ya bang!!!",
                },
                {
                    "nama": "Caesar Ozora Alrando",
                    "nim": "124450017",
                    "umur": "21",
                    "asal": "Painar, Sumatera Barat",
                    "alamat": "Gedung F",
                    "hobbi": "Mandiin anak ayam",
                    "sosmed": "@caesar.oriza",
                    "kesan": "Bang Caesar Baik, keren dan imut, serta suka berbagi ilmu",
                    "pesan": "Semoga selalu diberikan kelancaran ya bang!!!",
                },
                {
                    "nama": "Euodia Meiliana Friedita",
                    "nim": "124450029",
                    "umur": "18",
                    "asal": "Rahim ibu",
                    "alamat": "sebrang kost yazid rizal",
                    "hobbi": "ngapain aja deh",
                    "sosmed": "@yudiameilianaa_",
                    "kesan": "Kak Yudia ramah, tegas, keren, baik dan humble bangetttt",
                    "pesan": "Semoga selalu semangat dan bahagia ya kak!!!",
                },
                {
                    "nama": "Haikal Saventio Tamba",
                    "nim": "124450014",
                    "umur": "20",
                    "asal": "Sibolga",
                    "alamat": "Di depan kostan bang ayake belok kanan",
                    "hobbi": "Mencari pakan anak ayam",
                    "sosmed": "@_haikaaall",
                    "kesan": "Bang Haikal baik, tegas, asik, jago futsal, dan humble bangetttt",
                    "pesan": "Semoga selalu sehat dan terhindar dari segala penyakit ya bang!!!",
                },
                {
                    "nama": "Putri Manna Anantama Simbolon",
                    "nim": "124450056",
                    "umur": "18",
                    "asal": "Depok",
                    "alamat": "Oiya Cafe",
                    "hobbi": "jalan kaki ga boleh naik gojek",
                    "sosmed": "@putrimannaa",
                    "kesan": "Kak Putri baik, lucu, imut, dan humble bangetttt",
                    "pesan": "Semoga selalu diberikan keselamatan dan kebahagiaan ya kak!!!",
                },
                {
                    "nama": "Queenta Thifaal Nabila",
                    "nim": "124450059",
                    "umur": "21",
                    "asal": "Cikajang",
                    "alamat": "Tempat pemancingan",
                    "hobbi": "Baking",
                    "sosmed": "@queentanaabila",
                    "kesan": "Kak Queenta baik, ber aura, dan humble bangetttt",
                    "pesan": "Semoga selalu sehat, bahagia dan diberi keselamatan ya kak!!!",
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)

        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
                "https://drive.google.com/uc?export=view&id=19I1hpPyYplb4hpaYqGJ0JPmd-0xER0ug",
                "https://drive.google.com/uc?export=view&id=14hh_DaP8qn5U4UpFmBDIlf-79XZbuA8T",
                "https://drive.google.com/uc?export=view&id=1GDkM65zdKUkQtmO3Scws3oVR4MKuSoe5",
                "https://drive.google.com/uc?export=view&id=1xlqk7AYzc4hrynb2OOCSpYLGA9lM0IQ2",
                "https://drive.google.com/uc?export=view&id=1VU92JdMOmRmjXNNwmZB54UIxIgSZmeoj",
                "https://drive.google.com/uc?export=view&id=1uEbBzElrvNkB4AEfajAb6IPIijmajpCv",
                "https://drive.google.com/uc?export=view&id=1LIAOGsgyMPXSfMDNffyt93fymsgdhLBv",
            ]
            data_list_Divisi_Peningkatan_Mutu_Anggota = [
                {
                    "nama": "Desman Velius Halawa",
                    "nim": "123450113",
                    "umur": "25",
                    "asal": "Nias",
                    "alamat": "Airan",
                    "hobbi": "Main musik",
                    "sosmed": "@dsmanhal",
                    "kesan": "Bang Desman baik, asik, humble, dan jago bangetttt deffense futsalnya",
                    "pesan": "Semoga selalu semangat dan sukses ya bang!!!",
                },
                {
                    "nama": "Azzelya Thianandry",
                    "nim": "124450041",
                    "umur": "19",
                    "asal": "Bandar Lampung",
                    "alamat": "Sukarame",
                    "hobbi": "Pilates",
                    "sosmed": "@azzelytn",
                    "kesan": "Kak Azzel baik, kalem, dan humble bangetttt",
                    "pesan": "Semoga bahagia dimanapun kakak berada ya kak!!!",
                },
                {
                    "nama": "Charrlindah",
                    "nim": "124450037",
                    "umur": "21",
                    "asal": "Jakarta Pusat",
                    "alamat": "Cendrawasih 1",
                    "hobbi": "Ngurus Peternakan",
                    "sosmed": "@charrlln",
                    "kesan": "Kak Charrlindah baik, santai, dan humble bangetttt",
                    "pesan": "Semoga selalu sehat dan bahagia ya kak!!!",
                },
                {
                    "nama": "Jeremi Marolop P. Situmorang",
                    "nim": "124450111",
                    "umur": "17",
                    "asal": "Jayapura",
                    "alamat": "RS Airan",
                    "hobbi": "Nonton a day in my life",
                    "sosmed": "@jemarrro",
                    "kesan": "Bang Jere humble, asik, kece, dan baik bangetttt",
                    "pesan": "Semoga selalu kuat dan sehat ya bang!!!",
                },
                {
                    "nama": "Nabila Nur Azizah",
                    "nim": "124450048",
                    "umur": "18",
                    "asal": "Lampung",
                    "alamat": "Barokah",
                    "hobbi": "Main roblox",
                    "sosmed": "@n.bila_a",
                    "kesan": "Kak Nabila baik, santai, dan humble bangetttt",
                    "pesan": "Semoga selalu dilancarkan urusannya ya kak!!!",
                },
                {
                    "nama": "Rafli Al Mansyah Tambunan",
                    "nim": "124450007",
                    "umur": "18",
                    "asal": "Sibolga",
                    "alamat": "Belwis",
                    "hobbi": "Membaca peraturan rektor",
                    "sosmed": "@dearfkvmfl",
                    "kesan": "Bang Rafli kece, rambutnya keren terus, dan humble bangetttt",
                    "pesan": "Semoga selalu sehat dan doa nya diwujudkan ya bang!!!",
                },
                {
                    "nama": "Salavi Naharani",
                    "nim": "124450090",
                    "umur": "20",
                    "asal": "Lampung Timur",
                    "alamat": "jatimulyo",
                    "hobbi": "Minum air putih",
                    "sosmed": "@afi.nhr",
                    "kesan": "Kak Salafi baik, lucu, kalem dan humble bangetttt",
                    "pesan": "Semoga selalu sehat dan dilancarkan urusannya ya kak!!!",
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Peningkatan_Mutu_Anggota, data_list_Divisi_Peningkatan_Mutu_Anggota)

    PSDA()

elif menu == "Departemen MIKFES":
    def mikfes():
        st.markdown("<h3 style='text-align: center;'>Departemen Akademik dan Keprofesian</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Professional Skill and Development", "Divisi Pusat Inovasi dan Kajian Akademik", "Divisi Research & Development"])

        with tab1:
            gambar_urls_kepala_departemen_mikfes = [
                "https://drive.google.com/uc?export=view&id=10QX-AY9lgdHj5ZiCA3oKKM5W5hA1UPuP",
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
                    "kesan": "Sosok aseli multitalent",
                    "pesan": "Semangatt TA nya nanti banggg, dan teruslah ada koneksi dengan kami Datavora!!!",
                },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)

        with tab2:
            gambar_urls_sekretaris_mikfes = [
                "https://drive.google.com/uc?export=view&id=1cmM6YCUnTBkDLvjvm7DRE4ivpZMOotxc",
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
                    "kesan": "First impression ku ke kaka, kaka ceria bangettt beneran gemasss",
                    "pesan": "Semangatt TA nya kaa, semoga diberikan kelancaran dalam mengerjakan TA, jangan lupa jaga kesehatan!",
                },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)

        with tab3:
            gambar_urls_Divisi_Professional_Skill_and_Development = [
                "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
                "https://drive.google.com/uc?export=view&id=1d7x3iWqX7ZQe7K32DPI-JoDHySdFjBPJ",
                "https://drive.google.com/uc?export=view&id=1TPrWtMFQE4zQt7fCnyNalyfe4mHF80Ru",
                "https://drive.google.com/uc?export=view&id=1V7S4glSEWefpnxZJeh1JMoaN77VQZfwU",
                "https://drive.google.com/uc?export=view&id=1fKAh9825jZWtccAY8f40Sb0olhAWMyWf",
                "https://drive.google.com/uc?export=view&id=1FT0q-4-ntjOefUjS5_SbqtcVXstuAY0b",
            ]
            data_list_Divisi_Professional_Skill_and_Development = [
                {
                    "nama": "Fadil Prasetyo Alfarizzi",
                    "nim": "123450...",
                    "umur": "...",
                    "asal": "...",
                    "alamat": "...",
                    "hobbi": "...",
                    "sosmed": "...",
                    "kesan": "Inspiratif bangett",
                    "pesan": "Masih ga nyangka secepat itu abang kembali ke pangkuan-Nya, tapi sekarang abang udah ga sakit lagi ya.. Doa terbaik untuk mu bang Fadil, fly high and rest in peace a good soul",
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
                    "pesan": "Abang keren bangett, dilanjutkan ya bangg. Jangan lupa jaga pola tidur dan makan nya!",
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
                    "pesan": "Kaka semangat kuliahnya yaa, jaga pola makan dan pola tidurnyaa, jangan sampe drop yaa!!",
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
                    "pesan": "kakaa kerennn, semoga kaka selalu menemukan kebaikan di setiap hal hal kecil yaa! jaga kesehatan kaa!",
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
                    "pesan": "Semoga apapun plan kaka bisa tercapai satu persatu ya kaa, semangat kuliahnya dan jaga kesehatan!",
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
                    "pesan": "...",
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)

        with tab4:
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
                "https://drive.google.com/uc?export=view&id=1-gCTxwfUX7OYn5CtMqKbTMhRUHsKod9k",
                "https://drive.google.com/uc?export=view&id=1IAOq6mIFkOuz049C5lLMUyVqMQmb5Qub",
                "https://drive.google.com/uc?export=view&id=1BjcSdh0SEtUCRNeZ51w6W5mvTZMwXtsK",
                "https://drive.google.com/uc?export=view&id=1Wp_N4sxGr0WlM3EEoXw9D84UghDEyMpD",
                "https://drive.google.com/uc?export=view&id=13HYgLXa3XbCcemDyRrCm_XVHLTdhZkvc",
                "https://drive.google.com/uc?export=view&id=1Zws-R6iD4VVCqvGv5wHuC3Yb92Jqpy3j",
                "https://drive.google.com/uc?export=view&id=1Tn_V239Okn33aQccsbUTpvjcYPfGC6qh",
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
                    "pesan": "Semangat nanti TA nya bangg, semoga dipermudah jalan dan urusannyaa!",
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
                    "pesan": "Kaa walau perkuliahan semakin bertambah sem semakin terasa ngebantainya, tapi tetap semangatt ya kaa, jangan lupa jaga pola makan dan pola tidurnyaa jangan sampe drop-!",
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
                    "pesan": "Go semangat goo!! kaa semoga kakak selalu diberikan kemudahan di setiap langkah kakak yaa",
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
                    "pesan": "...",
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
                    "pesan": "Semangatt terus ya bang kuliahnyaa, jangan lupa jaga kesehatan jugaaa!!",
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
                    "pesan": "Semoga dunia selalu berbaik hati dengan kakak yaa, semangattt kuliahnyaa kaa!!",
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
                    "pesan": "Semangattt bang nanti TA nyaa, semoga dipermudah dan diperlancar semuanyaa, aamiin",
                },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)

        with tab5:
            gambar_urls_Divisi_Research_Development = [
                "https://drive.google.com/uc?export=view&id=1Qse_jhk2fMPiNqMeTS9yTy7XurJnn3-J",
                "https://drive.google.com/uc?export=view&id=1m4xx-En925aiusfGz6SDzUEiqnEom_mb",
                "https://drive.google.com/uc?export=view&id=1STh1besxJYPLdthiMn8nrFNg7DUXXpci",
                "https://drive.google.com/uc?export=view&id=1anT3sWu4alNhK-3n4ui_oUZg1NKPKuJK",
                "https://drive.google.com/uc?export=view&id=1xCxrvw_iGbRbZoUnYAftL-HOvCciYSE2",
                "https://drive.google.com/uc?export=view&id=1ub3ATcqiCwEaxtdgybevSphrxt2f-BA_",
                "https://drive.google.com/uc?export=view&id=1YOeClC2FIoVZRWn-k4qASmxWTBJfRzx8",
            ]
            data_list_Divisi_Research_Development = [
                {
                    "nama": "Faiza Try Anjani",
                    "nim": "124450075",
                    "umur": "19",
                    "asal": "Padang",
                    "alamat": "Belwis",
                    "hobbi": "Baca",
                    "sosmed": "@faizaanjanii",
                    "kesan": "Fisrt impression ku ke kaka beneran kagum dan my role modell",
                    "pesan": "Kaka beneran keren bangetttt, dari awal kenal saya kagum sama kakaa, tips n trick cara bagi waktu belajar dan organisasi kaa #helppp",
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
                    "pesan": "Semangatttt kuliahnya banggg, jangan lupa jaga kesehatan yaa!",
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
                    "pesan": "Semangatt bang kuliahnyaa!!",
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
                    "pesan": "Masih keinget saya momen kelompok saya dibantai oleh pertanyaan dari abang, tapi JUJURRR minat banget berguru mengenai komputasi ke abangg karena ilmu abang DAGING BANGETTT",
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
                    "pesan": "Semangatt kaa kuliahnyaaa!!",
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
                    "pesan": "Pengalaman abang beneran keren-keren bangett, semoga plan abang satu per satu bisa tercapai ya bangg, aamiin!",
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
                    "pesan": "Kocak bangett dah, semoga hal hal baik selalu melingkupi hidup abang yaaa, aamiin!",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
                "kesan": "Keliatan Aura Tegasnya dan wibawanya",
                "pesan": "Sukses dan sehat selalu kak dan jangan lupakan kami jugak!!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)

        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
                "hobbi": "Main layangan waktu hujan",
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

elif menu == "Departemen Internal":
    def internal():
        st.markdown("<h3 style='text-align: center;'>Departemen Internal</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Keharmonisasian", "Divisi Kerohanian"])

        with tab1:
            gambar_urls_Kadep_internal = [
                "https://drive.google.com/uc?export=view&id=1hsRjcZqsIur3pm4-bEA8ZpDDUUBMcbY5",
            ]
            data_list_Kadep_internal = [
                {
                    "nama": "Haikal Fransisko Simbolon",
                    "nim": "123450106",
                    "umur": "20",
                    "asal": "Jambi",
                    "alamat": "Way Halim",
                    "hobbi": "Ngeledek Orang",
                    "sosmed": "@haikalsbln",
                    "kesan": "Abang ini bisa menyesuaikan dengan semua kondisi, Respect",
                    "pesan": "Semoga setiap harinya selalu menjadi lebih baik lagi bang!!!",
                },
            ]
            display_images_with_data(gambar_urls_Kadep_internal, data_list_Kadep_internal)

        with tab2:
            gambar_urls_sekdep_internal = [
                "https://drive.google.com/uc?export=view&id=1a3o2Q7YjnOkLZFOChO3jVQlZps-h7Sfu",
            ]
            data_list_sekdep_internal = [
                {
                    "nama": "Kharisma Mustika Sari",
                    "nim": "123450034",
                    "umur": "21",
                    "asal": "Way Kanan",
                    "alamat": "Untung Senopati",
                    "hobbi": "Suka nolong orang",
                    "sosmed": "@rismaa.mustika_",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
            ]
            display_images_with_data(gambar_urls_sekdep_internal, data_list_sekdep_internal)

        with tab3:
            gambar_urls_keharmonisasian = [
                "https://drive.google.com/uc?export=view&id=1I1iaJuCDBKSDebl6uV2bYJC7PFPWsp8T",
                "https://drive.google.com/uc?export=view&id=1FwUGETSQtrJgiKcRA9LSNOfM6p1RGy6K",
                "https://drive.google.com/uc?export=view&id=1DVVJ5LpxwtVf6N3bnsgTbbqRCythNF1y",
                "https://drive.google.com/uc?export=view&id=1K3jIPU6dDVefn1jFU9SiOlRdDNqVlt8G",
                "https://drive.google.com/uc?export=view&id=1Q9aNH8QdvD2QX1OgKeneEDALZsonR6Ph",
                "https://drive.google.com/uc?export=view&id=15H9gL0G-0vJlxyAPop9chm1GSYlc4FX8",
            ]
            data_list_keharmonisasian = [
                {
                    "nama": "Hanna Grecia Sinaga",
                    "nim": "123450038",
                    "umur": "21",
                    "asal": "Sumatra Utara, Kisaran City",
                    "alamat": "Sukarame",
                    "hobbi": "Ngabarin orang tua",
                    "sosmed": "@hanna_g_sinaga",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
                {
                    "nama": "A Farhan Ghani",
                    "nim": "123450121",
                    "umur": "21",
                    "asal": "Kemiling",
                    "alamat": "Kemiling",
                    "hobbi": "Balap Liar",
                    "sosmed": "@farhanghani",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
                {
                    "nama": "Aisyah Khairun Nisa",
                    "nim": "124450096",
                    "umur": "18",
                    "asal": "Riau",
                    "alamat": "Belwis",
                    "hobbi": "Ngeliatin orang",
                    "sosmed": "@aisyahkhair._",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
                {
                    "nama": "Cerine Sihotang",
                    "nim": "124450049",
                    "umur": "19",
                    "asal": "Medan",
                    "alamat": "Belwis",
                    "hobbi": "Balap liar",
                    "sosmed": "@cerine_ipynb",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
                {
                    "nama": "Jaya Saputra Tamba",
                    "nim": "124450094",
                    "umur": "19",
                    "asal": "Medan",
                    "alamat": "Pemda",
                    "hobbi": "Berkebun dan membuat lagu",
                    "sosmed": "@jay.saputratmb",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
                {
                    "nama": "Najla Nur Syifa",
                    "nim": "124450051",
                    "umur": "20",
                    "asal": "Aceh",
                    "alamat": "Belwis",
                    "hobbi": "Gangguin cika",
                    "sosmed": "@njlanursyifa",
                    "kesan": "Kakak ini asik saya suka belajar dengan dia",
                    "pesan": "semangat terus kuliahnya kakak !!!",
                },
            ]
            display_images_with_data(gambar_urls_keharmonisasian, data_list_keharmonisasian)

        with tab4:
            gambar_urls_kerohanian = [
                "https://drive.google.com/uc?export=view&id=1zcw2jslxpLdolTEt4ls57rh0DW5zxJYH",
                "https://drive.google.com/uc?export=view&id=1BkC3Tr4baD30JdEuIYJSq4rLjOiwt_Km",
                "https://drive.google.com/uc?export=view&id=1D7tZ-p8QlpKHhhfymcArDBetqBcAxMjP",
                "https://drive.google.com/uc?export=view&id=1e1pkIImHb9qH2qZItUA0CoGl2VW1PCPe",
                "https://drive.google.com/uc?export=view&id=1NQFo19cVNrV6vtsB9G_zgG1CWI2ez9v-",
                "https://drive.google.com/uc?export=view&id=1PDnxcYOvhzW0fylCjOJpGyAtIv_Bl7Fx",
                "https://drive.google.com/uc?export=view&id=1xM2-W6u1Zuci3fIk8rmHKQA0tfVr0xt1",
                "https://drive.google.com/uc?export=view&id=143aQZRx0DRXDGiMa3YqM1bLaxCm8MFBF",
            ]
            data_list_kerohanian = [
                {
                    "nama": "Rozak Ramdani",
                    "nim": "124450100",
                    "umur": "18",
                    "asal": "Lampung Selatan",
                    "alamat": "Korpri Raya",
                    "hobbi": "Isengin harvin di kelas",
                    "sosmed": "@rozaqramdani__",
                    "kesan": "Orangnya asik dan ramah",
                    "pesan": "Semangat terus kuliahnya!",
                },
                {
                    "nama": "Teresa Christiani Purba",
                    "nim": "124450046",
                    "umur": "19",
                    "asal": "Riau",
                    "alamat": "Belwis",
                    "hobbi": "Masak",
                    "sosmed": "@christiani8872",
                    "kesan": "Kakak ini sangat baik dan menyenangkan diajak diskusi",
                    "pesan": "Semoga lancar dan sukses terus perkuliahan serta kegiatannya!",
                },
                {
                    "nama": "Muhammad Hanif Dzaky Arifin",
                    "nim": "124450064",
                    "umur": "21",
                    "asal": "Padang Sumbar",
                    "alamat": "Perumnas Way Kandis",
                    "hobbi": "Ngedistro",
                    "sosmed": "@hnfdzky_",
                    "kesan": "Orangnya sangat seru dan gampang berbaur",
                    "pesan": "Sukses terus untuk kuliah dan impian-impiannya!",
                },
                {
                    "nama": "Audina Fitria",
                    "nim": "124450038",
                    "umur": "20",
                    "asal": "Sumatera Barat",
                    "alamat": "Sukarame",
                    "hobbi": "Main ke air terjun",
                    "sosmed": "@audinaf_03",
                    "kesan": "Sangat ramah dan selalu membawa suasana positif",
                    "pesan": "Tetap semangat dan sukses selalu kuliahnya!",
                },
                {
                    "nama": "Cika Adelia Br Marbun",
                    "nim": "124450107",
                    "umur": "20",
                    "asal": "Riau",
                    "alamat": "Belwis",
                    "hobbi": "Terlambat",
                    "sosmed": "@cikamrbn",
                    "kesan": "Orangnya asik dan suka bikin suasana jadi ceria",
                    "pesan": "Semangat terus perkuliahannya dan makin sukses!",
                },
                {
                    "nama": "Gustin Haleluya Tampubolon",
                    "nim": "124450068",
                    "umur": "21",
                    "asal": "Toba Sumatera Utara",
                    "alamat": "Airan",
                    "hobbi": "Nonton",
                    "sosmed": "@gustinhaleluya",
                    "kesan": "Orangnya santai dan enak diajak berteman",
                    "pesan": "Sukses terus untuk akademik dan aktivitas lainnya!",
                },
                {
                    "nama": "Muhammad Arvinsyah",
                    "nim": "124450128",
                    "umur": "20",
                    "asal": "Sumatera Selatan",
                    "alamat": "Belwis",
                    "hobbi": "Nembak Burung",
                    "sosmed": "@muhvinz_",
                    "kesan": "Sangat seru dan selalu meramaikan suasana",
                    "pesan": "Semangat terus kuliahnya dan sukses selalu!",
                },
                {
                    "nama": "Rafa Sabina Fahimah",
                    "nim": "124450036",
                    "umur": "20",
                    "asal": "Natar",
                    "alamat": "Natar",
                    "hobbi": "Cari duit",
                    "sosmed": "@snasaa._",
                    "kesan": "Kakak yang rajin dan sangat menginspirasi",
                    "pesan": "Semangat terus nyari cuan dan kuliahnya!",
                },
            ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)

    internal()

elif menu == "Departemen SSD":
    def ssd():
        st.markdown("<h3 style='text-align: center;'>Departemen Storage Sains Data</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kemitraan", "Divisi Kewirausahaan"])

        with tab1:
            gambar_urls_Kadep_ssd = [
                "https://drive.google.com/uc?export=view&id=1CmMENsIg2aupLCIfzJu3npUhP0ENkEwd",
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
                    "kesan": "Abangnya lucu dan bisa di ajak bercanda",
                    "pesan": "Teruslah menghibur bang!",
                },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)

        with tab2:
            gambar_urls_sekdep_ssd = [
                "https://drive.google.com/uc?export=view&id=1vl3HPdMa95JJZHNe743s8cTG33Tk7yCE",
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
                "https://drive.google.com/uc?export=view&id=1be33eaRBWzmojsURmFQLlCd782utxra0",
                "https://drive.google.com/uc?export=view&id=1xj0uLa9NrXJxt4VT-FDlS_jKRt3ZR7vW",
                "https://drive.google.com/uc?export=view&id=1KiBtY1Qnlwxbo_N8xdlP7qA356gomBqU",
                "https://drive.google.com/uc?export=view&id=1vlH6265l22eWWAx_py4bhIMxCyluxC2w",
                "https://drive.google.com/uc?export=view&id=1dTSuQ7nyyk2N6IkhZHdojHjtwy_ppvts",
                "https://drive.google.com/uc?export=view&id=1pHz0GOkrkwu7ToUmOe-m35_LnPfSdxEv",
                "https://drive.google.com/uc?export=view&id=1f6e-hSP7qihaAa0hNClHXTkmvCKnXc-O",
                "https://drive.google.com/uc?export=view&id=106_UyztpX07GKIzRpIPuS9D2V_-1cNP4",
                "https://drive.google.com/uc?export=view&id=1Z5zo3p77LVgH1Lu3Piwtv_eavqpt96-_",
                "https://drive.google.com/uc?export=view&id=1A3lHzORWtxs3a67qAUled6iMXZC49sgS",
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
                    "pesan": "Semangat terus kuliahnya kakak !!!",
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
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)

        with tab4:
            gambar_urls_kewirausahaan = [
            ]
            data_list_kewirausahaan = [
            ]
            display_images_with_data(gambar_urls_kewirausahaan, data_list_kewirausahaan)

    ssd()

elif menu == "Departemen Medkraf":
    def medkraf():
        st.markdown("<h3 style='text-align: center;'>Departemen Media Kreatif</h3>", unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Dokumentasi", "Divisi Media dan Konten Spesialis", "Visual Design"])

        with tab1:
            gambar_urls_Kadep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1EiyJ-maI6nedPmYMxqs8yu12x2g64mKA",
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
                "kesan": "Suka memberi masukan dan baik!!",
                "pesan": "Berikanlah eksperimen yang dapat sangat berguna untuk kami kedepannya kak"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_medkraf, data_list_Kadep_medkraf)                

        with tab2:
            gambar_urls_sekdep_medkraf = [
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
            "https://drive.google.com/uc?export=view&id=1zAZLSYzoggK2o4c4Yo4ESCZTB4dz4DiC",
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

elif menu == "Departemen Minbak":
    def Departemen_Minbak():
        st.markdown("<h3 style='text-align: center;'>Departemen Minat dan Bakat</h3>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Manajemen Aktivitas dan Kompetisi", "Manajemen Minat dan Bakat"])

        with tab1:
            gambar_urls_kepala_departemen_minbak = [
                "https://drive.google.com/uc?export=view&id=1dFkoXY5zzFe0Rfa9thtZqq6eTlv--Jzk",
            ]
            data_list_kepala_departemen_minbak = [
                {
                    "nama": "Kevin Antonio Junior",
                    "nim": "123450109",
                    "umur": "23",
                    "asal": "Sulawesi Tengah",
                    "alamat": "Panjang",
                    "hobbi": "Mancing",
                    "sosmed": "@kevinaja__",
                    "kesan": "Bisa menyesuaikan dengan semua kondisi dan pastinya baik",
                    "pesan": "Teruslah menginspirasi saya dan teman-teman anak ayam bang!!!",
                },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)

        with tab2:
            gambar_urls_sekretaris_departemen_minbak = [
                "https://drive.google.com/uc?export=view&id=1ouZCVGgXTVIRLJpaWdmm45U_359KglCr",
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
                    "kesan": "Sangat rapi dan cekatan dalam mengelola administrasi",
                    "pesan": "Sukses selalu kak!",
                },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)

        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [
                "https://drive.google.com/uc?export=view&id=1sbOP9gVntI2Fz6jqBxbfgpZTaxp1Yzh9",
                "https://drive.google.com/uc?export=view&id=16_NHdVaA2z7on2J7ohMt5CrtbgzF24cu",
                "https://drive.google.com/uc?export=view&id=1pqdHDBIo7ft2vjWzu4STc-28OWNUHFM7",
                "https://drive.google.com/uc?export=view&id=1lrCl8uaWWW_GqCtPiXAw6PsHjUvCp3pg",
                "https://drive.google.com/uc?export=view&id=1WpAmkzFVMFmCPrT2P5zkuCdMnkQo3BYS",
                "https://drive.google.com/uc?export=view&id=14ayZfsihOL7CWHbHtwEsmsFVCy7azZrR",
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
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)

        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
                "https://drive.google.com/uc?export=view&id=1TZZlYwcI8zmClsvaxgHjTC5T-6waso_D",
                "https://drive.google.com/uc?export=view&id=1bt2Ip-IeexTc9Z57Yxd6cjgUKBIP9H9k",
                "https://drive.google.com/uc?export=view&id=1iHWbbLnnYsxiRSC-aTUJvPjLhbtAA8o_",
                "https://drive.google.com/uc?export=view&id=1x8mUZaN8Csf7wK_S1HMeNweth6rND00P",
                "https://drive.google.com/uc?export=view&id=1huYkCRMz_ljUNN3e4TjPtuJQwegcfI11",
                "https://drive.google.com/uc?export=view&id=1HWNanbYQChsW9PvuNoeli6RZmCFc76BE",
                "https://drive.google.com/uc?export=view&id=1FLbNMVkhu82bIuXUSJ2NJa2tYai5tQmq",
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
                    "nama": "Muhammad Rafka Fatih Al Ghathfaan",
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
            display_images_with_data(gambar_urls_manajemen_minat_dan_bakat, data_list_manajemen_minat_dan_bakat)

    Departemen_Minbak()