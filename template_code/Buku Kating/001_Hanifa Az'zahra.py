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
            "nav-link-selected": {"background-color": "#9C6AC0"},
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
            "https://drive.google.com/uc?export=view&id=1NXV0ECB8OUztJJUeZKTsc6lM2VToUt34",
            "https://drive.google.com/uc?export=view&id=1G-3XKw2y4vw2NLlMY4--IJ3GXpWx6PWN",
            "https://drive.google.com/uc?export=view&id=1EMLdsxhuRocxvwX9MrnxMRvUsuRh7rZO",
            "https://drive.google.com/uc?export=view&id=1dc3IAue-NgNttcR4asAODVP60tWY91nQ",
            "https://drive.google.com/uc?export=view&id=17bkuJzulY2c8KbWtTIGg0rvF0R7fY5IS",
            "https://drive.google.com/uc?export=view&id=1KOMsigI24XhhcfD4iCyiE8XfJGnk4YRA",
        ]
        data_list = [
            {
                "nama": "Ginda Fajar Riadi Marpaung",
                "nim": "123450103",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kesektariatan HMSD",
                "hobbi": "Push IMO",
                "sosmed": "@jars_mrp",
                "kesan": "Bang Fajar orangnya sangat humble, baik, dan juga sangat menginspirasi bagi saya.",  
                "pesan":"Pijarkan api semenyala mungkin bang, jangan sampai padam"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Bang Aqil keren banget apalagi pas ngejelasin materi",  
                "pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak efi suka banget penjelasan waktu materi, keren banget ngeliatnya.",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal": "Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois orangnya unik, lucu, dan hobinya seru sepertinya.",  
                "pesan": "Semangat kuliahnya bang, semoga ga ada hambatan dalam menempul hal yang di inginkan."
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kak Hafsa orangnya lucu banget, dan kalo ketawa bikin nular.",  
                "pesan": "Semoga kedepannya hani bisa tumbuh seperti kakak yang keren, dan tetap senyum ya kak jangan sampai pudar"# 1
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal": "Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Dari kak lutfia aku mendapatkan insight baru disunia perkulihan.",  
                "pesan": "Semoga lancar kuliahnya, karna aku pingin denger banyak cerita lagi dari kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EINzOceEaYbD2JSZvOA3p0bxtiSqBmIV",
            "https://drive.google.com/uc?export=view&id=1WLYyjiRX2RZNd-WsBsHe6D0XUCUY5D2E",
            "https://drive.google.com/uc?export=view&id=1nwovRCQ4f20QTUU5-l1Y_i2yiDjd9iJc",
            "https://drive.google.com/uc?export=view&id=1hNl1JgNO3xZEXBjiduvNhOhZL_eUmo6H",
            "https://drive.google.com/uc?export=view&id=1jL5rKV6YhnBxcdBAGA9kk073URW6bZXn",
            "https://drive.google.com/uc?export=view&id=1LKrFNBakZZZOKGnW5c5bwTpta62djJZa",
            "https://drive.google.com/uc?export=view&id=1i-U2dV72juuiXFuIrYMD74n-yoLsRVH2",
            "https://drive.google.com/uc?export=view&id=1Jl7laA_S_NkzbMZMrgBTynN9buI5Lc9B",
            "https://drive.google.com/uc?export=view&id=1EoYev3u4IKKikAt8UhE5vd3MgCMwq-6D",
            "https://drive.google.com/uc?export=view&id=1KQIyf49dnfg7hQxHN11-bmReKHEpvZMV",
            "https://drive.google.com/uc?export=view&id=1V1mVgVBvUTBi9QPs1Kxkky5isnDvUQcv",
            "https://drive.google.com/uc?export=view&id=1NDtPlQSFQ78upiz6hjY5u4h6ywxIyswD",
            "https://drive.google.com/uc?export=view&id=1fKPt9Ght0yLRG_zAjTA8UzfdXxeUPNGi",

        ]
        data_list = [
            {
                "nama": "Ridho Benedictus Togi Manik",
                "nim": "123450060",
                "umur": "20",
                "asal": "Kuala lumpur",
                "alamat": "GH",
                "hobbi": "Bernyanyi",
                "sosmed": "@iamridhomanik",
                "kesan": "Bang Ridho orangnya lucu banget, banyak hal yang didapakan dari ceritanya.",  
                "pesan":"Semoga kedepannya fadyl bisa tumbuh seperti bang fajar, terimakasih bang"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak mentor TPB aku yang sangat keren dan prestasinya sangat WOWWW.",  
                "pesan": "semangat terus kuliahnya kakak !!!, tetap ceria ya kak jangan pernah pudarsenyumnya"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Bang Dharu yang punya segudang prestasi, contoh yang baik dan meningkatkan semangatku untuk mengikuti jejaknya.",  
                "pesan": "Kobarkan semangat terus bang untuk meraih prestasi yang lebih banyak lagi!!!"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Abang Asprak ALPRO aku yang humoris.",  
                "pesan": "Semangat buat jadi asprak MK lainnya bang!!!!"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal": "Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Kakak yang baik hati, cantik, setiap ngeliat mukanya sejuk banget bawaannya.",  
                "pesan": "Mari tebarkan senyum itu kak biar orang lain ketika melihatnya ikut happy"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal": "Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bang Givaro orangnya suka ngelu hal yang random banget.",  
                "pesan": "Semangat kuliahnya bang, jangan sering ngelucu perutnya sakit pas ketawa"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal": "Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakak tutor metnum yang kalo ngajarin jelas banget akusuka metodenya.",  
                "pesan": "Harus jadi tutor privat aku sih kak"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "BTW nama panggilan kita sama kakkk.",  
                "pesan":"Semoga sehat terus ya kak, semangat buat meraih mimpi-mimpinyaaaa"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Aku ga bisa bedain antara bang Jeremia sama bang Kaleb semirip itu menurut aku",  
                "pesan":"Jangan sering-sering nempel sama bang jon takut ngeliatnya"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kakaknya seru dan lucuuuuu bangetttt omgg",  
                "pesan":"Semangat menjelajahi dunia bang"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Aku pikir bang jona itu medis ternyata Baleg keren banget sih, syok pas diteriakin dilapangan",  
                "pesan":"Jangan diteriakin lagi ya bang"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Keren banget waktu dilapangan ngawasinnya",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal": "Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "Kenal pas di kelas KDP ngeliatnya aku terpesona banget ga tau kenapa",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VO4n_QWkD4Od-TSCG9_dz9SXpam3x7JP",
            "https://drive.google.com/uc?export=view&id=1HAXjISF5IYlAU7RlP5bSF5xtfbeWMXvc",
            "https://drive.google.com/uc?export=view&id=1RlxhzaT1Tzbx3WePKuBHw6SNpwexn4EA",
            "https://drive.google.com/uc?export=view&id=160M584UVgKoiF9VIa8R84Rn-T0agnSol",
            "https://drive.google.com/uc?export=view&id=1tNrjmsnFGNChpgWz1XMiRTLX_vERXvvI",
            "https://drive.google.com/uc?export=view&id=16LQ_JCws1wd9qg8At4r8_G_FfL95_qLb",
            "https://drive.google.com/uc?export=view&id=181As08N5v3dK7GP4EdycPJiMAroPLrFq",
            "https://drive.google.com/uc?export=view&id=1QliBymxCl8dqdMVS6WEEX1eyYFAt2X2O",
            "https://drive.google.com/uc?export=view&id=1OmoB5Ny19KtUGXTKnRegWZcd8jR3Gx2S",
            "https://drive.google.com/uc?export=view&id=1mZPLq-PC3uAN_43nJxC5wTRKne65qa9P",
            "https://drive.google.com/uc?export=view&id=1iwOcPKTNqMLipyBHMrHctSm5uEM6zqav",
            "https://drive.google.com/uc?export=view&id=1RvigC2eZCSi_ft_aAl3H1Db6dUi2SDLd",
            "https://drive.google.com/uc?export=view&id=1QN-TFPZw7GZm9c5ouEkbNPAnGAsRwqYw",
            "https://drive.google.com/uc?export=view&id=1yCE-J3QmD5PyeZF3kzDyKoiG8aEqIq-y",

        ]
        data_list = [
            {
                "nama": "Kevin Antonio Junior",
                "nim": "123450109",
                "umur": "20",
                "asal": "Maluku",
                "alamat": "Panjang",
                "hobbi": "Menari",
                "sosmed": "@kevinaj__",
                "kesan": "Bang Kevin ga nyangkan ternyata kadep minbak keren banget sih.",  
                "pesan": "Semangatkuliahnya bang, semoga ga ada mk yang ngulang lagi"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakak ini asik, dan aku terpesona sama kecantikkannya sihhh omggg",  
                "pesan": "Jangan sampe kena tipu lagi ya kak"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal": "Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abangnya lucu banget",  
                "pesan": "Semangat untuk menjelajah dunia dan terbang setinggi mungkin"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Kakak yang cantik dan baik hati suka banget love.",  
                "pesan": "Pancarkan cahaya yang dipunya kak!!"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Abang yang aku sering liat di damaskus ternyata anak minbak keren.",  
                "pesan": "Jangan pernah cape untuk jadi medis ya bang"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakaknya cute banget, suka deh ngeliatnya.",  
                "pesan": "Semangat buat kedepannya menjalani banyak rindangan di hidup ini."# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Abang asprak alpro aku yang keren banget dan baik hati.",  
                "pesan": "Semoga kedepannya hani bisa jadi asprak alpro kaya abang"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Kakak yang cute, cantik, dan sering cerita yang bisa aku ambil pelajran dari hidupnya.",  
                "pesan": "Jangan lelah buat menghadapi dunia ya kak"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Orangnya lucu banget",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "Palu tensor 24 yang keren dan keren banget ngeliat dia bangga sama tensornya",  
                "pesan": "Kapan badminton sama tensor 25 bang!!"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abangnya lucu banget ketika lagi cerita sering diledekin sama temennya ",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak yang keren banget, pasti narinya jugakeren sih",  
                "pesan": "semangat buat terus nari kak, ajarin aku buat lenturin tubuh alias nari"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Abangnya keren banget",  
                "pesan": "semangat terus kuliahnya kakak !!! semangat menjalankan tugas di minbak"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Uw5IyIYrfpIbNyxaKCYCqU98a_iQ5F8I",
            "https://drive.google.com/uc?export=view&id=1mylWhn9GSbeU7zD73Who3vQe_Rho4w8L",
            "https://drive.google.com/uc?export=view&id=1_ceWsXsTB5_BCIa_Xmxkzf7bsRPEZqVi",
            "https://drive.google.com/uc?export=view&id=1NuoNgp6bRY17k_WXyTUsZj0FbatGuhof",
            "https://drive.google.com/uc?export=view&id=1Q5viHnfgjEWNojKprcEd_xrflV1RRnt5",
            "https://drive.google.com/uc?export=view&id=1iEKrVwwVMsvwgqWjnfcmvSKH-q4KNlll",
            "https://drive.google.com/uc?export=view&id=1sR7Fh6QpSJNKQbe22m09Avl78GfprEy4",
            "https://drive.google.com/uc?export=view&id=1C_9LAPTpZTxz1wHT485djE7d_Gr0Vdn8",
            "https://drive.google.com/uc?export=view&id=13WQ4NCrJqxNg1k-1EaeELdQx5QTGq_lS",
            "https://drive.google.com/uc?export=view&id=1Qt_KU9NVao6C2v-hirCA_kOEY-GRgdkC",
            "https://drive.google.com/uc?export=view&id=1DSsbmyvuRdILHvrMzdsCs0A2XLqiMS5N",
            "https://drive.google.com/uc?export=view&id=1fT0y8mOWfzTZOceNVWjfq-6qCmQxTrfg",
            "https://drive.google.com/uc?export=view&id=1H6TDK0Fw7Htp3_F6vk6Jj9xL7_WaxwLZ",
            "https://drive.google.com/uc?export=view&id=1irHI27lpQ-CRCSAz5y4AgRlYAyKjoTi3",
            "https://drive.google.com/uc?export=view&id=1-hc7QqvYLD2bBaktmqJ5XYTuEDoHpT3D",
            "https://drive.google.com/uc?export=view&id=1sTQtwszdcy-LYAQlttqFqRAQu4FiKULl",

        ]
        data_list = [
            {
                "nama": "Haikal Fransiskus Simbolon",
                "nim": "123450123",
                "umur": "23",
                "asal": "Bengkulu",
                "alamat": "Belwis",
                "hobbi": "Merokok",
                "sosmed": "@haikalsbln_",
                "kesan": "Nama yang ada disetiap angkatan.",  
                "pesan": "Semangat buat menjadi kadepnya bang!!"# 1
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya cantik banget dan lucu",  
                "pesan": "semangat terus kuliahnya kakak !!!, kelulusaan sudaah didepan mata kak semangat!!!"# 1
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Orangnya cerita banget kaya energinya ga pernah habis",  
                "pesan": "Terus ceria ya kak dan aku suka dengerin cerita kakak"# 1
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": "Keren banget bang waktu main di damaskus.",  
                "pesan": "Semoga terus membara semangatnya"
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": "kakanya lucu dan cantik banget suka ngeliatnya.",  
                "pesan": "Semangat terus kak, jangan sering-sering stalker takutttt"# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "....",
                "asal": "....",
                "alamat": "....",
                "hobbi": "....",
                "sosmed": "@...",
                "kesan": "orangnya lucu banget apa lagi waktu dia manggil aku hey polkadot karna baju aku.",  
                "pesan": "tetep ceria ya kak"# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal": "kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": "Bang Jaya mirip banget sama temen aku dari ujung rambut sampe ujung kaki.",  
                "pesan": "jangan terlalu di city city kan ya banggggg"# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "kakaknya cantik dan cute.",  
                "pesan": "Semangat kuliahnya mengejar sampai ujung dunia"# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "nama abang mirip banget sama abang aku yang nyebelin",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": "...",
                "asal":"...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "suka banget ngeliat kakaknya waktu senyum",  
                "pesan": "HIDUP ANAK ACARAAAA KAKKK SEMANGAT TERUSSS !!!"# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": "nama kita sama bang cuman kurang huruf a aja",  
                "pesan": "semangat terus kuliahnya banggg !!!"# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": "...",
                "asal":"....",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakaknya cute ",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": "Kakak asik saya suka belajar dengan dia",  
                "pesan": "semangat terus kuliahnya kakak, walau anak rantau !!!"# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakak lucu dan cute bangettt",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": "Bang harvinsyah orangnya lucu banget dan unik",  
                "pesan": "semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": "...",
                "asal": "...",
                "alamat": "...",
                "hobbi": "...",
                "sosmed": "@...",
                "kesan": "Kakaknya sejuk banget ketika ngeliat mukanya masyallah",  
                "pesan": "semangat terus kuliahnya kakak !!!, terbang setinggi mungkin"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BT2ZKdb7iiP_w2zJtHC5ikdy5Wc6Rg5b",
            "https://drive.google.com/uc?export=view&id=1AZ5_QUJDvk6ZT4wWWA5RPdXS6UMSJHOd",
            "https://drive.google.com/uc?export=view&id=1e6EFAPDey5JILjdcfGBNgI8joirlvV1r",
            "https://drive.google.com/uc?export=view&id=1wIPWNQuOB1-MQYOTZzi29IsCe_YoYQ-7",
            "https://drive.google.com/uc?export=view&id=1wVfn81q09K7nQ-0GotGdVqL3kH6JKNKe",
            "https://drive.google.com/uc?export=view&id=1dcSlfvmcIzdhm7f5Tuf0PW2TAPgy5caW",
            "https://drive.google.com/uc?export=view&id=1BxA47QFbubRUeIRxVlUqtcU42Poz4zPR",
            "https://drive.google.com/uc?export=view&id=13aFQzJMW3TVznknHGnQBjuePuHoJuLWw",
            "https://drive.google.com/uc?export=view&id=1PbjGQ1DxDtuOK5x0Kr8Gz5fFzmgkhtaW",
            "https://drive.google.com/uc?export=view&id=1xB1-abMGc6dO_Uq19nO1OlbLWQwzi2zp",
            "https://drive.google.com/uc?export=view&id=18RBGXCqqIYgcOiNfXE4wfB2TFDV1AmMr",
            "https://drive.google.com/uc?export=view&id=1rl6Ttw8_qOw4wmj6uv5aGZ2-n13EvHLn",
            "https://drive.google.com/uc?export=view&id=1pPqg3-H_DY6KpNNMKOXG5GqvvfYjuMVK",
            "https://drive.google.com/uc?export=view&id=186K4K5fjSTGbESMZEsL1mnd3P7DbGQqB",
            "https://drive.google.com/uc?export=view&id=1C02Ot-V3dm_XliIZDnIDu6ilMYIKqEIt",
            "https://drive.google.com/uc?export=view&id=1nUzTVIT7m2RIruIzwbHpYkhcwyEst5t5",
            "https://drive.google.com/uc?export=view&id=1x2kee3SEzSarPAUng_UPlHqb3jCrjF5u",

        ]
        data_list = [
            {
                "nama": "Arienta Khusnul Ananda",
                "nim": "123450097",
                "umur": "21",
                "asal": "Pinggir Pantai",
                "alamat": "Samping Kost Capo",
                "hobbi": "Ngerjain Anak Kader",
                "sosmed": "@arientakhsnl_",
                "kesan": "Kak arienta ternyata baikkk, walau awalnya sedikit serem",  
                "pesan": "Makasih banyak ya kak, udah jadi salah satu orang dibalik CEO HMSD yang bikin aku berkembang."# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kak vany baikkk, tegas jugaaa apalagi waktu dilapangan",  
                "pesan": "Semangat terus ya kakaaaa semester ini, semoga lancar2 kuliahnya sampai lulus"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Bang nobel tegas tapi saya rasa bang nobel jadi kaya bapak dari datavora",  
                "pesan": "Makasih banyak atas pelajaran yang telah diberikan"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal": "Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Bang azmi orang yang tegas juga",  
                "pesan": "Terimakasih atas hal yang di berikan selama rangkaian"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal": "Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Bang ayake orang yang perhatian apalagi kalo ada yang sakit gercep banget",  
                "pesan": "Terimakasih atas perhatian yang diberikan"# 1
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Orangnya tegas banget",  
                "pesan": "Terimakasih telah membentuk mental saya semakin berani selagi tidak melakukan kesalahan"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal": "dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Keren banget apalagi waktu di lapangan, tegas dan jadi contoh buat berani dalam hal apapun",  
                "pesan": "terimakasih atass pelajaran yang di berikan"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Keren banget bang apalagi waktu day-4",  
                "pesan":"Terimakasih atas hal yang di berikan selama rangkaian, dan membuat saya berani untuk bicara di day-4"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                 "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "sosmed": "@...",
                "kesan": "orangnya baik, suka banget liat kak putri waktu senyum manis bangett",  
                "pesan": "Terimakasih atas banyak hal, semangat kuliah kakk"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@andra.lhm",
                "kesan": "kakaaa cantikbanget aku suka ngeliatnya",  
                "pesan": "......."# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Keren sihhh apalagi waktu cerita cerita di wawancara",  
                "pesan": "Tetap semangat untuk kuliahnya bang"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "kakanya cantik dan cute",  
                "pesan": "Semangat buat kuliahnya, sampai lulus"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "kakanya keren  dan cantik",  
                "pesan": "Tetap ceria dan semangat kuliah"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "keren banget bang",  
                "pesan":"semangat kuliahnya bang!!!"
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                 "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "kakanya cantik dan cute",  
                "pesan":"terus ceria dan semangat kuliahnya"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "abangnya lucu gemasdan baik hati",  
                "pesan":"semangat kuliahnya bang dan terbang setinggi mungkin"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                 "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "kakaknya cantik banget suka ngeliatnya",  
                "pesan":"semangat kuliahnya kak,dan terus senyum karna buat happy orang lain"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
# Tambahkan menu lainnya sesuai kebutuhan
