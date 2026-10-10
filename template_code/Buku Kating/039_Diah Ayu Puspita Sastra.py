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
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen Medkraf",
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
            "https://drive.google.com/thumbnail?id=19ROTFld7HX_F3wFMyVcUo7XE0ecja5lT&sz=w1000",
            "https://drive.google.com/thumbnail?id=1kuYd6XlUje4KOP8Jtnu7mZNH9B1X2j6q&sz=w1000",
            "https://drive.google.com/thumbnail?id=14eTxLiIzl9YHXokX2YKuA9W79ggcutgJ&sz=w1000",
            "https://drive.google.com/thumbnail?id=1ESX89iJstfPzDnwTjA6ad1JiGTEUcxq7&sz=w1000",
            "https://drive.google.com/thumbnail?id=1HzXgBcN_BZPJ1-JSBUDCRBVSxeP9vDgj&sz=w1000",
            "https://drive.google.com/thumbnail?id=1-_VaDONRYup5c1H5ttDwOYA6ClADusc_&sz=w1000"
        ]
        
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung", 
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu", 
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Belum",
                "pesan" : "Belum"
            },
            {
                "nama": "Muhammad Aqil Ramadhan", 
                "nim" : "123450066",
                "asal" : "Riau",
                "alamat" : "Kotabaru", 
                "hobbi": "Dzikir",
                "umur" : "22",
                "sosmed" : "@Muhammadaqil1111",
                "kesan" : "Sosoknya tenang dan mengayomi.",
                "pesan" : "Tetap jadi kakak yang bisa diandalkan, Kak."
            },
            {
                "nama": "Efi Defiyati", 
                "nim" : "123450005",
                "asal" : "Lampung Timur",
                "alamat" : "Airan",
                "hobbi": "Membaca",
                "umur" : "21",
                "sosmed" : "@eeffiidefi",
                "kesan" : "Sosoknya ramah dan penuh semangat.",
                "pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
            },
            {
                "nama": "Qois Olifio", 
                "nim" : "123450067",
                "asal" : "Batam",
                "alamat" : "Kotabaru",
                "hobbi": "Mainin surat",
                "umur" : "22",
                "sosmed" : "@qoisolifio_",
                "kesan" : "Cara bicaranya santai tapi berisi.",
                "pesan" : "Jangan bosan membagi ilmu ke kami."    
            },
            {
                "nama": "Hafsa Fazilah Arradhi", 
                "nim" : "123450079",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung", 
                "hobbi": "Bertemu luluk",
                "umur" : "21",
                "sosmed" : "@hafsafazilahh",
                "kesan" : "Senyumnya hangat dan bikin suasana cair.",
                "pesan" : "Tetap jadi kakak yang ramah, ya, Kak."
            },
            {
                "nama": "Luthfia Laila Ramadhani", 
                "nim" : "123450004",
                "asal" : "Bengkulu",
                "alamat" : "Airan",
                "hobbi": "Keliling Balam",
                "umur" : "20",
                "sosmed" : "@luthhifiarmdhni",
                "kesan" : "Sosoknya ramah dan penuh semangat.",
                "pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

# Tambahkan menu lainnya sesuai kebutuhan

if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
           "https://drive.google.com/thumbnail?id=1BQ3XIi_QhqQrIDLohrH4aeejyzz7Fs8n&sz=w1000",
           "https://drive.google.com/thumbnail?id=1gmec5FZFyEQCUESVROO2AAt3aNa-M1f1&sz=w1000",
           "https://drive.google.com/thumbnail?id=1pxFtvTk_bXfVuj3PeKop2YxpDI7EVhOx&sz=w1000",
           "https://drive.google.com/thumbnail?id=1ih2qhiior-rvT1Rk3u329EtfHcYkttD7&sz=w1000",
           "https://drive.google.com/thumbnail?id=1qGRbcloEbheEolHYHoDgrCFB_lAKMalB&sz=w1000",
           "https://drive.google.com/thumbnail?id=1lx8F4yeaCkxm2JP3Opnsc5mbbBN0KCMf&sz=w1000",
           "https://drive.google.com/thumbnail?id=18IaqL6UjD9sh5WoyC8ptMN2_GN-iwcBM&sz=w1000",
           "https://drive.google.com/thumbnail?id=1uGPFIN2Go5-hVbh_KCfObzEH6MRS0STM&sz=w1000",
           "https://drive.google.com/thumbnail?id=1zhmS4F4K4BjLw5sdFJWo85TIHnZB37Hm&sz=w1000",
           "https://drive.google.com/thumbnail?id=1LzWsEijwv-qSfU5Cqj5AXD25M3vdA_N9&sz=w1000",
           "https://drive.google.com/thumbnail?id=1NPiwo6KIIqL7gAsWsU_emsIBrdPYb84L&sz=w1000",
           "https://drive.google.com/thumbnail?id=1QNyNI-bo_ABugNnAypV1wghv345eHc99&sz=w1000",
           "https://drive.google.com/thumbnail?id=10jbhS5iKBOAc5MnSXvGAtTMbKr1liUOJ&sz=w1000",
           "https://drive.google.com/thumbnail?id=11EuDo6T3Nhc1dNrR1Tl9Q5h10p9xKf9w&sz=w1000",
           "https://drive.google.com/thumbnail?id=1g9KbyKsIQUI1SzLyN61DpKVigRHwZjOx&sz=w1000",
           "https://drive.google.com/thumbnail?id=1Zd9hjH9A9G61kq0Kl02uJB0YA44E9DvW&sz=w1000"
        ]
        
        data_list = [
            {
                "nama": "Haikal Fransisko Simbolon",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Humornya sederhana tapi bikin akrab.",
                "pesan": "Jaga suasana cair tanpa berlebihan."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Cara bicaranya lembut tapi tegas.",
                "pesan": "Jangan ragu terus membimbing kami dengan sabar."
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "nim": "",
                "umur": "",
                "asal": "",
                "alamat": "",
                "hobbi": "",
                "sosmed": "",
                "kesan": "Perhatiannya ke adik tingkat sangat besar.",
                "pesan": "Semoga kebaikan Kakak selalu kembali."
            },
            {
                "nama": "Ahmad Farhan Ghani",
                "nim": "123450121",
                "umur": "21",
                "asal": "Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Supporteran",
                "sosmed": "@farhanghani",
                "kesan": "Tegas saat mengambil keputusan.",
                "pesan": "Tetap adil dan pertimbangkan banyak hal."
            },
            {
                "nama": "Aisyah Khairun Nisa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Indragiri",
                "alamat": "Samping Makam Perwira 2",
                "hobbi": "Nyicipin Makanan",
                "sosmed": "@aisyahkhair._",
                "kesan": "Selalu rapi dan enak dilihat.",
                "pesan": "Tetap jadi panutan tanpa harus menggurui."
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Belwis",
                "hobbi": "Suka Ngoding pakai R",
                "sosmed": "@cerine_ipynb",
                "kesan": "Pintar menenangkan saat kami panik.",
                "pesan": "Terus jadi tempat cerita yang aman."
            },
            {
                "nama": "Jaya Saputra Tamba",
                "nim": "124450094",
                "umur": "18",
                "asal": "Medan",
                "alamat": "Pemda",
                "hobbi": "Mencari Nafkah",
                "sosmed": "@jay.saputra.mb",
                "kesan": "Suka membantu tanpa pamrih.",
                "pesan": "Semoga kebaikan Kakak berbuah baik."
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Belwis",
                "hobbi": "Nonton ASMR",
                "sosmed": "@njlanursyifa",
                "kesan": "Humornya segar dan tidak berlebihan.",
                "pesan": "Jaga energi positif itu sampai kapan pun."
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "19",
                "asal": "Kalianda, Lampung Selatan",
                "alamat": "Korpri Raya",
                "hobbi": "Berantemin Kucing",
                "sosmed": "@rozakrabbani__",
                "kesan": "Disiplin dan tepat waktu.",
                "pesan": "Tularkan kebiasaan itu ke adik tingkat."
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "19",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Masak",
                "sosmed": "@kristiani8872",
                "kesan": "Tegas saat organisasi butuh keputusan.",
                "pesan": "Tetap adil dan bijak dalam memimpin."
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal": "Padang",
                "alamat": "Way Kandis",
                "hobbi": "Nonton F1 & MotoGP",
                "sosmed": "@hnfdzky_",
                "kesan": "Berwibawa tanpa harus marah.",
                "pesan": "Terus jadi panutan yang bijak."
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "20",
                "asal": "Sumatra Barat",
                "alamat": "Sukarame",
                "hobbi": "Masak",
                "sosmed": "@audinaf_03",
                "kesan": "Suka menolong tanpa banyak bicara.",
                "pesan": "Jangan lupa istirahat, Kak."
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450107",
                "umur": "20",
                "asal": "Bagan Batu, Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@cikamrbn",
                "kesan": "Disiplin soal waktu.",
                "pesan": "Ajari kami juga cara mengatur prioritas."
            },
            {
                "nama": "Gustin H Tampubolon",
                "nim": "124450068",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobbi": "Nonton",
                "sosmed": "@gustinhaleluya",
                "kesan": "Pandai memberi nasihat praktis.",
                "pesan": "Terus jadi kakak yang solutif."
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Ngadu Ikan Cupang",
                "sosmed": "@muhvinz_",
                "kesan": "Ramah ke semua orang.",
                "pesan": "Pertahankan sikap terbuka itu."
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "20",
                "asal": "Natar",
                "alamat": "Natar",
                "hobbi": "Nonton Drakor",
                "sosmed": "@snasaa._",
                "kesan": "Ramah ke semua orang.",
                "pesan": "Pertahankan sikap rendah hati itu."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1CpkgiRbxm4g-3XCQzPgS7mNt1dxzfx3e&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SUpeMz8pRKHTPxJm7ai-9JkeuFyUezBQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=16BGQYeiE16rOsIpXeE069NQOFPEnYE0l&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KaGDMGs2g3wu49UMg8xJg7jxc5zStIGG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rK4OrfhN2vap2X_139Kz_xvAHK-B53nl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LuBxz1dj4CJ4uaZr4qgO68mAI5jtZfNK&sz=w1000", 
                "https://drive.google.com/thumbnail?id=1bxoC2w1zvEFBXVCg_POcMWaSGgp3I_sv&sz=w1000",
                "https://drive.google.com/thumbnail?id=17yiwDzKg7O7oMYxSz4Ef99ivqjU8YlK5&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EgMCGYIm9_UhJ3FpdwNuhsKzB_XmPCbv&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WDgxzVzwllbujZs6OCcpFnDiEwUJdgNz&sz=w1000",
                "https://drive.google.com/thumbnail?id=13qx3ZTiMbtbr09odiRbS6u9WmapZ5BDQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xl1WHGohBDWFLhprfw3PVbiR0v3PwLUQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZAitTmeqanwoVGyNm3MvsBPuUqIaYHgU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1k4DyBp2J4apMynfDBfIxhfHCmLh4aj_r&sz=w1000",
                "https://drive.google.com/thumbnail?id=16URAPXha9Nuazp2obB4716fxGdwt1--F&sz=w1000"
        ]
        
        data_list = [
            {
                "nama": "Kevin Antonio Junior", 
                "nim" : "123450109",
                "asal" : "Bandar Lampung",
                "alamat" : "Panjang, Bandar Lampung",
                "hobbi": "Balap",
                "umur" : "21",
                "sosmed" : "@kevinaj__",
                "kesan" : "Sosoknya santai tapi tetap bisa diandalkan.",
                "pesan" : "Tetap jadi kakak yang asyik diajak ngobrol, Kak."
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika", 
                "nim" : "123450046",
                "asal" : "Lampung Utara",
                "alamat" : "Way Halim",
                "hobbi": "Baca",
                "umur" : "21",
                "sosmed" : "@ferazkaa",
                "kesan" : "Tutur katanya tenang dan enak didengar.",
                "pesan" : "Terus bagikan wawasan dari bacaanmu ke kami, Kak."
            },
            {
                "nama": "Ari Aristo Muthahari Parisi", 
                "nim" : "123450088",
                "asal" : "Lampung Timur",
                "alamat" : "Gang Sakum, Belwis",
                "hobbi": "Nonton F1",
                "umur" : "21",
                "sosmed" : "@ali_parisi3",
                "kesan" : "Orangnya kalem dan tidak banyak menuntut.",
                "pesan" : "Tetap jadi pribadi yang rendah hati, Kak."
            },
            {
                "nama": "Ayu Andriani Parlina Wati", 
                "nim" : "124450058",
                "asal" : "Lampung Barat",
                "alamat" : "Airan",
                "hobbi": "Belajar",
                "umur" : "20",
                "sosmed" : "@aayuandrianni_",
                "kesan" : "Rajin dan selalu bersungguh-sungguh dalam bekerja.",
                "pesan" : "Semoga semangat belajarnya menular ke kami, Kak."
            },
            {
                "nama": "Dafa Elpriza", 
                "nim" : "124450131",
                "asal" : "Bekasi",
                "alamat" : "Way Kandis",
                "hobbi": "Nemenin Bryan live TikTok",
                "umur" : "21",
                "sosmed" : "@dafaelpriza_",
                "kesan" : "Setia kawan dan gampang bikin suasana ramai.",
                "pesan" : "Jangan berubah, tetap jadi teman yang seru, Kak."
            },
            {
                "nama": "Juwita Sari", 
                "nim" : "124450066",
                "asal" : "Lampung Barat",
                "alamat" : "Pemda",
                "hobbi": "Lihat bulan",
                "umur" : "19",
                "sosmed" : "@ju.juwitaaa_",
                "kesan" : "Sikapnya lembut dan menenangkan.",
                "pesan" : "Tetap jadi tempat bercerita yang nyaman, Kak."
            },
            {
                "nama": "Muhammad Afdal Lutfi", 
                "nim" : "124450047",
                "asal" : "Lampung Tengah",
                "alamat" : "Jl Pulau Damar",
                "hobbi": "Taptap layar kalo Bryan live",
                "umur" : "19",
                "sosmed" : "@afdall.03",
                "kesan" : "Ceria dan selalu kompak dengan teman-temannya.",
                "pesan" : "Terus jaga kekompakan itu, Kak."
            },
            {
                "nama": "Salsabila Nazwa Putri", 
                "nim" : "124450002",
                "asal" : "Metro",
                "alamat" : "Korpri",
                "hobbi": "Nongkrong di Kopken",
                "umur" : "20",
                "sosmed" : "@slbnzw_",
                "kesan" : "Mudah akrab dan enak diajak berdiskusi.",
                "pesan" : "Tetap jadi kakak yang terbuka ke adik tingkat, ya, Kak."
            },
            {
                "nama": "Muhammad Ridwan", 
                "nim" : "123450091",
                "asal" : "Lampung Tengah",
                "alamat" : "Belwis",
                "hobbi": "Nganterin Datasena ke gedung F",
                "umur" : "21",
                "sosmed" : "@mridwaan_22",
                "kesan" : "Bertanggung jawab dan siap membantu kapan saja.",
                "pesan" : "Jangan lelah jadi tumpuan kami, Kak."
            },
            {
                "nama": "Andra Ilham Bintang", 
                "nim" : "124450060",
                "asal" : "Sumatera Selatan",
                "alamat" : "Kota Baru",
                "hobbi": "Ngitungin kelopak bunga di kebun",
                "umur" : "18",
                "sosmed" : "@andra.lhm",
                "kesan" : "Teliti dan sabar dalam mengerjakan sesuatu.",
                "pesan" : "Tetap semangat dan jangan ragu bertanya ke kami, Kak."
            },
            {
                "nama": "Bryan Paskah Telaumbanua", 
                "nim" : "124450003",
                "asal" : "Nias",
                "alamat" : "Belwis",
                "hobbi": "Live TikTok",
                "umur" : "22",
                "sosmed" : "@bryantel_",
                "kesan" : "Percaya dirinya tinggi dan bikin suasana hidup.",
                "pesan" : "Tetap jadi pribadi yang menghibur, Kak."
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy", 
                "nim" : "124450067",
                "asal" : "Bekasi",
                "alamat" : "Korpri",
                "hobbi": "Ngegift live Bryan",
                "umur" : "17",
                "sosmed" : "@meardhy_ghiyats",
                "kesan" : "Royal ke teman dan murah hati.",
                "pesan" : "Semoga kebaikanmu selalu dibalas, Kak."
            },
            {
                "nama": "Indah Julia Mawar Pratiwi", 
                "nim" : "124450055",
                "asal" : "Pringsewu",
                "alamat" : "Airan",
                "hobbi": "Bengong",
                "umur" : "Belum Tahu",
                "sosmed" : "@indahjuliaa",
                "kesan" : "Pembawaannya adem dan tidak neko-neko.",
                "pesan" : "Tetap jadi pribadi yang apa adanya, Kak."
            },
            {
                "nama": "Jacinda Kesya Alvara", 
                "nim" : "124450023",
                "asal" : "Kalimantan Barat",
                "alamat" : "Korpri",
                "hobbi": "Nyapu depan gacoan",
                "umur" : "18",
                "sosmed" : "@cacalvra",
                "kesan" : "Ceria dan punya selera humor yang unik.",
                "pesan" : "Terus tebar keceriaan ke sekitar, Kak."
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan", 
                "nim" : "124450089",
                "asal" : "Padang",
                "alamat" : "Kota Baru",
                "hobbi": "Bangun pagi",
                "umur" : "20",
                "sosmed" : "@muhammdrafka_",
                "kesan" : "Disiplin dan selalu memulai hari lebih awal.",
                "pesan" : "Ajari kami cara menjaga konsistensi, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1nH_1sn0sMUOh7_3qIISSYM9T84eJR2iq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1tQLTJk5hKuhK9oez4sFv_V_BXHQJFar7&sz=w1000",
                "https://drive.google.com/thumbnail?id=13KokHnm78hGBaEGT2pkErWe44rXJneVc&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jLPdABO7qyzRdkUJ8882kv_ZvlZ_WE3p&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wIHGtfTAEE1w3YW9WeJGG5OO6aiyNQZG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aC6kFPI702BixsmV1nbWNuJcWQ9M8mSf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1lMjvIjuHuwxWwz7YOw_7tN6za1ukLy-w&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qgnpFHACCBAlmUkDIWMt0Zdj0pG2k9U1&sz=w1000",
                "https://drive.google.com/thumbnail?id=14_vTVQXYcSRv3Aj33OV6OeTHMmqaiv-U&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Va2FO6AqYmorvBEz6QeqNfFitpDS-GhP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PSAhbM_pPO8UX01y0trU-4Sj424-WFZ4&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hXoeybqLaXywx-KUG8BeZ76rTxEVn1kC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1OyiZ4Bp3PWzJj8YztLym9qBsUIsrm5dn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Id19a1-GXLADLptIBse78enmXM7lxgCv&sz=w1000",
                "https://drive.google.com/thumbnail?id=1eqO7Eaop2q6rQWNTE7uqGJsuTj_9duPR&sz=w1000",
                "https://drive.google.com/thumbnail?id=1T2tgQP506eWJYmfsaqoxNhgL0-FI1vPw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1E6EJDFl4kIISfpAjxM5Hmgy0DLHkWhyA&sz=w1000",
                "https://drive.google.com/thumbnail?id=1guA749g_NUMONZcv-9-7L0QPYj7CqUlr&sz=w1000",
                "https://drive.google.com/thumbnail?id=15NA_9dMUwM7E3CnLQ7mbJcHEwJ949_tD&sz=w1000",
                "https://drive.google.com/thumbnail?id=12JkYRqTcdRUEtsdMyi-ciHG7JX-N0_0Z&sz=w1000",
                "https://drive.google.com/thumbnail?id=1fCN8Tml3KjNOMj6z9yD4H3VXLjZW8E9T&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dKlZtSSAUjL2KmCQCkg-QYUJknABlxpp&sz=w1000"
        ]
        
        data_list = [
            {
                "nama": "Fabio Banyu Cyto", 
                "nim" : "12340104",
                "asal" : "Bandar Lampung",
                "alamat" : "Kedaton",
                "hobbi": "Tidur",
                "umur" : "21",
                "sosmed" : "@biyokcb",
                "kesan" : "Gayanya santai dan tidak pernah ribet.",
                "pesan" : "Tetap jadi kakak yang asyik, Kak."
            },
            {
                "nama": "Tanty Widiyastuti", 
                "nim" : "123450094",
                "asal" : "Lampung",
                "alamat" : "Airan Raya",
                "hobbi": "Membaca",
                "umur" : "21",
                "sosmed" : "@tvnty_",
                "kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "nama": "Fadil Prasetyo Alfaritzi", 
                "nim" : "Belum Tahu",
                "asal" : "Bandar Lampungku",
                "alamat" : "Bandar Lampung",
                "hobbi": "Gitar",
                "umur" : "21",
                "sosmed" : "@fadilalfarizzii",
                "kesan" : "Permainan gitarnya bikin suasana nyaman.",
                "pesan" : "Sering-sering hibur kami lewat musikmu, Kak."
            },
            {
                "nama": "Manuel Frederika", 
                "nim" : "124450039",
                "asal" : "Batam",
                "alamat" : "Way Kandis",
                "hobbi": "Tenis meja",
                "umur" : "20",
                "sosmed" : "@manuelfdk_",
                "kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "nama": "Ni Made Okta Viola Darma Putri", 
                "nim" : "124450005",
                "asal" : "Bali",
                "alamat" : "Nusa Penida",
                "hobbi": "Menghayal",
                "umur" : "12",
                "sosmed" : "Violaadrtr_",
                "kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "nama": "Risa Romadona", 
                "nim" : "124450127",
                "asal" : "Natar",
                "alamat" : "Natar",
                "hobbi": "Rolling skate",
                "umur" : "20",
                "sosmed" : "risarmdna",
                "kesan" : "Aktif dan berani mencoba hal baru.",
                "pesan" : "Terus berani melangkah, Kak."
            },
            {
                "nama": "Vannisa Ramadhani", 
                "nim" : "124450078",
                "asal" : "Kepulauan Riau",
                "alamat" : "Teluk Betung",
                "hobbi": "Nonton KHW",
                "umur" : "19",
                "sosmed" : "@vunnycaa",
                "kesan" : "Ramah dan selalu terlihat ceria.",
                "pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "nama": "Yulia Cristine Malau", 
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Sopan dan menghargai orang lain.",
                "pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "nama": "Akeyla Fairuz Shafi", 
                "nim" : "1234501",
                "asal" : "Bandar Lampung",
                "alamat" : "Bandar Lampung",
                "hobbi": "Dengerin Musik",
                "umur" : "21",
                "sosmed" : "@keyashafi",
                "kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "nama": "Elsa Sitorus", 
                "nim" : "124450088",
                "asal" : "Sumatera Utara",
                "alamat" : "Pemda",
                "hobbi": "Rebahan",
                "umur" : "21",
                "sosmed" : "_els.a",
                "kesan" : "Murah senyum dan enak diajak bicara.",
                "pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "nama": "Fadya Izzatul ‘Aini", 
                "nim" : "124450062",
                "asal" : "Pringsewu",
                "alamat" : "Airan",
                "hobbi": "Mancing",
                "umur" : "20",
                "sosmed" : "fadyaizzatul_",
                "kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "nama": "Lovianora Saragih", 
                "nim" : "124450105",
                "asal" : "Sumatera Utara",
                "alamat" : "Way Huwi",
                "hobbi": "Dengerin Musik",
                "umur" : "19",
                "sosmed" : "_loviaa",
                "kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "nama": "M. Alsi Syahrulloh", 
                "nim" : "124450092",
                "asal" : "Kalianda",
                "alamat" : "Kotabaru",
                "hobbi": "Main Game, Tidur",
                "umur" : "20",
                "sosmed" : "@aluccy_",
                "kesan" : "Humoris dan gampang bikin tawa.",
                "pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "nama": "Sherena Florencia", 
                "nim" : "124450027",
                "asal" : "Bengkulu Selatan",
                "alamat" : "Belwis",
                "hobbi": "Make up",
                "umur" : "19",
                "sosmed" : "sher_renna",
                "kesan" : "Rapi dan selalu tampil percaya diri.",
                "pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "nama": "Razin Hafid Hamdi", 
                "nim" : "123450096",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Futsal",
                "umur" : "21",
                "sosmed" : "@razyn.hfd",
                "kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "nama": "Faiza Try Anjani", 
                "nim" : "124450075",
                "asal" : "Padang",
                "alamat" : "Belwis",
                "hobbi": "Membaca Novel",
                "umur" : "19",
                "sosmed" : "FAIZAANJANII",
                "kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "nama": "Gathfan Nadif Ali", 
                "nim" : "124450001",
                "asal" : "Bandar Lampung",
                "alamat" : "Rajabasa",
                "hobbi": "Main game",
                "umur" : "20",
                "sosmed" : "@gathfannadif",
                "kesan" : "Santai tapi tetap bertanggung jawab.",
                "pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "nama": "Hafidz Wahdiansyah", 
                "nim" : "tanya lintar",
                "asal" : "Metro",
                "alamat" : "Metro Kibang, Lampung Timur",
                "hobbi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "umur" : "20",
                "sosmed" : "@apiszzaja_",
                "kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "nama": "Kaleb Filbert Istel", 
                "nim" : "124450053",
                "asal" : "Bandar Lampung",
                "alamat" : "Campang Raya",
                "hobbi": "Ngegym, baca novel",
                "umur" : "20",
                "sosmed" : "@kelelep_comberan",
                "kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "nama": "Melva Shaprina Febrianti", 
                "nim" : "124450087",
                "asal" : "Sumsel",
                "alamat" : "Sukarame",
                "hobbi": "Scroll",
                "umur" : "19",
                "sosmed" : "@melva_fbrt",
                "kesan" : "Ceria dan mudah menyesuaikan diri.",
                "pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "nama": "Muhammad Syafiqul Falakh", 
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "@syaafiqui",
                "kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "nama": "Rifky Henry Ferdianto", 
                "nim" : "124450115",
                "asal" : "Kobum",
                "alamat" : "Rajabasa",
                "hobbi": "Lari dari kenyataan",
                "umur" : "28",
                "sosmed" : "henryferdianto",
                "kesan" : "Humornya unik dan bikin suasana cair.",
                "pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()

if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=14iYwo4zLbJrOef5hSpsv5CzztTDT3M3E&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QKtLVWd5UTS20p76_KI68UTlwbLngKPW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dqkvxLjs2eQCcUZ4-mQdjfpqWjczHNJ2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LAITpMrzuE2uuiZf4PdIKdB0ie9BnZDW&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BY75uzGUoS646SJ7D4pztcV_1Q7mSIHY&sz=w1000",
                "https://drive.google.com/thumbnail?id=1VtSwjVHmCSpInP9CxCiY9TakZvW7juBN&sz=w1000",
                "https://drive.google.com/thumbnail?id=1L6l5CQO16op-NXloIyxsJGIDUeiXJtMH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iTtqslvCmdUfSib6Tc_dw08br6YBIHxe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pXCOk6OdPwpbrbiRSk2bCHYH8fzuf_uq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ygeo8wX1IuOg2jXvvxGCFM4iSdF3TBiX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1SC2h3fpBQK7Mv1Gl5CVY-kG8dwU3dxLf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LEr1FBaJ0Jg9QtfYj5hAUGisL6xgq1bg&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hcyQoW2AcSNQ8L1CCtvyeC8r5qdtw4Cl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1E_eFzy4gGV_vMbRyhKCsyRFCl4Srv5Se&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EhDvjtozX4UCuvwQvmOCArjji8y2nHeK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aqW5i7oS32FAH3j_VgkA77y5_H9j5Gwj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xTxf3xwq2Cqg0JgWr-byy256KZWtrPML&sz=w1000",
                "https://drive.google.com/thumbnail?id=13RHyvO5yI8kLj7zmXedDFMuH3VPBNxij&sz=w1000"
        ]
        
        data_list = [
            {
                "nama": "Nayla Salsabila Fathianisa", 
                "nim" : "123450082",
                "asal" : "Payakumbuh, Sumatera Barat",
                "alamat" : "Belum Tahu",
                "hobbi": "Rebahan",
                "umur" : "20",
                "sosmed" : "@naylasalsabilaa._",
                "kesan" : "Bicaranya halus dan enak diajak ngobrol.",
                "pesan" : "Tetap jadi kakak yang sabar, ya, Kak."
            },
            {
                "nama": "Donna Maya Puspita", 
                "nim" : "123450028",
                "asal" : "Bekasi dan Lampung",
                "alamat" : "Belum Tahu",
                "hobbi": "Mendengarkan musik",
                "umur" : "21",
                "sosmed" : "@donnamaya.p",
                "kesan" : "Pendengar yang baik dan selalu tulus.",
                "pesan" : "Terus jadi teman berbagi yang nyaman, Kak."
            },
            {
                "nama": "Labo John Nuel Napitupulu", 
                "nim" : "37",
                "asal" : "Medan, Jakut, Palembang",
                "alamat" : "Belum Tahu",
                "hobbi": "Berburu burung",
                "umur" : "20",
                "sosmed" : "@noerruuu",
                "kesan" : "Wawasannya luas dan cerita pengalamannya seru.",
                "pesan" : "Sering-sering bagi cerita perjalananmu, Kak."
            },
            {
                "nama": "Anash Tasya Ausyaqila", 
                "nim" : "124450050",
                "asal" : "Bandar Lampung",
                "alamat" : "Belum Tahu",
                "hobbi": "Ngoding",
                "umur" : "20",
                "sosmed" : "@anshtsyaaql",
                "kesan" : "Fokus dan tekun kalau sudah mengerjakan sesuatu.",
                "pesan" : "Semoga ilmu codingmu terus berkembang, Kak."
            },
            {
                "nama": "Felisya Nabila Putri Nugroho", 
                "nim" : "124450104",
                "asal" : "Bekasi",
                "alamat" : "Belum Tahu",
                "hobbi": "Ngejahilin mama",
                "umur" : "18",
                "sosmed" : "@felisyanbl__",
                "kesan" : "Usilnya menyenangkan dan bikin suasana hidup.",
                "pesan" : "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "nama": "Muhammad Razan Maulana Pratama", 
                "nim" : "124450031",
                "asal" : "Sibolga",
                "alamat" : "Belum Tahu",
                "hobbi": "Jahilin Felisya",
                "umur" : "18",
                "sosmed" : "@muh_razan_",
                "kesan" : "Jahilnya bikin akrab, tapi tetap tahu batas.",
                "pesan" : "Jaga kekompakan sama teman-teman, Kak."
            },
            {
                "nama": "Sania Dwi Ayu Lestari", 
                "nim" : "123450086",
                "asal" : "Bandung",
                "alamat" : "Belum Tahu",
                "hobbi": "Bimbingan TA",
                "umur" : "21",
                "sosmed" : "@saniayyllstr",
                "kesan" : "Gigih dan tidak mudah menyerah.",
                "pesan" : "Semoga TA-nya lancar dan cepat selesai, Kak."
            },
            {
                "nama": "Allisha", 
                "nim" : "124450019",
                "asal" : "Rahim ibu",
                "alamat" : "Belum Tahu",
                "hobbi": "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah",
                "umur" : "6",
                "sosmed" : "@aallishaa.a",
                "kesan" : "Gampang akrab dan setia sama teman-temannya.",
                "pesan" : "Tetap jadi teman yang asyik buat semua, Kak."
            },
            {
                "nama": "Alya Ramadhanti", 
                "nim" : "124450091",
                "asal" : "Kota banyak sawit",
                "alamat" : "Belum Tahu",
                "hobbi": "Apa aja",
                "umur" : "19",
                "sosmed" : "@alya.rmdhnti",
                "kesan" : "Fleksibel dan mau mencoba apa saja.",
                "pesan" : "Jangan berhenti penasaran sama hal baru, Kak."
            },
            {
                "nama": "Bunga Clarisa Sefa", 
                "nim" : "124450097",
                "asal" : "Lampung Selatan",
                "alamat" : "Belum Tahu",
                "hobbi": "Belajar",
                "umur" : "20",
                "sosmed" : "@bungaclrssf",
                "kesan" : "Rajin dan disiplin dalam belajar.",
                "pesan" : "Bagi tips belajarmu ke kami juga, ya, Kak."
            },
            {
                "nama": "Difanya Husakina", 
                "nim" : "124450043",
                "asal" : "Deket Kebun Teh",
                "alamat" : "Belum Tahu",
                "hobbi": "Alhamdulillah Dzikir dan sholawatan",
                "umur" : "20",
                "sosmed" : "@difanyhsa",
                "kesan" : "Tutur katanya santun dan menyejukkan.",
                "pesan" : "Tetap istiqamah dan jadi teladan, Kak."
            },
            {
                "nama": "Nazlah Auliya", 
                "nim" : "124450054",
                "asal" : "Bandar Lampung",
                "alamat" : "Belum Tahu",
                "hobbi": "Ballet",
                "umur" : "20",
                "sosmed" : "@nzlhauly_",
                "kesan" : "Anggun dan penuh percaya diri.",
                "pesan" : "Terus kejar hobimu dengan semangat, Kak."
            },
            {
                "nama": "Raihana Adelia Putri", 
                "nim" : "123450041",
                "asal" : "Lampung Tengah",
                "alamat" : "Airan Raya 1",
                "hobbi": "Menulis, membaca",
                "umur" : "20",
                "sosmed" : "@r.hanaap",
                "kesan" : "Tenang dan pandai merangkai kata.",
                "pesan" : "Tetap menulis dan bagikan idemu ke kami, Kak."
            },
            {
                "nama": "Daffa Kharisma Adzana", 
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Kalem dan tidak banyak bicara, tapi tulus.",
                "pesan" : "Jangan sungkan bergabung ngobrol bareng, Kak."
            },
            {
                "nama": "Edsel Adya Pradipta", 
                "nim" : "098",
                "asal" : "Lampung Selatan, Natar",
                "alamat" : "Belum Tahu",
                "hobbi": "Scroll Fesbuk",
                "umur" : "20",
                "sosmed" : "@edsel_0712",
                "kesan" : "Santai dan punya selera humor yang khas.",
                "pesan" : "Tetap jadi kakak yang gampang diajak bercanda, Kak."
            },
            {
                "nama": "Lucia Advencia Rachel Nainggolan", 
                "nim" : "124450085",
                "asal" : "Bekasi",
                "alamat" : "Belwis",
                "hobbi": "Lari",
                "umur" : "20",
                "sosmed" : "@luciarachel_",
                "kesan" : "Energik dan selalu menyemangati sekitar.",
                "pesan" : "Terus tularkan semangat larimu ke kami, Kak."
            },
            {
                "nama": "Shafa Delaila Azzahra", 
                "nim" : "124450124",
                "asal" : "Lampung Tengah",
                "alamat" : "Belum Tahu",
                "hobbi": "Makan tempe mentah",
                "umur" : "20",
                "sosmed" : "@_shaazzh",
                "kesan" : "Apa adanya dan bikin suasana tidak kaku.",
                "pesan" : "Tetap jadi diri sendiri, ya, Kak."
            },
            {
                "nama": "Zannuba Arifah Ilman", 
                "nim" : "Belum Tahu",
                "asal" : "Belum Tahu",
                "alamat" : "Belum Tahu",
                "hobbi": "Belum Tahu",
                "umur" : "Belum Tahu",
                "sosmed" : "Belum Tahu",
                "kesan" : "Sopan dan selalu menghargai orang lain.",
                "pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()