import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

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
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
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

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_container_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14Ltb0h4v9C6oQMtNlYpbiJyN3UzAj7Lq",
            "https://drive.google.com/uc?export=view&id=17cAvk0CVbXBfy_l2bxCOHiytm_Hwlukt",
            "https://drive.google.com/uc?export=view&id=1pXIHg55_wd-ke61JcGkqLVpU0k8E5bAc",
            "https://drive.google.com/uc?export=view&id=1tapAFvkjFNjSJifoADCN9Igxv1b-d_3R",
            "https://drive.google.com/uc?export=view&id=15ZLEyLFtNxWfjlgRJBXakZOex0DB4dR8",
            "https://drive.google.com/uc?export=view&id=1TvjsRMq2GhnI_V84IbA4AaDtc4L6z_Zc",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesekretariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "pertama kali liat abangnya agak takut gitu dan waktu tau abangnya jadi asprak ADS makin takut gitu. Tapi ternyata selama praktikum, abangnya baik banget ngejelasin dan bantu ngerjain tugas-tugas praktikum aku.",  
                "pesan":"terimakasih atas bantuannya ya bang, mungkin kalo waktu itu aku ga nanya abang, tugas praktikum aku ga selesai. Dan semangat dalam memimpin Himpunan Mahasiswa Sains Data ADYATAMA ITERA"# 1
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "nim": "123450066",
                "umur": "22",
                "asal":"Bangkinam",
                "alamat": "Sekretariatan HMSD",
                "hobbi": "Dzikir",
                "sosmed": "@Muhammadaqil1111",
                "kesan": "Awal kenal bg aqil waktu latihan basket, waktu itu mainnya jago banget. Udah beberapa kali ngobrol sama abangnya dan orangnya santai banget!",  
                "pesan":"semangat terus kuliahnya bang! semoga nanti pas IO menang yaa!"# 1
            },
            {
                "nama": "Efi Defiyanti",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "kakaknya lucu kaya mirip loopy dari pertama kali liat, terus waktu praktikum ADS kakaknya bener-bener ngebantu.",  
                "pesan":"Makasih kak udah bantu aku ngerjain tugas praktikum, maaf yaa aku sebentar-sebentar udah nanya."# 1
            },
           {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kotabaru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio_",
                "kesan": "Jujur salut waktu tau bang qois jadi sekre karena jarang aku temuin ada cowo jadi sekretaris",  
                "pesan":"semangat kuliahnya bang, semoga kuliahnya selalu diberikan kelancaran"# 1
            }, 
            {
                "nama": "Luthfia Laila Rahmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Keliling Balam",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakak ini ramah banget, penjelasannya mudah dipahami",  
                "pesan":"semangat terus ngerjain tugas akhirnya kak!!"# 1
            },
            {
                "nama": "Hafsa Fazilah Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Bertemu lulu",
                "sosmed": "@hafsafazilaa",
                "kesan": "Kakak ini asik penjelasan waktu wawancara jadi mudah dimengerti",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },          
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

if menu == "Badan Legislatif":
    def Baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z2O2eUKpon98s1sAOIG2rDjGyx0FrvXl",
            "https://drive.google.com/uc?export=view&id=1gZnYlXnWPWHyQmQLLWRVHFTjgADXe1cw",
            "https://drive.google.com/uc?export=view&id=1ECA0utPmU1lMY2qWTOIhzF4XqQg6nUtr",
            "https://drive.google.com/uc?export=view&id=1Hn-iqkIK5TwFCiNr7bjhHdjn9mSYZcxR",
            "https://drive.google.com/uc?export=view&id=16ij-gTIQiqWjALh9TM-GPykLUfMd-dkG",
            "https://drive.google.com/uc?export=view&id=1uxJ0XF0mTLuRULbTfcvSKL9--khf6wJM",
            "https://drive.google.com/uc?export=view&id=1Vc8A0sKm4-LdgLsDUgZoK1_994b1n8VE",
            "https://drive.google.com/uc?export=view&id=18dEzzF91M65gootLXX-IkOLMNGsC86h0",
            "https://drive.google.com/uc?export=view&id=1CToly3CvSUvqxjauxlJM1aMlusRKiW12",
            "https://drive.google.com/uc?export=view&id=1OjXJd6DX5d-_3vZXAk-HFB32imydJtVb",
            "https://drive.google.com/uc?export=view&id=1QYjHEg-ggWEA2bwbARLNkJ0pZrBkZB2O",
            "https://drive.google.com/uc?export=view&id=16Ly7YRtNCjxDyCkIkbVb2fj8_es6DX4L",
            "https://drive.google.com/uc?export=view&id=1rPA12tnPceTzCM2VrUI3gC1rJeCxk5FK",
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
                "kesan": "abang ini asik dan seru banget saya suka belajar dengan dia",
                "pesan": "semangat terus kuliahnya bang !!!"  # 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "Dengerin lagu Duhai Sayang",
                "sosmed": "@j__eesia",
                "kesan": "Kakak ini asik bangett, lucu gemas gitu, cantik juga",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Nonton drama AI",
                "sosmed": "@ddharu_",
                "kesan": "abang ini keren banget, kagum banget liat projek EXVOLTAS",
                "pesan": "semoga EXVOLTAS semakin jaya!!!"  # 1
            },
            {
                "nama": "Siti Sarifah Sumamah",
                "nim": "12450015",
                "umur": "18",
                "asal": "Banten",
                "alamat": "Kedaton",
                "hobbi": "Koleksi Kartu Boboiboy",
                "sosmed": "@syt.rifah",
                "kesan": "lucu banget kakaknya ngoleksi kartu boboiboy, jujur ga nyangka",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Wan Naswa",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "KotaBaru",
                "hobbi": "Nyapa angin",
                "sosmed": "@nshayka",
                "kesan": "Kakaknya seruu, asik, dan humble banget",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "21",
                "asal": "Lampung Barat",
                "alamat": "Sukabumi",
                "hobbi": "Ngopi",
                "sosmed": "@givarooo",
                "kesan": "orangnya keren, kece, gayanya kalcer gitu mantaplah pokoknyaa",
                "pesan": "semangat terus kuliahnya bang !!!"  # 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "12450101",
                "umur": "20",
                "asal": "Cibaduyut",
                "alamat": "Teluk",
                "hobbi": "Makan Pedes",
                "sosmed": "@jeremia_hm",
                "kesan": "suaranya bagus bangett, jujur waktu liatnya di acara datapudi keren banget",
                "pesan": "semangat terus kuliahnya bang !!!"  # 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "124450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Gym dan Koleksi figur",
                "sosmed": "@nagatseee",
                "kesan": "Bang Jhoa orangnya lucu dan asik banget, enjoyy banget orangnya",
                "pesan": "Semangat terus Bang Jona dan selamat abis menang perlombaan!!!"  # 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@sekardnwp",
                "kesan": "kakaknya baik dan perhatian banget",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            },
         {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "20",
                "asal": "Kota Bumi",
                "alamat": "pemda"   ,
                "hobbi": "Nginep di kos putri",
                "sosmed": "@haniquratuain_",
                "kesan": "kakaknya seru bangett, apalagi waktu jadi pemateri teknik persidangan",
                "pesan": "semangat terus kuliahnya kakak !!!"  # 1
            }, 
            {
                "nama": "Gh Mikael Niko Antonio",
                "nim": "124450025",
                "umur": "20",
                "asal": "Jombang",
                "alamat": "Jati Agung",
                "hobbi": "COD Musang",
                "sosmed": "@me._kael",
                "kesan": "Bang Mikael orangnya humble dan asik, auranya presidiumnya kenceng banget.",
                "pesan": "semoga kuliahnya dan segala urusannya dilancarkan ya bang"  # 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "kak nisa baik dan pinter bangett, seru pokoknya kalo belajar bareng kakaknya",  
                "pesan":"Semoga kedepannya kak nisa selalu diberikan kelancaran dalam segala hal ya kak"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak Monica orangnya murah senyum, baik dan lucu",  
                "pesan":"semangat terus kuliahnya kakak, semoga sehat selaluuu"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Baleg()

if menu == "Badan Kesenatoran":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BiNk5M6Ci6N4ieWtwpg7HIcHNecztF_L",
            "https://drive.google.com/uc?export=view&id=1PFbWmbXemip08GdLYQXBgtSdlsz4Ohdi",
            "https://drive.google.com/uc?export=view&id=19ziY6jn9BuqaRz-5uLXNI5FcPuVCpIFL",
            "https://drive.google.com/uc?export=view&id=1Hg7JdAHRoXRbQa3_Mf-VqNGCqlVrKmJt",
            "https://drive.google.com/uc?export=view&id=1u-35So1IGuhboLrdhxjRaQajM7tpBMs9",
            "https://drive.google.com/uc?export=view&id=1Zv_yaDB0BGbAxggwQem6sin_Okx2m-Ae",
            "https://drive.google.com/uc?export=view&id=1ywi71_eg5aJyQDmitS-sp_n7Lz5oB4PF",
            "https://drive.google.com/uc?export=view&id=1EGc91St9QmGoQAW98O7rRth2NQYLc67c",
            "https://drive.google.com/uc?export=view&id=1phyGNH6m_o0gjmiOUtTzM8-RcjCV6Fc1",
            "https://drive.google.com/uc?export=view&id=1Lzp48GWSe0HtBxscC2NbSq9uRsjYlUE4",
        ]
        data_list = [
            {
                "nama": "Fathinah Nur Azizah",
                "nim": "123450072",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belakang PB",
                "hobbi": "Nulis di medium",
                "sosmed": "@fathinahnazzh",
                "kesan": "Kagum banget sama kakak, karena jadi perwakilan penyampaian aspirasi dari HMSD ADYATAMA, bener-bener suka liat kakaknya",  
                "pesan":"semangat terus kuliahnya kakak dan semangat juga dalam menyampaikan aspirasi"# 1
            },
            {
                "nama": "Nadya Ratu Anjani",
                "nim": "123450083",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "Denger lagu",
                "sosmed": "@nadyaanjaani",
                "kesan": "kakaknya ramah bangett, terus juga lembut banget waktu wawancara itu, KAKAKNYA JUGA CANTIK BANGET",  
                "pesan":"semangat kuliahnya kak, semoga segala urusannya dilancarkan ya"# 2
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@lia.h_264",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kuliahnya kakak!"# 3
            },
            {
                "nama": "Dwi Rahma Fitriani",
                "nim": "124450084",
                "umur": "19",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Lapas",
                "hobbi": "Baca buku, nonton film, dengerin musik",
                "sosmed": "@dwi_rahmftnii",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 4
            },
            {
                "nama": "Suci Aulia",
                "nim": "124450034",
                "umur": "19",
                "asal":"Jakarta",
                "alamat": "Kota baru",
                "hobbi": "Mancing",
                "sosmed": "@sciia_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 5
            },
            {
                "nama": "Aqila Zayyan Salsabil",
                "nim": "124450014",
                "umur": "19",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Mendokumentasikan Bayes",
                "sosmed": "@aqilazayyaan",
                "kesan": "Awal kenal kak aqila waktu jadi mentor bayes disitu kak aqila pembawaanya selalu happy gitu. Aku langsung seneng dapet mentor yang pembawaannya ceria, kak aqila juga sabar banget ngarahin aku yang selalu linglung ini, dan juga ternyata kak aqila word of affirmation, soalnya aku sempat cerita-cerita ke kak aqila dan kata-kata dari dia jadi penyemangat, aku terharu banget sih waktu itu, jadi nangis dulu baru bales chat dari kak aqila. Tapi kak aqila juga sangat tegas orangnya, bener-bener ada waktu dimana dia tegas ke kami, tapi ga lama langsung ketawa-ketawa lagi, heran juga transisinya cepat gitu.",  
                "pesan":"terimakasih banyak ya kak aqila sudah sabar menghadapi kelompok bayes ini. Ga kerasa kak aqila sudah membersamai kami selama kurang lebih 5 bulan dan masanya sebentar lagi habis, tapi kak aqila akan selalu jadi mentor yang terbaik. Semoga setelah masa kaderisasi selesai kita tetap berkomunikasi ya kak, semoga ada waktu dimana kita bisa kumpul untuk bertukar cerita dan bercanda lagi. Terimakasih juga atas ilmu yang udah kakak berikan, semoga dapat diterapkan sebagaimana mestinya. Sayang kak aqila banyak-banyak."# 6
            },                      
            {
                "nama": "Wielman Itolo Halawa",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Dibonceng",
                "sosmed": "@wielhawn",
                "kesan": "deket sama abangnya waktu jadi panitia di acara paskah, bener bener ngebantuin banget, terus abangnya keren banget waktu jadi MC",  
                "pesan":"Semangat terus kuliahnya bang!"# 7
            },
            {
                "nama": "Hazel Mahesa Handhaka",
                "nim": "124450114",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Gunung Terang",
                "hobbi": "giring ayam",
                "sosmed": "@hazelhandhaka",
                "kesan": "abangnya keren banget, tapi kalo udah dikuncir jadi lucu",  
                "pesan":"semoga sukses perkuliahannya bang!"# 8
            },
            {
                "nama": "Helmy Surya Pratama",
                "nim": "124450033",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Kedamaian",
                "hobbi": "Ngesen Kiri",
                "sosmed": "@helmy_inst",
                "kesan": "kenal sama abangnya waktu jadi panitia paskah juga, seru banget diajak ngobrol, foto sama abang ini harus melet",  
                "pesan":"Semangat terus bang"# 9
            },
            {
                "nama": "Fernando Dimetrius Barus",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@barus.fernando",
                "kesan": "abangnya keliatan kalem banget",  
                "pesan":"semoga perkuliahannya lancar selalu ya bang!
                "# 10
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

if menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eyqvx79ZWpnQoyR0lAyRr75Hyf0I-LuI",
            "https://drive.google.com/uc?export=view&id=1eAwxOqcO2CHwEVU9tD7etDWtyl__dwaX",
            "https://drive.google.com/uc?export=view&id=17uksT4DLi3Dl3Wm9eXkLgOboaMnBCNvf",
            "https://drive.google.com/uc?export=view&id=1rETxJSYLJ8b9dvIPSHnTBERaeVyqwE0a",
            "https://drive.google.com/uc?export=view&id=1FvCgEEhwao82YMF_lVNbzx2fH-9e6I89",
            "https://drive.google.com/uc?export=view&id=1qYo-6LdCrtd4Mo0-YNb7r_XZwtrl9jXs",
            "https://drive.google.com/uc?export=view&id=1Ml9GKM4ZJ0j5XPInbqklzBaUHOpXaCq0",
            "https://drive.google.com/uc?export=view&id=1y47hF232Pq91Qw3q8y6ZqeB4KSrndgFs",
            "https://drive.google.com/uc?export=view&id=1Y1XktCO2D4tnUNKvtCtm6cAIfkdLT9zb",
            "https://drive.google.com/uc?export=view&id=1FXvvC060njR1_-m-l_unZWmx7l_lJxCT",
            "https://drive.google.com/uc?export=view&id=1CfquAfSW3Gw41L6Q-lCI5RS23W4MM7-g",
            "https://drive.google.com/uc?export=view&id=1QKaz5MKfppFLCfSOAlkf_CS-HV7FbLx2",
            "https://drive.google.com/uc?export=view&id=1J2v3zGFWZemwxekT6Qw4FOn2mx13Tzu6",
            "https://drive.google.com/uc?export=view&id=1ncsLzwAu5BO5N_FyoaRSkOo4Ojw7cmYT",
            "https://drive.google.com/uc?export=view&id=1LIl_vL-UZ7oj49UD9nubhl-NXPBHWqge",    
            "https://drive.google.com/uc?export=view&id=1c6w7z9UabT6JBPf-YhNW-p2RRoLMdGYZ",
            "https://drive.google.com/uc?export=view&id=1Pv2sy-Ab-tBsc3fw9QN2BB8zwokpMgPf",
            "https://drive.google.com/uc?export=view&id=15cq-IfafVPT5QyJpVhF3kE7vGJoSGkLR",
            "https://drive.google.com/uc?export=view&id=1gexcjHkKZoxx9lxoZvPYbhmQ8rCso1GC",
            "https://drive.google.com/uc?export=view&id=1BSyGem1tMTKdubzR8fhmoBJ80LrthHoG",
            "https://drive.google.com/uc?export=view&id=1lfdYpo3fbXk1j78clkFuk2RQW4tS6pU0",
            "https://drive.google.com/uc?export=view&id=1LL8qT1U-bOlzDgdF6sTmJf0vAmTi79U3",
        ]

        data_list = [
            {
                "nama": "Fabio Banyu Cyto",
                "nim": "123450104",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobbi": "Main game",
                "sosmed": "@biyokcb",
                "kesan": "abangnya pinter banget, jujur kagum, seru juga orangnya",
                "pesan": "semangat terus kuliahnya bang!!!"
            },
            {
                "nama": "Tanty Widiyastuti",
                "nim": "123450094",
                "umur": "21",
                "asal": "Lampung Tengah",
                "alamat": "Airan",
                "hobbi": "Menonton",
                "sosmed": "@tvnty",
                "kesan": "kakaknya bener-bener mirip sama artis arafah, mana kakaknya seaktif itu, seru pokoknya",
                "pesan": "semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Razin Hafid Hamdi",
                "nim": "123450096",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Futssal",
                "sosmed": "@razyn.hfd",
                "kesan": "Abangnya mirip banget sama pak tirta, dari kepribadiannya juga mirip",
                "pesan": "Semoga perkuliahnnya dilancarkan selalu bang!"
            },
            {
                "nama": "Hafidz Wahdiansyah",
                "nim": "124450064",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Metro Kibang",
                "hobbi": "Ngegame, ngoding, nyibukin diri",
                "sosmed": "@apiszzaja_",
                "kesan": "Abangnya baik banget, lucu dan seru banget kalo diajak ngobrol",
                "pesan": "Semoga segala urusannya dilancarkan ya"
            },
            {
                "nama": "Gathfan Nadif Ali",
                "nim": "124450001",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Main Game",
                "sosmed": "@gathfannadif",
                "kesan": "Abangnya menginspirasi saya untuk belajar lebih giat",
                "pesan": "Semoga abangnya dapat membantu dan membimbing selalu"
            },
            {
                "nama": "Akeyla Fairuz Shafi",
                "nim": "123450119",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "sosmed": "@keyashafi_",
                "kesan": "Abangnya baik, ramah, dan asik banget, selalu semangat dalam segala hal.",
                "pesan": "Semangat terus kuliahnya bang"
            },
            {
                "nama": "M. Alsi Syahrulloh",
                "nim": "124450092",
                "umur": "20",
                "asal": "Kalianda",
                "alamat": "Gedung Harapan",
                "hobbi": "Main Game",
                "sosmed": "@aruccy_",
                "kesan": "Humoris dan gampang bikin ketawa",
                "pesan": "Semoga perkuliahannya lancar terus ya bang"
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri",
                "nim": "124450005",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Korpri",
                "hobbi": "Main Gitar",
                "sosmed": "@hazelhandhaka",
                "kesan": "Kakaknya baik dan cantik banget!!",
                "pesan": "Semangat terus perkuliahnnya kak!"
            },
            {
                "nama": "Sherena Florencia",
                "nim": "124450027",
                "umur": "20",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Msake Up",
                "sosmed": "@sher_renna",
                "kesan": "Kakaknya baik, lucu, dan seru banget!!",
                "pesan": "Tetap jadi inspirasi bagi adik tingkat, Kak"
            },
            {
                "nama": "Risa Romadona",
                "nim": "124450127",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Rolling Skate",
                "sosmed": "@risarmdna",
                "kesan": "Kak risa mirip banget sama dosen pancasila aku yang outfitnya selalu lucu-lucu",
                "pesan": "Semoga sehat dan perkuliahannya dilancarkan selalu!"
            },
            {
                "nama": "Fadya Izzatul 'Aini",
                "nim": "124450075",
                "umur": "20",
                "asal": "Pringsewu",
                "alamat": "Airan",
                "hobbi": "Makan",
                "sosmed": "@fadyaizzatul_",
                "kesan": "Kakaknya baik banget dan seru!!",
                "pesan": "Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Faiza Try Anjani",
                "nim": "124450075",
                "umur": "19",
                "asal": "Padang",
                "alamat": "Belwis",
                "hobbi": "Baca Novel",
                "sosmed": "@faizaanjanii",
                "kesan": "Kakaknya pinter bangett terus juga bener-bener kalem orangnya",
                "pesan": "Semoga urusan perkuliahannya dilancarkan ya kak!"
            },
            {
                "nama": "Melva Shaprina Febrianti",
                "nim": "124450087",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Sukarame",
                "hobbi": "Banyak",
                "sosmed": "@melva_fbrt",
                "kesan": "Kakaknya baik banget dan imut banget!!",
                "pesan": "Sukses selalu ya kak"
            },
            {
                "nama": "Vannisa Ramadhani",
                "nim" : "124450078",
                "umur" : "19",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan selalu terlihat ceria.",
                "pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "nama": "Yulia Cristine Malau",
                "nim" : "124450119",
                "umur" : "20",
                "asal" : "Jambi",
                "alamat" : "Sabah balau",
                "hobbi": "Belajar",
                "sosmed" : "@krnylee",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Elsa Sitorus",
                "nim" : "124450088",
                "umur" : "21",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "sosmed" : "@_els.a",
                "kesan" : "Murah senyum dan enak diajak bicara.",
                "pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "nama": "Lovianora Saragih",
                "nim" : "124450105",
                "umur" : "19",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "sosmed" : "_loviaa",
                "kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "nama": "Kaleb Filbert Istel",
                "nim" : "124450053",
                "umur" : "20",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh",
                "nim" : "124450099",
                "umur" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto",
                "nim" : "124450115",
                "umur" : "20",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
            {
                "nama": "Manuel Frederika",
                "nim" : "124450039",
                "umur" : "28",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi",
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "abangnya baik dan ramah",
                "pesan" : "semangat terus kuliahnya bang"
            },
            
        ]

        display_images_with_data(gambar_urls, data_list)

    mikfes()
# PSDA
if menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LdrnIp0OvtSvDT-IDldV3A22HaVR6Sdx",
            "https://drive.google.com/uc?export=view&id=1CbyhJd_x4vRCHuWH6ZXSmL7WseP8Gyv3",
            "https://drive.google.com/uc?export=view&id=1cWrkcMXWG7ZH3U3F7QPLIlAWxKexcsIG",
            "https://drive.google.com/uc?export=view&id=1cjH2G2801puyZL8kFQKfEcdUX9-W-4QS",
            "https://drive.google.com/uc?export=view&id=1FNgDX7rosek1F8oEcc8FCik2oBs2Hg64",
            "https://drive.google.com/uc?export=view&id=1t0jlFr1CLdf8S-7tji6jEsiKiCuaNRJq",
            "https://drive.google.com/uc?export=view&id=1lkRPwFFhOW5YX7nwcg74pirZeRK8Opis",
            "https://drive.google.com/uc?export=view&id=1lEQe4VmE_TN4f8E_lkKfvcgc7kk7gxqW",
            "https://drive.google.com/uc?export=view&id=1f1iZxkEA8dEWYyx6ZnSEHP7Iw01o_R4B",
            "https://drive.google.com/uc?export=view&id=1EpTz20jy2DcIeeEHj8SK0dJrpYX23sBQ",
            "https://drive.google.com/uc?export=view&id=1lN5v6I2K5I6bhRd6aAIJPLl1bdo2F9HZ",
            "https://drive.google.com/uc?export=view&id=17xseR4KYV7SuMCzfgwjk5p-B-I0niFCf",
            "https://drive.google.com/uc?export=view&id=1xPxUGMeCkt6Rayh8eV3_Vsr9ny8p72eh",
            "https://drive.google.com/uc?export=view&id=14b8qmnde8c_RCxwRR6zL5KXbnFzcEbi1",
            "https://drive.google.com/uc?export=view&id=1AkIZVmaFAbT8mI_NKknMb0aYa3wRC9Q_",
            "https://drive.google.com/uc?export=view&id=1N1-27XeDk4m3ff2BQ7xC8jholR5ehmSW",
            "https://drive.google.com/uc?export=view&id=1nOXS7amS3k3UD2HDvYO6EUF6NinWq9e7",
        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal":"Deket pantai",
                "alamat": "Samping kos capo",
                "hobbi": "ngerjain tugas",
                "sosmed": "@arientakhsnl_",
                "kesan": "kakaknya mirip banget sama loopy, lucu gemes gitu, bener-bener mirip banget. pokoknya kalo udah ketemu kakaknya pasti langsung keinget loopy",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450089",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Belwis",
                "hobbi": "nonton",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kak!"# 3
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450117",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Puri",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "abangnya baik banget, kalo ngejelasin materi tuh menarik banget ga ngeboseninn. terus waktu nunjukin sulapnya jujur keren banget",  
                "pesan":"semangat terus kuliahnya bang! sering sering tunjukin sulapnya  ya"# 4
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Samping Pasar",
                "hobbi": "duel boxing sama reno",
                "sosmed": "@friezaazmi",
                "kesan": "abangnya ramah banget, seru juga kalo diajak ngobrol, apalagi waktu bantuin aku di parkiran",  
                "pesan":"terimakasih udah bantuin aku ya bang, maaf ngerepotin. semangat kuliahnya ya bang, semoga segala urusan dilancarkan"# 5
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450108",
                "umur": "21",
                "asal":"Solo",
                "alamat": "Samping kost Ezra",
                "hobbi": "Masak ayam",
                "sosmed": "@ykeall",
                "kesan": "abangnya baik banget",  
                "pesan":"Semangat terus kuliahnya bang"# 6
            },                      
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450072",
                "umur": "20",
                "asal":"Nias Selatan",
                "alamat": "Asrama TB 3",
                "hobbi": "Giring anak ayam",
                "sosmed": "@caesar.oriza",
                "kesan": "kenal bang caesar waktu PPLK karena aku di titipin abang aku ke bang caesar, aku udah takut liat mukanya apalagi pas tau abangnya jadi komdis. tapi waktu pertama kali ngobrol itu lembut sih ngomongnya, beda banget kalo dibandingin sekarang, suka banget gara-garain aku. tapi bang caesar jadi garda terdepan aku sih kalo ada apa-apa di kampus tuh, dia bisa banget jadi pengganti abang aku",  
                "pesan":"terimakasih ya bang caesar udah bantuin aku waktu itu, maaf selalu ngerepotin dengan banyak nanya. semangat kuliahnya ya bang, semoga segala urusannya dilancarkan. "# 7
            },
            {
                "nama": "Euodia Meiliana Friedita",
                "nim": "124450029",
                "umur": "18",
                "asal":"Adam dan Hawa",
                "alamat": "Depan kontrakan",
                "hobbi": "nonjokin orang",
                "sosmed": "@yudiameilianaa_",
                "kesan": "tau kakaknya waktu PPLK, kakaknya jadi PJ gitu istilahnya di kelompok PPLK aku waktu itu, ternyata kakaknya seru banget, lucu juga.",  
                "pesan":"Semangat kuliahnya ya kak, selamat udah jadi staff of the month, jujur keren banget"# 8
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450012",
                "umur": "18",
                "asal":"Jakarta",
                "alamat": "Sebelah kost kak Vany",
                "hobbi": "Goreng ayam",
                "sosmed": "@_haikaaall",
                "kesan": "abangnya baik banget dan seru selama wawancara tuh!!",  
                "pesan":"Semoga perkuliahannya selalu dilancarkan bang"# 9
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@putrimannaa",
                "kesan": "Kakaknya cantik dan baik bangett, suka sama senyumannya manis banget",  
                "pesan":"Semangat terus kuliahnya kak"# 10
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450063",
                "umur": "19",
                "asal":"Tangerang kota",
                "alamat": "Sebelah kamar Biwa",
                "hobbi": "badminton",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya baik banget dan seru kalo diajak ngobrol",  
                "pesan":"Semoga segala urusannya dilancarkan ya kak"# 10
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "23",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Bang Desman orangnya kerenn, dan juga asikk, baikk. kenalnya waktu FG Sains Data, disitu abangnya banyak cerita-cerita lucu",  
                "pesan":"Semoga bang desman selalu didekat hal-hal baikk"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung",
                "alamat": "Sukarame",
                "hobbi": "pilates",
                "sosmed": "@azzelytn",
                "kesan": "Kak Azzel orangnya humble, dan juga baikkk sekali",  
                "pesan":"Semoga semua keinginan kak azzel tercapai"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus peternakan",
                "sosmed": "@charrlln",
                "kesan": "Kak Charrlindah orangnya baikk, dan juga ramah",  
                "pesan":"Semoga kak charlindah dikelilingi hal-hal baik"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Bang Jemar orangnya kerenn apalagi saat damaskus",  
                "pesan":"Semoga bang jeremi bisa menggapai semua keinginannya"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main Roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kak Nabila orangnya humble, dan juga baik, ramah jugaa",  
                "pesan":"Semoga kak nabila mendapatkan hal-hal yang diinginkan"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearrfkvmfl",
                "kesan": "Bang Rafli orangnya humble , baik, dan juga ramah",  
                "pesan":"Semoga bang rafli selalu bisa mencapai semua keinginannya"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Jatimulyo",
                "hobbi": "Minum air putih",
                "sosmed": "@avi.nhr",
                "kesan": "Kak Salavi orangnya seru, dan juga baik, ramahh",  
                "pesan":"Semoga kak salavi selalu didekatkan dengan hal-hal baikk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

if menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VH42xi_IUv-_Emp1_kHv4gUsBWxGU-Lm",
            "https://drive.google.com/uc?export=view&id=134PCNlfoJm8QOottXy8-MyZGJss4RBp1",
            "https://drive.google.com/uc?export=view&id=1b1BTkqErNIjciLfQS7BA-StzXK4Mzfsq",
            "https://drive.google.com/uc?export=view&id=1PZpCUg59Iz-es0dOojCrAXB7ceKdGlru",
            "https://drive.google.com/uc?export=view&id=1jgib2SdAXhv975xhTV4oGD31ZvhbuXCc",
            "https://drive.google.com/uc?export=view&id=19khIgsPY8T5uVzMW4UJFiu2DaHwcEGHX",
            "https://drive.google.com/uc?export=view&id=1s4vQJnmvbWui_xyqwrm5oXmOMTeQQsIr",
            "https://drive.google.com/uc?export=view&id=1qvTqoejpzOGkJ0NOprV5Zn8Hbn0VYZKp",
            "https://drive.google.com/uc?export=view&id=1ZMJ627XOaDBYPru269k8VsLHDFr2YvbH",
            "https://drive.google.com/uc?export=view&id=1egXh4XKBqig2vXfbulkm9SnOASs-Q-Xu",
            "https://drive.google.com/uc?export=view&id=122NEVojaihUDF2rmr8khc37IG70DzPbP",
            "https://drive.google.com/uc?export=view&id=1-V_Fbkd2Pgp4PjEIGesuvUsu7578h7VQ",
            "https://drive.google.com/uc?export=view&id=1HezxZ4848ol4dOKgfRUYeO_BLvY8Xpin",
            "https://drive.google.com/uc?export=view&id=1KX9xNwPyphQJn0B0iAWMTlcaOf4PvuNY",
            "https://drive.google.com/uc?export=view&id=1U0wV1rrxvzRzwEpERbawHV4XTI6UBok9",
            "https://drive.google.com/uc?export=view&id=1aPeFr15FGQMlBCIg9W13rTDRYLoVMjhu",
            "https://drive.google.com/uc?export=view&id=1CMRqwHoepKtuxkI9tGlqPxxn39z6zPZt",
            "https://drive.google.com/uc?export=view&id=1s6J5lnRExHAE2lNukYUB3Oyi87_aHLwD",
            "https://drive.google.com/uc?export=view&id=1LzJAmbYCF03WOBgsfMyn1aS2PuB6VEnn",
            "https://drive.google.com/uc?export=view&id=1zPipD8QFEZfLVzbVut-TsRKiZoCgUePD",
            "https://drive.google.com/uc?export=view&id=1K3I2YIqL4LcleSL0QDJ76zsN07Z0CM7C",
            "https://drive.google.com/uc?export=view&id=1TrKOnx9yQ_I-F9X0QQ46XBPGNFopMmBC",
        ]
        data_list = [
            {
                "nama": "Arini Puteri Elandra",
                "nim": "123450069",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Teluk Betung Selatan",
                "hobbi": "Nonton Kartun",
                "sosmed": "@elandraa_",
                "kesan": "kenal kak arini dari bang dear karena mereka temenan dari PPLK, udah sempat ngobrol juga tapi pas bareng bang dear sih, soalnya kalo gaada bang dear bingung gitu mau ngomongin apa. terus ternyata kakaknya jadi kadep itu eksternal, di departemen yang aku mau, jadi seneng banget soalnya berharap bisa lebih akrab lagii",  
                "pesan":"semangat kuliahnya ya kak, semoga segala urusannya dilancarkan ya"# 1
            },
            {
                "nama": "Nabyla Sharfina",
                "nim": "123450008",
                "umur": "20",
                "asal":"Bengkulu",
                "alamat": "Jalan Lapas",
                "hobbi": "Jalan-jalan",
                "sosmed": "@bylaash",
                "kesan": "kakaknya cantik dan baik bangett",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Aditya Taufiqurrohman",
                "nim": "123450032",
                "umur": "21",
                "asal":"Tetangga Kadep",
                "alamat": "Belwis",
                "hobbi": "Mancing Keributan",
                "sosmed": "@adityafq",
                "kesan": "udah tau abangnya dari masa PPLK disitu abangnya perhatian banget sih, terus waktu udah magang di pengmas abangnya ternyata asik juga, bener-bener ngebimbing banget sih selama magang",  
                "pesan":"Semangat terus kuliahnya bang, mohon bimbingannya selama magang"# 3
            },
            {
                "nama": "Khoirul Mutthoharoh",
                "nim": "1234500",
                "umur": "21",
                "asal":"Lampung Barat",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@khoirul_muttoharoh",
                "kesan": "awal ketemu waktu latihan basket, ternyata kecil-kecil jago banget main basketnya, bener-bener sejago itu aku salut dan kagum banget ke kakaknya",  
                "pesan":"Selamat udah lolos EXVOLTAS nya kakk! btw rindu main basket lagii bareng yang lain, soalnya pengen diajarin sama kakak"# 4
            },
            {
                "nama": "Selma Siti Aisyah",
                "nim": "123450044",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Jalan-jalan",
                "sosmed": "@selmasiti_aisyah",
                "kesan": "waktu wawancara itu ngira kakaknya pendiem gitu, ternyata pas magang kakaknya periang banget, suka ngajakin buat konten pokoknya",  
                "pesan":"mohon bantuan dan bimbingannya ya kak, bakal rindu masa-masa magang"# 5
            },
            {
                "nama": "Ashila Islamisahfa Vanisha",
                "nim": "124450028",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Natar",
                "hobbi": "Tidur",
                "sosmed": "@kshigf",
                "kesan": "kakaknya seru bangett apalagi waktu survei itu, ngebimbing banget soalnya linglung survei itu ngapain aja karena pertama kali ikut survei",  
                "pesan":"semangat kuliahnyaa ya kak dan tetap ada di divisi ini"# 6
            },                      
            {
                "nama": "Indah Khairunnisa",
                "nim": "124450077",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Disini aja",
                "hobbi": "mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "sosmed": "@khaindaa_",
                "kesan": "semoga segala urusan perkuliahannya dilancarkan ya kak"# 7
            },
            {
                "nama": "Bima Ekayasa",
                "nim": "1244500106",
                "umur": "20",
                "asal": "Lampung",
                "alamat": "bandar Lampung",
                "hobbi": "Berlaku humoris dan manis",
                "sosmed": "@bimayasa_",
                "kesan": "abangnya seru sih, apalagi waktu magang bareng divisi hublu disitu abangnya lucu sih",  
                "pesan":"semoga dilancarkan dalam semua urusannya ya bang, terutama dalam kegiatan selanjutnya yaitu viscom, semoga kami anak magang bisa join ya"# 8
            },
            {
                "nama": "Ahmad Bimo Akbar Arkana",
                "nim": "124450113",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Bandar Lampung",
                "hobbi": "lihat lihat perumahan ",
                "sosmed": "@bimo_arkana",
                "kesan": "abangnya tinggi banget, seru banget  kalo diajak ngobrol",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"# 9
            },
            {
                "nama": "Adinda Deswita Maharani",
                "nim": "124450083",
                "umur": "20",
                "asal":"Ikut Kadep",
                "alamat": "Love earth",
                "hobbi": "Jadi Idol",
                "sosmed": "@adindaadma",
                "kesan": "kakaknya lucu imut gitu, warna rambutnya juga lucu banget",  
                "pesan":"Semangat kuliahnya ya kak"# 10
            },
            {
                "nama": "Yollanda Agustina",
                "nim": "124450024",
                "umur": "20",
                "asal":"Kerangka Bawang Sebelah Barat",
                "alamat": "Kayu Mulya",
                "hobbi": "Tanya bang Henry",
                "sosmed": "@yollanda_agustina16",
                "kesan": "Kakaknya baik, lucu, dan seru banget!",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Riska Erlis Dayu Tiara",
                "nim": "124450022",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Bebas",
                "hobbi": "Ngefollow up chat",
                "sosmed": "@erlsriska",
                "kesan": "kakaknya seru bangett, udah banyak ngobrol waktu magang, jadi panitia bareng di viscom",  
                "pesan":"mohon bantuannya selama jadi panitia viscom yaa kak"
            },
            {
                "nama": "Fathya Intami Gusda",
                "nim": "123450095",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Sukarame",
                "hobbi": "Baca wattpad",
                "sosmed": "@fatthyaa_",
                "kesan": "kakak cantikk, mirip sama kak sania loh kok bisa ya, gampang ketawa juga kakaknya tuh",  
                "pesan":"kapan bertemu lagi kak, udah kangen soalnya, kalo kakak ga dateng sepi banget rasanya"
            },
            {
                "nama": "Tarisya Hidayatul Rahmi",
                "nim": "1234500552",
                "umur": "21",
                "asal":"Luhak tanah data",
                "alamat": "Gerbang Barat",
                "hobbi": "Jadi orang baik",
                "sosmed": "-",
                "kesan": "kakaknya periang banget sih, jujur sangat-sangat seru selama aku magang",  
                "pesan":"aku juga udah rindu kakak, rindu kelucuan kakak"
            },
            {
                "nama": "Danil N Fadillah",
                "nim": "123450103",
                "umur": "19",
                "asal":"Karawang",
                "alamat": "Belakang Polda",
                "hobbi": "Ngasih makan ikan cupang",
                "sosmed": "@d4niel_fdlh",
                "kesan": "ini nih bang duta yang suka kalo udah dibilang kalcer, ternyata suka cerita-cerita gitu walaupun terlihat cool",  
                "pesan":"ayo gabung pengmas lagi, biar bisa cerita-cerita lagi"
            },
            {
                "nama": "Favian Arkaanda",
                "nim": "123450021",
                "umur": "20",
                "asal":"Swiss",
                "alamat": "Tanya bapas",
                "hobbi": "Ngesen kanan",
                "sosmed": "@fvnnn05",
                "kesan": "bang vian kenapa ekspresi mukanya suka sigma mulu ya, mukanya juga gampang merah haha, jadi pengen sering muji abangnya biar liat muka merahnya terus",  
                "pesan":""
            },
            {
                "nama": "Muhammad Fathiy Zumar Yazid",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "jujur kaget sih ternyata abangnya di departemen eksternal, karena sering liat di rangkaian. tapi abangnya emang ga cocok kalo marah-marah gitu, karena mukanya lucu gitu. selama magang juga ternyata seru banget ya abang ini",  
                "pesan":""
            },
            {
                "nama": "Alfaya Abiyyi",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "abangnya kalem tapi ramah dan seru juga",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Muhammad Rizaldi",
                "nim": "123450093",
                "umur": "Masih muda lah",
                "asal":"Rahim Ibu",
                "alamat": "Pasar lantai 3.5",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@jaldii._",
                "kesan": "tau bang zaldi waktu jadi MC di PPLK, terus tau bang zaldi dari prodi sains data, aku merasa bangga gitu loh",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"
            },
            {
                "nama": "Saskia Nova Magdalena",
                "nim": "123450074",
                "umur": "20",
                "asal":"Lampung",
                "alamat": "Pinggir Jalan",
                "hobbi": "nonton thinkerbell",
                "sosmed": "@snova.19",
                "kesan": "kakaknya malu-malu gitu keliatannya, tapi seru banget kok",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Asri Meilani",
                "nim": "123450010",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Korpri Raya",
                "hobbi": "menonton film",
                "sosmed": "@asrmeilani",
                "kesan": "kakaknya cantik banget, kirain dari departemen medkraf soalnya liat postingan di ig nya tuh bagus-bagus banget. kakaknya juga ramah banget waktu wawancara itu",  
                "pesan":"Semoga segala perkuliahannya dilancarkan selalu ya kak"
            },
            {
                "nama": "Ahmad Rizky",
                "nim": "123450050",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "GH",
                "hobbi": "ga ngapa ngapain",
                "sosmed": "@ahmad.rizky___",
                "kesan": "waktu jadi maba pas tau abangnya jadi sekjen ngerasa bangga gitu, abang nim aku terkenal hehe. jujur salut banget abangnya selalu menyampaikan aspirasi",  
                "pesan":"semangat terus dalam menyampaikan aspirasinya bang"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

# INTERNAL
if menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Dy2WaPIP-mNApoBQUeZLTKx_zWDgXOEQ",
            "https://drive.google.com/uc?export=view&id=13_EQWhFOf6pOBc6tsKJjbAPMr-wrgZoS",
            "https://drive.google.com/uc?export=view&id=1by7KrPI41dF4wPV1fSd0ZBUKQ512GFGP",
            "https://drive.google.com/uc?export=view&id=1UM18LQ-quc6IjU8vCp5eA-DNPusDL8wP",
            "https://drive.google.com/uc?export=view&id=15JA2yj37_rjZYz0OWpBcxjYZo_X6dufO",
            "https://drive.google.com/uc?export=view&id=1hNuNNecoKJIgrLgVbo2sE08s28vxur4m",
            "https://drive.google.com/uc?export=view&id=1r0Dz7pSnuaiuy-3wqn-oezQbHQSC5ywg",
            "https://drive.google.com/uc?export=view&id=1otWKDCiY1Vz9lbzIwm1ZhGO_YTUj-VXR",
            "https://drive.google.com/uc?export=view&id=1biioK3BWksrmRkie21KTVfPfk3makdn3",
            "https://drive.google.com/uc?export=view&id=1bkiO3NkrxbHtKv5tLixLq24MxB_tqldB",
            "https://drive.google.com/uc?export=view&id=1rcd4J1ihIyQcfw6pbjbvqDq7-B2TiD4P",
            "https://drive.google.com/uc?export=view&id=1ohuYo9WCmesejZIxFl6JHJkM8KscwUOX",
            "https://drive.google.com/uc?export=view&id=1ZrFG35pkXSVWF3F72yAR9bK65qxa1MG-",
            "https://drive.google.com/uc?export=view&id=1R1jOVZ8oRUC4HHquuvOqSUk50DQkWlTX",
            "https://drive.google.com/uc?export=view&id=1QKTwc1sAwzaJJuTR1WuBXom_NUF1klHW",
            "https://drive.google.com/uc?export=view&id=1Oq05V-zpmejQnitAV9U0meTOVe4yICB1",
        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450006",
                "umur": "20",
                "asal":"Silikalang Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Ngoding",
                "sosmed": "@haikalsbln_",
                "kesan": "keliatannya sih serem, aslinya lucu dan seru banget, apalagi waktu ngajakin buat tiktok kemarin",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal":"Untung Suropati",
                "alamat": "Untung Suropati",
                "hobbi": "Suka menolong orang",
                "sosmed": "@risma.mustika_",
                "kesan": "kakaknya lucu bangett trus cantik juga, kepribadiannya juga keliatan yang kalem gitu",  
                "pesan":"Semangat terus kak!"# 2
            },
            {
                "nama": "Muhammad Hanif Zaky",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang Sumatera Barat",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Ngikutin drama tiktok",
                "sosmed": "@hnfdzky_",
                "kesan": "Bang Aqil juga ga kalah keren! baik jugaa",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Kakaknya baik banget dan ramah!!",  
                "pesan":"Semangat terus kuliahnya kak!"# 4
            },
            {
                "nama": "Cika Adelia Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin dina ngomong bahasa Minang",
                "sosmed": "@cikamrbn",
                "kesan": "Kakaknya gemes dan lucu banget!",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"# 5
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Airan ",
                "hobbi": "-",
                "sosmed": "@gustin.tpb",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semangat terus kak!"# 6
            },                      
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "122450128",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "berkuda",
                "sosmed": "@muhvnz",
                "kesan": "abangnya kalem tapi ramah dan seru juga",  
                "pesan":"Semangat terus kak!"# 7
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal":"Natar",
                "alamat": "Natar",
                "hobbi": "Nitip makan sama Aqila",
                "sosmed": "snasaa._",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"Semangat terus kuliahnya kak!"# 8
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "Menyapa satpam Itera",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya baik dan ramah banget, enak banget kalo diajak ngobrol!!",  
                "pesan":"Semangat terus kuliahnya kakak!"# 9
            },
            {
                "nama": "A Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Olahraga menembak",
                "sosmed": "@farhanghani",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semangat terus kuliahnya bang"# 10
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "20",
                "asal":"Riau",
                "alamat": "Samping kuburan Belwis",
                "hobbi": "Suka eksperimen",
                "sosmed": "@aisyahkhair._",
                "kesan": "Kakaknya baik banget dan humble!!",  
                "pesan":"Semangat terus kak!"# 11
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450079",
                "umur": "19",
                "asal":"Medan",
                "alamat": "Pesisir Belwis",
                "hobbi": "Begadang",
                "sosmed": "cerine.ipynb",
                "kesan": "kakaknya aktif bangett, udah kenal dari acara natal HMSD dan ternyata kota aku dekat banget sama kakaknya",  
                "pesan":"semangat menjalani perkuliahannya kak"# 12
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "19",
                "asal":"Kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Buat lagu",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "abangnya keren banget waktu main basket, terus seru banget kalo diajak ngobrol!",  
                "pesan":"Semoga segala urusan perkuliahannya dilancarkan ya bang"# 13
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Belwis",
                "hobbi": "main ML",
                "sosmed": "@njlanursyifa",
                "kesan": "Kakaknya baik dan cantik banget!!",  
                "pesan":"Semangat terus kak!"# 14
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "18",
                "asal":"Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "isengin harvin di kelas",
                "sosmed": "@rozakramdani__",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"# 15
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Jadi asprak",
                "sosmed": "@christiani8872",
                "kesan": "Kakaknya baik dan pinter banget!!",  
                "pesan":"Semangat terus kak, kamu keren banget!"# 16
            },  
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

if menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qCfbcnUVB1QQ_jf3dYaFO-lcXlCMYfFX",
            "https://drive.google.com/uc?export=view&id=1UnclgEwvBOpNKho72s1H15E5pLkYk502",
            "https://drive.google.com/uc?export=view&id=1B2J36jOsJRO_LvbG4BrzpABF-rinBo5Z",
            "https://drive.google.com/uc?export=view&id=1Ibe2mCNsOcSXGhCr0kkG43q7kWkLKJhJ",
            "https://drive.google.com/uc?export=view&id=1CsKNxOjTlKG0tA1iD3-dIEv4B2a7wF9W",
            "https://drive.google.com/uc?export=view&id=1eOQzk2ouRS6h3mbgzF_aAHvkTGTaoGNA",
            "https://drive.google.com/uc?export=view&id=1rUyR9XilGsIP77ViFRT3t2NY_kh4EIX1",
            "https://drive.google.com/uc?export=view&id=1_9OU93Cc4Aor2380YlS7vf5FKkVGdSiz",
            "https://drive.google.com/uc?export=view&id=13F42jW8Qe1idKhxz1wA2sFBuL21X2dO6",
            "https://drive.google.com/uc?export=view&id=1oQFFP0XscBifLOElh254Eb81x7I8tFJZ",
            "https://drive.google.com/uc?export=view&id=1WlQJVARoAVaFtNrX_AjgqlZv6SGH5Xvy",
            "https://drive.google.com/uc?export=view&id=150mYH747InLwsoEN0enh5PYC4xcsAdko",
        ]
        data_list = [
            {
                "nama": "Ihsan Maulana Yusuf",
                "nim": "123450110",
                "umur": "21 Tahun",
                "asal":"Sumbar",
                "alamat": "Belwis",
                "hobbi": "Membaca, Mencari Jurnal, berdagang, dan traktir staff SSD",
                "sosmed": "@ihsan.myusuf",
                "kesan": "abangnya serus dan lucu banget waktu wawancara tuh",  
                "pesan":"semangat terus kuliahnya bang!!"# 1
            },
            {
                "nama": "Hanifah Inaya Sari",
                "nim": "123450123",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Masak",
                "sosmed": "@_inayasani",
                "kesan": "Kakak lucu gemes gitu, cantik banget banget",  
                "pesan":"semangat terus kuliahnya ya kak"# 1
            },
            {
                "nama": "Afifah Fauziah",
                "nim": "123450002",
                "umur": "19",
                "asal":"Padang",
                "alamat": "Hasan 4",
                "hobbi": "Nonton Marvel, Tidur",
                "sosmed": "@fifah.zy",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Hasan Nur Ramadhan",
                "nim": "124450012",
                "umur": "21",
                "asal":"lampung",
                "alamat": "Pemda",
                "hobbi": "Main game",
                "sosmed": "@hasan.ramadhan08",
                "kesan": "abangnya tinggi banget, trus keliatan pendiem gitu",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Layina Ropiqo",
                "nim": "124450016",
                "umur": "19 tahun",
                "asal":"Semarang",
                "alamat": "Balam",
                "hobbi": "Nonton Drakor",
                "sosmed": "@lay.inr_",
                "kesan": "Kakak ini asik dan baik banget",  
                "pesan":"semangat selalu kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Moch. Iqbal Az-Zahir",
                "nim": "124450052",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Natar",
                "hobbi": "Mancing",
                "sosmed": "@iqbalazzahir_",
                "kesan": "abangnya pinter banget terus lucu juga",  
                "pesan":"semangat terus kuliahnya bang! kasih tips biar bisa ozt"# 1
            },
            {
                "nama": "Talitha Justine",
                "nim": "124450076",
                "umur": "19",
                "asal":"Sumbar",
                "alamat": "Kelengkeng 5",
                "hobbi": "Tidur",
                "sosmed": "@talithaaajtine",
                "kesan": "Kakak ini lucu dan gemes banget aku suka kakak ini",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!!!"# 1
            },
            {
                "nama": "Anadia Carana",
                "nim": "123450019",
                "umur": "19",
                "asal":"Palembang",
                "alamat": "Wayhui",
                "hobbi": "Nyari Duit",
                "sosmed": "@anadiacrn_",
                "kesan": "Kakaknya cantik dan pinter banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Abdillah Fikri Al pome",
                "nim": "123450062",
                "umur": "21",
                "asal":"Sumsel",
                "alamat": "Airan",
                "hobbi": "Basket",
                "sosmed": "@pomest_",
                "kesan": "pertama kali ngobrol waktu latihan basket, trus pas liat abangnya main basket kok jago banget, kirain di departemen minbak ternyata bukan",  
                "pesan":"semangat kuliahnya bang, semoga di IO nanti menang ya"# 1
            },
            {
                "nama": "Afdhal Rahmad Setiawan",
                "nim": "124450008",
                "umur": "20",
                "asal":"Sumbar",
                "alamat": "Samping kost rafli",
                "hobbi": "Fishing",
                "sosmed": "@dhal_setiawan",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"# 1
            },
            {
                "nama": "Anggun Nita",
                "nim": "124450009",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@anggunnitaaa_",
                "kesan": "Kakak ini seru dan ramah banget",  
                "pesan":"semangat selalu kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Della Anisa Fitri",
                "nim": "124450095",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Nargo Lestari",
                "hobbi": "Olahraga, Makan makanan manis",
                "sosmed": "@dellaansaftr",
                "kesan": "Kakak ini manis dan cantik bangett",  
                "pesan":"semoga segala urusan perkuliahannya dilancarkan !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

if menu == "Departemen Medkraf":
    def Medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1t8Z1QQ9ZyTw7OUy1FgWwu7QyVD3_Ghl_",
            "https://drive.google.com/uc?export=view&id=1voB_4NT1MAarGXrMKeLGyB1YPmqiAmJI",
            "https://drive.google.com/uc?export=view&id=185r10aTQWS29l3H17vi8w3SjAT0J7YkF",
            "https://drive.google.com/uc?export=view&id=1dAOxmFSJeUqHuOIlFDw0wZZUEjobzrXA",
            "https://drive.google.com/uc?export=view&id=1bIj5B269yHei8_cP4wrBTLFC1QDJMtEQ",
            "https://drive.google.com/uc?export=view&id=1DcPuI-04Svxoxd8OXBqaIntmtQLk6f3M",
            "https://drive.google.com/uc?export=view&id=114PdMhYYXwMVp4BK2J2znRDNImbEsXyL",
            "https://drive.google.com/uc?export=view&id=1HtAgDM57fyiJKpx2BYiEoHH6YYr9Xzrj",
            "https://drive.google.com/uc?export=view&id=1-_liH4pqN3RphAeKyo1FT6lFHj8Yo8i2",
            "https://drive.google.com/uc?export=view&id=1Jo6Dqt2ueL5qqLut7rco13Tad9aaM4fh",
            "https://drive.google.com/uc?export=view&id=1b6juagMAQpqVljKq_RLVpZohQiOl1R0E",
            "https://drive.google.com/uc?export=view&id=1o_8vV9m8WJpLN58wIGa4iKwphX890wOx",
            "https://drive.google.com/uc?export=view&id=1YmNRpVvUiOVl4e8HVa8Fv6aBdJ5liM85",
            "https://drive.google.com/uc?export=view&id=1bXoqZ2Zi_C8AEsB_dNzkoMTHweksBIsY",
            "https://drive.google.com/uc?export=view&id=19GZFOd0gVKbAwCPBQ2ONd0ezq-g0AOUi",
            "https://drive.google.com/uc?export=view&id=1puCbZ6ZUoV43fwI4LbrkGEQOqkHIe8Zh",
            "https://drive.google.com/uc?export=view&id=1DbguYb80_prM0j9rTddXXipU5Hk7l5U9",
            "https://drive.google.com/uc?export=view&id=1rTb2llk0G6-gCO6LfvDj_v6A8WdS_3nR",
        ]
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa",
                "nim": "123450082",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Musingin TA",
                "sosmed": "@naylasalsabilaa._",
                "kesan": "penjelasan waktu wawancara dari kakaknya bener-bener gampang dipahami",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Donna Maya Puspita",
                "nim": "123450028",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Way Huwi",
                "hobbi": "Berenang",
                "sosmed": "@donnamaya.p",
                "kesan": "kakaknya ramah dan seru banget",  
                "pesan":"semoga segala urusannya dilancarkan ya kak"# 2
            },
            {
                "nama": "Labo John Noel Napitupulu",
                "nim": "123450037",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Way Huwi",
                "hobbi": "Nonton tong setan",
                "sosmed": "@noerruuu",
                "kesan": "abangnya seru diajak ngobrol, terus lucu juga apalagi waktu jadi pemateri streamlit",  
                "pesan":"Semangat terus bang!"# 3
            },
            {
                "nama": "Sania Dwi Ayu Lestari",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik dan cantik banget!!",  
                "pesan":"Semoga semangat selalu kuliahnya!"# 4
            },
            {
                "nama": "Raihanna Adelia Putri",
                "nim": "123450041",
                "umur": "20",
                "asal":"Terbanggi Besar",
                "alamat": "Airan Raya 1",
                "hobbi": "Menulis dan membaca",
                "sosmed": "@n1tg.-",
                "kesan": "Kakaknya ramah dan seru banget!!",  
                "pesan":"Semangat terus kuliahnya kakak!"# 5
            },
            {
                "nama": "Alya Ramadhanti",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "Kakaknya baik dan ramah banget banget!!",  
                "pesan":"Semoga semangat selalu kuliahnya!"# 6
            },                      
            {
                "nama": "Bunga Clarisa Sefa",
                "nim": "124450097",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Pemda",
                "hobbi": " Belajar",
                "sosmed": "@bungaclrssf",
                "kesan": "Kakaknya cantik dan ramah banget!!",  
                "pesan":"Semangat terus dalam perkuliahannya kak!"# 7
            },
            {
                "nama": "Muhammad Razan Maulana Pratama",
                "nim": "1244500031",
                "umur": "18",
                "asal": "Rumah",
                "alamat": "Ryacudu",
                "hobbi": "Bully Felisya Nabila Nugroho",
                "sosmed": "@muh_razan_",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semangat terus bang!"# 8
            },
            {
                "nama": "Anash Tasya Ausyaqila",
                "nim": "124450050",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Way Halim",
                "hobbi": "Nonton F1",
                "sosmed": "@anshtsyaaql",
                "kesan": "akhirnya ketemu sama kak anashh, ternyata ada beberapa kesamaan!",  
                "pesan":"Semangat terus kuliahnya kak! semoga kita lebih banyak ngobrolnya ya kak"# 9
            },
            {
                "nama": "Felisya Nabila Putri Nugroho",
                "nim": "124450014",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mancing",
                "sosmed": "@adindaadma",
                "kesan": "Kakaknya imut dan lucu banget!!",  
                "pesan":"Semoga semangat selalu kuliahnya!!"# 10
            },
            {
                "nama": "Difanya Husakina",
                "nim": "124450043",
                "umur": "Gaada yang tau",
                "asal":"Rumah bapak",
                "alamat": "Gedung F",
                "hobbi": "Ngitungin beras di karung",
                "sosmed": "@difanyhsa",
                "kesan": "Kakaknya cantik banget udah cocok banget masuk departemen ini!",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Zannuba Arifah Ilman",
                "nim": "1244500112",
                "umur": "19",
                "asal":"Jabung",
                "alamat": "Rajabasa",
                "hobbi": "Bobo",
                "sosmed": "@Xifasky",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"Sehat dan semangat terus ya kak!"
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya cantik dan lucu banget!!",  
                "pesan":"Semoga semangat selalu kuliahnya!"
            },
            {
                "nama": "Edsel Adya Pradipta",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@edsel_0712",
                "kesan": "abangnya keliatan pendiem gitu sih",  
                "pesan":"Semangat terus bang!"
            },
            {
                "nama": "Daffa Kharisma Adzana",
                "nim": "124450061",
                "umur": "21",
                "asal":"Surabaya",
                "alamat": "SUkarame",
                "hobbi": "Nyuluh Manuk",
                "sosmed": "@daffascript_",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"
            },
            {
                "nama": "Nazlah Auliya",
                "nim": "124450054",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Main Piano",
                "sosmed": "@nzlhauly",
                "kesan": "Kakaknya lucu dan gemes banget!!",  
                "pesan":"semoga segala urusannya dilancarkan ya kak"
            },
            {
                "nama": "Allisha",
                "nim": "123450081",
                "umur": "20",
                "asal":"situlah",
                "alamat": "pohon mulia",
                "hobbi": "nyari hobi",
                "sosmed": "@zydddddd__",
                "kesan": "kaget banget pas tau kakaknya dari departemen medkraf, soalnya sering liat kakaknya main pas damaskus",  
                "pesan":"Semangat terus kuliahnya kak!"
            },
            {
                "nama": "Shafa Delaila Azzahra",
                "nim": "123450006",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "makan yang manis biar manis",
                "sosmed": "@alfabiyi",
                "kesan": "Kakaknya cantik banget, seru juga kalo diajak ngobrol",  
                "pesan":"Semangat kuliahnya kak!"
            },                                                                          
        ]
        display_images_with_data(gambar_urls, data_list)
    Medkraf()

if menu == "Departemen Minbak":
    def Minbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10DaNy71dwJ0U0vPLGYLhhwPKmayhxgoV",
            "https://drive.google.com/uc?export=view&id=1CIHuF6QpbHfetWm1jdUS0BKjH3K4BZVh",
            "https://drive.google.com/uc?export=view&id=1LVgkH49eIH3sjCI9_iUAtqwxuiPzL0lx",
            "https://drive.google.com/uc?export=view&id=1pM4ODCLyItCLUhNRq3Y9DhfJlzLs2BJp",
            "https://drive.google.com/uc?export=view&id=1vZnsXgjYX2iUzbCGelV2sjlP17FYplLt",
            "https://drive.google.com/uc?export=view&id=1nBVNBJnOUjF0o6J6NB_RkqgBipiJ92n4",
            "https://drive.google.com/uc?export=view&id=1u42S1OK5stQUXb7PsXL4_Nd1Jqg2uM85",
            "https://drive.google.com/uc?export=view&id=1uk9W8RcSu-0CJPWxQYW1aKzoaJTo2Ka6",
            "https://drive.google.com/uc?export=view&id=1mDUexD3NqRnmnz1-uJHoFOb4KksYfK45",
            "https://drive.google.com/uc?export=view&id=1uKMThjVNN55q8_LHMRoxKmBgecbAfxIM",
            "https://drive.google.com/uc?export=view&id=1DLtZ2dY8IWJHcRJpRLizkmpMVTJ-9lzs",
            "https://drive.google.com/uc?export=view&id=1G1L0S2d2tueECd5A583n_JP7txB3MAN5",
            "https://drive.google.com/uc?export=view&id=1-zuUpJr8iQLlyiqE99KlA-klPTE-6qXr",
            "https://drive.google.com/uc?export=view&id=1f6F3NLcdNE1BwKoMRtviTfq85vMt3OON",
            "https://drive.google.com/uc?export=view&id=1TBVXtbhc8YkQMfwz0FoDtXS0uif_G6ki",
        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal":"Payakumbuh",
                "alamat": "Way Huwi",
                "hobbi": "Lari",
                "sosmed": "@kevinaj_",
                "kesan": "abangnya keliatan pendiem gitu loh awal-awal ikut latihan basket, ternyata makin sering latihan makin banyak ngobrolnya juga, seru banget",  
                "pesan":"semangat terus kuliahnya bang, semoga di IO menang ya"# 1
            },
            {
                "nama": "Gusti Putu Ferazka D.",
                "nim": "123450046",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Way Dadi",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kirain kakaknya cowo soalnya namanya cowo banget, aku juga gatau arti nama depannya tuh, pas ketemu di wawancara ternyata cewe terus cantik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 2
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@ali_parisi3",
                "kesan": "abangnya seru diajak ngobrol, ramah, dan baik juga",  
                "pesan":"Semangat terus bang!"# 3
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450086",
                "umur": "21",
                "asal":"Karawang",
                "alamat": "Airan",
                "hobbi": " Nongkrong depan ruang prodi",
                "sosmed": "@saniayyllstr",
                "kesan": "Kakaknya baik dan ramah banget!!",  
                "pesan":"semoga segala urusannya dilancarkan ya kak"# 4
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450121",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Motoran bareng bang bryan",
                "sosmed": "@dafaelpriza_",
                "kesan": "Sangat menyenangkan dan mudah diajak kerja sama!",  
                "pesan":"Semangat terus dalam perkuliahannya kak!"# 5
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450091",
                "umur": "19",
                "asal":"Jambi",
                "alamat": "Airan",
                "hobbi": "Jalan-jalan dengan sepatu rodaku",
                "sosmed": "@alya.rmdhnti",
                "kesan": "kak juwii seru banget, katanya sih ga jago basket, ternyata mantan pemain basket loh ya, jago banget lagi",  
                "pesan":"Semangat terus kak kuliahnya, sering sering ikut latihan basket ya"# 6
            },                      
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jalan Pulau Damar",
                "hobbi": "Menjawab soal dari dosen dipapan tulis",
                "sosmed": "@afdal.03",
                "kesan": "Kakaknya baik dan lucu banget!! seru banget kalo  diajak ngobrol",  
                "pesan":"Semangat terus bang!"# 7
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "1244500024",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang ke Metro",
                "sosmed": "@slbnzw",
                "kesan": "Kakaknya baik dan ceria banget!!",  
                "pesan":"Semangat terus kuliahnya kak!"# 8
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nonton F1",
                "sosmed": "@mridwaan_22",
                "kesan": "Kakaknya baik dan bertanggung jawab banget!!",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"# 9
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@andra.lhm",
                "kesan": "awal ketemu itu waktu latihan basket, disitu masih keliatan pendiem gitu, tapi ternyata lucu banget loh abang ini, selama latihan tuh sabar banget ngelatihnya, kaya orang gaenakan gitu padahal gapapa juga kalo latihannya diseriusin. bang andra juga perhatian banget, ngebantu aku waktu masih sakit itu. pokoknya sayang bang andra banyak-banyak",  
                "pesan":"terimakasih bimbingannya selama latihan ya bang, maaf selalu ngeluh gabisa main. semangat terus kuliahnya, semoga segala urusannya dilancarkan ya"# 10
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Motoran",
                "sosmed": "@bryantel_",
                "kesan": "abangnya lucu tapi pendiem gitu",  
                "pesan":"Semangat dalam beraktivitasnya bang!"
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "1244500067",
                "umur": "17",
                "asal":"Semarang",
                "alamat": "Kemiling",
                "hobbi": "Ternak sapi",
                "sosmed": "@meardhy_ghiyats",
                "kesan": "abangnya unik dan baik banget!!",  
                "pesan":"Semangat terus kak!"
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450095",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Belwis",
                "hobbi": "Mencintai Andrew Garfield",
                "sosmed": "@luciarchel_",
                "kesan": "Kakaknya baik dan ceria banget!!",  
                "pesan":"sukses terus perkuliahannya kak!"
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "124450098",
                "umur": "20",
                "asal":"Lampung Selatan",
                "alamat": "Natar",
                "hobbi": "Scroll Fesbuk",
                "sosmed": "@cacalvra",
                "kesan": "kakaknya keren banget, aktif banget pokoknya",  
                "pesan":"Semangat terus kuliahnya kakak!"
            },
            {
                "nama": "Muhammad Rafka fatih Al Ghathfaan",
                "nim": "124450023",
                "umur": "18",
                "asal":"Kalimantan Barat",
                "alamat": "Korpri",
                "hobbi": "Tukang Parkir",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakaknya baik banget!!",  
                "pesan":"Semoga sehat dan perkuliahannya dilancarkan selalu!"
            },                                                                         
        ]
        display_images_with_data(gambar_urls, data_list)
    Minbak()
