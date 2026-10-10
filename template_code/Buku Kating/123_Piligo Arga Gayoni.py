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
            "https://drive.google.com/uc?export=view&id=1SRiCdfXwUoJzCrsldYcO1QJjnmHPYlXQ",
            "https://drive.google.com/uc?export=view&id=13jrcV2VxF6zWwlJSGJImRwQPe-z4ic6r",
            "https://drive.google.com/uc?export=view&id=1Jscj0-7kkTq2-MUf4O_snVTThbjYXdY7",
            "https://drive.google.com/uc?export=view&id=1vTZxoCos2uGY4B3QGi88sUdJCO7bFUvQ",
            "https://drive.google.com/uc?export=view&id=1kyBWYXpT6GzanZh1siuiKw6G2t4p4eba",
            "https://drive.google.com/uc?export=view&id=1FiVB3HrrK4NjV_gGogLYU6YZtkOV0Dtq",
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
                "kesan": "Bang Fajar orangnya kelihatan asik banget sih, soalnya hobinya push immo, beliau juga orang yang bertanggung jawab.",  
                "pesan":"Semoga bang fajar cepat di wisuda dan sehat selalu"# 1
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Lucu banget abangnya, sifatnya itu yang suka bercanda gampang bikin suasana cair",  
                "pesan":"Semangat terus ya bang aqil"# 1
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakak ini soft spoken banget, nada suaranya enak didengar",  
                "pesan":"Semangat terus kakak, semoga cepat diwisudaa"# 1
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Bang Qois ini bagi saya orangnya pendiem, tapi selalu berkomitmen",  
                "pesan":"Sehat terus ya banggg"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Orangnya lucu dan imut, suka bercanda",  
                "pesan":"Jangan menyerah dan terus semangat ya kakkk"# 1
            },
            {
                "nama": "Luthfia Laila Ramadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "kakaknya baik dan enak diajak kalau ngobrol",  
                "pesan":"jaga terus kesehatannya ya kakk"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ebe1fVSVNTresFzcKDcfaJkUlB5m5Tga",
            "https://drive.google.com/uc?export=view&id=1bJC22-jrAp-A8NvjNxkQVM22QIcqMjEp",
            "https://drive.google.com/uc?export=view&id=1B9ciiPsIsSdiSxDDuYbPnXFIOuqKbBAJ",
            "https://drive.google.com/uc?export=view&id=1sNt_Uqaj80_jVSQrPIrbuH29Dqd4N-iK",
            "https://drive.google.com/uc?export=view&id=1n3GOhJK3mneaSJ2depgdT1vOGO_AnC26",
            "https://drive.google.com/uc?export=view&id=1zxBiNESHIr-JqH-yR_VwRtgjPEK12FwZ",
            "https://drive.google.com/uc?export=view&id=1kVupPbZ32unNHxpSgUQCKE5vtNKvK_7k",
            "https://drive.google.com/uc?export=view&id=1_T5ylXTa_L7vCYiUaKg5LJj9FI0fqqBR",
            "https://drive.google.com/uc?export=view&id=1yO909EJCcsnf_zUSzWjXcGy5xpFMEicM",
            "https://drive.google.com/uc?export=view&id=1_npit5aelARaYIpUbQxvU0Bzg9r-ko-c",
            "https://drive.google.com/uc?export=view&id=1G66mKSL-qHFg7Mx8HmTH4nvg18veNPmW",
            "https://drive.google.com/uc?export=view&id=1EM5KEmYYKjtOTUb3b5voAYU-AxcYZj0W",
            "https://drive.google.com/uc?export=view&id=1wYxhCeZadt9UcyfOYCzQFC1GLKoWgucY",
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
                "kesan": "Bang ridho berwibawa banget, auranya kuat banget.",  
                "pesan":"Semangat terus ya bang, semoga juga bisa cepat diwisuda"# 1
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakak ini lucu banget orangnya, suka bercanda, tapi bisa juga serius",  
                "pesan":"Semangat kuliahnya ya kak"# 1
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abang ini seru orangnya, suka ngobrol dan pintarr",  
                "pesan":"Jaga selalu kesehatannya ya bangg"# 1
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "Pertama kali saya melihat abang ini pas pplkk, dan kesannya si abangnya ini pendiam",  
                "pesan":"Kejar terus mimpinya bang, jangan kasih kendor"
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": "Mukanya itu terlihat serius banget, tapi aslinya asik dan bisa diajak bercanda",  
                "pesan":"Jangan sampai semangatnya turun ya kakk"# 1
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": "Bagi saya abang ini keren aja gitu",  
                "pesan":"Semoga selalu diberi kesehatan ya bang"# 1
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": "Kakaknya itu bagi saya tipikal orang ya bisa ngelucu dan serius disaat bersamaan",  
                "pesan":"Semoga mimpi kakak bisa tercapai ya"# 1
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": "Lucu kakaknya, kelihatannya juga suka ngobrol",  
                "pesan":"Semangat terus kak!"# 1
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": "Abang ini orangnya pintar dan jago berbicara",  
                "pesan":"Sehat terus ya bangg"# 1
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": "Kak monica ini lucu dan suka senyum",  
                "pesan":"Jangan kendor ya kak semangatnyaa"# 1
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": "Lucu banget  abang ini, suka ketawa dan ngejokes",  
                "pesan":"Semangat mengejar mimpinya bangg"# 1
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Awal pas ketemu kakak ini saya merasa kakak ini galak banget, ternyata malah sebaliknya",  
                "pesan":"semoga cepat wisuda dan dapat pekerjaan yang terbaik ya kakk"# 1
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": "kakak ini aktif banget, suka ngobrol dan ketawa",  
                "pesan":"semangat terus ya kak kuliahnyaa"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1utYP0n5FN6rTA_vxNyjAoBQQP2z_jvlH",
            "https://drive.google.com/uc?export=view&id=1qpiKnz0FQ-9BKXlPEKxqjvma6YuhIou_",
            "https://drive.google.com/uc?export=view&id=1RdwFELGZZVMMEYhzvvrL7g4m9DTD25Rk",
            "https://drive.google.com/uc?export=view&id=1kFCo_eo4BkoHD45hgv7ZLndC5wCugG9y",
            "https://drive.google.com/uc?export=view&id=1lta38E7ynCLizjqL-0IGzhpnXvcykZiR",
            "https://drive.google.com/uc?export=view&id=1znHuKNPq4RCS3lLP_jx9_3ZQt51UbQXW",
            "https://drive.google.com/uc?export=view&id=1N3Fitv6zT00NblYXCBRODUEQp7c90eWD",
            "https://drive.google.com/uc?export=view&id=1b-LnDZJOA7ASDsnYv_Pjp-eyU77xbyRj",
            "https://drive.google.com/uc?export=view&id=1h-3tyjWjQJr9esVsl7xzPHIJcA-E6WRB",
            "https://drive.google.com/uc?export=view&id=1oFfbghS29Z3oBT8c9oBRlf2q0p2u99Y1",
            "https://drive.google.com/uc?export=view&id=1YSaVrzYrI_VXZtVncTVJjSN8RGwJGXWa",
            "https://drive.google.com/uc?export=view&id=1jm-YNR0LSwJdj4FftQocVrXkPggjRB-L",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1qfftq9-XulUD6AXGPGOemSVlMSqTSWNg",
            "https://drive.google.com/uc?export=view&id=1dLeHorV5wdha37V7WwBwgLa2AOloF-yX",

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
                "kesan": "abangnya keren sih dan terlihat cocok banget untuk departemen ini",  
                "pesan":"semangat terus ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kakak ini lucu dan suka ketawa untuk bikin cair suasana",  
                "pesan":"semangat dan sehat terus ya kakakk"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "kalau dari sudut pandangku itu abangnya bukan tipe orang yang sering ngobrol, tapi seru",  
                "pesan":"semangat terus ya bangg"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "kakaknya lucu gitu tingkahnya, bikin ketawa",  
                "pesan":"Semoga kedepannya bisa keterima di tempat yang kakak sukai"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa itu orangnya cool gitu dari yang saya liat",  
                "pesan":"Semoga selalu diberi kesehatan ya banggg"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini seru orangnya dan kelihatan aktif banget",  
                "pesan":"Semangat kulahnya kak, semoga cepat luluss"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Aura ekstrovertnya kerasa banget dan asik juga abangnya",  
                "pesan":"Semoga aura ekstrovernya ga luntur ya bangg"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Bukan tipe yang banyak bicara, tapi nyaman kalau mengobrol",  
                "pesan":"Sehat sehat terus ya kakk"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Keren sih abangnya, dari yang saya lihat itu berwibawa gitu",  
                "pesan":"Semangat terus dan pantang menyerah ya bang"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "asik dan suka ngobrol dengan bang andra, karna pembawaannya itu enak",  
                "pesan":"semoga terus diberi kesehatan dan kekuatan untuk maju terus"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abang ini lucu banget, suka bikin saya ketawa",  
                "pesan":"apapun yang terjadi jangan patah semangat ya bang"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "keren sih abangnya dan cool gitu",  
                "pesan":"semangat terus bang kuliahnya"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak lucu dan enak diajak ngobrol",  
                "pesan":"semoga bisa tercapai ya cita citanya"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini lucu dan imut gitu",  
                "pesan":"sehat terus ya kak, agar bisa terus maju"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w12G5JVVOQe9y-uwOGw1ENLBq0S3Rahs",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1MEwwWbQdVZ8LuSYKzJVLthLFQK2hV6SD",
            "https://drive.google.com/uc?export=view&id=1SAaYOs7fMtrcE6HY_kovK-yPcW4qSoIY",
            "https://drive.google.com/uc?export=view&id=1BPJp9IzdMF5OmpXZBevvYBWyt9PnTqH9",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mUaxKB_-6crqS7k-rxiIc3kQBUFNj7xX",
            "https://drive.google.com/uc?export=view&id=1dpBZKB8fNsJMTfXntHmLhA7ibmDfbVr6",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=169VVEV6vKZvHYdBryk9yYMz_U84GBzNI",
            "https://drive.google.com/uc?export=view&id=1dPd2Kz49NNiq0G4OPJ0EtKbIG-VZIyaX",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1g25n6U7nhnodrG-MkqLs4HpwRJzC2iJZ",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1usOIXqXuvgwImLT71NvCULHHP0GRX8ge",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",

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
                "kesan": "abangnya keren sih dan terlihat cocok banget untuk departemen ini",  
                "pesan":"semangat terus ya bang"# 1
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "kakak ini lucu dan suka ketawa untuk bikin cair suasana",  
                "pesan":"semangat dan sehat terus ya kakakk"# 1
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "kalau dari sudut pandangku itu abangnya bukan tipe orang yang sering ngobrol, tapi seru",  
                "pesan":"semangat terus ya bangg"# 1
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": "kakaknya lucu gitu tingkahnya, bikin ketawa",  
                "pesan":"Semoga kedepannya bisa keterima di tempat yang kakak sukai"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": "Bang Dafa itu orangnya cool gitu dari yang saya liat",  
                "pesan":"Semoga selalu diberi kesehatan ya banggg"# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": "Kakak ini seru orangnya dan kelihatan aktif banget",  
                "pesan":"Semangat kulahnya kak, semoga cepat luluss"# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": "Aura ekstrovertnya kerasa banget dan asik juga abangnya",  
                "pesan":"Semoga aura ekstrovernya ga luntur ya bangg"# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": "Bukan tipe yang banyak bicara, tapi nyaman kalau mengobrol",  
                "pesan":"Sehat sehat terus ya kakk"# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": "Keren sih abangnya, dari yang saya lihat itu berwibawa gitu",  
                "pesan":"Semangat terus dan pantang menyerah ya bang"# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": "asik dan suka ngobrol dengan bang andra, karna pembawaannya itu enak",  
                "pesan":"semoga terus diberi kesehatan dan kekuatan untuk maju terus"# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "abang ini lucu banget, suka bikin saya ketawa",  
                "pesan":"apapun yang terjadi jangan patah semangat ya bang"# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": "keren sih abangnya dan cool gitu",  
                "pesan":"semangat terus bang kuliahnya"# 1
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": "Kakak lucu dan enak diajak ngobrol",  
                "pesan":"semoga bisa tercapai ya cita citanya"# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "....",
                "umur": "..",
                "asal":"...",
                "alamat": "....",
                "hobbi": "...",
                "sosmed": "@....",
                "kesan": "Kakak ini lucu dan imut gitu",  
                "pesan":"sehat terus ya kak, agar bisa terus maju"# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()
# Tambahkan menu lainnya sesuai kebutuhan
