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
    st.write("Semua gambar telah dimuat")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Jl3TRqARa03G7sfnjmMp5Ic2WUMTrmXI",
            "https://drive.google.com/uc?export=view&id=10JdGKbS-sy0Q-WODYIiq-RHdxOgIoQdA",
            "https://drive.google.com/uc?export=view&id=1Y9gqqft8Q-1O2XTpIn1SLSwKE0Ww6Cza",
            "https://drive.google.com/uc?export=view&id=1_DhgtFl73HGdnTt_cFRGie75GBwmfEGk",
            "https://drive.google.com/uc?export=view&id=1CAfB_4CI6SRxThyXOIgRXsY7J7GU9-8m",
            "https://drive.google.com/uc?export=view&id=1CAfB_4CI6SRxThyXOIgRXsY7J7GU9-8m"
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
                "kesan": "Abangnya sangat ramah, murah senyum, dan asyik diajak ngobrol",  
                "pesan": "Semoga urusan akademiknya dipermudah, selalu sehat, dan sukses terus ke depannya"
            },
            {
                "nama": "Muhammmad Aqil Ramadhan",
                "nim": "1233450066",
                "umur": "22",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Dzikie",
                "sosmed": "@muhammadaqil1111",
                "kesan": "Abang yang baik hati, humble, serta pembawaannya tenang",  
                "pesan": "Tetap semangat kuliahnya, jaga kesehatan, dan amanah dalam setiap tanggung jawab"
            },
            {
                "nama": "Efi Defiyati",
                "nim": "123450005",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Airan",
                "hobbi": "Membaca",
                "sosmed": "@eeffiidefi",
                "kesan": "Kakaknya sangat baik dan ramah kepada siapa saja",  
                "pesan": "Semangat terus kuliahnya kak, semoga selalu diberkahi kemudahan dan kesehatan"
            },
            {
                "nama": "Qois Olifio",
                "nim": "123450067",
                "umur": "22",
                "asal":"Batam",
                "alamat": "Kota Baru",
                "hobbi": "Mainin Surat",
                "sosmed": "@qoisolifio",
                "kesan": "Abangnya humble, seru, dan sangat welcome",  
                "pesan": "Semoga sukses studinya dan panjang umur sehat selalu"
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "nim": "123450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Berkuda",
                "sosmed": "@Hafsafazilaa",
                "kesan": "Kakaknya baik banget, ramah, dan sangat menyenangkan",  
                "pesan": "Semangat terus ya kak kuliahnya dan bahagia selalu"
            },
            {
                "nama": "Luthfia Laila RAmadhani",
                "nim": "123450004",
                "umur": "21",
                "asal":"Bengkulu",
                "alamat": "Airan",
                "hobbi": "Bermain ke kost Efi",
                "sosmed": "@luthfiaarmdhni",
                "kesan": "Kakaknya murah senyum, humble, dan sangat asyik",  
                "pesan": "Semoga segala urusan perkuliahan dan aktivitasnya dimudahkan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lC3FWUt7p7CmmMCoGMACpHHNmyEMA7aS",
            "https://drive.google.com/uc?export=view&id=1jb5VY8k-pautrECcBiPxqhMvqmcluejD",
            "https://drive.google.com/uc?export=view&id=1GDcRO5vZrQg4sHzOJtyjihQpvISlc8IG",
            "https://drive.google.com/uc?export=view&id=1MTBV8RdtqTv2LYvtFocW6KUsgn2kdt8A",
            "https://drive.google.com/uc?export=view&id=1Y3RXg2UjBiYK2UFfOez1TFzzFRFC4zpD",
            "https://drive.google.com/uc?export=view&id=1H6uBb8MdRtVgd64vTAxQp-20PGVI9BGg",
            "https://drive.google.com/uc?export=view&id=1mv6MwjD8B-JTZcs2XENOAL6FTF-0_dnO",
            "https://drive.google.com/uc?export=view&id=1XUDGdVLBdlzS4SY0s4prXPZQlhLoaGYw",
            "https://drive.google.com/uc?export=view&id=1TfUx-1y0I5Apqs3U95EdHQbNIBMIDAft",
            "https://drive.google.com/uc?export=view&id=1c5BCtvvKOYLRNdkyNtRoH7ZEFV_ogV4L",
            "https://drive.google.com/uc?export=view&id=1h1GYlKkaRGsgxGLLDFV8w8AkO2Ya4UVY",
            "https://drive.google.com/uc?export=view&id=13SOqbRPnPykp29OWhxT687aPq-DdctGb",
            "https://drive.google.com/uc?export=view&id=1mTlzLtUFrCNyj9Y9fo5TBTOacV74TCcy"

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
                "kesan": "Abangnya asyik, ramah, lucu dan random",  
                "pesan": "Semoga sukses kuliahnya dan tetap semangat menjalani hari"
            },
            {
                "nama": "Juesi Apridelia Saragih",
                "nim": "123450085",
                "umur": "19",
                "asal": "Singkawang",
                "alamat": "Pelangi",
                "hobbi": "ngerepeat lagu lover dari taylor swiff",
                "sosmed": "@j__eesie",
                "kesan": "Kakaknya baik, humble, dan sangat ramah.",  
                "pesan": "Semoga kuliahnya lancar jaya, sehat selalu, dan tercapai semua impiannya."
            },
            {
                "nama": "Dharu Cahyoaji Sasongko",
                "nim": "123450023",
                "umur": "19",
                "asal":"Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Suka nonton AGZ",
                "sosmed": "@ddharu_",
                "kesan": "Abangnya baik, murah senyum, dan santai",  
                "pesan": "Semangat terus kuliahnya bang dan sehat selalu"
            },
            {
                "nama": "GH. Mikael Niko Antoni Setiadi",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Siti Sarifah Sumamahsa",
                "nim": "124450015",
                "umur": "18",
                "asal":"Palembang",
                "alamat": "Kedaton",
                "hobbi": "Bikin Pempek",
                "sosmed": "@syt.sarifa",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Givaro Ananta",
                "nim": "123450078",
                "umur": "20",
                "asal":"Gunung Pesagi",
                "alamat": "Sukabumi",
                "hobbi": "Minum Kopi",
                "sosmed": "@givarooo",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Afghanis Nursholehatunnisa",
                "nim": "124450042",
                "umur": "20",
                "asal":"Krui",
                "alamat": "Jatimulyo",
                "hobbi": "Memancing",
                "sosmed": "@afghanisnt_",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Hani Qurrota Aini",
                "nim": "124450020",
                "umur": "19",
                "asal":"City Eart",
                "alamat": "Sukarame",
                "hobbi": "Baca Au",
                "sosmed": "@haniquratuain_",
                "kesan": " ",  
                "pesan":""#
            },
            {
                "nama": "Jeremia Halim",
                "nim": "124450101",
                "umur": "20",
                "asal":"Beijing",
                "alamat": "Teluk",
                "hobbi": "Olahraga",
                "sosmed": "@jeremia_hm",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Monica Patricia Tanjung",
                "nim": "123450073",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Kota Baru",
                "hobbi": "Tidur",
                "sosmed": "@monica_tjg",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Jona Timothy Ogatse Panjaitan",
                "nim": "123450121",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Pemda Raya",
                "hobbi": "Ngegym dan Koleksi Figure",
                "sosmed": "@nagatseee",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Sekar Dini Widya Putri",
                "nim": "124450082",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Pemda",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": " ",  
                "pesan": ""
            },
            {
                "nama": "Wan Nashwa Alhasni Yuska",
                "nim": "123450077",
                "umur": "20",
                "asal":"Pasay",
                "alamat": "Belwis",
                "hobbi": "Nyapa",
                "sosmed": "@nshaysk",
                "kesan": " ",  
                "pesan":""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Departemen Minbak":
    def DepartemenMinbak():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Vm3Nd6Tinyp6efLMmi9YsJ2NIajq8qyw",
            "https://drive.google.com/uc?export=view&id=1IvqFmpJKcLawOJNgZyj6w207YqopfcGI",
            "https://drive.google.com/uc?export=view&id=1fZAnwPHYQyH-claqtow-yvEE9lFJPqnN",
            "https://drive.google.com/uc?export=view&id=1Onr5OF0X_xVIsfiCnrke9oFHbuoAFmuo",
            "https://drive.google.com/uc?export=view&id=1M2CS-Hk_gxBi9EUI2NJL7hx54NJdPr8Q",
            "https://drive.google.com/uc?export=view&id=1Da46NCZ-oXjk4Vhhg20cX0vhfEHFHlCk",
            "https://drive.google.com/uc?export=view&id=1EFFBwUCDN1SCPzyy12LOXa6vbnRXf39Q",
            "https://drive.google.com/uc?export=view&id=1uac_LVx74QJp95Y2C4aH49U1CKd3CarK",
            "https://drive.google.com/uc?export=view&id=1LDjzg_DMC365CujWm0Hlc2_GsMi8_Xqi",
            "https://drive.google.com/uc?export=view&id=1RQ7LGKcKK4AxUWLN4vv9Iqf1vy909IJU",
            "https://drive.google.com/uc?export=view&id=1h3jNg8SzuYNlTC_TouOqGQTmT3ojO20M",
            "https://drive.google.com/uc?export=view&id=1zvaz2s0MyQ9nt-ljAU911qKW5Cuh02IY",
            "https://drive.google.com/uc?export=view&id=18Lg4dGWduYlDt1u2akl-tAEQzbJe-DN8",
            "https://drive.google.com/uc?export=view&id=10l0Je27RNMoLUijI4pWp21Qt0ufno2X4",
            "https://drive.google.com/uc?export=view&id=1GmBpG1o-HtgIHhk5OxyRfdDa7M02Ihc9"

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
                "kesan": "Abangnya baik, humble, dan sangat ramah",  
                "pesan": "Semoga kuliahnya lancar, sehat selalu, dan sukses dalam setiap kegiatan"
            },
            {
                "nama": "Gusti Putu Ferazka Dhiyamika",
                "nim": "123450046",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Way Halim",
                "hobbi": "Mendaki",
                "sosmed": "@ferazkaa",
                "kesan": "Kakaknya ramah, murah senyum, dan seru",  
                "pesan": "Tetap semangat kuliahnya kak dan sehat terus"
            },
            {
                "nama": "Ali Aristo Muthahhari Parisi",
                "nim": "123450088",
                "umur": "21",
                "asal":"Lampung Timur",
                "alamat": "Gang Sakum Belwis",
                "hobbi": "Bawa makanan dari Luar",
                "sosmed": "ali_parisi3",
                "kesan": "Abangnya baik hati, humble, dan sangat asyik",  
                "pesan": "Semoga urusan akademiknya dimudahkan, sukses terus, dan sehat selalu"
            },
            {
                "nama": "Ayu Andriani Parlina Wati",
                "nim": "123450025",
                "umur": "20",
                "asal":"Jombang",
                "alamat": "Jatiagung",
                "hobbi": "Jalan-jalan nyari mangsa",
                "sosmed": "@me._kael",
                "kesan": " ",  
                "pesan":"Semoga kedepannya fadyl"
            },
            {
                "nama": "Dafa Elpriza",
                "nim": "124450131",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Way Kandis",
                "hobbi": "Mancing",
                "sosmed": "@dafaelpriza_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Salsabila Nazwa Putri",
                "nim": "124450002",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@slbnzw_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Muhammad Afdal Lutfi",
                "nim": "124450047",
                "umur": "19",
                "asal":"Lampung Tengah",
                "alamat": "Jln. Pulau Damar",
                "hobbi": "Surving",
                "sosmed": "@afdall.03",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Juwita Sari",
                "nim": "124450066",
                "umur": "19",
                "asal":"Lampung Barat",
                "alamat": "Pemda",
                "hobbi": "Liat Bila nulis",
                "sosmed": "@ju.juwitaaa_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Muhammad Ridwan",
                "nim": "123450091",
                "umur": "21",
                "asal":"Lampung Tengah",
                "alamat": "Belwis",
                "hobbi": "Nontonin Fadyl Badminton",
                "sosmed": "@mridwaan_22",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Andra Ilham Bintang",
                "nim": "124450060",
                "umur": "18",
                "asal":"Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi": "Nonton Drama Korea",
                "sosmed": "@andra.lhm",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Bryan Paskah Telaumbanua",
                "nim": "124450003",
                "umur": "20",
                "asal":"Nias",
                "alamat": "Belwis",
                "hobbi": "Yoga",
                "sosmed": "@bryantel_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Ghiyats Thabularasa Meardhy",
                "nim": "124450067",
                "umur": "17 tahun",
                "asal":"Jati Asih",
                "alamat": "Korpri",
                "hobbi": "Nyawit",
                "sosmed": "@meardhy_ghiyats",
                "kesan": " ",  
                "pesan":"" 
            },
            {
                "nama": "Indah Julia Mawar Pratiwi",
                "nim": "124450055",
                "umur": "20",
                "asal":"Pringsewu",
                "alamat": "Airan",
                "hobbi": "Main",
                "sosmed": "@sekardnwp",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Jacinda Kesya Alvara",
                "nim": "..",
                "umur": "",
                "asal":".",
                "alamat": "..",
                "hobbi": ".",
                "sosmed": "@..",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Muhammad Rafka Fatih Al Ghathfaan",
                "nim": "124450089",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Kota Baru",
                "hobbi": "Bangun Pagi",
                "sosmed": "@muhammdrafka_",
                "kesan": " ",  
                "pesan":" "# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenMinbak()

elif menu == "Departemen Internal":
    def DepartemenInternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13TYX3n6gfgWEVAhYtfR_RSXChAIV6GMG",
            "https://drive.google.com/uc?export=view&id=1jj19Xu38t4CImU0ORsXxpErmZyBZggoT",
            "https://drive.google.com/uc?export=view&id=1CeEy4gNHQyGV2FBtwvLhq-gECG5u0lGB",
            "https://drive.google.com/uc?export=view&id=1xJXrFYxahSb5WTxFOe_74ej_MaCcZ3Bb",
            "https://drive.google.com/uc?export=view&id=1yMNvCADGXoOLseH3jmOEsc0pai54PxCI",
            "https://drive.google.com/uc?export=view&id=1Ijlra46Fc0Ur-uz3TusMaWVz4rcWyn_a",
            "https://drive.google.com/uc?export=view&id=1Jx_9RdD5oK7dx-234jhBw3TybpT0Kqet",
            "https://drive.google.com/uc?export=view&id=1U0JT9IQ8JeY3rpQgEdKqsi94FPJu8gs1",
            "https://drive.google.com/uc?export=view&id=1vuB0sHxCnJgbz4AJjFXOR9rD2lcxCt0W",
            "https://drive.google.com/uc?export=view&id=1oLFAPBP89lhgwOgM6pvzb208w3ngNoE8",
            "https://drive.google.com/uc?export=view&id=1zeI4yFV9XiAeoygRvQQJP7x_fhnYqzbP",
            "https://drive.google.com/uc?export=view&id=1Jj51ZVmL-Jt4MaQrheqqYfzzRGHAUcq8",
            "https://drive.google.com/uc?export=view&id=1mEfGOdFMsnC-sGLA-9Gk-a6YLemdHmy0",
            "https://drive.google.com/uc?export=view&id=1DzIevEoLp5uvNNlbfbHMUYUwMVIE06gR",
            "https://drive.google.com/uc?export=view&id=16j0vqEwdaiHAUmKOfQSjiR-pI2D4TSJZ",
            "https://drive.google.com/uc?export=view&id=1aYAv0j_8_Pkqep6PDKx1cYbItnYl1rl3"

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
                "kesan": "Abangnya ramah, baik, dan asyik",  
                "pesan": "Semoga sukses akademiknya, sehat selalu, dan amanah dalam tugas."
            },
            {
                "nama": "Kharisma Mustika Sari",
                "nim": "123450034",
                "umur": "21",
                "asal": "Way Kanan",
                "alamat": "untung suropat",
                "hobbi": "Suka menolong orang",
                "sosmed": "@rismaa.mustika_",
                "kesan": "Kakaknya baik hati, suka menolong, dan sangat ramah",  
                "pesan": "Semoga kuliahnya lancar terus, sukses, dan selalu bahagia ya kak"
            },
            {
                "nama": "Hanna Grecia Sinaga",
                "nim": "123450038",
                "umur": "21",
                "asal":"Kisaran",
                "alamat": "Sukarame",
                "hobbi": "menyapa satpam gedung f",
                "sosmed": "@hanna_g_sinaga",
                "kesan": "Kakaknya ramah, murah senyum, dan ceria",  
                "pesan": "Semoga dimudahkan dalam setiap urusan kuliah dan sehat selalu."
            },
            {
                "nama": "Farhan Ghani",
                "nim": "123450121",
                "umur": "19",
                "asal":"Kemiling",
                "alamat": "Kemiling",
                "hobbi": "Suka motor bukan ngabers",
                "sosmed": "@farhanghani",
                "kesan": " ",  
                "pesan":""
            },
            {
                "nama": "Aisyah Khairun Nissa",
                "nim": "124450096",
                "umur": "18",
                "asal":"Riau",
                "alamat": "Belwis",
                "hobbi": "Ngestalker in orang",
                "sosmed": "@aisyahkhair",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Cerine Sihotang",
                "nim": "124450049",
                "umur": "..",
                "asal":"..",
                "alamat": "..",
                "hobbi": "..",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Jaya Saputra Tambak",
                "nim": "124450094",
                "umur": "22",
                "asal":"kisaran city",
                "alamat": "Pemda city",
                "hobbi": "Balap liar",
                "sosmed": "@jay_saputra_tmb",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Najla Nursyifa",
                "nim": "124450051",
                "umur": ".",
                "asal":".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Rozak Ramdani",
                "nim": "124450100",
                "umur": ".",
                "asal":".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Teresa Christiani Purba",
                "nim": "124450046",
                "umur": ".",
                "asal":".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "nim": "123450064",
                "umur": "21",
                "asal":"Padang",
                "alamat": "Perumnas Way Kandis",
                "hobbi": "Main game fps",
                "sosmed": "@hndfzky_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Audina Fitria",
                "nim": "124450038",
                "umur": ".",
                "asal":"..",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Cika Adelia Br Marbun",
                "nim": "124450050",
                "umur": "20",
                "asal": "Riau",
                "alamat": "Belwis",
                "hobbi": "Dengerin Musik",
                "sosmed": "@Cikamrbn",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Gustin H. Tampubolon",
                "nim": "124450068",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Muhammad Harvinsyah",
                "nim": "124450128",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Belwis",
                "hobbi": "Berkuda",
                "sosmed": "@Muhvnz_",
                "kesan": " ",  
                "pesan":" "# 1
            },
            {
                "nama": "Rafa Sabina Fahimah",
                "nim": "124450036",
                "umur": ".",
                "asal": ".",
                "alamat": ".",
                "hobbi": ".",
                "sosmed": "@.",
                "kesan": " ",  
                "pesan":" "# 1
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenInternal()

elif menu == "Departemen PSDA":
    def DepartemenPSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EtM17goe2HHL04LkI8XrKiy9H-Wobfl-",
            "https://drive.google.com/uc?export=view&id=1g8lpc7bRe4vLHvZNXYn6dlNhKuqWO-Wk",
            "https://drive.google.com/uc?export=view&id=1wPXz8WeN-NMdhXSPQHmdvwyRPoQbEeJE",
            "https://drive.google.com/uc?export=view&id=1f1rX29ld7E66FD7-CBDswAT7-6erwCNd",
            "https://drive.google.com/uc?export=view&id=1f8P1QX-TwPcAojsV8W3breCtMYCyZ1KB",
            "https://drive.google.com/uc?export=view&id=1KbECDCCiFmBhiILtgy00dnEaLnBGL2bL",
            "https://drive.google.com/uc?export=view&id=1a6KlieOPJLYTLMvOXQzZaay0cML9SSaB",
            "https://drive.google.com/uc?export=view&id=14AMEQ2ReqiSrlJTkxjfPJEFYGyUPktox",
            "https://drive.google.com/uc?export=view&id=1f1rX29ld7E66FD7-CBDswAT7-6erwCNd",
            "https://drive.google.com/uc?export=view&id=1rJ2X70qAKI3Dkibf477sjzKLvqCUXsac",
            "https://drive.google.com/uc?export=view&id=1f1rX29ld7E66FD7-CBDswAT7-6erwCNd",
            "https://drive.google.com/uc?export=view&id=1zj7FqC3-50fQzl5H-8_UVliIp5SJe9eY",
            "https://drive.google.com/uc?export=view&id=1yfF5VhdWtKiN_7y7Id7_LI65ZHIbV7GS",
            "https://drive.google.com/uc?export=view&id=1lbVIMOa-9da5ivrs0dnosRNPJYwNLYHb",
            "https://drive.google.com/uc?export=view&id=1oP01q7RKATO5p40R85bJYy1Ry373-SdS",
            "https://drive.google.com/uc?export=view&id=1o70JXDiPgFQrsxaJEn7Nyt9QZ5afx1t6",
            "https://drive.google.com/uc?export=view&id=1pRxV_pBKOXJsmX5A3WHhU1Q-0fgD7DRr"
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
                "kesan": "Kakaknya baik, ramah, dan murah senyum",  
                "pesan":"Semoga kuliahnya lancar jaya, sehat selalu, dan sukses terus"# 1
            },
            {
                "nama": "Vany Salsabila Putri",
                "nim": "123450022",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Pudan Kost",
                "hobbi": "Pacaran",
                "sosmed": "@vany.salsabilaa",
                "kesan": "Kakaknya ramah, humble, dan sangat baik",  
                "pesan": "Semoga urusan akademiknya lancar dan sehat selalu ya kak"# 1
            },
            {
                "nama": "Nobel Nizam Fathirizki",
                "nim": "123450023",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Banyak",
                "sosmed": "@nobelnizam",
                "kesan": "Abangnya asik, baik, dan jago sulap",  
                "pesan":"Semoga sukses terus, tetap semangat, dan amanah dalam menjalankan tugas"# 1
            },
            {
                "nama": "Afriza Azmi",
                "nim": "124450110",
                "umur": "20",
                "asal":"Malang",
                "alamat": "Lapangan",
                "hobbi": "Berantem",
                "sosmed": "@friezazmi",
                "kesan": "Abangnya seru, humble, dan ramah",  
                "pesan": "Semoga kuliahnya lancar terus bang, sehat selalu dan sukses ke depannya"
            },
            {
                "nama": "Ayake Alfatih Ramadan",
                "nim": "124450059",
                "umur": "21",
                "asal":"Peninjauan X kota diatas solok, Sumatera Barat",
                "alamat": "Blok D.79, Jln. Manggis 8 Pemda, Way huwi Jati Agung, Lampung Selatan, Lampung",
                "hobbi": "Cekek Ayam",
                "sosmed": "@ykeall",
                "kesan": "Abangnya ramah, baik, lucu, dan unik",  
                "pesan":"Semoga sukses selalu kuliahnya, makin semangat serta rajin dan sehat walafiat"
            },
            {
                "nama": "Caesar Ozora Alrando",
                "nim": "124450017",
                "umur": "20",
                "asal":"Metro",
                "alamat": "Korpri",
                "hobbi": "Pulang Kampung",
                "sosmed": "@caesar.oriza",
                "kesan": "Abangnya baik, ramah, dan humble",  
                "pesan":"Semoga urusannya dipermudah, selalu amanah, dan sukses"# 1
            },
            {
                "nama": "Euodia Meiliana Fredita",
                "nim": "124450029",
                "umur": "18",
                "asal":"dari mana aja boleh",
                "alamat": "Didalam Kamar dibalik pintu",
                "hobbi": "Surving",
                "sosmed": "@yudiameilianaa_",
                "kesan": "Kakaknya ramah, humble, dan asyik",  
                "pesan":"Semoga kuliahnya lancar, semangat terus, dan sehat selalu ya kak"# 1
            },
            {
                "nama": "Haikal Seventino Tamba",
                "nim": "124450032",
                "umur": "Tinggi Bang Azmi - 155",
                "asal":"Jambi",
                "alamat": "Belakang Pemancingan",
                "hobbi": "Tidur",
                "sosmed": "@_haikaaall",
                "kesan": "Abangnya baik hati, ramah, dan santai",  
                "pesan":"Semoga sukses kuliahnya bang, tetap semangat dan jaga kesehatan"# 1
            },
            {
                "nama": "Putri Manna Anantama Simbolon",
                "nim": "124450056",
                "umur": "18",
                "asal": "Depok",
                "alamat": "oiya cafe",
                "hobbi": "jalan kaki ga boleh naik gojek",
                "sosmed": "@putrimannaa",
                "kesan": "Kakaknya sangat ramah, baik, dan murah senyum",  
                "pesan":"Semoga sukses selalu studinya, lancar sampai akhir, dan bahagia"# 1
            },
            {
                "nama": "Queenta Thifaal Nabila",
                "nim": "124450059",
                "umur": "19",
                "asal": "Rumah sakit",
                "alamat": "Depan pemancingan",
                "hobbi": "Makanin anak ayam",
                "sosmed": "@queentanaabila",
                "kesan": "Kakaknya ramah, humble, dan seru",  
                "pesan":"Semoga kuliahnya lancar jaya, semangat terus, dan sehat selalu"# 1
            },
            {
                "nama": "Desman Velius Halawa",
                "nim": "123450114",
                "umur": "25",
                "asal": "Nias",
                "alamat": "Airan",
                "hobbi": "Main musik",
                "sosmed": "@dsmanhal",
                "kesan": "Abangnya baik, ramah, serta murah senyum",  
                "pesan":"Semoga urusan akademiknya dimudahkan, sukses dan sehat selalu"# 1
            },
            {
                "nama": "Azzelya Thianandry",
                "nim": "124450041",
                "umur": "19",
                "asal": "Bandar Lampung ",
                "alamat": "Sukarame ",
                "hobbi": "Pilates ",
                "sosmed": "@azzelytn",
                "kesan": "Kakaknya baik, ramah, dan punya pembawaan yang menyenangkan",  
                "pesan":"Semoga kuliahnya sukses, tercapai tujuannya, dan sehat selalu ya kak"# 1
            },
            {
                "nama": "Charrlindah",
                "nim": "124450041",
                "umur": "21",
                "asal": "Jakarta Pusat ",
                "alamat": "Cendrawasih 1",
                "hobbi": "Ngurus Peternakan ",
                "sosmed": "@charrlln",
                "kesan": "Kakaknya ramah, humble, dan baik banget",  
                "pesan":"emoga sukses selalu studinya, tetap semangat dan bahagia"# 1
            },
            {
                "nama": "Jeremi Marolop P. Situmorang",
                "nim": "124450111",
                "umur": "17",
                "asal":"Jayapura",
                "alamat": "RS Airan",
                "hobbi": "Nonton a day in my life",
                "sosmed": "@jemarrro",
                "kesan": "Abangnya baik, ramah, dan asyik diajak ngobrol",  
                "pesan":"Abangnya baik, ramah, dan asyik diajak ngobrol"# 1
            },
            {
                "nama": "Nabila Nur Azizah",
                "nim": "124450048",
                "umur": "18",
                "asal":"Lampung",
                "alamat": "Barokah",
                "hobbi": "Main roblox",
                "sosmed": "@n.bila_a",
                "kesan": "Kakak NIM saya yang ramah, murah senyum, dan baik hati",  
                "pesan":"Semoga urusan perkuliahan dimudahkan, semangat terus dan sehat selalu"
            },
            {
                "nama": "Rafli Al Mansyah Tambunan",
                "nim": "124450007",
                "umur": "18",
                "asal":"Sibolga",
                "alamat": "Belwis",
                "hobbi": "Membaca peraturan rektor",
                "sosmed": "@dearfkvmfl",
                "kesan": "Abangnya baik, humble, serta rama",  
                "pesan":"Semoga sukses studinya, selalu amanah, dan diberkahi kesehatan"
            },
            {
                "nama": "Salavi Naharani",
                "nim": "124450090",
                "umur": "20",
                "asal":"Lampung Timur ",
                "alamat": "Jatimulyo ",
                "hobbi": "Minum air putih ",
                "sosmed": "@afi.nhr",
                "kesan": "Kakaknya baik, ramah, dan sangat menyenangkan",  
                "pesan":"Semoga kuliahnya lancar sampai lulus, sukses selalu dan bahagia"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    DepartemenPSDA()
# Tambahkan menu lainnya sesuai kebutuhan
