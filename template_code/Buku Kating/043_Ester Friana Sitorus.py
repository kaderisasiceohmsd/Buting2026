import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');

    /* Global Styling - Background Krim dengan Grafik Multi-Layer Bertumpuk */
    .stApp {
        background-color: #fbf9f5;
        background-image: 
            radial-gradient(rgba(181, 142, 75, 0.28) 1.5px, transparent 1.5px), 
            radial-gradient(rgba(92, 64, 51, 0.15) 1.5px, #fbf9f5 1.5px),
            linear-gradient(45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(181, 142, 75, 0.05) 25%, transparent 25%);
        background-size: 36px 36px, 36px 36px, 60px 60px, 60px 60px;
        background-position: 0 0, 18px 18px, 0 0, 30px 30px;
        background-attachment: fixed;
        color: #1e1b18;
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar disesuaikan warnanya agar senada, terang, dan rapi */
    [data-testid="stSidebar"] {
        background-color: #f0e8d5 !important;
        border-right: 2px solid rgba(181, 142, 75, 0.4);
    }
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
        color: #1e1b18 !important;
        font-weight: 500;
    }

    /* Gaya Kotak Profil / Konten di halaman person */
    .person-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.96) 0%, rgba(246, 240, 226, 0.96) 100%); 
        backdrop-filter: blur(8px);
        border: 2px solid #b58e4b; 
        outline: 2px dashed rgba(181, 142, 75, 0.4);
        outline-offset: -6px;
        padding: 26px; 
        border-radius: 20px; 
        box-shadow: 0 10px 30px rgba(181, 142, 75, 0.15); 
        color: #1e1b18;
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
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
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {
                "background-color": "#FCF0DA !important",
                "color": "#000000 !important",
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
    # CSS Murni untuk Efek Gulungan Kertas (Scroll) Otentik
    st.markdown(
        """
        <style>
        /* Kontainer Utama Gulungan */
        .scroll-wrapper {
            max-width: 420px;
            margin: 20px auto;
            position: relative;
            filter: drop-shadow(0px 8px 12px rgba(0, 0, 0, 0.35));
        }

        /* Roll Atas & Bawah (Batang Kayu/Kertas Gulung) */
        .scroll-roller {
            height: 26px;
            background: linear-gradient(90deg, #5c3818 0%, #8d5b2d 20%, #e0aa68 50%, #8d5b2d 80%, #5c3818 100%);
            border-radius: 13px;
            border: 2px solid #3d230d;
            box-shadow: inset 0 3px 5px rgba(255,255,255,0.3), inset 0 -3px 5px rgba(0,0,0,0.5);
            position: relative;
            z-index: 2;
        }

        /* Badan Kertas Kuno */
        .scroll-body {
            background: #f4e3b1;
            background: radial-gradient(circle, #f9edd1 0%, #e8d08d 85%, #d1b164 100%);
            border-left: 3px dashed #b89547;
            border-right: 3px dashed #b89547;
            padding: 25px 30px;
            box-shadow: inset 0 0 25px rgba(115, 77, 20, 0.45);
            margin: -6px 12px; /* Menyelip halus di antara roller */
            position: relative;
            z-index: 1;
        }

        /* Gaya Teks di Dalam Kertas */
        .scroll-body p {
            color: #3d220a !important;
            font-family: 'Georgia', serif;
            font-size: 0.95em;
            line-height: 1.6;
            margin-bottom: 8px;
            border-bottom: 1px dashed rgba(140, 90, 30, 0.25);
            padding-bottom: 4px;
        }

        .scroll-body p:last-child {
            border-bottom: none;
        }

        /* Merapikan ekspander Streamlit */
        div[data-testid="stExpander"] {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

            if i < len(data_list):
                with st.expander(f"📜 Buka Biodata: {data_list[i]['nama']}"):
                    st.markdown(
                        f"""
                        <div class="scroll-wrapper">
                            <div class="scroll-roller"></div>
                            <div class="scroll-body">
                                <p><b>Nama:</b> {data_list[i]['nama']}</p>
                                <p><b>NIM:</b> {data_list[i]['nim']}</p>
                                <p><b>Umur:</b> {data_list[i]['umur']}</p>
                                <p><b>Asal:</b> {data_list[i]['asal']}</p>
                                <p><b>Alamat:</b> {data_list[i]['alamat']}</p>
                                <p><b>Hobbi:</b> {data_list[i]['hobbi']}</p>
                                <p><b>Sosmed:</b> {data_list[i]['sosmed']}</p>
                                <p><b>Kesan:</b> {data_list[i]['kesan']}</p>
                                <p><b>Pesan:</b> {data_list[i]['pesan']}</p>
                            </div>
                            <div class="scroll-roller"></div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    st.write("Semua gambar telah dimuat!")
    
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUBAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PPqcqT5Fuw-UdYji_m7JK3X9NqHaLdD0",
            "https://drive.google.com/uc?export=view&id=1KuSZTs7KvIC7SmxjKggXuPr0qU9UeSYF",
            "https://drive.google.com/uc?export=view&id=12VgN5JGWlnpGhfYZXd5QaTjg6a2zqVrZ",
            "https://drive.google.com/uc?export=view&id=1NsUs9Blri5FHJ9xUAw_TpDMiTaGIfnpc",
            "https://drive.google.com/uc?export=view&id=1nrzqiP2azCdLD5UBHwJo0BIGBeCOIixK",
            "https://drive.google.com/uc?export=view&id=1ctm4Itv2IqQb95hRrw6DO0ejG_-pqhLE",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung ",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Push Rank",
                "sosmed": "@jars_mrp",
                "kesan": "bang fajar orangnya baikk,ramah, bijaksana, tegas, pokok the best dah abngnya",  
                "pesan":" Semoga kedepanya makin gacor lagi bangg, makin sukses did unia kerja"
            },
            {
                "nama": "Muhammad Aqil Ramadhan ",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bakinang",
                "alamat": "Sekretariat HMSD ",
                "hobbi": "Zikir",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bangg aqill oranggnya baik banget , asikk diajak ngobroll, orangnya bijaksana juga",  
                "pesan":"sukses selalu bang , kedepannya semua aktivitas lancar, perkuliahan juga lancar "
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eefidefiyati",
                "kesan": "Kak Efi orangnya rapi, teratur, dan cekatan banget dalam mengurus berbagai hal. Kagum juga lihat cara Kak Efi mengerjakan sesuatu..",  
                "pesan":"Terima kasih sudah membagikan contoh kerja yang baik buat kami, Kak. Semoga dilancarkan urusan magang dan skripsinya"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Kak Qois orangnya asik dan enak diajak ngobrol",  
                "pesan":"Semangat terus kuliahnya, Kak. Semoga semua urusan ke depannya lancar dan cepat sampai di tujuan !!!"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Melukis",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kak Hafsa orangnya baik dan ramah. Asik juga kalau diajak ngobrol, jadi senang bisa kenal sama Kak Hafsa.",  
                "pesan":"Semangat terus kuliahnya, Kak. Semoga semua urusannya dilancarkan dan sukses terus ke depannya."
            },
            {
                "nama": "Luthfia Laila Ramadhani ",
                "nim": "123450004",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Nyari motor Pak Tirta ",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "awalnya kukira kakaknya judes , krena mukanya judes gtu, ternyata baikk bangetttt , ramah juugaaa.",  
                "pesan":" Semangat terus kuliahnya, Kak. Semoga magang, skripsi, dan semua urusannya dilancarkan sampai selesai."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# BADAN KESENATORAN
if menu == "Senator":
    def Senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-X8hYDumZuMDUZUdu5iN5T4F_2Vd1O2P",
            "https://drive.google.com/uc?export=view&id=1Xo4eO98Ao_LnGjUgAYImJswbYdBkt5Uk",
            "https://drive.google.com/uc?export=view&id=1LIsvEPxNBnyaIP9hzcj4uTEcttwaYCoI",
            "https://drive.google.com/uc?export=view&id=1nGfKlRosFmVFELKk_MPZg1IIXRlZr9YJ",
            "https://drive.google.com/uc?export=view&id=1REoPHNZECgoKPxQcLELTDwFefECzLTWT",
            "https://drive.google.com/uc?export=view&id=1D5E4G7s60xQPDvsBwa3oVlFlj8h-yrk4",
            "https://drive.google.com/uc?export=view&id=1FvVcn5NyIG_WNqClW6OH1ST5Q-fdOMCy",
            "https://drive.google.com/uc?export=view&id=1IGLs6u1lTCqvlNaxiI5Jyylf_vXU6ahl",
            "https://drive.google.com/uc?export=view&id=1siNOmJ6qzxP1r8SwRvj6IjgmuDUusJQd",
            "https://drive.google.com/uc?export=view&id=1QChZyQQG31Bqy26IhP1hDz0IbXrIN1Rn",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kakak ziza sosok alpha woman yang aku lihatt, gacor, kerennn , panutan dah kak ziza",  
                "pesan":"Tetap semangat ya Kak ngejalanin kuliah sama kegiatan lainnya. Semoga makin banyak hal keren yang bisa dicapai ke depannya !!!"
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal": "Jakarta ",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen kiri",
                "sosmed": "@helmy_inst",
                "kesan": "bang helmy sangat sangat asikk , kukkira awalnya abangnya sombongh, ternyata se asikk ituu lohh dan sebaik ituu",  
                "pesan":"Semangat terus bg buat kuliah dan segala kesibukannya. Semoga nanti jalan setelah lulusnya juga mulus dan sesuai yang diharapkan. !!!"
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Belwis",
                "hobbi": "Nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kak lia orangnya kalem dan baik. Pembawaannya juga bikin nyaman kalau lagi ngobrol",  
                "pesan":" Semoga apa pun yang sedang Kakak usahakan sekarang nantinya berbuah hasil yang bikin bangga!!!"
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "Kak nadya cantii bngett, mukany manis , imutt, dan juga kakaknya asikkk dan seruu",  
                "pesan":"Semoga apa pun yang sedang Kak Nadya usahakan sekarang nantinya berbuah hasil yang bikin bangga"
            },
            {
                "nama": "Fernando Diemtrius Barus",
                "nim": "124450063",
                "umur": "21",
                "asal": "Tangerang Kota",
                "alamat": "Sebelah kamar biwa",
                "hobbi": "Badminton",
                "sosmed": "@barus.fernando",
                "kesan": "abangnya asikk banget apalgi kalau diajka ngobrol selalu nyambung dan seruu",  
                "pesan":"Semangat terus sampai garis finish, bang fer! Semoga skripsinya nanti nggak banyak drama dan bisa lulus sesuai target wkwk"
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal": "Jakarta",
                "alamat": "Kotabaru",
                "hobbi": "Mancing",
                "sosmed": "@sciia__",
                "kesan": " Kak Suci, mentor terbaik sekaligus mentor tersayangnya Cosval 🥹🤍 Maminya Cosval yang selalu berusaha ada buat anak-anaknya. Bahkan ketika Kak Suci sendiri lagi capek, Kakak tetap nyempetin buat dengerin cerita, keluh kesah, dan nemenin kami. Rasanya beruntung banget bisa punya mentor yang nggak cuma membimbing, tapi juga benar-benar membersamai kami. Pokoknya sayang banget sama Maminya Cosval satu ini ",  
                "pesan":"Semoga semua kebaikan, waktu, tenaga, dan perhatian yang Kak Suci kasih ke Cosval dibalas dengan hal-hal yang jauh lebih baik. Semoga kuliah, TA, dan semua urusan Kak Suci dimudahkan sampai selesai. Jangan lupa jaga diri dan jangan terlalu capek, kakak , walaupun dunia penuh denegan gedebag gedebugnya. Cosval sayang banget sama Maminya dan bersyukur pernah punya mentor sebaik Kak Suci. !"
            },
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal": "Nias Selatan",
                "alamat": "Asrama TB3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "bang Wielman orangnya asik dan santai, enak juga diajak ngobrol. , salut lihat abangnya , publick speakingnya sangat bagusss banget, pantesan selalu gacor kalau jadi mc",  
                "pesan":"Semangat terus kuliahnya, bang! Semoga semua urusannya lancar sampai lulus, dan ngemc nya bisa samapi masuk tv , Amin"
            },
            {
                "nama": "Aqila Zayyan SalsabiL",
                "nim": "124450014",
                "umur": "19",
                "asal": "Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Kakak aqila ,kating terasikkkk, tergokill, udalah cantik imutt, vibesnya itu lohh buat orang sekitarr semangat gtuu, yahh walaupun sedikit cerewet dan bawell , tapii jujurr kakanya asikk bangett dann enjoyyy banget",  
                "pesan":"Tetap jadi versi terbaik dari diri Kak Aqila ya. Semangat ngejar apa yang Kakak mau, kurangin bawelnya kak hehe !!!"
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal": "Lamtim Timur",
                "alamat": "Gunung Terang",
                "hobbi": "Giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "jujurr beda rambut beda vibes, pas rambut nya pendekk kayak cowok soft gtuu , tapi pas rambutnya panjang kayak muka antagonis gtuu, tapii aslinya sangat berbanding terbalik dengab mukanya, abangnya baik banget , dan asikk juga, apalagi pas jadi ketuplak scienfest abangnya sabar banget ternyata",  
                "pesan":"Tetap jadi orang baikk , dan bermaanfaat bagii lingkungan yah bang, semangat kuliahnya!"
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal": "Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftrnii",
                "kesan": "Kak Dwi kelihatannya kalem, tapi kalau udah ngobrol ternyata asik juga orangnya",  
                "pesan":"Semoga tetap punya waktu buat hal-hal yang Kakak suka di tengah kesibukan kuliah !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Senator()

if menu == "Baleg":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LJa9Pcrsh7STm7UV4dMY7RyF54eXXxsd",
            "https://drive.google.com/uc?export=view&id=1C_qrF-Mft6qDqs5-TPLpHitAN2BM3l3G",
            "https://drive.google.com/uc?export=view&id=1Pr6UmX0mVWu7QqjqpTLH7lIvJjTKcuGg",
            "https://drive.google.com/uc?export=view&id=1URW3jgN2cvJSx3PIdaqWhso1eYRGlAVr",
            "https://drive.google.com/uc?export=view&id=1N5vwKA77C3U68QtPA6PMfTpico_vBWh1",
            "https://drive.google.com/uc?export=view&id=1MCvmGAnPAaPKrR8u4nbNfHXl2ebfGaRI",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Zw46RMkQHAwdvAtl4vsLAWco0pS-80Aw",
            "https://drive.google.com/uc?export=view&id=1GeN_I8H0YHDNjxp4XqW8mhI7KtE3gsvQ",
            "https://drive.google.com/uc?export=view&id=1eu9Pt4Ad8RIj6HhTgMKMlpYgpP0IR2jR",
            "https://drive.google.com/uc?export=view&id=1Ulnf0K4Vu-dsxR74s4V9ivZdzjIlCtbg",
            "https://drive.google.com/uc?export=view&id=1EjfPBXYoT_XwyTvsDuHvu8Wam2YIcUBK",
            "https://drive.google.com/uc?export=view&id=1S0rJNgnIg1UWwXffqKApTGxURXlUe0wt",
        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450066",
                "umur": "20",
                "asal": "Kuala Lumpur",
                "alamat": "GH",
                "hobbi": "Wawancara",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho keren sih, orangnya ramah, bijaksana, dan vibes pengayomnya dapet banget",
                "pesan": "Sehat-sehat terus, Bang! Semoga kuliah dan semua langkah setelah ini lancar , Pulang ke kula lumpur harus udah jadi orang sukses "
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Pelangi",
                "alamat": "Singkawang",
                "hobbi": "Dengerin lagu zona merah dari Kunto Aji",
                "sosmed": "@j__eesie",
                "kesan": "kak jue orangnya sangat cantik, ramah , imut, baik , aktif bangett , asik banget loh sm kakanya ngobrol ",
                "pesan": "Tetap jadi Kak Jue yang ceria dan sabar yaa. Semoga ke depannya makin banyak hal baik yang datang!"
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Makan mie gomak",
                "sosmed": "@exvoltas & @ddharu",
                "kesan": "Bang Dharu orang keren di sains data, udah lah pintar, bijak, imaprtes ikut kkn kebangsaan , wow kurang gacor apalagi coba dengann semua pencapainya",
                "pesan": " Semoga terus jadi inspirasi buat adik tingkat, Bang. Ditunggu pencapaian-pencapaian berikutnya, dan kmai adik tingkat  bis amengikuti jejak dari abang"
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "bang Givaro orangnya asik dan seru. Ngobrol sama abangnya juga nyaman, nggak bikin canggung.",
                "pesan": "Semoga kuliahnya nggak bikin pusing terus wkwk. Tetap semangat bang"
            },
                        {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal": "Jakarta Barat",
                "alamat": "Kotabaru",
                "hobbi": "Lari",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica asik, baik, dan pintarr banget. Pokoknya seru ",
                "pesan": " Jangan pernah berhenti ngejar hal-hal yang Kak Monica mau. Semoga ke depannya makin banyak pencapaian keren !!!"
            },
            {
                "nama": "GH Mikael Niko A S",
                "nim": "124450079",
                "umur": "20",
                "asal": "Pasir Sakti",
                "alamat": "Jati Agung",
                "hobbi": "Tidur",
                "sosmed": "@me._kael",
                "kesan": "bang niko awalnya kukira orangnya cuek, ternyata aslinya enggak , asik banget ternyataa,gak pelit ilmu dan baik",
                "pesan": "Sehat terus, Bang! Semoga semua urusannya dipermudah dan makin banyak hal seru ke depannya.o"
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "124450015",
                "umur": "19",
                "asal": "Bekasi",
                "alamat": "Kedaton",
                "hobbi": "Mancing",
                "sosmed": "@syt.rifa",
                "kesan": " Kak Siti orangnya baik .",
                "pesan": "Semangat dan sukses selalu  kak."
            },
            {
                "nama": "Afghanis Nursholehatunisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Kepulauan Mentawai",
                "alamat": "Kadang di kost putri kadang di kost sekar",
                "hobbi": "Memanjat",
                "sosmed": "@afghanisnt_",
                "kesan": "Kak nisa orangnya asikk banget, dan baik banget, kakkanya sabar banget apalgi pas ngajarin metnum anak rc ,sabar bangett ditengah keributan anak rc, gakpelit ilmu lagi ",
                "pesan": "semoga kebaikan kakak selama ini dibalasa dengan orang-orang baik dii sekeliling kakak, kuliahnya lancarrr, kkn, dll nya lancar!!!"
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "City earth",
                "alamat": "Sukarame",
                "hobbi": "Baca AU",
                "sosmed": "@haniqurratuain_",
                "kesan": "Kak Hani orangnya cantik, imut, soft banget. Vibes-nya juga lembut dan bikin gemas",
                "pesan": "Tetap jadi Kak Hani yang soft dan baik yaa. Semoga selalu ketemu hal-hal yang bikin bahagi!!!"
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Teluk Betung",
                "hobbi": "Nyanyi, olahraga",
                "sosmed": "jeremia_hm",
                "kesan": "bang Jeremia baik, pintar, dan asik banget orangnya. Enak juga kalau diajak ngobrol atau diskusi",
                "pesan": "Semoga semua yang bang Jeremia rencanain bisa berjalan sesuai harapan. Tetap rendah hati dan terus berkembang ya, bang"
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Nge-gym, koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "bang Jona baik banget dan nggak pernah pelit ilmu. Kalau ada yang butuh bantuan, bang Jona selalu mau nolong dan gak pernah nolakk, the best deh abangnya",
                "pesan": " Semoga semua kebaikan bg Jona balik dalam bentuk yang lebih baik lagi. Tetap jadi orang baik yang suka bantu orang lain ya bg"
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Melukis",
                "sosmed": "@sekardnwp",
                "kesan": "Awalnya kirain Kak Sekar judes  ternyata aslinya baik banget dan jauh dari kesan judesnya",
                "pesan": "Tetap jadi Kak Sekar yang baik dan jangan berubah yaa. Semoga semua urusan Kakak ke depannya dimudahkan"
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshaysk",
                "kesan": "Kak Nashwa mukanya Korea banget  vibes-nya juga cakep dan unik. Orangnya juga baik",
                "pesan": " Semoga selalu happy dan dikelilingi orang-orang baik. Jangan lupa tetap semangat sampai lulus, Kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list) 
    Baleg()
        

if menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ke1_l-TR_GmbPsVGhSZRCybSMYUfgmZ6",
            "https://drive.google.com/uc?export=view&id=13ohDk-KFRvkFcqQQFxQFN6rS7HtudLlm",
            "https://drive.google.com/uc?export=view&id=1FUBkV5qi6LSQxLwiKSxguwqr4yVWqbKi",
            "https://drive.google.com/uc?export=view&id=17IT0FeSaD1m_nJ78wTq05FEslxrsdJe1",
            "https://drive.google.com/uc?export=view&id=11tvLQ6Vf3VUu2PrqwY5gUHZS-p-f9GrI",
            "https://drive.google.com/uc?export=view&id=11ZFMOnCkxUqrRDrhaR2HZsjn-hSVyvKg",
            "https://drive.google.com/uc?export=view&id=16Z2-PBr_Em_bJq3OaxESV2wZFRCnbgqp",
            "https://drive.google.com/uc?export=view&id=1xC3HYPY0NjjbrPhASRqermQ9xhC9jOCB",
            "https://drive.google.com/uc?export=view&id=1S6Zkl6sHQ_UnsBRk2EtnL4G30mwIMtxd",
            "https://drive.google.com/uc?export=view&id=1wAT6F2f_X_1W9N10m5ucRKol6XXW4fs2",
            "https://drive.google.com/uc?export=view&id=1G47WmvJyGCUoSfrY780Fq5H89ZZFhqkA",
            "https://drive.google.com/uc?export=view&id=1YDIZZy_sYtco9GeVg8XJ3IyM-FU66cZl",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf ",
                "nim": "123450110",
                "umur": "21",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis ",
                "hobbi": "Jualan",
                "sosmed": "@ihsan.myusuf",
                "kesan": "Bang Ihsan orangnya baik, humoris, bijak, dan keren deh pokoknya. Kalau ngobrol sama Bang Ihsan juga ser", 
                "pesan":" Tetap jadi Bang Ihsan yang seru dan bijak ya, Bang. Semoga makin sukses dan makin gacor ke depannya!"
            },
            {
                "nama": "Hanifah Inaya Sani",
                "nim": "123450123",
                "umur": "20",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kak Hanifa baik bangett dan punya pembawaan yang tegas. Tipe cewek yang kelihatan punya pendirian banget",  
                "pesan":"Tetap jadi perempuan yang kuat dan tegas ya, Kak. Semoga semua yang Kakak perjuangin bisa tercapai !!!"
            },
            {
                "nama": "Afifah Fauziah ",
                "nim": "123450002",
                "umur": "20",
                "asal":"Bandung ",
                "alamat": "Airan",
                "hobbi": "Nonton marvel",
                "sosmed": "@fifah.zy",
                "kesan": "Kak Afifah orangnya baik dan ramah banget. Pembawaannya juga nyaman kalau diajak ngobrol",  
                "pesan":"moga selalu dikelilingi orang-orang baik dan banyak hal menyenangkan ke depannya, Kak!!!"
            },
            {
                "nama": "Anadia Carana ",
                "nim": "123450019",
                "umur": "21",
                "asal":"Palembang ",
                "alamat": "Way Huwi ",
                "hobbi": "Nyari duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kak Anadia keren banget sih. Agak tomboy, tapi tomboy yang keren dan punya vibes wanita pemimpin gitu",  
                "pesan":"Tetap jadi perempuan yang berani dan punya pendirian ya, Kak. Semoga makin banyak hal besar yang bisa dicapai !!!"
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450013",
                "umur": "25",
                "asal":"Lampung Tengah ",
                "alamat": "Sebelah kostan Ayake",
                "hobbi": "Nonton YouTube ",
                "sosmed": "@hasan.ramdhan08",
                "kesan": "Bang Hasan baik banget, tapi jujur pas pertama lihat agak keinget Bang Jona karena mukanya mirip wkwk",  
                "pesan":"sehat-sehat terus ya, Bang. Semoga semua urusannya dipermudah dan makin sukses"
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19",
                "asal":"Bandar Lampung ",
                "alamat": "Bandar Lampung ",
                "hobbi": "Nonton dracin ",
                "sosmed": "@lay.inr_",
                "kesan": "Kak Layina orangnya baik, imut, dan cute banget mukanya ",  
                "pesan":"Tetap jadi Kak Layina yang lucu dan baik yaa. Semoga hari-harinya selalu dipenuhi hal-hal yang bikin happy!"
            },
            {
                "nama": "Mochammad Iqbal Az-zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Nonton drakor ",
                "sosmed": "@iqbalazzahir_",
                "kesan": "Kak Iqbal orangnya baik banget dan kelihatan humble.",  
                "pesan":"Semoga selalu dimudahkan dalam setiap urusannya, Kak. Semangat terus sampai selesai!"
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Pemda",
                "hobbi": "Nonton",
                "sosmed": "@talljtine_",
                "kesan": "Kak Talitha ramahhh dan baik banget. Senang bisa kenal sama Kak Talitha",  
                "pesan":"Semoga selalu ketemu hal-hal baik di setiap langkahnya, Kak. Jangan lupa bahagiaa"
            },
            {
                "nama": "Abdilah Fikri Alpome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Baturaja, Sumatera Selatan ",
                "alamat": "Airan ",
                "hobbi": "Basket ",
                "sosmed": "@pomest__",
                "kesan": "Bang pome gacor banget abangnya wkwk. Pokoknya keren dan asik",  
                "pesan":"Tetap gacor terus ya, Bang! Semoga apa pun yang dikejar bisa dapet dan makin jauh melangkah!!!"
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumatera Barat ",
                "alamat": "Belwis",
                "hobbi": "Fishing",
                "sosmed": "@dhalsetiawan",
                "kesan": " bang Afdhal orangnya baik dan asik. Enak juga kalau diajak ngobrol, nggak bikin canggung",  
                "pesan":"Semoga selalu diberi kelancaran dalam setiap urusan dan tetap jadi orang yang asik "
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara ",
                "alamat": "Belwis ",
                "hobbi": "Nonton kartun ",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kak Anggun baik banget dan suka tetringin orang kalau lagi jualan  wkwk. Tapi seru sih a",  
                "pesan":"Semoga jualannya makin laris, Kak. Tetap jadi Kak Anggun yang seru!"
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "18",
                "asal":"Lampung Timur ",
                "alamat": "Margo Lestari  ",
                "hobbi": "Lagi gak punya hobi ",
                "sosmed": "@dellaansaftr",
                "kesan": "Kak Della asik banget sih orangnya, terus cantik juga Senang bisa kenal sama Kak Della",  
                "pesan":"Semoga selalu happy dan makin banyak hal baik yang datang. Tetap jadi Kak Della yang asik yaa!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

if menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1SPQd9vWUKqwiWhwDqvx69w47P010twc6",
            "https://drive.google.com/uc?export=view&id=1mwIApe4wkWweyiWvKOWCDPUp72b36-As",
            "https://drive.google.com/uc?export=view&id=18nx2GCXcFanOSXLRI5gYdPgV3gpZe6q3",
            "https://drive.google.com/uc?export=view&id=1eHb5tRGvTf4HHVg3wxgA_F1tQA3FvsRf",
            "https://drive.google.com/uc?export=view&id=1wHWD-je-cAKXoFFQqt_dABzBArritBkv",
            "https://drive.google.com/uc?export=view&id=15Wh17DegZI_4PGjKm2Jga7v8rSGOKOV4",
            "https://drive.google.com/uc?export=view&id=1brLs5TTR7nGARg72c_N_Bk8PoZZTpTRp",
            "https://drive.google.com/uc?export=view&id=1dSp7aOiCkAJF4k642DXIfSP8XZ5eB2uz",
            "https://drive.google.com/uc?export=view&id=1SApa2gnuiG9x9VXiV3Ln4UcpFa-8qUDe",
            "https://drive.google.com/uc?export=view&id=1-uVRtD5i5BYfQ24mBMpMmNVsoBkehiYP",
            "https://drive.google.com/uc?export=view&id=1TGDP564uIMUeebzGo-BokVX4d0EomsyA",
            "https://drive.google.com/uc?export=view&id=1B0Dq0A9rm90QlZscsMWz6gxhKUmHmIEw",
            "https://drive.google.com/uc?export=view&id=1-72V15pt7xq9USTdIFyT9MAS5kzYDp6F",
            "https://drive.google.com/uc?export=view&id=1QyCDr0TZG__zgjE6TQQfjeSEbbPUrzN9",
            "https://drive.google.com/uc?export=view&id=1bm3_7WsnyZG6nCbmgKBLrZNA5C5N07rk",
            "https://drive.google.com/uc?export=view&id=1ILZerOz3dfXswKdrXY9Wbjdj1OqjKg8A",
        ]
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "123450106",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Way Halim",
                "hobbi": "Ngeledek Orang",
                "sosmed": "@haikalsbln",
                "kesan": "Awalnya liat muka Bang Haikal kirain galak sama emosian, ternyata sabar banget, asik, suka bercanda, tapi kalau udah serius beda cerita ",
                "pesan": "Semoga makin gacor terus ya Bang, sukses di mana pun nantinya."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "Untung Senopati",
                "hobbi": "Suka nolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Awalnya kirain Kak Risma jutek  ternyata aslinya baik banget dan ramah.a",
                "pesan": "Semangat terus kuliahnya Kak, semoga semuanya lancar"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal": "Sumatra Utara, Kisaran City",
                "alamat": "Sukarame",
                "hobbi": "Ngabarin orang tua",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kak Hanna pembawaannya ceria banget, vibes positifnya juga kerasa terus, pokoknya baik dan asikk",
                "pesan": "Tetap bawa energi positifnya ke mana pun ya, Kak. Semoga kuliah dan semua urusannya selalu dilancarkan.!"
            },
            {
                "nama": "Muhammad Hanif Dzaky",
                "nim": "124450064",
                "umur": "21",
                "asal": "Padang Sumbar",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngedistro",
                "sosmed": "@hnfdzky_",
                "kesan": "bang Hanif orangnya baik banget dan gemoy. Pembawaannya juga asik",
                "pesan": " Semoga selalu diberi kelancaran dalam kuliah dan semua kegiatannya.!"
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Balap Liar",
                "sosmed": "@farhanghani",
                "kesan": "bang Farhan keren sih, baik juga. Awalnya kirain sombong, ternyata ramah banget",
                "pesan": "Semoga ke depannya makin banyak hal keren yang bisa dicapai. Sukses terus buat kuliah dan semua urusannya"
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngeliatin orang",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kak Aisyah orangnya baik, asik, dan ramah. Pembawaannya juga nyaman.",
                "pesan": "Semoga selalu dikelilingi orang-orang baik dan ketemu banyak hal seru ke depannya !!!"
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Balap liar",
                "sosmed": "@cerine_ipynb",
                "kesan": "Kak Cerine , kakakku tersayang. Baik banget, cantik, pengertian, dan selalu bikin nyaman. Pokoknya lopyouu buat Kak Cerine",
                "pesan": "Tetap jadi Kak Cerine yang baik dan pengertian ya. Semoga semua yang lagi diperjuangin berjalan lancar dan selalu bahagi!"
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Berkebun dan membuat lagu",
                "sosmed": "@jay.saputratmb",
                "kesan": "Awal ketemu Bang Jaya kirain cuek dan bodo amat, ternyata aslinya baik banget, ramah, dan asik. Suka bercanda juga ternyata",
                "pesan": "Tetap jadi Bang Jaya yang seru dan ramah ya. Semoga semua urusan ke depannya lancar !!!"
            },
            {
                "nama": "Najla Nur Syifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Aceh",
                "alamat": "Belwis",
                "hobbi": "Gangguin cika",
                "sosmed": "@njlanursyifa",
                "kesan": "Kak Najla tuh imut, lucu, cantik, dan baik bangeta",
                "pesan": "Semoga selalu ketemu hal-hal baik dan orang-orang baik juga.!"
            },
            {
                "nama": "Rozaq Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal": "Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Isengin harvin di kelas",
                "sosmed": "@rozaqramdani__",
                "kesan": "Bang Rozaq orangnya baik dan ramah.",
                "pesan": "Semoga kuliah dan semua kesibukannya dilancarkan. Sukses terus ya, Bang!"
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@christiani8872",
                "kesan": "Kak Teresa orangnya asik dan baik banget. Pokoknya salah satu kakak yang seru buat diajak ngobrol",
                "pesan": "Semoga lancar dan sukses terus perkuliahan serta kegiatannya!"
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Main ke air terjun",
                "sosmed": "@audinaf_03",
                "kesan": " Kak Audina, imut, lucu, tapi ternyata keren juga. Pembawaannya juga asik kalau diajak ngobrol",
                "pesan": "Semoga kuliahnya lancar dan makin banyak hal keren yang bisa dicapai. Sukses terus ya, Kak!"
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Terlambat",
                "sosmed": "@cikamrbn",
                "kesan": "Kak Cika orangnya baik banget, walaupun awalnya keliatan agak introvert. Tapi kalau udah kenal ternyata asik jugaa",
                "pesan": "Tetap jadi Kak Cika yang baik dan apa adanya ya. Semoga semua urusannya dipermudah dan kuliahnya lanca!"
            },
            {
                "nama": "Gustin Haleluya Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Toba Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Kak Gustin cakep banget dan orangnya juga baik.",
                "pesan": "Semoga selalu dikelilingi hal-hal baik dan orang-orang yang sayang sama Kakak.!"
            },
            {
                "nama": "Muhammad Arvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Nembak Burung",
                "sosmed": "@muhvinz_",
                "kesan": "Bang Arvin orangnya lucu, asik, dan baik banget",
                "pesan": "Semoga kuliah dan semua kesibukannya lancar terus!"
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Cari duit",
                "sosmed": "@snasaa._",
                "kesan": "Kak Rafa orangnya baik, ramah, dan asik.",
                "pesan": "Semoga kuliahnya lancar dan semua yang lagi dikejar bisa tercapai. Sukses terus ya, Ka!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

if menu == "Departemen Medkraf":
    def Departemen_Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sKwrdtZBm1Zj2n83XxULf22he0pCahEK",
            "https://drive.google.com/uc?export=view&id=1ZotL_pGsxSFdqqoAWhtT6NXcJePaEsny",
            "https://drive.google.com/uc?export=view&id=1N-tR5xogIV0KjxD87PhW9mDEgqMO3z6n",
            "https://drive.google.com/uc?export=view&id=1daJpnhjNXHjPHcRUiH-8bRLYzaTI27Xt",
            "https://drive.google.com/uc?export=view&id=1zaRAoIB9roSmRdD3FPUwOuPY2m4oiduu",
            "https://drive.google.com/uc?export=view&id=18FpoB_8C-SDHkZIH7Y_5Zanftc50s36t",
            "https://drive.google.com/uc?export=view&id=1lGXWJsE0xw6K00Qod9L6HUcJPirYv_2q",
            "https://drive.google.com/uc?export=view&id=1IXSYzwFBPnYlkI1sNs7_PqQ0pY3wfjU2",
            "https://drive.google.com/uc?export=view&id=1N9bguPVZ-qU3wZm46ss5DwiakyM3ZxAU",
            "https://drive.google.com/uc?export=view&id=1B0X5yPASwn21hjEIIFaXCLP1tbmNy06-",
            "https://drive.google.com/uc?export=view&id=19YieApI7AunNb7mKUzbxUAX8fQksrX_a",
            "https://drive.google.com/uc?export=view&id=1G8NMZgu9QXOLUSPfcaWVJCjMrAdcpFXT",
            "https://drive.google.com/uc?export=view&id=1RNqB4fC2jfS30CN-KNMlNSbB69jTgEZr",
            "https://drive.google.com/uc?export=view&id=1DZUEpO0ddYrZwQUocOpgdM3E7mDGxFtZ",
            "https://drive.google.com/uc?export=view&id=1LF3pW6y5p6gzTy5bcM1ZOuB282NDatrA",
            "https://drive.google.com/uc?export=view&id=11CEu1OQC3lvnZPZoE-qTbYzw-GS06yi9",
            "https://drive.google.com/uc?export=view&id=1NFtgKARaKIHBl7R_A-eBakM2uKDY2_3t",
            "https://drive.google.com/uc?export=view&id=1Bv4_KfMe7FkmUhwdM-NnZE47-3KwSGQV",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh, Sumatera Barat ",
                "alamat": "Way Huwi, Jati Agung, Lampung Selatan",
                "hobbi": "Mendengarkan Musik",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "Kak Nayla orangnya asik dan baik bangettt. Enak juga kalau diajak ngobrol, nggak bikin canggung",  
                "pesan":"Semoga hari-hari Kak Nayla ke depannya dipenuhi hal-hal baik dan menyenangkan. Semangat terus ya Kak!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Listening to music",
                "sosmed": "@donnamaya.p",
                "kesan": "Kak Donna baik banget, terus nggak pelit ilmu sama sekali. Apalagi pas ngajarin LMD di kelas RC, sabarnya sabar banget",  
                "pesan":"Makasih banyak ya Kak udah sabar ngajarin . Semoga semua urusan Kak Donna dilancarin terus!!"# 1
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Medan, Palembang, Jakpus",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@noerruuu",
                "kesan": "Bang Labo tuh seru banget orangnya,  Abangnya asik juga",  
                "pesan":"Semoga makin gacor ke depannya Bang, kuliahnya dilancarin!!"# 1
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan raya",
                "hobbi": "nonton netflix",
                "sosmed": "@saniayyllstr",
                "kesan": "ak Sania cantik banget, terus orangnya juga baik. Vibes-nya tuh kalem.",  
                "pesan":"Semoga hari-hari Kak Sania ke depannya selalu dipertemukan sama hal-hal baik!"# 1
            },
            {
                "nama": "Raihana Adelia putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis, Membaca",
                "sosmed": "@n1tg._",
                "kesan": "awalnyua aku kira judes gtu Ternyata pas udah kenal malah baik banget wkwk.",  
                "pesan":"Semoga makin sukses terus Kak dan selalu ketemu orang-orang yang baik juga!"# 1
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton",
                "sosmed": "@anshtsyaaql",
                "kesan": "Kak Anash cantik + imut banget sih 😭 Vibes-nya tuh gemesin",  
                "pesan":"tap jadi Kak Anash yang baik. Semoga selalu happy dan banyak hal baik yang dateng!"# 1
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450104",
                "umur": "19",
                "asal":"Lampung Timur",
                "alamat": "kota baru",
                "hobbi": "Gangguin Anash&Razan, jail di grup",
                "sosmed": "@felisyanbl__",
                "kesan": "Kak Felisya tuh babyface banget  mukanya nggak sesuai ekspektasi umur wkwk. Tapi orangnya juga asik.",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Razan Maulana",
                "nim": "124450031",
                "umur": "21",
                "asal":"Jawa Barat",
                "alamat": "Korpri",
                "hobbi": "Poto orang",
                "sosmed": "@muh_razan_",
                "kesan": " Bang Razan tuh baik dan asik banget",  
                "pesan":": Semangat terus Bang ngejalanin kuliahnya. Semoga satu-satu yang diinginin bisa kejadian!"# 1
            },
            {    
                "nama": "Allisha",
                "nim": "124450019",
                "umur": "16",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kak Allisha tuh ramah banget, jadi ketemu sekali aja rasanya udah nggak terlalu canggung. Friendly dan cantik juga",  
                "pesan":"Tetap seramah itu ya Kak! Semoga semua kegiatan dan urusannya selalu aman lancar sentosa!"# 1
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan jalan",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kak Alya cantik dan baik banget. Orangnya juga punya vibes yang bikin nyamana",  
                "pesan":"Semoga makin banyak hal baik yang datang ke Kak Alya!!"# 1
            },
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Lampung Selatan ",
                "hobbi": "Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kak Bunga tuh cantik dan asik. Kalau ketemu vibes-nya nggak kaku.",  
                "pesan":"Kak Bunga tuh cantik dan asik. Kalau ketemu vibes-nya nggak kaku, jadi enak aja gitu buat ngobro!"# 1
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Airan Raya",
                "hobbi": "Membaca Al-Qur'an",
                "sosmed": "@difanyhsa_",
                "kesan": "Kak Difa ini literally kakak NIM gue yang sangat baik ,funfacknya sebelum verbek  kenalan dari TikTok , ternyat bis ajadi kakak nim aku, dan aslina bisa seasik itu. Sekarang malah sering jadi tempat aku minta saran",  
                "pesan":"Makasih ya Kak udah sering mau kasih saran . Semoga Kak Difa juga selalu dikelilingi orang-orang yang baik!"# 1
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "berenang",
                "sosmed": "@nzlhauly_",
                "kesan": "Kak Nazlah tuh imut banget, terus vibes-nya pendiam dan kalem gitu. ",  
                "pesan":"Semoga selalu nyaman jadi diri sendiri ya Kak. Lancar terus kuliahnya dan jangan lupa have fun juga!"# 1
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "Sukarame",
                "hobbi": "Dangir",
                "sosmed": "@daffascript",
                "kesan": "Bang Daffa baik banget sih. Pembawaannya juga santai,",  
                "pesan":"Semoga semua yang lagi Bang Daffa jalanin sekarang dipermudah, semoga hubungan sama kakak ku yang itu langengg ya bang!"# 1
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan ",
                "alamat": "Natar",
                "hobbi": "Nonton Anime",
                "sosmed": "@edsel_0712",
                "kesan": "Kakak ini baik dan ramah",  
                "pesan":"Semoga kuliahnya aman sampai garis finish Bang wkwk. !"# 1
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450085",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@luciarachel_",
                "kesan": "Kak Rachel cakep banget sih 😭 Tapi bukan cuma cakep, orangnya juga baik bangeta",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "124450124",
                "umur": "20",
                "asal":"Lampung Tengah",
                "alamat": "Perum Pemda",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@Melukis & Menulis",
                "kesan": "Kak Shafa tuh gemoy banget, ada vibes lucu yang bikin gampang gemesa",  
                "pesan":"Semoga kuliahnya lancar dan hidupnya selalu aman sentosa!"# 1
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "124450112",
                "umur": "18",
                "asal":"Lampung Timur",
                "alamat": "Rajabasa",
                "hobbi": "Bengong",
                "sosmed": "@xifasky",
                "kesan": "Kak Zannuba tuh orangg baik dan seru aja orangnya",  
                "pesan":"Pokoknya semangat terus ya Kak buat kuliah dan kegiatan-kegiatannya!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Medkraf()

if menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12-Z9etKXRDja92smN1O-SjruoB9WQVCF",
            "https://drive.google.com/uc?export=view&id=1qIyYE7X7FkJHQq73fs1efB90Oe-MrY_a",
            "https://drive.google.com/uc?export=view&id=1gIygg4iUlWA_znZ3SFHnGFrNjZ91-blT",
            "https://drive.google.com/uc?export=view&id=1lTWjHsDsdID_L4UAta7PIwGycDuAieMf",
            "https://drive.google.com/uc?export=view&id=1MW_IvudoUT3Vy483plgfsc9p3QBPSBDd",
            "https://drive.google.com/uc?export=view&id=16H8t3C1kUIt68XIdq2PCg4cm28ORP2Ww",
            "https://drive.google.com/uc?export=view&id=1mTO3cDcsZUyAsqsjuhZ-nEDDeGz-GlQs",
            "https://drive.google.com/uc?export=view&id=1O-kWmg1lapLBjuuxswJYXS1z89LXxlod",
            "https://drive.google.com/uc?export=view&id=1FvkuNb8JxMjAZr8jJT_6MSoGlsm8ZDYX",
            "https://drive.google.com/uc?export=view&id=1OBynPgnePXxFnZpQF71ssJYp2A-PRPvs",
            "https://drive.google.com/uc?export=view&id=1dTcQLNxY3U87vEfyQ1lnl3a8-pEbx6BD",
            "https://drive.google.com/uc?export=view&id=1aaH6KZnvPhG_2DTD76RODaAjarxuzFA2",
            "https://drive.google.com/uc?export=view&id=1kpnUvbQ2guuE6ZllQsiY-vvLEu6URf4s",
            "https://drive.google.com/uc?export=view&id=1kAxgdpsR5lLZwU8F1_rhtkYsdqR_3gK9",
            "https://drive.google.com/uc?export=view&id=1xUCnUZKbj6mAQOl0H0wbpJvbVcGZXue6",
            "https://drive.google.com/uc?export=view&id=1i7bEpVNbWWqwgUTaOM2kbW5Es0qAypGc",
            "https://drive.google.com/uc?export=view&id=1LckTEOPmpM4nPMvDd77YzFovHWiUNaRs",
            "https://drive.google.com/uc?export=view&id=1GV_4oz_YfgmnpOPCwfsoSG-NaU_FYinI",
            "https://drive.google.com/uc?export=view&id=1hhkRYt_wsH5nm6V52IF_zivk7mTBTYL5",
            "https://drive.google.com/uc?export=view&id=1kffHOiLdW9YPgp7PLZn0aO3lg0YuOXmS",
            "https://drive.google.com/uc?export=view&id=1HDhR1d-rtJTbMAshj0GlddnSNi9wCWYl",
            "https://drive.google.com/uc?export=view&id=1-Axzq3d-zQYWtJfmqFpbDyardCVCsgm9",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "-",
                "tanggal_lahir": "06 Maret 2005",
                "asal": "LAMPUNG!!!",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "Kak Arini baik banget, cantik juga. Terus menurutku Kak Arini tuh punya jiwa pemimpin yang kuat, tegas banget orangnya",
                "pesan": "Semoga Kak Arini selalu sukses dan tetap jadi sosok pemimpin yang keren ya Kak"
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20 Tahun",
                "tanggal_lahir": "5 November 2005",
                "asal": "Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@bylaash",
                "kesan": "Kak Nabyla baik, imut, cantik, terus nggak pelit ilmu. Apalagi pas ngajarin ALE semester 2, sabar banget ngajarin kita",
                "pesan": "Makasih banyak ya Kak udah mau ngajarin dan bantuin. Semoga Kakak sukses terus!"
            },
            {
                "nama": "Khoirul Muthoharoh",
                "nim": "123450021",
                "umur": "-",
                "tanggal_lahir": "27 Januari 2005",
                "asal": "Lambar",
                "alamat": "Airan",
                "hobbi": "main",
                "sosmed": "@khoirul_muthoharoh",
                "kesan": "Kak Mut tuh manis banget, orangnya juga baik dan asik. Terus jago main basket lagi. Kalau pas main basket seru banget kakaknya",
                "pesan": "Semoga makin keren lagi kakk, dan makin menyala!"
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "15 Tahun",
                "tanggal_lahir": "15 September 2004",
                "asal": "tetangga kadep",
                "alamat": "belwis",
                "hobbi": "memancing keributan",
                "sosmed": "@adityatfq",
                "kesan": "Pertama kali ketemu Bang Aditya pas PPLK, dan dari awal udah ramah banget ke kita yang masih mabai",
                "pesan": "Semoga tetap seramah itu ke siapa pun. Lancar terus kuliah dan semua urusannya ya Ban!"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21 Tahun ini alhamdulillah",
                "tanggal_lahir": "16 Agustus 2005",
                "asal": "Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky____",
                "kesan": "Bang Ahmad tuh bijak banget. Menurutku sosok pemimpin yang bagus, cerdik, kritis, dan peduli banget sama banyak hal. Gacor parah sihh apalagi yang berhubungan dengan politik, sangat dikritisin banget. Public speaking-nya juga keren, soosk contoh yang keren dah abangya.",
                "pesan": "Semoga pemikiran dan keberanian Bang Ahmad buat menyuarakan sesuatu bisa terus dibawa ke tempat yang lebih besar. Siapa tau nanti bisa jadi orang penting yang beneran punya pengaruh!"
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "cepuyuh tayun",
                "tanggal_lahir": "21 Desember 2005",
                "asal": "ikut kadep",
                "alamat": "love earth",
                "hobbi": "jadi idol",
                "sosmed": "@adindaadma",
                "kesan": "Kak Adinda cantik banget sih, mukanya tuh nggak bosenin sama sekali ",
                "pesan": "Semoga Kak Adinda selalu happy dan ketemu banyak hal baik. Pokoknya lancar terus buat semuanya ya Kak"
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "-",
                "tanggal_lahir": "23 Juli 2006",
                "asal": "Tanggamus",
                "alamat": "Balam",
                "hobbi": "lihat lihat perumahan",
                "sosmed": "@bimo_arkana",
                "kesan": "Bang Bimo tuh baik, asik, sama seru.",
                "pesan": "Semoga ke depannya abang makin sukses dan semua yang lagi dikerjain bisa berjalan lancar!"
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "124450006",
                "umur": "nelson piquet",
                "tanggal_lahir": "666",
                "asal": "balam",
                "alamat": "balam",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": " Bang Alfa asik banget orangnya, ramah dan baik juga",
                "pesan": "Semoga  selalu dikelilingi orang baik dan banyak hal seru ke depannya!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20 tahun",
                "tanggal_lahir": "21 Mei 2006",
                "asal": "Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "Kak Asri cantik banget, terus senyumnya manis banget. Orangnya juga seru dan berbakat. Pokoknya best lah Kak Asr",
                "pesan": "semoga makin banyak hal keren yang bisa Kakak  capai!"
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "124450106",
                "umur": "-",
                "tanggal_lahir": "25 April 2006",
                "asal": "Lampung",
                "alamat": "Balam",
                "hobbi": "berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "Bang Bima aslinya baik banget. Diajak ngobrol juga nyambung dan seru, jadi enak aja kalau ngobrol dan sharing sama bang abim.",
                "pesan": " Semoga Bang Bima makin sukses dan semua yang lagi .dikejar bisa dapet!"
            },
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20 Tahun",
                "tanggal_lahir": "14 Agustus 2006",
                "asal": "Ampera",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": " Kak Indah tuh chill banget orangnya, terus asik juga",
                "pesan": "Semoga Kak Indah selalu bisa ngejalanin semuanya dengan aman. Semoga yang diinginkan satu-satu tercapai ya!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20 tahun",
                "tanggal_lahir": "15 Juni 2006",
                "asal": "palembang",
                "alamat": "bebas",
                "hobbi": "ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "Kak Riska baik dan asik banget. Apalagi pas praktikum Alpro, sabar banget ngajarin kita yang kerjaannya error",
                "pesan": "Semangat terus kuliahnya dan jaga kesehatannya , dan sukses selalu!"
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "-",
                "tanggal_lahir": "-",
                "asal": "Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kak Yollanda orangnya aktif banget. Salut sama energinya yang selalu 100% .",
                "pesan": "Semoga energi Kak Yollanda tetap sebanyak itu sampai kapan pun. Tapi jangan lupa istirahat juga ya Kak!"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "25 tahun",
                "tanggal_lahir": "-",
                "asal": "Tangsel",
                "alamat": "Sukarame",
                "hobbi": "baca wattpad",
                "sosmed": "@fathyya.__",
                "kesan": "Kak Fathya tuh asik, baik, dan ramah. Orangnya juga gampang diajak ngobrol",
                "pesan": "Semoga ke depannya Kak Fathya ketemu banyak hal baik dan orang-orang baik juga!"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "123450052",
                "umur": "-",
                "tanggal_lahir": "$\\sum_{k=1}^{n} k + \\int_{0}^{x} 2x \\, dx + \\sqrt{81} + \\log_{10}(100)$",
                "asal": "Luhak tanah data",
                "alamat": "Gerbar",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "kakkanya ceriaa dan gamopang senyum",
                "pesan": "Semoga selalu happy dan banyak hal baik yang dateng.!"
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20 tahun",
                "tanggal_lahir": "28 Mei 2006",
                "asal": "sini",
                "alamat": "jauh pokoknya",
                "hobbi": "tidur",
                "sosmed": "@kshigf",
                "kesan": "Kak Ashila baik dan asik. mukanya suka ngingetin aku sama Kak Juwita , ada mirip-miripnya dikit",
                "pesan": "Semoga Kak Ashila selalu happy dan semua urusannya lancar!"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "124450103",
                "umur": "-",
                "tanggal_lahir": "31 Desember 2006",
                "asal": "Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "Bang Danil tuh keren sih. Duta, berbakat, tapi orangnya tetap baik dan nggak sombong",
                "pesan": "Semoga makin banyak kesempatan keren yang datang ke Bang Danil. Tetap rendah hati dan terus berkembang ya Bang!!"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "124450021",
                "umur": "-",
                "tanggal_lahir": "05 Mei 2006",
                "asal": "Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "Bang Favian asik banget, apalagi pas kenal di praktikum Alpro. Sabar banget ngadepin kita yang kodingan-nya selalu error. Tapi tetap baik dan mau bantuin",
                "pesan": "Semoga ke depannya makin sukses dan sdipertemukan dengan orang orang baik!"
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "124450081",
                "umur": "-",
                "tanggal_lahir": "-",
                "asal": "situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd_",
                "kesan": "Bang Zumar baik banget dan asik juga.",
                "pesan": "Semoga ke depannya makin banyak hal baik yang datang ke Abang!"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "124450093",
                "umur": "Masih muda lah",
                "tanggal_lahir": "Hari Jum'at",
                "asal": "Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "Tanyain sama yuder (beneran ditanya ya)",
                "sosmed": "@jaldii.__",
                "kesan": "Bang Rizaldi keren parah. Pertama kali liat pas jadi MC PPLK tuh langsung kayak, “wah keren juga nih abang.” dan juga orangnya juga ramah dan asik.",
                "pesan": "Semoga sukses dan lancar terus kuliahnya bang, Pokoknya makin gacor terus Bang!!"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "124450074",
                "umur": "20 tahun",
                "tanggal_lahir": "18 November 2026",
                "asal": "Banyak Begal",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "Kak Saskia asik dan baik. Orangnya juga enak diajak ngobrol",
                "pesan": "Semoga Kakak selalu happy dan banyak hal seru yang bisa didapat ke depannya. !"
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20 tahun",
                "tanggal_lahir": "03 Juni 2006",
                "asal": "lampung",
                "alamat": "balam",
                "hobbi": "jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "Kak Selma cantik banget, terus baik juga orangnya",
                "pesan": "Semoga Kak Selma selalu happy dan ketemu banyak orang baik!"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

if menu == "Departemen Minbak":
    def Departemen_Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RQEoKFKLV35hIaQRU1luSI5DlTx68V56",
            "https://drive.google.com/uc?export=view&id=1XmdwqVKXiafYmmJsrb6fTEVWIALrEjAP",
            "https://drive.google.com/uc?export=view&id=1kZ0pfyWBZmA2P18ADULwf8PacYv41xOf",
            "https://drive.google.com/uc?export=view&id=1wP9NJQ2eUaxjIU6Vc8oCgNYKoqQjx3nw",
            "https://drive.google.com/uc?export=view&id=161jpan6sJtgdSx_puqTJlj9U52bQIGiV",
            "https://drive.google.com/uc?export=view&id=1rjy8j28GgiJeW0d6Ym2rO0IvzeTLZHOr",
            "https://drive.google.com/uc?export=view&id=1GmAVGaUQInnuklbaFAfU3X_AWZjKTCer",
            "https://drive.google.com/uc?export=view&id=1yR_Yy8OCR6IcqpOjlNhIs08dGmGNyM5N",
            "https://drive.google.com/uc?export=view&id=1n1w3NMypuFD_mKqAbrnNqa6AXEQTv9c5",
            "https://drive.google.com/uc?export=view&id=1qgenUe9ed7S8Q2_bU2OGwubeSOI0GFa7",
            "https://drive.google.com/uc?export=view&id=1iwvszp1-xfOfSB86gHE87s-yR6s2p56X",
            "https://drive.google.com/uc?export=view&id=1uA7oHw2iHApTdROMntHZ-M4JutUasZZd",
            "https://drive.google.com/uc?export=view&id=1UzZyIlYSh-9ug6ZjrUf8IdU4oiC3C-2Z",
            "https://drive.google.com/uc?export=view&id=16uzmjw2vc6OvCVlMr-Y0q3Qn6i0VNU6x",
            "https://drive.google.com/uc?export=view&id=1HLtYDzajN0Hd5WlNtDpJh5jM6wQ6KMFe",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Panjang, Bandar Lampung",
                "hobbi": "Balap",
                "sosmed": "@kevinaj__",
                "kesan": "Bang Kevin tuh asik dan baik banget, apalagi kalau pas basket. Kalau di luar basket aku malah agak segan nyapa Bang Kevin , beda banget vibes-nya",
                "pesan": "Semoga selalu semangat buataktivitas dan kuliahnya Bang!!!"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21 tahun",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Baca",
                "sosmed": "@ferazkaa",
                "kesan": "Kak Gusti cantik banget, terus vibes-nya positif. Imut dan lucu juga, jadi kalau ketemu tuh bawaannya adem",
                "pesan": "Semoga vibes positifnya selalu dibawa ke mana pun Kak Gusti pergi. Semoga banyak hal baik yang datang  !!!"
            },
            {
                "nama": "Ari Aristo Muthahari Parisi",
                "nim": "123450088",
                "umur": "21 tahun",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "Bang Ari tuh baik dan asik banget. Orangnya juga enak diajak ngobrol.",
                "pesan": "Semoga semua urusan abang  dilancarkan terus. Semangat kuliahnya !!"
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21 tahun",
                "asal": "Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nganterin Datasena ke gedung F",
                "sosmed": "@mridwaan_22",
                "kesan": "Bang Ridwan asik pol dan seru banget. Apalagi kalau ngajarin basket, baik banget dan sabar juga ngajarnya",
                "pesan": "Semoga makin jago dan menyala terus, sukses di semua urusanny!!!"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "124450058",
                "umur": "20 tahun",
                "asal": "Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Belajar",
                "sosmed": "@aayuandrianni_",
                "kesan": "Kak Ayu tuh imut dan lucu banget. Orangnya juga keliatan asik",
                "pesan": "Semoga selalu happy dan dikelilingi orang-orang baik. Semangat terus ya Kak!!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21 tahun",
                "asal": "Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Nemenin Bryan live TikTok",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa baik dan seru  orangnya",
                "pesan": "semangat terus kuliahnya kakak dan sukse selalu !!!"
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19 tahun",
                "asal": "Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Lihat bulan",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kak Juwita tuh partner basket yang asik dan seru banget. Kalau basket bareng jadi lebih rame dan seruuu",
                "pesan": "Semoga semua ukegiatan dilancarkan terus. Semangat kuliahnya dan sukses terus kak !!!"
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19 tahun",
                "asal": "Lampung Tengah",
                "alamat": "JI Pulau Damar",
                "hobbi": "Taptap layar kalo Bryan live",
                "sosmed": "@afdall.03",
                "kesan": "Bang Afdal tuh asik dan seru banget orangnya. Diajak ngobrol juga enak",
                "pesan": "Semoga selalu ketemu banyak hal seru ke depannya. Semangat terus kuliahnya !!!"
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini asik dan baik",
                "pesan": "Semoga kebaikan Kak Salsa selalu balik dalam bentuk hal-hal baik juga !!!"
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Ngitungin kelopak bunga di kebun",
                "sosmed": "@andra.lhm",
                "kesan": "Bang Andra tuh coach basket yang jago dan  sabar banget ngajarin kita. Sumpah baik banget juga, apalagi waktu nampung Cosval di kosannya. Kalau dimintain tolong juga selalu ditolongin , baik banget jujur",
                "pesan": "Makasih banyak ya Bang udah sabar ngajarin dan banyak bantuin. Semoga kebaikan Bang Andra dibalas dengan banyak hal baik juga!!!"
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "22 tahun",
                "asal": "Nias",
                "alamat": "Belwis",
                "hobbi": "Live TikTok",
                "sosmed": "@bryantel_",
                "kesan": "Bang Bryan tuh pintar banget, cuma orangnya agak introvert dan kayak nggak enakan gitu.",
                "pesan": "Semoga Bang Bryan makin percaya diri dan nggak terlalu sungkan buat nunjukin kemampuan. Tetap semangat terus Bang!!!!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobbi": "Ngegift live Bryan",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "Bang Ghiyats tuh baik dan asik banget orangnya.",
                "pesan": "Semoga selalu dikelilingi orang-orang baik dan makin banyak hal seru yang datang. Sukses terus Bang!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Bengong",
                "sosmed": "@indahjuliaa",
                "kesan": "Kak Indah tuh baik, asik, dan seru juga orangnya.",
                "pesan": "Semoga Kak Indah selalu happy dan semua yang lagi dijalanin bisa lancar. !!!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450023",
                "umur": "18 tahun",
                "asal": "Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "sosmed": "@cacalvra",
                "kesan": "Kak Caca tuh asik dan baik banget. Terus kalau lagi nari keren banget sih, beda banget auranya",
                "pesan": "Semoga terus berkembang dan makin keren di hal-hal yang Kak Caca suka !!!"
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20 tahun",
                "asal": "Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": " Bang Rafka tuh baik dan seru orangnya. Cuma pas rangkaian terakhir aku sempat agak takut dikit sama Bang Rafka karena ikut marah. Tapi overall tetap baik kok Bang",
                "pesan": "Semoga ke depannya makin sukses dan selalu dimudahkan dalam semua urusan !!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Minbak()

if menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vRzkUniLayC0BTJssMWzj6AWWlRc3f3Z",
            "https://drive.google.com/uc?export=view&id=1M4AojnD-TYwtp8NOGIfO5QfNf8EDjI-4",
            "https://drive.google.com/uc?export=view&id=1hiYImFG76xj-2i6GEEzCfzLNjNmPbt5K",
            "https://drive.google.com/uc?export=view&id=1DL5-_xoI2q8UY4CtGRKccxPGr34dj6ix",
            "https://drive.google.com/uc?export=view&id=1lmkq4msQ37IeJkBMjuFFQJULe_CsrqA-",
            "https://drive.google.com/uc?export=view&id=1ZqMRApJnU3wPl0rUbjCNitAH4qDw4uIQ",
            "https://drive.google.com/uc?export=view&id=1B2ZHqaMi3X_1lHolT7XF1KGiX2d3AWj1",
            "https://drive.google.com/uc?export=view&id=1189FQtqdb8doDXne5_XJpJrfQKy5N7Jy",
            "https://drive.google.com/uc?export=view&id=1mhEUR_SS89FgtISt5GTjyFAdSvv-PhEG",
            "https://drive.google.com/uc?export=view&id=1SLB-mhthNNa4ulUFgIKsL_dGHxzscGGT",
            "https://drive.google.com/uc?export=view&id=1yZtiZIeaDBK1umT17oOuoVVcHRMEX1Cf",
            "https://drive.google.com/uc?export=view&id=1xeBdN9V-U-aLuV6kdpMziG8pc4ZA4lr7",
            "https://drive.google.com/uc?export=view&id=12RuAKBgvwYKn0zsdxYBxwDl4wmA6BlAg",
            "https://drive.google.com/uc?export=view&id=1Am6gBNdy6BTcSc4GaPbmS-3N3DcZig7I",
            "https://drive.google.com/uc?export=view&id=1s0dEhlOCEt5EDrP0KYVLsidivH2b01Hx",
            "https://drive.google.com/uc?export=view&id=1t3QJiXg_HsZLOuol0_9aGfyxVZDpnJqA",
            "https://drive.google.com/uc?export=view&id=17mb-s0kHKaPYyUbB1xs8wDW3HwezMNHZ",
            "https://drive.google.com/uc?export=view&id=1KWn0nlNKTQ-keTutQxFUn_d-LJkML0el",
            "https://drive.google.com/uc?export=view&id=1Lqd2H6ZPhGoAjsCgTgK4gqRXWxd_G63_",
            "https://drive.google.com/uc?export=view&id=1rrPzS2nkWW0bEHrKSWoZYB35w4sCspZK",
            "https://drive.google.com/uc?export=view&id=1DVB5XOTr_oSywKYflqkhQ0d_E0TN54kn",
            "https://drive.google.com/uc?export=view&id=1yereIcgcjnGOA7BSemKNJa0XJFvWsGZW",
        ]
        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi": "Tidur",
                "sosmed": "@biyokcb",
                "kesan": "Bang Fabio tuh pinter banget sih, gacor, kritis. Pokoknya best lah abang satu ini",
                "pesan": "Gas terus Bang! Semoga makin gacor, makin keren, dan semua yang lagi dikejar bisa dapet. !!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21 tahun",
                "asal": "Lampung",
                "alamat": "Airan Raya",
                "hobbi": "Membaca",
                "sosmed": "@tvnty_",
                "kesan": "Kak Tanty tuh asik banget orangnyaa. Pintar, terus kalau diajak ngobrol tuh enak banget.",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Fadil Prasetyo Alfarizzi",
                "nim": "123450048",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Gitar",
                "sosmed": "@fadilalfarizzii",
                "kesan": "Bang Fadil tuh pintar, berbakat, dan jago banget. Sosok yang baik dan punya banyak hal keren buat dikenang. Senang pernah kenal dengan almarhum",
                "pesan": "Semoga semua kebaikan  Bang Fadil kasih tetap jadi kenangan baik buat orang-orang yang mengenal abang. Semoga tenang di sisi Allah SWT. Bang.!!!"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "21 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berenang",
                "sosmed": "@keyashafi_",
                "kesan": "Bang Akeyla tuh pinter dan asik banget",
                "pesan": "Semoga makin pinter, makin jago, dan makin banyak kesempatan keren yang datang!!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futsal",
                "sosmed": "@razyn.hfd",
                "kesan": "Bang Razin tuh mirip Pak Tirta wkwk. Terus orangnya juga ceria banget.",
                "pesan": "Semoga selalu ada alasan buat senyum dan makin banyak hal baik yang datang !!!"
            },
            {
                "nama": "Manuel Frederika",
                "nim": "124450039",
                "umur": "20 tahun",
                "asal": "Batam",
                "alamat": "Way Kandis",
                "hobbi": "Tenis meja",
                "sosmed": "@manuelfdk_",
                "kesan": "Bang Manuel tuh keren, baik, dan seru banget orangnya.a",
                "pesan": "Semoga makin banyak hal seru yang Abang temuin ke depannya.!!"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "12 tahun",
                "asal": "Bali",
                "alamat": "Nusa Penida",
                "hobbi": "Menghayal",
                "sosmed": "@Violaadrtr_",
                "kesan": "Kak Viola cantik banget sih. Terus mukanya juga keliatan dewasa banget, auranya tuh beda sendiri. Cakepnya nggak main-main",
                "pesan": "Semoga makin banyak hal baik yang datang dan semua yang diinginkan bisa tercapai. Tetap kece terus ya Kak!"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20 tahun",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak Risa tuh baik dan asik banget.",
                "pesan": "Semoga selalu ketemu orang-orang baik dan banyak momen seru ke depannya.!!"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim": "124450078",
                "umur": "19 tahun",
                "asal": "Kepulauan Riau",
                "alamat": "Teluk Betung",
                "hobbi": "Nonton KHW",
                "sosmed": "@vunnycaa",
                "kesan": "Kak Vannisa baik dan asik banget orangnyaa",
                "pesan": "Semoga semua urusannya dilancarin dan makin banyak hal seru yang datang!"
            },
            {
                "nama": "Yulia Kristine Malau",
                "nim": "124450119",
                "umur": "20 tahun",
                "asal": "Jambi",
                "alamat": "Sabah Balau",
                "hobbi": "Belajar",
                "sosmed": "@krnylee",
                "kesan": "Kak Yulia tuh baik, asik, cantik lagi. Pokoknya paket lengkap",
                "pesan": "Semoga makin banyak hal keren yang bisa Kak Yulia capai.!!"
            },
            {
                "nama": "Elsa Sitorus",
                "nim": "124450088",
                "umur": "21 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Rebahan",
                "sosmed": "@_els.a",
                "kesan": "Kak Elsa tuh the best banget sih. Pintar, baik, asik, terus kegiatannya super duper sibuk. tapi semangatnya tetap menyala",
                "pesan": "Semoga semua yang dikerjain selalu lancar dan hasilnya juga worth it, jangan lupa istirahat ya kak!!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450062",
                "umur": "20 tahun",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Mancing",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya tuh asik dan baik banget",
                "pesan": "Semoga makin banyak hal baik yang nyamperin Kak!!!"
            },
            {
                "nama": "Lovianora Saragih",
                "nim": "124450105",
                "umur": "19 tahun",
                "asal": "Sumatera Utara",
                "alamat": "Way Huwi",
                "hobbi": "Dengerin musik",
                "sosmed": "@_loviaa",
                "kesan": "Kak Lovi tuh berbakat banget, apalagi public speaking-nya. Udah jago, asik pula, dan yang paling penting nggak sombong sama sekali",
                "pesan": "semangat terus  kakak, semoga kedepanya makin gacor dan bisa bawa Kak Lovi ke panggung-panggung yang lebih besar. !!!"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20 tahun",
                "asal": "Kalianda",
                "alamat": "Kota Baru",
                "hobbi": "Main game, tidur",
                "sosmed": "@aruccy_",
                "kesan": "Bang Alsi tuh asik dan baik banget.",
                "pesan": "semangat terus kuliahnya kakak ,Semoga semua urusan Bang Alsi dilancarin!!!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "19 tahun",
                "asal": "Bengkulu Selatan",
                "alamat": "Belwis",
                "hobbi": "Make up",
                "sosmed": "@sher_renna",
                "kesan": "Kak Sherena tuh baik, cantik, ramah, dan vibes rohaninya kuat banget",
                "pesan": "Semoga selalu diberi kelancaran dan tetap jadi pribadi yang baik serta rendah hati!!!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19 tahun",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kak Faiza tuh agak pendiam, tapi kakanya pinter banget. Orangnya juga baik",
                "pesan": "Semoga makin pede nunjukin kemampuan Kak Faiza.!"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Main game",
                "sosmed": "@gathfannadif",
                "kesan": "Bang Gathfan tuh baik, asik, terus gemoy juga wkwk",
                "pesan": "Semoga makin banyak hal seru yang datang dan makin gacor terus!!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20 tahun",
                "asal": "Metro",
                "alamat": "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "sosmed": "@apiszzaja_",
                "kesan": "Bang Hafidz asik poll, baik, humoris, dan tentunya pinter. Paket lengkap sih i",
                "pesan": "Semoga makin pinter, makin gacor, dan semua kesibukannya membuahkan hasil. Gas terus Bang!"
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim": "124450053",
                "umur": "20 tahun",
                "asal": "Bandar Lampung",
                "alamat": "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed": "@kelelep_comberan",
                "kesan": "Bang Kaleb udah cakep, pinter, nggak pelit ilmu lagi. Keren dah pokoknya, paket lengkap banget ini abang satu",
                "pesan": "Tetap jadi orang yang nggak pelit ilmu ya Bang. Semoga makin sukses dan makin banyak hal keren yang bisa dicapai!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19 tahun",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Scroll",
                "sosmed": "@melva_fbrt",
                "kesan": "Kak Melva tuh imut, lucu, dan baik banget.",
                "pesan": "emoga selalu happy dan banyak hal baik yang mampir!"
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim": "124450099",
                "umur": "20 tahun",
                "asal": "Lampung Utara",
                "alamat": "Asrama TB 3",
                "hobbi": "Membaca",
                "sosmed": "@Syaafiqui",
                "kesan": "Bang Falakh tuh pinter banget sih, keren parah. Bisa dibilang salah satu panutan lah",
                "pesan": "etap gacor terus Bang! Semoga makin jauh melangkah, makin banyak yang bisa dicapai!"
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim": "124450115",
                "umur": "28 tahun",
                "asal": "Kota bumi",
                "alamat": "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed": "@henryferdianto",
                "kesan": "Bang Henry ini mah all role banget wkwk. Udah baik, pinter, jago, keren pula. Pokoknya paket lengkap.",
                "pesan": "Semoga semua skill dan kemampuan Bang Henry makin kepake di tempat-tempat keren. Pokoknya sukses terus, jangan redup!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

if menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13HDtJ_TqeS0bsyT49Mi19coarlqf5wen",
            "https://drive.google.com/uc?export=view&id=1lEyc2tUvuky0vXJgw-d3OGHqw0fTQkwQ",
            "https://drive.google.com/uc?export=view&id=1vg-iuoTstlSRiO55BE1sh3k2OLLIE4v4",
            "https://drive.google.com/uc?export=view&id=1leTPagic5YbR4JSCcu_4ukfgrjeEL7Hg",
            "https://drive.google.com/uc?export=view&id=1WlP-lqaBq5S566tJ7zDH3fib3nLhcpT6",
            "https://drive.google.com/uc?export=view&id=1dVTPZv3d6gQTKpPSnQFnIUwz_jNaijS-",
            "https://drive.google.com/uc?export=view&id=1TF_ejLsJTQ0B2JXUyF8Odyn0_kH6KlY8",
            "https://drive.google.com/uc?export=view&id=1N9vM0UCUMjBPxpJBGLthT-WJDqIbzzYm",
            "https://drive.google.com/uc?export=view&id=12wEdiCUup1nzE42dxm_U59-o4mlaV0KD",
            "https://drive.google.com/uc?export=view&id=1IYBptMFvZADGzgIb9rcvx7EKT74hbRKK",
            "https://drive.google.com/uc?export=view&id=1gi6j_6KXBmVZCC4EoeCYstbCfGNtz3vq",
            "https://drive.google.com/uc?export=view&id=1zcDTlgt0iV3RFtSn767kBS5M5Jg-XN5I",
            "https://drive.google.com/uc?export=view&id=1q5tYRQIEPoH0u-lbPJsOVTwUjF1VD9xA",
            "https://drive.google.com/uc?export=view&id=1Bj1fcVYQ5xihH_KmCPV-ehes_UXsfHLS",
            "https://drive.google.com/uc?export=view&id=1BaOrYL4TWr3L0vMW3BNQRV0odP6wqkn6",
            "https://drive.google.com/uc?export=view&id=1iV-JVSrKuKARyU_moB3_JBEz4q96hccu",
            "https://drive.google.com/uc?export=view&id=10E0Q98DNWrjQZcaThzhaibOVpadGytta",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket Pantai Kedu, Kalianda",
                "alamat": "Samping kos capo",
                "hobbi": "Baca jurnal",
                "sosmed": "@arientakhsnl_",
                "kesan": " Kak Arienta tuh salah satu kakak yang menurutku keren banget. Jiwa pemimpinnya dapet, tegas, pintar. Awalnya mukanya keliatan agak judes tapi kalau udah senyum cakep banget. Jujur, Kak Arienta termasuk panutan aku sih, cocok banget jadi sosok yang ditiru.",  
                "pesan":"Semoga Kak Arienta makin gacor ke depannya dan bisa jadi pemimpin di tempat yang lebih besar lagi.!!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Nyanyi dan masak ayam",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak Vany first impression-nya keliatan judes banget, padahal aslinya baik. Kalau udah kenal ternyata nggak sejutek mukanya wkwk. Orangnya juga enak diajak ngobrot",  
                "pesan":"Semoga selalu diberi kemudahan dan selalu dikelilingi orang-orang baik !"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Urip",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang Nobel tuh keren banget, apalagi dibagian kepemimpinannya gacor sihh. Cara mikirnya bagus, kritis, tapi pembawaannya tetap santai dan nggak ribet. Yang aku suka, walaupun santai tapi tetap bisa bikin semuanya jalan dengan baik. Gaya kepemimpinannya menurutku keren sih, the best lah Bang, dan bakatnya jago main sulapp.",  
                "pesan":"Semogaa sukses dan berkah selalu dan Semoga bisa bawa gaya kepemimpinan dan pola pikirnya ke tempat yang lebih jauh lagi!!"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450113",
                "umur": "25",
                "asal":"Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman tuh cara mikirnya bagus banget dan kritis. Kalau diajak bahas sesuatu tuh asik banget. Tapi walaupun pemikirannya kritis, orangnya tetap baik dan asik.",  
                "pesan":"Semoga selalu semangat dan makin baik lagi kedepanya bang!!!"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Teriak",
                "sosmed": "@friezazmi",
                "kesan": "Bang Azmi tuh keren, tegas, dan energik bangettt. Orangnya juga kritis,",  
                "pesan":"Semoga energi dan semangat abang selalu menyala. Sukses terus Bang, makin gacor ke depannya!!!"# 1
            },
            {
                "nama": "Ayake Alfatih Ramadhan",
                "nim": "124450081",
                "umur": "21",
                "asal":"paninjauan 10 kota di atas solok sumatera barat",
                "alamat": "blok d 79 jl.manggis 8 perum pemda wayhui jatiagung lampung selatan",
                "hobbi": "Memasak",
                "sosmed": "@_ykeal",
                "kesan": "Bang Ayake tuh salah satu sosok pemimpin yang menurutku baik banget, perhatian dan peduli sama orang lain",  
                "pesan":"Semoga tetap jadi orang yang peduli. Semoga makin sukses dan makin banyak hal baik yang datang!!!"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "21",
                "asal":"Painar, Sumatera Barat",
                "alamat": "Gedung F",
                "hobbi": "Mandiin anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "Bang Caesar kalau lagi rangkaian auranya bisa galak banget . Tapi pas udah di luar rangkaian ternyata lucu , gemoy dan gak pelit ilmu juga orangnya.",  
                "pesan":"Semoga makin sukses terus Bang! Tetap jadi abang yang seru dan gemoy!!"# 1
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Rahim ibu",
                "alamat": "sebrang kost yazid rizal",
                "hobbi": "ngapain aja deh",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kak Yudia ramah, tegas, keren, baik punya jiwa kepemimpinan yang bagus, dan cara bawa dirinya juga keren.",  
                "pesan":"Semoga selalu semangat dan bahagia Semoga Kak Yudia makin berkembang dan bisa bawa kemampuan memimpinnya ke tempat yang lebih besar lagi.!!"# 1
            },            
            {
                "nama": "Haikal Saventio Tamba",
                "nim": "124450014",
                "umur": "20",
                "asal":"Sibolga",
                "alamat": "Di depan kostan bang ayake belok kanan",
                "hobbi": "Mencari pakan anak ayam",
                "sosmed": "@_haikaaall",
                "kesan": "Bang Haikal tuh kritis dan tegas banget, tapi tetap baik orangnya.",  
                "pesan":"S Semoga ke depannya makin sukses dan selalu dimudahkan dalam semua urusan. Semangat terus Bang, makin baik lagi!!"# 1
            },            
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal":"Depok",
                "alamat": "Oiya Cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kak Putri tuh ramah banget, baik juga, dan tegas jugaa ",  
                "pesan":"Semoga Kak Putri selalu ketemu orang-orang baik dan banyak hal menyenangkan ke depannya!!!"# 1
            },            
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "21",
                "asal":"Cikajang",
                "alamat": "Tempat pemancingan",
                "hobbi": "Baking",
                "sosmed": "@queentanaabila",
                "kesan": "kak Queenta tuh first impression-nya judes banget wkwk, tapi ternyata aslinya baik bange",  
                "pesan":"Semoga semua urusan Kak Queenta dilancarkan dan selalu ada hal baik yang datang.!!!"# 1
            },                        
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel kalem, cantik dan baik banget.",  
                "pesan":"Semogal selalu dikelilingi hal-hal baik dan orang-orang yang bikin nyaman!!!"# 1
            },            
            {
                "nama": "Charrlindah",
                "nim": "124450037",
                "umur": "21",
                "asal":"Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah tuh cakep dan asik banget. Orangnya juga santai",  
                "pesan":"Semoga ke depannya makin banyak hal seru yang Kak Charrlindah lewatin.!!!"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jere tuh asik poll sih. Orangnya keren, baik, dan gampang diajak ngobrol",  
                "pesan":"Semoga Bang Jere makin sukses dan makin banyak kesempatan keren yang datang!!"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kak Nabila  Baik, keren, cantik, terus asik juga orangnya",  
                "pesan":"Semoga Kak Nabila makin sukses dan semua yang lagi diusahain bisa tercapai.!!"# 1
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Bang Rafli tuh keren dan kalcer banget. Pembawaannya juga beda aja, kayak punya vibes sendiri.",  
                "pesan":"Semoga makin banyak hal keren yang bisa dicapai dan makin jauh melangkah ke depannya.!!!"# 1
            },
            {
                "nama": "Salafi Maharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@afi.nhr",
                "kesan": "Kak Salafi tuh asik dan baik banget.t",  
                "pesan":"Semoga Kak Salafi selalu dikelilingi orang-orang baik dan banyak hal seru yang datang!!!"# 1
            },                      
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()
