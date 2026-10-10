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
            "people-fill"
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

# KESEKJENAN
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ydfq9Evnhui8Yqv56GlFmsZZyZUD4BSo",
            "https://drive.google.com/uc?export=view&id=1gKuqkzr7T4J7nYxeZQVvM3PgAUXsyvje",
            "https://drive.google.com/uc?export=view&id=1I-F931OZ9dC1YL5ue5nLOoMM8ZFmxqro",
            "https://drive.google.com/uc?export=view&id=1pveYH5_vp9Ti-YcLvqKgw3HguEDfqTzS",
            "https://drive.google.com/uc?export=view&id=1A-tjV1Cw5Nt8bhlRr0B1_1EMF725rben",
            "https://drive.google.com/uc?export=view&id=1-7LCL719bCdP3ba66VdshxS45PPfuTVI",
        ]
        data_list = [
            {
                "Nama": "Ginda Fajar Riadi Marpaung",
                "NIM" : "123450103",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Punya cara asyik sendiri buat ngasih arahan ke juniornya.",
                "Pesan" : "Sukses terus buat urusan kuliah dan rencana ke depannya."
            },
            {
                "Nama": "Muhammad Aqil Ramadhan",
                "NIM" : "123450066",
                "Asal" : "Riau",
                "Alamat" : "Kotabaru",
                "Hobi": "Dzikir",
                "Umur" : "22",
                "Sosmed" : "@Muhammadaqil1111",
                "Kesan" : "Kakak-kakak semuanya sangat suportif, ramah, dan bikin suasana kegiatan jadi jauh lebih seru.",
                "Pesan" : "Semoga silaturahmi kita tetap terjaga. Sukses selalu untuk kedepannya!"
            },
            {
                "Nama": "Efi Defiyati",
                "NIM" : "123450005",
                "Asal" : "Lampung Timur",
                "Alamat" : "Airan",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@eeffiidefi",
                "Kesan" : "Ramah, sabar banget, dan selalu telaten ngajarin kami.",
                "Pesan" : "Sukses terus kuliahnya, cepat lulus, dan jangan sombong-sombong!"
            },
            {
                "Nama": "Qois Olifio",
                "NIM" : "123450067",
                "Asal" : "Batam",
                "Alamat" : "Kotabaru",
                "Hobi": "Mainin surat",
                "Umur" : "22",
                "Sosmed" : "@qoisolifio_",
                "Kesan" : "Sabar banget menghadapi kami yang sering kebingungan dan banyak tanya.",
                "Pesan" : "Semoga sukses terus urusan kuliah dan kedepannya, ya!"
            },
            {
                "Nama": "Hafsa Fazilah Arradhi",
                "NIM" : "123450079",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Bertemu luluk",
                "Umur" : "21",
                "Sosmed" : "@hafsafazilahh",
                "Kesan" : "Orangnya sangat ramah dan bikin kami langsung akrab sejak pertama ketemu.",
                "Pesan" : "Terima kasih banyak atas waktu dan kesabarannya, Kak."
            },
            {
                "Nama": "Luthfia Laila Ramadhani",
                "NIM" : "123450004",
                "Asal" : "Bengkulu",
                "Alamat" : "Airan",
                "Hobi": "Keliling Balam",
                "Umur" : "20",
                "Sosmed" : "@luthhifiarmdhni",
                "Kesan" : "Kakaknya baik banget",
                "Pesan" : "semangat kuliah kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

    #INTERNAL
if menu == "Departemen Internal":
    def departemen_internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1N5OYZ9hATFqnablK-hFmacr2rdaRG4_V",
            "https://drive.google.com/uc?export=view&id=1J1DYIP_T05bR6RuBksL70zul0jsDQJxP",
            "https://drive.google.com/uc?export=view&id=1qq3Q9m9_atK01EAhnHUgTqYLbyygnHUC",
            "https://drive.google.com/uc?export=view&id=1uqiOIGWHF3deFZcCmTL2alTo6VCZSvNf",
            "https://drive.google.com/uc?export=view&id=1nyvxESh1leil7ru3XFGjl4uaUHhEBe1h",
            "https://drive.google.com/uc?export=view&id=1gyID6Cc0e5ItfYo6VZK0GH8RZiqkHPSw",
            "https://drive.google.com/uc?export=view&id=1qJ_Dre1ECzgmLhvHe3CRhTOa1u9dSpVU",
            "https://drive.google.com/uc?export=view&id=1Qg-Y__pzCPcghbJbpRTbp5ofX_rsV8Js",
            "https://drive.google.com/uc?export=view&id=1h70Bo9id77LKfqLk3_qE20w37q1bHHgF",
            "https://drive.google.com/uc?export=view&id=1iimFYJzZU9R52ct6SPZFKB8wtGGhPQUB",
            "https://drive.google.com/uc?export=view&id=1nUQojkJaVvSSeiN27rf499m-7-CN9wlu",
            "https://drive.google.com/uc?export=view&id=1Vr4wIF1m2jzgDd6YiicKnFqYMNt3k0hf",
            "https://drive.google.com/uc?export=view&id=1d8zaMXYlJ4MolCgfLw4f9bn-CnWL3WYn",
            "https://drive.google.com/uc?export=view&id=1qeuS9zf09FmSTfVWbiFi1jeSnwxWg2FT",
            "https://drive.google.com/uc?export=view&id=1B9-H5Lg9bmICHwXZm18doQJwFKrqPZjx",
            "https://drive.google.com/uc?export=view&id=1iwmfJcLJ9MgTOL8u7l2S84GyWFeS9rwt",
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
                "Kesan": "Kelihatan cuek, tapi sebenarnya sangat peduli",
                "Pesan": "Tetap jadi kating yang asyik dan asik diajak ngobrol!"
            },
            {
                "Nama": "Kharisma Mustika Sari",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "ngomong nya lembut dan ramah",
                "Pesan": "Sukses selalu kak"
            },
            {
                "Nama": "Hanna Gresia Sinaga",
                "NIM": "",
                "Umur": "",
                "Asal": "",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Kocak dan jago banget bikin suasana jadi cair dan nggak tegang.",
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
                "Kesan": "Orangnya santai, seru, dan gampang banget diajak ngobrol.",
                "Pesan": "Sukses terus buat urusan kuliah dan rencana ke depannya."
            },
            {
                "Nama": "Aisyah Khairun Nisa",
                "NIM": "124450096",
                "Umur": "18",
                "Asal": "Indragiri",
                "Alamat": "Samping Makam Perwira 2",
                "Hobi": "Nyicipin Makanan",
                "Sosmed": "@aisyahkhair._",
                "Kesan": "Asyik diajak ngobrol, nggak jaim, dan seru selama kegiatan bareng.",
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
                "Kesan": "Seru, asyik, dan gampang baur",
                "Pesan": "semangat kak"
            },
            {
                "Nama": "Jaya Saputra Tamba",
                "NIM": "124450094",
                "Umur": "18",
                "Asal": "Medan",
                "Alamat": "Pemda",
                "Hobi": "Mencari Nafkah",
                "Sosmed": "@jay.saputra.mb",
                "Kesan": "baik dan tenang banget abangnya",
                "Pesan": "sukses selalu bang."
            },
            {
                "Nama": "Najla Nursyifa",
                "NIM": "124450051",
                "Umur": "20",
                "Asal": "Sumatra Barat",
                "Alamat": "Belwis",
                "Hobi": "Nonton ASMR",
                "Sosmed": "@njlanursyifa",
                "Kesan": "Baik banget, ramah, dan seru kalau diajak diskusi atau ngobrol santai.",
                "Pesan": "Semoga sehat selalu, Kak, dan makin sukses ke depannya"
            },
            {
                "Nama": "Rozak Ramdani",
                "NIM": "124450100",
                "Umur": "19",
                "Asal": "Kalianda, Lampung Selatan",
                "Alamat": "Korpri Raya",
                "Hobi": "Berantemin Kucing",
                "Sosmed": "@rozakrabbani__",
                "Kesan": "Santai banget orangnya, asyik diajak nongkrong/ngobrol, nggak kaku..",
                "Pesan": "semangat kuliah bang."
            },
            {
                "Nama": "Teresa Christiani Purba",
                "NIM": "124450046",
                "Umur": "19",
                "Asal": "Riau",
                "Alamat": "Belwis",
                "Hobi": "Masak",
                "Sosmed": "@kristiani8872",
                "Kesan": "Asyik, nggak pelit ilmu, dan seru kalau lagi kerja kelompok atau tugas bareng.",
                "Pesan": "Makasih ilmunya, Kak. Semoga urusan perkuliahannya lancar terus."
            },
            {
                "Nama": "Muhammad Hanif Dzaky Arifin",
                "NIM": "123450064",
                "Umur": "21",
                "Asal": "Padang",
                "Alamat": "Way Kandis",
                "Hobi": "Nonton F1 & MotoGP",
                "Sosmed": "@hnfdzky_",
                "Kesan": "Asyik diajak kerja sama, seru, dan nggak ribet kalau diajak diskusi.",
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
                "Kesan": "Orangnya asyik, seru diajak ngobrol apa aja, dan nggak ngebosenin.",
                "Pesan": "Semangat kuliah, Kak."
            },
            {
                "Nama": "Cika Adelia Br Marbun",
                "NIM": "124450107",
                "Umur": "20",
                "Asal": "Bagan Batu, Riau",
                "Alamat": "Belwis",
                "Hobi": "Dengerin Musik",
                "Sosmed": "@cikamrbn",
                "Kesan": "Seru banget diajak ngobrol, asyik, dan gak bikin canggung sama sekali.",
                "Pesan": "Jaga kesehatan kak"
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
                "Pesan": "semangat kuliah bang."
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
                "Pesan": "Jaga Kesehatan Bang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_internal()


# MINBAK
if menu == "Departemen Minbak":
    def departemen_minbak():
        gambar_urls = [
                    "https://drive.google.com/uc?export=view&id=1LmTiRyUcWG_SqZ0MEPeWhkvOVrT3s4mh",
                    "https://drive.google.com/uc?export=view&id=1M0dQnyVPYdq1zw2RBR0qUh1mxVx-BcIj",
                    "https://drive.google.com/uc?export=view&id=1mNK7jsiP9fzP2MVhgoSFBuliJ-34yhgn",
                    "https://drive.google.com/uc?export=view&id=1CXdr-HnrFBxtU7lw_Gu_t6shs16bg-eT",
                    "https://drive.google.com/uc?export=view&id=1j6bKVLt-PqU-1PKop4xYh2668akcXXVi",
                    "https://drive.google.com/uc?export=view&id=1aaeqBP63GTE_0eWV71a-iFxPfvOCdmBK",
                    "https://drive.google.com/uc?export=view&id=1Z9WzO1pTPe5JvsoZmjOiC-LsOrPg0cQj",
                    "https://drive.google.com/uc?export=view&id=1DTTbc01e_WX9yanosw6rf6m5GxL4fLs7",
                    "https://drive.google.com/uc?export=view&id=1i0xPqVZ0c9WvlIdPiYDPbkWMNacaqHWE",
                    "https://drive.google.com/uc?export=view&id=19_wRgnJAfVLJkeNz_vWXEt-LR2etbfhI",
                    "https://drive.google.com/uc?export=view&id=11u6n9HdA-bDEL-iJYP7CjS-QOMi7Qd6S",
                    "https://drive.google.com/uc?export=view&id=1JuziGXCQ24p_ld9vRu9IaPF8pWXY8mHT",
                    "https://drive.google.com/uc?export=view&id=1pNUQIf2UcA2-lXrmvgBmCzQc6WGRWD2M",
                    "https://drive.google.com/uc?export=view&id=1PLW0frBFtUk69JjkIqeUe4rUXD2iYhGF",
                    "https://drive.google.com/uc?export=view&id=1klKh2QC87HzU6CGPfniznstefmlEFgkb",
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
                "Kesan" : "Asyik, santai, nggak kaku, dan seru dia diajak ngobrol apa aja.",
                "Pesan" : "Tetap jadi abang yang asyik diajak ngobrol, Kak."
            },
            {
                "Nama": "Gusti Putu Ferazka Dhiyamika",
                "NIM" : "123450046",
                "Asal" : "Lampung Utara",
                "Alamat" : "Way Halim",
                "Hobi": "Baca",
                "Umur" : "21",
                "Sosmed" : "@ferazkaa",
                "Kesan" : "Asyik, seru diajak ngobrol, dan pembawaannya santai banget.",
                "Pesan" : "sehat selalu"
            },
            {
                "Nama": "Ari Aristo Muthahari Parisi",
                "NIM" : "123450088",
                "Asal" : "Lampung Timur",
                "Alamat" : "Gang Sakum, Belwis",
                "Hobi": "Nonton F1",
                "Umur" : "21",
                "Sosmed" : "@ali_parisi3",
                "Kesan" : "syik dan nggak kaku.",
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
                "Pesan" : "Sehat terus dan cepat lulus Kak!"
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
                "Pesan" : "Semangat kuliah bang"
            },
            {
                "Nama": "Salsabila Nazwa Putri",
                "NIM" : "124450002",
                "Asal" : "Metro",
                "Alamat" : "Korpri",
                "Hobi": "Nongkrong di Kopken",
                "Umur" : "20",
                "Sosmed" : "@slbnzw_",
                "Kesan" : "Asyik diajak seru-seruan, solid, dan nggak ribet orangnya.",
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
                "Kesan" : "Abangnya lucu dan humble",
                "Pesan" : "Tetap semangat dalam hari hari bang."
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
                "Kesan" : "Asyik diajak seru-seruan, nggak jaim, dan asik diajak ngobrol apa aja.",
                "Pesan" : "Semoga urusan kuliahnya lancar terus, Kak. Cepat lulus ya!"
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
                "Kesan" : "Ceria dan lucu",
                "Pesan" : "semangat kuliah kak"
            },
            {
                "Nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "NIM" : "124450089",
                "Asal" : "Padang",
                "Alamat" : "Kota Baru",
                "Hobi": "Bangun pagi",
                "Umur" : "20",
                "Sosmed" : "@muhammdrafka_",
                "Kesan" : "Orangnya asyik, nggak kaku, dan seru diajak bareng.",
                "Pesan" : "Sukses terus. Jangan sombong-sombong, ya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_minbak()


if menu == "Departemen MIKFES":
    def departemen_mikfes():
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
                "Nama": "Fabio Banyu Cyto",
                "NIM" : "12340104",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Kedaton",
                "Hobi": "Tidur",
                "Umur" : "21",
                "Sosmed" : "@biyokcb",
                "Kesan" : "Asyik diajak becanda, solid, dan asik banget jadi tempat nanya-nanya.",
                "Pesan" : "Mantap, Kak! Semoga semua urusannya dipermudah dan cepat lulus."
            },
            {
                "Nama": "Tanty Widiyastuti",
                "NIM" : "123450094",
                "Asal" : "Lampung",
                "Alamat" : "Airan Raya",
                "Hobi": "Membaca",
                "Umur" : "21",
                "Sosmed" : "@tvnty_",
                "Kesan" : "Ramah dan ceria banget",
                "Pesan" : "Bahagia selalu"
            },
            {
                "Nama": "Fadil Prasetyo Alfaritzi",
                "NIM" : "Belum Tahu",
                "Asal" : "Bandar Lampungku",
                "Alamat" : "Bandar Lampung",
                "Hobi": "Gitar",
                "Umur" : "21",
                "Sosmed" : "@fadilalfarizzii",
                "Kesan" : "Asyik, seru kalau diajak diskusi, dan nggak ribet orangnya.",
                "Pesan" : "Lancar-lancar terus ya, Kak. Ditunggu kabar baik kelulusannya!"
            },
            {
                "Nama": "Manuel Frederika",
                "NIM" : "124450039",
                "Asal" : "Batam",
                "Alamat" : "Way Kandis",
                "Hobi": "Tenis meja",
                "Umur" : "20",
                "Sosmed" : "@manuelfdk_",
                "Kesan" : "Asyik, nggak kaku, dan seru.",
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
                "Kesan" : "Orangnya asyik, seru diajak ngobrol, dan pembawaannya santai banget..",
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
                "Kesan" : "Asyik, nggak jaim, dan gampang akrab sama siapa aja.",
                "Pesan" : "Semangat kuliah kak"
            },
            {
                "Nama": "Vannisa Ramadhani",
                "NIM" : "124450078",
                "Asal" : "Kepulauan Riau",
                "Alamat" : "Teluk Betung",
                "Hobi": "Nonton KHW",
                "Umur" : "19",
                "Sosmed" : "@vunnycaa",
                "Kesan" : "Baik, asyik, dan nggak pelit buat bagi-bagi cerita atau pengalaman.",
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
                "Kesan" : "Asyik dan seru.",
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
                "Kesan" : "Asyik, nggak jaim, dan asik banget diajak nongkrong atau ngobrol.",
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
                "Kesan" : "Seru banget banggg",
                "Pesan" : "Semangat kuliah bang"
            },
            {
                "Nama": "Lovianora Saragih",
                "NIM" : "124450105",
                "Asal" : "Sumatera Utara",
                "Alamat" : "Way Huwi",
                "Hobi": "Dengerin Musik",
                "Umur" : "19",
                "Sosmed" : "_loviaa",
                "Kesan" : "Awalnya kalem waktu dah kenalll, baik banget",
                "Pesan" : "Semoga selalu dimudahkan dalam urusan, Kak."
            },
            {
                "Nama": "M. Alsi Syahrulloh",
                "NIM" : "124450092",
                "Asal" : "Kalianda",
                "Alamat" : "Kotabaru",
                "Hobi": "Main Game, Tidur",
                "Umur" : "20",
                "Sosmed" : "@aluccy_",
                "Kesan" : "Asyik, seru, dan nggak kaku kalau diajak ngobrol..",
                "Pesan" : "Semangat kuliah bang"
            },
            {
                "Nama": "Sherena Florencia",
                "NIM" : "124450027",
                "Asal" : "Bengkulu Selatan",
                "Alamat" : "Belwis",
                "Hobi": "Make up",
                "Umur" : "19",
                "Sosmed" : "sher_renna",
                "Kesan" : "Kalem dan baik.",
                "Pesan" : "Jaga kesehatan kak"
            },
            {
                "Nama": "Razin Hafid Hamdi",
                "NIM" : "123450096",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Futsal",
                "Umur" : "21",
                "Sosmed" : "@razyn.hfd",
                "Kesan" : "Asyik, seru, dan asik diajarin atau diajak kerja bareng..",
                "Pesan" : "Lancar-lancar terus kuliahnya, Kak. Semangat!"
            },
            {
                "Nama": "Faiza Try Anjani",
                "NIM" : "124450075",
                "Asal" : "Padang",
                "Alamat" : "Belwis",
                "Hobi": "Membaca Novel",
                "Umur" : "19",
                "Sosmed" : "FAIZAANJANII",
                "Kesan" : "Asyik, seru, dan asik diajak diskusi..",
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
                "Kesan" : "Asyik, nggak ribet, dan seru.",
                "Pesan" : "Sukses terus buat kuliahnya, Kak!"
            },
            {
                "Nama": "Kaleb Filbert Istel",
                "NIM" : "124450053",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Campang Raya",
                "Hobi": "Ngegym, baca novel",
                "Umur" : "20",
                "Sosmed" : "@kelelep_comberan",
                "Kesan" : "Asyik, seru, dan solid banget sama juniornya.",
                "Pesan" : "Sehat selalu bang"
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
                "Kesan" : "Asyik, nggak jaim, dan asik banget diajak ngobrol.",
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
                "Kesan" : "Ramah, baik dan pintar.",
                "Pesan" : "Nular bang pinternya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_mikfes()


if menu == "Departemen Medkraf":
    def departemen_medkraf():
        gambar_urls = [
                "https://drive.google.com/uc?export=view&id=1eAlp4t8XqdI3MuDsOmXzRDucpXzqvDiP",
                "https://drive.google.com/uc?export=view&id=1sujJKUbssKQ001hcvsYqxA1nfkosiUIf",
                "https://drive.google.com/uc?export=view&id=1Ll9bGBLrHZZLILhqFGrny6g3SvpPb0zj",
                "https://drive.google.com/uc?export=view&id=1rsxHmnRVnUQHouRlqmhIQbwz1Vg9yqfI",
                "https://drive.google.com/uc?export=view&id=1BaUf1oF7XtN4iiR2xxUQPZ7-0k0M-hu8",
                "https://drive.google.com/uc?export=view&id=1g7p4SiU7KivD04BdVRudiaZ0AUJ-ESBC",
                "https://drive.google.com/uc?export=view&id=1LEh6IsF0jf0qXn7E-HVzyw7u34qpklVi",
                "https://drive.google.com/uc?export=view&id=1RmD8IE7h91oIFJXdV2oLSIC6SOb-YdIT",
                "https://drive.google.com/uc?export=view&id=1Qb6h8f9M_C6p1asBcCLuoCjARV7CMHGG",
                "https://drive.google.com/uc?export=view&id=19S3dLNqCr_I05ond63AcqU3_p5U7VGsd",
                "https://drive.google.com/uc?export=view&id=1FN7Zjt6sEtrpsuYznal0BDvFH4Ef8dbu",
                "https://drive.google.com/uc?export=view&id=1mhC5pXkfSbbQnRN8BoHNYS6yNl6FLc7p",
                "https://drive.google.com/uc?export=view&id=1bqhlP9z2i7wEGlHLKfaFXp5dXVFq8oJ2",
                "https://drive.google.com/uc?export=view&id=1Bl68yjC0pHzj5siwfCL0Tm4KBEbgYRoL",
                "https://drive.google.com/uc?export=view&id=1I2xYoSETY9_2ULNRoujzDAGEc-5FafoO",
                "https://drive.google.com/uc?export=view&id=1Z4ZJkmnzwYxZWZOS0Nklv3wHZ4eBvb50",
                "https://drive.google.com/uc?export=view&id=1fS4PLcacEBNpVWQmL1TR3j97-Tae2guU",
                "https://drive.google.com/uc?export=view&id=1XNHJnlrpx1Hm8hHtNjSiOgWlxrgFBuv9"
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
                "Kesan" : "Asyik, seru diajak ngobrol, dan pembawaannya santai banget.",
                "Pesan" : "Semangat kuliah ka"
            },
            {
                "Nama": "Donna Maya Puspita",
                "NIM" : "123450028",
                "Asal" : "Bekasi dan Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Mendengarkan musik",
                "Umur" : "21",
                "Sosmed" : "@donnamaya.p",
                "Kesan" : "Asyik diajak ngobrol, seru, dan nggak ngebosenin.",
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
                "Kesan" : "Awalnya dikira galak, eh ternyata asyik dan doyan ketawa juga.",
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
                "Kesan" : "Santai banget orangnya, kayak nggak punya beban hidup.",
                "Pesan" : "Jaga kesehatan bang"
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
                "Kesan" : "Cantik dan kalem, tapi aslinya seru banget diajak becanda.",
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
                "Kesan" : "Kakaknya asik dan seru pol",
                "Pesan" : "Sukses terus kuliahnya, Kak. Jangan lupa sapa kita kalau ketemu ya!"
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
                "Kesan" : "Santai banget orangnya, kayak nggak punya beban hidup.",
                "Pesan" : "Sukses terus kuliahnya, Kak."
            },
            {
                "Nama": "Nazlah Auliya",
                "NIM" : "124450054",
                "Asal" : "Bandar Lampung",
                "Alamat" : "Belum Tahu",
                "Hobi": "Ballet",
                "Umur" : "20",
                "Sosmed" : "@nzlhauly_",
                "Kesan" : "Asyik banget, seru diajak becanda, dan ramah.",
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
                "Kesan" : "Asyik banget, seru diajak becanda, dan ramah.",
                "Pesan" : "Jangan lupa sapa-sapa kita ya, Kak. Sukses terus!"
            },
            {
                "Nama": "Daffa Kharisma Adzana",
                "NIM" : "Belum Tahu",
                "Asal" : "Belum Tahu",
                "Alamat" : "Belum Tahu",
                "Hobi": "Belum Tahu",
                "Umur" : "Belum Tahu",
                "Sosmed" : "Belum Tahu",
                "Kesan" : "Asyik, seru, dan solid banget sama juniornya.",
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
                "Kesan" : "Muka sangar, tapi hati Hello Kitty.",
                "Pesan" : "Semangat kuliah kak"
            },
            {
                "Nama": "Shafa Delaila Azzahra",
                "NIM" : "124450124",
                "Asal" : "Lampung Tengah",
                "Alamat" : "Belum Tahu",
                "Hobi": "Makan tempe mentah",
                "Umur" : "20",
                "Sosmed" : "@_shaazzh",
                "Kesan" : "Semangat terus urusan perkuliahannya, Kak!",
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
                "Kesan" : "Sukses ya, Kak!",
                "Pesan" : "Jaga kesehatan bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    departemen_medkraf()