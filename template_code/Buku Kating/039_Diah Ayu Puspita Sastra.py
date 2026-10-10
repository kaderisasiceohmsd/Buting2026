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
            "Departemen Medkraf"
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
            "people-fill"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "13px",
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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
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
                "Nama": "Ginda Fajar Riadi Marpaung", 
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu", 
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Belum",
                "Pesan" : "Belum"
            },
            {
                "Nama": "Muhammad Aqil Ramadhan", 
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru", 
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Sosoknya tenang dan mengayomi.",
                "Pesan" : "Tetap jadi kakak yang bisa diandalkan, Kak."
            },
            {
                "Nama": "Efi Defiyati", 
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Sosoknya ramah dan penuh semangat.",
                "Pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
            },
            {
                "Nama": "Qois Olifio", 
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Cara bicaranya santai tapi berisi.",
                "Pesan" : "Jangan bosan membagi ilmu ke kami."    
            },
            {
                "Nama": "Hafsa Fazilah Arradhi", 
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung", 
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Senyumnya hangat dan bikin suasana cair.",
                "Pesan" : "Tetap jadi kakak yang ramah, ya, Kak."
            },
            {
                "Nama": "Luthfia Laila Ramadhani", 
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Sosoknya ramah dan penuh semangat.",
                "Pesan" : "Tetap semangat dalam menjalankan tugas sebagai kesekjenan, Kak."
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
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Humornya sederhana tapi bikin akrab.",
                "Pesan": "Jaga suasana cair tanpa berlebihan."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Cara bicaranya lembut tapi tegas.",
                "Pesan": "Jangan ragu terus membimbing kami dengan sabar."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Perhatiannya ke adik tingkat sangat besar.",
                "Pesan": "Semoga kebaikan Kakak selalu kembali."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "Tegas saat mengambil keputusan.",
                "Pesan": "Tetap adil dan pertimbangkan banyak hal."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Selalu rapi dan enak dilihat.",
                "Pesan": "Tetap jadi panutan tanpa harus menggurui."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Pintar menenangkan saat kami panik.",
                "Pesan": "Terus jadi tempat cerita yang aman."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Suka membantu tanpa pamrih.",
                "Pesan": "Semoga kebaikan Kakak berbuah baik."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Humornya segar dan tidak berlebihan.",
                "Pesan": "Jaga energi positif itu sampai kapan pun."
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Disiplin dan tepat waktu.",
                "Pesan": "Tularkan kebiasaan itu ke adik tingkat."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Tegas saat organisasi butuh keputusan.",
                "Pesan": "Tetap adil dan bijak dalam memimpin."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Berwibawa tanpa harus marah.",
                "Pesan": "Terus jadi panutan yang bijak."
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Suka menolong tanpa banyak bicara.",
                "Pesan": "Jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Disiplin soal waktu.",
                "Pesan": "Ajari kami juga cara mengatur prioritas."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Pandai memberi nasihat praktis.",
                "Pesan": "Terus jadi kakak yang solutif."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Ramah ke semua orang.",
                "Pesan": "Pertahankan sikap terbuka itu."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Ramah ke semua orang.",
                "Pesan": "Pertahankan sikap rendah hati itu."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()
 
# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Departemen Minbak":
    def departemen_minbak():
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
                "Nama": "Kevin Antonio Junior", 
                "NIM" : "123450109",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Panjang, Bandar Lampung",
                "Hobi": "Balap",
                "Umur" : "21",
                "Sosmed" : "@kevinaj__",
                "Kesan" : "Sosoknya santai tapi tetap bisa diandalkan.",
                "Pesan" : "Tetap jadi kakak yang asyik diajak ngobrol, Kak."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika", 
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Tutur katanya tenang dan enak didengar.",
                "Pesan" : "Terus bagikan wawasan dari bacaanmu ke kami, Kak."
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi", 
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Orangnya kalem dan tidak banyak menuntut.",
                "Pesan" : "Tetap jadi pribadi yang rendah hati, Kak."
            },
            {
                "Nama": "Ayu Andriani Parlina Wati", 
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "Rajin dan selalu bersungguh-sungguh dalam bekerja.",
                "Pesan" : "Semoga semangat belajarnya menular ke kami, Kak."
            },
            {
                "Nama": "Dafa Elpriza", 
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Setia kawan dan gampang bikin suasana ramai.",
                "Pesan" : "Jangan berubah, tetap jadi teman yang seru, Kak."
            },
            {
                "Nama": "Juwita Sari", 
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Sikapnya lembut dan menenangkan.",
                "Pesan" : "Tetap jadi tempat bercerita yang nyaman, Kak."
            },
            {
                "Nama": "Muhammad Afdal Lutfi", 
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Ceria dan selalu kompak dengan teman-temannya.",
                "Pesan" : "Terus jaga kekompakan itu, Kak."
            },
            {
                "Nama": "Salsabila Nazwa Putri", 
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Mudah akrab dan enak diajak berdiskusi.",
                "Pesan" : "Tetap jadi kakak yang terbuka ke adik tingkat, ya, Kak."
            },
            {
                "Nama": "Muhammad Ridwan", 
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Bertanggung jawab dan siap membantu kapan saja.",
                "Pesan" : "Jangan lelah jadi tumpuan kami, Kak."
            },
            {
                "Nama": "Andra Ilham Bintang", 
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Teliti dan sabar dalam mengerjakan sesuatu.",
                "Pesan" : "Tetap semangat dan jangan ragu bertanya ke kami, Kak."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua", 
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Percaya dirinya tinggi dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang menghibur, Kak."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy", 
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Royal ke teman dan murah hati.",
                "Pesan" : "Semoga kebaikanmu selalu dibalas, Kak."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi", 
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Pembawaannya adem dan tidak neko-neko.",
                "Pesan" : "Tetap jadi pribadi yang apa adanya, Kak."
            },
            {
                "Nama": "Jacinda Kesya Alvara", 
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Ceria dan punya selera humor yang unik.",
                "Pesan" : "Terus tebar keceriaan ke sekitar, Kak."
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan", 
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Disiplin dan selalu memulai hari lebih awal.",
                "Pesan" : "Ajari kami cara menjaga konsistensi, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()
 
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
                "Nama": "Fabio Banyu Cyto", 
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Gayanya santai dan tidak pernah ribet.",
                "Pesan" : "Tetap jadi kakak yang asyik, Kak."
            },
            {
                "Nama": "Tanty Widiyastuti", 
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Tenang dan suka memperhatikan hal-hal kecil.",
                "Pesan" : "Terus bagikan ketelitianmu ke kami, Kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi", 
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Permainan gitarnya bikin suasana nyaman.",
                "Pesan" : "Sering-sering hibur kami lewat musikmu, Kak."
            },
            {
                "Nama": "Manuel Frederika", 
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Energik dan cepat akrab dengan siapa saja.",
                "Pesan" : "Tetap semangat dan jangan berubah, Kak."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri", 
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Pembawaannya kalem dan penuh imajinasi.",
                "Pesan" : "Semoga ide-idemu terus berkembang, Kak."
            },
            {
                "Nama": "Risa Romadona", 
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Aktif dan berani mencoba hal baru.",
                "Pesan" : "Terus berani melangkah, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani", 
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Ramah dan selalu terlihat ceria.",
                "Pesan" : "Tetap jadi pribadi yang menyenangkan, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau", 
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Sopan dan menghargai orang lain.",
                "Pesan" : "Semoga selalu sukses dalam setiap kegiatan, Kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi", 
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Pendengar yang baik dan tidak suka menghakimi.",
                "Pesan" : "Tetap jadi teman cerita yang nyaman, Kak."
            },
            {
                "Nama": "Elsa Sitorus", 
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "_els.a",
                "Kesan" : "Murah senyum dan enak diajak bicara.",
                "Pesan" : "Tetap jadi kakak yang hangat, ya, Kak."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini", 
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Sabar dan telaten kalau menjelaskan sesuatu.",
                "Pesan" : "Jangan bosan membimbing kami, Kak."
            },
            {
                "Nama": "Lovianora Saragih", 
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Kalem tapi tetap hangat saat berinteraksi.",
                "Pesan" : "Semoga selalu dimudahkan dalam studinya, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh", 
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Humoris dan gampang bikin tawa.",
                "Pesan" : "Jangan lupa tetap fokus kuliah juga, Kak."
            },
            {
                "Nama": "Sherena Florencia", 
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Rapi dan selalu tampil percaya diri.",
                "Pesan" : "Tetap jadi inspirasi bagi adik tingkat, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi", 
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Sportif dan semangat kerja samanya tinggi.",
                "Pesan" : "Terus ajak kami aktif bersama, Kak."
            },
            {
                "Nama": "Faiza Try Anjani", 
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Tutur katanya sopan dan penuh pertimbangan.",
                "Pesan" : "Tetap jadi kakak yang bijak, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali", 
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Santai tapi tetap bertanggung jawab.",
                "Pesan" : "Terus jaga keseimbangan itu, Kak."
            },
            {
                "Nama": "Hafidz Wahdiansyah", 
                "NIM" : "tanya lintar",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Cekatan soal teknis dan mau berbagi ilmu.",
                "Pesan" : "Ajari kami ngoding dengan sabar, Kak."
            },
            {
                "Nama": "Kaleb Filbert Istel", 
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Konsisten menjaga kebiasaan hidup sehat.",
                "Pesan" : "Tularkan semangat hidup sehatmu ke kami, Kak."
            },
            {
                "Nama": "Melva Shaprina Febrianti", 
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Ceria dan mudah menyesuaikan diri.",
                "Pesan" : "Tetap jadi pribadi yang ramah, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh", 
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "@syaafiqui",
                "Kesan" : "Pendiam tapi diam-diam bisa diandalkan.",
                "Pesan" : "Jangan sungkan berbagi pendapat ke kami, Kak."
            },
            {
                "Nama": "Rifky Henry Ferdianto", 
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "henryferdianto",
                "Kesan" : "Humornya unik dan bikin suasana cair.",
                "Pesan" : "Semoga kenyataan selalu ramah padamu, Kak."
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
                "Nama": "Nayla Salsabila Fathianisa", 
                "NIM" : "123450082",
                "Asal" : "Payakumbuh, Sumatera Barat",
                "Alamat" : "Belum Tahu",
                "Hobi": "Rebahan",
                "Umur" : "20",
                "Sosmed" : "@naylasalsabilaa._",
                "Kesan" : "Bicaranya halus dan enak diajak ngobrol.",
                "Pesan" : "Tetap jadi kakak yang sabar, ya, Kak."
            },
            {
                "Nama": "Donna Maya Puspita", 
                "NIM" : "123450028",
                "Asal" : "Bekasi dan Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Pendengar yang baik dan selalu tulus.",
                "Pesan" : "Terus jadi teman berbagi yang nyaman, Kak."
            },
            {
                "Nama": "Labo John Nuel Napitupulu", 
                "NIM" : "37",
                "Asal" : "Medan, Jakut, Palembang",
                "Alamat" : "Belum Tahu",
                "Hobi": "Berburu burung",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Wawasannya luas dan cerita pengalamannya seru.",
                "Pesan" : "Sering-sering bagi cerita perjalananmu, Kak."
            },
            {
                "Nama": "Anash Tasya Ausyaqila", 
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ngoding",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Fokus dan tekun kalau sudah mengerjakan sesuatu.",
                "Pesan" : "Semoga ilmu codingmu terus berkembang, Kak."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho", 
                "NIM" : "124450104",
                "Asal" : "Bekasi",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ngejahilin mama",
                "Umur" : "18",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Usilnya menyenangkan dan bikin suasana hidup.",
                "Pesan" : "Tetap jadi pribadi yang ceria, Kak."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama", 
                "NIM" : "124450031",
                "Asal" : "Sibolga",
                "Alamat" : "Belum Tahu",
                "Hobi": "Jahilin Felisya",
                "Umur" : "18",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Jahilnya bikin akrab, tapi tetap tahu batas.",
                "Pesan" : "Jaga kekompakan sama teman-teman, Kak."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari", 
                "NIM" : "123450086",
                "Asal" : "Bandung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Bimbingan TA",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Gigih dan tidak mudah menyerah.",
                "Pesan" : "Semoga TA-nya lancar dan cepat selesai, Kak."
            },
            {
                "Nama": "Allisha", 
                "NIM" : "124450019",
                "Asal" : "Rahim ibu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Makan warbir bareng Queenta, Dipa, Della, Vio, Risa, Indah",
                "Umur" : "6",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Gampang akrab dan setia sama teman-temannya.",
                "Pesan" : "Tetap jadi teman yang asyik buat semua, Kak."
            },
            {
                "Nama": "Alya Ramadhanti", 
                "NIM" : "124450091",
                "Asal" : "Kota banyak sawit",
                "Alamat" : "Belum Tahu",
                "Hobi": "Apa aja",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Fleksibel dan mau mencoba apa saja.",
                "Pesan" : "Jangan berhenti penasaran sama hal baru, Kak."
            },
            {
                "Nama": "Bunga Clarisa Sefa", 
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Rajin dan disiplin dalam belajar.",
                "Pesan" : "Bagi tips belajarmu ke kami juga, ya, Kak."
            },
            {
                "Nama": "Difanya Husakina", 
                "NIM" : "124450043",
                "Asal" : "Deket Kebun Teh",
                "Alamat" : "Belum Tahu",
                "Hobi": "Alhamdulillah Dzikir dan sholawatan",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Tutur katanya santun dan menyejukkan.",
                "Pesan" : "Tetap istiqamah dan jadi teladan, Kak."
            },
            {
                "Nama": "Nazlah Auliya", 
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ballet",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Anggun dan penuh percaya diri.",
                "Pesan" : "Terus kejar hobimu dengan semangat, Kak."
            },
            {
                "Nama": "Raihana Adelia Putri", 
                "NIM" : "123450041",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur" : "20",
                "Sosmed" : "@r.hanaap",
                "Kesan" : "Tenang dan pandai merangkai kata.",
                "Pesan" : "Tetap menulis dan bagikan idemu ke kami, Kak."
            },
            {
                "Nama": "Daffa Kharisma Adzana", 
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Kalem dan tidak banyak bicara, tapi tulus.",
                "Pesan" : "Jangan sungkan bergabung ngobrol bareng, Kak."
            },
            {
                "Nama": "Edsel Adya Pradipta", 
                "NIM" : "098",
                "Asal" : "Lampung Selatan, Natar",
                "Alamat" : "Belum Tahu",
                "Hobi": "Scroll Fesbuk",
                "Umur" : "20",
                "Sosmed" : "@edsel_0712",
                "Kesan" : "Santai dan punya selera humor yang khas.",
                "Pesan" : "Tetap jadi kakak yang gampang diajak bercanda, Kak."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan", 
                "NIM" : "124450085",
                "Asal" : "Bekasi",
                "Alamat" : "Belwis",
                "Hobi": "Lari",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Energik dan selalu menyemangati sekitar.",
                "Pesan" : "Terus tularkan semangat larimu ke kami, Kak."
            },
            {
                "Nama": "Shafa Delaila Azzahra", 
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belum Tahu",
                "Hobi": "Makan tempe mentah",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Apa adanya dan bikin suasana tidak kaku.",
                "Pesan" : "Tetap jadi diri sendiri, ya, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman", 
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Sopan dan selalu menghargai orang lain.",
                "Pesan" : "Semoga selalu dimudahkan dalam setiap urusan, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()
 
