import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO
import html

st.markdown("""
    <style>
    .centered-title {
        text-align: center;
    }
    .stApp {
            background: linear-gradient(160deg, #DCE8D2 0%, #E9F0DE 50%, #F1F2E3 100%);
            background-attachment: fixed;
            color: var(--bark);
    }
    [data-testid="stHeader"] {
        background: linear-gradient(160deg, #DCE8D2 0%, #E9F0DE 50%, #F1F2E3 100%) !important;
        background-attachment: fixed !important;
    }
    </style>
""", unsafe_allow_html=True)
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
            "people-fill"
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#FBF8F0"},
            "icon": {"color": "#C08552", "font-size": "16px"},
            "nav-link": {
                "font-size": "13px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#E3EDD9",
            },
            "nav-link-selected": {"background-color": "#6B8F5E"},
        },
    )
    return selected

CSS_BIODATA = """
<style>
.bio-nama {font-size: 1.2rem; font-weight: 700; margin: 0.4rem 0 0.6rem 0;}
.bio-row {display: flex; gap: 0.6rem; font-size: 0.92rem; line-height: 1.5; padding: 3px 0;}
.bio-lbl {min-width: 80px; color: #6b7280; font-weight: 600;}
.bio-val {flex: 1; word-break: break-word;}
</style>
"""

FIELD_BIODATA = ["NIM", "Umur", "Asal", "Alamat", "Hobi", "Sosmed", "Kesan", "Pesan"]


@st.cache_data
def load_image(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img).convert("RGB")
        return ImageOps.fit(img, (400, 500), Image.LANCZOS)
    except Exception:
        return None


def tampilkan_kartu(img, data):
    with st.container(border=True):
        if img is not None:
            st.image(img, use_container_width=True)
        else:
            st.info("Foto tidak tersedia")

        baris = f'<div class="bio-nama">{html.escape(data["Nama"])}</div>'
        for field in FIELD_BIODATA:
            baris += (
                f'<div class="bio-row">'
                f'<span class="bio-lbl">{field}</span>'
                f'<span class="bio-val">: {html.escape(str(data[field]))}</span>'
                f'</div>'
            )
        st.markdown(baris, unsafe_allow_html=True)


def display_images_with_data(gambar_urls, data_list):
    st.markdown(CSS_BIODATA, unsafe_allow_html=True)

    with st.spinner("Memuat foto..."):
        images = [load_image(url) for url in gambar_urls]

    pasangan = list(zip(images, data_list))

    for i in range(0, len(pasangan), 2):
        cols = st.columns(2, gap="medium")
        for col, (img, data) in zip(cols, pasangan[i:i + 2]):
            with col:
                tampilkan_kartu(img, data)

menu = streamlit_menu()

if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1Ydfq9Evnhui8Yqv56GlFmsZZyZUD4BSo&sz=w1000",
                "https://drive.google.com/thumbnail?id=1gKuqkzr7T4J7nYxeZQVvM3PgAUXsyvje&sz=w1000",
                "https://drive.google.com/thumbnail?id=1I-F931OZ9dC1YL5ue5nLOoMM8ZFmxqro&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pveYH5_vp9Ti-YcLvqKgw3HguEDfqTzS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A-tjV1Cw5Nt8bhlRr0B1_1EMF725rben&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-7LCL719bCdP3ba66VdshxS45PPfuTVI&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung", 
                "NIM" : "123450103",
                "Asal" : "Bakinang",
                "Alamat" : "Sekretariat HMSD", 
                "Hobi": "Push Rank",
                "Umur" : "22",
                "Sosmed" : "@jars_mrp",
                "Kesan" : "Orangnya kalem dan enak diajak ngobrol.",
                "Pesan" : "Semoga selalu sehat dan sukses terus, Kak."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan", 
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru", 
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Pembawaannya tenang dan bikin nyaman di sekitarnya.",
                "Pesan" : "Terus istiqomah dan jaga kesehatan ya, Bang."
            },
            {
                "Nama": "Efi Defiyati", 
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Murah senyum dan gampang akrab dengan siapa saja.",
                "Pesan" : "Semoga makin banyak bacaan seru dan tetap semangat, Kak."
            },
            {
                "Nama": "Qois Olifio", 
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Humoris dan selalu punya cerita menarik.",
                "Pesan" : "Tetap jadi pribadi yang asyik dan jangan lupa istirahat, Bang."    
            },
            {
                "Nama": "Hafsa Fazilah Arradhi", 
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung", 
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Ceria dan selalu bikin suasana jadi lebih hidup.",
                "Pesan" : "Semoga selalu lancar dalam segala urusan, Kak."
            },
            {
                "Nama": "Luthfia Laila Ramadhani", 
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Santai dan menyenangkan, cocok diajak jalan bareng.",
                "Pesan" : "Tetap semangat kuliah, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()
 
if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1N5OYZ9hATFqnablK-hFmacr2rdaRG4_V&sz=w1000",
                "https://drive.google.com/thumbnail?id=1J1DYIP_T05bR6RuBksL70zul0jsDQJxP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qq3Q9m9_atK01EAhnHUgTqYLbyygnHUC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1uqiOIGWHF3deFZcCmTL2alTo6VCZSvNf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nyvxESh1leil7ru3XFGjl4uaUHhEBe1h&sz=w1000",
                "https://drive.google.com/thumbnail?id=1gyID6Cc0e5ItfYo6VZK0GH8RZiqkHPSw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qJ_Dre1ECzgmLhvHe3CRhTOa1u9dSpVU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Qg-Y__pzCPcghbJbpRTbp5ofX_rsV8Js&sz=w1000",
                "https://drive.google.com/thumbnail?id=1h70Bo9id77LKfqLk3_qE20w37q1bHHgF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iimFYJzZU9R52ct6SPZFKB8wtGGhPQUB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nUQojkJaVvSSeiN27rf499m-7-CN9wlu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Vr4wIF1m2jzgDd6YiicKnFqYMNt3k0hf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1d8zaMXYlJ4MolCgfLw4f9bn-CnWL3WYn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qeuS9zf09FmSTfVWbiFi1jeSnwxWg2FT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1B9-H5Lg9bmICHwXZm18doQJwFKrqPZjx&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iwmfJcLJ9MgTOL8u7l2S84GyWFeS9rwt&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Haikal Fransisko Simbolon",
                "NIM": "123450106",
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Way Halim",
                "Hobi": "Ngeledek Orang",
                "Sosmed": "@haikalsbln",
                "Kesan": "Orangnya seru dan gampang bikin suasana jadi akrab.",
                "Pesan": "Semoga selalu semangat dan sukses terus, Bang."
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "123450034",
                "Umur": "21",
                "Asal": "Way Kanan",
                "Alamat": "Untung Senopati",
                "Hobi": "Suka Nolong Orang",
                "Sosmed": "@rismaa.mustika_",
                "Kesan": "Baik hati dan selalu siap membantu siapa saja.",
                "Pesan": "Tetap jadi pribadi yang ramah dan jangan lupa jaga kesehatan, Kak."
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "123450038",
                "Umur": "21",
                "Asal": "Sumatera Utara, kisaran city",
                "Alamat": "Sukarame",
                "Hobi": "Ngabarin Orang Tua",
                "Sosmed": "@hanna_g_sinaga",
                "Kesan": "Hangat dan perhatian, enak diajak ngobrol.",
                "Pesan": "Semoga selalu dilancarkan dalam segala urusan, Kak."
            },
            {
                "Nama": "Ahmad Farhan Ghani",
                "NIM": "123450121",
                "Umur": "21",
                "Asal": "Kemiling",
                "Alamat": "Kemiling",
                "Hobi": "Supporteran",
                "Sosmed": "@farhanghani",
                "Kesan": "Semangat dan seru.",
                "Pesan": "Tetap kompak dan semoga tim kesayangannya sering menang, Bang."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Ceria dan menyenangkan, kelihatannya jago cari makanan enak.",
                "Pesan": "Tetap semangat dan semoga rekomendasi kulinernya makin banyak, Kak."
            },
            {
                "Nama": "Cerine Sihotang",
                "NIM": "124450049",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "Belwis",
                "Hobi": "Suka Ngoding pakai R",
                "Sosmed": "@cerine_ipynb",
                "Kesan": "Pintar dan teliti, enak diajak diskusi.",
                "Pesan": "Semoga kodingannya selalu lancar tanpa error, Kak."
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "Pekerja keras dan gigih.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat, Bang."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Kalem dan menyenangkan, bikin suasana jadi tenang.",
                "Pesan": "Tetap jadi diri sendiri dan semoga harinya selalu santai, Kak."
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Santai dan lucu, punya banyak cerita seru.",
                "Pesan": "Semangat terus dan semoga kucingnya makin akur, Bang."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Ramah dan kelihatannya jago masak.",
                "Pesan": "Tetap semangat dan semoga masakannya makin enak, Kak."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Asyik diajak ngobrol soal balapan.",
                "Pesan": "Terus semangat dan semoga jagoannya juara, Bang."
            },
            {
                "Nama": "Audina Fitria",
                "NIM": "124450038",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Sukarame",
                "Hobi": "Masak",
                "Sosmed": "@audinaf_03",
                "Kesan": "Kalem dan menyenangkan, enak diajak bergaul.",
                "Pesan": "Tetap semangat dan jaga kesehatan ya, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Ceria dan nyambung kalau ngobrol soal musik.",
                "Pesan": "Semoga playlist-nya selalu menemani hari yang menyenangkan, Kak."
            },
            {
                "Nama": "Gustin H Tampubolon",
                "NIM": "124450068",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@gustinhaleluya",
                "Kesan": "Santai dan menyenangkan, enak diajak ngobrol.",
                "Pesan": "Tetap semangat dan semoga selalu ada tontonan seru, Kak."
            },
            {
                "Nama": "Muhammad Harvinsyah",
                "NIM": "124450128",
                "Umur": "20",
                "Asal": "Sumatera Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngadu Ikan Cupang",
                "Sosmed": "@muhvinz_",
                "Kesan": "Santai dan seru, banyak bahan obrolannya.",
                "Pesan": "Semoga cupangnya selalu sehat dan menang terus, Bang."
            },
            {
                "Nama": "Rafa Sabina Fahimah",
                "NIM": "124450036",
                "Umur": "20",
                "Asal": "Natar",
                "Alamat": "Natar",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@snasaa._",
                "Kesan": "Asyik dan seru, banyak rekomendasi tontonannya.",
                "Pesan": "Tetap semangat dan jangan begadang kebanyakan gara-gara drakor, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()
 
if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1LmTiRyUcWG_SqZ0MEPeWhkvOVrT3s4mh&sz=w1000",
                "https://drive.google.com/thumbnail?id=1M0dQnyVPYdq1zw2RBR0qUh1mxVx-BcIj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mNK7jsiP9fzP2MVhgoSFBuliJ-34yhgn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1CXdr-HnrFBxtU7lw_Gu_t6shs16bg-eT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1j6bKVLt-PqU-1PKop4xYh2668akcXXVi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aaeqBP63GTE_0eWV71a-iFxPfvOCdmBK&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Z9WzO1pTPe5JvsoZmjOiC-LsOrPg0cQj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DTTbc01e_WX9yanosw6rf6m5GxL4fLs7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1i0xPqVZ0c9WvlIdPiYDPbkWMNacaqHWE&sz=w1000",
                "https://drive.google.com/thumbnail?id=19_wRgnJAfVLJkeNz_vWXEt-LR2etbfhI&sz=w1000",
                "https://drive.google.com/thumbnail?id=11u6n9HdA-bDEL-iJYP7CjS-QOMi7Qd6S&sz=w1000",
                "https://drive.google.com/thumbnail?id=1JuziGXCQ24p_ld9vRu9IaPF8pWXY8mHT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1pNUQIf2UcA2-lXrmvgBmCzQc6WGRWD2M&sz=w1000",
                "https://drive.google.com/thumbnail?id=1PLW0frBFtUk69JjkIqeUe4rUXD2iYhGF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1klKh2QC87HzU6CGPfniznstefmlEFgkb&sz=w1000",
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
                "Kesan" : "Energik dan punya gaya yang khas, seru.",
                "Pesan" : "Tetap semangat dan selalu hati-hati di jalan, Bang."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika", 
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Kalem dan wawasannya luas, nyaman diajak bertukar pikiran.",
                "Pesan" : "Semoga selalu ada waktu buat baca buku-buku favoritnya, Kak."
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi", 
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "Santai dan enak diajak ngobrol, apalagi soal balapan.",
                "Pesan" : "Semoga tim jagoannya sering naik podium, Bang."
            },
            {
                "Nama": "Ayu Andriani Parlina Wati", 
                "NIM" : "124450058",
                "Asal" : "Lampung Barat",
                "Alamat" : "Airan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@aayuandrianni_",
                "Kesan" : "Tekun dan fokus, jadi contoh yang baik buat teman-temannya.",
                "Pesan" : "Tetap semangat dan jangan lupa istirahat yang cukup, Kak."
            },
            {
                "Nama": "Dafa Elpriza", 
                "NIM" : "124450131",
                "Asal" : "Bekasi",
                "Alamat" : "Way Kandis",
                "Hobi": "Nemenin Bryan live TikTok",
                "Umur" : "21",
                "Sosmed" : "@dafaelpriza_",
                "Kesan" : "Asyik dan loyal, selalu ada buat teman.",
                "Pesan" : "Tetap jadi teman yang menyenangkan dan semangat terus, Bang."
            },
            {
                "Nama": "Juwita Sari", 
                "NIM" : "124450066",
                "Asal" : "Lampung Barat",
                "Alamat" : "Pemda",
                "Hobi": "Lihat bulan",
                "Umur" : "19",
                "Sosmed" : "@ju.juwitaaa_",
                "Kesan" : "Tenang dan puitis, bikin suasana jadi adem.",
                "Pesan" : "Semoga malam-malamnya selalu cerah buat lihat bulan, Kak."
            },
            {
                "Nama": "Muhammad Afdal Lutfi", 
                "NIM" : "124450047",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Jl Pulau Damar",
                "Hobi": "Taptap layar kalo Bryan live",
                "Umur" : "19",
                "Sosmed" : "@afdall.03",
                "Kesan" : "Humoris dan gampang akrab dengan siapa saja.",
                "Pesan" : "Terus semangat dan jaga kesehatan ya, Bang."
            },
            {
                "Nama": "Salsabila Nazwa Putri", 
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Supel dan asyik, cocok diajak nongkrong bareng.",
                "Pesan" : "Semoga kopinya selalu enak dan harinya menyenangkan, Kak."
            },
            {
                "Nama": "Muhammad Ridwan", 
                "NIM" : "123450091",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belwis",
                "Hobi": "Nganterin Datasena ke gedung F",
                "Umur" : "21",
                "Sosmed" : "@mridwaan_22",
                "Kesan" : "Baik hati dan sigap kalau dimintai tolong.",
                "Pesan" : "Tetap semangat dan semoga selalu dilancarkan urusannya, Bang."
            },
            {
                "Nama": "Andra Ilham Bintang", 
                "NIM" : "124450060",
                "Asal" : "Sumatera Selatan",
                "Alamat" : "Kota Baru",
                "Hobi": "Ngitungin kelopak bunga di kebun",
                "Umur" : "18",
                "Sosmed" : "@andra.lhm",
                "Kesan" : "Tenang dan sabar, punya hobi yang unik.",
                "Pesan" : "Semoga kebunnya selalu mekar dan tetap semangat, Bang."
            },
            {
                "Nama": "Bryan Paskah Telaumbanua", 
                "NIM" : "124450003",
                "Asal" : "Nias",
                "Alamat" : "Belwis",
                "Hobi": "Live TikTok",
                "Umur" : "22",
                "Sosmed" : "@bryantel_",
                "Kesan" : "Ekspresif dan seru, selalu punya bahan obrolan.",
                "Pesan" : "Semoga livenya makin ramai dan tetap semangat, Bang."
            },
            {
                "Nama": "Ghiyats Thabularasa Meardhy", 
                "NIM" : "124450067",
                "Asal" : "Bekasi",
                "Alamat" : "Korpri",
                "Hobi": "Ngegift live Bryan",
                "Umur" : "17",
                "Sosmed" : "@meardhy_ghiyats",
                "Kesan" : "Ramah dan dermawan, enak diajak berteman.",
                "Pesan" : "Tetap semangat kuliahnya dan jangan lupa atur uang jajan, Bang."
            },
            {
                "Nama": "Indah Julia Mawar Pratiwi", 
                "NIM" : "124450055",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Bengong",
                "Umur" : "20",
                "Sosmed" : "@indahjuliaa",
                "Kesan" : "Kalem dan santai, enak diajak ngobrol.",
                "Pesan" : "Semoga selalu tenang dan bahagia dengan caranya sendiri, Kak."
            },
            {
                "Nama": "Jacinda Kesya Alvara", 
                "NIM" : "124450023",
                "Asal" : "Kalimantan Barat",
                "Alamat" : "Korpri",
                "Hobi": "Nyapu depan gacoan",
                "Umur" : "18",
                "Sosmed" : "@cacalvra",
                "Kesan" : "Lucu dan seru, bikin suasana jadi lebih ramai.",
                "Pesan" : "Tetap jadi pribadi yang ceria dan semangat terus, Kak."
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan", 
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Rajin dan bersemangat, selalu terlihat segar di pagi hari.",
                "Pesan" : "Semoga paginya selalu produktif dan tetap semangat, Bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()

if menu == "Departemen MIKFES":
    def departemen_mikfes():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1KunJwKUAtXSeJWStiBY3E22g31ySE5db&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YVfyF_84PyH-iahmL7hGdNrkiuLrWvPj&sz=w1000",
                "https://drive.google.com/thumbnail?id=14VPk-ShjTjnj4fDiKztz_WEpKaOZzrqF&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mwulmzj9ZyG7_Hn9C3AcO6lL4fFZvxXq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1B1xnmTfBNm6THDaYEGumOzmoG26Oeb5X&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Wr5lendBrvxtk1fhkM8pSfzeJ899uSfD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1j_tkOe45i7phandICi4VXfeV2qle9hvO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xJ9kgCVoSDaX4I7VmpPAhgWurfQDpPnn&sz=w1000",
                "https://drive.google.com/thumbnail?id=1l-hshDMm9ZCSWt5Ez-F_nSHdh_TjEZBZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KIhipi1EfXGYoHwdSldLTS1dzCfymOFs&sz=w1000",
                "https://drive.google.com/thumbnail?id=18houjnI7YwabEryeJKmTpVycxLpWOpn7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Jzy9xKAbeLsgA2Rxm3WRp7GkfpS6dnuL&sz=w1000",
                "https://drive.google.com/thumbnail?id=1QX8uzydZnvooGNnCK_MgnqwRB9Yheagl&sz=w1000",
                "https://drive.google.com/thumbnail?id=1jWFBaCMtxsYbSr8KqQlw4yysy_P-TCB_&sz=w1000",
                "https://drive.google.com/thumbnail?id=15Azu_qQo0S0TQK-Q3LsdTEjEIradwduB&sz=w1000",
                "https://drive.google.com/thumbnail?id=1HgmYa77QaAtT_hNAr7jirMgcL1zppgOT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1U19Sb_Ep5xNnDspOK9gFdetqjfqXIBfm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1y2CPyR1PhmUTgRwuWjt2Fz3_n2C3y9v7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1_Ka2JD-5fdVwv4LlQJVsr0PW34S65Nyu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FaAgB1FbP8_E8c8N1FtBKiIwXHmjVQXC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nYeVLDt_Hu-mBQt7auGJf3hoSSlsektx&sz=w1000",
                "https://drive.google.com/thumbnail?id=13tzhGEnWEqtFuA8NQjU6JzUX9CR_sFnt&sz=w1000",
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
                "Kesan" : "Kalem dan menyenangkan, enak diajak ngobrol santai.",
                "Pesan" : "Semoga tidurnya selalu nyenyak dan tetap semangat kuliahnya, Bang."
            },
            {
                "Nama": "Tanty Widiyastuti", 
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Ramah dan wawasannya luas, nyambung diajak diskusi.",
                "Pesan" : "Semoga bacaannya selalu seru dan tetap semangat, Kak."
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi", 
                "NIM" : "123450048",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Asyik dan kreatif, apalagi kalau sudah main musik.",
                "Pesan" : "Terus berkarya, Bang."
            },
            {
                "Nama": "Manuel Frederika", 
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Lincah dan sportif, seru diajak diskusi bareng.",
                "Pesan" : "Semoga makin jago tenis mejanya dan tetap sehat, Bang."
            },
            {
                "Nama": "Ni Made Okta Viola Darma Putri", 
                "NIM" : "124450005",
                "Asal" : "Bali",
                "Alamat" : "Nusa Penida",
                "Hobi": "Menghayal",
                "Umur" : "12",
                "Sosmed" : "Violaadrtr_",
                "Kesan" : "Tenang dan kreatif, banyak ide yang menarik.",
                "Pesan" : "Semoga khayalannya jadi kenyataan dan tetap semangat, Kak."
            },
            {
                "Nama": "Risa Romadona", 
                "NIM" : "124450127",
                "Asal" : "Natar",
                "Alamat" : "Natar",
                "Hobi": "Rolling skate",
                "Umur" : "20",
                "Sosmed" : "risarmdna",
                "Kesan" : "Lincah dan penuh semangat, suka tantangan baru.",
                "Pesan" : "Tetap hati-hati dan semoga makin lihai main skate, Kak."
            },
            {
                "Nama": "Vannisa Ramadhani", 
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Hangat dan seru, gampang akrab dengan siapa saja.",
                "Pesan" : "Semoga selalu ada tontonan seru dan tetap semangat, Kak."
            },
            {
                "Nama": "Yulia Cristine Malau", 
                "NIM" : "124450119",
                "Asal" : "Jambi",
                "Alamat" : "Sabah Balau",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@krnylee",
                "Kesan" : "Rajin dan tekun, jadi teladan buat teman-temannya.",
                "Pesan" : "Tetap semangat belajarnya dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Akeyla Fairuz Shafi", 
                "NIM" : "1234501",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Dengerin Musik",
                "Umur" : "21",
                "Sosmed" : "@keyashafi",
                "Kesan" : "Santai dan menyenangkan, selera musiknya pasti asyik.",
                "Pesan" : "Semoga playlist-nya selalu menemani hari yang baik, Kak."
            },
            {
                "Nama": "Elsa Sitorus", 
                "NIM" : "124450088",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Pemda",
                "Hobi": "Rebahan",
                "Umur" : "21",
                "Sosmed" : "@_els.a",
                "Kesan" : "Santai dan apa adanya, nyaman diajak bergaul.",
                "Pesan" : "Semoga selalu bisa istirahat cukup dan tetap semangat, Kak."
            },
            {
                "Nama": "Fadya Izzatul ‘Aini", 
                "NIM" : "124450062",
                "Asal" : "Pringsewu",
                "Alamat" : "Airan",
                "Hobi": "Mancing",
                "Umur" : "20",
                "Sosmed" : "fadyaizzatul_",
                "Kesan" : "Sabar dan tenang, enak diajak ngobrol.",
                "Pesan" : "Semoga pancingannya selalu dapat hasil dan tetap semangat, Kak."
            },
            {
                "Nama": "Lovianora Saragih", 
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Lembut dan menyenangkan, mudah akrab.",
                "Pesan" : "Tetap semangat kuliahnya dan nikmati musik favoritnya, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh", 
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Santai dan lucu, asyik diajak main bareng.",
                "Pesan" : "Semoga rank-nya naik terus, tapi jangan lupa kuliah, Bang."
            },
            {
                "Nama": "Sherena Florencia", 
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "@sher_renna",
                "Kesan" : "Ceria dan stylish, enak diajak ngobrol soal tren.",
                "Pesan" : "Tetap semangat dan semoga makin kreatif berdandan, Kak."
            },
            {
                "Nama": "Razin Hafid Hamdi", 
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Energik dan kompak, seru diajak main bola.",
                "Pesan" : "Semoga makin jago futsalnya dan selalu sehat, Bang."
            },
            {
                "Nama": "Faiza Try Anjani", 
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "@Faizaanjanii",
                "Kesan" : "Kalem dan suka bercerita, nyambung kalau bahas novel.",
                "Pesan" : "Semoga selalu ada novel seru untuk dibaca, Kak."
            },
            {
                "Nama": "Gathfan Nadif Ali", 
                "NIM" : "124450001",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Rajabasa",
                "Hobi": "Main game",
                "Umur" : "20",
                "Sosmed" : "@gathfannadif",
                "Kesan" : "Asyik dan gampang akrab, seru diajak mabar.",
                "Pesan" : "Tetap semangat dan semoga menang terus, Bang."
            },
            {
                "Nama": "Hafidz Wahdiansyah", 
                "NIM" : "124450064",
                "Asal" : "Metro",
                "Alamat" : "Metro Kibang, Lampung Timur",
                "Hobi": "3N (Ngoding, Ngegame, Nyibukin diri)",
                "Umur" : "20",
                "Sosmed" : "@apiszzaja_",
                "Kesan" : "Kreatif dan multitalenta, seru diajak ngobrol soal teknologi.",
                "Pesan" : "Semoga kodingannya lancar dan jangan lupa istirahat, Bang."
            },
            {
                "Nama": "Kaleb Filbert Istel", 
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Disiplin dan berwawasan, enak diajak ngobrol.",
                "Pesan" : "Terus semangat dan semoga makin sehat serta kuat, Bang."
            },
            {
                "Nama": "Melva Shaprina Febrianti", 
                "NIM" : "124450087",
                "Asal" : "Sumsel",
                "Alamat" : "Sukarame",
                "Hobi": "Scroll",
                "Umur" : "19",
                "Sosmed" : "@melva_fbrt",
                "Kesan" : "Santai dan menyenangkan, update soal hal-hal terbaru.",
                "Pesan" : "Tetap semangat dan jangan terlalu lama scroll sebelum tidur, Kak."
            },
            {
                "Nama": "Muhammad Syafiqul Falakh", 
                "NIM" : "124450099",
                "Asal" : "Lampung Utara",
                "Alamat" : "Asrama TB 3",
                "Hobi": "Membaca",
                "Umur" : "20",
                "Sosmed" : "@syafiqui",
                "Kesan" : "Tenang dan sopan, enak diajak berdiskusi.",
                "Pesan" : "Semoga bacaannya terus bertambah dan tetap semangat, Bang."
            },
            {
                "Nama": "Rifky Henry Ferdianto", 
                "NIM" : "124450115",
                "Asal" : "Kobum",
                "Alamat" : "Rajabasa",
                "Hobi": "Lari dari kenyataan",
                "Umur" : "28",
                "Sosmed" : "@henryferdianto",
                "Kesan" : "Santai dan lucu, banyak cerita seru.",
                "Pesan" : "Tetap semangat dan semoga urusannya selalu lancar, Bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()
 
if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1eAlp4t8XqdI3MuDsOmXzRDucpXzqvDiP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sujJKUbssKQ001hcvsYqxA1nfkosiUIf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Ll9bGBLrHZZLILhqFGrny6g3SvpPb0zj&sz=w1000",
                "https://drive.google.com/thumbnail?id=1rsxHmnRVnUQHouRlqmhIQbwz1Vg9yqfI&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BaUf1oF7XtN4iiR2xxUQPZ7-0k0M-hu8&sz=w1000",
                "https://drive.google.com/thumbnail?id=1g7p4SiU7KivD04BdVRudiaZ0AUJ-ESBC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1LEh6IsF0jf0qXn7E-HVzyw7u34qpklVi&sz=w1000",
                "https://drive.google.com/thumbnail?id=1RmD8IE7h91oIFJXdV2oLSIC6SOb-YdIT&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Qb6h8f9M_C6p1asBcCLuoCjARV7CMHGG&sz=w1000",
                "https://drive.google.com/thumbnail?id=19S3dLNqCr_I05ond63AcqU3_p5U7VGsd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1FN7Zjt6sEtrpsuYznal0BDvFH4Ef8dbu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mhC5pXkfSbbQnRN8BoHNYS6yNl6FLc7p&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bqhlP9z2i7wEGlHLKfaFXp5dXVFq8oJ2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Bl68yjC0pHzj5siwfCL0Tm4KBEbgYRoL&sz=w1000",
                "https://drive.google.com/thumbnail?id=1I2xYoSETY9_2ULNRoujzDAGEc-5FafoO&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Z4ZJkmnzwYxZWZOS0Nklv3wHZ4eBvb50&sz=w1000",
                "https://drive.google.com/thumbnail?id=1fS4PLcacEBNpVWQmL1TR3j97-Tae2guU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XNHJnlrpx1Hm8hHtNjSiOgWlxrgFBuv9&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Nayla Salsabila Fathianisa", 
                "NIM" : "123450082",
                "Asal" : "Payakumbuh, Sumatera Barat",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "20",
                "Sosmed" : "@naylasalsabilaa._",
                "Kesan" : "Kalem dan hangat, nyambung kalau ngobrol soal lagu favorit.",
                "Pesan" : "Semoga harinya selalu ditemani lagu-lagu yang asyik, Kak."
            },
            {
                "Nama": "Donna Maya Puspita", 
                "NIM" : "123450028",
                "Asal" : "Bekasi",
                "Alamat" : "Way Huwi",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Ramah dan menyenangkan, gampang bikin orang nyaman.",
                "Pesan" : "Tetap semangat kuliahnya dan jaga kesehatan ya, Kak."
            },
            {
                "Nama": "Labo John Nuel Napitupulu", 
                "NIM" : "123450037",
                "Asal" : "Medan",
                "Alamat" : "Belwis",
                "Hobi": "Motoran",
                "Umur" : "20",
                "Sosmed" : "@noerruuu",
                "Kesan" : "Santai dan seru, asyik diajak ngobrol soal motor.",
                "Pesan" : "Semoga selalu aman di jalan dan tetap semangat, Bang."
            },
            {
                "Nama": "Anash Tasya Ausyaqila", 
                "NIM" : "124450050",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Way Halim",
                "Hobi": "Nonton",
                "Umur" : "20",
                "Sosmed" : "@anshtsyaaql",
                "Kesan" : "Ceria dan enak diajak ngobrol soal tontonan.",
                "Pesan" : "Semoga selalu ada film dan serial seru buat ditonton, Kak."
            },
            {
                "Nama": "Felisya Nabila Putri Nugroho", 
                "NIM" : "124450104",
                "Asal" : "Lampung Timur",
                "Alamat" : "Kota Baru",
                "Hobi": "Gangguin Anash dan Razan",
                "Umur" : "19",
                "Sosmed" : "@felisyanbl__",
                "Kesan" : "Lucu dan jahil, bikin suasana jadi rame.",
                "Pesan" : "Tetap semangat dan jangan kelewat jahil ya, Kak."
            },
            {
                "Nama": "Muhammad Razan Maulana Pratama", 
                "NIM" : "124450031",
                "Asal" : "Jawa Barat",
                "Alamat" : "Korpri",
                "Hobi": "Foto Orang",
                "Umur" : "21",
                "Sosmed" : "@muh_razan_",
                "Kesan" : "Santai dan kreatif, hasil fotonya pasti menarik.",
                "Pesan" : "Semoga makin jago motret dan tetap semangat, Bang."
            },
            {
                "Nama": "Sania Dwi Ayu Lestari", 
                "NIM" : "123450086",
                "Asal" : "Karawang",
                "Alamat" : "Airan Raya",
                "Hobi": "Nonton Netflix",
                "Umur" : "21",
                "Sosmed" : "@saniayyllstr",
                "Kesan" : "Asyik dan banyak rekomendasi tontonan seru.",
                "Pesan" : "Tetap semangat dan jangan begadang kebanyakan maraton film, Kak."
            },
            {
                "Nama": "Allisha", 
                "NIM" : "124450019",
                "Asal" : "Kayangan",
                "Alamat" : "Heaven",
                "Hobi": "Mancing",
                "Umur" : "16",
                "Sosmed" : "@aallishaa.a",
                "Kesan" : "Unik dan menyenangkan, selalu ada cerita seru.",
                "Pesan" : "Semoga pancingannya selalu dapat hasil dan tetap semangat, Kak."
            },
            {
                "Nama": "Alya Ramadhanti", 
                "NIM" : "124450091",
                "Asal" : "Jambi",
                "Alamat" : "Airan",
                "Hobi": "Jalan-jalan",
                "Umur" : "19",
                "Sosmed" : "@alya.rmdhnti",
                "Kesan" : "Ceria dan gampang akrab, banyak cerita perjalanan.",
                "Pesan" : "Semoga bisa jalan-jalan ke banyak tempat seru."
            },
            {
                "Nama": "Bunga Clarisa Sefa", 
                "NIM" : "124450097",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Lampung Selatan",
                "Hobi": "Belajar",
                "Umur" : "20",
                "Sosmed" : "@bungaclrssf",
                "Kesan" : "Tekun dan fokus, jadi contoh yang baik buat teman.",
                "Pesan" : "Tetap semangat belajarnya dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Difanya Husakina", 
                "NIM" : "124450043",
                "Asal" : "Pagar Alam",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca Al Qur'an",
                "Umur" : "20",
                "Sosmed" : "@difanyhsa",
                "Kesan" : "Tenang dan menyejukkan, enak diajak ngobrol.",
                "Pesan" : "Semoga selalu istiqomah dan diberi kelancaran dalam segala hal, Kak."
            },
            {
                "Nama": "Nazlah Auliya", 
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Berenang",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Aktif dan ceria, kelihatan hobi olahraga.",
                "Pesan" : "Tetap semangat berenangnya dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Raihana Adelia Putri", 
                "NIM" : "123450041",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Airan Raya 1",
                "Hobi": "Menulis, membaca",
                "Umur" : "20",
                "Sosmed" : "@r.hanaap",
                "Kesan" : "Kalem dan kreatif, tulisannya pasti menarik.",
                "Pesan" : "Terus menulis dan semoga karyanya makin banyak dibaca, Kak."
            },
            {
                "Nama": "Daffa Kharisma Adzana", 
                "NIM" : "124450061",
                "Asal" : "Surabaya",
                "Alamat" : "Sukarame",
                "Hobi": "-",
                "Umur" : "21",
                "Sosmed" : "@daffascript",
                "Kesan" : "Tenang dan sopan, nyaman diajak bergaul.",
                "Pesan" : "Tetap semangat dan semoga selalu dilancarkan urusannya, Bang."
            },
            {
                "Nama": "Edsel Adya Pradipta", 
                "NIM" : "124450098",
                "Asal" : "Lampung Selatan",
                "Alamat" : "Natar",
                "Hobi": "Nonton Anime",
                "Umur" : "20",
                "Sosmed" : "@edsel_0712",
                "Kesan" : "Asyik dan nyambung kalau ngobrol soal anime.",
                "Pesan" : "Semoga selalu ada anime baru yang seru buat ditonton, Bang."
            },
            {
                "Nama": "Lucia Advencia Rachel Nainggolan", 
                "NIM" : "124450085",
                "Asal" : "Bekasi",
                "Alamat" : "Belwis",
                "Hobi": "Tidur",
                "Umur" : "20",
                "Sosmed" : "@luciarachel_",
                "Kesan" : "Santai dan menyenangkan, gampang akrab.",
                "Pesan" : "Semoga tidurnya selalu nyenyak dan tetap semangat kuliahnya, Kak."
            },
            {
                "Nama": "Shafa Delaila Azzahra", 
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Perumahan Pemda",
                "Hobi": "Melukis dan menulis",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Kreatif dan hangat, punya banyak ide menarik.",
                "Pesan" : "Terus berkarya lewat lukisan dan tulisannya, Kak."
            },
            {
                "Nama": "Zannuba Arifah Ilman", 
                "NIM" : "124450112",
                "Asal" : "Lampung Timur",
                "Alamat" : "Rajabasa",
                "Hobi": "Begong",
                "Umur" : "18",
                "Sosmed" : "@xifasky",
                "Kesan" : "Kalem dan santai, enak diajak ngobrol.",
                "Pesan" : "Tetap semangat dan semoga harinya selalu menyenangkan."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()
 
if menu == "Departemen SSD":
    def departemen_ssd():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1AjKtQbIcfDbm7dHdWwas6Uvy-czCasni&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qOJLWWGaivBi7Du2SnocBVgh_Pqsc1Aa&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XTUm7ML0b-bjpO8uHAnUlD-F8gECb7Vg&sz=w1000",
                "https://drive.google.com/thumbnail?id=18vLZ5cfaUxSc-Cv4eRaTZ5cb-HNhVxgS&sz=w1000",
                "https://drive.google.com/thumbnail?id=1h17d0CmJr-LD_6-Az9QNcoGOaxznJDf2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1-T77RMt_eLytaqgH7zb_wQ2k_Mro7Deu&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aHo8ZT9QrpsulViLrpwGymT5E9NJ6lx1&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aIWCRZ1FsvaTK3AYQ0RqdOy75Olyd2v2&sz=w1000",
                "https://drive.google.com/thumbnail?id=1iWfkmE2Ufs6vGjjZa2gK5EDHoT0FdW_E&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dUcYvjZGuW7JM3ciwcV3XntfNkYtZepf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1dUcYvjZGuW7JM3ciwcV3XntfNkYtZepf&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A-3xxiUEpWl_Oqptum8w_lOnXX9Hkub5&sz=w1000",
        ]
        data_list = [
            {
                "Nama": "Ihsan Maulana Yusuf",
                "NIM": "123450110",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Belwis",
                "Hobi": "Mencari dan membaca jurnal, mencari pak lucy",
                "Sosmed": "@ihsan.myusuf",
                "Kesan": "Pembawaannya tenang dan wawasannya luas, nyaman diajak diskusi.",
                "Pesan": "Semoga jurnal yang dicari selalu ketemu dan tetap semangat, Bang."

            },
            {
                "Nama": "Hanifah Inaya Sani",
                "NIM": "123450123",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Masak",
                "Sosmed": "@_inayasani",
                "Kesan": "Hangat dan bersahabat, selalu enak diajak bercerita.",
                "Pesan": "Semoga masakannya makin lezat dan tetap semangat kuliahnya, Kak."    
            },
            {
                "Nama": "Afifah Fauziah",
                "NIM": "123450002",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Airan",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Menyenangkan dan punya banyak bahan obrolan seru.",
                "Pesan": "Semoga selalu ada waktu buat maraton film favoritnya, Kak." 
            },
            {
                "Nama": "Hasan Nur Ramadan",
                "NIM": "123450013",
                "Umur": "21",
                "Asal": "Lampung Tengah",
                "Alamat": "Pemda",
                "Hobi": "Megang Docker",
                "Sosmed": "@hasan.ramadan08",
                "Kesan": "Tenang dan cekatan, enak diajak ngobrol soal teknologi.",
                "Pesan": "Tetap semangat ngulik dan jangan lupa istirahat, Bang."
            },
            {
                "Nama": "Layina Ropiqo",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Ulet dan mandiri, tapi tetap asyik dan santai.",
                "Pesan": "Semoga rezekinya lancar dan tetap jaga kesehatan, Kak."
            },
            {
                "Nama": "Moch. Iqbal Az Zahir",
                "NIM": "124450052",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Natar",
                "Hobi": "Drakor",
                "Sosmed": "@iqbalazzahir_",
                "Kesan": "Supel dan seru, banyak rekomendasi tontonan menarik.",
                "Pesan": "Semoga selalu ada drama baru yang seru, tapi jangan sampai kurang tidur, Bang."
            },
            {
                "Nama": "Talitha Justine",
                "NIM": "124450076",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Pemda",
                "Hobi": "Tidur",
                "Sosmed": "@talljtine_",
                "Kesan": "Kalem dan adem, enak diajak bergaul.",
                "Pesan": "Tetap semangat dan semoga istirahatnya selalu berkualitas."
            },
            {
                "Nama": "Anadia Carana",
                "NIM": "123450019",
                "Umur": "19",
                "Asal": "Palembang",
                "Alamat": "Way Huwi",
                "Hobi": "Nyari Duit",
                "Sosmed": "@anadiacrn_",
                "Kesan": "Rajin dan bersemangat, bikin orang di sekitarnya ikut termotivasi.",
                "Pesan": "Semoga usahanya sukses dan jangan lupa luangkan waktu istirahat, Kak."
            },
            {
                "Nama": "Abdillah Fikri Al Pome",
                "NIM": "122450000",
                "Umur": "21",
                "Asal": "Oku",
                "Alamat": "Airan",
                "Hobi": "Basket",
                "Sosmed": "@pomest__",
                "Kesan": "Lincah dan kompak, asyik diajak ngobrol soal olahraga.",
                "Pesan": "Semoga makin jago di lapangan dan selalu sehat, Bang."
            },
            {
                "Nama": "Afdhal Rahmad Setiawan",
                "NIM": "124450008",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Samping kamar rafli",
                "Hobi": "Mancing Mania",
                "Sosmed": "@dhalsetiawan",
                "Kesan": "Tenang dan sabar, punya banyak cerita seru soal mancing.",
                "Pesan": "Semoga strike terus dan tetap semangat, Bang."
            },
            {
                "Nama": "Anggun Nita",
                "NIM": "124450009",
                "Umur": "20",
                "Asal": "Lampung Utara",
                "Alamat": "Belwis",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@anggunnitaaa_",
                "Kesan": "Riang dan hangat, gampang bikin suasana jadi santai.",
                "Pesan": "Tetap jadi pribadi yang menyenangkan dan semangat terus, Kak."
            },
            {
                "Nama": "Della Anisa Fitri",
                "NIM": "123450002",
                "Umur": "18",
                "Asal": "Lampung Timur",
                "Alamat": "Margo Lestasi",
                "Hobi": "Menonton Marvel",
                "Sosmed": "@fifah_zy",
                "Kesan": "Supel dan nyambung diajak ngobrol soal film superhero.",
                "Pesan": "Semoga selalu dapat tontonan seru dan tetap semangat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_ssd()

if menu == "Departemen Eksternal":
    def departemen_eksternal():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1RSDO3F7bp529iJSNawy5mFHMGG5y-YQY&sz=w1000",
                "https://drive.google.com/thumbnail?id=17lukf2TIbZQiEFe99zvV2jV33HfUGcnQ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1bf8OB-RRxrE7zmHy5tdJ4JLqw-OYRBw_&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nBe4fpFv_WhW4Pf_rF_njNHEcnl1vN-l&sz=w1000",
                "https://drive.google.com/thumbnail?id=1N6D21ZQryLs8lLTgwBWjRp0iYmIo6DmE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1WJ8GvPGEMkN7d1nERtATfbY7jIOPVx3y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1V-w39Nm-nCvZx6DcfWQTrOpl9fJ2KdCw&sz=w1000",
                "https://drive.google.com/thumbnail?id=1F-p3TN7JhIGkhvs54Ae-5_0OZQQxkzGP&sz=w1000",
                "https://drive.google.com/thumbnail?id=1H2mKEJpGLNEejTC1loDsMbPhr6m3Upbe&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hLcLvX2Hagv4X1d9lUU7YlRgePokQvvg&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ddXOr_yBPPahDbU9OSl4_LRSWeYLIlif&sz=w1000",
                "https://drive.google.com/thumbnail?id=1DKmXV2jWXeU2oVz-yryLUDVh9Ul9p-DZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zVxczPYmw5fcPDbZfxthgAfNbHKje7yz&sz=w1000",
                "https://drive.google.com/thumbnail?id=1AwnC95Bmsa8C4FlHReTJvXgQ1hvd15iD&sz=w1000",
                "https://drive.google.com/thumbnail?id=1_fQYaTiZ7WpRRA3x_zDediIyDbpsM6qd&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ojcsVhSddHqGnYorr7j6qR75Hq365qwX&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KfKBD0b8gJ5B7rCkzfpSVtBA5W2JqjDG&sz=w1000",
                "https://drive.google.com/thumbnail?id=16wSyfPQT_I-ifyb5EdTGnABxQEOZuMJZ&sz=w1000",
                "https://drive.google.com/thumbnail?id=149mHgBDznniRSNnE-hCAY0G7zeKDL3jm&sz=w1000",
                "https://drive.google.com/thumbnail?id=1sU-PKe-BUWa8d04ffwcPDnBE-sA5HKTq&sz=w1000",
                "https://drive.google.com/thumbnail?id=1EYBV6RRqusJHID9wBnWblQn3Bt5btWhU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1wqgESOTAgRvpxBRd9_VCeXJx59sqVNdt&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Arini Puteri Elandra",
                "NIM": "123450069",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Teluk Betung Selatan",
                "Hobi": "Nonton Kartun",
                "Sosmed": "@elandraa_",
                "Kesan": "Hangat dan bersahabat, gampang bikin orang betah ngobrol.",
                "Pesan": "Semoga selalu ada kartun seru buat ditonton dan tetap semangat, Kak."
            },
            {
                "Nama": "Nabyla Sharfina",
                "NIM": "123450008",
                "Umur": "20",
                "Asal": "Bengkulu",
                "Alamat": "Jalan Lapas",
                "Hobi": "Jalan - Jalan",
                "Sosmed": "@bylaash",
                "Kesan": "Supel dan penuh semangat, asyik diajak jalan bareng.",
                "Pesan": "Semoga bisa menjelajah banyak tempat baru dan tetap sehat, Kak."
            },
            {
                "Nama": "Khoirul Muttoharoh",
                "NIM": "1234500",
                "Umur": "21",
                "Asal": "Lambar",
                "Alamat": "Airan",
                "Hobi": "Main",
                "Sosmed": "@khoirul_muttoharoh",
                "Kesan": "Easy going dan menyenangkan, cocok jadi teman nongkrong.",
                "Pesan": "Tetap semangat dan jangan lupa kuliahnya, Bang."
            },
            {
                "Nama": "Ahmad Rizky",
                "NIM": "124450050",
                "Umur": "21",
                "Asal": "Tangerang Selatan",
                "Alamat": "GH",
                "Hobi": "Ga Ngapa Ngapain",
                "Sosmed": "@ahmad.rizky___",
                "Kesan": "Kalem dan apa adanya, nyaman diajak ngobrol.",
                "Pesan": "Semoga harinya selalu tenang dan tetap semangat, Bang."
            },
            {
                "Nama": "Adinda Deswita Maharani",
                "NIM": "124450083",
                "Umur": "20",
                "Asal": "Ikut kadep",
                "Alamat": "Love earth",
                "Hobi": "Jadi idol",
                "Sosmed": "@adindaadma",
                "Kesan": "Energik dan percaya diri, enak dilihat kalau lagi tampil.",
                "Pesan": "Semoga mimpinya jadi idol makin dekat, tetap semangat."
            },
            {
                "Nama": "Ahmad Bimo Akbar Arkana",
                "NIM": "124450113",
                "Umur": "20",
                "Asal": "Tanggamus",
                "Alamat": "Balam",
                "Hobi": "Lihat lihat perumahan",
                "Sosmed": "@bimo_arkana",
                "Kesan": "Tenang dan punya cita-cita yang jelas.",
                "Pesan": "Semoga nanti bisa punya rumah sesuai keinginan, Bang."
            },
            {
                "Nama": "Alfaya Abiyyi",
                "NIM": "124450006",
                "Umur": "20",
                "Asal": "Balam",
                "Alamat": "Balam",
                "Hobi": "Makan yang manis biar manis",
                "Sosmed": "@alfabiyi",
                "Kesan": "Murah senyum dan enak diajak bercanda.",
                "Pesan": "Tetap semangat dan jaga kesehatan, Bang."
            },
            {
                "Nama": "Asri Meilani",
                "NIM": "124450010",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri Raya",
                "Hobi": "Menonton film",
                "Sosmed": "@asrmeilani",
                "Kesan": "Tenang dan ramah, banyak rekomendasi film bagus.",
                "Pesan": "Semoga selalu ketemu film yang pas di hati, Kak."
            },
            {
                "Nama": "Bima Ekayasa",
                "NIM": "124450106",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Berlaku humoris dan manis",
                "Sosmed": "@bimayasa_",
                "Kesan": "Lucu dan hangat, bikin suasana jadi cair.",
                "Pesan": "Semoga humornya tetap segar dan semangat terus, Bang."
            },
            {
                "Nama": "Indah Khairunnisa",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Ampera",
                "Alamat": "Disini aja",
                "Hobi": "Mancing emosi, mancing ikan, mancing kecebong, mancing cupang",
                "Sosmed": "@khaindaa_",
                "Kesan": "Jenaka dan penuh kejutan, selalu ada yang bikin tertawa.",
                "Pesan": "Semoga pancingannya selalu menghasilkan hal yang menyenangkan, Kak."
            },
            {
                "Nama": "Riska Erlis Dayu Tiara",
                "NIM": "124450022",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Bebas",
                "Hobi": "Ngefollow up chat",
                "Sosmed": "@erlsriska",
                "Kesan": "Gesit dan komunikatif, enak diajak kerja bareng.",
                "Pesan": "Tetap semangat dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Yollanda Agustina",
                "NIM": "124450024",
                "Umur": "",
                "Asal": "Kerangka Bawang Sebelah Barat",
                "Alamat": "Kayu Mulya",
                "Hobi": "Tanya bang Henry",
                "Sosmed": "@yollanda_agustina16",
                "Kesan": "Penasaran dan suka belajar hal baru.",
                "Pesan": "Semoga selalu dapat jawaban yang dicari dan tetap semangat, Kak."
            },
            {
                "Nama": "Aditya Taufiqurrohman",
                "NIM": "123450032",
                "Umur": "22",
                "Asal": "Tetangga kadep",
                "Alamat": "Belwis",
                "Hobi": "Memancing keributan",
                "Sosmed": "@adityattj",
                "Kesan": "Ekspresif dan blak-blakan, selalu bikin ramai.",
                "Pesan": "Tetap semangat dan semoga makin adem, Bang."
            },
            {
                "Nama": "Fathya Intami Gusda",
                "NIM": "123450095",
                "Umur": "25",
                "Asal": "Tangsel",
                "Alamat": "Sukarame",
                "Hobi": "Baca wattpad",
                "Sosmed": "@fatthyaa_",
                "Kesan": "Kalem dan suka bercerita, nyambung kalau bahas cerita.",
                "Pesan": "Semoga selalu ada cerita baru yang seru untuk dibaca, Kak."
            },
            {
                "Nama": "Tarisya Hidayatul Rahmi",
                "NIM": "123450052",
                "Umur": "",
                "Asal": "Luhak tanah data",
                "Alamat": "Gerbar",
                "Hobi": "Jadi orang baik",
                "Sosmed": "",
                "Kesan": "Tulus dan murah hati, nyaman diajak berteman.",
                "Pesan": "Semoga kebaikannya selalu berbalas hal baik, Kak."
            },
            {
                "Nama": "Ashila Islamisahfa Vanisha",
                "NIM": "124450028",
                "Umur": "20",
                "Asal": "Sini",
                "Alamat": "Jauh pokoknya",
                "Hobi": "Tidur",
                "Sosmed": "@kshigf",
                "Kesan": "Santai dan adem, enak diajak ngobrol.",
                "Pesan": "Semoga istirahatnya selalu cukup dan tetap semangat, Kak."
            },
            {
                "Nama": "Dasil N Fadillah",
                "NIM": "124450103",
                "Umur": "19",
                "Asal": "Karawang",
                "Alamat": "Belakang Polda",
                "Hobi": "Ngasih makan ikan cupang",
                "Sosmed": "@d4niel_fdlh",
                "Kesan": "Penyayang dan rajin merawat, orangnya menyenangkan.",
                "Pesan": "Semoga cupang-cupangnya makin cantik dan sehat."
            },
            {
                "Nama": "Favian Arkaanda",
                "NIM": "124450021",
                "Umur": "20",
                "Asal": "Swiss",
                "Alamat": "Tanya bapas",
                "Hobi": "Ngesen kanan",
                "Sosmed": "@fvnun05",
                "Kesan": "Santai dan supel, gampang berbaur.",
                "Pesan": "Tetap semangat dan fokus kuliahnya juga, Bang."
            },
            {
                "Nama": "Muhammad Fathiy Zumar Yazid",
                "NIM": "124450081",
                "Umur": "20",
                "Asal": "Situlah",
                "Alamat": "Pohon mulia",
                "Hobi": "Nyari hobi",
                "Sosmed": "@zyddddddd_",
                "Kesan": "Penuh rasa ingin tahu dan terbuka mencoba hal baru.",
                "Pesan": "Semoga segera nemu hobi yang paling cocok, Bang."
            },
            {
                "Nama": "Muhammad Rizaldi",
                "NIM": "124450093",
                "Umur": "",
                "Asal": "Rahim Ibu",
                "Alamat": "Pasar lantai 3.5",
                "Hobi": "",
                "Sosmed": "@jaldii_",
                "Kesan": "Easy going dan suka bercanda, asyik diajak ngobrol.",
                "Pesan": "Semoga selalu sehat dan lancar semua urusannya, Bang."
            },
            {
                "Nama": "Saskia Nova Magdalena",
                "NIM": "124450074",
                "Umur": "20",
                "Asal": "Banyak Begal",
                "Alamat": "Pinggir Jalan",
                "Hobi": "Nonton thinkerbell",
                "Sosmed": "@smova.19",
                "Kesan": "Ceria dan hangat, enak diajak ngobrol soal tontonan.",
                "Pesan": "Semoga tontonan favoritnya selalu menghibur, Kak."
            },
            {
                "Nama": "Selma Siti Aisyah",
                "NIM": "124450044",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Balam",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@selmasiti_aisyah",
                "Kesan": "Bersahabat dan penuh semangat, seru diajak ke mana saja.",
                "Pesan": "Semoga perjalanannya selalu menyenangkan dan lancar, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_eksternal()

if menu == "Baleg":
    def baleg():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1hJ27yma7GlVYQnkjpwCTbSpdztyOFz4W&sz=w1000",
                "https://drive.google.com/thumbnail?id=1Zu92HLlM_21jSxGry-XqxWXbnRNjl8pg&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mKnfIaz83ci_lnfBA4xF419lGNvImKG-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1j03q4sMY7io4T6P_b_FnOZHKzKj6bM4Y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1BQHZ2S8CWJggymoRn2zotPScJlppFoan&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vvcplfUfK7DpH1YJT-pVmEtVnRnp969P&sz=w1000",
                "https://drive.google.com/thumbnail?id=1XXq5LkF3lCm5PP6TGfk1PF7fJbrz9kmV&sz=w1000",
                "https://drive.google.com/thumbnail?id=1hOWIvQHuczWU1PlbPL8236WJxQgrxb6B&sz=w1000",
                "https://drive.google.com/thumbnail?id=15dKMf8MOESCrcL_InR43lKskW0j4A_Zy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1l1hRfuWCCKYbtflwPbl1CfyWfIXjLhHk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ZyL-CDbkgCJ43Q3qm4bKIJ5nLs0T_T6Q&sz=w1000",
                "https://drive.google.com/thumbnail?id=1C73RoxxcTEAlmd6k7hp--MtZyaKW-rNy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1nIO-PvQG6LvH3pQqyRfnvzr8nqNc4G5J&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Ridho Benedictus Togi Manik",
                "NIM": "123450060",
                "Umur": "20",
                "Asal": "Bukittinggi",
                "Alamat": "Gh",
                "Hobi": "Cuci baju",
                "Sosmed": "@iamridhomanik",
                "Kesan": "Rapi dan telaten, nyaman diajak bergaul.",
                "Pesan": "Semoga selalu semangat dan lancar kuliahnya, Bang."
            },
            {
                "Nama": "Juessi Apridelia Saragih",
                "NIM": "123450085",
                "Umur": "19",
                "Asal": "Buah batu",
                "Alamat": "Pelangi",
                "Hobi": "Ngerepeat lagu stasiun bundaran Hi glen fredl",
                "Sosmed": "@j_eesie",
                "Kesan": "Hangat dan seru, selera musiknya bikin penasaran.",
                "Pesan": "Semoga lagu favoritnya selalu bikin hari jadi lebih baik."
            },
            {
                "Nama": "Dharu Cahyoaji Sasongko",
                "NIM": "123450023",
                "Umur": "19",
                "Asal": "Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Nonton drama AI",
                "Sosmed": "@exvoltas",
                "Kesan": "Santai dan penuh rasa ingin tahu soal hal-hal baru.",
                "Pesan": "Tetap semangat dan semoga selalu nemu tontonan yang seru."
            },
            {
                "Nama": "Gh Mikael Nico Antoni Setiadi",
                "NIM": "124450025",
                "Umur": "20",
                "Asal": "Lamtim",
                "Alamat": "Jati agung",
                "Hobi": "Main mcgg",
                "Sosmed": "@me._kael",
                "Kesan": "Asyik dan kompak, seru diajak mabar.",
                "Pesan": "Semoga menang terus dan tetap jaga waktu istirahat, Bang."
            },
            {
                "Nama": "Siti Sarifah Sumamah",
                "NIM": "124450015",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kedaton",
                "Hobi": "Koleksi kartu boboboi",
                "Sosmed": "@syt.rifa",
                "Kesan": "Riang dan tekun, punya hobi yang unik.",
                "Pesan": "Semoga koleksinya terus bertambah dan tetap semangat."
            },
            {
                "Nama": "Givaro Ananta",
                "NIM": "123450078",
                "Umur": "21",
                "Asal": "Lampung barat",
                "Alamat": "Sukabumi",
                "Hobi": "Minum kopi",
                "Sosmed": "@givarooo",
                "Kesan": "Kalem dan enak diajak ngobrol sambil ngopi.",
                "Pesan": "Semoga kopinya selalu enak dan tetap semangat, Bang."
            },
            {
                "Nama": "Afghanis Nursholehatunnisa",
                "NIM": "124450042",
                "Umur": "20",
                "Asal": "Kepulauan mentawai",
                "Alamat": "Owen kost",
                "Hobi": "Main bareng sekar putri dan suci",
                "Sosmed": "@afghanisnt_",
                "Kesan": "Ceria dan setia kawan, mudah akrab dengan siapa saja.",
                "Pesan": "Semoga pertemanannya selalu hangat dan tetap semangat, Kak."
            },
            {
                "Nama": "Hani Qurrota Aini",
                "NIM": "124450020",
                "Umur": "20",
                "Asal": "City earth",
                "Alamat": "Sukarame",
                "Hobi": "Baca AU",
                "Sosmed": "@haniquratuain_",
                "Kesan": "Imajinatif dan menyenangkan, banyak cerita seru.",
                "Pesan": "Semoga selalu ada bacaan baru yang bikin senang, Kak."
            },
            {
                "Nama": "Jeremia Halim",
                "NIM": "124450101",
                "Umur": "20",
                "Asal": "Tangerang",
                "Alamat": "Teluk Betung",
                "Hobi": "Nyanyi, olahraga",
                "Sosmed": "@jeremia_hm",
                "Kesan": "Energik dan bersahabat, suka berbagi keseruan.",
                "Pesan": "Semoga makin merdu suaranya dan selalu sehat, Bang."
            },
            {
                "Nama": "Monica Patricia Tanjung",
                "NIM": "123450073",
                "Umur": "21",
                "Asal": "Sumut",
                "Alamat": "Kota baru",
                "Hobi": "Merajut",
                "Sosmed": "@monica_tjg",
                "Kesan": "Tenang dan sabar, hasil karyanya pasti rapi.",
                "Pesan": "Semoga rajutannya makin cantik dan tetap semangat, Kak."
            },
            {
                "Nama": "Jona Timothy Ogatse Panjaitan",
                "NIM": "124450121",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Pemda Raya",
                "Hobi": "Nge-gym, koleksi figur",
                "Sosmed": "@nagatseee",
                "Kesan": "Konsisten dan bersemangat, enak diajak ngobrol soal hobi.",
                "Pesan": "Semoga koleksinya makin lengkap dan badan selalu bugar, Bang."
            },
            {
                "Nama": "Sekar Dini Widya Putri",
                "NIM": "124450082",
                "Umur": "20",
                "Asal": "Kota metro",
                "Alamat": "Pemda",
                "Hobi": "Nyiram bunga",
                "Sosmed": "@sekardnwp",
                "Kesan": "Lembut dan penyabar, bikin suasana jadi adem.",
                "Pesan": "Semoga bunga-bunganya mekar dan harinya selalu cerah, Kak."
            },
            {
                "Nama": "Wan Nashwa Alhasni Yuska",
                "NIM": "124450077",
                "Umur": "20",
                "Asal": "Pasay",
                "Alamat": "Belwis",
                "Hobi": "Nyapa angin",
                "Sosmed": "@nshysk",
                "Kesan": "Unik dan santai, selalu punya sudut pandang yang segar.",
                "Pesan": "Tetap jadi diri sendiri dan semoga selalu lancar, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

if menu == "Senator":
    def senator():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1fECzJ0JxSQxWnMWc46WwKfdTDuZ4LEVk&sz=w1000",
                "https://drive.google.com/thumbnail?id=1xz8_eS1BRXnNrypMPrTJLjJ1vdO9L21A&sz=w1000",
                "https://drive.google.com/thumbnail?id=1kkwer09MpI-GN9jU8OYdbPdGFTQqiyrH&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YbQcoDM1qdIxQLWkW3KR-QO6yTdSMKOC&sz=w1000",
                "https://drive.google.com/thumbnail?id=1eVvIxWZDuaTrbO4H_uTtQQqXCUBHEiYr&sz=w1000",
                "https://drive.google.com/thumbnail?id=1YMs1Cri_6JdEBTpU26J19TlvoA-ZUA5h&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KItobRtvCfhgRGN529DIeaQ3N7OT3A-Y&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A1CFDXEW96ku3QDlhfJTFzNRkgBdYVyX&sz=w1000",
                "https://drive.google.com/thumbnail?id=12IEIMFtaDznO9NcUrOTL4oFCAnsn9Nox&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ic3TjU_UanbrveqxZuXLmMuS2dJjVwdq&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Fathinah Nur Azizah",
                "NIM": "123450072",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belakang PB",
                "Hobi": "Nulis di medium",
                "Sosmed": "@fathinahnazzh",
                "Kesan": "Kalem dan hangat, punya banyak ide untuk dibagikan.",
                "Pesan": "Semoga tulisannya makin banyak yang baca dan tetap semangat, Kak."
            },
            {
                "Nama": "Helmy Surya Pratama",
                "NIM": "124450033",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Tanya Bapas",
                "Hobi": "Ngesen Kiri",
                "Sosmed": "@helmy_inst",
                "Kesan": "Easy going dan supel, gampang membaur dengan siapa saja.",
                "Pesan": "Semoga selalu lancar urusannya dan tetap jaga kesehatan, Bang."
            },
            {
                "Nama": "Fernando Dimetrius Barus",
                "NIM": "124450063",
                "Umur": "21",
                "Asal": "Tangerang Kota",
                "Alamat": "Sebelah kamar Biwa",
                "Hobi": "Badminton",
                "Sosmed": "@barus.fernando",
                "Kesan": "Gesit dan bersemangat, asyik diajak olahraga bareng.",
                "Pesan": "Semoga smash-nya makin tajam dan badan selalu bugar, Bang."
            },
            {
                "Nama": "Suci Aulia",
                "NIM": "124450034",
                "Umur": "19",
                "Asal": "Jakarta",
                "Alamat": "Kota baru",
                "Hobi": "Mancing",
                "Sosmed": "@sciia___",
                "Kesan": "Sabar dan periang, enak diajak bercerita.",
                "Pesan": "Semoga umpannya selalu disambar dan tetap semangat, Kak."
            },
            {
                "Nama": "Wielman Itolo Halawa",
                "NIM": "124450072",
                "Umur": "20",
                "Asal": "Nias Selatan",
                "Alamat": "Asrama TB 3",
                "Hobi": "Dibonceng",
                "Sosmed": "@wielhawn",
                "Kesan": "Kalem dan bersahabat, nyaman diajak jalan bareng.",
                "Pesan": "Tetap semangat dan semoga selalu ada tumpangan yang nyaman, Bang."
            },
            {
                "Nama": "Lia Hana Ichisasmita",
                "NIM": "123450089",
                "Umur": "21",
                "Asal": "Jakarta",
                "Alamat": "Belwis",
                "Hobi": "Nonton",
                "Sosmed": "@lia.h_264",
                "Kesan": "Ramah dan asyik, banyak rekomendasi tontonan bagus.",
                "Pesan": "Semoga selalu ketemu tontonan yang pas di hati, Kak."
            },
            {
                "Nama": "Aqila Zayyan Salsabil",
                "NIM": "124450014",
                "Umur": "19",
                "Asal": "Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Mendokumentasikan Bayes",
                "Sosmed": "@aqilazayyaan",
                "Kesan": "Telaten dan fokus, hasil kerjanya pasti rapi.",
                "Pesan": "Semoga catatan dan dokumentasinya selalu berguna buat banyak orang, Kak."
            },
            {
                "Nama": "Hazel Mahesa Handhaka",
                "NIM": "124450114",
                "Umur": "20",
                "Asal": "Lamtim Timur",
                "Alamat": "Gunung Terang",
                "Hobi": "Giring ayam",
                "Sosmed": "@hazelhandhaka",
                "Kesan": "Lucu dan santai, punya hobi yang bikin penasaran.",
                "Pesan": "Semoga ayam-ayamnya selalu sehat dan tetap semangat, Bang."
            },
            {
                "Nama": "Nadya Ratu Anjani",
                "NIM": "123450083",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Denger lagu",
                "Sosmed": "@nadyaanjaani",
                "Kesan": "Tenang dan hangat, nyambung diajak ngobrol soal musik.",
                "Pesan": "Semoga selalu ada lagu baru yang bikin semangat, Kak."
            },
            {
                "Nama": "Dwi Rahma Fitriani",
                "NIM": "124450084",
                "Umur": "19",
                "Asal": "Tulang Bawang",
                "Alamat": "Jl. Lapas",
                "Hobi": "Baca buku, nonton film, dengerin musik",
                "Sosmed": "@dwi_rahmftrnii",
                "Kesan": "Kalem dan berwawasan, nyaman diajak bertukar cerita.",
                "Pesan": "Tetap semangat dan nikmati hobinya, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


if menu == "Departemen PSDA":
    def departemen_psda():
        gambar_urls = [
                "https://drive.google.com/thumbnail?id=1rtQUYVQTjKv8mVXY-oTZjtSBt3AjBu-M&sz=w1000",
                "https://drive.google.com/thumbnail?id=1NzoFn9lIwkrNQzOM1G3etHVf3XPXg0th&sz=w1000",
                "https://drive.google.com/thumbnail?id=1qiqilQlorrXphwrSiIhWQ3MDb2piO1_l&sz=w1000",
                "https://drive.google.com/thumbnail?id=1vnhd8eZErjHQmcpf5remRLGUltxyGhl5&sz=w1000",
                "https://drive.google.com/thumbnail?id=13LarCMwZ3YIunv7I98ZA3QfMWj-m6eLy&sz=w1000",
                "https://drive.google.com/thumbnail?id=1UgRshhxRxk1fAOmWSmFIyMyrHubPwTSB&sz=w1000",
                "https://drive.google.com/thumbnail?id=17knx2695_QxkjHu2RPBbtID-aoC6q5AU&sz=w1000",
                "https://drive.google.com/thumbnail?id=1zlNQuXlbn38amNrJr9E2_hbbiL896172&sz=w1000",
                "https://drive.google.com/thumbnail?id=1mmRsK2iAa7TdVQjKuGznWkx9517LTPv0&sz=w1000",
                "https://drive.google.com/thumbnail?id=17OiJOleFfKx49e1GS6r5Ec-56oqMPln7&sz=w1000",
                "https://drive.google.com/thumbnail?id=1R6Ckl_3_VMm_B_LJr6RBe8Fto28-snpM&sz=w1000",
                "https://drive.google.com/thumbnail?id=11CxdtKFxua8AhzQhXogUumC3-XYbgqEG&sz=w1000",
                "https://drive.google.com/thumbnail?id=1KKRVWXLLlohoPI8w-6-_uvjBC7TBo3Py&sz=w1000",
                "https://drive.google.com/thumbnail?id=10qKYYH_fHAE5LBx2PebBkGH95WMvXRVE&sz=w1000",
                "https://drive.google.com/thumbnail?id=1ulBgNd3nFb2rmVrW58F7jFset460dUju&sz=w1000",
                "https://drive.google.com/thumbnail?id=1A9_mPnBNGbs2wgz8zL0eQPD_QblR1R3-&sz=w1000",
                "https://drive.google.com/thumbnail?id=1aJ6Qi8r_Vrk-gudloO62PPzqYGczn_qC&sz=w1000",
        ]
        
        data_list = [
            {
                "Nama": "Arienta Khusnul Ananda",
                "NIM": "123450097",
                "Umur": "21",
                "Asal": "Kalianda",
                "Alamat": "Samping kost Haikal",
                "Hobi": "Naksir cowo cakep",
                "Sosmed": "@arientakhsnl_",
                "Kesan": "Supel dan hangat, gampang bikin suasana jadi akrab.",
                "Pesan": "Semoga selalu dilancarkan urusannya dan tetap semangat, Kak."
            },
            {
                "Nama": "Vany Salsabila",
                "NIM": "124450022",
                "Umur": "21",
                "Asal": "Sibolga",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Kalem dan telaten, kelihatan sabar dalam mengurus sesuatu.",
                "Pesan": "Semoga peternakannya makin sukses dan selalu sehat, Kak."
            },
            {
                "Nama": "Nobel Nizam Fathirizki",
                "NIM": "123450117",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Urip",
                "Hobi": "-",
                "Sosmed": "@nobelnizam",
                "Kesan": "Tenang dan sopan, enak diajak bertukar pikiran.",
                "Pesan": "Semoga selalu lancar dalam studi dan tetap semangat, Bang."
            },
            {
                "Nama": "Afriza Azmi",
                "NIM": "124450110",
                "Umur": "20",
                "Asal": "Lamteng",
                "Alamat": "Sebelah kost Haikal",
                "Hobi": "Nyebar beras",
                "Sosmed": "@friezazmi",
                "Kesan": "Santai dan lucu, selalu ada hal seru buat dibahas.",
                "Pesan": "Tetap jadi pribadi yang menyenangkan dan jaga kesehatan, Kak."
            },
            {
                "Nama": "Ayake Alfatih Ramadan",
                "NIM": "124450108",
                "Umur": "20",
                "Asal": "Solo",
                "Alamat": "Blok D No 57, Jln Manggis, Pemda Way Huwi, Lamsel, Jatiagung",
                "Hobi": "Goreng ayam",
                "Sosmed": "@ykeall",
                "Kesan": "Ramah dan gampang berbaur, kelihatannya jago masak.",
                "Pesan": "Semoga masakannya makin enak dan tetap semangat, Bang."
            },
            {
                "Nama": "Caesar Ozora Alrando",
                "NIM": "124450017",
                "Umur": "21",
                "Asal": "Rahim ibu",
                "Alamat": "Gedung F",
                "Hobi": "Pengembala anak ayam",
                "Sosmed": "@caesar.oriza",
                "Kesan": "Easy going dan humoris, nyaman diajak ngobrol.",
                "Pesan": "Semoga anak-anak ayamnya sehat dan tetap semangat, Bang."
            },
            {
                "Nama": "Euodia Meiliana Friedita",
                "NIM": "124450029",
                "Umur": "20",
                "Asal": "Asal asalan",
                "Alamat": "Diatas tanjakan",
                "Hobi": "Ngekader",
                "Sosmed": "@yudiameilianaa_",
                "Kesan": "Enerjik dan komunikatif, pintar menghidupkan suasana.",
                "Pesan": "Semoga kegiatannya selalu berjalan lancar dan menyenangkan, Kak."
            },
            {
                "Nama": "Haikal Seventino Tamba",
                "NIM": "124450012",
                "Umur": "25",
                "Asal": "Jambi",
                "Alamat": "Sebelah kontrakan Jemar",
                "Hobi": "Ngurusin pakan anak ayam",
                "Sosmed": "@_haikaaalll",
                "Kesan": "Tenang dan perhatian, bisa jadi tempat bertanya.",
                "Pesan": "Semoga selalu sehat dan sukses terus, Bang."
            },
            {
                "Nama": "Putri Manna Anantama Simbolon",
                "NIM": "124450065",
                "Umur": "18",
                "Asal": "Depok",
                "Alamat": "Nomandenl",
                "Hobi": "Mancing emosi",
                "Sosmed": "@putrimannaa",
                "Kesan": "Asyik dan jenaka, gampang bikin orang tertawa.",
                "Pesan": "Tetap jadi pribadi yang ceria dan semangat terus."
            },
            {
                "Nama": "Queenta Thifaal Nabila",
                "NIM": "124450059",
                "Umur": "21",
                "Asal": "Lamteng",
                "Alamat": "Depan pemancingan",
                "Hobi": "Nyuapin anak ayam",
                "Sosmed": "@queentanaabila",
                "Kesan": "Lembut dan penyayang, orangnya menyenangkan.",
                "Pesan": "Semoga semua rencananya lancar dan tetap sehat."
            },
            {
                "Nama": "Desman Velius Halawa",
                "NIM": "123450114",
                "Umur": "18",
                "Asal": "Palembang Sekayu",
                "Alamat": "Asrama TB 3",
                "Hobi": "Ngejek orang",
                "Sosmed": "@dsmanhl",
                "Kesan": "Jenaka dan blak-blakan, bikin suasana jadi hidup.",
                "Pesan": "Tetap semangat dan jangan lupa jaga ucapan."
            },
            {
                "Nama": "Azzelya Thianandry",
                "NIM": "124450041",
                "Umur": "19",
                "Asal": "Teluk",
                "Alamat": "Bandar Lampung",
                "Hobi": "Pilates",
                "Sosmed": "@azzelytn",
                "Kesan": "Aktif dan teratur, kelihatan peduli sama kesehatan.",
                "Pesan": "Semoga makin kuat dan bugar, tetap semangat ya, Kak."
            },
            {
                "Nama": "Charrlindah",
                "NIM": "124450037",
                "Umur": "21",
                "Asal": "Jakarta Pusat",
                "Alamat": "Cenderawasih 1",
                "Hobi": "Ngurus peternakan",
                "Sosmed": "@charrlnn",
                "Kesan": "Gigih dan rajin, enak diajak kerja bareng.",
                "Pesan": "Semoga usahanya lancar dan jangan lupa istirahat, Kak."
            },
            {
                "Nama": "Jeremi Marolop Partogi Situmorang",
                "NIM": "124450111",
                "Umur": "16",
                "Asal": "Berlin",
                "Alamat": "Samping kos Rafli",
                "Hobi": "Mengembala anak ayam",
                "Sosmed": "@jemarrro",
                "Kesan": "Kalem dan bersahabat, gampang akrab dengan siapa saja.",
                "Pesan": "Semoga selalu semangat dan sukses kuliahnya, Bang."
            },
            {
                "Nama": "Nabila Nur Azizah",
                "NIM": "124450048",
                "Umur": "18",
                "Asal": "Lampung",
                "Alamat": "Barokah",
                "Hobi": "Main sama Azel",
                "Sosmed": "@n.bila_a",
                "Kesan": "Hangat dan setia kawan, seru diajak ngobrol.",
                "Pesan": "Semoga pertemanannya selalu akrab dan tetap semangat, Kak."
            },
            {
                "Nama": "Rafli Al Mansyah Tambunan",
                "NIM": "124450007",
                "Umur": "20",
                "Asal": "Sibolga",
                "Alamat": "Samping kos Haikal",
                "Hobi": "Nonton",
                "Sosmed": "@dearfkvmfl",
                "Kesan": "Santai dan menyenangkan, nyambung diajak ngobrol soal tontonan.",
                "Pesan": "Semoga selalu ada tontonan seru dan tetap sehat, Bang."
            },
            {
                "Nama": "Salavi Naharani",
                "NIM": "124450090",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Jatimulyo",
                "Hobi": "Minum air putih",
                "Sosmed": "@avi.nhr",
                "Kesan": "Kalem dan sederhana, nyaman diajak bergaul.",
                "Pesan": "Tetap rajin jaga kesehatan dan semangat terus, Kak."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_psda()
