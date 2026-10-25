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
            "https://drive.google.com/uc?export=view&id=1D_UN3rLMm5nypuPXsONCRF05bv_oQ8Fm",
            "https://drive.google.com/uc?export=view&id=1ywQxWrwv8jkFvqaGY08V3Ru2tm3zn8-v",
            "https://drive.google.com/uc?export=view&id=1dlQZffhSfdPGtTHjs_XJVDdfJCvG5lGr",
            "https://drive.google.com/uc?export=view&id=1SMjGrKj3JfE3Yj0vgvNvRuSxXFJP-xRu",
            "https://drive.google.com/uc?export=view&id=1_Jliw9dcizXRHBm5ubluQa9BiJWN1UvO",
            "https://drive.google.com/uc?export=view&id=1giS93lfc_6oODMGozbAS8Fg1Rj2AOBus",
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
                "kesan": "Bang Ginda kesannya baik, seru, asik juga dan ternyata sesuai sama kesannya, terus pas wawancara juga jawaban abangnya keren",  
                "pesan": "Semangat abang kahim, semoga cepat selesai TA nyaa"
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450046",
                "umur": "22",
                "asal": "Bangkinang",
                "alamat": "Sekretariat HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abangnya baik, terus kalo ngajar materi juga seru, keren juga kalo ngasih petuah bijak banget jujur",  
                "pesan": "Semangat abang sekjen kita semester 7 nyaa, semoga TA cepet selesaii ketemu di riuh wisudah nanti kitaa abang"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak cantik sekali, baik jugaa, ramah, cantik pokoknya",  
                "pesan": "Semangat kakak sekre kita yang paling cantik, semoga TA nya cepat selesaii"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Abangnya keren, baik banget saat wawancara, seruu banget jugaa",  
                "pesan": "Semangat abang menjalankan tupoksinya dan semangat juga untuk TA nya abangg"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakaknya cantik terus seru jugaa pas wawancara, kerenn kakaknyaa",  
                "pesan": "Semangat kakak bendaharaa, semoga TA nya cepat selesai kakak"
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bertemu Pak Tirta",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya cantik terus lucuu banget hobi ketemu pak tirtaa",  
                "pesan": "Semangat kakak bendahara mengerjakan TA, meet sama pak tirta + menjalankan tupoksinya"
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
            "https://drive.google.com/uc?export=view&id=1APvCEouNDZGGvrMM9KSMU-H8XaPyYisv",
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
            "kesan": "Kesan pertama kali liat bang ridho kek serem abangnya (karena aku nabrak abangnya), ternyata baik banget, seru, asik, sangat masyallah tabarakallah",  
            "pesan": "Semangat abangg TA. like dan komen, kabaleg keren."
            },
            ]
            display_images_with_data(gambar_urls_kabaleg, data_list_kabaleg)

        with tab2:
            # Pindahkan URL dan Data anggota Sekretaris ke dalam list ini
            gambar_urls_sekretaris = ["https://drive.google.com/uc?export=view&id=1CtYQfkn-7oQ9ayNJ2mU3nccTtHJXj3Vi",]
            data_list_sekretaris = [ 
            {
            "nama": "Juesi Apridelia Saragih",
            "nim": "123450085",
            "umur": "19",
            "asal": "Singkawang",
            "alamat": "Pelangi",
            "hobbi": "Dengerin lagu semusim dari marsel",
            "sosmed": "@j__eesie",
            "kesan": "Kakaknya cantikk banget, suka kalo ngobrol sama kak jue banyak obrolannya terus kakaknya seru banget jugaa",  
            "pesan": "Semangat kakak cantik TA dan penyiarannyaa, aku fans berat kakak, ditunggu cerita-cerita seru lainnyaa"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris, data_list_sekretaris)

        with tab3:
            # Pindahkan URL dan Data anggota Komisi I ke dalam list ini
            gambar_urls_komisi1 = [
            "https://drive.google.com/uc?export=view&id=1uYeDDORJD34qReI1atwBKh5IeDnZ6cSp",
            "https://drive.google.com/uc?export=view&id=1-G0fbypU7EwqTJXIg7-bKCCC-F970qG1",
            "https://drive.google.com/uc?export=view&id=1x84aGEakbajzbQpgA30ME-jZ2mXB6hWV",
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
            "kesan": "Abang ini keren banget pas KDP, aku ngefans bang, terus pintarnya pintar banget (wajar ozt ini)",  
            "pesan": "Infokan tutor mapress nya dong abangdaa"
            },
            {
            "nama": "Gh. Mikael Niko Antoni Setiadi",
            "nim": "124450025",
            "umur": "20",
            "asal": "Jabung",
            "alamat": "Jati Agung",
            "hobbi": "COD Musang",
            "sosmed": "@me._kael",
            "kesan": "Bang niko baik banget, sangat chill, sangat baik, sangat keren",  
            "pesan": "Semangat abangg kuliahnyaa, infokan tutor jadi pimsit"
            },
            {
            "nama": "Siti Sarifah Sumamah",
            "nim": "124450015",
            "umur": "19",
            "asal": "Bekasi",
            "alamat": "Kedaton",
            "hobbi": "Mancing",
            "sosmed": "@syt.rifa",
            "kesan": "Kakaknya cantik, terus kaget karena nama kami mirip, kakaknya sarifah aku zharifa, sama sama dipanggil rifa lagi",  
            "pesan": "Semangat kakak rifa kuliahnya - dari adik rifa"
            },
            ]
            display_images_with_data(gambar_urls_komisi1, data_list_komisi1)

        with tab4:
            # Pindahkan URL dan Data anggota Komisi II ke dalam list ini
            gambar_urls_komisi2 = [
                "https://drive.google.com/uc?export=view&id=1DBqY2wITFCuPFf0Zo5bRJFl5GwTgHrT0",
                "https://drive.google.com/uc?export=view&id=1c_ChPYs00RaFwOZLP5mASnR0PWXqH0vK",
                "https://drive.google.com/uc?export=view&id=1Gi6uBYlKKSJ4FN8G-Wr7mvBF6SL0DYD7",
                "https://drive.google.com/uc?export=view&id=1BKTO1WrhQtslcHr9ACsnJrI40XNYuXv0",
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
            "kesan": "Bang gip seru banget orangnya, asik, baik bangett juga, penjelasan studi kasusnya masuk akal",  
            "pesan": "Tutorkan kiat jadi kepala komisi II banggg"
            },
            {
            "nama": "Afghanis Nursholehatunnisa",
            "nim": "124450042",
            "umur": "19",
            "asal": "Kepulauan Mentawai",
            "alamat": "Owen Kost",
            "hobbi": "Ngoding",
            "sosmed": "@afghanisnt_",
            "kesan": "Kakaknya cantik dan baik bangett pas ngewawancarai aku, seru jugaa, terus kakaknya pas ngejawab pertanyaan di kelas masuk akal banget",  
            "pesan": "Kakak pj kami semangat yaa ngejalanin tupoksinyaa, semangat juga menghadapi huru hara semester 5 nyaa"
            },
            {
            "nama": "Hani Qurrota Aini",
            "nim": "124450020",
            "umur": "20",
            "asal": "CTR",
            "alamat": "Sukarame",
            "hobbi": "Baca AU",
            "sosmed": "@haniquratuain_",
            "kesan": "Kakak ini cantik bangett, suka kalo ngeliat kakak ini karena cantik banget pas aku di semester 1",  
            "pesan": "Semangat kak hani kuliahnyaa, semangat juga di baleg nya, kelompok greedy cinta kakak kokk"
            },
            {
            "nama": "Jeremia Halim",
            "nim": "124450101",
            "umur": "20",
            "asal": "Tanggerang",
            "alamat": "Teluk",
            "hobbi": "Nyanyi, olahraga",
            "sosmed": "@jeremia_hm",
            "kesan": "Abang ini keren banget kalo nyanyii udah kek lagi di Orkestra Sydney",  
            "pesan": "Abang semangat kuliahnya, semangat ketok ketok palunyaa, semangat abangg"
            },
            ]
            display_images_with_data(gambar_urls_komisi2, data_list_komisi2)

        with tab5:
            # Pindahkan URL dan Data anggota Komisi III ke dalam list ini
            gambar_urls_komisi3 = [
                "https://drive.google.com/uc?export=view&id=1ft829_eDMqlODPKF2868sZSnjJQUj-R4",
                "https://drive.google.com/uc?export=view&id=1o-GpRsP94mFu9NcbH9GHW6WOSFzrfqbr",
                "https://drive.google.com/uc?export=view&id=1vEPO1hA2U-cA0MmROIuGiDo1uZMao7Qd",
                "https://drive.google.com/uc?export=view&id=11AS58EsEH6Q7831c4bRe1kuBTnMloXKP",
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
            "kesan": "Kak monica keren banget pas ngejawab kalo dikasih pertanyaan, sukaa kerenn, cantik banget kakaknya jugaa",  
            "pesan": "Kak monica semangat kuliahnyaa, semangat jugaa di baleg, kamu keren kak cantik bangett"
            },
            {
            "nama": "Jona Timothy Ogatse Panjaitan",
            "nim": "124450111",
            "umur": "20",
            "asal": "Depok",
            "alamat": "Pemda Raya",
            "hobbi": "Gym sama Koleksi figure, nafas manual",
            "sosmed": "@nagatseee",
            "kesan": "Abangnya asik banget, baik banget, keren banget, palu nya juga keren banget",  
            "pesan": "Abang semangat kuliahnyaa, semangat ngebalegnyaa, infokan tutor ketok-ketok palunya bang"
            },
            {
            "nama": "Sekar Dini Widya Putri",
            "nim": "124450082",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Pemda",
            "hobbi": "Jajan sama nisa, putri, suci",
            "sosmed": "@sekardnwp",
            "kesan": "Kakaknya baik bangett, seru ngobrol sama kakaknya, terus ternyata kakaknya di baleg keren bangettt",  
            "pesan": "Semangat kak sekar kuliahnyaa, balegnyaa, ngawasnyaa, semuanya kakak"
            },
            {
            "nama": "Wan Nashwa Alhasni Yuska",
            "nim": "123450077",
            "umur": "20",
            "asal": "Pasay",
            "alamat": "Belwis",
            "hobbi": "Nyapa angin",
            "sosmed": "@nshaysk",
            "kesan": "Kakaknya cantik banget, ceria banget, suka kalo ngobrol sama kakak soalnya kakaknya seru banget pas diajak ngobrol",  
            "pesan": "Kak Nashwa semangat yaa TA nyaa, sehat sehat kakak semester 7 dan kakak baleg"
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
               "https://drive.google.com/uc?export=view&id=1JBoXUzygfyJQi8br3gTEO2-vt6GIoA9i",
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
                "kesan": "Kakaknya keren banget jujur, hebat banget bisa jadi senator terus kakaknya cantik banget",  
                "pesan": "Semangat kakak cantikk kuliahnyaa, semangat juga menyampaikan aspirasi kami kakak dan terimakasih"
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
                "kesan": "Abang ini lucu bangett pas wawancaraa #dutamelet, baik banget jujur, asik banget juga",  
                "pesan": "Semangat abang baik kuliahnyaa, kamu keren bangg"
                },
                {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "Bang nando baik orangnya, seru jugaa, keren juga, masyallah sekali",  
                "pesan": "Semangatt abang kuliahnyaaa"
                },
                {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Krui",
                "alamat": "Kota Baru",
                "hobbi": "Bikin video random dan upload di second",
                "sosmed": "@sciia_staff",
                "kesan": "Kakaknya cantik bangett, pertama kali ketemu kakaknya aku kaget karena cantik nya cantik banget",  
                "pesan": "Semangat kak sucii kuliah dan mendampingi cosvalnyaa, jangan lupa senyum kakak cantik"
                },
                {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Mancing",
                "sosmed": "@wielhawny",
                "kesan": "Abangnya asik bangettt seruuuuuu, baik banget banget jugaa, seru ngobrol sama abangnya",  
                "pesan": "Semangat bang wielman kuliahnyaa, semangat juga agenda mancingnyaa"
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
                "kesan": "Kak lia itu keren bangett pas nyampaikan materi, keren banget, aku kagumm",  
                "pesan": "Semangat kak lia kuliahnyaa, semangat juga ngerjain TA nyaa semoga cepat selesai"
                },
                {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayyesian",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kak qila itu cantik banget gemasss, lucu juga kakaknyaa",  
                "pesan": "Semangat kuliahnyaa kakak cantik secantik bunga matahari"
                },
                {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Ujung Terang",
                "hobbi": "Bulu Tangkis",
                "sosmed": "@hazelhandhaka",
                "kesan": "Bang hazel keren bangett, baik jugaa, ngefans aku bang",  
                "pesan": "Semangat abangg kuliahnyaa, semangat basonnyaa, semangatt"
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
                "kesan": "Kak nadya cantik banget, keren bangett pas materii",  
                "pesan": "Kakak semangat yaaa kuliahnyaa kamu keren bangett"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas Belwis",
                "hobbi": "Dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Ibu mentor yang cantik, baik, imup nan lucu sekaliii",  
                "pesan": "Semangat kak dwiiii kuliahnyaaa, greedy cinta kamu kakakk"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
            "kesan": "First impression ke bang Kevin tuh beneran sosok yang sangat menginspirasi dan wibawanya dapet banget",
            "pesan": "Semangatt terus bang Kevin buat kuliah dan urusan TA nya, semoga selalu dimudahkan dan dilancarkan segala urusannya yaa, aamiin!"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_minbak, data_list_kepala_departemen_minbak)
        with tab2:
            gambar_urls_sekretaris_departemen_minbak = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",]
            data_list_sekretaris_departemen_minbak = [ 
            {
            "nama": "Gusti Putu Ferazka Dhiyamika",
            "nim": "123450046",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Dadi",
            "hobbi": "Mendaki",
            "sosmed": "@ferazkaa",
            "kesan": "Kakanya rapi banget dan keliatan banget kalau orangnya super cekatan tiap diajak ngobrol",
            "pesan": "Semangatt terus yaa kak Ferazka buat perkuliahan dan TA nya, semoga selalu diberikan kelancaran di setiap langkahnya, aamiin!"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_departemen_minbak, data_list_sekretaris_departemen_minbak)            
        with tab3:
            gambar_urls_manajemen_aktivitas_dan_kompetisi = [            
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
            "kesan": "Abang satu ini keren banget dan vibesnya selalu tenang waktu ngasih penjelasan ke kita-kita",
            "pesan": "Semangatt terus bang Ali kuliah dan TA nya! Semoga dimudahkan segala urusannya dan sehat selalu yaa bang!"
            },
            {
            "nama": "Ayu Andriani Parlina Wati",
            "nim": "124450058",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Airan",
            "hobbi": "Belajar + menghitung uang",
            "sosmed": "@aayuandriani_",
            "kesan": "Kak Ayu orangnya ramah banget dan super aktif kalau pas lagi sesi ngobrol bareng",
            "pesan": "Semangat terus kaa Ayu kuliahnya! Jangan lupa selipin waktu istirahat di tengah padatnya jadwal perkuliahan yaa!"
            },
            {
            "nama": "Dafa Elpriza",
            "nim": "124450131",
            "umur": "21",
            "asal": "Bekasi",
            "alamat": "Way Kandis",
            "hobbi": "Jogging",
            "sosmed": "@dafaelpriza_",
            "kesan": "Asik banget pembawaannya dan gampang banget buat diajak komunikasi atau diskusi",
            "pesan": "Semangat terus kak Dafa perkuliahannya! Tetap jaga kesehatan di era jadwal yang serba padet ini yaa!"
            },
            {
            "nama": "Juwita Sari",
            "nim": "124450066",
            "umur": "19",
            "asal": "Lampung Barat",
            "alamat": "Pemda",
            "hobbi": "Mancing",
            "sosmed": "@ju.juwitaaa_",
            "kesan": "Kak Juwita murah senyum banget dan vibesnya positif abis kalau lagi cerita-cerita",
            "pesan": "Semangat terus kuliahnya kaa! Semoga kaka selalu diberikan kemudahan dan dikelilingi hal-hal baik yaa!"
            },
            {
            "nama": "Muhammad Afdal Luthfi",
            "nim": "124450047",
            "umur": "19",
            "asal": "Lampung Tengah",
            "alamat": "Jl. Pulau Damar",
            "hobbi": "Memantau dl tugas",
            "sosmed": "@afdall.03",
            "kesan": "Kelihatan bertanggung jawab banget dan selalu fokus pas kita lagi bahas sesuatu",
            "pesan": "Semangat terus kaa Afdal kuliahnya! Jaga kesehatan selalu dan jangan lupa buat luapin waktu rehat!"
            },
            {
            "nama": "Salsabila Nazwa Putri",
            "nim": "124450002",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Korpri",
            "hobbi": "Nongkrong di kopken",
            "sosmed": "@slbnzw_",
            "kesan": "Kak Caca orangnya asik banget dan ceria parah tiap kali disapa",
            "pesan": "Semangat terus kaa kuliahnya! Semoga harinya selalu menyenangkan dan sehat-sehat terus yaa!"
            },
            ]
            display_images_with_data(gambar_urls_manajemen_aktivitas_dan_kompetisi, data_list_manajemen_aktivitas_dan_kompetisi)
        with tab4:
            gambar_urls_manajemen_minat_dan_bakat = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
            "kesan": "Sangat mengayomi dan sabar banget waktu ngasih masukan pas ngobrol",
            "pesan": "Semangat terus yaa kak Ridwan! Semangat juga buat nyusun TA nya nanti, semoga dipermudah dan dilancarkan sampai selesai, aamiin!"
            },
            {
            "nama": "Andra Ilham Bintang",
            "nim": "124450060",
            "umur": "18",
            "asal": "Sumatera Selatan",
            "alamat": "Kotabaru",
            "hobbi": "Main rubik",
            "sosmed": "@andra.lhm",
            "kesan": "Baik banget, gemass parah, vibesnya ngayomi dan beneran orang baik banget",
            "pesan": "Semangatt terus yaa bang Andra kuliahnya! Jangan lupa kasih jeda waktu buat istirahat dari padetnya jadwal, semoga abang selalu dikelilingi hal-hal baik!"
            },
            {
            "nama": "Bryan Paskah Telaumbanua",
            "nim": "124450003",
            "umur": "20",
            "asal": "Nias",
            "alamat": "Belwis",
            "hobbi": "Live tiktok",
            "sosmed": "@bryantel_",
            "kesan": "Sangat menghibur dan ramah banget kalau diajak tukar pikiran",
            "pesan": "Semangat terus perkuliahannya kak Bryan! Jangan lupa buat selalu jaga kesehatan yaa!"
            },
            {
            "nama": "Ghiyats Thabularasa Meardhy",
            "nim": "124450067",
            "umur": "17",
            "asal": "Surabaya",
            "alamat": "Kemiling",
            "hobbi": "Nanem Sawit",
            "sosmed": "@meardhy_ghiyats",
            "kesan": "Orangnya unik banget dan selalu bersemangat tiap lagi diskusi",
            "pesan": "Tetap semangat dan sukses selalu buat perkuliahannya yaa bang Ghiyats!"
            },
            {
            "nama": "Indah Julia Mawar Pratiwi",
            "nim": "124450055",
            "umur": "20",
            "asal": "Pringsewu",
            "alamat": "Airan",
            "hobbi": "Bengong",
            "sosmed": "@indahjuliaa",
            "kesan": "Kak Indah bersahabat banget dan enak diajak ngobrolin banyak hal",
            "pesan": "Sukses terus perkuliahannya kak Indah! Semoga kaka selalu dikelilingi sama kebaikan yaa!"
            },
            {
            "nama": "Jacinda Kesya Alvara",
            "nim": "124450023",
            "umur": "18",
            "asal": "Kalimantan Barat",
            "alamat": "Korpri",
            "hobbi": "Nyapu depan gacoan",
            "sosmed": "@cacalvra",
            "kesan": "Vibesnya ceria banget dan selalu bisa bikin suasana ngobrol dapet",
            "pesan": "Semangat terus kaa Caca kuliahnya! Jaga kesehatannya di tengah jadwal yang serba padet ini yaa!"
            },
            {
            "nama": "Muhammad Rafka Fatih Ghathfaan",
            "nim": "124450089",
            "umur": "20",
            "asal": "Padang",
            "alamat": "Kotabaru",
            "hobbi": "Bangun pagi",
            "sosmed": "@muhammdrafka_",
            "kesan": "Disiplin banget keliatannya dan tipe yang bisa diandalkan pas diajak koordinasi",
            "pesan": "Sukses selalu buat perkuliahannya bang Rafka! Jangan lupa selipin waktu istirahat ya bang!"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Bang Ihsan asik banget dan cara dia ngejelasin sesuatu bikin aku betah ngobrol",
                "pesan": "Semangat terus kuliah dan persiapan TA nya yaa bang Ihsan! Semoga selalu diberi kemudahan!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_ssd, data_list_Kadep_ssd)
        with tab2:
            gambar_urls_sekdep_ssd = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kak Inaya ramah parah dan seru banget diajak tukar cerita",
                "pesan": "Semangat terus kuliahnya kak Inaya! Semoga lancar terus semua urusannya yaa!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_ssd, data_list_sekdep_ssd)
        with tab3:
            gambar_urls_kemitraan = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kak Afifah baik banget dan tenang banget bawaannya waktu diajak bicara",
                "pesan": "Semangat terus kuliahnya yaa kak Afifah! Jaga kesehatan selalu!"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal": "Lamteng",
                "alamat": "Pemda",
                "hobbi": "Nonton yutub",
                "sosmed": "-",
                "kesan": "Bang Hasan orangnya asik dan pembawaannya santai tapi tetep dapet",
                "pesan": "Semangat terus bang Hasan kuliahnya! Semoga dipermudah terus langkahnya!"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "20",
                "asal": "Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton dracin",
                "sosmed": "@layinr_",
                "kesan": "Kak Layina ramah dan humble banget pas ditanya-tanya",
                "pesan": "Semangat kuliahnya kak Layina! Semoga selalu diberikan kelancaran!"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal": "Sumbar",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Orangnya manis banget dan komunikatif kalau diajak ngobrol",
                "pesan": "Semangat terus kuliahnya kaa Talitha! Sukses terus yaa!"
            },
            ]
            display_images_with_data(gambar_urls_kemitraan, data_list_kemitraan)
        with tab4:
            gambar_urls_kewirausahaan = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Bang Iqbal asik banget diajak diskusi dan selalu seru kalau sharing",
                "pesan": "Semangat terus kuliahnya bang Iqbal! Sukses selalu yaa!"
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn",
                "kesan": "Kak Anadia keliatan pekerja keras dan ramah banget pas disapa",
                "pesan": "Semangat terus kuliahnya kak Anadia! Semoga impiannya tercapai satu-persatu!"
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "124450062",
                "umur": "21",
                "asal": "Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest",
                "kesan": "Bang Fikri keren dan pembawaannya santai tapi tetep asik",
                "pesan": "Semangat kuliahnya bang Fikri! Jaga kesehatan selalu yaa!"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal": "Sumbar",
                "alamat": "Belwis",
                "hobbi": "Fishing and game",
                "sosmed": "@Afdhal",
                "kesan": "Orangnya seru dan friendly banget kalau pas dapet kesempatan ngobrol",
                "pesan": "Semangat terus perkuliahannya bang Afdhal! Semoga lancar terus!"
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal": "Lamutara",
                "alamat": "-",
                "hobbi": "Nonton kartun",
                "sosmed": "@anggunitaaa_",
                "kesan": "Kak Anggun baikk dan manis banget vibesnya",
                "pesan": "Semangat terus kuliahnya kak Anggun! Jaga pola tidurnya yaa!"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal": "Lamtim",
                "alamat": "Kotabaru",
                "hobbi": "Olahraga",
                "sosmed": "@delaanisafitri",
                "kesan": "Kak Della sangat baik dan positif vibes banget pas diajak ngobrol",
                "pesan": "Semangat terus kuliahnya kak Della! Semoga bahagia selalu!"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "JUJUR KEREN BANGETTTT, pengetahuannya luas banget dan rasanya pengen berguru terus sama abang",
                "pesan": "Semangatt TA nya nanti banggg! Tapi saya beneran butuh banget belajar banyak dari abang karena ilmunya daging semua!"
            },
            ]
            display_images_with_data(gambar_urls_kepala_departemen_mikfes, data_list_kepala_departemen_mikfes)
        with tab2:
            gambar_urls_sekretaris_mikfes = ["https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",]
            data_list_sekretaris_mikfes = [ 
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@tvnty_",
                "kesan": "First impression ku ke kak Tanty tuh orangnya ceria banget dan beneran gemasss",
                "pesan": "Semangatt TA nya kaa Tanty! Semoga diberikan kelancaran dalam mengerjakan segalanya, jangan lupa jaga kesehatan!"
            },
            ]
            display_images_with_data(gambar_urls_sekretaris_mikfes, data_list_sekretaris_mikfes)
        with tab3:
            gambar_urls_Divisi_Professional_Skill_and_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Inspiratif banget dan sosok yang selalu ninggalin kesan baik pas diajak bicara",
                "pesan": "Masih ga nyangka secepat itu abang kembali ke pangkuan-Nya, tapi sekarang abang udah ga sakit lagi ya.. Doa terbaik untuk mu bang Fadil, fly high and rest in peace a good soul."
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20",
                "asal": "Batam",
                "alamat": "Way kandis",
                "hobbi": "Katama",
                "sosmed": "manuelfdk_",
                "kesan": "Penyampaian abang beneran ngebantu aku banget pas lagi diskusi",
                "pesan": "Abang keren bangett! Tetap dilanjutkan semangatnya yaa bang, dan jangan lupa jaga pola tidur serta makannya!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Travelling",
                "sosmed": "@violaadrtr_",
                "kesan": "Kak Viola cantik banget dan sangat welcome kalau diajak ngobrol",
                "pesan": "Kaka semangat kuliahnya yaa! Jaga pola makan dan pola tidurnya, jangan sampai drop yaa kaa!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "rolling skate",
                "sosmed": "@risarmdna",
                "kesan": "Cutee banget vibesnya dan enak diajak tukar cerita",
                "pesan": "Kaka keren banget! Semoga kaka selalu menemukan kebaikan di setiap hal-hal kecil yaa, jaga kesehatan selalu!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19",
                "asal": "Kepulauan Riau",
                "alamat": "Telung Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Waktu kak Vanny ngejelasin sesuatu pas ngobrol, jujur keren banget dan tertata rapi",
                "pesan": "Semoga apapun plan kaka bisa tercapai satu per satu yaa kaa! Semangat kuliahnya dan jaga kesehatan!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Cantik dan ramah sekali pembawaannya pas menyapa",
                "pesan": "Sukses selalu kaa Yulia kedepannya! Semoga apapun wishlist kakak bisa terwujud satu per satu yaa!"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Professional_Skill_and_Development, data_list_Divisi_Professional_Skill_and_Development)
        with tab4:
            gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Jujur keren banget penyampaian gagasan dari bang Keya, penyampaiannya selalu menarik",
                "pesan": "Semangat nanti TA nya bang Keya! Semoga dipermudah jalan dan urusannya selalu!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "_els.a",
                "kesan": "Ceria dan social butterfly banget pas ngobrol bareng",
                "pesan": "Kaa Elsa walau perkuliahan makin bertambah semester terasa makin ngebantai, tetap semangat yaa! Jaga pola makan dan tidurnya!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Gemasss dan super ceria kalau lagi cerita-cerita",
                "pesan": "Go semangat goo! Kaa Fadya semoga selalu diberikan kemudahan di setiap langkahnya yaa!"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Keren banget pembawaannya dan sangat berwawasan",
                "pesan": "Semangat terus kaa Lovi buat nyapai impian kaka satu per satu yaa!"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@keyashafi",
                "kesan": "Abang satu ini keren dan gaya bicaranya santai tapi berbobot",
                "pesan": "Semangatt terus yaa bang Alsi kuliahnya! Jangan lupa buat tetep jaga kesehatan!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Cantik, imut, cutee dan beneran gemas pas disapa",
                "pesan": "Semoga dunia selalu berbaik hati sama kak Sherena yaa, semangattt kuliahnyaa!"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Pusat_Inovasi_dan_Kajian_Akademik, data_list_Divisi_Pusat_Inovasi_dan_Kajian_Akademik)
        with tab5:
            gambar_urls_Divisi_Research_Development = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Pinter bangettt, beneran aku perlu banyak belajar dari bang Razin",
                "pesan": "Semangattt bang Razin nanti TA nyaa, semoga dipermudah dan diperlancar semuanyaa, aamiin!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca",
                "sosmed": "@faizaanjanii",
                "kesan": "First impression ku ke kak Faiza beneran kagum dan dia salah satu role model aku",
                "pesan": "Kaka beneran keren bangettt! Mau dong tips n trick cara bagi waktu belajar sama aktivitas lain kak #helppp!"
            },
            {
                "nama": "Gathfan Nadif ALi",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Abang satu ini keren dan gaya bicaranya santai tapi asik",
                "pesan": "Semangatttt kuliahnya bang Gathfan, jangan lupa jaga kesehatan selalu yaa!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame",
                "sosmed": "@apiszzaja_",
                "kesan": "Keren tapi kadang abangnya suka jail dikit kalau pas lagi ngobrol",
                "pesan": "Semangatt terus yaa bang Hafidz perkuliahannya!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450062",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Nge-gym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Keren dan pinter banget! Masih keinget momen diskusi waktu itu, ilmunya daging banget",
                "pesan": "Minat banget berguru tentang komputasi sama abang karena pengetahuannya luas banget! Semangat terus kuliahnya bang!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Menari",
                "sosmed": "@melva_fbrt",
                "kesan": "CUTEEE, beneran gemas banget gaya bicaranya pas sapaan",
                "pesan": "Semangatt terus kaa Melva kuliahnyaa! Stay happy selalu!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "125450099",
                "umur": "20",
                "asal": "Lampung Selatan",
                "alamat": "Asrama",
                "hobbi": "Membaca",
                "sosmed": "@syaafiq",
                "kesan": "Inspiratif person dan pembawaannya tenang banget pas lagi ngebahas topik",
                "pesan": "Pengalaman abang beneran keren-keren banget, semoga plan abang satu per satu bisa tercapai yaa, aamiin!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "150 (p, mksud bg??? #kaget)",
                "asal": "Rajabasa",
                "alamat": "Balam",
                "hobbi": "Tennis Meja",
                "sosmed": "@henryferdianto",
                "kesan": "Orang serius tapi kadang becandanya dapet banget pas ngobrol",
                "pesan": "Kocak banget dah, semoga hal-hal baik selalu melingkupi hidup abang yaa, aamiin!"
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
                "kesan": "Bang Haikal keren banget dan keliatan jago pas diajak tukar pikiran soal teknis",  
                "pesan":"Semangat TA nya bang Haikal, semoga diberi kemudahan dan dilancarkan semua urusannyaa!"
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
                "kesan": "Kak Risma cantik dan ramah banget tiap diajak komunikasi",  
                "pesan":"Semangattt kaa Risma untuk persiapan TA nyaa, jangan lupa jaga kesehatan yaa!"
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
                "kesan": "Positive energy banget vibes kak Hanna pas sapa-sapaan",  
                "pesan": "Semoga kaka selalu dilingkupi oleh banyak kebaikan yaa, dan semangat nanti nyusun TA nya!"
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "20",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhnghnii",
                "kesan": "Gaya bicaranya keren dan friendly banget kalau diajak ngobrol",  
                "pesan":"Sehat selalu bang Farhan dan semangat persiapan TA nya yaa!"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Menulis wishlist",
                "sosmed": "@aisyahkhair",
                "kesan": "Kakanya gemas banget dan super ramah tiap ketemu komunikasi",  
                "pesan":"Sehat-sehat selalu yaa ka Aisyah, semangat kuliahnya!"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap Liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Lucuuu banget pembawaannya dan enjoy kalau lagi diajak tukar ide",  
                "pesan":"Sehat selalu kaa Cerine, dan semangat terus perkuliahannya!"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "22",
                "asal": "Kisaran City",
                "alamat": "Pemda",
                "hobbi": "Kick Boxing",
                "sosmed": "@jay.saputratmb",
                "kesan": "Asik dan ramah banget kalau diajak bicara hal apapun",  
                "pesan": "Semangatt kuliahnya bang Jaya, semoga plan abang bisa tercapai satu per satu!"
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Nonton ASMR",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla gemasss banget dan tutur katanya halus pas ngobrol",  
                "pesan":"Semangatt terus kaa Najla kuliahnyaa, jaga kesehatan selalu!"
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin Harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "Abang satu ini keren dan ramah parah pas disapa",  
                "pesan":"Semangatt bang Rozak menjalani perkuliahan, sukses selalu!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Sangat membantu dan sabar banget pas ngejelasin hal-hal yang kurang aku pahamin",  
                "pesan":"Terima kasih banyak kaa Teresa udah luapin waktu buat ngajarin! Maaf kalau kemarin aku banyak diamnya pas ngobrol karena waktunya bentrok sama agenda lain."
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
                "kesan": "Abangnya ramah banget dan tenang pembawaannya pas ngobrol",  
                "pesan":"Semangattt bang Hanif kuliahnya, semoga lancar terus yaa!"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": "Kak Audina baik dan penyabar banget tiap diajak tukar pikiran",  
                "pesan":"Sehat selalu dan semangat kuliahnya yaa kaa Audina!"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Dengerin lagu",
                "sosmed": "@cikamrbn",
                "kesan": "Kak Cika baik dan lucuu pembawaannya pas disapa",  
                "pesan":"Semangatt kaa Cika kuliahnya! Stay safe & healthy!"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kakanya baik dan sangat terbuka kalau diajak ngobrol",  
                "pesan":"Jangan lupa jaga kesehatan dan semangat kuliahnya yaa kaa Gustin!"
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berburu ayam hutan",
                "sosmed": "@muhvinz_",
                "kesan": "Seruu banget abangnya kalau pas diajak ngobrolin topik apapun",  
                "pesan":"Semangattt kuliahnya bang Harvin! Sukses selalu!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nginep di rumah Yollanda",
                "sosmed": "@snasaa._",
                "kesan": "Anggun banget vibes kak Rafa dan ramah pas disapa",  
                "pesan":"Semangat teruss kaa Rafa kuliahnyaa, bahagia selalu!"
            },
        ]
            display_images_with_data(gambar_urls_kerohanian, data_list_kerohanian)
    internal()
elif menu == "Departemen PSDA":
    def PSDA():
        st.markdown("<h3 style='text-align: center;'>Departemen Pengembangan Sumber Daya Anggota</h3>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["Kepala Departemen", "Sekretaris Departemen", "Divisi Kaderisasi", "Divisi Peningkatan Mutu Anggota"])
        with tab1:
            gambar_urls_Kadep_psda = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Cantik dan fashionable banget penampilannya pas ngobrol",  
                "pesan":"Semangat TA nya kaa Arienta, semoga diberi kemudahan dan dilancarkan semua urusannyaa!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_psda, data_list_Kadep_psda)
        with tab2:
            gambar_urls_sekdep_psda = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kak Vany tegas tapi tetep dapet aura ramahnya kalau diajak komunikasi",  
                "pesan":"Semangattt kaa Vany untuk TA nyaa, jangan lupa jaga kesehatan ya kaa!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_psda, data_list_sekdep_psda)   
        with tab3:
            gambar_urls_Divisi_Kaderisasi = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Abang satu ini kharismatik banget pas bicara, penyampaian materinya berbobot dan daging semua",  
                "pesan": "Semoga abang Nobel selalu dilingkupi oleh banyak kebaikan yaa, dan semangat persiapan TA nya nanti!"
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Samping kos Jemar",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Kaget banget pas tau abang NIM ku ternyata keren begini, tensinya dapet tapi tetep humble pas diajak ngobrol",  
                "pesan":"Semangat terus bang Azmi, sukses buat hal-hal selanjutnya! #salampaguyuban110"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Peninjauan, 10 kota di atas, Solok, Sumatera Barat",
                "alamat": "Blok D 79, Jl Manggis 8 Perum Pemda, Way Huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "Tegas banget pembawaannya tapi aslinya baik pas denger dia ngejelasin sesuatu",  
                "pesan":"Jaga kesehatan selalu bang Ayake, seimbangin waktu pikiran biar gak gampang capek yaa!"
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal": "Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Keliatan tegas bgt tapi kalau diajak komunikasi sebenernya santai dan masuk akal",  
                "pesan":"Jaga pola pikir bang Caesar, jangan terlalu dibuat stress kalau ada kendala!"
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal": "Debu Tanah",
                "alamat": "Di sebelah pasar, di bawah turunan, di atas tanjakan, di seberang kontrakan Yazid Rizal",
                "hobbi": "Ngegiring anak ayam bermain di Lapangan",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah banget kalau pas lagi ngobrol santai",  
                "pesan": "Semangat kuliahnya kaa! Walaupun makin tambah semester makin banyak tantangan, tetep jaga pikiran dan kesehatan yaa!"
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal": "Rantau Perapat",
                "alamat": "Belakang kos Ayake",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Friendly dan gaya bicaranya asik pas diajak diskusi ringan",  
                "pesan":"Semangatt bang Haikal kuliahnya, semoga kebaikan selalu melingkupi abang!"
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Sabang",
                "alamat": "Nomaden",
                "hobbi": "Duduk samping Henry",
                "sosmed": "@putrimannaa",
                "kesan": "Pas awal kerasa tegas banget, tapi begitu denger penjelasan aslinya ramah bgt",  
                "pesan":"Ternyata kak Putri baik dan hangat bgt kalau diajak bicara santai. Semangat terus kuliahnya kaa!"
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "18",
                "asal": "Kota Gajah",
                "alamat": "Depan pemancingan",
                "hobbi": "Nyuapin anak ayam",
                "sosmed": "@queentanabila",
                "kesan": "Kak Queenta penyampaiannya soft spoken banget pas kita lagi ngobrol",  
                "pesan":"Jaga kesehatan kaa Queenta, dan semangat terus perkuliahannya!"
            },
            ]
            display_images_with_data(gambar_urls_Divisi_Kaderisasi, data_list_Divisi_Kaderisasi)
        with tab4:
            gambar_urls_Divisi_Peningkatan_Mutu_Anggota = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Asik dan seru banget bang Desman kalau diajak ngobrolin banyak hal",  
                "pesan":"Semangatt TA nya nanti bang Desman, semoga dilancarkan segala urusannya!"
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Sukarame",
                "hobbi": "Makan Aice",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzelya cantik dan ramah bgt pembawaannya pas disapa",  
                "pesan":"Semangattt kaa Azzelya kuliahnyaa! Jangan lupa jaga kesehatan jugaa!"
            },
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charlindah baik dan penyabar sekali waktu kita komunikasi",  
                "pesan":"Sehat selalu dan semangat kuliahnya yaa kaa Charlindah!"
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal": "Nibire, Papua",
                "alamat": "Sebelah kos Haikal",
                "hobbi": "Memahat patung",
                "sosmed": "@jemarrro",
                "kesan": "Tegas banget pembawaannya, tapi lumayan welcome pas diajak ngobrol",  
                "pesan":"Semangat kuliahnya bang Jemar, sehat-sehat selalu yaa!"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "19",
                "asal": "Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila baik dan ramah banget tiap kali disapa",  
                "pesan":"Jangan lupa jaga kesehatan dan semangat perkuliahannya kaa Nabila!"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "20",
                "asal": "Tembung",
                "alamat": "Belwis Tengah",
                "hobbi": "Mancing",
                "sosmed": "@dearfkvmfl",
                "kesan": "Baik dan asik banget cara bicaranya pas tukar pendapat",  
                "pesan":"Semangattt perkuliahannya yaa bang Rafli!"
            },
            {
                "nama": "Salavia Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal": "Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Nonton",
                "sosmed": "@avi.nhr",
                "kesan": "Imut dan lucu banget vibes kak Salavia pas disapa",  
                "pesan":"Semangat teruss kaa Salavia kuliahnyaa, stay happy!"
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Charismatic woman banget, baik tapi punya sisi tegas pas lagi ngomongin hal serius",
                "pesan": "Sukses selalu kaa Arini kedepannya, dan nanti semangat nyusun TA nyaa!"
            },
            ]
            display_images_with_data(gambar_urls_Kadep_eksternal, data_list_Kadep_eksternal)
        with tab2:
            gambar_urls_sekdep_eksternal = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "kesan": "Kak Byla cantik dan baik banget pas diajak tukar ide",
                "pesan": "Semangatt kaa Byla kuliahnya dan juga semangatt pas nyusun TA nanti!"
            },
            ]
            display_images_with_data(gambar_urls_sekdep_eksternal, data_list_sekdep_eksternal)
        with tab3:
            gambar_urls_hubungan_luar = [            
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
                "kesan": "Imut banget gaya bicaranya dan ramah pas ngobrol",
                "pesan": "Semangat kaa Khoirul nanti nyusun TA nyaa, semoga diberikan kemudahan dalam segala hal, aamiin!"
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
                "kesan": "KERENNNN! Bang Rizky beneran jadi salah satu role model aku pas denger gagasannya waktu wwc",
                "pesan": "Jaga kesehatan selalu yaa bang Rizky di tengah aktivitas perkuliahan!"
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
                "kesan": "Kakanya ramah dan baik banget pas diajak diskusi",
                "pesan": "Jaga kesehatan selalu kaa Adinda, dan semangatt kuliahnyaa!"
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
                "kesan": "Keren dan ramah pembawaannya pas menyapa",
                "pesan": "Semangat terus bang Bimo kuliahnyaa, jaga kesehatan juga!!"
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
                "kesan": "Keren dan santai bgt pas diajak tukar cerita",
                "pesan": "Semangattt bang Abiyyi kuliahnyaa, jaga kesehatan jugaa!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "124450010",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobbi": "Nonton Film",
                "sosmed": "@asemeilani",
                "kesan": "Baik dan lucu banget kak Asri kalau pas diajak omong",
                "pesan": "Sukses selalu kak Asri untuk ke depannya yaa!"
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
                "kesan": "Kerennn, baik dan ramah bgt pembawaannya pas sesi wawancara",
                "pesan": "Semangatt terus bang Bima kuliahnya walau makin nambah semester makin nambah tantangannya. Jaga kesehatan jugaa!"
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
                "kesan": "Baik dan lucu banget pas lagi sesi ngobrol",
                "pesan": "Kak Indah versi penyabar beneran terbaik banget, semangat terus yaa kaa!"
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
                "kesan": "Gemasss dan komunikatif banget pas diajak bicara",
                "pesan": "Jaga kesehatan yaa kaa Riska, dan semangat juga kuliahnya!!"
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
                "kesan": "Kak Yollanda keren, hebat, dan kuat banget dalam ngebagi urusannya pas kita ngobrol",
                "pesan": "Jaga kesehatan yaa kaa Yollanda! Jangan sampai drop yaa kaa!"
            },
            ]
            display_images_with_data(gambar_urls_hubungan_luar, data_list_hubungan_luar)
        with tab4:
            gambar_urls_pengabdian_masyarakat = [
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
                "kesan": "Baik, ramah, dan welcome banget pas disapa",
                "pesan": "Semangatt bang Adit ngerjain TA nya, semoga selalu dipermudah langkah selanjutnyaa, aamiin!"
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
                "kesan": "Keren banget kak Fathya dan enakan diajak bicara",
                "pesan": "Jaga kesehatan yaa kaa Fathya, dan capai impian kaka satu per satu!"
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
                "kesan": "Manis dan imut bgt vibes kak Tarisya pas kita ngobrol",
                "pesan": "Sukses selalu kaa Tarisya untuk kedepannya, raih goals kaka satu per satu!"
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
                "kesan": "Cantik dan ramah bgt waktu nyapa",
                "pesan": "Jangan lupa untuk selalu berbahagia yaa kaa Ashila!"
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
                "kesan": "Keren dan baik pembawaannya pas diajak tukar ide",
                "pesan": "Semangat kuliahnya dan jaga kesehatannya bang Danil!"
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
                "kesan": "Pembawaannya santai dan asik banget diajak omong",
                "pesan": "Kerenn bang Favian, semangatt menjalani perkuliahan dan kehidupan! #salambinjai"
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
                "kesan": "Abang satu ini keren bgt pas ngobrol santai dan enak diajak diskusi",
                "pesan": "Panjang umur sehat selalu bang Yazid, tetep semangat kuliahnya yaa!"
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
                "kesan": "KERENNN, jujur inspiring banget waktu denger tanggapannya pas wwc",
                "pesan": "Semangattt terus bang Jaldi buat gapai impiannya satu per satu!!"
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
                "kesan": "Kakanya imut dan ramah banget pas diajak omong",
                "pesan": "Semangatttttt kaa Saskia kuliahnyaa! GO GOO!!"
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
                "kesan": "Ramah dan cantik, vibes kak Selma ceria dan positif banget",
                "pesan": "Semangat terus perkuliahannya kak Selma! Stay bright!"
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
                "jabatan": "Kepala Departemen",
                "kesan": "KAKA KERENN!! Kagum banget sama daya tahannya pas ngobrolin kesibukannya",
                "pesan": "Jujur takjub sih aku sama tangguhnya kak Nayla! Tetap semangat terus yaa kak Nay!"
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
                "divisi": "Sekdep",
                "jabatan": "Sekdep",
                "kesan": "KEREN JUGA JUJURRR, enak diajak diskusi dan ramah bgt",
                "pesan": "Tetap semangat terus yaa ka Donna, semoga apapun wishlist kaka bisa tercapai satu per satuu!"
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
                "jabatan": "Kepala Divisi",
                "kesan": "TAKJUB banget sama pemikiran dan cara bicaranya pas diskusi",
                "pesan": "Semangatt terus bang Labo buat kuliah dan segalanya yaa!"
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
                "kesan": "Gemes bangettt dan ceria pembawaannya pas disapa",
                "pesan": "Tetap semangat yaa kaa Anash walau beban perkuliahan kadang lumayan padet!"
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
                "kesan": "Keren dan enak banget buat diajak ngobrolin banyak hal",
                "pesan": "Jaga kesehatan selalu kaa Felisya, jangan lupa bahagia jugaa!!"
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
                "kesan": "Kerennnnn dan komunikatif banget pas diajak diskusi",
                "pesan": "Semangattt terus bang Razan!! Sempetin waktu buat istirahat sejenak dari perkuliahan yaa!"
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
                "jabatan": "Kepala Divisi",
                "kesan": "Ramah sekali pembawaannya pas lagi tukar pikiran",
                "pesan": "Semangattt ka Sania kuliahnyaa, sempatin waktu buat self reward yaa!"
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
                "kesan": "My kaka cantik, ramah, dan imut banget kalau disapa",
                "pesan": "Terus bahagia yaa ka Allishaa, sukses kuliahnya!"
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
                "kesan": "Gemasss bgt dan selalu ceria pas ngobrol",
                "pesan": "Kak Alya ramah bangett, semoga kaka selalu dikelilingi oleh hal-hal baik yaa!"
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
                "kesan": "Ramah banget pas kita sempet ngobrol santai",
                "pesan": "Semangatt ka Bunga kuliahnyaa, jaga pola makan dan jangan stress-stress yaa!"
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
                "kesan": "Lucuuu dan pembawaannya santai banget pas bicara",
                "pesan": "Semangattt teruss ka Difanya kuliahnyaa, sempatkan waktu untuk rehat sejenak yaa!"
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
                "kesan": "Gemasss bgt vibesnya pas nyapa",
                "pesan": "Semangat selalu kaa Nazlah perkuliahannya!"
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
                "jabatan": "Anggota",
                "kesan": "Kakanya baik dan ramah banget pas diajak diskusi",
                "pesan": "Semangatt kuliahnya kaa Raihanna, jangan lupa selalu berbahagiaa!"
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
                "kesan": "Baik banget abangnya dan komunikatif pas diajak ngobrol",
                "pesan": "Semoga bang Daffa selalu dilingkupi oleh kebaikan yaa!"
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
                "kesan": "Kerenn bgt gaya bicaranya dan santai",
                "pesan": "Jangan lupa jaga kesehatan selalu bang Edsel dan tetap bahagia!"
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
                "kesan": "Kakanya asik bgt pas diajak tukar cerita",
                "pesan": "Sehat selalu dan semangat terus kaa Lucia!"
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
                "kesan": "Kakanya baik dan ramah banget pas disapa",
                "pesan": "Semangatt terus kaa Shafa, semoga selalu bahagiaa!"
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
                "kesan": "Cantik dan ramah sekali pembawaannya pas ngobrol",
                "pesan": "Semangattt kaa Zannuba untuk kuliahnyaa!"
            }
            ]
            display_images_with_data(gambar_urls_Divisi_Visual_Design, data_list_Divisi_Visual_Design)
    medkraf()